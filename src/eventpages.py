"""A page of its own for every event on the timeline: event-<slug>.html.

build.py calls setup(globals()) once, then pages() for the HTML and search_items() for search.json.
SLUG[i] is the page name of D.EVENTS[i]; the timeline (app.js, via DATA["EVS"]), the era pages and the person and place pages
link to it through event_li().

Each page gathers what the site already knows about the event: the date, the age, the place, the people named in it,
battles and documents of the same year, long reads that tell it, the events just before and after, and where to read further.
The big moments (key events) also get a longer telling from src/events_more.py.
"""
import re
import unicodedata

import data as D
import events_more as EM

g = {}  # build.py's helpers (bi, e, page, hero, section ...), filled by setup()

MONTHS = [("January", "Ionawr"), ("February", "Chwefror"), ("March", "Mawrth"), ("April", "Ebrill"), ("May", "Mai"), ("June", "Mehefin"),
          ("July", "Gorffennaf"), ("August", "Awst"), ("September", "Medi"), ("October", "Hydref"), ("November", "Tachwedd"), ("December", "Rhagfyr")]


def _slugify(s):
    s = unicodedata.normalize("NFKD", s.replace("’", "").replace("'", "")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:70].strip("-")


def _make_slugs():
    seen, out = set(), []
    for ev in D.EVENTS:
        base = _slugify(ev[5]) or "event"
        s = base
        if s in seen:
            s = f"{base}-{abs(ev[1])}{'bc' if ev[1] < 0 else ''}"
        n = 2
        while s in seen:
            s = f"{base}-{n}"
            n += 1
        seen.add(s)
        out.append(s)
    return out


SLUG = _make_slugs()
INDEX = {ev: i for i, ev in enumerate(D.EVENTS)}


def href(ev):
    return f"event-{SLUG[INDEX[ev]]}.html"


def setup(build_globals):
    g.update(build_globals)


def bi(en, cy, *a, **k):
    return g["bi"](en, cy, *a, **k)


def e(s):
    return g["e"](s)


def date_label(ev, cy=False):
    """'20 September 1486' when the day is known, else the year label used on the timeline."""
    yl = g["year_label"](ev, cy)
    if ev[4] and ev[1] > 0 and not ev[2]:
        m, d = int(ev[4][:2]), int(ev[4][3:])
        return f"{d} {MONTHS[m - 1][1 if cy else 0]} {yl}"
    return yl


def _people(ev):
    text = ev[5] + " " + ev[7]
    out = [p for p in D.PEOPLE if re.search(r"(?<!\w)" + re.escape(p[3]) + r"(?!\w)", text)]  # whole names only: Henry V is not Henry VII
    if "Dewi" in text:
        out += [p for p in D.PEOPLE if p[0] == "dewi-sant" and p not in out]
    return out[:6]


def _battles(ev):
    BT = g["RP"].BT
    t = ev[5].lower()
    return [b for b in BT.BATTLES if b["year"] == ev[1] or (len(b["en"]) > 6 and b["en"].lower().replace("battle of ", "") in t)][:4]


def _docs(ev):
    DC = g["RP"].DC
    return [d for d in DC.DOCS if d["year"] == ev[1]][:3]


def _link_list(items):
    return '<ul class="ev-rel">' + "".join(f'<li><a href="{h}"><b>{bi(en, cy)}</b>{f"<small>{bi(sen, scy)}</small>" if sen else ""}</a></li>' for h, en, cy, sen, scy in items) + "</ul>"


def event_page(i, ev):
    bi_, section, hero, page = g["bi"], g["section"], g["hero"], g["page"]
    ERA, ERA_ART, SITE = g["ERA"], g["ERA_ART"], g["SITE"]
    eid = ev[0]
    era = ERA[eid]
    slug = SLUG[i]
    place = next((p for p in D.PLACES if p["id"] == ev[10]), None) if ev[10] else None
    people = _people(ev)

    # the date line: date, age, on this day, the place, the source
    meta = [f'<span>{bi(date_label(ev), date_label(ev, True))}</span>', f'<a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a>']
    if ev[4]:
        m, d = int(ev[4][:2]), int(ev[4][3:])
        meta.append(f'<a href="onthisday.html#d-{ev[4]}">{bi(f"On this day: {d} {MONTHS[m - 1][0]}", f"Ar y dydd hwn: {d} {MONTHS[m - 1][1]}")}</a>')
    if place:
        meta.append(f'<a href="place-{place["id"]}.html">{bi(place["en"], place["cy"])}</a>')
    meta.append(f'<a href="timeline.html#ev-{i}">{bi("On the timeline", "Ar y llinell amser")}</a>')
    top = '<div class="person-meta">' + "".join(meta) + "</div>"

    # a picture: the place's photo, else the first person's
    fig = ""
    if place and g["PH"].PLACE_PHOTOS.get(place["id"]):
        fig = g["photo_fig"](g["PH"].PLACE_PHOTOS.get(place["id"]), "", "place-" + place["id"])
    else:
        for p in people:
            if g["PH"].PERSON_PHOTOS.get(p[0]):
                fig = g["photo_fig"](g["PH"].PERSON_PHOTOS.get(p[0]), "portrait", "person-" + p[0])
                break

    more = EM.MORE.get(ev[5])
    body = g["paras"](more[0], more[1]) if more else ""
    share = f'<p class="share no-print"><button type="button" class="btn" data-copy="event-{slug}.html">{bi_("Copy link to share", "Copïo dolen i’w rhannu")}</button></p>'
    main = (hero(eid, f'<a href="index.html">{SITE}</a> / <a href="timeline.html">{bi_("Timeline", "Llinell amser")}</a> / <a href="era-{eid}.html">{bi_(era["en"], era["cy"])}</a>',
                 era["ill"], date_label(ev), date_label(ev, True), ev[5], ev[6], ev[7], ev[8], art=ERA_ART[eid])
            + section(top + fig + body + g["further"](f"event:{slug}", ev[11]) + share, top=True))

    # long reads that tell this story
    sl = g["story_links"]("events", ev[5])
    if sl:
        main += section(_link_list([(f"story-{x['id']}.html", x["en"], x["cy"], x["sumEn"], x["sumCy"]) for x in sl]), "Read the long read", "Darllen yr erthygl")
    if place:
        main += section(f'<div class="era-places">{g["place_tile"](place)}</div>', "Where it happened", "Lle digwyddodd")
    if people:
        main += section(f'<div class="people">{"".join(g["plaque"](p) for p in people)}</div>', "The people", "Y bobl")
    rel = [(f"battles.html#b-{b['id']}", b["en"], b["cy"], b["dEn"], b["dCy"]) for b in _battles(ev)]
    rel += [(f"documents.html#doc-{d['id']}", d["en"], d["cy"], d["dEn"], d["dCy"]) for d in _docs(ev)]
    if rel:
        main += section(_link_list(rel), "Battles and documents of the time", "Brwydrau a dogfennau’r cyfnod")

    # just before and just after, on the timeline
    near = D.EVENTS[max(0, i - 2):i] + D.EVENTS[i + 1:i + 3]
    main += section(f'<ol class="era-events">{"".join(g["event_li"](x) for x in near)}</ol>', "Before and after", "Cyn ac wedyn")
    prev_e, next_e = (D.EVENTS[i - 1] if i > 0 else None), (D.EVENTS[i + 1] if i + 1 < len(D.EVENTS) else None)
    pager = ((f'<a class="btn" href="{href(prev_e)}">← {bi(prev_e[5], prev_e[6])}</a>' if prev_e else f'<a class="btn" href="timeline.html">← {bi_("The timeline", "Y llinell amser")}</a>')
             + (f'<a class="btn solid" href="{href(next_e)}">{bi(next_e[5], next_e[6])} →</a>' if next_e else f'<a class="btn solid" href="timeline.html">{bi_("The timeline", "Y llinell amser")} →</a>'))
    main += section(f'<div class="pager">{pager}</div>')

    yr = g["year_label"](ev)
    title = f"{ev[5]} ({yr}) · History of Wales"
    desc = ev[7] if not more else ev[7] + " " + more[0][0]
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": f"{ev[5]} ({yr})", "alternativeHeadline": ev[6], "description": ev[7],
          "inLanguage": ["en", "cy"], "about": {"@type": "Thing", "name": ev[5]}}
    if ev[11]:
        ld["about"]["sameAs"] = g["WIKI"] + ev[11]
    return page(f"event-{slug}.html", title, desc, main, era=eid, ld=ld, track=f"event:{slug}")


def pages():
    return {f"event-{SLUG[i]}.html": event_page(i, ev) for i, ev in enumerate(D.EVENTS)}


def search_items():
    yl = g["year_label"]
    return [dict(k="event", t=ev[5], c=ev[6], u=f"event-{SLUG[i]}.html", y=[yl(ev), yl(ev, True)], b=[ev[7], ev[8]], e=ev[0]) for i, ev in enumerate(D.EVENTS)]


CSS = """
.ev-rel { list-style: none; padding: 0; margin: 0; display: grid; gap: .6rem; grid-template-columns: repeat(auto-fill, minmax(min(100%, 280px), 1fr)) }
.ev-rel a { display: grid; gap: .25rem; padding: 1rem 1.1rem; border: 1px solid var(--line); border-radius: 16px; background: var(--card); color: inherit; text-decoration: none; height: 100% }
.ev-rel a:hover, .ev-rel a:focus-visible { border-color: color-mix(in srgb, var(--gold) 55%, var(--line)) }
.ev-rel small { color: var(--muted); font-size: .9rem; line-height: 1.45 }
.era-events .links .src.full { font-weight: 600 }
"""
