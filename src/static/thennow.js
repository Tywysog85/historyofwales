// Then and now: drag between an old picture and a photograph of the same place today (src/thennow.py).
// Without this script each pair shows side by side; with it, the two pictures sit on top of each other and a handle
// wipes between them. The whole picture takes the drag (mouse, pen or finger) with pointer capture, and
// touch-action: pan-y keeps an up-and-down swipe scrolling the page. The range input stays for the keyboard and
// screen readers; arrow keys, Page Up/Down, Home and End move it.
(function () {
  var d = document.documentElement;
  var still = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  function cy() { return d.classList.contains("cy"); }

  function setup(fig) {
    var stage = fig.querySelector(".tn-stage"), range = fig.querySelector(".tn-range");
    if (!stage || !range) return;
    fig.classList.add("on");
    var pos = 50, drag = false;
    function words(p) {
      var en = p > 92 ? "All then" : p < 8 ? "All now" : Math.round(p) + "% then, " + Math.round(100 - p) + "% now";
      var w = p > 92 ? "Y cyfan yn ddoe" : p < 8 ? "Y cyfan yn heddiw" : Math.round(p) + "% ddoe, " + Math.round(100 - p) + "% heddiw";
      return cy() ? w : en;
    }
    function set(p, glide) {
      pos = Math.max(0, Math.min(100, p));
      stage.classList.toggle("glide", !!glide && !still);
      stage.style.setProperty("--pos", pos + "%");
      range.value = pos;
      range.setAttribute("aria-valuetext", words(pos));
      fig.classList.toggle("at-then", pos > 92);
      fig.classList.toggle("at-now", pos < 8);
    }
    function fromX(x) {
      var r = stage.getBoundingClientRect();
      return ((x - r.left) / r.width) * 100;
    }
    stage.addEventListener("pointerdown", function (ev) {
      if (ev.button > 0) return;
      drag = true;
      fig.classList.add("used");
      try { stage.setPointerCapture(ev.pointerId); } catch (e) {}
      set(fromX(ev.clientX), ev.pointerType !== "touch");
    });
    stage.addEventListener("pointermove", function (ev) { if (drag) set(fromX(ev.clientX), false); });
    function end() { drag = false; }
    stage.addEventListener("pointerup", end);
    stage.addEventListener("pointercancel", end);
    stage.addEventListener("lostpointercapture", end);
    range.addEventListener("input", function () { fig.classList.add("used"); set(+range.value, false); });
    range.addEventListener("keydown", function (ev) {
      var k = ev.key, step = { ArrowLeft: -5, ArrowDown: -5, ArrowRight: 5, ArrowUp: 5, PageDown: -25, PageUp: 25 }[k];
      if (step != null) set(pos + step, true);
      else if (k === "Home") set(0, true);
      else if (k === "End") set(100, true);
      else return;
      ev.preventDefault();
      fig.classList.add("used");
    });
    [].forEach.call(fig.querySelectorAll("[data-tn-go]"), function (b) {
      b.addEventListener("click", function () { fig.classList.add("used"); set(+b.getAttribute("data-tn-go"), true); });
    });
    set(50, false);
    // a small nudge the first time the pair comes into view, so people see that it moves
    if (!still && "IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (en) {
          if (!en.isIntersecting) return;
          io.disconnect();
          setTimeout(function () { if (!fig.classList.contains("used")) set(62, true); }, 500);
          setTimeout(function () { if (!fig.classList.contains("used")) set(50, true); }, 1300);
        });
      }, { threshold: 0.6 });
      io.observe(stage);
    }
    // the Welsh / English switch changes the words read out
    new MutationObserver(function () { range.setAttribute("aria-valuetext", words(pos)); }).observe(d, { attributes: true, attributeFilter: ["class"] });
  }
  [].forEach.call(document.querySelectorAll(".tn"), setup);

  // the gallery page: filter chips
  var chips = [].slice.call(document.querySelectorAll(".tn-chip"));
  var cards = [].slice.call(document.querySelectorAll(".tn-card"));
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      var cat = c.getAttribute("data-cat");
      chips.forEach(function (x) { var on = x === c; x.classList.toggle("on", on); x.setAttribute("aria-pressed", on); });
      cards.forEach(function (k) { k.hidden = cat !== "all" && k.getAttribute("data-cat") !== cat; });
    });
  });
})();
