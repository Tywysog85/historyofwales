/* The weekly quiz (weekly-quiz.html). Ten questions a week, the same for everyone, from quiz/<Monday>.json (written by
   build.py from src/quiz_weeks.json). One go a week counts; past weeks can be played for practice.
   The leaderboard is a small Cloudflare Worker (worker/ in the repo). Its address is on #wq-root as data-lb; without
   it the quiz still works and keeps the score on this device only. Only a nickname, the score, the time and a random
   code made here (so one go a week is counted) are ever sent. */
(function () {
  var d = document, root = d.getElementById("wq-root"); if (!root) return;
  var board = d.getElementById("wq-board"), past = d.getElementById("wq-past");
  var LB = root.getAttribute("data-lb") || "";
  var cy = function () { return d.documentElement.classList.contains("cy"); };
  var T = function (en, c) { return cy() ? c : en; };
  var L = function (pair) { return pair ? (cy() ? pair[1] : pair[0]) : ""; };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var MON_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  var MON_CY = ["Ionawr", "Chwefror", "Mawrth", "Ebrill", "Mai", "Mehefin", "Gorffennaf", "Awst", "Medi", "Hydref", "Tachwedd", "Rhagfyr"];
  var KIND = {
    year: ["This week in Welsh history", "Yr wythnos hon yn hanes Cymru"], what: ["This week in Welsh history", "Yr wythnos hon yn hanes Cymru"],
    born: ["This week in Welsh history", "Yr wythnos hon yn hanes Cymru"], feast: ["This week in Welsh history", "Yr wythnos hon yn hanes Cymru"],
    who: ["A figure from history", "Ffigwr o hanes"], pic: ["Name the place", "Enwch y lle"], clue: ["Where in Wales?", "Ble yng Nghymru?"],
    word: ["A Welsh word", "Gair Cymraeg"], first: ["Which came first?", "Pa un ddaeth gyntaf?"], tale: ["A tale from Wales", "Chwedl o Gymru"]
  };

  /* ---------- this device: one go a week, the nickname, and a random code for the leaderboard ---------- */
  var KEY = "hc-weekly";
  function load() { try { var s = JSON.parse(localStorage.getItem(KEY) || "{}"); s.w = s.w || {}; return s; } catch (e) { return { w: {} }; } }
  function save(s) { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) {} }
  var S = load();
  if (!S.pid) { S.pid = (crypto && crypto.getRandomValues ? Array.prototype.map.call(crypto.getRandomValues(new Uint8Array(12)), function (b) { return ("0" + b.toString(16)).slice(-2); }).join("") : String(Math.random()).slice(2) + Date.now()); save(S); }

  function pad(n) { return ("0" + n).slice(-2); }
  function iso(dt) { return dt.getFullYear() + "-" + pad(dt.getMonth() + 1) + "-" + pad(dt.getDate()); }
  function mondayOf(dt) { var x = new Date(dt.getFullYear(), dt.getMonth(), dt.getDate()); x.setDate(x.getDate() - ((x.getDay() + 6) % 7)); return x; }
  function parse(k) { var p = k.split("-"); return new Date(+p[0], +p[1] - 1, +p[2]); }
  function dayLabel(dt, year) { return dt.getDate() + " " + (cy() ? MON_CY : MON_EN)[dt.getMonth()] + (year ? " " + dt.getFullYear() : ""); }
  function weekLabel(k) {
    var a = parse(k), b = new Date(a.getFullYear(), a.getMonth(), a.getDate() + 6);
    return a.getMonth() === b.getMonth() ? a.getDate() + "–" + dayLabel(b, true) : dayLabel(a, a.getFullYear() !== b.getFullYear()) + " – " + dayLabel(b, true);
  }
  function clock(s) { s = Math.max(0, Math.round(s)); return Math.floor(s / 60) + ":" + pad(s % 60); }
  function count(ev) { try { if (window.goatcounter && goatcounter.count) goatcounter.count({ path: ev, title: "Weekly quiz", event: true }); } catch (e) {} }

  var THIS = iso(mondayOf(new Date())), INDEX = [], WEEK = null, PRACTICE = false;

  function get(url) { return fetch(url, { cache: "no-cache" }).then(function (r) { if (!r.ok) throw r.status; return r.json(); }); }

  get("quiz/index.json").then(function (ix) {
    INDEX = ix.weeks || [];
    if (!LB && ix.lb) LB = ix.lb;
    var have = INDEX.filter(function (w) { return w[0] <= THIS; });
    if (!have.length) throw "none";
    var k = have[have.length - 1][0];
    if (k !== THIS) THIS = k;   /* a clock that is wrong, or a week not yet published: the newest there is */
    return get("quiz/" + k + ".json");
  }).then(function (w) { WEEK = w; start(); renderPast(); }).catch(function () {
    root.innerHTML = '<p class="wq-msg">' + T("The quiz could not be loaded. Check your connection and try again.", "Methwyd llwytho’r cwis. Gwiriwch eich cysylltiad a rhowch gynnig arall arni.") + "</p>";
  });

  /* ---------- the opening card ---------- */
  function start() {
    var st = S.w[WEEK.wk];
    PRACTICE = false;
    if (st && st.done) return results();
    root.innerHTML = '<div class="wq-card wq-open"><p class="eyebrow">' + T("Week ", "Wythnos ") + WEEK.n + " · " + esc(weekLabel(WEEK.wk)) + "</p>" +
      "<h2>" + T("This week’s quiz", "Cwis yr wythnos hon") + "</h2>" +
      '<ul class="wq-facts"><li><b>10</b>' + T("questions", "cwestiwn") + "</li><li><b>3</b>" + T("on this week’s anniversaries", "ar ben-blwyddi’r wythnos") + "</li><li><b>1</b>" + T("go each week", "cynnig yr wythnos") + "</li></ul>" +
      "<p>" + T("Your score counts first; if two players tie, the quicker one goes higher. The clock only runs while a question is waiting for your answer.",
        "Eich sgôr sy’n cyfrif gyntaf; os bydd dau’n gyfartal, yr un cyflymaf sy’n uwch. Dim ond tra bo cwestiwn yn aros am eich ateb y mae’r cloc yn rhedeg.") + "</p>" +
      '<p><button type="button" class="btn solid wq-go">' + T("Start the quiz", "Dechrau’r cwis") + " →</button></p></div>";
    root.querySelector(".wq-go").onclick = function () { begin(false); };
    showBoard(WEEK.wk, null);
  }

  /* ---------- playing ---------- */
  var G = null;
  function begin(practice, week) {
    PRACTICE = practice;
    G = { w: week || WEEK, i: 0, ans: [], secs: 0, t0: 0 };
    count(practice ? "weekly-practice" : "weekly-start");
    if (!practice) board.hidden = true;
    ask();
    root.scrollIntoView({ block: "start", behavior: "smooth" });
  }
  function ask() {
    var q = G.w.qs[G.i], n = G.w.qs.length, score = G.ans.filter(function (a, i) { return a === G.w.qs[i].a; }).length;
    var eyebrow = L(KIND[q.k]) + (q.tw ? " · " + esc(L(q.tw)) : "");
    var pic = q.ph ? '<figure class="wq-ph"><img src="' + esc(q.ph) + '" alt="' + T("A photograph of the place to name", "Llun o’r lle i’w enwi") + '" loading="eager" decoding="async">' +
      (q.cr ? '<figcaption>' + T("Photo: ", "Llun: ") + esc(q.cr[0]) + (q.cr[1] ? ", " + (q.cr[2] ? '<a href="' + esc(q.cr[2]) + '" target="_blank" rel="noopener license">' + esc(q.cr[1]) + "</a>" : esc(q.cr[1])) : "") + "</figcaption>" : "") + "</figure>" : "";
    root.innerHTML = '<div class="wq-card"><div class="q-top"><span>' + T("Question ", "Cwestiwn ") + (G.i + 1) + " / " + n + "</span><span>" + T("Score ", "Sgôr ") + score +
      (PRACTICE ? " · " + T("practice", "ymarfer") : "") + '</span></div><div class="q-bar"><i style="width:' + (G.i / n * 100) + '%"></i></div>' +
      '<p class="eyebrow wq-kind">' + eyebrow + "</p>" + pic + '<h3 class="wq-h">' + esc(L(q.h)) + "</h3>" +
      (q.t ? '<p class="wq-t">' + esc(L(q.t)) + "</p>" : "") + (q.c ? '<p class="wq-c">' + esc(L(q.c)) + "</p>" : "") +
      '<div class="answers wq-ans">' + q.o.map(function (o, i) { return '<button type="button" data-a="' + i + '">' + esc(L(o)) + "</button>"; }).join("") + "</div>" +
      '<div class="wq-fb" aria-live="polite"></div></div>';
    G.t0 = performance.now();
    var bs = root.querySelectorAll(".wq-ans button");
    Array.prototype.forEach.call(bs, function (b) { b.onclick = function () { answer(+b.dataset.a); }; });
    if (G.i > 0 && bs[0]) bs[0].focus({ preventScroll: true });
    if (G.i > 0 && root.getBoundingClientRect().top < 0) root.scrollIntoView({ block: "start", behavior: "smooth" });
  }
  function answer(a) {
    var q = G.w.qs[G.i], ok = a === q.a;
    G.secs += (performance.now() - G.t0) / 1000;
    G.ans.push(a);
    Array.prototype.forEach.call(root.querySelectorAll(".wq-ans button"), function (x, i) { x.disabled = true; if (i === q.a) x.classList.add("right"); else if (i === a) x.classList.add("wrong"); });
    var last = G.i === G.w.qs.length - 1;
    var fb = root.querySelector(".wq-fb");
    fb.innerHTML = '<div class="wq-x' + (q.p ? " has-pic" : "") + '">' + (q.p ? '<img src="' + esc(q.p) + '" alt="" loading="lazy" decoding="async">' : "") +
      "<div><p><b>" + (ok ? T("Correct.", "Cywir.") : T("Not quite. ", "Dim cweit. ") + T("The answer is ", "Yr ateb yw ") + esc(L(q.o[q.a])) + ".") + "</b></p><p>" + esc(L(q.x)) + "</p></div></div>" +
      '<p><button type="button" class="btn solid wq-next">' + (last ? T("See my score", "Gweld fy sgôr") : T("Next question", "Cwestiwn nesaf")) + " →</button></p>";
    var nx = fb.querySelector(".wq-next"); nx.focus({ preventScroll: true });
    try { nx.scrollIntoView({ block: "nearest", behavior: "smooth" }); } catch (e) {}
    nx.onclick = function () {
      G.i++;
      if (G.i < G.w.qs.length) { ask(); return; }
      finish();
    };
  }
  function scoreOf(w, ans) { return ans.filter(function (a, i) { return a === w.qs[i].a; }).length; }
  function finish() {
    var score = scoreOf(G.w, G.ans), secs = Math.round(G.secs);
    if (window.HC) { HC.flag("weekly"); if (score === 10) HC.flag("weekly10"); }
    count((PRACTICE ? "weekly-practice-" : "weekly-score-") + score);
    if (PRACTICE) return results(G.w, { ans: G.ans, secs: secs, score: score, done: true });
    S = load(); S.w[G.w.wk] = { ans: G.ans, secs: secs, score: score, done: true }; save(S);
    results();
  }

  /* ---------- the result, the share line and the leaderboard ---------- */
  function squares(w, ans) { return ans.map(function (a, i) { return a === w.qs[i].a ? "🟩" : "🟥"; }).join(""); }
  function untilMonday() {
    var now = new Date(), next = parse(THIS); next.setDate(next.getDate() + 7);
    var h = Math.max(1, Math.round((next - now) / 36e5));
    return h >= 48 ? T("in " + Math.round(h / 24) + " days", "ymhen " + Math.round(h / 24) + " diwrnod") : T("in " + h + " hours", "ymhen " + h + " awr");
  }
  function results(w, st) {
    var practice = !!w;
    w = w || WEEK; st = st || S.w[w.wk];
    var s = st.score, msg = s === 10 ? T("A perfect ten. Pencampwr!", "Deg perffaith. Pencampwr!") : s >= 8 ? T("Da iawn. A fine score.", "Da iawn wir. Sgôr gwych.") : s >= 5 ? T("Not bad at all. Every answer is on the site.", "Ddim yn ddrwg o gwbl. Mae pob ateb ar y wefan.") : T("A hard week. The answers below lead to the pages.", "Wythnos anodd. Mae’r atebion isod yn arwain at y tudalennau.");
    var line = (practice ? T("Practice, week ", "Ymarfer, wythnos ") + w.n : T("Week ", "Wythnos ") + w.n + " · " + esc(weekLabel(w.wk)));
    root.innerHTML = '<div class="wq-card wq-res"><p class="eyebrow">' + line + "</p>" +
      '<p class="q-score">' + s + "<small>/" + w.qs.length + "</small></p>" +
      '<p class="wq-sq" aria-label="' + T(s + " right out of " + w.qs.length, s + " yn gywir allan o " + w.qs.length) + '">' + squares(w, st.ans) + "</p>" +
      "<h3>" + msg + "</h3><p class=\"wq-time\">" + T("Time ", "Amser ") + "<b>" + clock(st.secs) + "</b></p>" +
      '<p class="wq-btns"><button type="button" class="btn solid wq-share">' + T("Share my score", "Rhannu fy sgôr") + "</button>" +
      (practice ? ' <button type="button" class="btn wq-back">' + T("Back to this week", "Yn ôl i’r wythnos hon") + "</button>" : "") + "</p>" +
      (!practice ? '<p class="wq-next-week">' + T("A new quiz comes out every Monday morning, the next one ", "Daw cwis newydd bob bore Llun, a’r nesaf ") + untilMonday() + ".</p>" : "") +
      (!practice && LB ? '<div class="wq-join"></div>' : "") + "</div>" + review(w, st.ans);
    root.querySelector(".wq-share").onclick = function () { share(w, st, this); };
    var bk = root.querySelector(".wq-back"); if (bk) bk.onclick = function () { start(); renderPast(); };
    if (!practice && LB) { joinForm(w, st); showBoard(w.wk, st); } else if (!practice) board.hidden = true;
  }
  function review(w, ans) {
    return '<div class="wq-review"><h3 class="sub-h">' + T("Your answers", "Eich atebion") + '</h3><ol>' + w.qs.map(function (q, i) {
      var ok = ans[i] === q.a, label = L(q.t) || L(q.h);
      return '<li class="' + (ok ? "ok" : "no") + (q.l ? " wl-card" : "") + '"><span class="m" aria-hidden="true">' + (ok ? "✓" : "✗") + '</span><div><p class="q">' + esc(label) + "</p><p>" +
        (ok ? "" : T("You said ", "Dywedoch ") + "<s>" + esc(L(q.o[ans[i]])) + "</s> · ") + "<b>" + esc(L(q.o[q.a])) + "</b></p></div>" +
        (q.l ? '<a class="wl" href="' + esc(q.l) + '">' + esc(L(q.o[q.a])) + "</a>" : "") + "</li>";
    }).join("") + "</ol></div>";
  }
  function share(w, st, btn) {
    var url = location.origin + location.pathname.replace(/[^\/]*$/, "") + "weekly-quiz.html";
    var txt = T("History of Wales weekly quiz, week ", "Cwis yr wythnos Hanes Cymru, wythnos ") + w.n + ": " + st.score + "/10 " + T("in ", "mewn ") + clock(st.secs) + "\n" + squares(w, st.ans) + "\n";
    if (navigator.share) { navigator.share({ text: txt, url: url }).catch(function () {}); return; }
    try { navigator.clipboard.writeText(txt + url).then(function () { var o = btn.textContent; btn.textContent = T("Copied, ready to paste", "Wedi copïo, yn barod i’w ludo"); setTimeout(function () { btn.textContent = o; }, 2200); }); } catch (e) {}
  }

  /* nicknames: letters (any language), numbers, spaces and - ' . _ ; no web or email addresses */
  function nickOk(n) { return /^[\p{L}\p{N}][\p{L}\p{N} '’._-]{1,23}$/u.test(n) && !/https?:|www\.|@|\.(com|net|org|uk|cymru|wales)\b/i.test(n); }
  function joinForm(w, st) {
    var box = root.querySelector(".wq-join"); if (!box) return;
    if (st.sent) { box.innerHTML = '<p class="wq-on">' + T("Your score is on the leaderboard as ", "Mae eich sgôr ar y tabl fel ") + "<b>" + esc(st.nick || S.nick || "") + "</b>.</p>"; return; }
    box.innerHTML = '<form class="wq-form" novalidate><label for="wq-nick">' + T("Put your score on this week’s leaderboard", "Rhowch eich sgôr ar dabl yr wythnos hon") + "</label>" +
      '<div class="wq-row"><input id="wq-nick" name="nick" maxlength="24" autocomplete="nickname" spellcheck="false" placeholder="' + T("A nickname", "Llysenw") + '" value="' + esc(S.nick || "") + '">' +
      '<button type="submit" class="btn solid">' + T("Add my score", "Ychwanegu fy sgôr") + "</button></div>" +
      '<p class="wq-note">' + T("Only the nickname, your score and your time are shown. No names or email addresses needed.", "Dim ond y llysenw, eich sgôr a’ch amser a ddangosir. Nid oes angen enw na chyfeiriad e-bost.") +
      ' <a href="about.html#privacy">' + T("Privacy", "Preifatrwydd") + '</a></p><p class="wq-err" aria-live="polite"></p></form>';
    var f = box.querySelector("form"), err = box.querySelector(".wq-err");
    f.onsubmit = function (ev) {
      ev.preventDefault();
      var nick = f.nick.value.trim().replace(/\s+/g, " ");
      if (!nickOk(nick)) { err.textContent = T("Use 2 to 24 letters or numbers, with no web or email address.", "Defnyddiwch 2 i 24 llythyren neu rif, heb gyfeiriad gwe nac e-bost."); f.nick.focus(); return; }
      var btn = f.querySelector("button"); btn.disabled = true; err.textContent = "";
      fetch(LB + "/score", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ week: w.wk, pid: S.pid, nick: nick, ans: st.ans, secs: st.secs }) })
        .then(function (r) { return r.json(); }).then(function (r) {
          if (r.error) {
            btn.disabled = false;
            err.textContent = r.error === "nick" ? T("Please choose another nickname.", "Dewiswch lysenw arall, os gwelwch yn dda.") :
              r.error === "week" ? T("This week’s leaderboard has closed. A new quiz is out.", "Mae tabl yr wythnos hon wedi cau. Mae cwis newydd allan.") :
              T("That didn’t go through. Try again in a moment.", "Ni weithiodd hynny. Rhowch gynnig arall arni mewn munud.");
            return;
          }
          S = load(); S.nick = nick; var s2 = S.w[w.wk] || st; s2.sent = 1; s2.nick = r.nick || nick; S.w[w.wk] = s2; save(S);
          count("weekly-leaderboard");
          joinForm(w, s2); drawBoard(w.wk, r, s2);
        }).catch(function () { btn.disabled = false; err.textContent = T("That didn’t go through. Try again in a moment.", "Ni weithiodd hynny. Rhowch gynnig arall arni mewn munud."); });
    };
  }
  function showBoard(wk, st) {
    if (!LB) { board.hidden = true; return; }
    get(LB + "/board?week=" + encodeURIComponent(wk) + "&pid=" + encodeURIComponent(S.pid)).then(function (r) { drawBoard(wk, r, st); }).catch(function () { board.hidden = true; });
  }
  function ordinal(n) { if (cy()) return String(n); var s = ["th", "st", "nd", "rd"], v = n % 100; return n + (s[(v - 20) % 10] || s[v] || s[0]); }
  function drawBoard(wk, r, st) {
    var top = r.top || [], me = r.you;
    var rows = top.map(function (x, i) {
      var mine = me && me.rank === i + 1;
      return '<li class="' + (mine ? "me" : "") + (i < 3 ? " m" + (i + 1) : "") + '"><span class="r">' + (i + 1) + '</span><span class="n">' + esc(x[0]) + '</span><span class="s">' + x[1] + "/10</span><span class=\"t\">" + clock(x[2]) + "</span></li>";
    }).join("");
    var mine = me && me.rank > top.length ? '<li class="me gap"><span class="r">' + me.rank + '</span><span class="n">' + esc(me.nick) + '</span><span class="s">' + me.score + "/10</span><span class=\"t\">" + clock(me.secs) + "</span></li>" : "";
    var players = r.players || 0;
    board.innerHTML = '<h2 class="sub-h">' + T("This week’s leaderboard", "Tabl yr wythnos hon") + "</h2>" +
      '<p class="wq-sub">' + (players ? (players === 1 ? T("1 player so far", "1 chwaraewr hyd yma") : T(players + " players so far", players + " o chwaraewyr hyd yma")) + (me ? " · " + T("you are ", "rydych yn safle ") + "<b>" + ordinal(me.rank) + "</b>" : "") : T("Nobody yet. Be the first on the board this week.", "Neb eto. Byddwch y cyntaf ar y tabl yr wythnos hon.")) + "</p>" +
      (rows ? '<ol class="wq-lb">' + rows + mine + "</ol>" : "") + (r.last && r.last.length ? lastWeek(r.last) : "");
    board.hidden = false;
  }
  function lastWeek(last) {
    return '<div class="wq-last"><p class="eyebrow">' + T("Last week’s champions", "Pencampwyr yr wythnos diwethaf") + '</p><ol>' + last.slice(0, 3).map(function (x, i) {
      return '<li><span class="r">' + ["🥇", "🥈", "🥉"][i] + '</span><span class="n">' + esc(x[0]) + '</span><span class="s">' + x[1] + "/10 · " + clock(x[2]) + "</span></li>";
    }).join("") + "</ol></div>";
  }

  /* ---------- past weeks, for practice ---------- */
  function renderPast() {
    var olds = INDEX.filter(function (w) { return w[0] < THIS; }).reverse();
    if (!olds.length) { past.hidden = true; return; }
    past.innerHTML = '<h2 class="sub-h">' + T("Quizzes from past weeks", "Cwisiau’r wythnosau a fu") + '</h2><p class="wq-sub">' + T("For practice: these don’t go on the leaderboard.", "I ymarfer: nid yw’r rhain yn mynd ar y tabl.") + '</p><ul class="wq-weeks">' +
      olds.map(function (w) { var st = S.w[w[0]]; return '<li><button type="button" data-wk="' + w[0] + '"><b>' + T("Week ", "Wythnos ") + w[1] + "</b><span>" + esc(weekLabel(w[0])) + "</span>" + (st && st.done ? "<i>" + st.score + "/10</i>" : "") + "</button></li>"; }).join("") + "</ul>";
    past.hidden = false;
    Array.prototype.forEach.call(past.querySelectorAll("button[data-wk]"), function (b) {
      b.onclick = function () { get("quiz/" + b.dataset.wk + ".json").then(function (w) { begin(true, w); }); };
    });
  }
})();
