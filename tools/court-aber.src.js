/* Abergwyngregyn: the court of the princes of Gwynedd at Aber, which they called Garth Celyn, as it might have looked
   around 1280, in the time of Llywelyn ap Gruffudd. Built on the shared court engine (tools/court3d.src.js); the words
   for each stop are in src/courts.py.
     npx esbuild court-aber.src.js --bundle --minify --format=esm --target=es2019 --outfile=court-aber.js
   What it rests on (see the page's "How we know"):
     - the hall found by excavation in 1993 (Johnstone) and dug again in 2010-11 (Snowdonia National Park, Gwynedd
       Archaeological Trust): a hall with a cross-wing at each end, 11.2 m by 8.0 m inside, with 13th- and
       14th-century pottery and a brooch, at SH 65682 72635 (Coflein NPRN 309171);
     - the mound Pen y Mwd at SH 65642 72662 (Coflein NPRN 95692): about 36 m across and 6.6 m high, its level top
       about 17 m by 14 m, with traces of a ditch on the south side; the hall lies at its foot to the south-east;
     - Pen y Bryn, at SH 65827 72730, on the rising ground across the Afon Aber, within a double bank and ditch
       90-100 m across (Coflein NPRN 32, Cadw), which the Garth Celyn Trust holds to be the court itself;
     - the land: real heights round Aber (tools/bake_court.py), the sea and the Lafan Sands to the north, Ynys Môn
       across the water, and the Carneddau to the south.
   Which way the hall ran, how high its walls stood, its roofs, the yard, the kitchen, the fence and the tower on
   the mound are imagined. x is east and z is south, in metres, with the middle of the hall at 0, 0. */
import { run, landHeights, smooth } from "./court3d.src.js";
import { LAND } from "./court-aber-land.js";

const STOPS = {
  arrive: [[-58, 62], [2, 6, 0]],
  hall: [[-3, 24], [0, 4.2, 0]],
  mound: [[-27, -2], [-40, 8.5, -27]],
  siwan: [[-43.4, -28.4], [-1380, 14, -1500], 40],
  dafydd: [[-15.5, 16], [-9, 6, 0]],
  inside: [[4.6, 2.2], [-5.6, 1.6, -.4]],
  eleanor: [[-8.6, .6], [-10, .7, -4.4]],
  letters: [[-.6, -1.9], [-4.4, .9, -1.1]],
  garthcelyn: [[104, -18], [129, 9, -104], 50],
  bera: [[60, 62], [520, 160, 900], 44],
  spade: [[-12, 20], [-26, 3, -16]],
};
const START = { x: -70, z: 76, yaw: -Math.PI * .3 };

// ---------- the land ----------
const B = landHeights(LAND);
const ABS0 = 34.7;              // the land at the middle of the hall is 34.7 m above the sea (the baked survey)
const SEA = 1 - ABS0;           // the sea, at a middling tide, 1 m above datum
// the court stands on level ground in the valley floor
const level = (x, z) => B(x, z) * smooth(40, 95, Math.hypot(x + 8, z));

// the Afon Aber, coming down from the falls and the mountains to the south-east, past the court to the sea
const RIVER = [[18, -1150], [30, -700], [45, -400], [60, -150], [68, 0], [78, 110], [150, 175], [240, 240], [360, 360], [480, 470], [600, 600], [720, 840], [720, 1250]];
function riverAt(z) {
  for (let i = 0; i < RIVER.length - 1; i++) { const [x1, z1] = RIVER[i], [x2, z2] = RIVER[i + 1]; if (z >= z1 && z <= z2) { const t = (z - z1) / (z2 - z1); return x1 + (x2 - x1) * t; } }
  return RIVER[z < 0 ? 0 : RIVER.length - 1][0];
}
// the shore: north of this line is the sea and the Lafan Sands
const coast = (x) => -980 + (x < -600 ? (-600 - x) * .6 : 0) + Math.sin(x * .004) * 30;

// the mound, Pen y Mwd
const MD = { x: -40, z: -27 }, M_H = 6.6, M_FOOT = 18;
const mTop = (a) => 1 / Math.sqrt((Math.cos(a) / 8.5) ** 2 + (Math.sin(a) / 7) ** 2);   // the level top, 17 m by 14 m
// Pen y Bryn, on the hill across the river
const PB = { x: 129, z: -104 };
const TW = { x: MD.x - 3, z: MD.z - 1, up: 4.6 };   // the look-out on the mound, with its platform 4.6 m up
const BRIDGE = { z: 46, w: 1.5 };

function shape(x, z) {
  let h = level(x, z);
  // the sea and the sands
  const c = coast(x) - z;
  if (c > 0) h = h * (1 - smooth(0, 70, c)) + (SEA - 1.2 - Math.min(6, c * .01)) * smooth(0, 70, c);
  // the river in its bed
  const rw = Math.abs(x - riverAt(z));
  h -= 2.2 * (1 - smooth(4, 9, rw));
  // the mound and the ditch on its south side
  const dx = x - MD.x, dz = z - MD.z, r = Math.hypot(dx, dz), a = Math.atan2(dz, dx), tr = mTop(a);
  const base0 = level(MD.x, MD.z);
  if (r < M_FOOT + 1) h = Math.max(h, base0 + M_H * Math.pow(1 - smooth(tr, M_FOOT + 1, r), 1.1));
  if (dz > 0 && r > M_FOOT && r < M_FOOT + 7) { const k = Math.sin(Math.PI * (r - M_FOOT) / 7) * smooth(.15, .6, Math.sin(a)); h -= 1.4 * k; }
  // the double bank and ditch round Pen y Bryn
  const pr = Math.hypot(x - PB.x, z - PB.z);
  h += 2.0 * Math.exp(-(((pr - 40) / 2.6) ** 2)) - 1.4 * Math.exp(-(((pr - 44.5) / 2) ** 2)) + 1.7 * Math.exp(-(((pr - 49) / 2.6) ** 2));
  return h;
}
const LANES = [
  [[-700, 130], [-400, 100], [-160, 72], [-60, 58], [-10, 54], [40, 50], [riverAt(46) - 9, 46]],   // the old road along the coast, from Bangor
  [[riverAt(46) + 9, 46], [110, 42], [200, 30], [420, 0], [700, -60]],                             // on to Conwy
  [[-62, 57], [-80, -60], [-95, -300], [-110, -700], [-125, -990]],                                // down to the shore and the crossing to Môn
  [[riverAt(46) + 9, 46], [105, -20], [124, -62]],                                                  // up to Pen y Bryn
  [[2, 54], [3, 44]],                                                                                // into the court
];
function laneDist(x, z) {
  let best = 1e9;
  LANES.forEach((L) => { for (let i = 0; i < L.length - 1; i++) {
    const [x1, z1] = L[i], [x2, z2] = L[i + 1], vx = x2 - x1, vz = z2 - z1, t = Math.max(0, Math.min(1, ((x - x1) * vx + (z - z1) * vz) / (vx * vx + vz * vz)));
    best = Math.min(best, Math.hypot(x - x1 - vx * t, z - z1 - vz * t));
  } });
  return best;
}
// the timber bridge over the Afon Aber, where the road crosses
function onBridge(x, z) {
  if (Math.abs(z - BRIDGE.z) > BRIDGE.w) return null;
  const rx = riverAt(BRIDGE.z), x1 = rx - 9, x2 = rx + 9;
  if (x < x1 || x > x2) return null;
  const y1 = shape(x1, BRIDGE.z), y2 = shape(x2, BRIDGE.z), t = (x - x1) / (x2 - x1);
  return y1 + (y2 - y1) * t + .15 + Math.sin(Math.PI * t) * .5;
}
// the hall: 11.2 m by 8 m inside, with a cross-wing at each end
const HALL = { x: 5.6, z: 4, t: .9 }, WING = { x0: 5.6, x1: 12.4, z: 6.9 };
function floor(x, z, ground) {
  const b = onBridge(x, z); if (b !== null) return b;
  let y = ground(x, z);
  if (x > -HALL.x && x < -HALL.x + 2 && Math.abs(z) < HALL.z) y += .3;   // the dais at the upper end
  // the look-out: its platform, and the stair up its east side
  const mt = level(MD.x, MD.z) + M_H;
  if (Math.abs(x - TW.x) < 1.8 && Math.abs(z - TW.z) < 1.8) return mt + TW.up + .1;
  if (x > TW.x + 1.65 && x < TW.x + 2.55 && z > TW.z - 1.8 && z < TW.z + 1.9) return mt + TW.up * Math.min(1, Math.max(0, (TW.z + 1.6 - z) / 3.2));
  return y;
}
function blocked(x, z) {
  if (onBridge(x, z) !== null) return false;
  if (Math.abs(x - riverAt(z)) < 4) return true;
  return shape(x, z) < SEA + .1;
}
function colour(x, z, y, c) {
  const C = c.constructor;
  // the sands and the shore
  if (y < SEA + 2.6) c.lerp(new C(0xc4b48a), y < SEA + .4 ? .9 : .6);
  else if (coast(x) - z > -60) c.lerp(new C(0x8f9a5a), .35);
  // the lanes, worn earth
  const lane = laneDist(x, z);
  if (lane < 2.6) c.lerp(new C(0x8a7656), .75 * (1 - lane / 2.6));
  // the court yard, trodden
  if (x > -24 && x < 40 && z > -12 && z < 46 && !(Math.abs(x) < 13 && Math.abs(z) < 7.5)) c.lerp(new C(0x8c7a5c), .35);
  // ploughed strips of the township's open field to the west, and hay by the river
  if (x < -130 && x > -700 && z > -500 && z < 300) { const rf = (Math.sin(x * .8 + z * .1) + 1) / 2; c.lerp(new C(0x8b8f45), .2 + rf * .15); }
  // the hills: bracken and heather above the fields
  if (y > 45) c.lerp(new C(0x7a6a3c), Math.min(.6, (y - 45) / 120));
}

// ---------- the buildings ----------
function build(K) {
  const { THREE, scene, M, R, block, cyl, wallLine, wallSeg, roof, trees, fire, smoke, posts, anim, ground } = K;
  const G = (x, z) => ground(x, z);
  const g0 = G(0, 0);

  // ----- the hall: stone walls, limewashed, a hall with a cross-wing at each end -----
  const T = HALL.t, hx = HALL.x + T / 2, hz = HALL.z + T / 2, H = 4.2;
  wallLine(-hx, hz, hx, hz, H, T, M.lime, [[hx + 4.3, 1.4]], g0, 2.4);     // south wall: the door of the cross-passage
  wallLine(-hx, -hz, hx, -hz, H, T, M.lime, [[hx + 4.3, 1.4]], g0, 2.4);                 // north wall: the other door of the passage
  // windows: small, with oak shutters
  [[-1.6, hz], [-1.6, -hz], [2, -hz]].forEach(([x, z]) => { block(.9, 1.1, T + .06, M.darkwood, x, g0 + 2.6, z); });
  // the two wings, two storeys, gable ends to north and south
  [-1, 1].forEach((s) => {
    const xi = s * (WING.x0 + T / 2), xo = s * (WING.x1 - T / 2), zz = WING.z - T / 2, WH = 6.2, cx = s * (WING.x0 + WING.x1) / 2;
    // the inner wall onto the hall: at the upper end one door into the chamber, at the lower end two, to the buttery and the pantry
    wallLine(xi, -zz, xi, zz, WH, T, M.lime, s < 0 ? [[zz - 2.4, 1.1]] : [[zz - 1.6, 1.0], [zz + 1.6, 1.0]], g0, 2.2);
    wallLine(xo, -zz, xo, zz, WH, T, M.lime, s < 0 ? [] : [[zz, 1.3]], g0, 2.3);
    wallLine(xi, -zz, xo, -zz, WH, T, M.lime, [], g0);
    wallLine(xi, zz, xo, zz, WH, T, M.lime, s < 0 ? [[Math.abs(xo - xi) / 2, 1.2]] : [], g0, 2.2);
    // the upper floor: the chamber above
    block(Math.abs(xo - xi) - T, .22, 2 * zz - T, M.boards, cx, g0 + 3.1, 0);
    roof(cx, 0, 2 * WING.z, WING.x1 - WING.x0, g0 + WH, 3.8, M.slate, Math.PI / 2, .45, M.lime, T);
    // windows in the gables and the outer wall, upper and lower
    [[cx, -WING.z - .03, 0], [cx, WING.z + .03, 0]].forEach(([x, z]) => { block(.8, 1.0, .1, M.darkwood, x, g0 + 4.6, z); });
    [-3, 3].forEach((o) => block(.1, 1.0, .8, M.darkwood, s * (WING.x1 + .03), g0 + 4.4, o));
    block(.1, .9, .7, M.darkwood, s * (WING.x1 + .03), g0 + 1.8, s < 0 ? -2 : 3);
  });
  // the hall roof, between the wings, with a louvre over the hearth for the smoke
  roof(0, 0, 2 * HALL.x + T, 2 * hz + T, g0 + H, 4.4, M.slate, 0, .55);
  block(1.4, 1.0, 1.4, M.wood, 0, g0 + H + 4.75, 0); roof(0, 0, 1.6, 1.6, g0 + H + 5.2, .7, M.slate, 0, .2);
  // trusses you can see from below
  const half = hz, ang = Math.atan2(4.4, half), len = Math.hypot(half, 4.4);
  [-2.8, 0, 2.8].forEach((x) => {
    [-1, 1].forEach((s) => { const rf = block(.24, .28, len, M.oak, x, g0 + H + 2.2 - .1, s * half / 2); rf.rotation.set(s * ang, 0, 0); });
    block(.24, .26, 3.2, M.oak, x, g0 + H + 2.6, 0);
  });
  // the hearth in the middle of the floor, ringed with stones
  const fl = new THREE.Mesh(new THREE.PlaneGeometry(2 * HALL.x, 2 * HALL.z), M.floor); fl.rotation.x = -Math.PI / 2; fl.position.set(0, g0 + .02, 0); fl.receiveShadow = true; scene.add(fl);
  for (let i = 0; i < 12; i++) { const a = i / 12 * Math.PI * 2; block(.36, .18, .3, M.stone, Math.cos(a) * 1.0, g0 + .09, Math.sin(a) * .8, -a); }
  fire(0, g0, 0, 1, 32, 14, true);
  smoke(0, g0 + H + 5.4, 0, 7);
  posts.push([0, 0, 1.0]);
  // the dais at the upper (west) end, the prince's table and chair, a hanging on the wall behind
  block(2, .3, 2 * HALL.z, M.boards, -HALL.x + 1, g0 + .15, 0);
  block(.85, .08, 4.4, M.wood, -HALL.x + 1.35, g0 + 1.1, 0); [-1.8, 1.8].forEach((o) => block(.07, .78, .07, M.oak, -HALL.x + 1.35, g0 + .7, o));
  block(.9, .5, .75, M.oak, -HALL.x + .55, g0 + .55, 0); block(.12, 1.7, .85, M.oak, -HALL.x + .2, g0 + 1.15, 0); block(.4, .5, .7, M.red, -HALL.x + .6, g0 + .85, 0);
  const hang = new THREE.Mesh(new THREE.PlaneGeometry(4.6, 2.3), M.green); hang.rotation.y = Math.PI / 2; hang.position.set(-HALL.x + .03, g0 + 2.4, 0); scene.add(hang);
  { // the three lions of Gwynedd on the hanging: gold on red, quartered
    const q = (cz, cy2, col) => { const p = new THREE.Mesh(new THREE.PlaneGeometry(1.1, 1.0), col); p.rotation.y = Math.PI / 2; p.position.set(-HALL.x + .05, cy2, cz); scene.add(p); };
    q(-.6, g0 + 2.9, M.red); q(.6, g0 + 1.9, M.red); q(.6, g0 + 2.9, M.gold); q(-.6, g0 + 1.9, M.gold);
  }
  // the letters on the prince's table: parchment, ink and the seal
  const parch = new THREE.MeshStandardMaterial({ color: 0xe9dcb8, roughness: .9 });
  [[-1.4, .1], [-1.0, -.25], [-.45, .15]].forEach(([o, r2]) => { const p = block(.42, .01, .32, parch, -HALL.x + 1.38, g0 + 1.15, o, r2); p.castShadow = false; });
  const seal = cyl(.07, .07, .03, M.red, -HALL.x + 1.25, g0 + 1.17, -1.0, 14); seal.castShadow = false;
  cyl(.04, .05, .14, M.darkwood, -HALL.x + 1.5, g0 + 1.21, -.7, 8);
  // tables and benches down the hall, for the household
  [-HALL.z + 1.2, HALL.z - 1.2].forEach((z) => { block(6.4, .07, .8, M.wood, .6, g0 + .78, z); block(6.4, .42, .3, M.oak, .6, g0 + .21, z + (z < 0 ? -.65 : .65)); [-2.4, 3.6].forEach((x) => block(.08, .74, .55, M.oak, x, g0 + .39, z)); });
  for (let i = 0; i < 7; i++) { const c = cyl(.05, .04, .15, M.gold, -HALL.x + 1.35, g0 + 1.22, -1.9 + i * .6); c.castShadow = false; }
  [[-HALL.x + 1.4, -2.2], [-HALL.x + 1.4, 2.2]].forEach(([x, z]) => { const L = new THREE.PointLight(0xffb36b, 4, 7, 1.6); L.position.set(x, g0 + 1.7, z); scene.add(L); });

  // ----- the chamber in the west wing: the prince's own room -----
  const CX = -(WING.x0 + WING.x1) / 2;
  block(1.7, .45, 2.1, M.oak, CX - .4, g0 + .25, -4.3); block(1.6, .2, 2.0, M.red, CX - .4, g0 + .56, -4.3); block(1.6, .5, .12, M.oak, CX - .4, g0 + .7, -5.35);
  block(.8, .55, .5, M.wood, CX + 1.6, g0 + .3, -5.6);
  { // a cradle by the bed
    const cr = new THREE.Group(); cr.position.set(CX - 2.0, g0, -2.6); scene.add(cr);
    const sideM = M.wood;
    const b1 = new THREE.Mesh(new THREE.BoxGeometry(.9, .32, .05), sideM); b1.position.set(0, .38, -.24); cr.add(b1);
    const b2 = b1.clone(); b2.position.z = .24; cr.add(b2);
    const b3 = new THREE.Mesh(new THREE.BoxGeometry(.05, .38, .5), sideM); b3.position.set(-.45, .4, 0); cr.add(b3);
    const b4 = b3.clone(); b4.position.x = .45; cr.add(b4);
    const bt = new THREE.Mesh(new THREE.BoxGeometry(.9, .05, .5), sideM); bt.position.y = .22; cr.add(bt);
    const sh = new THREE.Mesh(new THREE.BoxGeometry(.8, .08, .42), M.cloth); sh.position.y = .28; cr.add(sh);
    [-.4, .4].forEach((x) => { const rk = new THREE.Mesh(new THREE.TorusGeometry(.25, .03, 6, 12, Math.PI), M.oak); rk.position.set(x, .25, 0); rk.rotation.set(Math.PI, Math.PI / 2, 0); cr.add(rk); });
    if (!K.reduce) anim.push((t) => { cr.rotation.x = Math.sin(t * 1.3) * .05; });
  }
  // the fireplace on the outer wall of the chamber
  block(.6, 1.6, 2.2, M.stone, -WING.x1 + T + .3, g0 + .8, 1.4); block(.9, .35, 2.4, M.stone, -WING.x1 + T + .45, g0 + 1.75, 1.4);
  fire(-WING.x1 + T + .7, g0, 1.4, .55, 10, 7);
  block(.9, 3.4, 1.5, M.stone, -WING.x1 - .1, g0 + 7.6, 1.4);
  smoke(-WING.x1 - .1, g0 + 9.4, 1.4, 5);
  const wl = new THREE.Mesh(new THREE.PlaneGeometry(WING.x1 - WING.x0 - T, 2 * WING.z - T), M.floor); wl.rotation.x = -Math.PI / 2; wl.position.set(CX, g0 + .025, 0); scene.add(wl);
  const cl = new THREE.PointLight(0xffc888, 3, 7, 1.6); cl.position.set(CX, g0 + 2.2, -2.5); scene.add(cl);
  // the buttery and the pantry in the east wing: barrels and a cask of mead
  for (let i = 0; i < 5; i++) { const b = cyl(.38, .38, .9, M.wood, (WING.x0 + WING.x1) / 2 + (i % 3 - 1) * .9, g0 + .45, -4.4 + Math.floor(i / 3) * .9, 12); b.rotation.z = i > 2 ? Math.PI / 2 : 0; }

  // ----- the yard: a wattle fence, the kitchen, the stable, and the separate enclosure with the oven and the forge -----
  // wattle hurdles: hazel rods woven between stakes
  const wattle = new THREE.MeshStandardMaterial({ roughness: 1, map: K.tex(256, (x, s) => {
    x.fillStyle = "#6e5a3e"; x.fillRect(0, 0, s, s);
    for (let r = 0; r < 16; r++) for (let c = 0; c < 8; c++) { const g = 120 + R() * 40, y = r * 16, o = (r + c) % 2 ? 3 : -3; x.fillStyle = `rgb(${g},${g * .82},${g * .58})`; x.beginPath(); x.ellipse(c * 32 + 16, y + 8 + o, 17, 6.5, 0, 0, 7); x.fill(); }
    for (let c = 0; c <= 8; c++) { x.fillStyle = "#4a3a28"; x.fillRect(c * 32 - 3, 0, 6, s); }
  }) });
  wattle.userData.ts = 2;
  const fence = [[-24, -12], [40, -12], [40, 46], [-24, 46], [-24, -12]];
  for (let i = 0; i < fence.length - 1; i++) {
    const [x1, z1] = fence[i], [x2, z2] = fence[i + 1], L = Math.hypot(x2 - x1, z2 - z1);
    const gaps = []; if (z1 === 46 && z2 === 46) gaps.push([Math.abs(3 - x1), 4.2]); if (x1 === -24 && x2 === -24) gaps.push([Math.abs(-2 - z1), 3]);
    if (z1 === -12 && z2 === -12) gaps.push([Math.abs(26 - x1), 3]);
    gaps.sort((a, b) => a[0] - b[0]); let at = 0, ux = (x2 - x1) / L, uz = (z2 - z1) / L;
    const seg = (a, b) => { for (let d = a; d < b - .1; d += 3) { const e = Math.min(b, d + 3), sx = x1 + ux * d, sz = z1 + uz * d, ex = x1 + ux * e, ez = z1 + uz * e; wallSeg(sx, sz, ex, ez, 1.15, .1, wattle, Math.min(G(sx, sz), G(ex, ez)) - .15); } };
    gaps.forEach(([c, w]) => { seg(at, c - w / 2); at = c + w / 2; }); seg(at, L);
  }
  [[1, 46], [5, 46]].forEach(([x, z]) => { block(.3, 2.6, .3, M.oak, x - .1, G(x, z) + 1.2, z); posts.push([x - .1, z, .2]); });
  // the kitchen: a stone building of its own, away from the hall for fear of fire
  const kit = (cx, cz, w, d, h, mat, roofMat, ry, door) => {
    const gy = G(cx, cz) - .05, c = Math.cos(ry), s = Math.sin(ry), P = (a, b) => [cx + a * c + b * s, cz - a * s + b * c];
    const [p1, p2, p3, p4] = [P(-w / 2, -d / 2), P(w / 2, -d / 2), P(w / 2, d / 2), P(-w / 2, d / 2)];
    wallLine(...p4, ...p3, h, .7, mat, door ? [[w / 2, 1.3]] : [], gy, 2.1); wallLine(...p1, ...p2, h, .7, mat, [], gy);
    wallLine(...p1, ...p4, h, .7, mat, [], gy); wallLine(...p2, ...p3, h, .7, mat, [], gy);
    roof(cx, cz, w, d, gy + h, d * .55, roofMat, ry, .5, mat, .5);
  };
  kit(-12, 31, 9, 6, 2.8, M.stone, M.thatch, 0, true);
  block(1.4, 1.6, 1.0, M.stone, -9, G(-12, 31) + 5.4, 31); smoke(-9, G(-12, 31) + 6.3, 31, 5);
  kit(24, 34, 14, 6, 2.6, M.lime, M.thatch, 0, true);   // the stable
  // the small enclosure to the east, where the oven and the smith's hearth may have stood
  const ex = 27, ez = 8;
  wallLine(ex - 6, ez - 5, ex + 6, ez - 5, 1.2, .6, M.stone, [], G(ex, ez) - .1); wallLine(ex - 6, ez + 5, ex + 6, ez + 5, 1.2, .6, M.stone, [[4, 1.8]], G(ex, ez) - .1);
  wallLine(ex - 6, ez - 5, ex - 6, ez + 5, 1.2, .6, M.stone, [], G(ex, ez) - .1); wallLine(ex + 6, ez - 5, ex + 6, ez + 5, 1.2, .6, M.stone, [], G(ex, ez) - .1);
  const oven = new THREE.Mesh(new THREE.SphereGeometry(1.4, 18, 10, 0, Math.PI * 2, 0, Math.PI / 2), M.stone); oven.position.set(ex - 2.5, G(ex, ez), ez - 1.5); oven.castShadow = true; scene.add(oven); posts.push([ex - 2.5, ez - 1.5, 1.5]);
  smoke(ex - 2.5, G(ex, ez) + 1.4, ez - 1.5, 4);
  // the forge: a hearth under a lean-to, with an anvil
  block(1.4, .8, 1.2, M.stone, ex + 3, G(ex, ez) + .4, ez - 2.6); fire(ex + 3, G(ex, ez) + .8, ez - 2.6, .4, 6, 5);
  [[ex + 1.6, ez - 3.9], [ex + 4.4, ez - 3.9], [ex + 1.6, ez - 1.3], [ex + 4.4, ez - 1.3]].forEach(([x, z]) => block(.18, 2.4, .18, M.oak, x, G(x, z) + 1.2, z));
  roof(ex + 3, ez - 2.6, 3.4, 3.2, G(ex, ez) + 2.4, .8, M.thatch, 0, .3);
  block(.5, .55, .3, M.darkwood, ex + 1.3, G(ex, ez) + .3, ez); block(.55, .12, .22, M.stone, ex + 1.3, G(ex, ez) + .62, ez);
  // firewood and a cart in the yard
  for (let i = 0; i < 12; i++) { const l = cyl(.11, .11, 1.4, M.oak, -18 + (i % 4) * .24, G(-18, 20) + .12 + Math.floor(i / 4) * .21, 20, 7); l.rotation.x = Math.PI / 2; }
  { const cx = 12, cz = 30, gy = G(cx, cz); block(1.6, .12, 3, M.boards, cx, gy + .8, cz, .4); [-1, 1].forEach((s) => { const w = cyl(.55, .55, .1, M.wood, cx + s * .95 * Math.cos(.4), gy + .55, cz - s * .95 * Math.sin(.4), 12); w.rotation.set(0, .4, Math.PI / 2); }); }

  // ----- the mound, Pen y Mwd, with a look-out on its top: an open platform on four posts -----
  const mt = level(MD.x, MD.z) + M_H;
  {
    // the look-out: a timber tower on four posts, on the west of the top
    const tx = TW.x, tz = TW.z;
    [[-1.6, -1.6], [1.6, -1.6], [-1.6, 1.6], [1.6, 1.6]].forEach(([a, b]) => { block(.32, 5.9, .32, M.oak, tx + a, mt + 2.8, tz + b); posts.push([tx + a, tz + b, .25]); });
    block(3.9, .2, 3.9, M.boards, tx, mt + 4.6, tz);
    [[0, -1.8, 3.6, .12], [0, 1.8, 3.6, .12], [-1.8, 0, .12, 3.6], [1.8, 0, .12, 3.6]].forEach(([a, b, w, d]) => block(w, 1.1, d, M.boards, tx + a, mt + 5.25, tz + b));
    for (let i = 0; i < 9; i++) { const st = block(.9, .1, .36, M.oak, tx + 2.1, mt + TW.up * i / 8 - .05, tz + 1.6 - i * .4, 0); st.castShadow = false; }
    [-1, 1].forEach((s2) => { const sr = block(.08, .08, 4.6, M.oak, tx + 2.1 + s2 * .45, mt + TW.up / 2 + .9, tz, 0); sr.rotation.x = Math.atan2(TW.up, 3.2); });
    // a banner of Gwynedd on the tower
    const fx = tx + 1.6, fz = tz + 1.6, pole = cyl(.05, .05, 4, M.oak, fx, mt + 7.4, fz, 6);
    const flag = new THREE.Mesh(new THREE.PlaneGeometry(1.6, 1.1, 8, 1), new THREE.MeshStandardMaterial({ color: 0xa8231c, roughness: .9, side: THREE.DoubleSide }));
    flag.position.set(fx + .85, mt + 8.7, fz); scene.add(flag);
    const fq = new THREE.Mesh(new THREE.PlaneGeometry(.8, .55), new THREE.MeshStandardMaterial({ color: 0xd4a531, roughness: .6, side: THREE.DoubleSide }));
    fq.position.set(fx + .45, mt + 8.97, fz + .01); scene.add(fq);
    const fq2 = fq.clone(); fq2.position.set(fx + 1.25, mt + 8.43, fz + .01); scene.add(fq2);
    if (!K.reduce) { const p = flag.geometry.attributes.position, x0 = p.array.slice(); anim.push((t) => { for (let i = 0; i < p.count; i++) { const x = x0[i * 3]; p.setZ(i, Math.sin(t * 3 + x * 3) * .08 * (x + .8)); } p.needsUpdate = true; }); }
    void pole;
  }

  // ----- the church of St Bodfan, close by the mound -----
  {
    const cx = -100, cz = -78, gy = G(cx, cz) - .1;
    wallLine(cx - 7, cz - 3, cx + 5, cz - 3, 3.6, .8, M.lime, [], gy); wallLine(cx - 7, cz + 3, cx + 5, cz + 3, 3.6, .8, M.lime, [[3, 1.2]], gy, 2.2);
    wallLine(cx - 7, cz - 3, cx - 7, cz + 3, 3.6, .8, M.lime, [], gy); wallLine(cx + 5, cz - 3, cx + 5, cz + 3, 3.6, .8, M.lime, [], gy);
    roof(cx - 1, cz, 12, 6, gy + 3.6, 3.4, M.slate, 0, .4, M.lime, .8);
    wallLine(cx + 5, cz - 2.2, cx + 10, cz - 2.2, 3.0, .7, M.lime, [], gy); wallLine(cx + 5, cz + 2.2, cx + 10, cz + 2.2, 3.0, .7, M.lime, [], gy); wallLine(cx + 10, cz - 2.2, cx + 10, cz + 2.2, 3.0, .7, M.lime, [], gy);
    roof(cx + 7.6, cz, 5, 4.4, gy + 3.0, 2.6, M.slate, 0, .35, M.lime, .7);
    block(.8, 2.2, 1.6, M.lime, cx - 7.1, gy + 7.6, cz); block(.82, .5, .5, M.darkwood, cx - 7.1, gy + 7.7, cz);
    // the round churchyard
    for (let i = 0; i < 26; i++) { const a1 = i / 26 * Math.PI * 2, a2 = (i + 1) / 26 * Math.PI * 2; if (i === 9) continue; wallSeg(cx + Math.cos(a1) * 20, cz + Math.sin(a1) * 17, cx + Math.cos(a2) * 20, cz + Math.sin(a2) * 17, 1.2, .6, M.stone, G(cx + Math.cos(a1) * 20, cz + Math.sin(a1) * 17) - .2); }
    const yew = [[cx - 12, cz + 8, 9, 4.5], [cx + 13, cz - 8, 8, 4]];
    trees(yew);
  }

  // ----- the township round the court: the houses of the prince's bondmen, cruck-framed and thatched -----
  [[-78, 30, .2], [-96, 6, -.1], [-120, 58, .4], [-70, 96, -.3], [-40, 74, .1], [22, 74, -.2], [-20, 104, .3], [-150, 20, .1], [-60, -62, .5], [-140, -30, -.4], [44, 92, .2], [-8, 142, -.1]].forEach(([x, z, a]) => {
    const gy = G(x, z);
    block(7, 2, 4.5, M.lime, x, gy + 1, z, a);
    roof(x, z, 7, 4.5, gy + 2, 2.6, M.thatch, a, .5, M.lime, .3);
    block(.9, 1.7, .1, M.wood, x + Math.sin(a) * 2.3, gy + .85, z + Math.cos(a) * 2.3, a);
    posts.push([x, z, 3.6]);
    if (!K.small && R() < .6) smoke(x, gy + 4.4, z, 4);
  });

  // ----- the mill on the river, below the road -----
  {
    const mz = 18, mx = riverAt(mz) - 9, gy = G(mx, mz);
    wallLine(mx - 3, mz - 2.5, mx + 3, mz - 2.5, 3, .5, M.stone, [], gy - .2); wallLine(mx - 3, mz + 2.5, mx + 3, mz + 2.5, 3, .5, M.stone, [[3, 1.2]], gy - .2, 2.1);
    wallLine(mx - 3, mz - 2.5, mx - 3, mz + 2.5, 3, .5, M.stone, [], gy - .2); wallLine(mx + 3, mz - 2.5, mx + 3, mz + 2.5, 3, .5, M.stone, [], gy - .2);
    roof(mx, mz, 6.5, 5.5, gy + 2.8, 2.4, M.thatch, 0, .4, M.stone, .5);
    const wheel = new THREE.Group(); wheel.position.set(mx + 4.2, gy - .3, mz); scene.add(wheel);
    const rim = new THREE.Mesh(new THREE.TorusGeometry(1.9, .12, 6, 24), M.oak); rim.rotation.y = Math.PI / 2; wheel.add(rim);
    for (let i = 0; i < 12; i++) { const p = new THREE.Mesh(new THREE.BoxGeometry(.7, .1, .45), M.wood); const a = i / 12 * Math.PI * 2; p.position.set(0, Math.sin(a) * 1.9, Math.cos(a) * 1.9); p.rotation.x = -a; wheel.add(p); }
    for (let i = 0; i < 4; i++) { const sp = new THREE.Mesh(new THREE.BoxGeometry(.08, 3.8, .1), M.oak); sp.rotation.x = i * Math.PI / 4; wheel.add(sp); }
    anim.push((t) => { if (!K.reduce) wheel.rotation.x = t * .6; });
  }

  // ----- the bridge over the Afon Aber -----
  {
    const rx = riverAt(BRIDGE.z), x1 = rx - 9, x2 = rx + 9;
    for (let x = x1; x < x2 - .01; x += 1.5) {
      const ya = onBridge(x, BRIDGE.z), yb = onBridge(Math.min(x2, x + 1.5), BRIDGE.z), L = Math.hypot(1.5, yb - ya);
      const d = block(L + .05, .16, BRIDGE.w * 2, M.boards, x + .75, (ya + yb) / 2 - .08, BRIDGE.z); d.rotation.z = Math.atan2(yb - ya, 1.5);
      [-1, 1].forEach((s) => { const gy = G(x, BRIDGE.z + s * BRIDGE.w); if (ya - gy > .3) cyl(.13, .15, ya - gy + .4, M.oak, x, (ya + gy) / 2 - .2, BRIDGE.z + s * (BRIDGE.w - .1), 7); cyl(.06, .06, 1.1, M.oak, x, ya + .55, BRIDGE.z + s * (BRIDGE.w - .1), 6); });
    }
    [-1, 1].forEach((s) => { for (let x = x1; x < x2 - .01; x += 1.5) { const ya = onBridge(x, BRIDGE.z), yb = onBridge(Math.min(x2, x + 1.5), BRIDGE.z); const r = block(1.55, .09, .09, M.oak, x + .75, (ya + yb) / 2 + 1.05, BRIDGE.z + s * (BRIDGE.w - .1)); r.rotation.z = Math.atan2(yb - ya, 1.5); } });
  }

  // ----- Pen y Bryn on the hill across the river, within its banks -----
  {
    const cx = PB.x, cz = PB.z, gy = G(cx, cz) - .1;
    const hw = 8, hd = 3.6;
    wallLine(cx - hw, cz - hd, cx + hw, cz - hd, 4.6, .8, M.stone, [], gy); wallLine(cx - hw, cz + hd, cx + hw, cz + hd, 4.6, .8, M.stone, [[hw + 1, 1.3]], gy, 2.3);
    wallLine(cx - hw, cz - hd, cx - hw, cz + hd, 4.6, .8, M.stone, [], gy); wallLine(cx + hw, cz - hd, cx + hw, cz + hd, 4.6, .8, M.stone, [], gy);
    roof(cx, cz, 2 * hw, 2 * hd, gy + 4.6, 3.6, M.slate, 0, .45, M.stone, .8);
    cyl(3.3, 3.5, 12, M.stone, cx - hw - 1.6, gy + 6, cz, 18); posts.push([cx - hw - 1.6, cz, 3.5]);
    const cap = new THREE.Mesh(new THREE.ConeGeometry(3.7, 3, 18), M.slate); cap.position.set(cx - hw - 1.6, gy + 13.5, cz); cap.castShadow = true; scene.add(cap);
    smoke(cx + 3, gy + 8.6, cz, 4);
  }

  // ----- the water: the sea, and the river -----
  {
    const sg = new THREE.CircleGeometry(2600, 72); sg.rotateX(-Math.PI / 2);
    const seaM = M.water.clone(); seaM.color.set(0x5d7c86);
    const sea = new THREE.Mesh(sg, seaM); sea.position.y = SEA; sea.receiveShadow = true; scene.add(sea);
    const P = [], I = [];
    for (let z = -1150, k = 0; z <= 1250; z += 8, k++) {
      const x = riverAt(z), y = Math.max(SEA + .05, shape(x, z) + .9);
      P.push(x - 4.6, y, z, x + 4.6, y, z);
      if (z > -1150) { const a = (k - 1) * 2; I.push(a, a + 2, a + 1, a + 1, a + 2, a + 3); }
    }
    const rg = new THREE.BufferGeometry(); rg.setAttribute("position", new THREE.Float32BufferAttribute(P, 3)); rg.setIndex(I); rg.computeVertexNormals();
    scene.add(new THREE.Mesh(rg, M.water));
  }

  // ----- beyond the surveyed land: the mountains rising to the Carneddau, and Ynys Môn across the water -----
  {
    const half = LAND.size / 2, S2 = 4800, N = 96, g = new THREE.PlaneGeometry(S2, S2, N, N); g.rotateX(-Math.PI / 2);
    const p = g.attributes.position, col = [], c = new THREE.Color(), grass = new THREE.Color(0x6f8a45), moor = new THREE.Color(0x7a6a42), rock = new THREE.Color(0x7d7a70);
    for (let i = 0; i < p.count; i++) {
      const x = p.getX(i), z = p.getZ(i), ax = Math.abs(x), az = Math.abs(z);
      let y;
      if (ax < half - 1 && az < half - 1) y = -300;
      else {
        const cx = Math.max(-half, Math.min(half, x)), cz = Math.max(-half, Math.min(half, z)), e = shape(cx, cz), d = Math.hypot(x - cx, z - cz);
        if (e < SEA + 3) y = SEA - 3;
        else { const k = .1 + .3 * smooth(-400, 1000, z + Math.max(0, x) * .5); y = e + d * k * smooth(0, 300, d) + 70 * Math.sin(x * .004 + 1) * Math.sin(z * .005) * smooth(0, 500, d); if (z < coast(cx) + 20) y = Math.min(y, SEA - 3); }
      }
      p.setY(i, y);
      c.copy(grass).lerp(moor, Math.min(1, Math.max(0, (y - 40) / 300))).lerp(rock, Math.min(.6, Math.max(0, (y - 500) / 400)));
      col.push(c.r, c.g, c.b);
    }
    g.setAttribute("color", new THREE.Float32BufferAttribute(col, 3)); g.computeVertexNormals();
    scene.add(new THREE.Mesh(g, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 1 })));
    // the far shore: Ynys Môn from the Menai to Penmon, Ynys Seiriol, and the Great Orme far to the north-east; [bearing, height]
    const far = [[268, 0], [276, 10], [285, 22], [295, 30], [305, 26], [315, 34], [322, 30], [330, 40], [338, 36], [345, 28], [351, 18], [354, 4], [355, 0], [357, 0], [358, 9], [360, 10], [361, 0], [400, 0], [404, 22], [408, 32], [412, 30], [416, 18], [418, 0]];
    const FR = 2300, P = [], I = [], C = [];
    const farM = new THREE.MeshBasicMaterial({ vertexColors: true, fog: false });
    const near = new THREE.Color(0x8a9a92), top = new THREE.Color(0xa3b0ae);
    for (let b = 266, k = 0; b <= 420; b += .5, k++) {
      let h = 0;
      for (let i = 0; i < far.length - 1; i++) if (b >= far[i][0] && b <= far[i + 1][0]) { const t = (b - far[i][0]) / (far[i + 1][0] - far[i][0]); h = far[i][1] + (far[i + 1][1] - far[i][1]) * (t * t * (3 - 2 * t)); }
      h = h * 1.4 + (h > 2 ? Math.sin(b * 3.1) * 1.5 : 0);
      const a = b * Math.PI / 180, x = Math.sin(a) * FR, z = -Math.cos(a) * FR;
      P.push(x, SEA - 1, z, x, SEA + h, z); C.push(near.r, near.g, near.b, top.r, top.g, top.b);
      if (k) { const q = (k - 1) * 2; I.push(q, q + 2, q + 1, q + 1, q + 2, q + 3); }
    }
    const fg = new THREE.BufferGeometry(); fg.setAttribute("position", new THREE.Float32BufferAttribute(P, 3)); fg.setAttribute("color", new THREE.Float32BufferAttribute(C, 3)); fg.setIndex(I);
    const fm = new THREE.Mesh(fg, farM); fm.material.side = THREE.DoubleSide; scene.add(fm);
  }

  // ----- trees: the woods up the valley, the hedges, the orchard -----
  const TR = [], clear = (x, z) => Object.values(STOPS).every(([[sx, sz]]) => Math.hypot(x - sx, z - sz) > 16);
  for (let i = 0; i < (K.small ? 500 : 1100); i++) {   // Coedydd Aber: the wooded slopes of the valley to the south and east
    const x = 120 + R() * 900, z = 150 + R() * 1000;
    if (Math.abs(x - riverAt(z)) < 12) continue;
    const y = shape(x, z); if (y > 160) continue;
    if (clear(x, z)) TR.push([x, z, 9 + R() * 7, 3.5 + R() * 2.5]);
  }
  for (let i = 0; i < 90; i++) { const z = -600 + R() * 1200, x = riverAt(z) + (R() < .5 ? -1 : 1) * (7 + R() * 8); if (Math.abs(z - BRIDGE.z) < 8 || !clear(x, z)) continue; TR.push([x, z, 8 + R() * 6, 3 + R() * 2]); }
  for (let i = 0; i < 90; i++) { const x = -700 + R() * 1300, z = -500 + R() * 900; if (Math.hypot(x + 10, z) < 80 || Math.hypot(x - PB.x, z - PB.z) < 55 || Math.hypot(x + 100, z + 78) < 24 || !clear(x, z)) continue; TR.push([x, z, 7 + R() * 5, 3 + R() * 2]); }
  for (let i = 0; i < 5; i++) for (let j = 0; j < 4; j++) TR.push([2 + i * 6 + R(), -44 + j * 6 + R(), 3.4 + R(), 1.8 + R() * .6]);   // an orchard north of the court
  trees(TR);

  // cattle in the meadow and sheep on the hill
  const cowM = new THREE.MeshStandardMaterial({ color: 0x2b211a, roughness: 1 }), sheepM = new THREE.MeshStandardMaterial({ color: 0xd8d2c4, roughness: 1 });
  const beast = (x, z, m, s) => { const y = G(x, z), grp = new THREE.Group(); grp.position.set(x, y, z); grp.rotation.y = R() * 6.3; grp.scale.setScalar(s); scene.add(grp);
    const b = new THREE.Mesh(new THREE.BoxGeometry(1.5, .7, .6), m); b.position.y = .95; grp.add(b);
    const hd = new THREE.Mesh(new THREE.BoxGeometry(.45, .4, .35), m); hd.position.set(.9, 1.05, 0); grp.add(hd);
    [[-.55, -.2], [-.55, .2], [.55, -.2], [.55, .2]].forEach(([a, b2]) => { const l = new THREE.Mesh(new THREE.BoxGeometry(.12, .65, .12), m); l.position.set(a, .32, b2); grp.add(l); }); };
  for (let i = 0; i < 7; i++) beast(-200 + R() * 80, 120 + R() * 80, cowM, 1);
  for (let i = 0; i < 14; i++) beast(200 + R() * 160, -60 + R() * 120, sheepM, .55);
  // two boats drawn up on the shore, for the crossing to Môn
  const boatM = new THREE.MeshStandardMaterial({ color: 0x4a3a2a, roughness: .9 });
  [[-120, coast(-120) + 12, .3], [-108, coast(-108) + 16, -.2]].forEach(([x, z, a]) => { const y = Math.max(SEA, G(x, z)); const bt = new THREE.Mesh(new THREE.SphereGeometry(1, 12, 6, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2), boatM); bt.scale.set(3, .8, 1.1); bt.position.set(x, y + .7, z); bt.rotation.y = a; scene.add(bt); });
}

// inside the hall or its wings
const indoor = (x, z) => (Math.abs(x) < HALL.x && Math.abs(z) < HALL.z) || (Math.abs(x) > WING.x0 && Math.abs(x) < WING.x1 && Math.abs(z) < WING.z);
// tufts of grass everywhere but the trodden yard, the lanes, the water and the shore
const grass = (x, z) => { if (x > -24.5 && x < 40.5 && z > -12.5 && z < 46.5) return false; if (laneDist(x, z) < 2.8 || Math.abs(x - riverAt(z)) < 6) return false; return shape(x, z) > SEA + 3; };
// the river, the mound and the road on the plan
function planExtra(c, P, k) {
  c.strokeStyle = "rgba(95,140,160,.9)"; c.lineWidth = 8 * k; c.beginPath(); for (let z = -120; z <= 160; z += 8) { const [a, b] = P(riverAt(z), z); z === -120 ? c.moveTo(a, b) : c.lineTo(a, b); } c.stroke();
  c.fillStyle = "rgba(120,160,90,.85)"; c.beginPath(); const [a, b] = P(MD.x, MD.z); c.arc(a, b, M_FOOT * k, 0, 7); c.fill();
  c.fillStyle = "rgba(230,220,200,.45)"; const [h1, h2] = P(-WING.x1, -WING.z), [h3, h4] = P(WING.x1, WING.z); c.fillRect(h1, h2, h3 - h1, h4 - h2);
}

export function start(host, D) {
  return run(host, D, {
    STOPS, START, land: LAND, fine: 190, fineAt: [-14, 0], shape, floor, blocked, colour, build, bound: 620, seed: 1282, shadow: 70,
    indoor, grass, grassAt: { x: -10, z: 10, r: 130 }, plan: { x: 2, z: 6, r: 62 }, planExtra, sea: .8, harp: { x: -2, z: 0, r: 9 },
    look: { fog: 0xc9d3d8, fogNear: 90, fogFar: 2700, top: 0x86a2bc, mid: 0xc3d0d8, low: 0xd8dfe2, sun: [-50, 75, 35], sunI: 2.1, hemi: .9, exposure: 1.0 },
  });
}
