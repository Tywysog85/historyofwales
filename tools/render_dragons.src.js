/* Draws still pictures of the 3D dragon (src/static/dragon.glb) for the legend pages: a red one and a white one.
   Bundle with esbuild, open tools/render_dragons.html beside dragon.glb in headless Chromium and screenshot the canvas
   with a see-through background. See SKILLS.md, "Dragon pictures for the legend pages". Query: ?white=1&t=0.3&turn=1.0&tilt=0.1&exp=1.9 */
import { WebGLRenderer, Scene, OrthographicCamera, HemisphereLight, DirectionalLight, AnimationMixer, Vector3, Box3, SRGBColorSpace, ACESFilmicToneMapping, Color } from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
const q = new URLSearchParams(location.search), white = q.get("white") === "1", W = 1200, H = 900;
const canvas = document.getElementById("c"); canvas.width = W; canvas.height = H;
const renderer = new WebGLRenderer({ canvas, alpha: true, antialias: true, preserveDrawingBuffer: true });
renderer.setClearColor(0x000000, 0); renderer.outputColorSpace = SRGBColorSpace; renderer.toneMapping = ACESFilmicToneMapping; renderer.toneMappingExposure = +q.get("exp") || (white ? 1.25 : 1.9);
const scene = new Scene(), cam = new OrthographicCamera(-W / 2, W / 2, H / 2, -H / 2, -4000, 4000);
const hemi = new HemisphereLight(0xb9c8ff, white ? 0x30364a : 0x6a2420, 1.5), moon = new DirectionalLight(0xfff1e0, 3.2), rim = new DirectionalLight(white ? 0xb4c2f0 : 0xff5a3c, white ? 1.1 : 2.4);
moon.position.set(0.7, 0.9, 0.8); rim.position.set(-0.8, -0.2, -0.7); scene.add(hemi, moon, rim);
new GLTFLoader().load("dragon.glb", (g) => {
  const m = g.scene, mixer = new AnimationMixer(m), clip = g.animations[0]; mixer.clipAction(clip).play();
  m.traverse((o) => {
    o.frustumCulled = false;
    if (o.isMesh) {
      o.material.roughness = Math.min(o.material.roughness, 0.75);
      if (white) { /* the same beast in white: the red is taken out of the skin and the scales keep their light and dark */
        o.material.color = new Color(1, 1, 1); o.material.emissive = new Color(0x05060a);
        o.material.onBeforeCompile = (sh) => { sh.fragmentShader = sh.fragmentShader.replace("#include <map_fragment>", "#include <map_fragment>\n float lum = dot(diffuseColor.rgb, vec3(0.5, 0.4, 0.1)); diffuseColor.rgb = pow(lum, 0.6) * vec3(1.5, 1.47, 1.4);"); };
      } else { o.material.color = new Color(1.7, 0.95, 0.9); o.material.emissive = new Color(0x2a0503); }
    }
  });
  const v = new Vector3(), box = new Box3(); let chest = null; m.traverse((o) => { if (o.isBone && /^spine_05/.test(o.name)) chest = o; });
  [0.1, 0.35, 0.6, 0.85].forEach((k) => { mixer.setTime(clip.duration * k); m.updateMatrixWorld(true); m.traverse((o) => { if (o.isBone) box.expandByPoint(o.getWorldPosition(v)); }); });
  mixer.setTime(0); m.updateMatrixWorld(true); m.position.sub(chest.getWorldPosition(v).clone());
  const span = box.getSize(v).x; scene.add(m); const rig = new (m.constructor)(); scene.remove(m); rig.add(m); scene.add(rig);
  mixer.setTime(clip.duration * (+q.get("t") || 0.3)); rig.scale.setScalar((+q.get("size") || 760) / span);
  rig.rotation.set(+q.get("tilt") || 0.12, +q.get("turn") || 1.05, +q.get("roll") || 0); rig.position.set(+q.get("x") || 0, +q.get("y") || 0, 0);
  renderer.render(scene, cam); window.DONE = true;
});
