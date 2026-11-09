(function () {
  var D = DATA, ERAS = D.ERAS, EVENTS = D.EVENTS, PLACES = D.PLACES, PEOPLE = D.PEOPLE, MAPC = D.MAPC;
  var WIKI = "https://en.wikipedia.org/wiki/";
  var lang = "en";
  try { if (localStorage.getItem("hc-lang") === "cy") lang = "cy"; } catch (e) {}
  var $ = function (s, r) { return (r || document).querySelector(s); };
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
  var cv = $("#sky"), cx = cv.getContext("2d"), W = 0, H = 0, dpr = 1, mouse = 0, ridges = [], stars = [];
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
  function size() { var r = cv.getBoundingClientRect(); dpr = Math.min(window.devicePixelRatio || 1, 2); W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; draw(); }
  var t0 = 0;
  function draw(t) {
    t = t || t0;
    var sy = Math.min(window.scrollY, H);
    cx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var g = cx.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, "#0b0e16"); g.addColorStop(0.55, "#1a2032"); g.addColorStop(0.8, "#3a2a35"); g.addColorStop(1, "#0e1118");
    cx.fillStyle = g; cx.fillRect(0, 0, W, H);
    stars.forEach(function (s) { var tw = 0.5 + 0.5 * Math.sin(t / 900 + s[3] * 20); cx.fillStyle = "rgba(236,233,225," + (0.15 + 0.5 * tw * s[2] / 1.4) + ")"; cx.fillRect(s[0] * W, s[1] * H - sy * 0.02, s[2], s[2]); });
    var narrow = W < 640, mx = W * (narrow ? 0.84 : 0.74) - mouse * 10, my = H * (narrow ? 0.1 : 0.3) - sy * 0.03, mr = Math.max(28, Math.min(W, H) * 0.07);
    var mg = cx.createRadialGradient(mx, my, mr * 0.6, mx, my, mr * 4.5); mg.addColorStop(0, "rgba(226,69,61,.22)"); mg.addColorStop(1, "rgba(226,69,61,0)");
    cx.fillStyle = mg; cx.fillRect(0, 0, W, H);
    cx.fillStyle = "#e9d9c6"; cx.beginPath(); cx.arc(mx, my, mr, 0, 7); cx.fill();
    LAYERS.forEach(function (L, i) {
      var w = ridges[i], base = H * L.y + sy * L.s * 0.6, off = mouse * (i + 1) * 6;
      cx.beginPath(); cx.moveTo(0, H);
      for (var x = 0; x <= W + 8; x += 6) {
        var u = (x + off) / Math.max(W, 900) * 3, v = 0;
        for (var k = 0; k < w.length; k++) v += Math.sin(u * w[k][1] + w[k][0]) * w[k][2];
        v = Math.abs(v) * 0.6 + v * 0.4;
        cx.lineTo(x, base - v * H * L.a);
      }
      cx.lineTo(W, H); cx.closePath(); cx.fillStyle = L.c; cx.fill();
      if (i === 1 || i === 3) { var fg = cx.createLinearGradient(0, base - H * 0.08, 0, base + H * 0.05); fg.addColorStop(0, "rgba(160,170,200,0)"); fg.addColorStop(0.6, "rgba(160,170,200," + (0.06 + 0.02 * Math.sin(t / 2200 + i)) + ")"); fg.addColorStop(1, "rgba(160,170,200,0)"); cx.fillStyle = fg; cx.fillRect(0, base - H * 0.08, W, H * 0.13); }
    });
  }
  function loop(t) { t0 = t; if (window.scrollY < H) draw(t); requestAnimationFrame(loop); }
  window.addEventListener("resize", size);
  if (!reduce) {
    window.addEventListener("pointermove", function (e) { mouse = (e.clientX / window.innerWidth - 0.5) * 2; }, { passive: true });
    requestAnimationFrame(loop);
  } else { window.addEventListener("scroll", function () { if (window.scrollY < H) draw(); }, { passive: true }); }
  size();

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
    $("#foot-eras").innerHTML = ERAS.map(function (e) { return '<a href="era-' + e.id + '.html">' + T(e.en, e.cy) + "</a>"; }).join("") + '<a href="#sources">' + T("Sources", "Ffynonellau") + "</a>";
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
    var j = ev.target.closest("[data-jump]"); if (j) { var id = j.dataset.jump; closeChapter(); goTo($("#era-" + id)); return; }
    if (ev.target.closest("[data-close]") && (ev.target.dataset.close || ev.target.closest(".close"))) closeChapter();
    var m = ev.target.closest("[data-map]"); if (m) { setMode("sites"); selectPlace(m.dataset.map); goTo($("#map")); }
    var t = ev.target.closest("[data-tl]"); if (t) { if (tlEra !== "all") setTlEra("all"); goTo($("#ev-" + t.dataset.tl), "center"); }
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
      var secs = ["chapters", "timeline", "map", "people", "language", "quiz"], cur = null;
      secs.forEach(function (s) { var r = document.getElementById(s).getBoundingClientRect(); if (r.top < window.innerHeight * 0.4) cur = s; });
      $$(".nav ul a").forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#" + cur); });
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
    card.innerHTML = '<div class="art"><svg aria-hidden="true"><use href="#i-' + p.ill + '"/></svg></div>' +
      '<div style="display:grid;gap:.3rem"><h3>' + esc(T(p.en, p.cy)) + "</h3>" + (other !== T(p.en, p.cy) ? '<span class="cy-name">' + esc(other) + "</span>" : "") + "</div>" +
      '<div class="meta"><span><b>' + T(E.en, E.cy) + "</b></span><span>" + esc(p.year) + "</span><span>" + p.lat.toFixed(3) + "° N, " + Math.abs(p.lon).toFixed(3) + "° W</span></div>" +
      '<p class="desc">' + esc(T(p.dEn, p.dCy)) + "</p>" + '<div>' + srcLink(p.src) + "</div>" +
      '<div class="row">' + (evIdx >= 0 ? '<button type="button" class="btn" data-tl="' + evIdx + '">' + T("See it on the timeline", "Gweld ar y llinell amser") + "</button>" : "<span></span>") +
      '<div class="nav-btns"><button type="button" class="icon-btn" id="pl-prev" aria-label="' + T("Previous place", "Lle blaenorol") + '"><svg><use href="#i-left"/></svg></button><span class="people-count" style="align-self:center;min-width:3.2rem;text-align:center">' + (i + 1) + " / " + visible.length + '</span><button type="button" class="icon-btn" id="pl-next" aria-label="' + T("Next place", "Lle nesaf") + '"><svg><use href="#i-right"/></svg></button></div></div>';
    $("#pl-prev").onclick = function () { selectPlace(visible[(i - 1 + visible.length) % visible.length].id); };
    $("#pl-next").onclick = function () { selectPlace(visible[(i + 1) % visible.length].id); };
  }
  $("#pins").addEventListener("click", function (ev) { var g = ev.target.closest(".pin"); if (g) selectPlace(g.dataset.pid); });
  $("#pins").addEventListener("keydown", function (ev) { var g = ev.target.closest(".pin"); if (g && (ev.key === "Enter" || ev.key === " ")) { ev.preventDefault(); selectPlace(g.dataset.pid); var n = $('.pin[data-pid="' + g.dataset.pid + '"]'); if (n) n.focus(); } });

  /* ---------- Map: kingdoms ---------- */
  var kgStage = 0;
  function renderLAs() { $("#las").innerHTML = Object.keys(D.LA).map(function (n) { return '<path class="la" data-la="' + esc(n) + '" d="' + D.LA[n] + '"><title>' + esc(n) + "</title></path>"; }).join(""); }
  function renderKg() {
    var K = D.KINGDOMS[kgStage], colour = {};
    K.groups.forEach(function (g) { (g[3] === "*" ? Object.keys(D.LA) : g[3]).forEach(function (n) { colour[n] = g[2]; }); });
    $$("#las .la").forEach(function (p) { p.style.fill = colour[p.dataset.la] || "#2a3142"; });
    var card = $("#kg-card");
    card.innerHTML = '<p class="eyebrow">' + T("The changing map", "Y map yn newid") + '</p><h3 class="kg-stage">' + esc(T(K.en, K.cy)) + "</h3><p class=\"desc\">" + esc(T(K.nEn, K.nCy)) + '</p><ul class="kg-legend">' +
      K.groups.map(function (g) { return '<li style="--k:' + g[2] + '"><i></i>' + esc(T(g[0], g[1])) + "</li>"; }).join("") + "</ul>" +
      '<div class="kg-range"><label for="kg-in" class="eyebrow">' + T("Move through time", "Symud drwy amser") + '</label><input type="range" id="kg-in" min="0" max="' + (D.KINGDOMS.length - 1) + '" step="1" value="' + kgStage + '"><div class="kg-ticks">' +
      D.KINGDOMS.map(function (k) { return "<span>" + (k.id === "today" ? T("Now", "Nawr") : k.id.replace("c", "")) + "</span>"; }).join("") + '</div></div><p class="kg-note">' + T("Approximate: borders are drawn using modern council areas as building blocks.", "Bras: lluniwyd y ffiniau gan ddefnyddio ardaloedd cynghorau modern.") + "</p>";
    $("#kg-in").oninput = function () { kgStage = +this.value; renderKg(); var i = $("#kg-in"); if (i) i.focus(); };
  }
  function setMode(m) {
    mode = m;
    $("#mode-sites").setAttribute("aria-pressed", m === "sites"); $("#mode-kg").setAttribute("aria-pressed", m === "kg");
    $("#las").hidden = m !== "kg"; $("#pins").style.display = m === "kg" ? "none" : ""; $("#map-filter").hidden = m === "kg";
    $("#place-card").hidden = m === "kg"; $("#kg-card").hidden = m !== "kg";
    if (m === "kg") renderKg();
  }
  $("#mode-sites").onclick = function () { setMode("sites"); };
  $("#mode-kg").onclick = function () { setMode("kg"); };

  /* ---------- People ---------- */
  var pEra = "all";
  function renderPeople() {
    var counts = {}; PEOPLE.forEach(function (p) { counts[p[1]] = (counts[p[1]] || 0) + 1; });
    chips($("#people-filter"), pEra, function (v) { pEra = v; renderPeople(); }, counts);
    var list = PEOPLE.filter(function (p) { return pEra === "all" || p[1] === pEra; });
    $("#people-count").textContent = list.length + " " + T("people", "o bobl");
    $("#people-grid").innerHTML = list.map(function (p) {
      var name = T(p[3], p[4]), other = lang === "en" ? p[4] : p[3], link = "era-" + p[1] + ".html#" + p[0];
      return '<article class="plaque" data-era="' + p[1] + '"><span class="dates">' + esc(p[2]) + "</span><h3>" + esc(name) + '</h3><span class="epi">' + esc(T(p[5], p[6])) + (other !== name ? " · " + esc(other) : "") + "</span><p>" + esc(T(p[7], p[8])) + '</p><div class="links"><a class="go" href="' + link + '">' + T("Profile", "Proffil") + ' →</a><button type="button" class="copy" data-copy="' + link + '">' + T("Copy link", "Copïo’r ddolen") + "</button>" + srcLink(p[9]) + "</div></article>";
    }).join("");
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
  function renderWords() { $("#words").innerHTML = D.WORDS.map(function (w) { return "<li><b>" + esc(w[0]) + '</b><span class="say">' + esc(w[1]) + "</span><span>" + esc(T(w[2], w[3])) + "</span></li>"; }).join(""); }

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
      var s = Q.score, msg = s >= 9 ? T("Pencampwr! A true historian.", "Pencampwr! Hanesydd go iawn.") : s >= 6 ? T("Da iawn. Very good.", "Da iawn wir.") : s >= 3 ? T("Not bad. The timeline above has every answer.", "Ddim yn ddrwg. Mae pob ateb yn y llinell amser uchod.") : T("Time to scroll the timeline and try again.", "Amser i sgrolio’r llinell amser a rhoi cynnig arall.");
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
    renderChapters(); renderToday(); renderTimeline(); renderPeople(); renderChart(); renderDecoder(); renderWords(); renderSources(); selectPlace(sel); if (mode === "kg") renderKg(); renderQuiz();
    if (!ov.hidden) { var m = /^#pennod-(\w+)/.exec(location.hash); if (m) openChapter(m[1], false); }
  }
  function setLang(l) { lang = l; try { localStorage.setItem("hc-lang", l); } catch (e) {} applyLang(); }
  $("#lang-en").onclick = function () { setLang("en"); };
  $("#lang-cy").onclick = function () { setLang("cy"); };

  renderGrat(); renderLAs();
  applyLang();
  route();
})();
