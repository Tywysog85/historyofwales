"""Look up candidate pictures on Wikimedia Commons, on GitHub (Commons is blocked from Claude's cloud computer).

Reads tools/commons_research_in.json: {"branch": "<your claude/ branch>", "out": "<folder>", "categories": [...], "searches": [...], "files": [...],
"download": [...]}. Optional: "per_search" (results per search, default 40), "previews" (false = list only, no preview
pictures, for a first wide sweep) and "preview_px" (preview size, default 500) and "download_px" (size of the full copies, default 1400). Files listed under "download" are also saved full size (fits 1400 x 1400) as <folder>/full/<k>.jpg, ready to be
made into gallery pictures.
The workflow only runs it on the branch named in "branch" (or when started by hand), so set that to your own branch.
For every file found it records the title, size, licence, author and description, and saves a small preview JPEG
(fits 500 x 500) so the pictures can be looked at before any is used. Writes <folder>/found.json and <folder>/<n>.jpg.
Runs from .github/workflows/commons-research.yml. Delete the folder when the research is finished.
"""
import io, json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "HistoryOfWalesSiteBuilder/1.0 (https://historyofwales.cymru; picture research)"
API = "https://commons.wikimedia.org/w/api.php?"


def get(url, raw=False):
    for t in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                d = r.read()
                return d if raw else json.loads(d)
        except Exception as err:  # noqa: BLE001
            last = err
            time.sleep(2 + t * 3)
    raise last


def api(**p):
    p.update(format="json", formatversion="2")
    return get(API + urllib.parse.urlencode(p))


def strip(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


def main():
    cfg = json.load(open(os.path.join(ROOT, "tools", "commons_research_in.json"), encoding="utf-8"))
    out = os.path.join(ROOT, cfg["out"])
    os.makedirs(out, exist_ok=True)
    if cfg.get("people"):
        return people(cfg["people"], out)
    titles, where = [], {}
    def add(t, why):
        if t not in where:
            titles.append(t)
            where[t] = why
    for c in cfg.get("categories", []):
        cont = {}
        while True:
            r = api(action="query", list="categorymembers", cmtitle=c, cmtype="file", cmlimit="500", **cont)
            for m in r.get("query", {}).get("categorymembers", []):
                add(m["title"], c)
            if "continue" not in r:
                break
            cont = {"cmcontinue": r["continue"]["cmcontinue"]}
        r = api(action="query", list="categorymembers", cmtitle=c, cmtype="subcat", cmlimit="100")
        subs = [m["title"] for m in r.get("query", {}).get("categorymembers", [])]
        print(c, "subcats:", subs)
        where.setdefault("_subcats", {})[c] = subs
    for s in cfg.get("searches", []):
        r = api(action="query", list="search", srsearch=s, srnamespace="6", srlimit=str(cfg.get("per_search", 40)))
        for m in r.get("query", {}).get("search", []):
            add(m["title"], "search: " + s)
    for f in cfg.get("files", []):
        add(f if f.startswith("File:") else "File:" + f, "named")
    titles = titles[: cfg.get("max", 300)]
    found = []
    for i in range(0, len(titles), 40):
        chunk = titles[i:i + 40]
        r = api(action="query", prop="imageinfo", titles="|".join(chunk), iiprop="url|size|extmetadata|mime", iiurlwidth="500")
        for pg in r["query"]["pages"]:
            ii = (pg.get("imageinfo") or [{}])[0]
            md = ii.get("extmetadata", {})
            v = lambda k: strip(md.get(k, {}).get("value", ""))
            found.append(dict(title=pg["title"], why=where.get(pg["title"], ""), w=ii.get("width"), h=ii.get("height"), mime=ii.get("mime"),
                              licence=v("LicenseShortName"), licence_url=v("LicenseUrl"), artist=v("Artist"), credit=v("Credit"),
                              desc=v("ImageDescription")[:600], date=v("DateTimeOriginal")[:80], thumb=ii.get("thumburl")))
    for n, f in enumerate(found):
        f["n"] = n
        if cfg.get("previews", True) and f.get("thumb") and (f.get("mime") or "").startswith("image/"):
            try:
                from PIL import Image
                im = Image.open(io.BytesIO(get(f["thumb"], raw=True))).convert("RGB")
                px = cfg.get("preview_px", 500)
                im.thumbnail((px, px))
                im.save(os.path.join(out, f"{n}.jpg"), quality=70)
            except Exception as err:  # noqa: BLE001
                f["thumb_error"] = str(err)
            time.sleep(0.3)
    for k, f in enumerate(cfg.get("download", [])):  # full-size copies (fits 1400 x 1400) of the pictures chosen, for the site
        f = f if f.startswith("File:") else "File:" + f
        try:
            px = cfg.get("download_px", 1400)
            r = api(action="query", prop="imageinfo", titles=f, iiprop="url|size", iiurlwidth=str(px))
            ii = r["query"]["pages"][0]["imageinfo"][0]
            u = ii["thumburl"] if ii.get("width", 0) > px else ii["url"]
            from PIL import Image
            Image.MAX_IMAGE_PIXELS = None
            try:
                im = Image.open(io.BytesIO(get(u, raw=True))).convert("RGB")
            except Exception:  # noqa: BLE001  (Commons may refuse a thumbnail at an unusual width: take the original)
                im = Image.open(io.BytesIO(get(ii["url"], raw=True))).convert("RGB")
            im.thumbnail((px, px))
            os.makedirs(os.path.join(out, "full"), exist_ok=True)
            im.save(os.path.join(out, "full", f"{k}.jpg"), quality=90)
            found.append(dict(title=f, why="download", full=f"full/{k}.jpg", w=im.width, h=im.height))
        except Exception as err:  # noqa: BLE001
            found.append(dict(title=f, why="download", error=str(err)))
        time.sleep(0.5)
    json.dump(dict(found=found, subcats=where.get("_subcats", {})), open(os.path.join(out, "found.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(found), "files")


# ---------- portraits for people pages ----------
# "people": [{"slug": ..., "name": ..., "wiki": "<English Wikipedia title>"}, ...] looks up, for each person, the picture
# Wikidata gives them (P18 image, P1442 grave, P158 seal), the free lead image of their English and Welsh Wikipedia
# articles, the first files in their Commons category and a Commons search for their name. It writes <out>/people.json
# (every candidate with its licence and author) and contact sheets <out>/sheet-<n>.jpg: one row per person, each picture
# numbered as in people.json, so the right one can be picked by eye. Non-free licences are marked NONFREE and never used.
WD = "https://www.wikidata.org/w/api.php?"
FREE = re.compile(r"public domain|^pd|cc0|cc[ -]by(?![- ]n)|cc[ -]by[ -]sa|no restrictions|ogl|attribution|gfdl|free art", re.I)


def wiki_api(lang, **p):
    p.update(format="json", formatversion="2")
    return get(f"https://{lang}.wikipedia.org/w/api.php?" + urllib.parse.urlencode(p))


def chunks(xs, n):
    for i in range(0, len(xs), n):
        yield xs[i:i + n]


def people(ppl, out):
    from PIL import Image, ImageDraw, ImageFont
    cands = {x["slug"]: [] for x in ppl}
    def add(slug, title, why):
        title = title if title.startswith("File:") else "File:" + title
        title = title.replace("_", " ")
        if title not in [c["title"] for c in cands[slug]]:
            cands[slug].append(dict(title=title, why=why))
    # English Wikipedia: free lead image and Wikidata item
    qid = {}
    by_title = {}
    for x in ppl:
        if x.get("wiki"):
            by_title.setdefault(urllib.parse.unquote(x["wiki"]).replace("_", " "), []).append(x["slug"])
    for ch in chunks(list(by_title), 40):
        r = wiki_api("en", action="query", titles="|".join(ch), prop="pageimages|pageprops", piprop="name", pilicense="free", ppprop="wikibase_item", redirects="1")
        q = r.get("query", {})
        back = {}
        for m in q.get("normalized", []) + q.get("redirects", []):
            back[m["to"]] = back.get(m["from"], m["from"])
        for pg in q.get("pages", []):
            t = pg["title"]
            orig = back.get(t, t)
            orig = back.get(orig, orig)
            for slug in by_title.get(orig) or by_title.get(t) or []:
                if pg.get("pageimage"):
                    add(slug, pg["pageimage"], "enwiki lead image")
                if pg.get("pageprops", {}).get("wikibase_item"):
                    qid[slug] = pg["pageprops"]["wikibase_item"]
        time.sleep(1)
    # Wikidata: image, grave, seal, Commons category, Welsh article
    cat, cy = {}, {}
    slugs = list(qid)
    for ch in chunks(slugs, 45):
        r = get(WD + urllib.parse.urlencode(dict(action="wbgetentities", ids="|".join(qid[s] for s in ch), props="claims|sitelinks", sitefilter="cywiki", format="json")))
        for s in ch:
            ent = r.get("entities", {}).get(qid[s], {})
            cl = ent.get("claims", {})
            for prop, why in (("P18", "Wikidata image"), ("P1442", "Wikidata grave"), ("P158", "Wikidata seal"), ("P2716", "Wikidata collage")):
                for c in cl.get(prop, []):
                    v = c.get("mainsnak", {}).get("datavalue", {}).get("value")
                    if isinstance(v, str):
                        add(s, v, why)
            for c in cl.get("P373", []):
                v = c.get("mainsnak", {}).get("datavalue", {}).get("value")
                if isinstance(v, str):
                    cat[s] = v
            sl = ent.get("sitelinks", {}).get("cywiki")
            if sl:
                cy[sl["title"]] = s
        time.sleep(1)
    for ch in chunks(list(cy), 40):  # Welsh Wikipedia lead images
        r = wiki_api("cy", action="query", titles="|".join(ch), prop="pageimages", piprop="name", pilicense="free", redirects="1")
        q = r.get("query", {})
        back = {m["to"]: m["from"] for m in q.get("normalized", []) + q.get("redirects", [])}
        for pg in q.get("pages", []):
            s = cy.get(back.get(pg["title"], pg["title"])) or cy.get(pg["title"])
            if s and pg.get("pageimage"):
                add(s, pg["pageimage"], "cywiki lead image")
        time.sleep(1)
    for x in ppl:  # files named by hand, the Commons category, then a search for the name
        s = x["slug"]
        for f in x.get("files", []):
            add(s, f, "named")
        if s in cat:
            try:
                r = api(action="query", list="categorymembers", cmtitle="Category:" + cat[s], cmtype="file", cmlimit=str(x.get("cat", 4)))
                for m in r.get("query", {}).get("categorymembers", []):
                    add(s, m["title"], "category " + cat[s])
            except Exception as err:  # noqa: BLE001
                print("category failed", s, err)
        for q in x.get("search") or ([] if x.get("files") else ['"' + x["name"] + '"']):
            try:
                r = api(action="query", list="search", srsearch=q + " filetype:bitmap", srnamespace="6", srlimit=str(x.get("n", 4)))
                for m in r.get("query", {}).get("search", []):
                    add(s, m["title"], "search " + q)
            except Exception as err:  # noqa: BLE001
                print("search failed", s, err)
        time.sleep(0.4)
    # licences, authors and thumbnails
    allt = sorted({c["title"] for v in cands.values() for c in v})
    info = {}
    for ch in chunks(allt, 40):
        r = api(action="query", prop="imageinfo", titles="|".join(ch), iiprop="url|size|extmetadata|mime", iiurlwidth="330")
        q = r.get("query", {})
        back = {m["to"]: m["from"] for m in q.get("normalized", [])}
        for pg in q.get("pages", []):
            ii = (pg.get("imageinfo") or [{}])[0]
            md = ii.get("extmetadata", {})
            v = lambda k: strip(md.get(k, {}).get("value", ""))
            d = dict(w=ii.get("width"), h=ii.get("height"), mime=ii.get("mime"), licence=v("LicenseShortName"), licence_url=v("LicenseUrl"),
                     artist=v("Artist")[:200], desc=v("ImageDescription")[:400], date=v("DateTimeOriginal")[:60], thumb=ii.get("thumburl"), missing=pg.get("missing", False))
            info[pg["title"]] = d
            info[back.get(pg["title"], pg["title"])] = d
        time.sleep(0.5)
    try:
        font = ImageFont.truetype(os.path.join(ROOT, "tools", "fonts", "Figtree.ttf"), 15)
        big = ImageFont.truetype(os.path.join(ROOT, "tools", "fonts", "Figtree.ttf"), 20)
    except Exception:  # noqa: BLE001
        font = big = ImageFont.load_default()
    T, PER, NAMEW = 170, 8, 190
    rows = []
    for x in ppl:
        s = x["slug"]
        row = Image.new("RGB", (NAMEW + PER * (T + 6), T + 26), "white")
        d = ImageDraw.Draw(row)
        d.text((6, 6), x["name"][:22], fill="black", font=big)
        d.text((6, 34), s[:24], fill="#555", font=font)
        keep = []
        for c in cands[s]:
            c.update(info.get(c["title"], {}))
            c["free"] = bool(FREE.search(c.get("licence") or "")) and not re.search(r"\bNC\b|\bND\b|non-?commercial|no ?deriv|fair use", c.get("licence") or "", re.I)
            if c.get("missing") or not (c.get("mime") or "").startswith("image/"):
                continue
            keep.append(c)
        cands[s] = keep
        d.text((6, 58), f"{len(keep)} found", fill="#555", font=font)
        for n, c in enumerate(keep[:PER]):
            c["n"] = n
            xo = NAMEW + n * (T + 6)
            try:
                im = Image.open(io.BytesIO(get(c["thumb"], raw=True))).convert("RGB")
                im.thumbnail((T, T))
                row.paste(im, (xo + (T - im.width) // 2, (T - im.height) // 2))
            except Exception as err:  # noqa: BLE001
                c["thumb_error"] = str(err)
            lab = f'{n} {"" if c["free"] else "NONFREE "}{(c.get("licence") or "?")[:14]}'
            d.rectangle((xo, T + 2, xo + T, T + 24), fill="#fff" if c["free"] else "#fcc")
            d.text((xo + 2, T + 4), lab, fill="black", font=font)
            time.sleep(0.25)
        rows.append(row)
    for k, ch in enumerate(chunks(rows, 8)):
        sheet = Image.new("RGB", (ch[0].width, sum(r.height + 4 for r in ch)), "#999")
        y = 0
        for r in ch:
            sheet.paste(r, (0, y))
            y += r.height + 4
        sheet.save(os.path.join(out, f"sheet-{k:02d}.jpg"), quality=72)
    for v in cands.values():
        for c in v:
            c.pop("thumb", None)
    json.dump(dict(order=[x["slug"] for x in ppl], qid=qid, category=cat, people=cands), open(os.path.join(out, "people.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(ppl), "people,", sum(len(v) for v in cands.values()), "pictures")


if __name__ == "__main__":
    main()
