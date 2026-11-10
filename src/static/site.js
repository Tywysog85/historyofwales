/* Shared by every page: menu, scroll progress, reveal-on-scroll, back to top,
   and "Your journey" (what you have read and the badges you have earned, kept on this device only). */
(function () {
  window.__site = 1;
  var d = document, root = d.documentElement;
  var $ = function (s, r) { return (r || d).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || d).querySelectorAll(s)); };
  var cy = function () { return root.classList.contains("cy"); };
  var T = function (en, c) { return cy() ? c : en; };
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- journey store ---------- */
  var KEY = "hc-journey";
  function load() { try { var j = JSON.parse(localStorage.getItem(KEY) || "{}"); j.v = j.v || {}; j.b = j.b || {}; j.f = j.f || {}; j.d = j.d || { streak: 0, best: 0, played: 0, wins: 0, last: "" }; return j; } catch (e) { return { v: {}, b: {}, f: {}, d: { streak: 0, best: 0, played: 0, wins: 0, last: "" } }; } }
  function save(j) { try { localStorage.setItem(KEY, JSON.stringify(j)); } catch (e) {} }
  function count(j, kind) { var n = 0; for (var k in j.v) if (!kind || k.indexOf(kind + ":") === 0) n++; return n; }
  var BADGES = [
    ["first", "1", "First steps", "Camau cyntaf", "Read your first page", "Darllen eich tudalen gyntaf", function (j) { return count(j) >= 1; }],
    ["ages", "IX", "Time traveller", "Teithiwr amser", "Read all nine ages", "Darllen pob un o’r naw oes", function (j) { return count(j, "era") >= 9; }],
    ["people10", "10", "Good company", "Cwmni da", "Meet 10 people", "Cwrdd â 10 o bobl", function (j) { return count(j, "person") >= 10; }],
    ["people30", "30", "Who’s who", "Pwy yw pwy", "Meet 30 people", "Cwrdd â 30 o bobl", function (j) { return count(j, "person") >= 30; }],
    ["places10", "⌖", "Pilgrim", "Pererin", "Visit 10 places", "Ymweld â 10 lle", function (j) { return count(j, "place") >= 10; }],
    ["legends", "☾", "Storyteller", "Cyfarwydd", "Read all seven legends", "Darllen pob un o’r saith chwedl", function (j) { return count(j, "legend") >= 7; }],
    ["stories", "¶", "Scholar", "Ysgolhaig", "Read twelve long reads", "Darllen deuddeg erthygl", function (j) { return count(j, "story") >= 12; }],
    ["daily1", "?", "Day one", "Diwrnod un", "Solve a daily challenge", "Datrys her y dydd", function (j) { return j.d.wins >= 1; }],
    ["streak3", "3", "On a roll", "Ar rediad", "Play the daily challenge 3 days running", "Chwarae her y dydd 3 diwrnod yn olynol", function (j) { return j.d.best >= 3; }],
    ["streak7", "7", "A week of dates", "Wythnos o ddyddiadau", "Play the daily challenge 7 days running", "Chwarae her y dydd 7 diwrnod yn olynol", function (j) { return j.d.best >= 7; }],
    ["quiz8", "8", "Sharp", "Craff", "Score 8 or more in the quiz", "Sgorio 8 neu fwy yn y cwis", function (j) { return j.f.quiz8; }],
    ["quiz10", "★", "Pencampwr", "Pencampwr", "A perfect 10 in the quiz", "10 perffaith yn y cwis", function (j) { return j.f.quiz10; }],
    ["order15", "↕", "In good order", "Mewn trefn", "A perfect timeline challenge", "Her y llinell amser berffaith", function (j) { return j.f.order15; }],
    ["map300", "◎", "Map reader", "Darllenydd mapiau", "Score 300 or more in Where in Wales?", "Sgorio 300 neu fwy yn Ble yng Nghymru?", function (j) { return j.f.map300; }],
    ["pairs", "Aa", "Good memory", "Cof da", "Finish a game of word pairs", "Gorffen gêm o barau geiriau", function (j) { return j.f.pairs; }]
  ];
  var RANKS = [[0, "Newcomer", "Newydd-ddyfodiad"], [3, "Apprentice", "Prentis"], [12, "Storyteller", "Cyfarwydd"], [30, "Bard", "Bardd"], [60, "Chief bard", "Pencerdd"], [100, "Prince of history", "Tywysog hanes"]];
  function rank(n) { var r = RANKS[0]; RANKS.forEach(function (x) { if (n >= x[0]) r = x; }); return r; }
  function toast(b) {
    var a = d.createElement("a"); a.className = "toast"; a.href = "journey.html"; a.setAttribute("role", "status");
    a.innerHTML = "<i>" + b[1] + "</i><span>" + T("Badge earned: ", "Bathodyn newydd: ") + T(b[2], b[3]) + "</span>";
    d.body.appendChild(a); setTimeout(function () { a.remove(); }, 4300);
  }
  function check(j, quiet) {
    var fresh = [];
    BADGES.forEach(function (b) { if (!j.b[b[0]] && b[6](j)) { j.b[b[0]] = 1; fresh.push(b); } });
    if (fresh.length) { save(j); if (!quiet) toast(fresh[fresh.length - 1]); }
    paintChip(j);
  }
  function paintChip(j) {
    var chip = $("#journey-chip"); if (!chip) return;
    var n = count(j), tot = +chip.dataset.total || 118;
    $("#journey-n").textContent = n;
    $("#journey-ring").setAttribute("stroke-dasharray", Math.min(100, n / tot * 100).toFixed(1) + " 100");
  }
  var J = load();
  var track = d.body.getAttribute("data-track");
  if (track && !J.v[track]) { J.v[track] = 1; save(J); }
  check(J);
  window.HC = {
    T: T, load: load, save: save,
    flag: function (name) { var j = load(); if (!j.f[name]) { j.f[name] = 1; save(j); } check(j); },
    check: function () { check(load()); }
  };

  /* ---------- menu ---------- */
  var mb = $("#menu-btn"), menu = $("#menu");
  function setMenu(open) {
    if (!mb || !menu) return;
    menu.hidden = !open; mb.setAttribute("aria-expanded", open); root.classList.toggle("menu-open", open);
    if (open) menu.scrollTop = 0;
  }
  if (mb) mb.addEventListener("click", function () { setMenu(menu.hidden); });
  if (menu) menu.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
  d.addEventListener("keydown", function (e) { if (e.key === "Escape" && menu && !menu.hidden) { setMenu(false); mb.focus(); } });

  /* ---------- scroll progress + back to top ---------- */
  var bar = $("#progress"), top = $("#to-top"), tick = false;
  function onScroll() {
    if (tick) return; tick = true;
    requestAnimationFrame(function () {
      tick = false;
      var h = d.documentElement.scrollHeight - innerHeight, y = window.scrollY;
      if (bar) bar.style.transform = "scaleX(" + (h > 0 ? Math.min(1, y / h) : 0) + ")";
      if (top) top.hidden = y < innerHeight * 1.2;
    });
  }
  addEventListener("scroll", onScroll, { passive: true }); onScroll();
  if (top) top.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); });

  /* ---------- reveal on scroll ---------- */
  function reveal() {
    var els = $$(".rv:not(.in)");
    if (!("IntersectionObserver" in window) || reduce) { els.forEach(function (el) { el.classList.add("in"); }); return; }
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    els.forEach(function (el, i) { el.style.transitionDelay = (i % 4) * 70 + "ms"; io.observe(el); });
  }
  reveal();

  /* ---------- journey page ---------- */
  var jr = $("#journey-root");
  function renderJourney() {
    if (!jr || !window.JOURNEY) return;
    var j = load(), n = count(j), tot = 0, got = 0;
    window.JOURNEY.forEach(function (g) { tot += g.items.length; });
    BADGES.forEach(function (b) { if (j.b[b[0]]) got++; });
    var r = rank(n), next = RANKS.filter(function (x) { return x[0] > n; })[0];
    var h = '<div class="j-top"><div class="rank"><span>' + T("Your rank", "Eich gradd") + "</span><b>" + T(r[1], r[2]) + "</b><small>" +
      (next ? T((next[0] - n) + " more pages to become ", (next[0] - n) + " tudalen arall i ddod yn ") + "<b style=\"font:inherit;color:var(--ink)\">" + T(next[1], next[2]) + "</b>" : T("The highest rank there is.", "Y radd uchaf sydd.")) + "</small></div>" +
      "<div><span>" + T("Pages read", "Tudalennau a ddarllenwyd") + "</span><b>" + n + "<small> / " + tot + "</small></b></div>" +
      "<div><span>" + T("Badges", "Bathodynnau") + "</span><b>" + got + "<small> / " + BADGES.length + "</small></b></div>" +
      "<div><span>" + T("Daily streak", "Rhediad dyddiol") + "</span><b>" + (j.d.streak || 0) + "</b><small>" + T("Best: ", "Gorau: ") + (j.d.best || 0) + "</small></div></div>";
    h += '<h2 class="j-h">' + T("Badges", "Bathodynnau") + '</h2><div class="badges">' + BADGES.map(function (b) {
      return '<div class="badge' + (j.b[b[0]] ? " got" : "") + '"><i>' + b[1] + "</i><b>" + T(b[2], b[3]) + "</b><span>" + T(b[4], b[5]) + "</span></div>";
    }).join("") + "</div>";
    h += '<h2 class="j-h">' + T("What you have read", "Yr hyn a ddarllenoch") + "</h2>" + window.JOURNEY.map(function (g, gi) {
      var seen = g.items.filter(function (it) { return j.v[g.k + ":" + it[0]]; }).length;
      return '<details class="j-group"' + (gi < 3 ? " open" : "") + "><summary><b>" + T(g.en, g.cy) + "</b><span>" + seen + " / " + g.items.length + '</span><div class="j-bar"><i style="width:' + (seen / g.items.length * 100) + '%"></i></div></summary><ul class="j-list">' +
        g.items.map(function (it) { return '<li><a href="' + it[3] + '"' + (j.v[g.k + ":" + it[0]] ? ' class="seen"' : "") + ">" + T(it[1], it[2]) + "</a></li>"; }).join("") + "</ul></details>";
    }).join("");
    h += '<p class="more-row"><a class="btn solid" href="play.html">' + T("Play a game", "Chwarae gêm") + ' →</a><button type="button" class="btn" id="j-reset">' + T("Start again", "Dechrau eto") + "</button></p>";
    jr.innerHTML = h;
    $("#j-reset").onclick = function () { if (confirm(T("Clear your journey and badges on this device?", "Clirio eich taith a’ch bathodynnau ar y ddyfais hon?"))) { try { localStorage.removeItem(KEY); } catch (e) {} renderJourney(); paintChip(load()); } };
  }
  renderJourney();
  d.addEventListener("click", function (e) { if (e.target.closest(".lang button")) setTimeout(function () { renderJourney(); d.dispatchEvent(new Event("hc-lang")); }, 0); });
})();
