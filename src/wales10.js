/* Wales in 10 minutes: recolour the map as each step of the story scrolls into view. Data in window.W10 (build.py). */
(function () {
  var W = window.W10, svg = document.querySelector(".w10-svg");
  if (!W || !svg) return;
  var las = [].slice.call(svg.querySelectorAll(".la")), labG = document.getElementById("w10-labels"), pinG = document.getElementById("w10-pins");
  var bar = document.getElementById("w10-bar"), cap = document.getElementById("w10-stage"), pinList = document.getElementById("w10-places");
  var steps = [].slice.call(document.querySelectorAll(".w10-step")), last = steps.length - 2, curStage = null, curStep = -1, box = {};
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;"); }
  function both(tag, en, cy, attrs, cls) {
    var c = cls ? cls + " " : "";
    if (!cy || en === cy) return "<" + tag + (cls ? ' class="' + cls + '"' : "") + attrs + ">" + esc(en) + "</" + tag + ">";
    return "<" + tag + ' class="' + c + 'l-en"' + attrs + ">" + esc(en) + "</" + tag + "><" + tag + ' class="' + c + 'l-cy"' + attrs + ">" + esc(cy) + "</" + tag + ">";
  }
  /* the Kingdoms colours of the home page, made deeper and softer for this bigger map */
  var PAL = { "#e2453d": "#c4473d", "#d39a62": "#c48a4f", "#7cc495": "#4f9a6c", "#93a0e0": "#6e7ec4", "#c38fd6": "#9a6cb2",
    "#5b6478": "#4d566a", "#e8c65a": "#cfa944", "#62c6c4": "#3e9f9c", "#e58fb4": "#be6d92" };
  function bx(p) { if (!box[p.dataset.la]) box[p.dataset.la] = p.getBBox(); return box[p.dataset.la]; }
  function paintStage(id) {
    var K = W.stages[id], colour = {};
    K.groups.forEach(function (g) { (g[3] === "*" ? las.map(function (p) { return p.dataset.la; }) : g[3]).forEach(function (n) { colour[n] = g[2]; }); });
    las.forEach(function (p) { var c = PAL[colour[p.dataset.la]] || colour[p.dataset.la] || "#2a3142"; p.style.fill = c; p.style.stroke = c; });
    /* a name for each realm at the middle of its land, nudged apart where two would touch */
    var items = [];
    K.groups.forEach(function (g) {
      var en = g[4] ? g[4][0] : g[0], cy = g[4] ? g[4][1] : g[1]; if (!en) return;
      var sx = 0, sy = 0, sa = 0;
      las.forEach(function (p) { if (g[3] !== "*" && g[3].indexOf(p.dataset.la) < 0) return; var b = bx(p), a = b.width * b.height; sx += (b.x + b.width / 2) * a; sy += (b.y + b.height / 2) * a; sa += a; });
      if (sa) items.push({ en: en, cy: cy || en, x: sx / sa, y: sy / sa });
    });
    var fs = matchMedia("(max-width: 900px)").matches ? 26 : 21;
    function spread(key) {
      var r = items.map(function (o) { return { x: o.x, y: o.y, w: o[key].length * fs * 0.56 + 6, h: fs * 1.15 }; });
      for (var it = 0; it < 30; it++) {
        var moved = false;
        for (var i = 0; i < r.length; i++) for (var j = i + 1; j < r.length; j++) {
          var A = r[i], B = r[j], dx = (A.w + B.w) / 2 - Math.abs(A.x - B.x), dy = (A.h + B.h) / 2 - Math.abs(A.y - B.y);
          if (dx <= 0 || dy <= 0) continue;
          moved = true;
          if (dy < dx) { var s = B.y >= A.y ? 1 : -1; A.y -= s * (dy / 2 + 1); B.y += s * (dy / 2 + 1); }
          else { var t = B.x >= A.x ? 1 : -1; A.x -= t * (dx / 2 + 1); B.x += t * (dx / 2 + 1); }
        }
        if (!moved) break;
      }
      return r;
    }
    var pe = spread("en"), pc = spread("cy");
    labG.innerHTML = items.map(function (o, n) {
      var ae = ' x="' + pe[n].x.toFixed(0) + '" y="' + pe[n].y.toFixed(0) + '"', ac = ' x="' + pc[n].x.toFixed(0) + '" y="' + pc[n].y.toFixed(0) + '"';
      return o.en === o.cy ? '<text class="kg-label"' + ae + ">" + esc(o.en) + "</text>"
        : '<text class="kg-label l-en"' + ae + ">" + esc(o.en) + '</text><text class="kg-label l-cy"' + ac + ">" + esc(o.cy) + "</text>";
    }).join("");
    cap.innerHTML = both("span", K.en, K.cy, "");
  }
  function paintPins(i) {
    var P = W.pins[i] || [];
    pinG.innerHTML = P.map(function (p, n) {
      return '<a class="w10-pin" href="' + p[4] + '" style="animation-delay:' + (n * 0.12) + 's"><circle cx="' + p[0] + '" cy="' + p[1] + '" r="8"/>' + both("title", p[2], p[3], "") + "</a>";
    }).join("");
    pinList.innerHTML = P.length ? P.map(function (p) { return '<a href="' + p[4] + '"><i></i>' + both("span", p[2], p[3], "") + "</a>"; }).join("") : "";
  }
  function show(i) {
    if (i === curStep) return;
    curStep = i;
    var el = steps[i], stage = el.dataset.stage, n = +el.dataset.i;
    steps.forEach(function (s, k) { s.classList.toggle("on", k === i); });
    if (stage !== curStage) { curStage = stage; paintStage(stage); }
    paintPins(n);
    bar.style.width = (100 * Math.min(n, last) / last).toFixed(1) + "%";
  }
  show(0);
  if (!("IntersectionObserver" in window)) { steps.forEach(function (s) { s.classList.add("on"); }); return; }
  var phone = matchMedia("(max-width: 900px)").matches;
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (en) { if (en.isIntersecting) show(steps.indexOf(en.target)); });
  }, { rootMargin: phone ? "-62% 0px -37% 0px" : "-50% 0px -49% 0px" });
  steps.forEach(function (s) { io.observe(s); });
})();
