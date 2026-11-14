/* Long reads read aloud (src/listen.py makes the Listen box; tools/make_listen.py makes the sound).
   No sound is fetched until the reader presses Play. The place they got to is remembered on this device, so the
   big button carries on from there next time. Speed 0.8× to 2×, jumps of 15 and 30 seconds, section by section
   (the marks are the times each heading starts), a "listen from here" button beside every heading, a small bar at
   the foot of the screen while the box is out of sight, and the lock-screen controls of phones (Media Session). */
(function () {
  var d = document, box = d.querySelector(".listen");
  if (!box) return;
  var cy = d.documentElement.classList.contains("cy") || box.lang === "cy";
  var T = function (en, c) { return cy ? c : en; };
  var id = box.dataset.id, lang = box.lang || (cy ? "cy" : "en"), total = parseFloat(box.dataset.secs) || 0;
  var marks = (box.dataset.marks || "").split(",").filter(Boolean).map(parseFloat);
  var heads = Array.prototype.slice.call(d.querySelectorAll(".prose h2[id]"));
  if (heads.length !== marks.length) heads = [];             // the words changed since the sound was made: no jumping to headings
  var starts = [0].concat(marks);
  var KEY = "hc-listen:" + id + ":" + lang, RATES = [0.8, 1, 1.15, 1.3, 1.5, 1.75, 2];
  var $ = function (s) { return box.querySelector(s); };
  var go = $(".ls-go"), more = $(".ls-more"), seek = $(".ls-seek"), time = $(".ls-time"), sec = $(".ls-sec"), rateB = $(".ls-rate"), resume = $(".ls-resume");
  var audio = null, dragging = false, lastSave = 0, counted = false, mini = null;
  function store(k, v) { try { if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) {} }
  function load(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  var rate = parseFloat(load("hc-listen-rate")) || 1;
  if (RATES.indexOf(rate) < 0) rate = 1;
  rateB.textContent = String(rate).replace(".", cy ? "," : ".") + "×";

  function clock(s) {
    s = Math.max(0, Math.round(s || 0));
    var h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), x = s % 60;
    return (h ? h + ":" + (m < 10 ? "0" : "") : "") + m + ":" + (x < 10 ? "0" : "") + x;
  }
  function headName(i) {
    if (i <= 0) return T("Introduction", "Cyflwyniad");
    var h = heads[i - 1];
    if (!h) return T("Section ", "Adran ") + (i + 1);
    return (h.firstChild && h.firstChild.nodeType === 3 ? h.firstChild.nodeValue : h.textContent.replace(/#$/, "")).trim();
  }
  function secAt(t) { var i = 0; for (var k = 0; k < starts.length; k++) if (t + 0.5 >= starts[k]) i = k; return i; }

  var dl = $(".ls-dl"); if (dl) dl.href = box.dataset.src.split("?")[0];  // set here, so the link checker never looks for a file made later
  // section ticks along the bar
  var ticks = $(".ls-ticks");
  if (total && marks.length && ticks) marks.forEach(function (m) { var i = d.createElement("i"); i.style.left = (m / total * 100).toFixed(2) + "%"; ticks.appendChild(i); });

  // carry on from where they stopped
  var saved = parseFloat(load(KEY)) || 0;
  if (saved > 15 && saved < total - 10) {
    $(".ls-len").textContent = T("Carry on from ", "Parhau o ") + clock(saved) + " · " + clock(total);
    resume.textContent = T("From the start", "O’r dechrau");
    resume.hidden = false;
  } else saved = 0;

  function ensure() {
    if (audio) return audio;
    audio = new Audio();
    audio.preload = "auto";
    audio.src = box.dataset.src;
    audio.playbackRate = rate;
    audio.addEventListener("timeupdate", tick);
    audio.addEventListener("play", state); audio.addEventListener("pause", state);
    audio.addEventListener("ended", function () { store(KEY, null); state(); });
    audio.addEventListener("error", function () {
      box.classList.add("err"); box.querySelector(".ls-txt small").setAttribute("data-err", T("the sound could not be loaded", "methwyd llwytho’r sain"));
    });
    more.hidden = false;
    addHere(); makeMini(); session();
    return audio;
  }
  function play(from) {
    var a = ensure();
    if (typeof from === "number") {
      var set = function () { try { a.currentTime = from; } catch (e) {} };
      if (a.readyState >= 1) set(); else a.addEventListener("loadedmetadata", set, { once: true });
    }
    var p = a.play(); if (p && p.catch) p.catch(function () {});
    if (!counted) {
      counted = true;
      try { if (window.goatcounter && goatcounter.count) goatcounter.count({ path: "listen-" + id + "-" + lang, title: "Listen: " + id + " (" + lang + ")", event: true }); } catch (e) {}
    }
  }
  function toggle() { if (audio && !audio.paused) audio.pause(); else play(audio ? undefined : saved || 0); }
  function state() {
    var on = audio && !audio.paused;
    box.classList.toggle("playing", !!on);
    go.setAttribute("aria-label", on ? T("Pause", "Oedi") : T("Listen to this long read", "Gwrando ar yr erthygl hon"));
    if (mini) { mini.classList.toggle("playing", !!on); mini.querySelector("button").setAttribute("aria-label", on ? T("Pause", "Oedi") : T("Play", "Chwarae")); }
    if (audio) store(KEY, audio.ended ? null : String(Math.floor(audio.currentTime)));
    if ("mediaSession" in navigator) navigator.mediaSession.playbackState = on ? "playing" : "paused";
    spy();
  }
  function tick() {
    var t = audio.currentTime, dur = audio.duration && isFinite(audio.duration) ? audio.duration : total;
    if (!dragging) seek.value = t;
    seek.max = dur;
    time.textContent = clock(t) + " / " + clock(dur);
    var i = secAt(t), name = headName(i);
    if (sec.textContent !== name) sec.textContent = name;
    if (mini) { mini.querySelector("small").textContent = clock(t) + " / " + clock(dur) + " · " + name; mini.querySelector(".ls-mbar i").style.width = (t / dur * 100).toFixed(2) + "%"; }
    if (Math.abs(t - lastSave) > 5) { lastSave = t; store(KEY, String(Math.floor(t))); }
  }
  function jump(t) { var a = ensure(); a.currentTime = Math.max(0, Math.min((a.duration || total) - 1, t)); tick(); }

  go.addEventListener("click", toggle);
  resume.addEventListener("click", function () { resume.hidden = true; saved = 0; store(KEY, null); play(0); });
  $(".ls-back").addEventListener("click", function () { jump(audio.currentTime - 15); });
  $(".ls-fwd").addEventListener("click", function () { jump(audio.currentTime + 30); });
  $(".ls-prev").addEventListener("click", function () { var i = secAt(audio.currentTime); jump(audio.currentTime - starts[i] > 4 ? starts[i] : starts[Math.max(0, i - 1)]); });
  $(".ls-next").addEventListener("click", function () { var i = secAt(audio.currentTime); if (i + 1 < starts.length) jump(starts[i + 1]); });
  rateB.addEventListener("click", function () {
    rate = RATES[(RATES.indexOf(rate) + 1) % RATES.length];
    if (audio) audio.playbackRate = rate;
    rateB.textContent = String(rate).replace(".", cy ? "," : ".") + "×";
    store("hc-listen-rate", String(rate));
  });
  seek.addEventListener("input", function () { dragging = true; time.textContent = clock(seek.value) + " / " + clock(audio ? audio.duration || total : total); });
  seek.addEventListener("change", function () { dragging = false; jump(parseFloat(seek.value)); });

  // a small play button beside every heading
  function addHere() {
    heads.forEach(function (h, i) {
      var b = d.createElement("button");
      b.type = "button"; b.className = "ls-here no-print";
      b.setAttribute("aria-label", T("Listen from here", "Gwrando o fan hyn"));
      b.title = T("Listen from here", "Gwrando o fan hyn");
      b.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg>';
      b.addEventListener("click", function (e) { e.preventDefault(); play(); jump(marks[i]); });
      var link = h.querySelector(".h-link");
      h.insertBefore(b, link || null);
    });
  }

  // the small bar at the foot of the screen, while the Listen box is out of sight
  var boxSeen = true;
  function makeMini() {
    mini = d.createElement("div");
    mini.className = "ls-mini no-print"; mini.hidden = true; mini.lang = lang;
    mini.innerHTML = '<button type="button"><svg viewBox="0 0 24 24" aria-hidden="true"><path class="i-play" d="M8 5.5v13l11-6.5z"/><path class="i-pause" d="M7 5h4v14H7zM13 5h4v14h-4z"/></svg></button>'
      + '<a href="#"><b></b><small></small></a><span class="ls-mbar"><i></i></span>';
    mini.querySelector("b").textContent = box.dataset.title;
    mini.querySelector("button").addEventListener("click", toggle);
    mini.querySelector("a").addEventListener("click", function (e) { e.preventDefault(); box.scrollIntoView({ behavior: "smooth", block: "center" }); });
    d.body.appendChild(mini);
    if ("IntersectionObserver" in window) new IntersectionObserver(function (es) { boxSeen = es[0].isIntersecting; spy(); }).observe(box);
  }
  function spy() {
    if (!mini) return;
    var show = !boxSeen && audio && (!audio.paused || audio.currentTime > 0) && !audio.ended;
    mini.hidden = !show;
    d.body.classList.toggle("ls-on", !!show);
  }

  // lock screen and headphone buttons
  function session() {
    if (!("mediaSession" in navigator) || !window.MediaMetadata) return;
    var og = d.querySelector('meta[property="og:image"]');
    navigator.mediaSession.metadata = new MediaMetadata({ title: box.dataset.title, artist: T("History of Wales", "Hanes Cymru"), album: T("Long reads", "Erthyglau"),
      artwork: og ? [{ src: og.content, sizes: "1200x630", type: "image/jpeg" }] : [] });
    var h = function (a, f) { try { navigator.mediaSession.setActionHandler(a, f); } catch (e) {} };
    h("play", function () { play(); }); h("pause", function () { audio.pause(); });
    h("seekbackward", function () { jump(audio.currentTime - 15); }); h("seekforward", function () { jump(audio.currentTime + 30); });
    h("previoustrack", function () { $(".ls-prev").click(); }); h("nexttrack", function () { $(".ls-next").click(); });
    h("seekto", function (e) { jump(e.seekTime); });
  }
  addEventListener("pagehide", function () { if (audio && !audio.ended) store(KEY, String(Math.floor(audio.currentTime))); });
})();
