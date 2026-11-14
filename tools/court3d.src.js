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
   x is east and z is south, in metres. Bundle each court with three.js:
     npx esbuild court-<id>.src.js --bundle --minify --format=esm --target=es2019 --outfile=court-<id>.js
   and copy it to src/static/. Everything is made in code: no models or pictures to download. */
import * as THREE from "three";

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
  try { renderer = new THREE.WebGLRenderer({ canvas, antialias: !small, powerPreference: "high-performance" }); }
  catch (e) { host.classList.add("fail"); canvas.remove(); return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, small ? 1.5 : 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = look.exposure;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;

  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(look.fog, look.fogNear, look.fogFar);
  const camera = new THREE.PerspectiveCamera(small ? 70 : 62, 1, 0.1, 3000);
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

  // ---------- helpers for the scene ----------
  const walls = [];   // [x1, z1, x2, z2, half thickness, bottom, top]: what you bump into
  const posts = [];   // [x, z, radius]
  const anim = [];    // functions (time, dt) run every frame
  function block(w, h, d, mat, x, y, z, ry = 0, ts = 2) {
    ts = (mat.userData && mat.userData.ts) || ts;   // a material can set its own tile size in metres
    const g = new THREE.BoxGeometry(w, h, d), uv = g.attributes.uv;
    const faces = [[d, h], [d, h], [w, d], [w, d], [w, h], [w, h]];
    for (let f = 0; f < 6; f++) for (let i = 0; i < 4; i++) { const k = f * 4 + i; uv.setXY(k, uv.getX(k) * faces[f][0] / ts, uv.getY(k) * faces[f][1] / ts); }
    const m = new THREE.Mesh(g, mat); m.position.set(x, y, z); m.rotation.y = ry; m.castShadow = m.receiveShadow = true; scene.add(m); return m;
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
    if (gableMat) [-w / 2, w / 2].forEach((gx) => {
      const sh = new THREE.Shape(); sh.moveTo(-d / 2, 0); sh.lineTo(d / 2, 0); sh.lineTo(0, rh * (d / 2) / hd); sh.closePath();
      const gg = new THREE.ExtrudeGeometry(sh, { depth: gt, bevelEnabled: false });
      gg.attributes.uv.array.forEach((v, i, arr) => { arr[i] = v / 2; });
      const gm = new THREE.Mesh(gg, gableMat); gm.rotation.y = Math.PI / 2; gm.position.set(gx - gt / 2, ey, 0); gm.castShadow = gm.receiveShadow = true; grp.add(gm);
    });
    return grp;
  }
  // trees, drawn as two instanced meshes: trunks and crowns. list of [x, z, height, crown radius]
  function trees(list, y = (x, z) => ground(x, z)) {
    if (!list.length) return;
    const tg = new THREE.CylinderGeometry(.18, .32, 1, 6); tg.translate(0, .5, 0);
    const cg = new THREE.IcosahedronGeometry(1, 1);
    const ti = new THREE.InstancedMesh(tg, M.bark, list.length), ci = new THREE.InstancedMesh(cg, M.leaf, list.length * 2);
    const m = new THREE.Matrix4(), q = new THREE.Quaternion(), e = new THREE.Euler(), col = new THREE.Color();
    list.forEach(([x, z, h, r], i) => {
      const g0 = y(x, z);
      m.compose(new THREE.Vector3(x, g0 - .2, z), q.identity(), new THREE.Vector3(1 + r * .08, h * .55, 1 + r * .08)); ti.setMatrixAt(i, m);
      for (let k = 0; k < 2; k++) {
        e.set(R() * 3, R() * 3, R() * 3); q.setFromEuler(e);
        const s = r * (k ? .72 : 1);
        m.compose(new THREE.Vector3(x + (k ? (R() - .5) * r * .8 : 0), g0 + h * (k ? .82 : .62), z + (k ? (R() - .5) * r * .8 : 0)), q, new THREE.Vector3(s, s * .85, s)); ci.setMatrixAt(i * 2 + k, m);
        col.setHSL(.24 + R() * .06, .32 + R() * .12, .26 + R() * .1); ci.setColorAt(i * 2 + k, col);
      }
    });
    ti.castShadow = ci.castShadow = true; ci.receiveShadow = true;
    scene.add(ti, ci);
  }
  // a fire: embers, flames and a flickering light; returns the light
  function fire(x, y, z, size = 1, power = 30, dist = 14) {
    const em = new THREE.Mesh(new THREE.CircleGeometry(.5 * size, 16), M.ember); em.rotation.x = -Math.PI / 2; em.position.set(x, y + .03, z); scene.add(em);
    const fl = [];
    for (let i = 0; i < 4; i++) { const f = new THREE.Mesh(new THREE.ConeGeometry((.14 + R() * .08) * size, (.6 + R() * .3) * size, 7), M.flame); f.position.set(x + (R() - .5) * .35 * size, y + .35 * size, z + (R() - .5) * .35 * size); scene.add(f); fl.push([f, R() * 6]); }
    const L = new THREE.PointLight(0xff8c3a, power, dist, 1.6); L.position.set(x, y + 1, z); scene.add(L);
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
        p.setY(i, sink && Math.abs(x - cx) < fine / 2 - 2 && Math.abs(z - cz) < fine / 2 - 2 ? y - 4 : y);
        c.copy(grass).lerp(dark, (Math.sin(x * .05) * Math.sin(z * .04) + 1) / 2 * .6);
        if (S.colour) S.colour(x, z, y, c);
        col.push(c.r, c.g, c.b);
      }
      g.setAttribute("color", new THREE.Float32BufferAttribute(col, 3)); g.computeVertexNormals();
      const land = new THREE.Mesh(g, landM); land.receiveShadow = true; scene.add(land);
    };
    piece(size, N, 0, 0, fine > 0);
    if (fine) piece(fine, FN, (S.fineAt || [0, 0])[0], (S.fineAt || [0, 0])[1], false);
    // the sky
    const sky = new THREE.Mesh(new THREE.SphereGeometry(2400, 32, 16), new THREE.ShaderMaterial({
      side: THREE.BackSide, depthWrite: false, fog: false,
      uniforms: { top: { value: new THREE.Color(look.top) }, mid: { value: new THREE.Color(look.mid) }, low: { value: new THREE.Color(look.low) } },
      vertexShader: "varying vec3 v;void main(){v=normalize(position);gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}",
      fragmentShader: "uniform vec3 top,mid,low;varying vec3 v;void main(){float h=v.y;vec3 c=h>.1?mix(mid,top,smoothstep(.1,.7,h)):mix(low,mid,smoothstep(-.02,.1,h));gl_FragColor=vec4(c,1.);}",
    }));
    scene.add(sky);
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
  const hemi = new THREE.HemisphereLight(0xdfe8f2, 0x6a5a3c, look.hemi); scene.add(hemi);
  const sun = new THREE.DirectionalLight(0xfff0d8, look.sunI);
  sun.position.set(...look.sun); sun.target.position.set(0, 0, 0); scene.add(sun, sun.target);
  sun.castShadow = true; sun.shadow.mapSize.set(small ? 1024 : 2048, small ? 1024 : 2048);
  const sr = S.shadow || 60;
  Object.assign(sun.shadow.camera, { left: -sr, right: sr, top: sr, bottom: -sr, near: 1, far: 260 });
  sun.shadow.bias = -.0004; sun.shadow.normalBias = .04;

  // ---------- the court ----------
  const K = { THREE, scene, M, R, tex, block, cyl, wallSeg, wallLine, roof, trees, fire, smoke, walls, posts, anim, ground, floor, small, reduce, smooth };
  S.build(K);

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
  const me = { x: S.START.x, z: S.START.z, yaw: S.START.yaw || 0, pitch: -.02 };
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

  // ---------- the controls and the panel ----------
  const ui = document.createElement("div"); ui.className = "ll-ui";
  ui.innerHTML = '<div class="ll-panel" hidden><p class="ll-n"></p><h2 tabindex="-1"></h2><div class="ll-txt"></div><p class="ll-src"></p><div class="ll-btns">' +
    '<button type="button" class="btn" data-k="prev">← ' + T(D.ui.prev) + '</button><button type="button" class="btn solid" data-k="next">' + T(D.ui.next) + ' →</button>' +
    '<button type="button" class="ll-x" data-k="close" aria-label="' + T(D.ui.close) + '">×</button></div></div>' +
    '<div class="ll-bar"><button type="button" class="btn solid" data-k="tour">' + T(D.ui.tour) + ' →</button>' +
    '<button type="button" class="btn" data-k="fs">' + T(D.ui.fs) + '</button><span class="ll-help">' + T(small || matchMedia("(pointer: coarse)").matches ? D.ui.helpTouch : D.ui.help) + "</span></div>" +
    '<div class="ll-stick" aria-hidden="true"><i></i></div>';
  host.appendChild(ui);
  const panel = ui.querySelector(".ll-panel"), stick = ui.querySelector(".ll-stick"), knob = stick.querySelector("i");
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
  function goStop(i) {
    i = (i + stops.length) % stops.length;
    const [[x, z], [lx, ly, lz]] = STOPS[stops[i].id];
    const yaw = Math.atan2(-(lx - x), -(lz - z)), pitch = Math.atan2(ly - eye(x, z), Math.hypot(lx - x, lz - z));
    let dy = yaw - me.yaw; while (dy > Math.PI) dy -= 2 * Math.PI; while (dy < -Math.PI) dy += 2 * Math.PI;
    fly = { t: 0, dur: reduce ? .01 : Math.min(3.6, .9 + Math.hypot(x - me.x, z - me.z) / 16), from: { ...me }, to: { x, z, yaw: me.yaw + dy, pitch } };
    showStop(i); dismissed = -1;
  }
  ui.addEventListener("click", (e) => {
    const b = e.target.closest("button"); if (!b) return;
    const k = b.dataset.k;
    if (k === "tour" || k === "next") goStop(cur + 1);
    else if (k === "prev") goStop(cur - 1);
    else if (k === "close") { panel.hidden = true; dismissed = cur; canvas.focus({ preventScroll: true }); }
    else if (k === "fs") { const fs = document.fullscreenElement; if (fs) document.exitFullscreen(); else if (host.requestFullscreen) host.requestFullscreen().catch(() => {}); }
  });

  const keys = {};
  canvas.addEventListener("keydown", (e) => {
    const k = e.key.toLowerCase();
    if (["w", "a", "s", "d", "arrowup", "arrowdown", "arrowleft", "arrowright", "q", "e", "shift"].includes(k)) { keys[k] = 1; e.preventDefault(); fly = null; }
    if (k === "n") goStop(cur + 1);
  });
  canvas.addEventListener("keyup", (e) => { keys[e.key.toLowerCase()] = 0; });
  canvas.addEventListener("blur", () => { for (const k in keys) keys[k] = 0; });

  let drag = null;
  const ray = new THREE.Raycaster(), ndc = new THREE.Vector2();
  canvas.addEventListener("pointerdown", (e) => { drag = { id: e.pointerId, x: e.clientX, y: e.clientY, moved: 0 }; canvas.setPointerCapture(e.pointerId); canvas.focus({ preventScroll: true }); });
  canvas.addEventListener("pointermove", (e) => {
    if (!drag || drag.id !== e.pointerId) return;
    const dx = e.clientX - drag.x, dy = e.clientY - drag.y; drag.x = e.clientX; drag.y = e.clientY; drag.moved += Math.abs(dx) + Math.abs(dy);
    const k = e.pointerType === "touch" ? .006 : .0045;
    me.yaw += dx * k; me.pitch = Math.max(-1.2, Math.min(1.2, me.pitch + dy * k)); fly = null;
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
  stick.addEventListener("pointerdown", (e) => { sid = e.pointerId; stick.setPointerCapture(sid); stickAt(e); fly = null; e.preventDefault(); });
  stick.addEventListener("pointermove", (e) => { if (e.pointerId === sid) stickAt(e); });
  const stickEnd = () => { sid = null; mv.x = mv.y = 0; knob.style.transform = ""; };
  stick.addEventListener("pointerup", stickEnd); stick.addEventListener("pointercancel", stickEnd);

  // ---------- the loop ----------
  function size() { const w = host.clientWidth, h = host.clientHeight; renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); }
  size(); new ResizeObserver(size).observe(host);
  let visible = true;
  new IntersectionObserver((en) => { visible = en[0].isIntersecting; if (visible) last = performance.now(); }).observe(host);
  let last = performance.now(), time = 0, fixed = null, showMarks = true;
  function frame(now) {
    requestAnimationFrame(frame);
    if (!visible || document.hidden) return;
    const raw = Math.min(.5, (now - last) / 1000), dt = Math.min(.05, raw); last = now; time += dt;
    if (fly) {
      fly.t += raw / fly.dur; const k = fly.t >= 1 ? 1 : (1 - Math.cos(Math.PI * fly.t)) / 2;
      ["x", "z", "yaw", "pitch"].forEach((p) => { me[p] = fly.from[p] + (fly.to[p] - fly.from[p]) * k; });
      if (fly.t >= 1) fly = null;
    } else {
      const run = keys.shift ? 2 : 1, sp = 3.6 * run * dt;
      let f = (keys.w || keys.arrowup ? 1 : 0) - (keys.s || keys.arrowdown ? 1 : 0) - mv.y;
      let s = (keys.d ? 1 : 0) - (keys.a ? 1 : 0) + mv.x;
      if (keys.arrowleft || keys.q) me.yaw += 1.8 * dt;
      if (keys.arrowright || keys.e) me.yaw -= 1.8 * dt;
      if (f || s) {
        const l = Math.max(1, Math.hypot(f, s)); f /= l; s /= l;
        const nx = me.x + (-Math.sin(me.yaw) * f + Math.cos(me.yaw) * s) * sp, nz = me.z + (-Math.cos(me.yaw) * f - Math.sin(me.yaw) * s) * sp;
        [me.x, me.z] = bump(nx, nz, me.x, me.z);
      }
      stops.forEach((st, i) => { const [[x, z]] = STOPS[st.id]; if (i !== cur && i !== dismissed && Math.hypot(me.x - x, me.z - z) < 1.8) showStop(i); });
    }
    if (fixed) { camera.position.set(fixed[0], fixed[1], fixed[2]); camera.lookAt(fixed[3], fixed[4], fixed[5]); }
    else {
    const ey = eye(me.x, me.z); camera.position.set(me.x, camera.position.y ? camera.position.y + (ey - camera.position.y) * Math.min(1, dt * 8) : ey, me.z);
    camera.rotation.set(me.pitch, me.yaw, 0);
    }
    // the sun's shadows follow the walker, so they are sharp wherever you are
    sun.position.set(me.x + look.sun[0], look.sun[1], me.z + look.sun[2]); sun.target.position.set(me.x, 0, me.z);
    anim.forEach((f) => f(time, dt));
    marks.forEach((m, i) => { m.rotation.y = time * 1.4 + i; m.position.y = m.userData.y + Math.sin(time * 2 + i) * .06; m.visible = showMarks && (i !== cur || !!fly) && m.position.distanceTo(camera.position) > 4; });
    renderer.render(scene, camera);
  }
  requestAnimationFrame(frame);
  host.classList.add("ready");
  camera.position.y = 0;
  canvas.focus({ preventScroll: true });
  setTimeout(() => goStop(0), 400);
  // for making the still pictures (tools/court_stills.js): stand anywhere and look anywhere, or go back to walking
  const api = { goStop, me, view: (v) => { fixed = v; }, panel: (on) => { panel.hidden = !on; ui.style.display = on ? "" : "none"; showMarks = on; } };
  host.__court = api;
  return api;
}
