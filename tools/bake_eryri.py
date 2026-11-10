"""Bake the Yr Wyddfa height data into the three files the 3D scene reads.

    python3 -I tools/bake_eryri.py <dir with h.npy> <out dir> [height scale, 1.3]

Writes eryri-h.png (heights), eryri-c.webp (colour, with the moon's shadows and
the shade of hollows baked in) and eryri-n.webp (fine relief for the light).

What makes it read as a real mountain rather than a smooth model:
  * gullies carved where water would run (flow accumulation on the real heights)
  * the crags themselves come from a photograph of rock laid on the steep ground
    by the scene (tools/land3d.src.js), so this bake keeps the steep ground plain
  * colour laid by what the ground is: grass and heather on gentle ground, scree
    under the crags, bare rock where it is steep, snow lying on ledges, in
    gullies and on the high gentle ground, never in soft blobs
  * shadows cast by the ridges from where the moon stands in the scene
"""
import sys, numpy as np
from PIL import Image
dem, out = sys.argv[1], sys.argv[2]
VE = float(sys.argv[3]) if len(sys.argv) > 3 else 1.3
T = 2048; N = 900; KM = N * 11.4816; cell = KM / T; M = 512
LIGHT = np.array([-0.445, 0.35, -0.82])  # x, up, z: the same as moonL in tools/land3d.src.js
h = np.load(dem + '/h.npy'); c = h[190:190 + N, 150:150 + N]
def resize(a, n, how=Image.BICUBIC): return np.asarray(Image.fromarray(a.astype(np.float32), mode='F').resize((n, n), how)).astype(np.float64)
def blur(a, s):
    pad = 64; b = np.pad(a, pad, mode='reflect'); fy = np.fft.fftfreq(b.shape[0])[:, None]; fx = np.fft.fftfreq(b.shape[1])[None, :]
    return np.real(np.fft.ifft2(np.fft.fft2(b) * np.exp(-2 * (np.pi * s) ** 2 * (fx ** 2 + fy ** 2))))[pad:-pad, pad:-pad]
rng = np.random.default_rng(5)
FY = np.fft.fftfreq(T)[:, None] * T; FX = np.fft.fftfreq(T)[None, :] * T; FR = np.hypot(FX, FY); FR[0, 0] = 1
def spec(lo, hi, beta=1.0):
    w = rng.normal(size=(T, T)); F = np.fft.fft2(w) * np.where((FR >= lo) & (FR <= hi), FR ** -beta, 0)
    a = np.real(np.fft.ifft2(F)); a = (a - a.mean()) / a.std(); return np.clip(a * 0.22 + 0.5, 0, 1)
def fbm(n0, octaves, ridged=False, gain=0.5):
    a = np.zeros((T, T)); amp = 1; tot = 0
    for o in range(octaves):
        v = spec(n0 * 2 ** o * 0.7, n0 * 2 ** o * 1.5, 0)
        if ridged: v = 1 - np.abs(2 * v - 1); v = v * v
        a += v * amp; tot += amp; amp *= gain
    return a / tot
def ss(a, lo, hi): k = np.clip((a - lo) / (hi - lo), 0, 1); return k * k * (3 - 2 * k)
def lerp(a, b, k): return a + (b - a) * k[..., None]

base = blur(resize(c, T), 3.2)
water = ((np.abs(base - 432.2) < 1.0) | (np.abs(base - 604.3) < 1.0))
gy, gx = np.gradient(base, cell); water &= (np.hypot(gx, gy) < 0.01)

# ---- where water runs: flow accumulation on a half-size copy, then gullies cut along it
F = 1024; fb = resize(base, F, Image.BILINEAR) + (resize(fbm(24, 4), F, Image.BILINEAR) - 0.5) * 26   # the noise makes the streams wander: without it they run in ruled lines
pad = np.pad(fb, 1, mode='edge'); best = np.zeros((F, F), np.int64) - 1; drop = np.zeros((F, F))
idx = np.arange(F * F).reshape(F, F)
for dy in (-1, 0, 1):
    for dx in (-1, 0, 1):
        if dy == 0 and dx == 0: continue
        nb = pad[1 + dy:1 + dy + F, 1 + dx:1 + dx + F]; d = (fb - nb) / np.hypot(dy, dx)
        yy = np.clip(np.arange(F)[:, None] + dy, 0, F - 1); xx = np.clip(np.arange(F)[None, :] + dx, 0, F - 1)
        better = d > drop; drop = np.where(better, d, drop); best = np.where(better, yy * F + xx, best)
order = np.argsort(fb.ravel())[::-1].tolist(); recv = best.ravel().tolist(); acc = [1.0] * (F * F)
for i in order:
    r = recv[i]
    if r >= 0: acc[r] += acc[i]
flow = np.log(np.array(acc).reshape(F, F))
gul = resize(ss(flow, 4.6, 8.0), T, Image.BILINEAR)            # 0..1, only where a real stream gathers
gul = np.clip(blur(gul, 2.0) * 2.2, 0, 1)

sharp = base + 0.9 * (base - blur(base, 14)) + 0.5 * (base - blur(base, 40))
gy, gx = np.gradient(blur(base, 6), cell); slope = np.hypot(gx, gy)
st = ss(slope, 0.28, 0.75); hi = ss(base, 430, 800)
rid = fbm(20, 6, True, 0.55); soft = fbm(10, 5); warp = fbm(14, 4)
det = sharp + (rid - 0.3) * (10 + 70 * st * (0.35 + 0.65 * hi)) + (soft - 0.5) * 12
det -= gul * (5 + 24 * ss(slope, 0.12, 0.5))
det = np.where(water, base, det)

gy, gx = np.gradient(det * VE, cell); l = 1 / np.sqrt(gx * gx + gy * gy + 1); nx, ny, nz = -gx * l, l, -gy * l
Image.fromarray((np.stack([nx * .5 + .5, ny * .5 + .5, nz * .5 + .5], -1) * 255).clip(0, 255).astype(np.uint8)).save(out + '/eryri-n.webp', quality=84)
sl = 1 - ny  # fine slope: 0 flat, 1 vertical

# ---- shadows cast by the ridges, from where the moon stands
L = LIGHT / np.hypot(LIGHT[0], LIGHT[2]); hv = blur(det, 1.0) * VE; lit = np.ones((T, T))
far = int(1100 * VE / L[1] / cell)
for k in range(2, far, 2):
    ox = int(round(k * L[0])); oz = int(round(k * L[2]))
    src = np.roll(np.roll(hv, -oz, 0), -ox, 1)
    if ox > 0: src[:, -ox:] = 0
    if oz < 0: src[:-oz, :] = 0
    elif oz > 0: src[-oz:, :] = 0
    over = (src - (hv + k * cell * L[1])) / (k * cell * 0.06 + 6)   # soft edge that widens with distance
    lit = np.minimum(lit, 1 - np.clip(over, 0, 1))
lit = blur(lit, 1.5)
# ---- the shade of hollows
ao = np.clip(1 - (blur(det, 5) - det) / 26, 0.5, 1.12) * np.clip(1 - (blur(det, 40) - det) / 260, 0.6, 1.1)

# ---- colour, by what the ground is
f = fbm(96, 4); f2 = fbm(10, 4); f3 = fbm(320, 2); f4 = fbm(40, 3); strata = fbm(180, 2)
grass = lerp(np.array([0.060, 0.070, 0.030]), np.array([0.150, 0.125, 0.060]), ss(f2 + 0.5 * (f - 0.5), 0.35, 0.7))   # green hollows to bleached winter grass
grass = lerp(grass, np.array([0.050, 0.036, 0.034]), ss(f4, 0.55, 0.75) * 0.8)                                       # heather
grass = lerp(grass, np.array([0.030, 0.045, 0.022]), gul * 0.6)                                                      # rushes along the streams
scree = (0.120 + 0.07 * f + 0.05 * f3)[..., None] * np.array([1.04, 1.0, 0.97])
rock = (0.045 + 0.07 * f + 0.05 * strata + 0.02)[..., None] * np.array([1.0, 1.0, 1.05])
col = lerp(grass, scree, ss(sl + (f - 0.5) * 0.08, 0.10, 0.18) * ss(base + f2 * 150, 430, 640))
col = lerp(col, rock, ss(sl + (f3 - 0.5) * 0.06, 0.17, 0.27))
# snow lies where it can: high gentle ground, ledges and gullies; the steep rock stays bare
line = base + (f2 - 0.5) * 160 + (f - 0.5) * 50
sn = ss(line, 560, 700) * (1 - ss(sl - gul * 0.08 + (f - 0.5) * 0.08, 0.26, 0.42))
sn = np.maximum(sn, ss(line, 720, 860) * (1 - ss(sl + (f - 0.5) * 0.06, 0.40, 0.56)))
sn *= 0.7 + 0.3 * ss(f2 + f * 0.4, 0.4, 0.8) + 0.4 * ss(line, 760, 900)                                           # wind-scoured patches low down
sn = np.clip(sn, 0, 1)
col = lerp(col, np.array([0.80, 0.85, 0.93]), sn)
col *= (ao * (0.93 + 0.14 * f3 * (1 - sn)))[..., None]
col *= (0.32 + 0.68 * lit)[..., None] * np.where(lit[..., None] < 1, lerp(np.ones(3), np.array([0.82, 0.9, 1.12]), 1 - lit), 1)   # shadow is bluer
col = np.where(water[..., None], np.array([0.01, 0.018, 0.035]), col)
Image.fromarray((np.clip(col, 0, 1) ** (1 / 2.2) * 255).astype(np.uint8)).save(out + '/eryri-c.webp', quality=82)

rough = np.where(water, 0.12, 0.96 - 0.3 * sn)
hm = resize(blur(det, 2.0), M, Image.BILINEAR)
v = np.clip(hm * 56, 0, 65535).astype(np.uint16); rgb = np.zeros((M, M, 3), np.uint8); rgb[:, :, 0] = v >> 8; rgb[:, :, 1] = v & 255
rgb[:, :, 2] = np.asarray(Image.fromarray((rough * 255).astype(np.uint8)).resize((M, M), Image.BILINEAR))
Image.fromarray(rgb).save(out + '/eryri-h.png', optimize=True)
print('max', det.max(), 'water px', water.sum(), 'lit', lit.mean(), 'snow', sn.mean())
