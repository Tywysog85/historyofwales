/* A walk through Llys Rhosyr, the royal court of the princes of Gwynedd on Ynys Môn, as it might have looked in the 1230s.
   Bundled into src/static/llys3d.js (loaded only when a visitor presses "Enter the court" on llys-rhosyr.html):
     npx esbuild llys3d.src.js --bundle --minify --format=esm --target=es2019 --outfile=llys3d.js
   Everything is made here in code: no models or pictures to download. The words for each stop come from the page (src/llys.py).
   The plan follows the excavated footings in spirit (a walled enclosure, a great hall, a chamber block and other buildings);
   the heights, roofs and furnishings are imagined. */
import * as THREE from "three";

const STOPS = {   // where you stand [x, z] and where you look [x, y, z] at each stop. x is east, z is south, in metres.
  gate: [[2, 29], [-3, 1.6, -4]],
  hall: [[-4, -5.6], [-15, 1.7, -8]],
  hearth: [[-2.6, -8.6], [-7, 0.5, -8]],
  seat: [[-11.2, -8], [-16.2, 1.6, -8]],
  chamber: [[11.6, -11], [16.4, 0.6, -14.8]],
  kitchen: [[11, 7.2], [15.5, 1, 7]],
  wall: [[34, 26], [200, 22, 60]],
  sands: [[-18, 44], [-95, 1, 105]],
};

function rng(seed) { return function () { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
const smooth = (a, b, x) => { const t = Math.max(0, Math.min(1, (x - a) / (b - a))); return t * t * (3 - 2 * t); };

// the land: flat around the court, rolling fields, dunes to the south west (Niwbwrch), the sea beyond, the Menai to the east
function ground(x, z) {
  const r = Math.hypot(x, z);
  let h = smooth(40, 110, r) * .6 * (1.8 + 1.1 * Math.sin(x * 0.04 + 1.3) * Math.cos(z * 0.05) + 0.7 * Math.sin(x * 0.1 + z * 0.07));
  const sw = (-x + z) / Math.SQRT2;
  const dune = smooth(70, 170, sw) * (1 - smooth(330, 380, sw));
  h += dune * (3.2 + 2.4 * Math.sin(x * 0.07) * Math.sin(z * 0.06) + 1.6 * Math.sin((x + z) * 0.13) + 0.8 * Math.sin(x * 0.31 - z * 0.17));
  h -= smooth(320, 400, sw) * 9;
  h -= smooth(230, 290, x - z * 0.2) * 8;
  return h;
}
function sandiness(x, z) {
  const sw = (-x + z) / Math.SQRT2;
  return Math.max(smooth(80, 150, sw), smooth(215, 245, x - z * 0.2));
}

export function start(host, D) {
  const cy = !!D.cy, T = (p) => (cy ? p[1] : p[0]);
  const small = Math.min(screen.width, screen.height) <= 600;
  const reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  const R = rng(1237);

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
  renderer.toneMappingExposure = 1.05;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;

  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(0xd5dde3, 90, 950);
  const camera = new THREE.PerspectiveCamera(small ? 70 : 62, 1, 0.1, 2500);
  camera.rotation.order = "YXZ";

  // ---------- textures, drawn in code ----------
  function tex(size, draw, rep, srgb = true) {
    const c = document.createElement("canvas"); c.width = c.height = size;
    draw(c.getContext("2d"), size);
    const t = new THREE.CanvasTexture(c);
    t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = renderer.capabilities.getMaxAnisotropy ? Math.min(8, renderer.capabilities.getMaxAnisotropy()) : 4;
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
  const woodTex = tex(256, (x, s) => {
    x.fillStyle = "#6b4a2e"; x.fillRect(0, 0, s, s);
    for (let i = 0; i < 160; i++) { x.strokeStyle = `rgba(${30 + R() * 40},${20 + R() * 25},${10},${R() * .4 + .1})`; x.lineWidth = R() * 2 + .5; const yy = R() * s; x.beginPath(); x.moveTo(0, yy); x.bezierCurveTo(s * .3, yy + (R() - .5) * 10, s * .6, yy + (R() - .5) * 10, s, yy); x.stroke(); }
  });
  const floorTex = tex(256, (x, s) => { x.fillStyle = "#6e5b42"; x.fillRect(0, 0, s, s); noise(x, s, 3000, 70, 100); for (let i = 0; i < 500; i++) { x.strokeStyle = `rgba(${170 + R() * 40},${150 + R() * 30},${80},.35)`; x.lineWidth = 1; const xx = R() * s, yy = R() * s, a = R() * 6.3; x.beginPath(); x.moveTo(xx, yy); x.lineTo(xx + Math.cos(a) * 18, yy + Math.sin(a) * 18); x.stroke(); } }, [3, 3]);
  const grassTex = tex(256, (x, s) => { x.fillStyle = "#b5b5b5"; x.fillRect(0, 0, s, s); noise(x, s, 6000, 120, 180); }, [220, 220], false);
  const armsTex = tex(256, (x, s) => {   // the arms of Gwynedd: quartered gold and red, four lions passant, colours swapped
    const gold = "#d9a520", red = "#b3201c", h = s / 2;
    [[0, 0, gold], [h, 0, red], [0, h, red], [h, h, gold]].forEach(([qx, qy, c]) => {
      x.fillStyle = c; x.fillRect(qx, qy, h, h);
      const l = c === gold ? red : gold; x.fillStyle = l; x.strokeStyle = l; x.lineCap = "round";
      const cx = qx + h * .5, cyy = qy + h * .52, k = h / 100;
      x.beginPath(); x.ellipse(cx - 4 * k, cyy + 2 * k, 24 * k, 8 * k, 0, 0, 7); x.fill();          // body
      x.beginPath(); x.ellipse(cx + 16 * k, cyy - 2 * k, 11 * k, 12 * k, 0, 0, 7); x.fill();        // chest
      x.beginPath(); for (let a = 0; a < 16; a++) { const r = (a % 2 ? 11 : 17) * k, an = a / 16 * Math.PI * 2; x.lineTo(cx + 24 * k + Math.cos(an) * r, cyy - 14 * k + Math.sin(an) * r); } x.fill();   // mane
      x.fillStyle = c; x.beginPath(); x.arc(cx + 21 * k, cyy - 17 * k, 2.2 * k, 0, 7); x.arc(cx + 28 * k, cyy - 17 * k, 2.2 * k, 0, 7); x.fill(); x.fillStyle = l;   // eyes, looking out
      x.lineWidth = 5 * k;
      [[-22, -6, 26], [-12, 2, 26], [12, -4, 26], [20, 12, 6]].forEach(([dx, ex, ey]) => { x.beginPath(); x.moveTo(cx + dx * k, cyy + 4 * k); x.lineTo(cx + (dx + ex) * k, cyy + ey * k); x.stroke(); });   // legs, one raised
      x.lineWidth = 3.5 * k; x.beginPath(); x.moveTo(cx - 26 * k, cyy); x.bezierCurveTo(cx - 44 * k, cyy - 8 * k, cx - 30 * k, cyy - 36 * k, cx - 14 * k, cyy - 30 * k); x.stroke();   // tail over the back
      x.beginPath(); x.moveTo(cx - 14 * k, cyy - 30 * k); x.lineTo(cx - 6 * k, cyy - 38 * k); x.lineTo(cx - 8 * k, cyy - 26 * k); x.fill();
    });
  });

  // ---------- materials ----------
  const M = {
    stone: new THREE.MeshStandardMaterial({ map: stoneTex, roughness: .95 }),
    lime: new THREE.MeshStandardMaterial({ map: limeTex, roughness: .92 }),
    thatch: new THREE.MeshStandardMaterial({ map: thatchTex, roughness: 1, side: THREE.DoubleSide }),
    wood: new THREE.MeshStandardMaterial({ map: woodTex, roughness: .85 }),
    darkwood: new THREE.MeshStandardMaterial({ map: woodTex, color: 0x8a7a6a, roughness: .8 }),
    floor: new THREE.MeshStandardMaterial({ map: floorTex, roughness: 1 }),
    arms: new THREE.MeshStandardMaterial({ map: armsTex, roughness: .9, side: THREE.DoubleSide }),
    red: new THREE.MeshStandardMaterial({ color: 0x8e1d18, roughness: .9, side: THREE.DoubleSide }),
    gold: new THREE.MeshStandardMaterial({ color: 0xc89a2a, roughness: .45, metalness: .6 }),
    cloth: new THREE.MeshStandardMaterial({ color: 0x2d4a6b, roughness: .95 }),
    ember: new THREE.MeshBasicMaterial({ color: 0xff7a2a }),
    flame: new THREE.MeshBasicMaterial({ color: 0xffb347, transparent: true, opacity: .85, blending: THREE.AdditiveBlending, depthWrite: false }),
    mark: new THREE.MeshStandardMaterial({ color: 0xf2c14e, emissive: 0xc8901a, emissiveIntensity: 1.2, roughness: .3, metalness: .4 }),
  };

  // a box with its texture at true size (texScale metres per tile)
  function block(w, h, d, mat, x, y, z, ry = 0, ts = 2) {
    const g = new THREE.BoxGeometry(w, h, d), uv = g.attributes.uv;
    const faces = [[d, h], [d, h], [w, d], [w, d], [w, h], [w, h]];
    for (let f = 0; f < 6; f++) for (let i = 0; i < 4; i++) { const k = f * 4 + i; uv.setXY(k, uv.getX(k) * faces[f][0] / ts, uv.getY(k) * faces[f][1] / ts); }
    const m = new THREE.Mesh(g, mat); m.position.set(x, y, z); m.rotation.y = ry; m.castShadow = m.receiveShadow = true; scene.add(m); return m;
  }
  const walls = [];   // [x1, z1, x2, z2, half thickness] for bumping into
  const posts = [];   // [x, z, radius]
  function wallSeg(x1, z1, x2, z2, h, t, mat, base) {
    const L = Math.hypot(x2 - x1, z2 - z1); if (L < .05) return;
    const ry = -Math.atan2(z2 - z1, x2 - x1);
    const mx = (x1 + x2) / 2, mz = (z1 + z2) / 2;
    if (base) { block(L + t, .55, t + .12, M.stone, mx, .275, mz, ry); block(L + t, h - .55, t, mat, mx, .55 + (h - .55) / 2, mz, ry); }
    else block(L + .02, h, t, mat, mx, h / 2, mz, ry);
    walls.push([x1, z1, x2, z2, t / 2]);
  }
  // a line of wall with gaps: gaps are [distance along, width]
  function wallLine(x1, z1, x2, z2, h, t, mat, gaps = [], base = false, lintel = 0) {
    const L = Math.hypot(x2 - x1, z2 - z1), ux = (x2 - x1) / L, uz = (z2 - z1) / L;
    let at = 0;
    gaps.slice().sort((a, b) => a[0] - b[0]).forEach(([c, w]) => {
      wallSeg(x1 + ux * at, z1 + uz * at, x1 + ux * (c - w / 2), z1 + uz * (c - w / 2), h, t, mat, base);
      if (lintel) block(w + .1, h - lintel, t, mat, x1 + ux * c, lintel + (h - lintel) / 2, z1 + uz * c, -Math.atan2(uz, ux));
      at = c + w / 2;
    });
    wallSeg(x1 + ux * at, z1 + uz * at, x2, z2, h, t, mat, base);
  }

  // a building with lime-washed walls on a stone footing, a thatched roof and doors: doors are [side, offset from middle, width]
  function building(cx, cz, w, d, h, rh, doors) {
    const t = .75, x0 = cx - w / 2, x1 = cx + w / 2, z0 = cz - d / 2, z1 = cz + d / 2;
    const g = (side, len) => doors.filter((q) => q[0] === side).map((q) => [len / 2 + q[1], q[2]]);
    wallLine(x0, z1, x1, z1, h, t, M.lime, g("s", w), true, 2.15);
    wallLine(x0, z0, x1, z0, h, t, M.lime, g("n", w), true, 2.15);
    wallLine(x0, z0, x0, z1, h, t, M.lime, g("w", d), true, 2.15);
    wallLine(x1, z0, x1, z1, h, t, M.lime, g("e", d), true, 2.15);
    // floor
    const fl = new THREE.Mesh(new THREE.PlaneGeometry(w, d), M.floor); fl.rotation.x = -Math.PI / 2; fl.position.set(cx, .02, cz); fl.receiveShadow = true; scene.add(fl);
    // roof: two slopes from the eaves (beyond the walls) up to the ridge, with the ends closed by lime-washed gables
    const oh = .7, ey = h - .3, ry = h + rh, hw = w / 2 + oh, hd = d / 2 + oh;
    const roof = new THREE.BufferGeometry();
    const P = [], U = [], slope = Math.hypot(hd, ry - ey);
    [[1], [-1]].forEach(([s]) => {
      const a = [cx - hw, ey, cz + s * hd], b = [cx + hw, ey, cz + s * hd], c = [cx + hw, ry, cz], dd = [cx - hw, ry, cz];
      const q = s > 0 ? [a, b, c, a, c, dd] : [b, a, dd, b, dd, c];
      q.forEach((v) => { P.push(...v); });
      const uw = 2 * hw / 2, us = slope / 2;
      (s > 0 ? [[0, 0], [uw, 0], [uw, us], [0, 0], [uw, us], [0, us]] : [[uw, 0], [0, 0], [0, us], [uw, 0], [0, us], [uw, us]]).forEach((v) => U.push(...v));
    });
    roof.setAttribute("position", new THREE.Float32BufferAttribute(P, 3));
    roof.setAttribute("uv", new THREE.Float32BufferAttribute(U, 2));
    roof.computeVertexNormals();
    const rm = new THREE.Mesh(roof, M.thatch); rm.castShadow = true; rm.receiveShadow = true; scene.add(rm);
    // thickness of the thatch at the eaves, so the roof doesn't look like paper
    [1, -1].forEach((s) => block(2 * hw, .35, .5, M.thatch, cx, ey - .05, cz + s * (hd - .2), 0, 2));
    const ridge = new THREE.Mesh(new THREE.CylinderGeometry(.22, .22, 2 * hw, 8), M.thatch); ridge.rotation.z = Math.PI / 2; ridge.position.set(cx, ry, cz); ridge.castShadow = true; scene.add(ridge);
    const ys = ey + (ry - ey) * (oh / hd);
    [x0, x1].forEach((gx) => {
      const sh = new THREE.Shape(); sh.moveTo(-d / 2, h); sh.lineTo(d / 2, h); sh.lineTo(d / 2, ys); sh.lineTo(0, ry); sh.lineTo(-d / 2, ys); sh.closePath();
      const gg = new THREE.ExtrudeGeometry(sh, { depth: t, bevelEnabled: false });
      gg.attributes.uv.array.forEach((v, i, arr) => { arr[i] = v / 2; });
      const gm = new THREE.Mesh(gg, M.lime); gm.rotation.y = Math.PI / 2; gm.position.set(gx - t / 2, 0, cz); gm.castShadow = gm.receiveShadow = true; scene.add(gm);
    });
    // tie beams across the building
    for (let bx = x0 + 3; bx < x1 - 1.5; bx += 4) block(.28, .3, d, M.darkwood, bx, h - .1, cz);
    return { x0, x1, z0, z1, h, ry, ey, hd };
  }

  // ---------- the land, the sea and the mountains ----------
  {
    const S = small ? 140 : 200, size = 1100;
    const g = new THREE.PlaneGeometry(size, size, S, S); g.rotateX(-Math.PI / 2);
    const p = g.attributes.position, col = [], c = new THREE.Color(), sand = new THREE.Color(0xd8c49a), grass = new THREE.Color(0x6f8f45), dark = new THREE.Color(0x56733a);
    for (let i = 0; i < p.count; i++) {
      const x = p.getX(i), z = p.getZ(i), y = ground(x, z); p.setY(i, y);
      c.copy(grass).lerp(dark, (Math.sin(x * .05) * Math.sin(z * .04) + 1) / 2 * .6).lerp(sand, Math.min(1, sandiness(x, z) + (y < .4 && Math.hypot(x, z) > 150 ? .8 : 0)));
      col.push(c.r, c.g, c.b);
    }
    g.setAttribute("color", new THREE.Float32BufferAttribute(col, 3)); g.computeVertexNormals();
    const land = new THREE.Mesh(g, new THREE.MeshStandardMaterial({ vertexColors: true, map: grassTex, roughness: 1 }));
    land.receiveShadow = true; scene.add(land);
    // a worn earth yard inside the court
    const yard = new THREE.Mesh(new THREE.CircleGeometry(26, 40), new THREE.MeshStandardMaterial({ map: floorTex, color: 0xb8a487, roughness: 1, transparent: true, opacity: .55, depthWrite: false }));
    yard.rotation.x = -Math.PI / 2; yard.position.set(2, .03, 0); yard.receiveShadow = true; scene.add(yard);
    const sea = new THREE.Mesh(new THREE.PlaneGeometry(4000, 4000), new THREE.MeshStandardMaterial({ color: 0x46708a, roughness: .25, metalness: .1 }));
    sea.rotation.x = -Math.PI / 2; sea.position.y = -.6; scene.add(sea);
    // Eryri across the Menai, to the east and south east
    const A = 90, Rr = 7, mg = new THREE.BufferGeometry(), mp = [], mi = [];
    for (let i = 0; i <= A; i++) for (let j = 0; j <= Rr; j++) {
      const th = -0.75 + i / A * 1.75, r = 560 + j * 30;
      const ridge = Math.max(0, Math.sin(i * .21) * 45 + Math.sin(i * .53 + 1) * 28 + Math.sin(i * 1.3) * 10 + 70) * Math.sin(Math.PI * j / Rr) * (1 + .5 * Math.exp(-((th - .45) ** 2) / .02));
      mp.push(Math.cos(th) * r, ridge - 4, Math.sin(th) * r);
    }
    for (let i = 0; i < A; i++) for (let j = 0; j < Rr; j++) { const a = i * (Rr + 1) + j, b = a + Rr + 1; mi.push(a, b, a + 1, b, b + 1, a + 1); }
    mg.setAttribute("position", new THREE.Float32BufferAttribute(mp, 3)); mg.setIndex(mi); mg.computeVertexNormals();
    scene.add(new THREE.Mesh(mg, new THREE.MeshStandardMaterial({ color: 0x77869a, roughness: 1, flatShading: true })));
    // the sky
    const sky = new THREE.Mesh(new THREE.SphereGeometry(2000, 32, 16), new THREE.ShaderMaterial({
      side: THREE.BackSide, depthWrite: false, fog: false,
      uniforms: { top: { value: new THREE.Color(0x5d8fc4) }, mid: { value: new THREE.Color(0xb9d0e2) }, low: { value: new THREE.Color(0xe9e4da) } },
      vertexShader: "varying vec3 v;void main(){v=normalize(position);gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}",
      fragmentShader: "uniform vec3 top,mid,low;varying vec3 v;void main(){float h=v.y;vec3 c=h>.12?mix(mid,top,smoothstep(.12,.7,h)):mix(low,mid,smoothstep(-.02,.12,h));gl_FragColor=vec4(c,1.);}",
    }));
    scene.add(sky);
    // clouds: soft flat discs high up
    const cm = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: .55, depthWrite: false, fog: false });
    for (let i = 0; i < 26; i++) { const c2 = new THREE.Mesh(new THREE.CircleGeometry(40 + R() * 60, 20), cm); c2.rotation.x = Math.PI / 2; c2.scale.set(1.8, 1, 1); const a = R() * 6.3, r = 300 + R() * 700; c2.position.set(Math.cos(a) * r, 160 + R() * 80, Math.sin(a) * r); scene.add(c2); }
  }

  // ---------- light ----------
  const hemi = new THREE.HemisphereLight(0xd6e6ff, 0x6a5a3c, .75); scene.add(hemi);
  const sun = new THREE.DirectionalLight(0xfff0d8, 2.6);
  sun.position.set(-45, 60, 35); sun.target.position.set(0, 0, 0); scene.add(sun, sun.target);
  sun.castShadow = true; sun.shadow.mapSize.set(small ? 1024 : 2048, small ? 1024 : 2048);
  Object.assign(sun.shadow.camera, { left: -45, right: 45, top: 45, bottom: -45, near: 1, far: 200 });
  sun.shadow.bias = -.0004; sun.shadow.normalBias = .03;

  // ---------- the court ----------
  // the enclosure wall, with the gate on the south side
  const C = [[-27, -24], [25, -26], [28, 21], [-25, 24]];
  for (let i = 0; i < 4; i++) {
    const [ax, az] = C[i], [bx, bz] = C[(i + 1) % 4];
    const gaps = i === 2 ? [[Math.hypot(28 - 2, 21 - 22.47), 3.6]] : [];
    wallLine(ax, az, bx, bz, 2.1, 1.1, M.stone, gaps);
    block(1.5, 2.5, 1.5, M.stone, ax, 1.25, az, 0);
  }
  [[3.9, 22.36], [.1, 22.58]].forEach(([x, z]) => block(.4, 2.9, .4, M.darkwood, x, 1.45, z));
  block(4.2, .3, .4, M.darkwood, 2, 2.9, 22.47);
  block(1.8, 2.1, .12, M.wood, 4.6, 1.15, 21.5, -1.25);

  // the great hall (neuadd), its doors facing each other in the long walls
  const H = building(-7, -8, 19, 9.5, 3.1, 4.3, [["s", 3, 1.9], ["n", 3, 1.9]]);
  // the chamber (ystafell), the prince's own rooms
  building(13, -13, 10, 6.5, 2.9, 3.3, [["s", -1.5, 1.4]]);
  // the kitchen and stores
  building(13, 7, 8, 5.5, 2.6, 2.9, [["w", 0, 1.5]]);
  // a store or stable
  building(-14, 13, 9, 5, 2.5, 2.7, [["n", 0, 2.4]]);

  // inside the hall: two rows of posts, the hearth, the dais, the prince's seat, tables, benches and hangings
  const pz = [H.z0 + 2.4, H.z1 - 2.4];
  for (let x = H.x0 + 3.6; x < H.x1 - 2; x += 3.6) pz.forEach((z) => {
    const off = Math.abs(z - (H.z0 + H.z1) / 2), top = H.ry - (H.ry - H.ey) * (off / H.hd);
    const p = new THREE.Mesh(new THREE.CylinderGeometry(.17, .2, top, 10), M.darkwood); p.position.set(x, top / 2, z); p.castShadow = p.receiveShadow = true; scene.add(p);
    posts.push([x, z, .3]);
  });
  const hx = -6, hz = -8;
  for (let i = 0; i < 14; i++) { const a = i / 14 * Math.PI * 2, s = new THREE.Mesh(new THREE.DodecahedronGeometry(.17 + R() * .06), M.stone); s.position.set(hx + Math.cos(a) * .85, .1, hz + Math.sin(a) * .85); s.rotation.set(R() * 3, R() * 3, R() * 3); s.castShadow = true; scene.add(s); }
  const embers = new THREE.Mesh(new THREE.CircleGeometry(.72, 20), M.ember); embers.rotation.x = -Math.PI / 2; embers.position.set(hx, .05, hz); scene.add(embers);
  for (let i = 0; i < 4; i++) { const l = new THREE.Mesh(new THREE.CylinderGeometry(.07, .08, 1.1, 7), M.darkwood); l.rotation.set(Math.PI / 2 - .25, i * .8, 0); l.position.set(hx, .2, hz); scene.add(l); }
  const flames = [];
  for (let i = 0; i < 5; i++) { const f = new THREE.Mesh(new THREE.ConeGeometry(.16 + R() * .1, .7 + R() * .4, 7), M.flame); f.position.set(hx + (R() - .5) * .45, .45, hz + (R() - .5) * .45); scene.add(f); flames.push([f, R() * 6]); }
  const fire = new THREE.PointLight(0xff8c3a, 34, 16, 1.6); fire.position.set(hx, 1.1, hz); scene.add(fire);
  const glow = new THREE.PointLight(0xffb070, 14, 11, 1.6); glow.position.set(H.x0 + 2.4, 2.2, hz); scene.add(glow);
  // the dais at the upper (west) end, and the prince's seat with the arms of Gwynedd behind it
  block(3.3, .3, H.z1 - H.z0 - .75, M.wood, H.x0 + .35 + 1.65, .15, hz, 0, 2);
  block(1.1, .5, .8, M.darkwood, H.x0 + 1.2, .55, hz);
  block(.18, 1.9, .9, M.darkwood, H.x0 + .72, 1.25, hz);
  block(.12, .12, .95, M.gold, H.x0 + .8, 2.24, hz);
  [-.42, .42].forEach((o) => block(.9, .1, .1, M.gold, H.x0 + 1.2, .85, hz + o));
  block(.35, .5, .8, M.red, H.x0 + 1.25, .82, hz);
  const banner = new THREE.Mesh(new THREE.PlaneGeometry(2.1, 2.1), M.arms); banner.rotation.y = Math.PI / 2; banner.position.set(H.x0 + .4, 2.1, hz); scene.add(banner);
  block(.9, .08, 6, M.wood, H.x0 + 2.7, .95, hz);   // the high table
  [-2.4, 2.4].forEach((o) => block(.06, .7, .06, M.darkwood, H.x0 + 2.7, .6, hz + o));
  // long tables and benches down the hall
  [H.z0 + 1.35, H.z1 - 1.35].forEach((z) => {
    block(6, .08, .8, M.wood, -8.5, .8, z); block(6, .4, .35, M.darkwood, -8.5, .2, z + (z < hz ? -.7 : .7));
    for (let x = -11; x <= -6; x += 2.5) block(.1, .78, .6, M.darkwood, x, .39, z);
  });
  // hangings on the long walls
  [H.z0 + .4, H.z1 - .4].forEach((z, k) => [-11, -2].forEach((x) => { const hg = new THREE.Mesh(new THREE.PlaneGeometry(2.4, 1.6), k ? M.red : M.cloth); hg.position.set(x, 2, z); if (k) hg.rotation.y = Math.PI; scene.add(hg); }));
  // cups and a jug on the high table
  for (let i = 0; i < 5; i++) { const c = new THREE.Mesh(new THREE.CylinderGeometry(.05, .04, .14, 10), M.gold); c.position.set(H.x0 + 2.7, 1.06, hz - 2 + i); scene.add(c); }

  // the chamber: a bed with a red cover, a chest, a candle
  block(2, .45, 1.5, M.darkwood, 16.2, .25, -14.6); block(1.9, .2, 1.45, M.red, 16.2, .55, -14.6); block(.15, 1.1, 1.5, M.darkwood, 17.2, .55, -14.6);
  block(1, .55, .6, M.wood, 10.2, .3, -15.4); block(.6, .7, .6, M.wood, 12.4, .35, -15.4);
  const candle = new THREE.PointLight(0xffb36b, 8, 8, 1.6); candle.position.set(12.4, 1.2, -15.4); scene.add(candle);
  const cf = new THREE.Mesh(new THREE.ConeGeometry(.03, .1, 6), M.flame); cf.position.set(12.4, .84, -15.4); scene.add(cf);
  // the kitchen: a hearth, barrels, a table; a bread oven outside
  for (let i = 0; i < 3; i++) { const b = new THREE.Mesh(new THREE.CylinderGeometry(.32, .28, .8, 12), M.wood); b.position.set(15.7, .4, 5.3 + i * .75); b.castShadow = true; scene.add(b); }
  block(2, .08, .8, M.wood, 13.2, .85, 8.6); block(1.2, .6, .6, M.stone, 15.9, .3, 8.8);
  const kf = new THREE.PointLight(0xff9440, 10, 8, 1.6); kf.position.set(15.9, .9, 8.8); scene.add(kf);
  const oven = new THREE.Mesh(new THREE.SphereGeometry(1.2, 18, 10, 0, Math.PI * 2, 0, Math.PI / 2), M.stone); oven.position.set(19.5, 0, 13); oven.castShadow = true; scene.add(oven);
  posts.push([19.5, 13, 1.3]);
  // a stack of firewood and a cart in the yard
  for (let i = 0; i < 12; i++) { const l = new THREE.Mesh(new THREE.CylinderGeometry(.11, .11, 1.4, 7), M.darkwood); l.rotation.x = Math.PI / 2; l.position.set(6 + (i % 4) * .24, .12 + Math.floor(i / 4) * .21, -20.5); l.castShadow = true; scene.add(l); }
  block(2.6, .12, 1.4, M.wood, -4, .75, 15, .4);
  [-0.75, 0.75].forEach((o) => { const wh = new THREE.Mesh(new THREE.TorusGeometry(.5, .07, 6, 16), M.darkwood); wh.position.set(-4 + Math.sin(.4) * o, .5, 15 + Math.cos(.4) * o); wh.rotation.y = .4; scene.add(wh); });
  posts.push([-4, 15, 1.4]);

  // ---------- the stops: a gold marker over each, and the panel that tells about it ----------
  const stops = D.stops.filter((s) => STOPS[s.id]);
  const marks = [];
  stops.forEach((s, i) => {
    const [[x, z], [lx, ly, lz]] = STOPS[s.id], dx = lx - x, dz = lz - z, L = Math.hypot(dx, dz);
    const m = new THREE.Mesh(new THREE.OctahedronGeometry(.15), M.mark);
    m.position.set(x + dx / L * 1.6, ground(x, z) * (Math.hypot(x, z) > 40 ? 1 : 0) + 2.1, z + dz / L * 1.6); m.userData.i = i; scene.add(m); marks.push(m);
  });

  // ---------- the walker ----------
  const me = { x: 2, z: 36, yaw: 0, pitch: -.02 };
  const eye = (x, z) => {
    let y = 1.65;
    if (x > H.x0 && x < H.x0 + 3.65 && z > H.z0 && z < H.z1) y += .3;      // up on the dais
    if (Math.hypot(x, z) > 40) y += Math.max(-.4, ground(x, z));
    return y;
  };
  function bump(nx, nz) {
    const r = .35;
    for (let k = 0; k < 2; k++) {
      walls.forEach(([x1, z1, x2, z2, ht]) => {
        const vx = x2 - x1, vz = z2 - z1, L2 = vx * vx + vz * vz; let t = ((nx - x1) * vx + (nz - z1) * vz) / L2; t = Math.max(0, Math.min(1, t));
        const px = x1 + vx * t, pz = z1 + vz * t, dx = nx - px, dz = nz - pz, d = Math.hypot(dx, dz), min = r + ht;
        if (d < min && d > 1e-6) { nx = px + dx / d * min; nz = pz + dz / d * min; }
      });
      posts.forEach(([px, pz, pr]) => { const dx = nx - px, dz = nz - pz, d = Math.hypot(dx, dz), min = r + pr; if (d < min && d > 1e-6) { nx = px + dx / d * min; nz = pz + dz / d * min; } });
    }
    const far = Math.hypot(nx, nz); if (far > 140) { nx *= 140 / far; nz *= 140 / far; }
    return [nx, nz];
  }

  // ---------- the controls and the panel ----------
  const ui = document.createElement("div"); ui.className = "ll-ui";
  ui.innerHTML = '<div class="ll-panel" hidden><p class="ll-n"></p><h2 tabindex="-1"></h2><div class="ll-txt"></div><div class="ll-btns">' +
    '<button type="button" class="btn" data-k="prev">← ' + T(D.ui.prev) + '</button><button type="button" class="btn solid" data-k="next">' + T(D.ui.next) + ' →</button>' +
    '<button type="button" class="ll-x" data-k="close" aria-label="' + T(D.ui.close) + '">×</button></div></div>' +
    '<div class="ll-bar"><button type="button" class="btn solid" data-k="tour">' + T(D.ui.tour) + ' →</button>' +
    '<button type="button" class="btn" data-k="fs">' + T(D.ui.fs) + '</button><span class="ll-help">' + T(small || matchMedia("(pointer: coarse)").matches ? D.ui.helpTouch : D.ui.help) + "</span></div>" +
    '<div class="ll-stick" aria-hidden="true"><i></i></div>';
  host.appendChild(ui);
  const panel = ui.querySelector(".ll-panel"), stick = ui.querySelector(".ll-stick"), knob = stick.querySelector("i");
  let cur = -1, dismissed = -1, fly = null;

  function showStop(i) {
    cur = i; const s = stops[i];
    panel.hidden = false; panel.scrollTop = 0;
    panel.querySelector(".ll-n").textContent = T(D.ui.stop).replace("{n}", i + 1).replace("{of}", stops.length);
    panel.querySelector("h2").textContent = T(s.t);
    panel.querySelector(".ll-txt").innerHTML = T(s.p).map((p) => "<p>" + p.replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c])) + "</p>").join("");
    panel.querySelector('[data-k="prev"]').disabled = i === 0;
    panel.querySelector('[data-k="next"]').textContent = (i === stops.length - 1 ? T(D.ui.again) : T(D.ui.next)) + " →";
  }
  function goStop(i) {
    i = (i + stops.length) % stops.length;
    const [[x, z], [lx, ly, lz]] = STOPS[stops[i].id];
    const yaw = Math.atan2(-(lx - x), -(lz - z)), pitch = Math.atan2(ly - eye(x, z), Math.hypot(lx - x, lz - z));
    let dy = yaw - me.yaw; while (dy > Math.PI) dy -= 2 * Math.PI; while (dy < -Math.PI) dy += 2 * Math.PI;
    fly = { t: 0, dur: reduce ? .01 : Math.min(3.2, .9 + Math.hypot(x - me.x, z - me.z) / 14), from: { ...me }, to: { x, z, yaw: me.yaw + dy, pitch } };
    showStop(i); dismissed = -1;
  }
  ui.addEventListener("click", (e) => {
    const b = e.target.closest("button"); if (!b) return;
    const k = b.dataset.k;
    if (k === "tour") goStop(cur + 1);
    else if (k === "next") goStop(cur + 1);
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

  // look by dragging; tap a gold marker to go to it
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
  // the stick, for thumbs
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
  let last = performance.now(), time = 0;
  function frame(now) {
    requestAnimationFrame(frame);
    if (!visible || document.hidden) return;
    const raw = Math.min(.5, (now - last) / 1000), dt = Math.min(.05, raw); last = now; time += dt;
    if (fly) {
      fly.t += raw / fly.dur; const k = fly.t >= 1 ? 1 : (1 - Math.cos(Math.PI * fly.t)) / 2;
      ["x", "z", "yaw", "pitch"].forEach((p) => { me[p] = fly.from[p] + (fly.to[p] - fly.from[p]) * k; });
      if (fly.t >= 1) fly = null;
    } else {
      const run = keys.shift ? 2 : 1, sp = 3.4 * run * dt;
      let f = (keys.w || keys.arrowup ? 1 : 0) - (keys.s || keys.arrowdown ? 1 : 0) - mv.y;
      let s = (keys.d ? 1 : 0) - (keys.a ? 1 : 0) + mv.x;
      if (keys.arrowleft || keys.q) me.yaw += 1.8 * dt;
      if (keys.arrowright || keys.e) me.yaw -= 1.8 * dt;
      if (f || s) {
        const l = Math.max(1, Math.hypot(f, s)); f /= l; s /= l;
        const nx = me.x + (-Math.sin(me.yaw) * f + Math.cos(me.yaw) * s) * sp, nz = me.z + (-Math.cos(me.yaw) * f - Math.sin(me.yaw) * s) * sp;
        [me.x, me.z] = bump(nx, nz);
      }
      // walking up to a stop opens its panel
      stops.forEach((st, i) => { const [[x, z]] = STOPS[st.id]; if (i !== cur && i !== dismissed && Math.hypot(me.x - x, me.z - z) < 1.8) showStop(i); });
    }
    const ey = eye(me.x, me.z); camera.position.set(me.x, camera.position.y ? camera.position.y + (ey - camera.position.y) * Math.min(1, dt * 8) : ey, me.z);
    camera.rotation.set(me.pitch, me.yaw, 0);
    // flicker the fires, turn the markers
    const fl = 1 + Math.sin(time * 11) * .08 + Math.sin(time * 23.7) * .06 + (Math.random() - .5) * .08;
    fire.intensity = 34 * fl; kf.intensity = 10 * fl; candle.intensity = 8 * (1 + Math.sin(time * 9) * .05);
    flames.forEach(([f, o]) => { f.scale.set(1, .8 + Math.sin(time * 9 + o) * .25 + Math.random() * .1, 1); f.rotation.y = time * 2 + o; });
    marks.forEach((m, i) => { m.rotation.y = time * 1.4 + i; m.position.y += Math.sin(time * 2 + i) * .002; m.visible = i !== cur || !!fly; });
    renderer.render(scene, camera);
  }
  requestAnimationFrame(frame);
  host.classList.add("ready");
  camera.position.y = 0;
  canvas.focus({ preventScroll: true });
  setTimeout(() => goStop(0), 400);
  return { goStop };
}
