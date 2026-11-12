"""Look up candidate pictures on Wikimedia Commons, on GitHub (Commons is blocked from Claude's cloud computer).

Reads tools/commons_research_in.json: {"branch": "<your claude/ branch>", "out": "<folder>", "categories": [...], "searches": [...], "files": [...],
"download": [...]}. Files listed under "download" are also saved full size (fits 1400 x 1400) as <folder>/full/<k>.jpg, ready to be
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
        r = api(action="query", list="search", srsearch=s, srnamespace="6", srlimit="40")
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
        if f.get("thumb") and (f.get("mime") or "").startswith("image/"):
            try:
                from PIL import Image
                im = Image.open(io.BytesIO(get(f["thumb"], raw=True))).convert("RGB")
                im.thumbnail((500, 500))
                im.save(os.path.join(out, f"{n}.jpg"), quality=70)
            except Exception as err:  # noqa: BLE001
                f["thumb_error"] = str(err)
            time.sleep(0.3)
    for k, f in enumerate(cfg.get("download", [])):  # full-size copies (fits 1400 x 1400) of the pictures chosen, for the site
        f = f if f.startswith("File:") else "File:" + f
        try:
            r = api(action="query", prop="imageinfo", titles=f, iiprop="url", iiurlwidth="1400")
            u = r["query"]["pages"][0]["imageinfo"][0]["thumburl"]
            from PIL import Image
            im = Image.open(io.BytesIO(get(u, raw=True))).convert("RGB")
            im.thumbnail((1400, 1400))
            os.makedirs(os.path.join(out, "full"), exist_ok=True)
            im.save(os.path.join(out, "full", f"{k}.jpg"), quality=90)
            found.append(dict(title=f, why="download", full=f"full/{k}.jpg", w=im.width, h=im.height))
        except Exception as err:  # noqa: BLE001
            found.append(dict(title=f, why="download", error=str(err)))
        time.sleep(0.5)
    json.dump(dict(found=found, subcats=where.get("_subcats", {})), open(os.path.join(out, "found.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(found), "files")


if __name__ == "__main__":
    main()
