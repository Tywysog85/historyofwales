/* The place-name decoder, shared by the home page and towns.html.
   build.py writes the words from src/placenames.py in front of this file as PND, and saves both as _site/placenames.js.
   How it works: the name is split into words at spaces and hyphens. A word that is a known English word (Wells, Bay,
   Junction) or an English name (Builth, Swansea) is shown as that. Any other word is cut into the known Welsh parts that
   cover it best (fewest unknown letters, then fewest parts), where a part may be mutated: Cammarch -> gammarch after llan,
   pont -> bont, Buallt -> Muallt. Letters no part explains are shown as one unknown piece, per word. */
(function () {
  var D = window.PND;
  if (!D) return;
  var DIG = { ch: 1, dd: 1, ff: 1, ll: 1, ng: 1, ph: 1, rh: 1, th: 1 };
  var RULES = [
    ["s", [["p", "b"], ["t", "d"], ["c", "g"], ["b", "f"], ["d", "dd"], ["g", ""], ["m", "f"], ["ll", "l"], ["rh", "r"]]],
    ["n", [["p", "mh"], ["t", "nh"], ["c", "ngh"], ["b", "m"], ["d", "n"], ["g", "ng"]]],
    ["a", [["p", "ph"], ["t", "th"], ["c", "ch"]]]
  ];
  var COST = { s: 3, n: 5, a: 5 };
  function low(s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function norm(s) { return low(s).replace(/[^a-z]/g, ""); }
  function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }

  var BASE = {}, MUT = {}, ENG = {}, WHOLE = {}, TOWN = {}, MAXL = 0;
  D.W.forEach(function (r) {
    var sp = r[0].split("|"), e = { w: sp[0], en: r[1], cy: r[2], k: r[3] };
    sp.forEach(function (x) {
      x = norm(x);
      var into = e.k === "e" ? ENG : e.k === "n" ? WHOLE : BASE;
      if (!into[x]) into[x] = e;
    });
  });
  Object.keys(BASE).forEach(function (k) {
    var e = BASE[k];
    RULES.forEach(function (R) {
      R[1].forEach(function (ab) {
        var a = ab[0], b = ab[1];
        if (k.slice(0, a.length) !== a || (a.length === 1 && DIG[k.slice(0, 2)])) return;
        var f = b + k.slice(a.length);
        if (f.length < 3 || BASE[f] || (MUT[f] && COST[MUT[f].type] <= COST[R[0]])) return;
        MUT[f] = { e: e, type: R[0], a: a, b: b };
      });
    });
  });
  Object.keys(BASE).concat(Object.keys(MUT)).forEach(function (k) { if (k.length > MAXL) MAXL = k.length; });
  (D.T || []).forEach(function (t) { TOWN[norm(t[0])] = TOWN[norm(t[1])] = t; });

  /* cut one word (already normalised) into parts */
  function cut(s) {
    var n = s.length, best = [0], back = [], i, j;
    for (i = 1; i <= n; i++) best[i] = Infinity;
    for (i = 0; i < n; i++) {
      if (best[i] === Infinity) continue;
      for (j = i + 1; j <= Math.min(n, i + MAXL); j++) {
        var sub = s.slice(i, j), hit = BASE[sub] ? { e: BASE[sub] } : MUT[sub] || (j === n && sub.length > 3 && ENG[sub] ? { e: ENG[sub], eng: 1 } : null);
        if (!hit) continue;
        var c = best[i] + 10 + (hit.type ? COST[hit.type] : 0) + (sub.length <= 2 ? (sub.length === 1 ? 8 : 4) : 0) + (hit.eng ? 6 : 0);
        if (c < best[j]) { best[j] = c; back[j] = [i, hit]; }
      }
      for (j = i + 1; j <= n; j++) {
        var u = best[i] + 25 + 6 * (j - i);
        if (u < best[j]) { best[j] = u; back[j] = [i, null]; }
      }
    }
    var out = [];
    for (j = n; j > 0; j = back[j][0]) out.unshift([back[j][0], j, back[j][1]]);
    return out;
  }

  /* the name -> { hit: a town in the list or null, words: [[part, ...], ...] } where part = { t, e, type, a, b } */
  function decode(raw) {
    var whole = norm(raw || ""), words = [];
    (raw || "").split(/[\s\-‐-―\/,.;:]+/).forEach(function (w) {
      var map = [], s = "", ch, k;
      for (k = 0; k < w.length; k++) { ch = norm(w[k]); if (ch) { s += ch; map.push(k); } }
      if (!s) return;
      var piece = function (a, b) { return w.slice(map[a], map[b - 1] + 1); };
      if (BASE[s]) { words.push([{ t: w, e: BASE[s] }]); return; }
      if (WHOLE[s]) { words.push([{ t: w, e: WHOLE[s] }]); return; }
      if (ENG[s]) { words.push([{ t: w, e: ENG[s] }]); return; }
      words.push(cut(s).map(function (c) {
        var h = c[2] || {};
        return { t: piece(c[0], c[1]), e: h.e || null, type: h.type, a: h.a, b: h.b };
      }));
    });
    return { hit: TOWN[whole] || null, words: words };
  }

  function show(e) { return e.k === "r" || e.k === "s" ? cap(e.w) : e.w; }
  /* one part, in words: { t, mean, note, kind } where kind is w (Welsh), e (English) or u (unknown) */
  function label(p, cy) {
    var e = p.e;
    if (!e) return { t: p.t, kind: "u", mean: cy ? "dim yn y rhestr eto: enw person, sant neu nant efallai" : "not in the glossary yet: perhaps a person, saint or stream" };
    var mean = e.k === "r" ? (cy ? "afon " : "the river ") + cap(e.w) + ((cy ? e.cy : e.en) ? ", " + (cy ? e.cy : e.en) : "") : (cy ? e.cy : e.en), note = "";
    if (p.type) {
      var kind = { s: ["soft mutation", "treiglad meddal"], n: ["nasal mutation", "treiglad trwynol"], a: ["aspirate mutation", "treiglad llaes"] }[p.type];
      note = (cy ? "o " : "from ") + show(e) + " (" + (cy ? kind[1] : kind[0]) + ": " + p.a + " → " + (p.b || "–") + ")";
    } else if (e.k !== "e" && e.k !== "n" && low(p.t).replace(/[^a-z]/g, "") !== low(e.w).replace(/[^a-z]/g, "")) {
      note = (cy ? "ffurf ar " : "a spelling of ") + show(e);
    } else if (e.k !== "e" && e.k !== "n" && p.t.toLowerCase() !== e.w && p.t.toLowerCase() !== show(e).toLowerCase()) {
      note = show(e);
    }
    return { t: p.t, kind: e.k === "e" ? "e" : e.k === "n" ? "n" : "w", mean: mean, note: note };
  }
  function townLink(t) {
    var id = t[4], pre = document.documentElement.classList.contains("cy") ? "cy/" : "";
    if (t[5]) return pre + id + ".html";  /* the town's own page (src/townpages.py) */
    return document.getElementById(id) ? "#" + id : (document.documentElement.classList.contains("cy") ? "cy/" : "") + "towns.html#" + id;
  }

  /* today's name for the home page box: by the visitor's own date, so everyone sees the same name that day */
  function today() {
    var list = D.D || [], d = new Date();
    if (!list.length) return "";
    var n = Math.floor(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 864e5);
    return list[n % list.length];
  }

  window.PN = { decode: decode, label: label, townLink: townLink, today: today, samples: D.S || [] };
  try { document.dispatchEvent(new Event("pn:ready")); } catch (err) { /* very old browsers: the decoder just waits for a keypress */ }
})();
