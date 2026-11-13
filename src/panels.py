# Picture backgrounds for the plain panels and cards (Ifan, 13 November 2026: "give these cards image/picture
# backgrounds, something to make them look better ... same with all cards on the site, check them all").
#
# A panel gets a real picture behind it, darkened from the top down so its words stay easy to read (a dark veil of
# 50 % at the top to 88 %, and a soft shadow under the words). Panels of one kind that sit side by side take turns from a set of
# pictures (ROTATE), so a grid never shows the same picture twelve times. Panels that belong to one thing (the
# Visiting box of a place, a town, a symbol) carry their own picture in the page: class "pbg" and --pbg in style,
# made by bg_style(). Cards that already show a picture of their own (people, places, long reads, battles ...) are
# left as they are. Every picture is one already kept on the site, with its credit on its own page or the gallery.
import json
import os

import pictures as PX
import thumbs as TH

_HERE = os.path.dirname(os.path.abspath(__file__))
_LOCAL = json.load(open(os.path.join(_HERE, "photo_files.json"), encoding="utf-8"))


def url(ref, small=False):
    """Site path of a picture: a src/pictures.py ref ("g:", "p:", "l:", "c:") or "f:<Commons file>" kept in photos/.
    small=True gives the 220 px copy (src/thumbs.py), for cards that come many to a page."""
    if ref.startswith("f:"):
        loc = _LOCAL.get(ref[2:])
        path = f"photos/{loc[0]}-s.webp" if loc else None
    else:
        path = PX._parse(ref)["small"]
    if not path or path.startswith("http"):
        return None
    return TH.thumb(path) if small else path


def bg_style(ref_or_path, small=False):
    """The style attribute for one panel's own picture (class "pbg")."""
    path = ref_or_path if "/" in ref_or_path and ":" not in ref_or_path else url(ref_or_path, small)
    if path and small and not path.startswith("t/"):
        path = TH.thumb(path)
    return f' style="--pbg:url(\'{path}\')"' if path else ""


LLANFAIR = "f:The James Pringle Weavers shop in Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch on the Isle of Anglesey in North Wales.jpg"
LAND = ["g:land-yr-wyddfa", "g:land-brecon-beacons", "g:land-cadair-idris", "g:land-llyn-y-fan", "g:land-tryfan", "g:land-three-cliffs",
        "g:land-llyn-idwal", "g:land-pen-y-fan", "g:land-worms-head", "g:land-llyn-tegid", "g:land-strumble", "g:land-barafundle"]
BOOKS = ["g:trea-red-book", "g:trea-black-book", "g:trea-book-aneirin", "g:trea-book-taliesin", "g:trea-laws-hywel", "g:trea-bible-1588",
         "g:trea-pennal-letter", "g:trea-st-chad"]
HOLY = ["g:holy-st-davids-bishops", "g:holy-pennant-melangell", "g:holy-llangelynnin", "g:holy-penmon", "g:holy-valle-crucis", "g:holy-st-govans",
        "g:holy-talley", "g:holy-llanbadarn", "g:holy-margam", "g:holy-cwmhir", "g:holy-basingwerk", "g:holy-soar-y-mynydd"]
CASTLES = ["g:cast-carreg-cennen", "g:cast-dolwyddelan", "g:cast-criccieth", "g:cast-dinas-bran", "g:cast-castell-coch", "g:cast-kidwelly",
           "g:cast-cilgerran", "g:cast-llansteffan", "g:cast-powis", "g:cast-denbigh", "g:cast-white-castle", "g:cast-dryslwyn"]

# One picture for a kind of panel: (CSS selector, picture)
SINGLE = [
    # the home page
    (".lang-grid > .panel:not(.decoder)", "l:iaith-1966"),        # Welsh speakers by census: Cymdeithas yr Iaith at Llangefni, 1966
    (".panel.decoder", LLANFAIR),                                  # the place-name decoder: the long name of Llanfairpwllgwyngyll
    (".wotd", "g:land-brecon-beacons"),                            # word of the day (home page and Learn Welsh)
    (".lang-words", "g:trea-black-book"),                          # words to know
    (".b-fact", "g:trea-red-book"),                                # did you know?
    (".news-box", "g:land-three-cliffs"),                          # new on the site
    (".reading", "g:trea-bible-1588"),                             # further reading
    (".tl-band", "g:land-yr-wyddfa"),                              # the timeline band
    # on many pages
    (".refs", "g:trea-red-book"),                                  # references and further reading
    (".further", "g:trea-red-book"),
    (".note-box", "g:trea-laws-hywel"),
    (".behind", "g:trea-red-book"),                                # behind the legend
    (".just-added", "g:land-strumble"),
    (".sm-card", "g:holy-st-davids-bishops"),                      # the saints' map card
    (".today-card", "g:holy-pennant-melangell"),                   # saint of the day
    (".ll-out", "g:holy-llangelynnin"),
    (".cm-card", "g:cast-carreg-cennen"),                          # the castles map card
    (".near", "g:land-yr-wyddfa"),                                 # history near you (map page)
    (".g-root", "g:anci-llys-rhosyr"),                             # the games
    (".game-box", "g:anci-llys-rhosyr"),
    (".quiz", "g:anci-llys-rhosyr"),
    (".tw-dec", LLANFAIR),                                         # the place-name decoder (towns page)
    (".sheet-print", "g:buil-old-college"),                        # teacher packs
    (".pk-source", "g:trea-pennal-letter"),
    (".pk-list", "g:buil-old-college"),
    (".about-facts", "g:buil-old-college"),                        # about the site
    (".fix-box", "g:trea-pennal-letter"),
    (".cyng", "g:trea-book-taliesin"),                             # cynghanedd (literature)
    (".lw-quiz", "g:trea-laws-hywel"),                             # the Laws of Hywel Dda
    (".lw-words", "g:trea-laws-hywel"),
    (".lw-worth", "g:place-hendygwyn"),
    (".lw-dates", "g:place-hendygwyn"),
    (".cyw-week", "g:land-llyn-tegid"),                            # Learn Welsh
    (".letters", "g:trea-black-book"),
    (".ref-big-search", "g:trea-red-book"),
]

# Panels that come side by side take turns: (selector of one panel, pictures)
ROTATE = [
    (".phr > li", LAND),                # Learn Welsh: the phrases
    (".ms-lib", BOOKS),                 # the libraries that keep the manuscripts
    (".lit-q", BOOKS),                  # literature quotes
    (".tri", BOOKS),                    # the Triads
    (".cal-m", HOLY),                   # the saints' calendar, month by month
    (".mut", HOLY),
    (".cm-feat", CASTLES),              # castles: the features
    (".author", BOOKS),                 # books and authors
    (".lw-off", BOOKS),                 # the officers of the court (laws)
    (".pk-box", LAND),                  # teacher pack boxes
    (".ref-desk > a", LAND),            # the reference desk
    (".otd-day", LAND),                 # On this day, day by day (each row also has its own picture)
]
SMALL = {".author", ".otd-day", ".tri", ".lw-off", ".ref-desk > a", ".cm-feat", ".cal-m", ".phr > li", ".pk-box"}   # many to a page: small copies

STRONG = {".author", ".otd-day", ".tri", ".lw-off", ".lit-q", ".behind", ".refs", ".further", ".note-box", ".b-fact", ".lw-worth", ".ms-lib", ".fix-box"}  # long text: a darker veil
VEIL_STRONG = ("linear-gradient(180deg, rgba(12,15,22,.66) 0, rgba(12,15,22,.86) 6rem, rgba(12,15,22,.92) 100%)")
VEIL = ("linear-gradient(180deg, rgba(12,15,22,.50) 0, rgba(12,15,22,.78) 9rem, rgba(12,15,22,.88) 100%)")


def css():
    out = ["/* picture backgrounds for plain panels (src/panels.py) */"]
    sels = [".pbg"]
    for sel, ref in SINGLE:
        u = url(ref)
        if u:
            out.append(f"html body {sel}{{--pbg:url('{u}')}}")
            sels.append(sel)
    for sel, refs in ROTATE:
        us = [u for u in (url(r, sel in SMALL) for r in refs) if u]
        n = len(us)
        for k, u in enumerate(us):
            out.append(f"html body {sel}:nth-child({n}n+{k + 1}){{--pbg:url('{u}')}}")
        sels.append(sel)
    sel_all = ", ".join(sels)
    out.append(f"html body :is({sel_all}){{background-image:{VEIL},var(--pbg)!important;background-size:cover!important;"
               f"background-position:center 35%!important;background-repeat:no-repeat!important}}")
    strong = ", ".join(x for x in sels if x in STRONG)
    out.append(f"html body :is({strong}){{background-image:{VEIL_STRONG},var(--pbg)!important}}")
    out.append(f"html body :is({sel_all}){{text-shadow:0 1px 3px rgba(0,0,0,.65)}}")
    out.append("@media print{html body :is(" + sel_all + "){background-image:none!important}}")
    out.append("@supports (content-visibility:auto){.author,.tw-card,.otd-day{content-visibility:auto;contain-intrinsic-size:auto 260px}}")
    return "\n".join(out) + "\n"
