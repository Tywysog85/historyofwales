/* The lifelike dragon of the opening screen: a rigged 3D model that beats its wings, drawn on its own see-through canvas
   above the painted sky. src/app.js decides where the dragon is each frame and calls HCD3.frame(). */
import { WebGLRenderer, Scene, OrthographicCamera, HemisphereLight, DirectionalLight, PointLight, AnimationMixer, Vector3, Group, Box3, SRGBColorSpace, ACESFilmicToneMapping, Color } from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";

const api = (window.HCD3 = window.HCD3 || {});
const canvas = document.getElementById("sky3d");
function fail() { window.HCD3_WANT = 0; if (canvas) canvas.remove(); }
try {
  const renderer = new WebGLRenderer({ canvas, alpha: true, antialias: true, powerPreference: "low-power", preserveDrawingBuffer: !!window.HCD3_KEEP });
  renderer.outputColorSpace = SRGBColorSpace; renderer.toneMapping = ACESFilmicToneMapping; renderer.toneMappingExposure = 1.45;
  const scene = new Scene(), cam = new OrthographicCamera(0, 1, 1, 0, -4000, 4000);
  const hemi = new HemisphereLight(0xb9c8ff, 0x6a2420, 1.5), moon = new DirectionalLight(0xfff1e0, 3.2), rim = new DirectionalLight(0xff5a3c, 2.4), fireL = new PointLight(0xffa040, 0, 0, 0);
  moon.position.set(0.7, 0.9, 0.8); rim.position.set(-0.8, -0.2, -0.7); scene.add(hemi, moon, rim, fireL);
  const rig = new Group(); scene.add(rig);
  let mixer = null, dur = 1, head = null, snout = null, neck = null, span = 1, W = 0, H = 0;
  const v1 = new Vector3(), v2 = new Vector3();
  new GLTFLoader().load("dragon.glb", (g) => {
    const m = g.scene; mixer = new AnimationMixer(m); const clip = g.animations[0]; dur = clip.duration; mixer.clipAction(clip).play();
    m.traverse((o) => { o.frustumCulled = false; if (o.isMesh) { o.material.color = new Color(1.7, 0.95, 0.9); o.material.emissive = new Color(0x2a0503); o.material.roughness = Math.min(o.material.roughness, 0.75); } if (o.isBone && /^head/.test(o.name)) head = o; if (o.isBone && /^jaw_02/.test(o.name)) snout = o; if (o.isBone && /^neck_09/.test(o.name)) neck = o; });
    /* centre the model on its chest and measure it, so that app.js can size it in pixels */
    let chest = null; m.traverse((o) => { if (o.isBone && /^spine_05/.test(o.name)) chest = o; });
    const box = new Box3(); [0.1, 0.35, 0.6, 0.85].forEach((k) => { mixer.setTime(dur * k); m.updateMatrixWorld(true); m.traverse((o) => { if (o.isBone) box.expandByPoint(o.getWorldPosition(v1)); }); });
    mixer.setTime(0); m.updateMatrixWorld(true); const c = chest ? chest.getWorldPosition(v1).clone() : box.getCenter(v1).clone();
    m.position.sub(c); span = box.getSize(v2).x || 1; rig.add(m); api.ready = true; window.dispatchEvent(new Event("hcd3"));
  }, undefined, fail);
  /* st: W, H (hero size in CSS pixels), x, y (centre of the dragon), size (wingspan in pixels), alpha, t (ms), turn, fire (0..1), day (0..1) */
  api.frame = function (st) {
    if (!api.ready) return null;
    if (st.W !== W || st.H !== H) { W = st.W; H = st.H; renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2)); renderer.setSize(W, H, false); cam.right = W; cam.top = H; cam.updateProjectionMatrix(); }
    const s = st.size / span, tt = st.t / 1000;
    mixer.setTime(tt % dur);
    rig.position.set(st.x, H - st.y, 0); rig.scale.setScalar(s);
    rig.rotation.set(0.12 + 0.05 * Math.sin(tt * 0.7), (st.turn == null ? 1.05 : st.turn) + 0.12 * Math.sin(tt * 0.4), 0.06 * Math.sin(tt * 0.9));
    hemi.intensity = 1.5 + 1.6 * (st.day || 0); moon.intensity = 3.2 + 1.5 * (st.day || 0);
    canvas.style.opacity = st.alpha;
    rig.updateMatrixWorld(true);
    let out = null;
    if (head && snout && neck) {
      /* the mouth is at the end of the jaw; the fire leaves along the line of the neck and head */
      neck.getWorldPosition(v1); head.getWorldPosition(v2); const dx = v2.x - v1.x, dy = v2.y - v1.y;
      snout.getWorldPosition(v2);
      fireL.position.set(v2.x + dx, v2.y + dy, v2.z + 200); fireL.intensity = (st.fire || 0) * 5;
      out = { x: v2.x, y: H - v2.y, a: Math.atan2(-dy, dx) };
    }
    renderer.render(scene, cam);
    return out;
  };
  canvas.addEventListener("webglcontextlost", fail);
} catch (e) { fail(); }
