"""A history page for every town and village: town-<slug>.html (Ifan, 14 November 2026).

The towns themselves (names, meaning, a one-line history, links, map position) are in src/ref_towns.py and
src/towns_more.py; the fuller story of each is in src/town_long.py. A town gets its own page once it has a story there;
until then it is only a card on towns.html.

Each page gathers what the site already knows about the place, by distance from the town: historic places with pages of
their own, castles from the castles map, battles, timeline events that name the town, people born or living there, and
the nearest other towns. The name is decoded word by word by the same decoder as towns.html (src/placenames.js).

build.py calls setup(globals()) once, then pages() for the HTML and search_items() for search.json.
"""
import math
import re

import data as D
import town_long as TL
import town_wiki as TWW

g = {}  # build.py's helpers (bi, e, page, hero, section ...), filled by setup()
ROWS = []   # every town on towns.html (refpages.town_rows)
BY_ID = {}  # "town-aberystwyth" -> row


def setup(build_globals):
    g.update(build_globals)
    ROWS[:] = g["RP"].town_rows()
    BY_ID.clear()
    BY_ID.update({r["id"]: r for r in ROWS})
    unknown = set(TL.LONG) - set(BY_ID)
    assert not unknown, f"src/town_long.py: no such town in towns.html: {sorted(unknown)}"
    # each town page's picture (src/pictures.py): its own photo, else the photo of a historic place in or by the town
    PX = g["PX"]
    for r in pages_rows():
        path = r["id"] + ".html"
        if path in PX.PAGE:
            continue
        own = TL.PICS.get(r["id"])
        if own:
            PX.PAGE[path] = own
            continue
        for d, p in near_places(r, 6):
            if ("place-" + p["id"]) in g["GP"].GALLERY:
                PX.PAGE[path] = "g:place-" + p["id"]
                break


def has_page(tid):
    return tid in TL.LONG


def pages_rows():
    return [r for r in ROWS if has_page(r["id"])]


def href(r):
    return r["id"] + ".html"


def km(lat1, lon1, lat2, lon2):
    return math.hypot((lat1 - lat2) * 111.2, (lon1 - lon2) * 111.2 * math.cos(math.radians((lat1 + lat2) / 2)))


def near_places(r, within):
    out = [(km(r["lat"], r["lon"], p["lat"], p["lon"]), p) for p in D.PLACES if p.get("lat") is not None]
    return sorted([x for x in out if x[0] <= within], key=lambda x: x[0])


def near_castles(r, within, places):
    """Castles from the castles map (src/castles_data.json) near the town, leaving out any that have a place page shown already."""
    out = []
    for c in g["CASTLES"]:
        d = km(r["lat"], r["lon"], c["lat"], c["lon"])
        if d > within:
            continue
        if any(km(c["lat"], c["lon"], p["lat"], p["lon"]) < 0.6 for _, p in places):
            continue
        out.append((d, c))
    return sorted(out, key=lambda x: x[0])


def near_battles(r, within):
    out = []
    for b in g["RP"].BT.BATTLES:
        if not b.get("geo"):
            continue
        d = km(r["lat"], r["lon"], b["geo"][0], b["geo"][1])
        if d <= within:
            out.append((d, b))
    return sorted(out, key=lambda x: x[0])


def _names(r):
    """The names the town is known by, for finding it in other text: English, Welsh and any extra forms in src/town_long.py."""
    ns = {r["en"].replace(" (Pembrokeshire)", ""), r["cy"]} | set(TL.ALSO.get(r["id"], ()))
    return [n for n in ns if len(n) > 3]


def _named(text, names):
    return any(re.search(r"(?<![\w’'-])" + re.escape(n) + r"(?![\w-])", text) for n in names)


def town_events(r):
    """Timeline events that name the town, or whose place is in the town (2 km)."""
    names = _names(r)
    place_ids = {p["id"] for d, p in near_places(r, 2)}
    out = []
    for ev in D.EVENTS:
        if ev[10] in place_ids or _named(ev[5] + " " + ev[7], names):
            out.append(ev)
    return out


BORN_RE = r"\b(?:born|grew up|brought up|raised)\b[^.;]{0,40}?\b(?:in|at)\s+"


def town_people(r):
    """People of the town: those listed in src/town_long.py, then anyone whose short life says they were born there."""
    slugs = list(TL.PEOPLE.get(r["id"], [])) + [h[7:-5] for h in r["see"] if h.startswith("person-") and h.endswith(".html")]
    out = []
    for s in slugs:
        if s in g["PERSON"] and g["PERSON"][s] not in out:
            out.append(g["PERSON"][s])
    names = _names(r)
    pat = re.compile(BORN_RE + "(?:" + "|".join(re.escape(n) for n in sorted(names, key=len, reverse=True)) + r")(?![\w-])")
    for p in D.PEOPLE:
        if p in out:
            continue
        long_en = (g["L"].PEOPLE_LONG.get(p[0]) or D.PEOPLE_EXTRA_LONG.get(p[0]) or ([], []))[0]
        if pat.search(p[7]) or any(pat.search(x) for x in long_en[:2]):
            out.append(p)
    return out[:12]


def _dist(d):
    return f"{d:.0f} km" if d >= 1.5 else bi("in the town", "yn y dref")


def bi(en, cy, *a, **k):
    return g["bi"](en, cy, *a, **k)


def e(s):
    return g["e"](s)


def town_page(r, i, rows):
    section, hero, page = g["section"], g["hero"], g["page"]
    SITE = g["SITE"]
    tid, la, la_cy = r["id"], r["la"], r["laCy"]
    rec = TL.LONG[tid]
    era = rec.get("era", "medieval")
    two = r["en"] != r["cy"]
    en_name = r["en"].replace(" (Pembrokeshire)", "")
    crumbs = (f'<a href="index.html">{SITE}</a> / <a href="towns.html">{bi("Towns and villages", "Trefi a phentrefi")}</a> / '
              f'<a href="towns.html#tw-{g["RP"].slug(la)}">{bi(la, la_cy)}</a>')
    h_en = f"{en_name} · {r['cy']}" if two else en_name
    h_cy = f"{r['cy']} · {en_name}" if two else r["cy"]
    top = hero(era, crumbs, "castle", la, la_cy, h_en, h_cy, r["hEn"], r["hCy"])

    osm = f'https://www.openstreetmap.org/?mlat={r["lat"]:.4f}&mlon={r["lon"]:.4f}#map=13/{r["lat"]:.4f}/{r["lon"]:.4f}'
    meta = (f'<div class="person-meta"><a href="towns.html#tw-{g["RP"].slug(la)}">{bi(la, la_cy)}</a>'
            + (f'<span>{bi("In Welsh", "Yn Gymraeg")}: <b lang="cy">{e(r["cy"])}</b></span>' if two else "")
            + f'<span>{r["lat"]:.3f}° N, {abs(r["lon"]):.3f}° W</span><a href="{osm}" target="_blank" rel="noopener">{bi("Open in a map", "Agor mewn map")} ↗</a></div>')

    # the name, decoded: the meaning in words, then the decoder's word-by-word parts (filled in by the script below)
    names = [r["cy"]] + ([en_name] if two and not _english_only(r) else [])
    name_box = (f'<div class="tn-name"><p class="eyebrow">{bi("What the name means", "Ystyr yr enw")}</p>'
                f'<p class="tn-mean"><b lang="cy">{e(r["cy"])}</b>: {bi(r["mEn"], r["mCy"])}</p>'
                + "".join(f'<div class="tn-parts" data-tn-name="{e(n)}"></div>' for n in names)
                + f'<p class="tn-more"><a href="towns.html#tw-in">{bi("Decode any other Welsh place name", "Datgodio unrhyw enw lle arall")} →</a></p></div>')

    body = g["paras"](rec["en"], rec["cy"])
    chips = g["RP"].link_chips(r["see"], g["HAVE"]) if r["see"] else ""
    main = top + section(meta + name_box + body + chips + _map(r), top=True)
    then_now = g["TN"].place_block(None, page=href(r))  # an old picture beside today's (src/thennow.py)
    if then_now:
        main += section(then_now, "Then and now", "Ddoe a heddiw")

    places = near_places(r, 16)[:8]
    if places:
        tiles = "".join(_place_tile(d, p) for d, p in places)
        main += section(f'<div class="era-places">{tiles}</div>', "Historic places nearby", "Lleoedd hanesyddol gerllaw")
    castles = near_castles(r, 10, places)[:8]
    if castles:
        main += section('<ul class="tn-list">' + "".join(
            f'<li><a href="castles.html#castle-{c["q"]}"><b>{bi(c["en"], c["cy"] or c["en"])}</b><small>{_dist(d)}{(" · " + e(c["y"])) if c.get("y") else ""}</small></a></li>'
            for d, c in castles) + "</ul>", "Castles nearby", "Cestyll gerllaw")

    ppl = town_people(r)
    if ppl:
        main += section(f'<div class="people">{"".join(g["plaque"](p) for p in ppl)}</div>', f"People of {en_name}", f"Pobl {r['cy']}")

    evs = town_events(r)
    if evs:
        main += section(f'<ol class="era-events">{"".join(g["event_li"](ev) for ev in evs[:12])}</ol>', "On the timeline", "Ar y llinell amser")

    bts = near_battles(r, 12)[:6]
    if bts:
        main += section('<ul class="tn-list">' + "".join(
            f'<li><a href="battles.html#b-{b["id"]}"><b>{bi(b["en"], b["cy"])}</b><small>{e(str(b["year"]) if b["year"] > 0 else str(-b["year"]) + " BC")} · {_dist(d)}</small></a></li>'
            for d, b in bts) + "</ul>", "Battles fought nearby", "Brwydrau gerllaw")

    nxt = sorted([x for x in rows if x is not r], key=lambda x: km(r["lat"], r["lon"], x["lat"], x["lon"]))[:6]
    if nxt:
        main += section('<ul class="tn-list">' + "".join(
            f'<li><a href="{href(x)}"><b>{bi(x["en"].replace(" (Pembrokeshire)", ""), x["cy"])}</b><small>{km(r["lat"], r["lon"], x["lat"], x["lon"]):.0f} km</small></a></li>'
            for x in nxt) + "</ul>", "Towns nearby", "Trefi gerllaw")

    share = f'<p class="share no-print"><button type="button" class="btn" data-copy="{href(r)}">{bi("Copy link to share", "Copïo dolen i’w rhannu")}</button></p>'
    main += section(share + g["further"](f"town:{tid}", TWW.wiki(r["en"]))
                    + f'<div class="pager"><a class="btn" href="towns.html">← {bi("All towns and villages", "Pob tref a phentref")}</a>'
                    + f'<a class="btn solid" href="towns.html#tw-{g["RP"].slug(la)}">{bi(f"More in {la}", f"Mwy yn {la_cy}")} →</a></div>')

    title = f"{en_name} ({r['cy']}): history and name" if two else f"{en_name}: history and name"
    desc = f"The history of {en_name}" + (f" ({r['cy']})" if two else "") + f", {la}: what the name means, its story, and the historic places and people nearby. " + r["hEn"]
    ld = {"@context": "https://schema.org", "@type": "Place", "name": en_name, "alternateName": r["cy"], "description": r["hEn"],
          "geo": {"@type": "GeoCoordinates", "latitude": r["lat"], "longitude": r["lon"]},
          "containedInPlace": {"@type": "AdministrativeArea", "name": la}, "sameAs": g["WIKI"] + TWW.wiki(r["en"])}
    return page(href(r), f"{title} · History of Wales", desc, main, era=era, ld=ld, og_type="place", active="reference.html",
                track=f"town:{tid[5:]}", extra=g["PN_SCRIPT"] + TN_JS + (g["TN_JS"] if then_now else ""))


def _english_only(r):
    """True when the English name is simply the Welsh one spelt the English way (Conway), so it adds nothing to decode."""
    return False


def _place_tile(d, p):
    return (f'<a href="place-{p["id"]}.html" data-era="{p["era"]}">{g["tile_pic"](g["card_pic"](f"place-{p['id']}.html"), p["ill"])}'
            f'<span><b>{bi(p["en"], p["cy"])}</b><span>{_dist(d)} · {e(p["year"])}</span></span></a>')


def _map(r):
    """A small map of Wales with the town marked, linking to the towns map."""
    x, y = g["RP"].wales_xy(r["lat"], r["lon"])
    return (f'<a class="tn-map" href="towns.html#{r["id"]}" aria-label="{e(r["en"])}: on the map of towns">'
            f'<svg viewBox="-20 -20 640 711" aria-hidden="true"><path class="land" d="{g["geo"]["outline"]}"/>'
            f'<circle class="h" cx="{x:.1f}" cy="{y:.1f}" r="26"/><circle class="d" cx="{x:.1f}" cy="{y:.1f}" r="9"/></svg>'
            f'<span>{bi("On the map of towns", "Ar fap y trefi")} →</span></a>')


def pages(have=()):
    g["RP"]._titles()  # the names of the pages a town links to (src/refpages.py)
    g["HAVE"] = set(have) | {href(r) for r in pages_rows()} | set(g["RP"].PAGE_NAMES)
    rows = pages_rows()
    return {href(r): town_page(r, i, rows) for i, r in enumerate(rows)}


def search_items():
    return [dict(k="town", t=r["cy"], c=r["cy"], u=href(r), y=[r["en"].replace(" (Pembrokeshire)", "") if r["en"] != r["cy"] else r["la"], r["laCy"]],
                 b=[r["mEn"].capitalize() + ". " + r["hEn"], r["mCy"].capitalize() + ". " + r["hCy"]], e="saints", a=r["en"]) for r in pages_rows()]


# The name's parts, from the shared decoder. Each [data-tn-name] box gets one list of parts.
TN_JS = r"""<script>(function(){var cy=function(){return document.documentElement.classList.contains("cy")};
var esc=function(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})};
function run(){var P=window.PN;if(!P)return;[].slice.call(document.querySelectorAll("[data-tn-name]")).forEach(function(box){var n=box.getAttribute("data-tn-name"),r=P.decode(n),c=cy();
box.innerHTML='<p class="tn-n" lang="cy">'+esc(n)+'</p><div class="tw-words-out">'+r.words.map(function(w){return'<ul class="tw-parts">'+w.map(function(p){var l=P.label(p,c),eng=l.kind==="e"||l.kind==="n";
return'<li class="'+(l.kind==="u"?"un":eng?"en":"")+'"><b>'+esc(l.t)+"</b><span>"+(eng?"<em>"+(c?"Saesneg":"English")+":</em> ":"")+esc(l.mean)+"</span>"+(l.note?"<small>"+esc(l.note)+"</small>":"")+"</li>"}).join("")+"</ul>"}).join("")+"</div>"})}
if(window.PN)run();else document.addEventListener("pn:ready",run)})();</script>
"""

CSS = """
.tn-name{background:var(--slate);border:1px solid var(--line);border-radius:16px;padding:1.1rem 1.2rem;margin:0 0 1.4rem;max-width:50rem}
.tn-name .eyebrow{margin:0 0 .35rem}
.tn-mean{font-size:1.08rem;margin:0 0 .6rem}
.tn-mean b{font-family:var(--f-display);font-weight:600}
.tn-parts:empty{display:none}
.tn-n{font:600 .82rem var(--f-ui,inherit);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:.7rem 0 .3rem}
.tn-more{margin:.7rem 0 0;font-size:.92rem}
.tn-list{list-style:none;padding:0;margin:0;display:grid;gap:.5rem;grid-template-columns:repeat(auto-fill,minmax(min(100%,240px),1fr))}
.tn-list a{display:grid;gap:.15rem;padding:.75rem 1rem;border:1px solid var(--line);border-radius:14px;background:var(--card);color:inherit;text-decoration:none;height:100%;box-sizing:border-box;min-height:44px}
.tn-list a:hover,.tn-list a:focus-visible{border-color:color-mix(in srgb,var(--gold) 55%,var(--line))}
.tn-list small{color:var(--muted);font-size:.88rem}
.tn-map{display:flex;align-items:center;gap:1rem;max-width:22rem;margin:1.4rem 0 0;color:inherit;text-decoration:none}
.tn-map svg{width:7.5rem;height:auto;flex:none}
.tn-map .land{fill:color-mix(in srgb,var(--gold) 14%,var(--slate));stroke:color-mix(in srgb,var(--gold) 45%,var(--line));stroke-width:2}
.tn-map .h{fill:color-mix(in srgb,var(--red,#c8102e) 30%,transparent)}
.tn-map .d{fill:var(--red,#c8102e);stroke:#fff;stroke-width:3}
.tn-map span{font-weight:600}
.tn-map:hover span,.tn-map:focus-visible span{text-decoration:underline}
"""
