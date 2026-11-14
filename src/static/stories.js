// Long reads (stories.html): filter by subject, age and reading time (November 2026).
// build.py writes every card with data-subj, data-era and data-time, and the three rows of chips (story_filters()).
// One choice per row; the rows combine. The choice goes in the address (?subject=…&age=…&time=…) so a filtered list can be shared.
(function () {
  var box = document.getElementById("sf"), grid = document.getElementById("s-all");
  if (!box || !grid) return;
  var d = document.documentElement, cy = d.classList.contains("cy");
  var cards = [].slice.call(grid.querySelectorAll(".s-card")), lead = grid.querySelector(".s-card.lead");
  var GROUPS = ["subject", "age", "time"], pick = { subject: "", age: "", time: "" };
  var count = document.getElementById("sf-count"), clear = document.getElementById("sf-clear"), none = document.getElementById("sf-none");

  function fits(c, g, v) {
    if (!v) return true;
    if (g === "subject") return (" " + c.dataset.subj + " ").indexOf(" " + v + " ") >= 0;
    if (g === "age") return c.dataset.era === v;
    return c.dataset.time === v;
  }
  function fitsAll(c, skip) { return GROUPS.every(function (g) { return g === skip || fits(c, g, pick[g]); }); }

  function paint(first) {
    var shown = 0, any = GROUPS.some(function (g) { return pick[g]; });
    cards.forEach(function (c) { var on = fitsAll(c); c.hidden = !on; if (on) { shown++; if (!first) c.classList.add("in"); } });  // cards that come back skip the fade-in
    // the big first card only when nothing is chosen: a filtered list reads best as even rows
    if (lead) lead.classList.toggle("lead", !any);
    // each chip shows how many long reads it would leave, given the other two rows
    [].forEach.call(box.querySelectorAll(".chip[data-f]"), function (b) {
      var g = b.dataset.f, v = b.dataset.v;
      b.setAttribute("aria-pressed", String(pick[g] === v));
      var n = b.querySelector(".n");
      if (n) { var k = cards.filter(function (c) { return fitsAll(c, g) && fits(c, g, v); }).length; n.textContent = k; b.classList.toggle("zero", !k); }
    });
    count.textContent = any ? (cy ? shown + " o " + cards.length + " erthygl" : shown + " of " + cards.length + " long reads") : (cy ? cards.length + " erthygl" : cards.length + " long reads");
    clear.hidden = !any;
    none.hidden = shown > 0;
    var q = GROUPS.filter(function (g) { return pick[g]; }).map(function (g) { return g + "=" + encodeURIComponent(pick[g]); }).join("&");
    if (history.replaceState) history.replaceState(null, "", location.pathname + (q ? "?" + q : "") + location.hash);
  }

  // keep a swiped row where it was and bring the chosen chip into view (the same as the timeline and the map)
  function show(row) {
    var on = row.querySelector('[aria-pressed="true"]');
    if (on && row.scrollWidth > row.clientWidth) { var l = on.offsetLeft - row.offsetLeft, r = l + on.offsetWidth; if (l < row.scrollLeft || r > row.scrollLeft + row.clientWidth) row.scrollLeft = Math.max(0, l - 24); }
  }

  box.addEventListener("click", function (ev) {
    var b = ev.target.closest(".chip[data-f]");
    if (b) {
      var g = b.dataset.f;
      pick[g] = pick[g] === b.dataset.v ? "" : b.dataset.v;  // a second tap on a chosen chip takes it off
      paint(); show(b.parentNode);
      if (window.goatcounter && goatcounter.count) try { goatcounter.count({ path: "stories-filter-" + g + "-" + (pick[g] || "all"), event: true }); } catch (e) {}
      return;
    }
    if (ev.target.closest("#sf-clear")) { GROUPS.forEach(function (g) { pick[g] = ""; }); paint(); [].forEach.call(box.querySelectorAll(".sf-row"), function (r) { r.scrollLeft = 0; }); }
  });

  var qs = location.search.slice(1).split("&");
  qs.forEach(function (kv) {
    var p = kv.split("="), g = p[0], v = "";
    try { v = decodeURIComponent(p[1] || "").replace(/[^\w-]/g, ""); } catch (e) {}
    if (v && GROUPS.indexOf(g) >= 0 && box.querySelector('.chip[data-f="' + g + '"][data-v="' + v + '"]')) pick[g] = v;
  });
  box.hidden = false;
  paint(true);
  [].forEach.call(box.querySelectorAll(".sf-row"), show);
})();
