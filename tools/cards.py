"""Share pictures: the 1200 x 630 card Facebook, WhatsApp, X and others show when a page is shared.

build.py calls make() for each page (when Pillow is installed) and writes _site/cards/<page>.jpg. Each card has the page's
title in the display font, its kind and age in the age's colour, a line under the title, the site's address, and on the
right the page's photo or, where there is none, the red dragon. Fonts are in tools/fonts (SIL Open Font Licence).
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


def _cover(im, w, h):
    s = max(w / im.width, h / im.height)
    im = im.resize((max(w, round(im.width * s)), max(h, round(im.height * s))), Image.LANCZOS)
    x, y = (im.width - w) // 2, max(0, min(im.height - h, round((im.height - h) * 0.3)))
    return im.crop((x, y, x + w, y + h))


_bg = {}


def _background(c):
    """The night with a glow of the age's colour, top right (made once per colour: the blur is the slow part)."""
    if c not in _bg:
        glow = Image.new("RGB", (W, H), NIGHT)
        ImageDraw.Draw(glow).ellipse((560, -380, 1500, 420), fill=tuple(int(NIGHT[i] * 0.55 + c[i] * 0.45) for i in range(3)))
        _bg[c] = Image.blend(Image.new("RGB", (W, H), NIGHT), glow.filter(ImageFilter.GaussianBlur(140)), 0.9)
    return _bg[c]


def make(out, eyebrow, title, sub, colour, photo=None, dragon=None):
    c = hexrgb(colour)
    img = _background(c).copy()
    right = 470
    if photo and os.path.exists(photo):
        ph = _cover(Image.open(photo).convert("RGB"), right, H)
        mask = Image.new("L", (right, H), 255)
        md = ImageDraw.Draw(mask)
        for x in range(170):  # fade the photo into the night on its left edge
            md.line([(x, 0), (x, H)], fill=round(255 * (x / 170) ** 1.4))
        img.paste(ph, (W - right, 0), mask)
    elif dragon and os.path.exists(dragon):
        dr = Image.open(dragon).convert("RGBA")
        dr.thumbnail((400, 300), Image.LANCZOS)
        img.paste(dr, (W - dr.width - 24, (H - dr.height) // 2 - 40), dr)
    d = ImageDraw.Draw(img)
    has_photo = bool(photo and os.path.exists(photo))
    x, maxw = 72, (W - right - 72 - 40) if has_photo else 590
    d.rectangle((x, 70, x + 56, 76), fill=c)
    d.text((x, 96), eyebrow.upper(), font=font("Figtree.ttf", 26, 700), fill=c, spacing=4)
    size = 92
    while size > 50:
        tf = font("Gloock-Regular.ttf", size)
        lines = wrap(d, title, tf, maxw, 3)
        if len(lines) <= 2 or size <= 64:
            break
        size -= 6
    y = 150
    for ln in lines:
        d.text((x, y), ln, font=tf, fill=INK)
        y += round(size * 1.08)
    if sub:
        sf = font("Figtree.ttf", 30, 400)
        for ln in wrap(d, sub, sf, maxw, 3 if len(lines) < 3 else 2):
            y += 4
            d.text((x, y + 14), ln, font=sf, fill=MUTED)
            y += 40
    d.text((x, H - 78), "History of Wales", font=font("Gloock-Regular.ttf", 34), fill=INK)
    d.text((x + 262, H - 70), "historyofwales.cymru", font=font("Figtree.ttf", 24, 500), fill=MUTED)
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
