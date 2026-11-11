// Photo gallery: category filter and the big-picture viewer with credits.
(function () {
  var d = document.documentElement;
  function cy() { return d.classList.contains("cy"); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  // ---------- categories ----------
  var chips = [].slice.call(document.querySelectorAll(".g-chip"));
  var secs = [].slice.call(document.querySelectorAll(".g-sec"));
  function show(cat, scroll) {
    if (cat !== "all" && !secs.some(function (s) { return s.dataset.cat === cat; })) cat = "all";
    chips.forEach(function (c) { var on = c.dataset.cat === cat; c.classList.toggle("on", on); c.setAttribute("aria-pressed", on); if (on && c.scrollIntoView) c.scrollIntoView({ block: "nearest", inline: "nearest" }); });
    secs.forEach(function (s) { s.hidden = cat !== "all" && s.dataset.cat !== cat; });
    if (scroll) {
      var bar = document.querySelector(".g-secs");
      if (bar) window.scrollTo({ top: bar.getBoundingClientRect().top + window.scrollY - 130, behavior: "smooth" });
    }
  }
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      var cat = c.dataset.cat;
      show(cat, true);
      try { history.replaceState(null, "", cat === "all" ? location.pathname : "#" + cat); } catch (e) {}
    });
  });
  if (location.hash) show(location.hash.slice(1), false);

  // ---------- viewer ----------
  var box = document.getElementById("g-box");
  if (!box || !box.showModal) return;
  var img = box.querySelector(".g-stage img");
  var cur = -1, list = [];
  function visible() { return [].slice.call(document.querySelectorAll(".g-sec:not([hidden]) .g-item")); }
  function open(i) {
    cur = (i + list.length) % list.length;
    var a = list[cur];
    var b = a.querySelector(".cap b");
    img.classList.add("ld");
    img.onload = function () { img.classList.remove("ld"); };
    img.src = a.dataset.full;
    img.alt = a.dataset.wen;
    box.querySelector("h3").innerHTML = b ? b.innerHTML : "";
    box.querySelector(".g-what").innerHTML = '<span class="l-en" lang="en">' + esc(a.dataset.wen) + '</span><span class="l-cy" lang="cy">' + esc(a.dataset.wcy) + "</span>";
    box.querySelector(".g-cred").innerHTML = (cy() ? "Llun: " : "Picture: ") + esc(a.dataset.by) + ', <a href="' + esc(a.dataset.licu) + '" target="_blank" rel="noopener license">' + esc(a.dataset.lic) + '</a>, <a href="' + esc(a.dataset.file) + '" target="_blank" rel="noopener">Wikimedia Commons</a>';
    box.querySelector(".g-count").textContent = (cur + 1) + " / " + list.length;
    var go = box.querySelector(".g-go");
    go.hidden = !a.dataset.go;
    if (a.dataset.go) go.href = a.dataset.go;
    // load the next picture early so it shows at once
    var nx = list[(cur + 1) % list.length];
    if (nx) (new Image()).src = nx.dataset.full;
  }
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest(".g-item");
    if (!a || ev.ctrlKey || ev.metaKey || ev.shiftKey) return;
    ev.preventDefault();
    list = visible();
    if (!box.open) box.showModal();
    open(list.indexOf(a));
  });
  box.querySelector(".g-prev").addEventListener("click", function () { open(cur - 1); });
  box.querySelector(".g-next").addEventListener("click", function () { open(cur + 1); });
  box.querySelector("[data-x]").addEventListener("click", function () { box.close(); });
  box.addEventListener("click", function (ev) { if (ev.target === box || ev.target.classList.contains("g-stage")) box.close(); });
  box.addEventListener("keydown", function (ev) {
    if (ev.key === "ArrowRight") { ev.preventDefault(); open(cur + 1); }
    else if (ev.key === "ArrowLeft") { ev.preventDefault(); open(cur - 1); }
  });
  box.addEventListener("close", function () { img.removeAttribute("src"); var a = list[cur]; if (a) a.focus({ preventScroll: true }); });
  // swipe on phones
  var x0 = null, y0 = 0;
  var stage = box.querySelector(".g-stage");
  stage.addEventListener("touchstart", function (ev) { x0 = ev.touches[0].clientX; y0 = ev.touches[0].clientY; }, { passive: true });
  stage.addEventListener("touchend", function (ev) {
    if (x0 === null) return;
    var dx = ev.changedTouches[0].clientX - x0, dy = ev.changedTouches[0].clientY - y0;
    x0 = null;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) open(cur + (dx < 0 ? 1 : -1));
    else if (dy > 90 && Math.abs(dy) > Math.abs(dx) * 1.5) box.close();
  }, { passive: true });
})();
