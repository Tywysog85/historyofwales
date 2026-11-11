"""Keep the Wikimedia Commons photos on our own site instead of loading them from Wikimedia on every visit.

Run after `python3 build.py`. It finds every photo the built pages still load from Commons (the Special:FilePath links),
downloads each one once, and saves two WebP copies in src/static/photos/: <id>.webp (fits 1280 x 1000) and <id>-s.webp
(fits 600 x 800). src/photo_files.json records which Commons file each id is. build.py then uses the local copies, and the
credit links still go to the file's page on Commons.

Wikimedia is blocked from Claude's cloud computer, so this runs on GitHub: .github/workflows/fetch-photos.yml (start it from
the Actions tab, or it runs by itself when this file changes on a claude/ branch) and commits the pictures to the branch.
Needs Pillow (pip install pillow).
"""
import glob, hashlib, io, json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "src", "static", "photos")
MAP = os.path.join(ROOT, "src", "photo_files.json")
UA = "HistoryOfWalesSiteBuilder/1.0 (https://historyofwales.cymru; static site build)"


def wanted():
    names = set()
    for f in glob.glob(os.path.join(ROOT, "_site", "*.html")) + glob.glob(os.path.join(ROOT, "_site", "*.js")) + glob.glob(os.path.join(ROOT, "_site", "*.json")):
        for m in re.finditer(r"commons\.wikimedia\.org/wiki/Special:FilePath/([^\"'?\s<>]+)", open(f, encoding="utf-8").read()):
            names.add(urllib.parse.unquote(m.group(1)))
    return sorted(names)


def pid(name):
    base = re.sub(r"[^a-z0-9]+", "-", os.path.splitext(name)[0].lower()).strip("-")[:40].strip("-")
    return f"{base}-{hashlib.sha1(name.encode()).hexdigest()[:6]}"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def main():
    from PIL import Image
    os.makedirs(OUT, exist_ok=True)
    have = json.load(open(MAP, encoding="utf-8")) if os.path.exists(MAP) else {}
    todo = [n for n in wanted() if n not in have]
    print(f"{len(todo)} photos to fetch ({len(have)} already on the site)")
    failed = []
    for k, name in enumerate(todo):
        q = urllib.parse.quote(name, safe="")
        data = None
        for w in ("1280", "960", ""):
            try:
                data = get(f"https://commons.wikimedia.org/wiki/Special:FilePath/{q}" + (f"?width={w}" if w else ""))
                break
            except Exception as err:  # noqa: BLE001
                last = err
                time.sleep(2)
        if data is None:
            failed.append((name, str(last)))
            continue
        try:
            im = Image.open(io.BytesIO(data))
            im.load()
            im = im.convert("RGB")
        except Exception as err:  # noqa: BLE001
            failed.append((name, "not a picture: " + str(err)))
            continue
        i = pid(name)
        big = im.copy(); big.thumbnail((1280, 1000), Image.LANCZOS); big.save(os.path.join(OUT, i + ".webp"), "WEBP", quality=80, method=6)
        small = im.copy(); small.thumbnail((600, 800), Image.LANCZOS); small.save(os.path.join(OUT, i + "-s.webp"), "WEBP", quality=78, method=6)
        have[name] = [i, big.width, big.height]
        print(f"[{k + 1}/{len(todo)}] {name} -> {i} {big.width}x{big.height}")
        time.sleep(0.5)
    json.dump(dict(sorted(have.items())), open(MAP, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"Done: {len(have)} on the site, {len(failed)} failed")
    for n, why in failed:
        print("  failed:", n, why)


if __name__ == "__main__":
    sys.exit(main())
