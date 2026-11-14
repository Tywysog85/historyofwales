(function () {
  var D = DATA, ERAS = D.ERAS, EVENTS = D.EVENTS, PLACES = D.PLACES, PEOPLE = D.PEOPLE, MAPC = D.MAPC;
  var WIKI = "https://en.wikipedia.org/wiki/";
  var lang = document.documentElement.classList.contains("cy") ? "cy" : "en";  /* each page is one language: /cy/ pages are Welsh */
  var $ = function (s, r) { return (r || document).querySelector(s) || document.createElement("input"); };
  var HAS_TL = !!document.getElementById("events"), HERO = !!document.getElementById("sky"), HAS_MAP = !!document.getElementById("pins");
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  /* --nav-h: the top bar's real height (it grows with big phone text or a wrapped bar), so sticky bars below it sit flush under it */
  (function () {
    var nav = document.querySelector(".nav"), root = document.documentElement; if (!nav) return;
    function set() { root.style.setProperty("--nav-h", nav.offsetHeight + "px"); var d = document.getElementById("dial"); if (d) root.style.setProperty("--dial-h", d.offsetHeight + "px"); }
    set(); if (window.ResizeObserver) { var ro = new ResizeObserver(set); ro.observe(nav); var d = document.getElementById("dial"); if (d) ro.observe(d); } else window.addEventListener("resize", set);
  })();
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var ERA = {}; ERAS.forEach(function (e) { ERA[e.id] = e; });
  var PLACE = {}; PLACES.forEach(function (p) { PLACE[p.id] = p; });
  function T(en, cy) { return lang === "cy" ? cy : en; }
  /* today as a day number, by the visitor's own date: the build picks the home page's daily things with the same number (src/daily.py) */
  function dayNo() { var d = new Date(); return Math.floor(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 864e5); }
  function fmt(n) { n = Math.abs(n); return n >= 10000 ? n.toLocaleString("en-GB") : String(n); }  /* 2026, not 2,026; 230,000 BC keeps its comma */
  /* event fields */
  var E_ERA = 0, E_Y = 1, E_C = 2, E_END = 3, E_DAY = 4, E_TEN = 5, E_TCY = 6, E_BEN = 7, E_BCY = 8, E_KEY = 9, E_PLACE = 10, E_SRC = 11;
  function yearLabel(e) {
    var y = e[E_Y], c = e[E_C] ? "c. " : "", end = e[E_END] ? "–" + e[E_END] : "";
    if (y < 0) return c + fmt(y) + " " + T("BC", "CC");
    if (y < 1000) return c + y + " " + T("AD", "OC");
    return c + y + end;
  }
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  /* A slow connection (Ifan, 13 Nov 2026: "slow phones just show a picture of the dragon"): the 3D scene (about 2.7 MB) is not
     downloaded. Instead a still picture of the same land and castle, rendered from the 3D scene (hero-land-*.webp), and a picture
     of the same dragon (dragon-red.webp). "Slow" is what the browser reports (Chrome and Android do; Safari reports nothing,
     so iPhones always get the 3D). Data saver and very old phones still get the drawn scene, as before. */
  var SLOW = !reduce && !!(navigator.connection && /^(slow-2g|2g|3g)$/.test(navigator.connection.effectiveType || "")) && !navigator.connection.saveData;
  var STILL_IMG = { land: null, dragon: null, ref: null };
  /* how the pictures were taken (tools: see SKILLS.md "Still pictures of the 3D land"): w = page width, d = pixels per CSS pixel,
     h = hero height, b = how far the bottom of the picture runs below the row of figures (p) or the hero's foot (w) */
  var STILL_REF = { p: { w: 390, d: 1.5, h: 1160, b: 220 }, w: { w: 1440, d: 1.5, h: 977, b: 0 } };
  var MONTHS_EN = ["January","February","March","April","May","June","July","August","September","October","November","December"];
  var MONTHS_CY = ["Ionawr","Chwefror","Mawrth","Ebrill","Mai","Mehefin","Gorffennaf","Awst","Medi","Hydref","Tachwedd","Rhagfyr"];

  /* ---------- Hero sky ---------- */
  var cv = $("#sky"), cx = HERO ? cv.getContext("2d") : null, W = 0, H = 0, dpr = 1, mouse = 0, ridges = [], stars = [], milky = [];
  function rnd(seed) { return function () { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }; }
  (function () {
    var r = rnd(1282);
    for (var l = 0; l < 5; l++) { var w = []; for (var k = 0; k < 6; k++) w.push([r() * 6.28, 0.6 + r() * (k + 1) * 1.7, (1 / (k + 1.2)) * (0.6 + r() * 0.6)]); ridges.push(w); }
    for (var s = 0; s < 140; s++) stars.push([r(), r() * 0.6, r() * 1.2 + 0.2, r()]);
    /* the Milky Way: a band of faint stars rising from the left horizon */
    for (var q = 0; q < 420; q++) { var p = r(), n = (r() + r() + r() - 1.5) * 0.13; milky.push([0.0 + p * 0.62 + n * 0.5, 0.46 - p * 0.5 + n, r() * 0.9 + 0.3, r()]); }
  })();
  var LAYERS = [
    { y: 0.50, a: 0.16, c: "#232a3d", s: 0.05 }, { y: 0.60, a: 0.14, c: "#1d2433", s: 0.12 },
    { y: 0.70, a: 0.12, c: "#171d2a", s: 0.2 }, { y: 0.80, a: 0.09, c: "#121722", s: 0.3 }, { y: 0.92, a: 0.06, c: "#0e1118", s: 0.42 }
  ];
  /* where the words sit, so the scene can keep clear of them */
  var M = { h1t: 40, h1h: 80, sub: 0, cta: 0, tick: 0, nav: 0 }, hEl = HERO ? document.getElementById("top") : null;
  function measure() {
    if (!HERO) return false;
    var r = cv.getBoundingClientRect(), q = function (sel) { var el = hEl.querySelector(sel); return el ? el.getBoundingClientRect() : null; };
    var a = q("h1"), b = q(".sub"), c = q(".ticker"), e = q(".begin"), old = M.h1t + "," + M.h1h + "," + M.sub + "," + M.tick + "," + M.cta;
    if (a) { M.h1t = a.top - r.top; M.h1h = a.height; } var nv = document.querySelector(".nav"); M.nav = nv && window.scrollY < 4 ? Math.max(0, nv.getBoundingClientRect().bottom - r.top) : M.nav;
    if (b) M.sub = b.bottom - r.top; if (e) { /* the buttons slide up as they arrive, so their resting place is read from the layout, not from where they are mid-slide */ var ce = hEl.querySelector(".begin"), cy = ce.offsetHeight, cn = ce; while (cn && cn !== hEl) { cy += cn.offsetTop; cn = cn.offsetParent; } M.cta = cn === hEl ? cy + hEl.getBoundingClientRect().top - r.top : e.bottom - r.top; } M.tick = c ? c.top - r.top : r.height;
    return old !== M.h1t + "," + M.h1h + "," + M.sub + "," + M.tick + "," + M.cta;
  }
  /* the land waits for the lettering: when the fonts arrive the words reflow, and land drawn before that would shift */
  var FONTS = !(document.fonts && document.fonts.ready); if (!FONTS) { document.fonts.ready.then(function () { measure(); FONTS = 1; }); setTimeout(function () { FONTS = 1; }, 3500); }
  var VIS = 0; /* how much of the hero the first screen shows */
  function size() { if (!HERO) return; var r = cv.getBoundingClientRect(); dpr = Math.min(window.devicePixelRatio || 1, 2); W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; VIS = window.innerHeight - (r.top + window.scrollY); measure(); draw(); }
  if (HERO) setInterval(function () { var r = cv.getBoundingClientRect(); if (Math.abs(r.height - H) > 1 || Math.abs(r.width - W) > 1) size(); else if (measure() && reduce) draw(); }, 500);
  /* ---- the sky follows the real sun over Wales: night, dawn, day, dusk ---- */
  function hex(c) { return [parseInt(c.slice(1, 3), 16), parseInt(c.slice(3, 5), 16), parseInt(c.slice(5, 7), 16)]; }
  function mix(a, b, k) { var x = hex(a), y = hex(b); return "rgb(" + Math.round(x[0] + (y[0] - x[0]) * k) + "," + Math.round(x[1] + (y[1] - x[1]) * k) + "," + Math.round(x[2] + (y[2] - x[2]) * k) + ")"; }
  function mixHex(a, b, k) { var x = hex(a), y = hex(b); return "#" + [0, 1, 2].map(function (i) { return ("0" + Math.round(x[i] + (y[i] - x[i]) * k).toString(16)).slice(-2); }).join(""); }
  /* a glowing star, painted once in three tints (white, blue-white, warm) and stamped wherever a bright star shines */
  var STAR = ["255,255,255", "205,222,255", "255,232,205"].map(function (c) {
    var k = document.createElement("canvas"); k.width = k.height = 64; var q = k.getContext("2d"), g = q.createRadialGradient(32, 32, 0, 32, 32, 32);
    g.addColorStop(0, "rgba(255,255,255,1)"); g.addColorStop(0.14, "rgba(" + c + ",.95)"); g.addColorStop(0.3, "rgba(" + c + ",.4)"); g.addColorStop(0.6, "rgba(" + c + ",.1)"); g.addColorStop(1, "rgba(" + c + ",0)");
    q.fillStyle = g; q.fillRect(0, 0, 64, 64); return k;
  });
  /* sky: four colours top to bottom; star: how bright the stars are; orb: sun or moon colour; tint/k: colour washed over the hills; glow: red glow behind the summit */
  var SKIES = {
    night: { sky: ["#0b0e16", "#1a2032", "#3a2a35", "#0e1118"], star: 1, orb: "#e9d9c6", tint: "#232a3d", k: 0, glow: 1, sun: 0 },
    dawn: { sky: ["#141a33", "#3b3157", "#8c4b4f", "#0e1118"], star: 0.3, orb: "#ffd9a8", tint: "#5a4660", k: 0.3, glow: 1.2, sun: 0.6 },
    day: { sky: ["#0f2646", "#1c446f", "#2f5f8f", "#0e1118"], star: 0, orb: "#fff1c9", tint: "#2c4f73", k: 0.42, glow: 0.25, sun: 1 },
    dusk: { sky: ["#10142a", "#35274a", "#8a3a3c", "#0e1118"], star: 0.35, orb: "#ffc48f", tint: "#553a52", k: 0.28, glow: 1.5, sun: 0.6 }
  };
  function sunOverWales() {
    /* height of the sun above the horizon in mid Wales, in degrees, and whether it is still morning */
    var R = Math.PI / 180, d = Date.now() / 864e5 - 10957.5, g = (357.529 + 0.98560028 * d) * R, q = 280.459 + 0.98564736 * d;
    var L = (q + 1.915 * Math.sin(g) + 0.02 * Math.sin(2 * g)) * R, e = (23.439 - 0.00000036 * d) * R;
    var ra = Math.atan2(Math.cos(e) * Math.sin(L), Math.cos(L)), dec = Math.asin(Math.sin(e) * Math.sin(L));
    var ha = ((18.697374558 + 24.06570982441908 * d) * 15 - 3.7) * R - ra, lat = 52.4 * R;
    return { el: Math.asin(Math.sin(lat) * Math.sin(dec) + Math.cos(lat) * Math.cos(dec) * Math.cos(ha)) / R, am: Math.sin(ha) < 0 };
  }
  var SKY = SKIES.night;
  function setSky() {
    var force = (/[?&]sky=(night|dawn|day|dusk)/.exec(location.search) || [])[1];
    if (force) { SKY = SKIES[force]; return; }
    var s = sunOverWales(), tw = SKIES[s.am ? "dawn" : "dusk"], a, b, k;
    if (s.el <= -9) { SKY = SKIES.night; return; }
    if (s.el >= 9) { SKY = SKIES.day; return; }
    if (s.el < 0) { a = SKIES.night; b = tw; k = (s.el + 9) / 9; } else { a = tw; b = SKIES.day; k = s.el / 9; }
    SKY = { sky: a.sky.map(function (c, i) { return mixHex(c, b.sky[i], k); }), star: a.star + (b.star - a.star) * k, orb: mixHex(a.orb, b.orb, k), tint: mixHex(a.tint, b.tint, k), k: a.k + (b.k - a.k) * k, glow: a.glow + (b.glow - a.glow) * k, sun: a.sun + (b.sun - a.sun) * k };
  }
  if (HERO) { setSky(); setInterval(function () { setSky(); if (reduce) draw(); }, 60000); }
  var t0 = 0;
  function draw(t) {
    if (!HERO) return;
    t = t || t0;
    var sy = Math.min(window.scrollY, H);
    cx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var g = cx.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, SKY.sky[0]); g.addColorStop(0.55, SKY.sky[1]); g.addColorStop(0.8, SKY.sky[2]); g.addColorStop(1, SKY.sky[3]);
    cx.fillStyle = g; cx.fillRect(0, 0, W, H);
    stars.forEach(function (s, i) {
      var tw = 0.5 + 0.5 * Math.sin(t / 900 + s[3] * 20), X = s[0] * W, Y = s[1] * H - sy * 0.02;
      if (SKY.star <= 0.02) return;
      cx.fillStyle = "rgba(236,233,225," + (0.15 + 0.5 * tw * s[2] / 1.4) * SKY.star + ")"; cx.beginPath(); cx.arc(X, Y, Math.max(0.35, s[2] * 0.55), 0, 6.283); cx.fill();
      /* the brighter stars: a soft glowing point, each a little different in size and colour, twinkling gently */
      if (i % 7 === 0 && !(Y > M.h1t - 6 && (W < 1100 ? Y < M.cta + 6 : X < W * 0.62))) { var R = (4.5 + 7 * s[3]) * (0.85 + 0.15 * tw); cx.globalAlpha = Math.min(1, (0.5 + 0.5 * tw) * SKY.star); cx.drawImage(STAR[i % 3], X - R, Y - R, R * 2, R * 2); cx.globalAlpha = 1; }
    });
    if (W >= 1100 && SKY.star > 0.5) {
      for (var b = 0; b < 5; b++) { var bx = W * (0.06 + b * 0.125), by = H * (0.4 - b * 0.1), br = H * 0.2, bg = cx.createRadialGradient(bx, by, 0, bx, by, br); bg.addColorStop(0, "rgba(150,165,215," + 0.1 * SKY.star + ")"); bg.addColorStop(1, "rgba(150,165,215,0)"); cx.fillStyle = bg; cx.fillRect(bx - br, by - br, br * 2, br * 2); }
      milky.forEach(function (s) {
        var X = s[0] * W, Y = s[1] * H - sy * 0.02; if (Y < 0 || X < 0) return;
        cx.fillStyle = "rgba(226,230,245," + (0.2 + 0.55 * s[3] * (0.6 + 0.4 * Math.sin(t / 1300 + s[3] * 40))) * SKY.star + ")"; cx.fillRect(X, Y, s[2], s[2]);
      });
    }
    /* phones and tall, narrow windows: the mountain sits below the words. Wide screens: it stands to the right of them. */
    var narrow = W < 640, stacked = W < 1100;
    var ex0, ew, eb, eh;
    if (stacked) {
      var top = narrow ? M.cta + 18 : M.sub + 4, bot = Math.max(top + 120, M.tick + (narrow ? 26 : 10));
      eh = Math.min(bot - top, W * 0.62); if (narrow) eh = Math.max(120, eh * 0.56); /* on phones the mountains take the upper part of the strip and the moor the rest; this must not depend on the window height, which changes as the phone's address bar hides, or the castle jumps */ eb = top + eh; ew = Math.max(W * (narrow ? 1.05 : 0.8), eh * 2.3); ex0 = W * (narrow ? 0.6 : 0.7) - 0.53 * ew;
    } else { ew = Math.min(W * 0.6, H * 1.2); ex0 = W * 0.985 - ew; eb = H * 0.74; eh = Math.min(H * 0.5, ew * 0.62); }
    var sumX = ex0 + 0.53 * ew - mouse * 4, sumY = eb - eh - sy * 0.04;
    var mr = Math.max(narrow ? 15 : 18, Math.min(W, H) * 0.04);
    var mx = narrow ? W - mr - 14 : W * 0.9, my = (stacked ? Math.max(mr + 8, M.h1t - mr * 0.2) : H * 0.13) - sy * 0.03;
    var mg = cx.createRadialGradient(sumX, sumY, 10, sumX, sumY, Math.max(W, H) * 0.45); mg.addColorStop(0, "rgba(226,69,61," + Math.min(0.42, 0.26 * SKY.glow) + ")"); mg.addColorStop(1, "rgba(226,69,61,0)");
    cx.fillStyle = mg; cx.fillRect(0, 0, W, H);
    var halo = cx.createRadialGradient(mx, my, mr * 0.9, mx, my, mr * 4.2), pulse = 0.2 + 0.05 * Math.sin(t / 2600);
    var oc = hex(SKY.orb).join(","); pulse *= 1 + SKY.sun * 1.3;
    halo.addColorStop(0, "rgba(" + oc + "," + pulse + ")"); halo.addColorStop(0.35, "rgba(" + oc + "," + pulse * 0.3 + ")"); halo.addColorStop(1, "rgba(" + oc + ",0)");
    cx.fillStyle = halo; cx.fillRect(mx - mr * 4.5, my - mr * 4.5, mr * 9, mr * 9);
    cx.fillStyle = SKY.orb; cx.beginPath(); cx.arc(mx, my, mr, 0, 7); cx.fill();
    cx.fillStyle = "rgba(180,160,140," + 0.22 * (1 - SKY.sun) + ")"; [[-.3, -.25, .22], [.28, .1, .16], [-.1, .4, .12]].forEach(function (c) { cx.beginPath(); cx.arc(mx + c[0] * mr, my + c[1] * mr, c[2] * mr, 0, 7); cx.fill(); });
    /* first light on the horizon behind the mountain */
    var hz = cx.createLinearGradient(0, eb - eh * 0.75, 0, eb + eh * 0.1); hz.addColorStop(0, "rgba(232,120,76,0)"); hz.addColorStop(1, "rgba(232,120,76," + Math.min(0.3, 0.17 * SKY.glow) + ")");
    cx.fillStyle = hz; cx.fillRect(0, eb - eh * 0.75, W, eh * 0.85);
    /* where the device can draw it, the mountain and castle are real 3D on their own canvas (tools/land3d.src.js); until that is ready only the sky shows */
    /* the opening is staged: sky and title first, then the words, then the land fades in (never before 1.2 s, so it does not arrive under a half-drawn title), then the dragon flies in */
    var L3 = window.HCL3 && HCL3.ready && performance.now() > 1200 && FONTS, noLand = L3 || window.HCL3_WANT || (SLOW && !STILL_IMG.failed), STILLP = SLOW && STILL_IMG.land;
    if (L3 || STILLP) {
      /* the valley mist the mountains rise out of, which also hides the stars below the skyline. It is dark at night and a soft blue
         haze by day: a light grey mist read as a flat grey sheet behind the castle at night (Ifan, 13 Nov 2026), so keep it dark. */
      var vm = cx.createLinearGradient(0, eb - eh * 0.7, 0, H), mistC = mixHex(mixHex(SKY.sky[2], SKY.sky[1], 0.45), mixHex("#262b3d", "#444d68", SKY.sun), 0.7), vc = hex(mistC).join(",");
      vm.addColorStop(0, "rgba(" + vc + ",0)"); vm.addColorStop(0.34, "rgba(" + vc + ",.9)"); vm.addColorStop(0.55, "rgba(" + vc + ",1)"); vm.addColorStop(1, SKY.sky[3]); cx.fillStyle = vm; cx.fillRect(0, eb - eh * 0.7, W, H);
      if (!L3) drawStillLand(stacked); else {
        if (!FLAG) FLAG = flagArt(); HCL3.frame({ W: W, H: H, sumX: sumX - ew * 0.13, sumY: sumY + ew * 0.15, ppm: ew / 2000, ground: stacked ? { x: W * 0.7, y: eb - eh * 0.07 - sy * 0.04, ppm: Math.min(W * 0.0095, eh * 0.019), tilt: narrow ? 0 : 0.12 } : { x: Math.min(W * 0.885, W - H * 0.3) - mouse * 9, y: H * 0.7 - sy * 0.1, ppm: H * 0.0098, tilt: 0.1 }, castle: true, t: t, sun: SKY.sun, fog: mixHex(SKY.sky[2], SKY.sky[1], 0.45), mist: mistC, flag: FLAG, flagV: FLAGV });
        if (HCL3.shown && !LANDT) LANDT = t; }
    }
    LAYERS.forEach(function (L, i) {
      if (noLand) return;
      if (i === 3 && !stacked) drawCastle(Math.min(W * 0.885, W - H * 0.3) - mouse * 9, H * 0.7 - sy * 0.1, H * 0.125, mix("#0d111b", SKY.tint, SKY.k * 0.35), t);
      if (i === 1 && !noLand) { drawEryri(ex0 - ew * 0.34 - mouse * 2, eb - sy * 0.03, ew * 0.9, eh * 0.62, true); drawEryri(ex0 - mouse * 4, eb - sy * 0.04, ew, eh); }
      var w = ridges[i], amp = stacked ? eh * (0.34 - i * 0.04) : H * L.a, base = (stacked ? eb - eh * (0.42 - i * 0.15) : H * L.y) + sy * L.s * 0.6, off = mouse * (i + 1) * 6 + (reduce ? 0 : t / 1000 * (i + 1) * 1.2);
      cx.beginPath(); cx.moveTo(0, H);
      for (var x = 0; x <= W + 8; x += 6) {
        var u = (x + off) / Math.max(W, 900) * 3, v = 0;
        for (var k = 0; k < w.length; k++) v += Math.sin(u * w[k][1] + w[k][0]) * w[k][2];
        v = Math.abs(v) * 0.6 + v * 0.4;
        cx.lineTo(x, base - v * amp);
      }
      cx.lineTo(W, H); cx.closePath(); cx.fillStyle = mix(L.c, SKY.tint, SKY.k * (1 - i * 0.2)); cx.fill();
      if (i === 1 || i === 3) {
        var fg = cx.createLinearGradient(0, base - H * 0.08, 0, base + H * 0.05); fg.addColorStop(0, "rgba(160,170,200,0)"); fg.addColorStop(0.6, "rgba(160,170,200," + (0.06 + 0.02 * Math.sin(t / 2200 + i)) + ")"); fg.addColorStop(1, "rgba(160,170,200,0)"); cx.fillStyle = fg; cx.fillRect(0, base - H * 0.08, W, H * 0.13);
        /* mist: soft banks drifting across the valley */
        for (var m = 0; m < 3; m++) {
          var mw = W * (0.5 + m * 0.14), px = ((m * 0.41 + i * 0.17) * (W + mw) + (reduce ? 0 : t / 1000 * (5 + m * 3 + i))) % (W + mw) - mw / 2, py = base - H * 0.02 + m * 9, rg = cx.createRadialGradient(px, py, 0, px, py, mw / 2);
          rg.addColorStop(0, "rgba(176,186,214,.11)"); rg.addColorStop(1, "rgba(176,186,214,0)");
          cx.save(); cx.translate(0, py); cx.scale(1, 0.12); cx.translate(0, -py); cx.fillStyle = rg; cx.fillRect(px - mw / 2, py - mw / 2, mw, mw); cx.restore();
        }
      }
    });
    if (SKY.star > 0.5) drawMeteors(t);
    drawDragon(t, sumX, sumY, narrow, stacked);
  }
  /* Y Ddraig Goch: the real dragon of the national flag, as vector artwork.
     Artwork from the flag-icons project (gb-wls), MIT licence, copyright (c) 2013 Panayiotis Lipiridis. */
  var DSVG = '<g stroke="#000" stroke-width="1.4"><path fill="#d21034" d="M419 70.8h-.1zm-.1 0a694 694 0 0 0-111.8 75c-17 14.9-12.2 26.7-12.9 40 .6 9-1.9 17.4-7.4 22.4l-37.8 7.6-3.6-10.4c1.1-5.4 5.5-8 14.9-4.7.7-6.8-4.9-9.6-11.3-12-2.3-1.8-5-3-4.7-9-1-13.5 20.6 1 20.8 1s-.8-13.7-10.7-16.4c-5.4-1.9-7.7-7.6-5.6-11.8 4.3-8.7 12.5.6 18.7 1-.2-5.7-1.8-9.7-6.7-14.2-2.6-1.7-9-2.9-9.2-5.6-.1-3.6 6-5.2 14.5-4.2-1.8-5.1-7.5-8.4-15.3-10.8l-4.6-8.1c-2.2-4-3.2-4.2 1.9-11.8 4.5-3 10.6-7.2 15.2-10.1l-5-.6c.6-5.5.7-7.4 2-16.5-5 6.7-11 5.5-16.6 8.2 0 0-15.6 2.8-20.7 9.5l-39.4-2c-8.4 1.1-15.5 3.5-16.9 11.6-19.1 2-39.1.3-53.7 18.5 10-.4 18.6-2.8 29.8-1.4 0 0 9.5.2 11.4 10.3.2.4 3.3.4 3.3.4l3.6 2.8 1.4-3.8 3.2 2.2 1-4.2 3.2 2.2.2-5 4.2 3v-6.7s15.6 0 20.4 10c.2.1-43.7 8-86.1 4.3l12.2-6c-15.4-3.2-30-6-43.6-16.7 5.1 19.4 31.7 42.1 37.2 42l-5.2-9.4 46 2c1.7 5.1 1 10.8 5 15.3 0 0-2.5 8.4 3.2 11.8.2.4 6.7-17 6.7-17s2 4.7 4 7.8c3-15 19.4-17.5 19.4-17.5l3.4 8c-5.1.8-11.5 11.2-8 17-3.5 0-9.6 10.1-7.7 15.6-2.9 2.9-10 6.7-8.3 18.8-5.6 1.2-9 11.5-7.2 22.5-8.8 8.1-6.6 23 1.2 29.1-3.2 3-5.2 5.1-5.2 8.7-3.1-1.1-6-.2-7.3 1.8-3.8-3.9-9.2-7.2-13-3.6-1-4.6-7-9.6-13.5-9a12 12 0 0 0-9-13s-1.5-22.6-8.3-30c-.7-4 .4-6.8 6-10.2 5.7-3 6.9-5.3 6.4-13.9 2.3-5.7 4-11.5-3-15.4.2 6.8-1.8 10-4.6 13-3.3-.4-4.4 3.4-6.6 5-3.1-4.1 6.5-10.6-.6-19.9-.4-.4-5-12-16.3-11.8 5.3 3.1 7.6 8.4 7.6 13.9a41 41 0 0 0-1.8 29.3c-4.7-7-7.4-20.4-11.3-22.7-3.4-.7-5-8.7-18.3-6.4 5.7 1.5 7.6 5.9 9 9.8-3.4 1.8-1.7 6.6.9 9.9-.5 7.7 4.1 12.2 11 15L85.6 237c-2.7-.3-7 10.4-8.6 10.7-2.7 1.7-7.4 6.2-2 7.5-1.6 5.7-3.1 9.2-11.7 10.4 0 0 9 5.4 16.6-3.8 8-.2 5.4-9.8 9.3-14 0-.3 2.3-1.7 5.5-10.2 1.4 7.6 9.2 30.8 26.7 42.3 15.3 16.4 28 31.9 27.8 53.7a54 54 0 0 0 12.3-22.7 89 89 0 0 1 30.8-3.6c-1.8 3.9-3.9 7.6-1.3 10-7.4 2.6-9 8-6 13.3-7.8 5.3-8.3 8.7-8.4 17.5-14.5 18.5-23.4 17.9-37.7 13-4.6-2.7-12-6.6-15.3-4.5-6.1-4.2-15-4.8-16.5 4.6 4.7-3.9 7.4-3.1 11.1.6-.7 1.9-1.3 3.7 1.4 4.8l-3.6 4c-6.6-1-15.6-1-17.9 8.7 3.4-2.9 11-3.5 17-.8l3.5 1.2.4 4.6s-9-1.4-11.4 13.3c8.4-9 14.4-6.7 14.4-6.7 3.3 4.8 15.3 4.1 24-3.8 12.1-6.8 15.7 3 23.5-3.4 6.5-4.8 14.2-1.6 19.5 4 6.1 2.3 12.5 4.2 17.5 0 0 0 6.2-3.9 12.3 2.4 0-7-5-10.9-11.8-11l-2-2c-6.5-1.4-13.7-.8-19.4-4a58 58 0 0 1 14.1-27c9.3-10 16.2-14.6 28-29.9-.5 8.7 6.1 18.3 9.6 27 0 0 7-11.1 8-20.3.3 0 8.9-4.4 12.5-8.3 7.8 4.9 20.4-3.8 28.6-11 5 2 8.9 1.8 14.7 0-4.7 9.6 2.7 18.5 14.5 22.2 1 8.4 9.6 10.2 22.5 10.2.6 5 8.3 5.7 8.3 5.7-5 2.2-7.4 4.5-7.3 9.6-5 0-8.7 1.3-10 7-6.9.2-13.9.7-19.8 4-6.3-.9-14-3.5-18.9-8.6-2.5-2.1-3.2-5.2-7.6-6.4-2.8-3.3-6.2-2.6-7.3.6-2.9-2.3-13.8-3.3-15.7 7 5.2-3.7 9.7-5.1 13-.5-1.8 3.1 4.2 5 9.4 6.2 3.7.2 10.2 3.6 12.2 9.2a20 20 0 0 1-16.7-2.6 11 11 0 0 0-13-.8c-4.4-2.8-14.7 2.5-15.1 10.9 4.3-4 8.3-6 12.3-3.4-2 .4-1.3.6-1 1.8l10 5.8c-5 1.3-9.6 3.3-7.4 12.5 0 0 4-8 13-5 .2-.3 1.3 2.8 3.9.7 3.9-4.4 12.8-6.4 20.7-7.2 6.3-.7 12.6-2.6 18 1 5-2.5 10.4-4.2 16-.2 6.6 2 11.4 9.8 19.7 6.3 4.2-3 9.3-3 14.5 2.8 0-7.4-5.5-9.9-13.3-11.5l-5.4-3.2c-5-.8-10 .1-15.1-2.3a92 92 0 0 0 57.7-42.4l12.5 4.4c3 .2 3.2 1.2 9.3 3 .2-8.9-3.7-18.1-19.8-19l-21-8c-4.6-4.8-6.6-14.9-.9-20.8 5.6-5 6.6-4.4 10.3-10.5 4.5-.4 8.7 4.2 12.8 4.2 2 5.9 13.4 11 20.6 9.3 4.5 4 13 6.2 22.5 3a18 18 0 0 0 20.5 3c2.2 2.2 6.8 4 12 2.8.5 0 2.8 5.8 8.5 7.9-2.5 2.4-1 13 1.7 16.9a17 17 0 0 0-.9 12.7c-5.8 3.7-7 6.5-4.4 12.8-7.6 12.3-16.7 13.7-25.3 10l-9.3-6-9.8-9.6c-1.7-1.6-5.2-2-5.9 1.4 0 0-12.6-2.8-13.7 7.9 5.3-5.1 12.7-.6 12.7-.4s-1.8 1.4-.4 3.4c.3-.3 9.3 3.3 17.2 6.7 4.3 1.7 5.3 2.2 7.2 3.2l-7.2-3.2a33 33 0 0 0-11-2.9c-4.4-.4-9.2-1-11.4 2.4-4.8 2-12.4 3.7-12 12.7 3.2-5.4 7.7-5.1 13.4-4.6l-.4 1.2c6.2 2.8 5-.8 10.8-1.3a44 44 0 0 1 15.3 2.5c-4.5 1.3-10.7.7-13.6 4-.6 1-2.5.6-1.6 3.2 0 0-9-.2-11.3 12 9-5.7 15.9-5.5 16-5.5l2.9.6 11-7.3c.3 0 10.6-4.6 15.3.6 4.2 2 8.6 2.2 13-.4 8.4-3.7 16.3-4 24 1.2l7.1 4.2 3-2s8-2.2 13.8 4.9c-2.4-12.3-11.2-12.7-11.2-12.7l-2-1.8-12.4-4.9c-1.9-4.5-6.4-8-1.9-13.4 4.7-23.1 10.2-40.4 1.2-63.8 8.4 3.6 14.7 14.8 25.2 10.9 0-9.4-34.6-27.3-61-41.6C508 264 560 232.1 540 191.5l9.4-29.4c4.5 9 13.5 15.8 21.6 18.7-6.7-12.7-10.5-51.6-6.7-78.4a627 627 0 0 1-57.1 60c10 2.4 18.9.7 28.6-.5l-8.2 17c-26.6-15.7-57.8-4-58 16.8.9 24.2 30.8 27.7 48.1 19.2-3.4 22.1-54.2 14-54.2 14-18-6.2-35.1-5.2-54-5 3.9-12.1 25.7-22.9 42.4-18.1-23.3-26.2 3.3-58.7 35.4-68.6-35-11.6-4.9-38.3 21.3-57.4 0 0-75.3 31.7-82.2 31.6-21.4-1.6-15.6-27-7.4-40.6zm-236.4 30.4q2.8 0 5.5.6c3.4.9 7.5 1.3 7.5 2.4-1.6 2.6-5.5 5.7-9.3 5.6s-6-2.5-7.2-8.2q.8-.4 3.5-.4zm317 89.4c5 0 10.9 2 16.6 8.2-2.7 8-26.8 12-28.4.2-.5-3.6 4.6-8.3 11.8-8.4z"/><path fill="none" stroke-linejoin="round" d="m207.4 171.2 3.7 5.3m-.2.1s0 7.2 1.5 7.3m-3.3 3.9 3.8 6.3m-10.5 1.6c.2 0 4.7 5.2 4.7 5.2m3.9-4c0 .2 4.2 8.1 4.5 8.1m-10-2.6s1.4 9.6 2.7 9.3m-9 8.3 4.2 6.5m3.7-13.3s2.3 9.1 4.1 8.3m1.9-13.8c.1.2 4.3 6.1 5.4 5.3m-1 2.3 4 8m-10.6-1.8 3.3 9.4m-11-4.6s3 10.1 5.7 8.5m-6.8 5s.2 5.3 2.8 5.6m1.8-8.3c0 .2 2.7 3.8 2.7 3.8m5-10.1 2.1 3.5m4.9-10 3.3 4.1M206 176.7c.1 4.5 7.2-1.6 10-5.4m-13 21s7.7-5.5 13.7-13.8m-16.3 26.9c5.5-1.5 15.6-13.7 17.6-20.2m-18.7 32.3c1.5.7 20.3-13 20.8-22.9M198.8 228c0-.1 17.2-4.4 24.3-23.3M198 242.3s27.5-16.5 29-28.6M412.4 270s-1.8 14.2-16 16.4m20.5 9c.1-.2 13.6-15 10.1-19.5m21.1 5.2s-.2 10.3-8.6 17.4m25.4-14.4s.3 12.4-5 17.4m20.4-10s-6 11.7-8.1 12.9m7.9 7.8s7.8 2 10.3-3.2m-8.3 20.1s7.2 1.3 10.6-5.6m-11.4 18.7s5.9 5 9.9-1.6m-94-94.4s-.7 25.3 34.8 30.4c39.7 11 58.5 5.2 60.8 49.7-1.5 17-3.6 36-16 28.7m-117.4-85.5s5.7 10.1 12.5 9.4c9-2.6 12.3 2.9 12.3 2.9m-49-2.2s15 7.3 27.7-4.5m-26-6c1.3 17.5-20.1 27.5-28.6 25.8m29.6 41c.1 0 11.6-6.8 9.3-11.6m-32.1 1.5c.3-.4 19.3-2.2 22.8-9m-31.6-19s26.9.2 28.7 5.1m7-21s-26.2 44.9 22.2 44.9m-50-45.5s-5.6 16.7-13.6 22.4m-14.2-28.2s9.7 18.8 0 28.1M261 280.8c.1.3 3.1 26.7-3.5 34.2m-9.2-33.4s1 16.8-4 22.8 1.2 18.4 1.2 18.4m-60.5 8s3.6 6.3 8.5 4.1m-2.5-17.8s8 3.5 10.7 2.2m-2-30.4s-11.8 3.3-7.3 17.3c6.8 5.5 13.4 4.6 13.4 4.6m-29.4 37.4c-.1 0 1.4 11 9 2.7 5.3-11.2 22-42.6 25.9-53.4m7.8-5.1s-8.1-6.3-7.8 2.5c-.2 5.5 2.5 6.8 2.5 6.8.3 4 3.8 9.6 6.6 4.5 1.2-5-.8-7.2-.8-7.2m4.7-9c-7.3-.4-11.3 15.7 2.8 5.6m4.8-11s-1.8 2.5-4.7-.2c-1.5-2.6-6.8 12 2.5 12.5 1.7-4.3 6.8-5.5 6.8-5.5m4.4-13.8s-4.2 2-5.7 1.7c-5 1.1-4 12.8 2.3 12.1 2.2-2.5 4.5-6 4.5-6m-40.3-23c-.2 0-16.5 25.7 9.1 32.5m198-71s-10 8.4-.7 22c-31-.5-47.5 13.8-48.8 23.4-39.4-2.8-32.2 8.8-45 12.6-17.1-14.3-42.2-6.3-40.6 8-11.4-16.1-29-8.3-31.2-4.3s-1.3-19.8-1.3-19.8-11.5 5.2-19.4 14.6v-19.9c-9.6 2-18.9 2-28.8 1.8m-25.9-7.3s14.3 8 32-2.8M166 226.3s11 10 32 6.8m-25-29.7s2.4 8.1 26.3 8.6M181 184.6s9 11 21.2 9.3m-13.5-25s3.5 6 16.8 7m-9-24.5s7 7.6 15 6.3M238 89.3s3.1-3 8.3-1.5m-10.5 17.8s-9.6-.3-9-4c.8-4.4 10.2-7.5 10.2-7.5s12.5-8 14.4-10.8m-56.6 44 12.2 23.3 5.8-8.8 3 6 5-8.7 8.6 5.5-3.2-10.7 7.2-.5s-2-5.1-8.4-6.2c1.7-1.3 7.7-5.3 7.7-5.3s-3.4-4-8.8-4.1c1.8-1.9 4.2-6.5 4-6.5l-5.3-1.2s12.2 4 21.6-1.6M221 89.7c.1.1-.7 4.8-3.3 7.5m-43.7 5.3s7.5-2 13.1-.9 13.1 3.2 13.1 3.2 9-1.2 11.9-3.3m-56.8 6s-1 3.6-1.4 6c0 1.7-5.5 4-5.5 4m10.3-17.4s4.8 6 5 9.5c.1 3.4-3.6 6-3.6 6M109 141l-5-8 4.5-1.6m90.5 121c-4-5.2 3-84.2 17.7-104.8-5.1 37.2 12 75.2 16.3 75m-79-97s6.8 2.5 20.7-8.6m18.9 26.8 10 .1m300.3-62s-166.7 77.8-169.1 82c28.1-8.6 147.5-28.5 150.4-26.8-7 1.7-151.9 35-158.7 43 36.2-1.2 111.9 11.6 123.8 24C424.5 198.3 347.6 187 324 192c17.2 4.1 83.2 46.8 83.2 53.6-10-9.5-89.3-42.2-92.4-39 18.2 10.9 43.9 51.4 43.9 61.3-5.3-8.4-51.2-57.7-53.9-54.5 4.9 6.7 14.5 64.9 9.6 67.6 0-7-17.8-58-19.3-59.4-3.6 1-26.3 62-21.8 67.8-3-20.4.5-63 6-61.3-10 1.5-41.7 43.4-38.3 50 1-10.5 2.4-17.4 20.4-52.1-20 1.2-61.2 27.1-68.2 36.4 5.6-16.5 40.5-44.4 55.8-46.4m72-60.7c17.6-9.8 72-29.7 108.4-44.4m-142.6 97s12-.2 24-32.8c11.8-44.6 105.7-94.3 107.6-103.6M128 252.8s-2.8 6-6.2 7.6m19.7 1.4s-3.7 7.2-4.6 10.6m17.5-7s3 9.8.5 14.4m-36.4-40.1c-9.4 5.3 5.4 39 50.1 42.2m-7.2-18.2s-1.2 6 7.2 18c-2.4 13.4 10.2 23.9 15.2 25.6m-26-164.2 1.4-3.6 1.5 4 2.5-.1 1.6-4 1.4 4h2.4l1.5-4.4 2.3 4.2h2l1.5-5 3 3.6 1.2-.4 1-5.2 3.1 3.6 1-.5 1.4-5 2.5 3.7 1.3-.4 1.2-4.3 2.4 4m-39 6.2 18.8-.3c6 0 15.8-8.3 26.7-5.7m-84.9 46s3.1 6.8 7.4 3m-14.6 1.5s-6 16.2 1.2 20m-9.8-37.8s0 3.8 8-2m-32.5 86.7s6.3 2 5.3 6.7m-3-80.8s4 1.9 7.8-4m34.2 189.7c6.1-.4 7.5 2.4 13 2.4 6.6.2 12.9-2.4 21-4.7m53.1 15c-.2 0-3 5.8-.5 8.7m-87.5-8.2s9.8-8 15-3.1c4.9 1.7 7.6 1.4 7.6 1.4m-17.5-21.3s2.4 6.2-5.6 5.3m-2.4 9s5.1 3.2-.7 7.5m3.8 5.8s7 1 2.9 6.7M346 341.6s19 2 20 3.4c2.2-2.3 19.2-16.2-1.7-18.1a19 19 0 0 1-18.3 14.7zm-6.8 9.5c7.1 5.7 4.2 9.1 26.6-5.9m-36.8 13s10.5 11.4 18.2-2.4m-38.3 6.5-14.3 7.5M269 380.3s8.7-7.4 12.7-3.5 21.3-3.4 21.3-3.4M275.5 348s3 6-2.8 6.7m-8.5 11.9s3 5.6-2.8 7m9.5 8.1s9 .5 5.8 7.3m78.4-8.5s-5 4.2-1.3 9m73-39s5.7 2.8-1.1 7.5m-5.7 9.9s4.3 4.5 1.4 8.2m10.6 9s5.9 1.7 5.2 6.6m77.8-11s-5 3.7-2.3 8.4M427 236.3c11.8-1.4 28.8 25 37.5 30.1m51.9-67.4s6 5.3.7 18m10.4-38.2c1.7 1.3 8.1 4.8 12.4 12.8m4.1-52.2-8.3 22.5m17.6-23.6s-1.6 20-4 24M516 198.8c-2.7 8-26.8 12-28.4.2-.9-6 14.2-15.3 28.4-.2z"/><path stroke-linejoin="round" d="m182.3 101.3 9.3 1.7s-6.5 8.8-9.3-1.7z"/></g>';
  function svgImage(inner, vb, w, h, done) {
    var im = new Image(); im.onload = function () { done(im); };
    im.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="' + vb + '" width="' + w + '" height="' + h + '">' + inner + "</svg>");
  }
  /* the flag is painted flat once (white over green, then the dragon when it has loaded), and drawn in thin slices that billow */
  var FLAG = null, FLAGV = 0;
  function flagArt() {
    var c = document.createElement("canvas"); c.width = 600; c.height = 360; var g = c.getContext("2d");
    g.fillStyle = "#f6f3ec"; g.fillRect(0, 0, 600, 180); g.fillStyle = "#00a03a"; g.fillRect(0, 180, 600, 180);
    svgImage(DSVG, "-80 0 800 480", 600, 360, function (im) { g.drawImage(im, 0, 0, 600, 360); FLAGV++; if (reduce) draw(); });
    return c;
  }
  /* the same dragon for the sky, a little brighter so that it shows against the night */
  var SKYD = null;
  if (HERO) svgImage(DSVG.replace(/#d21034/g, "#e2453d").replace(/#000/g, "#4e0d10"), "60 68 514 332", 771, 498, function (im) { SKYD = im; if (reduce) draw(); });
  /* a castle of the princes on its crag: great keep, round towers, a twin-towered gatehouse, and Y Ddraig Goch flying over it */
  function drawCastle(x, y, s, col, t) {
    var lit = "rgba(" + hex(mixHex("#aab6d6", SKY.tint, SKY.k * 0.5)).join(",") + ",", i;
    function fl(n) { return reduce ? 0.9 : 0.78 + 0.22 * Math.sin(t / (290 + n * 37) + n * 1.9) * Math.sin(t / (90 + n * 11)); }
    function tower(xc, w, h, n) {
      var tw = w * 1.18, th = w * 0.2, mw = tw / (2 * n - 1);
      cx.fillStyle = col; cx.fillRect(xc - w / 2, -h, w, h + 0.06); cx.fillRect(xc - tw / 2, -h - th, tw, th + 0.01);
      for (var k = 0; k < n; k++) cx.fillRect(xc - tw / 2 + k * 2 * mw, -h - th - mw * 1.15, mw, mw * 1.15 + 0.01);
      /* round stone: moonlight on one side, shadow on the other */
      var g = cx.createLinearGradient(xc - tw / 2, 0, xc + tw / 2, 0); g.addColorStop(0, lit + ".2)"); g.addColorStop(0.4, lit + ".04)"); g.addColorStop(1, "rgba(0,0,0,.28)");
      cx.fillStyle = g; cx.fillRect(xc - w / 2, -h, w, h); cx.fillRect(xc - tw / 2, -h - th, tw, th);
      cx.fillStyle = lit + ".1)"; for (var c = 1; c * 0.16 < h; c++) cx.fillRect(xc - w / 2, -c * 0.16, w, 0.012);
    }
    function slit(wx, wy, h, n) {
      var f = fl(n), g = cx.createRadialGradient(wx, wy, 0, wx, wy, 0.3); g.addColorStop(0, "rgba(255,190,104," + 0.42 * f + ")"); g.addColorStop(1, "rgba(255,190,104,0)");
      cx.fillStyle = g; cx.fillRect(wx - 0.3, wy - 0.3, 0.6, 0.6);
      cx.fillStyle = "rgba(255,218,150," + (0.7 + 0.3 * f) + ")"; cx.beginPath(); cx.moveTo(wx - 0.028, wy + h / 2); cx.lineTo(wx - 0.028, wy - h / 2 + 0.028); cx.arc(wx, wy - h / 2 + 0.028, 0.028, Math.PI, 0); cx.lineTo(wx + 0.028, wy + h / 2); cx.closePath(); cx.fill();
    }
    cx.save(); cx.translate(x, y); cx.scale(s, s);
    /* the crag */
    cx.fillStyle = col; cx.beginPath(); cx.moveTo(-4.4, 1.8);
    [[-3.5, 1.2], [-3.0, 1.05], [-2.6, 0.62], [-2.25, 0.5], [-2.0, 0.16], [-1.8, 0.02], [1.8, 0.02], [2.0, 0.2], [2.3, 0.28], [2.6, 0.7], [3.1, 0.86], [3.5, 1.3], [4.4, 1.8]].forEach(function (p) { cx.lineTo(p[0], p[1]); });
    cx.closePath(); cx.fill();
    /* at the back: the flag turret, the great keep and a tall tower */
    tower(-0.56, 0.22, 1.98, 2); tower(-0.35, 0.66, 1.55, 4); tower(0.98, 0.4, 1.12, 3);
    /* the curtain wall */
    cx.fillStyle = col; cx.fillRect(-1.5, -0.52, 3, 0.58);
    for (i = 0; i < 20; i++) cx.fillRect(-1.5 + i * 0.155, -0.6, 0.085, 0.09);
    var wg = cx.createLinearGradient(0, -0.52, 0, 0); wg.addColorStop(0, lit + ".13)"); wg.addColorStop(1, lit + "0)"); cx.fillStyle = wg; cx.fillRect(-1.5, -0.52, 3, 0.52);
    cx.fillStyle = lit + ".09)"; for (i = 1; i < 3; i++) cx.fillRect(-1.5, -i * 0.16, 3, 0.012);
    /* corner towers and the gatehouse */
    tower(-1.5, 0.46, 0.92, 3); tower(1.5, 0.46, 0.86, 3);
    cx.fillStyle = col; cx.fillRect(0.3, -0.7, 0.36, 0.76); for (i = 0; i < 3; i++) cx.fillRect(0.33 + i * 0.11, -0.77, 0.07, 0.08);
    tower(0.2, 0.34, 0.82, 3); tower(0.76, 0.34, 0.82, 3);
    /* the gate, with firelight in the passage */
    var gf = fl(7), gg = cx.createRadialGradient(0.48, -0.1, 0, 0.48, -0.1, 0.5); gg.addColorStop(0, "rgba(255,176,90," + 0.5 * gf + ")"); gg.addColorStop(1, "rgba(255,176,90,0)");
    cx.fillStyle = gg; cx.fillRect(-0.02, -0.6, 1, 1);
    var ag = cx.createLinearGradient(0, -0.36, 0, 0.02); ag.addColorStop(0, "rgba(255,226,160," + (0.75 + 0.25 * gf) + ")"); ag.addColorStop(1, "rgba(236,128,60," + (0.7 + 0.2 * gf) + ")");
    cx.fillStyle = ag; cx.beginPath(); cx.moveTo(0.395, 0.02); cx.lineTo(0.395, -0.25); cx.arc(0.48, -0.25, 0.085, Math.PI, 0); cx.lineTo(0.565, 0.02); cx.closePath(); cx.fill();
    cx.fillStyle = col; for (i = 1; i < 4; i++) cx.fillRect(0.395 + i * 0.0425 - 0.006, -0.34, 0.012, 0.2);
    /* lit windows */
    slit(-0.35, -1.12, 0.17, 1); slit(-0.2, -0.74, 0.13, 2); slit(0.98, -0.82, 0.13, 3); slit(-1.5, -0.6, 0.13, 4); slit(1.5, -0.56, 0.13, 5); slit(-0.56, -1.74, 0.1, 6);
    /* Y Ddraig Goch on its pole: thin slices of the painted flag, each lifted and shaded by the wind */
    var px = -0.56, top = -2.86, fw = 0.86, fh = 0.516, n = 48, tt = reduce ? 0 : t;
    cx.strokeStyle = "#565c6c"; cx.lineWidth = 0.03; cx.beginPath(); cx.moveTo(px, -2.1); cx.lineTo(px, top - 0.05); cx.stroke();
    cx.fillStyle = "#c9a24a"; cx.beginPath(); cx.arc(px, top - 0.06, 0.032, 0, 7); cx.fill();
    if (!FLAG) FLAG = flagArt();
    for (i = 0; i < n; i++) {
      var u = (i + 0.5) / n, ph = u * 7.5 - tt / 230, lift = (Math.sin(ph) * 0.034 + Math.sin(ph * 1.7 + 1) * 0.012) * u + 0.05 * u * u, slope = (Math.cos(ph) + 0.4 * Math.cos(ph * 1.7 + 1)) * Math.min(1, u * 2.5);
      var fx = px + 0.015 + i * fw / n, fy = top + lift, sh = fh * (1 - 0.03 * Math.sin(ph + 1) * u);
      cx.drawImage(FLAG, i * 600 / n, 0, 600 / n, 360, fx, fy, fw / n + 0.006, sh);
      cx.fillStyle = slope > 0 ? "rgba(255,255,255," + 0.15 * slope + ")" : "rgba(8,12,24," + -0.3 * slope + ")"; cx.fillRect(fx, fy, fw / n, sh);
    }
    cx.restore();
  }
  /* shooting stars: one every few seconds, high in the sky */
  var meteors = [], nextMeteor = 2500;
  function drawMeteors(t) {
    if (reduce) return;
    if (t > nextMeteor) { nextMeteor = t + 3500 + Math.random() * 6000; var left = Math.random() < 0.5; meteors.push({ t: t, x: W * (left ? 0.05 + Math.random() * 0.4 : 0.55 + Math.random() * 0.4), y: H * Math.random() * 0.22, dx: (left ? 1 : -1) * (0.5 + Math.random() * 0.4), dy: 0.28 + Math.random() * 0.2, life: 700 + Math.random() * 500 }); }
    meteors = meteors.filter(function (m) { return t - m.t < m.life; });
    meteors.forEach(function (m) {
      var p = (t - m.t) / m.life, d = p * Math.min(W, 700) * 0.55, x = m.x + m.dx * d, y = m.y + m.dy * d, len = 70 * Math.sin(p * Math.PI) + 12;
      var g = cx.createLinearGradient(x, y, x - m.dx * len, y - m.dy * len); g.addColorStop(0, "rgba(255,250,235," + 0.95 * Math.sin(p * Math.PI) + ")"); g.addColorStop(1, "rgba(255,250,235,0)");
      cx.strokeStyle = g; cx.lineWidth = 1.6; cx.lineCap = "round"; cx.beginPath(); cx.moveTo(x, y); cx.lineTo(x - m.dx * len, y - m.dy * len); cx.stroke();
    });
  }
  /* Yr Wyddfa seen from the east: Crib Goch, Garnedd Ugain, the summit, then Y Lliwedd */
  var ERYRI = [[0,.04],[.07,.14],[.14,.3],[.2,.47],[.23,.55],[.245,.52],[.26,.6],[.275,.57],[.29,.64],[.31,.61],[.335,.71],[.37,.77],[.41,.82],[.445,.79],[.48,.86],[.51,.95],[.53,1],[.55,.95],[.575,.86],[.61,.76],[.64,.69],[.665,.73],[.685,.7],[.705,.74],[.725,.71],[.76,.6],[.82,.44],[.89,.27],[.95,.14],[1,.06]];
  function drawEryri(x0, base, w, h, far) {
    cx.beginPath(); cx.moveTo(x0, base + h * 0.2);
    ERYRI.forEach(function (p) { cx.lineTo(x0 + p[0] * w, base - p[1] * h); });
    cx.lineTo(x0 + w, base + h * 0.2); cx.closePath();
    var g = cx.createLinearGradient(0, base - h, 0, base); g.addColorStop(0, mix(far ? "#2a3350" : "#36405e", SKY.tint, SKY.k)); g.addColorStop(1, mix(far ? "#1c2334" : "#1e2537", SKY.tint, SKY.k));
    cx.fillStyle = g; cx.fill();
    if (far) return;
    /* snow on the tops: only above the snow line, with a ragged lower edge */
    cx.save(); cx.clip();
    var line = base - h * 0.8, sg = cx.createLinearGradient(0, base - h, 0, line + h * 0.08); sg.addColorStop(0, "rgba(240,236,228,.92)"); sg.addColorStop(0.7, "rgba(214,218,232,.5)"); sg.addColorStop(1, "rgba(214,218,232,0)");
    cx.beginPath(); cx.moveTo(x0 + w * 0.3, base - h * 1.05); cx.lineTo(x0 + w * 0.75, base - h * 1.05);
    for (var k = 0; k <= 18; k++) { var u = 0.75 - k * 0.025; cx.lineTo(x0 + w * u, line + h * (k % 2 ? 0.075 : -0.015) + h * 0.03 * Math.sin(k * 2.3)); }
    cx.closePath(); cx.fillStyle = sg; cx.fill();
    /* shaded eastern faces */
    cx.beginPath(); cx.moveTo(x0 + w * 0.53, base - h); cx.lineTo(x0 + w * 0.6, base - h * 0.3); cx.lineTo(x0 + w * 0.9, base); cx.lineTo(x0 + w, base - h * 0.06); cx.lineTo(x0 + w, base - h * 1.1); cx.closePath();
    cx.fillStyle = "rgba(11,14,22,.2)"; cx.fill();
    cx.restore();
    cx.beginPath(); ERYRI.forEach(function (p, j) { var X = x0 + p[0] * w, Y = base - p[1] * h; if (j) cx.lineTo(X, Y); else cx.moveTo(X, Y); });
    cx.strokeStyle = "rgba(233,217,198,.28)"; cx.lineWidth = 1.4; cx.stroke();
  }
  var FIRE_PREVIEW = /[?&]fire=1/.test(location.search);
  var DPOS = { x: -999, y: -999, r: 0 }, fireAt = 0, nextFire = 5000;
  /* the still land: phones and narrow windows scale it to the width and stand it on the row of figures; wide screens cover from the bottom right */
  function drawStillLand(stacked) {
    var im = STILL_IMG.land, r = STILL_IMG.ref, s, w, h;
    if (stacked) { s = W / r.w; w = im.width / r.d * s; h = im.height / r.d * s; cx.drawImage(im, 0, M.tick + r.b * s - h, w, h); }
    else { s = Math.max(W / r.w, H / r.h); w = im.width / r.d * s; h = im.height / r.d * s; cx.drawImage(im, W - w, H + r.b * s - h, w, h); }
  }
  var LANDT = 0, DT0 = -1, WING_UP = /[?&]wing=([\d.]+)/.test(location.search) ? +RegExp.$1 : 0.62; /* how far the wingtips rise above the chest, as a share of the wingspan */
  function drawDragon(t, sumX, sumY, narrow, stacked) {
    /* the dragon waits for the land to finish fading in, then starts at the beginning of its flight */
    if (DT0 < 0 && !reduce) { if (window.HCD3_WANT && !(window.HCD3 && HCD3.ready)) return; if (window.HCL3_WANT && !(LANDT && t > LANDT + 1700)) return; DT0 = t; nextFire = t + 5000; }
    var fixed = reduce || SLOW, period = 26000, k = fixed ? 0.55 : ((t - DT0) % period) / period;
    var base = narrow ? W * 0.27 : Math.min(W * 0.17, 260);
    var sx = narrow ? W * 0.61 : W * 0.6, ex = narrow ? W * 0.72 : stacked ? W * 0.78 : sumX - W * 0.06;
    var sy0 = narrow ? M.h1t + M.h1h * 0.3 : stacked ? M.h1t + M.h1h * 0.1 : H * 0.07, ey = narrow ? M.h1t + M.h1h * 0.42 : stacked ? M.h1t + M.h1h * 0.45 : sumY - H * 0.05;
    var x = sx + (ex - sx) * k, y = sy0 + (ey - sy0) * k + Math.sin(t / 900) * Math.min(H * 0.008, 6);
    var size = base * (1 - (narrow ? 0.18 : 0.3) * k), sc = size / 220;
    /* keep the whole dragon, wingtips included, below the menu bar */
    var clear = M.nav + 10 + size * WING_UP - (y + 60 * sc); if (clear > 0) y += clear;
    var alpha = fixed ? 1 : Math.min(1, k / 0.08, (1 - k) / 0.12);
    DPOS.x = x + 110 * sc; DPOS.y = y + 60 * sc; DPOS.r = Math.max(44, 120 * sc);
    if (!fixed && t > nextFire && alpha >= 1) { fireAt = t; nextFire = t + 9000 + Math.random() * 7000; }
    if (FIRE_PREVIEW && !reduce && (!fireAt || t - fireAt > 1300)) fireAt = t; /* preview: add ?fire=1 to the address and the dragon breathes fire without stopping */
    var fp = (t - fireAt) / 1300, pow = fireAt && fp >= 0 && fp < 1 ? Math.sin(Math.min(1, fp * 1.15) * Math.PI) : 0;
    /* the lifelike dragon: a 3D model on its own canvas (hero3d.js). It tells us where its mouth is, for the fire. */
    if (window.HCD3 && HCD3.ready) {
      /* the fire is painted on a small canvas of its own and handed over, so that it shows in front of the mountain */
      if (pow) { if (!FIRE) { FIRE = document.createElement("canvas"); FIRE.width = 320; FIRE.height = 128; } var keep = cx; cx = FIRE.getContext("2d"); cx.setTransform(1, 0, 0, 1, 0, 0); cx.clearRect(0, 0, 320, 128); cx.setTransform(2, 0, 0, 2, 10, 64); flames(t, pow); cx = keep; }
      HCD3.frame({ W: W, H: H, x: DPOS.x, y: DPOS.y, size: size * (narrow ? 0.85 : 1.05), alpha: alpha, t: t, fire: pow, day: SKY.sun, flame: pow ? FIRE : null, fs: sc * 1.7 });
      return;
    }
    if (window.HCD3_WANT) return; /* still loading: no stand-in, so the dragon never changes shape in front of the visitor */
    /* fallback (no WebGL, data saver, reduced motion): the dragon of the flag, turned to face the mountain */
    cx.save(); cx.globalAlpha = alpha; cx.translate(x, y); cx.scale(sc, sc); cx.rotate(-0.06);
    if (pow) { cx.save(); cx.translate(198, 22); cx.rotate(0.12); flames(t, pow); cx.restore(); }
    if (SLOW && !STILL_IMG.failed) { if (STILL_IMG.dragon) cx.drawImage(STILL_IMG.dragon, -20, 25, 300, 113.7); } /* the render of the 3D dragon, already facing the mountain */
    else if (SKYD) { cx.translate(222, 0); cx.scale(-1, 1); cx.drawImage(SKYD, 0, 0, 222, 143.4); }
    cx.restore();
  }
  /* fire: three flickering tongues from the mouth, brightest at the root */
  var FIRE = null;
  function flames(t, pow) {
    var L = 135 * pow; cx.save(); cx.globalCompositeOperation = "lighter";
    [[1, 22, "rgba(226,69,61,.8)"], [0.78, 14, "rgba(255,150,60,.9)"], [0.5, 7.5, "rgba(255,236,170,.95)"]].forEach(function (f, n) {
      var l = L * f[0] * (0.9 + 0.1 * Math.sin(t / 45 + n * 2)), w = f[1] * pow * (0.85 + 0.15 * Math.sin(t / 60 + n)), wob = 4 * Math.sin(t / 70 + n * 1.7);
      var g = cx.createLinearGradient(0, 0, l, 0); g.addColorStop(0, f[2]); g.addColorStop(1, f[2].replace(/[\d.]+\)$/, "0)"));
      cx.fillStyle = g; cx.beginPath(); cx.moveTo(0, 0); cx.bezierCurveTo(l * 0.3, -w + wob * 0.3, l * 0.7, -w * 0.9 + wob, l, wob); cx.bezierCurveTo(l * 0.7, w * 0.9 + wob, l * 0.3, w + wob * 0.3, 0, 0); cx.fill();
    });
    cx.restore();
  }
  function loop(t) { t0 = t; if (window.scrollY < H) draw(t); requestAnimationFrame(loop); }
  window.addEventListener("resize", size);
  if (HERO && !reduce) {
    /* load the lifelike 3D dragon where the device can draw it; otherwise the flag dragon stays */
    try {
      var tc = document.createElement("canvas"), gl3 = window.WebGLRenderingContext && (tc.getContext("webgl2") || tc.getContext("webgl"));
      /* skipped on data saver and on very old phones with 1 GB of memory or less (Ifan, 13 Nov 2026: keep it on every modern phone).
         deviceMemory is only reported by Chrome-based browsers; Safari never reports it, so iPhones always get the dragon. */
      var lowMem = navigator.deviceMemory && navigator.deviceMemory <= 1;
      /* old phones (1 GB of memory or less), data saver and browsers without WebGL get the still pictures too (Ifan, 13 Nov 2026) */
      if (SLOW || lowMem || !gl3 || (navigator.connection && navigator.connection.saveData)) {
        SLOW = true;
        var narrowS = Math.min(innerWidth, screen.width) < 1100, sky = SKY.sun > 0.5 ? "day" : "night";
        STILL_IMG.ref = narrowS ? STILL_REF.p : STILL_REF.w;
        var li = new Image(); li.onload = function () { STILL_IMG.land = li; }; li.onerror = function () { STILL_IMG.failed = 1; }; li.src = "hero-land-" + (narrowS ? "p" : "w") + "-" + sky + ".webp";
        var di = new Image(); di.onload = function () { STILL_IMG.dragon = di; }; di.src = "dragon-red.webp";
      } else if (gl3 && !lowMem && !(navigator.connection && navigator.connection.saveData)) {
        window.HCD3_WANT = window.HCL3_WANT = 1;
        var c3 = document.createElement("canvas"); c3.id = "sky3d"; c3.setAttribute("aria-hidden", "true"); cv.after(c3);
        var cl = document.createElement("canvas"); cl.id = "land3d"; cl.setAttribute("aria-hidden", "true"); cv.after(cl);
        /* the 3D scene starts downloading once the page itself has loaded, so the words, fonts and pictures come first on a slow phone */
        var go3 = function () {
          var s3 = document.createElement("script"); s3.type = "module"; s3.src = "hero3d.js?v=8"; /* raise the number whenever hero3d.js changes, so browsers fetch the new one */ s3.onerror = function () { window.HCD3_WANT = window.HCL3_WANT = 0; c3.remove(); cl.remove(); }; document.head.appendChild(s3);
          setTimeout(function () { if (!(window.HCD3 && HCD3.ready)) window.HCD3_WANT = 0; if (!(window.HCL3 && HCL3.ready)) { window.HCL3_WANT = 0; cl.remove(); } }, 15000);
        };
        if (document.readyState === "complete") go3(); else window.addEventListener("load", go3, { once: true });
      }
    } catch (e3) { window.HCD3_WANT = 0; }
    window.addEventListener("pointermove", function (e) { if (e.pointerType === "mouse") mouse = (e.clientX / window.innerWidth - 0.5) * 2; }, { passive: true });
    /* tap or click the dragon and it breathes fire */
    hEl.addEventListener("pointerdown", function (e) {
      if (e.target.closest("a, button")) return;
      var r = cv.getBoundingClientRect(), dx = e.clientX - r.left - DPOS.x, dy = e.clientY - r.top - DPOS.y;
      if (dx * dx + dy * dy < DPOS.r * DPOS.r) { fireAt = t0; nextFire = t0 + 9000; }
    });
    /* tilt the phone and the scene shifts a little. iOS asks permission for this, so it is left alone there. */
    if (window.DeviceOrientationEvent && typeof DeviceOrientationEvent.requestPermission !== "function") {
      window.addEventListener("deviceorientation", function (e) { if (e.gamma == null) return; var g = Math.max(-1, Math.min(1, e.gamma / 28)); mouse += (g * 1.6 - mouse) * 0.12; }, { passive: true });
    }
    requestAnimationFrame(loop);
  } else { window.addEventListener("scroll", function () { if (window.scrollY < H) draw(); }, { passive: true }); }
  size();

  /* ---------- Word strip: two rows. The top row drifts by itself and can be dragged, swiped or scrolled either way;
     the gold row under it always moves the opposite way (dragging or swiping the gold row works too, the other way round). */
  (function () {
    var m = document.getElementById("marquee"); if (!m) return;
    var nav = m.parentNode, under = nav.querySelector(".mq-under"), tr2 = under && under.firstElementChild;
    var tr = m.firstElementChild, hold = false, idle = 0, pos = 0, down = null, moved = false, last = 0, h2 = 0, seen = 0, off = 0;
    function half() { return tr.children[tr.children.length / 2].offsetLeft - tr.children[0].offsetLeft; }
    /* the gold row is four copies of the same words, so it loops after a quarter of its width. It follows how far the top
       row has moved (not where it is), so the top row's jump back to the start each loop doesn't show in the gold row. */
    function sync() {
      var d = m.scrollLeft - seen; seen = m.scrollLeft;
      if (!tr2) return; if (!h2) h2 = tr2.scrollWidth / 4; if (h2 <= 0) return;
      off = ((off + d) % h2 + h2) % h2; tr2.style.transform = "translate3d(" + (off - h2).toFixed(1) + "px,0,0)";
    }
    function shift(by) { var b = m.scrollLeft; m.scrollLeft = b + by; seen += m.scrollLeft - b; return m.scrollLeft - b; }
    function wrap() { var h = half(); if (h <= 0) return; if (m.scrollLeft >= h) shift(-h); else if (m.scrollLeft <= 0) shift(h); pos = m.scrollLeft; }
    function rest(ms) { idle = performance.now() + (ms || 2500); }
    m.addEventListener("scroll", function () { if (Math.abs(m.scrollLeft - pos) > 2) { wrap(); } sync(); }, { passive: true });
    window.addEventListener("resize", function () { h2 = 0; sync(); }, { passive: true });
    nav.addEventListener("pointerenter", function (e) { if (e.pointerType === "mouse") hold = true; });
    nav.addEventListener("pointerleave", function () { hold = false; rest(600); });
    m.addEventListener("touchstart", function () { rest(4000); }, { passive: true });
    m.addEventListener("touchmove", function () { rest(4000); }, { passive: true });
    m.addEventListener("wheel", function () { rest(); }, { passive: true });
    nav.addEventListener("focusin", function () { hold = true; }); nav.addEventListener("focusout", function () { hold = false; rest(); });
    /* mouse drag on either row; a finger on the gold row (the top row scrolls natively) */
    function grab(x, sign) { down = { x: x, s: m.scrollLeft, k: sign }; moved = false; }
    function drag(x) {
      var dx = (x - down.x) * down.k;
      if (!moved && Math.abs(dx) > 5) { moved = true; nav.classList.add("drag"); }
      if (moved) { m.scrollLeft = down.s - dx; sync(); var h = half(); if (m.scrollLeft <= 0) down.s += shift(h); else if (m.scrollLeft >= h) down.s += shift(-h); pos = m.scrollLeft; }
    }
    function drop() { if (!down) return; down = null; if (moved) { setTimeout(function () { nav.classList.remove("drag"); }, 0); rest(); } }
    nav.addEventListener("pointerdown", function (e) { if (e.pointerType !== "mouse" || e.button) return; grab(e.clientX, under && under.contains(e.target) ? -1 : 1); });
    window.addEventListener("pointermove", function (e) { if (down && down.mouse !== false) drag(e.clientX); });
    window.addEventListener("pointerup", drop);
    if (under) {
      under.addEventListener("touchstart", function (e) { grab(e.touches[0].clientX, -1); down.mouse = false; rest(4000); }, { passive: true });
      under.addEventListener("touchmove", function (e) { if (down) { drag(e.touches[0].clientX); rest(4000); } }, { passive: true });
      under.addEventListener("touchend", drop, { passive: true });
    }
    nav.addEventListener("click", function (e) { if (moved) { e.preventDefault(); moved = false; } }, true);
    nav.addEventListener("dragstart", function (e) { e.preventDefault(); });
    m.scrollLeft = pos = 1; seen = m.scrollLeft; sync();
    if (reduce) return;
    requestAnimationFrame(function step(t) {
      var dt = Math.min(50, t - (last || t)); last = t;
      if (!hold && !down && t > idle) { pos += dt * 0.04; var h = half(); if (h > 0 && pos >= h) { pos -= h; shift(-h); } m.scrollLeft = pos; sync(); }
      else pos = m.scrollLeft;
      requestAnimationFrame(step);
    });
  })();

  /* ---------- Count-up ticker ---------- */
  $$("[data-count]").forEach(function (el) {
    var target = +el.dataset.count, suf = el.dataset.suffix || "", st = null;
    if (reduce) return;
    function f(ts) { if (!st) st = ts; var p = Math.min(1, (ts - st) / 1600), k = 1 - Math.pow(1 - p, 3); el.textContent = Math.round(target * k).toLocaleString("en-GB") + suf; if (p < 1) requestAnimationFrame(f); }
    requestAnimationFrame(f);
  });

  /* ---------- Chapters ---------- */
  function renderChapters() {
    $("#chap-list").innerHTML = ERAS.map(function (e) {
      return '<button type="button" class="chap" data-era="' + e.id + '" data-open="' + e.id + '"><svg aria-hidden="true"><use href="#i-' + e.ill + '"/></svg><span class="span">' + T(e.spanEn, e.spanCy) + "</span><h3>" + T(e.en, e.cy) + "</h3><p>" + esc(T(e.blurbEn, e.blurbCy)) + "</p></button>";
    }).join("");
    $("#foot-eras").innerHTML = ERAS.map(function (e) { return '<a href="era-' + e.id + '.html">' + T(e.en, e.cy) + "</a>"; }).join("") + '<a href="trails.html">' + T("Trails", "Llwybrau") + '</a><a href="teachers.html">' + T("For teachers", "I athrawon") + '</a><a href="#sources">' + T("Sources", "Ffynonellau") + "</a>";
    $("#trail-list").innerHTML = D.TRAILS.map(function (t, i) { return '<a class="trail-card" href="trail-' + t.id + '.html" data-era="' + ERAS[i % ERAS.length].id + '"><svg aria-hidden="true"><use href="#i-' + t.ill + '"/></svg><span><b>' + esc(T(t.en, t.cy)) + "</b><span>" + t.n + " " + T("stops", "arhosfan") + "</span></span></a>"; }).join("");
  }

  /* ---------- Chapter overlay ---------- */
  var ov = $("#overlay"), lastFocus = null;
  function openChapter(id, push) {
    var e = ERA[id]; if (!e) return;
    var i = ERAS.indexOf(e), prev = ERAS[i - 1], next = ERAS[i + 1];
    var keys = EVENTS.filter(function (x) { return x[E_ERA] === id && x[E_KEY]; });
    var story = T(e.storyEn, e.storyCy);
    ov.innerHTML = '<div class="overlay" data-close="1"><div class="sheet" role="dialog" aria-modal="true" aria-labelledby="sh-t" data-era="' + id + '">' +
      '<button type="button" class="icon-btn close" data-close="1" aria-label="' + T("Close", "Cau") + '"><svg><use href="#i-x"/></svg></button>' +
      '<div class="top"><svg class="ill" aria-hidden="true"><use href="#i-' + e.ill + '"/></svg><p class="eyebrow">' + T("Chapter", "Pennod") + " " + (i + 1) + " · " + T(e.spanEn, e.spanCy) + '</p><h2 id="sh-t">' + T(e.en, e.cy) + "</h2></div>" +
      '<div class="body">' + story.map(function (p) { return "<p>" + esc(p) + "</p>"; }).join("") +
      '<div class="keys"><p class="eyebrow">' + T("Turning points", "Trobwyntiau") + "</p><ul>" + keys.map(function (k) { return "<li><time>" + yearLabel(k) + "</time><span><b>" + esc(T(k[E_TEN], k[E_TCY])) + "</b>. " + esc(T(k[E_BEN], k[E_BCY])) + "</span></li>"; }).join("") + "</ul></div>" +
      '<p><a class="btn" href="era-' + id + '.html">' + T("Open the full chapter page", "Agor tudalen lawn y bennod") + " →</a></p></div>" +
      '<div class="foot">' + (prev ? '<button type="button" class="btn" data-open="' + prev.id + '">← ' + T(prev.en, prev.cy) + "</button>" : "<span></span>") +
      (next ? '<button type="button" class="btn solid" data-open="' + next.id + '">' + T(next.en, next.cy) + " →</button>" : '<button type="button" class="btn solid" data-jump="' + id + '">' + T("See it on the timeline", "Gweld ar y llinell amser") + "</button>") + "</div></div></div>";
    ov.hidden = false; document.documentElement.style.overflow = "hidden";
    if (!lastFocus) lastFocus = document.activeElement;
    $(".sheet", ov).scrollTop = 0; $(".close", ov).focus();
    if (push !== false && location.hash !== "#pennod-" + id) { try { history.replaceState(null, "", "#pennod-" + id); } catch (er) {} }
  }
  function closeChapter() {
    if (ov.hidden) return;
    ov.hidden = true; ov.innerHTML = ""; document.documentElement.style.overflow = "";
    if (/^#pennod-/.test(location.hash)) { try { history.replaceState(null, "", location.pathname + location.search); } catch (er) {} }
    if (lastFocus) { lastFocus.focus(); lastFocus = null; }
  }
  function goTo(el, block) { if (el) el.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: block || "start" }); }
  document.addEventListener("click", function (ev) {
    var o = ev.target.closest("[data-open]"); if (o) { openChapter(o.dataset.open); return; }
    var j = ev.target.closest("[data-jump]"); if (j) { var id = j.dataset.jump; if (!HAS_TL) { location.href = "timeline.html#era-" + id; return; } closeChapter(); goTo($("#era-" + id)); return; }
    if (ev.target.closest("[data-close]") && (ev.target.dataset.close || ev.target.closest(".close"))) closeChapter();
    var m = ev.target.closest("[data-map]"); if (m) { if (!HAS_MAP) { location.href = "map.html#lle-" + m.dataset.map; return; } setMode("sites"); selectPlace(m.dataset.map); goTo($("#map")); }
    var t = ev.target.closest("[data-tl]"); if (t) { if (!HAS_TL) { location.href = "timeline.html#ev-" + t.dataset.tl; return; } if (tlEra !== "all") setTlEra("all"); goTo($("#ev-" + t.dataset.tl), "center"); }
    var c = ev.target.closest("[data-copy]"); if (c) copyLink(c);
  });
  function copyLink(btn) {
    var url = new URL(btn.dataset.copy, location.href).href, done = function () { var o = btn.textContent; btn.textContent = T("Copied", "Wedi copïo"); setTimeout(function () { btn.textContent = o; }, 1600); };
    try { navigator.clipboard.writeText(url).then(done, function () { window.prompt && done(); }); } catch (e) {}
  }
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape") closeChapter();
    if (ev.key === "Tab" && !ov.hidden) {
      var f = $$("button, a[href]", ov); if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (ev.shiftKey && document.activeElement === first) { ev.preventDefault(); last.focus(); }
      else if (!ev.shiftKey && document.activeElement === last) { ev.preventDefault(); first.focus(); }
    }
  });
  function route() {
    if (HERO && !HAS_MAP && /^#lle-/.test(location.hash)) { location.replace("map.html" + location.hash); return; }
    if (HERO && /[?&]field=/.test(location.search)) { location.replace("people.html" + location.search); return; }
    if (HAS_MAP && /^#(kingdoms|teyrnasoedd)$/.test(location.hash)) { setMode("kg"); }
    var m = /^#pennod-(\w+)/.exec(location.hash); if (m && ERA[m[1]]) { openChapter(m[1], false); return; }
    closeChapter();
    if (HERO && /^#(quiz|game)$/.test(location.hash)) { location.replace("quiz.html" + location.hash); return; }
    var q = /^#(ev-\d+|era-(\w+))$/.exec(location.hash);
    if (q && HAS_TL) { if (q[2] && ERA[q[2]]) { setTlEra(q[2]); } else if (tlEra !== "all") setTlEra("all"); setTimeout(function () { if (q[2]) window.scrollTo(0, 0); else goTo(document.getElementById(q[1]), "center"); }, 60); }
    var p = /^#lle-([\w-]+)/.exec(location.hash); if (p && PLACE[p[1]]) { setMode("sites"); selectPlace(p[1]); setTimeout(function () { goTo($("#map")); }, 50); }
  }
  window.addEventListener("hashchange", route);

  /* ---------- Chips ---------- */
  function chips(el, cur, onPick, counts) {
    el.innerHTML = '<button type="button" class="chip" data-v="all" aria-pressed="' + (cur === "all") + '">' + T("All", "Y cyfan") + "</button>" +
      ERAS.filter(function (e) { return !counts || counts[e.id]; }).map(function (e) { return '<button type="button" class="chip" data-era="' + e.id + '" data-v="' + e.id + '" aria-pressed="' + (cur === e.id) + '"><i></i>' + T(e.en, e.cy) + ' <span class="c-dates">' + T(e.spanEn, e.spanCy) + "</span>" + (counts ? ' <span style="opacity:.7">' + counts[e.id] + "</span>" : "") + "</button>"; }).join("");
    el.onclick = function (ev) { var b = ev.target.closest(".chip"); if (b) onPick(b.dataset.v); };
  }

  /* ---------- On this day ---------- */
  // Until onthisday.json arrives (or if it cannot load) the panel uses the dated timeline events.
  // The JSON adds saints' days, traditions, births and deaths for nearly every day; ‹ › step through the year.
  var OTD = null, otdDay = null, otdAll = false;
  var OTD_TAG = { born: ["Born", "Ganed"], died: ["Died", "Bu farw"], feast: ["Feast day", "Dydd gŵyl"], custom: ["Tradition", "Traddodiad"] };
  function mdOf(d) { return ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  function dateOf(md) { return new Date(2024, +md.slice(0, 2) - 1, +md.slice(3)); }  // a leap year, so 29 February is a day too
  function stepDay(md, n) { var d = dateOf(md); d.setDate(d.getDate() + n); return mdOf(d); }
  function dayLabel(md, short) { var m = +md.slice(0, 2) - 1, d = +md.slice(3); return d + " " + (short ? T(MONTHS_EN[m].slice(0, 3), MONTHS_CY[m]) : T(MONTHS_EN[m], MONTHS_CY[m])); }
  var HAS_OTD = !!document.getElementById("today-box");
  var WD = [["Sun", "Sul"], ["Mon", "Llun"], ["Tue", "Maw"], ["Wed", "Mer"], ["Thu", "Iau"], ["Fri", "Gwe"], ["Sat", "Sad"]];
  if (HAS_OTD) {
    fetch("onthisday.json").then(function (r) { if (!r.ok) throw r; return r.json(); }).then(function (d) { OTD = d; renderToday(); }).catch(function () {});
    $("#today-box").addEventListener("click", function (ev) {
      var w = ev.target.closest("[data-otd-day]"), b = ev.target.closest("[data-otd]"), today = mdOf(new Date());
      if (w) { otdDay = w.dataset.otdDay === today ? null : w.dataset.otdDay; otdAll = false; renderToday(); var f0 = $("#today-box [data-otd-day='" + w.dataset.otdDay + "']"); if (f0) f0.focus(); return; }
      if (!b) return;
      var v = b.dataset.otd;
      otdDay = v === "today" ? null : v === "more" ? otdDay : stepDay(otdDay || today, +v);
      if (otdDay === today) otdDay = null;
      otdAll = v === "more"; renderToday();
      if (v !== "more") { var f = $("#today-box [data-otd='" + v + "']"); if (f) f.focus(); }
    });
  }
  // One row: its picture, when, the title and a line. The whole row is one link (see "Whole cards are links" in SKILLS.md); build.py draws the same.
  function otdLi(r, showDate) {
    var tag = OTD_TAG[r[2]], bits = [];
    if (showDate) bits.push('<span class="dt">' + dayLabel(r[0], true) + "</span>");
    if (r[1] != null) bits.push('<span class="y">' + r[1] + "</span>");
    if (tag) bits.push('<span class="k">' + T(tag[0], tag[1]) + "</span>");
    var t = esc(T(r[3], r[4])), href = r[7] || "onthisday.html#d-" + r[0];
    var pic = r[9] || "i:castle";  // "i:<icon>": no picture of its own, so a small drawing (build.py otd_pic)
    var bg = r[10] || (pic.slice(0, 2) === "i:" ? "" : pic);  // the darkened picture behind the row (build.py otd_bg)
    return '<li class="otd-row wl-card pbg" data-era="' + r[8] + '"' + (bg ? ' style="--pbg:url(\'' + esc(bg) + '\')"' : "") + '>' + (pic.slice(0, 2) === "i:" ? '<span class="otd-pic otd-ic" aria-hidden="true"><svg><use href="#i-' + pic.slice(2) + '"/></svg></span>' :
      '<span class="otd-pic"><img src="' + esc(pic) + '" alt="" width="96" height="96" loading="lazy" decoding="async"></span>') +
      '<div class="otd-txt"><p class="otd-meta">' + bits.join("") + "</p><h3>" + t + "</h3><p>" + esc(T(r[5], r[6])) + '</p></div><a class="wl" href="' + esc(href) + '">' + t + "</a></li>";
  }
  function renderToday() {
    if (!HAS_OTD || !OTD) return;  // until onthisday.json arrives, the panel build.py wrote stays
    var md = mdOf(new Date()), day = otdDay || md, isToday = day === md;
    var at = function (x) { return OTD.filter(function (r) { return r[0] === x; }); };
    var hit = at(day), near = null;
    if (!hit.length) {  // nothing on this exact day: show the closest dates either side
      for (var k = 1; k < 200 && !near; k++) {
        var ha = at(stepDay(day, -k)), hb = at(stepDay(day, k));
        if (ha.length || hb.length) near = ha.slice(0, 2).concat(hb.slice(0, 2));
      }
    }
    var list = hit.length ? hit : near || [], shown = otdAll || list.length <= 3 ? list : list.slice(0, 3);
    var m = +day.slice(0, 2) - 1, week = "";
    for (var i = -3; i <= 3; i++) {
      var dm = stepDay(day, i), dd = dateOf(dm), n = Math.min(at(dm).length, 3), dots = "";
      dd.setFullYear(new Date().getFullYear());
      for (var j = 0; j < n; j++) dots += "<b></b>";
      week += '<button type="button" class="otd-wd' + (i === 0 ? " on" : "") + (n ? " has" : "") + (dm === md ? " is-today" : "") + '" data-otd-day="' + dm + '" aria-pressed="' + (i === 0) + '" aria-label="' + T(WD[dd.getDay()][0], WD[dd.getDay()][1]) + " " + dayLabel(dm) + '">' + /* the label starts with the words on the button (WCAG 2.5.3) */
        '<span class="w">' + T(WD[dd.getDay()][0], WD[dd.getDay()][1]) + '</span> <span class="n">' + +dm.slice(3) + '</span><i aria-hidden="true">' + dots + "</i></button>";
    }
    var pic = (shown.filter(function (r) { return r[9] && r[9].slice(0, 2) !== "i:"; })[0] || [])[9];  // the first real picture, or none
    $("#today-box").innerHTML = '<div class="otd-head">' + (pic ? '<img class="otd-bg" src="' + esc(pic) + '" alt="" decoding="async">' : "") +
      '<p class="otd-date"><span class="d">' + +day.slice(3) + '</span><span class="m">' + T(MONTHS_EN[m], MONTHS_CY[m]) + '</span><span class="lab">' +
      (isToday ? T("Today", "Heddiw") : '<button type="button" class="otd-back" data-otd="today">' + T("Back to today", "Yn ôl i heddiw") + "</button>") + "</span></p>" +
      '<span class="otd-nav"><button type="button" data-otd="-1" aria-label="' + T("Day before", "Y diwrnod cynt") + '">‹</button><button type="button" data-otd="1" aria-label="' + T("Next day", "Y diwrnod nesaf") + '">›</button></span></div>' +
      '<div class="otd-week" role="group" aria-label="' + T("Choose a day", "Dewiswch ddiwrnod") + '">' + week + "</div>" +
      '<div class="otd-body" aria-live="polite">' + (hit.length ? "" : '<p class="otd-near">' + T("Nothing we know of happened on exactly this day. Here are the nearest dates.", "Ni wyddom am ddim a ddigwyddodd ar union y diwrnod hwn. Dyma’r dyddiadau agosaf.") + "</p>") +
      '<ul class="otd-rows">' + shown.map(function (r) { return otdLi(r, !hit.length); }).join("") + "</ul>" +
      (shown.length < list.length ? '<button type="button" class="otd-more" data-otd="more">+' + (list.length - shown.length) + " " + T("more on this day", "arall ar y dydd hwn") + "</button>" : "") + "</div>" +
      '<a class="otd-year" href="onthisday.html#d-' + (hit.length ? day : list[0] ? list[0][0] : day) + '"><span class="ic" aria-hidden="true"><b>' + OTD.length + "</b></span>" +
      '<span class="t"><b>' + T("The whole year", "Y flwyddyn gyfan") + "</b><small>" + T(OTD.length + " dates, day by day", OTD.length + " o ddyddiadau, fesul diwrnod") + '</small></span><span class="ar" aria-hidden="true">→</span></a>';
  }

  /* ---------- Timeline ---------- */
  var tlEra = "all", evEls = [], active = -1, shownYear = EVENTS[0][E_Y], yrAnim = null;
  function setTlEra(v) { tlEra = v; renderTimeline(); }
  function renderTimeline() {
    var counts = {}; EVENTS.forEach(function (e) { counts[e[E_ERA]] = (counts[e[E_ERA]] || 0) + 1; });
    if (!HAS_TL) {
      $("#tl-teaser").innerHTML = '<a class="chip" href="timeline.html">' + T("All", "Y cyfan") + ' <span style="opacity:.7">' + EVENTS.length + "</span></a>" +
        ERAS.map(function (e) { return '<a class="chip" data-era="' + e.id + '" href="timeline.html#era-' + e.id + '"><i></i>' + T(e.en, e.cy) + ' <span class="c-dates">' + T(e.spanEn, e.spanCy) + "</span></a>"; }).join("");
      return;
    }
    chips($("#tl-filter"), tlEra, setTlEra, counts);
    var html = "", last = null, n = 0;
    EVENTS.forEach(function (e, i) {
      if (tlEra !== "all" && e[E_ERA] !== tlEra) return;
      n++;
      if (e[E_ERA] !== last) { var E = ERA[e[E_ERA]]; html += '<li class="era-head" id="era-' + E.id + '" data-era="' + E.id + '"><span class="eyebrow">' + T(E.spanEn, E.spanCy) + "</span><h3>" + T(E.en, E.cy) + '</h3><button type="button" data-open="' + E.id + '">' + T("Read the chapter", "Darllen y bennod") + "</button></li>"; last = e[E_ERA]; }
      html += '<li class="ev' + (D.EVS ? " wl-card" : "") + (e[E_KEY] ? " key" : "") + '" id="ev-' + i + '" data-i="' + i + '" data-era="' + e[E_ERA] + '"><time>' + yearLabel(e) + "</time><h4>" + esc(T(e[E_TEN], e[E_TCY])) + "</h4><p>" + esc(T(e[E_BEN], e[E_BCY])) + '</p><div class="links">' +
        (D.EVS ? '<a class="wl" href="event-' + D.EVS[i] + '.html">' + esc(T(e[E_TEN], e[E_TCY])) + "</a>" : "") +
        (e[E_PLACE] ? '<button type="button" class="maplink" data-map="' + e[E_PLACE] + '"><svg aria-hidden="true"><use href="#i-pin"/></svg>' + T("See it on the map", "Gweld ar y map") + "</button>" : "") + "</div></li>";
    });
    $("#events").innerHTML = html;
    $("#tl-count").textContent = n + " " + T("events", "digwyddiad");
    evEls = $$("#events .ev"); active = -1;
    $("#dial-bar").innerHTML = ERAS.map(function (E) { return '<div data-era="' + E.id + '" style="--n:' + counts[E.id] + '"><i></i></div>'; }).join("");
    onScroll();
  }
  function showYear(e) {
    var to = e[E_Y], from = shownYear, el = $("#dial-yr"), st = null;
    function paint(v) { var neg = v < 0, a = Math.round(Math.abs(v)); el.innerHTML = (e[E_C] ? '<small style="margin:0 .2em 0 0">c.</small>' : "") + fmt(a) + (neg ? "<small>" + T("BC", "CC") + "</small>" : (a < 1000 ? "<small>" + T("AD", "OC") + "</small>" : "")); }
    if (yrAnim) cancelAnimationFrame(yrAnim);
    if (reduce || from === to) { shownYear = to; paint(to); return; }
    function f(ts) { if (!st) st = ts; var p = Math.min(1, (ts - st) / 550), k = 1 - Math.pow(1 - p, 3); var v = from + (to - from) * k; shownYear = v; paint(v); if (p < 1) yrAnim = requestAnimationFrame(f); else { shownYear = to; paint(to); } }
    yrAnim = requestAnimationFrame(f);
  }
  function setActive(idx, force) {
    if ((idx === active && !force) || !evEls[idx]) return;
    if (evEls[active]) evEls[active].classList.remove("on");
    active = idx; var el = evEls[idx]; el.classList.add("on");
    var e = EVENTS[+el.dataset.i], E = ERA[e[E_ERA]];
    showYear(e);
    $("#dial").setAttribute("data-era", e[E_ERA]);
    $("#dial-era").textContent = T(E.en, E.cy);
    $("#dial-now").textContent = T(e[E_TEN], e[E_TCY]);
    var seen = {}, tot = {}; EVENTS.forEach(function (x, j) { tot[x[E_ERA]] = (tot[x[E_ERA]] || 0) + 1; if (j <= +el.dataset.i) seen[x[E_ERA]] = (seen[x[E_ERA]] || 0) + 1; });
    $$("#dial-bar div").forEach(function (b) { var id = b.dataset.era; b.firstChild.style.setProperty("--p", (seen[id] || 0) / tot[id]); });
  }
  var ticking = false;
  function onScroll() {
    if (ticking) return; ticking = true;
    requestAnimationFrame(function () {
      ticking = false;
      var mid = window.innerHeight * 0.45, best = 0, bd = 1e9;
      for (var i = 0; i < evEls.length; i++) { var r = evEls[i].getBoundingClientRect(); var dd = Math.abs(r.top + r.height / 2 - mid); if (dd < bd) { bd = dd; best = i; } if (r.top > window.innerHeight) break; }
      setActive(best);
      var secs = ["chapters", "stories", "map", "people", "legends", "language", "play", "sources"], cur = null;
      secs.forEach(function (s) { var el = document.getElementById(s); if (!el) return; var r = el.getBoundingClientRect(); if (r.top < window.innerHeight * 0.4) cur = s; });
      if (HERO) $$(".nav-inline a").forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "index.html#" + cur); });
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- Map: sites ---------- */
  var mapEra = "all", sel = "caernarfon", mode = "sites";
  function proj(lat, lon) { return [(lon - MAPC.minx) * MAPC.k * MAPC.sc, (MAPC.maxy - lat) * MAPC.sc]; }
  function renderGrat() {
    var g = "";
    [51.5, 52, 52.5, 53].forEach(function (la) { var y = proj(la, 0)[1]; g += '<path class="grat" d="M-30 ' + y.toFixed(1) + 'H640"/><text class="grat-l" x="640" y="' + (y - 5).toFixed(1) + '" text-anchor="end">' + la.toFixed(1) + "°N</text>"; });
    [-5, -4, -3].forEach(function (lo) { var x = proj(52, lo)[0]; g += '<path class="grat" d="M' + x.toFixed(1) + ' -20V700"/><text class="grat-l" x="' + (x + 5).toFixed(1) + '" y="-12">' + Math.abs(lo) + "°W</text>"; });
    $("#grat").innerHTML = g;
  }
  function renderPins() {
    var counts = {}; PLACES.forEach(function (p) { counts[p.era] = (counts[p.era] || 0) + 1; });
    chips($("#map-filter"), mapEra, function (v) { mapEra = v; renderPins(); if (mapEra !== "all" && PLACE[sel].era !== mapEra) selectPlace(PLACES.filter(function (p) { return p.era === mapEra; })[0].id); }, counts);
    $("#pins").innerHTML = PLACES.map(function (p) {
      var xy = proj(p.lat, p.lon), right = xy[0] > 430;
      return '<g class="pin' + (p.id === sel ? " sel" : "") + (mapEra !== "all" && p.era !== mapEra ? " dim" : "") + '" data-era="' + p.era + '" data-pid="' + p.id + '" tabindex="0" role="button" aria-label="' + esc(T(p.en, p.cy)) + '" transform="translate(' + xy[0].toFixed(1) + " " + xy[1].toFixed(1) + ')">' +
        '<circle class="halo" r="20"/><circle class="dot" r="7"/><text class="lbl" x="' + (right ? -14 : 14) + '" y="4" text-anchor="' + (right ? "end" : "start") + '">' + esc(T(p.en, p.cy)) + "</text></g>";
    }).join("");
  }
  function cap(s) { return s ? s.charAt(0).toUpperCase() + s.slice(1) : s; }
  function selectPlace(id) {
    if (!PLACE[id]) return;
    sel = id; var p = PLACE[id], E = ERA[p.era];
    if (mapEra !== "all" && p.era !== mapEra) mapEra = "all";
    renderPins();
    var visible = PLACES.filter(function (x) { return mapEra === "all" || x.era === mapEra; }), i = visible.indexOf(p);
    var evIdx = -1; EVENTS.forEach(function (e, j) { if (e[E_PLACE] === id && evIdx < 0) evIdx = j; });
    var other = lang === "en" ? p.cy : p.en;
    var card = $("#place-card"); card.setAttribute("data-era", p.era);
    var art = p.ph ? '<div class="art has-photo"><img src="' + p.ph[0] + '" alt="' + esc(T(p.ph[2], p.ph[3])) + '" referrerpolicy="no-referrer" onerror="var a=this.parentNode;a.className=\'art\';a.innerHTML=\'<svg aria-hidden=&quot;true&quot;><use href=&quot;#i-' + p.ill + '&quot;/></svg>\'"></div>' : '<div class="art"><svg aria-hidden="true"><use href="#i-' + p.ill + '"/></svg></div>';
    card.innerHTML = art +
      '<div style="display:grid;gap:.3rem"><h3>' + esc(T(p.en, p.cy)) + "</h3>" + (other !== T(p.en, p.cy) ? '<span class="cy-name">' + esc(other) + "</span>" : "") + "</div>" +
      '<div class="meta"><span><b>' + T(E.en, E.cy) + "</b></span><span>" + esc(p.year) + "</span><span>" + p.lat.toFixed(3) + "° N, " + Math.abs(p.lon).toFixed(3) + "° W</span></div>" +
      '<p class="desc">' + esc(T(p.dEn, p.dCy)) + "</p>" + (p.vis ? '<p class="pc-visit"><b>' + T("Visit", "Ymweld") + ':</b> ' + esc(cap(T(p.vis[0], p.vis[1]))) + " · " + esc(T(p.vis[3], p.vis[4])) + (p.vis[5] ? " · " + esc(p.vis[5]) : "") + (p.vis[2] ? ' · <a href="' + esc(p.vis[2]) + '" target="_blank" rel="noopener">' + T("Times and prices", "Amseroedd a phrisiau") + " ↗</a>" : "") + ' · <a href="' + esc(p.vis[6]) + '" target="_blank" rel="noopener">' + T("Directions", "Cyfarwyddiadau") + " ↗</a></p>" : "") + '<div style="display:flex;gap:1.2rem;flex-wrap:wrap;align-items:center"><a class="wl" href="place-' + p.id + '.html">' + esc(T(p.en, p.cy)) + "</a>" + (p.ph ? '<a class="credit" href="' + p.ph[1] + '" target="_blank" rel="noopener">' + T("Photo: Wikimedia Commons", "Llun: Wikimedia Commons") + " ↗</a>" : "") + "</div>" +
      '<div class="row">' + (evIdx >= 0 ? '<button type="button" class="btn" data-tl="' + evIdx + '">' + T("See it on the timeline", "Gweld ar y llinell amser") + "</button>" : "<span></span>") +
      '<div class="nav-btns"><button type="button" class="icon-btn" id="pl-prev" aria-label="' + T("Previous place", "Lle blaenorol") + '"><svg><use href="#i-left"/></svg></button><span class="people-count" style="align-self:center;min-width:3.2rem;text-align:center">' + (i + 1) + " / " + visible.length + '</span><button type="button" class="icon-btn" id="pl-next" aria-label="' + T("Next place", "Lle nesaf") + '"><svg><use href="#i-right"/></svg></button></div></div>';
    $("#pl-prev").onclick = function () { selectPlace(visible[(i - 1 + visible.length) % visible.length].id); };
    $("#pl-next").onclick = function () { selectPlace(visible[(i + 1) % visible.length].id); };
  }
  $("#pins").addEventListener("click", function (ev) { var g = ev.target.closest(".pin"); if (g) selectPlace(g.dataset.pid); });
  $("#pins").addEventListener("keydown", function (ev) { var g = ev.target.closest(".pin"); if (g && (ev.key === "Enter" || ev.key === " ")) { ev.preventDefault(); selectPlace(g.dataset.pid); var n = $('.pin[data-pid="' + g.dataset.pid + '"]'); if (n) n.focus(); } });

  /* ---------- Map: kingdoms ---------- */
  var kgStage = 5, kgTimer = 0, kgDrag = false;
  function kgStop() { if (kgTimer) { clearInterval(kgTimer); kgTimer = 0; } }
  function renderLAs() { $("#las").innerHTML = Object.keys(D.LA).map(function (n) { return '<path class="la" data-la="' + esc(n) + '" d="' + D.LA[n] + '"><title>' + esc(n) + "</title></path>"; }).join(""); }
  function renderKg() {
    var K = D.KINGDOMS[kgStage], colour = {};
    K.groups.forEach(function (g) { (g[3] === "*" ? Object.keys(D.LA) : g[3]).forEach(function (n) { colour[n] = g[2]; }); });
    $$("#las .la").forEach(function (p) { p.style.fill = colour[p.dataset.la] || "#2a3142"; p.style.stroke = colour[p.dataset.la] || ""; });
    /* a name on the map for each realm, placed at the middle of its land */
    var labels = K.groups.map(function (g) {
      var name = g[4] ? T(g[4][0], g[4][1]) : T(g[0], g[1]); if (!name) return "";
      var sx = 0, sy = 0, sa = 0;
      $$("#las .la").forEach(function (p) { if (g[3] !== "*" && g[3].indexOf(p.dataset.la) < 0) return; var b = p.getBBox(), a = b.width * b.height; sx += (b.x + b.width / 2) * a; sy += (b.y + b.height / 2) * a; sa += a; });
      return sa ? '<text class="kg-label" x="' + (sx / sa).toFixed(0) + '" y="' + (sy / sa).toFixed(0) + '">' + esc(name) + "</text>" : "";
    }).join("");
    $("#kg-labels").innerHTML = labels;
    var card = $("#kg-card"), N = D.KINGDOMS.length;
    /* The card is built once per language and then only updated, so the slider is never
       replaced while someone is dragging it (replacing it mid-drag is what made it hard to move). */
    if (card.dataset.lang !== lang || !$("#kg-in")) { card.dataset.lang = lang; kgShell(card, N); }
    kgText(card, K);
    [].forEach.call(card.querySelectorAll(".kg-ticks span"), function (t, n) { t.classList.toggle("on", n === kgStage); });
    var inp = $("#kg-in"); inp.setAttribute("aria-valuetext", T(K.en, K.cy));
    if (!kgDrag) { inp.value = kgStage; kgFill(kgStage); }
    $("#kg-play").textContent = kgTimer ? T("Pause", "Oedi") : "▶ " + T("Play through time", "Chwarae drwy amser");
  }
  function kgText(card, K) {
    card.querySelector(".kg-stage").textContent = T(K.en, K.cy);
    card.querySelector(".kg-desc").textContent = T(K.nEn, K.nCy);
    card.querySelector(".kg-legend").innerHTML = K.groups.map(function (g) { var u = (D.KGLINK || {})[g[0]], n = esc(T(g[0], g[1])); return '<li style="--k:' + g[2] + '"><i></i>' + (u ? '<a href="' + u + '">' + n + "</a>" : n) + "</li>"; }).join("");
  }
  function kgYear(k) { return k.id === "today" ? T("Now", "Nawr") : k.id.replace("c", ""); }
  function kgFill(v) { var w = document.querySelector(".kg-slide"); if (w) w.style.setProperty("--f", (v / (D.KINGDOMS.length - 1)).toFixed(4)); }
  function kgGo(n) {
    n = Math.max(0, Math.min(D.KINGDOMS.length - 1, n));
    var changed = n !== kgStage || !!kgTimer;
    kgStop();
    if (changed) { kgStage = n; renderKg(); }
  }
  /* glide the thumb onto the nearest year once the finger or mouse lets go */
  function kgSnap() {
    var inp = $("#kg-in"); if (!inp) return;
    var from = +inp.value, to = kgStage, t0 = performance.now();
    if (Math.abs(from - to) < .01 || matchMedia("(prefers-reduced-motion: reduce)").matches) { inp.value = to; kgFill(to); return; }
    (function step(now) {
      if (kgDrag) return;
      var k = Math.min(1, (now - t0) / 160), v = from + (to - from) * (1 - Math.pow(1 - k, 3));
      inp.value = v; kgFill(v); if (k < 1) requestAnimationFrame(step);
    })(t0);
  }
  function kgShell(card, N) {
    /* the slider comes first: nothing above it changes, so it never moves while it is dragged */
    card.innerHTML = '<p class="eyebrow">' + T("The changing map", "Y map yn newid") + "</p>" +
      '<div class="kg-range"><label for="kg-in" class="eyebrow">' + T("Move through time", "Symud drwy amser") + "</label>" +
      '<div class="kg-slide" style="--n:' + (N - 1) + '"><input type="range" id="kg-in" min="0" max="' + (N - 1) + '" step="any" value="' + kgStage + '">' +
      '<div class="kg-ticks" aria-hidden="true">' + D.KINGDOMS.map(function (k, n) { return '<span style="--i:' + n + '">' + kgYear(k) + "</span>"; }).join("") + "</div></div>" +
      '<p class="kg-hint">' + T("Drag the slider, or tap a year to jump to it.", "Llusgwch y llithrydd, neu tapiwch flwyddyn i neidio ati.") + "</p>" +
      '<div class="kg-btns"><button type="button" class="btn" id="kg-prev" aria-label="' + T("Earlier", "Cynharach") + '">←</button><button type="button" class="btn solid" id="kg-play"></button><button type="button" class="btn" id="kg-next" aria-label="' + T("Later", "Diweddarach") + '">→</button></div></div>' +
      '<div class="kg-body"><h3 class="kg-stage"></h3><p class="desc kg-desc"></p><ul class="kg-legend"></ul></div>' +
      '<p class="kg-kings"><a href="kings.html">' + T("Every king and prince of Wales", "Pob brenin a thywysog yng Nghymru") + " →</a></p>" +
      '<p class="kg-note">' + T("Approximate: borders are drawn using modern council areas as building blocks.", "Bras: lluniwyd y ffiniau gan ddefnyddio ardaloedd cynghorau modern.") + "</p>";
    var inp = $("#kg-in"), slide = card.querySelector(".kg-slide");
    /* The whole strip (track and years) takes the pointer, so a tap or drag anywhere on it works,
       with a mouse or a finger. The input itself keeps the keyboard and screen readers. */
    function valAt(x) {
      var r = inp.getBoundingClientRect(), th = parseFloat(getComputedStyle(slide).getPropertyValue("--th")) || 32;
      var f = (x - r.left - th / 2) / Math.max(1, r.width - th);
      return Math.max(0, Math.min(1, f)) * (N - 1);
    }
    function move(ev) { var v = valAt(ev.clientX); inp.value = v; kgFill(v); kgGo(Math.round(v)); }
    slide.addEventListener("pointerdown", function (ev) {
      if (ev.button > 0) return;
      ev.preventDefault(); kgDrag = true; slide.classList.add("drag");
      try { slide.setPointerCapture(ev.pointerId); } catch (e) {}
      inp.focus({ preventScroll: true }); move(ev);
    });
    slide.addEventListener("pointermove", function (ev) { if (kgDrag) move(ev); });
    function end() { if (!kgDrag) return; kgDrag = false; slide.classList.remove("drag"); kgSnap(); }
    slide.addEventListener("pointerup", end); slide.addEventListener("pointercancel", end); slide.addEventListener("lostpointercapture", end);
    /* screen readers, and anything else that sets the value directly */
    inp.addEventListener("input", function () { if (!kgDrag) kgGo(Math.round(+inp.value)); });
    inp.addEventListener("change", function () { if (!kgDrag) kgSnap(); });
    inp.addEventListener("keydown", function (ev) {
      var d = { ArrowLeft: -1, ArrowDown: -1, ArrowRight: 1, ArrowUp: 1, PageDown: -3, PageUp: 3, Home: -N, End: N }[ev.key];
      if (d) { ev.preventDefault(); kgGo(kgStage + d); }
    });
    $("#kg-prev").onclick = function () { kgGo(kgStage - 1); };
    $("#kg-next").onclick = function () { kgGo(kgStage + 1); };
    $("#kg-play").onclick = function () {
      if (kgTimer) { kgStop(); renderKg(); return; }
      kgStage = kgStage >= N - 1 ? 0 : kgStage + 1;
      kgTimer = setInterval(function () { if (kgStage >= N - 1) kgStop(); else kgStage++; renderKg(); }, 2600);
      renderKg();
    };
  }
  function setMode(m) {
    mode = m;
    $("#mode-sites").setAttribute("aria-pressed", m === "sites"); $("#mode-kg").setAttribute("aria-pressed", m === "kg");
    /* SVG elements have no .hidden property in every browser, so set the attribute itself */
    $("#las").toggleAttribute("hidden", m !== "kg"); $("#kg-labels").toggleAttribute("hidden", m !== "kg"); if (m !== "kg") kgStop(); $("#pins").style.display = m === "kg" ? "none" : ""; $("#map-filter").hidden = m === "kg";
    $("#place-card").hidden = m === "kg"; $("#kg-card").hidden = m !== "kg";
    if (m === "kg") renderKg();
  }
  $("#mode-sites").onclick = function () { setMode("sites"); };
  $("#mode-kg").onclick = function () { setMode("kg"); };

  /* ---------- People ---------- */
  var P_PAGE = !!(document.getElementById("people-grid") && document.getElementById("people-grid").dataset.all);  /* people.html: show everyone */
  var pEra = "all", pAll = P_PAGE, pField = "all";
  try { var qf = new URLSearchParams(location.search).get("field"); if (qf && (qf === "first" || (D.PFIELDS || []).some(function (f) { return f[0] === qf; }))) pField = qf; } catch (e) {}
  function fieldOk(p) { return pField === "all" || (pField === "first" ? !!(D.PFIRST || {})[p[0]] : (D.PFIELD || {})[p[0]] === pField); }
  function fieldChips() {
    var el = $("#people-field"); if (!el || !D.PFIELDS) return;
    var fc = {}, nf = 0; PEOPLE.forEach(function (p) { if (pEra !== "all" && p[1] !== pEra) return; var f = D.PFIELD[p[0]]; fc[f] = (fc[f] || 0) + 1; if (D.PFIRST[p[0]]) nf++; });
    el.innerHTML = '<button type="button" class="chip" data-v="all" aria-pressed="' + (pField === "all") + '">' + T("Every field", "Pob maes") + "</button>" +
      '<button type="button" class="chip star" data-v="first" aria-pressed="' + (pField === "first") + '">★ ' + T("Firsts", "Y cyntaf") + ' <span style="opacity:.7">' + nf + "</span></button>" +
      D.PFIELDS.filter(function (f) { return fc[f[0]]; }).map(function (f) { return '<button type="button" class="chip" data-v="' + f[0] + '" aria-pressed="' + (pField === f[0]) + '">' + esc(T(f[1], f[2])) + ' <span style="opacity:.7">' + fc[f[0]] + "</span></button>"; }).join("");
    el.onclick = function (ev) { var b = ev.target.closest(".chip"); if (b) { pField = b.dataset.v; renderPeople(); } };
  }
  function initials(n) { var w = n.replace(/\b(ap|ab|ferch|the|of|yr|y)\b/gi, " ").trim().split(/\s+/); return (w[0].charAt(0) + (w.length > 1 ? w[w.length - 1].charAt(0) : "")).toUpperCase(); }
  function renderPeople() {
    var counts = {}; PEOPLE.forEach(function (p) { counts[p[1]] = (counts[p[1]] || 0) + 1; });
    chips($("#people-filter"), pEra, function (v) { pEra = v; renderPeople(); }, counts);
    fieldChips();
    var list = PEOPLE.filter(function (p) { return (pEra === "all" || p[1] === pEra) && fieldOk(p); }), total = list.length;
    var short = pEra === "all" && pField === "all" && !pAll;
    if (short) list = D.FEATURED.slice(0, matchMedia("(max-width: 700px)").matches ? 6 : 12).map(function (s) { return PEOPLE.filter(function (p) { return p[0] === s; })[0]; }).filter(Boolean);
    $("#people-count").textContent = short ? T(list.length + " of " + total + " people", list.length + " o " + total + " o bobl") : total + " " + T("people", "o bobl");
    var more = $("#people-more"); more.hidden = P_PAGE || pEra !== "all" || pField !== "all"; more.textContent = pAll ? T("Show fewer", "Dangos llai") : T("Show all " + PEOPLE.length + " people", "Dangos pob un o’r " + PEOPLE.length);
    $("#people-grid").innerHTML = list.map(function (p) {
      var name = T(p[3], p[4]), other = lang === "en" ? p[4] : p[3], link = "person-" + p[0] + ".html", ph = D.PPH[p[0]];
      return '<article class="plaque wl-card" data-era="' + p[1] + '"><div class="top-row"><span class="ava" aria-hidden="true">' + initials(p[3]) + (ph ? '<img src="' + ph + '" alt="" width="96" height="96" loading="lazy" referrerpolicy="no-referrer" onerror="this.remove()">' : "") + '</span><div><span class="dates">' + esc(p[2]) + "</span><h3>" + esc(name) + '</h3></div></div><span class="epi">' + esc(T(p[5], p[6])) + (other !== name ? " · " + esc(other) : "") + "</span>" + ((D.PFIRST || {})[p[0]] ? '<span class="first-tag">★ ' + esc(T(D.PFIRST[p[0]][1], D.PFIRST[p[0]][2])) + "</span>" : "") + "<p>" + esc(T(p[7], p[8])) + '</p><a class="wl" href="' + link + '">' + esc(name) + "</a></article>";
    }).join("");
  }
  $("#people-more").onclick = function () { pAll = !pAll; renderPeople(); if (!pAll) goTo($("#people")); };

  /* ---------- Did you know? + daily streak ---------- */
  var factI = dayNo() % D.FACTS.length;  /* a new fact each day; Another gives the next */
  function renderFact() { var f = D.FACTS[factI % D.FACTS.length]; $("#fact").innerHTML = T(f[0], f[1]); var m = $("#fact-more"); if (m) m.setAttribute("href", f[2]); }  /* our own text, escaped at build, with its source chip (src/cites.py) */
  $("#fact-next").onclick = function () { factI++; renderFact(); };
  // The Daily challenge card shows today's own puzzle and the visitor's guesses so far.
  // It picks the event exactly as play.js does on daily.html (same pool, same seeded shuffle, same day number): change both together.
  var DAILY = null;
  function dailyPick() {
    if (DAILY) return DAILY;
    var pool = EVENTS.filter(function (e) { return e[E_Y] >= 500 && !e[E_C]; }), seed = 20261110;
    var rnd = function () { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
    for (var i = pool.length - 1; i > 0; i--) { var j = Math.floor(rnd() * (i + 1)), t = pool[i]; pool[i] = pool[j]; pool[j] = t; }
    var now = new Date(), key = now.getFullYear() + "-" + ("0" + (now.getMonth() + 1)).slice(-2) + "-" + ("0" + now.getDate()).slice(-2);
    var n = Math.round((Date.UTC(now.getFullYear(), now.getMonth(), now.getDate()) - Date.UTC(2026, 10, 10)) / 864e5);
    return (DAILY = { ev: pool[((n % pool.length) + pool.length) % pool.length], n: n + 1, key: key });
  }
  function renderStreak() {
    var el = document.getElementById("daily-streak"); if (!el) return;
    var j = {}; try { j = JSON.parse(localStorage.getItem("hc-journey") || "{}"); } catch (e) {}
    var n = j.d && j.d.streak || 0;
    if (n > 0) { el.hidden = false; el.textContent = "🔥 " + T(n + " day streak", n + " diwrnod yn olynol"); }
    var P = dailyPick(), ev = P.ev, ans = ev[E_Y], st = j.daily && j.daily.date === P.key ? j.daily : { g: [] }, g = st.g || [];
    $("#daily-n").textContent = "#" + P.n;
    var blank = function (x) { return esc(x).replace(/\b(1[0-9]{3}|20[0-9]{2}|[5-9][0-9]{2})\b/g, "<b>____</b>"); };
    $("#daily-ev").innerHTML = blank(T(ev[E_TEN], ev[E_TCY])) + "<small>" + blank(T(ev[E_BEN], ev[E_BCY])) + "</small>";
    $("#daily-tiles").innerHTML = [0, 1, 2, 3, 4, 5].map(function (i) {
      if (g[i] == null) return i === g.length && !st.done ? '<i class="next">?</i>' : "<i></i>";
      var a = Math.abs(g[i] - ans), k = a === 0 ? "ok" : a <= 5 ? "c5" : a <= 25 ? "c25" : a <= 100 ? "c100" : "far";
      return '<i class="' + k + '">' + (st.done ? g[i] : "") + "</i>";
    }).join("");
    $("#daily-sub").textContent = st.done ? (st.win ? T("Solved in " + g.length + ". A new event at midnight.", "Wedi’i datrys mewn " + g.length + ". Digwyddiad newydd am hanner nos.") : T("The answer was " + ans + ". A new event at midnight.", "Yr ateb oedd " + ans + ". Digwyddiad newydd am hanner nos."))
      : g.length ? T((6 - g.length) + " guesses left. Keep going!", (6 - g.length) + " cynnig ar ôl. Daliwch ati!") : T("Six guesses. A new event every midnight.", "Chwe chynnig. Her newydd bob hanner nos.");
    $(".b-daily").classList.toggle("done", !!st.done);
  }

  /* ---------- Census chart ---------- */
  function renderChart() {
    var C = D.CENSUS, w = 560, h = 260, l = 34, r = 16, t = 18, b = 28, x0 = 1891, x1 = 2021, ymax = 60;
    function X(y) { return l + (y - x0) / (x1 - x0) * (w - l - r); }
    function Y(v) { return t + (1 - v / ymax) * (h - t - b); }
    var s = '<svg class="chart" viewBox="0 0 ' + w + " " + h + '" width="100%" style="min-width:420px" role="img" aria-label="' + T("Line chart: Welsh speakers fell from 54.4% in 1891 to 17.8% in 2021", "Siart: gostyngodd canran y siaradwyr Cymraeg o 54.4% yn 1891 i 17.8% yn 2021") + '"><defs><linearGradient id="gArea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2453d" stop-opacity=".35"/><stop offset="1" stop-color="#e2453d" stop-opacity="0"/></linearGradient></defs>';
    [0, 20, 40, 60].forEach(function (v) { s += '<line class="grid" x1="' + l + '" x2="' + (w - r) + '" y1="' + Y(v) + '" y2="' + Y(v) + '"/><text x="' + (l - 6) + '" y="' + (Y(v) + 3.5) + '" text-anchor="end">' + v + "%</text>"; });
    [1891, 1921, 1951, 1981, 2021].forEach(function (yv) { s += '<text x="' + X(yv) + '" y="' + (h - 8) + '" text-anchor="middle">' + yv + "</text>"; });
    var pts = C.map(function (c) { return X(c[0]).toFixed(1) + "," + Y(c[1]).toFixed(1); });
    s += '<path class="area" d="M' + pts.join(" L") + " L" + X(2021) + "," + Y(0) + " L" + X(1891) + "," + Y(0) + 'Z"/><polyline class="ln" points="' + pts.join(" ") + '"/>';
    C.forEach(function (c, i) { var end = i === 0 || i === C.length - 1; s += '<circle class="' + (end ? "end" : "") + '" cx="' + X(c[0]) + '" cy="' + Y(c[1]) + '" r="' + (end ? 4.5 : 3) + '"><title>' + c[0] + ": " + c[1] + "%</title></circle>"; if (end || c[0] === 2001) s += '<text class="val" x="' + (X(c[0]) + (i === 0 ? 8 : -6)) + '" y="' + (Y(c[1]) - 10) + '" text-anchor="' + (i === 0 ? "start" : "end") + '">' + c[1] + "%</text>"; });
    $("#chart").innerHTML = s + "</svg>";
  }

  /* ---------- Place-name decoder: the words and the decoder itself are in placenames.js (src/placenames.py, src/placenames.js) ---------- */
  function renderDecoder() {
    var out = $("#dec-out"), P = window.PN;
    if (!out) return;
    if (!P) { out.innerHTML = '<p style="color:var(--muted)">' + T("Loading the word list…", "Yn llwytho’r geiriau…") + "</p>"; return; }
    var box = $("#dec-in");
    if (!box.dataset.daily) { box.dataset.daily = "1"; if (!box.value) box.value = P.today(); }  /* a new name each day, until the visitor types */
    var r = P.decode(box.value), cy = lang === "cy", i = 0, html = "";
    if (r.hit) html += '<p class="dec-hit"><a href="' + esc(P.townLink(r.hit)) + '"><b>' + esc(r.hit[1]) + (r.hit[0] !== r.hit[1] ? " / " + esc(r.hit[0]) : "") + "</b></a>: " + esc(cy ? r.hit[3] : r.hit[2]) + "</p>";
    html += r.words.map(function (w) {
      return '<div class="dec-word">' + w.map(function (p) {
        var l = P.label(p, cy), eng = l.kind === "e" || l.kind === "n";
        return '<div class="part' + (l.kind === "u" ? " unk" : eng ? " eng" : "") + '" style="--i:' + (i++) + '"><b>' + esc(l.t) + "</b><span>" + (eng ? "<em>" + T("English", "Saesneg") + ":</em> " : "") + esc(l.mean) + "</span>" + (l.note ? "<small>" + esc(l.note) + "</small>" : "") + "</div>";
      }).join("") + "</div>";
    }).join("");
    out.innerHTML = html || '<p style="color:var(--muted)">' + T("Type a Welsh place name above.", "Teipiwch enw lle uchod.") + "</p>";
    $("#dec-samples").innerHTML = '<span class="eyebrow" style="align-self:center;margin-right:.25rem">' + T("Try", "Rhowch gynnig ar") + "</span>" + P.samples.map(function (s) { return '<button type="button" data-s="' + esc(s) + '">' + esc(s) + "</button>"; }).join("");
  }
  document.addEventListener("pn:ready", renderDecoder);
  $("#dec-in").addEventListener("input", renderDecoder);
  $("#dec-form").addEventListener("submit", function (e) { e.preventDefault(); });
  $("#dec-samples").addEventListener("click", function (e) { var b = e.target.closest("[data-s]"); if (b) { $("#dec-in").value = b.dataset.s; renderDecoder(); } });
  /* ---------- Words, with play buttons ---------- */
  var AUDIO = {}; (D.AUDIO || []).forEach(function (a) { AUDIO[a] = 1; });
  var canSpeak = "speechSynthesis" in window;
  function slugW(w) { return w.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, ""); }
  function sayWord(w) {
    var slug = slugW(w[0]);
    if (AUDIO[slug]) {
      try { if (canSpeak) speechSynthesis.cancel(); if (sayWord.a) sayWord.a.pause(); sayWord.a = new Audio("audio/" + slug + ".mp3"); sayWord.a.play(); } catch (e) {}
      return;
    }
    if (!canSpeak) return;
    var vs = speechSynthesis.getVoices(), cy = vs.filter(function (v) { return /^cy/i.test(v.lang); })[0];
    var en = vs.filter(function (v) { return /^en-GB/i.test(v.lang); })[0] || vs.filter(function (v) { return /^en/i.test(v.lang); })[0];
    var u = new SpeechSynthesisUtterance(cy ? w[0] : w[1].toLowerCase().replace(/-/g, " "));
    if (cy) { u.voice = cy; u.lang = cy.lang; } else if (en) { u.voice = en; u.lang = en.lang; }
    u.rate = 0.8; speechSynthesis.cancel(); speechSynthesis.speak(u);
  }
  /* today's ten words: the next ten in turn from the shuffled list (WORD_POOL in build.py, src/daily.py window()) */
  var WORDS_TODAY = (function () {
    var all = D.WORDS, k = Math.min(D.WORDS_N || 10, all.length), start = (dayNo() * k) % all.length, out = [];
    for (var j = 0; j < k; j++) out.push((start + j) % all.length);
    return out;
  })();
  function renderWords() {
    var play = canSpeak || D.AUDIO && D.AUDIO.length;
    $("#words").innerHTML = WORDS_TODAY.map(function (i) { var w = D.WORDS[i];
      return "<li><b>" + esc(w[0]) + '</b><span class="say"><span class="g">' + w[1].split(" ").map(function (x) { return "<i>" + esc(x) + "</i>"; }).join(" ") + "</span>" + (play ? '<button type="button" class="play" data-w="' + i + '" aria-label="' + T("Hear ", "Clywed ") + esc(w[0]) + '">▶</button>' : "") + "</span><span>" + esc(T(w[2], w[3])) + "</span></li>";
    }).join("");
  }
  $("#words").addEventListener("click", function (ev) { var b = ev.target.closest(".play"); if (b) sayWord(D.WORDS[+b.dataset.w]); });
  if (canSpeak) { try { speechSynthesis.getVoices(); } catch (e) {} }

  /* ---------- Quiz ---------- */
  var Q = null;
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function newQuiz() {
    var qs = [], evs = shuffle(EVENTS.map(function (e, i) { return i; }).filter(function (i) { return EVENTS[i][E_Y] > 0; })).slice(0, 7);
    evs.forEach(function (i) {
      var e = EVENTS[i], wrong = shuffle(EVENTS.filter(function (x) { return x[E_Y] > 0 && Math.abs(x[E_Y] - e[E_Y]) > 15; })).slice(0, 3);
      var opts = shuffle([e].concat(wrong));
      qs.push({ k: "date", ev: i, opts: opts.map(function (x) { return EVENTS.indexOf(x); }), ans: opts.indexOf(e) });
    });
    shuffle(PEOPLE.map(function (p, i) { return i; })).slice(0, 3).forEach(function (pi) {
      var wrong = shuffle(PEOPLE.map(function (p, i) { return i; }).filter(function (i) { return i !== pi; })).slice(0, 3), opts = shuffle([pi].concat(wrong));
      qs.push({ k: "who", p: pi, opts: opts, ans: opts.indexOf(pi) });
    });
    Q = { qs: shuffle(qs), i: 0, score: 0, picked: -1 };
    renderQuiz();
  }
  function renderQuiz() {
    var box = $("#quiz-box");
    if (!Q) return newQuiz();
    if (Q.i >= Q.qs.length) {
      var s = Q.score, msg = s >= 9 ? T("Pencampwr! A true historian.", "Pencampwr! Hanesydd go iawn.") : s >= 6 ? T("Da iawn. Very good.", "Da iawn wir.") : s >= 3 ? T("Not bad. The timeline has every answer.", "Ddim yn ddrwg. Mae pob ateb yn y llinell amser.") : T("Time to explore the timeline and try again.", "Amser i bori drwy’r llinell amser a rhoi cynnig arall.");
      if (window.HC) { if (s >= 8) HC.flag("quiz8"); if (s >= 10) HC.flag("quiz10"); }
      box.innerHTML = '<p class="eyebrow">' + T("Your score", "Eich sgôr") + '</p><p class="q-score">' + s + "/" + Q.qs.length + '</p><h3>' + msg + '</h3><p><button type="button" class="btn solid" id="q-again">' + T("Play again", "Chwarae eto") + "</button></p>";
      $("#q-again").onclick = function () { newQuiz(); $("#quiz-box button") && $("#quiz-box button").focus(); };
      return;
    }
    var q = Q.qs[Q.i], head, ctx = "", labels;
    if (q.k === "date") {
      var e = EVENTS[q.ev];
      head = T("When did this happen?", "Pryd ddigwyddodd hyn?") + " " + esc(T(e[E_TEN], e[E_TCY]));
      ctx = esc(T(e[E_BEN], e[E_BCY])).replace(/\b(1[0-9]{3}|20[0-9]{2}|[1-9][0-9]{1,2})\b/g, "____");
      labels = q.opts.map(function (i) { return yearLabel(EVENTS[i]); });
    } else {
      var p = PEOPLE[q.p];
      head = T("Who is this?", "Pwy yw hwn?");
      ctx = esc(p[2]) + " · " + esc(T(p[7], p[8]));
      labels = q.opts.map(function (i) { return T(PEOPLE[i][3], PEOPLE[i][4]); });
    }
    box.innerHTML = '<div class="q-top"><span>' + T("Question", "Cwestiwn") + " " + (Q.i + 1) + " / " + Q.qs.length + "</span><span>" + T("Score", "Sgôr") + " " + Q.score + '</span></div><div class="q-bar"><i style="width:' + (Q.i / Q.qs.length * 100) + '%"></i></div>' +
      "<h3>" + head + '</h3><p class="q-ctx">' + ctx + '</p><div class="answers">' + labels.map(function (l, i) { return '<button type="button" data-a="' + i + '">' + esc(l) + "</button>"; }).join("") + '</div><p class="q-fb" id="q-fb" aria-live="polite"></p><p><button type="button" class="btn" id="q-next" hidden>' + (Q.i === Q.qs.length - 1 ? T("See my score", "Gweld fy sgôr") : T("Next question", "Cwestiwn nesaf")) + " →</button></p>";
    $$(".answers button", box).forEach(function (b) {
      b.onclick = function () {
        var a = +b.dataset.a, ok = a === q.ans;
        if (ok) Q.score++;
        $$(".answers button", box).forEach(function (x, i) { x.disabled = true; if (i === q.ans) x.classList.add("right"); else if (i === a) x.classList.add("wrong"); });
        var right = labels[q.ans];
        $("#q-fb").innerHTML = ok ? "<b>" + T("Correct.", "Cywir.") + "</b>" : T("Not quite. The answer is ", "Dim cweit. Yr ateb yw ") + "<b>" + esc(right) + "</b>.";
        var n = $("#q-next"); n.hidden = false; n.focus();
        n.onclick = function () { Q.i++; renderQuiz(); var f = $(".answers button", box) || $("#q-again"); if (f) f.focus({ preventScroll: true }); };
      };
    });
  }


  /* ---------- History near you ---------- */
  var TW = window.TOWNS || [], nearAt = null;
  function km(a, b, c, d) { var R = 6371, r = Math.PI / 180, x = Math.sin((c - a) * r / 2), y = Math.sin((d - b) * r / 2); return 2 * R * Math.asin(Math.sqrt(x * x + Math.cos(a * r) * Math.cos(c * r) * y * y)); }
  function findTown(q) { q = q.trim().toLowerCase(); if (!q) return null; var hit = null; TW.forEach(function (t) { if (!hit && (t[0].toLowerCase() === q || t[1].toLowerCase() === q)) hit = t; }); if (!hit) TW.forEach(function (t) { if (!hit && (t[0].toLowerCase().indexOf(q) === 0 || t[1].toLowerCase().indexOf(q) === 0)) hit = t; }); return hit; }
  function renderNear() {
    $("#near-towns").innerHTML = TW.map(function (t) { return '<option value="' + esc(T(t[0], t[1])) + '">'; }).join("");
    var inp = $("#near-in"); inp.placeholder = T("Type your town, e.g. Bala", "Teipiwch eich tref, e.e. Y Bala");
    var list = $("#near-list"), you = $("#you-pin");
    if (!nearAt) { list.innerHTML = ""; if (you) you.remove(); return; }
    var near = PLACES.map(function (p) { return [km(nearAt.lat, nearAt.lon, p.lat, p.lon), p]; }).sort(function (a, b) { return a[0] - b[0]; }).slice(0, 5);
    $("#near-msg").textContent = T("Nearest historic places to ", "Y lleoedd hanesyddol agosaf at ") + nearAt.name + ":";
    list.innerHTML = near.map(function (x) {
      var p = x[1], d = x[0] < 1 ? T("under 1 km", "llai nag 1 km") : Math.round(x[0]) + " km";
      return '<li data-era="' + p.era + '"><button type="button" class="near-go" data-pid="' + p.id + '"><b>' + esc(T(p.en, p.cy)) + "</b><span>" + d + " · " + esc(p.year) + "</span></button></li>";
    }).join("");
    var xy = proj(nearAt.lat, nearAt.lon);
    if (!you) { you = document.createElementNS("http://www.w3.org/2000/svg", "g"); you.id = "you-pin"; you.setAttribute("class", "you"); $("#wales").appendChild(you); }
    you.setAttribute("transform", "translate(" + xy[0].toFixed(1) + " " + xy[1].toFixed(1) + ")");
    you.innerHTML = '<circle r="9"/><circle class="in" r="3.5"/><text x="0" y="-15" text-anchor="middle">' + esc(T("You", "Chi")) + "</text>";
  }
  $("#near-form").addEventListener("submit", function (ev) {
    ev.preventDefault();
    var t = findTown($("#near-in").value);
    if (!t) { nearAt = null; renderNear(); $("#near-msg").textContent = T("Sorry, I don’t know that town yet. Try a nearby larger town.", "Mae’n ddrwg gen i, dw i ddim yn adnabod y dref honno eto. Rhowch gynnig ar dref fwy gerllaw."); return; }
    nearAt = { lat: t[2], lon: t[3], name: T(t[0], t[1]) }; renderNear();
  });
  $("#near-geo").onclick = function () {
    var msg = $("#near-msg");
    if (!navigator.geolocation) { msg.textContent = T("Your browser can’t share your location. Type your town instead.", "Ni all eich porwr rannu’ch lleoliad. Teipiwch eich tref yn lle hynny."); return; }
    msg.textContent = T("Finding you…", "Yn chwilio amdanoch…");
    navigator.geolocation.getCurrentPosition(function (pos) {
      var la = pos.coords.latitude, lo = pos.coords.longitude;
      if (la < 51.2 || la > 53.6 || lo < -5.8 || lo > -2.5) { msg.textContent = T("You seem to be outside Wales, so here is the nearest corner of it.", "Mae’n ymddangos eich bod y tu allan i Gymru, felly dyma’r gornel agosaf ati."); la = Math.min(53.45, Math.max(51.38, la)); lo = Math.min(-2.75, Math.max(-5.3, lo)); }
      nearAt = { lat: la, lon: lo, name: T("you", "chi") }; renderNear();
    }, function () { msg.textContent = T("Location wasn’t shared. Type your town instead.", "Ni rannwyd eich lleoliad. Teipiwch eich tref yn lle hynny."); }, { timeout: 10000, maximumAge: 600000 });
  };
  $("#near-list").addEventListener("click", function (ev) { var b = ev.target.closest(".near-go"); if (!b) return; selectPlace(b.dataset.pid); var c = $("#place-card"); if (c && c.scrollIntoView && innerWidth < 900) c.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" }); });

  /* ---------- Home page: history near you, in the Map section (#mh-near). The three nearest places become picture cards, and a "You" pin lands on the small map. ---------- */
  var MH = document.getElementById("mh-near"), mhAt = null;
  function renderMh() {
    if (!MH) return;
    $("#mh-towns").innerHTML = TW.map(function (t) { return '<option value="' + esc(T(t[0], t[1])) + '">'; }).join("");
    $("#mh-in").placeholder = T("Your town, e.g. Bala", "Eich tref, e.e. Y Bala");
    $(".mh-go", MH).setAttribute("aria-label", T("Find", "Chwilio")); $("#mh-geo").setAttribute("aria-label", T("Use my location", "Defnyddio fy lleoliad"));
    var res = $("#mh-res"), you = document.getElementById("mh-you");
    $$(".map-teaser .pin.hl").forEach(function (g) { g.classList.toggle("hl", false); });
    if (!mhAt) { res.innerHTML = ""; if (you) you.setAttribute("hidden", ""); return; }
    var near = PLACES.map(function (p) { return [km(mhAt.lat, mhAt.lon, p.lat, p.lon), p]; }).sort(function (a, b) { return a[0] - b[0]; }).slice(0, 3);
    $("#mh-msg").textContent = T("The nearest historic places to ", "Y lleoedd hanesyddol agosaf at ") + mhAt.name + ":";
    res.innerHTML = near.map(function (x) {
      var p = x[1], d = x[0] < 1 ? T("under 1 km", "llai nag 1 km") : Math.round(x[0]) + " km", name = esc(T(p.en, p.cy));
      var pin = document.querySelector('.map-teaser .pin[data-pid="' + p.id + '"]'); if (pin) pin.classList.add("hl");
      return '<li class="mh-place wl-card" data-era="' + p.era + '"><span class="mh-ph">' + (p.ph ? '<img src="' + esc(p.ph[0]) + '" alt="" loading="lazy" decoding="async">' : "") + '</span><span class="mh-pt"><b>' + name + "</b><small>" + d + " · " + esc(p.year) + '</small></span><a class="wl" href="place-' + p.id + '.html">' + name + "</a></li>";
    }).join("");
    if (you) {
      var xy = proj(mhAt.lat, mhAt.lon);
      you.toggleAttribute("hidden", false);
      you.setAttribute("transform", "translate(" + xy[0].toFixed(1) + " " + xy[1].toFixed(1) + ")");
      you.innerHTML = '<circle class="ring" r="22"/><circle r="12"/><circle class="in" r="5"/><text x="0" y="-26" text-anchor="middle">' + esc(T("You", "Chi")) + "</text>";
    }
  }
  if (MH) {
    MH.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var t = findTown($("#mh-in").value);
      if (!t) { mhAt = null; renderMh(); $("#mh-msg").textContent = T("Sorry, I don’t know that town yet. Try a nearby larger town.", "Mae’n ddrwg gen i, dw i ddim yn adnabod y dref honno eto. Rhowch gynnig ar dref fwy gerllaw."); return; }
      mhAt = { lat: t[2], lon: t[3], name: T(t[0], t[1]) }; renderMh(); $("#mh-in").blur();
    });
    $("#mh-geo").onclick = function () {
      var msg = $("#mh-msg");
      if (!navigator.geolocation) { msg.textContent = T("Your browser can’t share your location. Type your town instead.", "Ni all eich porwr rannu’ch lleoliad. Teipiwch eich tref yn lle hynny."); return; }
      msg.textContent = T("Finding you…", "Yn chwilio amdanoch…");
      navigator.geolocation.getCurrentPosition(function (pos) {
        var la = pos.coords.latitude, lo = pos.coords.longitude, out = la < 51.2 || la > 53.6 || lo < -5.8 || lo > -2.5;
        if (out) { la = Math.min(53.45, Math.max(51.38, la)); lo = Math.min(-2.75, Math.max(-5.3, lo)); }
        mhAt = { lat: la, lon: lo, name: T("you", "chi") }; renderMh();
        if (out) msg.textContent = T("You seem to be outside Wales, so here is the nearest corner of it:", "Mae’n ymddangos eich bod y tu allan i Gymru, felly dyma’r gornel agosaf ati:");
      }, function () { msg.textContent = T("Location wasn’t shared. Type your town instead.", "Ni rannwyd eich lleoliad. Teipiwch eich tref yn lle hynny."); }, { timeout: 10000, maximumAge: 600000 });
    };
  }

  /* ---------- Timeline challenge ---------- */
  var G = null;
  function gameRound() {
    var pool = shuffle(EVENTS.map(function (e, i) { return i; })), pick = [];
    for (var k = 0; k < pool.length && pick.length < 5; k++) {
      var y = EVENTS[pool[k]][E_Y];
      if (pick.every(function (j) { return Math.abs(EVENTS[j][E_Y] - y) >= 25; })) pick.push(pool[k]);
    }
    return { cards: pick, order: [], done: false };
  }
  function newGame() { G = { round: 1, total: 0, r: gameRound() }; renderGame(); }
  function renderGame() {
    if (!G) return newGame();
    var box = $("#game-box"), r = G.r;
    if (G.over) {
      var s = G.total, msg = s >= 13 ? T("Brilliant! You know your history.", "Gwych! Rydych chi’n gwybod eich hanes.") : s >= 9 ? T("Da iawn! Well done.", "Da iawn wir!") : T("Good try. Every play teaches you more.", "Ymdrech dda. Mae pob gêm yn dysgu mwy i chi.");
      if (s >= 15 && window.HC) HC.flag("order15");
      box.innerHTML = '<p class="eyebrow">' + T("Final score", "Sgôr terfynol") + '</p><p class="q-score">' + s + '/15</p><h3>' + msg + '</h3><div class="game-row"><button type="button" class="btn solid" id="g-again">' + T("Play again", "Chwarae eto") + '</button><button type="button" class="btn" id="g-share">' + T("Copy my score", "Copïo fy sgôr") + "</button></div>";
      $("#g-again").onclick = function () { newGame(); var f = $("#game-box .g-card"); if (f) f.focus(); };
      $("#g-share").onclick = function () {
        var b = this, txt = T("I scored " + s + "/15 in the Timeline challenge on History of Wales. Can you beat me? ", "Sgoriais " + s + "/15 yn Her y llinell amser ar Hanes Cymru. Allwch chi wneud yn well? ") + "https://historyofwales.cymru/quiz.html#game";
        try { navigator.clipboard.writeText(txt).then(function () { b.textContent = T("Copied", "Wedi copïo"); }, function () { b.textContent = txt; }); } catch (e) { b.textContent = txt; }
      };
      return;
    }
    var sorted = r.cards.slice().sort(function (a, b) { return EVENTS[a][E_Y] - EVENTS[b][E_Y]; });
    box.innerHTML = '<div class="q-top"><span>' + T("Round", "Rownd") + " " + G.round + " / 3</span><span>" + T("Score", "Sgôr") + " " + G.total + "</span></div>" +
      '<ol class="g-cards">' + r.cards.map(function (i) {
        var e = EVENTS[i], n = r.order.indexOf(i), cls = "g-card";
        if (r.done) cls += sorted.indexOf(i) === n ? " right" : " wrong";
        return '<li><button type="button" class="' + cls + '" data-era="' + e[E_ERA] + '" data-i="' + i + '"' + (r.done ? " disabled" : "") + ' aria-pressed="' + (n >= 0) + '"><span class="g-n">' + (n >= 0 ? n + 1 : "") + "</span><span><b>" + esc(T(e[E_TEN], e[E_TCY])) + "</b>" + (r.done ? '<span class="g-y">' + yearLabel(e) + (sorted.indexOf(i) !== n ? " · " + T("should be ", "dylai fod yn ") + (sorted.indexOf(i) + 1) : "") + "</span>" : "") + "</span></button></li>";
      }).join("") + "</ol>" +
      '<div class="game-row"><p class="q-fb" aria-live="polite">' + (r.done ? T("You got ", "Cawsoch ") + r.pts + "/5." : T("Tap the oldest event first.", "Tapiwch y digwyddiad hynaf yn gyntaf.") + " " + r.order.length + "/5") + "</p>" +
      (r.done ? '<button type="button" class="btn solid" id="g-next">' + (G.round < 3 ? T("Next round", "Rownd nesaf") : T("See my score", "Gweld fy sgôr")) + "</button>" : '<button type="button" class="btn solid" id="g-check"' + (r.order.length < 5 ? " disabled" : "") + ">" + T("Check", "Gwirio") + "</button>") + "</div>";
    $$(".g-card", box).forEach(function (b) {
      b.onclick = function () {
        var i = +b.dataset.i, n = r.order.indexOf(i);
        if (n >= 0) r.order = r.order.slice(0, n); else r.order.push(i);
        renderGame(); var f = $('.g-card[data-i="' + i + '"]', box); if (f) f.focus();
      };
    });
    if ($("#g-check")) $("#g-check").onclick = function () {
      r.pts = r.order.filter(function (i, n) { return sorted[n] === i; }).length; r.done = true; G.total += r.pts; renderGame(); $("#g-next").focus();
    };
    if ($("#g-next")) $("#g-next").onclick = function () {
      if (G.round >= 3) G.over = true; else { G.round++; G.r = gameRound(); }
      renderGame(); var f = $("#game-box .g-card") || $("#g-again"); if (f) f.focus();
    };
  }

  /* ---------- Sources ---------- */
  function renderSources() {
    $("#read-books").innerHTML = D.READING.map(function (r) { var b = "<b>" + esc(r.t) + "</b>"; return "<li>" + (r.u ? '<a href="' + r.u + '" target="_blank" rel="noopener">' + b + "</a>" : b) + "<span>" + esc(T(r.n, r.nCy)) + "</span>" + (r.b ? '<span class="ref-buy">' + T("Buy:", "Prynu:") + ' <a href="' + r.b[0] + '" target="_blank" rel="noopener nofollow">Amazon</a> · <a href="' + r.b[1] + '" target="_blank" rel="noopener nofollow">AbeBooks</a></span>' : "") + "</li>"; }).join("");
    $("#read-online").innerHTML = D.ONLINE.map(function (r) { var u = T(r.u, r.uCy || r.u); return '<li><a href="' + u + '" target="_blank" rel="noopener"><b>' + esc(T(r.t, r.tCy)) + "</b></a><span>" + esc(u.replace(/^https:\/\/(www\.)?/, "").replace(/\/$/, "")) + "</span></li>"; }).join("");
  }

  /* ---------- Language toggle ---------- */
  $$("[data-cy]").forEach(function (el) { el.dataset.en = el.textContent; });
  $$("[data-cy-svg]").forEach(function (el) { el.dataset.enSvg = el.textContent; });
  function applyLang() {
    document.documentElement.lang = lang; document.documentElement.classList.toggle("cy", lang === "cy");
    $$("[data-cy]").forEach(function (el) { el.textContent = lang === "cy" ? el.dataset.cy : el.dataset.en; });
    $$("[data-cy-svg]").forEach(function (el) { el.textContent = lang === "cy" ? el.dataset.cySvg : el.dataset.enSvg; });
    renderChapters(); renderToday(); renderTimeline(); renderPeople(); renderFact(); renderStreak(); renderChart(); renderDecoder(); renderWords(); renderSources(); renderNear(); renderMh(); renderGame(); selectPlace(sel); if (mode === "kg") renderKg(); renderQuiz();
    if (!ov.hidden) { var m = /^#pennod-(\w+)/.exec(location.hash); if (m) openChapter(m[1], false); }
  }
  /* the EN / CY switch is a pair of links to the other language's page (see welshpages.py) */

  renderGrat(); renderLAs();
  applyLang();
  route();
})();
