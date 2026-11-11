"""Turn the Wikimedia Commons research for the photo gallery into site files.

Usage:  python tools/gallery_import.py <research folder>

The research folder holds results.json (one entry per picture: id, file, author, licence,
licence_url, width, height, what) and img/<id>.jpg (about 1400 px wide). Welsh captions come
from tools/gallery_cy.json (id -> Welsh sentence). Pictures listed in tools/gallery_skip.json
are left out.

Writes:
  src/static/gallery/<id>.webp     1400 px wide, for the big-picture viewer
  src/static/gallery/<id>-s.webp   600 px wide, for the grid
  src/gallery_photos.py            the credits
"""
import json
import os
import sys

from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "src", "static", "gallery")


def load(name, default):
    p = os.path.join(ROOT, "tools", name)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else default


def main(folder):
    res = json.load(open(os.path.join(folder, "results.json"), encoding="utf-8"))
    cy = load("gallery_cy.json", {})
    skip = set(load("gallery_skip.json", []))
    os.makedirs(OUT, exist_ok=True)
    rows, missing = [], []
    for r in res:
        if not r.get("file") or r["id"] in skip:
            continue
        src = os.path.join(folder, "img", r["id"] + ".jpg")
        if not os.path.exists(src):
            missing.append(r["id"])
            continue
        im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        w, h = im.size
        for suffix, width, q in (("", 1400, 78), ("-s", 600, 72)):
            t = im if w <= width else im.resize((width, round(h * width / w)), Image.LANCZOS)
            t.save(os.path.join(OUT, r["id"] + suffix + ".webp"), "WEBP", quality=q, method=6)
        what = r.get("what", "").strip()
        rows.append((r["id"], r["file"], r.get("author", "").strip() or "Unknown", r.get("licence", "").strip(), r.get("licence_url", "").strip(),
                     what, cy.get(r["id"], what), w, h))
    with open(os.path.join(ROOT, "src", "gallery_photos.py"), "w", encoding="utf-8") as f:
        f.write("# Gallery pictures from Wikimedia Commons. Made by tools/gallery_import.py: edit the research and run it again rather than editing by hand.\n")
        f.write("# id -> (Commons file name, author, licence, licence link, what it shows EN, CY, width, height)\nGALLERY = {\n")
        for row in rows:
            f.write(f" {row[0]!r}: {row[1:]!r},\n")
        f.write("}\n")
    print(f"{len(rows)} pictures written; missing images: {missing}")


if __name__ == "__main__":
    main(sys.argv[1])
