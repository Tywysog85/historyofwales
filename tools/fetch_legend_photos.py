"""Fetch the photographs for the legend pictures from Wikimedia Commons.

Wikimedia is blocked from Claude's cloud computer, so this runs on GitHub with tools/fetch_photos.py
(.github/workflows/fetch-photos.yml) and the pictures are committed to the branch.

PICKS maps an art key (src/art.py) to a Commons file. Each is saved as src/static/legends/<key>.webp (1600 px wide)
and <key>-s.webp (700 px, for the cards). The credits are in LEGEND_PHOTOS in src/art.py: keep the two in step.
Needs Pillow.
"""
import io, os, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "src", "static", "legends")
UA = "HistoryOfWalesSiteBuilder/1.0 (https://historyofwales.cymru; static site build)"
PICKS = {
 "hound": "Drew - Irish Wolfhound (20540782194).jpg", "owl": "Waldkauz-Strix aluco.jpg",
 "bird": "Sturnus vulgaris (European starling) at Bodega Head-1209.jpg", "lady": "Llyn y fan fach.jpg",
 "sunken": "Submerged forest at Ynyslas, Ceredigion.jpg", "sword": "Llyn Ogwen Milky Way.jpg", "cauldron": "Gundestrup cauldron.jpg",
 # not a legend: the picture at the top of the Welsh Not long read (src/pictures.py PAGE uses "l:iaith-1966")
 "iaith-1966": "Members of the Welsh Language Society protesting outside Llangefni Post Office (1502061).jpg",
}


def main():
    from PIL import Image
    os.makedirs(OUT, exist_ok=True)
    bad = 0
    for name, f in PICKS.items():
        dst = os.path.join(OUT, name + ".webp")
        if os.path.exists(dst):
            continue
        q = urllib.parse.quote(f.replace(" ", "_"), safe="")
        data = None
        for w in ("1920", "1280", ""):  # Commons only serves its standard widths
            try:
                req = urllib.request.Request(f"https://commons.wikimedia.org/wiki/Special:FilePath/{q}" + (f"?width={w}" if w else ""), headers={"User-Agent": UA})
                data = urllib.request.urlopen(req, timeout=90).read()
                break
            except Exception as err:  # noqa: BLE001
                last = err
                time.sleep(3)
        if data is None:
            print("failed:", name, f, last); bad += 1
            continue
        im = Image.open(io.BytesIO(data)).convert("RGB")
        im.thumbnail((1600, 1600), Image.LANCZOS)
        im.save(dst, "WEBP", quality=80, method=6)
        sm = im.copy(); sm.thumbnail((700, 700), Image.LANCZOS); sm.save(dst[:-5] + "-s.webp", "WEBP", quality=78, method=6)
        print(name, im.size)
        time.sleep(1.5)
    print("failed", bad)


if __name__ == "__main__":
    sys.exit(main())
