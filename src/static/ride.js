/* Ride with Glyndŵr, 1400: the story engine. The story itself is RIDE, written by src/ride.py.
   Your place is kept on this device (hc-ride), so you can come back to it. Finishing earns a badge. */
(function () {
  var R = window.RIDE; if (!R) return;
  var d = document, KEY = "hc-ride";
  var box = d.getElementById("rd-story"), log = d.getElementById("rd-log"), bar = d.getElementById("rd-bar");
  var path = d.getElementById("rd-path"), here = d.getElementById("rd-here");
  var cy = function () { return d.documentElement.lang === "cy" || d.documentElement.classList.contains("cy"); };
  var T = function (p) { return p ? p[cy() ? 1 : 0] : ""; };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  function fresh() { return { role: "", at: R.start, renown: 0, path: [R.start], say: null }; }
  function load() { try { var s = JSON.parse(localStorage.getItem(KEY) || "null"); if (s && R.nodes[s.at]) return s; } catch (e) {} return null; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }
  function done() { try { return JSON.parse(localStorage.getItem(KEY + "-done") || "{}"); } catch (e) { return {}; } }
  function markDone() { var x = done(); x[S.role] = Math.max(x[S.role] || 0, S.renown); try { localStorage.setItem(KEY + "-done", JSON.stringify(x)); } catch (e) {} }

  var S = load() || fresh();

  function paintSide() {
    var pts = [], items = "";
    S.path.forEach(function (id) {
      var n = R.nodes[id]; if (n.xy) pts.push(n.xy[0] + "," + n.xy[1]);
      if (id !== "start" && id !== "why") items += "<li><span><b>" + esc(T(n.d)) + "</b> · " + esc(T(n.p)) + "</span></li>";
    });
    var uniq = pts.filter(function (p, i) { return i === 0 || p !== pts[i - 1]; });
    if (path) path.setAttribute("points", uniq.join(" "));
    var last = uniq[uniq.length - 1];
    if (here && last) here.setAttribute("transform", "translate(" + last + ")");
    if (log) log.innerHTML = items;
    var n = R.nodes[S.at];
    if (bar) bar.style.width = Math.max(0, Math.min(100, (n.y - 1400) / 15 * 100)) + "%";
  }

  function factBox(f) {
    if (!f) return "";
    var links = f[2].map(function (x) { return '<a href="event-' + x[0] + '.html">' + esc(cy() ? x[2] : x[1]) + " →</a>"; }).join("");
    return '<details class="rd-fact"><summary>' + (cy() ? "Beth ddigwyddodd go iawn" : "What really happened") + "</summary><p>" + esc(T(f)) + "</p>" + (links ? "<p>" + links + "</p>" : "") + "</details>";
  }

  function rankOf() {
    var max = R.max[S.role] || 1, frac = S.renown / max, r = R.ranks[0];
    R.ranks.forEach(function (x) { if (frac >= x[0]) r = x; });
    return [r[1], r[2]];
  }

  function show(focus) {
    var n = R.nodes[S.at], role = R.roles[S.role], h = "";
    h += '<p class="rd-when">' + esc(T(n.d)) + "</p>";
    h += '<h2 tabindex="-1" id="rd-h">' + esc(T(n.p)) + "</h2>";
    if (S.say) h += '<p class="rd-say">' + esc(T(S.say)) + "</p>";
    T(n.t).forEach(function (p) { h += "<p>" + esc(p) + "</p>"; });
    if (role && n.r && n.r[S.role]) h += '<p class="rd-role"><i aria-hidden="true">' + role[2] + "</i><span>" + esc(T(n.r[S.role])) + "</span></p>";
    h += factBox(n.f);
    if (n.c.length) {
      h += '<ul class="rd-choices">' + n.c.map(function (c, i) {
        var icon = c.set ? R.roles[c.set][2] : "→";
        return '<li><button type="button" data-i="' + i + '"><i aria-hidden="true">' + icon + "</i><span>" + esc(T(c.t)) + "</span></button></li>";
      }).join("") + "</ul>";
    } else {
      h += ending();
    }
    box.innerHTML = '<article class="rd-card in">' + h + "</article>";
    paintSide();
    if (focus) {
      var hd = d.getElementById("rd-h");
      if (hd) { hd.focus({ preventScroll: true }); }
      var top = box.getBoundingClientRect().top + window.pageYOffset - 90;
      if (box.getBoundingClientRect().top < 60 || box.getBoundingClientRect().top > window.innerHeight * .6) window.scrollTo({ top: top, behavior: reduce ? "auto" : "smooth" });
    }
  }

  function ending() {
    var r = rankOf(), roleName = R.roles[S.role], others = Object.keys(R.roles).filter(function (k) { return k !== S.role; });
    var past = done(), rode = Object.keys(past).map(function (k) { return T([R.roles[k][0].toLowerCase(), R.roles[k][1].toLowerCase()]); });
    var h = '<div class="rd-end"><hr><p class="rd-when">' + (cy() ? "Sut y’ch cofir" : "How you are remembered") + "</p>";
    h += '<p class="rd-rank">' + esc(T(r)) + "</p>";
    h += "<p>" + esc(T(R.ends[S.role])) + "</p>";
    h += '<p class="rd-score">' + esc(T(roleName)) + " · " + (cy() ? "Bri: " : "Renown: ") + S.renown + " / " + (R.max[S.role] || 0) + "</p>";
    if (rode.length) h += '<p class="rd-score">' + (cy() ? "Rydych wedi marchogaeth fel: " : "You have ridden as: ") + esc(rode.join(", ")) + "</p>";
    h += '<div class="rd-again">' + others.map(function (k) {
      return '<button type="button" class="btn solid" data-role="' + k + '">' + (cy() ? "Marchogaeth eto fel " : "Ride again as ") + esc(T([R.roles[k][0].toLowerCase(), R.roles[k][1].toLowerCase()])) + "</button>";
    }).join("") + '<a class="btn" href="story-glyndwr.html">' + (cy() ? "Darllen hanes Owain" : "Read Owain’s story") + " →</a></div></div>";
    return h;
  }

  function go(c) {
    if (c.set) S.role = c.set;
    S.renown += (c.add || 0) + ((c.bonus && c.bonus[S.role]) || 0);
    S.at = c.to; S.say = c.say || null; S.path.push(c.to);
    if (!R.nodes[S.at].c.length) { markDone(); if (window.HC) window.HC.flag("ride"); }
    save(); show(true);
  }

  function restart(role) {
    S = fresh();
    if (role) { var c = R.nodes[R.start].c.filter(function (x) { return x.set === role; })[0]; if (c) { go(c); return; } }
    save(); show(true);
  }

  box.addEventListener("click", function (ev) {
    var b = ev.target.closest("button"); if (!b) return;
    if (b.dataset.i != null) go(R.nodes[S.at].c[+b.dataset.i]);
    else if (b.dataset.role) restart(b.dataset.role);
    else if (b.dataset.act === "new") restart();
    else if (b.dataset.act === "go") show(true);
  });

  // a ride already under way: offer to carry on or start again
  if (S.at !== R.start && R.nodes[S.at].c.length) {
    var n = R.nodes[S.at];
    box.innerHTML = '<article class="rd-card in"><p class="rd-when">' + (cy() ? "Croeso’n ôl" : "Welcome back") + '</p><h2 tabindex="-1" id="rd-h">' +
      esc(cy() ? "Mae eich taith ar ei hanner" : "Your ride is under way") + "</h2><p>" +
      esc(cy() ? "Fe adawsoch y stori yn " + T(n.p) + ", " + T(n.d) + "." : "You left the story at " + T(n.p) + ", " + T(n.d) + ".") + '</p><div class="rd-resume">' +
      '<button type="button" class="btn solid" data-act="go">' + (cy() ? "Mynd ymlaen" : "Carry on") + " →</button>" +
      '<button type="button" class="btn" data-act="new">' + (cy() ? "Dechrau eto" : "Start again") + "</button></div></article>";
    paintSide();
  } else {
    if (!R.nodes[S.at].c.length) S = fresh();
    show(false);
  }
})();
