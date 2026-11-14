/* Site search: opens from the magnifier in the menu, or by pressing "/". */
(function () {
  var data = null, box = null, last = null;
  var cy = function () { return document.documentElement.classList.contains("cy"); };
  var T = function (en, c) { return cy() ? c : en; };
  var KIND = { era: ["Age", "Oes"], person: ["Person", "Person"], place: ["Place", "Lle"], event: ["Event", "Digwyddiad"], trail: ["Trail", "Llwybr"], page: ["Page", "Tudalen"], story: ["Long read", "Erthygl"], legend: ["Legend", "Chwedl"],
    ruler: ["King or prince", "Brenin neu dywysog"], term: ["A–Z", "A–Y"], town: ["Town or village", "Tref neu bentref"], battle: ["Battle", "Brwydr"], doc: ["Document", "Dogfen"], question: ["Question", "Cwestiwn"], site: ["Historic site", "Safle hanesyddol"], topic: ["Topic guide", "Canllaw pwnc"], map: ["Map", "Map"] };
  var norm = function (s) { return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[’']/g, "").replace(/-/g, " "); };
  /* Old English spellings and English names, so "Llewellyn", "Glendower" or "Caernarvon" still find the page. Each word also keeps itself. */
  var ALIAS = { llewellyn: "llywelyn", llewelyn: "llywelyn", llewelin: "llywelyn", llywellyn: "llywelyn", llewellin: "llywelyn", glendower: "glyndwr", glendwr: "glyndwr", owen: "owain",
    howel: "hywel", howell: "hywel", hoel: "hywel", griffith: "gruffudd", griffiths: "gruffudd", gruffydd: "gruffudd", gruffyd: "gruffudd", griffin: "gruffudd", rees: "rhys", rice: "rhys", reese: "rhys",
    cadwallader: "cadwaladr", caradoc: "caradog", caractacus: "caradog caratacus", caratacus: "caradog", maximus: "macsen", merlin: "myrddin", gerald: "gerallt", giraldus: "gerallt", david: "dewi", davids: "dewi tyddewi",
    henry: "harri", tudor: "tudur", great: "fawr mawr", good: "dda", taffy: "dewi", boudicca: "buddug", boadicea: "buddug", vortigern: "gwrtheyrn", cunedda: "cunedda",
    caernarvon: "caernarfon", carnarvon: "caernarfon", conway: "conwy", dolgelley: "dolgellau", llanelly: "llanelli", portmadoc: "porthmadog", aberdovey: "aberdyfi", dovey: "dyfi", towy: "tywi",
    snowdon: "wyddfa eryri", snowdonia: "eryri", anglesey: "mon", cardiff: "caerdydd", swansea: "abertawe", newport: "casnewydd", carmarthen: "caerfyrddin", brecon: "aberhonddu brycheiniog",
    brecknock: "brycheiniog", glamorgan: "morgannwg", powis: "powys", cardigan: "aberteifi ceredigion", pembroke: "penfro", monmouth: "mynwy", denbigh: "dinbych", wrexham: "wrecsam",
    holyhead: "caergybi", neath: "nedd", bridgend: "pen y bont", mold: "wyddgrug", chepstow: "cas gwent", abergavenny: "fenni", welshpool: "trallwng", llandovery: "llanymddyfri",
    beaumaris: "biwmares", builth: "buallt", radnor: "maesyfed", ruthin: "rhuthun", asaph: "llanelwy", milford: "aberdaugleddau", haverfordwest: "hwlffordd", fishguard: "abergwaun",
    tenby: "dinbych pysgod", barmouth: "abermaw", lampeter: "llanbedr", druid: "derwydd", druids: "derwyddon derwydd", bard: "bardd", bards: "beirdd bardd", saint: "sant", saints: "seintiau sant",
    law: "cyfraith", laws: "cyfraith cyfreithiau", king: "brenin", prince: "tywysog", castle: "castell", battle: "brwydr", chapel: "capel", welsh: "cymraeg cymru wales", wales: "cymru welsh" };
  /* Soft, nasal and aspirate mutations undone, so "Gaerdydd", "Nghymru" or "Fangor" find Caerdydd, Cymru and Bangor. */
  var MUT = [["ngh", "c"], ["mh", "p"], ["nh", "t"], ["ng", "g"], ["ch", "c"], ["ph", "p"], ["th", "t"], ["dd", "d"], ["f", "b m"], ["g", "c"], ["b", "p"], ["d", "t"], ["l", "ll"], ["r", "rh"], ["m", "b"], ["n", "d"], ["", "g"]];
  var unmutate = function (w) {
    var out = [];
    MUT.forEach(function (m) { if (w.indexOf(m[0]) === 0 && w.length > m[0].length + 2) m[1].split(" ").forEach(function (b) { out.push(b + w.slice(m[0].length)); }); });
    return out;
  };
  var edits = function (a, b, max) {
    if (Math.abs(a.length - b.length) > max) return max + 1;
    var prev = [], cur, i, j;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      cur = [i]; var best = i;
      for (j = 1; j <= b.length; j++) { cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)); if (cur[j] < best) best = cur[j]; }
      if (best > max) return max + 1;
      prev = cur;
    }
    return prev[b.length];
  };
  var vocab = null;
  /* Welsh pages live in cy/ and carry <base href="../">, so a bare "person-x.html" would open the English page.
     Build the Welsh address here, so Enter, a click and "open in new tab" all keep the reader's language. */
  var href = function (u) { return cy() && /^[^:\/?#]+\.html([?#].*)?$/.test(u) ? "cy/" + u.replace(/^index\.html/, "") : u; };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var css = ".sx{position:fixed;inset:0;z-index:100;background:color-mix(in srgb,var(--night) 82%,transparent);backdrop-filter:blur(6px);display:flex;justify-content:center;align-items:flex-start;padding:calc(env(safe-area-inset-top,0px) + 8vh) var(--gut-r,16px) 16px var(--gut-l,16px)}" +
    ".sx-panel{width:min(44rem,100%);max-height:80vh;display:grid;grid-template-rows:auto 1fr;background:var(--slate);border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.5)}" +
    ".sx-top{display:flex;gap:.6rem;align-items:center;padding:.8rem 1rem;border-bottom:1px solid var(--line)}.sx-top svg{width:1.2rem;height:1.2rem;color:var(--muted);flex:none}" +
    ".sx-top input{flex:1;min-width:0;background:none;border:0;color:var(--ink);font:inherit;font-size:1.15rem;padding:.4rem 0;outline:none}" +
    ".sx-close{background:none;border:1px solid var(--line);color:var(--muted);border-radius:8px;padding:.25rem .55rem;font:500 .75rem var(--f-mono);cursor:pointer}" +
    ".sx-list{list-style:none;margin:0;padding:.4rem;overflow:auto}.sx-list a{display:grid;gap:.15rem;padding:.7rem .8rem;border-radius:10px;text-decoration:none;color:var(--ink);border-left:3px solid var(--c)}" +
    ".sx-list a:hover,.sx-list a:focus,.sx-list a[aria-selected=true]{background:var(--slate-2);outline:none}.sx-list a:focus-visible,.sx-close:focus-visible{outline:2px solid var(--ink);outline-offset:-2px}" +
    ".sx-sr{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}.sx-list b{font-weight:600}" +
    ".sx-meta{font:500 .72rem var(--f-mono);color:var(--muted);letter-spacing:.04em;text-transform:uppercase}.sx-b{font-size:.9rem;color:var(--muted);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}" +
    ".sx-empty{padding:1.2rem;color:var(--muted)}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  function load() {
    if (data) return Promise.resolve(data);
    return fetch("search.json").then(function (r) { return r.json(); }).then(function (d) {
      var v = {};
      d.forEach(function (x) {
        x.n = norm(x.t + " " + x.c); x.n += " " + x.n.replace(/ /g, ""); x.m = norm(x.b[0] + " " + x.b[1] + " " + x.y[0] + " " + (x.a || ""));
        x.n.split(" ").forEach(function (w) { if (w.length > 3) v[w] = 1; });
      });
      vocab = Object.keys(v); data = d; return d;
    });
  }
  var rank = { person: 0, ruler: 0.5, place: 1, town: 1, battle: 1, term: 1.5, question: 1.5, doc: 1.5, topic: 1.5, era: 2, story: 2, legend: 2, site: 2.5, trail: 3, page: 3, map: 3, event: 4 };
  function score(x, alts) {  // alts: the spellings one query word may take; best one counts
    var best = -1;
    alts.forEach(function (w) {
      var s = (x.n.indexOf(w) === 0 || x.n.indexOf(" " + w) >= 0) ? 10 : x.n.indexOf(w) >= 0 ? 6 : x.m.indexOf(w) >= 0 ? 2 : -1;
      if (s > best) best = s;
    });
    return best;
  }
  function run(groups) {
    return data.map(function (x) {
      var s = 0;
      for (var i = 0; i < groups.length; i++) { var g = score(x, groups[i]); if (g < 0) return null; s += g; }
      return [s - rank[x.k] * 0.1, x];
    }).filter(Boolean).sort(function (a, b) { return b[0] - a[0]; }).slice(0, 40).map(function (r) { return r[1]; });
  }
  function hits(alts) { if (!data) return true; for (var i = 0; i < data.length; i++) if (score(data[i], alts) >= 0) return true; return false; }
  var fixed = null;  // the spelling search used instead of what was typed, shown above the results
  function search(q) {
    fixed = null;
    var words = norm(q).split(/\s+/).filter(Boolean); if (!words.length) return [];
    var groups = words.map(function (w) { var a = [w]; if (ALIAS[w]) a = a.concat(ALIAS[w].split(" ")); return a; });
    var swapped = [];
    groups = groups.map(function (alts) {
      if (hits(alts)) return alts;
      var w = alts[0], um = unmutate(w).filter(function (u) { return hits([u]); });
      if (um.length) { swapped.push(um[0]); return um; }
      if (w.length < 4) return alts;
      var max = w.length >= 7 ? 2 : 1, near = null, nd = max + 1;
      vocab.forEach(function (v) { var d = edits(w, v, max); if (d < nd) { nd = d; near = v; } });
      if (near) { swapped.push(near); return [near]; }
      return alts;
    });
    if (swapped.length) fixed = swapped.join(", ");
    return run(groups);
  }
  function render() {
    var q = box.querySelector("input").value, list = box.querySelector(".sx-list");
    say(""); active(-1);
    if (!q.trim()) { list.innerHTML = '<li class="sx-empty">' + T("Search everything on the site: people, kings, saints, castles, towns, battles, words and dates. Try ‘Llewellyn’, ‘1282’, ‘cantref’ or ‘Merthyr’.", "Chwiliwch bopeth ar y wefan: pobl, brenhinoedd, seintiau, cestyll, trefi, brwydrau, geiriau a dyddiadau. Rhowch gynnig ar ‘Llywelyn’, ‘1282’, ‘cantref’ neu ‘Merthyr’.") + "</li>"; return; }
    if (!data) { list.innerHTML = '<li class="sx-empty">' + T("Loading…", "Yn llwytho…") + "</li>"; return; }  // typed before the index arrived: load() renders again
    var r = search(q);
    list.innerHTML = (fixed && r.length ? '<li class="sx-empty">' + T("Showing results for", "Yn dangos canlyniadau ar gyfer") + " <b>" + esc(fixed) + "</b></li>" : "") + (r.length ? r.map(function (x, i) {
      return '<li><a href="' + esc(href(x.u)) + '" id="sx-o' + i + '" role="option" aria-selected="' + (i === 0) + '" data-era="' + x.e + '"><span class="sx-meta">' + T(KIND[x.k][0], KIND[x.k][1]) + (x.y[0] ? " · " + esc(T(x.y[0], x.y[1])) : "") + "</span><b>" + esc(T(x.t, x.c)) + '</b><span class="sx-b">' + esc(T(x.b[0], x.b[1])) + "</span></a></li>";
    }).join("") : '<li class="sx-empty">' + T("Nothing found. Try a shorter word, or look in the <a href=\"a-z.html\">A–Z</a> or the <a href=\"questions.html\">quick answers</a>.", "Dim byd wedi’i ganfod. Rhowch gynnig ar air byrrach, neu edrychwch yn yr <a href=\"cy/a-z.html\">A–Y</a> neu’r <a href=\"cy/questions.html\">atebion cyflym</a>.") + "</li>");
    if (r.length) active(0);
    say(r.length ? T(r.length === 1 ? "1 result" : r.length + (r.length === 40 ? "+" : "") + " results", r.length === 1 ? "1 canlyniad" : r.length + (r.length === 40 ? "+" : "") + " canlyniad") : T("Nothing found", "Dim byd wedi’i ganfod"));
  }
  /* For screen readers: the input points at the highlighted result, and the number of results is read out. */
  function active(i) {
    var inp = box.querySelector("input"), links = box.querySelectorAll(".sx-list a[role=option]");
    [].forEach.call(links, function (a, j) { a.setAttribute("aria-selected", String(j === i)); });
    if (i >= 0 && links[i]) inp.setAttribute("aria-activedescendant", links[i].id); else inp.removeAttribute("aria-activedescendant");
  }
  var sayT = null;
  function say(t) { var el = box.querySelector(".sx-sr"); clearTimeout(sayT); sayT = setTimeout(function () { el.textContent = t; }, t ? 400 : 0); }
  /* Everything Tab can reach inside the box, in order. */
  function tabbables() { return [].slice.call(box.querySelectorAll("input,button,a[href]")).filter(function (el) { return el.offsetParent !== null || el === document.activeElement; }); }
  var shut = [];  // the rest of the page, made inert while search is open
  function open() {
    if (box && !box.hidden) { box.querySelector("input").focus(); return; }  // already open ("/" pressed on Close or a result): opening again would lose what to give back on close
    last = document.activeElement;
    if (!box) {
      box = document.createElement("div"); box.className = "sx"; box.setAttribute("role", "dialog"); box.setAttribute("aria-modal", "true");
      box.innerHTML = '<div class="sx-panel"><div class="sx-top"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.5 15.5 21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>' +
        '<input type="search" autocomplete="off" spellcheck="false" role="combobox" aria-autocomplete="list" aria-expanded="true" aria-controls="sx-list"><button type="button" class="sx-close" aria-keyshortcuts="Escape"></button></div>' +
        '<ul class="sx-list" id="sx-list" role="listbox"></ul><p class="sx-sr" role="status" aria-live="polite"></p></div>';
      document.body.appendChild(box);
      var inp = box.querySelector("input");
      inp.addEventListener("input", render);
      inp.addEventListener("keydown", function (ev) {
        var links = [].slice.call(box.querySelectorAll(".sx-list a[role=option]")), i = links.findIndex(function (a) { return a.getAttribute("aria-selected") === "true"; });
        if (ev.key === "ArrowDown" || ev.key === "ArrowUp") { ev.preventDefault(); if (!links.length) return; i = (i + (ev.key === "ArrowDown" ? 1 : -1) + links.length) % links.length; active(i); links[i].scrollIntoView({ block: "nearest" }); }
        if (ev.key === "Enter" && links.length) { ev.preventDefault(); var to = links[Math.max(0, i)].href; close(); location.href = to; }
      });
      /* A result that has focus (reached with Tab): the arrows move between results, and up from the first goes back to the box. */
      box.querySelector(".sx-list").addEventListener("keydown", function (ev) {
        if (ev.key !== "ArrowDown" && ev.key !== "ArrowUp") return;
        var links = [].slice.call(box.querySelectorAll(".sx-list a[role=option]")), i = links.indexOf(document.activeElement);
        if (i < 0) return; ev.preventDefault();
        if (ev.key === "ArrowUp" && i === 0) { box.querySelector("input").focus(); return; }
        var n = links[Math.min(links.length - 1, i + (ev.key === "ArrowDown" ? 1 : -1))]; n.focus(); active(links.indexOf(n));
      });
      box.addEventListener("click", function (ev) { if (ev.target === box || ev.target.closest(".sx-close")) close(); else if (ev.target.closest(".sx-list a")) setTimeout(close, 0); });
      /* Keep keyboard focus inside the search box while it is open: Tab and Shift+Tab go round its own controls. */
      box.addEventListener("keydown", function (ev) {
        if (ev.key === "Escape") { ev.preventDefault(); close(); return; }
        if (ev.key !== "Tab") return;
        var t = tabbables(); if (!t.length) return;
        var i = t.indexOf(document.activeElement);
        if (ev.shiftKey && i <= 0) { ev.preventDefault(); t[t.length - 1].focus(); }
        else if (!ev.shiftKey && (i < 0 || i === t.length - 1)) { ev.preventDefault(); t[0].focus(); }
      });
      /* If focus still escapes (a screen reader, or a click on the page behind), bring it back. */
      document.addEventListener("focusin", function (ev) { if (!box.hidden && !box.contains(ev.target)) box.querySelector("input").focus(); });
    }
    var inp = box.querySelector("input"), x = box.querySelector(".sx-close");
    box.setAttribute("aria-label", T("Search the site", "Chwilio’r wefan"));
    inp.placeholder = T("Search the history of Wales", "Chwilio hanes Cymru"); inp.setAttribute("aria-label", T("Search the history of Wales", "Chwilio hanes Cymru"));
    x.textContent = T("Close", "Cau"); x.setAttribute("aria-label", T("Close search", "Cau’r chwilio")); x.title = T("Close search (Esc)", "Cau’r chwilio (Esc)");
    shut = [].filter.call(document.body.children, function (el) { return el !== box && !el.inert; });
    shut.forEach(function (el) { el.inert = true; });
    box.hidden = false; document.body.style.overflow = "hidden"; inp.focus(); inp.select();
    load().then(render, function () { box.querySelector(".sx-list").innerHTML = '<li class="sx-empty">' + T("Search isn’t available offline.", "Nid yw chwilio ar gael all-lein.") + "</li>"; });
  }
  function close() { if (!box || box.hidden) return; box.hidden = true; document.body.style.overflow = ""; shut.forEach(function (el) { el.inert = false; }); shut = []; if (last && last.focus) last.focus(); }
  document.addEventListener("click", function (ev) { if (ev.target.closest("[data-search]")) open(); });
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "/" && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName) && !ev.metaKey && !ev.ctrlKey) { ev.preventDefault(); open(); }
  });
})();
