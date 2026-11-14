"""Real land heights for a court in 3D (court-<id>.html): writes tools/court-<id>-land.js for the scene to import.

    python3 tools/bake_court.py sycharth 52.824498 -3.180842 [size_m=1400] [n=141]

Downloads the free Terrarium height tiles (AWS open data: s3.amazonaws.com/elevation-tiles-prod, zoom 15, about 3 m
per pixel, from SRTM and other public surveys), and samples an n x n grid, size metres square, centred on the court,
north up. Heights are stored in decimetres above the lowest point, as base64 16-bit numbers, so the scene can rebuild
the land exactly and the walker's eye can follow it. The scene adds the man-made earthworks (motte, moat, bailey)
itself, because the survey is too coarse to show them.
"""
import base64
import io
import math
import os
import sys
import urllib.request

import numpy as np
from PIL import Image

Z = 15


def tile(x, y, cache={}):
    if (x, y) not in cache:
        u = f"https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{Z}/{x}/{y}.png"
        im = np.asarray(Image.open(io.BytesIO(urllib.request.urlopen(u, timeout=60).read())).convert("RGB")).astype(float)
        cache[(x, y)] = im[..., 0] * 256 + im[..., 1] + im[..., 2] / 256 - 32768
    return cache[(x, y)]


def height(lat, lon):
    n = 2 ** Z
    fx = (lon + 180) / 360 * n * 256
    fy = (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n * 256
    x0, y0 = math.floor(fx - .5), math.floor(fy - .5)
    tx, ty = fx - .5 - x0, fy - .5 - y0

    def px(x, y):
        return tile(x // 256, y // 256)[y % 256, x % 256]
    return (px(x0, y0) * (1 - tx) * (1 - ty) + px(x0 + 1, y0) * tx * (1 - ty) + px(x0, y0 + 1) * (1 - tx) * ty + px(x0 + 1, y0 + 1) * tx * ty)


def main():
    cid, lat, lon = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    size = float(sys.argv[4]) if len(sys.argv) > 4 else 1400
    n = int(sys.argv[5]) if len(sys.argv) > 5 else 141
    mlat = 111320.0
    mlon = 111320.0 * math.cos(math.radians(lat))
    H = np.zeros((n, n))
    for j in range(n):          # rows: z, north (-) to south (+)
        for i in range(n):      # columns: x, west (-) to east (+)
            x = -size / 2 + size * i / (n - 1)
            z = -size / 2 + size * j / (n - 1)
            H[j, i] = height(lat - z / mlat, lon + x / mlon)
    base = H.min()
    dm = np.round((H - base) * 10).astype("<u2")
    b64 = base64.b64encode(dm.tobytes()).decode()
    out = os.path.join(os.path.dirname(__file__), f"court-{cid}-land.js")
    with open(out, "w") as f:
        f.write(f"/* Made by tools/bake_court.py {cid} {lat} {lon} {size:g} {n}: real heights (Terrarium tiles), decimetres above {base:.1f} m. Do not edit. */\n")
        f.write(f"export const LAND = {{ size: {size:g}, n: {n}, base: {base:.1f}, h: \"{b64}\" }};\n")
    print(out, f"{len(b64) / 1024:.0f} KB, heights {base:.1f} to {H.max():.1f} m, centre {H[n // 2, n // 2] - base:.1f} m above base")


if __name__ == "__main__":
    main()
