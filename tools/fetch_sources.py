"""Find each person's entry in the Dictionary of Welsh Biography, each place's record in Coflein, and the Welsh Wikipedia
article for both, using Wikipedia (to follow redirects to each article's Wikidata item) and Wikidata (which links the item to all of them).

Writes src/source_links.json:
    {"person:<id>": {"dwb": "<url>", "cy": "<Welsh Wikipedia title>"}, "place:<id>": {"coflein": "<url>", "cy": "..."}}
build.py adds the links to the person and place pages. Anything Wikidata does not know is simply left out.

Wikidata is blocked from Claude's cloud computer, so this runs on GitHub: .github/workflows/fetch-sources.yml (start it
from the Actions tab; it also runs by itself when this file changes on a claude/ branch, and on the 1st of each month).
"""
import json, os, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
OUT = os.path.join(ROOT, "src", "source_links.json")
API = "https://www.wikidata.org/w/api.php"
WP = "https://en.wikipedia.org/w/api.php"
UA = "HistoryOfWalesSiteBuilder/1.0 (https://historyofwales.cymru; static site build)"
# The Wikidata properties we want, found by name so a renumbering cannot break this.
WANT = {"dwb": "Dictionary of Welsh Biography ID", "coflein": "Coflein ID"}


def api(_base=API, **params):
    params.update(format="json", formatversion="2")
    url = _base + "?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except Exception as ex:  # noqa: BLE001
            print("  retry:", ex)
            time.sleep(2 ** attempt)
    raise SystemExit("Wikidata did not answer")


def prop(label):
    """The property id for a label, and its formatter URL (what turns an id into a link)."""
    r = api(action="wbsearchentities", search=label, type="property", language="en", limit=5)
    hit = next((x for x in r.get("search", []) if x.get("label", "").lower() == label.lower()), None)
    if not hit:
        print(f"No Wikidata property called {label!r}")
        return None, None
    e = api(action="wbgetentities", ids=hit["id"], props="claims")["entities"][hit["id"]]
    fmts = [c["mainsnak"]["datavalue"]["value"] for c in e.get("claims", {}).get("P1630", []) if c["mainsnak"].get("datavalue")]
    fmt = next((f for f in fmts if "https" in f), fmts[0] if fmts else None)
    print(f"{label}: {hit['id']} -> {fmt}")
    return hit["id"], fmt


def main():
    import data as D
    pages = {}
    for p in D.PEOPLE:
        if p[9]:
            pages.setdefault(urllib.parse.unquote(p[9]).replace("_", " "), []).append("person:" + p[0])
    for pl in D.PLACES:
        if pl.get("src"):
            pages.setdefault(urllib.parse.unquote(pl["src"]).replace("_", " "), []).append("place:" + pl["id"])
    props = {k: prop(v) for k, v in WANT.items()}
    # 1. English Wikipedia turns each title (after following redirects) into its Wikidata item.
    qid_keys, titles = {}, sorted(pages)
    for i in range(0, len(titles), 50):
        batch = titles[i:i + 50]
        r = api(WP, action="query", titles="|".join(batch), redirects="1", prop="pageprops", ppprop="wikibase_item")
        q = r.get("query", {})
        step = {}
        for n in q.get("normalized", []):
            step[n["from"]] = n["to"]
        for n in q.get("redirects", []):
            step[n["from"]] = n["to"]
        final = {}
        for t in batch:
            u, seen = t, set()
            while u in step and u not in seen:
                seen.add(u)
                u = step[u]
            final[t] = u
        item = {pg["title"]: pg.get("pageprops", {}).get("wikibase_item") for pg in q.get("pages", [])}
        for t in batch:
            qid = item.get(final[t])
            if qid:
                qid_keys.setdefault(qid, []).extend(pages[t])
            else:
                print("  no Wikidata item for", t)
        time.sleep(0.3)
    # 2. Wikidata gives the Dictionary of Welsh Biography id, the Coflein id and the Welsh Wikipedia article.
    out, qids = {}, sorted(qid_keys)
    for i in range(0, len(qids), 50):
        r = api(action="wbgetentities", ids="|".join(qids[i:i + 50]), props="claims|sitelinks", sitefilter="cywiki")
        for qid, ent in r.get("entities", {}).items():
            keys = qid_keys.get(qid, [])
            rec = {}
            cy = ent.get("sitelinks", {}).get("cywiki", {}).get("title")
            if cy:
                rec["cy"] = cy
            for k, (pid, fmt) in props.items():
                if not pid or not fmt:
                    continue
                vals = [c["mainsnak"]["datavalue"]["value"] for c in ent.get("claims", {}).get(pid, []) if c["mainsnak"].get("datavalue")]
                if vals:
                    rec[k] = fmt.replace("$1", urllib.parse.quote(str(vals[0]), safe="-_.~/"))
            for key in keys:
                kind = key.split(":")[0]
                keep = {a: b for a, b in rec.items() if a == "cy" or (kind == "person" and a == "dwb") or (kind == "place" and a == "coflein")}
                if keep:
                    out[key] = keep
        time.sleep(0.5)
    out = dict(sorted(out.items()))
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")
    n = lambda k: sum(1 for v in out.values() if k in v)  # noqa: E731
    print(f"Wrote {OUT}: {n('dwb')} Dictionary of Welsh Biography links, {n('coflein')} Coflein links, {n('cy')} Welsh Wikipedia links")


if __name__ == "__main__":
    main()
