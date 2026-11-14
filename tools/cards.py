"""Share pictures: the 1200 x 630 card Facebook, WhatsApp, X and others show when a page is shared, in English and Cymraeg.

build.py (share_cards() and make_cards()) calls render() for each page when Pillow is installed and writes
_site/cards/<page>.jpg and _site/cards/cy/<page>.jpg. Each card has the page's own photo across it, the night drawn over
the left where the words sit: its kind and age in the age's colour, its title in Gloock, a line about it, and the red
dragon with the site's name and address at the foot. Fonts are in tools/fonts (SIL Open Font Licence).
"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 630
NIGHT = (14, 17, 24)
INK = (236, 233, 225)
MUTED = (165, 171, 184)
_fonts = {}


def font(name, size, weight=None):
    k = (name, size, weight)
    if k not in _fonts:
        f = ImageFont.truetype(os.path.join(HERE, "fonts", name), size)
        if weight:
            f.set_variation_by_axes([weight])
        _fonts[k] = f
    return _fonts[k]


def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def wrap(draw, text, f, width, lines):
    words, out, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= width or not cur:
            cur = t
        else:
            out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    if len(out) > lines:
        out = out[:lines]
        while out[-1] and draw.textlength(out[-1] + "…", font=f) > width:
            out[-1] = out[-1].rsplit(" ", 1)[0] if " " in out[-1] else out[-1][:-1]
        out[-1] += "…"
    return out


def _cover(im, w, h, pos=None):
    """Crop a picture to fill w x h. pos is where its subject sits, as "x% y%" (from src/pictures.py), so a face or a
    castle stays in the frame; without it the crop keeps the middle across and a little above the middle down."""
    fx, fy = 0.5, 0.3
    if pos:
        try:
            fx, fy = (float(v.strip().rstrip("%")) / 100 for v in pos.split()[:2])
        except ValueError:
            pass
    s = max(w / im.width, h / im.height)
    im = im.resize((max(w, round(im.width * s)), max(h, round(im.height * s))), Image.LANCZOS)
    x, y = round((im.width - w) * fx), round((im.height - h) * fy)
    return im.crop((x, y, x + w, y + h))


_bg = {}


def _background(c):
    """The night with a glow of the age's colour, top right (made once per colour: the blur is the slow part)."""
    if c not in _bg:
        glow = Image.new("RGB", (W, H), NIGHT)
        ImageDraw.Draw(glow).ellipse((560, -380, 1500, 420), fill=tuple(int(NIGHT[i] * 0.55 + c[i] * 0.45) for i in range(3)))
        _bg[c] = Image.blend(Image.new("RGB", (W, H), NIGHT), glow.filter(ImageFilter.GaussianBlur(140)), 0.9)
    return _bg[c]


_veil = {}


def _veils(c):
    """The night laid over the photo: solid on the left where the words go, clearing to the right, with a touch of the
    age's colour, and a shade along the foot for the site's name. Made once per colour."""
    if c not in _veil:
        tint = tuple(int(NIGHT[i] * 0.8 + c[i] * 0.2) for i in range(3))
        col = Image.new("RGB", (W, H), NIGHT)
        cd = ImageDraw.Draw(col)
        for x in range(W):   # night on the far left, the age's tint where the veil thins
            t = min(1, max(0, (x - 380) / 520))
            cd.line([(x, 0), (x, H)], fill=tuple(round(NIGHT[i] * (1 - t) + tint[i] * t) for i in range(3)))
        a = Image.new("L", (W, H), 0)
        ad = ImageDraw.Draw(a)
        for x in range(W):
            t = min(1, max(0, (x - 430) / 480))
            ad.line([(x, 0), (x, H)], fill=round(250 - 220 * t * t * (3 - 2 * t)))   # smoothstep from 250 down to 30
        foot = Image.new("L", (W, H), 0)
        fd = ImageDraw.Draw(foot)
        for y in range(170):  # a shade rising from the foot, so the name reads over a bright sky or wall
            fd.line([(0, H - 1 - y), (W, H - 1 - y)], fill=round(200 * (1 - y / 170) ** 1.6))
        from PIL import ImageChops
        _veil[c] = (col, ImageChops.lighter(a, foot))
    return _veil[c]


_marks = {}


def _mark(dragon, h):
    """The red dragon, small, for the site's name at the foot."""
    k = (dragon, h)
    if k not in _marks:
        dr = Image.open(dragon).convert("RGBA")
        _marks[k] = dr.resize((round(dr.width * h / dr.height), h), Image.LANCZOS)
    return _marks[k]


def _shadowed(img, xy, text, f, fill, blur=6, strength=170):
    """Words with a soft dark shadow behind them, so they read where the veil over the photo is thin."""
    l, t, r, b = ImageDraw.Draw(img).textbbox(xy, text, font=f)
    pad = blur * 3
    box = (round(l) - pad, round(t) - pad, round(r) + pad, round(b) + pad + 2)   # blur only the patch around the words: fast
    sh = Image.new("L", (box[2] - box[0], box[3] - box[1]), 0)
    ImageDraw.Draw(sh).text((xy[0] - box[0], xy[1] + 2 - box[1]), text, font=f, fill=strength)
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    img.paste(Image.new("RGB", sh.size, (6, 8, 12)), box[:2], sh)
    ImageDraw.Draw(img).text(xy, text, font=f, fill=fill)


def make(out, eyebrow, title, sub, colour, photo=None, dragon=None, pos=None, lang="en"):
    """A page's share picture: its photo across the card, the night drawn over the left half where the words sit (the
    kind of page and its age in the age's colour, the title in Gloock, a line about it), and the site's name with the
    red dragon at the foot. Welsh pages get the Welsh words and "Hanes Cymru"."""
    c = hexrgb(colour)
    has_photo = bool(photo and os.path.exists(photo))
    if has_photo:
        img = Image.new("RGB", (W, H), NIGHT)
        src = Image.open(photo).convert("RGB")
        if src.height > src.width * 1.05:
            # a portrait or a statue: a narrower frame on the right, cropped near the top so the face stays in,
            # its left edge fading into the night
            pw = 620
            ph = _cover(src, pw, H, pos or "50% 12%")
            fade = Image.new("L", (pw, H), 255)
            fd = ImageDraw.Draw(fade)
            for x in range(200):
                fd.line([(x, 0), (x, H)], fill=round(255 * (x / 200) ** 1.3))
            img.paste(ph, (W - pw, 0), fade)
        else:
            img.paste(_cover(src, W - 300, H, pos), (300, 0))
        col, a = _veils(c)
        img.paste(col, (0, 0), a)
    else:
        img = _background(c).copy()
        if dragon and os.path.exists(dragon):
            dr = Image.open(dragon).convert("RGBA")
            dr.thumbnail((420, 320), Image.LANCZOS)
            img.paste(dr, (W - dr.width - 40, (H - dr.height) // 2 - 40), dr)
    d = ImageDraw.Draw(img)
    x, maxw = 72, 600
    d.rectangle((x, 66, x + 56, 72), fill=c)
    ef = font("Figtree.ttf", 25, 700)
    eb = eyebrow.upper()
    while d.textlength(eb, font=ef) > maxw + 60 and " · " in eb:
        eb = eb.rsplit(" · ", 1)[0]
    _shadowed(img, (x, 92), eb, ef, c, 5, 140)
    size = 88
    while size > 50:
        tf = font("Gloock-Regular.ttf", size)
        lines = wrap(d, title, tf, maxw, 3)
        if len(lines) <= 2 or size <= 64:
            break
        size -= 6
    y = 142
    for ln in lines:
        _shadowed(img, (x, y), ln, tf, INK)
        y += round(size * 1.08)
    if sub:
        sf = font("Figtree.ttf", 29, 400)
        room = 3 if len(lines) == 1 else 2 if len(lines) == 2 else 1
        y += 14
        for ln in wrap(d, sub, sf, maxw - 20, room):
            _shadowed(img, (x, y), ln, sf, (205, 209, 218), 4, 150)
            y += 39
    # the foot: dragon, the site's name, its address; a line of the age's colour along the bottom edge
    name, site = ("Hanes Cymru", "historyofwales.cymru/cy") if lang == "cy" else ("History of Wales", "historyofwales.cymru")
    fx = x
    if dragon and os.path.exists(dragon):
        m = _mark(dragon, 40)
        img.paste(m, (x - 6, H - 92), m)
        fx = x - 6 + m.width + 12
    nf = font("Gloock-Regular.ttf", 34)
    _shadowed(img, (fx, H - 90), name, nf, INK, 5, 160)
    af = font("Figtree.ttf", 23, 500)
    _shadowed(img, (fx + d.textlength(name, font=nf) + 18, H - 81), site, af, (190, 195, 206), 4, 160)
    d = ImageDraw.Draw(img)
    d.rectangle((0, H - 8, W, H), fill=c)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out, "JPEG", quality=82, optimize=True, progressive=True)


def make_home(out, line, photo, dragon, pos=None, lang="en"):
    """The home page's share picture: "Cymru" large with the y in dragon red, as at the top of the home page, one line
    under it, over a photo of Wales."""
    c = hexrgb("#e5443c")
    img = Image.new("RGB", (W, H), NIGHT)
    if photo and os.path.exists(photo):
        img.paste(_cover(Image.open(photo).convert("RGB"), W - 300, H, pos), (300, 0))
        col, a = _veils(c)
        img.paste(col, (0, 0), a)
    d = ImageDraw.Draw(img)
    x = 64
    big = font("Gloock-Regular.ttf", 210)
    for part, fill in (("C", INK), ("y", c), ("mru", INK)):
        _shadowed(img, (x, 70), part, big, fill, 8, 150)
        x += d.textlength(part, font=big)
    sf = font("Gloock-Regular.ttf", 44)
    y = 350
    for ln in wrap(d, line, sf, 640, 3):
        _shadowed(img, (70, y), ln, sf, INK, 6, 170)
        y += 56
    name, site = ("Hanes Cymru", "historyofwales.cymru/cy") if lang == "cy" else ("History of Wales", "historyofwales.cymru")
    fx = 70
    if dragon and os.path.exists(dragon):
        m = _mark(dragon, 40)
        img.paste(m, (64, H - 92), m)
        fx = 64 + m.width + 12
    nf = font("Gloock-Regular.ttf", 34)
    _shadowed(img, (fx, H - 90), name, nf, INK, 5, 160)
    _shadowed(img, (fx + d.textlength(name, font=nf) + 18, H - 81), site, font("Figtree.ttf", 23, 500), (190, 195, 206), 4, 160)
    ImageDraw.Draw(img).rectangle((0, H - 8, W, H), fill=c)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out, "JPEG", quality=84, optimize=True, progressive=True)


def make_square(out, eyebrow, date, title, line, colour, photo=None, dragon=None, site="historyofwales.cymru", name="History of Wales"):
    """The daily "On this day" picture for Instagram, Facebook and X: 1080 x 1080, the day's photo at the top fading
    into the night, the date large in the age's colour, then the title and one line."""
    S = 1080
    c = hexrgb(colour)
    glow = Image.new("RGB", (S, S), NIGHT)
    ImageDraw.Draw(glow).ellipse((420, -520, 1500, 520), fill=tuple(int(NIGHT[i] * 0.55 + c[i] * 0.45) for i in range(3)))
    img = Image.blend(Image.new("RGB", (S, S), NIGHT), glow.filter(ImageFilter.GaussianBlur(160)), 0.9)
    top = 72
    if photo and os.path.exists(photo):
        ph_h = 520
        ph = _cover(Image.open(photo).convert("RGB"), S, ph_h)
        mask = Image.new("L", (S, ph_h), 255)
        md = ImageDraw.Draw(mask)
        for y in range(220):  # fade the photo into the night at its foot
            md.line([(0, ph_h - 1 - y), (S, ph_h - 1 - y)], fill=round(255 * (y / 220) ** 1.3))
        img.paste(ph, (0, 0), mask)
        top = ph_h - 90
    elif dragon and os.path.exists(dragon):
        dr = Image.open(dragon).convert("RGBA")
        dr.thumbnail((520, 380), Image.LANCZOS)
        img.paste(dr, (S - dr.width - 40, 60), dr)
        top = 400
    d = ImageDraw.Draw(img)
    x, maxw = 80, S - 160
    d.rectangle((x, top, x + 64, top + 7), fill=c)
    d.text((x, top + 28), eyebrow.upper(), font=font("Figtree.ttf", 30, 700), fill=c)
    d.text((x, top + 72), date, font=font("Gloock-Regular.ttf", 96), fill=c)
    y = top + 200
    size = 66
    while True:
        tf = font("Gloock-Regular.ttf", size)
        lines = wrap(d, title, tf, maxw, 3)
        if len(lines) <= 2 or size <= 50:
            break
        size -= 6
    for ln in lines:
        d.text((x, y), ln, font=tf, fill=INK)
        y += round(size * 1.1)
    sf = font("Figtree.ttf", 34, 400)
    room = max(1, (S - 150 - y - 16) // 48)
    for ln in wrap(d, line, sf, maxw, min(4, room)):
        d.text((x, y + 16), ln, font=sf, fill=MUTED)
        y += 48
    d.line((x, S - 118, S - x, S - 118), fill=(48, 54, 66), width=2)
    d.text((x, S - 92), name, font=font("Gloock-Regular.ttf", 38), fill=INK)
    sw = d.textlength(site, font=font("Figtree.ttf", 28, 500))
    d.text((S - x - sw, S - 84), site, font=font("Figtree.ttf", 28, 500), fill=MUTED)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out, "JPEG", quality=88, optimize=True, progressive=True)


def render(job):
    """Draw one share picture from build.py's share_cards() list: (file to write, what goes on it)."""
    out, s = job
    if s["kind"] == "home":
        make_home(out, s["line"], s["photo"], s["dragon"], s["pos"], s["lang"])
    else:
        make(out, s["eyebrow"], s["title"], s["sub"], s["colour"], s["photo"], s["dragon"], s["pos"], s["lang"])
