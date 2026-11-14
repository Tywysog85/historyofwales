"""Make the small pictures that fill the letters of the scrolling words band on the home page (Ifan, 14 Nov 2026).

Each word ("Castles", "Saints", "Coal"...) is painted with a strip cut from a picture the site already keeps, with its
Wikimedia Commons credit in src/gallery_photos.py or src/art.py. The strips are small (512 x 160, about 12 KB) so the
band stays light on phones. "Dragons" is the Welsh flag: white over green with the site's own 3D red dragon across it.

Run from the repository root:   python3 tools/make_marquee_pictures.py
It writes src/static/mq/<word>.webp and src/static/mq-dragon.webp (the little dragon between the words). Commit them.
To change a word's picture, change its line in STRIPS (file, then the part of the picture to keep, as fractions
left, top, right, bottom) and run it again.
"""
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ST = os.path.join(ROOT, "src", "static")
OUT = os.path.join(ST, "mq")
W, H = 512, 160

STRIPS = {
    "castles": ("gallery/place-caernarfon.webp", (0.0, 0.12, 1.0, 0.55)),
    "kings": ("gallery/trea-laws-hywel.webp", (0.22, 0.22, 0.95, 0.52)),
    "poets": ("gallery/trea-black-book.webp", (0.08, 0.10, 0.92, 0.48)),
    "saints": ("gallery/person-dewi-sant.webp", (0.12, 0.24, 0.88, 0.50)),
    "princes": ("gallery/trea-seal-glyndwr.webp", (0.08, 0.22, 0.92, 0.70)),
    "coal": ("gallery/indu-rhondda.webp", (0.0, 0.05, 1.0, 0.65)),
    "slate": ("gallery/place-dinorwig.webp", (0.0, 0.35, 1.0, 0.90)),
    "song": ("gallery/holy-tabernacl.webp", (0.0, 0.10, 1.0, 0.62)),
    "language": ("gallery/trea-bible-1588.webp", (0.10, 0.30, 0.90, 0.62)),
    "rebels": ("legends/iaith-1966.webp", (0.0, 0.20, 1.0, 0.72)),
    "legends": ("gallery/person-arthur.webp", (0.0, 0.18, 1.0, 0.55)),
}


def strip(src, box):
    im = Image.open(os.path.join(ST, src)).convert("RGB")  # the 1400 px picture
    w, h = im.size
    l, t, r, b = box
    im = im.crop((int(l * w), int(t * h), int(r * w), int(b * h)))
    # fill W x H without stretching: scale to cover, then cut the middle
    s = max(W / im.width, H / im.height)
    im = im.resize((max(W, round(im.width * s)), max(H, round(im.height * s))), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H) // 2
    return im.crop((x, y, x + W, y + H))


def flag():
    """The Welsh flag with the site's red dragon flying across it."""
    im = Image.new("RGB", (W, H), (246, 244, 236))
    im.paste((0, 150, 70), (0, H // 2, W, H))
    d = Image.open(os.path.join(ST, "dragon-red.webp")).convert("RGBA")
    dh = int(H * 0.95)
    d = d.resize((int(d.width * dh / d.height), dh), Image.LANCZOS)
    im.paste(d, ((W - d.width) // 2, (H - dh) // 2), d)
    return im


def small_dragon():
    """The little dragon between the words: the 3D dragon, its long tail trimmed so the body reads at 60 px."""
    d = Image.open(os.path.join(ST, "dragon-red.webp")).convert("RGBA")
    d = d.crop((int(d.width * 0.24), 0, d.width, d.height))
    d = d.crop(d.getbbox())
    d.thumbnail((180, 90), Image.LANCZOS)
    d.save(os.path.join(ST, "mq-dragon.webp"), quality=82, method=6)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k, (src, box) in STRIPS.items():
        strip(src, box).save(os.path.join(OUT, k + ".webp"), quality=60, method=6)
    flag().save(os.path.join(OUT, "dragons.webp"), quality=74, method=6)
    small_dragon()
    for f in sorted(os.listdir(OUT)):
        print(f, os.path.getsize(os.path.join(OUT, f)) // 1024, "KB")
    print("mq-dragon.webp", os.path.getsize(os.path.join(ST, "mq-dragon.webp")) // 1024, "KB")
