/* Dolwyddelan: the castle of the princes of Gwynedd on its rock above the Lledr valley, as it might have looked about
   1280, in the time of Llywelyn ap Gruffudd. Built on the shared court engine (tools/court3d.src.js); the words for
   each stop are in src/courts.py.
     npx esbuild court-dolwyddelan.src.js --bundle --minify --format=esm --target=es2020 --outfile=court-dolwyddelan.js
   What it rests on (see the page's "How we know"):
     - Coflein NPRN 95299 (SH 72181 52338) and Cadw (CN040, listed 18253): two rectangular towers joined by an
       irregular curtain wall on the top of a narrow rocky ridge, with rock-cut ditches and banks on the north-east and
       south-west; the keep first, begun by Llywelyn ab Iorwerth, of local grit and slate rubble on a battered base;
     - the keep: a basement reached by a trapdoor and one great room above it, entered at first-floor level up a
       flight of steps through a forebuilding with a drawbridge pit; a steep roof whose gable line is still in the
       south wall; a fireplace in the east wall and a stair in that wall's thickness to the top;
     - the curtain, up to 2 m thick; the gate in the north-east wall, reached by a timber bridge over the ditch;
       a postern, and an oven in the southern corner between the keep and the curtain;
     - the west tower, of two storeys, each one room, with a fireplace under a hood upstairs, built after the curtain;
     - Tomen Castell, the older tower on its rock below, 8.8 by 9.5 m with walls 2.3-2.95 m thick (Coflein 303046);
     - the land: real heights round the castle (tools/bake_court.py), with Moel Siabod to the north-west.
   The sizes of the towers and the shape of the walls are drawn to the proportions of the plan, not measured; the
   buildings in the ward, the people and the beasts are imagined. x is east and z is south, in metres, with the
   middle of the ward near 0, 0. Positions on the castle are given along the ridge (s, towards the north-east) and
   across it (t, towards the south-east), and turned into x, z by W(s, t). */
import { run, landHeights, smooth } from "./court3d.src.js";
import { LAND } from "./court-dolwyddelan-land.js";

// along and across the ridge, which runs from the south-west up to the north-east
const UA = Math.cos(-.5), UB = Math.sin(-.5), RY = .5;
const W = (s, t) => [s * UA - t * UB, s * UB + t * UA];
const loc = (x, z) => [x * UA + z * UB, -x * UB + z * UA];
const P = 6;   // the top of the rock, inside the walls, 6 m above the slope at its middle
const ell = (s, t) => Math.hypot((s + 3) / 31, t / 19);   // the top of the rock: 1 at its edge

const B = landHeights(LAND);
const bumpC = (v, c, w) => { const k = Math.max(-1, Math.min(1, (v - c) / w)); return .5 * (1 + Math.cos(Math.PI * k)); };

// the gate faces along N (in s, t): the bridge runs out along it over the north-east ditch
const GATE = [18.49, -6.03], N = [.936, -.351];
const gq = (s, t) => [(s - GATE[0]) * N[0] + (t - GATE[1]) * N[1], -(s - GATE[0]) * N[1] + (t - GATE[1]) * N[0]];
const BR = { q0: .9, q1: 23.2, w: 1.25 };

// the Lledr, from Roman Bridge down towards Dolwyddelan village and Betws-y-Coed: [x, z]
const RIVER = [[-2700, 860], [-2000, 830], [-1400, 740], [-800, 830], [-300, 800], [0, 610], [150, 430], [300, 330], [500, 205], [800, 120], [1100, 170], [1400, 115], [1700, -70], [2100, -170], [2400, -560], [2700, -900]];
function riverAt(x) {
  for (let i = 0; i < RIVER.length - 1; i++) { const [x1, z1] = RIVER[i], [x2, z2] = RIVER[i + 1]; if (x >= x1 && x <= x2) return z1 + (z2 - z1) * (x - x1) / (x2 - x1); }
  return RIVER[x < 0 ? 0 : RIVER.length - 1][1];
}
// Tomen Castell, the older castle on its rock between the castle and the river
const TM = { x: 307, z: 173 };   // SH 72488 52165, 307 m east and 173 m south of the castle (Coflein)

function shape(x, z, b) {
  let h = b;
  const [s, t] = loc(x, z), e = ell(s, t);
  // the rock: level inside the walls, falling steeply all round, and running on along the ridge beyond the ditches
  if (e < 1.7) {
    let ridge = P - 13 * Math.pow(smooth(1, 1.65, e), .8);
    ridge += 1.1 * Math.sin(s * .55 + t * .3) * Math.sin(t * .7 - s * .2) * smooth(1, 1.12, e) * (1 - smooth(1.4, 1.7, e));   // crags
    h = Math.max(h, ridge);
  }
  if (Math.abs(t) < 16 && Math.abs(s + 3) < 75) h = Math.max(h, P - 2.5 - .06 * Math.max(0, Math.abs(s + 3) - 31) - (t / 13) ** 2 * 9);
  // the north-east ditch, cut across the ridge in front of the gate, with its bank beyond
  const [q, r] = gq(s, t), wq = 1 - smooth(15, 22, Math.abs(r));
  h += (-4.6 * bumpC(q, 15.5, 3.2) + 1.1 * bumpC(q, 21.2, 2)) * wq;
  // the south-west ditch, cutting the castle off from the higher ground
  const ws = 1 - smooth(14, 21, Math.abs(t));
  h += (-4.4 * bumpC(s, -40, 3.2) + 1.2 * bumpC(s, -45.5, 2.2)) * ws;
  // Tomen Castell's rock, and the ditch on its west side
  const tr = Math.hypot(x - TM.x, z - TM.z), tb = B(TM.x, TM.z);
  h = Math.max(h, tb + 7.5 * (1 - smooth(7, 26, tr)));
  if (x < TM.x - 14 && x > TM.x - 26 && Math.abs(z - TM.z) < 20) h -= 2.2 * bumpC(x, TM.x - 20, 5) * (1 - smooth(12, 20, Math.abs(z - TM.z)));
  // the river in its bed
  const rd = Math.abs(z - riverAt(x));
  h -= 1.6 * (1 - smooth(3, 8, rd));
  return h;
}

const ROAD = [[-2400, 760], [-1500, 600], [-700, 330], [-250, 120], [-72, 42], [-52, -36], [20, -62], [60, -72], [400, -140], [900, -150], [1500, -120], [2400, -330]];
const TRACKS = [
  [W(BR.q1 * N[0] + GATE[0], BR.q1 * N[1] + GATE[1]), [44, -50], [58, -70]],   // from the castle bridge down to the road
  [[60, -72], [150, 40], [205, 170], [TM.x - 12, TM.z - 8]],                     // down the slope to Tomen Castell and the meadows
];
function lineDist(L, x, z) {
  let best = 1e9;
  for (let i = 0; i < L.length - 1; i++) {
    const [x1, z1] = L[i], [x2, z2] = L[i + 1], vx = x2 - x1, vz = z2 - z1, k = Math.max(0, Math.min(1, ((x - x1) * vx + (z - z1) * vz) / (vx * vx + vz * vz)));
    best = Math.min(best, Math.hypot(x - x1 - vx * k, z - z1 - vz * k));
  }
  return best;
}
const laneDist = (x, z) => Math.min(lineDist(ROAD, x, z), ...TRACKS.map((L) => lineDist(L, x, z)));

// the keep: s 10-20 along the ridge, t -2 to 10.5 across it; its great room upstairs; the forebuilding and steps on
// its west side, rising from the north to the door at the south end
const KP = { s0: 10, s1: 20, t0: -2, t1: 10.5, T: 2, up: 3.6, top: 10 };
const STAIR = { s0: 8.2, s1: 9.8, t0: -1.2, t1: 6 }, PORCH = { s0: 7.2, s1: 10, t0: 6, t1: 10.2 };
const DOOR_T = 7.5;
// the west tower, s -26.5 to -15.5, t -6 to 6
const WT = { s0: -26.5, s1: -15.5, t0: -6, t1: 6, T: 1.8, up: 3.8, top: 8.4 };

function onBridge(x, z, ground) {
  const [s, t] = loc(x, z), [q, r] = gq(s, t);
  if (Math.abs(r) > BR.w || q < BR.q0 || q > BR.q1) return null;
  const [ex, ez] = W(GATE[0] + N[0] * BR.q1, GATE[1] + N[1] * BR.q1), y1 = ground(ex, ez), k = (q - BR.q0) / (BR.q1 - BR.q0);
  return P + (y1 - P) * k * k + .12;
}
function floor(x, z, ground) {
  const b = onBridge(x, z, ground); if (b !== null) return b;
  const [s, t] = loc(x, z);
  // in the keep: the great room and the passage through the wall to it; the wall-walks on the east and west walls
  if (s > KP.s0 && s < KP.s1 && t > KP.t0 && t < KP.t1) {
    if (s > 18.7 && s < 19.45 && t > -1.4 && t < 9.9) return P + KP.top + .05;
    if (s > 10.55 && s < 11.3 && t > -1.4 && t < 9.9) return P + KP.top + .05;
    return P + KP.up;
  }
  // the porch of the forebuilding, and the steps up to it
  if (s > 7.9 && s < PORCH.s1 && t > PORCH.t0 && t < 9.5) return P + KP.up;
  if (s > STAIR.s0 && s < STAIR.s1 && t > STAIR.t0 && t <= PORCH.t0) return P + KP.up * Math.max(0, Math.min(1, (t - STAIR.t0) / (PORCH.t0 - STAIR.t0)));
  return ground(x, z);
}
function blocked(x, z) { return Math.abs(z - riverAt(x)) < 4; }
function colour(x, z, y, c) {
  const C = c.constructor, [s, t] = loc(x, z), e = ell(s, t);
  // bare rock on the crags of the ridge, and in the ditches
  const crag = smooth(.98, 1.08, e) * (1 - smooth(1.45, 1.75, e));
  if (crag > 0) c.lerp(new C(0x7a766c), .75 * crag);
  if (e < .99) c.lerp(new C(0x857a62), .55);   // the ward, worn by feet and hooves
  const [q, r] = gq(s, t);
  if (Math.abs(q - 15.5) < 3.4 && Math.abs(r) < 18) c.lerp(new C(0x6e6a5c), .5);
  if (Math.abs(s + 40) < 3.4 && Math.abs(t) < 17) c.lerp(new C(0x6e6a5c), .5);
  // Tomen Castell's rock
  const tr = Math.hypot(x - TM.x, z - TM.z); if (tr < 22 && tr > 6) c.lerp(new C(0x7d786c), .5 * (1 - smooth(14, 22, tr)));
  // the road and the tracks
  const lane = laneDist(x, z); if (lane < 2.6) c.lerp(new C(0x8a7656), .7 * (1 - lane / 2.6));
  // the meadows of Ffriddgelli by the river, the hay greener; the hillsides bracken and heather higher up
  const rd = Math.abs(z - riverAt(x));
  if (rd < 140 && y < -15) c.lerp(new C(0x7e9a4a), .3);
  if (y > 70) c.lerp(new C(0x6e6a40), Math.min(.38, (y - 70) / 220));
  if (y > 300) c.lerp(new C(0x7f7b70), Math.min(.45, (y - 300) / 300));
}

// stops: where you stand [x, z] and where you look [x, y, z]
const T0 = B(TM.x, TM.z) + 7.5;
const STOPS = {
  arrive: [[-80, 50], [W(4, 2)[0], P + 5, W(4, 2)[1]], 42],
  ditch: [W(-50, -5), [W(-21, 0)[0], P + 5, W(-21, 0)[1]]],
  bridge: [W(GATE[0] + N[0] * 11.5, GATE[1] + N[1] * 11.5), [W(18.4, -6)[0], P + 2.6, W(18.4, -6)[1]]],
  ward: [W(-5, -2.5), [W(12, 5)[0], P + 5, W(12, 5)[1]]],
  westtower: [W(-6, 3), [W(-15.5, -1)[0], P + 4.4, W(-15.5, -1)[1]]],
  steps: [W(4.6, -4.8), [W(9, 6.4)[0], P + 3.4, W(9, 6.4)[1]]],
  hall: [W(12.8, 6.6), [W(17.6, 2.2)[0], P + KP.up + 1.2, W(17.6, 2.2)[1]]],
  top: [W(19.05, 2.9), [TM.x, T0 + 2, TM.z], 46],
  tomen: [[TM.x + 34, TM.z + 30], [TM.x, T0 + 4, TM.z], 48],
  pass: [[42, -88], [-1780, 560, -2300], 34],
  siege: [[-30, -62], [W(4, 0)[0], P + 5, W(4, 0)[1]], 52],
  today: [[52, 42], [W(4, 2)[0], P + 6, W(4, 2)[1]], 50],
};
const START = { x: -92, z: 58, yaw: -Math.PI * .28 };

// ---------- the buildings ----------
function build(K) {
  const { THREE, scene, M, R, block, bblock, cyl, wallLine, wallSeg, roof, trees, fire, smoke, posts, anim, ground, table, bench, person, horse, hound, sheep, cow, goose, DYE } = K;
  const G = (x, z) => ground(x, z);
  const S2 = (s, t) => W(s, t);
  const lowest = (pts) => Math.min(...pts.map(([x, z]) => G(x, z)));

  // a wall from (s1, t1) to (s2, t2), in layers [y0, y1, gaps, lintel]: so that windows can open above a floor
  function sWall(s1, t1, s2, t2, T, mat, layers) {
    const [x1, z1] = S2(s1, t1), [x2, z2] = S2(s2, t2);
    layers.forEach(([y0, y1, gaps, lintel]) => wallLine(x1, z1, x2, z2, y1 - y0, T, mat, gaps || [], y0, lintel || 0));
  }
  // a parapet along the outer edge of a wall top, with merlons
  function parapet(s1, t1, s2, t2, T, y, side) {
    const L = Math.hypot(s2 - s1, t2 - t1), us = (s2 - s1) / L, ut = (t2 - t1) / L, ns = -ut * side, nt = us * side, o = T / 2 - .27;
    const [x1, z1] = S2(s1 + ns * o, t1 + nt * o), [x2, z2] = S2(s2 + ns * o, t2 + nt * o);
    wallSeg(x1, z1, x2, z2, .95, .54, M.rubble, y);
    const ry = -Math.atan2(z2 - z1, x2 - x1);
    for (let d = .7; d < L - .5; d += 2.1) bblock(1.05, .8, .54, M.rubble, x1 + (x2 - x1) * d / L, y + 1.35, z1 + (z2 - z1) * d / L, ry);
  }
  // a dark opening in a wall face: shutters, an arrow loop
  const shutter = (s, t, y, w, h, ry) => { const [x, z] = S2(s, t); bblock(w, h, .14, M.darkwood, x, y, z, ry); };

  // ----- the keep -----
  const K0 = KP, T = K0.T;
  const kBase = lowest([S2(K0.s0, K0.t0), S2(K0.s1, K0.t0), S2(K0.s0, K0.t1), S2(K0.s1, K0.t1), S2(K0.s1 + 1.5, (K0.t0 + K0.t1) / 2)]) - 1.2;
  const yU = P + K0.up, yT = P + K0.top;
  // the battered base: the foot of the walls splays out onto the rock
  { const [cx, cz] = S2((K0.s0 + K0.s1) / 2, (K0.t0 + K0.t1) / 2); const bb = block(K0.s1 - K0.s0 + 1.2, P + 1.2 - kBase, K0.t1 - K0.t0 + 1.2, M.rubble, cx, (kBase + P + 1.2) / 2, cz, RY); bb.receiveShadow = true;
    const ft = block(K0.s1 - K0.s0 + .6, .6, K0.t1 - K0.t0 + .6, M.rubble, cx, P + 1.5, cz, RY); void ft; }
  // west and east walls (along t), the full length; north and south walls between them
  const sW = K0.s0 + T / 2, sE = K0.s1 - T / 2, tN = K0.t0 + T / 2, tS = K0.t1 - T / 2;
  const lenT = K0.t1 - K0.t0;
  // the west wall: the door at first-floor level from the forebuilding, and a window
  sWall(sW, K0.t0, sW, K0.t1, T, M.rubble, [[P + 1, yU, []], [yU, yU + 1, [[DOOR_T - K0.t0, 1.2]]], [yU + 1, yT, [[DOOR_T - K0.t0, 1.2], [2.6, .6]], 1.3]]);
  // the east wall: a window to the valley either side of the fireplace
  sWall(sE, K0.t0, sE, K0.t1, T, M.rubble, [[P + 1, yU + 1], [yU + 1, yT, [[1.9, .6], [lenT - 2.4, .6]], 1.3]]);
  // the north wall and the south wall, which carry the gables of the steep roof
  sWall(sW + T / 2, tN, sE - T / 2, tN, T, M.rubble, [[P + 1, yU + 1], [yU + 1, yT, [[3, .6]], 1.3]]);
  sWall(sW + T / 2, tS, sE - T / 2, tS, T, M.rubble, [[P + 1, yU + 1], [yU + 1, yT, [[3, .6]], 1.3]]);
  // narrow loops lighting the basement
  [[K0.s1 + .02, 3], [K0.s1 + .02, 7], [K0.s0 - .02, 1.5]].forEach(([s, t]) => shutter(s, t, P + 1.6, .14, .8, RY + Math.PI / 2));
  // the wall-walks behind the parapets of the east and west walls; the roof between the gables
  parapet(K0.s1, K0.t0, K0.s1, K0.t1, T, yT, 1); parapet(K0.s0, K0.t1, K0.s0, K0.t0, T, yT, 1);
  { const [cx, cz] = S2((K0.s0 + K0.s1) / 2, (K0.t0 + K0.t1) / 2); roof(cx, cz, lenT - T, K0.s1 - K0.s0 - 2 * T + 1.3, yT, 4.3, M.slate, RY - Math.PI / 2, .05, M.rubble, T); }
  // the great room: a boarded floor, the fireplace in the east wall with its 13th-century back, the table and the bed
  { const [cx, cz] = S2((sW + sE) / 2, (tN + tS) / 2); const f = block(sE - sW - T, .2, tS - tN - T, M.boards, cx, yU - .1, cz, RY); f.receiveShadow = true;
    const fm = new THREE.Mesh(new THREE.PlaneGeometry(sE - sW - T - .1, tS - tN - T - .1), M.floor); fm.rotation.set(-Math.PI / 2, 0, RY); fm.position.set(cx, yU + .015, cz); fm.receiveShadow = true; scene.add(fm); }
  // ceiling beams under the roof: tie-beams across from wall to wall
  for (let t = 1; t < 8.6; t += 1.9) { const [x, z] = S2((K0.s0 + K0.s1) / 2, t); bblock(K0.s1 - K0.s0 - 2.2, .3, .28, M.oak, x, yT - .2, z, RY); }
  const FP = { s: K0.s1 - T - .02, t: 4.3 };
  { const [hx, hz] = S2(FP.s - .35, FP.t); block(.7, .3, 2.2, M.rubble, hx, yU + 1.9, hz, RY); block(.5, 1.0, 2.0, M.rubble, ...S2(FP.s - .25, FP.t), RY);   // the hood and the jambs
    const [jx, jz] = S2(FP.s - .25, FP.t - 1.05), [kx, kz] = S2(FP.s - .25, FP.t + 1.05); bblock(.5, 1.75, .3, M.rubble, jx, yU + .87, jz, RY); bblock(.5, 1.75, .3, M.rubble, kx, yU + .87, kz, RY);
    const [fx, fz] = S2(FP.s - .5, FP.t); fire(fx, yU, fz, .7, 16, 9, true);
    const [cx, cz] = S2(K0.s1 - T / 2, K0.t0 + .7); block(1.2, 2.4, 1.3, M.rubble, cx, yT + 1.2, cz, RY); smoke(cx, yT + 2.6, cz, 6); }
  { const L = new THREE.PointLight(0xffc27a, 3.2, 8, 1.6); const [x, z] = S2(14, 3.5); L.position.set(x, yU + 2.2, z); scene.add(L); }
  // the table and its benches, well clear of the hearth and of the door
  { const ry = RY - Math.PI / 2; const [tx, tz] = S2(13.9, 3.0); table(tx, tz, 3.4, .8, ry, yU); const [bx, bz] = S2(13.2, 3.0); bench(bx, bz, 3.2, ry, yU); const [b2x, b2z] = S2(14.65, 3.0); bench(b2x, b2z, 3.2, ry, yU);
    [[13.85, 1.9], [13.95, 3.3], [13.9, 4.2]].forEach(([s, t]) => { const [x, z] = S2(s, t); const c = cyl(.05, .04, .15, M.gold, x, yU + .9, z, 8); c.castShadow = false; }); }
  // a bed in the north-east corner, a chest, and the trapdoor to the basement
  { const [x, z] = S2(16.6, .9); block(1.9, .45, 1.5, M.oak, x, yU + .23, z, RY); block(1.8, .18, 1.4, M.red, x, yU + .52, z, RY);
    const [cx, cz] = S2(12.5, 8.3); block(1.0, .55, .6, M.darkwood, cx, yU + .28, cz, RY);
    const [dx, dz] = S2(16.2, 7.6); const td = block(1.0, .04, 1.0, M.darkwood, dx, yU + .03, dz, RY); td.castShadow = false; }
  // a hanging on the north wall: the lions of Gwynedd
  { const [x, z] = S2((sW + sE) / 2, tN + T / 2 + .03), hm = new THREE.MeshStandardMaterial({ map: K.hanging("#9c1f1a", "#d4a531", "#e8d9a0", "roundel"), roughness: .95, side: THREE.DoubleSide });
    hm.map.repeat.set(1.6, .9); const m = new THREE.Mesh(new THREE.PlaneGeometry(3.4, 1.8), hm); m.position.set(x, yU + 2.3, z); m.rotation.y = RY + Math.PI; scene.add(m); }

  // ----- the forebuilding and its steps -----
  { const [cx, cz] = S2((PORCH.s0 + PORCH.s1) / 2, (PORCH.t0 + PORCH.t1) / 2);
    const base = lowest([S2(PORCH.s0, PORCH.t0), S2(PORCH.s0, PORCH.t1)]) - .6;
    block(PORCH.s1 - PORCH.s0, yU - base, PORCH.t1 - PORCH.t0, M.rubble, cx, (yU + base) / 2, cz, RY);
    // its walls: the outer (west) wall and the south wall, with a window; open to the north, where the steps come up
    sWall(PORCH.s0 + .35, PORCH.t0 - .1, PORCH.s0 + .35, PORCH.t1, .7, M.rubble, [[yU, yU + .9], [yU + .9, yU + 3.0, [[1.9, .5]], 1.0]]);
    sWall(PORCH.s0 + .7, PORCH.t1 - .35, PORCH.s1, PORCH.t1 - .35, .7, M.rubble, [[yU, yU + 3.0]]);
    roof(cx, cz, PORCH.t1 - PORCH.t0 + .2, PORCH.s1 - PORCH.s0 + .2, yU + 3.0, 1.4, M.slate, RY - Math.PI / 2, .2, M.rubble, .4);
    // the drawbridge at the head of the steps, let down, and its pit below
    const [dx, dz] = S2(9, PORCH.t0 + .05); const db = block(1.5, .14, 1.6, M.boards, dx, yU - .02, dz, RY); db.castShadow = true;
    // the steps: stone, each on its own footing
    const n = 15;
    for (let i = 0; i < n; i++) {
      const t0 = STAIR.t0 + (PORCH.t0 - .8 - STAIR.t0) * i / n, t1 = STAIR.t0 + (PORCH.t0 - .8 - STAIR.t0) * (i + 1) / n, y = P + (KP.up) * (i + 1) / (n + 1);
      const [x, z] = S2((STAIR.s0 + STAIR.s1) / 2, (t0 + t1) / 2); bblock(STAIR.s1 - STAIR.s0, y - P + .2, t1 - t0 + .02, M.rubble, x, P - .2 + (y - P + .2) / 2, z, RY);
    }
    // the outer side of the steps, a low wall
    const [ax, az] = S2(STAIR.s0 - .15, STAIR.t0), [bx, bz] = S2(STAIR.s0 - .15, PORCH.t0);
    for (let i = 0; i < 6; i++) { const k0 = i / 6, k1 = (i + 1) / 6, y = P + KP.up * k1; wallSeg(ax + (bx - ax) * k0, az + (bz - az) * k0, ax + (bx - ax) * k1, az + (bz - az) * k1, .8, .3, M.rubble, y - .2, false); }
  }

  // ----- the curtain wall, following the edge of the rock -----
  const CUR = { T: 1.8, top: P + 5.2 };
  const NORTH = [[20, -2], [17, -10], [4, -13.5], [-12, -12.5], [-20, -6]], SOUTH = [[-20, 6], [-17, 11], [-4, 13.5], [10, 10.5]];
  const centre = [-3, 0];
  [NORTH, SOUTH].forEach((line) => {
    for (let i = 0; i < line.length - 1; i++) {
      const [s1, t1] = line[i], [s2, t2] = line[i + 1], L = Math.hypot(s2 - s1, t2 - t1);
      // which side is outside
      const ms = (s1 + s2) / 2, mt = (t1 + t2) / 2, ns = -(t2 - t1) / L, nt = (s2 - s1) / L, side = (ms + ns - centre[0]) ** 2 + (mt + nt - centre[1]) ** 2 > (ms - centre[0]) ** 2 + (mt - centre[1]) ** 2 ? 1 : -1;
      const outs = [0, .25, .5, .75, 1].map((k) => S2(s1 + (s2 - s1) * k + ns * side * 1.8, t1 + (t2 - t1) * k + nt * side * 1.8));
      const y0 = lowest(outs) - .8;
      const gaps = [];
      if (line === NORTH && i === 0) gaps.push([4.3, 2.8]);   // the gate
      if (line === NORTH && i === 1) gaps.push([2.2, 1.0]);   // the postern
      // extend each run a little into the next, so the corners close
      const e1 = i === 0 ? 0 : .6, e2 = i === line.length - 2 ? 0 : .6;
      const a = [s1 - (s2 - s1) / L * e1, t1 - (t2 - t1) / L * e1], b = [s2 + (s2 - s1) / L * e2, t2 + (t2 - t1) / L * e2];
      sWall(a[0], a[1], b[0], b[1], CUR.T, M.rubble, [[y0, CUR.top, gaps.map(([d, w]) => [d + e1, w]), gaps.length ? (line === NORTH && i === 0 ? P + 3.4 - y0 : P + 2.0 - y0) : 0]]);
      parapet(a[0], a[1], b[0], b[1], CUR.T, CUR.top, side);
    }
  });
  // the gate: an arch of dressed stone and two oak leaves standing open; the postern's small door
  { const [s1, t1] = NORTH[0], [s2, t2] = NORTH[1], L = Math.hypot(s2 - s1, t2 - t1), ry = -Math.atan2(S2(s2, t2)[1] - S2(s1, t1)[1], S2(s2, t2)[0] - S2(s1, t1)[0]);
    const at = (d, o) => S2(s1 + (s2 - s1) * d / L - (t2 - t1) / L * o, t1 + (t2 - t1) * d / L + (s2 - s1) / L * o);
    [-1, 1].forEach((k) => { const [jx, jz] = at(4.3 + k * 1.45, 0); bblock(.3, 3.5, 1.9, M.rubble, jx, P + 1.7, jz, ry);
      const [lx, lz] = at(4.3 + k * 1.4 * .5, -1.35), leaf = block(.12, 3.0, 1.35, M.boards, lx, P + 1.55, lz, ry + Math.PI / 2 + k * .15); leaf.castShadow = true;
      for (let j = 0; j < 3; j++) bblock(.06, .12, 1.32, M.iron, lx, P + .5 + j * 1.05, lz, ry + Math.PI / 2 + k * .15); });
  }
  // a timber stair up to the wall-walk, against the inside of the north wall
  { const [s1, t1] = NORTH[2], [s2, t2] = NORTH[3];
    for (let i = 0; i < 16; i++) { const k = .3 + i * .024, s = s1 + (s2 - s1) * k, t = t1 + (t2 - t1) * k + 1.55, [x, z] = S2(s, t); bblock(.32, .08, 1.0, M.oak, x, P + .3 + i * .31, z, RY + .07); }
    [[.3, 1.9], [.66, 1.9]].forEach(([k, o]) => { const [x, z] = S2(s1 + (s2 - s1) * k, t1 + (t2 - t1) * k + o); const h = P + .3 + (k - .3) / .024 * .31; bblock(.14, h - P + .4, .14, M.oak, x, P + (h - P + .4) / 2 - .2, z, RY); });
  }
  // the oven in the southern corner, between the keep and the curtain, and a kitchen against the curtain beside it
  const OV = S2(5.2, 10.4);
  { const oven = new THREE.Mesh(new THREE.SphereGeometry(1.3, 18, 10, 0, Math.PI * 2, 0, Math.PI / 2), M.rubble); oven.position.set(OV[0], P, OV[1]); oven.castShadow = true; scene.add(oven); posts.push([OV[0], OV[1], 1.35]);
    const [mx, mz] = S2(5.2, 9.05); block(.8, .7, .2, M.darkwood, mx, P + .35, mz, RY); smoke(OV[0], P + 1.4, OV[1], 4); }
  // lean-to sheds against the curtain: the kitchen on the south, the stable and the store on the north
  function leanTo(s1, t1, s2, t2, depth, h, side) {
    const L = Math.hypot(s2 - s1, t2 - t1), us = (s2 - s1) / L, ut = (t2 - t1) / L, ns = -ut * side, nt = us * side;
    const o0 = CUR.T / 2, o1 = o0 + depth;
    for (let d = 0; d <= L + .01; d += L / Math.max(1, Math.round(L / 3))) { const [x, z] = S2(s1 + us * d + ns * o1, t1 + ut * d + nt * o1); bblock(.22, h - .2, .22, M.oak, x, P + (h - .2) / 2, z, RY); posts.push([x, z, .15]); }
    const [cx, cz] = S2((s1 + s2) / 2 + ns * (o0 + o1) / 2, (t1 + t2) / 2 + nt * (o0 + o1) / 2), ry = -Math.atan2(S2(s2, t2)[1] - S2(s1, t1)[1], S2(s2, t2)[0] - S2(s1, t1)[0]);
    const pitch = Math.atan2(1.0, depth), rf = block(L + .4, .14, Math.hypot(depth + .4, 1.0), M.thatch, cx, P + h + .5, cz, ry); rf.rotation.set(0, ry, 0); rf.rotateX(-side * pitch);
    const rb = block(L + .3, .1, Math.hypot(depth + .3, 1.0), M.boards, cx, P + h + .38, cz, ry); rb.rotation.set(0, ry, 0); rb.rotateX(-side * pitch);
    return [ns, nt];
  }
  const [kns, knt] = leanTo(-4, 13.5 - .1, 3.5, 11.9, 3.0, 2.3, -1);
  { const [x, z] = S2(-.5 + kns * 2, 12.6 + knt * 2); block(1.2, .8, .9, M.wood, x, P + .4, z, RY); for (let i = 0; i < 4; i++) { const [bx, bz] = S2(-3 + i * .8 + kns * 1.6, 13.1 + knt * 1.6); cyl(.3, .3, .8, M.wood, bx, P + .4, bz, 10); } }
  leanTo(4, -13.5, -8, -12.75, 3.4, 2.4, -1);
  // firewood stacked by the kitchen; a mounting block; a well-trough
  for (let i = 0; i < 12; i++) { const [x, z] = S2(-6.5 + (i % 4) * .25, 10.6); const l = cyl(.1, .1, 1.3, M.oak, x, P + .1 + Math.floor(i / 4) * .2, z, 7); l.rotation.set(0, RY, Math.PI / 2); }

  // ----- the west tower: two storeys, a room on each, with a fireplace under a hood upstairs -----
  {
    const Q = WT, T2 = Q.T, base = lowest([S2(Q.s0, Q.t0), S2(Q.s0, Q.t1), S2(Q.s0 - 1.5, 0), S2(Q.s1, Q.t0), S2(Q.s1, Q.t1)]) - 1.2;
    const yF = P + Q.up, yTop = P + Q.top, lenT = Q.t1 - Q.t0;
    { const [cx, cz] = S2((Q.s0 + Q.s1) / 2, 0); block(Q.s1 - Q.s0 + 1, P + .8 - base, lenT + 1, M.rubble, cx, (base + P + .8) / 2, cz, RY).receiveShadow = true; }
    const sw = Q.s0 + T2 / 2, se = Q.s1 - T2 / 2, tn = Q.t0 + T2 / 2, ts = Q.t1 - T2 / 2;
    // the east wall, onto the ward: the door and a window below, a window above
    sWall(se, Q.t0, se, Q.t1, T2, M.rubble, [[P, P + 1, [[8, 1.3]]], [P + 1, yF, [[8, 1.3], [3.2, .8]], 1.2], [yF, yF + 1.1], [yF + 1.1, yTop, [[4, .7], [8.6, .7]], 1.3]]);
    sWall(sw, Q.t0, sw, Q.t1, T2, M.rubble, [[base, yF + 1.1], [yF + 1.1, yTop, [[lenT / 2, .6]], 1.3]]);
    sWall(sw + T2 / 2, tn, se - T2 / 2, tn, T2, M.rubble, [[base, yTop]]);
    sWall(sw + T2 / 2, ts, se - T2 / 2, ts, T2, M.rubble, [[base, yF + 1.1], [yF + 1.1, yTop, [[3.6, .6]], 1.3]]);
    parapet(Q.s0, Q.t0, Q.s1, Q.t0, T2, yTop, -1); parapet(Q.s1, Q.t1, Q.s0, Q.t1, T2, yTop, -1);
    { const [cx, cz] = S2((Q.s0 + Q.s1) / 2, 0); roof(cx, cz, Q.s1 - Q.s0 - T2, lenT - 2 * T2 + 1.3, yTop, 3.9, M.slate, RY, .05, M.rubble, T2); }
    // the upper floor, and the hooded fireplace
    { const [cx, cz] = S2((sw + se) / 2, 0); block(se - sw - T2, .22, ts - tn - T2, M.boards, cx, yF - .11, cz, RY); }
    { const [hx, hz] = S2(se - T2 / 2 - .5, -1.5); block(.9, 1.2, 2.0, M.rubble, hx, yF + 2.2, hz, RY); const [fx, fz] = S2(se - T2 / 2 - .45, -1.5); fire(fx, yF, fz, .45, 6, 6); }
    { const [cx, cz] = S2(Q.s1 - T2 / 2, -1.5); block(1.0, 2.0, 1.1, M.rubble, cx, yTop + 2.6, cz, RY); smoke(cx, yTop + 3.7, cz, 4); }
    const fl = new THREE.Mesh(new THREE.PlaneGeometry(se - sw - T2 - .1, ts - tn - T2 - .1), M.floor); const [fx, fz] = S2((sw + se) / 2, 0); fl.rotation.set(-Math.PI / 2, 0, RY); fl.position.set(fx, P + .02, fz); fl.receiveShadow = true; scene.add(fl);
    // the ground-floor room: a store of casks, sacks and arms
    for (let i = 0; i < 5; i++) { const [x, z] = S2(-23.5 + (i % 3) * 1.0, -3 + Math.floor(i / 3) * 1.0); cyl(.38, .38, .9, M.wood, x, P + .45, z, 12); }
    { const [x, z] = S2(-23.8, 3.3); block(1.6, .8, .9, M.wood, x, P + .4, z, RY); }
    const L = new THREE.PointLight(0xffc27a, 2, 7, 1.6); const [lx, lz] = S2(-21, 0); L.position.set(lx, P + 2.4, lz); scene.add(L);
  }

  // ----- the bridge over the north-east ditch -----
  {
    const q0 = BR.q0, q1 = BR.q1, n = Math.round((q1 - q0) / 1.6), [bs, bt] = GATE;
    const pt = (q, r) => W(bs + N[0] * q - N[1] * r, bt + N[1] * q + N[0] * r);
    const ry = -Math.atan2(pt(1, 0)[1] - pt(0, 0)[1], pt(1, 0)[0] - pt(0, 0)[0]);
    for (let i = 0; i < n; i++) {
      const qa = q0 + (q1 - q0) * i / n, qb = q0 + (q1 - q0) * (i + 1) / n, [ax, az] = pt(qa, 0), [bx, bz] = pt(qb, 0);
      const ya = onBridge(ax, az, G), yb = onBridge(bx, bz, G), L = Math.hypot(bx - ax, bz - az);
      const d = block(L + .05, .16, BR.w * 2, M.boards, (ax + bx) / 2, (ya + yb) / 2 - .08, (az + bz) / 2, ry); d.rotation.set(0, ry, 0); d.rotateZ(Math.atan2(yb - ya, L));
      [-1, 1].forEach((k) => {
        const [px, pz] = pt(qa, k * (BR.w - .1)), gy = G(px, pz);
        if (ya - gy > .4) cyl(.14, .16, ya - gy + .5, M.oak, px, (ya + gy) / 2 - .25, pz, 7);
        cyl(.06, .06, 1.1, M.oak, px, ya + .55, pz, 6);
        const [rx, rz] = pt((qa + qb) / 2, k * (BR.w - .1)), rl = block(L + .05, .09, .09, M.oak, rx, (ya + yb) / 2 + 1.05, rz, ry); rl.rotation.set(0, ry, 0); rl.rotateZ(Math.atan2(yb - ya, L));
      });
    }
  }

  // ----- Tomen Castell: the older tower on its rock, already old -----
  {
    const ty = B(TM.x, TM.z) + 7.5 - .3, ry = .35, hw = 4.75, hd = 4.4, T3 = 2.5;
    const c = Math.cos(ry), s = Math.sin(ry), Pt = (a, b) => [TM.x + a * c + b * s, TM.z - a * s + b * c];
    const tops = [6.5, 5.2, 7.2, 4.4];
    [[[-hw, -hd + T3 / 2], [hw, -hd + T3 / 2]], [[hw - T3 / 2, -hd], [hw - T3 / 2, hd]], [[hw, hd - T3 / 2], [-hw, hd - T3 / 2]], [[-hw + T3 / 2, hd], [-hw + T3 / 2, -hd]]].forEach(([a, b], i) => {
      const [x1, z1] = Pt(...a), [x2, z2] = Pt(...b);
      wallLine(x1, z1, x2, z2, tops[i] + 1.5, T3, M.rubble, i === 2 ? [[5, 1.2]] : [], ty - 1.5, i === 2 ? 3.5 : 0);
      // the broken top of the wall
      for (let k = 0; k < 4; k++) { const f = .15 + k * .22, h = .4 + R() * 1.2; bblock(1.6 + R(), h, T3 - .2, M.rubble, x1 + (x2 - x1) * f, ty + tops[i] + h / 2 - .1, z1 + (z2 - z1) * f, -Math.atan2(z2 - z1, x2 - x1)); }
    });
  }

  // ----- the crags: bare rock breaking through on the ridge, in the ditches and round Tomen Castell -----
  {
    const RK = [];
    const nearStop = (x, z) => Object.values(STOPS).some(([[sx, sz]]) => Math.hypot(x - sx, z - sz) < 7);
    for (let i = 0; i < 400 && RK.length < (K.small ? 70 : 120); i++) {
      const a = R() * 6.283, e = 1.02 + R() * .75, s = -3 + Math.cos(a) * 31 * e, t = Math.sin(a) * 19 * e, [x, z] = S2(s, t), [q, r] = gq(s, t);
      if (Math.abs(r) < 3.2 && q > 0 && q < BR.q1 + 2) continue;   // keep the bridge clear
      if (nearStop(x, z)) continue;
      RK.push([x, z, .6 + R() * R() * 2.6]);
    }
    for (let i = 0; i < 40; i++) { const a = R() * 6.283, r = 8 + R() * 13; RK.push([TM.x + Math.cos(a) * r, TM.z + Math.sin(a) * r, .8 + R() * 2]); }
    for (let i = 0; i < 160; i++) { const x = -1200 + R() * 2400, z = -1400 + R() * 1200, y = G(x, z); if (y > 60 && Math.abs(x) + Math.abs(z) > 120) RK.push([x, z, 1.5 + R() * 4]); }
    const rg = new THREE.DodecahedronGeometry(1, 0), rm = new THREE.MeshStandardMaterial({ color: 0x9c998f, roughness: .95, flatShading: true });
    const im = new THREE.InstancedMesh(rg, rm, RK.length), m4 = new THREE.Matrix4(), qn = new THREE.Quaternion(), eu = new THREE.Euler(), col = new THREE.Color();
    RK.forEach(([x, z, k], i) => {
      m4.compose(new THREE.Vector3(x, G(x, z) - k * .4, z), qn.setFromEuler(eu.set(R() * .6, R() * 6.3, R() * .6)), new THREE.Vector3(k * (1 + R() * .6), k * (.45 + R() * .4), k * (.8 + R() * .5)));
      im.setMatrixAt(i, m4); col.setHSL(.1 + R() * .04, .06 + R() * .05, .42 + R() * .12); im.setColorAt(i, col);
    });
    im.castShadow = im.receiveShadow = true; scene.add(im);
  }

  // ----- the meadows of Ffriddgelli: huts of the herdsmen at their summer pasture, and a hay barn -----
  [[330, 230, .4], [372, 205, .1], [140, 300, -.3]].forEach(([x, z, a]) => {
    const gy = G(x, z);
    block(5, 1.8, 3.6, M.rubble, x, gy + .9, z, a);
    roof(x, z, 5, 3.6, gy + 1.8, 2.0, M.thatch, a, .4, M.rubble, .4);
    block(.8, 1.5, .1, M.wood, x + Math.sin(a) * 1.85, gy + .75, z + Math.cos(a) * 1.85, a);
    posts.push([x, z, 2.8]);
    if (!K.small) smoke(x, gy + 3.6, z, 3);
  });

  // ----- the water: the Lledr -----
  {
    const Pp = [], I = [];
    for (let x = -2500, k = 0; x <= 2500; x += 8, k++) {
      const z = riverAt(x), y = Math.max(G(x, z - 6), G(x, z), G(x, z + 6)) + .55;
      Pp.push(x, y, z - 4.4, x, y, z + 4.4);
      if (k) { const a = (k - 1) * 2; I.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
    }
    const rg = new THREE.BufferGeometry(); rg.setAttribute("position", new THREE.Float32BufferAttribute(Pp, 3)); rg.setIndex(I); rg.computeVertexNormals();
    const wm = new THREE.Mesh(rg, M.water); wm.material.polygonOffset = true; wm.material.polygonOffsetFactor = -2; scene.add(wm);
  }

  // ----- beyond the surveyed land: the hills going on -----
  {
    const half = LAND.size / 2, S3 = 9000, n = 80, g = new THREE.PlaneGeometry(S3, S3, n, n); g.rotateX(-Math.PI / 2);
    const p = g.attributes.position, col = [], c = new THREE.Color(), grass = new THREE.Color(0x6f8a45), moor = new THREE.Color(0x7a6a42), rock = new THREE.Color(0x7d7a70);
    for (let i = 0; i < p.count; i++) {
      const x = p.getX(i), z = p.getZ(i);
      let y;
      if (Math.abs(x) < half - 1 && Math.abs(z) < half - 1) y = -400;
      else { const cx = Math.max(-half, Math.min(half, x)), cz = Math.max(-half, Math.min(half, z)), e = G(cx, cz), d = Math.hypot(x - cx, z - cz); y = e + d * .1 * smooth(0, 400, d) + 120 * Math.sin(x * .0016 + 1) * Math.sin(z * .0019 + .4) * smooth(0, 800, d); }
      p.setY(i, y);
      c.copy(grass).lerp(moor, Math.min(1, Math.max(0, (y - 60) / 300))).lerp(rock, Math.min(.5, Math.max(0, (y - 450) / 400)));
      col.push(c.r, c.g, c.b);
    }
    g.setAttribute("color", new THREE.Float32BufferAttribute(col, 3)); g.computeVertexNormals();
    scene.add(new THREE.Mesh(g, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 1 })));
  }

  // ----- trees: oak woods on the valley sides, alders along the river; none on the castle's rock -----
  const TR = [], clear = (x, z) => Object.values(STOPS).every(([[sx, sz]]) => Math.hypot(x - sx, z - sz) > 18);
  const offRock = (x, z) => { const [s, t] = loc(x, z); return ell(s, t) > 2.2 && Math.hypot(x - TM.x, z - TM.z) > 34; };
  for (let i = 0; i < (K.small ? 700 : 1500); i++) {
    const x = -1800 + R() * 3600, z = -900 + R() * 2200, rz = riverAt(x), y = G(x, z);
    if (Math.abs(z - rz) < 14 || y > 150 || y < -60 && Math.abs(z - rz) < 120 && R() < .8) continue;   // open meadows on the valley floor
    if (laneDist(x, z) < 5 || !offRock(x, z) || !clear(x, z)) continue;
    if (z < rz && y > 40 && R() < .55) continue;   // the north side is more open, grazed
    TR.push([x, z, 8 + R() * 8, 3 + R() * 2.6]);
  }
  for (let i = 0; i < 160; i++) { const x = -1500 + R() * 3000, z = riverAt(x) + (R() < .5 ? -1 : 1) * (7 + R() * 9); if (!clear(x, z) || !offRock(x, z)) continue; TR.push([x, z, 7 + R() * 5, 2.6 + R() * 1.8]); }
  trees(TR);

  // ----- the people of the castle, about 1280, and their beasts -----
  // at the gate, two of the garrison with spears; a watchman on the keep and one on the north wall
  { const [s1, t1] = NORTH[0], [s2, t2] = NORTH[1]; const L = Math.hypot(s2 - s1, t2 - t1);
    [[3.3, -2.3], [5.3, -2.3]].forEach(([d, o], i) => { const [x, z] = S2(s1 + (s2 - s1) * d / L - (t2 - t1) / L * o, t1 + (t2 - t1) * d / L + (s2 - s1) / L * o); person(x, z, RY - Math.PI / 2 + .3 - i * .5, { arms: "spear", tunic: i ? DYE.woad : DYE.madder, hose: DYE.black, cloak: i ? DYE.green : DYE.woad, beard: !i, h: 1.02 }); }); }
  { const [x, z] = S2(10.95, 2.5); person(x, z, RY + Math.PI / 2 + .4, { arms: "spear", tunic: DYE.green, hose: DYE.black, cloak: DYE.fawn, y: P + KP.top + .05 }); }
  // in the great room: the constable at the table with his men, a woman at the fire, a hound
  { const ry = RY - Math.PI / 2;
    [[13.2, 2.0], [13.2, 3.9]].forEach(([s, t], i) => { const [x, z] = S2(s, t); person(x, z, RY + Math.PI / 2 - Math.PI, { sit: .47, y: yU, tunic: i ? DYE.rust : DYE.madder, hose: DYE.black, cloak: i ? 0 : DYE.woad, beard: true, hair: 0x3d2a1b, arms: i ? "" : "table" }); });
    [[14.65, 2.6]].forEach(([s, t]) => { const [x, z] = S2(s, t); person(x, z, RY + Math.PI / 2, { sit: .47, y: yU, tunic: DYE.green, hose: DYE.brown, beard: false }); });
    { const [x, z] = S2(16.3, 5.8); person(x, z, RY + Math.PI * .1, { arms: "work", woman: true, tunic: DYE.weld, veil: DYE.linen, y: yU }); }
    { const [x, z] = S2(16.4, 3.2); hound(x, z, ry, 0x6a5440, true, yU); }
  }
  // the ward: the cook at the oven, a groom with the horses, a man splitting wood, the smith's boy, hounds and geese
  { const [x, z] = S2(5.0, 8.7); person(x, z, RY + Math.PI, { arms: "work", tunic: DYE.brown, hose: DYE.grey, hood: DYE.fawn }); }
  { const [x, z] = S2(-1.5, 10.0); person(x, z, RY + Math.PI * .9, { arms: "work", woman: true, tunic: DYE.woad, veil: 0xd9cfb8 }); }
  { const [x, z] = S2(-2, -8.8); horse(x, z, RY + Math.PI, 0x6b3d22, true); const [x2, z2] = S2(1.2, -9.0); horse(x2, z2, RY + Math.PI + .1, 0x2b2420); const [gx, gz] = S2(-.2, -7.4); person(gx, gz, RY + .4, { tunic: DYE.fawn, hose: DYE.brown, hood: DYE.green }); }
  { const [x, z] = S2(-7.2, 9.6); person(x, z, RY - .5, { arms: "work", tunic: DYE.rust, hose: DYE.brown, beard: true }); }
  { const [x, z] = S2(2.5, 4.5); hound(x, z, RY + 1, 0x8f7454, true); const [x2, z2] = S2(3.6, 3.6); hound(x2, z2, RY - 2, 0xd8cdb8); }
  for (let i = 0; i < 6; i++) { const [x, z] = S2(-10 + R() * 3, 4 + R() * 3); goose(x, z, R() * 6.3); }
  // on the road below: a traveller leading a packhorse up the pass towards Meirionnydd
  horse(-150, 92, -2.0, 0x8f8a80, true); person(-146.5, 89.5, -2.0, { tunic: DYE.grey, hose: DYE.brown, cloak: DYE.brown, hood: DYE.fawn, free: true });
  // the summer pasture: black cattle on the meadows with their herdsman, sheep on the hill with their shepherd
  for (let i = 0; i < 14; i++) { const x = 300 + R() * 160, z = riverAt(x) - 30 - R() * 70; cow(x, z, R() * 6.3); }
  person(318, riverAt(318) - 58, 1.2, { tunic: DYE.fawn, hose: DYE.brown, cloak: DYE.green, hood: DYE.brown, free: true });
  for (let i = 0; i < 40; i++) { const a = R() * 6.3, r = Math.sqrt(R()) * 45; sheep(-260 + Math.cos(a) * r * 1.5, -220 + Math.sin(a) * r, R() * 6.3, R()); }
  person(-228, -190, -.8, { tunic: DYE.grey, hose: DYE.brown, cloak: DYE.fawn, hood: DYE.brown, free: true });
  hound(-232, -186, -.6, 0x2b2420);
}

// inside the keep's great room or the west tower
const indoor = (x, z) => { const [s, t] = loc(x, z); return (s > 12 && s < 18 && t > 0 && t < 8.5) || (s > WT.s0 + WT.T && s < WT.s1 - WT.T && t > WT.t0 + WT.T && t < WT.t1 - WT.T); };
// tufts of grass everywhere but the ward, the ditches' rock, the lanes and the river
const grass = (x, z) => { const [s, t] = loc(x, z), e = ell(s, t); if (e < 1.04) return false; if (laneDist(x, z) < 2.8 || Math.abs(z - riverAt(x)) < 6) return false; return true; };
function planExtra(c, P2, k) {
  // the rock-cut ditches
  c.strokeStyle = "rgba(110,100,80,.8)"; c.lineWidth = 5 * k;
  c.beginPath(); for (let r = -16; r <= 16; r += 4) { const [s, t] = [GATE[0] + N[0] * 15.5 - N[1] * r, GATE[1] + N[1] * 15.5 + N[0] * r], [a, b] = P2(...W(s, t)); r === -16 ? c.moveTo(a, b) : c.lineTo(a, b); } c.stroke();
  c.beginPath(); for (let t = -15; t <= 15; t += 5) { const [a, b] = P2(...W(-40, t)); t === -15 ? c.moveTo(a, b) : c.lineTo(a, b); } c.stroke();
}

export function start(host, D) {
  return run(host, D, {
    STOPS, START, land: LAND, fine: 230, fineAt: [-2, 0], fineMore: [[110, TM.x, TM.z]], shape, floor, blocked, colour, build, bound: 700, seed: 1283, shadow: 70, far: 9000,
    indoor, grass, grassAt: { x: 0, z: 0, r: 150 }, plan: { x: -1.5, z: 0, r: 46 }, planExtra, harp: { x: W(14, 4)[0], z: W(14, 4)[1], r: 7 },
    people: true, birds: { kind: "rook", x: 60, z: 0, r: 420 }, flock: { x: -260, z: -220 }, kennel: { x: W(3, 4)[0], z: W(3, 4)[1] }, water: (x, z) => Math.abs(z - riverAt(x)),
    look: { fog: 0xc6cfd4, fogNear: 300, fogFar: 9000, top: 0x7f9fbd, mid: 0xc1ccd4, low: 0xd6dde0, sun: [-40, 62, 32], sunI: 2.1, hemi: .9, exposure: 1.0 },
  });
}
