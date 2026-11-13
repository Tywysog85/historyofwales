/* Welsh word of the day and the play buttons for Welsh words and phrases.
   build.py writes _site/welsh.js as "var CYW = {...};" followed by this file.
   CYW.W: words [id, word, sound guide, meaning, example cy, example en, note en, note cy, link]
   CYW.ORDER: word indexes for ordinary days; CYW.DAYS: "MM-DD" -> word index for fixed days
   CYW.AUDIO: recordings present in audio/ (file names without .mp3) */
(function () {
  "use strict";
  var W = CYW.W, AUDIO = {};
  (CYW.AUDIO || []).forEach(function (a) { AUDIO[a] = 1; });
  var canSpeak = "speechSynthesis" in window;
  var MON_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  var MON_CY = ["Ionawr", "Chwefror", "Mawrth", "Ebrill", "Mai", "Mehefin", "Gorffennaf", "Awst", "Medi", "Hydref", "Tachwedd", "Rhagfyr"];
  var DAY_EN = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  var DAY_CY = ["Dydd Sul", "Dydd Llun", "Dydd Mawrth", "Dydd Mercher", "Dydd Iau", "Dydd Gwener", "Dydd Sadwrn"];

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function bi(en, cy, tag) { tag = tag || "span"; return "<" + tag + ' class="l-en" lang="en">' + en + "</" + tag + "><" + tag + ' class="l-cy" lang="cy">' + cy + "</" + tag + ">"; }
  function slug(w) { return w.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, ""); }

  /* ---------- sound: a real recording if there is one, otherwise the device's voice ---------- */
  function welshVoice() {
    var vs = speechSynthesis.getVoices();
    return vs.filter(function (v) { return /^cy/i.test(v.lang); })[0] || null;
  }
  function englishVoice() {
    var vs = speechSynthesis.getVoices();
    return vs.filter(function (v) { return /^en-GB/i.test(v.lang); })[0] || vs.filter(function (v) { return /^en/i.test(v.lang); })[0] || null;
  }
  function speak(text, guide) {
    if (!canSpeak) return;
    var cy = welshVoice(), u;
    if (cy) { u = new SpeechSynthesisUtterance(text); u.voice = cy; u.lang = cy.lang; }
    else {
      /* no Welsh voice on this device: read the English sound guide instead */
      u = new SpeechSynthesisUtterance(guide.toLowerCase().replace(/…/g, "").replace(/-/g, " ").replace(/\bkh/g, "k").replace(/\bhl/g, "l"));
      var en = englishVoice(); if (en) { u.voice = en; u.lang = en.lang; }
    }
    u.rate = 0.8; speechSynthesis.cancel(); speechSynthesis.speak(u);
  }
  var current = null;
  function play(text, guide, btn) {
    var s = slug(text);
    if (current) { try { current.pause(); } catch (e) {} current = null; }
    if (btn) { btn.classList.add("on"); setTimeout(function () { btn.classList.remove("on"); }, 1400); }
    if (AUDIO[s]) {
      var a = new Audio("audio/" + s + ".mp3"); current = a;
      var p = a.play(); if (p && p.catch) p.catch(function () { speak(text, guide); });
      return;
    }
    speak(text, guide);
  }
  window.CYW_PLAY = play;
  if (canSpeak) { try { speechSynthesis.getVoices(); } catch (e) {} }
  function hasSound(text) { return canSpeak || !!AUDIO[slug(text)]; }
  function hearBtn(text, guide, label) {
    if (!hasSound(text)) return "";
    return '<button type="button" class="hear" data-hear="' + esc(text) + '" data-guide="' + esc(guide) + '" aria-label="' + esc("Hear / Clywed: " + text) + '">'
      + '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4z" fill="currentColor"/><path d="M16 8.5a5 5 0 0 1 0 7M18.5 6a8.5 8.5 0 0 1 0 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
      + (label ? bi("Hear it", "Gwrando") : "") + "</button>";
  }
  document.addEventListener("click", function (ev) {
    var b = ev.target.closest && ev.target.closest("[data-hear]");
    if (b) play(b.getAttribute("data-hear"), b.getAttribute("data-guide") || "", b);
  });
  /* static buttons on welsh.html are hidden until we know the device can play something */
  [].forEach.call(document.querySelectorAll("[data-hear]"), function (b) { if (!hasSound(b.getAttribute("data-hear"))) b.hidden = true; });

  /* ---------- the word of the day ---------- */
  function two(n) { return (n < 10 ? "0" : "") + n; }
  function dayOf(back) {
    var d = new Date(); d.setHours(12, 0, 0, 0); d.setDate(d.getDate() - back);
    var key = two(d.getMonth() + 1) + "-" + two(d.getDate());
    var n = Math.round(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 864e5);
    var i = CYW.DAYS[key] != null ? CYW.DAYS[key] : CYW.ORDER[((n % CYW.ORDER.length) + CYW.ORDER.length) % CYW.ORDER.length];
    return { i: i, d: d };
  }
  function dateLabel(d, back) {
    var en = back === 0 ? "Today" : back === 1 ? "Yesterday" : DAY_EN[d.getDay()];
    var cy = back === 0 ? "Heddiw" : back === 1 ? "Ddoe" : DAY_CY[d.getDay()];
    return bi(en + ", " + d.getDate() + " " + MON_EN[d.getMonth()], cy + ", " + d.getDate() + " " + MON_CY[d.getMonth()]);
  }
  function card(back) {
    var x = dayOf(back), w = W[x.i];
    // the whole card is one link to the history behind the word (see "Whole cards are links" in SKILLS.md); the buttons stay their own
    var more = w[8] ? '<a class="wl" href="' + esc(w[8]) + '">' + bi("The history behind the word " + esc(w[1]), "Yr hanes y tu ôl i’r gair " + esc(w[1])) + "</a>" : "";
    return '<div class="wotd-top"><p class="eyebrow"><b>' + bi("Word of the day", "Gair y dydd") + "</b> · " + dateLabel(x.d, back) + "</p>"
      + '<div class="wotd-nav"><button type="button" data-wotd-go="1"' + (back >= 6 ? " disabled" : "") + ' aria-label="' + esc("Previous day / Diwrnod blaenorol") + '">‹</button>'
      + '<button type="button" data-wotd-go="-1"' + (back <= 0 ? " disabled" : "") + ' aria-label="' + esc("Next day / Diwrnod nesaf") + '">›</button></div></div>'
      + '<div class="wotd-main"><div class="wotd-word"><p class="wotd-w" lang="cy">' + esc(w[1]) + "</p>"
      + '<p class="wotd-say"><span>' + esc(w[2]) + "</span>" + hearBtn(w[1], w[2], true) + "</p>"
      + '<p class="wotd-mean">' + bi(esc(w[3]), "Saesneg: " + esc(w[3])) + "</p></div>"
      + '<div class="wotd-body"><figure class="wotd-ex"><blockquote lang="cy">' + esc(w[4]) + '</blockquote><figcaption lang="en">' + esc(w[5]) + "</figcaption></figure>"
      + "<p>" + bi(esc(w[6]), esc(w[7])) + "</p>" + more + "</div></div>";
  }
  [].forEach.call(document.querySelectorAll("[data-wotd]"), function (el) {
    var back = 0;
    function draw() { el.innerHTML = card(back); el.classList.toggle("wl-card", !!el.querySelector("a.wl")); el.classList.remove("in"); void el.offsetWidth; el.classList.add("in"); }
    el.addEventListener("click", function (ev) {
      var b = ev.target.closest("[data-wotd-go]"); if (!b || b.disabled) return;
      back = Math.max(0, Math.min(6, back + +b.getAttribute("data-wotd-go"))); draw();
    });
    draw();
  });
  /* the last seven days, as a list (welsh.html) */
  [].forEach.call(document.querySelectorAll("[data-wotd-week]"), function (el) {
    var h = "";
    for (var k = 1; k <= 7; k++) {
      var x = dayOf(k), w = W[x.i];
      h += '<li><span class="eyebrow">' + dateLabel(x.d, k) + '</span><b lang="cy">' + esc(w[1]) + '</b><span class="say">' + esc(w[2]) + hearBtn(w[1], w[2], false) + "</span><span>" + bi(esc(w[3]), "Saesneg: " + esc(w[3])) + "</span></li>";
    }
    el.innerHTML = h;
  });
})();
