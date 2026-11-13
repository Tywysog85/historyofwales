# Small copies of the site's pictures for the little pictures on cards and list rows (Ifan, 13 November 2026: "add
# pictures to all cards on the site"). A card picture is drawn at 50 to 90 pixels, so the 600 pixel "-s" copy is
# far more than a phone needs: thumb() names a copy whose short side is SHORT pixels (about 8 KB) and write() makes
# them at the end of the build, in _site/t/. Nothing is kept in the repository, so a new picture gets its small copy
# by itself. Without Pillow (a quick build on a computer that lacks it) the cards simply use the 600 pixel copy.
import os

try:
    from PIL import Image
    OK = True
except ImportError:  # pragma: no cover
    OK = False

SHORT = 220          # short side of a small copy, in pixels (a 72 px picture on a phone with a sharp screen)
_HERE = os.path.dirname(os.path.abspath(__file__))
_WANT = {}           # "t/<name>.webp" -> picture in src/static


def thumb(rel):
    """The small copy of a picture kept on the site (gallery/x-s.webp, photos/y-s.webp, legends/z-s.webp ...)."""
    if not OK or not rel or rel.startswith(("http:", "https:", "t/")):
        return rel
    src = os.path.join(_HERE, "static", rel)
    if not os.path.exists(src):
        return rel
    name = "t/" + rel.rsplit(".", 1)[0].replace("/", "-")
    name = (name[:-2] if name.endswith("-s") else name) + ".webp"
    _WANT[name] = src
    return name


def write(out):
    """Make every small copy asked for during the build. Returns how many."""
    os.makedirs(os.path.join(out, "t"), exist_ok=True)
    for name, src in _WANT.items():
        with Image.open(src) as im:
            im.load()
            w, h = im.size
            k = SHORT / min(w, h)
            if k < 1:
                im = im.resize((max(1, round(w * k)), max(1, round(h * k))), Image.LANCZOS)
            im.save(os.path.join(out, name), "WEBP", quality=74, method=5)
    return len(_WANT)
