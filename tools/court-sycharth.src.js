/* Sycharth, the court of Owain Glyndŵr, as it might have looked around 1390, when Iolo Goch sang about it.
   Built on the shared court engine (tools/court3d.src.js); the words for each stop are in src/courts.py.
     npx esbuild court-sycharth.src.js --bundle --minify --format=esm --target=es2019 --outfile=court-sycharth.js
   What it rests on (see the page's "How we know"):
     - the earthworks, from the Royal Commission (Coflein NPRN 306999) and Cadw: a ditched motte about 50 m across and
       10.6 m high with a summit 26 m across; a crescent-shaped bailey 64 m across and 32 m deep on the south-west;
     - the 1962-63 excavation (Hague and Warhurst, Archaeologia Cambrensis 1966): two timber-framed buildings on the
       motte top, one about 13 m (43 ft) long, burnt oak, blue roofing slates;
     - Iolo Goch's poem: the moat, the bridge, the gate, the timber "couples", lofts on pillars, a chimney, glass,
       tiled (slate) roofs, a house shaped like a church with its arms (an H plan: a hall with a wing at each end,
       G. A. Williams), the mill, dovecot, orchard, vineyard, fishpond, warren and deer park;
     - the land itself: real heights of the Cynllaith valley (tools/bake_court.py), the river where the survey puts it,
       and the later Pont Sycharth mill site (Coflein NPRN 308885) for the mill.
   The palisades follow the usual way of timber castles and the artist's reconstruction Ifan shared. Sizes of
   buildings, their heights and the layout of the bailey are imagined. x is east and z is south, in metres, with the
   centre of the motte at 0, 0. */
import { run, landHeights, smooth } from "./court3d.src.js";
import { LAND } from "./court-sycharth-land.js";

const STOPS = {
  bridge: [[-58, 58], [-44, 3.2, 44]],
  bailey: [[-38, 40], [-6, 7, 6]],
  motte: [[-27.6, 27.6], [0, 13.5, -1]],
  frame: [[-6.2, 7.6], [-2, 13.6, -1.5]],
  hall: [[2.4, -1.4], [0, 11.2, -6.1]],
  lofts: [[7.2, 5.6], [6.2, 13.4, 1.6]],
  table: [[0.4, -3.2], [-3.4, 10.9, -3]],
  estate: [[8.6, 8.2], [58, 0, 72]],
  park: [[11.3, 2.4], [230, 70, -10], 48],
  prince: [[-11.3, 2.6], [-320, 60, -240], 48],
  fire: [[-37, 30], [0, 14, -3]],
  spade: [[-18, 96], [0, 9, 0]],
};
const START = { x: -66, z: 66, yaw: Math.PI * .75 };

// ---------- the land ----------
const B = landHeights(LAND);
// the valley floor around the court is made level (the survey smears the motte into a low hump)
let ring = 0; for (let i = 0; i < 24; i++) { const a = i / 24 * Math.PI * 2; ring += B(Math.cos(a) * 110, Math.sin(a) * 110); } ring /= 24;
const valley = (x, z) => { const r = Math.hypot(x, z); return (B(x, z) - ring) * smooth(70, 130, r); };

// the river Cynllaith, flowing south down the valley west of the court, along the lowest ground in the survey
const RIVER = [[-30, -560], [-60, -470], [-98, -400], [-112, -300], [-140, -200], [-188, -100], [-204, 0], [-192, 100], [-158, 200], [-90, 300], [-112, 400], [-108, 560]];
function riverAt(z) {
  for (let i = 0; i < RIVER.length - 1; i++) { const [x1, z1] = RIVER[i], [x2, z2] = RIVER[i + 1]; if (z >= z1 && z <= z2) { const t = (z - z1) / (z2 - z1), k = t * t * (3 - 2 * t); return x1 + (x2 - x1) * (k * .5 + t * .5); } }
  return RIVER[z < 0 ? 0 : RIVER.length - 1][0];
}

// the earthworks, measured from the motte's centre
const SW = Math.PI * .75, HALF = .56;                  // the bailey lies to the south-west, about 64 m across
const M_TOP = 9.6, M_R = 13, M_FOOT = 25, MOAT = 8;    // motte top 26 m across, foot 50 m across, about 10.6 m above the moat bottom
const B_IN = 33, B_OUT = 64, B_Y = 1.0;                // the bailey platform, from the motte's moat out to 64 m
function baileyEdge(x, z) {                            // > 0 inside the bailey, metres from its nearest edge
  const r = Math.hypot(x, z); let d = Math.atan2(z, x) - SW; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI;
  return Math.min(r - B_IN, B_OUT - r, (HALF - Math.abs(d)) * r);
}
const POND = { x: 64, z: 76, w: 56, d: 26, a: -.35 };   // the fishpond, below the court to the south-east, with a dam at its lower end
function pondLocal(x, z) { const c = Math.cos(POND.a), s = Math.sin(POND.a), dx = x - POND.x, dz = z - POND.z; return [dx * c - dz * s, dx * s + dz * c]; }
function shape(x, z) {
  const r = Math.hypot(x, z);
  let h = valley(x, z);
  // the river channel
  const rx = x - riverAt(z), rw = Math.abs(rx);
  h -= 1.7 * (1 - smooth(3, 7, rw));
  // the fishpond, dug into the valley floor
  const [px, pz] = pondLocal(x, z), pe = Math.min(POND.w / 2 - Math.abs(px), POND.d / 2 - Math.abs(pz));
  if (pe > 0) h -= 1.8 * smooth(0, 3, pe);
  else if (pe > -5) h += .7 * Math.sin(Math.PI * -pe / 5);   // its banks
  // the motte and its moat
  const be = baileyEdge(x, z);
  if (r < M_FOOT) h = Math.max(h, M_TOP * Math.pow(1 - smooth(M_R, M_FOOT + 1, r), 1.15));
  let moat = r >= M_FOOT - 1 && r <= M_FOOT + MOAT ? Math.sin(Math.PI * (r - (M_FOOT - 1)) / (MOAT + 1)) : 0;
  if (be > -MOAT && be < 0 && r > M_FOOT) moat = Math.max(moat, Math.sin(Math.PI * -be / MOAT));
  if (moat > 0) h = Math.min(h, -2.2 * moat + h * (1 - moat));
  // the bailey platform
  if (be > 0) h = Math.max(h, B_Y * smooth(0, 2.5, be));
  return h;
}
const WATER = -.7;   // the water in the moat
const PONDW = -.45;

const LANE = [[-53, 53], [-80, 90], [-72, 160], [-42, 260], [-22, 420], [-10, 560]];
function laneDist(x, z) {
  let best = 1e9;
  for (let i = 0; i < LANE.length - 1; i++) {
    const [x1, z1] = LANE[i], [x2, z2] = LANE[i + 1], vx = x2 - x1, vz = z2 - z1, t = Math.max(0, Math.min(1, ((x - x1) * vx + (z - z1) * vz) / (vx * vx + vz * vz)));
    best = Math.min(best, Math.hypot(x - x1 - vx * t, z - z1 - vz * t));
  }
  return best;
}
// the bridges: [start x, z, start height, end x, z, end height, half width]
const ax = Math.cos(SW), az = Math.sin(SW);
const BRIDGES = [
  [ax * 75, az * 75, .05, ax * (B_OUT - 1), az * (B_OUT - 1), B_Y + .12, 1.4],          // over the outer moat into the bailey
  [ax * (B_IN + 1.5), az * (B_IN + 1.5), B_Y + .12, ax * (M_R - .2), az * (M_R - .2), M_TOP + .12, 1.15],   // from the bailey up to the motte
];
function onBridge(x, z) {
  for (const [x1, z1, y1, x2, z2, y2, w] of BRIDGES) {
    const vx = x2 - x1, vz = z2 - z1, L2 = vx * vx + vz * vz, t = ((x - x1) * vx + (z - z1) * vz) / L2;
    if (t < 0 || t > 1) continue;
    const px = x1 + vx * t, pz = z1 + vz * t;
    if (Math.hypot(x - px, z - pz) < w) return y1 + (y2 - y1) * t;
  }
  return null;
}
// the house on the motte: an H, a hall between two wings (x from -8.1 to 8.1, z from -7.8 to 1.8)
const STEP = .85;   // a timber fire-step round the inside of the motte palisade, from which you see over it
function inStep(x, z) { const r = Math.hypot(x, z); if (r < M_R - 2.1 || r > M_R - .5) return false; let d = Math.atan2(z, x) - SW; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI; return Math.abs(d) > .32; }
const HALL = { x0: -4.3, x1: 4.3, z0: -6.1, z1: .1 }, WING = { w: 3.8, z0: -7.8, z1: 1.8 };
function floor(x, z, ground) {
  const b = onBridge(x, z); if (b !== null) return b;
  let y = ground(x, z);
  if (x > HALL.x0 && x < HALL.x0 + 2 && z > HALL.z0 && z < HALL.z1) y = M_TOP + .3;   // the dais at the upper end of the hall
  if (inStep(x, z)) y = M_TOP + STEP;   // the fire-step behind the motte palisade
  return y;
}
function blocked(x, z) {
  if (onBridge(x, z) !== null) return false;
  const h = shape(x, z), [px, pz] = pondLocal(x, z);
  if (Math.abs(px) < POND.w / 2 && Math.abs(pz) < POND.d / 2) return true;
  if (Math.abs(x - riverAt(z)) < 3.5) return true;
  return h < WATER + .15;
}
function colour(x, z, y, c) {
  // the lane up the valley to the gate, worn earth
  const lane = laneDist(x, z);
  if (lane < 2.6) c.lerp(new (c.constructor)(0x8a7656), .75 * (1 - lane / 2.6));
  // fields: ridge and furrow down the valley, and hay meadows by the river
  if (Math.abs(z) > 130 && x < 120 && x > -260) { const rf = (Math.sin(x * .9 + z * .05) + 1) / 2; c.lerp(new (c.constructor)(z > 0 ? 0x8b8f45 : 0x7d8a40), .25 + rf * .15); }
  // the bare moat banks and the motte's flanks keep their grass; the bailey yard is trodden
  if (baileyEdge(x, z) > 2) c.lerp(new (c.constructor)(0x8c7a5c), .45);
  if (Math.hypot(x, z) < M_R - .5) c.lerp(new (c.constructor)(0x8c7a5c), .35);
  // the wooded hill of the deer park
  if (x > 150 && y > 18) c.lerp(new (c.constructor)(0x41562c), .5);
}

// ---------- the buildings ----------
function build(K) {
  const { THREE, scene, M, R, tex, block, cyl, wallLine, wallSeg, roof, trees, fire, smoke, posts, walls, anim, ground } = K;
  // close-studded timber framing, the way of the March in Owain's day: dark oak studs, lime-washed panels, a rail at each floor
  const frameTex = tex(512, (x, s) => {
    x.fillStyle = "#e6dfcf"; x.fillRect(0, 0, s, s);
    for (let i = 0; i < 2500; i++) { const v = 200 + (R() - .5) * 50; x.fillStyle = `rgba(${v},${v - 4},${v - 14},.3)`; x.fillRect(R() * s, R() * s, R() * 5 + 1, R() * 5 + 1); }
    const oak = (X, Y, W, H) => { x.fillStyle = "#3b2a1c"; x.fillRect(X, Y, W, H); x.fillStyle = "rgba(255,230,190,.07)"; x.fillRect(X + 2, Y, 3, H); };
    const st = s / 6;   // six studs in 3 m
    for (let i = 0; i < 6; i++) oak(i * st, 0, st * .42, s);
    oak(0, s - 26, s, 26); oak(0, s * .5 - 12, s, 24); oak(0, 0, s, 18);   // sill, floor rail, head
  });
  M.frame = new THREE.MeshStandardMaterial({ map: frameTex, roughness: .9 }); M.frame.userData.ts = 3;
  const MT = M_TOP;

  // ----- the house on the motte -----
  // the hall: two long walls between the wings, 8.6 m long and 6.2 m wide, open to the roof
  const hz = (HALL.z0 + HALL.z1) / 2;
  wallLine(HALL.x0, HALL.z1, HALL.x1, HALL.z1, 4.2, .3, M.frame, [[5.4, 1.5]], MT, 2.3);   // south wall with the door
  wallLine(HALL.x0, HALL.z0, HALL.x1, HALL.z0, 4.2, .3, M.frame, [], MT);                  // north wall, with the chimney
  // the two wings, two storeys, the upper floor jettied out over the lower
  [-1, 1].forEach((s) => {
    const cx = s * (HALL.x1 + WING.w / 2), w = WING.w, x0 = cx - w / 2, x1 = cx + w / 2, z0 = WING.z0, z1 = WING.z1, zc = (z0 + z1) / 2, dd = z1 - z0;
    const inner = s < 0 ? x1 : x0, outer = s < 0 ? x0 : x1;
    wallLine(outer, z0, outer, z1, 3, .3, M.frame, [], MT);
    wallLine(x0, z0, x1, z0, 3, .3, M.frame, [], MT);
    wallLine(x0, z1, x1, z1, 3, .3, M.frame, [[w / 2, 1.2]], MT, 2.1);
    wallLine(inner, z0, inner, z1, 3, .3, M.frame, [[dd / 2 + (hz - zc), 1.3]], MT, 2.1);
    const up = block(w + .8, 2.9, dd + .8, M.frame, cx, MT + 3 + 1.45, zc);   // the upper floor: the lofts
    up.castShadow = true;
    block(w + .9, .22, dd + .9, M.oak, cx, MT + 3.05, zc);                    // the jetty bressumer
    [[x0, z0], [x1, z0], [x0, z1], [x1, z1]].forEach(([px, pz]) => { block(.3, 3, .3, M.oak, px, MT + 1.5, pz); });   // corner posts: Iolo's pillars
    roof(cx, zc, dd + .8, w + .8, MT + 5.9, 3.1, M.slate, Math.PI / 2, .45, M.frame, .3);
    // windows: glass in oak mullions, on the outer wall and the gable
    [[outer + s * .17, MT + 1.4, z0 + 2.4], [outer + s * .17, MT + 1.4, z1 - 2.4], [outer + s * .57, MT + 4.4, zc]].forEach(([wx, wy, wz]) => {
      block(.06, .9, 1.1, M.glass, wx, wy, wz); [-.55, 0, .55].forEach((o) => block(.1, .95, .08, M.oak, wx + s * .03, wy, wz + o)); block(.12, .1, 1.2, M.oak, wx + s * .03, wy - .5, wz); block(.12, .1, 1.2, M.oak, wx + s * .03, wy + .5, wz);
    });
    // inside each wing on the ground floor: a bed, a chest
    block(1.6, .45, 2.0, M.oak, cx, MT + .25, z0 + 1.4); block(1.5, .18, 1.9, s < 0 ? M.red : M.green, cx, MT + .55, z0 + 1.4); block(1, .55, .55, M.wood, cx + s * .8, MT + .3, z1 - 1.0);
  });
  // the hall roof, its ridge running between the wings, and its "couples": arch-braced trusses you can see from below
  const HE = MT + 4.2, HR = 3.4;
  roof(0, hz, HALL.x1 - HALL.x0 + 1.2, HALL.z1 - HALL.z0, HE, HR, M.slate, 0, .7);
  for (let x = HALL.x0 + 1.6; x < HALL.x1 - .5; x += 1.8) {
    const half = (HALL.z1 - HALL.z0) / 2, ang = Math.atan2(HR, half), len = Math.hypot(half, HR);
    [-1, 1].forEach((s) => {
      const rf = block(.22, .26, len, M.oak, x, HE + HR / 2 - .1, hz + s * half / 2); rf.rotation.set(s * ang, 0, 0);
      const br = block(.18, .2, 2.2, M.oak, x, HE - .25, hz + s * (half - .9)); br.rotation.set(-s * .85, 0, 0);
    });
    block(.22, .24, 2.6, M.oak, x, HE + HR * .58, hz);       // collar
    block(.24, .3, HALL.z1 - HALL.z0, M.oak, x, HE - .05, hz); // tie beam
  }
  // the chimney: a stone stack on the north wall, the fire in the hearth at its foot
  block(1.8, 10.6, 1.1, M.stone, 0, MT + 5.3, HALL.z0 - .55);
  block(1.3, .9, .5, M.stone, 0, MT + 10.4 - .2, HALL.z0 - .55);
  block(2.2, 1.6, .5, M.stone, -.0, MT + .8, HALL.z0 + .25);   // the fireplace's back and hood
  block(2.4, .35, .9, M.stone, 0, MT + 1.75, HALL.z0 + .45);
  fire(0, MT, HALL.z0 + .55, .9, 26, 12, true);
  smoke(0, MT + 10.6, HALL.z0 - .55);
  posts.push([0, HALL.z0 + .5, .9]);
  // the hall windows: glass, which Iolo praised
  [-2.2, 2.2].forEach((wx) => { block(1.1, 1.1, .06, M.glass, wx, MT + 2.4, HALL.z1 + .17); block(1.2, .1, .1, M.oak, wx, MT + 1.8, HALL.z1 + .2); block(1.2, .1, .1, M.oak, wx, MT + 3.0, HALL.z1 + .2); [-.55, 0, .55].forEach((o) => block(.08, 1.2, .1, M.oak, wx + o, MT + 2.4, HALL.z1 + .2)); });
  [-2.6, 2.6].forEach((wx) => block(1.0, 1.0, .06, M.glass, wx, MT + 2.6, HALL.z0 - .17));
  // the hall floor of rushes, the dais at the upper (west) end, the high table, Owain's chair, the benches and the tables
  const fl = new THREE.Mesh(new THREE.PlaneGeometry(HALL.x1 - HALL.x0, HALL.z1 - HALL.z0), M.floor); fl.rotation.x = -Math.PI / 2; fl.position.set(0, MT + .02, hz); fl.receiveShadow = true; scene.add(fl);
  block(2, .3, HALL.z1 - HALL.z0 - .4, M.boards, HALL.x0 + 1, MT + .15, hz);
  block(.8, .08, 4.2, M.wood, HALL.x0 + 1.25, MT + 1.1, hz); [-1.7, 1.7].forEach((o) => block(.06, .75, .06, M.oak, HALL.x0 + 1.25, MT + .7, hz + o));
  block(.9, .5, .7, M.oak, HALL.x0 + .5, MT + .55, hz); block(.12, 1.6, .8, M.oak, HALL.x0 + .2, MT + 1.1, hz); block(.4, .5, .7, M.red, HALL.x0 + .55, MT + .85, hz);
  const hang = new THREE.Mesh(new THREE.PlaneGeometry(3.2, 2.2), M.red); hang.rotation.y = Math.PI / 2; hang.position.set(HALL.x0 + .2, MT + 2.2, hz); scene.add(hang);
  [HALL.z0 + 1.1, HALL.z1 - 1.1].forEach((z) => { block(4.2, .07, .75, M.wood, 1.2, MT + .78, z); block(4.2, .4, .3, M.oak, 1.2, MT + .2, z + (z < hz ? -.6 : .6)); [-.8, 3.2].forEach((x) => block(.08, .72, .5, M.oak, x, MT + .38, z)); });
  for (let i = 0; i < 6; i++) { const c = cyl(.05, .04, .14, M.gold, HALL.x0 + 1.25, MT + 1.21, hz - 1.6 + i * .64); c.castShadow = false; }
  [[HALL.x0 + 1.25, hz - 1.9], [HALL.x0 + 1.25, hz + 1.9]].forEach(([x, z]) => { const L = new THREE.PointLight(0xffb36b, 4, 7, 1.6); L.position.set(x, MT + 1.6, z); scene.add(L); });
  // the second building on the motte: the kitchen, with its own hearth
  const KX = 1.6, KZ = 6.9;
  wallLine(KX - 2.8, KZ - 1.9, KX + 2.8, KZ - 1.9, 2.8, .3, M.frame, [[1.5, 1.3]], MT, 2.1);
  wallLine(KX - 2.8, KZ + 1.9, KX + 2.8, KZ + 1.9, 2.8, .3, M.frame, [], MT);
  wallLine(KX - 2.8, KZ - 1.9, KX - 2.8, KZ + 1.9, 2.8, .3, M.frame, [], MT);
  wallLine(KX + 2.8, KZ - 1.9, KX + 2.8, KZ + 1.9, 2.8, .3, M.frame, [], MT);
  roof(KX, KZ, 6.2, 3.8, MT + 2.8, 2.4, M.slate, 0, .5, M.frame, .3);
  block(1.2, 1.4, .6, M.stone, KX + 2.2, MT + 4.6, KZ); smoke(KX + 2.2, MT + 5.4, KZ, 5);
  fire(KX + 1.8, MT, KZ, .6, 8, 6);
  // the palisade round the top of the motte, with a gate where the bridge comes in
  palisade(0, 0, M_R - .4, MT - .2, 2.2, [SW, .18]);
  {   // the fire-step: boards on posts round the inside of the palisade
    const N = 40, r = M_R - 1.3;
    for (let i = 0; i < N; i++) {
      const a = i / N * Math.PI * 2 + Math.PI / N; let d = a - SW; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI;
      if (Math.abs(d) < .36) continue;
      block(1.6, .12, r * Math.PI * 2 / N + .05, M.boards, Math.cos(a) * r, MT + STEP - .06, Math.sin(a) * r, -a);
      block(1.5, STEP - .1, .14, M.oak, Math.cos(a) * r, MT + (STEP - .1) / 2, Math.sin(a) * r, -a + Math.PI / 2);
    }
  }
  // the gate on the motte
  const gx = Math.cos(SW) * (M_R - .4), gz = Math.sin(SW) * (M_R - .4);
  [-1, 1].forEach((s) => block(.35, 3.6, .35, M.oak, gx + Math.cos(SW + Math.PI / 2) * s * 1.35, MT + 1.6, gz + Math.sin(SW + Math.PI / 2) * s * 1.35));
  block(3.2, .35, .4, M.oak, gx, MT + 3.3, gz, -SW - Math.PI / 2);

  // ----- the bridges -----
  BRIDGES.forEach(([x1, z1, y1, x2, z2, y2, w]) => {
    const L = Math.hypot(x2 - x1, z2 - z1), ry = -Math.atan2(z2 - z1, x2 - x1), pitch = Math.atan2(y2 - y1, L);
    const deck = block(L + .4, .18, w * 2, M.boards, (x1 + x2) / 2, (y1 + y2) / 2 - .09, (z1 + z2) / 2); deck.rotation.set(0, ry, pitch, "YXZ");
    const ux = (x2 - x1) / L, uz = (z2 - z1) / L, nx = -uz, nz = ux;
    for (let t = 0; t <= L; t += 3) {   // trestles and handrail posts
      const px = x1 + ux * t, pz = z1 + uz * t, py = y1 + (y2 - y1) * t / L, gy = ground(px, pz);
      [-1, 1].forEach((s) => {
        const qx = px + nx * s * (w - .1), qz = pz + nz * s * (w - .1);
        if (py - gy > .3) cyl(.14, .16, py - gy + .6, M.oak, qx, (py + gy) / 2 - .3, qz, 7);
        cyl(.07, .07, 1.1, M.oak, qx, py + .55, qz, 6);
      });
    }
    [-1, 1].forEach((s) => {   // handrails, which you cannot step over
      const r = block(L, .1, .1, M.oak, (x1 + x2) / 2 + nx * s * (w - .1), (y1 + y2) / 2 + 1.05, (z1 + z2) / 2 + nz * s * (w - .1)); r.rotation.set(0, ry, pitch, "YXZ");
    });
  });

  // ----- the bailey -----
  // the palisade round the bailey: the outer curve, the two ends, and the inner curve facing the motte, with two gates
  {
    const a0 = SW - HALF, a1 = SW + HALF, Ro = B_OUT - 1.2, Ri = B_IN + 1.3, pts = [];
    for (let i = 0; i <= 19; i++) { const a = a0 + (a1 - a0) * i / 19; pts.push([Math.cos(a) * Ro, Math.sin(a) * Ro]); }
    for (let i = 0; i <= 11; i++) { const a = a1 - (a1 - a0) * i / 11; pts.push([Math.cos(a) * Ri, Math.sin(a) * Ri]); }
    pts.push(pts[0]);
    const gates = [[Math.cos(SW) * Ro, Math.sin(SW) * Ro, 3.4], [Math.cos(SW) * Ri, Math.sin(SW) * Ri, 2.4]];
    for (let i = 0; i < pts.length - 1; i++) {
      const [x1, z1] = pts[i], [x2, z2] = pts[i + 1], L = Math.hypot(x2 - x1, z2 - z1);
      const gaps = [];
      gates.forEach(([gx2, gz2, gw]) => { const t = ((gx2 - x1) * (x2 - x1) + (gz2 - z1) * (z2 - z1)) / (L * L); if (t > -.05 && t < 1.05 && Math.hypot(x1 + (x2 - x1) * t - gx2, z1 + (z2 - z1) * t - gz2) < .5) gaps.push([t * L, gw]); });
      wallLine(x1, z1, x2, z2, 3.4, .35, M.logs, gaps, B_Y - .3);
    }
    // the gatehouse over the outer gate: a timber tower on four posts, with a slate roof
    const gxo = Math.cos(SW) * Ro, gzo = Math.sin(SW) * Ro, ry = -SW - Math.PI / 2;
    const px = Math.cos(SW + Math.PI / 2), pz = Math.sin(SW + Math.PI / 2), qx = Math.cos(SW), qz = Math.sin(SW);
    [[-1, -1], [-1, 1], [1, -1], [1, 1]].forEach(([a, b]) => { block(.4, 6.2, .4, M.oak, gxo + px * a * 2 + qx * b * 1.3, B_Y + 3.1, gzo + pz * a * 2 + qz * b * 1.3); posts.push([gxo + px * a * 2 + qx * b * 1.3, gzo + pz * a * 2 + qz * b * 1.3, .3]); });
    block(4.6, 2.4, 3.2, M.frame, gxo, B_Y + 5.1, gzo, ry);
    roof(gxo, gzo, 4.6, 3.2, B_Y + 6.3, 2.2, M.slate, ry, .4, M.frame, .3);
    block(1.6, .12, 2.6, M.oak, gxo + px * 1.1, B_Y + 1.6, gzo + pz * 1.1, ry - .8);   // one leaf of the gate, standing open
  }
  // the ranges round the bailey: lodgings, kitchen and bakehouse, stables, each framed and roofed in slate
  const range = (r, a, len, dep, h) => {
    const cx = Math.cos(a) * r, cz = Math.sin(a) * r, ry = -a - Math.PI / 2;   // long side along the curve
    const ux = Math.cos(a + Math.PI / 2), uz = Math.sin(a + Math.PI / 2), nx = Math.cos(a), nz = Math.sin(a);
    const c = (s, t) => [cx + ux * s * len / 2 + nx * t * dep / 2, cz + uz * s * len / 2 + nz * t * dep / 2];
    const [a1, a2, a3, a4] = [c(-1, -1), c(1, -1), c(1, 1), c(-1, 1)];
    const doors = [];
    for (let d = 2.5; d < len - 1; d += 5) doors.push([d, 1.2]);
    wallLine(...a1, ...a2, h, .3, M.frame, doors, B_Y, 2.0);   // the side facing the yard
    wallLine(...a2, ...a3, h, .3, M.frame, [], B_Y); wallLine(...a3, ...a4, h, .3, M.frame, [], B_Y); wallLine(...a4, ...a1, h, .3, M.frame, [], B_Y);
    roof(cx, cz, len, dep, B_Y + h, 2.3, M.slate, ry, .5, M.frame, .3);
  };
  range(54.5, SW - .3, 14, 5.5, 2.8);
  range(54.5, SW + .3, 14, 5.5, 2.8);
  // along the ends of the crescent
  [[SW - HALF + .1, 1], [SW + HALF - .1, -1]].forEach(([a, s]) => {
    const r = 46, cx = Math.cos(a) * r, cz = Math.sin(a) * r, tx = Math.cos(a + s * Math.PI / 2) * 2.8, tz = Math.sin(a + s * Math.PI / 2) * 2.8;
    const x0 = cx + tx, z0 = cz + tz, ux = Math.cos(a), uz = Math.sin(a), L = 13, dep = 5.4;
    const p1 = [x0 - ux * L / 2, z0 - uz * L / 2], p2 = [x0 + ux * L / 2, z0 + uz * L / 2], nx = -Math.cos(a + s * Math.PI / 2) * dep, nz = -Math.sin(a + s * Math.PI / 2) * dep;
    wallLine(p1[0] + nx, p1[1] + nz, p2[0] + nx, p2[1] + nz, 2.7, .3, M.frame, [[L / 2, 2.4]], B_Y, 2.1);
    wallLine(...p1, ...p2, 2.7, .3, M.frame, [], B_Y);
    wallLine(...p1, p1[0] + nx, p1[1] + nz, 2.7, .3, M.frame, [], B_Y); wallLine(...p2, p2[0] + nx, p2[1] + nz, 2.7, .3, M.frame, [], B_Y);
    roof(x0 + nx / 2, z0 + nz / 2, L, dep, B_Y + 2.7, 2.2, M.slate, -a, .5, M.frame, .3);
  });
  // the bakehouse oven, the well, the dovecot of stone with its slate cap, firewood and a cart
  const bx = Math.cos(SW + .32) * 44, bz = Math.sin(SW + .32) * 44;
  const oven = new THREE.Mesh(new THREE.SphereGeometry(1.3, 18, 10, 0, Math.PI * 2, 0, Math.PI / 2), M.stone); oven.position.set(bx, B_Y, bz); oven.castShadow = true; scene.add(oven); posts.push([bx, bz, 1.4]);
  smoke(bx, B_Y + 1.4, bz, 4);
  const wx = Math.cos(SW - .1) * 41, wz = Math.sin(SW - .1) * 41;
  cyl(.8, .85, .8, M.stone, wx, B_Y + .4, wz, 14); posts.push([wx, wz, .9]);
  [-1, 1].forEach((s) => block(.12, 1.6, .12, M.oak, wx + s * .75, B_Y + 1.2, wz)); block(1.7, .12, .12, M.oak, wx, B_Y + 2, wz);
  const dx = Math.cos(SW - .36) * 44, dz = Math.sin(SW - .36) * 44;
  cyl(2.1, 2.2, 4.6, M.stone, dx, B_Y + 2.3, dz, 18); posts.push([dx, dz, 2.3]);
  const cap = new THREE.Mesh(new THREE.ConeGeometry(2.6, 2.2, 18), M.slate); cap.position.set(dx, B_Y + 5.7, dz); cap.castShadow = true; scene.add(cap);
  cyl(.35, .35, .6, M.wood, dx, B_Y + 7, dz, 8);
  for (let i = 0; i < 6; i++) { const a = i / 6 * Math.PI * 2; block(.25, .2, .05, M.oak, dx + Math.cos(a) * 2.13, B_Y + 3.6, dz + Math.sin(a) * 2.13, -a + Math.PI / 2); }
  // doves on the dovecot roof, and peacocks in the yard
  const birdM = new THREE.MeshStandardMaterial({ color: 0xdedbd4, roughness: .9 }), peaM = new THREE.MeshStandardMaterial({ color: 0x1f5a6e, roughness: .6, metalness: .2 }), tailM = new THREE.MeshStandardMaterial({ color: 0x2f6d3c, roughness: .6, side: THREE.DoubleSide });
  for (let i = 0; i < 5; i++) { const a = R() * 6.3, b = new THREE.Mesh(new THREE.SphereGeometry(.12, 8, 6), birdM); b.scale.set(1.5, 1, 1); b.position.set(dx + Math.cos(a) * 1.3, B_Y + 5.4 + R() * .3, dz + Math.sin(a) * 1.3); scene.add(b); }
  [[SW + .12, 39], [SW - .2, 49]].forEach(([a, r], i) => {
    const x = Math.cos(a) * r, z = Math.sin(a) * r, grp = new THREE.Group(); grp.position.set(x, B_Y, z); grp.rotation.y = i * 2.2; scene.add(grp);
    const body = new THREE.Mesh(new THREE.SphereGeometry(.22, 10, 8), peaM); body.scale.set(1.5, 1, 1); body.position.y = .55; grp.add(body);
    const neck = new THREE.Mesh(new THREE.CylinderGeometry(.04, .06, .45, 6), peaM); neck.position.set(.28, .85, 0); neck.rotation.z = -.3; grp.add(neck);
    const tail = new THREE.Mesh(new THREE.CircleGeometry(.75, 18, 0, Math.PI), tailM); tail.position.set(-.3, .6, 0); tail.rotation.set(0, Math.PI / 2, 0); if (i) tail.scale.set(1, .35, 1); grp.add(tail);
    [-.06, .06].forEach((o) => { const l = new THREE.Mesh(new THREE.CylinderGeometry(.015, .015, .45, 4), M.oak); l.position.set(0, .22, o); grp.add(l); });
  });
  for (let i = 0; i < 12; i++) { const l = cyl(.11, .11, 1.4, M.oak, Math.cos(SW + .45) * 50 + (i % 4) * .24, B_Y + .12 + Math.floor(i / 4) * .21, Math.sin(SW + .45) * 50, 7); l.rotation.x = Math.PI / 2; }

  // ----- the water: the moat, the fishpond and the river -----
  {
    const mg = new THREE.CircleGeometry(B_OUT + MOAT + 6, 64); mg.rotateX(-Math.PI / 2);
    const moat = new THREE.Mesh(mg, M.water); moat.position.y = WATER; moat.receiveShadow = true; scene.add(moat);
    const pg = new THREE.PlaneGeometry(POND.w + 2, POND.d + 2); pg.rotateX(-Math.PI / 2);
    const pond = new THREE.Mesh(pg, M.water); pond.position.set(POND.x, PONDW + valley(POND.x, POND.z), POND.z); pond.rotation.y = -POND.a; scene.add(pond);
    // the dam at the pond's lower (south) end
    const [dlx, dlz] = [POND.x + Math.sin(POND.a) * (POND.d / 2 + 2.5), POND.z + Math.cos(POND.a) * (POND.d / 2 + 2.5)];
    const dam = block(POND.w + 6, 1.6, 3, new THREE.MeshStandardMaterial({ color: 0x6a8040, roughness: 1 }), dlx, valley(dlx, dlz) + .2, dlz, -POND.a); dam.castShadow = false;
    // the river as a ribbon of water down its channel
    const P = [], I = [];
    for (let z = -560, k = 0; z <= 560; z += 8, k++) {
      const x = riverAt(z), y = shape(x, z) + .9;
      P.push(x - 4.2, y, z, x + 4.2, y, z);
      if (z > -560) { const a = (k - 1) * 2; I.push(a, a + 2, a + 1, a + 1, a + 2, a + 3); }
    }
    const rg = new THREE.BufferGeometry(); rg.setAttribute("position", new THREE.Float32BufferAttribute(P, 3)); rg.setIndex(I); rg.computeVertexNormals();
    scene.add(new THREE.Mesh(rg, M.water));
  }

  // ----- the mill on the Cynllaith, where Pont Sycharth mill later stood -----
  {
    const mz = -30, mx = riverAt(mz) + 9, gy = ground(mx, mz);
    wallLine(mx - 3, mz - 2.5, mx + 3, mz - 2.5, 3, .5, M.stone, [], gy - .2); wallLine(mx - 3, mz + 2.5, mx + 3, mz + 2.5, 3, .5, M.stone, [[3, 1.2]], gy - .2, 2.1);
    wallLine(mx - 3, mz - 2.5, mx - 3, mz + 2.5, 3, .5, M.stone, [], gy - .2); wallLine(mx + 3, mz - 2.5, mx + 3, mz + 2.5, 3, .5, M.stone, [], gy - .2);
    roof(mx, mz, 6.5, 5.5, gy + 2.8, 2.4, M.slate, 0, .4, M.stone, .5);
    const wheel = new THREE.Group(); wheel.position.set(mx - 4.2, gy - .2, mz); scene.add(wheel);
    const rim = new THREE.Mesh(new THREE.TorusGeometry(1.9, .12, 6, 24), M.oak); rim.rotation.y = Math.PI / 2; wheel.add(rim);
    for (let i = 0; i < 12; i++) { const p = new THREE.Mesh(new THREE.BoxGeometry(.7, .1, .45), M.wood); const a = i / 12 * Math.PI * 2; p.position.set(0, Math.sin(a) * 1.9, Math.cos(a) * 1.9); p.rotation.x = -a; wheel.add(p); }
    for (let i = 0; i < 4; i++) { const sp = new THREE.Mesh(new THREE.BoxGeometry(.08, 3.8, .1), M.oak); sp.rotation.x = i * Math.PI / 4; wheel.add(sp); }
    anim.push((t) => { if (!K.reduce) wheel.rotation.x = -t * .6; });
  }

  // ----- tenants' houses down the valley: cruck-framed, thatched -----
  [[-70, 170, .3], [-40, 205, -.2], [30, -170, .1], [-95, -150, .5], [-60, -230, -.3], [10, 230, .2]].forEach(([x, z, a]) => {
    const gy = ground(x, z);
    block(7, 2, 4.5, M.lime, x, gy + 1, z, a);
    roof(x, z, 7, 4.5, gy + 2, 2.6, M.thatch, a, .5, M.lime, .3);
    block(.9, 1.7, .1, M.wood, x + Math.sin(a) * 2.3, gy + .85, z + Math.cos(a) * 2.3, a);
    posts.push([x, z, 3.6]);
    if (!K.small) smoke(x, gy + 4.4, z, 4);
  });

  // ----- the orchard, the vineyard, the deer park and its pale, the warren -----
  const T = [];
  for (let i = 0; i < 6; i++) for (let j = 0; j < 5; j++) T.push([-30 + i * 6 + R() * 1.5, -78 + j * 6 + R() * 1.5, 3.4 + R(), 1.8 + R() * .6]);   // the orchard, north of the motte
  // the vineyard: rows of staked vines on the slope to the north-east
  const vineM = new THREE.MeshStandardMaterial({ color: 0x55702f, roughness: 1 });
  for (let r = 0; r < 9; r++) {
    const z = -75 + r * 3.2;
    for (let x = 70; x < 104; x += 1.6) { const y = ground(x, z); const v = new THREE.Mesh(new THREE.BoxGeometry(1.5, .9, .5), vineM); v.position.set(x, y + .6, z); scene.add(v); }
  }
  // the woods of the deer park on the hill to the east, inside its pale
  for (let i = 0; i < (K.small ? 420 : 900); i++) {
    const x = 175 + R() * 330, z = -520 + R() * 1000;
    if (R() < .2 && Math.abs(z + 20) < 60 && x < 300) continue;   // a clearing where the deer graze
    T.push([x, z, 9 + R() * 7, 3.5 + R() * 2.5]);
  }
  // scattered trees along the river and the hedges
  for (let i = 0; i < 70; i++) { const z = -520 + R() * 1040, x = riverAt(z) + (R() < .5 ? -1 : 1) * (6 + R() * 8); T.push([x, z, 8 + R() * 6, 3 + R() * 2]); }
  for (let i = 0; i < 40; i++) { const x = -260 + R() * 200, z = R() < .5 ? -150 - R() * 300 : 150 + R() * 300; T.push([x, z, 7 + R() * 5, 3 + R() * 2]); }
  trees(T);
  // the park pale: a fence of cleft oak along the foot of the hill
  for (let z = -440; z < 440; z += 12) {
    const x = 162 + Math.sin(z * .01) * 8, x2 = 162 + Math.sin((z + 12) * .01) * 8;
    const y1 = ground(x, z), y2 = ground(x2, z + 12), L = Math.hypot(x2 - x, 12, y2 - y1);
    const p = block(.12, 1.8, L, M.logs, (x + x2) / 2, (y1 + y2) / 2 + .9, z + 6); p.rotation.set(-Math.atan2(y2 - y1, 12), Math.atan2(x2 - x, 12), 0, "YXZ");
  }
  // deer in the clearing
  const deerM = new THREE.MeshStandardMaterial({ color: 0x7a5232, roughness: 1 });
  for (let i = 0; i < 6; i++) {
    const x = 195 + R() * 60, z = -50 + R() * 60, y = ground(x, z), grp = new THREE.Group(); grp.position.set(x, y, z); grp.rotation.y = R() * 6.3; scene.add(grp);
    const b = new THREE.Mesh(new THREE.BoxGeometry(1.2, .5, .4), deerM); b.position.y = 1.05; grp.add(b);
    const n = new THREE.Mesh(new THREE.BoxGeometry(.2, .6, .2), deerM); n.position.set(.6, 1.45, 0); n.rotation.z = -.4; grp.add(n);
    const hd = new THREE.Mesh(new THREE.BoxGeometry(.35, .2, .2), deerM); hd.position.set(.8, 1.75, 0); grp.add(hd);
    [[-.45, -.13], [-.45, .13], [.45, -.13], [.45, .13]].forEach(([a, b2]) => { const l = new THREE.Mesh(new THREE.BoxGeometry(.08, .8, .08), deerM); l.position.set(a, .4, b2); grp.add(l); });
  }
  // the warren: long low pillow mounds where the rabbits were kept
  const turf = new THREE.MeshStandardMaterial({ color: 0x6d8a42, roughness: 1 });
  for (let i = 0; i < 4; i++) { const x = 118 + i * 9, z = 40 + (i % 2) * 7, y = ground(x, z); const m = new THREE.Mesh(new THREE.SphereGeometry(1, 14, 8, 0, Math.PI * 2, 0, Math.PI / 2), turf); m.scale.set(2, .9, 8); m.position.set(x, y - .1, z); m.receiveShadow = true; scene.add(m); }

  // the palisade helper: a ring of upright logs round (cx, cz) at radius r, with gaps [angle, half angle]
  function palisade(cx, cz, r, y0, h, ...gaps) {
    const N = 28;
    for (let i = 0; i < N; i++) {
      const a1 = i / N * Math.PI * 2, a2 = (i + 1) / N * Math.PI * 2, am = (a1 + a2) / 2;
      if (gaps.some(([ga, gw]) => { let d = am - ga; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI; return Math.abs(d) < gw; })) continue;
      wallSeg(cx + Math.cos(a1) * r, cz + Math.sin(a1) * r, cx + Math.cos(a2) * r, cz + Math.sin(a2) * r, h, .3, M.logs, y0);
    }
  }
}

// inside the house on the motte, or the kitchen beside it
const indoor = (x, z) => (Math.abs(x) < HALL.x1 + WING.w && z > WING.z0 && z < WING.z1) || (Math.abs(x - 1.6) < 2.8 && Math.abs(z - 6.9) < 1.9);
// tufts of grass on the banks and in the fields, not in the trodden yard, on the motte top, in the water or on the lane
const grass = (x, z) => { const r = Math.hypot(x, z); if (r < M_R + .5 || baileyEdge(x, z) > 1 || onBridge(x, z) !== null || laneDist(x, z) < 2.8) return false; const [px, pz] = pondLocal(x, z); if (Math.abs(px) < POND.w / 2 + 1 && Math.abs(pz) < POND.d / 2 + 1) return false; return shape(x, z) > WATER + .25 && Math.abs(x - riverAt(z)) > 5; };
// the moat, the fishpond and the river on the plan
function planExtra(c, P, k) {
  c.strokeStyle = "rgba(95,140,160,.9)"; c.lineWidth = MOAT * k * .8; c.beginPath(); const [a, b] = P(0, 0); c.arc(a, b, (M_FOOT + MOAT / 2) * k, 0, 7); c.stroke();
  c.save(); const [pa, pb] = P(POND.x, POND.z); c.translate(pa, pb); c.rotate(-POND.a); c.fillStyle = "rgba(95,140,160,.9)"; c.fillRect(-POND.w / 2 * k, -POND.d / 2 * k, POND.w * k, POND.d * k); c.restore();
  c.strokeStyle = "rgba(95,140,160,.9)"; c.lineWidth = 6 * k; c.beginPath(); for (let z = -200; z <= 200; z += 10) { const [x2, y2] = P(riverAt(z), z); z === -200 ? c.moveTo(x2, y2) : c.lineTo(x2, y2); } c.stroke();
}

export function start(host, D) {
  return run(host, D, {
    STOPS, START, land: LAND, fine: 170, fineAt: [-12, 14], shape, floor, blocked, colour, build, bound: 460, seed: 1403, shadow: 70,
    indoor, grass, grassAt: { x: -10, z: 10, r: 120 }, plan: { x: -12, z: 12, r: 78 }, planExtra, sea: 0, harp: { x: -1, z: -3, r: 9 },
    look: { fog: 0xc4ccc8, fogNear: 50, fogFar: 760, top: 0x8ea4b8, mid: 0xc4cfd3, low: 0xd9ddd6, sun: [-60, 70, 40], sunI: 2.0, hemi: .9, exposure: 1.0 },
  });
}
