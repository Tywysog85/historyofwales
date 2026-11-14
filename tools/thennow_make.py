"""Make the then and now pictures (src/static/thennow/<id>-then.webp, -now.webp and -s copies) from the research downloads.

    python3 tools/thennow_make.py tools/thennow_align.json [id ...]

tools/thennow_align.json gives, for each pair id:
    then, now      the full-size downloads (paths from the repo root, e.g. _research/thennow3/full/4.jpg)
    then_box       optional [x0, y0, x1, y1] as fractions of the old picture: the part to use (cuts off an engraving's title panel).
    trim           optional true: then cut off any plain border left round the old picture (paper, black mount) with trim().
                   Only where needed: a pale, even sky can look like a border to it (it never cuts more than 6% a side).
    now_box        optional, the same for today's photo
    mode           "auto": find the same stones in both pictures (OpenCV SIFT) and line the old picture up on today's
                   (scale, turn and shift only), then cut the largest frame both cover. Works for the 1890s photochroms.
                   "box": just cut then_box and now_box, both to the shape of then_box (for engravings, where the artist's
                   view never lines up exactly). Falls back to "box" when "auto" finds too few matches.
    ar             optional width / height for the result (default: whatever the frame gives, kept between 1.2 and 2.4)
    zoom           optional, > 1 cuts in further around the middle after lining up
It prints each pair's shape (ar) for src/thennow.py. Needs Pillow, NumPy and opencv-python-headless (pip install).
"""
import json
import os
import sys

import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "src", "static", "thennow")
W, WS = 1200, 640


def crop_frac(im, box):
    if not box:
        return im
    w, h = im.size
    return im.crop((round(box[0] * w), round(box[1] * h), round(box[2] * w), round(box[3] * h)))


def trim(im, tol=10, most=0.06):
    """Cut off the plain border of a scanned print (white paper, black mount or grey card) round the picture."""
    a = np.asarray(im.convert("L"), dtype=np.float32)
    h, w = a.shape

    def plain(v):
        return v.std() < tol

    t, b, l, r = 0, h, 0, w
    while t < h * most and plain(a[t, l:r]):
        t += 1
    while h - b < h * most and plain(a[b - 1, l:r]):
        b -= 1
    while l < w * most and plain(a[t:b, l]):
        l += 1
    while w - r < w * most and plain(a[t:b, r - 1]):
        r -= 1
    pad = 4 if (t, b, l, r) != (0, h, 0, w) else 0  # a little more, past the soft edge of the border
    return im.crop((min(l + pad, w), min(t + pad, h), max(r - pad, 0), max(b - pad, 0)))


def fit_ar(w, h, ar, cx=.5, cy=.5):
    """The largest box of shape ar inside w x h, centred on (cx, cy) as far as it can be."""
    if w / h > ar:
        bw, bh = h * ar, h
    else:
        bw, bh = w, w / ar
    x0 = min(max(cx * w - bw / 2, 0), w - bw)
    y0 = min(max(cy * h - bh / 2, 0), h - bh)
    return x0, y0, x0 + bw, y0 + bh


def zoom_box(b, z):
    if not z or z <= 1:
        return b
    cx, cy, bw, bh = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2, (b[2] - b[0]) / z, (b[3] - b[1]) / z
    return cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2


def auto(old, new, spec):
    import cv2
    a = cv2.cvtColor(np.array(old), cv2.COLOR_RGB2GRAY)
    b = cv2.cvtColor(np.array(new), cv2.COLOR_RGB2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    a, b = clahe.apply(a), clahe.apply(b)
    sift = cv2.SIFT_create(nfeatures=6000)
    ka, da = sift.detectAndCompute(a, None)
    kb, db = sift.detectAndCompute(b, None)
    if da is None or db is None:
        return None
    m = cv2.BFMatcher().knnMatch(da, db, k=2)
    good = [x for x, y in (p for p in m if len(p) == 2) if x.distance < 0.75 * y.distance]
    if len(good) < 12:
        return None
    src = np.float32([ka[x.queryIdx].pt for x in good])
    dst = np.float32([kb[x.trainIdx].pt for x in good])
    M, inl = cv2.estimateAffinePartial2D(src, dst, method=cv2.RANSAC, ransacReprojThreshold=6.0, maxIters=5000, confidence=0.995)
    n = int(inl.sum()) if inl is not None else 0
    if M is None or n < spec.get("min_inliers", 15):
        return None
    s = float(np.hypot(M[0, 0], M[1, 0]))
    if not (0.15 < s < 6):
        return None
    # put the old picture into today's frame, and find where both have picture
    nw, nh = new.size
    warped = cv2.warpAffine(np.array(old), M, (nw, nh), flags=cv2.INTER_CUBIC, borderValue=(0, 0, 0))
    mask = cv2.warpAffine(np.full(a.shape, 255, np.uint8), M, (nw, nh), flags=cv2.INTER_NEAREST)
    ys, xs = np.where(mask > 0)
    # largest axis-aligned box inside the (turned) footprint: shrink the bounding box until it is all inside
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    for _ in range(400):
        sub = mask[y0:y1, x0:x1]
        if sub.size and sub.min() > 0:
            break
        x0, x1, y0, y1 = x0 + 2, x1 - 2, y0 + 2, y1 - 2
    return Image.fromarray(warped), (x0, y0, x1, y1), n, s


def make(pid, spec):
    old = crop_frac(Image.open(os.path.join(ROOT, spec["then"])).convert("RGB"), spec.get("then_box"))
    if spec.get("trim"):
        old = trim(old)
    new = crop_frac(Image.open(os.path.join(ROOT, spec["now"])).convert("RGB"), spec.get("now_box"))
    how = "box"
    if spec.get("mode") == "auto":
        r = auto(old, new, spec)
        if r:
            warped, (x0, y0, x1, y1), n, s = r
            ar = spec.get("ar") or min(1.9, max(1.2, (x1 - x0) / (y1 - y0)))
            bx = fit_ar(x1 - x0, y1 - y0, ar)
            bx = zoom_box((bx[0] + x0, bx[1] + y0, bx[2] + x0, bx[3] + y0), spec.get("zoom"))
            old, new = warped.crop(tuple(round(v) for v in bx)), new.crop(tuple(round(v) for v in bx))
            how = f"auto ({n} matches, scale {s:.2f})"
        else:
            how = "box (auto found too few matches)"
    if not how.startswith("auto"):
        ar = spec.get("ar") or min(2.4, max(1.2, old.width / old.height))
        bo = zoom_box(fit_ar(old.width, old.height, ar, *spec.get("then_at", (.5, .5))), spec.get("zoom"))
        bn = zoom_box(fit_ar(new.width, new.height, ar, *spec.get("now_at", (.5, .5))), spec.get("now_zoom"))
        old, new = old.crop(tuple(round(v) for v in bo)), new.crop(tuple(round(v) for v in bn))
    h = round(W / ar)
    os.makedirs(OUT, exist_ok=True)
    for kind, im in (("then", old), ("now", new)):
        big = im.resize((W, h), Image.LANCZOS)
        big.save(os.path.join(OUT, f"{pid}-{kind}.webp"), quality=80, method=6)
        big.resize((WS, round(WS / ar)), Image.LANCZOS).save(os.path.join(OUT, f"{pid}-{kind}-s.webp"), quality=78, method=6)
    print(f"{pid}: ar={ar:.4f}  {how}  (old {old.size[0]}x{old.size[1]} px used)")
    return ar


def main():
    specs = json.load(open(sys.argv[1], encoding="utf-8"))
    only = set(sys.argv[2:])
    for pid, spec in specs.items():
        if not only or pid in only:
            make(pid, spec)


if __name__ == "__main__":
    main()
