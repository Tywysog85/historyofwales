"""Surfaces for the courts in 3D (court-<id>.html): oak, boards, bark, limewashed daub, rubble stone, slate, thatch,
rushes on the floor, grass and leaves, each a colour picture and a normal map (the little bumps that catch the light).

    python3 tools/make_court_textures.py

Everything is made here from noise, so there is nothing to license: the textures tile seamlessly because all the noise
is made by filtering random numbers in the frequency domain, which wraps round at the edges. Writes
src/static/court/tex/<name>.webp (1024 px) and <name>-s.webp (512 px, for phones), and <name>_n / <name>_n-s for the
normal maps. The engine (tools/court3d.src.js) loads them and draws with its own canvas textures until they come.
"""
import os

import numpy as np
from PIL import Image

OUT = os.path.join(os.path.dirname(__file__), "..", "src", "static", "court", "tex")
N = 1024
rng = np.random.default_rng(1403)


# ---------- tileable noise ----------
def fbm(n=N, beta=2.0, lo=1.0, stretch=(1.0, 1.0), seed=None):
    """Tileable noise with power falling as 1/f^beta; stretch makes it streaky (grain along x if stretch[0] < 1)."""
    r = np.random.default_rng(seed) if seed is not None else rng
    w = r.standard_normal((n, n))
    fy = np.fft.fftfreq(n)[:, None] * n * stretch[1]
    fx = np.fft.fftfreq(n)[None, :] * n * stretch[0]
    f = np.sqrt(fx ** 2 + fy ** 2)
    f[0, 0] = 1
    amp = 1 / np.maximum(f, lo) ** (beta / 2)
    amp[0, 0] = 0
    out = np.real(np.fft.ifft2(np.fft.fft2(w) * amp))
    return (out - out.mean()) / (out.std() + 1e-9)


def norm01(a):
    a = a - a.min()
    return a / (a.max() + 1e-9)


def voronoi(n, pts, aspect=(1.0, 1.0)):
    """Tileable nearest and second-nearest distance to a set of points (in 0..1), and the index of the nearest."""
    ys, xs = np.mgrid[0:n, 0:n] / n
    d1 = np.full((n, n), 9.0)
    d2 = np.full((n, n), 9.0)
    idx = np.zeros((n, n), int)
    for i, (px, py) in enumerate(pts):
        dx = np.abs(xs - px)
        dx = np.minimum(dx, 1 - dx) * aspect[0]
        dy = np.abs(ys - py)
        dy = np.minimum(dy, 1 - dy) * aspect[1]
        d = np.sqrt(dx * dx + dy * dy)
        closer = d < d1
        d2 = np.where(closer, d1, np.minimum(d2, d))
        idx = np.where(closer, i, idx)
        d1 = np.where(closer, d, d1)
    return d1, d2, idx


def blur(a, k=1):
    """A small tileable blur (k passes of a 3x3 box)."""
    for _ in range(k):
        a = (a + np.roll(a, 1, 0) + np.roll(a, -1, 0)) / 3
        a = (a + np.roll(a, 1, 1) + np.roll(a, -1, 1)) / 3
    return a


def normal_map(h, strength):
    """A tangent-space normal map from a height field (OpenGL way up: green is up the picture)."""
    dx = (np.roll(h, -1, 1) - np.roll(h, 1, 1)) * strength
    dy = (np.roll(h, 1, 0) - np.roll(h, -1, 0)) * strength
    nz = np.ones_like(h)
    L = np.sqrt(dx * dx + dy * dy + nz * nz)
    n = np.stack([-dx / L, -dy / L, nz / L], -1)
    return ((n * .5 + .5) * 255).clip(0, 255).astype(np.uint8)


def colour(t, stops):
    """Map 0..1 to a colour ramp: stops are [(t, (r, g, b)), ...]."""
    t = np.clip(t, 0, 1)
    out = np.zeros(t.shape + (3,))
    ts = [s[0] for s in stops]
    for c in range(3):
        out[..., c] = np.interp(t, ts, [s[1][c] for s in stops])
    return out


def save(name, rgb, h, strength):
    """Colour at 1024 (512 for phones), normal map at 512 (256 for phones): the bumps need less detail than the colour."""
    os.makedirs(OUT, exist_ok=True)
    im = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8), "RGB")
    im.save(os.path.join(OUT, f"{name}.webp"), quality=74, method=6)
    im.resize((N // 2, N // 2), Image.LANCZOS).save(os.path.join(OUT, f"{name}-s.webp"), quality=74, method=6)
    pool = lambda a: (a[::2, ::2] + a[1::2, ::2] + a[::2, 1::2] + a[1::2, 1::2]) / 4
    h2 = pool(blur(h, 1))
    Image.fromarray(normal_map(h2, strength / 2), "RGB").save(os.path.join(OUT, f"{name}_n.webp"), quality=80, method=6)
    Image.fromarray(normal_map(pool(h2), strength / 4), "RGB").save(os.path.join(OUT, f"{name}_n-s.webp"), quality=80, method=6)
    print(name)


ys, xs = np.mgrid[0:N, 0:N] / N


# ---------- oak: an adzed beam, the grain along the picture (x), 1 m per tile ----------
def oak():
    grain = fbm(beta=2.2, stretch=(1.0, .04))
    fine = fbm(beta=1.6, stretch=(1.0, .06))
    rays = fbm(beta=1.4, stretch=(1.0, .5))
    adze = fbm(beta=3.0, stretch=(1.0, .35))
    # checks: a few long splits along the grain
    checks = np.zeros((N, N))
    for _ in range(4):
        y0, x0, L, w = rng.random(), rng.random(), .25 + rng.random() * .6, .0015 + rng.random() * .002
        dy = np.abs(((ys - y0 + .5) % 1) - .5 + .004 * np.sin(xs * 9 + rng.random() * 6))
        dx = ((xs - x0) % 1)
        checks += np.where((dx < L), np.exp(-(dy / w) ** 2) * np.sin(np.pi * np.clip(dx / L, 0, 1)) ** .5, 0)
    h = .5 * adze + .25 * grain + .08 * fine - 1.2 * np.clip(checks, 0, 1)
    t = norm01(.55 * grain + .3 * fine + .25 * adze + .1 * rays) - .45 * np.clip(checks, 0, 1)
    rgb = colour(t, [(0, (58, 42, 28)), (.35, (92, 70, 48)), (.6, (118, 94, 68)), (.85, (140, 118, 90)), (1, (160, 140, 112))])
    save("oak", rgb, h, 3.0)


# ---------- boards: floor and deck planks across the picture, 6 to a tile (2 m) ----------
def boards():
    planks = 6
    row = np.floor(ys * planks)
    off = rng.random(planks)
    grain = fbm(beta=2.0, stretch=(1.0, .03))
    fine = fbm(beta=1.6, stretch=(1.0, .05))
    tone = off[row.astype(int)] - .5
    v = (ys * planks) % 1
    edge = np.minimum(v, 1 - v)
    groove = np.exp(-(edge / .018) ** 2)
    # butt joints at random places along each plank
    ends = np.zeros((N, N))
    for i in range(planks):
        for _ in range(2):
            x0 = rng.random()
            dxe = np.abs(((xs - x0 + .5) % 1) - .5)
            ends += np.where(row == i, np.exp(-(dxe / .0025) ** 2), 0)
    # nails: two by each joint and every so often
    nails = np.zeros((N, N))
    for i in range(planks):
        for k in range(5):
            cx, cy = (k + .5 + rng.random() * .2) / 5, (i + .5) / planks
            for s in (-.22, .22):
                d = np.hypot(((xs - cx + .5) % 1) - .5, ((ys - cy - s / planks + .5) % 1) - .5)
                nails += np.exp(-(d / .004) ** 2)
    h = .35 * grain + .12 * fine - 1.6 * np.clip(groove + ends, 0, 1) + .3 * tone + .4 * nails
    t = norm01(.5 * grain + .3 * fine) * .8 + .25 * tone - .55 * np.clip(groove + ends, 0, 1)
    rgb = colour(t, [(0, (52, 38, 26)), (.3, (96, 72, 48)), (.6, (128, 100, 70)), (1, (162, 132, 96))])
    rgb = rgb * (1 - .5 * np.clip(nails, 0, 1))[..., None] + np.array([40, 38, 36]) * .5 * np.clip(nails, 0, 1)[..., None]
    save("boards", rgb, h, 2.6)


# ---------- bark: the outside of a log, fissures running along it (y), for palisades and trunks ----------
def bark():
    pts = rng.random((180, 2))
    d1, d2, idx = voronoi(N, pts, aspect=(1.0, .28))
    ridge = np.clip((d2 - d1) * 40, 0, 1)
    fiss = 1 - ridge
    long = fbm(beta=2.0, stretch=(.1, 1.0))
    fine = fbm(beta=1.6)
    h = 1.2 * ridge ** .6 + .3 * long + .1 * fine
    t = norm01(.7 * ridge + .25 * long + .1 * fine)
    rgb = colour(t, [(0, (34, 27, 21)), (.35, (62, 50, 40)), (.65, (92, 80, 66)), (1, (128, 118, 102))])
    lich = norm01(fbm(beta=2.5))
    rgb = rgb * (1 - .25 * (lich > .72)[..., None]) + np.array([120, 128, 96]) * .25 * (lich > .72)[..., None]
    save("bark", rgb, h, 4.0)
    del fiss


# ---------- daub: wattle and daub under limewash, warm white with soft bumps and hairline cracks, 1 m per tile ----------
def daub():
    lump = fbm(beta=3.0)
    mid = fbm(beta=2.0)
    fine = fbm(beta=1.6)
    pts = rng.random((14, 2))
    d1, d2, _ = voronoi(N, pts)
    crack = np.exp(-((d2 - d1) / .0025) ** 2) * (norm01(fbm(beta=2.5)) > .72) * .6
    h = .8 * lump + .25 * mid + .06 * fine - .9 * crack
    t = norm01(.5 * mid + .3 * lump + .1 * fine)
    rgb = colour(t, [(0, (196, 186, 166)), (.4, (220, 212, 194)), (.75, (232, 226, 212)), (1, (240, 236, 226))])
    stain = norm01(fbm(beta=3.2)) ** 3
    rgb = rgb * (1 - .18 * stain[..., None]) + np.array([150, 132, 100]) * .18 * stain[..., None]
    rgb = rgb * (1 - .35 * crack[..., None])
    save("daub", rgb, h, 2.2)


# ---------- stone: random rubble in rough courses with lime mortar, 2 m per tile ----------
def stone():
    h = np.full((N, N), -.4)
    rgb = colour(norm01(fbm(beta=1.5)), [(0, (150, 144, 128)), (1, (196, 190, 172))])
    rough = fbm(beta=1.8)
    wob = fbm(beta=2.6) * .006
    y = 0.0
    while y < 1 - .04:
        ch = min(1 - y, .07 + rng.random() * .06)
        if 1 - y - ch < .05:
            ch = 1 - y
        x = rng.random() * .1
        x_end = x + 1
        while x < x_end - .03:
            w = min(x_end - x, .07 + rng.random() * .14)
            if x_end - x - w < .05:
                w = x_end - x
            sh = ch * (.7 + rng.random() * .3)            # stones do not fill their course: smaller ones float in mortar
            sw = w - .008
            cx, cy = x + w / 2, y + ch / 2 + (rng.random() - .5) * (ch - sh)
            rad = min(sw, sh) * (.25 + rng.random() * .3)
            # signed distance to a rounded rectangle, with wrap-round
            dx = np.abs(((xs - cx + .5) % 1) - .5) - (sw / 2 - rad)
            dy = np.abs(((ys - cy + .5) % 1) - .5) - (sh / 2 - rad)
            sdf = np.hypot(np.maximum(dx, 0), np.maximum(dy, 0)) + np.minimum(np.maximum(dx, dy), 0) - rad + wob
            m = sdf < 0
            if m.any():
                dome = np.clip(-sdf / (min(sw, sh) * .35), 0, 1) ** .55
                hh = dome * (1.0 + .3 * rng.random()) + .12 * rough
                h = np.where(m, np.maximum(h, hh), h)
                tone = rng.random()
                c = colour(np.full(1, tone * .65 + .2), [(0, (88, 84, 78)), (.4, (118, 112, 102)), (.75, (142, 136, 122)), (1, (168, 160, 146))])[0]
                c = c + (rng.random() - .5) * np.array([28, 16, -4])
                col = c[None, None, :] * (.8 + .2 * dome[..., None]) * (1 + .08 * rough[..., None])
                rgb = np.where(m[..., None], col, rgb)
            x += w
        y += ch
    save("stone", rgb, h, 3.2)


# ---------- slate: Welsh slates in courses, each overlapping the one below, 2 m per tile (16 courses) ----------
def slate():
    rows = 16
    rowf = ys * rows
    row = np.floor(rowf).astype(int)
    v = rowf % 1
    h = np.zeros((N, N))
    rgb = np.zeros((N, N, 3))
    tile_id = np.zeros((N, N))
    for r in range(rows):
        sel = row == r
        cuts = np.sort(rng.random(int(9 + rng.random() * 4)))
        xr = (xs + (.5 / 11 if r % 2 else 0)) % 1
        k = np.searchsorted(cuts, xr)
        tile_id = np.where(sel, r * 50 + k, tile_id)
    ids = np.unique(tile_id)
    tone = dict(zip(ids, rng.random(len(ids))))
    tv = np.vectorize(tone.get)(tile_id)
    # vertical gaps between slates
    gx = np.abs(np.diff(tile_id, axis=1, append=tile_id[:, :1])) > 0
    gx = blur(gx.astype(float), 1) > .05
    rag = fbm(beta=1.5) * .03
    bottom = np.clip((1 - v - .02 + rag) * 30, 0, 1)   # the ragged bottom edge of each course
    h = v * .9 + .25 * fbm(beta=1.8) * .3 - .8 * gx + (1 - bottom) * -.5
    t = norm01(tv * .55 + norm01(fbm(beta=1.6)) * .45)
    rgb = colour(t, [(0, (54, 60, 70)), (.4, (74, 82, 94)), (.7, (90, 98, 110)), (1, (110, 116, 124))])
    purple = (tv > .78)[..., None]
    rgb = rgb * (1 - .3 * purple) + np.array([88, 76, 92]) * .3 * purple
    shade = (.72 + .28 * v) * (1 - .55 * gx) * (.6 + .4 * bottom)
    rgb *= shade[..., None]
    save("slate", rgb, h, 2.6)


# ---------- thatch: straw laid down the slope (down the picture), combed in courses, 2 m per tile ----------
def thatch():
    straw = fbm(beta=1.5, stretch=(.03, 1.0))
    straw2 = fbm(beta=1.2, stretch=(.08, 1.0))
    clump = fbm(beta=2.6, stretch=(.4, 1.0))
    courses = 5
    wav = fbm(beta=3.0) * .03                       # the courses are not ruled lines: they wander
    v = ((ys + wav) * courses) % 1
    butt = np.clip(1 - v * 3, 0, 1) ** 2            # the cut ends of the bundles, at the foot of each course
    h = .5 * straw + .25 * straw2 + .5 * clump + .25 * v - .25 * butt
    t = norm01(.5 * straw + .25 * straw2 + .35 * clump) * (.88 + .12 * v)
    rgb = colour(t, [(0, (66, 52, 34)), (.35, (112, 88, 56)), (.65, (142, 114, 74)), (1, (176, 150, 102))])
    moss = norm01(fbm(beta=3.0)) > .72
    rgb = rgb * (1 - .28 * moss[..., None]) + np.array([92, 98, 58]) * .28 * moss[..., None]
    rgb *= (.86 + .14 * v)[..., None]
    save("thatch", rgb, h, 3.0)


# ---------- rushes: rushes and herbs strewn on a beaten earth floor, 1.5 m per tile ----------
def rushes():
    earth = fbm(beta=2.2)
    img = colour(norm01(earth), [(0, (70, 56, 40)), (1, (106, 88, 64))])
    h = .2 * earth
    acc = np.zeros((N, N))
    col = np.zeros((N, N, 3))
    for _ in range(1400):
        x0, y0, a, L = rng.random() * N, rng.random() * N, rng.random() * np.pi, 30 + rng.random() * 110
        w = 1.2 + rng.random() * 2.2
        c = np.array([150, 130, 70]) + rng.random() * np.array([60, 50, 30]) - np.array([0, 0, 0]) * rng.random()
        if rng.random() < .25:
            c = np.array([96, 112, 56]) + rng.random() * 30
        tt = np.linspace(0, 1, int(L))
        px = (x0 + np.cos(a) * L * tt).astype(int) % N
        py = (y0 + np.sin(a) * L * tt).astype(int) % N
        for o in range(int(np.ceil(w))):
            qx, qy = (px + int(-np.sin(a) * o)) % N, (py + int(np.cos(a) * o)) % N
            acc[qy, qx] = 1
            col[qy, qx] = c
            h[qy, qx] += .35
    acc = blur(acc, 1)
    m = np.clip(acc * 2.2, 0, 1)[..., None]
    rgb = img * (1 - m) + col * m
    save("rushes", rgb, blur(h, 1), 2.2)


# ---------- grass: a light, near-grey grass detail to lay over the land's own colours, 2 m per tile ----------
def grass():
    a = fbm(beta=1.2)
    b = fbm(beta=2.4)
    blades = np.zeros((N, N))
    for _ in range(9000):
        x0, y0, L = rng.random() * N, rng.random() * N, 6 + rng.random() * 18
        a0 = -np.pi / 2 + (rng.random() - .5) * 1.4
        tt = np.linspace(0, 1, int(L))
        px = (x0 + np.cos(a0) * L * tt).astype(int) % N
        py = (y0 + np.sin(a0) * L * tt).astype(int) % N
        blades[py, px] += .6 + rng.random() * .6
    blades = blur(blades, 1)
    t = norm01(.45 * a + .35 * b + 1.2 * np.clip(blades, 0, 1.5))
    rgb = colour(t, [(0, (150, 152, 140)), (.5, (192, 196, 180)), (1, (232, 238, 214))])
    save("grass", rgb, .3 * b + .9 * blades + .2 * a, 1.6)


# ---------- leaves: a cluster of leaves with see-through gaps, for the crowns of the trees ----------
def leaves():
    n = 512
    img = np.zeros((n, n, 3))
    al = np.zeros((n, n))
    yy, xx = np.mgrid[0:n, 0:n]
    cx, cy = n / 2, n / 2
    for i in range(1100):
        r = (rng.random() ** .6) * n * .46
        a = rng.random() * 2 * np.pi
        lx, ly = cx + np.cos(a) * r, cy + np.sin(a) * r * .92
        L, W, rot = 9 + rng.random() * 9, 4 + rng.random() * 3, rng.random() * np.pi
        x0, x1, y0, y1 = int(max(0, lx - L - 2)), int(min(n, lx + L + 2)), int(max(0, ly - L - 2)), int(min(n, ly + L + 2))
        sx, sy = xx[y0:y1, x0:x1] - lx, yy[y0:y1, x0:x1] - ly
        u = sx * np.cos(rot) + sy * np.sin(rot)
        v = -sx * np.sin(rot) + sy * np.cos(rot)
        inside = (u / L) ** 2 + (v / W) ** 2 < 1
        depth = 1 - r / (n * .46)   # leaves deep in the crown are darker
        g = .45 + .55 * rng.random()
        c = np.array([62, 92, 40]) * (.55 + .45 * g) * (.7 + .3 * (1 - depth)) + (np.array([30, 26, 6]) if rng.random() < .15 else 0)
        shade = (.85 + .15 * (u / L))[..., None]
        img[y0:y1, x0:x1] = np.where(inside[..., None], c * shade, img[y0:y1, x0:x1])
        al[y0:y1, x0:x1] = np.where(inside, 1, al[y0:y1, x0:x1])
    # a few twigs
    for _ in range(14):
        a = rng.random() * 2 * np.pi
        for t in np.linspace(0, 1, 160):
            px, py = int(cx + np.cos(a) * t * n * .38), int(cy + np.sin(a) * t * n * .38)
            img[py - 1:py + 1, px - 1:px + 1] = (52, 40, 28)
            al[py - 1:py + 1, px - 1:px + 1] = 1
    os.makedirs(OUT, exist_ok=True)
    im = Image.fromarray(np.dstack([np.clip(img, 0, 255).astype(np.uint8), (al * 255).astype(np.uint8)]), "RGBA")
    im.save(os.path.join(OUT, "leaves.webp"), quality=82, method=6)
    im.resize((256, 256), Image.LANCZOS).save(os.path.join(OUT, "leaves-s.webp"), quality=80, method=6)
    print("leaves")


if __name__ == "__main__":
    import sys
    which = sys.argv[1:] or ["oak", "boards", "bark", "daub", "stone", "slate", "thatch", "rushes", "grass", "leaves"]
    for w in which:
        globals()[w]()
