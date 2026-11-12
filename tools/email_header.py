"""Draws the picture at the top of the weekly email: src/static/email/head.jpg (1200 x 440, shown at 600 x 220).

It reuses the night sky, moon and hills of the share picture (src/static/og.png) and writes the email's name over it in
Gloock, with the Welsh name under it in Figtree. Run it again only if the wording or look should change:
    python3 tools/email_header.py
The file is committed, so the email never depends on Pillow being installed.
"""
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "tools", "fonts")
OUT = os.path.join(ROOT, "src", "static", "email", "head.jpg")
W, H = 1200, 440
INK, GOLD, RED, MUTED = (236, 233, 225), (232, 198, 90), (226, 69, 61), (176, 182, 196)


def main():
    import math, random
    rnd = random.Random(1282)                      # same stars every time
    im = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(im)
    for y in range(H):                             # night sky, darkest at the top
        t = y / H
        d.line([(0, y), (W, y)], fill=(int(14 + 14 * t), int(17 + 15 * t), int(24 + 22 * t)))
    glow = Image.new("L", (W, H), 0)               # a warm red glow behind the moon, as on og.png
    gd = ImageDraw.Draw(glow)
    for r in range(330, 0, -6):
        gd.ellipse((930 - r, 150 - r, 930 + r, 150 + r), fill=int(160 * (1 - r / 330) ** 1.6))
    im.paste(Image.new("RGB", (W, H), (120, 36, 40)), (0, 0), glow)
    d = ImageDraw.Draw(im)
    for _ in range(140):
        x, y = rnd.randrange(W), rnd.randrange(300)
        b = rnd.randrange(110, 230)
        d.point((x, y), fill=(b, b, b + 10))
        if rnd.random() < .12:
            d.ellipse((x - 1, y - 1, x + 1, y + 1), fill=(b, b, b + 10))
    d.ellipse((870, 90, 990, 210), fill=(232, 216, 196))           # the moon
    def hills(base, amp, waves, colour, seed):
        r = random.Random(seed)
        ph = [r.random() * 6.3 for _ in waves]
        pts = [(x, base - sum(a * math.sin(x / w + p) for a, w, p in zip(amp, waves, ph))) for x in range(0, W + 8, 8)]
        d.polygon(pts + [(W, H), (0, H)], fill=colour)
    hills(352, (26, 12), (190, 70), (35, 41, 58), 1)
    hills(382, (20, 9), (150, 55), (28, 33, 47), 2)
    hills(412, (14, 7), (120, 45), (21, 25, 36), 3)
    d = ImageDraw.Draw(im)
    mono = ImageFont.truetype(os.path.join(FONTS, "Figtree.ttf"), 26)
    try:
        mono.set_variation_by_axes([700])
    except Exception:
        pass
    big = ImageFont.truetype(os.path.join(FONTS, "Gloock-Regular.ttf"), 92)
    sub = ImageFont.truetype(os.path.join(FONTS, "Figtree.ttf"), 34)
    x = 72
    d.rectangle((x, 62, x + 56, 68), fill=GOLD)
    d.text((x, 86), "HANES CYMRU  ·  HISTORY OF WALES", font=mono, fill=GOLD)
    d.text((x, 128), "This week in", font=big, fill=INK)
    w1 = d.textlength("Welsh ", font=big)
    d.text((x, 222), "Welsh ", font=big, fill=RED)
    d.text((x + w1, 222), "history", font=big, fill=INK)
    d.text((x + 2, 336), "Yr wythnos hon yn hanes Cymru", font=sub, fill=MUTED)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    im.save(OUT, "JPEG", quality=86, optimize=True, progressive=True)
    print("Wrote", OUT, os.path.getsize(OUT) // 1024, "KB")


if __name__ == "__main__":
    main()
