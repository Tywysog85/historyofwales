(function () {
  var D = DATA, ERAS = D.ERAS, EVENTS = D.EVENTS, PLACES = D.PLACES, PEOPLE = D.PEOPLE, MAPC = D.MAPC;
  var WIKI = "https://en.wikipedia.org/wiki/";
  var lang = "en";
  try { if (localStorage.getItem("hc-lang") === "cy") lang = "cy"; } catch (e) {}
  var $ = function (s, r) { return (r || document).querySelector(s) || document.createElement("input"); };
  var HAS_TL = !!document.getElementById("events"), HERO = !!document.getElementById("sky"), HAS_MAP = !!document.getElementById("pins");
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var ERA = {}; ERAS.forEach(function (e) { ERA[e.id] = e; });
  var PLACE = {}; PLACES.forEach(function (p) { PLACE[p.id] = p; });
  function T(en, cy) { return lang === "cy" ? cy : en; }
  function fmt(n) { return Math.abs(n).toLocaleString("en-GB"); }
  /* event fields */
  var E_ERA = 0, E_Y = 1, E_C = 2, E_END = 3, E_DAY = 4, E_TEN = 5, E_TCY = 6, E_BEN = 7, E_BCY = 8, E_KEY = 9, E_PLACE = 10, E_SRC = 11;
  function yearLabel(e) {
    var y = e[E_Y], c = e[E_C] ? "c. " : "", end = e[E_END] ? "–" + e[E_END] : "";
    if (y < 0) return c + fmt(y) + " " + T("BC", "CC");
    if (y < 1000) return c + y + " " + T("AD", "OC");
    return c + y + end;
  }
  function srcLink(s) { return s ? '<a class="src" href="' + WIKI + s + '" target="_blank" rel="noopener">' + T("Source", "Ffynhonnell") + " ↗</a>" : ""; }
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var MONTHS_EN = ["January","February","March","April","May","June","July","August","September","October","November","December"];
  var MONTHS_CY = ["Ionawr","Chwefror","Mawrth","Ebrill","Mai","Mehefin","Gorffennaf","Awst","Medi","Hydref","Tachwedd","Rhagfyr"];

  /* ---------- Hero sky ---------- */
  var cv = $("#sky"), cx = HERO ? cv.getContext("2d") : null, W = 0, H = 0, dpr = 1, mouse = 0, ridges = [], stars = [];
  function rnd(seed) { return function () { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }; }
  (function () {
    var r = rnd(1282);
    for (var l = 0; l < 5; l++) { var w = []; for (var k = 0; k < 6; k++) w.push([r() * 6.28, 0.6 + r() * (k + 1) * 1.7, (1 / (k + 1.2)) * (0.6 + r() * 0.6)]); ridges.push(w); }
    for (var s = 0; s < 140; s++) stars.push([r(), r() * 0.6, r() * 1.2 + 0.2, r()]);
  })();
  var LAYERS = [
    { y: 0.50, a: 0.16, c: "#232a3d", s: 0.05 }, { y: 0.60, a: 0.14, c: "#1d2433", s: 0.12 },
    { y: 0.70, a: 0.12, c: "#171d2a", s: 0.2 }, { y: 0.80, a: 0.09, c: "#121722", s: 0.3 }, { y: 0.92, a: 0.06, c: "#0e1118", s: 0.42 }
  ];
  /* where the words sit, so the scene can keep clear of them */
  var M = { h1t: 40, h1h: 80, sub: 0, cta: 0, tick: 0 }, hEl = HERO ? document.getElementById("top") : null;
  function measure() {
    if (!HERO) return false;
    var r = cv.getBoundingClientRect(), q = function (sel) { var el = hEl.querySelector(sel); return el ? el.getBoundingClientRect() : null; };
    var a = q("h1"), b = q(".sub"), c = q(".ticker"), e = q(".cta"), old = M.h1t + "," + M.h1h + "," + M.sub + "," + M.tick + "," + M.cta;
    if (a) { M.h1t = a.top - r.top; M.h1h = a.height; } if (b) M.sub = b.bottom - r.top; if (e) M.cta = e.bottom - r.top; M.tick = c ? c.top - r.top : r.height;
    return old !== M.h1t + "," + M.h1h + "," + M.sub + "," + M.tick + "," + M.cta;
  }
  var VIS = 0; /* how much of the hero the first screen shows */
  function size() { if (!HERO) return; var r = cv.getBoundingClientRect(); dpr = Math.min(window.devicePixelRatio || 1, 2); W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; VIS = window.innerHeight - (r.top + window.scrollY); measure(); draw(); }
  if (HERO) setInterval(function () { var r = cv.getBoundingClientRect(); if (Math.abs(r.height - H) > 1 || Math.abs(r.width - W) > 1) size(); else if (measure() && reduce) draw(); }, 500);
  /* ---- the sky follows the real sun over Wales: night, dawn, day, dusk ---- */
  function hex(c) { return [parseInt(c.slice(1, 3), 16), parseInt(c.slice(3, 5), 16), parseInt(c.slice(5, 7), 16)]; }
  function mix(a, b, k) { var x = hex(a), y = hex(b); return "rgb(" + Math.round(x[0] + (y[0] - x[0]) * k) + "," + Math.round(x[1] + (y[1] - x[1]) * k) + "," + Math.round(x[2] + (y[2] - x[2]) * k) + ")"; }
  function mixHex(a, b, k) { var x = hex(a), y = hex(b); return "#" + [0, 1, 2].map(function (i) { return ("0" + Math.round(x[i] + (y[i] - x[i]) * k).toString(16)).slice(-2); }).join(""); }
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
      cx.fillStyle = "rgba(236,233,225," + (0.15 + 0.5 * tw * s[2] / 1.4) * SKY.star + ")"; cx.fillRect(X, Y, s[2], s[2]);
      if (i % 12 === 0 && !(Y > M.h1t - 6 && (W < 1100 ? Y < M.cta + 6 : X < W * 0.62))) { var a = (0.25 + 0.6 * tw) * SKY.star, L2 = 2.5 + 3 * tw; cx.fillStyle = "rgba(244,238,226," + a + ")"; cx.fillRect(X - L2, Y, L2 * 2 + 1, 1); cx.fillRect(X, Y - L2, 1, L2 * 2 + 1); }
    });
    /* phones and tall, narrow windows: the mountain sits below the words. Wide screens: it stands to the right of them. */
    var narrow = W < 640, stacked = W < 1100;
    var ex0, ew, eb, eh;
    if (stacked) {
      var top = narrow ? M.cta + 18 : M.sub + 4, bot = Math.max(top + 120, M.tick + (narrow ? 26 : 10));
      eh = Math.min(bot - top, W * 0.62); if (narrow && VIS > top + 110) eh = Math.min(eh, Math.max(120, VIS - top - 4)); eb = top + eh; ew = Math.max(W * (narrow ? 1.05 : 0.8), eh * 2.3); ex0 = W * (narrow ? 0.6 : 0.7) - 0.53 * ew;
    } else { ex0 = W * 0.38; ew = W * 0.7; eb = H * 0.72; eh = H * 0.5; }
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
    LAYERS.forEach(function (L, i) {
      if (i === 1) { drawEryri(ex0 - ew * 0.34 - mouse * 2, eb - sy * 0.03, ew * 0.9, eh * 0.62, true); drawEryri(ex0 - mouse * 4, eb - sy * 0.04, ew, eh); }
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
  /* Y Ddraig Goch: an original silhouette, facing right, 220 x 130 units */
  var DR = {
    body: new Path2D("M186 34C190 33 196 35 200 38L193 40C196 42 199 44 200 46C194 47 188 46 184 45C178 47 172 52 168 58C163 66 156 72 146 74C132 77 116 78 102 77C88 76 76 74 66 76C52 79 40 88 28 96C20 101 12 102 6 98C10 98 16 95 22 90C34 80 46 70 60 66C74 62 90 64 104 63C118 62 132 62 142 58C152 54 158 46 164 38C168 32 174 28 180 28L176 20L184 27L186 18L189 29C189 31 188 32 186 34ZM8 99L-6 92L0 104L-4 112L12 102ZM138 72C142 80 144 86 150 90L156 90L152 94L158 96L146 96C138 92 134 84 130 76ZM76 74C76 84 72 92 66 98L72 100L64 102L68 106L58 104C62 96 64 86 64 76Z"),
    far: new Path2D("M128 62C130 40 140 18 160 2C150 18 150 26 152 32C144 30 140 36 142 42C134 42 132 50 134 58Z"),
    near: new Path2D("M92 64C86 40 74 18 48 0C62 4 80 10 96 20L104 10C112 22 118 36 120 52C114 48 108 50 108 56C102 52 96 56 98 62Z")
  };
  var DPOS = { x: -999, y: -999, r: 0 }, fireAt = 0, nextFire = 5000;
  function drawDragon(t, sumX, sumY, narrow, stacked) {
    var period = 26000, k = reduce ? 0.55 : (t % period) / period;
    var base = narrow ? W * 0.27 : Math.min(W * 0.17, 260);
    var sx = narrow ? W * 0.61 : W * 0.6, ex = narrow ? W * 0.72 : stacked ? W * 0.78 : sumX - W * 0.06;
    var sy0 = narrow ? M.h1t + M.h1h * 0.3 : stacked ? M.h1t + M.h1h * 0.1 : H * 0.07, ey = narrow ? M.h1t + M.h1h * 0.42 : stacked ? M.h1t + M.h1h * 0.45 : sumY - H * 0.05;
    var x = sx + (ex - sx) * k, y = sy0 + (ey - sy0) * k + Math.sin(t / 900) * Math.min(H * 0.008, 6);
    var size = base * (1 - (narrow ? 0.18 : 0.3) * k), sc = size / 220;
    var alpha = reduce ? 1 : Math.min(1, k / 0.08, (1 - k) / 0.12);
    var flap = reduce ? 1 : 0.62 + 0.38 * Math.cos(t / 260);
    DPOS.x = x + 110 * sc; DPOS.y = y + 60 * sc; DPOS.r = Math.max(44, 120 * sc);
    if (!reduce && t > nextFire && alpha >= 1) { fireAt = t; nextFire = t + 9000 + Math.random() * 7000; }
    cx.save(); cx.globalAlpha = alpha; cx.translate(x, y); cx.scale(sc, sc); cx.rotate(-0.06);
    var fp = (t - fireAt) / 1300;
    if (fireAt && fp >= 0 && fp < 1) {
      /* fire: three flickering tongues from the mouth, brightest at the root */
      var pow = Math.sin(Math.min(1, fp * 1.15) * Math.PI), L = 135 * pow;
      cx.save(); cx.translate(199, 41); cx.rotate(0.12); cx.globalCompositeOperation = "lighter";
      [[1, 22, "rgba(226,69,61,.8)"], [0.78, 14, "rgba(255,150,60,.9)"], [0.5, 7.5, "rgba(255,236,170,.95)"]].forEach(function (f, n) {
        var l = L * f[0] * (0.9 + 0.1 * Math.sin(t / 45 + n * 2)), w = f[1] * pow * (0.85 + 0.15 * Math.sin(t / 60 + n)), wob = 4 * Math.sin(t / 70 + n * 1.7);
        var g = cx.createLinearGradient(0, 0, l, 0); g.addColorStop(0, f[2]); g.addColorStop(1, f[2].replace(/[\d.]+\)$/, "0)"));
        cx.fillStyle = g; cx.beginPath(); cx.moveTo(0, 0); cx.bezierCurveTo(l * 0.3, -w + wob * 0.3, l * 0.7, -w * 0.9 + wob, l, wob); cx.bezierCurveTo(l * 0.7, w * 0.9 + wob, l * 0.3, w + wob * 0.3, 0, 0); cx.fill();
      });
      cx.restore();
    }
    cx.fillStyle = "#c9372f";
    cx.save(); cx.translate(0, 62); cx.scale(1, flap); cx.translate(0, -62); cx.fill(DR.far); cx.restore();
    cx.fillStyle = "#e2453d"; cx.fill(DR.body);
    cx.save(); cx.translate(0, 64); cx.scale(1, flap); cx.translate(0, -64); cx.fill(DR.near); cx.restore();
    cx.restore();
  }
  function loop(t) { t0 = t; if (window.scrollY < H) draw(t); requestAnimationFrame(loop); }
  window.addEventListener("resize", size);
  if (HERO && !reduce) {
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

  /* ---------- Word strip: drifts by itself, and can be dragged, swiped or scrolled either way ---------- */
  (function () {
    var m = document.getElementById("marquee"); if (!m) return;
    var tr = m.firstElementChild, hold = false, idle = 0, pos = 0, down = null, moved = false, last = 0;
    function half() { return tr.children[tr.children.length / 2].offsetLeft - tr.children[0].offsetLeft; }
    function wrap() { var h = half(); if (h <= 0) return; if (m.scrollLeft >= h) m.scrollLeft -= h; else if (m.scrollLeft <= 0) m.scrollLeft += h; pos = m.scrollLeft; }
    function rest(ms) { idle = performance.now() + (ms || 2500); }
    m.addEventListener("scroll", function () { if (Math.abs(m.scrollLeft - pos) > 2) { wrap(); } }, { passive: true });
    m.addEventListener("pointerenter", function (e) { if (e.pointerType === "mouse") hold = true; });
    m.addEventListener("pointerleave", function () { hold = false; rest(600); });
    m.addEventListener("touchstart", function () { rest(4000); }, { passive: true });
    m.addEventListener("touchmove", function () { rest(4000); }, { passive: true });
    m.addEventListener("wheel", function () { rest(); }, { passive: true });
    m.addEventListener("focusin", function () { hold = true; }); m.addEventListener("focusout", function () { hold = false; rest(); });
    m.addEventListener("pointerdown", function (e) { if (e.pointerType !== "mouse" || e.button) return; down = { x: e.clientX, s: m.scrollLeft }; moved = false; });
    window.addEventListener("pointermove", function (e) {
      if (!down) return; var dx = e.clientX - down.x;
      if (!moved && Math.abs(dx) > 5) { moved = true; m.classList.add("drag"); }
      if (moved) { m.scrollLeft = down.s - dx; var h = half(); if (m.scrollLeft <= 0) { m.scrollLeft += h; down.s += h; } else if (m.scrollLeft >= h) { m.scrollLeft -= h; down.s -= h; } pos = m.scrollLeft; }
    });
    window.addEventListener("pointerup", function () { if (!down) return; down = null; if (moved) { setTimeout(function () { m.classList.remove("drag"); }, 0); rest(); } });
    m.addEventListener("click", function (e) { if (moved) { e.preventDefault(); moved = false; } }, true);
    m.addEventListener("dragstart", function (e) { e.preventDefault(); });
    m.scrollLeft = pos = 1;
    if (reduce) return;
    requestAnimationFrame(function step(t) {
      var dt = Math.min(50, t - (last || t)); last = t;
      if (!hold && !down && t > idle) { pos += dt * 0.045; var h = half(); if (h > 0 && pos >= h) pos -= h; m.scrollLeft = pos; }
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
      return '<button type="button" class="chap" data-era="' + e.id + '" data-open="' + e.id + '"><svg aria-hidden="true"><use href="#i-' + e.ill + '"/></svg><span class="span">' + T(e.spanEn, e.spanCy) + "</span><h3>" + T(e.en, e.cy) + "</h3><p>" + esc(T(e.blurbEn, e.blurbCy)) + '</p><span class="go">' + T("Read the chapter →", "Darllen y bennod →") + "</span></button>";
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
    var m = ev.target.closest("[data-map]"); if (m) { if (!HAS_MAP) { location.href = "index.html#lle-" + m.dataset.map; return; } setMode("sites"); selectPlace(m.dataset.map); goTo($("#map")); }
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
      ERAS.map(function (e) { return '<button type="button" class="chip" data-era="' + e.id + '" data-v="' + e.id + '" aria-pressed="' + (cur === e.id) + '"><i></i>' + T(e.en, e.cy) + (counts ? ' <span style="opacity:.6">' + counts[e.id] + "</span>" : "") + "</button>"; }).join("");
    el.onclick = function (ev) { var b = ev.target.closest(".chip"); if (b) onPick(b.dataset.v); };
  }

  /* ---------- On this day ---------- */
  function renderToday() {
    var now = new Date(), md = ("0" + (now.getMonth() + 1)).slice(-2) + "-" + ("0" + now.getDate()).slice(-2);
    var dated = EVENTS.map(function (e, i) { return [e[E_DAY], i]; }).filter(function (x) { return x[0]; }).sort(function (a, b) { return a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0; });
    var hit = dated.filter(function (x) { return x[0] === md; }), isToday = hit.length > 0, day = md;
    if (!isToday) { var nx = dated.filter(function (x) { return x[0] > md; })[0] || dated[0]; day = nx[0]; hit = dated.filter(function (x) { return x[0] === day; }); }
    var mm = +day.slice(0, 2) - 1, dd = +day.slice(3);
    $("#today-box").innerHTML = '<div class="cal"><span class="d">' + dd + '</span><span class="m">' + T(MONTHS_EN[mm], MONTHS_CY[mm]) + '</span><span class="lab">' + (isToday ? T("Today", "Heddiw") : T("Next anniversary", "Y pen-blwydd nesaf")) + "</span></div>" +
      '<div class="items">' + hit.map(function (x) { var e = EVENTS[x[1]]; return '<div class="it" data-era="' + e[E_ERA] + '"><time>' + e[E_Y] + "</time><div><h3>" + esc(T(e[E_TEN], e[E_TCY])) + "</h3><p>" + esc(T(e[E_BEN], e[E_BCY])) + "</p></div></div>"; }).join("") +
      '<div class="more"><span class="eyebrow">' + T("Also coming up", "Hefyd ar y gorwel") + "</span>" + (function () {
        var after = dated.filter(function (x) { return x[0] > day; }).concat(dated.filter(function (x) { return x[0] < day; })).slice(0, 3);
        return after.map(function (x) { var e = EVENTS[x[1]], m = +x[0].slice(0, 2) - 1; return '<button type="button" class="chip" data-tl="' + x[1] + '">' + +x[0].slice(3) + " " + T(MONTHS_EN[m].slice(0, 3), MONTHS_CY[m]) + " · " + esc(T(e[E_TEN], e[E_TCY])) + "</button>"; }).join("");
      })() + "</div></div>";
  }

  /* ---------- Timeline ---------- */
  var tlEra = "all", evEls = [], active = -1, shownYear = EVENTS[0][E_Y], yrAnim = null;
  function setTlEra(v) { tlEra = v; renderTimeline(); }
  function renderTimeline() {
    var counts = {}; EVENTS.forEach(function (e) { counts[e[E_ERA]] = (counts[e[E_ERA]] || 0) + 1; });
    if (!HAS_TL) {
      $("#tl-teaser").innerHTML = '<a class="chip" href="timeline.html">' + T("All", "Y cyfan") + ' <span style="opacity:.6">' + EVENTS.length + "</span></a>" +
        ERAS.map(function (e) { return '<a class="chip" data-era="' + e.id + '" href="timeline.html#era-' + e.id + '"><i></i>' + T(e.en, e.cy) + ' <span style="opacity:.6">' + counts[e.id] + "</span></a>"; }).join("");
      return;
    }
    chips($("#tl-filter"), tlEra, setTlEra, counts);
    var html = "", last = null, n = 0;
    EVENTS.forEach(function (e, i) {
      if (tlEra !== "all" && e[E_ERA] !== tlEra) return;
      n++;
      if (e[E_ERA] !== last) { var E = ERA[e[E_ERA]]; html += '<li class="era-head" id="era-' + E.id + '" data-era="' + E.id + '"><span class="eyebrow">' + T(E.spanEn, E.spanCy) + "</span><h3>" + T(E.en, E.cy) + '</h3><button type="button" data-open="' + E.id + '">' + T("Read the chapter", "Darllen y bennod") + "</button></li>"; last = e[E_ERA]; }
      html += '<li class="ev' + (e[E_KEY] ? " key" : "") + '" id="ev-' + i + '" data-i="' + i + '" data-era="' + e[E_ERA] + '"><time>' + yearLabel(e) + "</time><h4>" + esc(T(e[E_TEN], e[E_TCY])) + "</h4><p>" + esc(T(e[E_BEN], e[E_BCY])) + '</p><div class="links">' +
        (e[E_PLACE] ? '<button type="button" class="maplink" data-map="' + e[E_PLACE] + '"><svg aria-hidden="true"><use href="#i-pin"/></svg>' + T("See it on the map", "Gweld ar y map") + "</button>" : "") + srcLink(e[E_SRC]) + "</div></li>";
    });
    $("#events").innerHTML = html;
    $("#tl-count").textContent = n + " " + T("events", "digwyddiad");
    evEls = $$("#events .ev"); active = -1;
    $("#dial-bar").innerHTML = ERAS.map(function (E) { return '<div data-era="' + E.id + '" style="--n:' + counts[E.id] + '"><i></i></div>'; }).join("");
    onScroll();
  }
  function showYear(e) {
    var to = e[E_Y], from = shownYear, el = $("#dial-yr"), st = null;
    function paint(v) { var neg = v < 0, a = Math.round(Math.abs(v)); el.innerHTML = (e[E_C] ? '<small style="margin:0 .2em 0 0">c.</small>' : "") + a.toLocaleString("en-GB") + (neg ? "<small>" + T("BC", "CC") + "</small>" : (a < 1000 ? "<small>" + T("AD", "OC") + "</small>" : "")); }
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
      '<p class="desc">' + esc(T(p.dEn, p.dCy)) + "</p>" + '<div style="display:flex;gap:1.2rem;flex-wrap:wrap;align-items:center"><a class="src" style="color:var(--ink)" href="place-' + p.id + '.html">' + T("Read the full story", "Darllen y stori lawn") + " →</a>" + srcLink(p.src) + (p.ph ? '<a class="credit" href="' + p.ph[1] + '" target="_blank" rel="noopener">' + T("Photo: Wikimedia Commons", "Llun: Wikimedia Commons") + " ↗</a>" : "") + "</div>" +
      '<div class="row">' + (evIdx >= 0 ? '<button type="button" class="btn" data-tl="' + evIdx + '">' + T("See it on the timeline", "Gweld ar y llinell amser") + "</button>" : "<span></span>") +
      '<div class="nav-btns"><button type="button" class="icon-btn" id="pl-prev" aria-label="' + T("Previous place", "Lle blaenorol") + '"><svg><use href="#i-left"/></svg></button><span class="people-count" style="align-self:center;min-width:3.2rem;text-align:center">' + (i + 1) + " / " + visible.length + '</span><button type="button" class="icon-btn" id="pl-next" aria-label="' + T("Next place", "Lle nesaf") + '"><svg><use href="#i-right"/></svg></button></div></div>';
    $("#pl-prev").onclick = function () { selectPlace(visible[(i - 1 + visible.length) % visible.length].id); };
    $("#pl-next").onclick = function () { selectPlace(visible[(i + 1) % visible.length].id); };
  }
  $("#pins").addEventListener("click", function (ev) { var g = ev.target.closest(".pin"); if (g) selectPlace(g.dataset.pid); });
  $("#pins").addEventListener("keydown", function (ev) { var g = ev.target.closest(".pin"); if (g && (ev.key === "Enter" || ev.key === " ")) { ev.preventDefault(); selectPlace(g.dataset.pid); var n = $('.pin[data-pid="' + g.dataset.pid + '"]'); if (n) n.focus(); } });

  /* ---------- Map: kingdoms ---------- */
  var kgStage = 5, kgTimer = 0;
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
    var card = $("#kg-card");
    card.innerHTML = '<p class="eyebrow">' + T("The changing map", "Y map yn newid") + '</p><h3 class="kg-stage">' + esc(T(K.en, K.cy)) + "</h3><p class=\"desc\">" + esc(T(K.nEn, K.nCy)) + '</p><ul class="kg-legend">' +
      K.groups.map(function (g) { return '<li style="--k:' + g[2] + '"><i></i>' + esc(T(g[0], g[1])) + "</li>"; }).join("") + "</ul>" +
      '<div class="kg-range"><label for="kg-in" class="eyebrow">' + T("Move through time", "Symud drwy amser") + '</label><input type="range" id="kg-in" min="0" max="' + (D.KINGDOMS.length - 1) + '" step="1" value="' + kgStage + '"><div class="kg-ticks">' +
      D.KINGDOMS.map(function (k, n) { return "<span" + (n === kgStage ? ' class="on"' : "") + ">" + (k.id === "today" ? T("Now", "Nawr") : k.id.replace("c", "")) + "</span>"; }).join("") + '</div><div class="kg-btns"><button type="button" class="btn" id="kg-prev" aria-label="' + T("Earlier", "Cynharach") + '">←</button><button type="button" class="btn solid" id="kg-play">' + (kgTimer ? T("Pause", "Oedi") : "▶ " + T("Play through time", "Chwarae drwy amser")) + '</button><button type="button" class="btn" id="kg-next" aria-label="' + T("Later", "Diweddarach") + '">→</button></div></div><p class="kg-note">' + T("Approximate: borders are drawn using modern council areas as building blocks.", "Bras: lluniwyd y ffiniau gan ddefnyddio ardaloedd cynghorau modern.") + "</p>";
    $("#kg-in").oninput = function () { kgStop(); kgStage = +this.value; renderKg(); var i = $("#kg-in"); if (i) i.focus(); };
    $("#kg-prev").onclick = function () { kgStop(); kgStage = Math.max(0, kgStage - 1); renderKg(); $("#kg-prev").focus(); };
    $("#kg-next").onclick = function () { kgStop(); kgStage = Math.min(D.KINGDOMS.length - 1, kgStage + 1); renderKg(); $("#kg-next").focus(); };
    $("#kg-play").onclick = function () {
      if (kgTimer) { kgStop(); renderKg(); } else {
        if (kgStage >= D.KINGDOMS.length - 1) kgStage = 0; else kgStage++;
        kgTimer = setInterval(function () { if (kgStage >= D.KINGDOMS.length - 1) { kgStop(); } else kgStage++; renderKg(); }, 2600);
        renderKg();
      }
      $("#kg-play").focus();
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
  var pEra = "all", pAll = false;
  function initials(n) { var w = n.replace(/\b(ap|ab|ferch|the|of|yr|y)\b/gi, " ").trim().split(/\s+/); return (w[0].charAt(0) + (w.length > 1 ? w[w.length - 1].charAt(0) : "")).toUpperCase(); }
  function renderPeople() {
    var counts = {}; PEOPLE.forEach(function (p) { counts[p[1]] = (counts[p[1]] || 0) + 1; });
    chips($("#people-filter"), pEra, function (v) { pEra = v; renderPeople(); }, counts);
    var list = PEOPLE.filter(function (p) { return pEra === "all" || p[1] === pEra; }), total = list.length;
    var short = pEra === "all" && !pAll;
    if (short) list = D.FEATURED.map(function (s) { return PEOPLE.filter(function (p) { return p[0] === s; })[0]; }).filter(Boolean);
    $("#people-count").textContent = short ? T("12 of " + total + " people", "12 o " + total + " o bobl") : total + " " + T("people", "o bobl");
    var more = $("#people-more"); more.hidden = pEra !== "all"; more.textContent = pAll ? T("Show fewer", "Dangos llai") : T("Show all " + PEOPLE.length + " people", "Dangos pob un o’r " + PEOPLE.length);
    $("#people-grid").innerHTML = list.map(function (p) {
      var name = T(p[3], p[4]), other = lang === "en" ? p[4] : p[3], link = "person-" + p[0] + ".html", ph = D.PPH[p[0]];
      return '<article class="plaque" data-era="' + p[1] + '"><div class="top-row"><span class="ava" aria-hidden="true">' + initials(p[3]) + (ph ? '<img src="' + ph + '" alt="" loading="lazy" referrerpolicy="no-referrer" onerror="this.remove()">' : "") + '</span><div><span class="dates">' + esc(p[2]) + "</span><h3>" + esc(name) + '</h3></div></div><span class="epi">' + esc(T(p[5], p[6])) + (other !== name ? " · " + esc(other) : "") + "</span><p>" + esc(T(p[7], p[8])) + '</p><div class="links"><a class="go" href="' + link + '">' + T("Read more", "Darllen mwy") + ' →</a><button type="button" class="copy" data-copy="' + link + '">' + T("Copy link", "Copïo’r ddolen") + "</button>" + srcLink(p[9]) + "</div></article>";
    }).join("");
  }
  $("#people-more").onclick = function () { pAll = !pAll; renderPeople(); if (!pAll) goTo($("#people")); };

  /* ---------- Did you know? + daily streak ---------- */
  var factI = Math.floor(Date.now() / 864e5) % D.FACTS.length;
  function renderFact() { var f = D.FACTS[factI % D.FACTS.length]; $("#fact").textContent = T(f[0], f[1]); }
  $("#fact-next").onclick = function () { factI++; renderFact(); };
  function renderStreak() {
    var el = document.getElementById("daily-streak"); if (!el) return;
    try { var j = JSON.parse(localStorage.getItem("hc-journey") || "{}"), n = j.d && j.d.streak || 0; if (n > 0) { el.hidden = false; el.textContent = T(n + " day streak", n + " diwrnod yn olynol"); } } catch (e) {}
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

  /* ---------- Place-name decoder ---------- */
  var DICT = D.DICT, keys = Object.keys(DICT).sort(function (a, b) { return b.length - a.length; });
  function norm(s) { return s.toLowerCase().replace(/[âàá]/g, "a").replace(/[êé]/g, "e").replace(/[îí]/g, "i").replace(/[ôó]/g, "o").replace(/[ûú]/g, "u").replace(/ŵ/g, "w").replace(/ŷ/g, "y").replace(/[^a-z]/g, ""); }
  function decode(raw) {
    var s = norm(raw), out = [], unk = "", i = 0;
    while (i < s.length) {
      var hit = null;
      for (var k = 0; k < keys.length; k++) if (s.substr(i, keys[k].length) === keys[k]) { hit = keys[k]; break; }
      if (hit && !(hit === "y" && unk)) { if (unk) { out.push([unk, null]); unk = ""; } out.push([hit, DICT[hit]]); i += hit.length; }
      else { unk += s[i]; i++; }
    }
    if (unk) out.push([unk, null]);
    return out;
  }
  function renderDecoder() {
    var parts = decode($("#dec-in").value);
    $("#dec-out").innerHTML = parts.length ? parts.map(function (p, i) { return '<div class="part' + (p[1] ? "" : " unk") + '" style="--i:' + i + '"><b>' + esc(p[0]) + "</b><span>" + esc(p[1] ? T(p[1][0], p[1][1]) : T("not in this glossary", "dim yn y rhestr")) + "</span></div>"; }).join("") :
      '<p style="color:var(--muted)">' + T("Type a Welsh place name above.", "Teipiwch enw lle uchod.") + "</p>";
    $("#dec-samples").innerHTML = '<span class="eyebrow" style="align-self:center;margin-right:.25rem">' + T("Try", "Rhowch gynnig ar") + "</span>" + D.SAMPLES.map(function (s) { return '<button type="button" data-s="' + esc(s) + '">' + esc(s) + "</button>"; }).join("");
  }
  $("#dec-in").addEventListener("input", renderDecoder);
  $("#dec-form").addEventListener("submit", function (e) { e.preventDefault(); });
  $("#dec-samples").addEventListener("click", function (e) { var b = e.target.closest("[data-s]"); if (b) { $("#dec-in").value = b.dataset.s; renderDecoder(); } });
  /* ---------- Words, with play buttons ---------- */
  var AUDIO = {}; (D.AUDIO || []).forEach(function (a) { AUDIO[a] = 1; });
  var canSpeak = "speechSynthesis" in window;
  function slugW(w) { return w.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, ""); }
  function sayWord(w) {
    var slug = slugW(w[0]);
    if (AUDIO[slug]) { try { new Audio("audio/" + slug + ".mp3").play(); } catch (e) {} return; }
    if (!canSpeak) return;
    var vs = speechSynthesis.getVoices(), cy = vs.filter(function (v) { return /^cy/i.test(v.lang); })[0];
    var en = vs.filter(function (v) { return /^en-GB/i.test(v.lang); })[0] || vs.filter(function (v) { return /^en/i.test(v.lang); })[0];
    var u = new SpeechSynthesisUtterance(cy ? w[0] : w[1].toLowerCase().replace(/-/g, " "));
    if (cy) { u.voice = cy; u.lang = cy.lang; } else if (en) { u.voice = en; u.lang = en.lang; }
    u.rate = 0.8; speechSynthesis.cancel(); speechSynthesis.speak(u);
  }
  function renderWords() {
    var play = canSpeak || D.AUDIO && D.AUDIO.length;
    $("#words").innerHTML = D.WORDS.map(function (w, i) {
      return "<li><b>" + esc(w[0]) + '</b><span class="say">' + esc(w[1]) + (play ? ' <button type="button" class="play" data-w="' + i + '" aria-label="' + T("Hear ", "Clywed ") + esc(w[0]) + '">▶</button>' : "") + "</span><span>" + esc(T(w[2], w[3])) + "</span></li>";
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
    $("#read-books").innerHTML = D.READING.map(function (r) { return "<li><b>" + esc(r.t) + "</b><span>" + esc(T(r.n, r.nCy)) + "</span></li>"; }).join("");
    $("#read-online").innerHTML = D.ONLINE.map(function (r) { return '<li><a href="' + r.u + '" target="_blank" rel="noopener"><b>' + esc(T(r.t, r.tCy)) + "</b></a><span>" + esc(r.u.replace(/^https:\/\/(www\.)?/, "").replace(/\/$/, "")) + "</span></li>"; }).join("");
  }

  /* ---------- Language toggle ---------- */
  $$("[data-cy]").forEach(function (el) { el.dataset.en = el.textContent; });
  $$("[data-cy-svg]").forEach(function (el) { el.dataset.enSvg = el.textContent; });
  function applyLang() {
    document.documentElement.lang = lang; document.documentElement.classList.toggle("cy", lang === "cy");
    $("#lang-en").setAttribute("aria-pressed", lang === "en"); $("#lang-cy").setAttribute("aria-pressed", lang === "cy");
    $$("[data-cy]").forEach(function (el) { el.textContent = lang === "cy" ? el.dataset.cy : el.dataset.en; });
    $$("[data-cy-svg]").forEach(function (el) { el.textContent = lang === "cy" ? el.dataset.cySvg : el.dataset.enSvg; });
    renderChapters(); renderToday(); renderTimeline(); renderPeople(); renderFact(); renderStreak(); renderChart(); renderDecoder(); renderWords(); renderSources(); renderNear(); renderGame(); selectPlace(sel); if (mode === "kg") renderKg(); renderQuiz();
    if (!ov.hidden) { var m = /^#pennod-(\w+)/.exec(location.hash); if (m) openChapter(m[1], false); }
  }
  function setLang(l) { lang = l; try { localStorage.setItem("hc-lang", l); } catch (e) {} applyLang(); }
  $("#lang-en").onclick = function () { setLang("en"); };
  $("#lang-cy").onclick = function () { setLang("cy"); };

  renderGrat(); renderLAs();
  applyLang();
  route();
})();
