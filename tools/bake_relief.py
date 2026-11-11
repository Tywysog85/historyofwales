"""Bake the shaded-relief picture of Wales used under the castles map (castles.html).

    python3 tools/bake_relief.py /tmp/relief      (tile cache folder)

Heights: Terrarium elevation tiles (Mapzen / AWS open data, s3.amazonaws.com/elevation-tiles-prod).
The picture is drawn in the same projection as src/geo/map.json (x = (lon-minx)*k*sc, y = (maxy-lat)*sc,
600 x 671 units), so the castle dots, the county lines and the picture line up.
Writes src/static/relief-1200.webp and src/static/relief-3600.webp.
"""
import json, math, os, re, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cache = sys.argv[1] if len(sys.argv) > 1 else "/tmp/relief"
os.makedirs(cache, exist_ok=True)
G = json.load(open(os.path.join(ROOT, "src", "geo", "map.json")))
sc, k, minx, maxy, W, H = G["sc"], G["k"], G["minx"], G["maxy"], G["W"], G["H"]
Z = 11
S = 6                      # 600 units -> 3600 pixels
PW, PH = int(W * S), int(math.ceil(H * S))


def tile_xy(lat, lon):
    n = 2 ** Z
    return (lon + 180) / 360 * n, (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n


# the picture's corners in lat/lon (a little margin all round)
lon0, lon1 = minx, minx + W / (k * sc)
lat1, lat0 = maxy, maxy - H / sc
tx0, ty0 = [int(v) for v in tile_xy(lat1, lon0)]
tx1, ty1 = [int(v) for v in tile_xy(lat0, lon1)]
mos = np.zeros(((ty1 - ty0 + 1) * 256, (tx1 - tx0 + 1) * 256), np.float32)
for ty in range(ty0, ty1 + 1):
    for tx in range(tx0, tx1 + 1):
        f = f"{cache}/{Z}_{tx}_{ty}.png"
        if not os.path.exists(f):
            subprocess.run(["curl", "-sf", "--retry", "4", "-o", f, f"https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{Z}/{tx}/{ty}.png"], check=True)
        a = np.asarray(Image.open(f).convert("RGB")).astype(np.float32)
        mos[(ty - ty0) * 256:(ty - ty0 + 1) * 256, (tx - tx0) * 256:(tx - tx0 + 1) * 256] = a[:, :, 0] * 256 + a[:, :, 1] + a[:, :, 2] / 256 - 32768

# resample into the map projection (bilinear)
xs = (np.arange(PW) + .5) / S
ys = (np.arange(PH) + .5) / S
lon = minx + xs / (k * sc)
lat = maxy - ys / sc
n = 2 ** Z
mx = ((lon + 180) / 360 * n - tx0) * 256
my = ((1 - np.arcsinh(np.tan(np.radians(lat))) / math.pi) / 2 * n - ty0) * 256
MX, MY = np.meshgrid(mx, my)
x0 = np.clip(np.floor(MX).astype(int), 0, mos.shape[1] - 2); y0 = np.clip(np.floor(MY).astype(int), 0, mos.shape[0] - 2)
fx = MX - x0; fy = MY - y0
h = (mos[y0, x0] * (1 - fx) * (1 - fy) + mos[y0, x0 + 1] * fx * (1 - fy) + mos[y0 + 1, x0] * (1 - fx) * fy + mos[y0 + 1, x0 + 1] * fx * fy)

# Wales mask from the outline in map.json
mask = Image.new("L", (PW, PH), 0)
dr = ImageDraw.Draw(mask)
for sub in re.split(r"(?=M)", G["outline"]):
    pts = [(float(a) * S, float(b) * S) for a, b in re.findall(r"(-?[\d.]+)[ ,](-?[\d.]+)", sub)]
    if len(pts) > 2:
        dr.polygon(pts, fill=255)
# The outline is simplified, so along the sea coasts the coastline is taken from the heights instead:
# there the mask is widened; along the land border with England the outline is used as it is.
wide = np.asarray(mask.filter(ImageFilter.MaxFilter(31))).astype(np.float32) / 255
raw = np.asarray(mask).astype(np.float32) / 255
LON, LAT = np.meshgrid(lon, lat)
border = (LON > -3.35) & (LAT > 51.62) & (LAT < 53.22)
wal = np.where(border, raw, wide)
wal = np.where(LON < -3.9, 1.0, wal)        # every island west of 3.9 W is Welsh (Enlli, Sgomer, Ynys Dewi...)
wal = np.asarray(Image.fromarray((wal * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))).astype(np.float32) / 255

# hillshade (light from the north-west), metres per pixel ~ 1000*... in projected units
mpp = 1000 * (1 / sc) * 111.32 / S        # one pixel in metres (north-south)
hl = np.maximum(h, 0)
gy, gx = np.gradient(hl, mpp)
ex = 2.2                                   # exaggeration
slope = np.arctan(ex * np.hypot(gx, gy))
aspect = np.arctan2(-gx, gy)
az, alt = math.radians(315), math.radians(42)
shade = np.sin(alt) * np.cos(slope) + np.cos(alt) * np.sin(slope) * np.cos(az - aspect)
shade = np.clip(shade, 0, 1)

land = (h > 0.5).astype(np.float32)
land = np.asarray(Image.fromarray((land * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.1))).astype(np.float32) / 255

# colours (night palette of the site): low green-slate, uplands warm moorland, summits pale
t = np.clip(hl / 950, 0, 1) ** .8
low = np.array([38, 52, 50], np.float32); mid = np.array([74, 72, 58], np.float32); top = np.array([168, 160, 140], np.float32)
col = np.where(t[..., None] < .45, low + (mid - low) * (t[..., None] / .45), mid + (top - mid) * ((t[..., None] - .45) / .55))
lit = (.45 + .95 * shade)[..., None]
landc = np.clip(col * lit, 0, 255)
# England and Ireland: same relief, much dimmer and greyer
grey = landc.mean(axis=2, keepdims=True)
other = grey * .42 + 10
landc = landc * wal[..., None] + other * (1 - wal[..., None])
# sea: deep blue-black, a touch lighter in the shallows
depth = np.clip(-h / 120, 0, 1)[..., None]
sea = np.array([22, 34, 52], np.float32) * (1 - depth) + np.array([12, 17, 28], np.float32) * depth
img = landc * land[..., None] + sea * (1 - land[..., None])
# faint coast glow
edge = np.asarray(Image.fromarray((land * 255).astype(np.uint8)).filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(1.5))).astype(np.float32) / 255
img = np.clip(img + edge[..., None] * np.array([40, 50, 60]) * wal[..., None], 0, 255).astype(np.uint8)
out = Image.fromarray(img, "RGB")
out.save(os.path.join(ROOT, "src", "static", "relief-3600.webp"), quality=70, method=6)
out.resize((PW // 3, PH // 3), Image.LANCZOS).save(os.path.join(ROOT, "src", "static", "relief-1200.webp"), quality=78, method=6)
print("wrote", PW, PH, "height range", float(h.min()), float(h.max()))
