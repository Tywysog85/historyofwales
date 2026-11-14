"""Bake the real land around Llys Rhosyr for the 3D court (tools/llys3d.src.js).

Downloads Terrarium height tiles (Mapzen / AWS open data, z12, about 23 m a pixel) for a square 64 km across,
centred on the court (Coflein grid reference SH 41928 65359 = 53.16182 N, 4.36583 W), and writes to src/static/:
  llys-h.png      heights, 384 x 384 (167 m apart): metres = (R*256 + G) / 20 - 50
  llys-n.webp     the shape of the land as light sees it (object-space normals), 2048 x 2048; llys-n-m.webp 1024 for phones
  llys-c.webp     the colour of the land (sea floor, shore sand, fields, heather, scree, crag), with the shadows the
                  ridges cast for the scene's sun baked in, 1024 x 1024; llys-c-m.webp 512 for phones
The scene's x runs east and z south, in metres, with the court at 0, 0. Row 0 of each picture is the north edge.
SUN must match SUN in tools/llys3d.src.js.
usage: python3 tools/bake_rhosyr.py <folder for downloaded tiles>
"""
import math, os, subprocess, sys
import numpy as np
from PIL import Image

LAT0, LON0 = 53.16182, -4.36583
HALF = 32000.0                      # metres from the court to each edge
SUN = (228.0, 17.0)                 # azimuth (degrees from north, clockwise) and height of the sun
Z = 12
cache = sys.argv[1]
OUT = os.path.join(os.path.dirname(__file__), "..", "src", "static")

def tile_xy(lat, lon):
    n = 2 ** Z
    return (lon + 180) / 360 * n, (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n

R_E = 6371000.0
dlat = math.degrees(HALF / R_E); dlon = math.degrees(HALF / (R_E * math.cos(math.radians(LAT0))))
x0, y0 = tile_xy(LAT0 + dlat * 1.02, LON0 - dlon * 1.02); x1, y1 = tile_xy(LAT0 - dlat * 1.02, LON0 + dlon * 1.02)
tx0, ty0, tx1, ty1 = int(x0), int(y0), int(x1), int(y1)
big = np.zeros(((ty1 - ty0 + 1) * 256, (tx1 - tx0 + 1) * 256), np.float32)
for ty in range(ty0, ty1 + 1):
    for tx in range(tx0, tx1 + 1):
        f = f"{cache}/{Z}_{tx}_{ty}.png"
        if not os.path.exists(f):
            subprocess.run(["curl", "-sf", "-o", f, f"https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{Z}/{tx}/{ty}.png"], check=True)
        a = np.asarray(Image.open(f).convert("RGB")).astype(np.float32)
        big[(ty - ty0) * 256:(ty - ty0 + 1) * 256, (tx - tx0) * 256:(tx - tx0 + 1) * 256] = a[:, :, 0] * 256 + a[:, :, 1] + a[:, :, 2] / 256 - 32768

def sample(N):
    """heights on an N x N grid in scene metres (row 0 = north)"""
    s = (np.arange(N) + .5) / N * 2 * HALF - HALF
    X, Zs = np.meshgrid(s, s)                       # x east, z south
    lat = LAT0 - np.degrees(Zs / R_E); lon = LON0 + np.degrees(X / (R_E * np.cos(np.radians(LAT0))))
    n = 2 ** Z
    px = ((lon + 180) / 360 * n - tx0) * 256 - .5
    py = ((1 - np.arcsinh(np.tan(np.radians(lat))) / np.pi) / 2 * n - ty0) * 256 - .5
    i0 = np.floor(px).astype(int); j0 = np.floor(py).astype(int); fx = px - i0; fy = py - j0
    g = lambda j, i: big[np.clip(j, 0, big.shape[0] - 1), np.clip(i, 0, big.shape[1] - 1)]
    return (g(j0, i0) * (1 - fx) * (1 - fy) + g(j0, i0 + 1) * fx * (1 - fy) + g(j0 + 1, i0) * (1 - fx) * fy + g(j0 + 1, i0 + 1) * fx * fy), X, Zs

def blur(a, r):
    n = int(math.ceil(r * 3)); k = np.exp(-np.arange(-n, n + 1) ** 2 / (2 * r * r)); k /= k.sum()
    a = np.apply_along_axis(lambda v: np.convolve(np.pad(v, len(k) // 2, mode="edge"), k, "valid"), 0, a)
    return np.apply_along_axis(lambda v: np.convolve(np.pad(v, len(k) // 2, mode="edge"), k, "valid"), 1, a)

# ---- heights for the mesh ----
N = 384
# each mesh point is the mean of the 4 x 4 finer samples around it, except that water wins: if any of them is sea,
# the point takes the lowest, so narrow water like the Menai Strait still shows from a distance
hf = sample(N * 4)[0].reshape(N, 4, N, 4)
h = np.where(hf.min(axis=(1, 3)) < -.5, np.minimum(hf.min(axis=(1, 3)) * .5, hf.mean(axis=(1, 3))), hf.mean(axis=(1, 3)))

c = sample(2049)[0]; print("height at the court:", c[1024, 1024], "max", c.max(), "min", c.min())   # H0 in tools/llys3d.src.js
v = np.clip(np.round((h + 50) * 20), 0, 65535).astype(np.uint32)
rgb = np.stack([(v >> 8) & 255, v & 255, np.zeros_like(v)], -1).astype(np.uint8)
Image.fromarray(rgb).save(os.path.join(OUT, "llys-h.png"), optimize=True)

# ---- normals and colour, from a finer sample ----
M = 2048
H, X, Zs = sample(M)
H = np.maximum(H, -30)
d = 2 * HALF / M
gx = (np.roll(H, -1, 1) - np.roll(H, 1, 1)) / (2 * d); gz = (np.roll(H, -1, 0) - np.roll(H, 1, 0)) / (2 * d)
nrm = np.stack([-gx, np.ones_like(H), -gz], -1); nrm /= np.linalg.norm(nrm, axis=-1, keepdims=True)
# object-space normal map: x east, y up, z south. three.js reads rgb = n * .5 + .5, with v running up the picture,
# and the mesh's uv has v = 1 at the north edge, so row 0 (north) is the top of the picture: no flip needed.
enc = ((nrm * .5 + .5) * 255).round().astype(np.uint8)
for size, name in ((2048, "llys-n.webp"), (1024, "llys-n-m.webp")):
    Image.fromarray(enc).resize((size, size), Image.LANCZOS).save(os.path.join(OUT, name), quality=82, method=6)

slope = np.degrees(np.arccos(nrm[..., 1]))
rng = np.random.default_rng(7)
noise = blur(rng.standard_normal((M, M)).astype(np.float32), 3) * 3 + blur(rng.standard_normal((M, M)).astype(np.float32), 12) * 6
def col(hexs): return np.array([int(hexs[i:i + 2], 16) for i in (0, 2, 4)], np.float32) / 255
C = np.zeros((M, M, 3), np.float32)
lerp = lambda a, b, t: a * (1 - t[..., None]) + b * t[..., None]
st = lambda a, b, x: np.clip((x - a) / (b - a), 0, 1) ** 2 * (3 - 2 * np.clip((x - a) / (b - a), 0, 1))
field = lerp(col("5f7d3a")[None, None].repeat(M, 0).repeat(M, 1), col("7c8f45"), st(-1, 1, noise))
moor = lerp(col("6c6a3c")[None, None].repeat(M, 0).repeat(M, 1), col("5b4a3c"), st(-1, 1.5, noise))   # bracken, heather
C = lerp(field, moor, st(140, 330, H + noise * 8))
C = lerp(C, col("7b7768"), st(24, 38, slope + noise))              # scree
C = lerp(C, col("6a6a66"), st(34, 46, slope + noise * .6))         # crag
C = lerp(C, col("d6c69c"), st(4, .5, H) * (1 - st(8, 14, slope)))  # shore sand
# the dunes of Niwbwrch (Newborough Warren) and Aberffraw: low ground close to the sea, south and west of the court
sea = (H < 0).astype(np.float32); near_sea = np.clip(blur(sea, 40) * 6, 0, 1)
dunes = near_sea * st(26, 10, H) * st(-.5, 2, H) * (1 - st(10, 18, slope)) * st(.2, 1.2, noise * .3 + 1)
C = lerp(C, col("cdbb8c"), np.clip(dunes, 0, 1) * .85)
C = lerp(C, col("b9a982"), st(0, -4, H))                           # wet sand and sea floor (seen through shallow water)
# shadows the ridges cast for the sun: march toward the sun over the heights
az, el = math.radians(SUN[0]), math.radians(SUN[1])
sx, sz = math.sin(az), -math.cos(az)                               # toward the sun, in x east / z south
tan_e = math.tan(el)
lit = np.ones((M, M), np.float32)
Hs = H.copy()
for k in range(1, 260):
    dist = k * d * 1.5
    sh = np.roll(np.roll(Hs, -int(round(sz * k * 1.5)), 0), -int(round(sx * k * 1.5)), 1)
    lit = np.minimum(lit, np.clip(1 - (sh - (Hs + dist * tan_e)) / 25, 0, 1))
lit = blur(lit, 2.5)
C *= (.62 + .38 * lit)[..., None]
C8 = (np.clip(C, 0, 1) ** (1 / 1) * 255).round().astype(np.uint8)
for size, name in ((1024, "llys-c.webp"), (512, "llys-c-m.webp")):
    Image.fromarray(C8).resize((size, size), Image.LANCZOS).save(os.path.join(OUT, name), quality=80, method=6)
for f in ("llys-h.png", "llys-n.webp", "llys-n-m.webp", "llys-c.webp", "llys-c-m.webp"):
    print(f, os.path.getsize(os.path.join(OUT, f)))
