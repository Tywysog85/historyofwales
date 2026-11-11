/* The castles of Wales map (castles.html).
   Data comes from build.py as window.CASTLES:
     c  rows [q, en, cy, x, y, group, kind, date, area, lat, lon, hasStory]   x, y in map units (600 x 671, as src/geo/map.json)
     d  details by Wikidata id {b, bc (built by), n, nc (note), l (links), ph (photo url, file page, credit en, credit cy)}
     k  kinds {kind: [en, cy, about en, about cy]}   g groups [[en, cy, colour]]   la areas [[en, cy]]
   The picture under the dots is src/static/relief-1200.webp (relief-3600.webp once you zoom in), baked by tools/bake_relief.py. */
(function () {
  "use strict";
  var D = window.CASTLES;
  var map = document.getElementById("cm-map");
  if (!D || !map) return;
  var NS = "http://www.w3.org/2000/svg";
  var W = D.W, H = D.H;
  var rows = D.c, N = rows.length;
  var html = document.documentElement;
  function cy() { return html.classList.contains("cy"); }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function bi(en, c, tag) { tag = tag || "span"; if (c == null || c === en) return esc(en); return "<" + tag + ' class="l-en" lang="en">' + esc(en) + "</" + tag + "><" + tag + ' class="l-cy" lang="cy">' + esc(c) + "</" + tag + ">"; }
  function cyDate(s) { return (D.dc && D.dc[s]) || String(s || "").replace(/c\. /g, "tua "); }   // Welsh dates come from build.py (castle_date_cy)
  function el(tag, attrs, parent) { var n = document.createElementNS(NS, tag); for (var a in attrs) n.setAttribute(a, attrs[a]); if (parent) parent.appendChild(n); return n; }

  /* ---------- the picture ---------- */
  var svg = el("svg", { viewBox: "0 0 " + W + " " + H, role: "img", "aria-label": "Map of Wales with castles" });
  svg.setAttribute("preserveAspectRatio", "xMidYMid meet");
  var defs = el("defs", {}, svg);
  var glow = el("radialGradient", { id: "cm-sel" }, defs);
  el("stop", { offset: "0", "stop-color": "#fff", "stop-opacity": ".55" }, glow);
  el("stop", { offset: "1", "stop-color": "#fff", "stop-opacity": "0" }, glow);
  el("rect", { x: -W, y: -H, width: W * 3, height: H * 3, fill: "#121a2a" }, svg);
  el("image", { href: "relief-1200.webp", x: 0, y: 0, width: W, height: H, preserveAspectRatio: "none" }, svg);
  var hi = el("image", { x: 0, y: 0, width: W, height: H, preserveAspectRatio: "none" }, svg);
  el("path", { d: D.counties, fill: "none", stroke: "rgba(236,233,225,.16)", "stroke-width": ".6", "vector-effect": "non-scaling-stroke", "stroke-dasharray": "3 3" }, svg);
  var gLayer = [];
  var order = [4, 3, 2, 1, 0];          // draw the red Welsh-built dots on top
  var groupsG = el("g", {}, svg);
  order.forEach(function (gi) { gLayer[gi] = el("g", { "data-g": gi }, groupsG); });
  var dots = new Array(N);
  var BIG = [];
  for (var i = 0; i < N; i++) {
    var r = rows[i], g = r[5];
    var big = g === 0 || r[11] === 1;
    BIG[i] = big;
    var c = el("circle", { cx: r[3], cy: r[4], r: 1, fill: D.g[g][2], stroke: g === 0 ? "#f6d77a" : "rgba(10,12,20,.75)" }, gLayer[g]);
    dots[i] = c;
  }
  var selG = el("g", { "pointer-events": "none" }, svg);
  var selHalo = el("circle", { r: 0, fill: "url(#cm-sel)", opacity: 0 }, selG);
  var selRing = el("circle", { r: 0, fill: "none", stroke: "#fff", "stroke-width": "1", opacity: 0 }, selG);
  var youG = el("g", { "pointer-events": "none", opacity: 0 }, svg);
  var youDot = el("circle", { r: 2, fill: "#4da3ff", stroke: "#fff" }, youG);
  var labels = el("g", { class: "cm-labels", "pointer-events": "none" }, svg);
  map.insertBefore(svg, map.firstChild);

  /* ---------- view: pan and zoom by moving the viewBox ---------- */
  var vb = { x: 0, y: 0, w: W, h: H };
  var MINW = 22;
  var shown = [true, true, true, true, true];
  function aspect() { var b = map.getBoundingClientRect(); return b.width && b.height ? b.height / b.width : H / W; }
  function fit() {
    // keep the whole of Wales in view at the widest zoom, whatever the box shape
    var a = aspect();
    if (H / W > a) { vb.h = H; vb.w = H / a; } else { vb.w = W; vb.h = W * a; }
    vb.x = (W - vb.w) / 2; vb.y = (H - vb.h) / 2;
  }
  function maxW() { var a = aspect(); return H / W > a ? H / a : W; }
  function clamp() {
    var a = aspect(), mw = maxW();
    vb.w = Math.max(MINW, Math.min(mw, vb.w)); vb.h = vb.w * a;
    var padX = vb.w * .35, padY = vb.h * .35;
    if (vb.w >= mw - .01) { vb.x = (W - vb.w) / 2; vb.y = (H - vb.h) / 2; return; }
    vb.x = Math.max(-padX, Math.min(W - vb.w + padX, vb.x));
    vb.y = Math.max(-padY, Math.min(H - vb.h + padY, vb.y));
  }
  var raf = 0, labelT = 0;
  function apply() {
    raf = 0;
    svg.setAttribute("viewBox", vb.x.toFixed(2) + " " + vb.y.toFixed(2) + " " + vb.w.toFixed(2) + " " + vb.h.toFixed(2));
    var px = vb.w / Math.max(1, map.clientWidth);      // map units per screen pixel
    var zoom = maxW() / vb.w;
    var boost = Math.pow(zoom, .45);
    for (var i = 0; i < N; i++) {
      var rr = (BIG[i] ? (rows[i][5] === 0 ? 5 : 4.2) : 3) * boost * px;
      dots[i].setAttribute("r", rr.toFixed(3));
      dots[i].setAttribute("stroke-width", ((rows[i][5] === 0 ? 1.4 : .8) * px).toFixed(3));
    }
    if (sel >= 0) { var s0 = 5 * boost * px; selRing.setAttribute("r", (s0 + 4 * px).toFixed(3)); selRing.setAttribute("stroke-width", (2 * px).toFixed(3)); selHalo.setAttribute("r", (s0 * 4).toFixed(3)); }
    youDot.setAttribute("r", (6 * px).toFixed(3)); youDot.setAttribute("stroke-width", (2 * px).toFixed(3));
    if (zoom > 2.2 && !hi.getAttribute("href")) hi.setAttribute("href", "relief-3600.webp");
    clearTimeout(labelT); labelT = setTimeout(drawLabels, 120);
    hint.classList.toggle("off", zoom > 1.05);
  }
  function redraw() { if (!raf) raf = requestAnimationFrame(apply); }
  function drawLabels() {
    while (labels.firstChild) labels.removeChild(labels.firstChild);
    var px = vb.w / Math.max(1, map.clientWidth), zoom = maxW() / vb.w;
    if (zoom < 2.4) return;
    var fs = 12.5 * px, all = zoom > 7, c = cy(), placed = [], n = 0;
    var cand = [];
    for (var i = 0; i < N; i++) {
      var r = rows[i];
      if (!shown[r[5]]) continue;
      if (r[3] < vb.x || r[3] > vb.x + vb.w || r[4] < vb.y || r[4] > vb.y + vb.h) continue;
      if (!all && !BIG[i]) continue;
      cand.push(i);
    }
    cand.sort(function (a, b) { return (BIG[b] - BIG[a]) || (rows[a][5] - rows[b][5]); });
    for (var k = 0; k < cand.length && n < 90; k++) {
      var j = cand[k], rw = rows[j], name = c ? rw[2] : rw[1];
      var w = name.length * fs * .52, x = rw[3] + 7 * px, y = rw[4] + fs * .35;
      var clash = placed.some(function (p) { return x < p[2] && x + w > p[0] && y - fs < p[3] && y > p[1]; });
      if (clash) continue;
      placed.push([x, y - fs, x + w, y]);
      var t = el("text", { x: x.toFixed(2), y: y.toFixed(2), "font-size": fs.toFixed(3), "stroke-width": (3 * px).toFixed(3) }, labels);
      t.textContent = name; n++;
    }
  }
  function toMap(cx, cyy) {
    var b = map.getBoundingClientRect();
    return { x: vb.x + (cx - b.left) / b.width * vb.w, y: vb.y + (cyy - b.top) / b.height * vb.h };
  }
  function zoomAt(f, cx, cyy) {
    var p = cx == null ? { x: vb.x + vb.w / 2, y: vb.y + vb.h / 2 } : toMap(cx, cyy);
    var nw = Math.max(MINW, Math.min(maxW(), vb.w / f)), k = nw / vb.w;
    vb.x = p.x - (p.x - vb.x) * k; vb.y = p.y - (p.y - vb.y) * k; vb.w = nw; vb.h = nw * aspect();
    clamp(); redraw();
  }
  var anim = 0;
  function flyTo(x, y, w, ms) {
    cancelAnimationFrame(anim);
    var a = aspect(), from = { x: vb.x, y: vb.y, w: vb.w }, to = { w: Math.max(MINW, Math.min(maxW(), w)) };
    to.x = x - to.w / 2; to.y = y - to.w * a / 2;
    var t0 = performance.now(), dur = matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : (ms || 700);
    (function step(now) {
      var t = dur ? Math.min(1, (now - t0) / dur) : 1, e = t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
      vb.w = from.w + (to.w - from.w) * e; vb.h = vb.w * a;
      vb.x = from.x + (to.x - from.x) * e; vb.y = from.y + (to.y - from.y) * e;
      clamp(); apply();
      if (t < 1) anim = requestAnimationFrame(step);
    })(t0);
  }

  /* ---------- pointer: drag, pinch, tap ---------- */
  var hint = document.getElementById("cm-hint");
  var pts = {}, start = null, moved = 0, last = null, pinch = null;
  map.addEventListener("pointerdown", function (ev) {
    if (ev.target.closest && ev.target.closest(".cm-zoom")) return;
    map.setPointerCapture(ev.pointerId);
    pts[ev.pointerId] = { x: ev.clientX, y: ev.clientY };
    var ids = Object.keys(pts);
    if (ids.length === 1) { start = { x: ev.clientX, y: ev.clientY, t: Date.now() }; moved = 0; last = { x: ev.clientX, y: ev.clientY }; }
    if (ids.length === 2) { var a = pts[ids[0]], b = pts[ids[1]]; pinch = { d: Math.hypot(a.x - b.x, a.y - b.y), w: vb.w }; moved = 99; }
    cancelAnimationFrame(anim);
  });
  map.addEventListener("pointermove", function (ev) {
    if (!pts[ev.pointerId]) return;
    pts[ev.pointerId] = { x: ev.clientX, y: ev.clientY };
    var ids = Object.keys(pts);
    if (ids.length === 2 && pinch) {
      var a = pts[ids[0]], b = pts[ids[1]], d = Math.hypot(a.x - b.x, a.y - b.y);
      var mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2;
      zoomAt(vb.w / (pinch.w * pinch.d / d), mx, my);
      return;
    }
    if (ids.length === 1 && last) {
      var dx = ev.clientX - last.x, dy = ev.clientY - last.y;
      moved += Math.abs(dx) + Math.abs(dy);
      var bx = map.getBoundingClientRect();
      vb.x -= dx / bx.width * vb.w; vb.y -= dy / bx.height * vb.h;
      last = { x: ev.clientX, y: ev.clientY };
      clamp(); redraw();
    }
  });
  function up(ev) {
    if (!pts[ev.pointerId]) return;
    delete pts[ev.pointerId];
    var ids = Object.keys(pts);
    if (ids.length < 2) pinch = null;
    if (ids.length === 1) { last = pts[ids[0]]; return; }
    if (ev.type === "pointerup" && start && moved < 8 && Date.now() - start.t < 600) tapAt(ev.clientX, ev.clientY);
    start = null; last = null;
  }
  map.addEventListener("pointerup", up);
  map.addEventListener("pointercancel", up);
  map.addEventListener("wheel", function (ev) {
    ev.preventDefault();
    zoomAt(Math.pow(1.0018, -ev.deltaY * (ev.deltaMode === 1 ? 30 : 1)), ev.clientX, ev.clientY);
  }, { passive: false });
  map.addEventListener("dblclick", function (ev) { ev.preventDefault(); zoomAt(2, ev.clientX, ev.clientY); });
  map.addEventListener("keydown", function (ev) {
    var s = vb.w * .12, k = ev.key;
    if (k === "+" || k === "=") zoomAt(1.5); else if (k === "-" || k === "_") zoomAt(1 / 1.5);
    else if (k === "ArrowLeft") { vb.x -= s; clamp(); redraw(); } else if (k === "ArrowRight") { vb.x += s; clamp(); redraw(); }
    else if (k === "ArrowUp") { vb.y -= s; clamp(); redraw(); } else if (k === "ArrowDown") { vb.y += s; clamp(); redraw(); }
    else return;
    ev.preventDefault();
  });
  document.getElementById("cm-in").addEventListener("click", function () { zoomAt(1.8); });
  document.getElementById("cm-out").addEventListener("click", function () { zoomAt(1 / 1.8); });
  document.getElementById("cm-home").addEventListener("click", function () { var w0 = maxW(); flyTo(W / 2, H / 2, w0); });
  function tapAt(cx, cyy) {
    var b = map.getBoundingClientRect(), best = -1, bd = 22;
    for (var i = 0; i < N; i++) {
      var r = rows[i];
      if (!shown[r[5]]) continue;
      var sx = b.left + (r[3] - vb.x) / vb.w * b.width, sy = b.top + (r[4] - vb.y) / vb.h * b.height;
      var d = Math.hypot(sx - cx, sy - cyy) - (BIG[i] ? 3 : 0);
      if (d < bd) { bd = d; best = i; }
    }
    if (best >= 0) select(best, false);
  }

  /* ---------- the card ---------- */
  var card = document.getElementById("cm-card");
  var sel = -1;
  function kmFrom(lat1, lon1, lat2, lon2) {
    var R = 6371, t = Math.PI / 180, a = Math.sin((lat2 - lat1) * t / 2), o = Math.sin((lon2 - lon1) * t / 2);
    return 2 * R * Math.asin(Math.sqrt(a * a + Math.cos(lat1 * t) * Math.cos(lat2 * t) * o * o));
  }
  function select(i, fly) {
    sel = i;
    var r = rows[i], d = D.d[r[0]] || {}, g = D.g[r[5]], k = D.k[r[6]] || D.k[""];
    selG.setAttribute("transform", "translate(" + r[3] + " " + r[4] + ")");
    selRing.setAttribute("opacity", 1); selHalo.setAttribute("opacity", 1);
    var h = "";
    if (d.ph) h += '<figure class="cm-photo"><img src="' + esc(d.ph[0]) + '" alt="' + esc(r[1]) + '" decoding="async" referrerpolicy="no-referrer" onerror="this.closest(\'figure\').remove()"><figcaption><a href="' + esc(d.ph[1]) + '" target="_blank" rel="noopener">' + bi(d.ph[2], d.ph[3]) + "</a></figcaption></figure>";
    h += '<p class="eyebrow cm-g" style="--gc:' + g[2] + '"><i></i>' + bi(g[0], g[1]) + "</p>";
    h += "<h2>" + bi(r[1], r[2]) + "</h2>";
    if (r[1] !== r[2]) h += '<p class="cm-alt">' + bi(r[2], r[1]) + "</p>";
    h += '<dl class="cm-facts">';
    if (d.b) h += "<dt>" + bi("Built by", "Codwyd gan") + "</dt><dd>" + bi(d.b, d.bc) + "</dd>";
    if (r[7]) h += "<dt>" + bi("When", "Pryd") + "</dt><dd>" + bi(r[7], cyDate(r[7])) + "</dd>";
    h += "<dt>" + bi("What it is", "Beth yw e") + "</dt><dd>" + bi(k[0], k[1]) + "</dd>";
    h += "<dt>" + bi("Where", "Ble") + "</dt><dd>" + bi(D.la[r[8]][0], D.la[r[8]][1]) + "</dd>";
    if (you) h += "<dt>" + bi("From you", "O’ch lle chi") + "</dt><dd>" + Math.round(kmFrom(you.lat, you.lon, r[9], r[10])) + " km</dd>";
    h += "</dl>";
    if (d.n) h += '<p class="cm-note">' + bi(d.n, d.nc) + "</p>";
    else if (k[2] && r[6] !== "stone") h += '<p class="cm-note muted">' + bi(k[2], k[3]) + "</p>";
    h += '<p class="cm-links">';
    (d.l || []).forEach(function (l) { h += '<a class="go" href="' + esc(l[0]) + '">' + bi(l[1], l[2]) + " →</a>"; });
    h += '<a href="https://www.google.com/maps/dir/?api=1&amp;destination=' + r[9] + "," + r[10] + '" target="_blank" rel="noopener">' + bi("Directions", "Cyfarwyddiadau") + " ↗</a>";
    h += '<a href="https://www.openstreetmap.org/?mlat=' + r[9] + "&amp;mlon=" + r[10] + "#map=16/" + r[9] + "/" + r[10] + '" target="_blank" rel="noopener">' + bi("Open in a map", "Agor mewn map") + " ↗</a>";
    h += '<a href="https://www.wikidata.org/wiki/' + r[0] + '" target="_blank" rel="noopener">' + bi("Record", "Cofnod") + " ↗</a></p>";
    h += '<p class="cm-access muted">' + bi("Many castle sites are on private land. Please check access before you visit.", "Mae llawer o safleoedd cestyll ar dir preifat. Gwiriwch fynediad cyn ymweld.") + "</p>";
    card.innerHTML = h;
    card.classList.remove("pop"); void card.offsetWidth; card.classList.add("pop");
    try { history.replaceState(null, "", "#castle-" + r[0]); } catch (e) { }
    if (fly) flyTo(r[3], r[4], Math.min(vb.w, maxW() / 5));
    else redraw();
    if (matchMedia("(max-width: 899px)").matches && fly !== "nos") {
      var bx = card.getBoundingClientRect();
      if (bx.top > innerHeight - 80) card.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  /* ---------- filters ---------- */
  Array.prototype.forEach.call(document.querySelectorAll(".cm-chip"), function (b) {
    b.addEventListener("click", function () {
      var g = +b.getAttribute("data-g"); shown[g] = !shown[g];
      b.classList.toggle("on", shown[g]); b.setAttribute("aria-pressed", shown[g]);
      gLayer[g].style.display = shown[g] ? "" : "none";
      drawLabels();
    });
  });

  /* ---------- search ---------- */
  var q = document.getElementById("cm-q"), res = document.getElementById("cm-res");
  function norm(s) { return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[’'`]/g, ""); }
  var keys = rows.map(function (r) { return norm(r[1] + " " + r[2]); });
  var hits = [], act = -1;
  function showRes() {
    var t = norm(q.value.trim());
    hits = [];
    if (t.length >= 2) {
      for (var i = 0; i < N && hits.length < 60; i++) if (keys[i].indexOf(t) >= 0) hits.push(i);
      hits.sort(function (a, b) { return (rows[b][11] - rows[a][11]) || (keys[a].indexOf(t) - keys[b].indexOf(t)); });
      hits = hits.slice(0, 8);
    }
    act = -1;
    if (!hits.length) { res.hidden = true; res.innerHTML = t.length >= 2 ? "" : ""; if (t.length >= 2) { res.innerHTML = '<li class="none">' + bi("No castle by that name", "Dim castell o’r enw hwnnw") + "</li>"; res.hidden = false; } return; }
    res.innerHTML = hits.map(function (i, k) { var r = rows[i]; return '<li role="option" id="cm-o' + k + '" data-i="' + i + '" style="--gc:' + D.g[r[5]][2] + '"><i></i>' + bi(r[1], r[2]) + "<small>" + bi(D.la[r[8]][0], D.la[r[8]][1]) + "</small></li>"; }).join("");
    res.hidden = false;
  }
  q.addEventListener("input", showRes);
  q.addEventListener("keydown", function (ev) {
    if (ev.key === "ArrowDown" || ev.key === "ArrowUp") {
      if (!hits.length) return; ev.preventDefault();
      act = (act + (ev.key === "ArrowDown" ? 1 : -1) + hits.length) % hits.length;
      Array.prototype.forEach.call(res.children, function (li, k) { li.classList.toggle("act", k === act); });
    } else if (ev.key === "Enter") {
      ev.preventDefault(); var i = hits[act >= 0 ? act : 0]; if (i != null) pick(i);
    } else if (ev.key === "Escape") { res.hidden = true; }
  });
  res.addEventListener("click", function (ev) { var li = ev.target.closest("li[data-i]"); if (li) pick(+li.getAttribute("data-i")); });
  document.addEventListener("click", function (ev) { if (!ev.target.closest(".cm-search")) res.hidden = true; });
  function pick(i) {
    res.hidden = true; q.value = cy() ? rows[i][2] : rows[i][1]; q.blur();
    if (!shown[rows[i][5]]) document.querySelector('.cm-chip[data-g="' + rows[i][5] + '"]').click();
    toMapView(); select(i, true);
  }
  function setPh() { q.placeholder = q.getAttribute(cy() ? "data-ph-cy" : "data-ph-en"); }
  setPh();
  new MutationObserver(function () { setPh(); drawLabels(); }).observe(html, { attributes: true, attributeFilter: ["class"] });

  /* ---------- near me ---------- */
  var you = null;
  function project(lat, lon) {   // the same projection as build.py and src/geo/map.json
    var P = D.P;
    return { x: (lon - P[0]) * P[2] * P[3], y: (P[1] - lat) * P[3] };
  }
  var nearBtn = document.getElementById("cm-near");
  nearBtn.addEventListener("click", function () {
    if (!navigator.geolocation) return nearMsg("Your device cannot share its location.", "Ni all eich dyfais rannu ei lleoliad.");
    nearBtn.disabled = true;
    navigator.geolocation.getCurrentPosition(function (p) {
      nearBtn.disabled = false;
      you = { lat: p.coords.latitude, lon: p.coords.longitude };
      var list = rows.map(function (r, i) { return [kmFrom(you.lat, you.lon, r[9], r[10]), i]; }).sort(function (a, b) { return a[0] - b[0]; }).slice(0, 10);
      var pt = project(you.lat, you.lon);
      youG.setAttribute("transform", "translate(" + pt.x + " " + pt.y + ")"); youG.setAttribute("opacity", 1);
      var h = '<p class="eyebrow">' + bi("Near you", "Yn agos atoch") + "</p><h2>" + bi("The ten castles nearest to you", "Y deg castell agosaf atoch") + '</h2><ol class="cm-near">';
      list.forEach(function (x) { var r = rows[x[1]]; h += '<li><button type="button" class="cm-show" data-i="' + x[1] + '" style="--gc:' + D.g[r[5]][2] + '"><i></i>' + bi(r[1], r[2]) + "<small>" + (x[0] < 10 ? x[0].toFixed(1) : Math.round(x[0])) + " km</small></button></li>"; });
      h += "</ol>";
      if (list[0][0] > 60) h += '<p class="muted">' + bi("You look to be a long way from Wales. Here are the nearest castles all the same.", "Mae’n ymddangos eich bod ymhell o Gymru. Dyma’r cestyll agosaf er hynny.") + "</p>";
      card.innerHTML = h;
      toMapView();
      var far = rows[list[list.length - 1][1]];
      if (list[0][0] < 60) flyTo(pt.x, pt.y, Math.max(40, Math.abs(far[3] - pt.x) * 2.6, Math.abs(far[4] - pt.y) * 2.6 / aspect()));
      else flyTo(rows[list[0][1]][3], rows[list[0][1]][4], maxW() / 3);
    }, function () {
      nearBtn.disabled = false;
      nearMsg("We could not get your location. Check that location is allowed for this site.", "Ni allem gael eich lleoliad. Gwiriwch fod lleoliad wedi’i ganiatáu i’r wefan hon.");
    }, { enableHighAccuracy: false, timeout: 12000, maximumAge: 600000 });
  });
  function nearMsg(en, c) { card.innerHTML = '<p class="eyebrow">' + bi("Near you", "Yn agos atoch") + "</p><p>" + bi(en, c) + "</p>"; }

  /* ---------- surprise me ---------- */
  document.getElementById("cm-rand").addEventListener("click", function () {
    var pool = []; for (var i = 0; i < N; i++) if (rows[i][11] && shown[rows[i][5]]) pool.push(i);
    if (!pool.length) for (i = 0; i < N; i++) if (shown[rows[i][5]]) pool.push(i);
    if (pool.length) select(pool[Math.floor(Math.random() * pool.length)], true);
  });

  /* ---------- "show on the map" buttons in the page ---------- */
  var byQ = {}; rows.forEach(function (r, i) { byQ[r[0]] = i; });
  function toMapView() {
    var b = map.getBoundingClientRect();
    if (b.top < 0 || b.bottom > innerHeight + 40) document.getElementById("map").scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" });
  }
  document.addEventListener("click", function (ev) {
    var b = ev.target.closest(".cm-show"); if (!b) return;
    var i = b.hasAttribute("data-i") ? +b.getAttribute("data-i") : byQ[b.getAttribute("data-q")];
    if (i == null) return;
    if (!shown[rows[i][5]]) document.querySelector('.cm-chip[data-g="' + rows[i][5] + '"]').click();
    if (!card.contains(b)) toMapView();
    select(i, true);
  });

  /* ---------- start ---------- */
  fit(); apply();
  var lastW = map.clientWidth, lastH = map.clientHeight;
  new ResizeObserver(function () {
    if (map.clientWidth === lastW && map.clientHeight === lastH) return;
    var cx = vb.x + vb.w / 2, cy0 = vb.y + vb.h / 2, z = maxW() / vb.w;
    lastW = map.clientWidth; lastH = map.clientHeight;
    vb.w = maxW() / Math.max(1, z); vb.h = vb.w * aspect(); vb.x = cx - vb.w / 2; vb.y = cy0 - vb.h / 2; clamp(); apply();
  }).observe(map);
  function fromHash() {
    var m = /castle-(Q\d+)/.exec(location.hash);
    if (m && byQ[m[1]] != null) { select(byQ[m[1]], true); return true; }
    return false;
  }
  if (location.hash) setTimeout(function () { if (fromHash()) toMapView(); }, 60);
  addEventListener("hashchange", fromHash);
})();
