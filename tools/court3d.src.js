/* The shared engine for the courts of Wales in 3D (court-<id>.html, src/courts.py).
   Each court is a small scene file (tools/court-<id>.src.js) that imports run() from here and gives:
     STOPS   where you stand [x, z] and where you look [x, y, z] at each stop, by the stop ids in src/courts.py
     START   { x, z, yaw } where the walker first stands
     LAND    real heights from tools/bake_court.py (optional), and shape(x, z, h) to add the earthworks to them
     floor(x, z)    the height you walk on (ground, bridges, floors), default the land
     blocked(x, z)  true where you cannot walk (water), default nowhere
     colour(x, z, h, c)  tint the land (c is a THREE.Color to change), optional
     build(K)       makes the buildings with the helpers in K (below)
     look           sky, fog, sun and light settings, optional
     indoor(x, z)   true inside a building: the eye opens up to the firelight there and the wind drops (optional)
     grass(x, z)    true where tufts of grass may grow (optional), within grassAt { x, z, r }
     plan           { x, z, r }: the area the little plan (top right) shows; planExtra(ctx, P, k) draws water on it
     sea            0 to 1, how loud the sea is (0 inland); harp { x, z, r }, where the harp plays in the hall
   A stop may give a third number, a narrower field of view (degrees) for far views, as the eye sees mountains.
   Brought up to the Llys Rhosyr engine (tools/llys3d.src.js, November 2026): log depth, sky light, fire shadows,
   grass tufts, smoothed looking and walking, a fade when the straight way to a stop is blocked, the field of view per
   stop, the pixel ratio falling when frames are slow, sound made in code, and the plan.
     fineMore       [[size, x, z], ...]: more pieces of finer land, for a second place seen close
     far            how far the eye sees, in metres (default 3000), for courts with mountains far off
     people         true if the hall has its household (their talk is heard); birds { kind: "gull" | "rook", x, z, r };
                    flock { x, z } and kennel { x, z } for the bleating and the barking; water(x, z), the distance to a stream
   build(K) has, besides the boxes and walls: framed() and framedBox() for timber framing, logWall() for palisades, table()
   and bench(), bblock() for small pieces merged by material, person(), horse(), hound(), sheep(), cow() and goose()
   (from Llys Rhosyr), and hanging() for an embroidered cloth. Surfaces come from src/static/court/tex
   (tools/make_court_textures.py), found from this file's own address.
   x is east and z is south, in metres. Bundle each court with three.js:
     npx esbuild court-<id>.src.js --bundle --minify --format=esm --target=es2020 --outfile=court-<id>.js
   and copy it to src/static/. Everything is made in code: no models or pictures to download. */
import * as THREE from "three";
import { mergeGeometries } from "three/examples/jsm/utils/BufferGeometryUtils.js";

export function rng(seed) { return function () { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
export const smooth = (a, b, x) => { const t = Math.max(0, Math.min(1, (x - a) / (b - a))); return t * t * (3 - 2 * t); };

// real land: bilinear heights from the baked grid, in metres, 0 at the court's own ground level
export function landHeights(L, zeroAt = [0, 0]) {
  const raw = atob(L.h), n = L.n, a = new Uint16Array(n * n);
  for (let i = 0; i < n * n; i++) a[i] = raw.charCodeAt(2 * i) | (raw.charCodeAt(2 * i + 1) << 8);
  const step = L.size / (n - 1), half = L.size / 2;
  const at = (x, z) => {
    const fx = Math.max(0, Math.min(n - 1.001, (x + half) / step)), fz = Math.max(0, Math.min(n - 1.001, (z + half) / step));
    const i = Math.floor(fx), j = Math.floor(fz), tx = fx - i, tz = fz - j;
    const h = (ii, jj) => a[jj * n + ii] / 10;
    return h(i, j) * (1 - tx) * (1 - tz) + h(i + 1, j) * tx * (1 - tz) + h(i, j + 1) * (1 - tx) * tz + h(i + 1, j + 1) * tx * tz;
  };
  const z0 = at(zeroAt[0], zeroAt[1]);
  return (x, z) => at(x, z) - z0;
}

export function run(host, D, S) {
  const cy = !!D.cy, T = (p) => (cy ? p[1] : p[0]);
  const small = Math.min(screen.width, screen.height) <= 600;
  const reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  const R = rng(S.seed || 1237);
  const look = Object.assign({ fog: 0xc9d1cf, fogNear: 60, fogFar: 900, top: 0x8fa9c2, mid: 0xc6d2d6, low: 0xdfe2dc, sun: [-45, 55, 35], sunI: 2.2, hemi: .8, exposure: 1.0 }, S.look || {});

  const canvas = document.createElement("canvas");
  canvas.className = "ll-canvas"; canvas.tabIndex = 0;
  canvas.setAttribute("role", "img"); canvas.setAttribute("aria-label", T(D.ui.canvas));
  host.appendChild(canvas);
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ canvas, antialias: !small, powerPreference: "high-performance", logarithmicDepthBuffer: true }); }
  catch (e) { host.classList.add("fail"); canvas.remove(); return; }
  const maxDpr = Math.min(devicePixelRatio || 1, small ? 1.6 : 2);
  let dpr = small ? Math.min(maxDpr, 1.25) : maxDpr;
  renderer.setPixelRatio(dpr);
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = look.exposure;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;

  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(look.fog, look.fogNear, look.fogFar);
  const FOV = small ? 68 : 60, camera = new THREE.PerspectiveCamera(FOV, 1, 0.1, S.far || 3000);
  camera.rotation.order = "YXZ";

  // ---------- textures, drawn in code ----------
  const aniso = renderer.capabilities.getMaxAnisotropy ? Math.min(8, renderer.capabilities.getMaxAnisotropy()) : 4;
  function tex(size, draw, rep, srgb = true) {
    const c = document.createElement("canvas"); c.width = c.height = size;
    draw(c.getContext("2d"), size);
    const t = new THREE.CanvasTexture(c);
    t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = aniso;
    if (srgb) t.colorSpace = THREE.SRGBColorSpace;
    if (rep) t.repeat.set(rep[0], rep[1]);
    return t;
  }
  const noise = (x, s, n, a, base) => { for (let i = 0; i < n; i++) { const v = base + (R() - .5) * a; x.fillStyle = `rgba(${v},${v},${v},${R() * .35 + .1})`; x.fillRect(R() * s, R() * s, R() * 6 + 1, R() * 6 + 1); } };
  const stoneTex = tex(512, (x, s) => {           // rubble stone, 2 m per tile
    x.fillStyle = "#7d786c"; x.fillRect(0, 0, s, s);
    let y = 0;
    while (y < s) {
      const rh = 26 + R() * 30; let xx = -R() * 40;
      while (xx < s) {
        const w = 34 + R() * 70, g = 105 + R() * 60, warm = R() * 22;
        x.fillStyle = `rgb(${g + warm},${g + warm * .6},${g - 6})`;
        x.beginPath(); x.roundRect ? x.roundRect(xx + 2, y + 2, w - 4, rh - 4, 9) : x.rect(xx + 2, y + 2, w - 4, rh - 4); x.fill();
        x.fillStyle = "rgba(0,0,0,.18)"; x.fillRect(xx + 3, y + rh - 7, w - 6, 4);
        x.fillStyle = "rgba(255,255,255,.08)"; x.fillRect(xx + 4, y + 3, w - 8, 3);
        xx += w;
      }
      y += rh;
    }
    noise(x, s, 3000, 90, 120);
  });
  const limeTex = tex(256, (x, s) => { x.fillStyle = "#e9e3d6"; x.fillRect(0, 0, s, s); noise(x, s, 2500, 60, 205); for (let i = 0; i < 30; i++) { x.fillStyle = "rgba(150,140,120,.06)"; x.beginPath(); x.ellipse(R() * s, R() * s, R() * 40 + 10, R() * 20 + 5, R() * 3, 0, 7); x.fill(); } });
  const thatchTex = tex(256, (x, s) => {
    x.fillStyle = "#8a6a3c"; x.fillRect(0, 0, s, s);
    for (let i = 0; i < 2600; i++) { const g = 120 + R() * 90; x.strokeStyle = `rgba(${g},${g * .78},${g * .45},.55)`; x.lineWidth = R() * 1.6 + .4; const xx = R() * s, yy = R() * s; x.beginPath(); x.moveTo(xx, yy); x.lineTo(xx + (R() - .5) * 4, yy + 14 + R() * 26); x.stroke(); }
    for (let yy = 0; yy < s; yy += 32) { x.fillStyle = "rgba(40,28,10,.25)"; x.fillRect(0, yy, s, 3); }
  });
  const slateTex = tex(512, (x, s) => {           // blue roofing slates in courses, 2 m per tile, smaller towards the ridge is not needed at this scale
    x.fillStyle = "#3d4650"; x.fillRect(0, 0, s, s);
    const rows = 16, rh = s / rows;
    for (let r = 0; r < rows; r++) {
      let xx = (r % 2) * -14 - R() * 10;
      while (xx < s) {
        const w = 22 + R() * 16, g = 70 + R() * 30, b = g + 10 + R() * 14;
        x.fillStyle = `rgb(${g - 6},${g + 2},${b})`; x.fillRect(xx + 1, r * rh, w - 2, rh - 2);
        x.fillStyle = "rgba(0,0,0,.35)"; x.fillRect(xx + 1, r * rh + rh - 4, w - 2, 3);
        x.fillStyle = "rgba(255,255,255,.06)"; x.fillRect(xx + 2, r * rh + 1, w - 4, 2);
        xx += w;
      }
    }
    noise(x, s, 1500, 50, 90);
  });
  const woodTex = tex(256, (x, s) => {
    x.fillStyle = "#6b4a2e"; x.fillRect(0, 0, s, s);
    for (let i = 0; i < 160; i++) { x.strokeStyle = `rgba(${30 + R() * 40},${20 + R() * 25},${10},${R() * .4 + .1})`; x.lineWidth = R() * 2 + .5; const yy = R() * s; x.beginPath(); x.moveTo(0, yy); x.bezierCurveTo(s * .3, yy + (R() - .5) * 10, s * .6, yy + (R() - .5) * 10, s, yy); x.stroke(); }
  });
  const logTex = tex(256, (x, s) => {             // a palisade of split oak logs, 2 m per tile, the logs upright
    x.fillStyle = "#4a3624"; x.fillRect(0, 0, s, s);
    const n = 8, w = s / n;
    for (let i = 0; i < n; i++) {
      const g = 90 + R() * 30;
      const gr = x.createLinearGradient(i * w, 0, i * w + w, 0);
      gr.addColorStop(0, `rgb(${g * .55},${g * .42},${g * .3})`); gr.addColorStop(.45, `rgb(${g},${g * .78},${g * .55})`); gr.addColorStop(1, `rgb(${g * .5},${g * .38},${g * .26})`);
      x.fillStyle = gr; x.fillRect(i * w + 1, 0, w - 2, s);
      for (let k = 0; k < 14; k++) { x.strokeStyle = `rgba(30,20,10,${R() * .3 + .1})`; x.lineWidth = 1; const xx = i * w + 3 + R() * (w - 6); x.beginPath(); x.moveTo(xx, 0); x.lineTo(xx + (R() - .5) * 3, s); x.stroke(); }
    }
  });
  const floorTex = tex(256, (x, s) => { x.fillStyle = "#6e5b42"; x.fillRect(0, 0, s, s); noise(x, s, 3000, 70, 100); for (let i = 0; i < 500; i++) { x.strokeStyle = `rgba(${170 + R() * 40},${150 + R() * 30},${80},.35)`; x.lineWidth = 1; const xx = R() * s, yy = R() * s, a = R() * 6.3; x.beginPath(); x.moveTo(xx, yy); x.lineTo(xx + Math.cos(a) * 18, yy + Math.sin(a) * 18); x.stroke(); } }, [3, 3]);
  const boardTex = tex(256, (x, s) => { x.fillStyle = "#7a5a3a"; x.fillRect(0, 0, s, s); for (let i = 0; i < 8; i++) { const g = 100 + R() * 30; x.fillStyle = `rgb(${g},${g * .75},${g * .5})`; x.fillRect(0, i * 32 + 1, s, 30); } for (let i = 0; i < 300; i++) { x.strokeStyle = `rgba(40,25,10,${R() * .25})`; x.lineWidth = 1; const yy = R() * s; x.beginPath(); x.moveTo(R() * s, yy); x.lineTo(R() * s, yy + (R() - .5) * 2); x.stroke(); } });
  const grassTex = tex(256, (x, s) => { x.fillStyle = "#b5b5b5"; x.fillRect(0, 0, s, s); noise(x, s, 6000, 120, 180); }, [260, 260], false);

  // ---------- materials ----------
  const M = {
    stone: new THREE.MeshStandardMaterial({ map: stoneTex, roughness: .95 }),
    lime: new THREE.MeshStandardMaterial({ map: limeTex, roughness: .92 }),
    thatch: new THREE.MeshStandardMaterial({ map: thatchTex, roughness: 1, side: THREE.DoubleSide }),
    slate: new THREE.MeshStandardMaterial({ map: slateTex, roughness: .55, metalness: .05, side: THREE.DoubleSide }),
    wood: new THREE.MeshStandardMaterial({ map: woodTex, roughness: .85 }),
    oak: new THREE.MeshStandardMaterial({ map: woodTex, color: 0x5a4a3c, roughness: .8 }),
    darkwood: new THREE.MeshStandardMaterial({ map: woodTex, color: 0x8a7a6a, roughness: .8 }),
    logs: new THREE.MeshStandardMaterial({ map: logTex, roughness: .95 }),
    boards: new THREE.MeshStandardMaterial({ map: boardTex, roughness: .9 }),
    floor: new THREE.MeshStandardMaterial({ map: floorTex, roughness: 1 }),
    red: new THREE.MeshStandardMaterial({ color: 0x8e1d18, roughness: .9, side: THREE.DoubleSide }),
    green: new THREE.MeshStandardMaterial({ color: 0x2f5a34, roughness: .9, side: THREE.DoubleSide }),
    gold: new THREE.MeshStandardMaterial({ color: 0xc89a2a, roughness: .45, metalness: .6 }),
    cloth: new THREE.MeshStandardMaterial({ color: 0x2d4a6b, roughness: .95, side: THREE.DoubleSide }),
    glass: new THREE.MeshStandardMaterial({ color: 0x9fb4b8, roughness: .1, metalness: .5, emissive: 0x1d2a2e, emissiveIntensity: .6 }),
    water: new THREE.MeshStandardMaterial({ color: 0x5f7a80, roughness: .12, metalness: .2, transparent: true, opacity: .92 }),
    leaf: new THREE.MeshStandardMaterial({ color: 0x4f6b36, roughness: 1, flatShading: true }),
    bark: new THREE.MeshStandardMaterial({ color: 0x4b3b2c, roughness: 1 }),
    ember: new THREE.MeshBasicMaterial({ color: 0xff7a2a }),
    flame: new THREE.MeshBasicMaterial({ color: 0xffb347, transparent: true, opacity: .85, blending: THREE.AdditiveBlending, depthWrite: false }),
    smoke: new THREE.MeshBasicMaterial({ color: 0xcfcfcf, transparent: true, opacity: .22, depthWrite: false }),
    mark: new THREE.MeshStandardMaterial({ color: 0xf2c14e, emissive: 0xc8901a, emissiveIntensity: 1.2, roughness: .3, metalness: .4 }),
  };
  M.daub = M.lime.clone(); M.daub.userData.ts = 1.5;
  M.rubble = M.stone.clone(); M.rubble.userData.ts = 1.15;   // castle walls: smaller stones, grit and slate rubble   // wattle and daub under limewash, between the timbers of a framed wall
  ["oak", "wood", "darkwood"].forEach((k) => { M[k].userData.ts = 1.3; M[k].userData.grain = true; });
  M.boards.userData.grain = true;

  // ---------- real surfaces: colour and bump pictures made by tools/make_court_textures.py (src/static/court/tex), drawn
  // over the canvas ones as soon as they come; phones get the half-size ones ----------
  const TEX = S.texBase || new URL("court/tex/", import.meta.url).href, sfx = small ? "-s" : "", loader = new THREE.TextureLoader();
  function surf(mat, name, o = {}) {
    const rep2 = o.rep || (mat.map && mat.map.repeat ? [mat.map.repeat.x, mat.map.repeat.y] : [1, 1]);
    const set = (t, srgb) => { t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = aniso; t.colorSpace = srgb ? THREE.SRGBColorSpace : THREE.NoColorSpace; t.repeat.set(rep2[0], rep2[1]); };
    loader.load(TEX + name + sfx + ".webp", (t) => { set(t, true); mat.map = t; if (o.tint !== undefined) mat.color.set(o.tint); mat.needsUpdate = true; });
    if (o.normal !== false) loader.load(TEX + name + "_n" + sfx + ".webp", (t) => { set(t, false); mat.normalMap = t; mat.normalScale.set(o.n || 1, o.n || 1); mat.needsUpdate = true; });
  }
  surf(M.stone, "stone"); surf(M.rubble, "stone", { tint: 0xf2f0ea }); surf(M.lime, "daub", { n: .7 }); surf(M.daub, "daub", { n: .7 }); surf(M.thatch, "thatch"); surf(M.slate, "slate", { n: 1.2 });
  surf(M.wood, "oak", { tint: 0xd8c8b4 }); surf(M.oak, "oak", { tint: 0x9a8a7a }); surf(M.darkwood, "oak", { tint: 0x6e6258 });
  surf(M.logs, "bark", { tint: 0xc8bcae }); surf(M.boards, "boards", { tint: 0xe0d0bc }); surf(M.floor, "rushes"); surf(M.bark, "bark", { tint: 0xb0a496 });

  // ---------- helpers for the scene ----------
  const walls = [];   // [x1, z1, x2, z2, half thickness, bottom, top]: what you bump into
  const posts = [];   // [x, z, radius]
  const anim = [];    // functions (time, dt) run every frame
  // a box with its texture at true size; a material with grain (oak, boards) has the grain run along each face's longer side
  function boxGeo(w, h, d, mat, ts = 2) {
    const ud = mat.userData || {}; ts = ud.ts || ts;   // a material can set its own tile size in metres
    const g = new THREE.BoxGeometry(w, h, d), uv = g.attributes.uv, ou = R(), ov = R();
    const faces = [[d, h], [d, h], [w, d], [w, d], [w, h], [w, h]];
    for (let f = 0; f < 6; f++) {
      const [fa, fb] = faces[f], sw = ud.grain && fb > fa;
      for (let i = 0; i < 4; i++) { const k = f * 4 + i, u = uv.getX(k), v = uv.getY(k); if (sw) uv.setXY(k, v * fb / ts + ou, u * fa / ts + ov); else uv.setXY(k, u * fa / ts + ou, v * fb / ts + ov); }
    }
    return g;
  }
  function block(w, h, d, mat, x, y, z, ry = 0, ts = 2) {
    const m = new THREE.Mesh(boxGeo(w, h, d, mat, ts), mat); m.position.set(x, y, z); m.rotation.y = ry; m.castShadow = m.receiveShadow = true; scene.add(m); return m;
  }
  // many small fixed pieces (studs, rails, furniture, the logs' rails) are gathered by material and drawn as one mesh each
  const batch = new Map(), mtx = new THREE.Matrix4(), eul = new THREE.Euler(0, 0, 0, "YXZ"), qq = new THREE.Quaternion(), one = new THREE.Vector3(1, 1, 1);
  function bblock(w, h, d, mat, x, y, z, ry = 0, rx = 0, rz = 0) {
    const g = boxGeo(w, h, d, mat); eul.set(rx, ry, rz); mtx.compose(new THREE.Vector3(x, y, z), qq.setFromEuler(eul), one); g.applyMatrix4(mtx);
    if (!batch.has(mat)) batch.set(mat, []); batch.get(mat).push(g);
  }
  // a point along a line turned ry about the up axis: a along it, b across it
  const along = (x, z, ry, a, b) => [x + a * Math.cos(ry) + b * Math.sin(ry), z - a * Math.sin(ry) + b * Math.cos(ry)];
  // furniture: a trestle table (boards on two splayed trestles) and a bench, both standing on y0
  function table(x, z, len, wid, ry, y0) {
    bblock(len, .06, wid, M.wood, x, y0 + .77, z, ry);
    [-1, 1].forEach((s) => {
      const [tx, tz] = along(x, z, ry, s * (len / 2 - .3), 0);
      [-1, 1].forEach((k) => { const [lx, lz] = along(tx, tz, ry, 0, k * wid * .22); bblock(.07, .8, .07, M.oak, lx, y0 + .37, lz, ry, -k * .2); });
      bblock(.08, .07, wid * .82, M.oak, tx, y0 + .7, tz, ry); bblock(.08, .06, wid * .7, M.oak, tx, y0 + .2, tz, ry);
    });
    const [sx, sz] = along(x, z, ry, 0, 0); bblock(len - .7, .06, .06, M.oak, sx, y0 + .25, sz, ry);   // the stretcher between them
  }
  function bench(x, z, len, ry, y0) {
    bblock(len, .05, .3, M.wood, x, y0 + .45, z, ry);
    [-1, 1].forEach((s) => { const [lx, lz] = along(x, z, ry, s * (len / 2 - .22), 0); bblock(.05, .43, .28, M.oak, lx, y0 + .215, lz, ry, 0, s * .06); });
  }
  // a timber-framed wall: daub panels between oak posts, studs and rails that stand a little proud of them on both faces.
  // gaps are [distance along, width] as for wallLine; door heads are at lintel; o.stud is the spacing of the studs
  function framed(x1, z1, x2, z2, h, y0, gaps = [], lintel = 2.1, o = {}) {
    const t = o.t || .26, st = o.stud || .6, L = Math.hypot(x2 - x1, z2 - z1), ux = (x2 - x1) / L, uz = (z2 - z1) / L, ry = -Math.atan2(uz, ux);
    wallLine(x1, z1, x2, z2, h, t - .07, o.infill || M.daub, gaps, y0, lintel);
    const P = (d) => [x1 + ux * d, z1 + uz * d];
    const inGap = (d, pad) => gaps.some(([c, w]) => Math.abs(d - c) < w / 2 + pad);
    const post = (d, w, yA, yB) => { const [px, pz] = P(d); bblock(w, yB - yA, t, M.oak, px, (yA + yB) / 2, pz, ry); };
    const rail = (yc, hh) => {   // a horizontal member along the wall, broken at the doors that rise above it
      let at = 0; const cuts = gaps.filter(([, , top]) => (top || lintel) > yc - y0 - hh / 2).map(([c, w]) => [c - w / 2, c + w / 2]).sort((a, b) => a[0] - b[0]);
      cuts.concat([[L, L]]).forEach(([a, b]) => { if (a - at > .05) { const [cx, cz] = P((at + a) / 2); bblock(a - at, hh, t, M.oak, cx, yc, cz, ry); } at = Math.max(at, b); });
    };
    post(.14, .28, y0, y0 + h); post(L - .14, .28, y0, y0 + h);   // the corner posts
    gaps.forEach(([c, w]) => { [-1, 1].forEach((s) => post(c + s * (w / 2 + .1), .2, y0, y0 + h)); post(c, w + .4, y0 + lintel, y0 + lintel + .2); });
    for (let d = st; d < L - st * .6; d += st) {
      if (inGap(d, .18)) { if (lintel && h - lintel > .5) post(d, .16, y0 + lintel + .2, y0 + h); continue; }
      post(d, .16, y0, y0 + h);
    }
    rail(y0 + .1, .2);                       // the sill
    if (o.mid !== false && h > 2.6) rail(y0 + h * .5, .18);   // a middle rail
    rail(y0 + h - .1, .2);                   // the wall plate
    if (o.brace) { [[.28, 1], [L - .28, -1]].forEach(([d0, s]) => { const [bx, bz] = P(d0 + s * .55); bblock(1.5, .16, t, M.oak, bx, y0 + h - .75, bz, ry, 0, s * .9); }); }
  }
  // a framed box, such as an upper storey: four framed walls round a w by d rectangle centred at (cx, cz), turned ry
  function framedBox(cx, cz, w, d, h, y0, ry = 0, o = {}) {
    const c = [[-w / 2, -d / 2], [w / 2, -d / 2], [w / 2, d / 2], [-w / 2, d / 2]].map(([a, b]) => along(cx, cz, ry, a, b));
    for (let i = 0; i < 4; i++) framed(...c[i], ...c[(i + 1) % 4], h, y0, (o.gaps && o.gaps[i]) || [], o.lintel || 2.1, o);
  }
  // a palisade of upright split logs with sharpened tops, standing on y0 (a number or a function of x and z), with
  // gaps [distance along, width]; rail = 1 or -1 puts a backing rail on the left or the right of the line
  const logs = [];
  function logWall(x1, z1, x2, z2, h, y0, gaps = [], rail = 0) {
    const L = Math.hypot(x2 - x1, z2 - z1), ux = (x2 - x1) / L, uz = (z2 - z1) / L, n = Math.max(1, Math.round(L / .33)), Y = typeof y0 === "function" ? y0 : () => y0;
    const inGap = (d) => gaps.some(([c, w]) => Math.abs(d - c) < w / 2);
    let run = null; const runs = [];
    for (let i = 0; i < n; i++) {
      const d = (i + .5) * L / n;
      if (inGap(d)) { run = null; continue; }
      const x = x1 + ux * d, z = z1 + uz * d; logs.push([x, Y(x, z) - .35, z, .15 + R() * .035, h + .35 + (R() - .5) * .3]);
      if (!run) { run = [d, d]; runs.push(run); } run[1] = d;
    }
    runs.forEach(([a, b]) => {
      a -= L / n / 2; b += L / n / 2;
      const ax = x1 + ux * a, az = z1 + uz * a, bx = x1 + ux * b, bz = z1 + uz * b, yb = Math.min(Y(ax, az), Y(bx, bz));
      walls.push([ax, az, bx, bz, .2, yb, yb + h]);
      if (rail) { const nx = -uz * rail * .24, nz = ux * rail * .24, ry = -Math.atan2(uz, ux); [.25, .62].forEach((f) => bblock(b - a, .14, .1, M.oak, (ax + bx) / 2 + nx, yb + h * f, (az + bz) / 2 + nz, ry)); }
    });
  }
  function cyl(r1, r2, h, mat, x, y, z, seg = 10) { const m = new THREE.Mesh(new THREE.CylinderGeometry(r1, r2, h, seg), mat); m.position.set(x, y, z); m.castShadow = m.receiveShadow = true; scene.add(m); return m; }
  // a straight wall from (x1, z1) to (x2, z2), standing on y0
  function wallSeg(x1, z1, x2, z2, h, t, mat, y0 = 0, solid = true) {
    const L = Math.hypot(x2 - x1, z2 - z1); if (L < .05) return;
    const ry = -Math.atan2(z2 - z1, x2 - x1);
    block(L + .02, h, t, mat, (x1 + x2) / 2, y0 + h / 2, (z1 + z2) / 2, ry);
    if (solid) walls.push([x1, z1, x2, z2, t / 2, y0, y0 + h]);
  }
  // a line of wall with gaps: gaps are [distance along, width]; a lintel closes the gap above that height
  function wallLine(x1, z1, x2, z2, h, t, mat, gaps = [], y0 = 0, lintel = 0) {
    const L = Math.hypot(x2 - x1, z2 - z1), ux = (x2 - x1) / L, uz = (z2 - z1) / L;
    let at = 0;
    gaps.slice().sort((a, b) => a[0] - b[0]).forEach(([c, w]) => {
      if (c - w / 2 > at) wallSeg(x1 + ux * at, z1 + uz * at, x1 + ux * (c - w / 2), z1 + uz * (c - w / 2), h, t, mat, y0);
      if (lintel) block(w + .1, h - lintel, t, mat, x1 + ux * c, y0 + lintel + (h - lintel) / 2, z1 + uz * c, -Math.atan2(uz, ux));
      at = c + w / 2;
    });
    if (L > at) wallSeg(x1 + ux * at, z1 + uz * at, x2, z2, h, t, mat, y0);
  }
  // a gabled roof over a w (along x) by d box centred at (cx, cz), turned ry, eaves at ey, ridge rh above them
  function roof(cx, cz, w, d, ey, rh, mat, ry = 0, oh = .6, gableMat = null, gt = .3) {
    const grp = new THREE.Group(); grp.position.set(cx, 0, cz); grp.rotation.y = ry; scene.add(grp);
    const hw = w / 2 + oh, hd = d / 2 + oh, ry2 = ey + rh;
    const g = new THREE.BufferGeometry(), P = [], U = [], slope = Math.hypot(hd, rh);
    [1, -1].forEach((s) => {
      const a = [-hw, ey, s * hd], b = [hw, ey, s * hd], c = [hw, ry2, 0], dd = [-hw, ry2, 0];
      (s > 0 ? [a, b, c, a, c, dd] : [b, a, dd, b, dd, c]).forEach((v) => P.push(...v));
      const uw = hw, us = slope / 2;
      (s > 0 ? [[0, 0], [uw, 0], [uw, us], [0, 0], [uw, us], [0, us]] : [[uw, 0], [0, 0], [0, us], [uw, 0], [0, us], [uw, us]]).forEach((v) => U.push(...v));
    });
    g.setAttribute("position", new THREE.Float32BufferAttribute(P, 3)); g.setAttribute("uv", new THREE.Float32BufferAttribute(U, 2)); g.computeVertexNormals();
    const m = new THREE.Mesh(g, mat); m.castShadow = m.receiveShadow = true; grp.add(m);
    const ridge = new THREE.Mesh(new THREE.BoxGeometry(2 * hw, .16, .3), mat); ridge.position.set(0, ry2 + .02, 0); ridge.castShadow = true; grp.add(ridge);
    // the roof has a thickness: boards (or the reed of the thatch) seen from under it, and a board along each edge
    const under = new THREE.Mesh(g.clone(), mat === M.thatch ? M.thatch : M.boards); under.position.y = -.14; under.receiveShadow = true; grp.add(under);
    const edge = mat === M.thatch ? M.thatch : M.darkwood, th = mat === M.thatch ? .32 : .2;
    [1, -1].forEach((s) => {
      const f = new THREE.Mesh(boxGeo(2 * hw, th, .07, edge), edge); f.position.set(0, ey - th / 2 + .03, s * hd); f.castShadow = true; grp.add(f);
      [1, -1].forEach((e) => { const b = new THREE.Mesh(boxGeo(.07, th, slope + .05, edge), edge); b.position.set(e * hw, ey + rh / 2 - th / 2 + .03, s * hd / 2); b.rotation.x = s * Math.atan2(rh, hd); b.castShadow = true; grp.add(b); });
    });
    if (gableMat) [-w / 2, w / 2].forEach((gx) => {
      const sh = new THREE.Shape(); sh.moveTo(-d / 2, 0); sh.lineTo(d / 2, 0); sh.lineTo(0, rh * (d / 2) / hd); sh.closePath();
      const gg = new THREE.ExtrudeGeometry(sh, { depth: gt, bevelEnabled: false });
      gg.attributes.uv.array.forEach((v, i, arr) => { arr[i] = v / 2; });
      const gm = new THREE.Mesh(gg, gableMat); gm.rotation.y = Math.PI / 2; gm.position.set(gx - gt / 2, ey, 0); gm.castShadow = gm.receiveShadow = true; grp.add(gm);
    });
    return grp;
  }
  // trees: a trunk with three boughs, and crowns of leafy cards (a picture of a cluster of leaves, with gaps you see
  // the sky through), lit as if each crown were round. list of [x, z, height, crown radius]
  const noFlip = (sh) => { sh.fragmentShader = sh.fragmentShader.replace("#include <normal_fragment_begin>", THREE.ShaderChunk.normal_fragment_begin.replace("normal *= faceDirection;", "")); };
  const leafTex = tex(256, (x, s) => {
    x.clearRect(0, 0, s, s);
    for (let i = 0; i < 520; i++) {
      const r = Math.pow(R(), .6) * s * .46, a = R() * 6.283, d = 1 - r / (s * .46), g = 70 + R() * 50;
      x.fillStyle = `rgb(${g * .62 * (.75 + .25 * (1 - d))},${g * (.85 + .15 * (1 - d))},${g * .42})`;
      x.beginPath(); x.ellipse(s / 2 + Math.cos(a) * r, s / 2 + Math.sin(a) * r * .92, 5 + R() * 4, 2.2 + R() * 1.6, R() * 3.14, 0, 7); x.fill();
    }
  });
  leafTex.wrapS = leafTex.wrapT = THREE.ClampToEdgeWrapping;
  M.leaves = new THREE.MeshStandardMaterial({ map: leafTex, alphaTest: .5, side: THREE.DoubleSide, roughness: .85 });
  M.leaves.onBeforeCompile = noFlip;
  loader.load(TEX + "leaves" + sfx + ".webp", (t) => { t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = aniso; M.leaves.map = t; M.leaves.needsUpdate = true; });
  function crownGeo(nq) {
    const parts = [], v = new THREE.Vector3();
    for (let i = 0; i < nq; i++) {
      const g = new THREE.PlaneGeometry(1.05, 1.05), u = R() * 2 - 1, a = R() * 6.283, sq = Math.sqrt(1 - u * u), rr = .3 + .62 * Math.sqrt(R());
      g.rotateX(R() * 6.3); g.rotateY(R() * 6.3); g.rotateZ(R() * 6.3); g.translate(sq * Math.cos(a) * rr, u * .8 * rr, sq * Math.sin(a) * rr);
      const p = g.attributes.position, n = g.attributes.normal;
      for (let k = 0; k < p.count; k++) { v.set(p.getX(k), p.getY(k) + .25, p.getZ(k)).normalize(); n.setXYZ(k, v.x, v.y, v.z); }
      parts.push(g);
    }
    return mergeGeometries(parts);
  }
  function trunkGeo() {
    const parts = [], t = new THREE.CylinderGeometry(.3, .5, 1, 7, 1, true); t.translate(0, .5, 0); parts.push(t);
    for (let i = 0; i < 3; i++) { const b = new THREE.CylinderGeometry(.1, .22, .55, 5, 1, true); b.translate(0, .27, 0); b.rotateZ(.7 + R() * .3); b.rotateY(i * 2.1 + R()); b.translate(0, .72 + R() * .15, 0); parts.push(b); }
    parts.forEach((g) => { if (g.index) g.toNonIndexed && 0; });
    return mergeGeometries(parts.map((g) => g.index ? g.toNonIndexed() : g));
  }
  function trees(list, y = (x, z) => ground(x, z)) {
    if (!list.length) return;
    const tg = trunkGeo(), cg = crownGeo(small ? 16 : 26);
    const ti = new THREE.InstancedMesh(tg, M.bark, list.length), ci = new THREE.InstancedMesh(cg, M.leaves, list.length * 3);
    const m = new THREE.Matrix4(), q = new THREE.Quaternion(), e = new THREE.Euler(), col = new THREE.Color();
    list.forEach(([x, z, h, r], i) => {
      const g0 = y(x, z), tw = .5 + r * .1;
      m.compose(new THREE.Vector3(x, g0 - .2, z), q.setFromEuler(e.set(0, R() * 6.3, 0)), new THREE.Vector3(tw, h * .66, tw)); ti.setMatrixAt(i, m);
      const hue = .2 + R() * .07, lit = .62 + R() * .14;
      for (let k = 0; k < 3; k++) {
        e.set(R() * .4, R() * 6.3, R() * .4); q.setFromEuler(e);
        const s = r * (k ? .62 + R() * .15 : 1), ox = k ? (R() - .5) * r * 1.1 : 0, oz = k ? (R() - .5) * r * 1.1 : 0, oy = k ? h * (.5 + R() * .35) : h * .68;
        m.compose(new THREE.Vector3(x + ox, g0 + oy, z + oz), q, new THREE.Vector3(s, s * .82, s)); ci.setMatrixAt(i * 3 + k, m);
        col.setHSL(hue + (R() - .5) * .02, .35, lit + (R() - .5) * .06); ci.setColorAt(i * 3 + k, col);
      }
    });
    ti.castShadow = ci.castShadow = true; ti.receiveShadow = ci.receiveShadow = true;
    scene.add(ti, ci);
  }
  // a fire: embers, flames and a flickering light; returns the light
  const fires = [];
  function fire(x, y, z, size = 1, power = 30, dist = 14, shadow = false) {
    fires.push([x, z, power]);
    const em = new THREE.Mesh(new THREE.CircleGeometry(.5 * size, 16), M.ember); em.rotation.x = -Math.PI / 2; em.position.set(x, y + .03, z); scene.add(em);
    const fl = [];
    for (let i = 0; i < 4; i++) { const f = new THREE.Mesh(new THREE.ConeGeometry((.14 + R() * .08) * size, (.6 + R() * .3) * size, 7), M.flame); f.position.set(x + (R() - .5) * .35 * size, y + .35 * size, z + (R() - .5) * .35 * size); scene.add(f); fl.push([f, R() * 6]); }
    const L = new THREE.PointLight(0xff8c3a, power, dist, 1.6); L.position.set(x, y + 1, z); scene.add(L);
    if (shadow && !small) { L.castShadow = true; L.shadow.mapSize.set(512, 512); L.shadow.bias = -.002; L.shadow.radius = 3; L.shadow.camera.near = .2; L.shadow.camera.far = dist; }
    anim.push((t) => { const k = 1 + Math.sin(t * 11) * .08 + Math.sin(t * 23.7) * .06 + (Math.random() - .5) * .08; L.intensity = power * k; fl.forEach(([f, o]) => { f.scale.set(1, .8 + Math.sin(t * 9 + o) * .25 + Math.random() * .1, 1); f.rotation.y = t * 2 + o; }); });
    return L;
  }
  // smoke rising from a chimney or a roof
  function smoke(x, y, z, n = 7) {
    if (reduce) return;
    const g = new THREE.SphereGeometry(1, 8, 6), puffs = [];
    for (let i = 0; i < n; i++) { const p = new THREE.Mesh(g, M.smoke.clone()); scene.add(p); puffs.push([p, i / n]); }
    anim.push((t) => puffs.forEach(([p, o]) => { const k = (t * .08 + o) % 1; p.position.set(x + k * 4 + Math.sin(t + o * 9) * .3, y + k * 9, z + k * 1.5); const s = .5 + k * 2.4; p.scale.set(s, s, s); p.material.opacity = .26 * (1 - k); }));
  }

  // ---------- people and animals (from Llys Rhosyr, tools/llys3d.src.js): each piece carries its colour as a tint ----------
  const linenTex = tex(128, (x, s) => { x.fillStyle = "#d8d2c4"; x.fillRect(0, 0, s, s); for (let i = 0; i < s; i += 2) { x.fillStyle = `rgba(255,255,255,${.05 + R() * .06})`; x.fillRect(0, i, s, 1); x.fillStyle = `rgba(0,0,0,${.04 + R() * .05})`; x.fillRect(i, 0, 1, s); } }, [3, 3]);
  const woolTex = tex(128, (x, s) => { x.fillStyle = "#cfc6b2"; x.fillRect(0, 0, s, s); for (let i = 0; i < 900; i++) { const px = R() * s, py = R() * s, r = 1.5 + R() * 3; x.strokeStyle = R() < .5 ? "rgba(255,250,236,.55)" : "rgba(120,108,88,.45)"; x.lineWidth = .8 + R(); x.beginPath(); x.arc(px, py, r, R() * 6, R() * 6 + 3.5); x.stroke(); } });
  const vstd = (o) => new THREE.MeshStandardMaterial(Object.assign({ roughness: .9, vertexColors: true }, o));
  Object.assign(M, { dress: vstd({ map: linenTex, roughness: .95, side: THREE.DoubleSide }), skin: vstd({ color: 0xc8977a, roughness: .62 }), coat: vstd({ roughness: .72 }), wool: vstd({ map: woolTex, roughness: 1 }),
    iron: new THREE.MeshStandardMaterial({ color: 0x2b2a28, roughness: .55, metalness: .7 }), glaze: new THREE.MeshStandardMaterial({ color: 0x6f7a35, roughness: .35 }) });
  const figBuckets = new Map();
  function add(geo, mat, m4, noShade, tint) {
    if (m4) geo.applyMatrix4(m4);
    if (geo.index) geo = geo.toNonIndexed();
    if (!geo.attributes.normal) geo.computeVertexNormals();
    if (!geo.attributes.uv) geo.setAttribute("uv", new THREE.Float32BufferAttribute(new Float32Array(geo.attributes.position.count * 2), 2));
    const p = geo.attributes.position, c = new Float32Array(p.count * 3);
    for (let i = 0; i < p.count; i++) { c[i * 3] = tint ? tint.r : 1; c[i * 3 + 1] = tint ? tint.g : 1; c[i * 3 + 2] = tint ? tint.b : 1; }
    geo.setAttribute("color", new THREE.Float32BufferAttribute(c, 3));
    for (const k of Object.keys(geo.attributes)) if (!["position", "normal", "uv", "color"].includes(k)) geo.deleteAttribute(k);
    geo.clearGroups();
    if (!figBuckets.has(mat)) figBuckets.set(mat, []);
    figBuckets.get(mat).push(geo);
  }
  const mtxF = (x, y, z, ry = 0, rx = 0, rz = 0, sc = 1) => new THREE.Matrix4().compose(new THREE.Vector3(x, y, z), new THREE.Quaternion().setFromEuler(new THREE.Euler(rx, ry, rz, "YXZ")), new THREE.Vector3(sc, sc, sc));
  const shieldG = (() => { const sh = new THREE.Shape(); sh.moveTo(-.3, .32); sh.lineTo(.3, .32); sh.quadraticCurveTo(.32, -.1, 0, -.42); sh.quadraticCurveTo(-.32, -.1, -.3, .32); return new THREE.ExtrudeGeometry(sh, { depth: .04, bevelEnabled: true, bevelSize: .015, bevelThickness: .015, bevelSegments: 1 }); })();
  const jugG = new THREE.LatheGeometry([[0, 0], [.08, 0], [.11, .08], [.1, .2], [.06, .28], [.065, .33], [0, .33]].map(([a, b]) => new THREE.Vector2(a, b)), 12);
  // an embroidered hanging: a lozenge pattern on a coloured ground, with a cross or a roundel in each
  function hanging(base, a, b, motif) {
    return tex(256, (x) => {
      x.fillStyle = base; x.fillRect(0, 0, 256, 256);
      for (let j = 0; j < 4; j++) for (let i = 0; i < 4; i++) {
        const cx = 32 + i * 64, cyy = 32 + j * 64;
        x.fillStyle = a; x.beginPath(); x.moveTo(cx, cyy - 26); x.lineTo(cx + 26, cyy); x.lineTo(cx, cyy + 26); x.lineTo(cx - 26, cyy); x.closePath(); x.fill();
        x.fillStyle = base; x.beginPath(); x.moveTo(cx, cyy - 20); x.lineTo(cx + 20, cyy); x.lineTo(cx, cyy + 20); x.lineTo(cx - 20, cyy); x.closePath(); x.fill();
        x.fillStyle = b;
        if (motif === "cross") { x.fillRect(cx - 3, cyy - 12, 6, 24); x.fillRect(cx - 12, cyy - 3, 24, 6); }
        else { x.beginPath(); x.arc(cx, cyy, 8, 0, 7); x.fill(); x.fillStyle = a; x.beginPath(); x.arc(cx, cyy, 3.5, 0, 7); x.fill(); }
      }
      for (let i = 0; i < 2600; i++) { x.fillStyle = `rgba(0,0,0,${R() * .08})`; x.fillRect(R() * 256, R() * 256, 1, 3); }
    });
  }

  // ---------- people and animals ----------
  // Simple figures, like the people in a museum model: dressed in dyed wool and linen, standing at their work or sitting at
  // the tables. Everyone faces the way given by ry (0 = facing +z, south). They are merged into the court like everything else.
  const C3 = (h) => new THREE.Color(h);
  const limb = (a, b, r0, r1, seg = 7) => {   // a tapering cylinder from point a (radius r0) to point b (radius r1)
    const va = new THREE.Vector3(...a), vb = new THREE.Vector3(...b), L = va.distanceTo(vb), g = new THREE.CylinderGeometry(r1, r0, L, seg);
    g.applyQuaternion(new THREE.Quaternion().setFromUnitVectors(new THREE.Vector3(0, 1, 0), vb.clone().sub(va).normalize()));
    g.translate((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, (a[2] + b[2]) / 2); return g;
  };
  const ball = (r, x, y, z, sx = 1, sy = 1, sz = 1, seg = 10) => { const g = new THREE.SphereGeometry(r, seg, Math.max(6, seg * .7 | 0)); g.scale(sx, sy, sz); g.translate(x, y, z); return g; };
  const boxG = (w, h, d, x, y, z) => { const g = new THREE.BoxGeometry(w, h, d); g.translate(x, y, z); return g; };
  const lathe = (pts, seg = 12) => new THREE.LatheGeometry(pts.map(([a, b]) => new THREE.Vector2(a, b)), seg);
  const DYE = { madder: 0x9a3f2c, woad: 0x4a6690, weld: 0x9c9450, fawn: 0xa6936f, grey: 0x868077, brown: 0x6a5038, green: 0x4d6640, black: 0x35322e, linen: 0xe2dccd, rust: 0x8a5532, plum: 0x5e3a4a };
  const HAIR = [0x2b1f16, 0x3d2a1b, 0x5a3c22, 0x6e5a40, 0x8a7a68, 0x231a14, 0x7a4a26];
  const leather = C3(0x3d2b1e);
  function person(x, z, ry, o = {}) {
    const y0 = o.y != null ? o.y : ground(x, z), B = mtxF(x, y0, z, ry, 0, 0, o.h || 1);
    const put = (g, mat, tint) => add(g, mat, B.clone(), false, tint);
    const tun = C3(o.tunic || DYE.fawn), hose = C3(o.hose || DYE.brown), hair = C3(o.hair || HAIR[(R() * HAIR.length) | 0]);
    const sit = o.sit || 0, dy = sit ? sit - .75 : 0;
    // legs, or a gown to the ground
    if (o.woman && !sit) put(lathe([[0, .02], [.3, .02], [.27, .3], [.22, .7], [.17, .98], [.2, 1.2], [.21, 1.34], [.16, 1.44], [.07, 1.5], [0, 1.5]]), M.dress, tun);
    else {
      for (const sx of [-.09, .09]) {
        if (sit) { put(limb([sx, sit + .07, -.02], [sx * 1.1, sit + .08, .44], .1, .08), M.dress, tun); put(limb([sx * 1.1, sit + .05, .44], [sx * 1.1, .08, .47], .062, .052), M.dress, o.woman ? tun : hose); put(boxG(.1, .08, .22, sx * 1.1, .04, .52), M.coat, leather); }
        else { put(limb([sx, .06, 0], [sx, .62, 0], .052, .066), M.dress, hose); put(boxG(.1, .08, .23, sx, .04, .05), M.coat, leather); }
      }
      const body = sit ? [[0, .82], [.21, .82], [.19, .95], [.18, 1.0], [.2, 1.2], [.22, 1.36], [.17, 1.45], [.07, 1.5], [0, 1.5]]
        : [[0, .5], [.26, .5], [.23, .62], [.2, .85], [.18, 1.0], [.2, 1.2], [.22, 1.36], [.17, 1.45], [.07, 1.5], [0, 1.5]];
      const g = lathe(body.map(([a, b]) => [a, b + (sit ? dy : 0)])); g.scale(1, 1, .74); put(g, M.dress, tun);
      if (!o.woman) { const bt = new THREE.TorusGeometry(.185, .018, 5, 16); bt.rotateX(Math.PI / 2); bt.scale(1, 1, .74); bt.translate(0, 1.0 + dy, 0); put(bt, M.coat, leather); }
    }
    if (o.woman && sit) { const g = lathe([[0, .82], [.22, .82], [.18, 1.0], [.2, 1.2], [.21, 1.34], [.16, 1.44], [.07, 1.5], [0, 1.5]].map(([a, b]) => [a, b + dy])); g.scale(1, 1, .74); put(g, M.dress, tun); }
    // arms
    const arm = (side, el, hd) => { const sh = [side * .2, 1.38 + dy, 0]; put(limb(sh, el, .058, .05), M.dress, tun); put(limb(el, hd, .048, .04), M.dress, tun); put(ball(.045, ...hd), M.skin); };
    const pose = o.arms || (sit ? "table" : "down");
    for (const sd of [-1, 1]) {
      if (pose === "table") arm(sd, [sd * .25, .86, .18], [sd * .14, .87, .44]);
      else if (pose === "work") arm(sd, [sd * .25, 1.12 + dy, .16], [sd * .1, 1.0 + dy, .4]);
      else if (pose === "spear") arm(sd, sd > 0 ? [.27, 1.1, .1] : [-.27, 1.1, .08], sd > 0 ? [.3, 1.2, .24] : [-.24, 1.02, .26]);
      else if (pose === "hold" && sd > 0) arm(sd, [.26, 1.1 + dy, .14], [.24, 1.18 + dy, .36]);
      else arm(sd, [sd * .25, 1.1 + dy, .02], [sd * .25, .86 + dy, .05]);
    }
    // head
    put(limb([0, 1.47 + dy, 0], [0, 1.58 + dy, .01], .05, .048), M.skin);
    put(ball(.1, 0, 1.67 + dy, .015, .92, 1.12, 1), M.skin); put(ball(.024, 0, 1.655 + dy, .108), M.skin);
    if (o.woman) {   // a linen veil (a wimple at court), or a hood
      const v = new THREE.SphereGeometry(.118, 12, 9, Math.PI / 2 + 1.05, Math.PI * 2 - 2.1, 0, 2.3); v.scale(.95, 1.1, 1); v.translate(0, 1.69 + dy, -.005); put(v, M.dress, C3(o.veil || DYE.linen));
      put(limb([0, 1.62 + dy, -.05], [0, 1.4 + dy, -.1], .1, .17, 10), M.dress, C3(o.veil || DYE.linen));
    } else if (o.hood) {
      const v = new THREE.SphereGeometry(.125, 12, 9, Math.PI / 2 + .95, Math.PI * 2 - 1.9, 0, 2.2); v.scale(.95, 1.1, 1); v.translate(0, 1.69 + dy, -.01); put(v, M.dress, C3(o.hood));
      put(lathe([[.24, 1.32], [.2, 1.42], [.12, 1.52], [0, 1.55]].map(([a, b]) => [a, b + dy])), M.dress, C3(o.hood));
    } else {
      put(new THREE.SphereGeometry(.106, 12, 6, 0, Math.PI * 2, 0, 1.0).scale(.95, 1.1, 1).translate(0, 1.685 + dy, .005), M.coat, hair);
      const bk = new THREE.SphereGeometry(.108, 12, 8, Math.PI / 2 + .95, Math.PI * 2 - 1.9, 0, 2.0); bk.scale(.95, 1.1, 1); bk.translate(0, 1.685 + dy, 0); put(bk, M.coat, hair);
      if (o.beard) put(ball(.068, 0, 1.6 + dy, .055, 1, 1.15, .8), M.coat, hair);
    }
    if (o.cloak) {   // a cloak, open at the front, pinned at the shoulder
      const ch = sit ? .72 : 1.02, g = new THREE.CylinderGeometry(.205, sit ? .27 : .33, ch, 16, 1, true, Math.PI * .36, Math.PI * 1.28); g.scale(1, 1, .82); g.translate(0, 1.44 + dy - ch / 2, -.02); put(g, M.dress, C3(o.cloak));
      put(ball(.025, .16, 1.42 + dy, .1), M.gold);
    }
    if (pose === "spear") { put(limb([.3, .02, .27], [.3, 2.35, .27], .02, .018), M.oak); put(limb([.3, 2.35, .27], [.3, 2.58, .27], .03, .002, 5), M.iron); const sg = shieldG.clone(); sg.scale(1.15, 1.15, 1); sg.translate(-.28, 1.0, .2); put(sg, o.shield || M.red); }
    if (pose === "hold" && o.jug) put(jugG.clone().translate(.24, 1.02 + dy, .38), M.glaze);
    if (!o.free) posts.push([x, z, sit ? .26 : .3]);
  }
  // a horse of the Welsh kind, small and strong (about 14 hands)
  function horse(x, z, ry, coat, saddle) {
    const B = mtxF(x, ground(x, z), z, ry), c = C3(coat), dk = C3(0x1e1915), put = (g, m, t) => add(g, m, B.clone(), false, t);
    const bd = new THREE.CapsuleGeometry(.3, .85, 4, 12); bd.rotateX(Math.PI / 2); bd.scale(1, 1.12, 1); bd.translate(0, 1.04, 0); put(bd, M.coat, c);
    put(ball(.3, 0, 1.08, .45, .95, 1.05, 1), M.coat, c); put(ball(.31, 0, 1.07, -.45, 1, 1.02, 1), M.coat, c);
    put(limb([0, 1.15, .55], [0, 1.58, .88], .21, .13, 9), M.coat, c);
    put(limb([0, 1.66, .86], [0, 1.36, 1.13], .1, .07, 9), M.coat, c); put(ball(.075, 0, 1.36, 1.13, 1, .9, 1.1), M.coat, C3(0x2a221c));
    for (const s of [-1, 1]) put(limb([s * .05, 1.7, .84], [s * .06, 1.82, .82], .03, .005, 5), M.coat, c);
    put(limb([0, 1.28, .5], [0, 1.74, .83], .045, .035, 5), M.coat, dk);
    for (const [lx, lz] of [[-.15, .48], [.15, .48], [-.15, -.5], [.15, -.5]]) {
      put(limb([lx, .98, lz], [lx, .5, lz + (lz < 0 ? -.04 : 0)], .085, .055), M.coat, c);
      put(limb([lx, .5, lz + (lz < 0 ? -.04 : 0)], [lx, .06, lz], .045, .042), M.coat, lz > 0 && coat === 0x6b3d22 ? C3(0x1c1612) : c);
      put(ball(.055, lx, .04, lz + .01, 1, .7, 1.1), M.coat, dk);
    }
    put(limb([0, 1.25, -.78], [0, .58, -.9], .07, .03), M.coat, dk);
    if (saddle) { put(boxG(.66, .04, .7, 0, 1.36, -.02), M.dress, C3(DYE.madder)); put(boxG(.5, .12, .56, 0, 1.42, -.02), M.coat, leather); }
    posts.push([x + Math.sin(ry) * .2, z + Math.cos(ry) * .2, .65]);
  }
  // hounds: tall, lean greyhounds and a rough-coated hound; lying by the fire, or standing
  function hound(x, z, ry, coat, lying, y0) {
    const B = mtxF(x, y0 != null ? y0 : ground(x, z), z, ry), c = C3(coat), put = (g, m) => add(g, m, B.clone(), false, c);
    if (lying) {
      const bd = new THREE.CapsuleGeometry(.14, .42, 4, 10); bd.rotateX(Math.PI / 2); bd.scale(1.15, .85, 1); bd.translate(0, .14, 0); put(bd, M.coat);
      put(limb([-.08, .07, .2], [-.06, .05, .5], .035, .03), M.coat); put(limb([.08, .07, .2], [.06, .05, .5], .035, .03), M.coat);
      put(ball(.17, .03, .17, -.24, 1.1, .9, 1.1), M.coat); put(ball(.16, 0, .19, .2, 1, 1, 1), M.coat);
      put(limb([0, .22, .3], [0, .2, .46], .08, .07), M.coat); put(ball(.085, 0, .17, .5, 1, .9, 1.1), M.coat); put(limb([0, .15, .54], [0, .1, .7], .055, .025), M.coat);
      for (const s of [-1, 1]) put(limb([s * .05, .22, .48], [s * .1, .16, .42], .035, .01, 4), M.coat);
      put(limb([.05, .12, -.34], [.2, .05, -.6], .03, .015), M.coat);
      return;
    }
    const bd = new THREE.CapsuleGeometry(.13, .42, 4, 10); bd.rotateX(Math.PI / 2); bd.translate(0, .55, 0); put(bd, M.coat);
    put(ball(.16, 0, .53, .2, .85, 1.15, 1), M.coat);
    put(limb([0, .6, .3], [0, .8, .42], .075, .06), M.coat); put(limb([0, .82, .4], [0, .74, .62], .07, .028), M.coat);
    for (const s of [-1, 1]) put(limb([s * .04, .86, .41], [s * .07, .84, .34], .03, .01, 4), M.coat);
    for (const [lx, lz] of [[-.07, .22], [.07, .22], [-.07, -.25], [.07, -.25]]) put(limb([lx, .52, lz], [lx, .02, lz + (lz < 0 ? -.05 : .02)], .04, .022), M.coat);
    put(limb([0, .58, -.36], [0, .3, -.58], .025, .012), M.coat);
    posts.push([x, z, .35]);
  }
  // sheep, white-faced like the Welsh Mountain breed, some grazing with their heads down; and black cattle
  function sheep(x, z, ry, k) {
    const B = mtxF(x, ground(x, z), z, ry, 0, 0, .9 + R() * .2), fl = C3(k < .12 ? 0x4a3a2c : k < .2 ? 0xa59a88 : 0xf2ecdf), face = C3(k < .12 ? 0x2a211a : 0xb4a58c), put = (g, m, t) => add(g, m, B.clone(), true, t);
    put(ball(.4, 0, .55, 0, .82, .78, 1.15, 12), M.wool, fl);
    const graze = R() < .6;
    put(limb([0, .62, .3], graze ? [0, .42, .5] : [0, .72, .5], .16, .12), M.wool, fl); put(limb(graze ? [0, .42, .5] : [0, .72, .5], graze ? [0, .2, .64] : [0, .74, .66], .085, .055), M.coat, face);
    put(ball(.075, 0, graze ? .2 : .74, graze ? .64 : .66, .85, .9, 1.1), M.coat, face); for (const s of [-1, 1]) put(limb([s * .05, graze ? .4 : .78, graze ? .52 : .55], [s * .13, graze ? .38 : .76, graze ? .5 : .52], .022, .01, 4), M.coat, face);
    for (const [lx, lz] of [[-.13, .22], [.13, .22], [-.13, -.24], [.13, -.24]]) put(limb([lx, .35, lz], [lx, .01, lz], .04, .03, 5), M.coat, C3(0x2a2420));
  }
  function cow(x, z, ry) {
    const B = mtxF(x, ground(x, z), z, ry), c = C3(0x1f1c1a), put = (g, m, t) => add(g, m, B.clone(), true, t || c);
    const bd = new THREE.CapsuleGeometry(.4, 1.0, 4, 12); bd.rotateX(Math.PI / 2); bd.scale(1, 1.08, 1); bd.translate(0, .98, 0); put(bd, M.coat);
    const graze = R() < .5;
    put(limb([0, 1.05, .7], graze ? [0, .45, 1.05] : [0, 1.0, 1.05], .24, .17, 9), M.coat); put(ball(.15, 0, graze ? .35 : .92, graze ? 1.12 : 1.18, .9, 1, 1.25), M.coat);
    for (const s of [-1, 1]) put(limb([s * .1, graze ? .52 : 1.08, graze ? 1.04 : 1.08], [s * .3, graze ? .6 : 1.2, graze ? 1.0 : 1.04], .03, .01, 5), M.coat, C3(0xd6cbb0));
    for (const [lx, lz] of [[-.2, .5], [.2, .5], [-.2, -.52], [.2, -.52]]) put(limb([lx, .8, lz], [lx, .02, lz], .085, .055), M.coat);
    put(limb([0, 1.2, -.85], [0, .45, -.95], .04, .03, 5), M.coat);
  }
  function goose(x, z, ry) {
    const B = mtxF(x, ground(x, z), z, ry, 0, 0, .9 + R() * .2), put = (g, m, t) => add(g, m, B.clone(), true, t);
    const w = C3(R() < .7 ? 0xf2efe6 : 0x9a948a);
    put(ball(.2, 0, .3, 0, .78, .72, 1.25), M.coat, w); put(limb([0, .36, .18], [0, .62, .25], .05, .04), M.coat, w); put(ball(.055, 0, .65, .27), M.coat, w);
    put(limb([0, .64, .3], [0, .62, .38], .022, .006, 5), M.coat, C3(0xe08a2a));
    for (const s of [-1, 1]) put(limb([s * .06, .16, 0], [s * .06, .0, .02], .015, .012, 4), M.coat, C3(0xe08a2a));
  }

  // ---------- the land ----------
  const base = S.land ? landHeights(S.land, S.landZero || [0, 0]) : () => 0;
  const ground = (x, z) => (S.shape ? S.shape(x, z, base(x, z)) : base(x, z));
  const floor = S.floor ? (x, z) => S.floor(x, z, ground) : ground;
  {
    // two pieces: the whole valley, and a finer piece over the court itself so that moats and banks are sharp.
    // Under the fine piece the coarse one is sunk out of sight.
    const size = S.land ? S.land.size : 1100, N = small ? 150 : 230, fine = S.fine || 0, FN = Math.round(fine / (small ? 1.25 : .9));
    const landM = new THREE.MeshStandardMaterial({ vertexColors: true, map: grassTex, roughness: 1 });
    const piece = (sz, n, cx, cz, sink) => {
      const g = new THREE.PlaneGeometry(sz, sz, n, n); g.rotateX(-Math.PI / 2); g.translate(cx, 0, cz);
      const p = g.attributes.position, col = [], c = new THREE.Color(), grass = new THREE.Color(0x6f8f45), dark = new THREE.Color(0x55703a);
      for (let i = 0; i < p.count; i++) {
        const x = p.getX(i), z = p.getZ(i), y = ground(x, z);
        p.setY(i, sink && fines.some(([fs, fx, fz]) => Math.abs(x - fx) < fs / 2 - 2 && Math.abs(z - fz) < fs / 2 - 2) ? y - 4 : y);
        c.copy(grass).lerp(dark, (Math.sin(x * .05) * Math.sin(z * .04) + 1) / 2 * .6);
        if (S.colour) S.colour(x, z, y, c);
        col.push(c.r, c.g, c.b);
      }
      g.setAttribute("color", new THREE.Float32BufferAttribute(col, 3)); g.computeVertexNormals();
      const land = new THREE.Mesh(g, landM); land.receiveShadow = true; scene.add(land);
    };
    surf(landM, "grass", { n: .55 });
    // more fine pieces, [size, x, z], for a second place worth seeing close (fineMore)
    const fines = (fine ? [[fine, (S.fineAt || [0, 0])[0], (S.fineAt || [0, 0])[1]]] : []).concat(S.fineMore || []);
    piece(size, N, 0, 0, fines.length > 0);
    fines.forEach(([fs, fx, fz], i) => piece(fs, i === 0 && fine ? FN : Math.round(fs / (small ? 2 : 1.4)), fx, fz, false));
    // the sky
    const sky = new THREE.Mesh(new THREE.SphereGeometry(2400, 32, 16), new THREE.ShaderMaterial({
      side: THREE.BackSide, depthWrite: false, fog: false,
      uniforms: { top: { value: new THREE.Color(look.top) }, mid: { value: new THREE.Color(look.mid) }, low: { value: new THREE.Color(look.low) } },
      vertexShader: "#include <common>\n#include <logdepthbuf_pars_vertex>\nvarying vec3 v;void main(){v=normalize(position);gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);\n#include <logdepthbuf_vertex>\n}",
      fragmentShader: "#include <logdepthbuf_pars_fragment>\nuniform vec3 top,mid,low;varying vec3 v;void main(){\n#include <logdepthbuf_fragment>\nfloat h=v.y;vec3 c=h>.1?mix(mid,top,smoothstep(.1,.7,h)):mix(low,mid,smoothstep(-.02,.1,h));gl_FragColor=vec4(c,1.);}",
    }));
    sky.renderOrder = -1; scene.add(sky);   // drawn first, so far mountains beyond its sphere (S.far) still show
    // soft light from the whole sky (and the green land below it) on every surface, as Llys Rhosyr has
    try {
      const es = new THREE.Scene(); es.add(sky.clone());
      const gnd = new THREE.Mesh(new THREE.CircleGeometry(2000, 24), new THREE.MeshBasicMaterial({ color: 0x4d5e36 })); gnd.rotation.x = -Math.PI / 2; gnd.position.y = -40; es.add(gnd);
      const pm = new THREE.PMREMGenerator(renderer); scene.environment = pm.fromScene(es, 0, 1, 3000).texture; pm.dispose();
    } catch (e) { /* the hemisphere light is enough */ }
    // clouds: soft puffs painted on a canvas, laid flat high up
    const cloudTex = tex(256, (x, s) => {
      x.clearRect(0, 0, s, s);
      for (let i = 0; i < 14; i++) {
        const cx = s * (.2 + R() * .6), cyy = s * (.35 + R() * .3), r = s * (.1 + R() * .16), gr = x.createRadialGradient(cx, cyy, 0, cx, cyy, r);
        gr.addColorStop(0, "rgba(255,255,255,.55)"); gr.addColorStop(1, "rgba(255,255,255,0)"); x.fillStyle = gr; x.fillRect(0, 0, s, s);
      }
    });
    cloudTex.wrapS = cloudTex.wrapT = THREE.ClampToEdgeWrapping;
    const cm = new THREE.MeshBasicMaterial({ map: cloudTex, transparent: true, opacity: .8, depthWrite: false, fog: false });
    for (let i = 0; i < 26; i++) { const c2 = new THREE.Mesh(new THREE.PlaneGeometry(260 + R() * 260, 160 + R() * 120), cm); c2.rotation.x = Math.PI / 2; c2.rotation.z = R() * 3; const a = R() * 6.3, r = 350 + R() * 900; c2.position.set(Math.cos(a) * r, 260 + R() * 120, Math.sin(a) * r); scene.add(c2); }
  }

  // ---------- light ----------
  const hemi = new THREE.HemisphereLight(0xdfe8f2, 0x6a5a3c, look.hemi * .35); scene.add(hemi);
  const sun = new THREE.DirectionalLight(0xfff0d8, look.sunI);
  sun.position.set(...look.sun); sun.target.position.set(0, 0, 0); scene.add(sun, sun.target);
  sun.castShadow = true; sun.shadow.mapSize.set(small ? 1024 : 2048, small ? 1024 : 2048);
  const sr = S.shadow || 60;
  Object.assign(sun.shadow.camera, { left: -sr, right: sr, top: sr, bottom: -sr, near: 1, far: 260 });
  sun.shadow.bias = -.0004; sun.shadow.normalBias = .04;

  // ---------- the court ----------
  const K = { THREE, scene, M, R, tex, hanging, add, limb, ball, mtxF, person, horse, hound, sheep, cow, goose, DYE, block, bblock, cyl, wallSeg, wallLine, framed, framedBox, logWall, table, bench, along, roof, trees, fire, smoke, walls, posts, anim, ground, floor, small, reduce, smooth };
  S.build(K);
  // draw the gathered pieces: one mesh for each material, and one instanced mesh for all the palisade logs
  batch.forEach((list, mat) => { const g = mergeGeometries(list); if (!g) return; const me2 = new THREE.Mesh(g, mat); me2.castShadow = me2.receiveShadow = true; scene.add(me2); });
  figBuckets.forEach((list, mat) => { const g = mergeGeometries(list); if (!g) return; const fm = new THREE.Mesh(g, mat); fm.castShadow = fm.receiveShadow = true; scene.add(fm); });
  if (logs.length) {
    const lg = new THREE.LatheGeometry([new THREE.Vector2(1, 0), new THREE.Vector2(1, .9), new THREE.Vector2(.55, .955), new THREE.Vector2(.08, 1)], 8);
    const uv = lg.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setY(i, uv.getY(i) * 1.6);
    const li = new THREE.InstancedMesh(lg, M.logs, logs.length), m4 = new THREE.Matrix4(), e2 = new THREE.Euler(), q2 = new THREE.Quaternion();
    logs.forEach(([x, y, z, r, h], i) => { m4.compose(new THREE.Vector3(x, y, z), q2.setFromEuler(e2.set((R() - .5) * .03, R() * 6.3, (R() - .5) * .03)), new THREE.Vector3(r, h, r)); li.setMatrixAt(i, m4); });
    li.castShadow = li.receiveShadow = true; scene.add(li);
  }

  // ---------- tufts of grass round the court: a colour canvas and a separate black-and-white alpha map, lit alike on both sides ----------
  if (S.grass) {
    const ga = S.grassAt || { x: 0, z: 0, r: 80 }, n = small ? 2600 : 8000;
    const col = tex(128, (x, s) => { const gr = x.createLinearGradient(0, s, 0, 0); gr.addColorStop(0, "#5b7431"); gr.addColorStop(1, "#b3c872"); x.fillStyle = gr; x.fillRect(0, 0, s, s); });
    const alpha = tex(128, (x, s) => { x.fillStyle = "#000"; x.fillRect(0, 0, s, s); x.strokeStyle = "#fff"; x.lineCap = "round"; for (let i = 0; i < 26; i++) { const bx = s * (.12 + R() * .76), lean = (R() - .5) * s * .35, h = s * (.45 + R() * .5); x.lineWidth = 2 + R() * 3; x.beginPath(); x.moveTo(bx, s); x.quadraticCurveTo(bx + lean * .3, s - h * .6, bx + lean, s - h); x.stroke(); } }, null, false);
    const gm = new THREE.MeshStandardMaterial({ map: col, alphaMap: alpha, alphaTest: .5, side: THREE.DoubleSide, roughness: 1 }); gm.onBeforeCompile = noFlip;
    const q1 = new THREE.PlaneGeometry(.55, .42); q1.translate(0, .21, 0); const q2 = q1.clone(); q2.rotateY(Math.PI / 2);
    const P = [...q1.attributes.position.array, ...q2.attributes.position.array], U = [...q1.attributes.uv.array, ...q2.attributes.uv.array], Nn = [...q1.attributes.normal.array, ...q2.attributes.normal.array];
    const I = [...q1.index.array, ...Array.from(q2.index.array, (v) => v + 4)];
    const tg = new THREE.BufferGeometry(); tg.setAttribute("position", new THREE.Float32BufferAttribute(P, 3)); tg.setAttribute("uv", new THREE.Float32BufferAttribute(U, 2)); tg.setAttribute("normal", new THREE.Float32BufferAttribute(Nn, 3)); tg.setIndex(I);
    const inst = new THREE.InstancedMesh(tg, gm, n), m4 = new THREE.Matrix4(), q = new THREE.Quaternion(), c = new THREE.Color(), up = new THREE.Vector3(0, 1, 0);
    let k = 0;
    for (let tries = 0; k < n && tries < n * 4; tries++) {
      const a = R() * Math.PI * 2, r = Math.sqrt(R()) * ga.r, x = ga.x + Math.cos(a) * r, z = ga.z + Math.sin(a) * r;
      if (!S.grass(x, z)) continue;
      const sc = .7 + R() * .8; q.setFromAxisAngle(up, R() * 6.3);
      m4.compose(new THREE.Vector3(x, ground(x, z) - .03, z), q, new THREE.Vector3(sc, sc * (.8 + R() * .5), sc)); inst.setMatrixAt(k, m4);
      c.setHSL(.2 + R() * .06, .3 + R() * .15, .6 + R() * .15); inst.setColorAt(k, c); k++;
    }
    inst.count = k; inst.receiveShadow = true; scene.add(inst);
  }

  // birds wheeling over the court: gulls by the sea, rooks inland (S.birds: { kind, x, z, r }; moved each frame by moveGulls)
  const BI = S.birds || null, GN = BI ? (small ? 7 : 12) : 0, gullBody = [], gull = [];
  {
    const rook = BI && BI.kind === "rook", gm = new THREE.MeshStandardMaterial({ color: rook ? 0x1d1d22 : 0xf0efe9, roughness: .7, side: THREE.DoubleSide });
    const sh = new THREE.Shape(); sh.moveTo(0, .13); sh.lineTo(.3, .11); sh.lineTo(.74, -.03); sh.lineTo(.6, -.08); sh.lineTo(.3, -.1); sh.lineTo(0, -.1);
    const wr = new THREE.ShapeGeometry(sh); wr.rotateX(Math.PI / 2); const wl = wr.clone(); wl.scale(-1, 1, 1);
    const tip = new THREE.Color(rook ? 0x111114 : 0x3a3a3c), white = new THREE.Color(1, 1, 1);
    for (const w of [wr, wl]) { const p = w.attributes.position, c = new Float32Array(p.count * 3); for (let i = 0; i < p.count; i++) { const k = Math.abs(p.getX(i)) > .58 ? tip : white; c.set([k.r, k.g, k.b], i * 3); } w.setAttribute("color", new THREE.Float32BufferAttribute(c, 3)); }
    const wmat = gm.clone(); wmat.vertexColors = true;
    const bodyG = new THREE.SphereGeometry(.065, 8, 6); bodyG.scale(1, .9, 3.4);
    for (const [g, m] of [[bodyG, gm], [wr, wmat], [wl, wmat]]) { if (!GN) break; const im = new THREE.InstancedMesh(g, m, GN); im.frustumCulled = false; scene.add(im); gullBody.push(im); }
    for (let i = 0; i < GN; i++) gull.push({ c: [BI.x + (R() - .5) * BI.r, ground(BI.x, BI.z) + 16 + R() * 34, BI.z + (R() - .5) * BI.r], r: 25 + R() * 70, w: (R() < .5 ? -1 : 1) * (.09 + R() * .08), a: R() * 6.3, ph: R() * 9 });
  }
  const gM = new THREE.Matrix4(), gW = new THREE.Matrix4(), gQ = new THREE.Quaternion(), gE = new THREE.Euler(), gP = new THREE.Vector3(), gS = new THREE.Vector3(1.4, 1.4, 1.4);
  function moveGulls(t) {
    gull.forEach((b, i) => {
      const a = b.a + t * b.w, sg = Math.sign(b.w);
      gP.set(b.c[0] + Math.cos(a) * b.r, b.c[1] + Math.sin(t * .3 + b.ph) * 3, b.c[2] + Math.sin(a) * b.r);
      gQ.setFromEuler(gE.set(0, Math.atan2(-Math.sin(a) * sg, Math.cos(a) * sg), -sg * .32, "YXZ"));
      gM.compose(gP, gQ, gS); gullBody[0].setMatrixAt(i, gM);
      const flap = (Math.sin(t * 7.5 + b.ph) * .5) * (Math.sin(t * .5 + b.ph) > .25 ? 1 : .12) + .1;
      gullBody[1].setMatrixAt(i, gW.makeRotationZ(flap).premultiply(gM)); gullBody[2].setMatrixAt(i, gW.makeRotationZ(-flap).premultiply(gM));
    });
    for (const im of gullBody) im.instanceMatrix.needsUpdate = true;
  }

  // ---------- the stops: a gold marker over each, and the panel that tells about it ----------
  const STOPS = S.STOPS;
  const stops = D.stops.filter((s) => STOPS[s.id]);
  const marks = [];
  stops.forEach((s, i) => {
    const [[x, z], [lx, ly, lz]] = STOPS[s.id], dx = lx - x, dz = lz - z, L = Math.hypot(dx, dz);
    const mx = x + dx / L * 1.6, mz = z + dz / L * 1.6;
    const m = new THREE.Mesh(new THREE.OctahedronGeometry(.15), M.mark);
    m.position.set(mx, floor(x, z) + 2.1, mz); m.userData.i = i; m.userData.y = m.position.y; scene.add(m); marks.push(m);
  });

  // ---------- the walker ----------
  const me = { x: S.START.x, z: S.START.z, yaw: S.START.yaw || 0, pitch: -.02, vx: 0, vz: 0 }, look2 = { yaw: me.yaw, pitch: me.pitch };
  const eye = (x, z) => floor(x, z) + 1.65;
  const lim = S.bound || 420;
  function bump(nx, nz, ox, oz) {
    const r = .35, fy = floor(nx, nz);
    for (let k = 0; k < 2; k++) {
      walls.forEach(([x1, z1, x2, z2, ht, b, t]) => {
        if (fy + 1.6 < b || fy + .3 > t) return;   // walls below your feet or above your head do not stop you
        const vx = x2 - x1, vz = z2 - z1, L2 = vx * vx + vz * vz; let tt = ((nx - x1) * vx + (nz - z1) * vz) / L2; tt = Math.max(0, Math.min(1, tt));
        const px = x1 + vx * tt, pz = z1 + vz * tt, dx = nx - px, dz = nz - pz, d = Math.hypot(dx, dz), min = r + ht;
        if (d < min && d > 1e-6) { nx = px + dx / d * min; nz = pz + dz / d * min; }
      });
      posts.forEach(([px, pz, pr]) => { const dx = nx - px, dz = nz - pz, d = Math.hypot(dx, dz), min = r + pr; if (d < min && d > 1e-6) { nx = px + dx / d * min; nz = pz + dz / d * min; } });
    }
    if (S.blocked && S.blocked(nx, nz) && !S.blocked(ox, oz)) return [ox, oz];
    if (Math.abs(floor(nx, nz) - floor(ox, oz)) > .9) return [ox, oz];   // no stepping off a bridge or up a wall
    const far = Math.hypot(nx, nz); if (far > lim) { nx *= lim / far; nz *= lim / far; }
    return [nx, nz];
  }

  // is the straight way from a to b through a wall? then going to a stop fades out and in, instead of flying through it
  function pathBlocked(ax, az, bx, bz) {
    const ex = bx - ax, ez = bz - az;
    for (const [x1, z1, x2, z2, , b, t] of walls) {
      const fx = x2 - x1, fz = z2 - z1, den = ex * fz - ez * fx; if (Math.abs(den) < 1e-9) continue;
      const u = ((x1 - ax) * fz - (z1 - az) * fx) / den, v = ((x1 - ax) * ez - (z1 - az) * ex) / den;
      if (u <= .02 || u >= .98 || v < 0 || v > 1) continue;
      const fy = floor(ax + ex * u, az + ez * u);
      if (t > fy + 1.0 && b < fy + 1.6) return true;
    }
    return false;
  }

  // ---------- sound: made in the browser (the wind, the sea, birds, the fire, a harp in the hall) ----------
  let AC = null, snd = null, soundOn = true;
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  function startSound() {
    if (AC) { if (soundOn && AC.state === "suspended") AC.resume(); return; }
    if (!soundOn) return;
    try { AC = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { return; }
    const sr = AC.sampleRate, nb = AC.createBuffer(1, sr * 4, sr), d = nb.getChannelData(0);
    let b0 = 0, b1 = 0, b2 = 0; for (let i = 0; i < d.length; i++) { const w = Math.random() * 2 - 1; b0 = .99765 * b0 + w * .099; b1 = .963 * b1 + w * .2965; b2 = .57 * b2 + w * 1.0527; d[i] = (b0 + b1 + b2 + w * .1848) * .2; }
    const master = AC.createGain(); master.gain.value = .9; master.connect(AC.destination);
    const loop = (f, q, type = "bandpass") => { const s = AC.createBufferSource(); s.buffer = nb; s.loop = true; s.playbackRate.value = .5 + Math.random() * .1; const fl2 = AC.createBiquadFilter(); fl2.type = type; fl2.frequency.value = f; fl2.Q.value = q; const g = AC.createGain(); g.gain.value = 0; s.connect(fl2); fl2.connect(g); g.connect(master); s.start(); return { g, f: fl2 }; };
    // the hall's talk: noise shaped by the rise and fall of many voices; a stream where there is water near
    snd = { wind: loop(500, .6), sea: loop(260, .4, "lowpass"), rumble: loop(180, .7, "lowpass"), talk: [loop(420, 1.4), loop(950, 1.6)], brook: loop(2400, .5), master, crackT: 0, harpT: 2, note: 0, birdT: 3, talkT: 0, larkT: 3, larkOn: 0, callT: 5, bleatT: 5, barkT: 6, songT: 4 };
  }
  function crackle(vol) {
    const len = .02 + Math.random() * .05, b = AC.createBuffer(1, Math.ceil(AC.sampleRate * len), AC.sampleRate), d = b.getChannelData(0);
    for (let i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / d.length, 3);
    const s = AC.createBufferSource(); s.buffer = b; const f = AC.createBiquadFilter(); f.type = "highpass"; f.frequency.value = 900 + Math.random() * 2500; const g = AC.createGain(); g.gain.value = vol * (.2 + Math.random() * .5);
    s.connect(f); f.connect(g); g.connect(snd.master); s.start();
  }
  function chirp(vol) {   // a small bird, somewhere in the hedges
    const t = AC.currentTime, n = 2 + (Math.random() * 4 | 0), base = 2600 + Math.random() * 1800;
    for (let i = 0; i < n; i++) {
      const o = AC.createOscillator(), g = AC.createGain(), t0 = t + i * (.11 + Math.random() * .05);
      o.frequency.setValueAtTime(base, t0); o.frequency.exponentialRampToValueAtTime(base * (1.3 + Math.random() * .4), t0 + .07);
      g.gain.setValueAtTime(0, t0); g.gain.linearRampToValueAtTime(vol, t0 + .015); g.gain.exponentialRampToValueAtTime(.0005, t0 + .09);
      o.connect(g); g.connect(snd.master); o.start(t0); o.stop(t0 + .1);
    }
  }
  // a short tone: a sine (or other wave) sliding from f0 to f1, through a band filter, with a quick rise and a fall
  function tone(type, f0, f1, dur, vol, bp, q = 2, vib = 0) {
    const t = AC.currentTime, o = AC.createOscillator(), g = AC.createGain(), f = AC.createBiquadFilter();
    o.type = type; o.frequency.setValueAtTime(f0, t); o.frequency.exponentialRampToValueAtTime(f1, t + dur * .7);
    if (vib) { const l = AC.createOscillator(), lg = AC.createGain(); l.frequency.value = 7 + Math.random() * 2; lg.gain.value = vib; l.connect(lg); lg.connect(o.frequency); l.start(t); l.stop(t + dur + .05); }
    f.type = "bandpass"; f.frequency.value = bp || f0; f.Q.value = q;
    g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(vol, t + Math.min(.03, dur * .2)); g.gain.exponentialRampToValueAtTime(.0005, t + dur);
    o.connect(f); f.connect(g); g.connect(snd.master); o.start(t); o.stop(t + dur + .05);
  }
  // a blackbird's song: a few fluting phrases, rising and falling
  function blackbird(vol) {
    const n = 4 + (Math.random() * 5 | 0); let at = 0;
    for (let i = 0; i < n; i++) { const f0 = 1500 + Math.random() * 1300, f1 = f0 * (.75 + Math.random() * .6), d = .08 + Math.random() * .16; setTimeout(() => AC && tone("sine", f0, f1, d, vol, f0, .8, Math.random() < .3 ? 60 : 0), at * 1000); at += d + .02 + Math.random() * .06; }
  }
  const SCALE = [146.83, 164.81, 174.61, 196, 220, 246.94, 261.63, 293.66, 329.63, 349.23, 392];   // D, in the Dorian mode
  const TUNE = [7, 5, 4, 5, 7, 7, 8, 7, 5, 4, 2, 4, 5, 4, 2, 0, 2, 4, 5, 7, 5, 4, 2, 4];
  function pluck(freq, vol) {   // a plucked string (Karplus and Strong)
    const sr = AC.sampleRate, n = Math.round(sr / freq), len = Math.ceil(sr * 2.6), b = AC.createBuffer(1, len, sr), d = b.getChannelData(0), ring = new Float32Array(n);
    for (let i = 0; i < n; i++) ring[i] = Math.random() * 2 - 1;
    let p = 0; for (let i = 0; i < len; i++) { const nxt = (p + 1) % n; const v = (ring[p] + ring[nxt]) * .4985; d[i] = ring[p]; ring[p] = v; p = nxt; }
    const s = AC.createBufferSource(); s.buffer = b; const g = AC.createGain(); g.gain.value = vol; const f = AC.createBiquadFilter(); f.type = "lowpass"; f.frequency.value = 2600;
    s.connect(f); f.connect(g); g.connect(snd.master); s.start();
  }
  function sound(dt, ind) {
    if (!AC || !snd) return;
    const t = AC.currentTime, out = 1 - ind;
    let fireV = 0; for (const [x, z, pw] of fires) fireV = Math.max(fireV, clamp(1.3 - Math.hypot(me.x - x, me.z - z) / (pw > 15 ? 8 : 4), 0, 1) * (pw > 15 ? 1 : .5));
    snd.wind.g.gain.setTargetAtTime((1 - ind * .8) * (.3 + .17 * Math.sin(t * .23) + .1 * Math.sin(t * .71)), t, .4);
    snd.wind.f.frequency.setTargetAtTime(380 + 160 * Math.sin(t * .17), t, .5);
    snd.sea.g.gain.setTargetAtTime((S.sea || 0) * (1 - ind * .7) * (.25 + .15 * Math.sin(t * .45)), t, .5);
    snd.rumble.g.gain.setTargetAtTime(fireV * .6, t, .3);
    snd.crackT -= dt; if (snd.crackT < 0 && fireV > .02) { crackle(fireV); snd.crackT = Math.random() * .22; }
    // running water: the stream or the river, when the walker is near it (S.water(x, z) gives the distance to it)
    const wd = S.water ? S.water(me.x, me.z) : 1e9; snd.brook.g.gain.setTargetAtTime(out * clamp(1 - wd / 40, 0, 1) * .16, t, .5);
    // the talk of the household in the hall, rising and falling, with the harp
    const H = S.harp, inHall = H && ind > .5 && Math.hypot(me.x - H.x, me.z - H.z) < H.r;
    snd.talkT -= dt; if (snd.talkT < 0) { snd.talkT = .1 + Math.random() * .16; const tv = inHall && S.people ? .26 : 0; snd.talk[0].g.gain.setTargetAtTime(tv * (.25 + Math.random() * .75), t, .05); snd.talk[1].g.gain.setTargetAtTime(tv * .45 * Math.random(), t, .04); }
    if (inHall) { snd.harpT -= dt; if (snd.harpT < 0) { const n = TUNE[snd.note++ % TUNE.length]; const v = clamp(1.2 - Math.hypot(me.x - H.x, me.z - H.z) / H.r, .15, 1) * .45; pluck(SCALE[n], v); if (snd.note % 4 === 1) pluck(SCALE[Math.max(0, n - 4)] / 2, v * .55); snd.harpT = (snd.note % 8 === 0 ? 1.1 : .52) * (1 + (Math.random() - .5) * .08); } }
    if (out > .3 && !reduce) {
      // a skylark high over the fields, small birds in the hedges, a blackbird now and then
      snd.larkT -= dt;
      if (snd.larkT < 0) { if (snd.larkOn <= 0) snd.larkOn = 1.5 + Math.random() * 3; snd.larkOn -= dt; tone("sine", 2600 + Math.random() * 2600, 2600 + Math.random() * 3200, .05 + Math.random() * .06, .02 * out, 0, .7); snd.larkT = snd.larkOn > 0 ? .05 + Math.random() * .09 : 3 + Math.random() * 6; }
      snd.birdT -= dt; if (snd.birdT < 0) { chirp(.03 + Math.random() * .03); snd.birdT = 2.5 + Math.random() * 6; }
      snd.songT -= dt; if (snd.songT < 0) { blackbird(.03 * out); snd.songT = 9 + Math.random() * 14; }
      // gulls by the sea, rooks inland
      snd.callT -= dt;
      if (snd.callT < 0 && S.birds) { const n = 1 + (Math.random() * 3 | 0); for (let i = 0; i < n; i++) setTimeout(() => AC && (S.birds.kind === "rook" ? tone("sawtooth", 560, 380, .26, .03 * out, 900, 2.2) : tone("sawtooth", 760, 1250, .32, .028 * out, 1500, 3)), i * 380); snd.callT = 7 + Math.random() * 12; }
      // the sheep on the pasture
      if (S.flock) { snd.bleatT -= dt; if (snd.bleatT < 0) { const v = clamp(1.3 - Math.hypot(me.x - S.flock.x, me.z - S.flock.z) / 90, 0, 1) * out; if (v > .02) tone("sawtooth", 290 + Math.random() * 60, 250 + Math.random() * 40, .7, .05 * v, 1000, 2.5, 18); snd.bleatT = 4 + Math.random() * 9; } }
    }
    // the hounds
    if (S.kennel) { snd.barkT -= dt; if (snd.barkT < 0) { const v = clamp(1.2 - Math.hypot(me.x - S.kennel.x, me.z - S.kennel.z) / 60, 0, 1) * (1 - ind * .7); if (v > .03) { const n = 1 + (Math.random() * 3 | 0); for (let i = 0; i < n; i++) setTimeout(() => AC && tone("square", 420, 240, .16, .045 * v, 700, 1.5), i * 260); } snd.barkT = 8 + Math.random() * 16; } }
  }

  // ---------- the controls and the panel ----------
  const ui = document.createElement("div"); ui.className = "ll-ui";
  ui.innerHTML = '<div class="ll-panel" hidden><p class="ll-n"></p><h2 tabindex="-1"></h2><div class="ll-txt"></div><p class="ll-src"></p><div class="ll-btns">' +
    '<button type="button" class="btn" data-k="prev">← ' + T(D.ui.prev) + '</button><button type="button" class="btn solid" data-k="next">' + T(D.ui.next) + ' →</button>' +
    '<button type="button" class="ll-x" data-k="close" aria-label="' + T(D.ui.close) + '">×</button></div></div>' +
    '<div class="ll-bar"><button type="button" class="btn solid" data-k="tour">' + T(D.ui.tour) + ' →</button>' +
    '<button type="button" class="btn" data-k="snd" aria-pressed="true"></button>' +
    '<button type="button" class="btn" data-k="fs">' + T(D.ui.fs) + '</button><span class="ll-help">' + T(small || matchMedia("(pointer: coarse)").matches ? D.ui.helpTouch : D.ui.help) + "</span></div>" +
    (S.plan ? '<canvas class="ll-plan" width="200" height="160" aria-hidden="true"></canvas>' : "") +
    '<div class="ll-stick" aria-hidden="true"><i></i></div><div class="ll-fade"></div>';
  host.appendChild(ui);
  const panel = ui.querySelector(".ll-panel"), stick = ui.querySelector(".ll-stick"), knob = stick.querySelector("i"), fade = ui.querySelector(".ll-fade"), sndB = ui.querySelector('[data-k="snd"]');
  const setSnd = () => { sndB.textContent = (soundOn ? "♪ " : "") + T(soundOn ? D.ui.soundOff : D.ui.soundOn); sndB.setAttribute("aria-pressed", soundOn); };
  setSnd();
  let cur = -1, dismissed = -1, fly = null;
  const esc = (p) => p.replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));

  function showStop(i) {
    cur = i; const s = stops[i];
    panel.hidden = false; panel.scrollTop = 0;
    panel.querySelector(".ll-n").textContent = T(D.ui.stop).replace("{n}", i + 1).replace("{of}", stops.length);
    panel.querySelector("h2").textContent = T(s.t);
    panel.querySelector(".ll-txt").innerHTML = T(s.p).map((p) => "<p>" + esc(p) + "</p>").join("");
    const src = s.src ? T(s.src) : [];
    panel.querySelector(".ll-src").textContent = src.length ? T(D.ui.src) + ": " + src.join(" · ") : "";
    panel.querySelector('[data-k="prev"]').disabled = i === 0;
    panel.querySelector('[data-k="next"]').textContent = (i === stops.length - 1 ? T(D.ui.again) : T(D.ui.next)) + " →";
  }
  let snapF = false;
  function goStop(i, instant) {
    i = (i + stops.length) % stops.length;
    const [[x, z], [lx, ly, lz]] = STOPS[stops[i].id];
    const yaw = Math.atan2(-(lx - x), -(lz - z)), pitch = Math.atan2(ly - eye(x, z), Math.hypot(lx - x, lz - z));
    let dy = yaw - me.yaw; while (dy > Math.PI) dy -= 2 * Math.PI; while (dy < -Math.PI) dy += 2 * Math.PI;
    const far = Math.hypot(x - me.x, z - me.z), jump = instant || reduce || far > 140 || pathBlocked(me.x, me.z, x, z);
    fly = { t: 0, jump, dur: jump ? .9 : Math.min(3.6, .9 + far / 16), from: { ...me }, to: { x, z, yaw: me.yaw + dy, pitch } };
    if (instant) { Object.assign(me, fly.to); look2.yaw = me.yaw; look2.pitch = me.pitch; fly = null; snapF = true; camera.position.y = 0; }
    showStop(i); dismissed = -1;
  }
  ui.addEventListener("click", (e) => {
    const b = e.target.closest("button"); if (!b) return;
    const k = b.dataset.k;
    if (k === "tour" || k === "next") goStop(cur + 1);
    else if (k === "prev") goStop(cur - 1);
    else if (k === "close") { panel.hidden = true; dismissed = cur; canvas.focus({ preventScroll: true }); }
    else if (k === "snd") { soundOn = !soundOn; setSnd(); if (soundOn) { if (!AC) startSound(); else AC.resume(); } else if (AC) AC.suspend(); }
    else if (k === "fs") { const fs = document.fullscreenElement; if (fs) document.exitFullscreen(); else if (host.requestFullscreen) host.requestFullscreen().catch(() => {}); }
  });

  // the plan of the court, with you on it (top right; bottom right on phones): tap it to go to a stop
  const plan = ui.querySelector(".ll-plan"), pc = plan && plan.getContext("2d");
  const PL = S.plan || { x: 0, z: 0, r: 60 }, PK = 72 / PL.r, PP = (x, z) => [100 + (x - PL.x) * PK, 80 + (z - PL.z) * PK];
  function drawPlan() {
    if (!pc) return;
    pc.clearRect(0, 0, 200, 160); pc.fillStyle = "rgba(8,10,16,.62)"; pc.fillRect(0, 0, 200, 160);
    if (S.planExtra) S.planExtra(pc, PP, PK);
    pc.strokeStyle = "rgba(230,220,200,.8)"; pc.lineWidth = 1.6; pc.beginPath();
    for (const [x1, z1, x2, z2] of walls) { if (Math.abs(x1 - PL.x) > PL.r * 1.5 || Math.abs(z1 - PL.z) > PL.r * 1.2) continue; const [a, b] = PP(x1, z1), [c, d] = PP(x2, z2); pc.moveTo(a, b); pc.lineTo(c, d); }
    pc.stroke();
    stops.forEach((st, i) => { const [[x, z]] = STOPS[st.id]; const [a, b] = PP(x, z); if (a < 3 || a > 197 || b < 3 || b > 157) return; pc.fillStyle = i === cur ? "#fff" : "#f2c14e"; pc.beginPath(); pc.arc(a, b, 3.2, 0, 7); pc.fill(); });
    const [a, b] = PP(clamp(me.x, PL.x - PL.r * 1.35, PL.x + PL.r * 1.35), clamp(me.z, PL.z - PL.r * 1.08, PL.z + PL.r * 1.08));
    pc.save(); pc.translate(a, b); pc.rotate(-me.yaw); pc.fillStyle = "#e8483f"; pc.beginPath(); pc.moveTo(0, -7); pc.lineTo(5, 5); pc.lineTo(0, 2); pc.lineTo(-5, 5); pc.closePath(); pc.fill(); pc.restore();
    pc.fillStyle = "rgba(230,220,200,.85)"; pc.font = "600 10px system-ui, sans-serif"; pc.fillText(cy ? "G" : "N", 188, 14); pc.beginPath(); pc.moveTo(191, 18); pc.lineTo(191, 30); pc.strokeStyle = "rgba(230,220,200,.85)"; pc.lineWidth = 1.2; pc.stroke();
  }
  if (plan) plan.addEventListener("click", (e) => {
    const r = plan.getBoundingClientRect(), x = (e.clientX - r.left) / r.width * 200, y = (e.clientY - r.top) / r.height * 160;
    let best = -1, bd = 14; stops.forEach((st, i) => { const [[sx, sz]] = STOPS[st.id]; const [a, b] = PP(sx, sz); const d = Math.hypot(a - x, b - y); if (d < bd) { bd = d; best = i; } });
    if (best >= 0) goStop(best);
  });

  const keys = {};
  canvas.addEventListener("keydown", (e) => {
    const k = e.key.toLowerCase();
    if (["w", "a", "s", "d", "arrowup", "arrowdown", "arrowleft", "arrowright", "q", "e", "shift"].includes(k)) { keys[k] = 1; e.preventDefault(); if (fly) { look2.yaw = me.yaw; look2.pitch = me.pitch; fly = null; fade.style.opacity = "0"; } }
    if (k === "n") goStop(cur + 1);
    startSound();
  });
  canvas.addEventListener("keyup", (e) => { keys[e.key.toLowerCase()] = 0; });
  canvas.addEventListener("blur", () => { for (const k in keys) keys[k] = 0; });

  let drag = null;
  const ray = new THREE.Raycaster(), ndc = new THREE.Vector2();
  canvas.addEventListener("pointerdown", (e) => { drag = { id: e.pointerId, x: e.clientX, y: e.clientY, moved: 0 }; canvas.setPointerCapture(e.pointerId); canvas.focus({ preventScroll: true }); startSound(); });
  canvas.addEventListener("pointermove", (e) => {
    if (!drag || drag.id !== e.pointerId) return;
    const dx = e.clientX - drag.x, dy = e.clientY - drag.y; drag.x = e.clientX; drag.y = e.clientY; drag.moved += Math.abs(dx) + Math.abs(dy);
    const k = e.pointerType === "touch" ? .006 : .0045;
    if (fly) { look2.yaw = me.yaw; look2.pitch = me.pitch; fly = null; fade.style.opacity = "0"; }
    look2.yaw += dx * k; look2.pitch = clamp(look2.pitch + dy * k, -1.25, 1.25);
  });
  canvas.addEventListener("pointerup", (e) => {
    if (drag && drag.moved < 6) {
      const r = canvas.getBoundingClientRect(); ndc.set((e.clientX - r.left) / r.width * 2 - 1, -(e.clientY - r.top) / r.height * 2 + 1);
      ray.setFromCamera(ndc, camera); const hit = ray.intersectObjects(marks)[0];
      if (hit) goStop(hit.object.userData.i);
    }
    drag = null;
  });
  const mv = { x: 0, y: 0 }; let sid = null;
  const stickAt = (e) => { const r = stick.getBoundingClientRect(), cx = r.left + r.width / 2, cyy = r.top + r.height / 2; let x = (e.clientX - cx) / (r.width / 2), y = (e.clientY - cyy) / (r.height / 2); const l = Math.hypot(x, y); if (l > 1) { x /= l; y /= l; } mv.x = x; mv.y = y; knob.style.transform = `translate(${x * 34}px,${y * 34}px)`; };
  stick.addEventListener("pointerdown", (e) => { sid = e.pointerId; stick.setPointerCapture(sid); stickAt(e); if (fly) { look2.yaw = me.yaw; look2.pitch = me.pitch; fly = null; fade.style.opacity = "0"; } e.preventDefault(); startSound(); });
  stick.addEventListener("pointermove", (e) => { if (e.pointerId === sid) stickAt(e); });
  const stickEnd = () => { sid = null; mv.x = mv.y = 0; knob.style.transform = ""; };
  stick.addEventListener("pointerup", stickEnd); stick.addEventListener("pointercancel", stickEnd);

  // shadows of clouds drifting over the land, the court and the mountains on the south-west wind: every lit material
  // has the sun's light dimmed where a cloud's shadow falls (world position worked out from the view position)
  const cloudT = { value: 0 };
  {
    const CSH = `uniform float ctime;
float csH(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float csN(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(csH(i),csH(i+vec2(1.,0.)),f.x),mix(csH(i+vec2(0.,1.)),csH(i+vec2(1.,1.)),f.x),f.y);}
float cloudShade(vec3 v){vec3 w=(vec4(v-viewMatrix[3].xyz,0.)*viewMatrix).xyz;vec2 p=(w.xz+ctime*vec2(-6.5,4.5))/520.+vec2(3.7,1.3);
float n=csN(p)*.55+csN(p*2.07+3.1)*.3+csN(p*4.3+7.7)*.15;return smoothstep(.55,.7,n);}
`;
    const LB = THREE.ShaderChunk.lights_fragment_begin.replace("getDirectionalLightInfo( directionalLight, directLight );", "getDirectionalLightInfo( directionalLight, directLight );\n\t\tdirectLight.color *= csh;");
    const done = new Set();
    scene.traverse((o) => {
      for (const m of [].concat(o.material || [])) {
        if (!m.isMeshStandardMaterial || done.has(m)) continue;
        done.add(m);
        const prev = m.onBeforeCompile, key = prev && prev !== THREE.Material.prototype.onBeforeCompile ? prev.toString() : "";
        m.onBeforeCompile = (sh, r) => {
          if (key) prev.call(m, sh, r);
          sh.uniforms.ctime = cloudT;
          sh.fragmentShader = CSH + sh.fragmentShader.replace("#include <lights_fragment_begin>", "float cmask = cloudShade(-vViewPosition), csh = 1. - .72 * cmask;\n" + LB)
            .replace("#include <aomap_fragment>", "reflectedLight.indirectDiffuse *= 1. - .3 * cmask; reflectedLight.indirectSpecular *= 1. - .3 * cmask;\n#include <aomap_fragment>");
        };
        m.customProgramCacheKey = () => key + "|cs";
        m.needsUpdate = true;
      }
    });
  }

  // ---------- the loop ----------
  function size() { const w = host.clientWidth, h = host.clientHeight; renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); }
  size(); new ResizeObserver(size).observe(host);
  let visible = true;
  new IntersectionObserver((en) => { visible = en[0].isIntersecting; if (visible) last = performance.now(); }).observe(host);
  let last = performance.now(), time = 0, fixed = null, showMarks = true;
  let slowT = 0, fastT = 0, bob = 0, indoor = 0;
  const allMats = new Set(); scene.traverse((o) => { if (o.material) (Array.isArray(o.material) ? o.material : [o.material]).forEach((m) => { if (m.isMeshStandardMaterial) allMats.add(m); }); });
  function frame(now) {
    requestAnimationFrame(frame);
    if (!visible || document.hidden) return;
    const raw = Math.min(.5, (now - last) / 1000), dt = Math.min(.05, raw); last = now; time += dt;
    // keep it smooth: lower the resolution if frames are slow, raise it again when there is room
    if (raw > .034) { slowT += raw; fastT = 0; } else if (raw < .019) { fastT += raw; slowT = 0; }
    if (slowT > 1.2 && dpr > .6) { dpr = Math.max(.6, dpr - .15); renderer.setPixelRatio(dpr); size(); slowT = 0; }
    if (fastT > 4 && dpr < maxDpr) { dpr = Math.min(maxDpr, dpr + .1); renderer.setPixelRatio(dpr); size(); fastT = 0; }
    let moving = 0;
    if (fly) {
      fly.t += raw / fly.dur; const k = fly.t >= 1 ? 1 : (1 - Math.cos(Math.PI * fly.t)) / 2;
      if (fly.jump) {   // through a wall, or far away: fade out, move, fade in
        fade.style.opacity = String(Math.sin(Math.min(1, fly.t) * Math.PI));
        if (fly.t >= .5 && !fly.done) { Object.assign(me, fly.to); fly.done = true; camera.position.y = eye(me.x, me.z); }
      } else ["x", "z", "yaw", "pitch"].forEach((p) => { me[p] = fly.from[p] + (fly.to[p] - fly.from[p]) * k; });
      if (fly.t >= 1) { Object.assign(me, fly.to); fly = null; fade.style.opacity = "0"; }
      look2.yaw = me.yaw; look2.pitch = me.pitch; me.vx = me.vz = 0;
    } else {
      // turn smoothly toward where the visitor is looking, and walk with a little weight
      const kk = 1 - Math.exp(-dt * 16);
      me.yaw += (look2.yaw - me.yaw) * kk; me.pitch += (look2.pitch - me.pitch) * kk;
      if (keys.arrowleft || keys.q) look2.yaw += 1.8 * dt;
      if (keys.arrowright || keys.e) look2.yaw -= 1.8 * dt;
      const run = keys.shift ? 2.1 : 1;
      let f = (keys.w || keys.arrowup ? 1 : 0) - (keys.s || keys.arrowdown ? 1 : 0) - mv.y;
      let s = (keys.d ? 1 : 0) - (keys.a ? 1 : 0) + mv.x;
      const l = Math.max(1, Math.hypot(f, s)); f /= l; s /= l;
      const tx = (-Math.sin(me.yaw) * f + Math.cos(me.yaw) * s) * 3.4 * run, tz = (-Math.cos(me.yaw) * f - Math.sin(me.yaw) * s) * 3.4 * run;
      const a = 1 - Math.exp(-dt * 9); me.vx += (tx - me.vx) * a; me.vz += (tz - me.vz) * a;
      const sp = Math.hypot(me.vx, me.vz);
      if (sp > .02) { const ox = me.x, oz = me.z; [me.x, me.z] = bump(me.x + me.vx * dt, me.z + me.vz * dt, ox, oz); moving = Math.min(1, sp / 3.4); }
      stops.forEach((st, i) => { const [[x, z]] = STOPS[st.id]; if (i !== cur && i !== dismissed && Math.hypot(me.x - x, me.z - z) < 1.8) showStop(i); });
    }
    bob += dt * 9 * moving;
    // the field of view: a stop may narrow it for far views (as the eye sees mountains), and a still may set its own
    const sf = cur >= 0 && !fly ? STOPS[stops[cur].id][2] : 0, wantFov = (fixed && fixed[6]) || sf || FOV;
    if (snapF) { camera.fov = wantFov; camera.updateProjectionMatrix(); snapF = false; }
    if (Math.abs(camera.fov - wantFov) > .05) { camera.fov += (wantFov - camera.fov) * Math.min(1, dt * 2.5); camera.updateProjectionMatrix(); }
    if (fixed) { camera.position.set(fixed[0], fixed[1], fixed[2]); camera.lookAt(fixed[3], fixed[4], fixed[5]); }
    else {
      const ey = eye(me.x, me.z) + (reduce ? 0 : Math.sin(bob) * .025 * moving);
      camera.position.set(me.x, camera.position.y ? camera.position.y + (ey - camera.position.y) * Math.min(1, dt * 10) : ey, me.z);
      camera.rotation.set(me.pitch, me.yaw, 0);
    }
    // indoors or out: inside, the eye opens up to the firelight and the sky's light drops away
    const inNow = S.indoor ? (S.indoor(fixed ? fixed[0] : me.x, fixed ? fixed[2] : me.z) ? 1 : 0) : 0;
    indoor += (inNow - indoor) * Math.min(1, fixed ? 1 : dt * 2.2);
    renderer.toneMappingExposure = look.exposure * (1 + indoor * .3);
    const env = 1 - indoor * .75; for (const m of allMats) m.envMapIntensity = env;
    // the sun's shadows follow the walker, kept to whole shadow pixels so their edges do not swim
    const tx2 = (sr * 2) / sun.shadow.mapSize.x, sx = Math.round((fixed ? fixed[0] : me.x) / tx2) * tx2, sz = Math.round((fixed ? fixed[2] : me.z) / tx2) * tx2;
    sun.position.set(sx + look.sun[0], look.sun[1], sz + look.sun[2]); sun.target.position.set(sx, 0, sz); sun.target.updateMatrixWorld();
    anim.forEach((f) => f(time, dt));
    cloudT.value = time; if (GN) moveGulls(time);
    marks.forEach((m, i) => { m.rotation.y = time * 1.4 + i; m.position.y = m.userData.y + Math.sin(time * 2 + i) * .06; m.visible = showMarks && (i !== cur || !!fly) && m.position.distanceTo(camera.position) > 4; });
    sound(dt, indoor);
    if ((time * 10 | 0) % 2 === 0) drawPlan();
    renderer.render(scene, camera);
  }
  requestAnimationFrame(frame);
  host.classList.add("ready");
  camera.position.y = 0;
  canvas.focus({ preventScroll: true });
  if (soundOn) startSound();
  setTimeout(() => goStop(0), 400);
  // for making the still pictures (tools/court_stills.js): stand anywhere and look anywhere, or go back to walking
  const api = { goStop, me, view: (v) => { fixed = v; snapF = true; }, panel: (on) => { panel.hidden = !on; ui.style.display = on ? "" : "none"; showMarks = on; } };
  host.__court = api;
  return api;
}
