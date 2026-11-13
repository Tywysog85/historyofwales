/* The land of the opening screen in 3D: Yr Wyddfa and its horseshoe, built from real height data (see tools/bake_eryri.py),
   and a castle on its crag in front. Bundled with the dragon into src/static/hero3d.js. */
import { mergeGeometries } from "three/addons/utils/BufferGeometryUtils.js";
import * as THREE from "three";
const KM = 10333.4, HN = 512, VE = 1.3; /* the height map covers 10.3 km square; heights are drawn 1.3 times taller */
function readHeights(img) {
  const c = document.createElement("canvas"); c.width = c.height = HN; const g = c.getContext("2d", { willReadFrequently: true }); g.drawImage(img, 0, 0, HN, HN);
  const d = g.getImageData(0, 0, HN, HN).data, h = new Float32Array(HN * HN);
  for (let i = 0; i < h.length; i++) h[i] = (d[i * 4] * 256 + d[i * 4 + 1]) / 56 * VE;
  return h;
}
function heightAt(h, x, z) { /* metres east and south of the map corner */
  const u = Math.min(HN - 1.001, Math.max(0, x / KM * (HN - 1))), v = Math.min(HN - 1.001, Math.max(0, z / KM * (HN - 1)));
  const xi = u | 0, yi = v | 0, fx = u - xi, fy = v - yi, i = yi * HN + xi;
  return (h[i] * (1 - fx) + h[i + 1] * fx) * (1 - fy) + (h[i + HN] * (1 - fx) + h[i + HN + 1] * fx) * fy;
}
const MIST = { value: new THREE.Vector3(0.2, 0.18, 0.24) }; /* the colour of the valley mist as it is painted on screen, set each frame from the sky */
function buildLand(h, colour, normal, detail, rock, rockN) {
  const seg = HN - 1, geo = new THREE.PlaneGeometry(KM, KM, seg, seg); geo.rotateX(-Math.PI / 2); geo.translate(KM / 2, 0, KM / 2);
  const p = geo.attributes.position; /* the hill nearest the eye is levelled into the valley floor: it was too close and too low to read as anything but a blob */
  for (let i = 0; i < p.count; i++) { const k = Math.min(1, Math.max(0, (p.getX(i) / KM - 0.55) / 0.08)), f = k * k * (3 - 2 * k); p.setY(i, h[i] * (1 - f) + Math.min(h[i], 600) * f); }
  geo.deleteAttribute("normal");
  colour.colorSpace = THREE.SRGBColorSpace; colour.anisotropy = normal.anisotropy = 8; colour.flipY = normal.flipY = true;
  const mat = new THREE.MeshStandardMaterial({ map: colour, normalMap: normal, normalMapType: THREE.ObjectSpaceNormalMap, roughness: 0.93, metalness: 0, transparent: true });
  /* fine grain from a photograph of rock, so that the slopes hold up close to */
  detail.wrapS = detail.wrapT = THREE.RepeatWrapping; detail.anisotropy = 8;
  mat.onBeforeCompile = (sh) => {
    sh.uniforms.detail = { value: detail }; sh.uniforms.rockT = { value: rock }; sh.uniforms.rockN = { value: rockN }; sh.uniforms.mist = MIST;
    sh.vertexShader = sh.vertexShader.replace("#include <common>", "varying float vH; varying vec3 vWP;\n#include <common>").replace("#include <begin_vertex>", "#include <begin_vertex>\n vH = position.y; vWP = position;");
    sh.fragmentShader = sh.fragmentShader.replace("uniform float opacity;", "#define CRAG_LO 0.10\n#define CRAG_HI 0.34\n#define CRAG_N 0.9\nuniform float opacity; uniform sampler2D detail, rockT, rockN; uniform vec3 mist; varying float vH; varying vec3 vWP;")
      /* the crags: a photograph of rock laid on the steep ground from the side (not from above, which would smear it down the faces), at two sizes */
      .replace("#include <map_fragment>", `#include <map_fragment>
 float d1 = texture2D(detail, vMapUv * 61.0).g * 2.0, d2 = texture2D(detail, vMapUv * 17.3).g * 2.0; float snowK = smoothstep(0.25, 0.6, diffuseColor.g);
 diffuseColor.rgb *= mix(1.0, d1 * mix(1.0, d2, 0.4), 0.45 * (1.0 - snowK));
 vec3 oN = normalize(texture2D(normalMap, vNormalMapUv).xyz * 2.0 - 1.0); float steep = smoothstep(CRAG_LO, CRAG_HI, 1.0 - oN.y);
 vec2 bw = abs(oN.xz) / (abs(oN.x) + abs(oN.z) + 0.0001); vec2 ux = vWP.zy * vec2(1.0, 1.0 / ${VE.toFixed(2)}), uz = vWP.xy * vec2(1.0, 1.0 / ${VE.toFixed(2)});
 float rl = (texture2D(rockT, ux / 1300.0).g * bw.x + texture2D(rockT, uz / 1300.0).g * bw.y) * 0.6 + (texture2D(rockT, ux / 370.0 + 0.37).g * bw.x + texture2D(rockT, uz / 370.0 + 0.37).g * bw.y) * 0.4;
 diffuseColor.rgb *= mix(1.0, clamp(rl / 0.12, 0.2, 2.2), steep * (1.0 - 0.5 * snowK));`)
      .replace("#include <normal_fragment_maps>", `#include <normal_fragment_maps>
 { vec3 tx = texture2D(rockN, ux / 1300.0).xyz * 2.0 - 1.0 + 0.6 * (texture2D(rockN, ux / 370.0 + 0.37).xyz * 2.0 - 1.0), tz = texture2D(rockN, uz / 1300.0).xyz * 2.0 - 1.0 + 0.6 * (texture2D(rockN, uz / 370.0 + 0.37).xyz * 2.0 - 1.0);
   normal = normalize(normalMatrix * (oN + steep * CRAG_N * (bw.x * vec3(0.0, tx.y, tx.x) + bw.y * vec3(tz.x, tz.y, 0.0)))); }`)
      /* the low ground, the ground near the eye and the outlying spurs melt away, so that the horseshoe rises out of the valley mist */
      .replace("#include <premultiplied_alpha_fragment>", "gl_FragColor.rgb = mix(mist, gl_FragColor.rgb, 0.1 + 0.9 * smoothstep(610.0, 840.0, vH)); gl_FragColor.a *= smoothstep(900.0, 2200.0, length(vViewPosition)) * (1.0 - smoothstep(0.31, 0.44, distance(vMapUv, vec2(0.342, 0.494)))); if (gl_FragColor.a < 0.02) discard;\n#include <premultiplied_alpha_fragment>");
  };
  const g = new THREE.Group(), mesh = new THREE.Mesh(geo, mat); mesh.frustumCulled = false; g.add(mesh);
  return g;
}

/* ---- A castle of the princes on its crag, built in 3D from plain shapes and clad in photographed slate walling. Units are metres. */
const TILE = 7.5; /* one repeat of the wall photograph covers this many metres */
let seed = 11; const rnd = () => ((seed = (seed * 1664525 + 1013904223) >>> 0) / 4294967296);
function uvScale(g, f) { const uv = g.attributes.uv, ox = rnd(), oy = rnd(); for (let i = 0; i < uv.count; i++) { const s = f(i); uv.setXY(i, uv.getX(i) * s[0] + ox, uv.getY(i) * s[1] + oy); } return g; }
function box(w, h, d, x, y, z, ry) {
  const g = new THREE.BoxGeometry(w, h, d);
  uvScale(g, (i) => { const f = (i / 4) | 0; return f < 2 ? [d / TILE, h / TILE] : f < 4 ? [w / TILE, d / TILE] : [w / TILE, h / TILE]; });
  if (ry) g.rotateY(ry); g.translate(x, y + h / 2, z); return g;
}
function drum(r, h, x, y, z, rb) {
  const g = new THREE.CylinderGeometry(r, rb || r, h, 36, Math.max(1, Math.round(h / 3)), true, Math.PI);
  uvScale(g, () => [Math.max(1, Math.round(2 * Math.PI * r / TILE)), h / TILE]); g.translate(x, y + h / 2, z); return g;
}
function disc(r, x, y, z) { const g = new THREE.CircleGeometry(r, 36); g.rotateX(-Math.PI / 2); uvScale(g, () => [2 * r / TILE, 2 * r / TILE]); g.translate(x, y, z); return g; }
/* battlements along a straight run */
function crenel(out, x1, z1, x2, z2, y, th) {
  const L = Math.hypot(x2 - x1, z2 - z1), a = Math.atan2(-(z2 - z1), x2 - x1), n = Math.max(1, Math.round(L / 2.3)), step = L / n;
  for (let i = 0; i < n; i++) { const k = (i + 0.5) / n; out.push(box(step * 0.56, 1.25, th, x1 + (x2 - x1) * k, y, z1 + (z2 - z1) * k, a)); }
}
function tower(out, x, z, r, h, o) {
  o = o || {};
  out.push(drum(r, h, x, 0, z));
  out.push(drum(r, 3.2, x, -0.2, z, r * 1.22)); /* the spreading foot */
  out.push(drum(r * 1.07, 0.55, x, h - 0.2, z), drum(r * 1.07, 1.0, x, h + 0.35, z)); /* corbelled parapet */
  out.push(disc(r * 1.07, x, h + 0.36, z));
  const n = Math.max(6, Math.round(2 * Math.PI * r / 2.2));
  for (let i = 0; i < n; i++) { const a = (i / n) * Math.PI * 2 + (o.turn || 0); out.push(box(2 * Math.PI * r * 1.07 / n * 0.56, 1.2, 0.5, x + Math.sin(a) * r * 1.04, h + 1.35, z + Math.cos(a) * r * 1.04, a)); }
  if (o.band) out.push(drum(r * 1.025, 0.35, x, h * o.band, z));
}
function wall(out, x1, z1, x2, z2, h, th) {
  const L = Math.hypot(x2 - x1, z2 - z1), a = Math.atan2(-(z2 - z1), x2 - x1), mx = (x1 + x2) / 2, mz = (z1 + z2) / 2;
  out.push(box(L, h, th, mx, 0, mz, a), box(L, 0.4, th + 0.5, mx, h - 0.2, mz, a), box(L, 0.9, th + 0.5, mx, h + 0.2, mz, a));
  const nx = Math.sin(a) * (th / 2 + 0.0), nz = Math.cos(a) * (th / 2 + 0.0);
  crenel(out, x1 + nx, z1 + nz, x2 + nx, z2 + nz, h + 1.1, 0.5);
}
function glowTex() { const c = document.createElement("canvas"); c.width = c.height = 128; const g = c.getContext("2d"), r = g.createRadialGradient(64, 64, 0, 64, 64, 64); r.addColorStop(0, "rgba(255,190,110,1)"); r.addColorStop(0.25, "rgba(255,150,70,.45)"); r.addColorStop(1, "rgba(255,120,40,0)"); g.fillStyle = r; g.fillRect(0, 0, 128, 128); return new THREE.CanvasTexture(c); }
function slitTex(lit) {
  const c = document.createElement("canvas"); c.width = 32; c.height = 96; const g = c.getContext("2d");
  g.fillStyle = "#000"; g.fillRect(0, 0, 32, 96);
  if (lit) { const r = g.createLinearGradient(0, 0, 0, 96); r.addColorStop(0, "#fff1c4"); r.addColorStop(0.6, "#ffc46a"); r.addColorStop(1, "#f08a2e"); g.fillStyle = r; } else g.fillStyle = "#020304";
  g.beginPath(); g.moveTo(5, 96); g.lineTo(5, 26); g.quadraticCurveTo(5, 6, 16, 2); g.quadraticCurveTo(27, 6, 27, 26); g.lineTo(27, 96); g.closePath(); g.fill();
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}
function gateTex() {
  const c = document.createElement("canvas"); c.width = 128; c.height = 192; const g = c.getContext("2d");
  const r = g.createRadialGradient(64, 150, 4, 64, 130, 150); r.addColorStop(0, "#ffd58a"); r.addColorStop(0.35, "#e8853a"); r.addColorStop(1, "#3a1508"); g.fillStyle = r; g.fillRect(0, 0, 128, 192);
  g.fillStyle = "#0a0503"; for (let i = 1; i < 6; i++) g.fillRect(i * 128 / 6 - 3, 0, 6, 192); for (let j = 0; j < 6; j++) g.fillRect(0, 14 + j * 30, 128, 5);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}
function buildCastle(tex) {
  const g = new THREE.Group(), out = [], lights = [], glows = [];
  /* the great keep with its stair turret, the corner towers, the walls between them, and the twin-towered gatehouse */
  out.push(box(13, 25, 11, -7, 0, -9)); out.push(box(13.6, 0.5, 11.6, -7, 24.6, -9), box(13.6, 0.9, 11.6, -7, 25.1, -9), box(13.2, 0.4, 11.2, -7, 14, -9));
  crenel(out, -13.6, -3.3, -0.4, -3.3, 26, 0.5); crenel(out, -0.3, -3.4, -0.3, -14.6, 26, 0.5); crenel(out, -13.7, -3.4, -13.7, -14.6, 26, 0.5); crenel(out, -13.6, -14.7, -0.4, -14.7, 26, 0.5);
  tower(out, -13.5, -14.5, 2.5, 32, { band: 0.8 });
  tower(out, -21, 8, 4.3, 17.5, { band: 0.62 }); tower(out, 21.5, 7, 4.3, 16.5, { band: 0.62 }); tower(out, 18, -13, 3.7, 21, { band: 0.7 }); tower(out, -20, -13, 3.4, 15);
  tower(out, 3.2, 10.5, 3.1, 14.5, { band: 0.66 }); tower(out, 11.8, 10.5, 3.1, 14.5, { band: 0.66 });
  wall(out, -21, 8.4, 3.2, 9.6, 10.5, 2); wall(out, 11.8, 9.6, 21.5, 7.4, 10.5, 2); wall(out, 21.6, 7, 18.2, -13, 10.5, 2); wall(out, -21.2, 8, -20.2, -13, 10.5, 2); wall(out, -20, -13.2, 18, -13.4, 9, 2);
  /* gate passage: the wall above the arch, and the stone ring of the arch itself */
  out.push(box(6, 6.6, 3.4, 7.5, 5.4, 10.2), box(6, 0.4, 3.9, 7.5, 11.8, 10.2), box(6, 0.9, 3.9, 7.5, 12.2, 10.2), box(1.6, 5.6, 3.4, 5.3, 0, 10.2), box(1.6, 5.6, 3.4, 9.7, 0, 10.2));
  crenel(out, 4.7, 12, 10.3, 12, 13.1, 0.5);
  const geo = mergeGeometries(out.map((q) => q.index ? q.toNonIndexed() : q), false);
  /* weathering: darker and damper towards the foot, streaked and blotched all over */
  const p = geo.attributes.position, col = new Float32Array(p.count * 3);
  for (let i = 0; i < p.count; i++) {
    const x = p.getX(i), y = p.getY(i), z = p.getZ(i), n = 0.5 + 0.25 * Math.sin(x * 0.9 + z * 1.3) * Math.sin(y * 0.55 + x * 0.3) + 0.25 * Math.sin(x * 0.23 - z * 0.31 + y * 0.17);
    const k = (0.62 + 0.38 * Math.min(1, Math.max(0, y / 7))) * (0.82 + 0.3 * n), moss = Math.max(0, 1 - y / 4) * 0.25;
    col[i * 3] = k * (1 - moss * 0.5); col[i * 3 + 1] = k * (1 - moss * 0.1); col[i * 3 + 2] = k * (1 - moss * 0.6);
  }
  geo.setAttribute("color", new THREE.BufferAttribute(col, 3));
  [tex.stone, tex.stoneN].forEach((t) => { t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = 8; }); tex.stone.colorSpace = THREE.SRGBColorSpace;
  const stone = new THREE.MeshStandardMaterial({ map: tex.stone, normalMap: tex.stoneN, normalScale: new THREE.Vector2(1.6, 1.6), roughness: 0.9, metalness: 0, vertexColors: true, side: THREE.DoubleSide });
  const body = new THREE.Mesh(geo, stone); body.castShadow = body.receiveShadow = true; g.add(body);
  /* windows: arrow loops, some with firelight behind them */
  const litM = new THREE.MeshBasicMaterial({ map: slitTex(true), toneMapped: false }), darkM = new THREE.MeshBasicMaterial({ map: slitTex(false) }), glowT = glowTex();
  const glowM = new THREE.SpriteMaterial({ map: glowT, blending: THREE.AdditiveBlending, depthWrite: false, transparent: true, opacity: 0.4, fog: false });
  const slit = (x, y, z, ry, lit, s) => {
    const m = new THREE.Mesh(new THREE.PlaneGeometry(0.62 * (s || 1), 1.9 * (s || 1)), lit ? litM : darkM); m.position.set(x, y, z); m.rotation.y = ry; g.add(m);
    if (lit) { const sp = new THREE.Sprite(glowM); sp.position.set(x + Math.sin(ry) * 0.6, y, z + Math.cos(ry) * 0.6); sp.scale.setScalar(6.5 * (s || 1)); g.add(sp); glows.push(sp); }
  };
  const onDrum = (cx, cz, r, a, y, lit, s) => slit(cx + Math.sin(a) * (r + 0.04), y, cz + Math.cos(a) * (r + 0.04), a, lit, s);
  onDrum(-21, 8, 4.3, 0.25, 11.5, true); onDrum(-21, 8, 4.3, -0.5, 6.5, false); onDrum(21.5, 7, 4.3, 0.1, 10.5, true); onDrum(21.5, 7, 4.3, 0.75, 5.8, false);
  onDrum(18, -13, 3.7, 0.3, 17, true); onDrum(3.2, 10.5, 3.1, -0.25, 9.5, false); onDrum(11.8, 10.5, 3.1, 0.3, 9.5, true); onDrum(-13.5, -14.5, 2.5, 0.2, 28.5, true, 0.85);
  slit(-9.5, 19.5, -3.46, 0, true, 1.25); slit(-4.2, 19.5, -3.46, 0, false, 1.25); slit(-7, 9.5, -3.46, 0, true, 1.1); slit(-0.46, 17, -8, Math.PI / 2, true, 1.1); slit(-10, 7, 9.05, 0.05, false); slit(-14.5, 7, 8.8, 0.05, false); slit(16.5, 7, 8.9, -0.2, false);
  /* the gate: firelight behind the portcullis */
  const sh = new THREE.Shape(); sh.moveTo(-1.4, 0); sh.lineTo(-1.4, 3.6); sh.absarc(0, 3.6, 1.4, Math.PI, 0, true); sh.lineTo(1.4, 0); sh.closePath();
  const gt = gateTex(), gg = new THREE.ShapeGeometry(sh, 16), uv = gg.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, (uv.getX(i) + 1.4) / 2.8, uv.getY(i) / 5);
  const gate = new THREE.Mesh(gg, new THREE.MeshBasicMaterial({ map: gt, toneMapped: false })); gate.position.set(7.5, 0, 11.3); g.add(gate);
  out.length = 0;
  const gs = new THREE.Sprite(glowM.clone()); gs.material.opacity = 0.8; gs.position.set(7.5, 2.4, 13); gs.scale.setScalar(15); g.add(gs); glows.push(gs);
  const fire = new THREE.PointLight(0xff9a4a, 260, 34, 2); fire.position.set(7.5, 2.6, 15.5); g.add(fire); lights.push(fire);
  const f2 = new THREE.PointLight(0xffb060, 60, 16, 2); f2.position.set(-8, 19, -1.5); g.add(f2); lights.push(f2);
  /* the flag of Wales on the stair turret */
  const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.11, 0.14, 11, 8), new THREE.MeshStandardMaterial({ color: 0x8a8f9c, roughness: 0.5, metalness: 0.6 })); pole.position.set(-13.5, 33.2 + 5.5, -14.5); g.add(pole);
  const knob = new THREE.Mesh(new THREE.SphereGeometry(0.3, 12, 8), new THREE.MeshStandardMaterial({ color: 0xd9b24a, roughness: 0.35, metalness: 0.9, emissive: 0x2a1c05 })); knob.position.set(-13.5, 44.9, -14.5); g.add(knob);
  const FW = 9.4, FH = 5.64, fg = new THREE.PlaneGeometry(FW, FH, 28, 12); fg.translate(FW / 2, 0, 0);
  const flagTex = new THREE.CanvasTexture(tex.flag); flagTex.colorSpace = THREE.SRGBColorSpace; flagTex.anisotropy = 8;
  const flag = new THREE.Mesh(fg, new THREE.MeshStandardMaterial({ map: flagTex, side: THREE.DoubleSide, roughness: 0.85, emissive: 0xffffff, emissiveMap: flagTex, emissiveIntensity: 0.16 }));
  flag.position.set(-13.4, 44.5 - FH / 2 - 0.2, -14.5); flag.castShadow = false; g.add(flag);
  const rest = fg.attributes.position.array.slice();
  const wave = (t) => {
    const a = fg.attributes.position.array;
    for (let i = 0; i < a.length; i += 3) {
      const x = rest[i], y = rest[i + 1], k = x / FW, ph = x * 1.25 - t * 5.2 + y * 0.35;
      a[i + 2] = (Math.sin(ph) * 0.42 + Math.sin(ph * 0.47 + 1.3 + t * 1.1) * 0.3) * (0.15 + 0.85 * k);
      a[i] = x - 0.5 * k * k * (1 + 0.3 * Math.sin(t * 0.9)); a[i + 1] = y - 0.55 * k * k + Math.sin(ph * 0.8) * 0.12 * k;
    }
    fg.attributes.position.needsUpdate = true; fg.computeVertexNormals();
  };
  wave(0);
  /* the crag */
  const prof = [[0.01, 0.5], [22, 0.4], [28, 0], [31, -2.5], [33.5, -9], [37, -19], [43, -31], [52, -44], [66, -56], [90, -66], [130, -72]].map((q) => new THREE.Vector2(q[0], q[1]));
  const cg = new THREE.LatheGeometry(new THREE.SplineCurve(prof).getPoints(40), 96), cp = cg.attributes.position, cc = new Float32Array(cp.count * 3);
  const nz = (a, y) => Math.sin(a * 3 + 1) * 0.5 + Math.sin(a * 7 + y * 0.21) * 0.28 + Math.sin(a * 13 - y * 0.4 + 2) * 0.16 + Math.sin(a * 29 + y * 0.9) * 0.07;
  for (let i = 0; i < cp.count; i++) {
    const x = cp.getX(i), y = cp.getY(i), z = cp.getZ(i), r = Math.hypot(x, z), a = Math.atan2(x, z), d = Math.min(1, Math.max(0, (-y) / 12)), k = 1 + nz(a, y) * 0.2 * d + (r > 27 ? 0.04 * Math.sin(a * 5) : 0);
    cp.setXYZ(i, x * k, y + nz(a + 2, y * 1.7) * 2.4 * d, z * k);
    const m = 1 - d, sh2 = 0.55 + 0.25 * nz(a * 2, y);
    cc[i * 3] = sh2 * (1 - 0.35 * m); cc[i * 3 + 1] = sh2 * (1 - 0.1 * m); cc[i * 3 + 2] = sh2 * (1 - 0.45 * m);
  }
  cg.setAttribute("color", new THREE.BufferAttribute(cc, 3)); { const ix = cg.index.array; for (let i = 0; i < ix.length; i += 3) { const q = ix[i]; ix[i] = ix[i + 1]; ix[i + 1] = q; } } cg.computeVertexNormals();
  const cuv = cg.attributes.uv; for (let i = 0; i < cuv.count; i++) cuv.setXY(i, cuv.getX(i) * 14, cuv.getY(i) * 7);
  [tex.rock, tex.rockN].forEach((t) => { t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = 8; }); tex.rock.colorSpace = THREE.SRGBColorSpace;
  const crag = new THREE.Mesh(cg, new THREE.MeshStandardMaterial({ map: tex.rock, normalMap: tex.rockN, normalScale: new THREE.Vector2(2, 2), roughness: 0.95, vertexColors: true, color: new THREE.Color(2.6, 2.6, 2.6), side: THREE.DoubleSide })); crag.receiveShadow = true; crag.castShadow = true; g.add(crag);
  return { group: g, wave, lights, glows, flagTex, litM, gate };
}

/* ---- The moor between the eye and the mountains: rolling ground clad in a photograph of mossy rock, fading into the valley mist. ---- */
function buildMoor(tex) {
  const X0 = -4300, X1 = 900, Z0 = -3300, Z1 = 60, geo = new THREE.PlaneGeometry(X1 - X0, Z1 - Z0, 220, 150); geo.rotateX(-Math.PI / 2); geo.translate((X0 + X1) / 2, 0, (Z0 + Z1) / 2);
  const p = geo.attributes.position, uv = geo.attributes.uv, col = new Float32Array(p.count * 3);
  const hill = (x, z) => Math.sin(x * 0.0031 + 1.2) * Math.sin(z * 0.0043 + 0.4) * 30 + Math.sin(x * 0.0083 + z * 0.0051) * 13 + Math.sin(x * 0.019 - z * 0.013 + 2) * 5 + Math.sin(x * 0.047 + 1) * Math.sin(z * 0.039) * 2.2;
  for (let i = 0; i < p.count; i++) {
    const x = p.getX(i), z = p.getZ(i), far = Math.min(1, -z / 3000), y = -58 + hill(x, z) * (0.45 + 0.9 * far) + far * 60 + far * far * 80;
    p.setY(i, y); uv.setXY(i, x / 64, z / 64);
    const n = 0.5 + 0.5 * Math.sin(x * 0.011 + z * 0.017) * Math.sin(x * 0.004 - z * 0.006 + 1), k = 0.75 + 0.4 * n;
    col[i * 3] = k * (1 + 0.25 * n); col[i * 3 + 1] = k; col[i * 3 + 2] = k * (0.95 - 0.2 * n);
  }
  geo.setAttribute("color", new THREE.BufferAttribute(col, 3)); geo.computeVertexNormals();
  const mat = new THREE.MeshStandardMaterial({ map: tex.rock, normalMap: tex.rockN, normalScale: new THREE.Vector2(1.5, 1.5), roughness: 0.96, vertexColors: true, color: new THREE.Color(2.1, 2.1, 2.1), transparent: true });
  mat.onBeforeCompile = (sh) => {
    sh.fragmentShader = sh.fragmentShader.replace("#include <map_fragment>", "#include <map_fragment>\n vec2 ru = mat2(0.766, 0.643, -0.643, 0.766) * vMapUv; diffuseColor.rgb = mix(diffuseColor.rgb, texture2D(map, ru * 0.31 + 0.17).rgb * vColor.rgb * diffuse, 0.5) * (0.5 + 1.0 * texture2D(map, ru * 0.047 + 0.31).g / 0.2);")
      .replace("#include <premultiplied_alpha_fragment>", "gl_FragColor.a *= 1.0 - smoothstep(1400.0, 2700.0, length(vViewPosition)); if (gl_FragColor.a < 0.02) discard;\n#include <premultiplied_alpha_fragment>");
  };
  const m = new THREE.Mesh(geo, mat); m.receiveShadow = false; return m;
}

/* ---- Drawing it: the mountain first, then the castle in front, on a see-through canvas between the painted sky and the dragon.
   src/app.js says where the summit and the castle belong each frame and calls HCL3.frame(). Only the flag moves, so after a full
   picture only the small patch around the flag is drawn again. ---- */
const api = (window.HCL3 = window.HCL3 || {});
const canvas = document.getElementById("land3d");
function fail() { window.HCL3_WANT = 0; api.ready = false; if (canvas) canvas.remove(); }
try {
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true, preserveDrawingBuffer: true });
  renderer.autoClear = false; renderer.setClearColor(0x000000, 0); renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.3;
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap; renderer.shadowMap.autoUpdate = false;
  const L = new THREE.TextureLoader(), ld = (u) => new Promise((ok, no) => L.load(u, ok, undefined, no));
  /* the mountain */
  const land = new THREE.Scene(), camL = new THREE.PerspectiveCamera(30, 1, 20, 30000);
  land.fog = new THREE.FogExp2(0x2a2536, 0.0001);
  const hemiL = new THREE.HemisphereLight(0x5a6a9a, 0x10121a, 0.55), moonL = new THREE.DirectionalLight(0xb8c8ff, 2.2); moonL.position.set(-0.445, 0.35, -0.82); land.add(hemiL, moonL);
  const SUMMIT = new THREE.Vector3(3536, 1150, 5224), EYE = [9760, 3790]; /* looking at the summit from the Capel Curig side */
  /* the castle */
  const fort = new THREE.Scene(), camF = new THREE.PerspectiveCamera(20, 1, 5, 3000), FD = 190;
  fort.fog = new THREE.Fog(0x1c1d2c, 160, 2600);
  const hemiF = new THREE.HemisphereLight(0x6272a8, 0x0c0e16, 0.5), moonF = new THREE.DirectionalLight(0xbfcfff, 1.9); moonF.position.set(70, 60, 25);
  moonF.castShadow = true; moonF.shadow.mapSize.set(2048, 2048); Object.assign(moonF.shadow.camera, { left: -60, right: 60, top: 60, bottom: -60, near: 1, far: 300 }); moonF.shadow.bias = -0.0006; moonF.shadow.normalBias = 0.05;
  fort.add(hemiF, moonF); camF.position.set(0, -4, FD); camF.lookAt(0, 14, 0);
  let castle = null, wantCastle = false, W = 0, H = 0, key = "", flagV = -1;
  const cA = new THREE.Color(), cB = new THREE.Color(), v = new THREE.Vector3();
  const img = new Image();
  /* phones, and screens no more than 1600 real pixels wide, get half-size castle stone pictures (the same look there, 250 KB less).
     Sharp wide screens keep the full-size stone: half-size softens the mortar lines at 2x. The mountain pictures stay full size on every screen:
     half-size colour dims the snow and half-size relief loses the gullies (side-by-side renders, 13 November 2026). */
  const SM = Math.min(screen.width, screen.height) <= 600 || screen.width * (window.devicePixelRatio || 1) <= 1600 ? "-m" : "";
  let rockT = null;
  img.onload = () => Promise.all(["eryri-c.webp", "eryri-n.webp", "detail.webp", "rock.webp", "rock-n.webp"].map(ld)).then((t) => {
    [t[3], t[4]].forEach((q) => { q.wrapS = q.wrapT = THREE.RepeatWrapping; q.anisotropy = 8; }); t[3].colorSpace = THREE.SRGBColorSpace;
    const h = readHeights(img); land.add(buildLand(h, t[0], t[1], t[2], t[3], t[4])); rockT = { rock: t[3], rockN: t[4] }; fort.add(buildMoor(rockT));
    camL.position.set(EYE[0], heightAt(h, EYE[0], EYE[1]) + 40, EYE[1]); camL.lookAt(SUMMIT); camL.updateMatrixWorld(true);
    api.ready = true; window.dispatchEvent(new Event("hcl3"));
  }).catch(fail);
  img.onerror = fail; img.src = "eryri-h.webp"; /* lossless WebP: heights in red and green, roughness in blue, all must come back exact */
  /* the castle's stone is fetched straight away, and nothing is shown until the castle stands, so the scene arrives whole */
  let noCastle = false; const stoneP = true ? Promise.all(["stone" + SM + ".webp", "stone-n" + SM + ".webp"].map(ld)) : null; if (stoneP) stoneP.catch(() => {});
  function loadCastle(flag) {
    wantCastle = true;
    (stoneP || Promise.all(["stone" + SM + ".webp", "stone-n" + SM + ".webp"].map(ld))).then((t) => {
      castle = buildCastle({ stone: t[0], stoneN: t[1], rock: rockT.rock, rockN: rockT.rockN, flag }); castle.group.rotation.y = 0.42; fort.add(castle.group);
      castle.base = castle.lights.map((l) => l.intensity); renderer.shadowMap.needsUpdate = true; key = "";
    }).catch(() => { noCastle = true; });
  }
  function place(cam, D, ppm, x, y) { /* put the point the camera looks at on pixel (x, y), at ppm pixels to the metre */
    const Hf = 2 * Math.tan(cam.fov * Math.PI / 360) * D * ppm, Wf = Hf * W / H;
    cam.aspect = W / H; cam.setViewOffset(Wf, Hf, Wf / 2 - x, Hf / 2 - y, W, H); cam.updateProjectionMatrix();
  }
  /* st: W, H, sumX, sumY (where the summit goes), ppm (pixels to the metre at the summit), ground {x, y, ppm} (where the foot of the castle goes), castle (true to show it),
     t (ms), sun (0..1), fog (colour of the haze), flag (the flag painted on a canvas), flagV (goes up when that painting changes) */
  api.frame = function (st) {
    if (!api.ready) return;
    if (st.W !== W || st.H !== H) { W = st.W; H = st.H; renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, W < 700 ? 1.5 : 2)); renderer.setSize(W, H, false); key = ""; }
    if (st.castle && !wantCastle) loadCastle(st.flag);
    if (st.castle && !castle && !noCastle) return;
    const c = castle && st.castle, tt = st.t / 1000; if (castle) castle.group.visible = !!c;
    if (c && st.flagV !== flagV) { flagV = st.flagV; castle.flagTex.needsUpdate = true; key = ""; }
    const k = [st.sumX, st.sumY, st.ppm * 1000, st.sun, st.fog, st.mist, st.ground.x, st.ground.y, st.ground.ppm * 1000, c ? 1 : 0].map((q) => typeof q === "number" ? q.toFixed(1) : q).join("|");
    const full = k !== key; key = k;
    if (!full && !c) return;
    if (full) {
      const sun = st.sun || 0;
      { const m = cA.set(st.mist || st.fog); MIST.value.set(Math.pow(m.r, 1 / 2.2), Math.pow(m.g, 1 / 2.2), Math.pow(m.b, 1 / 2.2)); }
      land.fog.color.set(st.fog); fort.fog.color.set(st.fog).multiplyScalar(0.8);
      hemiL.intensity = 0.4 + 0.25 * sun; moonL.intensity = 1.7 + 0.45 * sun; moonL.color.copy(cA.set(0xc4cdea)).lerp(cB.set(0xffe6c4), sun);
      hemiL.color.copy(cA.set(0x5a6a9a)).lerp(cB.set(0xa9c4ee), sun);
      hemiF.intensity = 0.5 + 0.7 * sun; moonF.intensity = 1.9 + 1.3 * sun; moonF.color.copy(cA.set(0xbfcfff)).lerp(cB.set(0xffe9cc), sun);
      place(camL, camL.position.distanceTo(SUMMIT), st.ppm, st.sumX, st.sumY);
      place(camF, Math.hypot(FD, 18), st.ground.ppm, st.ground.x, st.ground.y - 14 * st.ground.ppm);
      if (c) { castle.lights.forEach((l, i) => { l.intensity = castle.base[i] * (1 - 0.7 * sun); }); castle.glows.forEach((g) => { g.material.opacity = 0.4 * (1 - 0.7 * sun); }); }
      renderer.setScissorTest(false);
    } else {
      /* only the flag has moved: draw again just the patch of screen it flies in */
      let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
      for (let i = 0; i < 8; i++) { v.set(i & 1 ? -15 : -2.5, i & 2 ? 37.5 : 46, -14.5 + (i & 4 ? 2 : -2)).applyMatrix4(castle.group.matrixWorld).project(camF); const px = (v.x * 0.5 + 0.5) * W, py = (v.y * 0.5 + 0.5) * H; x0 = Math.min(x0, px); x1 = Math.max(x1, px); y0 = Math.min(y0, py); y1 = Math.max(y1, py); }
      x0 = Math.floor(x0) - 4; y0 = Math.floor(y0) - 4; x1 = Math.ceil(x1) + 4; y1 = Math.ceil(y1) + 4;
      if (x1 < 0 || y1 < 0 || x0 > W || y0 > H) return;
      renderer.setScissor(x0, y0, x1 - x0, y1 - y0); renderer.setScissorTest(true);
    }
    if (c) castle.wave(tt);
    renderer.clear(); renderer.render(land, camL);
    renderer.clearDepth(); renderer.render(fort, camF);
    if (full && !api.shown) { api.shown = true; canvas.style.opacity = 1; }
  };
  canvas.addEventListener("webglcontextlost", fail);
} catch (e) { fail(); }
