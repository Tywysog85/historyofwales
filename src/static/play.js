/* Games: daily year challenge, Where in Wales?, Welsh names, which figure are you?, word pairs.
   Each page has <div id="g-root" data-game="…"> and a PLAY object written by build.py. */
(function () {
  var d = document, root = d.getElementById("g-root"); if (!root || !window.PLAY) return;
  var P = window.PLAY, kind = root.dataset.game;
  var cy = function () { return d.documentElement.classList.contains("cy"); };
  var T = function (en, c) { return cy() ? c : en; };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var $ = function (s) { return root.querySelector(s); };
  var HC = function () { return window.HC; };
  function shuffle(a, rnd) { a = a.slice(); rnd = rnd || Math.random; for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(rnd() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function seeded(seed) { return function () { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }; }
  function copy(btn, txt) { var done = function () { var o = btn.textContent; btn.textContent = T("Copied", "Wedi copïo"); setTimeout(function () { btn.textContent = o; }, 1600); }; try { navigator.clipboard.writeText(txt).then(done, function () {}); } catch (e) {} }
  var ERA_NAMES = { ancient: ["Ancient Wales", "Cymru Hynafol"], saints: ["The Age of Saints (410–800)", "Oes y Seintiau (410–800)"], kings: ["The Age of Kings (800–1100)", "Oes y Brenhinoedd (800–1100)"], medieval: ["The Age of Princes (1100–1485)", "Oes y Tywysogion (1100–1485)"], industrial: ["Tudors to Industry (1485–1914)", "Y Tuduriaid a Diwydiant (1485–1914)"], modern: ["Modern Wales (1914 to today)", "Cymru Fodern (1914 hyd heddiw)"] };
  var render;

  /* ================= Daily challenge ================= */
  if (kind === "daily") {
    var pool = P.EV.filter(function (e) { return e[0] >= 500 && !e[1]; });
    pool = shuffle(pool, seeded(20261110));
    var now = new Date(), key = now.getFullYear() + "-" + ("0" + (now.getMonth() + 1)).slice(-2) + "-" + ("0" + now.getDate()).slice(-2);
    var dayN = Math.round((Date.UTC(now.getFullYear(), now.getMonth(), now.getDate()) - Date.UTC(2026, 10, 10)) / 864e5);
    var ev = pool[((dayN % pool.length) + pool.length) % pool.length], ANS = ev[0], MAX = 6;
    var j = HC() ? HC().load() : { d: {} }, st = j.daily && j.daily.date === key ? j.daily : { date: key, g: [], done: false, win: false };
    var blank = function (s) { return esc(s).replace(/\b(1[0-9]{3}|20[0-9]{2}|[5-9][0-9]{2})\b/g, "<b>____</b>"); };
    function grade(g) { var a = Math.abs(g - ANS); return a === 0 ? ["#7cc495", "🟩", T("Correct!", "Cywir!")] : a <= 5 ? ["#e8c65a", "🟨", T("So close", "Agos iawn")] : a <= 25 ? ["#f0975a", "🟧", T("Close", "Agos")] : a <= 100 ? ["#f26a62", "🟥", T("Within a century", "O fewn canrif")] : ["#6b7385", "⬛", T("Far off", "Ymhell")]; }
    function persist() {
      if (!HC()) return; var jj = HC().load(); jj.daily = st;
      if (st.done && jj.d.last !== key) {
        var y = new Date(now.getFullYear(), now.getMonth(), now.getDate() - 1), yk = y.getFullYear() + "-" + ("0" + (y.getMonth() + 1)).slice(-2) + "-" + ("0" + y.getDate()).slice(-2);
        jj.d.streak = jj.d.last === yk ? (jj.d.streak || 0) + 1 : 1; jj.d.best = Math.max(jj.d.best || 0, jj.d.streak); jj.d.played = (jj.d.played || 0) + 1; if (st.win) jj.d.wins = (jj.d.wins || 0) + 1; jj.d.last = key;
      }
      HC().save(jj); HC().check();
    }
    render = function () {
      var rows = "";
      for (var i = 0; i < MAX; i++) {
        var g = st.g[i];
        if (g == null) { rows += '<li class="empty"></li>'; continue; }
        var gr = grade(g);
        rows += '<li style="--k:' + gr[0] + '"><b>' + g + "</b><span>" + gr[2] + (g === ANS ? "" : " · " + (g < ANS ? T("it was later", "roedd yn hwyrach") + " ↑" : T("it was earlier", "roedd yn gynharach") + " ↓")) + "</span><i>" + gr[1] + "</i></li>";
      }
      var hint = st.g.length >= 3 && !st.done ? '<p class="g-note">' + T("Clue: it happened in ", "Cliw: digwyddodd yn ") + "<b>" + T(ERA_NAMES[ev[4]][0], ERA_NAMES[ev[4]][1]) + "</b>.</p>" : "";
      var h = '<div class="q-top"><span>' + T("Challenge", "Her") + " #" + (dayN + 1) + "</span><span>" + T("Guess", "Cynnig") + " " + Math.min(st.g.length + (st.done ? 0 : 1), MAX) + " / " + MAX + "</span></div>" +
        "<h2>" + blank(T(ev[2], ev[3])) + '</h2><p class="g-ctx">' + blank(T(ev[5], ev[6])) + "</p>";
      if (!st.done) h += '<form class="g-form" id="d-form" autocomplete="off"><label for="d-in" class="sr-only">' + T("Year", "Blwyddyn") + '</label><input class="g-in" id="d-in" inputmode="numeric" pattern="[0-9]*" maxlength="4" placeholder="' + T("Year", "Blwyddyn") + '" required><button class="btn solid" type="submit">' + T("Guess", "Cynnig") + "</button></form>" + hint;
      h += '<ol class="g-rows">' + rows + "</ol>";
      if (st.done) {
        var jj = HC() ? HC().load() : { d: {} }, squares = st.g.map(function (g) { return grade(g)[1]; }).join("");
        var share = T("History of Wales daily challenge #", "Her y dydd Hanes Cymru #") + (dayN + 1) + " · " + (st.win ? st.g.length : "X") + "/" + MAX + "\n" + squares + "\nhttps://historyofwales.cymru/daily.html";
        h += '<div class="g-result"><p class="eyebrow">' + (st.win ? T("You got it", "Fe’i cawsoch") : T("The answer", "Yr ateb")) + '</p><p class="g-big">' + ANS + '</p><p class="g-ctx"><b>' + esc(T(ev[2], ev[3])) + ".</b> " + esc(T(ev[5], ev[6])) + "</p>" +
          '<div class="g-stats"><div><b>' + (jj.d.streak || 0) + "</b><span>" + T("Day streak", "Rhediad") + "</span></div><div><b>" + (jj.d.best || 0) + "</b><span>" + T("Best streak", "Rhediad gorau") + "</span></div><div><b>" + (jj.d.wins || 0) + "/" + (jj.d.played || 0) + "</b><span>" + T("Solved", "Datryswyd") + "</span></div></div>" +
          '<p class="g-share">' + esc(share) + '</p><div class="g-row"><button type="button" class="btn solid" id="d-share">' + T("Copy my result", "Copïo fy nghanlyniad") + '</button><a class="btn" href="timeline.html#ev-' + ev[7] + '">' + T("See it on the timeline", "Gweld ar y llinell amser") + ' →</a></div><p class="g-note">' + T("A new challenge appears at midnight. Come back tomorrow to keep your streak.", "Daw her newydd am hanner nos. Dewch yn ôl yfory i gadw’ch rhediad.") + "</p></div>";
      }
      root.innerHTML = h;
      var f = $("#d-form");
      if (f) f.onsubmit = function (e) {
        e.preventDefault(); var v = parseInt($("#d-in").value, 10); if (!(v > 0 && v < 2100)) return;
        st.g.push(v); if (v === ANS) { st.done = true; st.win = true; } else if (st.g.length >= MAX) st.done = true;
        persist(); render(); var n = $("#d-in"); if (n) n.focus();
      };
      var sb = $("#d-share"); if (sb) sb.onclick = function () { copy(sb, share); };
    };
  }

  /* ================= Where in Wales? ================= */
  if (kind === "map") {
    var M = P.MAPC, G = null, NS = "http://www.w3.org/2000/svg";
    var proj = function (lat, lon) { return [(lon - M.minx) * M.k * M.sc, (M.maxy - lat) * M.sc]; };
    var unproj = function (x, y) { return [M.maxy - y / M.sc, M.minx + x / (M.k * M.sc)]; };
    var km = function (a, b, c, e) { var R = 6371, r = Math.PI / 180, x = Math.sin((c - a) * r / 2), y = Math.sin((e - b) * r / 2); return 2 * R * Math.asin(Math.sqrt(x * x + Math.cos(a * r) * Math.cos(c * r) * y * y)); };
    var all = P.PL.map(function (p) { return [p[1], p[2], p[3], p[4], "place-" + p[0] + ".html"]; }).concat(P.TW.map(function (t) { return [t[0], t[1], t[2], t[3], ""]; }));
    var newGame = function () { G = { r: 0, total: 0, qs: shuffle(all).slice(0, 5), guess: null, pts: 0, km: 0 }; };
    newGame();
    render = function () {
      if (G.r >= 5) {
        var s = G.total, msg = s >= 400 ? T("Outstanding. You could draw the map yourself.", "Rhagorol. Gallech dynnu’r map eich hun.") : s >= 300 ? T("Da iawn! You know your way around.", "Da iawn! Rydych chi’n adnabod y wlad.") : s >= 150 ? T("Not bad. The map on the home page will help.", "Ddim yn ddrwg. Bydd y map ar yr hafan o gymorth.") : T("Wales is bigger than it looks. Try again.", "Mae Cymru’n fwy nag y mae’n edrych. Rhowch gynnig arall.");
        root.innerHTML = '<p class="eyebrow">' + T("Final score", "Sgôr terfynol") + '</p><p class="g-big">' + s + "<small style=\"font-size:.35em;color:var(--muted)\"> / 500</small></p><h2>" + msg + '</h2><div class="g-row"><button type="button" class="btn solid" id="m-again">' + T("Play again", "Chwarae eto") + '</button><button type="button" class="btn" id="m-share">' + T("Copy my score", "Copïo fy sgôr") + "</button></div>";
        if (s >= 300 && HC()) HC().flag("map300");
        $("#m-again").onclick = function () { newGame(); render(); };
        var b = $("#m-share"); b.onclick = function () { copy(b, T("I scored " + s + "/500 in Where in Wales? on History of Wales. Can you beat me? ", "Sgoriais " + s + "/500 yn Ble yng Nghymru? ar Hanes Cymru. Allwch chi wneud yn well? ") + "https://historyofwales.cymru/map-game.html"); };
        return;
      }
      var q = G.qs[G.r], done = G.guess != null, xy = proj(q[2], q[3]);
      var marks = "";
      if (done) {
        var gp = proj(G.guess[0], G.guess[1]), right = xy[0] > 400;
        marks = '<line class="link" x1="' + gp[0] + '" y1="' + gp[1] + '" x2="' + xy[0] + '" y2="' + xy[1] + '"/><circle class="guess" cx="' + gp[0] + '" cy="' + gp[1] + '" r="7"/><circle class="real" cx="' + xy[0] + '" cy="' + xy[1] + '" r="9"/><text x="' + (xy[0] + (right ? -14 : 14)) + '" y="' + (xy[1] + 4) + '" text-anchor="' + (right ? "end" : "start") + '">' + esc(T(q[0], q[1])) + "</text>";
      }
      root.innerHTML = '<div class="q-top"><span>' + T("Round", "Rownd") + " " + (G.r + 1) + " / 5</span><span>" + T("Score", "Sgôr") + " " + G.total + "</span></div><h2>" + T("Where is ", "Ble mae ") + '<span style="color:var(--gold)">' + esc(T(q[0], q[1])) + "</span>?</h2>" +
        '<p class="g-note" aria-live="polite">' + (done ? "<b style=\"color:var(--ink)\">" + (G.km < 1 ? T("Spot on", "Yn union") : Math.round(G.km) + " km " + T("away", "i ffwrdd")) + "</b> · +" + G.pts + " " + T("points", "pwynt") : T("Tap the map where you think it is.", "Tapiwch y map lle credwch ei fod.")) + "</p>" +
        '<svg class="g-map" id="g-map" viewBox="-20 -20 640 712" role="img" aria-label="' + T("Map of Wales", "Map Cymru") + '"><path class="land" d="' + P.OUT + '"/>' + marks + "</svg>" +
        (done ? '<div class="g-row"><button type="button" class="btn solid" id="m-next">' + (G.r < 4 ? T("Next place", "Lle nesaf") : T("See my score", "Gweld fy sgôr")) + " →</button>" + (q[4] ? '<a class="btn" href="' + q[4] + '">' + T("Read about it", "Darllen amdano") + "</a>" : "") + "</div>" : "");
      var svg = $("#g-map");
      if (!done) svg.addEventListener("click", function (e) {
        var pt = svg.createSVGPoint(); pt.x = e.clientX; pt.y = e.clientY; var p = pt.matrixTransform(svg.getScreenCTM().inverse()), ll = unproj(p.x, p.y);
        G.guess = ll; G.km = km(ll[0], ll[1], q[2], q[3]); G.pts = Math.round(100 * Math.exp(-G.km / 45)); G.total += G.pts; render(); var n = $("#m-next"); if (n) n.focus({ preventScroll: true });
      });
      var nx = $("#m-next"); if (nx) nx.onclick = function () { G.r++; G.guess = null; render(); root.scrollIntoView({ block: "start", behavior: "auto" }); };
    };
  }

  /* ================= Welsh names ================= */
  if (kind === "names") {
    var SN = {
      jones: ["John’s child. From the Welsh ‘Siôn’ or ‘Ioan’ with an English -s. The most common surname in Wales.", "Plentyn John. O ‘Siôn’ neu ‘Ioan’ gydag -s Saesneg. Y cyfenw mwyaf cyffredin yng Nghymru."],
      williams: ["William’s child. ‘Gwilym’ in Welsh.", "Plentyn William, sef Gwilym."],
      davies: ["David’s child, from ‘Dafydd’ and its pet form ‘Dai’. The patron saint’s name.", "Plentyn Dafydd, a’i ffurf anwes ‘Dai’. Enw’r nawddsant."],
      evans: ["Evan’s child. ‘Ifan’ or ‘Ieuan’ is the Welsh form of John.", "Plentyn Ifan neu Ieuan, ffurf Gymraeg ar John."],
      thomas: ["From the given name Thomas, ‘Tomos’ in Welsh.", "O’r enw bedydd Tomos."],
      roberts: ["Robert’s child. A Norman name taken up eagerly in north Wales.", "Plentyn Robert. Enw Normanaidd a fabwysiadwyd yn frwd yn y gogledd."],
      hughes: ["Hugh’s child. ‘Huw’ in Welsh, often used for the older Welsh name Hywel.", "Plentyn Huw, a ddefnyddid yn aml am yr hen enw Hywel."],
      lewis: ["An English form used for ‘Llywelyn’, the name of two great princes of Gwynedd.", "Ffurf Saesneg a ddefnyddid am ‘Llywelyn’, enw dau o dywysogion mawr Gwynedd."],
      morgan: ["A very old Welsh name, ‘Morcant’, borne by the kings who gave Morgannwg (Glamorgan) its name.", "Hen enw Cymraeg, ‘Morcant’, enw’r brenhinoedd a roddodd ei enw i Forgannwg."],
      griffiths: ["From ‘Gruffudd’, a name of Welsh kings and princes: ‘strong lord’.", "O ‘Gruffudd’, enw brenhinoedd a thywysogion Cymru."],
      edwards: ["Edward’s child. In Wales it often stood in for the Welsh name Iorwerth.", "Plentyn Edward. Yng Nghymru safai’n aml am yr enw Iorwerth."],
      owen: ["From ‘Owain’, the name of Owain Gwynedd and Owain Glyndŵr.", "O ‘Owain’, enw Owain Gwynedd ac Owain Glyndŵr."],
      james: ["From the given name James, ‘Iago’ in Welsh.", "O’r enw bedydd James, sef Iago."],
      price: ["ap Rhys: ‘son of Rhys’. The ‘ap’ fused onto the name.", "ap Rhys: ‘mab Rhys’. Glynodd yr ‘ap’ wrth yr enw."],
      powell: ["ap Hywel: ‘son of Hywel’.", "ap Hywel: ‘mab Hywel’."],
      bowen: ["ab Owain: ‘son of Owain’.", "ab Owain: ‘mab Owain’."],
      bevan: ["ab Ifan: ‘son of Ifan’. Aneurin Bevan’s surname.", "ab Ifan: ‘mab Ifan’. Cyfenw Aneurin Bevan."],
      pritchard: ["ap Rhisiart: ‘son of Richard’.", "ap Rhisiart: ‘mab Rhisiart’."],
      parry: ["ap Harri: ‘son of Harry’.", "ap Harri: ‘mab Harri’."],
      pugh: ["ap Huw: ‘son of Huw’.", "ap Huw: ‘mab Huw’."],
      probert: ["ap Robert: ‘son of Robert’.", "ap Robert: ‘mab Robert’."],
      prosser: ["ap Rosser: ‘son of Roger’.", "ap Rosser: ‘mab Rosser’."],
      prothero: ["ap Rhydderch: ‘son of Rhydderch’.", "ap Rhydderch: ‘mab Rhydderch’."],
      penry: ["ap Henri: ‘son of Henry’.", "ap Henri: ‘mab Henri’."],
      bellis: ["ab Elis: ‘son of Elis’.", "ab Elis: ‘mab Elis’."],
      beynon: ["ab Einion: ‘son of Einion’.", "ab Einion: ‘mab Einion’."],
      lloyd: ["From ‘llwyd’, grey or brown: a nickname for someone with grey hair. English clerks could not write ‘ll’.", "O ‘llwyd’: llysenw ar rywun â gwallt llwyd. Ni allai clercod Saesneg ysgrifennu ‘ll’."],
      vaughan: ["From ‘fychan’, small or younger: used to tell a son from a father of the same name.", "O ‘fychan’: i wahaniaethu rhwng mab a thad o’r un enw."],
      gough: ["From ‘coch’, red: a nickname for someone red-haired.", "O ‘coch’: llysenw ar rywun pengoch."],
      wynn: ["From ‘gwyn’, white or fair, also meaning blessed.", "O ‘gwyn’, sydd hefyd yn golygu bendigaid."],
      gwynne: ["From ‘gwyn’, white or fair, also meaning blessed.", "O ‘gwyn’, sydd hefyd yn golygu bendigaid."],
      howells: ["From ‘Hywel’, ‘eminent’: the name of Hywel Dda.", "O ‘Hywel’, enw Hywel Dda."],
      rees: ["From ‘Rhys’, the name of the princes of Deheubarth.", "O ‘Rhys’, enw tywysogion Deheubarth."],
      phillips: ["Philip’s child. Common in Pembrokeshire.", "Plentyn Phylip. Cyffredin yn Sir Benfro."],
      jenkins: ["‘Little John’: a pet form brought by Flemish settlers and taken up in south Wales.", "‘Siôn bach’: ffurf anwes a ddaeth gyda’r Ffleminiaid ac a fabwysiadwyd yn y de."],
      meredith: ["From ‘Maredudd’, an old princely name.", "O ‘Maredudd’, hen enw tywysogaidd."],
      llewellyn: ["From ‘Llywelyn’, the name of Llywelyn Fawr and Llywelyn ap Gruffudd.", "O ‘Llywelyn’, enw Llywelyn Fawr a Llywelyn ap Gruffudd."],
      maddox: ["From ‘Madog’, ‘fortunate’, with an English -s.", "O ‘Madog’ gydag -s Saesneg."],
      tudor: ["From ‘Tudur’. The family of Penmynydd on Ynys Môn who became kings of England.", "O ‘Tudur’. Teulu Penmynydd ym Môn a ddaeth yn frenhinoedd Lloegr."],
      sayce: ["From ‘Sais’, Englishman: a nickname for someone who spoke English or had lived in England.", "O ‘Sais’: llysenw ar rywun a siaradai Saesneg neu a fu’n byw yn Lloegr."],
      walsh: ["‘The Welshman’: the name the English and Irish gave to people from Wales.", "‘Y Cymro’: yr enw a roddai’r Saeson a’r Gwyddelod ar bobl o Gymru."],
      voyle: ["From ‘moel’, bald.", "O ‘moel’."],
      dee: ["From ‘du’, black or dark-haired.", "O ‘du’: rhywun gwallt tywyll."],
      gethin: ["From ‘cethin’, swarthy or fierce.", "O ‘cethin’: tywyll neu ffyrnig."],
      anwyl: ["From ‘annwyl’, dear or beloved.", "O ‘annwyl’."],
      nanney: ["A place-name surname, from Nannau near Dolgellau. Rare in Wales, where most surnames come from fathers’ names.", "Cyfenw o enw lle, Nannau ger Dolgellau. Prin yng Nghymru, lle daw’r rhan fwyaf o gyfenwau o enwau tadau."],
      mostyn: ["A place-name surname from Mostyn in Flintshire. The family chose it in the 1500s when told their string of ‘ap’s was too long for an English court.", "Cyfenw o enw lle, Mostyn yn Sir y Fflint. Dewisodd y teulu ef yn y 1500au pan ddywedwyd bod eu rhes o ‘ap’ yn rhy hir i lys Saesneg."]
    };
    var ALIAS = { davis: "davies", evan: "evans", hugh: "hughes", griffith: "griffiths", owens: "owen", pryce: "price", preece: "price", prys: "price", howell: "howells", powel: "powell", bevin: "bevan", prichard: "pritchard", pugh: "pugh", pew: "pugh", floyd: "lloyd", llwyd: "lloyd", vaughn: "vaughan", fychan: "vaughan", gooch: "gough", goch: "gough", wynne: "wynn", wyn: "wynn", gwyn: "wynn", gwynn: "gwynne", rhys: "rees", reese: "rees", rice: "rees", reece: "rees", philips: "phillips", jenkin: "jenkins", llewelyn: "llewellyn", llywelyn: "llewellyn", maddocks: "maddox", madoc: "maddox", tudur: "tudor", welsh: "walsh", welch: "walsh", lewes: "lewis", roberts: "roberts", robert: "roberts", william: "williams", edward: "edwards", john: "jones", bennion: "beynon", beinon: "beynon", protheroe: "prothero", meredydd: "meredith", maredudd: "meredith" };
    var CYN = { john: "Siôn", david: "Dafydd", dave: "Dafydd", william: "Gwilym", will: "Gwilym", evan: "Ifan", hugh: "Huw", richard: "Rhisiart", thomas: "Tomos", tom: "Tomos", james: "Iago", edward: "Iorwerth", stephen: "Steffan", steven: "Steffan", peter: "Pedr", paul: "Pawl", andrew: "Andreas", michael: "Mihangel", george: "Siôr", henry: "Harri", harry: "Harri", philip: "Phylip", mary: "Mair", margaret: "Marged", elizabeth: "Elisabeth", catherine: "Catrin", katherine: "Catrin", kate: "Catrin", jane: "Siân", jean: "Siân", joan: "Siwan", alice: "Alys", helen: "Elen", ellen: "Elen", sarah: "Sara", eleanor: "Elinor", matthew: "Mathew", mark: "Marc", luke: "Luc", jacob: "Iago", owen: "Owain", griffith: "Gruffudd", rees: "Rhys", lewis: "Llywelyn", howell: "Hywel", roger: "Rosser", walter: "Gwallter", morris: "Morys", maurice: "Morys", geoffrey: "Sieffre", jeffrey: "Sieffre", charles: "Siarl", anne: "Ann", anna: "Ann", martha: "Martha", lucy: "Lleucu", gwen: "Gwen", daniel: "Deiniol", joseph: "Ioseff", samuel: "Samiwel", nicholas: "Nicolas", laura: "Lowri", emily: "Emlyn" };
    delete CYN.emily;
    var sex = "m", cap = function (s) { s = s.trim().replace(/\s+/g, " "); return s ? s.charAt(0).toUpperCase() + s.slice(1) : ""; };
    var cyName = function (s) { var k = s.trim().toLowerCase(); return CYN[k] || cap(s); };
    var link = function (parent) { if (sex === "f") return "ferch"; return /^[aeiouwyâêîôûŵŷAEIOUWY]/.test(parent) ? "ab" : "ap"; };
    var vals = { sn: "", a: "", b: "", c: "" };
    render = function () {
      root.innerHTML = "<h2>" + T("What does your surname mean?", "Beth yw ystyr eich cyfenw?") + '</h2><p class="g-ctx">' + T("Until Tudor times most Welsh people had no fixed surname. You were your father’s child: Rhys ap Gruffudd, Gwenllian ferch Gruffudd. When English law demanded surnames, the father’s name was frozen in place, which is why so few surnames cover so many Welsh families.", "Hyd at oes y Tuduriaid nid oedd gan y rhan fwyaf o’r Cymry gyfenw sefydlog. Plentyn eich tad oeddech: Rhys ap Gruffudd, Gwenllian ferch Gruffudd. Pan fynnodd cyfraith Lloegr gyfenwau, rhewyd enw’r tad yn ei le, a dyna pam mae cyn lleied o gyfenwau gan gynifer o deuluoedd Cymru.") + "</p>" +
        '<form class="g-form" id="sn-form" autocomplete="off"><label for="sn-in" class="sr-only">' + T("Surname", "Cyfenw") + '</label><input class="g-in txt" id="sn-in" placeholder="' + T("Type a surname, e.g. Powell", "Teipiwch gyfenw, e.e. Powell") + '" value="' + esc(vals.sn) + '"></form><div class="sn-out" id="sn-out" aria-live="polite"></div>' +
        '<div class="sn-list" id="sn-list">' + ["Jones", "Davies", "Price", "Powell", "Bevan", "Lloyd", "Vaughan", "Gough", "Pritchard", "Morgan", "Tudor", "Sayce"].map(function (n) { return '<button type="button">' + n + "</button>"; }).join("") + "</div>" +
        '<h2 class="g-sub">' + T("Your name in the age of the princes", "Eich enw yn oes y tywysogion") + '</h2><p class="g-ctx">' + T("Enter your first name, a parent’s first name, and a grandparent’s if you like. Medieval Welsh people could recite their line back seven generations or more.", "Rhowch eich enw cyntaf, enw cyntaf rhiant, ac enw taid neu nain os dymunwch. Gallai Cymry’r Oesoedd Canol adrodd eu hachau’n ôl saith cenhedlaeth neu fwy.") + "</p>" +
        '<div class="seg2" role="group" aria-label="' + T("I am a", "Rwy’n") + '"><button type="button" data-sex="m" aria-pressed="' + (sex === "m") + '">' + T("Son (ap)", "Mab (ap)") + '</button><button type="button" data-sex="f" aria-pressed="' + (sex === "f") + '">' + T("Daughter (ferch)", "Merch (ferch)") + "</button></div>" +
        '<div class="g-form"><label class="sr-only" for="n-a">' + T("Your first name", "Eich enw cyntaf") + '</label><input class="g-in txt" id="n-a" placeholder="' + T("Your first name", "Eich enw cyntaf") + '" value="' + esc(vals.a) + '"><label class="sr-only" for="n-b">' + T("Parent’s first name", "Enw cyntaf rhiant") + '</label><input class="g-in txt" id="n-b" placeholder="' + T("Parent’s first name", "Enw cyntaf rhiant") + '" value="' + esc(vals.b) + '"><label class="sr-only" for="n-c">' + T("Grandparent’s first name (optional)", "Enw cyntaf taid neu nain (dewisol)") + '</label><input class="g-in txt" id="n-c" placeholder="' + T("Grandparent (optional)", "Taid neu nain (dewisol)") + '" value="' + esc(vals.c) + '"></div>' +
        '<div class="sn-out" id="n-out" aria-live="polite"></div>';
      var lookup = function () {
        var raw = $("#sn-in").value; vals.sn = raw; var k = raw.trim().toLowerCase().replace(/[^a-zâêîôûŵŷ]/g, ""); var hit = SN[k] || SN[ALIAS[k]] || (k.slice(-1) === "s" ? SN[k.slice(0, -1)] : null) || SN[k + "s"];
        $("#sn-out").innerHTML = !k ? "<span>" + T("Type a surname above, or choose one below.", "Teipiwch gyfenw uchod, neu dewiswch un isod.") + "</span>" : hit ? "<b>" + esc(cap(raw)) + "</b><span>" + T(hit[0], hit[1]) + "</span>" : "<b>" + esc(cap(raw)) + "</b><span>" + T("Not in our list of Welsh surnames yet. If it starts with P or B, try reading it as ‘ap’ plus a name: Probert is ap Robert.", "Nid yw yn ein rhestr o gyfenwau Cymreig eto. Os yw’n dechrau â P neu B, ceisiwch ei ddarllen fel ‘ap’ ac enw: ap Robert yw Probert.") + "</span>";
      };
      var make = function () {
        vals.a = $("#n-a").value; vals.b = $("#n-b").value; vals.c = $("#n-c").value;
        var a = cyName(vals.a), b = cyName(vals.b), c = cyName(vals.c);
        if (!a || !b) { $("#n-out").innerHTML = "<span>" + T("Your name will appear here.", "Bydd eich enw’n ymddangos yma.") + "</span>"; return; }
        var name = a + " " + link(b) + " " + b + (c ? " " + (/^[aeiouwyAEIOUWY]/.test(c) ? "ab" : "ap") + " " + c : "");
        var notes = [vals.a, vals.b, vals.c].filter(function (x) { return CYN[x.trim().toLowerCase()]; }).map(function (x) { return cap(x) + " → " + CYN[x.trim().toLowerCase()]; });
        $("#n-out").innerHTML = "<b>" + esc(name) + "</b><span>" + T("‘" + (sex === "f" ? "ferch" : "ap") + "’ means ‘" + (sex === "f" ? "daughter" : "son") + " of’. ‘ap’ becomes ‘ab’ before a vowel.", "Mae ‘ap’ yn troi’n ‘ab’ o flaen llafariad.") + (notes.length ? " " + T("Welsh forms used: ", "Ffurfiau Cymraeg: ") + esc(notes.join(", ")) + "." : "") + "</span>";
      };
      $("#sn-in").oninput = lookup; $("#sn-form").onsubmit = function (e) { e.preventDefault(); };
      $("#sn-list").onclick = function (e) { var b = e.target.closest("button"); if (b) { $("#sn-in").value = b.textContent; lookup(); } };
      ["#n-a", "#n-b", "#n-c"].forEach(function (id) { $(id).oninput = make; });
      root.querySelectorAll("[data-sex]").forEach(function (b) { b.onclick = function () { sex = b.dataset.sex; vals.a = $("#n-a").value; vals.b = $("#n-b").value; vals.c = $("#n-c").value; render(); }; });
      lookup(); make();
    };
  }

  /* ================= Which figure are you? ================= */
  if (kind === "hero") {
    var H = { i: 0, tally: {} };
    render = function () {
      if (H.i >= P.HQ.length) {
        var best = null, bn = -1; Object.keys(P.HEROES).forEach(function (k) { var n = H.tally[k] || 0; if (n > bn) { bn = n; best = k; } });
        var h = P.HEROES[best], share = T("I am " + h[4] + " (“" + h[0] + "”) on History of Wales. Which figure from Welsh history are you? ", "Fi yw " + h[5] + " (“" + h[1] + "”) ar Hanes Cymru. Pa ffigwr o hanes Cymru ydych chi? ") + "https://historyofwales.cymru/hero.html";
        root.innerHTML = '<div class="g-hero-card"><p class="eyebrow">' + T("You are", "Chi yw") + "</p><h2>" + esc(T(h[4], h[5])) + '</h2><p class="who">' + esc(T(h[0], h[1])) + " · " + esc(h[6]) + '</p><p class="g-ctx">' + esc(T(h[2], h[3])) + '</p></div><div class="g-row"><a class="btn solid" href="person-' + best + '.html">' + T("Read their story", "Darllen eu stori") + ' →</a><button type="button" class="btn" id="h-share">' + T("Copy to share", "Copïo i’w rannu") + '</button><button type="button" class="btn" id="h-again">' + T("Start again", "Dechrau eto") + "</button></div>";
        var b = $("#h-share"); b.onclick = function () { copy(b, share); };
        $("#h-again").onclick = function () { H = { i: 0, tally: {} }; render(); };
        return;
      }
      var q = P.HQ[H.i];
      root.innerHTML = '<div class="q-top"><span>' + T("Question", "Cwestiwn") + " " + (H.i + 1) + " / " + P.HQ.length + "</span></div><h2>" + esc(T(q[0], q[1])) + '</h2><div class="g-opts">' + q[2].map(function (a, i) { return '<button type="button" data-i="' + i + '">' + esc(T(a[0], a[1])) + "</button>"; }).join("") + "</div>";
      root.querySelectorAll(".g-opts button").forEach(function (b) { b.onclick = function () { var k = q[2][+b.dataset.i][2]; H.tally[k] = (H.tally[k] || 0) + 1; H.i++; render(); var f = root.querySelector(".g-opts button"); if (f) f.focus({ preventScroll: true }); }; });
    };
  }

  /* ================= Word pairs ================= */
  if (kind === "pairs") {
    var WORDS = [["draig", "dragon", "draig"], ["castell", "castle", "castell"], ["mynydd", "mountain", "mynydd"], ["môr", "sea", "môr"], ["afon", "river", "afon"], ["llyfr", "book", "llyfr"], ["brenin", "king", "brenin"], ["cân", "song", "cân"], ["telyn", "harp", "telyn"], ["glo", "coal", "glo"], ["llechen", "slate", "llechen"], ["eglwys", "church", "eglwys"], ["pont", "bridge", "pont"], ["ysgol", "school", "ysgol"], ["calon", "heart", "calon"], ["haul", "sun", "haul"], ["lleuad", "moon", "lleuad"], ["coeden", "tree", "coeden"], ["ci", "dog", "ci"], ["cath", "cat", "cath"], ["bara", "bread", "bara"], ["dŵr", "water", "dŵr"], ["tywysog", "prince", "tywysog"], ["bardd", "poet", "bardd"], ["cleddyf", "sword", "cleddyf"], ["llong", "ship", "llong"], ["tân", "fire", "tân"], ["seren", "star", "seren"]];
    var PIC = { dragon: "🐉", castle: "🏰", mountain: "⛰️", sea: "🌊", river: "🏞️", book: "📖", king: "👑", song: "🎵", harp: "🪕", coal: "⚫", slate: "◼️", church: "⛪", bridge: "🌉", school: "🏫", heart: "❤️", sun: "☀️", moon: "🌙", tree: "🌳", dog: "🐕", cat: "🐈", bread: "🍞", water: "💧", prince: "🤴", poet: "✍️", sword: "🗡️", ship: "⛵", fire: "🔥", star: "⭐" };
    var S = null;
    var deal = function () { var pick = shuffle(WORDS).slice(0, 8), cards = []; pick.forEach(function (w, i) { cards.push({ p: i, cy: 1, t: w[0] }); cards.push({ p: i, cy: 0, t: w[1] }); }); S = { cards: shuffle(cards), up: [], done: {}, moves: 0, lock: false }; };
    deal();
    render = function () {
      var all = Object.keys(S.done).length === 8;
      root.innerHTML = '<div class="q-top"><span>' + T("Pairs found", "Parau a gafwyd") + " " + Object.keys(S.done).length + " / 8</span><span>" + T("Turns", "Troeon") + " " + S.moves + '</span></div><div class="pairs">' + S.cards.map(function (c, i) {
        var up = S.up.indexOf(i) >= 0 || S.done[c.p];
        return '<button type="button" class="pair' + (up ? " up" : "") + (S.done[c.p] ? " done" : "") + '" data-i="' + i + '" aria-label="' + (up ? esc(c.t) : T("Card", "Cerdyn") + " " + (i + 1)) + '"><span class="bk">C</span><span class="ft' + (c.cy ? " cy" : "") + '">' + (c.cy ? esc(c.t) : "<span style=\"position:static;display:block;font-size:1.6em\">" + (PIC[c.t] || "") + "</span>" + (cy() ? "" : esc(c.t))) + "</span></button>";
      }).join("") + "</div>" + (all ? '<div class="g-result"><h2>' + T("Da iawn! All eight pairs in " + S.moves + " turns.", "Da iawn! Pob un o’r wyth pâr mewn " + S.moves + " tro.") + '</h2><div class="g-row"><button type="button" class="btn solid" id="p-again">' + T("Play again with new words", "Chwarae eto â geiriau newydd") + "</button></div></div>" : '<p class="g-note">' + T("Gold cards are Welsh words. Find the picture that matches each one.", "Geiriau Cymraeg yw’r cardiau aur. Dewch o hyd i’r llun sy’n cyfateb i bob un.") + "</p>");
      root.querySelectorAll(".pair").forEach(function (b) {
        b.onclick = function () {
          var i = +b.dataset.i, c = S.cards[i]; if (S.lock || S.done[c.p] || S.up.indexOf(i) >= 0) return;
          S.up.push(i); b.classList.add("up"); b.setAttribute("aria-label", c.t);
          if (S.up.length === 2) {
            S.moves++; var a = S.cards[S.up[0]], bb = S.cards[S.up[1]];
            if (a.p === bb.p) { S.done[a.p] = 1; S.up = []; if (Object.keys(S.done).length === 8 && HC()) HC().flag("pairs"); setTimeout(render, 450); }
            else { S.lock = true; setTimeout(function () { S.up = []; S.lock = false; render(); }, 950); }
          }
        };
      });
      var ag = $("#p-again"); if (ag) ag.onclick = function () { deal(); render(); };
    };
  }

  if (render) { render(); d.addEventListener("hc-lang", render); }
})();
