// Saints of Wales pages: the map of the llannau, the llan name decoder and today's saint.
(function () {
  var d = document.documentElement;
  function cy() { return d.classList.contains("cy"); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function bi(en, cyT) { return en === cyT ? esc(en) : '<span class="l-en" lang="en">' + esc(en) + '</span><span class="l-cy" lang="cy">' + esc(cyT) + "</span>"; }

  // ---------- the map ----------
  var dots = [].slice.call(document.querySelectorAll(".sm-dot"));
  var card = document.getElementById("sm-card");
  var pick = document.getElementById("sm-saint");
  var NAMES = {};
  if (pick) [].forEach.call(pick.querySelectorAll("option"), function (o) { if (o.value) NAMES[o.value] = o.textContent.split(" / "); });
  var LINKS = window.LLDEC ? window.LLDEC.s : null;

  function saintLink(id) {
    var n = NAMES[id] || [id, id];
    var href = LINKS && LINKS[id] ? LINKS[id][2] : "#s-" + id;
    return '<a href="' + href + '">' + bi(n[0], n[1] || n[0]) + "</a>";
  }

  function showDot(g) {
    dots.forEach(function (x) { x.classList.remove("sel"); });
    g.classList.add("sel");
    var ids = g.dataset.s.split(" ");
    card.style.setProperty("--c", g.style.getPropertyValue("--c"));
    card.innerHTML = '<p class="eyebrow">' + bi("Llan", "Llan") + "</p><h2>" + esc(g.dataset.n) + "</h2>" + (g.dataset.en ? '<p class="en l-en" lang="en">' + esc(g.dataset.en) + "</p>" : "") +
      "<p>" + bi("Named after, or linked with:", "Wedi’i henwi ar ôl, neu’n gysylltiedig â:") + "</p><ul>" +
      ids.map(function (id) { return "<li>" + saintLink(id) + " →</li>"; }).join("") + "</ul>";
  }

  function showSaint(id) {
    dots.forEach(function (x) {
      var on = !id || x.dataset.s.split(" ").indexOf(id) >= 0;
      x.classList.toggle("dim", !on && !!id);
      x.classList.toggle("hit", on && !!id);
      x.classList.remove("sel");
    });
    if (!id) {
      dots.forEach(function (x) { if (x.dataset.base === "dim") x.classList.add("dim"); });
      card.innerHTML = '<p class="muted">' + bi("Tap a dot to see whose llan it is.", "Tapiwch ddot i weld llan pwy yw hi.") + "</p>";
      return;
    }
    var mine = dots.filter(function (x) { return x.dataset.s.split(" ").indexOf(id) >= 0; });
    if (mine[0]) card.style.setProperty("--c", mine[0].style.getPropertyValue("--c"));
    card.innerHTML = '<p class="eyebrow">' + bi(mine.length + (mine.length === 1 ? " place" : " places"), mine.length + " o leoedd") + "</p><h2>" + saintLink(id) + "</h2><ul>" +
      mine.map(function (x) { return "<li>" + esc(x.dataset.n) + (x.dataset.en ? ' <span class="en l-en" lang="en">· ' + esc(x.dataset.en) + "</span>" : "") + "</li>"; }).join("") + "</ul>";
  }

  dots.forEach(function (g) {
    if (g.classList.contains("dim")) g.dataset.base = "dim";
    g.addEventListener("click", function () { showDot(g); });
    g.addEventListener("keydown", function (ev) { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); showDot(g); } });
  });
  if (pick) pick.addEventListener("change", function () { showSaint(pick.value); });

  // ---------- the llan decoder ----------
  var form = document.getElementById("ll-dec");
  if (form && window.LLDEC) {
    var K = window.LLDEC.k, S = window.LLDEC.s, O = window.LLDEC.o;
    var out = document.getElementById("ll-out"), inp = document.getElementById("ll-in");
    var keys = Object.keys(K), okeys = Object.keys(O);
    function norm(s) { return s.toLowerCase().replace(/[’'`\s-]/g, "").replace(/[âêîôûŵŷ]/g, function (c) { return "aeiouwy"["âêîôûŵŷ".indexOf(c)]; }); }
    function find(list, q) { for (var i = 0; i < list.length; i++) if (norm(list[i]) === q) return list[i]; return null; }
    // undo the soft mutation after "llan", giving the likely first letters of the name
    function unmutate(rest) {
      var r = rest.toLowerCase(), cap = function (s) { return s.charAt(0).toUpperCase() + s.slice(1); };
      if (/^dd/.test(r)) return ["D" + r.slice(2)];
      if (/^ll/.test(r)) return [cap(r)];
      if (/^rh/.test(r)) return [cap(r)];
      if (/^b/.test(r)) return ["P" + r.slice(1)];
      if (/^g/.test(r)) return ["C" + r.slice(1)];
      if (/^d/.test(r)) return ["T" + r.slice(1)];
      if (/^f/.test(r)) return ["M" + r.slice(1), "B" + r.slice(1)];
      if (/^l/.test(r)) return ["Ll" + r.slice(1)];
      if (/^r/.test(r)) return ["Rh" + r.slice(1)];
      if (/^[aeiouwy]/.test(r)) return ["G" + r, cap(r)];
      return [cap(r)];
    }
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var raw = inp.value.trim();
      if (!raw) return;
      var q = norm(raw);
      var hit = find(keys, q), other = find(okeys, q), html;
      if (hit) {
        var ids = K[hit];
        html = '<p class="eq">' + esc(hit) + "</p>" + ids.map(function (id) {
          var s = S[id];
          return "<p>" + bi("The llan of ", "Llan ") + '<a href="' + s[2] + '"><b>' + bi(s[0], s[1]) + "</b></a> · " + bi(s[3], s[4]) + "</p>";
        }).join("");
      } else if (other) {
        var o = O[other];
        html = '<p class="eq">' + esc(other) + " = Llan + <em>" + esc(o[0]) + "</em></p><p>" + bi(o[1], o[2]) + "</p>";
      } else if (/^llan/i.test(raw) && raw.length > 5) {
        var rest = raw.replace(/^llan[-\s]?/i, "").split(/[\s-]/)[0];
        var g = unmutate(rest);
        html = '<p class="eq">' + esc(raw) + " = Llan + <em>" + esc(g.join(" / ")) + "</em>?</p><p>" +
          bi("This one is not on our map yet. Take away the softening that follows llan and the saint is probably " + g.join(" or ") + ".",
             "Nid yw hon ar ein map eto. Tynnwch y treiglad sy’n dilyn llan a’r sant, fwy na thebyg, yw " + g.join(" neu ") + ".") + "</p>";
      } else {
        html = "<p>" + bi("Try a name that begins with Llan, such as Llandeilo, Llanelli or Llangollen.", "Rhowch gynnig ar enw sy’n dechrau â Llan, fel Llandeilo, Llanelli neu Langollen.") + "</p>";
      }
      out.innerHTML = html;
    });
  }

  // ---------- today's saint ----------
  var box = document.getElementById("today-saint");
  if (box && window.FEASTS && FEASTS.length) {
    var now = new Date(), m = now.getMonth() + 1, day = now.getDate();
    var today = FEASTS.filter(function (f) { return f[0] === m && f[1] === day; });
    var next = FEASTS.filter(function (f) { return f[0] > m || (f[0] === m && f[1] > day); })[0] || FEASTS[0];
    var MON = [["January", "Ionawr"], ["February", "Chwefror"], ["March", "Mawrth"], ["April", "Ebrill"], ["May", "Mai"], ["June", "Mehefin"], ["July", "Gorffennaf"], ["August", "Awst"], ["September", "Medi"], ["October", "Hydref"], ["November", "Tachwedd"], ["December", "Rhagfyr"]];
    var f = today[0] || next;
    var when = f[1] + " " + MON[f[0] - 1][0], whenCy = f[1] + " " + MON[f[0] - 1][1];
    box.innerHTML = '<p class="eyebrow">' + (today.length ? bi("Today, " + when + ", is the feast of", "Heddiw, " + whenCy + ", yw gŵyl") : bi("The next saint’s day: " + when, "Dydd gŵyl nesaf y saint: " + whenCy)) + "</p>" +
      today.concat(today.length ? [] : [f]).map(function (x) { return '<h2><a href="' + x[4] + '">' + bi(x[2], x[3]) + "</a></h2><p>" + bi(x[5], x[6]) + "</p>"; }).join("") +
      '<p><a class="go" href="#cal">' + bi("See the whole calendar", "Gweld y calendr cyfan") + " →</a></p>";
    [].forEach.call(document.querySelectorAll('.cal li[data-m="' + m + '"][data-d="' + day + '"]'), function (li) { li.classList.add("today"); });
  }
})();
