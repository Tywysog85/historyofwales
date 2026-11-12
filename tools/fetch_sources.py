"""Find better sources than Wikipedia for every person, place and event: the Dictionary of Welsh Biography, the Oxford
Dictionary of National Biography, Britannica, the History of Parliament and UK Parliament, Art UK, Olympedia, World Athletics,
Coflein and Cadw, plus the Welsh Wikipedia article. English Wikipedia leads to each article's Wikidata item, and Wikidata
links the item to all of them.

Writes src/source_links.json:
    {"person:<id>": {"dwb": "<url>", "odnb": "<url>", ..., "cy": "<Welsh Wikipedia title>"}, "place:<id>": {...}, "event:<slug>": {...}}
Every link is opened before it is kept, so a link that does not open is left out. build.py shows them on the person, place
and event pages and on the cards (SOURCES in build.py sets the order and the names). Anything Wikidata does not know is left out.

Wikidata is blocked from Claude's cloud computer, so this runs on GitHub: .github/workflows/fetch-sources.yml (start it
from the Actions tab; it also runs by itself when this file changes on a claude/ branch, and on the 1st of each month).
"""
import json, os, sys, time, urllib.error, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
OUT = os.path.join(ROOT, "src", "source_links.json")
API = "https://www.wikidata.org/w/api.php"
WP = "https://en.wikipedia.org/w/api.php"
UA = "HistoryOfWalesSiteBuilder/1.0 (https://historyofwales.cymru; static site build)"
# The Wikidata properties we want: (property id, its English label). The id is checked against the label, and if they
# don't match the property is found by its label, so a renumbering cannot break this.
WANT = {
    "dwb": ("P1648", "Dictionary of Welsh Biography ID"),
    "odnb": ("P1415", "Oxford Dictionary of National Biography ID"),
    "britannica": ("P1417", "Encyclopædia Britannica Online ID"),
    "histparl": ("P1614", "History of Parliament ID"),
    "ukparl": ("P6213", "UK Parliament identifier"),
    "artuk": ("P1367", "Art UK artist ID"),
    "olympedia": ("P8286", "Olympedia people ID"),
    "athletics": ("P1146", "World Athletics athlete ID"),
    "coflein": (None, "Coflein ID"),
    "cadwb": ("P1459", "Cadw Building ID"),
    "cadwm": ("P3007", "Cadw Monument ID"),
}
# Which sources belong on which kind of page.
KINDS = {
    "person": {"dwb", "odnb", "britannica", "histparl", "ukparl", "artuk", "olympedia", "athletics"},
    "place": {"coflein", "cadwb", "cadwm", "britannica"},
    "event": {"coflein", "cadwm", "britannica"},
}


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


def _norm(t):
    return t.lower().replace("æ", "ae").replace("–", "-")


def prop(guess, label):
    """The property id for a label, and its formatter URL (what turns an id into a link)."""
    pid = None
    if guess:
        ent = api(action="wbgetentities", ids=guess, props="labels", languages="en").get("entities", {}).get(guess, {})
        got = ent.get("labels", {}).get("en", {}).get("value", "")
        if _norm(got) == _norm(label):
            pid = guess
        else:
            print(f"  {guess} is {got!r}, not {label!r}: searching by label")
    if not pid:
        r = api(action="wbsearchentities", search=label, type="property", language="en", limit=10)
        hit = next((x for x in r.get("search", []) if _norm(x.get("label", "")) == _norm(label)), None)
        if not hit:
            print(f"No Wikidata property called {label!r}")
            return None, None
        pid = hit["id"]
    e = api(action="wbgetentities", ids=pid, props="claims")["entities"][pid]
    fmts = [c["mainsnak"]["datavalue"]["value"] for c in e.get("claims", {}).get("P1630", []) if c["mainsnak"].get("datavalue")]
    fmt = next((f for f in fmts if "https" in f), fmts[0] if fmts else None)
    print(f"{label}: {pid} -> {fmt}")
    return pid, fmt


def opens(url):
    """True if the link opens (after redirects) without an error."""
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status < 400
        except urllib.error.HTTPError as ex:
            if ex.code in (429, 500, 502, 503, 504):
                time.sleep(3 * (attempt + 1))
                continue
            return False
        except Exception:  # noqa: BLE001
            time.sleep(2)
    return False


def main():
    import data as D
    pages = {}
    for p in D.PEOPLE:
        if p[9]:
            pages.setdefault(urllib.parse.unquote(p[9]).replace("_", " "), []).append("person:" + p[0])
    for pl in D.PLACES:
        if pl.get("src"):
            pages.setdefault(urllib.parse.unquote(pl["src"]).replace("_", " "), []).append("place:" + pl["id"])
    import eventpages as EP
    for i, ev in enumerate(D.EVENTS):
        if ev[11]:
            pages.setdefault(urllib.parse.unquote(ev[11]).split("#")[0].replace("_", " "), []).append("event:" + EP.SLUG[i])
    props = {k: prop(*v) for k, v in WANT.items()}
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
                keep = {a: b for a, b in rec.items() if a == "cy" or a in KINDS[kind]}
                if keep:
                    out[key] = keep
        time.sleep(0.5)
    # 3. Open every link once and drop any that doesn't open.
    from concurrent.futures import ThreadPoolExecutor
    urls = sorted({u for v in out.values() for k, u in v.items() if k != "cy"})
    with ThreadPoolExecutor(8) as pool:
        ok = dict(zip(urls, pool.map(opens, urls)))
    bad = [u for u in urls if not ok[u]]
    print(f"Opened {len(urls)} links: {len(bad)} did not open and are left out")
    for u in bad:
        print("  did not open:", u)
    out = {key: {k: u for k, u in v.items() if k == "cy" or ok[u]} for key, v in out.items()}
    out = {key: v for key, v in out.items() if v}
    out = dict(sorted(out.items()))
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")
    n = lambda k: sum(1 for v in out.values() if k in v)  # noqa: E731
    print(f"Wrote {OUT}: " + ", ".join(f"{n(k)} {k}" for k in list(WANT) + ["cy"]))


if __name__ == "__main__":
    main()
