"""Fetch the photographs for the legend pictures from Wikimedia Commons.

Wikimedia is blocked from Claude's cloud computer, so this runs on GitHub with tools/fetch_photos.py
(.github/workflows/fetch-photos.yml) and the pictures are committed to the branch.

PICKS maps a name to a Commons file. Each is saved as src/static/legends/<name>.webp, 1600 px wide.
Needs Pillow.
"""
import io, os, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "src", "static", "legends")
UA = "HistoryOfWalesSiteBuilder/1.0 (https://historyofwales.cymru; static site build)"
PICKS = {
 "hound-1": "Tommy - Irish Wolfhound (14487067883).jpg", "hound-2": "Drew - Irish Wolfhound (20540782194).jpg",
 "hound-3": "Drew - Irish Wolfhound (21562428508).jpg", "hound-4": "Karrie.JPG", "hound-5": "Irish wolfhound giaccomo.JPG",
 "owl-1": "Waldkauz-Strix aluco.jpg", "owl-2": "Tyto alba 1 Luc Viatour.jpg", "owl-3": "Tyto alba - Cetrería - 02.jpg",
 "owl-4": "Tyto alba (Scopoli, 1769).jpg", "owl-5": "Strix aluco, Neuss (DE) -- 2022 -- 0132.jpg",
 "starling-1": "European starling in CP (33849).jpg", "starling-2": "Sturnus vulgaris (European starling) at Bodega Head-1209.jpg",
 "starling-3": "Sturnus vulgaris -California-8.jpg", "starling-4": "Toulouse - Sturnus vulgaris - 2012-02-26 - 1.jpg",
 "starling-5": "Sturnus vulgaris in Napa Valley.jpg",
 "lake-1": "Llyn Y Fan Fach - geograph.org.uk - 1755206.jpg", "lake-2": "Llyn y Fan Fach from Waun Lefrith.jpg", "lake-3": "Llyn y fan fach.jpg",
 "lake-4": "Llyn y Fan Fach (1323880330).jpg", "lake-5": "Bannau Sir Gaer ^ Llyn y Fan Fach - geograph.org.uk - 6462329.jpg",
 "sunken-1": "Submerged forest at Ynyslas, Ceredigion.jpg", "sunken-2": "Ancient sunken forest at sunset 02.jpg",
 "sunken-3": "Coedwig foddedig - Submerged forest - geograph.org.uk - 4076781.jpg",
 "sunken-4": "Coedwig foddedig - Y Borth - Borth - Submerged forest - geograph.org.uk - 4076827.jpg",
 "sunken-5": "Coedwig foddedig - Y Borth - Borth - Submerged forest - geograph.org.uk - 4076830.jpg",
 "sword-1": "Llyn Ogwen Milky Way.jpg", "sword-2": "Glaslyn and Llyn Llydaw.jpg", "sword-3": "Llyn Llydaw with Snowdon in silhouette - geograph.org.uk - 4302052.jpg",
 "sword-4": "Llyn Ogwen - geograph.org.uk - 4675361.jpg", "sword-5": "Early La Tene Sword from Hallstatt Grave 994.JPG",
 "cauldron-1": "Battersea Cauldron in the British Museum.jpg", "cauldron-2": "Gundestrup cauldron.jpg", "cauldron-3": "UlsterMuseumPrehistorybr.JPG",
 "cauldron-4": "Dusk at Llyn Tegid - geograph.org.uk - 6334350.jpg", "cauldron-5": "Llyn Tegid and Aran Benllyn - geograph.org.uk - 3650834.jpg",
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
        im.save(dst, "WEBP", quality=82, method=6)
        print(name, im.size)
        time.sleep(1.5)
    print("failed", bad)


if __name__ == "__main__":
    sys.exit(main())
