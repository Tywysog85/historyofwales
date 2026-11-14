/* Plan a day out (visit.html). The data comes from build.py as window.VPD (src/visitplan.py _payload):
     s  stops [id, en, cy, lat, lon, kind, minutes, weight, entry, who en, who cy, official url, postcode, own page, line en, line cy, picture, drawing, note en, note cy]
     t  towns [en, cy, lat, lon]   K kinds [en, cy]   L lengths {key: [en, cy, minutes, most stops, km to look, lunch]}
     B  estuaries [[mouth], [head], [[bridge] ...]]   E entry {key: [en, cy]}   G map frame [minx, maxy, k, sc, W, H]   C [road, km/h, park, lunch]
   plan() is the same, step for step, as plan() in src/visitplan.py (tools/visit_check.js checks the two agree), so a
   ready-made day opened here ("Change this day") comes out the same. The state lives in the address, so a day can be shared:
     from  a town, "s:<stop id>" (start at a place) or "@lat,lon"   len  half | day | long   k  kinds (0-5, comma)   f=1 free only
     o=1  places seen from the road   t  minutes after midnight   p  stops to keep   x  stops left out   nf=1  add nothing more */
(function () {
  "use strict";
  var D = window.VPD, form = document.getElementById("vp-form"), outEl = document.getElementById("vp-out");
  if (!D) return;
  var CY = document.documentElement.classList.contains("cy");
  var S = D.s.map(function (r) {
    return { id: r[0], en: r[1], cy: r[2], lat: r[3], lon: r[4], k: r[5], m: r[6], w: r[7], e: r[8], who: [r[9], r[10]], url: r[11], pc: r[12], href: r[13],
             dEn: r[14], dCy: r[15], pic: r[16], ill: r[17], note: r[18] ? [r[18], r[19]] : null };
  });
  var IX = {}; S.forEach(function (s, i) { IX[s.id] = i; });
  var ROAD = D.C[0], KMH = D.C[1], PARK = D.C[2], LUNCH = D.C[3];
  function T(en, cy) { return CY ? cy : en; }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function fold(s) { return String(s || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[’'‘`.,]/g, "").replace(/[-\s]+/g, " ").trim(); }

  /* ---------- the planner (src/visitplan.py) ---------- */
  var RAD = Math.PI / 180;
  function km(a, b) {
    var la1 = a[0] * RAD, lo1 = a[1] * RAD, la2 = b[0] * RAD, lo2 = b[1] * RAD;
    var h = Math.pow(Math.sin((la2 - la1) / 2), 2) + Math.cos(la1) * Math.cos(la2) * Math.pow(Math.sin((lo2 - lo1) / 2), 2);
    return 12742.0 * Math.asin(Math.min(1.0, Math.sqrt(h)));
  }
  function o3(a, b, c) { return (b[1] * .61 - a[1] * .61) * (c[0] - a[0]) - (b[0] - a[0]) * (c[1] * .61 - a[1] * .61); }
  function cross(p, q, r, s) { return ((o3(p, q, r) > 0) !== (o3(p, q, s) > 0)) && ((o3(r, s, p) > 0) !== (o3(r, s, q) > 0)); }
  function roadKm(a, b) {
    var d = km(a, b);
    for (var i = 0; i < D.B.length; i++) {
      var br = D.B[i];
      if (cross(a, b, br[0], br[1])) {
        d = Infinity;
        br[2].forEach(function (x) { d = Math.min(d, km(a, x) + km(x, b)); });
        break;
      }
    }
    return d * ROAD;
  }
  function r5(x) { return Math.floor(x / 5.0 + 0.5) * 5; }
  function drive(a, b) { return r5(roadKm(a, b) / KMH * 60.0 + PARK); }
  function miles(k) { return Math.max(1, Math.floor(k / 1.609344 + .5)); }

  function plan(start, len, kinds, free, outside, exclude, first, pins, fill) {
    var L = D.L[len], budget = L[2], most = L[3], radius = L[4];
    var ks = {}; (kinds && kinds.length ? kinds : [0, 1, 2, 3, 4, 5]).forEach(function (k) { ks[k] = 1; });
    var ex = {}; (exclude || []).forEach(function (x) { ex[x] = 1; });
    var pos = S.map(function (s) { return [s.lat, s.lon]; });
    var route = first != null ? [first] : [];
    (pins || []).forEach(function (j) { if (route.indexOf(j) < 0 && !ex[S[j].id]) route.push(j); });
    var cand = [];
    S.forEach(function (s, i) {
      if (route.indexOf(i) >= 0 || ex[s.id] || !ks[s.k]) return;
      if (s.e === "outside" && !outside) return;
      if (free && s.e === "ticket") return;
      if (km(start, pos[i]) > radius) return;
      cand.push(i);
    });
    function P(j) { return j < 0 ? start : pos[j]; }
    var lo = first != null ? 1 : 0;
    function total(rt) {
      var t = 0, prev = -1;
      rt.forEach(function (j) { t += drive(P(prev), P(j)) + S[j].m; prev = j; });
      return t + drive(P(prev), start);
    }
    function tidy(rt) {
      var better = true;
      while (better) {
        better = false;
        for (var i = lo; i < rt.length - 1; i++) {
          for (var j = i + 1; j < rt.length; j++) {
            var r2 = rt.slice(0, i).concat(rt.slice(i, j + 1).reverse(), rt.slice(j + 1));
            if (total(r2) < total(rt)) { rt = r2; better = true; }
          }
        }
      }
      return rt;
    }
    route = tidy(route);
    var cur = total(route);
    while (fill && route.length < most) {
      var best = null, bs = -1.0;
      for (var ci = 0; ci < cand.length; ci++) {
        var c = cand[ci];
        if (route.indexOf(c) >= 0) continue;
        for (var k = lo; k <= route.length; k++) {
          var a = k > 0 ? P(route[k - 1]) : start, b = k < route.length ? P(route[k]) : start;
          var dd = drive(a, P(c)) + drive(P(c), b) - drive(a, b);
          var add = dd + S[c].m;
          if (cur + add > budget) continue;
          var w = S[c].w, sc = w * Math.sqrt(w) / (S[c].m + 3.0 * dd + 20.0);
          if (sc > bs + 1e-9) { best = [c, k, add]; bs = sc; }
        }
      }
      if (!best) break;
      route.splice(best[1], 0, best[0]);
      cur += best[2];
    }
    return tidy(route);
  }
  window.VP_PLAN = function (start, len, kinds, free, outside, exclude, first, pins, fill) {   // for tools/visit_check.js
    return plan(start, len, kinds, free, outside, exclude, first, pins, fill).map(function (j) { return S[j].id; });
  };

  if (!form || !outEl) return;

  /* ---------- the day, laid out (day_html() in src/visitplan.py) ---------- */
  function hm(t) { var h = Math.floor(t / 60), m = t % 60; return (h < 10 ? "0" : "") + h + ":" + (m < 10 ? "0" : "") + m; }
  function dur(m) {
    var h = Math.floor(m / 60), mm = m % 60;
    if (CY) return (h ? h + " awr" : "") + (h && mm ? " " : "") + (mm || !h ? mm + " munud" : "");
    return (h ? h + " h" : "") + (h && mm ? " " : "") + (mm || !h ? mm + " min" : "");
  }
  function cap(s) { return s ? s.charAt(0).toUpperCase() + s.slice(1) : s; }
  function directions(s) { return "https://www.google.com/maps/dir/?api=1&destination=" + s.lat + "," + s.lon; }
  function gmaps(start, route) {
    var o = start[0].toFixed(5) + "," + start[1].toFixed(5);
    var w = route.slice(0, 9).map(function (j) { return S[j].lat.toFixed(5) + "," + S[j].lon.toFixed(5); }).join("%7C");
    return "https://www.google.com/maps/dir/?api=1&origin=" + o + "&destination=" + o + "&travelmode=driving" + (w ? "&waypoints=" + w : "");
  }

  function mapSvg(route, start, startName) {
    var G = D.G, minx = G[0], maxy = G[1], kk = G[2], sc = G[3], W = G[4], H = G[5];
    function X(lon) { return (lon - minx) * kk * sc; }
    function Y(lat) { return (maxy - lat) * sc; }
    var pts = [[X(start[1]), Y(start[0])]].concat(route.map(function (j) { return [X(S[j].lon), Y(S[j].lat)]; }));
    var xs = pts.map(function (p) { return p[0]; }), ys = pts.map(function (p) { return p[1]; });
    var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs), y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys);
    var w = Math.max(x1 - x0, 30) * 1.3 + 10, h = Math.max(y1 - y0, 22) * 1.3 + 10;
    if (w / h < 4 / 3) w = h * 4 / 3; else h = w * 3 / 4;
    var vx = (x0 + x1) / 2 - w / 2, vy = (y0 + y1) / 2 - h / 2, u = w / 100, f = function (n) { return n.toFixed(1); }, f2 = function (n) { return n.toFixed(2); };
    var o = ['<svg class="vp-svg" viewBox="' + f(vx) + " " + f(vy) + " " + f(w) + " " + f(h) + '" role="img" aria-label="' + T("Map of the day", "Map o’r diwrnod") + '" preserveAspectRatio="xMidYMid slice">',
      '<rect x="' + f(vx - w) + '" y="' + f(vy - h) + '" width="' + f(w * 3) + '" height="' + f(h * 3) + '" fill="#121a2a"/>',
      '<image href="relief-3600.webp" x="0" y="0" width="' + W + '" height="' + H + '" preserveAspectRatio="none"/>'];
    var labels = [];
    D.t.forEach(function (t) {
      var tx = X(t[3]), ty = Y(t[2]);
      if (tx > vx + 4 * u && tx < vx + w - 4 * u && ty > vy + 3 * u && ty < vy + h - 2 * u && t[0] !== startName[0] &&
          pts.every(function (p) { return Math.pow(tx - p[0], 2) + Math.pow(ty - p[1], 2) > Math.pow(6 * u, 2); }) &&
          labels.every(function (l) { return Math.abs(tx - l[0]) > 16 * u || Math.abs(ty - l[1]) > 3.4 * u; })) {
        labels.push([tx, ty]);
        o.push('<g class="vp-town"><circle cx="' + f(tx) + '" cy="' + f(ty) + '" r="' + f2(.5 * u) + '"/><text x="' + f(tx + u) + '" y="' + f(ty + .9 * u) + '" font-size="' + f2(2.4 * u) + '">' + esc(T(t[0], t[1])) + "</text></g>");
      }
    });
    o.push('<path class="vp-line" d="M' + pts.concat([pts[0]]).map(function (p) { return f(p[0]) + " " + f(p[1]); }).join(" L") + '" stroke-width="' + f2(.55 * u) + '" stroke-dasharray="' + f2(1.6 * u) + " " + f2(1.1 * u) + '"/>');
    var sx = pts[0][0], sy = pts[0][1];
    o.push('<g class="vp-home"><rect x="' + f(sx - 2.1 * u) + '" y="' + f(sy - 2.1 * u) + '" width="' + f(4.2 * u) + '" height="' + f(4.2 * u) + '" rx="' + f(.8 * u) + '" stroke-width="' + f2(.4 * u) + '"/>' +
      '<path d="M' + f(sx - 1.2 * u) + " " + f(sy + .1 * u) + " L" + f(sx) + " " + f(sy - 1.1 * u) + " L" + f(sx + 1.2 * u) + " " + f(sy + .1 * u) + " M" + f(sx - .8 * u) + " " + f(sy - .2 * u) + " V" + f(sy + 1.2 * u) + " H" + f(sx + .8 * u) + " V" + f(sy - .2 * u) + '" stroke-width="' + f2(.35 * u) + '"/></g>');
    var placed = [pts[0]];
    pts.slice(1).forEach(function (p0, n) {
      var p = p0, angs = [0, -45, 45, -135, 135, -90, 90, 180];   // a pin on top of another moves aside, with a short line back
      for (var i = 0; i < angs.length; i++) {
        var a = angs[i] * RAD;
        p = a ? [p0[0] + 4.8 * u * Math.sin(a), p0[1] - 4.8 * u * Math.cos(a)] : p0;
        if (placed.every(function (q) { return Math.pow(p[0] - q[0], 2) + Math.pow(p[1] - q[1], 2) >= Math.pow(4.4 * u, 2); })) break;
      }
      placed.push(p);
      if (p !== p0) o.push('<path class="vp-lead" d="M' + f(p0[0]) + " " + f(p0[1]) + " L" + f(p[0]) + " " + f(p[1]) + '" stroke-width="' + f2(.3 * u) + '"/><circle class="vp-dot" cx="' + f(p0[0]) + '" cy="' + f(p0[1]) + '" r="' + f2(.7 * u) + '"/>');
      o.push('<g class="vp-pin"><circle cx="' + f(p[0]) + '" cy="' + f(p[1]) + '" r="' + f2(2.3 * u) + '" stroke-width="' + f2(.4 * u) + '"/><text x="' + f(p[0]) + '" y="' + f(p[1] + .95 * u) + '" font-size="' + f2(2.7 * u) + '">' + (n + 1) + "</text></g>");
    });
    o.push("</svg>");
    return o.join("");
  }

  function stopLi(s, n, ta, tl) {
    var ent = D.E[s.e];
    var meta = esc(cap(T(s.who[0], s.who[1])) + " · " + T(ent[0], ent[1])) + (s.pc ? " · <b>" + esc(s.pc) + "</b>" : "");
    var links = (s.url ? '<a href="' + esc(s.url) + '" target="_blank" rel="noopener">' + T("Opening times and prices", "Amseroedd agor a phrisiau") + " ↗</a>" : "") +
      '<a href="' + directions(s) + '" target="_blank" rel="noopener">' + T("Directions", "Cyfarwyddiadau") + " ↗</a>" +
      '<button type="button" data-swap="' + esc(s.id) + '">' + T("Show me another", "Dangos un arall") + "</button>" +
      '<button type="button" data-drop="' + esc(s.id) + '">' + T("Remove", "Tynnu") + "</button>";
    var name = esc(T(s.en, s.cy));
    var wl = s.href ? '<a class="wl" href="' + s.href + '">' + name + "</a>" : s.url ? '<a class="wl" href="' + esc(s.url) + '" target="_blank" rel="noopener">' + name + "</a>" : "";
    var pic = s.pic ? '<span class="vp-pic" aria-hidden="true"><img src="' + esc(s.pic) + '" alt="" width="96" height="96" loading="lazy" decoding="async"></span>'
      : '<span class="vp-pic ic" aria-hidden="true"><svg><use href="' + (D.sp || "sprite.svg") + '#i-' + s.ill + '"/></svg></span>';
    return '<li class="vp-stop' + (wl ? " wl-card" : "") + '" data-k="' + s.k + '"><span class="vp-n">' + n + '</span><div class="vp-b">' +
      '<p class="vp-time"><time>' + hm(ta) + "</time> – <time>" + hm(tl) + "</time> · " + T("about " + dur(s.m) + " here", "tua " + dur(s.m) + " yma") + "</p>" +
      "<h3>" + name + '</h3><p class="vp-d">' + esc(T(s.dEn, s.dCy)) + '</p><p class="vp-meta">' + meta + "</p>" +
      (s.note ? '<p class="vp-note">' + esc(T(s.note[0], s.note[1])) + "</p>" : "") + '<p class="vp-links">' + links + "</p></div>" + pic + wl + "</li>";
  }

  function render(route, start, startName, t0, len) {
    var t = t0, prev = start, road = 0, mi = 0, lunch = D.L[len][5], lis = [];
    lis.push('<li class="vp-mark"><time>' + hm(t0) + "</time><span>" + esc(T("Leave " + startName[0], "Gadael " + startName[1])) + "</span></li>");
    route.forEach(function (j, n) {
      var s = S[j], p = [s.lat, s.lon], d = drive(prev, p), m = miles(roadKm(prev, p));
      t += d; road += d; mi += m;
      lis.push('<li class="vp-drive">' + T(d + " min drive, about " + m + (m > 1 ? " miles" : " mile"), d + " munud yn y car, tua " + m + " milltir") + "</li>");
      lis.push(stopLi(s, n + 1, t, t + s.m));
      t += s.m;
      if (lunch && t >= 735) {
        lis.push('<li class="vp-mark vp-lunch"><time>' + hm(t) + "</time><span>" + T("Lunch break, " + LUNCH + " min", "Egwyl ginio, " + LUNCH + " munud") + "</span></li>");
        t += LUNCH; lunch = false;
      }
      prev = p;
    });
    var d = drive(prev, start), m = miles(roadKm(prev, start));
    t += d; road += d; mi += m;
    lis.push('<li class="vp-drive">' + T(d + " min drive, about " + m + (m > 1 ? " miles" : " mile"), d + " munud yn y car, tua " + m + " milltir") + "</li>");
    lis.push('<li class="vp-mark"><time>' + hm(t) + "</time><span>" + esc(T("Back at " + startName[0], "Yn ôl i’r man cychwyn, " + startName[1])) + "</span></li>");
    var n = route.length;
    var sum = '<p class="vp-sum"><b>' + T(n + " stops", n + " arhosfan") + "</b><span>" + T(dur(road) + " on the road, about " + mi + " miles", dur(road) + " ar y ffordd, tua " + mi + " milltir") +
      "</span><span>" + T("Leave at " + hm(t0) + ", back by about " + hm(t), "Gadael am " + hm(t0) + ", yn ôl erbyn tua " + hm(t)) + "</span></p>";
    var addOpts = S.map(function (s, i) { return route.indexOf(i) < 0 ? '<option value="' + esc(T(s.en, s.cy)) + '">' : ""; }).join("");
    return '<h2 class="sub-h" tabindex="-1" id="vp-h">' + esc(T("Your day from " + startName[0], "Eich diwrnod: " + startName[1])) + "</h2>" +
      '<div class="vp-day">' + sum + '<div class="vp-cols"><figure class="vp-map">' + mapSvg(route, start, startName) +
      "<figcaption>" + T("The lines show the order of the day, not the roads.", "Mae’r llinellau’n dangos trefn y diwrnod, nid y ffyrdd.") + "</figcaption></figure>" +
      '<div><ul class="vp-plan">' + lis.join("") + "</ul>" +
      '<form class="vp-add" id="vp-add"><label class="sr-only" for="vp-addq">' + T("Add a place", "Ychwanegu lle") + '</label><input id="vp-addq" list="vp-addl" placeholder="' +
      T("Add a place to the day…", "Ychwanegu lle at y diwrnod…") + '"><datalist id="vp-addl">' + addOpts + '</datalist><button class="btn" type="submit">' + T("Add", "Ychwanegu") + "</button></form>" +
      "</div></div></div>" +
      '<p class="vp-acts"><a class="btn solid" href="' + esc(gmaps(start, route)) + '" target="_blank" rel="noopener">' + T("Open the route in Google Maps", "Agor y daith yn Google Maps") + ' ↗</a>' +
      '<button type="button" class="btn" id="vp-print">' + T("Print this day", "Argraffu’r diwrnod") + "</button>" +
      '<button type="button" class="btn" id="vp-copy">' + T("Copy the link to this day", "Copïo’r ddolen i’r diwrnod") + "</button></p>";
  }

  /* ---------- the form, the address and the buttons ---------- */
  var st = { from: "", len: "day", k: [0, 1, 2, 3, 4, 5], f: 0, o: 0, t: 600, p: null, x: [], nf: 0 };

  function findStart(q) {
    q = String(q || "").trim();
    var m = /^@(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)$/.exec(q);
    if (m) return { ll: [+m[1], +m[2]], name: ["your start", "eich man cychwyn"], first: null };
    if (/^s:/.test(q) && IX[q.slice(2)] != null) { var s0 = S[IX[q.slice(2)]]; return { ll: [s0.lat, s0.lon], name: [s0.en, s0.cy], first: IX[q.slice(2)] }; }
    var fq = fold(q);
    if (!fq) return null;
    var hit = null;
    D.t.forEach(function (t) { if (!hit && (fold(t[0]) === fq || fold(t[1]) === fq)) hit = { ll: [t[2], t[3]], name: [t[0], t[1]], first: null }; });
    if (hit) return hit;
    S.forEach(function (s, i) { if (!hit && (fold(s.en) === fq || fold(s.cy) === fq)) hit = { ll: [s.lat, s.lon], name: [s.en, s.cy], first: i }; });
    if (hit) return hit;
    D.t.forEach(function (t) { if (!hit && (fold(t[0]).indexOf(fq) === 0 || fold(t[1]).indexOf(fq) === 0)) hit = { ll: [t[2], t[3]], name: [t[0], t[1]], first: null }; });
    return hit;
  }

  function fromForm() {
    var fd = new FormData(form);
    st.from = String(fd.get("from") || "").trim();
    st.len = fd.get("len") || "day";
    st.k = fd.getAll("k").map(Number);
    st.f = fd.get("free") ? 1 : 0;
    st.o = fd.get("out") ? 1 : 0;
    st.t = +fd.get("t") || 600;
  }
  function toForm() {
    var q = document.getElementById("vp-q");
    var s = findStart(st.from);
    q.value = /^(@|s:)/.test(st.from) && s ? (/^@/.test(st.from) ? T("My location", "Fy lleoliad") : T(s.name[0], s.name[1])) : st.from;
    if (/^@/.test(st.from)) q.dataset.at = st.from; else delete q.dataset.at;
    form.querySelectorAll("input[name=len]").forEach(function (r) { r.checked = r.value === st.len; });
    form.querySelectorAll("input[name=k]").forEach(function (c) { c.checked = st.k.indexOf(+c.value) >= 0; });
    form.querySelector("input[name=free]").checked = !!st.f;
    form.querySelector("input[name=out]").checked = !!st.o;
    form.querySelector("select[name=t]").value = String(st.t);
  }
  function toQuery() {
    var a = ["from=" + encodeURIComponent(st.from)];
    if (st.len !== "day") a.push("len=" + st.len);
    if (st.k.length && st.k.length < 6) a.push("k=" + st.k.join(","));
    if (st.f) a.push("f=1");
    if (st.o) a.push("o=1");
    if (st.t !== 600) a.push("t=" + st.t);
    if (st.p) a.push("p=" + st.p.join(","));
    if (st.x.length) a.push("x=" + st.x.join(","));
    if (st.nf) a.push("nf=1");
    return a.join("&");
  }
  function fromQuery() {
    var q = new URLSearchParams(location.search);
    if (!q.get("from")) return false;
    st.from = q.get("from");
    st.len = D.L[q.get("len")] ? q.get("len") : "day";
    st.k = q.get("k") ? q.get("k").split(",").map(Number).filter(function (n) { return n >= 0 && n < 6; }) : [0, 1, 2, 3, 4, 5];
    st.f = q.get("f") === "1" ? 1 : 0;
    st.o = q.get("o") === "1" ? 1 : 0;
    st.t = Math.min(900, Math.max(420, +q.get("t") || 600));
    st.p = q.get("p") ? q.get("p").split(",").filter(function (x) { return IX[x] != null; }) : null;
    st.x = q.get("x") ? q.get("x").split(",") : [];
    st.nf = q.get("nf") === "1" ? 1 : 0;
    return true;
  }

  var current = null;
  function go(scroll) {
    var err = document.getElementById("vp-err");
    var s = findStart(st.from);
    if (!s) {
      err.hidden = false;
      err.textContent = T("We could not find “" + st.from + "”. Try a nearby town, or use your location.", "Methwyd dod o hyd i “" + st.from + "”. Rhowch gynnig ar dref gerllaw, neu defnyddiwch eich lleoliad.");
      outEl.innerHTML = "";
      return;
    }
    err.hidden = true;
    var pins = st.p ? st.p.map(function (id) { return IX[id]; }) : [];
    var route = plan(s.ll, st.len, st.k, st.f, st.o, st.x, s.first, pins, !st.nf);
    current = { route: route, start: s };
    try { history.replaceState(null, "", location.pathname + "?" + toQuery()); } catch (e) {}
    if (!route.length) {
      outEl.innerHTML = '<p class="vp-err">' + T("No places to visit match within reach of there. Try more interests, a longer day, or a place nearer the middle of Wales.",
        "Does dim lleoedd i ymweld â nhw sy’n cyfateb o fewn cyrraedd. Rhowch gynnig ar fwy o ddiddordebau, diwrnod hirach, neu le nes at ganol Cymru.") + "</p>";
      return;
    }
    outEl.innerHTML = render(route, s.ll, s.name, st.t, st.len);
    if (scroll) {
      var h = document.getElementById("vp-h");
      h.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" });
      h.focus({ preventScroll: true });
    }
    try { if (window.goatcounter && goatcounter.count) goatcounter.count({ path: "visit-plan", title: "Visit planner", event: true }); } catch (e) {}
  }

  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var q = document.getElementById("vp-q");
    fromForm();
    if (q.dataset.at && (q.value === "My location" || q.value === "Fy lleoliad")) st.from = q.dataset.at;
    st.p = null; st.x = []; st.nf = 0;
    go(true);
  });
  document.getElementById("vp-q").addEventListener("input", function () { delete this.dataset.at; });
  document.getElementById("vp-loc").addEventListener("click", function () {
    var b = this, err = document.getElementById("vp-err");
    if (!navigator.geolocation) return;
    b.disabled = true;
    navigator.geolocation.getCurrentPosition(function (p) {
      b.disabled = false;
      var at = "@" + p.coords.latitude.toFixed(2) + "," + p.coords.longitude.toFixed(2);   // to about a kilometre: enough for a day out, and kept on your device
      var q = document.getElementById("vp-q");
      q.value = T("My location", "Fy lleoliad"); q.dataset.at = at;
      fromForm(); st.from = at; st.p = null; st.x = []; st.nf = 0;
      go(true);
    }, function () {
      b.disabled = false;
      err.hidden = false;
      err.textContent = T("Your location could not be found. Type a town instead.", "Methwyd canfod eich lleoliad. Teipiwch dref yn lle hynny.");
    }, { timeout: 10000, maximumAge: 600000 });
  });
  outEl.addEventListener("click", function (ev) {
    var b = ev.target.closest("button");
    if (!b || !current) return;
    var ids = current.route.map(function (j) { return S[j].id; });
    if (b.dataset.swap || b.dataset.drop) {
      var id = b.dataset.swap || b.dataset.drop;
      st.p = ids.filter(function (x) { return x !== id && (current.start.first == null || x !== S[current.start.first].id); });
      if (st.x.indexOf(id) < 0) st.x.push(id);
      st.nf = b.dataset.drop ? 1 : 0;
      go(false);
      var back = outEl.querySelector(".vp-plan");
      if (back) back.scrollIntoView({ block: "nearest" });
    } else if (b.id === "vp-print") {
      window.print();
    } else if (b.id === "vp-copy") {
      var done = function () { b.textContent = T("Link copied", "Dolen wedi’i chopïo"); };
      if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(done, function () {}); else done();
    }
  });
  outEl.addEventListener("submit", function (ev) {
    if (ev.target.id !== "vp-add") return;
    ev.preventDefault();
    var fq = fold(document.getElementById("vp-addq").value), hit = null;
    S.forEach(function (s, i) { if (hit == null && (fold(s.en) === fq || fold(s.cy) === fq)) hit = i; });
    if (hit == null) S.forEach(function (s, i) { if (hit == null && fq && (fold(s.en).indexOf(fq) >= 0 || fold(s.cy).indexOf(fq) >= 0)) hit = i; });
    if (hit == null || !current) return;
    st.p = current.route.map(function (j) { return S[j].id; }).concat([S[hit].id]);
    st.x = st.x.filter(function (x) { return x !== S[hit].id; });
    st.nf = 1;
    go(false);
  });

  if (fromQuery()) { toForm(); go(false); }
})();
