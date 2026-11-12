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
  function load() { try { var j = JSON.parse(localStorage.getItem(KEY) || "{}"); j.v = j.v || {}; j.b = j.b || {}; j.f = j.f || {}; j.s = j.s || {}; j.d = j.d || { streak: 0, best: 0, played: 0, wins: 0, last: "" }; return j; } catch (e) { return { v: {}, b: {}, f: {}, s: {}, d: { streak: 0, best: 0, played: 0, wins: 0, last: "" } }; } }
  function save(j) { try { localStorage.setItem(KEY, JSON.stringify(j)); } catch (e) {} }
  function count(j, kind) { var n = 0; for (var k in j.v) if (!kind || k.indexOf(kind + ":") === 0) n++; return n; }
  var BADGES = [
    ["first", "1", "First steps", "Camau cyntaf", "Read your first page", "Darllen eich tudalen gyntaf", function (j) { return count(j) >= 1; }],
    ["ages", "IX", "Time traveller", "Teithiwr amser", "Read all nine ages", "Darllen pob un o’r naw oes", function (j) { return count(j, "era") >= 9; }],
    ["people10", "10", "Good company", "Cwmni da", "Meet 10 people", "Cwrdd â 10 o bobl", function (j) { return count(j, "person") >= 10; }],
    ["people30", "30", "Who’s who", "Pwy yw pwy", "Meet 30 people", "Cwrdd â 30 o bobl", function (j) { return count(j, "person") >= 30; }],
    ["places10", "⌖", "Pilgrim", "Pererin", "Visit 10 places", "Ymweld â 10 lle", function (j) { return count(j, "place") >= 10; }],
    ["legends", "☾", "Storyteller", "Cyfarwydd", "Read ten legends", "Darllen deg chwedl", function (j) { return count(j, "legend") >= 10; }],
    ["stories", "¶", "Scholar", "Ysgolhaig", "Read twelve long reads", "Darllen deuddeg erthygl", function (j) { return count(j, "story") >= 12; }],
    ["daily1", "?", "Day one", "Diwrnod un", "Solve a daily challenge", "Datrys her y dydd", function (j) { return j.d.wins >= 1; }],
    ["streak3", "3", "On a roll", "Ar rediad", "Play the daily challenge 3 days running", "Chwarae her y dydd 3 diwrnod yn olynol", function (j) { return j.d.best >= 3; }],
    ["streak7", "7", "A week of dates", "Wythnos o ddyddiadau", "Play the daily challenge 7 days running", "Chwarae her y dydd 7 diwrnod yn olynol", function (j) { return j.d.best >= 7; }],
    ["quiz8", "8", "Sharp", "Craff", "Score 8 or more in the quiz", "Sgorio 8 neu fwy yn y cwis", function (j) { return j.f.quiz8; }],
    ["quiz10", "★", "Pencampwr", "Pencampwr", "A perfect 10 in the quiz", "10 perffaith yn y cwis", function (j) { return j.f.quiz10; }],
    ["order15", "↕", "In good order", "Mewn trefn", "A perfect timeline challenge", "Her y llinell amser berffaith", function (j) { return j.f.order15; }],
    ["map300", "◎", "Map reader", "Darllenydd mapiau", "Score 300 or more in Where in Wales?", "Sgorio 300 neu fwy yn Ble yng Nghymru?", function (j) { return j.f.map300; }],
    ["pairs", "Aa", "Good memory", "Cof da", "Finish a game of word pairs", "Gorffen gêm o barau geiriau", function (j) { return j.f.pairs; }],
    ["ride", "♞", "Glyndŵr’s companion", "Cydymaith Glyndŵr", "Finish Ride with Glyndŵr, 1400", "Gorffen Marchogaeth gyda Glyndŵr, 1400", function (j) { return j.f.ride; }],
    ["set1", "❖", "Collector", "Casglwr", "Complete a set of cards", "Cwblhau set o gardiau", function (j) { return Object.keys(j.s).length >= 1; }],
    ["set5", "♛", "Keeper of treasures", "Ceidwad y trysorau", "Complete five sets of cards", "Cwblhau pum set o gardiau", function (j) { return Object.keys(j.s).length >= 5; }]
  ];
  var RANKS = [[0, "Newcomer", "Newydd-ddyfodiad"], [3, "Apprentice", "Prentis"], [12, "Storyteller", "Cyfarwydd"], [30, "Bard", "Bardd"], [60, "Chief bard", "Pencerdd"], [100, "Prince of history", "Tywysog hanes"]];
  function rank(n) { var r = RANKS[0]; RANKS.forEach(function (x) { if (n >= x[0]) r = x; }); return r; }
  var toasts = [], toasting = false;
  function say(icon, text, href) { toasts.push([icon, text, href || "journey.html"]); if (!toasting) nextToast(); }
  function nextToast() {
    var t = toasts.shift(); toasting = !!t; if (!t) return;
    var a = d.createElement("div"); a.className = "toast"; a.setAttribute("role", "status");
    a.innerHTML = '<a href="' + t[2] + '"><i aria-hidden="true">' + t[0] + "</i><span>" + t[1] + "</span></a>";
    d.body.appendChild(a); setTimeout(function () { a.remove(); nextToast(); }, 4300);
  }
  function toast(b) { say(b[1], T("Badge earned: ", "Bathodyn newydd: ") + T(b[2], b[3])); }
  /* ---------- collectable cards: each set on the page (.cset) is painted from the journey ---------- */
  function paintSets(j, fresh) {
    var sets = $$(".cset"); if (!sets.length) return;
    var seen = {}, nGot = 0, nSets = 0, changed = false;
    sets.forEach(function (el) {
      var cards = $$(".cc", el), have = 0, full;
      cards.forEach(function (c) { var g = !!j.v[c.dataset.k]; c.classList.toggle("got", g); if (g) have++; if (!seen[c.dataset.k]) { seen[c.dataset.k] = 1; if (g) nGot++; } });
      full = have === cards.length; el.classList.toggle("full", full); if (full) nSets++;
      var here = $(".cc.here", el), row = here && here.parentNode;
      if (row && row.scrollWidth > row.clientWidth) row.scrollLeft += here.getBoundingClientRect().left - row.getBoundingClientRect().left - 8;
      $(".cset-n b", el).textContent = have; $(".j-bar i", el).style.width = (have / cards.length * 100) + "%";
      var name = $(".cset-h h3", el), en = name && $(".l-en", name), cy = name && $(".l-cy", name), nm = name ? (en || cy ? T((en || cy).textContent, (cy || en).textContent) : name.textContent) : "";
      if (full && !j.s[el.dataset.set]) { j.s[el.dataset.set] = 1; changed = true; if (fresh) say("❖", T("Set complete: ", "Set yn gyflawn: ") + nm, "journey.html#cards"); }
      else if (fresh && $(".cc.here", el)) say("✦", T("New card for ", "Cerdyn newydd i ") + nm + " · " + have + " / " + cards.length, "journey.html#cards");
    });
    if (changed) save(j);
    var sum = $("#cards-sum");
    if (sum) sum.innerHTML = T("Every person, place and legend you read is a card. You have <b>" + nGot + "</b> of " + sum.dataset.total + " cards, and <b>" + nSets + "</b> of " + sum.dataset.sets + " sets are complete.",
      "Mae pob person, lle a chwedl a ddarllenwch yn gerdyn. Mae gennych <b>" + nGot + "</b> o " + sum.dataset.total + " o gardiau, ac mae <b>" + nSets + "</b> o " + sum.dataset.sets + " set yn gyflawn.");
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
    chip.setAttribute("aria-label", n + T(n === 1 ? " page read: your journey" : " pages read: your journey", " tudalen wedi’u darllen: eich taith"));
    chip.title = T("Pages you have read. Tap to see your journey and badges.", "Y tudalennau rydych wedi’u darllen. Tapiwch i weld eich taith a’ch bathodynnau.");
    $("#journey-ring").setAttribute("stroke-dasharray", Math.min(100, n / tot * 100).toFixed(1) + " 100");
  }
  var J = load();
  var track = d.body.getAttribute("data-track");
  var freshCard = false;
  if (track && !J.v[track]) { J.v[track] = 1; save(J); freshCard = true; }
  paintSets(J, freshCard);
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
  d.addEventListener("click", function (e) { if (e.target.closest(".lang button")) setTimeout(function () { renderJourney(); paintSets(load()); d.dispatchEvent(new Event("hc-lang")); }, 0); });
})();

/* The one-time hint that explains the journey circle in the menu bar, and the invitation to put the site on the home screen
   (on the third day someone visits; Android and desktop Chrome show the browser's own install box, iPhones get the two steps). */
(function () {
  var d = document, root = d.documentElement;
  var T = function (en, c) { return root.classList.contains("cy") ? c : en; };
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function put(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  var q = location.search;

  /* ---------- the journey circle hint: shown once, on the second page someone reads ---------- */
  var chip = d.getElementById("journey-chip"), n = 0;
  try { var j = JSON.parse(get("hc-journey") || "{}"); n = Object.keys(j.v || {}).length; } catch (e) {}
  if (chip && ((n >= 2 && !get("hc-hint")) || /[?&]hint=1/.test(q))) {
    put("hc-hint", "1");
    setTimeout(function () {
      var r = chip.getBoundingClientRect(); if (!r.width) return;
      var h = d.createElement("div"); h.className = "chip-hint"; h.setAttribute("role", "status");
      h.innerHTML = "<b>" + T("Your journey", "Eich taith") + "</b>" + T("Every page you read is counted here, and games earn badges. Tap the circle to see them.", "Mae pob tudalen a ddarllenwch yn cael ei chyfrif yma, ac mae gemau’n ennill bathodynnau. Tapiwch y cylch i’w gweld.");
      d.body.appendChild(h);
      var w = h.offsetWidth, left = Math.max(12, Math.min(innerWidth - w - 12, r.left + r.width / 2 - w / 2));
      h.style.left = left + "px"; h.style.top = (r.bottom + 12) + "px"; h.style.setProperty("--ax", (r.left + r.width / 2 - left - 6) + "px");
      function bye() { h.remove(); removeEventListener("scroll", bye); }
      h.addEventListener("click", bye); addEventListener("scroll", bye, { passive: true }); setTimeout(bye, 8000);
    }, 1800);
  }

  /* ---------- add to home screen ---------- */
  var standalone = (window.matchMedia && matchMedia("(display-mode: standalone)").matches) || navigator.standalone;
  if (standalone) return;
  var today = new Date().toISOString().slice(0, 10), days = (get("hc-days") || "").split(",").filter(Boolean);
  if (days.indexOf(today) < 0) { days.push(today); put("hc-days", days.slice(-30).join(",")); }
  var force = /[?&]install=1/.test(q), ios = /iphone|ipad|ipod/i.test(navigator.userAgent) && !/crios|fxios/i.test(navigator.userAgent);
  var want = force || (days.length >= 3 && !get("hc-install-no"));
  var prompt = null;
  function show() {
    if (d.querySelector(".install-bar")) return;
    var b = d.createElement("div"); b.className = "install-bar"; b.setAttribute("role", "dialog"); b.setAttribute("aria-label", T("Add to your home screen", "Ychwanegu at eich sgrin gartref"));
    var how = ios ? T("Tap the Share button, then “Add to Home Screen”.", "Tapiwch y botwm Rhannu, yna “Add to Home Screen”.") : T("One tap puts it on your home screen, like an app. It works offline too.", "Un tap ac mae ar eich sgrin gartref, fel ap. Mae’n gweithio heb y we hefyd.");
    b.innerHTML = '<img src="icon-192.png" alt=""><p><b>' + T("Keep Wales close", "Cadwch Gymru’n agos") + "</b>" + how + '</p><div class="row"><button type="button" class="no">' + T("Not now", "Dim nawr") + "</button>" + (prompt ? '<button type="button" class="go">' + T("Add it", "Ychwanegu") + "</button>" : "") + "</div>";
    d.body.appendChild(b);
    b.querySelector(".no").addEventListener("click", function () { put("hc-install-no", today); b.remove(); });
    var go = b.querySelector(".go");
    if (go) go.addEventListener("click", function () { b.remove(); prompt.prompt(); prompt.userChoice.then(function (c) { if (c.outcome !== "accepted") put("hc-install-no", today); }); prompt = null; });
  }
  addEventListener("beforeinstallprompt", function (e) { e.preventDefault(); prompt = e; if (want) setTimeout(show, 6000); });
  if (want && (ios || force)) setTimeout(show, force ? 500 : 6000);
})();

/* What's new: "New" labels on news added since someone's last look, and a red dot on the menu until they have seen the
   What's new page. First-time visitors start with nothing marked new. */
(function () {
  var d = document;
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function put(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  var mb = d.getElementById("menu-btn"), latest = mb && mb.getAttribute("data-news");
  if (!latest) return;
  var seen = get("hc-news-seen");
  if (!seen) {
    var j = {}; try { j = JSON.parse(get("hc-journey") || "{}"); } catch (e) {}
    var old = Object.keys(j.v || {}).length > 1;   /* visited before this feature: show what has arrived since */
    seen = old ? "2026-11-10" : latest; put("hc-news-seen", seen);
  }
  Array.prototype.forEach.call(d.querySelectorAll(".news-item[data-date]"), function (li) { if (li.getAttribute("data-date") > seen) li.classList.add("is-new"); });
  if (location.pathname.indexOf("whatsnew") >= 0) put("hc-news-seen", latest);
  else if (latest > seen) {
    mb.classList.add("has-news");
    Array.prototype.forEach.call(d.querySelectorAll('.menu a[href="whatsnew.html"]'), function (a) { a.classList.add("has-news"); });
  }
})();

/* The Share button: the phone's own share sheet where there is one, otherwise WhatsApp, Facebook, X, email or copy the link. */
(function () {
  var d = document, root = d.documentElement;
  var T = function (en, c) { return root.classList.contains("cy") ? c : en; };
  var pop = null;
  function close() { if (pop) { pop.remove(); pop = null; } }
  d.addEventListener("click", function (e) {
    var b = e.target.closest("[data-share]");
    if (!b) { if (pop && !e.target.closest(".share-pop")) close(); return; }
    var can = d.querySelector('link[rel="canonical"]'), url = can ? can.href : location.href.split("#")[0];
    var title = d.title.replace(/ · History of Wales$/, ""), text = title + " · History of Wales";
    if (navigator.share) { navigator.share({ title: text, url: url }).catch(function () {}); return; }
    if (pop) { close(); return; }
    var u = encodeURIComponent(url), t = encodeURIComponent(text);
    pop = d.createElement("div"); pop.className = "share-pop"; pop.setAttribute("role", "menu");
    pop.innerHTML = '<a role="menuitem" target="_blank" rel="noopener" href="https://wa.me/?text=' + t + "%20" + u + '">WhatsApp</a>' +
      '<a role="menuitem" target="_blank" rel="noopener" href="https://www.facebook.com/sharer/sharer.php?u=' + u + '">Facebook</a>' +
      '<a role="menuitem" target="_blank" rel="noopener" href="https://twitter.com/intent/tweet?text=' + t + "&url=" + u + '">X</a>' +
      '<a role="menuitem" href="mailto:?subject=' + t + "&body=" + u + '">' + T("Email", "E-bost") + "</a>" +
      '<button type="button" role="menuitem" class="copy">' + T("Copy the link", "Copïo’r ddolen") + "</button>";
    d.body.appendChild(pop);
    var r = b.getBoundingClientRect(), left = Math.min(r.left, innerWidth - pop.offsetWidth - 12);
    pop.style.left = Math.max(12, left) + "px"; pop.style.top = (r.bottom + 8 + pop.offsetHeight > innerHeight ? r.top - pop.offsetHeight - 8 : r.bottom + 8) + "px";
    pop.querySelector(".copy").addEventListener("click", function () {
      var c = this; (navigator.clipboard ? navigator.clipboard.writeText(url) : Promise.reject()).then(function () { c.textContent = T("Link copied", "Wedi copïo"); setTimeout(close, 900); }, function () { prompt(T("Copy this link", "Copïwch y ddolen hon"), url); close(); });
    });
  });
  addEventListener("scroll", close, { passive: true });
  d.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
})();
