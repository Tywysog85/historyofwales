/* A walk through Llys Rhosyr, the royal court of the princes of Gwynedd at Niwbwrch on Ynys Môn, as it might have looked in the 1230s.
   Bundled into src/static/llys3d.js (loaded only when a visitor presses "Enter the court" on llys-rhosyr.html):
     npx esbuild llys3d.src.js --bundle --minify --format=esm --target=es2019 --outfile=llys3d.js   (three@0.160.0)
   The words for each stop come from the page (src/llys.py). See SKILLS.md, "Llys Rhosyr in 3D".

   WHAT IT RESTS ON
   - The plan follows the published measurements: a stone-walled enclosure about 85 m east to west by 65 m, its entrance
     facing east (Coflein, RCAHMW, site 306904); a hall 17 by 11 m and a chamber 13 by 7.5 m beside it (the two buildings
     Amgueddfa Cymru rebuilt at St Fagans as Llys Llywelyn). The other buildings are the ones the courts of Gwynedd had:
     a kitchen, stables, a barn, a privy and kennels (Amgueddfa Cymru). Where each stood, beyond the hall and chamber, is imagined.
   - The walls are clay-bonded rubble, lime-washed; the halls' oak posts are painted in red and white chevrons and carry
     semicircular arched braces painted as ashlar, as at St Fagans (after the carved columns of Penmon); roofs are thatched.
   - The land, the sea and the mountains of Eryri and Llŷn are real: heights from Terrarium elevation data, baked by
     tools/bake_rhosyr.py into llys-h.png, llys-n.webp and llys-c.webp. The court is at 0, 0; x runs east and z south, in metres.
   - The rubble is a real photograph of slate walling (stone.webp, shared with the front page castle). Everything else is
     drawn on canvases here: lime-wash, thatch, oak, the painted posts, hangings, the arms of Gwynedd, rushes on the floor.
*/
import * as THREE from "three";
import { mergeGeometries } from "three/examples/jsm/utils/BufferGeometryUtils.js";
import { Sky } from "three/examples/jsm/objects/Sky.js";

// where you stand [x, z] and where you look [x, y, z] at each stop (ids match STOPS in src/llys.py)
const STOPS = {
  gate: [[55, 4], [10, 2.5, -4]],
  hall: [[-13.4, -11.2], [-28, 2.3, -12]],
  hearth: [[-16.4, -14.6], [-19.6, .5, -12]],
  seat: [[-23.2, -12], [-28, 2.1, -12]],
  chamber: [[-4.6, -18.2], [3.2, .9, -21.6]],
  kitchen: [[-20.6, 14.6], [-27, 1.1, 13.6]],
  stables: [[10, 12.5], [6, 1.6, 23]],
  wall: [[60, -44], [19300, 950, 10400]],
  sands: [[-50, 44], [-2600, -52, 3600]],
};
const SUN = [228, 17];        // azimuth from north and height of the sun, in degrees (must match tools/bake_rhosyr.py)
const H0 = 48.9;              // height of the court above the sea, from the height data (metres)
const HALF = 32000;           // the baked land runs 32 km from the court each way

function rng(seed) { return function () { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
const smooth = (a, b, x) => { const t = Math.max(0, Math.min(1, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));

export async function start(host, D) {
  const cy = !!D.cy, T = (p) => (cy ? p[1] : p[0]);
  const small = Math.min(screen.width, screen.height) <= 600;
  const coarse = matchMedia("(pointer: coarse)").matches;
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const R = rng(1237);
  const url = (f) => new URL(f, document.baseURI).href;   // the files sit beside the page (Welsh pages have <base href="../">)

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
  renderer.toneMappingExposure = .62;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  const aniso = Math.min(8, renderer.capabilities.getMaxAnisotropy());
  const Q = { grass: small ? 2600 : 9000, fireShadow: !small, shadow: small ? 1024 : 2048 };

  // ---------- files: the real land, and the photograph of rubble walling ----------
  const SM = small ? "-m" : "";
  const loader = new THREE.TextureLoader();
  const loadTex = (f, srgb) => new Promise((ok, no) => loader.load(url(f), (t) => { if (srgb) t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = aniso; ok(t); }, undefined, no));
  const loadImg = (f) => new Promise((ok, no) => { const i = new Image(); i.onload = () => ok(i); i.onerror = no; i.src = url(f); });
  let files;
  try {
    files = await Promise.all([loadImg("llys-h.png"), loadTex(`llys-n${SM}.webp`), loadTex(`llys-c${SM}.webp`, true), loadTex(`stone${SM}.webp`, true), loadTex(`stone-n${SM}.webp`)]);
  } catch (e) { host.classList.add("fail"); canvas.remove(); return; }
  const [hImg, landN, landC, stoneC, stoneN] = files;

  // the heights, read back from the picture
  const HN = hImg.width, hc = document.createElement("canvas"); hc.width = hc.height = HN;
  const hx2 = hc.getContext("2d", { willReadFrequently: true }); hx2.drawImage(hImg, 0, 0);
  const hd = hx2.getImageData(0, 0, HN, HN).data, HT = new Float32Array(HN * HN);
  for (let i = 0; i < HN * HN; i++) HT[i] = (hd[i * 4] * 256 + hd[i * 4 + 1]) / 20 - 50;
  function dem(x, z) {   // metres above the sea at x, z (scene metres)
    const fx = clamp((x + HALF) / (2 * HALF) * HN - .5, 0, HN - 1.001), fz = clamp((z + HALF) / (2 * HALF) * HN - .5, 0, HN - 1.001);
    const i = Math.floor(fx), j = Math.floor(fz), u = fx - i, v = fz - j, a = j * HN + i;
    return HT[a] * (1 - u) * (1 - v) + HT[a + 1] * u * (1 - v) + HT[a + HN] * (1 - u) * v + HT[a + HN + 1] * u * v;
  }
  const curve = (r) => r * r / (2 * 6371000 * 1.15);   // the earth curving away (with the usual allowance for the air bending light)
  // the ground near the court: flat inside the walls, gently rolling fields, then the real land
  function ground(x, z) {
    const r = Math.hypot(x, z);
    const roll = .6 * Math.sin(x * .031 + 1.3) * Math.cos(z * .027) + .35 * Math.sin(x * .07 + z * .05) + .15 * Math.sin(x * .19 - z * .13);
    const near = roll * smooth(48, 110, Math.max(Math.abs(x) * 1.25, Math.abs(z) * 1.6));
    const t = smooth(220, 760, r);
    return near * (1 - t) + (dem(x, z) - H0) * t - curve(r);
  }

  const scene = new THREE.Scene();
  const fogCol = new THREE.Color(0x93a7bd);
  scene.fog = new THREE.FogExp2(fogCol, 2.1e-5);
  const camera = new THREE.PerspectiveCamera(small ? 68 : 60, 1, .1, 80000);
  camera.rotation.order = "YXZ";

  // ---------- textures drawn in code ----------
  const cv = (s) => { const c = document.createElement("canvas"); c.width = c.height = s; return [c, c.getContext("2d")]; };
  function tex(c, rep, srgb = true) {
    const t = new THREE.CanvasTexture(c);
    t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = aniso;
    if (srgb) t.colorSpace = THREE.SRGBColorSpace;
    if (rep) t.repeat.set(rep[0], rep[1]);
    return t;
  }
  // a normal map from a height drawing (lighter = higher)
  function normalFrom(c, k = 2) {
    const s = c.width, src = c.getContext("2d").getImageData(0, 0, s, s).data;
    const [o, x] = cv(s), img = x.createImageData(s, s), d = img.data;
    const H = (i, j) => src[(((j + s) % s) * s + ((i + s) % s)) * 4] / 255;
    for (let j = 0; j < s; j++) for (let i = 0; i < s; i++) {
      const dx = (H(i + 1, j) - H(i - 1, j)) * k, dy = (H(i, j + 1) - H(i, j - 1)) * k, l = Math.hypot(dx, dy, 1), p = (j * s + i) * 4;
      d[p] = (-dx / l * .5 + .5) * 255; d[p + 1] = (dy / l * .5 + .5) * 255; d[p + 2] = (1 / l * .5 + .5) * 255; d[p + 3] = 255;
    }
    x.putImageData(img, 0, 0); return tex(o, null, false);
  }
  const speck = (x, s, n, rgb, a0, a1, r0, r1) => { for (let i = 0; i < n; i++) { x.fillStyle = `rgba(${rgb},${a0 + R() * (a1 - a0)})`; const r = r0 + R() * (r1 - r0); x.fillRect(R() * s, R() * s, r, r); } };
  const blot = (x, s, n, rgb, a, r0, r1) => { for (let i = 0; i < n; i++) { const cx = R() * s, cyy = R() * s, r = r0 + R() * (r1 - r0); for (const ox of [-s, 0, s]) for (const oy of [-s, 0, s]) { const g = x.createRadialGradient(cx + ox, cyy + oy, 0, cx + ox, cyy + oy, r); g.addColorStop(0, `rgba(${rgb},${a})`); g.addColorStop(1, `rgba(${rgb},0)`); x.fillStyle = g; x.fillRect(cx + ox - r, cyy + oy - r, 2 * r, 2 * r); } } };

  // lime-wash: chalky white, patchy where it has been renewed, a little green and grey where the weather gets it
  const [limeC, lx] = cv(512);
  lx.fillStyle = "#e8e2d4"; lx.fillRect(0, 0, 512, 512);
  blot(lx, 512, 60, "214,205,186", .35, 30, 120); blot(lx, 512, 40, "246,243,236", .5, 20, 90); blot(lx, 512, 14, "180,178,160", .12, 40, 140);
  speck(lx, 512, 5000, "120,110,95", .02, .1, 1, 3);
  for (let i = 0; i < 70; i++) { lx.strokeStyle = `rgba(150,140,120,${.03 + R() * .05})`; lx.lineWidth = 1 + R() * 3; const xx = R() * 512, yy = R() * 512; lx.beginPath(); lx.moveTo(xx, yy); lx.lineTo(xx + (R() - .5) * 6, yy + 40 + R() * 90); lx.stroke(); }
  const limeTex = tex(limeC);
  // false ashlar, painted on lime-wash with red joints: window reveals and the arches of the hall (as at St Fagans)
  const [ashC, ax] = cv(256);
  ax.drawImage(limeC, 0, 0, 256, 256);
  ax.strokeStyle = "rgba(150,48,30,.85)"; ax.lineWidth = 2.2;
  for (let r = 0; r < 4; r++) { ax.beginPath(); ax.moveTo(0, r * 64 + 1); ax.lineTo(256, r * 64 + 1); ax.stroke(); for (let c = 0; c < 3; c++) { const xx = c * 96 + (r % 2) * 48; ax.beginPath(); ax.moveTo(xx, r * 64); ax.lineTo(xx, r * 64 + 64); ax.stroke(); } }
  const ashTex = tex(ashC);

  // thatch: courses of straw laid down the slope, weathered grey-brown with fresher gold beneath
  const [thC, tx2] = cv(512), [thH, th2] = cv(512);
  tx2.fillStyle = "#6d5a3e"; tx2.fillRect(0, 0, 512, 512); th2.fillStyle = "#555"; th2.fillRect(0, 0, 512, 512);
  for (let i = 0; i < 9000; i++) {
    const xx = R() * 512, yy = R() * 512, len = 18 + R() * 34, w = .6 + R() * 1.6, g = R();
    const c = g < .45 ? [118 + R() * 40, 100 + R() * 30, 70 + R() * 20] : g < .85 ? [150 + R() * 50, 122 + R() * 35, 72 + R() * 25] : [110, 108, 100];
    for (const ox of [-512, 0, 512]) for (const oy of [-512, 0, 512]) {
      tx2.strokeStyle = `rgba(${c[0] | 0},${c[1] | 0},${c[2] | 0},.75)`; tx2.lineWidth = w; tx2.beginPath(); tx2.moveTo(xx + ox, yy + oy); tx2.lineTo(xx + ox + (R() - .5) * 3, yy + oy + len); tx2.stroke();
      const v = 110 + g * 120; th2.strokeStyle = `rgba(${v},${v},${v},.7)`; th2.lineWidth = w; th2.beginPath(); th2.moveTo(xx + ox, yy + oy); th2.lineTo(xx + ox + (R() - .5) * 3, yy + oy + len); th2.stroke();
    }
  }
  for (let yy = 0; yy < 512; yy += 64) { const g = tx2.createLinearGradient(0, yy, 0, yy + 64); g.addColorStop(0, "rgba(30,22,12,.0)"); g.addColorStop(.85, "rgba(30,22,12,.12)"); g.addColorStop(1, "rgba(30,22,12,.4)"); tx2.fillStyle = g; tx2.fillRect(0, yy, 512, 64);
    const g2 = th2.createLinearGradient(0, yy, 0, yy + 64); g2.addColorStop(0, "rgba(255,255,255,.15)"); g2.addColorStop(1, "rgba(0,0,0,.45)"); th2.fillStyle = g2; th2.fillRect(0, yy, 512, 64); }
  blot(tx2, 512, 16, "70,72,60", .25, 30, 90);    // weathering
  const thatchTex = tex(thC), thatchN = normalFrom(thH, 3);
  // the underside of the thatch, blackened by centuries of hearth smoke (and its laths)
  const [suC, sx] = cv(256);
  sx.fillStyle = "#2a2119"; sx.fillRect(0, 0, 256, 256);
  for (let i = 0; i < 2500; i++) { const v = 30 + R() * 45; sx.strokeStyle = `rgba(${v + 10},${v},${v - 8},.6)`; sx.lineWidth = .5 + R(); const xx = R() * 256, yy = R() * 256; sx.beginPath(); sx.moveTo(xx, yy); sx.lineTo(xx + (R() - .5) * 2, yy + 10 + R() * 16); sx.stroke(); }
  const sootTex = tex(suC);

  // oak, split and adzed, with its grain
  const [okC, ox2] = cv(512), [okH, oh2] = cv(512);
  ox2.fillStyle = "#6a5440"; ox2.fillRect(0, 0, 512, 512); oh2.fillStyle = "#808080"; oh2.fillRect(0, 0, 512, 512);
  for (let i = 0; i < 700; i++) {
    const yy = R() * 512, d = R() < .2 ? 50 : 25, a = .08 + R() * .25, w = .5 + R() * 2.5, wob = (R() - .5) * 16;
    ox2.strokeStyle = `rgba(${d + 20},${d + 8},${d - 5},${a})`; oh2.strokeStyle = `rgba(40,40,40,${a})`; ox2.lineWidth = oh2.lineWidth = w;
    for (const c of [ox2, oh2]) for (const o of [-512, 0, 512]) { c.beginPath(); c.moveTo(0, yy + o); c.bezierCurveTo(170, yy + o + wob, 340, yy + o - wob, 512, yy + o); c.stroke(); }
  }
  blot(ox2, 512, 20, "140,118,92", .18, 20, 80); blot(ox2, 512, 12, "40,30,22", .2, 10, 50);
  for (let i = 0; i < 26; i++) { const xx = R() * 512, yy = R() * 512; ox2.fillStyle = "rgba(35,25,15,.5)"; ox2.beginPath(); ox2.ellipse(xx, yy, 5 + R() * 6, 2 + R() * 3, 0, 0, 7); ox2.fill(); }   // knots
  const oakTex = tex(okC), oakN = normalFrom(okH, 1.5);
  // the posts, painted in alternating red and white chevrons (St Fagans, after the columns of Penmon)
  const [chC, chx] = cv(256);
  chx.fillStyle = "#e6dfcf"; chx.fillRect(0, 0, 256, 256);
  chx.fillStyle = "#93331f";
  for (let b = -1; b < 5; b++) { const y0 = b * 64; chx.beginPath(); chx.moveTo(0, y0); chx.lineTo(128, y0 + 40); chx.lineTo(256, y0); chx.lineTo(256, y0 + 32); chx.lineTo(128, y0 + 72); chx.lineTo(0, y0 + 32); chx.closePath(); chx.fill(); }
  chx.globalAlpha = .25; chx.drawImage(okC, 0, 0, 256, 256); chx.globalAlpha = 1;
  speck(chx, 256, 900, "60,40,30", .03, .12, 1, 3);
  const chevTex = tex(chC);

  // the floor: beaten earth, strewn with rushes
  const [flC, fx2] = cv(512);
  fx2.fillStyle = "#4e3f2e"; fx2.fillRect(0, 0, 512, 512);
  blot(fx2, 512, 50, "70,58,42", .5, 20, 70); blot(fx2, 512, 30, "38,30,22", .45, 15, 60);
  for (let i = 0; i < 2600; i++) {
    const xx = R() * 512, yy = R() * 512, a = R() * Math.PI, l = 14 + R() * 30, g = R();
    fx2.strokeStyle = g < .6 ? `rgba(${150 + R() * 40},${140 + R() * 30},${70 + R() * 20},.75)` : `rgba(${90 + R() * 30},${110 + R() * 30},${50},.7)`;
    fx2.lineWidth = .8 + R() * 1.4; fx2.beginPath(); fx2.moveTo(xx, yy); fx2.lineTo(xx + Math.cos(a) * l, yy + Math.sin(a) * l); fx2.stroke();
  }
  const floorTex = tex(flC);

  // grass, close to (tiles every 3 m), and the worn earth of the yard and paths
  const [grC, gx2] = cv(512);
  gx2.fillStyle = "#58693c"; gx2.fillRect(0, 0, 512, 512);
  blot(gx2, 512, 40, "90,104,58", .45, 20, 80); blot(gx2, 512, 30, "66,80,42", .4, 20, 70); blot(gx2, 512, 10, "120,120,60", .25, 30, 90);
  for (let i = 0; i < 16000; i++) { const xx = R() * 512, yy = R() * 512, g = R(); gx2.strokeStyle = g < .5 ? `rgba(${76 + R() * 44},${96 + R() * 40},${42 + R() * 20},.55)` : g < .9 ? `rgba(${40 + R() * 30},${60 + R() * 30},${20},.5)` : `rgba(${150 + R() * 40},${150 + R() * 30},${90},.5)`; gx2.lineWidth = .7 + R(); gx2.beginPath(); gx2.moveTo(xx, yy); gx2.lineTo(xx + (R() - .5) * 5, yy - 4 - R() * 8); gx2.stroke(); }
  const grassTex = tex(grC);
  const [eaC, ex2] = cv(256);
  ex2.fillStyle = "#6b5a44"; ex2.fillRect(0, 0, 256, 256);
  blot(ex2, 256, 40, "92,78,58", .5, 10, 40); blot(ex2, 256, 20, "60,50,38", .5, 10, 30);
  speck(ex2, 256, 3000, "150,140,120", .1, .4, 1, 3); speck(ex2, 256, 1500, "40,32,24", .1, .4, 1, 2);
  const earthTex = tex(eaC);
  // where the yard is worn: an overhead plan of the court, 160 m across (paths from the gate to each door)
  const [spC, spx] = cv(512), SPW = 160, sp = (v) => (v + SPW / 2) / SPW * 512;
  spx.fillStyle = "#000"; spx.fillRect(0, 0, 512, 512);
  spx.lineCap = "round"; spx.lineJoin = "round"; spx.strokeStyle = "rgba(255,255,255,.9)";
  const path = (pts, w) => { spx.lineWidth = w / SPW * 512; spx.beginPath(); pts.forEach(([x, z], i) => (i ? spx.lineTo(sp(x), sp(z)) : spx.moveTo(sp(x), sp(z)))); spx.stroke(); };
  path([[75, 6], [44, 1], [20, 2], [0, -2], [-14.5, -5.5]], 4.2); path([[0, -2], [-4, -15.5]], 2.6); path([[20, 2], [10, 14], [8, 19.5]], 3.2);
  path([[0, -2], [-12, 8], [-18.5, 13.5]], 2.8); path([[20, 2], [22, -15.5]], 3); path([[20, 2], [30, 11]], 2); path([[8, 2.5], [8, 2.5]], 7);
    for (const [x, z, r] of [[42, 1, 7], [-14.5, -5, 4], [-14.5, -18.5, 3.5], [8, 19, 6], [-18, 14, 4], [22, -15, 5]]) { const g = spx.createRadialGradient(sp(x), sp(z), 0, sp(x), sp(z), r / SPW * 512); g.addColorStop(0, "rgba(255,255,255,.85)"); g.addColorStop(1, "rgba(255,255,255,0)"); spx.fillStyle = g; spx.fillRect(0, 0, 512, 512); }
  const spData = spx.getImageData(0, 0, 512, 512).data;
  const worn = (x, z) => { const i = clamp(Math.round(sp(x)), 0, 511), j = clamp(Math.round(sp(z)), 0, 511); return spData[(j * 512 + i) * 4] / 255; };
  const splatTex = tex(spC, null, false); splatTex.wrapS = splatTex.wrapT = THREE.ClampToEdgeWrapping; splatTex.flipY = false;

  // cloth: embroidered hangings for the upper end of the hall, a coverlet, linen
  function hanging(base, a, b, motif) {
    const [c, x] = cv(256);
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
    return tex(c);
  }
  const hangRed = hanging("#7d1d1a", "#c9962e", "#2f5a3a", "cross"), hangGreen = hanging("#2c4a35", "#c9962e", "#8e2a20", "ring");
  const [liC, lix] = cv(128); lix.fillStyle = "#d8d1c0"; lix.fillRect(0, 0, 128, 128); for (let i = 0; i < 128; i += 2) { lix.fillStyle = "rgba(160,150,130,.12)"; lix.fillRect(i, 0, 1, 128); lix.fillRect(0, i, 128, 1); } blot(lix, 128, 6, "200,190,170", .25, 10, 30);
  const linenTex = tex(liC);

  // the arms of Gwynedd: quartered gold and red, four lions passant guardant, the colours counterchanged
  const [arC, arx] = cv(512);
  function lion(x, cx, cyy, k, col, bg) {
    x.save(); x.translate(cx, cyy); x.scale(k, k); x.fillStyle = col; x.strokeStyle = col; x.lineCap = "round"; x.lineJoin = "round";
    x.beginPath(); x.moveTo(-34, -6); x.bezierCurveTo(-30, -16, 10, -16, 20, -12); x.bezierCurveTo(26, -10, 28, -2, 24, 6); x.bezierCurveTo(10, 10, -20, 10, -32, 6); x.closePath(); x.fill();   // body
    x.beginPath(); x.arc(24, -18, 11, 0, 7); x.fill();                                                    // head, facing out
    x.beginPath(); for (let a = 0; a < 18; a++) { const r = a % 2 ? 12 : 17, an = a / 18 * Math.PI * 2; x.lineTo(24 + Math.cos(an) * r, -18 + Math.sin(an) * r); } x.closePath(); x.fill();   // mane
    x.lineWidth = 6;
    [[-26, 4, -32, 26], [-16, 6, -14, 26], [10, 6, 8, 26], [20, 2, 34, 6]].forEach(([a, b, c, d]) => { x.beginPath(); x.moveTo(a, b); x.lineTo(c, d); x.stroke(); });   // legs, the fore leg raised
    x.lineWidth = 4; x.beginPath(); x.moveTo(-33, -4); x.bezierCurveTo(-52, -10, -46, -40, -30, -36); x.stroke();     // tail over the back
    x.beginPath(); x.moveTo(-30, -36); x.lineTo(-20, -44); x.lineTo(-24, -30); x.closePath(); x.fill();
    x.fillStyle = bg; x.beginPath(); x.arc(20, -20, 2.4, 0, 7); x.arc(28, -20, 2.4, 0, 7); x.fill();   // eyes
    x.fillRect(19, -12, 10, 2);                                                                          // mouth
    x.restore();
  }
  const gold = "#d4a22a", red = "#a51f1b";
  [[0, 0, gold, red], [256, 0, red, gold], [0, 256, red, gold], [256, 256, gold, red]].forEach(([qx, qy, bg, fg]) => { arx.fillStyle = bg; arx.fillRect(qx, qy, 256, 256); lion(arx, qx + 128, qy + 140, 2.9, fg, bg); });
  speck(arx, 512, 4000, "0,0,0", .02, .08, 1, 3);
  const armsTex = tex(arC);

  // the fields around the court, 1.8 km across: pasture, oats, barley and hay in strips (the open fields of the maerdref),
  // fallow, each field ringed by a bank. Drawn on a canvas for the colour of the ground, and the banks are built too (below).
  const FW = 1800, [fdC, fdx] = cv(1024), fp = (v) => (v + FW / 2) / FW * 1024, parcels = [];
  {
    const G = 15, cell = FW / (G - 1), P = [];
    for (let i = 0; i < G; i++) { P.push([]); for (let j = 0; j < G; j++) P[i].push([-FW / 2 + i * cell + (i && i < G - 1 ? (R() - .5) * cell * .5 : 0), -FW / 2 + j * cell + (j && j < G - 1 ? (R() - .5) * cell * .5 : 0)]); }
    fdx.fillStyle = "#5b7a36"; fdx.fillRect(0, 0, 1024, 1024);
    const kinds = [["#587a34", 0], ["#62843a", 0], ["#4f6f2e", 0], ["#a39a52", 1], ["#b4a65c", 1], ["#8c9248", 1], ["#7b8a44", 2], ["#7a6648", 3]];
    for (let i = 0; i < G - 1; i++) for (let j = 0; j < G - 1; j++) {
      const q = [P[i][j], P[i + 1][j], P[i + 1][j + 1], P[i][j + 1]], cx = q.reduce((a, b) => a + b[0], 0) / 4, cz = q.reduce((a, b) => a + b[1], 0) / 4;
      if (Math.hypot(cx, cz) < 110) continue;
      const [col, kind] = kinds[Math.floor(R() * kinds.length)];
      fdx.save(); fdx.beginPath(); q.forEach(([x, z], k) => (k ? fdx.lineTo(fp(x), fp(z)) : fdx.moveTo(fp(x), fp(z)))); fdx.closePath(); fdx.clip();
      fdx.fillStyle = col; fdx.fillRect(0, 0, 1024, 1024);
      if (kind === 1 || kind === 3) {   // strips (selions), each a little different
        const ang = Math.atan2(q[1][1] - q[0][1], q[1][0] - q[0][0]) + (R() < .5 ? 0 : Math.PI / 2);
        fdx.translate(fp(cx), fp(cz)); fdx.rotate(ang);
        for (let k = -40; k < 40; k++) { fdx.fillStyle = `rgba(${R() < .5 ? "255,240,200" : "40,50,20"},${.04 + R() * .1})`; fdx.fillRect(-200, k * 5.7, 400, 5.7 * (.5 + R() * .5)); }
      }
      fdx.restore();
      fdx.strokeStyle = "rgba(48,58,30,.9)"; fdx.lineWidth = 2.2; fdx.beginPath(); q.forEach(([x, z], k) => (k ? fdx.lineTo(fp(x), fp(z)) : fdx.moveTo(fp(x), fp(z)))); fdx.closePath(); fdx.stroke();
      parcels.push(q);
    }
    blot(fdx, 1024, 70, "120,110,70", .08, 20, 80); blot(fdx, 1024, 60, "30,50,20", .08, 20, 70);
  }
  const fieldTex = tex(fdC, null); fieldTex.wrapS = fieldTex.wrapT = THREE.ClampToEdgeWrapping; fieldTex.flipY = false;

  // fleece: curly wool, for the sheep
  const [woC, wox] = cv(128);
  wox.fillStyle = "#cfc6b2"; wox.fillRect(0, 0, 128, 128);
  for (let i = 0; i < 900; i++) { const x = R() * 128, y = R() * 128, r = 1.5 + R() * 3, g = R(); wox.strokeStyle = g < .5 ? "rgba(255,250,236,.55)" : "rgba(120,108,88,.45)"; wox.lineWidth = .8 + R(); wox.beginPath(); wox.arc(x, y, r, R() * 6, R() * 6 + 3.5); wox.stroke(); }
  const woolTex = tex(woC);

  // ---------- materials ----------
  // everything built is merged into one mesh per material; a vertex colour carries the shade of corners, damp at the
  // foot of walls and soot high in the halls (see shade())
  const std = (o) => new THREE.MeshStandardMaterial(Object.assign({ roughness: .9, vertexColors: true }, o));
  const M = {
    stone: std({ map: stoneC, normalMap: stoneN, normalScale: new THREE.Vector2(1.1, 1.1), roughness: .95 }),
    lime: std({ map: limeTex, normalMap: stoneN, normalScale: new THREE.Vector2(.45, .45), roughness: .93 }),
    ash: std({ map: ashTex, normalMap: stoneN, normalScale: new THREE.Vector2(.25, .25) }),
    thatch: std({ map: thatchTex, normalMap: thatchN, normalScale: new THREE.Vector2(1.4, 1.4), roughness: 1 }),
    soot: std({ map: sootTex, roughness: 1 }),
    oak: std({ map: oakTex, normalMap: oakN, roughness: .8 }),
    chev: std({ map: chevTex, normalMap: oakN, normalScale: new THREE.Vector2(.4, .4), roughness: .75 }),
    floor: std({ map: floorTex, roughness: 1 }),
    linen: std({ map: linenTex, roughness: .95 }),
    hangR: std({ map: hangRed, roughness: .95, side: THREE.DoubleSide }),
    hangG: std({ map: hangGreen, roughness: .95, side: THREE.DoubleSide }),
    arms: std({ map: armsTex, roughness: .9, side: THREE.DoubleSide }),
    red: std({ color: 0x8a201a, roughness: .9 }),
    green: std({ color: 0x2e4d33, roughness: .9 }),
    iron: std({ color: 0x2b2a28, roughness: .55, metalness: .7 }),
    gold: std({ color: 0xc89a2a, roughness: .35, metalness: .85 }),
    clay: std({ color: 0x9b6a45, roughness: .8 }),
    glaze: std({ color: 0x6f7a35, roughness: .35 }),          // green-glazed jugs
    horn: std({ color: 0xa0844f, roughness: .45 }),
    straw: std({ map: thatchTex, color: 0xd8c08a, roughness: 1 }),
    wattle: std({ map: oakTex, color: 0x9a8a72, roughness: 1 }),
    daub: std({ map: limeTex, color: 0xcbbfa6, normalMap: stoneN, normalScale: new THREE.Vector2(.3, .3) }),
    bread: std({ color: 0xa8743a, roughness: .9 }),
    turf: std({ map: grassTex, color: 0xb8c49a, roughness: 1 }),
    cloth: std({ map: linenTex, roughness: .95, side: THREE.DoubleSide }),   // wool and linen clothes, dyed by a tint (see add())
    skin: std({ color: 0xc8977a, roughness: .62 }),
    coat: std({ roughness: .72 }),                                            // horses, hounds and cattle, coloured by a tint
    wool: std({ map: woolTex, roughness: 1 }),
  };
  const mats = Object.values(M);
  M.stone.map.wrapS = M.stone.map.wrapT = THREE.RepeatWrapping; stoneN.wrapS = stoneN.wrapT = THREE.RepeatWrapping;

  // ---------- building with merged geometry ----------
  const buckets = new Map();
  const roofs = [];                         // rooms under a roof: [x0, z0, x1, z1, eaves, ridge] (for soot, and for knowing when you are indoors)
  const inside = (x, z, m = 0) => roofs.find((r) => x > r[0] - m && x < r[2] + m && z > r[1] - m && z < r[3] + m);
  const roofY = (r, x, z) => { const along = r[2] - r[0] >= r[3] - r[1], half = along ? (r[3] - r[1]) / 2 : (r[2] - r[0]) / 2, d = along ? Math.abs(z - (r[1] + r[3]) / 2) : Math.abs(x - (r[0] + r[2]) / 2); return r[4] + (r[5] - r[4]) * (1 - d / half); };
  function shade(x, y, z, nx, ny, nz) {
    let s = 1;
    const qx = x + nx * .3, qy = y + ny * .3, qz = z + nz * .3, r = inside(qx, qz);
    if (r && qy < roofY(r, qx, qz) - .2) {                                                            // indoors: smoke-blackened up into the roof, darker in the corners
      s *= 1 - .62 * smooth(1.6, r[5], y);
      const dc = Math.min(x - r[0], r[2] - x, z - r[1], r[3] - z);
      s *= .78 + .22 * smooth(0, 1.6, dc);
      s *= .86 + .14 * smooth(0, .8, y);
    } else if (ny < .5) s *= .74 + .26 * smooth(0, 1.1, y);            // out of doors: damp and splash at the foot of the walls
    return s;
  }
  function add(geo, mat, m4, noShade, tint) {
    if (m4) geo.applyMatrix4(m4);
    if (geo.index) geo = geo.toNonIndexed();
    if (!geo.attributes.normal) geo.computeVertexNormals();
    if (!geo.attributes.uv) geo.setAttribute("uv", new THREE.Float32BufferAttribute(new Float32Array(geo.attributes.position.count * 2), 2));
    const p = geo.attributes.position, n = geo.attributes.normal, c = new Float32Array(p.count * 3);
    for (let i = 0; i < p.count; i++) { const s = noShade ? 1 : shade(p.getX(i), p.getY(i), p.getZ(i), n.getX(i), n.getY(i), n.getZ(i)); c[i * 3] = s * (tint ? tint.r : 1); c[i * 3 + 1] = s * (tint ? tint.g : 1); c[i * 3 + 2] = s * (tint ? tint.b : 1); }
    geo.setAttribute("color", new THREE.Float32BufferAttribute(c, 3));
    for (const k of Object.keys(geo.attributes)) if (!["position", "normal", "uv", "color"].includes(k)) geo.deleteAttribute(k);
    geo.clearGroups();
    if (!buckets.has(mat)) buckets.set(mat, []);
    buckets.get(mat).push(geo);
  }
  const mtx = (x, y, z, ry = 0, rx = 0, rz = 0, s = 1) => new THREE.Matrix4().compose(new THREE.Vector3(x, y, z), new THREE.Quaternion().setFromEuler(new THREE.Euler(rx, ry, rz, "YXZ")), new THREE.Vector3(s, s, s));
  // a box whose texture is laid at true size (ts metres a tile)
  function box(w, h, d, mat, x, y, z, ry = 0, ts = 2, segs = 1) {
    const g = new THREE.BoxGeometry(w, h, d, 1, segs, 1), uv = g.attributes.uv;
    const faces = [[d, h], [d, h], [w, d], [w, d], [w, h], [w, h]], per = uv.count / 6;
    for (let f = 0; f < 6; f++) for (let i = 0; i < per; i++) { const k = f * per + i; uv.setXY(k, uv.getX(k) * faces[f][0] / ts, uv.getY(k) * faces[f][1] / ts); }
    add(g, mat, mtx(x, y, z, ry));
  }
  function cyl(r0, r1, h, mat, x, y, z, seg = 8, rx = 0, ry = 0, rz = 0, ts = 1) {
    const g = new THREE.CylinderGeometry(r0, r1, h, seg, 1); const uv = g.attributes.uv;
    for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) * Math.PI * (r0 + r1) / ts, uv.getY(i) * h / ts);
    add(g, mat, mtx(x, y, z, ry, rx, rz));
  }
  // split a geometry with groups into one geometry per group
  function groupsOf(g) {
    const ng = g.index ? g.toNonIndexed() : g, out = [];
    const groups = g.groups.length ? g.groups : [{ start: 0, count: ng.attributes.position.count, materialIndex: 0 }];
    for (const gr of groups) {
      const s = new THREE.BufferGeometry();
      for (const k of ["position", "normal", "uv"]) { const a = ng.attributes[k]; if (a) s.setAttribute(k, new THREE.Float32BufferAttribute(a.array.slice(gr.start * a.itemSize, (gr.start + gr.count) * a.itemSize), a.itemSize)); }
      out[gr.materialIndex] = out[gr.materialIndex] ? mergeGeometries([out[gr.materialIndex], s]) : s;
    }
    return out;
  }

  const walls = [];   // [x1, z1, x2, z2, half thickness]: what you bump into
  const posts = [];   // [x, z, radius]
  const solid = (x, z, w, d, ry = 0) => { const c = Math.cos(ry), s = Math.sin(ry), P = [[-w / 2, -d / 2], [w / 2, -d / 2], [w / 2, d / 2], [-w / 2, d / 2]].map(([a, b]) => [x + a * c + b * s, z - a * s + b * c]); for (let i = 0; i < 4; i++) walls.push([...P[i], ...P[(i + 1) % 4], .05]); };

  // a flat piece of wall (an outline in the wall's own x and y) with round- or square-headed holes, extruded t thick
  function prism(outline, holes, t) {
    const sh = new THREE.Shape(); outline.forEach(([x, y], i) => (i ? sh.lineTo(x, y) : sh.moveTo(x, y))); sh.closePath();
    for (const o of holes) {
      const hp = new THREE.Path(), x0 = o.at - o.w / 2, x1 = o.at + o.w / 2, top = o.y + o.h;
      hp.moveTo(x0, o.y); hp.lineTo(x1, o.y);
      if (o.arch) { hp.lineTo(x1, top - o.w / 2); hp.absarc(o.at, top - o.w / 2, o.w / 2, 0, Math.PI, false); } else { hp.lineTo(x1, top); hp.lineTo(x0, top); }
      hp.closePath(); sh.holes.push(hp);
    }
    const g = new THREE.ExtrudeGeometry(sh, { depth: t, bevelEnabled: false, curveSegments: 12 }); g.translate(0, 0, -t / 2);
    const [caps, sides] = groupsOf(g);
    for (const q of [caps, sides]) if (q) { const uv = q.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) / 2.2, uv.getY(i) / 2.2); }
    return [caps, sides];
  }
  // a straight wall from (x1, z1) to (x2, z2): rubble footing, lime-washed (or bare stone) above, doors and windows cut through,
  // a gable on top if asked. Its own +z side is the outside (walls run round each building the same way).
  function wall(x1, z1, x2, z2, H, t, mat, openings = [], gable = null, reveal = M.ash) {
    const L = Math.hypot(x2 - x1, z2 - z1), ry = -Math.atan2(z2 - z1, x2 - x1);
    const m = mtx(x1, 0, z1, ry), put = (g, mm, x = 0, y = 0, z = 0) => { if (g) add(g, mm, m.clone().multiply(mtx(x, y, z))); };
    const doors = openings.filter((o) => !o.y).sort((a, b) => a.at - b.at), wins = openings.filter((o) => o.y);
    const low = wins.filter((o) => o.y + o.h <= H - .15), high = wins.filter((o) => o.y + o.h > H - .15);
    // the wall is split at each door so the doorway runs to the ground; the wall over the door is filled in afterward
    let at = 0; const pieces = [];
    for (const d of doors) { pieces.push([at, d.at - d.w / 2]); at = d.at + d.w / 2; }
    pieces.push([at, L]);
    for (const [a, b] of pieces) {
      if (b - a < .02) continue;
      const [caps, sides] = prism([[0, 0], [b - a, 0], [b - a, H], [0, H]], low.filter((o) => o.at > a && o.at < b).map((o) => Object.assign({}, o, { at: o.at - a })), t);
      put(caps, mat, a); put(sides, reveal, a);
      walls.push([x1 + (x2 - x1) * a / L, z1 + (z2 - z1) * a / L, x1 + (x2 - x1) * b / L, z1 + (z2 - z1) * b / L, t / 2]);
      if (mat !== M.stone) {   // a footing of bare rubble, a little proud of the wash
        const g = new THREE.BoxGeometry(b - a, .42, t + .14); g.translate((a + b) / 2, .21, 0);
        const uv = g.attributes.uv, mx = Math.max(b - a, t) / 2.2; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) * mx, uv.getY(i) * .2);
        add(g, M.stone, m.clone());
      }
    }
    for (const d of doors) {
      const x0 = d.at - d.w / 2, x1d = d.at + d.w / 2, rr = d.w / 2;
      if (d.arch) {
        // the wall over a round-headed door, and its arch of voussoirs (painted as ashlar on lime-washed walls)
        const sh = new THREE.Shape(); sh.moveTo(x0, d.h - rr); sh.absarc(d.at, d.h - rr, rr, Math.PI, 0, true); sh.lineTo(x1d, H); sh.lineTo(x0, H); sh.closePath();
        const g = new THREE.ExtrudeGeometry(sh, { depth: t, bevelEnabled: false, curveSegments: 12 }); g.translate(0, 0, -t / 2);
        const [c2, s2] = groupsOf(g); for (const q of [c2, s2]) { const uv = q.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) / 2.2, uv.getY(i) / 2.2); }
        put(c2, mat); put(s2, reveal);
        const v = new THREE.Shape(); v.moveTo(x0 - .3, d.h - rr); v.absarc(d.at, d.h - rr, rr + .3, Math.PI, 0, true); v.lineTo(x1d, d.h - rr); v.absarc(d.at, d.h - rr, rr, 0, Math.PI, false); v.closePath();
        const vg = new THREE.ExtrudeGeometry(v, { depth: t + .04, bevelEnabled: false, curveSegments: 12 }); vg.translate(0, 0, -t / 2 - .02);
        const uv = vg.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) / 1.2, uv.getY(i) / 1.2);
        add(vg, mat === M.lime ? M.ash : M.stone, m.clone());
      } else {
        const g = new THREE.BoxGeometry(d.w + .02, H - d.h, t); g.translate(d.at, d.h + (H - d.h) / 2, 0); add(g, mat, m.clone());
        const lt = new THREE.BoxGeometry(d.w + .5, .2, t + .06); lt.translate(d.at, d.h + .1, 0); add(lt, M.oak, m.clone());
      }
      if (d.leaf !== false) {   // a plank door with iron straps, standing open into the room
        const lw = d.w - .04, lh = d.arch ? d.h - rr * .25 : d.h, side = -1, ang = side * -1.3;
        const hm = m.clone().multiply(mtx(x0 + .03, 0, side * (t / 2 - .06), ang));
        const lg = new THREE.BoxGeometry(lw, lh, .07); lg.translate(lw / 2, lh / 2, 0); add(lg, M.oak, hm.clone());
        for (const hy of [.45, lh - .5]) { const s = new THREE.BoxGeometry(lw * .8, .06, .09); s.translate(lw * .4, hy, 0); add(s, M.iron, hm.clone()); }
      }
    }
    for (const w of low.concat(high)) {   // shutters inside each window, folded back
      for (const s of [-1, 1]) { const g = new THREE.BoxGeometry(w.w / 2, w.h - w.w / 2, .05); g.translate(-s * w.w / 4, 0, 0); add(g, M.oak, m.clone().multiply(mtx(w.at + s * w.w / 2, w.y + (w.h - w.w / 2) / 2, -t / 2 - .04, -s * 1.35))); }
      openingsW.push({ x: x1 + (x2 - x1) * w.at / L, z: z1 + (z2 - z1) * w.at / L, y: w.y + w.h / 2, w: w.w, h: w.h, nx: -(z2 - z1) / L, nz: (x2 - x1) / L });
    }
    for (const d of doors) openingsW.push({ x: x1 + (x2 - x1) * d.at / L, z: z1 + (z2 - z1) * d.at / L, y: d.h / 2, w: d.w, h: d.h, nx: -(z2 - z1) / L, nz: (x2 - x1) / L, door: true });
    if (gable) {   // the gable, from the wall top to just under the ridge, with any windows set high in it
      const [gH, gW] = gable;
      const [caps, sides] = prism([[0, H], [L, H], [L / 2 + gW, gH], [L / 2 - gW, gH]], high, t);
      put(caps, mat); put(sides, reveal);
    }
    return { L, ry };
  }
  const openingsW = [];

  // a thatched roof over a rectangle (the ridge along x, or along z), the walls reaching `eaves`, the ridge `ridge`.
  // Gabled, or hipped (sloping at the ends too). Thatch on top, smoke-blackened underside, rafters and purlins beneath.
  function roof(cx, cz, len, span, eaves, ridge, alongZ, hips = false, louvre = null) {
    const oh = .55, hw = span / 2 + oh, hl = len / 2 + (hips ? oh : .35), th = .42;
    const ey = eaves - oh * (ridge - eaves) / (span / 2), rise = ridge - ey, slope = Math.hypot(hw, rise);
    const rl = hips ? Math.max(.4, hl - hw * .95) : hl;                      // half the length of the ridge
    const rot = alongZ ? mtx(cx, 0, cz, Math.PI / 2) : mtx(cx, 0, cz);
    const tri = (A, B, Cc, mat, uvs, flipTo) => {                                // one triangle, turned to face flipTo
      const g = new THREE.BufferGeometry(); let P = [A, B, Cc], U = uvs;
      const n = new THREE.Vector3().subVectors(new THREE.Vector3(...B), new THREE.Vector3(...A)).cross(new THREE.Vector3().subVectors(new THREE.Vector3(...Cc), new THREE.Vector3(...A)));
      if (n.dot(flipTo) < 0) { P = [A, Cc, B]; U = [uvs[0], uvs[2], uvs[1]]; }
      g.setAttribute("position", new THREE.Float32BufferAttribute(P.flat(), 3)); g.setAttribute("uv", new THREE.Float32BufferAttribute(U.flat(), 2)); g.computeVertexNormals();
      add(g, mat, rot.clone());
    };
    for (const s of [1, -1]) {
      // the long slopes: subdivided a little so the thatch can sag between the rafters
      const g = new THREE.PlaneGeometry(2, 1, 10, 6), pos = g.attributes.position, uv = g.attributes.uv;
      for (let i = 0; i < pos.count; i++) {
        const u = pos.getX(i), v = pos.getY(i) + .5;                       // u: -1..1 along, v: 0 at the eaves, 1 at the ridge
        const halfAt = hl + (rl - hl) * v, x = u * halfAt;
        const sag = Math.sin(v * Math.PI) * .09 * (1 - Math.abs(u) * .5) + (R() - .5) * .035;
        pos.setXYZ(i, x, ey + rise * v - sag + th / 2, s * hw * (1 - v)); uv.setXY(i, x / 1.6, v * slope / 1.6);
      }
      if (s < 0) g.index.array.reverse();
      g.computeVertexNormals(); add(g, M.thatch, rot.clone());
      const u2 = new THREE.PlaneGeometry(2, 1, 1, 4), p2 = u2.attributes.position, uv2 = u2.attributes.uv;
      for (let i = 0; i < p2.count; i++) { const u = p2.getX(i), v = p2.getY(i) + .5, x = u * (hl - .1 + (rl - hl) * v); p2.setXYZ(i, x, ey + rise * v - th / 2, s * (hw - .05) * (1 - v)); uv2.setXY(i, x, v * slope); }
      if (s > 0) u2.index.array.reverse();
      u2.computeVertexNormals(); add(u2, M.soot, rot.clone());
      // the cut ends of the straw along the eaves
      const e = new THREE.BoxGeometry(2 * hl, th * 1.15, .32, 6, 1, 1); e.translate(0, ey, s * (hw - .12));
      const ev = e.attributes.uv; for (let i = 0; i < ev.count; i++) ev.setXY(i, ev.getX(i) * hl, ev.getY(i) * .3);
      add(e, M.thatch, rot.clone());
      // rafters every 60 cm, and two purlins
      for (let x = -hl + .5; x < hl - .3; x += .6) { const k = Math.max(0, (Math.abs(x) - rl) / (hl - rl || 1)); if (hips && k > .98) continue; const r = new THREE.BoxGeometry(.11, .14, slope * (1 - k) - .2); r.rotateX(s * Math.atan2(rise, hw)); r.translate(x, ey + rise * (1 - k) / 2 - th / 2 - .09, s * hw * (1 - (1 - k) / 2)); add(r, M.oak, rot.clone()); }
      for (const v of [.33, .66]) { const p = new THREE.BoxGeometry(2 * (hl + (rl - hl) * v) - .4, .2, .2); p.translate(0, ey + rise * v - th / 2 - .26, s * hw * (1 - v)); add(p, M.oak, rot.clone()); }
    }
    if (hips) for (const e of [-1, 1]) {
      const A = [e * hl, ey + th / 2, -hw], B = [e * hl, ey + th / 2, hw], Cc = [e * rl, ridge + th / 2, 0], out = new THREE.Vector3(e, 1, 0);
      tri(A, B, Cc, M.thatch, [[-hw / 1.6, 0], [hw / 1.6, 0], [0, slope / 1.6]], out);
      tri([A[0] - e * .1, ey - th / 2, A[2] + .05], [B[0] - e * .1, ey - th / 2, B[2] - .05], [Cc[0], ridge - th / 2, 0], M.soot, [[0, 0], [hw, 0], [hw / 2, slope]], new THREE.Vector3(-e, -1, 0));
      const eb = new THREE.BoxGeometry(.32, th * 1.15, 2 * hw); eb.translate(e * (hl - .12), ey, 0); add(eb, M.thatch, rot.clone());
    }
    // the ridge, rounded
    const rg = new THREE.CylinderGeometry(.3, .3, 2 * rl + .3, 10, 1); rg.rotateZ(Math.PI / 2); rg.translate(0, ridge + th / 2 - .12, 0);
    const ru = rg.attributes.uv; for (let i = 0; i < ru.count; i++) ru.setXY(i, ru.getX(i) * 1.3, ru.getY(i) * rl / .8);
    add(rg, M.thatch, rot.clone());
    if (!hips) for (const s of [-1, 1]) {   // the verges over the gables
      const sh = new THREE.Shape(); sh.moveTo(-hw, ey - th * .6); sh.lineTo(0, ridge - th * .6 + .2); sh.lineTo(hw, ey - th * .6); sh.lineTo(hw, ey + th * .6); sh.lineTo(0, ridge + th * .6 + .2); sh.lineTo(-hw, ey + th * .6); sh.closePath();
      const g = new THREE.ExtrudeGeometry(sh, { depth: .3, bevelEnabled: false }); g.rotateY(Math.PI / 2); g.translate(s * hl - (s > 0 ? .3 : 0), 0, 0);
      const gu = g.attributes.uv; for (let i = 0; i < gu.count; i++) gu.setXY(i, gu.getX(i) / 1.6, gu.getY(i) / 1.6);
      add(g, M.thatch, rot.clone());
    }
    if (louvre != null) {   // a louvre over the hearth, to let out the smoke
      const lx = louvre, at = alongZ ? [cx, cz + lx] : [cx + lx, cz];
      box(1.3, 1, 1.3, M.oak, at[0], ridge + .45, at[1], 0, 1);
      for (let k = -1; k <= 1; k += 2) box(1.34, .08, .04, M.soot, at[0], ridge + .3 + k * .2, at[1] + .66, 0, 1);
      const lr = new THREE.ConeGeometry(1.2, .85, 4, 1); lr.rotateY(Math.PI / 4); lr.translate(at[0], ridge + 1.35, at[1]); add(lr, M.thatch);
    }
    return { ey, hw, hl };
  }

  // a building: walls of lime-washed rubble, its long side along x; doors and windows on each side: {side: n/s/e/w, at (from the middle), w, h, y}
  function building(o) {
    const { cx, cz, w, d, h, ridge, t = .9, mat = M.lime } = o, x0 = cx - w / 2, x1 = cx + w / 2, z0 = cz - d / 2, z1 = cz + d / 2;
    // "at" is measured from the middle of each side: east-positive on the long sides, south-positive on the ends
    const op = (side, L) => (o.open || []).filter((q) => q.side === side).map((q) => Object.assign({ arch: true, y: 0 }, q, { at: L / 2 + (side === "n" || side === "e" ? -q.at : q.at) }));
    if (!o.noRoom) roofs.push([x0, z0, x1, z1, h, ridge]);
    const rv = mat === M.lime ? M.ash : mat;
    const gH = ridge - .5, gW = .25;
    wall(x0 + t / 2, z1 - t / 2, x1 - t / 2, z1 - t / 2, h, t, mat, op("s", w - t), null, rv);
    wall(x1 - t / 2, z0 + t / 2, x0 + t / 2, z0 + t / 2, h, t, mat, op("n", w - t), null, rv);
    wall(x0 + t / 2, z0 + t / 2, x0 + t / 2, z1 - t / 2, h, t, mat, op("w", d - t), o.hips ? null : [gH, gW], rv);
    wall(x1 - t / 2, z1 - t / 2, x1 - t / 2, z0 + t / 2, h, t, mat, op("e", d - t), o.hips ? null : [gH, gW], rv);
    const fl = new THREE.PlaneGeometry(w - t * 2 + .1, d - t * 2 + .1); fl.rotateX(-Math.PI / 2); fl.translate(cx, .025, cz);
    const fu = fl.attributes.uv; for (let i = 0; i < fu.count; i++) fu.setXY(i, fu.getX(i) * (w - 2 * t) / 3, fu.getY(i) * (d - 2 * t) / 3);
    add(fl, o.floor || M.floor);
    const rf = roof(cx, cz, w, d, h, ridge, false, o.hips, o.louvre);
    return { x0, x1, z0, z1, t, h, ridge, ix0: x0 + t, ix1: x1 - t, iz0: z0 + t, iz1: z1 - t, ey: rf.ey };
  }

  // ---------- THE COURT ----------
  // the enclosure wall (85 by 65 m), the gate facing east
  const C = [[-44, -31], [41, -33], [43, 32], [-42, 34]];
  for (let i = 0; i < 4; i++) {
    const [a, b] = [C[i], C[(i + 1) % 4]];
    const L = Math.hypot(b[0] - a[0], b[1] - a[1]);
    const ops = i === 1 ? [{ at: Math.hypot(42.03 - 41, .45 + 33), w: 3.6, h: 2.2, y: 0, arch: false, leaf: false }] : [];
    wall(a[0], a[1], b[0], b[1], 2.2, 1.3, M.stone, ops);
    // a coping of flat stones
    const cg = new THREE.BoxGeometry(L, .14, 1.45); cg.translate(L / 2, 2.27, 0); const cu = cg.attributes.uv; for (let k = 0; k < cu.count; k++) cu.setXY(k, cu.getX(k) * L / 2.2, cu.getY(k) * .66);
    if (!ops.length) add(cg, M.stone, mtx(a[0], 0, a[1], -Math.atan2(b[1] - a[1], b[0] - a[0])));
    box(1.8, 2.5, 1.8, M.stone, a[0], 1.25, a[1], -Math.atan2(b[1] - a[1], b[0] - a[0]), 2.2);
  }
  // the gate: a timber gatehouse over the opening, its two leaves open
  const gx = 42.03, gz = .45;
  box(1.6, 3.8, 1.6, M.stone, gx, 1.9, gz - 2.7); box(1.6, 3.8, 1.6, M.stone, gx, 1.9, gz + 2.7);
  roof(gx, gz, 7.2, 3.6, 3.8, 5.6, true);   // (not a room: the gate is open to the sky on both sides)
  for (const s of [-1, 1]) { const g = new THREE.BoxGeometry(.08, 2.9, 1.75); g.translate(0, 1.45, s * .88); add(g, M.oak, mtx(gx - .6, 0, gz + s * 1.75, s * -1.2)); }

  // the great hall (neuadd): 17 by 11 m, its doors facing each other near the lower (east) end, the dais at the west
  const HB = building({ cx: -20, cz: -12, w: 17, d: 11, h: 3.6, ridge: 9.4, louvre: .5,
    open: [{ side: "s", at: 5.5, w: 1.7, h: 3.0 }, { side: "n", at: 5.5, w: 1.7, h: 3.0 },
      { side: "s", at: -4.5, w: .62, h: 1.3, y: 1.55 }, { side: "s", at: .5, w: .62, h: 1.3, y: 1.55 }, { side: "n", at: -2, w: .62, h: 1.3, y: 1.55 },
      { side: "w", at: 0, w: .7, h: 1.6, y: 4.3 }, { side: "e", at: 0, w: .62, h: 1.4, y: 4.0 }] });
  // the chamber (ystafell): 13 by 7.5 m, beside the hall
  const CB = building({ cx: -1, cz: -20, w: 13, d: 7.5, h: 3.3, ridge: 7.8,
    open: [{ side: "s", at: -3.4, w: 1.3, h: 2.5 }, { side: "s", at: 1.8, w: .6, h: 1.2, y: 1.4 }, { side: "s", at: 4.6, w: .6, h: 1.2, y: 1.4 }, { side: "w", at: 0, w: .55, h: 1.2, y: 1.5 }] });
  // the kitchen, apart from the hall for fear of fire
  const KB = building({ cx: -24, cz: 14, w: 10, d: 6.5, h: 2.9, ridge: 6.6, mat: M.stone, louvre: -1.5,
    open: [{ side: "e", at: -.4, w: 1.4, h: 2.3 }, { side: "s", at: 1.5, w: .55, h: .9, y: 1.4 }] });
  // the stables, timber-framed on stone footings, along the south wall
  const SB = building({ cx: 8, cz: 24, w: 22, d: 6.5, h: 2.6, ridge: 6.2, mat: M.daub, hips: true,
    open: [{ side: "n", at: -6, w: 2.2, h: 2.3, arch: false, leaf: false }, { side: "n", at: 2, w: 2.2, h: 2.3, arch: false, leaf: false }, { side: "n", at: 7.5, w: .55, h: .8, y: 1.3, arch: false }] });
  // the barn
  const BB = building({ cx: 24, cz: -20, w: 16, d: 8, h: 3, ridge: 7.6, mat: M.daub, hips: true,
    open: [{ side: "s", at: 0, w: 3.2, h: 2.9, arch: false, leaf: false }, { side: "n", at: 0, w: 3.2, h: 2.9, arch: false, leaf: false }] });
  // the kennels, with a pen of wattle
  building({ cx: 33, cz: 16, w: 5.5, d: 4, h: 2, ridge: 4.2, mat: M.daub, hips: true, open: [{ side: "w", at: 0, w: 1, h: 1.5, arch: false, leaf: false }] });
  // the privy, out of the way in the north-west corner
  building({ cx: -37.5, cz: -25.5, w: 3, d: 2.6, h: 2.1, ridge: 3.8, mat: M.daub, hips: true, open: [{ side: "s", at: 0, w: .9, h: 1.8, arch: false }] });
  // timber framing showing on the daub walls of the stables and barn
  for (const B of [SB, BB]) {
    for (let x = B.x0 + .3; x <= B.x1 - .2; x += 2.2) for (const z of [B.z0 - .02, B.z1 + .02]) box(.22, B.h, .08, M.oak, x, B.h / 2, z, 0, 1);
    for (const z of [B.z0 - .02, B.z1 + .02]) box(B.x1 - B.x0, .22, .08, M.oak, (B.x0 + B.x1) / 2, B.h - .15, z, 0, 1);
  }

  // inside the hall: two rows of oak posts painted in chevrons, carrying semicircular arched braces painted as ashlar
  const hz = -12, hx = -19.6, postZ = [hz - 2.7, hz + 2.7], bays = [-26, -22.4, -18.8, -15.2];
  const plateY = 5.0;
  for (const x of bays) for (const z of postZ) { cyl(.19, .21, plateY, M.chev, x, plateY / 2, z, 8, 0, 0, 0, .62); posts.push([x, z, .3]); }
  for (const z of postZ) box(bays[3] - bays[0] + 1.2, .3, .3, M.oak, (bays[0] + bays[3]) / 2, plateY + .15, z, 0, 2);   // arcade plates
  function arch(x1, z1, x2, z2, yTop, depth = .22, thick = .26) {   // a semicircular brace between two posts
    const L = Math.hypot(x2 - x1, z2 - z1), rr = L / 2, sh = new THREE.Shape();
    sh.moveTo(-rr, yTop - rr - .2); sh.lineTo(-rr, yTop - rr); sh.absarc(0, yTop - rr, rr, Math.PI, 0, true); sh.lineTo(rr, yTop - rr - .2);
    sh.lineTo(rr - thick, yTop - rr - .2); sh.lineTo(rr - thick, yTop - rr); sh.absarc(0, yTop - rr, rr - thick, 0, Math.PI, false); sh.lineTo(-rr + thick, yTop - rr - .2); sh.closePath();
    const g = new THREE.ExtrudeGeometry(sh, { depth, bevelEnabled: false, curveSegments: 18 }); g.translate(0, 0, -depth / 2);
    const uv = g.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) / 1.4, uv.getY(i) / 1.4);
    add(g, M.ash, mtx((x1 + x2) / 2, 0, (z1 + z2) / 2, -Math.atan2(z2 - z1, x2 - x1)));
  }
  for (let i = 0; i < 3; i++) for (const z of postZ) arch(bays[i], z, bays[i + 1], z, plateY);           // along the arcades
  for (const x of bays) {
    arch(x, postZ[0], x, postZ[1], plateY + 1.35, .26, .3);                                              // across the hall
    box(.28, .3, HB.iz1 - HB.iz0, M.oak, x, plateY + 1.5, hz, 0, 2);                                   // tie beam
    for (const s of [-1, 1]) { const g = new THREE.BoxGeometry(.2, .2, 1.9); g.rotateX(s * .55); g.translate(x, plateY - .75, hz + s * 3.7); add(g, M.oak); }   // aisle ties to the wall
    box(.18, HB.ridge - plateY - 2, .18, M.oak, x, (HB.ridge + plateY + 1.4) / 2 - .5, hz, 0, 1);       // king post
  }
  // the hearth in the middle of the floor: a kerb of rubble round a bed of flat stones and ash
  const hearthC = [hx, hz];
  for (let i = 0; i < 22; i++) {
    const a = i / 22 * Math.PI * 2, g = new THREE.DodecahedronGeometry(.2 + R() * .07, 0);
    g.scale(1.3, .7, 1); const uv = g.attributes.uv; for (let k = 0; k < uv.count; k++) uv.setXY(k, uv.getX(k) * .4, uv.getY(k) * .4);
    add(g, M.stone, mtx(hx + Math.cos(a) * 1.15 * 1.25, .09, hz + Math.sin(a) * 1.15, a + R(), R() * .3, R() * .3));
  }
  posts.push([hx, hz, 1.25]);
  // the dais at the upper (west) end, the prince's chair, the high table, hangings and the arms of Gwynedd
  const dx0 = HB.ix0, dW = 3.4;
  box(dW, .32, HB.iz1 - HB.iz0, M.oak, dx0 + dW / 2, .16, hz, 0, 1.6);
  box(.08, .32, HB.iz1 - HB.iz0, M.oak, dx0 + dW, .16, hz, 0, 1);
  const seatX = dx0 + .9;
  box(.75, .5, .7, M.oak, seatX, .57, hz, 0, 1); box(.12, 1.9, .82, M.oak, seatX - .38, 1.27, hz, 0, 1);                                     // chair, its tall back
  for (const s of [-1, 1]) { box(.7, .1, .1, M.oak, seatX + .02, 1.1, hz + s * .38, 0, 1); cyl(.06, .06, .9, M.oak, seatX + .35, .77, hz + s * .38, 6); }
  box(.6, .14, .62, M.red, seatX + .04, .88, hz); box(.06, .9, .6, M.red, seatX - .3, 1.45, hz);
  for (const s of [-1, 1]) { const g = new THREE.SphereGeometry(.09, 10, 8); add(g, M.gold, mtx(seatX - .38, 2.27, hz + s * .34)); }
  // the dorsal: an embroidered hanging behind the dais, and the banner of the arms of Gwynedd above the seat
  { const g = new THREE.PlaneGeometry(HB.iz1 - HB.iz0 - .2, 2.6); g.rotateY(Math.PI / 2); const uv = g.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) * 3.6, uv.getY(i)); add(g, M.hangR, mtx(dx0 + .04, 1.65, hz)); }
  { const g = new THREE.PlaneGeometry(1.7, 2.1, 6, 6), p = g.attributes.position; for (let i = 0; i < p.count; i++) p.setZ(i, Math.sin(p.getX(i) * 3.4) * .04); g.computeVertexNormals(); g.rotateY(Math.PI / 2); add(g, M.arms, mtx(dx0 + .1, 3.95, hz), true); }
  cyl(.03, .03, 1.9, M.oak, dx0 + .14, 5.0, hz, 6, Math.PI / 2);
  // hangings on the side walls toward the upper end
  for (const z of [HB.iz0 + .03, HB.iz1 - .03]) for (const [x, m] of [[-25.4, M.hangG], [-21.6, M.hangR]]) { const g = new THREE.PlaneGeometry(2.6, 1.9); const uv = g.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) * 2.6, uv.getY(i) * 1.9); add(g, m, mtx(x, 2.35, z, z < hz ? 0 : Math.PI)); }
  // shields hung on the posts
  const shieldG = (() => { const s = new THREE.Shape(); s.moveTo(-.3, .32); s.lineTo(.3, .32); s.quadraticCurveTo(.32, -.1, 0, -.42); s.quadraticCurveTo(-.32, -.1, -.3, .32); const g = new THREE.ExtrudeGeometry(s, { depth: .04, bevelEnabled: true, bevelSize: .015, bevelThickness: .015, bevelSegments: 1 }); return g; })();
  const shieldMats = [M.arms, M.red, M.green, M.arms, M.red, M.green, M.arms, M.red];
  let si = 0;
  for (const x of bays) for (const z of postZ) {
    const out = z < hz ? 1 : -1, g = shieldG.clone();
    const uv = g.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) * 1.4 + .5, uv.getY(i) * 1.4 + .5);
    add(g, shieldMats[si++ % shieldMats.length], mtx(x, 3.1, z + out * .23, out > 0 ? 0 : Math.PI, -.12));
  }
  // the high table, its cloth, and the long tables and benches down the hall
  function table(x, z, L, alongX, cloth) {
    const [w, d] = alongX ? [L, .85] : [.85, L];
    box(w, .07, d, M.oak, x, .78, z, 0, 1.4);
    if (cloth) { box(w + .02, .01, d + .2, M.linen, x, .82, z, 0, 1.2); for (const s of [-1, 1]) box(alongX ? w + .02 : .01, .32, alongX ? .01 : d + .02, M.linen, alongX ? x : x + s * .52, .66, alongX ? z + s * .52 : z, 0, 1.2); }
    for (const t of [-.38, .38]) box(alongX ? .08 : .7, .74, alongX ? .7 : .08, M.oak, alongX ? x + t * L : x, .37, alongX ? z : z + t * L, 0, 1);
    solid(x, z, w, d);
  }
  table(dx0 + 2.35, hz, 6.6, false, true);
  for (const s of [-1, 1]) { box(.36, .44, 2, M.oak, dx0 + 1.55, .54, hz + s * 2.15, 0, 1); }   // benches behind the high table, either side of the chair
  for (const s of [-1, 1]) {
    const z = hz + s * 4.1;
    table(-19.9, z, 6.4, true, s < 0);
    box(6.4, .42, .32, M.oak, -19.9, .21, z - s * .75, 0, 1.4); solid(-19.9, z - s * .75, 6.4, .32);
  }
  // cups, bowls, jugs and loaves on the tables
  const cupG = new THREE.CylinderGeometry(.045, .035, .12, 10), bowlG = new THREE.SphereGeometry(.12, 12, 6, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2), jugG = new THREE.LatheGeometry([[0, 0], [.08, 0], [.11, .08], [.1, .2], [.06, .28], [.065, .33], [0, .33]].map(([a, b]) => new THREE.Vector2(a, b)), 12), loafG = new THREE.SphereGeometry(.1, 10, 6);
  loafG.scale(1.3, .55, 1);
  bowlG.rotateX(Math.PI);
  const onTable = (x, z, n, alongX) => { for (let i = 0; i < n; i++) { const t = (i + .5) / n - .5, px = alongX ? x + t * 5.8 : x + (R() - .5) * .3, pz = alongX ? z + (R() - .5) * .3 : z + t * 6.2; const k = R(); if (k < .4) add(cupG.clone(), R() < .5 ? M.horn : M.clay, mtx(px, .88, pz)); else if (k < .65) add(bowlG.clone(), M.oak, mtx(px, .94, pz)); else if (k < .85) add(loafG.clone(), M.bread, mtx(px, .86, pz, R() * 3)); else add(jugG.clone(), M.glaze, mtx(px, .82, pz)); } };
  onTable(dx0 + 2.35, hz, 10, false); onTable(-19.9, hz - 4.1, 9, true); onTable(-19.9, hz + 4.1, 7, true);
  for (let i = 0; i < 5; i++) add(cupG.clone(), M.gold, mtx(dx0 + 2.2, .88, hz - 1.6 + i * .8));
  // the pencerdd's harp by the fire, and a gaming board
  {
    const hp = mtx(-17.3, 0, -13.6, -.6);
    const st = new THREE.CylinderGeometry(.2, .22, .45, 8); st.translate(0, .225, 0); add(st, M.oak, hp.clone());
    // the harp: a soundbox leaning back, a curved neck, a straight pillar in front, and strings of horsehair
    const bar = (a, b, w, d, mat) => { const L = Math.hypot(b[0] - a[0], b[1] - a[1]); const g = new THREE.BoxGeometry(L, w, d); g.rotateZ(Math.atan2(b[1] - a[1], b[0] - a[0])); g.translate((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0); add(g, mat, hp.clone()); };
    bar([0, .47], [.16, 1.4], .13, .12, M.oak); bar([.16, 1.4], [.36, 1.36], .07, .05, M.oak); bar([.36, 1.36], [.6, 1.2], .07, .05, M.oak); bar([.6, 1.2], [.1, .5], .05, .05, M.oak);
    for (let i = 0; i < 10; i++) { const t = (i + 1) / 11, bx = .02 + t * .14, by = .55 + t * .82, tx = .16 + t * .44, ty = 1.39 - t * .19; const g = new THREE.CylinderGeometry(.003, .003, 1, 3); const L = Math.hypot(tx - bx, ty - by); g.scale(1, L, 1); g.rotateZ(-Math.atan2(tx - bx, ty - by)); g.translate((bx + tx) / 2, (by + ty) / 2, 0); add(g, M.gold, hp.clone(), true); }
    box(.5, .04, .5, M.oak, -13.4, .55, -12.4, .3, .5); box(.3, .55, .3, M.oak, -13.4, .27, -12.4, .3, .5); posts.push([-13.4, -12.4, .4]);
    // a gwyddbwyll board: squares burnt into the wood, the pegs of a game left as it stood
    for (let i = 0; i < 7; i++) for (let j = 0; j < 7; j++) if ((i + j) % 2) box(.06, .006, .06, M.soot, -13.4 + (i - 3) * .062, .573, -12.4 + (j - 3) * .062, 0, .5);
    for (let k = 0; k < 9; k++) cyl(.014, .014, .05, k ? M.oak : M.gold, -13.4 + (R() - .5) * .38, .6, -12.4 + (R() - .5) * .38, 6);
  }
  // torches in iron brackets on the posts
  const torches = [[bays[0], postZ[0] + .25], [bays[0], postZ[1] - .25], [bays[2], postZ[0] + .25], [bays[2], postZ[1] - .25]];
  for (const [x, z] of torches) { cyl(.025, .02, .5, M.iron, x, 2.75, z, 5); cyl(.04, .03, .45, M.oak, x, 3.05, z, 6); }

  // the chamber: a bed with curtains, chests, a chair, a hanging, a brazier
  {
    const bx = 3, bz = -21.4;
    box(2.2, .5, 1.7, M.oak, bx, .3, bz, 0, 1); box(2.15, .22, 1.65, M.red, bx, .62, bz, 0, 1); box(.5, .14, 1.5, M.linen, bx + .8, .78, bz, 0, 1);
    for (const [px, pz] of [[-1.1, -.85], [1.1, -.85], [-1.1, .85], [1.1, .85]]) cyl(.05, .05, 2.4, M.oak, bx + px, 1.2, bz + pz, 6);
    box(2.3, .06, 1.8, M.oak, bx, 2.4, bz, 0, 1);
    for (const [w, d, x, z] of [[2.3, .02, 0, -.88], [.02, 1.8, 1.12, 0]]) box(w, 1.6, d, M.green, bx + x, 1.6, bz + z, 0, 1);
    for (const s of [-1, 1]) { const g = new THREE.PlaneGeometry(.6, 1.9, 4, 1), p = g.attributes.position; for (let i = 0; i < p.count; i++) p.setZ(i, Math.sin(p.getX(i) * 18) * .04); g.computeVertexNormals(); add(g, M.green, mtx(bx - 1.12 + .3, 1.42, bz + s * .87)); }
    solid(bx, bz, 2.3, 1.8);
    box(1.1, .6, .6, M.oak, -1.8, .3, CB.iz0 + .4, 0, .8); box(1.12, .06, .62, M.iron, -1.8, .58, CB.iz0 + .4, 0, .8); solid(-1.8, CB.iz0 + .4, 1.1, .6);
    box(.9, .5, .5, M.oak, -6, .25, CB.iz1 - .35, 0, .8); solid(-6, CB.iz1 - .35, .9, .5);
    box(.55, .45, .5, M.oak, 0, .45, -19.5, 0, .8); box(.08, 1.1, .5, M.oak, -.24, .9, -19.5, 0, .8); box(.5, .1, .5, M.red, .02, .73, -19.5);
    const g = new THREE.PlaneGeometry(3, 1.8); add(g, M.hangG, mtx(-1.2, 1.9, CB.iz0 + .03));
    const br = new THREE.CylinderGeometry(.35, .2, .3, 10, 1, true); add(br, M.iron, mtx(-2.4, .55, -19.4)); cyl(.03, .03, .45, M.iron, -2.4, .2, -19.4, 4);
  }

  // the kitchen: an open fire with a cauldron on a chain, a table, barrels, sacks, a quern; the bread oven outside
  const kfx = -26.8, kfz = 14;
  for (let i = 0; i < 12; i++) { const a = i / 12 * Math.PI * 2; const g = new THREE.DodecahedronGeometry(.17, 0); add(g, M.stone, mtx(kfx + Math.cos(a) * .7, .08, kfz + Math.sin(a) * .7, R() * 3)); }
  posts.push([kfx, kfz, .9]);
  { const ca = new THREE.SphereGeometry(.38, 14, 8, 0, Math.PI * 2, Math.PI * .35, Math.PI * .65); add(ca, M.iron, mtx(kfx, .95, kfz)); cyl(.012, .012, 1.6, M.iron, kfx, 2.1, kfz, 3); for (const a of [0, 2.1, 4.2]) { const g = new THREE.CylinderGeometry(.04, .05, 3.2, 5); g.rotateZ(.32); g.translate(.5, 1.5, 0); add(g, M.oak, mtx(kfx, 0, kfz, a)); } }
  box(2.4, .08, .9, M.oak, -23.4, .82, 12.1, 0, 1.2); for (const s of [-1, 1]) box(.08, .78, .7, M.oak, -23.4 + s * 1, .39, 12.1, 0, 1); solid(-23.4, 12.1, 2.4, .9);
  add(loafG.clone(), M.bread, mtx(-23, .9, 12.1)); add(loafG.clone(), M.bread, mtx(-23.4, .9, 12.2, 1)); add(bowlG.clone(), M.oak, mtx(-24, .97, 12));
  const barrelG = new THREE.LatheGeometry([[0, 0], [.27, 0], [.32, .2], [.34, .4], [.32, .6], [.27, .8], [0, .8]].map(([a, b]) => new THREE.Vector2(a, b)), 14);
  for (let i = 0; i < 3; i++) { add(barrelG.clone(), M.oak, mtx(-20.4 + i * .1, 0, 15.9 - i * .75 - 0, R())); posts.push([-20.4 + i * .1, 15.9 - i * .75, .35]); }
  for (let i = 0; i < 4; i++) { const g = new THREE.SphereGeometry(.3, 10, 8); g.scale(1, 1.25, .9); add(g, M.straw, mtx(-27.5 + i * .55, .35, 15.9, R() * 3)); }
  box(.9, .5, .7, M.stone, -20.6, .25, 19.4, 0, 1);
  { const ov = new THREE.SphereGeometry(1.3, 18, 10, 0, Math.PI * 2, 0, Math.PI / 2); const uv = ov.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) * 4, uv.getY(i) * 1.2); add(ov, M.daub, mtx(-17, 0, 19.5)); posts.push([-17, 19.5, 1.4]); }

  // the stables inside: stalls and a hay rack; the barn: sheaves of oats and the threshing floor
  for (let x = SB.ix0 + 2.2; x < SB.ix1 - 1; x += 2.2) { box(.1, 1.3, 2.4, M.oak, x, .65, SB.iz1 - 1.2, 0, 1); }
  box(SB.ix1 - SB.ix0 - .4, .5, .4, M.oak, (SB.ix0 + SB.ix1) / 2, 1.5, SB.iz1 - .3, 0, 1.2); box(SB.ix1 - SB.ix0 - .4, .2, .3, M.straw, (SB.ix0 + SB.ix1) / 2, 1.85, SB.iz1 - .3, 0, 1);
  for (let i = 0; i < 26; i++) { const g = new THREE.CylinderGeometry(.16, .2, .9, 7); add(g, M.straw, mtx(BB.ix0 + .6 + (i % 13) * .5, .45 + Math.floor(i / 13) * .0, BB.iz0 + .4 + Math.floor(i / 13) * .45, 0, .1 * (R() - .5))); }
  // the yard: a well, a woodpile, a hay rick, a cart, a mounting block by the gate, wattle pens
  { const wg = new THREE.CylinderGeometry(.95, 1, .8, 16, 1, true); const uv = wg.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) * 3, uv.getY(i) * .4); add(wg, M.stone, mtx(8, .4, 2.5)); add(new THREE.CircleGeometry(.95, 16).rotateX(-Math.PI / 2), M.iron, mtx(8, .5, 2.5), true);
    for (const s of [-1, 1]) box(.14, 1.7, .14, M.oak, 8 + s * 1.05, .85, 2.5, 0, 1); cyl(.08, .08, 2.3, M.oak, 8, 1.55, 2.5, 8, 0, 0, Math.PI / 2); posts.push([8, 2.5, 1.2]);
    const bk = new THREE.CylinderGeometry(.16, .13, .3, 10); add(bk, M.oak, mtx(8.6, .65, 3.3)); }
  for (let i = 0; i < 30; i++) { const g = new THREE.CylinderGeometry(.09 + R() * .05, .1 + R() * .05, 1.1, 7); add(g, M.oak, mtx(-9 + (i % 8) * .24, .12 + Math.floor(i / 8) * .2, 5 + (R() - .5) * .1, 0, Math.PI / 2)); } solid(-8.2, 5, 2.2, 1.2);
  { const rk = new THREE.CylinderGeometry(.2, 2.1, 1.8, 14); const uv = rk.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) * 5, uv.getY(i)); add(rk, M.straw, mtx(33, 3.2, -6)); const rb = new THREE.CylinderGeometry(2.1, 2.2, 2.3, 14); const ub = rb.attributes.uv; for (let i = 0; i < ub.count; i++) ub.setXY(i, ub.getX(i) * 5, ub.getY(i) * 1.2); add(rb, M.straw, mtx(33, 1.15, -6)); posts.push([33, -6, 2.3]); }
  { const cm = mtx(20, 0, 6, .5); const bed = new THREE.BoxGeometry(2.6, .1, 1.4); bed.translate(0, .78, 0); add(bed, M.oak, cm.clone()); for (const s of [-1, 1]) { const sd = new THREE.BoxGeometry(2.6, .4, .06); sd.translate(0, 1, s * .7); add(sd, M.oak, cm.clone()); const wh = new THREE.TorusGeometry(.55, .06, 6, 18); wh.translate(-.3, .58, s * .82); add(wh, M.oak, cm.clone()); }
    const sh = new THREE.BoxGeometry(2.2, .08, .08); sh.translate(2.3, .55, .35); add(sh, M.oak, cm.clone()); const sh2 = sh.clone(); sh2.translate(0, 0, -.7); add(sh2, M.oak, cm.clone()); posts.push([20, 6, 1.5]); }
  box(1, .7, 1, M.stone, 37.5, .35, 4.5, .1, 1);
  function wattle(pts, h = 1.1) { for (let i = 0; i < pts.length - 1; i++) { const [a, b] = [pts[i], pts[i + 1]]; const L = Math.hypot(b[0] - a[0], b[1] - a[1]); const g = new THREE.BoxGeometry(L, h, .08); g.translate(L / 2, h / 2, 0); const uv = g.attributes.uv; for (let k = 0; k < uv.count; k++) uv.setXY(k, uv.getX(k) * L * 2, uv.getY(k) * h); add(g, M.wattle, mtx(a[0], 0, a[1], -Math.atan2(b[1] - a[1], b[0] - a[0]))); walls.push([a[0], a[1], b[0], b[1], .06]); for (let s = 0; s <= L; s += .6) cyl(.035, .035, h + .15, M.oak, a[0] + (b[0] - a[0]) * s / L, (h + .15) / 2, a[1] + (b[1] - a[1]) * s / L, 5); } }
  wattle([[30.2, 18], [30.2, 22.5], [36, 22.5], [36, 18.2]]);
  wattle([[-36, 18], [-36, 26], [-30, 26]], .95);

  // a few cottages of the maerdref, the court's own township, outside the walls; trees and hedges in the fields
  const cot = [[-120, -60, .3], [-150, -20, 1.1], [-128, 82, -.4], [-160, 60, .7], [110, -95, .2], [-60, -120, 1.4]];
  for (const [x, z, a] of cot) {
    const y = ground(x, z), m = mtx(x, y, z, a);
    const w = new THREE.BoxGeometry(7, 2, 4.2); w.translate(0, 1, 0); const uv = w.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) * 3, uv.getY(i)); add(w, M.daub, m.clone(), true);
    const r = new THREE.ConeGeometry(4.4, 3, 4, 1); r.rotateY(Math.PI / 4); r.scale(1.25, 1, .78); r.translate(0, 3.4, 0); const ru = r.attributes.uv; for (let i = 0; i < ru.count; i++) ru.setXY(i, ru.getX(i) * 6, ru.getY(i) * 3); add(r, M.thatch, m.clone(), true);
    walls.push([x - 4, z, x + 4, z, 2.4]);
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
    const y0 = o.y != null ? o.y : ground(x, z), B = mtx(x, y0, z, ry, 0, 0, o.h || 1);
    const put = (g, mat, tint) => add(g, mat, B.clone(), false, tint);
    const tun = C3(o.tunic || DYE.fawn), hose = C3(o.hose || DYE.brown), hair = C3(o.hair || HAIR[(R() * HAIR.length) | 0]);
    const sit = o.sit || 0, dy = sit ? sit - .75 : 0;
    // legs, or a gown to the ground
    if (o.woman && !sit) put(lathe([[0, .02], [.3, .02], [.27, .3], [.22, .7], [.17, .98], [.2, 1.2], [.21, 1.34], [.16, 1.44], [.07, 1.5], [0, 1.5]]), M.cloth, tun);
    else {
      for (const sx of [-.09, .09]) {
        if (sit) { put(limb([sx, sit + .07, -.02], [sx * 1.1, sit + .08, .44], .1, .08), M.cloth, tun); put(limb([sx * 1.1, sit + .05, .44], [sx * 1.1, .08, .47], .062, .052), M.cloth, o.woman ? tun : hose); put(boxG(.1, .08, .22, sx * 1.1, .04, .52), M.coat, leather); }
        else { put(limb([sx, .06, 0], [sx, .62, 0], .052, .066), M.cloth, hose); put(boxG(.1, .08, .23, sx, .04, .05), M.coat, leather); }
      }
      const body = sit ? [[0, .82], [.21, .82], [.19, .95], [.18, 1.0], [.2, 1.2], [.22, 1.36], [.17, 1.45], [.07, 1.5], [0, 1.5]]
        : [[0, .5], [.26, .5], [.23, .62], [.2, .85], [.18, 1.0], [.2, 1.2], [.22, 1.36], [.17, 1.45], [.07, 1.5], [0, 1.5]];
      const g = lathe(body.map(([a, b]) => [a, b + (sit ? dy : 0)])); g.scale(1, 1, .74); put(g, M.cloth, tun);
      if (!o.woman) { const bt = new THREE.TorusGeometry(.185, .018, 5, 16); bt.rotateX(Math.PI / 2); bt.scale(1, 1, .74); bt.translate(0, 1.0 + dy, 0); put(bt, M.coat, leather); }
    }
    if (o.woman && sit) { const g = lathe([[0, .82], [.22, .82], [.18, 1.0], [.2, 1.2], [.21, 1.34], [.16, 1.44], [.07, 1.5], [0, 1.5]].map(([a, b]) => [a, b + dy])); g.scale(1, 1, .74); put(g, M.cloth, tun); }
    // arms
    const arm = (side, el, hd) => { const sh = [side * .2, 1.38 + dy, 0]; put(limb(sh, el, .058, .05), M.cloth, tun); put(limb(el, hd, .048, .04), M.cloth, tun); put(ball(.045, ...hd), M.skin); };
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
      const v = new THREE.SphereGeometry(.118, 12, 9, Math.PI / 2 + 1.05, Math.PI * 2 - 2.1, 0, 2.3); v.scale(.95, 1.1, 1); v.translate(0, 1.69 + dy, -.005); put(v, M.cloth, C3(o.veil || DYE.linen));
      put(limb([0, 1.62 + dy, -.05], [0, 1.4 + dy, -.1], .1, .17, 10), M.cloth, C3(o.veil || DYE.linen));
    } else if (o.hood) {
      const v = new THREE.SphereGeometry(.125, 12, 9, Math.PI / 2 + .95, Math.PI * 2 - 1.9, 0, 2.2); v.scale(.95, 1.1, 1); v.translate(0, 1.69 + dy, -.01); put(v, M.cloth, C3(o.hood));
      put(lathe([[.24, 1.32], [.2, 1.42], [.12, 1.52], [0, 1.55]].map(([a, b]) => [a, b + dy])), M.cloth, C3(o.hood));
    } else {
      put(new THREE.SphereGeometry(.106, 12, 6, 0, Math.PI * 2, 0, 1.0).scale(.95, 1.1, 1).translate(0, 1.685 + dy, .005), M.coat, hair);
      const bk = new THREE.SphereGeometry(.108, 12, 8, Math.PI / 2 + .95, Math.PI * 2 - 1.9, 0, 2.0); bk.scale(.95, 1.1, 1); bk.translate(0, 1.685 + dy, 0); put(bk, M.coat, hair);
      if (o.beard) put(ball(.068, 0, 1.6 + dy, .055, 1, 1.15, .8), M.coat, hair);
    }
    if (o.cloak) {   // a cloak, open at the front, pinned at the shoulder
      const ch = sit ? .72 : 1.02, g = new THREE.CylinderGeometry(.205, sit ? .27 : .33, ch, 16, 1, true, Math.PI * .36, Math.PI * 1.28); g.scale(1, 1, .82); g.translate(0, 1.44 + dy - ch / 2, -.02); put(g, M.cloth, C3(o.cloak));
      put(ball(.025, .16, 1.42 + dy, .1), M.gold);
    }
    if (pose === "spear") { put(limb([.3, .02, .27], [.3, 2.35, .27], .02, .018), M.oak); put(limb([.3, 2.35, .27], [.3, 2.58, .27], .03, .002, 5), M.iron); const sg = shieldG.clone(); sg.scale(1.15, 1.15, 1); sg.translate(-.28, 1.0, .2); put(sg, o.shield || M.arms); }
    if (pose === "hold" && o.jug) put(jugG.clone().translate(.24, 1.02 + dy, .38), M.glaze);
    if (!o.free) posts.push([x, z, sit ? .26 : .3]);
  }
  // a horse of the Welsh kind, small and strong (about 14 hands)
  function horse(x, z, ry, coat, saddle) {
    const B = mtx(x, ground(x, z), z, ry), c = C3(coat), dk = C3(0x1e1915), put = (g, m, t) => add(g, m, B.clone(), false, t);
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
    if (saddle) { put(boxG(.66, .04, .7, 0, 1.36, -.02), M.cloth, C3(DYE.madder)); put(boxG(.5, .12, .56, 0, 1.42, -.02), M.coat, leather); }
    posts.push([x + Math.sin(ry) * .2, z + Math.cos(ry) * .2, .65]);
  }
  // hounds: tall, lean greyhounds and a rough-coated hound; lying by the fire, or standing
  function hound(x, z, ry, coat, lying, y0) {
    const B = mtx(x, y0 != null ? y0 : ground(x, z), z, ry), c = C3(coat), put = (g, m) => add(g, m, B.clone(), false, c);
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
    const B = mtx(x, ground(x, z), z, ry, 0, 0, .9 + R() * .2), fl = C3(k < .12 ? 0x4a3a2c : k < .2 ? 0xa59a88 : 0xf2ecdf), face = C3(k < .12 ? 0x2a211a : 0xb4a58c), put = (g, m, t) => add(g, m, B.clone(), true, t);
    put(ball(.4, 0, .55, 0, .82, .78, 1.15, 12), M.wool, fl);
    const graze = R() < .6;
    put(limb([0, .62, .3], graze ? [0, .42, .5] : [0, .72, .5], .16, .12), M.wool, fl); put(limb(graze ? [0, .42, .5] : [0, .72, .5], graze ? [0, .2, .64] : [0, .74, .66], .085, .055), M.coat, face);
    put(ball(.075, 0, graze ? .2 : .74, graze ? .64 : .66, .85, .9, 1.1), M.coat, face); for (const s of [-1, 1]) put(limb([s * .05, graze ? .4 : .78, graze ? .52 : .55], [s * .13, graze ? .38 : .76, graze ? .5 : .52], .022, .01, 4), M.coat, face);
    for (const [lx, lz] of [[-.13, .22], [.13, .22], [-.13, -.24], [.13, -.24]]) put(limb([lx, .35, lz], [lx, .01, lz], .04, .03, 5), M.coat, C3(0x2a2420));
  }
  function cow(x, z, ry) {
    const B = mtx(x, ground(x, z), z, ry), c = C3(0x1f1c1a), put = (g, m, t) => add(g, m, B.clone(), true, t || c);
    const bd = new THREE.CapsuleGeometry(.4, 1.0, 4, 12); bd.rotateX(Math.PI / 2); bd.scale(1, 1.08, 1); bd.translate(0, .98, 0); put(bd, M.coat);
    const graze = R() < .5;
    put(limb([0, 1.05, .7], graze ? [0, .45, 1.05] : [0, 1.0, 1.05], .24, .17, 9), M.coat); put(ball(.15, 0, graze ? .35 : .92, graze ? 1.12 : 1.18, .9, 1, 1.25), M.coat);
    for (const s of [-1, 1]) put(limb([s * .1, graze ? .52 : 1.08, graze ? 1.04 : 1.08], [s * .3, graze ? .6 : 1.2, graze ? 1.0 : 1.04], .03, .01, 5), M.coat, C3(0xd6cbb0));
    for (const [lx, lz] of [[-.2, .5], [.2, .5], [-.2, -.52], [.2, -.52]]) put(limb([lx, .8, lz], [lx, .02, lz], .085, .055), M.coat);
    put(limb([0, 1.2, -.85], [0, .45, -.95], .04, .03, 5), M.coat);
  }
  function goose(x, z, ry) {
    const B = mtx(x, ground(x, z), z, ry, 0, 0, .9 + R() * .2), put = (g, m, t) => add(g, m, B.clone(), true, t);
    const w = C3(R() < .7 ? 0xf2efe6 : 0x9a948a);
    put(ball(.2, 0, .3, 0, .78, .72, 1.25), M.coat, w); put(limb([0, .36, .18], [0, .62, .25], .05, .04), M.coat, w); put(ball(.055, 0, .65, .27), M.coat, w);
    put(limb([0, .64, .3], [0, .62, .38], .022, .006, 5), M.coat, C3(0xe08a2a));
    for (const s of [-1, 1]) put(limb([s * .06, .16, 0], [s * .06, .0, .02], .015, .012, 4), M.coat, C3(0xe08a2a));
  }

  // the people of the court
  const tz = hz;
  // at the gate: two of the teulu, the prince's war-band, with spears and shields
  person(44.4, -1.75, Math.PI / 2, { arms: "spear", tunic: DYE.madder, hose: DYE.black, cloak: DYE.woad, beard: true, h: 1.03 });
  person(44.4, 2.65, Math.PI / 2, { arms: "spear", tunic: DYE.woad, hose: DYE.brown, cloak: DYE.green, shield: M.red, h: 1.0 });
  horse(36.2, 6.6, -2.2, 0x5a3820, true);
  // in the hall: the household at the long tables, the uchelwyr at the high table either side of the prince's chair
  const hallSeat = (x, z, ry, i, high) => person(x, z, ry, { sit: high ? .76 : .42, y: 0, tunic: [DYE.madder, DYE.woad, DYE.green, DYE.weld, DYE.rust, DYE.plum][i % 6], hose: DYE.black, cloak: high && i % 2 ? [DYE.woad, DYE.madder][i % 2] : (i % 3 === 0 ? DYE.fawn : 0), beard: i % 3 === 1, woman: !high && i % 4 === 2, veil: i % 8 === 2 ? DYE.linen : 0xd9cfb8 });
  [-21.7, -20.7, -19.7, -17.9, -17.0].forEach((x, i) => hallSeat(x, tz - 4.1 + .75, Math.PI, i));
  [-21.4, -20.4, -17.6].forEach((x, i) => hallSeat(x, tz + 4.1 - .75, 0, i + 5));
  [-2.55, -1.75, 1.75, 2.55].forEach((d, i) => hallSeat(dx0 + 1.55, tz + d, Math.PI / 2, i, true));
  // a servant bringing a jug of mead, and the bard standing to speak
  person(-16.8, -9.6, -Math.PI / 2 - .3, { arms: "hold", jug: true, tunic: DYE.fawn, hose: DYE.grey });
  person(-14.6, -13.9, -Math.PI / 2 + .5, { tunic: DYE.green, cloak: DYE.madder, beard: true, hair: 0x8a7a68 });
  hound(-17.4, -11.0, -2.3, 0x8f7454, true, 0); hound(-21.3, -12.6, 1.2, 0x4a3f36, true, 0);
  // the kitchen: the cook at the cauldron, a maid at the table
  person(-25.95, 13.35, Math.atan2(-.85, .65), { arms: "work", tunic: DYE.brown, hose: DYE.grey, hood: DYE.fawn });
  person(-23.4, 12.85, Math.PI, { arms: "work", woman: true, tunic: DYE.weld, veil: 0xd9cfb8 });
  // the yard: the pengwastrawd's grooms with the horses at the stables, a woman at the well, a man at the woodpile
  horse(4.6, 18.6, Math.PI / 2, 0x6b3d22); horse(12.4, 18.9, -Math.PI / 2 + .2, 0x8f8a80); horse(15.2, 18.7, -Math.PI / 2 - .15, 0x2b2420);
  person(10.6, 18.3, Math.PI / 2 + .3, { tunic: DYE.fawn, hose: DYE.brown, hood: DYE.green });
  person(9.25, 3.55, -2.5, { woman: true, tunic: DYE.woad, veil: 0xd9cfb8 });
  add(new THREE.CylinderGeometry(.14, .11, .26, 10), M.oak, mtx(9.55, .13, 3.95));
  person(-8.2, 6.35, Math.PI, { arms: "work", tunic: DYE.rust, hose: DYE.brown });
  // the hounds in the kennel yard, and geese in the pen by the kitchen
  hound(32, 20, .6, 0xd8cdb8); hound(34.2, 19.4, -1.9, 0x5a4a3c); hound(33.4, 21.5, 2.6, 0xb08a60, true);
  for (let i = 0; i < 7; i++) goose(-34.6 + R() * 3.6, 19.6 + R() * 5, R() * 6.3);
  // the fields: a flock of sheep and their shepherd on the pasture toward the sands, black cattle to the east
  for (let i = 0; i < 46; i++) { const a = R() * 6.3, r = Math.sqrt(R()) * 26; sheep(-82 + Math.cos(a) * r * 1.3, 58 + Math.sin(a) * r, R() * 6.3, R()); }
  person(-70, 46, -.9, { tunic: DYE.grey, hose: DYE.brown, cloak: DYE.fawn, hood: DYE.brown, free: true });
  for (let i = 0; i < 9; i++) cow(98 + R() * 26, -62 + R() * 16, R() * 6.3);

  // the banks round the fields: earth faced with stone, grass on top
  {
    const done = new Set();
    for (const q of parcels) for (let k = 0; k < 4; k++) {
      const a = q[k], b = q[(k + 1) % 4], key = [a, b].map((p) => p.map((v) => v.toFixed(1)).join(",")).sort().join("|");
      if (done.has(key)) continue; done.add(key);
      const mx = (a[0] + b[0]) / 2, mz = (a[1] + b[1]) / 2; if (Math.hypot(mx, mz) > 480 || Math.hypot(mx, mz) < 100) continue;
      // open fields had few boundaries: only some edges have a bank, and none in the way of the views to Eryri and to the sea
      const bearing = (Math.atan2(mx, -mz) * 180 / Math.PI + 360) % 360;
      if (R() < .45 || (bearing > 95 && bearing < 135) || (bearing > 200 && bearing < 250)) continue;
      const L = Math.hypot(b[0] - a[0], b[1] - a[1]), ry = -Math.atan2(b[1] - a[1], b[0] - a[0]), n = Math.ceil(L / 8);
      for (let i = 0; i < n; i++) {   // in pieces, so the bank follows the ground
        const t0 = i / n, t1 = (i + 1) / n, x0 = a[0] + (b[0] - a[0]) * t0, z0 = a[1] + (b[1] - a[1]) * t0, x1 = a[0] + (b[0] - a[0]) * t1, z1 = a[1] + (b[1] - a[1]) * t1;
        const y = (ground(x0, z0) + ground(x1, z1)) / 2, l = L / n + .05;
        const g = new THREE.BoxGeometry(l, 1, 1.3); const uv = g.attributes.uv; for (let k2 = 0; k2 < uv.count; k2++) uv.setXY(k2, uv.getX(k2) * l / 2.2, uv.getY(k2) * .45);
        add(g, M.stone, mtx((x0 + x1) / 2, y + .32, (z0 + z1) / 2, ry), true);
        const tg = new THREE.BoxGeometry(l, .3, 1.2); add(tg, M.turf, mtx((x0 + x1) / 2, y + .92, (z0 + z1) / 2, ry), true);
      }
      walls.push([a[0], a[1], b[0], b[1], .65]);
    }
  }

  // ---------- merge ----------
  for (const [mat, list] of buckets) {
    const g = mergeGeometries(list, false); if (!g) continue;
    const mesh = new THREE.Mesh(g, mat); mesh.castShadow = mesh.receiveShadow = true; mesh.matrixAutoUpdate = false; scene.add(mesh);
  }
  buckets.clear();

  // ---------- THE LAND ----------
  // near: a round mesh, fine at the middle and coarser outward, out to 900 m
  {
    const rings = [], A = small ? 96 : 160;
    let r = 0, step = .9; while (r < 900) { rings.push(r); r += step; step *= r < 60 ? 1.0 : 1.045; }
    rings.push(900);
    const pos = [], uv = [], idx = [];
    for (let i = 0; i < rings.length; i++) for (let j = 0; j < (i ? A : 1); j++) {
      const a = j / A * Math.PI * 2, x = Math.cos(a) * rings[i], z = Math.sin(a) * rings[i];
      pos.push(x, ground(x, z), z); uv.push(x / 3, z / 3);
    }
    const at = (i, j) => (i === 0 ? 0 : 1 + (i - 1) * A + (j % A));
    for (let i = 0; i < rings.length - 1; i++) for (let j = 0; j < A; j++) {
      if (i === 0) idx.push(0, at(1, j + 1), at(1, j));
      else idx.push(at(i, j), at(i, j + 1), at(i + 1, j), at(i, j + 1), at(i + 1, j + 1), at(i + 1, j));
    }
    const g = new THREE.BufferGeometry(); g.setAttribute("position", new THREE.Float32BufferAttribute(pos, 3)); g.setAttribute("uv", new THREE.Float32BufferAttribute(uv, 2)); g.setIndex(idx); g.computeVertexNormals();
    const mat = new THREE.MeshStandardMaterial({ map: grassTex, roughness: 1 });
    mat.onBeforeCompile = (s) => {
      s.uniforms.splat = { value: splatTex }; s.uniforms.earth = { value: earthTex }; s.uniforms.landC = { value: landC }; s.uniforms.fields = { value: fieldTex };
      s.vertexShader = s.vertexShader.replace("#include <common>", "#include <common>\nvarying vec3 vW;").replace("#include <worldpos_vertex>", "#include <worldpos_vertex>\nvW = (modelMatrix * vec4(transformed, 1.)).xyz;");
      s.fragmentShader = s.fragmentShader.replace("#include <common>", "#include <common>\nvarying vec3 vW; uniform sampler2D splat, earth, landC, fields;")
        .replace("#include <map_fragment>", `
          vec2 suv = vW.xz / ${SPW.toFixed(1)} + .5;
          float wornA = texture2D(splat, suv).r * step(0., suv.x) * step(suv.x, 1.) * step(0., suv.y) * step(suv.y, 1.);
          vec3 g1 = texture2D(map, vMapUv).rgb, g2 = texture2D(map, vMapUv * .21 + .37).rgb, e = texture2D(earth, vMapUv * .8).rgb;
          vec3 gr = mix(g1, g2, .45) * (0.86 + .28 * texture2D(map, vMapUv * .031).g);
          gr = mix(vec3(dot(gr, vec3(.3, .55, .15))), gr, .8);
          float d = length(vW.xz);
          vec3 far = texture2D(landC, vec2(vW.x, -vW.z) / ${(2 * HALF).toFixed(1)} + .5).rgb * 1.08;
          vec3 fc = texture2D(fields, vW.xz / ${FW.toFixed(1)} + .5).rgb;
          float lum = dot(mix(g1, g2, .45), vec3(.3, .55, .15)) / .36;
          vec3 fld = fc * mix(1., lum, .55) * 1.1;
          vec3 c = mix(gr, fld, smoothstep(70., 130., d));
          c = mix(c, e, smoothstep(.15, .7, wornA));
          c = mix(c, far, smoothstep(620., 880., d));
          diffuseColor.rgb *= c;`);
    };
    const land = new THREE.Mesh(g, mat); land.receiveShadow = true; scene.add(land);
  }
  // far: the real land, 64 km across, with the court's own patch sunk beneath the near mesh
  {
    const N = small ? 192 : 384, g = new THREE.PlaneGeometry(2 * HALF, 2 * HALF, N - 1, N - 1);
    g.rotateX(-Math.PI / 2);
    const p = g.attributes.position;
    for (let i = 0; i < p.count; i++) {
      const x = p.getX(i), z = p.getZ(i), r = Math.hypot(x, z);
      let y = dem(x, z) - H0 - curve(r);
      y -= 4 * (1 - smooth(820, 1100, r));
      p.setY(i, Math.max(y, -H0 - curve(r) - 25));
    }
    g.computeVertexNormals();
    const mat = new THREE.MeshStandardMaterial({ map: landC, normalMap: landN, normalMapType: THREE.ObjectSpaceNormalMap, roughness: 1 });
    const far = new THREE.Mesh(g, mat); scene.add(far);
  }
  // the sea: sky reflected more as you look across it, broken by small waves, a path of sunlight
  const sunDir = new THREE.Vector3().setFromSphericalCoords(1, THREE.MathUtils.degToRad(90 - SUN[1]), Math.PI - THREE.MathUtils.degToRad(SUN[0]));
  // (three's spherical coordinates: theta from +z toward +x; the scene's north is -z, so azimuth A puts the sun at (sin A, ., -cos A))
  sunDir.set(Math.sin(THREE.MathUtils.degToRad(SUN[0])) * Math.cos(THREE.MathUtils.degToRad(SUN[1])), Math.sin(THREE.MathUtils.degToRad(SUN[1])), -Math.cos(THREE.MathUtils.degToRad(SUN[0])) * Math.cos(THREE.MathUtils.degToRad(SUN[1])));
  const seaU = { time: { value: 0 }, sunDir: { value: sunDir }, deep: { value: new THREE.Color(0x173447) }, skyC: { value: new THREE.Color(0x6f8ba6) }, fogC: { value: fogCol }, fogD: { value: scene.fog.density } };
  {
    const g = new THREE.PlaneGeometry(2 * HALF * 2.5, 2 * HALF * 2.5, 200, 200); g.rotateX(-Math.PI / 2);
    { const p = g.attributes.position; for (let i = 0; i < p.count; i++) p.setY(i, -curve(Math.hypot(p.getX(i), p.getZ(i)))); }
    const m = new THREE.ShaderMaterial({ uniforms: seaU, transparent: true, depthWrite: true,
      vertexShader: "#include <common>\n#include <logdepthbuf_pars_vertex>\nvarying vec3 vW;void main(){vec4 w=modelMatrix*vec4(position,1.);vW=w.xyz;gl_Position=projectionMatrix*viewMatrix*w;\n#include <logdepthbuf_vertex>\n}",
      fragmentShader: `#include <logdepthbuf_pars_fragment>
uniform float time,fogD;uniform vec3 sunDir,deep,skyC,fogC;varying vec3 vW;
        float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
        float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}
        vec2 g(vec2 p){float e=.1;return vec2(n(p+vec2(e,0))-n(p-vec2(e,0)),n(p+vec2(0,e))-n(p-vec2(0,e)))/(2.*e);}
        void main(){
#include <logdepthbuf_fragment>
vec3 V=cameraPosition-vW;float d=length(V);V/=d;
          vec2 p=vW.xz*.035;vec2 s=g(p+vec2(time*.06,time*.04))*.5+g(p*2.7-vec2(time*.09,0.))*.3+g(p*7.3+vec2(0.,time*.15))*.2;
          float k=clamp(1.-d/9000.,0.,1.);vec3 N=normalize(vec3(-s.x*.35*k,1.,-s.y*.35*k));
          float fr=.03+.6*pow(1.-max(dot(N,V),0.),5.);
          vec3 R=reflect(-V,N);float sp=pow(max(dot(R,sunDir),0.),220.)*5.+pow(max(dot(R,sunDir),0.),18.)*.25;
          vec3 c=mix(deep,skyC,fr)+vec3(1.,.86,.62)*sp;
          float f=1.-exp(-pow(fogD*d,2.));c=mix(c,fogC,f);
          gl_FragColor=vec4(c,1.);
          #include <tonemapping_fragment>
          #include <colorspace_fragment>
        }`,
    });
    const sea = new THREE.Mesh(g, m); sea.position.y = -H0 + .3; sea.renderOrder = -1; scene.add(sea);
  }
  // the sky, and the light it gives (an environment map made from it)
  const sky = new Sky(); sky.scale.setScalar(70000);
  const su = sky.material.uniforms;
  su.turbidity.value = 2.6; su.rayleigh.value = 1.7; su.mieCoefficient.value = .0028; su.mieDirectionalG.value = .8;
  su.sunPosition.value.copy(sunDir);
  sky.renderOrder = -2; sky.material.depthTest = false; scene.add(sky);
  {
    const pm = new THREE.PMREMGenerator(renderer), sc = new THREE.Scene(), s2 = new Sky(); s2.scale.setScalar(60); s2.material.uniforms.sunPosition.value.copy(sunDir);
    s2.material.uniforms.turbidity.value = 2.6; s2.material.uniforms.rayleigh.value = 1.7; s2.material.uniforms.mieCoefficient.value = .0028;
    sc.add(s2);
    const gnd = new THREE.Mesh(new THREE.CircleGeometry(50, 24).rotateX(-Math.PI / 2), new THREE.MeshBasicMaterial({ color: 0x3c4a2c })); gnd.position.y = -1; sc.add(gnd);
    scene.environment = pm.fromScene(sc, .04).texture; pm.dispose();
  }
  // clouds: one high layer of soft summer cumulus, drawn by a shader
  const cloudU = { time: { value: 0 }, sunDir: { value: sunDir } };
  {
    const g = new THREE.PlaneGeometry(120000, 120000); g.rotateX(Math.PI / 2);
    const m = new THREE.ShaderMaterial({ uniforms: cloudU, transparent: true, depthWrite: false, side: THREE.DoubleSide, fog: false,
      vertexShader: "#include <common>\n#include <logdepthbuf_pars_vertex>\nvarying vec3 vW;void main(){vec4 w=modelMatrix*vec4(position,1.);vW=w.xyz;gl_Position=projectionMatrix*viewMatrix*w;\n#include <logdepthbuf_vertex>\n}",
      fragmentShader: `#include <logdepthbuf_pars_fragment>
uniform float time;uniform vec3 sunDir;varying vec3 vW;
        float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
        float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}
        float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<5;i++){v+=a*n(p);p=p*2.03+17.;a*=.5;}return v;}
        void main(){
#include <logdepthbuf_fragment>
vec2 p=vW.xz/2600.+vec2(time*.004,time*.002);
          float c=fbm(p),c2=fbm(p+sunDir.xz*.06);
          float cov=smoothstep(.54,.78,c);
          float lit=clamp(.55+(c-c2)*5.,0.,1.2);
          vec3 col=mix(vec3(.55,.58,.64),vec3(1.,.95,.86),lit);
          float d=length(vW.xz-cameraPosition.xz);
          float fade=1.-smoothstep(16000.,52000.,d);
          gl_FragColor=vec4(col*1.6,cov*.92*fade);
          #include <tonemapping_fragment>
          #include <colorspace_fragment>
        }`,
    });
    const cl = new THREE.Mesh(g, m); cl.position.y = 1500; cl.renderOrder = 1; scene.add(cl);
  }

  const noFlip = (s) => { s.fragmentShader = s.fragmentShader.replace("#include <normal_fragment_begin>", THREE.ShaderChunk.normal_fragment_begin.replace("normal *= faceDirection;", "")); };
  // ---------- grass and nettles in the fields, swaying ----------
  const windU = { time: { value: 0 } };
  {
    const [bc, bx] = cv(128), [ba, bax] = cv(128);
    bx.fillStyle = "#76844f"; bx.fillRect(0, 0, 128, 128); bax.fillStyle = "#000"; bax.fillRect(0, 0, 128, 128);

    for (let i = 0; i < 70; i++) { const x0 = 6 + R() * 116, lean = (R() - .5) * 34, h = 50 + R() * 74, g = 130 + R() * 90; bx.strokeStyle = `rgb(${g * .68 | 0},${g * .82 | 0},${g * .46 | 0})`; bx.lineWidth = bax.lineWidth = 1.2 + R() * 2; bax.strokeStyle = "#fff"; for (const c of [bx, bax]) { c.beginPath(); c.moveTo(x0, 128); c.quadraticCurveTo(x0 + lean * .3, 128 - h * .6, x0 + lean, 128 - h); c.stroke(); } }
    for (let i = 0; i < 6; i++) { bx.fillStyle = `rgb(${170 + R() * 50},${150 + R() * 40},${90})`; const x0 = 10 + R() * 108, y0 = 10 + R() * 40; bax.fillStyle = "#fff"; for (const c of [bx, bax]) { c.beginPath(); c.ellipse(x0, y0, 2.5, 7, (R() - .5), 0, 7); c.fill(); } }
    const bt = tex(bc), bm = tex(ba, null, false); bt.wrapS = bt.wrapT = bm.wrapS = bm.wrapT = THREE.ClampToEdgeWrapping;
    const q = new THREE.PlaneGeometry(.6, .42); q.translate(0, .2, 0);
    const q2 = q.clone().rotateY(Math.PI / 2), q3 = q.clone().rotateY(Math.PI / 4);
    const tuft = mergeGeometries([q, q2, q3]);
    tuft.setAttribute("normal", new THREE.Float32BufferAttribute(new Float32Array(tuft.attributes.position.count * 3).map((v, i) => (i % 3 === 1 ? 1 : 0)), 3));
    const m = new THREE.MeshStandardMaterial({ map: bt, alphaMap: bm, alphaTest: .5, side: THREE.DoubleSide, roughness: 1 });
    m.onBeforeCompile = (s) => {
      s.uniforms.time = windU.time; noFlip(s);
      s.vertexShader = s.vertexShader.replace("#include <common>", "#include <common>\nuniform float time;").replace("#include <begin_vertex>", `#include <begin_vertex>
        vec4 ip = instanceMatrix * vec4(0.,0.,0.,1.);
        float sw = sin(time * 1.7 + ip.x * .23 + ip.z * .17) * .5 + sin(time * 3.1 + ip.x * .7) * .25;
        transformed.x += sw * .12 * position.y; transformed.z += sw * .06 * position.y;`);
    };
    const inst = new THREE.InstancedMesh(tuft, m, Q.grass); const mm = new THREE.Matrix4(), cc = new THREE.Color();
    let n = 0, tries = 0;
    while (n < Q.grass && tries++ < Q.grass * 6) {
      const r = 5 + Math.pow(R(), 1.6) * 70, a = R() * Math.PI * 2, x = Math.cos(a) * r, z = Math.sin(a) * r;
      if (worn(x, z) > .25 || inside(x, z, 1.2) || walls.some(([x1, z1, x2, z2, ht]) => { const vx = x2 - x1, vz = z2 - z1, L2 = vx * vx + vz * vz || 1; const t = clamp(((x - x1) * vx + (z - z1) * vz) / L2, 0, 1); return Math.hypot(x - x1 - vx * t, z - z1 - vz * t) < ht + .5; })) continue;
      const s = .6 + R() * .9;
      mm.compose(new THREE.Vector3(x, ground(x, z) - .02, z), new THREE.Quaternion().setFromEuler(new THREE.Euler(0, R() * 6.3, 0)), new THREE.Vector3(s, s * (.7 + R() * .6), s));
      inst.setMatrixAt(n, mm); inst.setColorAt(n, cc.setHSL(.19 + R() * .05, .25 + R() * .15, .42 + R() * .16)); n++;
    }
    inst.count = n; inst.receiveShadow = true; scene.add(inst);
  }
  // trees: wind-shaped hawthorn and ash in the hedgerows beyond the court
  {
    const [lc, lx3] = cv(128), [la, lax] = cv(128);
    lx3.fillStyle = "#4d6a2c"; lx3.fillRect(0, 0, 128, 128); lax.fillStyle = "#000"; lax.fillRect(0, 0, 128, 128);
    for (let i = 0; i < 1500; i++) { const g = 80 + R() * 100, a = R() * 6.28, r = Math.sqrt(R()) * 60, x = 64 + Math.cos(a) * r, y = 64 + Math.sin(a) * r, rx = 3 + R() * 3, ry2 = 1.5 + R() * 2, rot = R() * 3;
      lx3.fillStyle = `rgb(${g * .58 | 0},${g * .9 | 0},${g * .34 | 0})`; lax.fillStyle = "#fff"; for (const c of [lx3, lax]) { c.beginPath(); c.ellipse(x, y, rx, ry2, rot, 0, 7); c.fill(); } }
    const lt = tex(lc), lm2 = tex(la, null, false);
    const leaf = new THREE.MeshStandardMaterial({ map: lt, alphaMap: lm2, alphaTest: .5, side: THREE.DoubleSide, roughness: .9 }); leaf.onBeforeCompile = noFlip;
    const blob = new THREE.IcosahedronGeometry(1, 2);
    const fol = [], trunks = [];
    const spots = [[62, -60], [70, -20], [-75, -55], [-85, 20], [-104, 72], [40, 75], [95, 40], [-110, -15], [20, -85], [-30, 90], [120, -40], [-140, -70], [150, 62], [-60, -95], [85, 85], [-96, 44], [58, 98], [130, 70], [-120, 100], [10, 120]];
    const lean = [Math.cos(THREE.MathUtils.degToRad(SUN[0])) * 0 + .5, .35];   // shaped by the south-west wind: leaning north-east
    for (const [x, z] of spots) {
      const y = ground(x, z), s = 2.2 + R() * 2.2, cx = x + lean[0] * s * .45, cz = z - lean[1] * s * .45, cyy = y + s * 1.0;
      const tg = new THREE.CylinderGeometry(.12 * s / 2.4, .3 * s / 2.4, s * 1.05, 6); tg.translate(0, s * .52, 0); tg.rotateZ(-.28); tg.rotateY(.6); tg.translate(x, y, z); trunks.push(tg);
      for (let k = 0; k < 12; k++) {
        const b = blob.clone(), r = s * (.38 + R() * .3), ox = (R() - .35) * s * 1.0, oy = (R() - .35) * s * .75, oz = (R() - .5) * s * 1.0;
        b.scale(r * 1.1, r * .95, r * 1.1); b.translate(cx + ox, cyy + oy, cz + oz);
        // normals point out from the middle of the whole crown, so the tree is lit as one soft mass
        const p = b.attributes.position, nn = new Float32Array(p.count * 3);
        for (let i = 0; i < p.count; i++) { const v = new THREE.Vector3(p.getX(i) - cx, (p.getY(i) - cyy) * 1.4, p.getZ(i) - cz).normalize(); nn.set([v.x, v.y, v.z], i * 3); }
        b.setAttribute("normal", new THREE.BufferAttribute(nn, 3)); fol.push(b);
      }
    }
    const fg = mergeGeometries(fol.map((g) => (g.index ? g.toNonIndexed() : g)));
    const uvA = fg.attributes.uv; for (let i = 0; i < uvA.count; i++) uvA.setXY(i, uvA.getX(i) * 3, uvA.getY(i) * 3);
    const crowns = new THREE.Mesh(fg, leaf); crowns.castShadow = crowns.receiveShadow = true; scene.add(crowns);
    const tm = new THREE.Mesh(mergeGeometries(trunks), new THREE.MeshStandardMaterial({ map: oakTex, color: 0x8a8070, roughness: .9 })); tm.castShadow = true; scene.add(tm);
    for (const [x, z] of spots) posts.push([x, z, .5]);
  }

  // gulls from the Menai, wheeling over the court and the fields (moved each frame: see moveGulls)
  const GN = small ? 7 : 12, gullBody = [], gull = [];
  {
    const gm = new THREE.MeshStandardMaterial({ color: 0xf0efe9, roughness: .7, side: THREE.DoubleSide });
    const sh = new THREE.Shape(); sh.moveTo(0, .13); sh.lineTo(.3, .11); sh.lineTo(.74, -.03); sh.lineTo(.6, -.08); sh.lineTo(.3, -.1); sh.lineTo(0, -.1);
    const wr = new THREE.ShapeGeometry(sh); wr.rotateX(Math.PI / 2); const wl = wr.clone(); wl.scale(-1, 1, 1);
    const tip = new THREE.Color(0x3a3a3c), white = new THREE.Color(1, 1, 1);
    for (const w of [wr, wl]) { const p = w.attributes.position, c = new Float32Array(p.count * 3); for (let i = 0; i < p.count; i++) { const k = Math.abs(p.getX(i)) > .58 ? tip : white; c.set([k.r, k.g, k.b], i * 3); } w.setAttribute("color", new THREE.Float32BufferAttribute(c, 3)); }
    const wmat = gm.clone(); wmat.vertexColors = true;
    const bodyG = new THREE.SphereGeometry(.065, 8, 6); bodyG.scale(1, .9, 3.4);
    for (const [g, m] of [[bodyG, gm], [wr, wmat], [wl, wmat]]) { const im = new THREE.InstancedMesh(g, m, GN); im.frustumCulled = false; scene.add(im); gullBody.push(im); }
    for (let i = 0; i < GN; i++) gull.push({ c: [(R() - .5) * 140, 16 + R() * 34, (R() - .5) * 140], r: 25 + R() * 70, w: (R() < .5 ? -1 : 1) * (.09 + R() * .08), a: R() * 6.3, ph: R() * 9 });
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

  // ---------- light ----------
  const sun = new THREE.DirectionalLight(0xffe2bb, 3.3);
  sun.position.copy(sunDir).multiplyScalar(120); scene.add(sun, sun.target);
  sun.castShadow = true; sun.shadow.mapSize.set(Q.shadow, Q.shadow);
  Object.assign(sun.shadow.camera, { left: -38, right: 38, top: 38, bottom: -38, near: 1, far: 300 });
  sun.shadow.bias = -.0005; sun.shadow.normalBias = .04; sun.shadow.radius = 3;
  const hemi = new THREE.HemisphereLight(0xbcd2ff, 0x4c4433, .15); scene.add(hemi);
  // the hearth fire, which casts its own flickering shadows on larger screens
  const fire = new THREE.PointLight(0xff8a3c, 60, 0, 2); fire.position.set(hx, 1.0, hz); scene.add(fire);
  if (Q.fireShadow) { fire.castShadow = true; fire.shadow.mapSize.set(512, 512); fire.shadow.bias = -.004; fire.shadow.camera.near = .3; fire.shadow.camera.far = 22; fire.shadow.radius = 4; }
  const dais = new THREE.PointLight(0xffa860, 9, 0, 2); dais.position.set(dx0 + 2.4, 2.4, hz); scene.add(dais);
  const torchL = new THREE.PointLight(0xff9a4a, 6, 0, 2); torchL.position.set(bays[2], 3.4, hz); scene.add(torchL);
  const kfire = new THREE.PointLight(0xff8a3c, 22, 0, 2); kfire.position.set(kfx, .9, kfz); scene.add(kfire);
  const brazier = new THREE.PointLight(0xff9446, 9, 0, 2); brazier.position.set(-2.4, 1.1, -19.4); scene.add(brazier);

  // ---------- fire, smoke and dust: drawn by shaders on little cards that always face you ----------
  const fireU = { time: { value: 0 } };
  const flameMat = new THREE.ShaderMaterial({
    uniforms: fireU, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending,
    vertexShader: "#include <common>\n#include <logdepthbuf_pars_vertex>\nattribute vec4 off;varying vec2 vU;varying float vS;void main(){vU=uv;vS=off.w;vec3 c=off.xyz;vec4 mv=modelViewMatrix*vec4(c,1.);mv.xy+=position.xy*off.w;gl_Position=projectionMatrix*mv;\n#include <logdepthbuf_vertex>\n}",
    fragmentShader: `#include <logdepthbuf_pars_fragment>
uniform float time;varying vec2 vU;varying float vS;
      float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
      float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}
      void main(){
#include <logdepthbuf_fragment>
vec2 p=vU;float t=time*2.2+vS*31.;
        float q=n(vec2(p.x*4.+vS*9.,p.y*3.-t*1.6))*.6+n(vec2(p.x*9.,p.y*7.-t*2.6))*.4;
        float w=1.-abs(p.x-.5)*2.;float shape=w*(1.-p.y)*1.6-q*.75-p.y*.35;
        float a=smoothstep(.05,.45,shape);
        vec3 c=mix(vec3(1.,.28,.04),vec3(1.,.82,.45),smoothstep(.25,.9,shape));
        gl_FragColor=vec4(c*a*1.8,a);
        #include <tonemapping_fragment>
        #include <colorspace_fragment>
      }`,
  });
  function cards(list, mat) {
    const g = new THREE.InstancedBufferGeometry(); const q = new THREE.PlaneGeometry(1, 1); q.translate(0, .5, 0);
    g.setIndex(q.index); g.setAttribute("position", q.attributes.position); g.setAttribute("uv", q.attributes.uv);
    g.setAttribute("off", new THREE.InstancedBufferAttribute(new Float32Array(list.flat()), 4)); g.instanceCount = list.length;
    const m = new THREE.Mesh(g, mat); m.frustumCulled = false; m.renderOrder = 3; scene.add(m); return m;
  }
  const fl = [];
  for (let i = 0; i < 6; i++) fl.push([hx + (R() - .5) * .7, .02, hz + (R() - .5) * .5, .7 + R() * .4]);
  for (let i = 0; i < 3; i++) fl.push([kfx + (R() - .5) * .4, .02, kfz + (R() - .5) * .4, .45 + R() * .2]);
  for (const [x, z] of torches) fl.push([x, 3.25, z, .3]);
  fl.push([-2.4, .66, -19.4, .32]);
  cards(fl, flameMat);
  // logs and embers on the hearth
  const emberMat = new THREE.MeshBasicMaterial({ color: 0xff5a1a });
  { const e = new THREE.Mesh(new THREE.CircleGeometry(.8, 20).rotateX(-Math.PI / 2), emberMat); e.scale.set(1.2, 1, 1); e.position.set(hx, .04, hz); scene.add(e);
    const e2 = e.clone(); e2.scale.set(.55, 1, .55); e2.position.set(kfx, .04, kfz); scene.add(e2);
    const lg = []; for (let i = 0; i < 6; i++) lg.push(new THREE.CylinderGeometry(.07, .09, 1.2, 6).rotateZ(Math.PI / 2 - .18).rotateY(i * 1.05).translate(hx, .14, hz));
    const lm = new THREE.Mesh(mergeGeometries(lg), new THREE.MeshStandardMaterial({ color: 0x2a1a10, emissive: 0x401204, roughness: 1 })); scene.add(lm); }
  // smoke rising from the hearth, gathering under the roof and finding the louvre; smoke from the kitchen roof
  const smokeU = { time: { value: 0 }, light: { value: 1 } };
  const smokeMat = new THREE.ShaderMaterial({
    uniforms: smokeU, transparent: true, depthWrite: false,
    vertexShader: `#include <common>
#include <logdepthbuf_pars_vertex>
uniform float time;attribute vec4 off;attribute vec3 rise;varying vec2 vU;varying float vA;
      void main(){vU=uv;float life=fract(time/rise.z+off.w);vec3 c=off.xyz;
        float ht=life*rise.x;c.y+=ht;c.x+=sin(life*6.+off.w*30.)*.5*life+life*rise.y;c.z+=cos(life*5.+off.w*20.)*.4*life;
        float sz=.6+life*2.4;vA=sin(life*3.14159)*.55;
        vec4 mv=modelViewMatrix*vec4(c,1.);mv.xy+=(position.xy)*sz;gl_Position=projectionMatrix*mv;
#include <logdepthbuf_vertex>
}`,
    fragmentShader: `#include <logdepthbuf_pars_fragment>
uniform float light;varying vec2 vU;varying float vA;
      void main(){
#include <logdepthbuf_fragment>
vec2 p=vU-.5;float d=length(p);float a=smoothstep(.5,.0,d)*vA;
        a*=.75+.25*sin(p.x*13.+p.y*9.);gl_FragColor=vec4(vec3(.72,.7,.68)*light,a*.42);
        #include <tonemapping_fragment>
        #include <colorspace_fragment>
      }`,
  });
  {
    const q = new THREE.PlaneGeometry(1, 1), g = new THREE.InstancedBufferGeometry();
    g.setIndex(q.index); g.setAttribute("position", q.attributes.position); g.setAttribute("uv", q.attributes.uv);
    const off = [], rise = [];
    for (let i = 0; i < 26; i++) { off.push(hx, 1.2, hz, i / 26); rise.push(7.6, .4, 9); }              // in the hall
    for (let i = 0; i < 18; i++) { off.push(hx + .5, HB.ridge + 1.4, hz, i / 18); rise.push(14, 6, 14); }   // out of the louvre, drifting east
    for (let i = 0; i < 14; i++) { off.push(kfx + 1.5, KB.ridge + 1.3, kfz, i / 14); rise.push(12, 5, 12); }
    for (const [x, z] of cot.slice(0, 4)) for (let i = 0; i < 6; i++) { off.push(x, ground(x, z) + 4.6, z, i / 6); rise.push(10, 4, 10); }
    g.setAttribute("off", new THREE.InstancedBufferAttribute(new Float32Array(off), 4)); g.setAttribute("rise", new THREE.InstancedBufferAttribute(new Float32Array(rise), 3)); g.instanceCount = off.length / 4;
    const m = new THREE.Mesh(g, smokeMat); m.frustumCulled = false; m.renderOrder = 4; scene.add(m);
  }
  // shafts of sunlight through the hall's doors and windows, with dust turning in them
  const shaftU = { time: { value: 0 }, k: { value: 1 } };
  {
    const mat = new THREE.ShaderMaterial({ uniforms: shaftU, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide,
      vertexShader: "#include <common>\n#include <logdepthbuf_pars_vertex>\nvarying float vL;varying vec2 vU;varying vec3 vN,vV;void main(){vU=uv;vL=position.z;vN=normalMatrix*normal;vec4 mv=modelViewMatrix*vec4(position,1.);vV=mv.xyz;gl_Position=projectionMatrix*mv;\n#include <logdepthbuf_vertex>\n}",
      fragmentShader: `#include <logdepthbuf_pars_fragment>
uniform float time,k;varying float vL;varying vec2 vU;varying vec3 vN,vV;void main(){
#include <logdepthbuf_fragment>
float a=(1.-smoothstep(0.,1.,vL))*smoothstep(0.,.08,vL);float e=smoothstep(0.,.25,vU.x)*smoothstep(1.,.75,vU.x);a*=smoothstep(.12,.85,abs(dot(normalize(vN),normalize(-vV))))*smoothstep(.6,3.,length(vV));gl_FragColor=vec4(vec3(1.,.86,.62)*a*e*.05*k,1.);
        #include <tonemapping_fragment>
        #include <colorspace_fragment>
      }` });
    const shafts = [];
    const sd = sunDir.clone().negate();   // the way the light travels
    const hole = (cx, y, cz, w, h, nx, nz) => {          // a window on a wall facing (nx, nz): the light enters if the sun is on that side
      if (sunDir.x * nx + sunDir.z * nz <= .05) return;
      const len = Math.min(9, (y + h * .5) / Math.max(.15, -sd.y)) * 1.15;
      const g = new THREE.BoxGeometry(w, h, 1, 1, 1, 1); g.translate(0, 0, .5);
      const p = g.attributes.position; for (let i = 0; i < p.count; i++) { const t = p.getZ(i); p.setXYZ(i, p.getX(i), p.getY(i), t); }
      const m = new THREE.Mesh(g, mat);
      const look = new THREE.Matrix4().lookAt(new THREE.Vector3(0, 0, 0), sd.clone().multiplyScalar(-1), new THREE.Vector3(0, 1, 0));
      m.quaternion.setFromRotationMatrix(look); m.scale.set(1, 1, len); m.position.set(cx, y, cz); m.renderOrder = 2; scene.add(m); shafts.push(m);
    };
    for (const o of openingsW) if (o.x < 6 && o.z < -4 && o.y < 6) hole(o.x - o.nx * .3, o.y, o.z - o.nz * .3, o.w * .9, o.h * .85, o.nx, o.nz);
    hole(HB.x0 + .45, 4.9, hz, .7, 1.2, -1, 0); hole(-4.4, 1.9, CB.z1 - .45, .6, .9, 0, 1); hole(-1.6, 1.9, CB.z1 - .45, .6, .9, 0, 1); hole(-4.4, 1.9, CB.z1 - .45, .01, .01, 0, 1);
  }
  const dP = []; for (let i = 0; i < 160; i++) dP.push(hx - 7 + R() * 14, .3 + R() * 4.5, hz - 4 + R() * 8);
  const dust = new THREE.Points(new THREE.BufferGeometry().setAttribute("position", new THREE.Float32BufferAttribute(dP, 3)), new THREE.PointsMaterial({ color: 0xffd9a0, size: .022, transparent: true, opacity: .55, depthWrite: false, blending: THREE.AdditiveBlending }));
  scene.add(dust);

  // ---------- the stops: a gold marker over each, and the panel that tells about it ----------
  const stops = D.stops.filter((s) => STOPS[s.id]);
  const marks = [];
  const markMat = new THREE.MeshStandardMaterial({ color: 0xf2c14e, emissive: 0xc8901a, emissiveIntensity: 1.4, roughness: .3, metalness: .4 });
  stops.forEach((s, i) => {
    const [[x, z], [lx, ly, lz]] = STOPS[s.id], dxx = lx - x, dzz = lz - z, L = Math.hypot(dxx, dzz);
    const m = new THREE.Mesh(new THREE.OctahedronGeometry(.16), markMat);
    const mx = x + dxx / L * 1.8, mz = z + dzz / L * 1.8;
    m.position.set(mx, ground(mx, mz) + 2.05, mz); m.userData.i = i; m.userData.y = m.position.y; scene.add(m); marks.push(m);
  });

  // ---------- the walker ----------
  const me = { x: 70, z: 6, yaw: Math.PI / 2, pitch: 0, vx: 0, vz: 0 }, look = { yaw: me.yaw, pitch: 0 };
  const daisAt = (x, z) => x > HB.ix0 - .1 && x < HB.ix0 + dW && z > HB.iz0 && z < HB.iz1;
  const eye = (x, z) => 1.62 + (daisAt(x, z) ? .32 : 0) + ground(x, z);
  function bump(nx, nz) {
    const r = .32;
    for (let k = 0; k < 2; k++) {
      for (const [x1, z1, x2, z2, ht] of walls) {
        const vx = x2 - x1, vz = z2 - z1, L2 = vx * vx + vz * vz || 1e-6; const t = clamp(((nx - x1) * vx + (nz - z1) * vz) / L2, 0, 1);
        const px = x1 + vx * t, pz = z1 + vz * t, ddx = nx - px, ddz = nz - pz, d = Math.hypot(ddx, ddz), min = r + ht;
        if (d < min && d > 1e-6) { nx = px + ddx / d * min; nz = pz + ddz / d * min; }
      }
      for (const [px, pz, pr] of posts) { const ddx = nx - px, ddz = nz - pz, d = Math.hypot(ddx, ddz), min = r + pr; if (d < min && d > 1e-6) { nx = px + ddx / d * min; nz = pz + ddz / d * min; } }
    }
    const far = Math.hypot(nx, nz); if (far > 260) { nx *= 260 / far; nz *= 260 / far; }
    return [nx, nz];
  }
  const blocked = (x1, z1, x2, z2) => walls.some(([a, b, c, d, ht]) => {   // does a straight line cross a wall?
    const den = (x2 - x1) * (d - b) - (z2 - z1) * (c - a); if (Math.abs(den) < 1e-9) return false;
    const t = ((a - x1) * (d - b) - (b - z1) * (c - a)) / den, u = ((a - x1) * (z2 - z1) - (b - z1) * (x2 - x1)) / den;
    return t > 0 && t < 1 && u >= 0 && u <= 1 && ht > .1;
  });

  // ---------- sound: made in the browser (wind, the sea, the fire, the pencerdd's harp) ----------
  let AC = null, snd = null, soundOn = true;
  function startSound() {
    if (AC) { if (soundOn && AC.state === "suspended") AC.resume(); return; }
    if (!soundOn) return;
    try { AC = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { return; }
    const sr = AC.sampleRate, nb = AC.createBuffer(1, sr * 4, sr), d = nb.getChannelData(0);
    let b0 = 0, b1 = 0, b2 = 0; for (let i = 0; i < d.length; i++) { const w = Math.random() * 2 - 1; b0 = .99765 * b0 + w * .099; b1 = .963 * b1 + w * .2965; b2 = .57 * b2 + w * 1.0527; d[i] = (b0 + b1 + b2 + w * .1848) * .2; }
    const master = AC.createGain(); master.gain.value = .9; master.connect(AC.destination);
    const loop = (f, q, type = "bandpass") => { const s = AC.createBufferSource(); s.buffer = nb; s.loop = true; s.playbackRate.value = .5 + Math.random() * .1; const fl2 = AC.createBiquadFilter(); fl2.type = type; fl2.frequency.value = f; fl2.Q.value = q; const g = AC.createGain(); g.gain.value = 0; s.connect(fl2); fl2.connect(g); g.connect(master); s.start(); return { g, f: fl2 }; };
    const wind = loop(500, .6), sea = loop(260, .4, "lowpass"), rumble = loop(180, .7, "lowpass");
    const talk = [loop(420, 1.4), loop(950, 1.6)];   // the hall's talk: noise shaped by the rise and fall of many voices
    snd = { wind, sea, rumble, master, talk, crackT: 0, harpT: 2, note: 0, talkT: 0, larkT: 3, larkOn: 0, gullT: 4, bleatT: 5, barkT: 6 };
  }
  function crackle(vol) {
    const len = .02 + Math.random() * .05, b = AC.createBuffer(1, Math.ceil(AC.sampleRate * len), AC.sampleRate), d = b.getChannelData(0);
    for (let i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / d.length, 3);
    const s = AC.createBufferSource(); s.buffer = b; const f = AC.createBiquadFilter(); f.type = "highpass"; f.frequency.value = 900 + Math.random() * 2500; const g = AC.createGain(); g.gain.value = vol * (.2 + Math.random() * .5);
    s.connect(f); f.connect(g); g.connect(snd.master); s.start();
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
  const SCALE = [146.83, 164.81, 174.61, 196, 220, 246.94, 261.63, 293.66, 329.63, 349.23, 392];   // D, in the Dorian mode
  const TUNE = [7, 5, 4, 5, 7, 7, 8, 7, 5, 4, 2, 4, 5, 4, 2, 0, 2, 4, 5, 7, 5, 4, 2, 4];
  function pluck(freq, vol) {   // a plucked string (Karplus and Strong)
    const sr = AC.sampleRate, n = Math.round(sr / freq), len = Math.ceil(sr * 2.6), b = AC.createBuffer(1, len, sr), d = b.getChannelData(0), ring = new Float32Array(n);
    for (let i = 0; i < n; i++) ring[i] = Math.random() * 2 - 1;
    let p = 0; for (let i = 0; i < len; i++) { const nxt = (p + 1) % n; const v = (ring[p] + ring[nxt]) * .4985; d[i] = ring[p]; ring[p] = v; p = nxt; }
    const s = AC.createBufferSource(); s.buffer = b; const g = AC.createGain(); g.gain.value = vol; const f = AC.createBiquadFilter(); f.type = "lowpass"; f.frequency.value = 2600;
    s.connect(f); f.connect(g); g.connect(snd.master); s.start();
  }
  function sound(dt) {
    if (!AC || !snd) return;
    const t = AC.currentTime, ind = indoor;
    const dFire = Math.hypot(me.x - hx, me.z - hz), dK = Math.hypot(me.x - kfx, me.z - kfz);
    const fireV = Math.max(inHall ? clamp(1.4 - dFire / 9, 0, 1) : 0, clamp(1 - dK / 7, 0, 1) * (inKitchen ? 1 : .3));
    snd.wind.g.gain.setTargetAtTime((1 - ind * .8) * (.32 + .18 * Math.sin(t * .23) + .1 * Math.sin(t * .71)), t, .4);
    snd.wind.f.frequency.setTargetAtTime(380 + 160 * Math.sin(t * .17), t, .5);
    snd.sea.g.gain.setTargetAtTime((1 - ind * .7) * (.25 + .15 * Math.sin(t * .45)), t, .5);
    snd.rumble.g.gain.setTargetAtTime(fireV * .7, t, .3);
    snd.crackT -= dt; if (snd.crackT < 0 && fireV > .02) { crackle(fireV); snd.crackT = Math.random() * .22; }
    // the talk of the household at the tables, rising and falling
    snd.talkT -= dt; if (snd.talkT < 0) { snd.talkT = .1 + Math.random() * .16; const tv = inHall ? .3 : 0; snd.talk[0].g.gain.setTargetAtTime(tv * (.25 + Math.random() * .75), t, .05); snd.talk[1].g.gain.setTargetAtTime(tv * .45 * Math.random(), t, .04); }
    // out of doors: a skylark singing high over the fields, gulls, the sheep and the hounds
    const out = 1 - ind;
    if (out > .3) {
      snd.larkT -= dt;
      if (snd.larkT < 0) { if (snd.larkOn <= 0) { snd.larkOn = 1.5 + Math.random() * 3; } snd.larkOn -= dt; tone("sine", 2600 + Math.random() * 2600, 2600 + Math.random() * 3200, .05 + Math.random() * .06, .022 * out, 0, .7); snd.larkT = snd.larkOn > 0 ? .05 + Math.random() * .09 : 2.5 + Math.random() * 5; }
      snd.gullT -= dt; if (snd.gullT < 0) { const n = 1 + (Math.random() * 3 | 0); for (let i = 0; i < n; i++) setTimeout(() => AC && tone("sawtooth", 760, 1250, .32, .028 * out, 1500, 3), i * 380); snd.gullT = 7 + Math.random() * 12; }
      const dS = Math.hypot(me.x + 82, me.z - 58); snd.bleatT -= dt;
      if (snd.bleatT < 0) { const v = clamp(1.3 - dS / 90, 0, 1) * out; if (v > .02) tone("sawtooth", 290 + Math.random() * 60, 250 + Math.random() * 40, .7, .05 * v, 1000, 2.5, 18); snd.bleatT = 4 + Math.random() * 9; }
    }
    const dD = Math.hypot(me.x - 33, me.z - 20); snd.barkT -= dt;
    if (snd.barkT < 0) { const v = clamp(1.2 - dD / 60, 0, 1) * (1 - ind * .7); if (v > .03) { const n = 1 + (Math.random() * 3 | 0); for (let i = 0; i < n; i++) setTimeout(() => AC && tone("square", 420, 240, .16, .045 * v, 700, 1.5), i * 260); } snd.barkT = 8 + Math.random() * 16; }
    if (inHall) { snd.harpT -= dt; if (snd.harpT < 0) { const n = TUNE[snd.note++ % TUNE.length]; const v = clamp(1.2 - Math.hypot(me.x + 17.3, me.z + 13.6) / 12, .15, 1) * .5; pluck(SCALE[n], v); if (snd.note % 4 === 1) pluck(SCALE[Math.max(0, n - 4)] / 2, v * .55); snd.harpT = (snd.note % 8 === 0 ? 1.1 : .52) * (1 + (Math.random() - .5) * .08); } }
  }

  // ---------- the controls, the panel and the plan ----------
  const ui = document.createElement("div"); ui.className = "ll-ui";
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  ui.innerHTML = '<div class="ll-panel" hidden><p class="ll-n"></p><h2 tabindex="-1"></h2><div class="ll-txt"></div><p class="ll-src"></p><div class="ll-btns">' +
    '<button type="button" class="btn" data-k="prev">← ' + esc(T(D.ui.prev)) + '</button><button type="button" class="btn solid" data-k="next">' + esc(T(D.ui.next)) + ' →</button>' +
    '<button type="button" class="ll-x" data-k="close" aria-label="' + esc(T(D.ui.close)) + '">×</button></div></div>' +
    '<div class="ll-bar"><button type="button" class="btn solid" data-k="tour">' + esc(T(D.ui.tour)) + ' →</button>' +
    '<button type="button" class="btn" data-k="snd" aria-pressed="' + soundOn + '"></button>' +
    '<button type="button" class="btn" data-k="fs">' + esc(T(D.ui.fs)) + '</button><span class="ll-help">' + esc(T(coarse ? D.ui.helpTouch : D.ui.help)) + "</span></div>" +
    '<canvas class="ll-plan" width="200" height="160" aria-hidden="true"></canvas>' +
    '<div class="ll-stick" aria-hidden="true"><i></i></div><div class="ll-fade"></div>';
  host.appendChild(ui);
  const panel = ui.querySelector(".ll-panel"), stick = ui.querySelector(".ll-stick"), knob = stick.querySelector("i"), fade = ui.querySelector(".ll-fade"), sndB = ui.querySelector('[data-k="snd"]');
  const setSndLabel = () => { sndB.textContent = (soundOn ? "♪ " : "") + T(soundOn ? D.ui.soundOff : D.ui.soundOn); sndB.setAttribute("aria-pressed", soundOn); };
  setSndLabel();
  let cur = -1, dismissed = -1, fly = null;

  function showStop(i) {
    cur = i; const s = stops[i];
    panel.hidden = false; panel.scrollTop = 0;
    panel.querySelector(".ll-n").textContent = T(D.ui.stop).replace("{n}", i + 1).replace("{of}", stops.length);
    panel.querySelector("h2").textContent = T(s.t);
    panel.querySelector(".ll-txt").innerHTML = T(s.p).map((p) => "<p>" + esc(p) + "</p>").join("");
    const src = panel.querySelector(".ll-src");
    src.innerHTML = s.src && s.src.length ? esc(T(D.ui.sources)) + ": " + s.src.map((r) => (r.url ? `<a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(T(r.t))}</a>` : esc(T(r.t)))).join(" · ") : "";
    panel.querySelector('[data-k="prev"]').disabled = i === 0;
    panel.querySelector('[data-k="next"]').textContent = (i === stops.length - 1 ? T(D.ui.again) : T(D.ui.next)) + " →";
  }
  let snapF = false;
  function goStop(i, instant) {
    me.fov = 0;
    i = (i + stops.length) % stops.length;
    const [[x, z], [lx, ly, lz]] = STOPS[stops[i].id];
    const yaw = Math.atan2(-(lx - x), -(lz - z)), pitch = Math.atan2(ly - eye(x, z), Math.hypot(lx - x, lz - z));
    let dy = yaw - me.yaw; while (dy > Math.PI) dy -= 2 * Math.PI; while (dy < -Math.PI) dy += 2 * Math.PI;
    const jump = instant || reduce || blocked(me.x, me.z, x, z) || Math.hypot(x - me.x, z - me.z) > 90;
    fly = { t: 0, dur: jump ? .9 : Math.min(3.4, 1 + Math.hypot(x - me.x, z - me.z) / 12), jump, from: { ...me }, to: { x, z, yaw: me.yaw + dy, pitch } };
    if (instant) { Object.assign(me, fly.to); look.yaw = me.yaw; look.pitch = me.pitch; fly = null; snapF = true; }
    showStop(i); dismissed = -1;
  }
  ui.addEventListener("click", (e) => {
    const b = e.target.closest("button"); if (!b) return;
    const k = b.dataset.k;
    if (k === "tour" || k === "next") goStop(cur + 1);
    else if (k === "prev") goStop(cur - 1);
    else if (k === "close") { panel.hidden = true; dismissed = cur; canvas.focus({ preventScroll: true }); }
    else if (k === "snd") { soundOn = !soundOn; setSndLabel(); if (soundOn) { if (!AC) startSound(); else AC.resume(); } else if (AC) AC.suspend(); }
    else if (k === "fs") { const fs = document.fullscreenElement; if (fs) document.exitFullscreen(); else if (host.requestFullscreen) host.requestFullscreen().catch(() => {}); }
  });
  // the plan of the court, with you on it (top right)
  const plan = ui.querySelector(".ll-plan"), px = plan.getContext("2d");
  const PS = 1.85, P = (x, z) => [100 + x * PS, 80 + z * PS * 1.0];
  function drawPlan() {
    px.clearRect(0, 0, 200, 160);
    px.fillStyle = "rgba(8,10,16,.62)"; px.fillRect(0, 0, 200, 160);
    px.strokeStyle = "rgba(230,220,200,.75)"; px.lineWidth = 2.2; px.beginPath(); C.forEach(([x, z], i) => { const [a, b] = P(x, z); i ? px.lineTo(a, b) : px.moveTo(a, b); }); px.closePath(); px.stroke();
    px.fillStyle = "rgba(230,220,200,.45)"; for (const r of roofs) { if (r[2] - r[0] > 40) continue; const [a, b] = P(r[0], r[1]), [c, d] = P(r[2], r[3]); px.fillRect(a, b, c - a, d - b); }
    stops.forEach((s, i) => { const [[x, z]] = STOPS[s.id]; if (Math.abs(x) > 50 || Math.abs(z) > 40) return; const [a, b] = P(x, z); px.fillStyle = i === cur ? "#fff" : "#f2c14e"; px.beginPath(); px.arc(a, b, 3.2, 0, 7); px.fill(); });
    const [a, b] = P(clamp(me.x, -52, 52), clamp(me.z, -42, 42)); px.save(); px.translate(a, b); px.rotate(-me.yaw); px.fillStyle = "#e8483f"; px.beginPath(); px.moveTo(0, -7); px.lineTo(5, 5); px.lineTo(0, 2); px.lineTo(-5, 5); px.closePath(); px.fill(); px.restore();
    px.fillStyle = "rgba(230,220,200,.85)"; px.font = "600 10px system-ui, sans-serif"; px.fillText(cy ? "G" : "N", 188, 14); px.beginPath(); px.moveTo(191, 18); px.lineTo(191, 30); px.strokeStyle = "rgba(230,220,200,.85)"; px.lineWidth = 1.2; px.stroke();
  }
  plan.addEventListener("click", (e) => {
    const r = plan.getBoundingClientRect(), x = (e.clientX - r.left) / r.width * 200, y = (e.clientY - r.top) / r.height * 160;
    let best = -1, bd = 14; stops.forEach((s, i) => { const [[sx, sz]] = STOPS[s.id]; const [a, b] = P(sx, sz); const d = Math.hypot(a - x, b - y); if (d < bd) { bd = d; best = i; } });
    if (best >= 0) goStop(best);
  });

  const keys = {};
  canvas.addEventListener("keydown", (e) => {
    const k = e.key.toLowerCase();
    if (["w", "a", "s", "d", "arrowup", "arrowdown", "arrowleft", "arrowright", "q", "e", "shift"].includes(k)) { keys[k] = 1; e.preventDefault(); fly = null; }
    if (k === "n") goStop(cur + 1);
    startSound();
  });
  canvas.addEventListener("keyup", (e) => { keys[e.key.toLowerCase()] = 0; });
  canvas.addEventListener("blur", () => { for (const k in keys) keys[k] = 0; });

  // look by dragging (smoothed); tap a gold marker to go to it
  let drag = null;
  const ray = new THREE.Raycaster(), ndc = new THREE.Vector2();
  canvas.addEventListener("pointerdown", (e) => { drag = { id: e.pointerId, x: e.clientX, y: e.clientY, moved: 0 }; canvas.setPointerCapture(e.pointerId); canvas.focus({ preventScroll: true }); startSound(); });
  canvas.addEventListener("pointermove", (e) => {
    if (!drag || drag.id !== e.pointerId) return;
    const ddx = e.clientX - drag.x, ddy = e.clientY - drag.y; drag.x = e.clientX; drag.y = e.clientY; drag.moved += Math.abs(ddx) + Math.abs(ddy);
    const k = e.pointerType === "touch" ? .0062 : .0045;
    if (fly) { look.yaw = me.yaw; look.pitch = me.pitch; fly = null; }
    look.yaw += ddx * k; look.pitch = clamp(look.pitch + ddy * k, -1.25, 1.25);
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
  stick.addEventListener("pointerdown", (e) => { sid = e.pointerId; stick.setPointerCapture(sid); stickAt(e); if (fly) { look.yaw = me.yaw; look.pitch = me.pitch; fly = null; } e.preventDefault(); startSound(); });
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
  let last = performance.now(), time = 0, indoor = 0, inHall = false, inKitchen = false, slowT = 0, fastT = 0, bob = 0;
  const camPos = new THREE.Vector3(), shadowAt = new THREE.Vector3();
  function frame(now) {
    requestAnimationFrame(frame);
    if (!visible || document.hidden) return;
    const raw = Math.min(.5, (now - last) / 1000), dt = Math.min(.05, raw); last = now; time += dt;
    // keep it smooth: lower the resolution if frames are slow, raise it again when there is room
    {
      if (raw > .034) { slowT += raw; fastT = 0; } else if (raw < .019) { fastT += raw; slowT = 0; }
      if (slowT > 1.2 && dpr > .6) { dpr = Math.max(.6, dpr - .15); renderer.setPixelRatio(dpr); size(); slowT = 0; }
      if (fastT > 4 && dpr < maxDpr) { dpr = Math.min(maxDpr, dpr + .1); renderer.setPixelRatio(dpr); size(); fastT = 0; }
    }
    let moving = 0;
    if (fly) {
      fly.t += raw / fly.dur; const k = fly.t >= 1 ? 1 : (1 - Math.cos(Math.PI * fly.t)) / 2;
      if (fly.jump) {                                 // through a wall: fade out, move, fade in
        fade.style.opacity = String(Math.sin(Math.min(1, fly.t) * Math.PI));
        if (fly.t >= .5 && !fly.done) { Object.assign(me, fly.to); fly.done = true; camera.position.y = eye(me.x, me.z); }
      } else ["x", "z", "yaw", "pitch"].forEach((p) => { me[p] = fly.from[p] + (fly.to[p] - fly.from[p]) * k; });
      if (fly.t >= 1) { Object.assign(me, fly.to); fly = null; fade.style.opacity = "0"; }
      look.yaw = me.yaw; look.pitch = me.pitch; me.vx = me.vz = 0;
    } else {
      // turn smoothly toward where the visitor is looking
      const kk = 1 - Math.exp(-dt * 16);
      me.yaw += (look.yaw - me.yaw) * kk; me.pitch += (look.pitch - me.pitch) * kk;
      if (keys.arrowleft || keys.q) { look.yaw += 1.8 * dt; }
      if (keys.arrowright || keys.e) { look.yaw -= 1.8 * dt; }
      const run = keys.shift ? 2.1 : 1;
      let f = (keys.w || keys.arrowup ? 1 : 0) - (keys.s || keys.arrowdown ? 1 : 0) - mv.y;
      let s = (keys.d ? 1 : 0) - (keys.a ? 1 : 0) + mv.x;
      const l = Math.max(1, Math.hypot(f, s)); f /= l; s /= l;
      const tx = (-Math.sin(me.yaw) * f + Math.cos(me.yaw) * s) * 3.3 * run, tz = (-Math.cos(me.yaw) * f - Math.sin(me.yaw) * s) * 3.3 * run;
      const a = 1 - Math.exp(-dt * 9); me.vx += (tx - me.vx) * a; me.vz += (tz - me.vz) * a;
      const sp = Math.hypot(me.vx, me.vz);
      if (sp > .02) { [me.x, me.z] = bump(me.x + me.vx * dt, me.z + me.vz * dt); moving = Math.min(1, sp / 3.3); }
      // walking up to a stop opens its panel
      stops.forEach((st, i) => { const [[x, z]] = STOPS[st.id]; if (i !== cur && i !== dismissed && Math.hypot(me.x - x, me.z - z) < 1.8) showStop(i); });
    }
    bob += dt * 9 * moving;
    const ey = me.hy != null ? me.hy : eye(me.x, me.z) + (reduce ? 0 : Math.sin(bob) * .025 * moving);
    camera.position.set(me.x, camera.position.y ? camera.position.y + (ey - camera.position.y) * Math.min(1, dt * 10) : ey, me.z);
    camera.rotation.set(me.pitch, me.yaw, 0);
    // narrow the view a little when looking at the far mountains (as the eye does)
    const wantFov = me.fov || (small ? 68 : 60) - (cur >= 0 && (stops[cur].id === "wall" || stops[cur].id === "sands") && !fly ? (small ? 38 : 42) : 0);
    if (snapF) { camera.fov = wantFov; camera.updateProjectionMatrix(); snapF = false; }
    if (Math.abs(camera.fov - wantFov) > .05) { camera.fov += (wantFov - camera.fov) * Math.min(1, dt * 2.5); camera.updateProjectionMatrix(); }

    // indoors or out: inside, the eye opens up to the firelight; outside, the sky does the lighting
    const rr = inside(me.x, me.z, -.3);
    inHall = inKitchen = false;
    if (rr) { inHall = me.x > HB.x0 && me.x < HB.x1 && me.z > HB.z0 && me.z < HB.z1; inKitchen = me.x > KB.x0 && me.x < KB.x1 && me.z > KB.z0 && me.z < KB.z1; }
    indoor += ((rr ? 1 : 0) - indoor) * Math.min(1, dt * 2.2);
    renderer.toneMappingExposure = .62 + indoor * .38;
    const env = 1 - indoor * .82;
    for (const m of mats) m.envMapIntensity = env;
    hemi.intensity = .15 * env;
    smokeU.light.value = .35 + (1 - indoor) * .65;
    shaftU.k.value = .25 + indoor * .45;
    // the sun's shadow follows you, kept to whole shadow pixels so its edges do not swim
    camPos.set(me.x, 0, me.z);
    const texel = 76 / Q.shadow;
    shadowAt.set(Math.round(camPos.x / texel) * texel, 0, Math.round(camPos.z / texel) * texel);
    sun.target.position.copy(shadowAt); sun.position.copy(shadowAt).addScaledVector(sunDir, 120); sun.target.updateMatrixWorld();
    // flicker the fires, turn the markers, move the water and clouds
    const flk = 1 + Math.sin(time * 11) * .07 + Math.sin(time * 23.7) * .05 + (Math.random() - .5) * .09;
    fire.intensity = 60 * flk; kfire.intensity = 22 * flk; torchL.intensity = 6 * (1 + Math.sin(time * 13) * .08); brazier.intensity = 9 * (1 + Math.sin(time * 9.3) * .07);
    fire.position.x = hx + Math.sin(time * 7) * .05; fire.position.z = hz + Math.cos(time * 9) * .05;
    emberMat.color.setRGB(1, .3 + Math.sin(time * 3) * .04, .08);
    fireU.time.value = time; smokeU.time.value = time; seaU.time.value = time; cloudU.time.value = time; windU.time.value = time; shaftU.time.value = time; cloudT.value = time; moveGulls(time);
    dust.rotation.y = Math.sin(time * .05) * .02; dust.position.y = Math.sin(time * .3) * .05;
    marks.forEach((m, i) => { m.rotation.y = time * 1.4 + i; m.position.y = m.userData.y + Math.sin(time * 2 + i) * .06; m.visible = i !== cur || !!fly; });
    sound(dt);
    if ((time * 10 | 0) % 2 === 0) drawPlan();
    renderer.render(scene, camera);
  }
  host.classList.add("ready");
  camera.position.y = 0;
  canvas.focus({ preventScroll: true });
  if (soundOn) startSound();
  const api = { dem, ground, goStop: (i, inst) => goStop(i, inst), renderer, me, view: (x, y, z, lx, ly, lz, fov) => { panel.hidden = true; me.fov = fov || 0; snapF = true; fly = null; me.x = x; me.z = z; me.hy = y; camera.position.y = y; me.yaw = look.yaw = Math.atan2(-(lx - x), -(lz - z)); me.pitch = look.pitch = Math.atan2(ly - y, Math.hypot(lx - x, lz - z)); } };
  requestAnimationFrame(frame); setTimeout(() => goStop(0), 300);
  window.LLYS3D = api;
  return api;
}
