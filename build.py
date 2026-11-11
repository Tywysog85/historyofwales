#!/usr/bin/env python3
"""Build History of Wales into a static site.

Usage:  python3 build.py            -> writes _site/ (for GitHub Pages)
        python3 build.py --artifact -> also writes _artifact/ (preview without a document skeleton)

Environment:
  SITE_URL     public address of the site, ending in /   (default: the GitHub Pages address)
  GOATCOUNTER  your GoatCounter code, e.g. "hanescymru", to switch on visitor statistics
"""
import datetime, html, json, os, re, sys, shutil
from xml.sax.saxutils import escape as xesc

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)
import data as D  # noqa: E402
import long as L  # noqa: E402
import towns as TW  # noqa: E402
import photos as PH  # noqa: E402
import ages as AG  # noqa: E402
import features as F  # noqa: E402
import art as A  # noqa: E402
L.TEACH.update(AG.TEACH)
import ages9 as AG9
import royal as RY  # noqa: E402
import trees as TR  # noqa: E402
L.TEACH.update(AG9.TEACH)
from urllib.parse import quote as _q

BASE_URL = os.environ.get("SITE_URL", "https://tywysog85.github.io/historyofwales/")
GOATCOUNTER = os.environ.get("GOATCOUNTER", "").strip()
WIKI = "https://en.wikipedia.org/wiki/"


def read(*p):
    with open(os.path.join(SRC, *p), encoding="utf-8") as f:
        return f.read()


def e(s):
    return html.escape(str(s), quote=True)


head = read("head.html")
body = read("body.html")
app = read("app.js")
extra_css = read("extra.css") + read("v6.css")
geo = json.loads(read("geo", "map.json"))
la = json.loads(read("geo", "la.json"))


def _split_la():
    """Cut Powys and Gwynedd into their historic shires, so the Kingdoms map can show Brycheiniog, Meirionnydd and the rest.
    The cuts are straight lines of latitude and longitude, so the borders are approximate."""
    import re as _re
    sc, k, minx, maxy = geo["sc"], geo["k"], geo["minx"], geo["maxy"]
    Y = lambda lat: (maxy - lat) * sc
    X = lambda lon: (lon - minx) * k * sc

    def pts(d):
        return [(float(a), float(b)) for a, b in _re.findall(r"(-?[\d.]+) (-?[\d.]+)", d)]

    def clip(poly, axis, v, keep_less):
        out = []
        for i, p in enumerate(poly):
            q = poly[i - 1]
            pin, qin = (p[axis] < v) == keep_less, (q[axis] < v) == keep_less
            if pin != qin:
                t = (v - q[axis]) / (p[axis] - q[axis])
                out.append((q[0] + (p[0] - q[0]) * t, q[1] + (p[1] - q[1]) * t))
            if pin:
                out.append(p)
        return out

    def path(*polys):
        return " ".join("M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in poly) + " Z" for poly in polys if len(poly) > 2)

    powys, gwynedd = pts(la.pop("Powys")), pts(la.pop("Gwynedd"))
    la["Montgomeryshire"] = path(clip(powys, 1, Y(52.42), True))
    la["Radnorshire"] = path(clip(clip(powys, 1, Y(52.42), False), 1, Y(52.12), True))
    la["Brecknockshire"] = path(clip(powys, 1, Y(52.12), False))
    south = clip(gwynedd, 1, Y(52.97), False)
    la["Meirionnydd"] = path(clip(south, 0, X(-4.15), False))
    la["Caernarfonshire"] = path(clip(gwynedd, 1, Y(52.97), True), clip(south, 0, X(-4.15), True))


_split_la()

style = head[head.index("<style>") + 7: head.index("</style>")] + extra_css
symbols = head[head.index('<svg width="0"'): head.index("</svg>", head.index('<svg width="0"')) + 6]
fonts = "".join(re.findall(r'<link [^>]+>', head))

ERA = {x["id"]: x for x in D.ERAS}
PERSON = {p[0]: p for p in D.PEOPLE}
PLACE = {p["id"]: p for p in D.PLACES}
COL = dict(ancient="#d39a62", roman="#e58fb4", saints="#b9a0ea", kings="#e8c65a", medieval="#f26a62", tudor="#62c6c4", industrial="#93a0e0", modern="#7cc495", today="#f59a4a")
ERA_ART = dict(ancient="dolmen", roman="fort", saints="cross", kings="ship", medieval="castle", tudor="book", industrial="pit", modern="terrace", today="senedd")
TRAIL_ART = dict(women="torch", sea="ship", chapel="book", iron="pit")
EVENT_BY_TITLE = {ev[5]: ev for ev in D.EVENTS}


def bi(en, cy, tag="span", cls=""):
    if en == cy:
        return e(en)
    c = f" {cls}" if cls else ""
    return f'<{tag} class="l-en{c}" lang="en">{e(en)}</{tag}><{tag} class="l-cy{c}" lang="cy">{e(cy)}</{tag}>'


SEARCH_BTN = '<button type="button" class="search-btn" data-search aria-label="Search / Chwilio"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.5 15.5 21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>'
SITE = bi("History of Wales", "Hanes Cymru")


def paras(en_list, cy_list, cls="story"):
    return (f'<div class="{cls} l-en" lang="en">' + "".join(f"<p>{e(a)}</p>" for a in en_list) + "</div>"
            f'<div class="{cls} l-cy" lang="cy">' + "".join(f"<p>{e(a)}</p>" for a in cy_list) + "</div>")


def year_label(ev, cy=False):
    y, c, end = ev[1], ev[2], ev[3]
    pre = "c. " if c else ""
    if y < 0:
        return f"{pre}{abs(y):,} {'CC' if cy else 'BC'}"
    if y < 1000:
        return f"{pre}{y} {'OC' if cy else 'AD'}"
    return f"{pre}{y}" + (f"–{end}" if end else "")


def src(s):
    return f'<a class="src" href="{WIKI}{s}" target="_blank" rel="noopener">{bi("Source", "Ffynhonnell")} ↗<span class="sr-only"> (Wikipedia)</span></a>' if s else ""


# ---------- shared head tags ----------
def head_tags(title, desc, path, og_type="website"):
    url = BASE_URL + path
    t = (f'<title>{e(title)}</title>\n<meta name="description" content="{e(desc)}">\n<link rel="canonical" href="{url}">\n'
         '<meta name="theme-color" content="#0e1118">\n<link rel="icon" href="favicon.svg" type="image/svg+xml">\n'
         '<link rel="apple-touch-icon" href="apple-touch-icon.png">\n<link rel="manifest" href="manifest.webmanifest">\n'
         f'<meta property="og:title" content="{e(title)}">\n<meta property="og:description" content="{e(desc)}">\n'
         f'<meta property="og:type" content="{og_type}">\n<meta property="og:url" content="{url}">\n'
         f'<meta property="og:image" content="{BASE_URL}og.png">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
         '<meta property="og:locale" content="en_GB">\n<meta property="og:locale:alternate" content="cy_GB">\n'
         '<meta name="twitter:card" content="summary_large_image">\n')
    return t


TAIL_JS = ('<script src="site.js" defer></script>\n<script src="search.js" defer></script>\n<script>if("serviceWorker" in navigator&&location.protocol==="https:"){addEventListener("load",function(){navigator.serviceWorker.register("sw.js").catch(function(){})})}</script>\n'
           + (f'<script data-goatcounter="https://{GOATCOUNTER}.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>\n' if GOATCOUNTER else ""))

LANG_BOOT = '<script>(function(){var h=document.documentElement;h.classList.add("js");setTimeout(function(){if(!window.__site)h.classList.add("rv-all")},2500);try{if(localStorage.getItem("hc-lang")==="cy"){h.classList.add("cy");h.lang="cy"}}catch(e){}})()</script>'
LANG_JS = '''<script>(function(){var d=document.documentElement;function s(l){d.classList.toggle("cy",l==="cy");d.lang=l;document.getElementById("lang-en").setAttribute("aria-pressed",l==="en");document.getElementById("lang-cy").setAttribute("aria-pressed",l==="cy");try{localStorage.setItem("hc-lang",l)}catch(e){}}
s(d.classList.contains("cy")?"cy":"en");document.getElementById("lang-en").onclick=function(){s("en")};document.getElementById("lang-cy").onclick=function(){s("cy")};
document.addEventListener("click",function(ev){var p=ev.target.closest("[data-print]");if(p){window.print();return}var b=ev.target.closest("[data-copy]");if(!b)return;var u=new URL(b.dataset.copy,location.href).href,o=b.innerHTML;try{navigator.clipboard.writeText(u).then(function(){b.textContent=d.classList.contains("cy")?"Wedi copïo":"Copied";setTimeout(function(){b.innerHTML=o},1600)})}catch(e){}});})();</script>'''

PRINT_CSS = """
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap }
.skip { position: absolute; left: -9999px; top: 0; z-index: 50; background: var(--ink); color: var(--night); padding: .6rem 1rem; border-radius: 0 0 8px 0 }
.skip:focus { left: 0 }
@media print {
  :root { --night: #fff; --slate: #fff; --slate-2: #f2f2f2; --ink: #111; --muted: #444; --line: #bbb; color-scheme: light }
  body { background: #fff; color: #111; font-size: 11pt }
  .nav, footer, .no-print, .pager, .era-hero svg.ill { display: none !important }
  section { padding-block: 12pt !important; break-inside: avoid-page }
  .sheet-print { break-before: page }
  a { color: #111; text-decoration: none }
}
"""


NAV_MAIN = [("timeline.html", "Timeline", "Llinell amser"), ("index.html#chapters", "Ages", "Oesoedd"), ("index.html#map", "Map", "Map"),
            ("index.html#people", "People", "Pobl"), ("stories.html", "Long reads", "Erthyglau"), ("legends.html", "Legends", "Chwedlau"), ("play.html", "Play", "Chwarae")]
NAV_MORE = [("kings.html", "Kings and princes", "Brenhinoedd a thywysogion"), ("family-trees.html", "Royal family trees", "Coed teulu brenhinol"), ("symbols.html", "Symbols and traditions", "Symbolau a thraddodiadau"), ("trails.html", "Themed trails", "Llwybrau thema"), ("gallery.html", "Photo gallery", "Oriel luniau"),
            ("index.html#language", "The Welsh language", "Yr iaith Gymraeg"), ("journey.html", "Your journey", "Eich taith"), ("teachers.html", "For teachers", "I athrawon"),
            ("index.html#sources", "Sources", "Ffynonellau")]
# extra links for the home page top bar, where the site name has moved into the opening screen and left room
NAV_HOME_MORE = [("symbols.html", "Symbols", "Symbolau"), ("trails.html", "Trails", "Llwybrau"), ("gallery.html", "Gallery", "Oriel"), ("index.html#language", "Language", "Iaith")]
SEARCH_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.5 15.5 21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'


def nav(active="", skip="#main", home=False):
    def li(h, a, b, n=None):
        num = f'<span class="n">{n:02d}</span>' if n else ""
        return f'<li><a href="{h}"{" class=on aria-current=page" if active == h else ""}>{num}{bi(a, b)}</a></li>'
    main = "".join(li(*x) for x in NAV_MAIN)
    if home:
        main += "".join(li(*x).replace("<li>", '<li class="x">', 1) for x in NAV_HOME_MORE)
    big = li("index.html", "Home", "Hafan", 1) + "".join(li(h, a, b, i + 2) for i, (h, a, b) in enumerate(NAV_MAIN))
    more = "".join(li(*x) for x in NAV_MORE)
    return (f'<a class="skip" href="{skip}">{bi("Skip to content", "Neidio i’r cynnwys")}</a><div class="progress" aria-hidden="true"><i id="progress"></i></div>'
            f'<nav class="nav" aria-label="Main"><div class="wrap">' + ("" if home else f'<a class="brand" href="index.html">{bi("History of Wales", "Hanes Cymru")}</a>') +
            f'<ul class="nav-inline">{main}</ul>' + ('<span class="brand" aria-hidden="true"></span>' if home else "") +
            f'<a class="journey-chip" href="journey.html" id="journey-chip" data-total="{JOURNEY_TOTAL}" aria-label="Your journey / Eich taith"><svg viewBox="0 0 36 36" aria-hidden="true"><circle cx="18" cy="18" r="15" class="tr"/><circle cx="18" cy="18" r="15" class="fg" id="journey-ring" pathLength="100" stroke-dasharray="0 100"/></svg><b id="journey-n">0</b></a>'
            f'<button type="button" class="search-btn" data-search aria-label="Search / Chwilio">{SEARCH_SVG}</button>'
             '<div class="lang" role="group" aria-label="Language / Iaith"><button type="button" id="lang-en" aria-pressed="true">EN</button><button type="button" id="lang-cy" aria-pressed="false">CY</button></div>'
            f'<button type="button" class="menu-btn" id="menu-btn" aria-expanded="false" aria-controls="menu"><span class="bars" aria-hidden="true"><i></i><i></i></span>{bi("Menu", "Dewislen")}</button></div></nav>'
            f'<div class="menu" id="menu" hidden><div class="wrap"><ul class="menu-big">{big}</ul><div class="menu-side"><p class="eyebrow">{bi("More", "Rhagor")}</p><ul class="menu-more">{more}</ul>'
            f'<p class="menu-note">{bi("230,000 years of history, in English and Cymraeg.", "230,000 o flynyddoedd o hanes, yn Gymraeg ac yn Saesneg.")}</p></div></div></div>')


# Name shown in the copyright line at the bottom of every page.
COPYRIGHT_OWNER = "History of Wales"
COPYRIGHT_OWNER_CY = "Hanes Cymru"


def footer():
    def col(title_en, title_cy, links):
        return f'<div><p class="eyebrow">{bi(title_en, title_cy)}</p><ul>' + "".join(f'<li><a href="{h}">{bi(a, b)}</a></li>' for h, a, b in links) + "</ul></div>"
    eras = [(f'era-{x["id"]}.html', x["en"], x["cy"]) for x in D.ERAS]
    explore = [("timeline.html", "Timeline", "Llinell amser"), ("index.html#map", "Map of Wales", "Map Cymru"), ("index.html#people", "People", "Pobl"), ("kings.html", "Kings and princes", "Brenhinoedd a thywysogion"), ("family-trees.html", "Royal family trees", "Coed teulu brenhinol"), ("trails.html", "Themed trails", "Llwybrau thema"),
               ("gallery.html", "Photo gallery", "Oriel luniau"), ("index.html#language", "The Welsh language", "Yr iaith Gymraeg")]
    read = [("stories.html", "Long reads", "Erthyglau"), ("legends.html", "Legends", "Chwedlau"), ("symbols.html", "Symbols and traditions", "Symbolau a thraddodiadau"),
            ("teachers.html", "For teachers", "I athrawon"), ("index.html#sources", "Sources", "Ffynonellau")]
    play = [("daily.html", "Daily challenge", "Her y dydd"), ("quiz.html", "Quiz", "Cwis"), ("map-game.html", "Where in Wales?", "Ble yng Nghymru?"), ("names.html", "Welsh names", "Enwau Cymraeg"),
            ("play.html", "All games", "Pob gêm"), ("journey.html", "Your journey", "Eich taith")]
    yr = datetime.date.today().year
    yrs = "2026" if yr <= 2026 else f"2026–{yr}"
    copy_en = (f"© {yrs} {COPYRIGHT_OWNER}. All rights reserved. The text and design of this site may not be copied without permission. "
               "Photographs and the 3D dragon belong to their own creators and are used under their licences.")
    copy_cy = (f"© {yrs} {COPYRIGHT_OWNER_CY}. Cedwir pob hawl. Ni chaniateir copïo testun na chynllun y wefan hon heb ganiatâd. "
               "Mae’r ffotograffau a’r ddraig 3D yn eiddo i’w crewyr eu hunain ac fe’u defnyddir dan eu trwyddedau.")
    return ('<footer class="site-foot"><div class="wrap"><div class="foot-top"><p class="big">Diolch<span>.</span></p>'
            f'<p class="foot-tag">{bi("Thank you for reading. Wales is a small country with a long memory; this site is a way in.", "Diolch am ddarllen. Gwlad fach â chof hir yw Cymru; ffordd i mewn yw’r wefan hon.")}</p></div>'
            f'<div class="foot-cols">{col("The nine ages", "Y naw oes", eras)}{col("Explore", "Archwilio", explore)}{col("Read", "Darllen", read)}{col("Play", "Chwarae", play)}</div>'
            f'<div class="foot-base"><span>{bi("History of Wales · Hanes Cymru", "Hanes Cymru · History of Wales")}</span>'
            f'<span>{bi("Event links go to Wikipedia, which lists academic sources. Dates marked c. are approximate. Original illustrations; photographs from Wikimedia Commons, credited on each page.", "Mae dolenni’r digwyddiadau’n mynd i Wicipedia, sy’n rhestru ffynonellau academaidd. Dyddiadau bras yw’r rhai a nodir c. Darluniau gwreiddiol; ffotograffau o Wikimedia Commons, gyda chydnabyddiaeth ar bob tudalen.")}</span></div><p class="foot-copy">{bi(copy_en, copy_cy)}</p></div></footer>'
            f'<button type="button" class="to-top" id="to-top" aria-label="Back to top / Yn ôl i’r brig" hidden><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>')


def page(path, title, desc, main_html, era=None, og_type="article", ld=None, active="", track="", extra=""):
    ld_html = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>' if ld else ""
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
{head_tags(title, desc, path, og_type)}{LANG_BOOT}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{fonts}
<style>{style}{PRINT_CSS}</style>
{ld_html}
</head>
<body{f' data-era="{era}"' if era else ""}{f' data-track="{track}"' if track else ""}>
{symbols}
{nav(active)}
<main id="main">
{main_html}
</main>
{footer()}
{LANG_JS}
{TAIL_JS}{extra}</body>
</html>
'''


def hero(era_id, crumbs, ill, eyebrow_en, eyebrow_cy, h_en, h_cy, sub_en="", sub_cy="", art=None, extra=""):
    bg = f'<div class="hero-art">{A.scene(art, COL[era_id])}</div>' if art else ""
    icon = "" if art else f'<svg class="ill" aria-hidden="true"><use href="#i-{ill}"/></svg>'
    return (f'<header class="era-hero{" has-art" if art else ""}" data-era="{era_id}">{bg}<div class="wrap"><p class="crumbs">{crumbs}</p>'
            f'{icon}<p class="span">{bi(eyebrow_en, eyebrow_cy)}</p>'
            f'<h1>{bi(h_en, h_cy)}</h1>' + (f'<p class="lede">{bi(sub_en, sub_cy)}</p>' if sub_en else "") + extra + "</div></header>")


def section(inner, title_en=None, title_cy=None, top=False):
    h = f'<h2 class="sub-h">{bi(title_en, title_cy)}</h2>' if title_en else ""
    cls = "" if top else ' class="tight"'
    return f'<section{cls}><div class="wrap">{h}{inner}</div></section>'


EVI = {ev: i for i, ev in enumerate(D.EVENTS)}
COMMONS = "https://commons.wikimedia.org/wiki/"


def photo_url(f, w=1200):
    return f"{COMMONS}Special:FilePath/{_q(f, safe='')}?width={w}"


def photo_fig(ph, cls=""):
    if not ph:
        return ""
    f, cen, ccy = ph
    return (f'<figure class="photo {cls}"><img src="{photo_url(f)}" alt="{e(cen)}" loading="lazy" decoding="async" referrerpolicy="no-referrer" '
            f'onerror="this.closest(\'figure\').remove()">'
            f'<figcaption>{bi(cen, ccy)} · <a href="{COMMONS}File:{_q(f, safe="")}" target="_blank" rel="noopener">{bi("Photo: Wikimedia Commons", "Llun: Wikimedia Commons")}</a></figcaption></figure>')


def event_li(ev, k=0):
    links = ("".join(f'<a class="src" href="story-{x["id"]}.html">{bi("Read the long read", "Darllen yr erthygl")} →</a>' for x in story_links("events", ev[5]))
             + (f'<a class="src" href="place-{ev[10]}.html">{bi("The place", "Y lle")} →</a>' if ev[10] else "") + src(ev[11]))
    return (f'<li id="e{EVI[ev]}" class="{"key" if ev[9] else ""}" data-era="{ev[0]}"><time>{bi(year_label(ev), year_label(ev, True))}</time>'
            f'<div><h3>{bi(ev[5], ev[6])}</h3><p>{bi(ev[7], ev[8])}</p><div class="links">{links}</div></div></li>')


def plaque(p, link=True):
    return (f'<article class="plaque" id="{p[0]}" data-era="{p[1]}"><span class="dates">{e(p[2])}</span><h3>{bi(p[3], p[4])}</h3>'
            f'<span class="epi">{bi(p[5], p[6])}</span><p>{bi(p[7], p[8])}</p><div class="links">'
            + (f'<a class="go" href="person-{p[0]}.html">{bi("Read more", "Darllen mwy")} →</a>' if link else "")
            + f'{src(p[9])}</div></article>')


def place_tile(p):
    return (f'<a href="place-{p["id"]}.html" data-era="{p["era"]}"><svg aria-hidden="true"><use href="#i-{p["ill"]}"/></svg>'
            f'<span><b>{bi(p["en"], p["cy"])}</b><span>{e(p["year"])}</span></span></a>')


# ---------- era pages ----------
def era_page(i, era):
    eid = era["id"]
    prev_e = D.ERAS[i - 1] if i > 0 else None
    next_e = D.ERAS[i + 1] if i + 1 < len(D.ERAS) else None
    evs = [ev for ev in D.EVENTS if ev[0] == eid]
    ppl = [p for p in D.PEOPLE if p[1] == eid]
    plc = [p for p in D.PLACES if p["era"] == eid]
    pager = (f'<a class="btn" href="era-{prev_e["id"]}.html">← {bi(prev_e["en"], prev_e["cy"])}</a>' if prev_e else f'<a class="btn" href="index.html">← {bi("History of Wales", "Hanes Cymru")}</a>') + \
            (f'<a class="btn solid" href="era-{next_e["id"]}.html">{bi(next_e["en"], next_e["cy"])} →</a>' if next_e else f'<a class="btn solid" href="trails.html">{bi("Follow a trail", "Dilyn llwybr")} →</a>')
    main = (hero(eid, f'<a href="index.html">{SITE}</a> / {bi("Chapter", "Pennod")} {i + 1}', era["ill"], era["spanEn"], era["spanCy"], era["en"], era["cy"], era["blurbEn"], era["blurbCy"], art=ERA_ART[eid])
            + section(paras(era["storyEn"], era["storyCy"]), top=True)
            + section(f'<ol class="era-events">{"".join(event_li(ev) for ev in evs)}</ol>', "Timeline", "Llinell amser")
            + section(f'<div class="people">{"".join(plaque(p) for p in ppl)}</div>', "People", "Pobl")
            + (section(f'<div class="era-places">{"".join(place_tile(p) for p in plc)}</div>', "Places to visit", "Lleoedd i ymweld â nhw") if plc else "")
            + section(f'<div class="pager">{pager}</div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": era["en"], "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page(f"era-{eid}.html", f'{era["en"]} · History of Wales', era["blurbEn"], main, era=eid, ld=ld, track=f"era:{eid}")


# ---------- person pages ----------
def person_page(p):
    slug, eid = p[0], p[1]
    era = ERA[eid]
    long_en, long_cy = L.PEOPLE_LONG.get(slug) or D.PEOPLE_EXTRA_LONG[slug]
    related = [ev for ev in D.EVENTS if p[3] in ev[7] or p[3] in ev[5] or (slug == "dewi-sant" and "Dewi" in ev[7])]
    same = [x for x in D.PEOPLE if x[1] == eid and x[0] != slug][:4]
    idx = D.PEOPLE.index(p)
    prev_p, next_p = D.PEOPLE[idx - 1] if idx > 0 else None, D.PEOPLE[idx + 1] if idx + 1 < len(D.PEOPLE) else None
    pager = (f'<a class="btn" href="person-{prev_p[0]}.html">← {bi(prev_p[3], prev_p[4])}</a>' if prev_p else f'<a class="btn" href="era-{eid}.html">← {bi(era["en"], era["cy"])}</a>') + \
            (f'<a class="btn solid" href="person-{next_p[0]}.html">{bi(next_p[3], next_p[4])} →</a>' if next_p else '<a class="btn solid" href="index.html#people">' + bi("All people", "Pawb") + " →</a>")
    meta = (f'<div class="person-meta"><span>{e(p[2])}</span><span>{bi(p[5], p[6])}</span><a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a></div>')
    rl = realm_links(f"person-{slug}.html") + ft_link_for_person(f"person-{slug}.html")
    meta += f'<p class="realm-links">{rl}</p>' if rl else ""
    main = (hero(eid, f'<a href="index.html">{SITE}</a> / <a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a>', era["ill"], p[2], p[2], p[3], p[4], p[7], p[8], art=ERA_ART[eid])
            + section(meta + photo_fig(PH.PERSON_PHOTOS.get(slug), "portrait") + paras(long_en, long_cy) + f'<p class="share no-print"><button type="button" class="btn" data-copy="person-{slug}.html">{bi("Copy link to share", "Copïo dolen i’w rhannu")}</button> {src(p[9])}</p>', top=True)
            + story_feature("people", slug)
            + (section(f'<ol class="era-events">{"".join(event_li(ev) for ev in related)}</ol>', "On the timeline", "Ar y llinell amser") if related else "")
            + section(f'<div class="people">{"".join(plaque(x) for x in same)}</div>', "Also in this age", "Hefyd yn yr oes hon")
            + section(f'<div class="pager">{pager}</div>'))
    ld = {"@context": "https://schema.org", "@type": "Person", "name": p[3], "alternateName": p[4], "description": p[7], "sameAs": WIKI + p[9]}
    return page(f"person-{slug}.html", f"{p[3]} · History of Wales", p[7], main, era=eid, ld=ld, og_type="profile", track=f"person:{slug}")


# ---------- place pages ----------
def place_page(pl):
    pid, eid = pl["id"], pl["era"]
    era = ERA[eid]
    long_en, long_cy = L.PLACE_LONG.get(pid, ([], []))
    related = [ev for ev in D.EVENTS if ev[10] == pid]
    near = sorted([x for x in D.PLACES if x["id"] != pid], key=lambda x: (x["lat"] - pl["lat"]) ** 2 + ((x["lon"] - pl["lon"]) * 0.61) ** 2)[:3]
    osm = f'https://www.openstreetmap.org/?mlat={pl["lat"]}&mlon={pl["lon"]}#map=14/{pl["lat"]}/{pl["lon"]}'
    meta = (f'<div class="person-meta"><span>{e(pl["year"])}</span><span>{pl["lat"]:.3f}° N, {abs(pl["lon"]):.3f}° W</span>'
            f'<a href="{osm}" target="_blank" rel="noopener">{bi("Open in a map", "Agor mewn map")} ↗</a><a href="index.html#lle-{pid}">{bi("On our map", "Ar ein map")} →</a></div>')
    rl = realm_links(f"place-{pid}.html")
    meta += f'<p class="realm-links">{rl}</p>' if rl else ""
    main = (hero(eid, f'<a href="index.html">{SITE}</a> / <a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a>', pl["ill"], era["en"], era["cy"], pl["en"], pl["cy"], pl["dEn"], pl["dCy"], art=ERA_ART[eid])
            + section(meta + photo_fig(PH.PLACE_PHOTOS.get(pid)) + paras(long_en, long_cy) + f'<p class="share no-print">{src(pl["src"])}</p>', top=True)
            + story_feature("places", pid)
            + (section(f'<ol class="era-events">{"".join(event_li(ev) for ev in related)}</ol>', "What happened here", "Beth ddigwyddodd yma") if related else "")
            + section(f'<div class="era-places">{"".join(place_tile(x) for x in near)}</div>', "Nearby", "Gerllaw"))
    ld = {"@context": "https://schema.org", "@type": "TouristAttraction", "name": pl["en"], "alternateName": pl["cy"], "description": pl["dEn"],
          "geo": {"@type": "GeoCoordinates", "latitude": pl["lat"], "longitude": pl["lon"]}}
    return page(f"place-{pid}.html", f'{pl["en"]} · History of Wales', pl["dEn"], main, era=eid, ld=ld, og_type="place", track=f"place:{pid}")


# ---------- trails ----------
def trail_item(kind, ref):
    if kind == "person":
        p = PERSON[ref]
        return (f'<li data-era="{p[1]}"><time>{e(p[2])}</time><div><h3><a href="person-{ref}.html">{bi(p[3], p[4])}</a></h3><p>{bi(p[7], p[8])}</p></div></li>')
    if kind == "place":
        p = PLACE[ref]
        return (f'<li data-era="{p["era"]}"><time>{e(p["year"])}</time><div><h3><a href="place-{ref}.html">{bi(p["en"], p["cy"])}</a></h3><p>{bi(p["dEn"], p["dCy"])}</p></div></li>')
    ev = EVENT_BY_TITLE[ref]
    return event_li(ev)


def trail_page(t, i):
    nxt = L.TRAILS[(i + 1) % len(L.TRAILS)]
    main = (hero("medieval", f'<a href="index.html">{SITE}</a> / <a href="trails.html">{bi("Trails", "Llwybrau")}</a>', t["ill"], "Trail", "Llwybr", t["en"], t["cy"], art=TRAIL_ART.get(t["id"], "castle"))
            + section(paras(t["introEn"], t["introCy"]), top=True)
            + section(f'<ol class="era-events trail">{"".join(trail_item(k, r) for k, r in t["items"])}</ol>', "Stops on the trail", "Arosfannau ar y llwybr")
            + section(f'<div class="pager"><a class="btn" href="trails.html">← {bi("All trails", "Pob llwybr")}</a><a class="btn solid" href="trail-{nxt["id"]}.html">{bi(nxt["en"], nxt["cy"])} →</a></div>'))
    return page(f"trail-{t['id']}.html", f'{t["en"]} · History of Wales', t["introEn"][0], main, era="medieval", active="trails.html")


def trails_index():
    cards = "".join(f'<a class="chap" href="trail-{t["id"]}.html" data-era="{D.ERAS[i % len(D.ERAS)]["id"]}"><svg aria-hidden="true"><use href="#i-{t["ill"]}"/></svg>'
                    f'<span class="span">{len(t["items"])} {bi("stops", "arhosfan")}</span><h3>{bi(t["en"], t["cy"])}</h3><p>{bi(t["introEn"][0], t["introCy"][0])}</p>'
                    f'<span class="go">{bi("Follow the trail →", "Dilyn y llwybr →")}</span></a>' for i, t in enumerate(L.TRAILS))
    main = (hero("modern", f'<a href="index.html">{SITE}</a>', "mtn", "Themed trails", "Llwybrau thema", "Trails through Welsh history", "Llwybrau drwy hanes Cymru",
                 "Follow one thread through the centuries.", "Dilynwch un edefyn drwy’r canrifoedd.", art="arches")
            + section(f'<h2 class="sr-only">{bi("All trails", "Pob llwybr")}</h2><div class="chapters">{cards}</div>', top=True))
    return page("trails.html", "Trails · History of Wales", "Themed trails through Welsh history: women, the sea, chapel and song, iron and coal.", main, era="modern", og_type="website", active="trails.html")


# ---------- teachers ----------
def quiz_sheet(era, n=10):
    evs = [ev for ev in D.EVENTS if ev[0] == era["id"]]
    pick = (sorted(evs, key=lambda x: -x[9])[:n])
    pick = sorted(pick, key=lambda x: x[5])  # mixed order: alphabetical by title, not by date
    years = sorted(pick, key=lambda x: x[1])
    letters = "ABCDEFGHIJKL"
    rows = "".join(f'<tr><td>{k + 1}</td><td>{bi(ev[5], ev[6])}</td><td class="blank"></td></tr>' for k, ev in enumerate(pick))
    bank = " · ".join(f"<b>{letters[k]}</b> {bi(year_label(ev), year_label(ev, True))}" for k, ev in enumerate(years))
    key = ", ".join(f"{k + 1}{letters[years.index(ev)]}" for k, ev in enumerate(pick))
    return (f'<div class="sheet-print"><h3 class="sheet-h">{bi(era["en"], era["cy"])}: {bi("match the event to the date", "parwch y digwyddiad â’r dyddiad")}</h3>'
            f'<p class="muted">{bi("Name", "Enw")}: ____________________ &nbsp; {bi("Class", "Dosbarth")}: ________</p>'
            f'<p class="bank">{bank}</p><table class="qs"><thead><tr><th>#</th><th>{bi("Event", "Digwyddiad")}</th><th>{bi("Letter", "Llythyren")}</th></tr></thead><tbody>{rows}</tbody></table>'
            f'<details class="answers-key"><summary>{bi("Answers", "Atebion")}</summary><p>{key}</p></details></div>')


def teachers_page():
    blocks = ""
    for i, era in enumerate(D.ERAS):
        t = L.TEACH[era["id"]]
        acts_en = "".join(f"<li>{e(a)}</li>" for a in t["aEn"])
        acts_cy = "".join(f"<li>{e(a)}</li>" for a in t["aCy"])
        blocks += (f'<article class="lesson" data-era="{era["id"]}"><p class="span">{bi(era["spanEn"], era["spanCy"])}</p><h3><a href="era-{era["id"]}.html">{bi(era["en"], era["cy"])}</a></h3>'
                   f'<p class="eq">{bi("Enquiry question", "Cwestiwn ymholi")}: <b>{bi(t["qEn"], t["qCy"])}</b></p>'
                   f'<ol class="l-en" lang="en">{acts_en}</ol><ol class="l-cy" lang="cy">{acts_cy}</ol></article>')
    sheets = "".join(quiz_sheet(era) for era in D.ERAS)
    intro_en = ["History of Wales is free to use in the classroom. Every page works in English and Welsh, and every event links to a source, so pupils can practise checking evidence.",
                "The ideas below fit the Humanities Area of Learning and Experience in the Curriculum for Wales, with its focus on cynefin, enquiry and the diverse stories of Wales. Adapt them freely."]
    intro_cy = ["Mae Hanes Cymru am ddim i’w ddefnyddio yn y dosbarth. Mae pob tudalen yn gweithio yn Gymraeg ac yn Saesneg, ac mae pob digwyddiad yn cysylltu â ffynhonnell, fel y gall disgyblion ymarfer gwirio tystiolaeth.",
                "Mae’r syniadau isod yn addas ar gyfer Maes Dysgu a Phrofiad y Dyniaethau yng Nghwricwlwm i Gymru, gyda’i bwyslais ar gynefin, ymholi a straeon amrywiol Cymru. Addaswch nhw fel y mynnwch."]
    main = (hero("industrial", f'<a href="index.html">{SITE}</a>', "book", "For teachers", "I athrawon", "History of Wales in the classroom", "Hanes Cymru yn y dosbarth",
                 "Lesson ideas, enquiry questions and printable quiz sheets for each age.", "Syniadau gwersi, cwestiynau ymholi a thaflenni cwis i’w hargraffu ar gyfer pob oes.", art="book")
            + section(paras(intro_en, intro_cy), top=True)
            + section(f'<div class="lessons">{blocks}</div>', "Lesson ideas", "Syniadau gwersi")
            + section(f'<p class="no-print"><button type="button" class="btn solid" data-print="1">{bi("Print the quiz sheets", "Argraffu’r taflenni cwis")}</button> '
                      f'<span class="muted">{bi("Prints in whichever language is selected. Answers are hidden until opened.", "Yn argraffu yn yr iaith a ddewiswyd. Mae’r atebion yn gudd nes eu hagor.")}</span></p>{sheets}', "Printable quiz sheets", "Taflenni cwis i’w hargraffu")
            + section(f'<p>{bi("Spotted a mistake, or have a resource to share? Contact the site owner through the GitHub repository.", "Wedi gweld camgymeriad, neu am rannu adnodd? Cysylltwch â pherchennog y wefan drwy’r ystorfa GitHub.")} '
                      '<a href="https://github.com/Tywysog85/historyofwales/issues" target="_blank" rel="noopener">GitHub ↗</a></p>'))
    return page("teachers.html", "For teachers · History of Wales", "Lesson ideas and printable quiz sheets on the history of Wales, in English and Welsh.", main, era="industrial", og_type="website", active="teachers.html")


EXTRA_PAGE_CSS = """
.tight { padding-top: 0 }
.lede { color: var(--muted); max-width: 40rem; font-size: 1.15rem }
.person-meta { display: flex; flex-wrap: wrap; gap: .4rem 1.4rem; font-family: var(--f-mono); font-size: .8rem; color: var(--muted); margin-bottom: 1.5rem }
.person-meta a { color: var(--ink) }
.share { margin-top: 1.5rem; display: flex; flex-wrap: wrap; gap: 1rem; align-items: center }
.era-events .links { display: flex; gap: 1rem; flex-wrap: wrap; margin-top: .3rem }
.era-events h3 a { text-decoration-color: var(--line); text-underline-offset: 4px }
.era-events li[data-era] time { color: var(--c) }
a.chap { text-decoration: none; color: inherit }
.lessons { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 20rem), 1fr)); gap: 1rem }
.lesson { background: var(--slate); border: 1px solid var(--line); border-top: 3px solid var(--c); border-radius: 12px; padding: 1.3rem 1.4rem; display: grid; gap: .6rem; align-content: start }
.lesson .span { font-family: var(--f-mono); font-size: .75rem; color: var(--c) }
.lesson h3 { font-size: 1.7rem } .lesson h3 a { text-decoration: none }
.lesson ol { margin: 0; padding-left: 1.2rem; display: grid; gap: .5rem; color: #cfd2d8 }
.lesson .eq { color: var(--muted) } .lesson .eq b { color: var(--ink) }
.muted { color: var(--muted) }
.sheet-print { background: var(--slate); border: 1px solid var(--line); border-radius: 12px; padding: 1.4rem; margin-top: 1.25rem; display: grid; gap: .8rem; overflow-x: auto }
.sheet-h { font-size: 1.6rem }
.bank { font-size: .95rem; line-height: 1.9 }
.qs { width: 100%; border-collapse: collapse; min-width: 22rem }
.qs th, .qs td { text-align: left; border-bottom: 1px solid var(--line); padding: .55rem .5rem; vertical-align: top }
.qs th { font-family: var(--f-mono); font-size: .72rem; color: var(--muted); text-transform: uppercase; letter-spacing: .08em; font-weight: 500 }
.qs td:first-child { width: 2rem; color: var(--muted) } .qs td.blank { width: 6rem; border-bottom: 1px solid var(--muted) }
.answers-key summary { cursor: pointer; color: var(--muted); font-size: .9rem }
"""
style += EXTRA_PAGE_CSS

# ---------- new feature pages ----------
JOURNEY_TOTAL = len(D.ERAS) + len(D.PEOPLE) + len(D.PLACES) + len(F.STORIES) + len(F.LEGENDS)
STORY = {x["id"]: x for x in F.STORIES}


def prose(pars, cls="prose"):
    # "## " sub-heading, "> quote | source" pull quote, "|| left | right" table row (rows in a run make one table)
    out, rows = "", []
    for a in pars + [""]:
        if a.startswith("|| "):
            rows.append(a[3:].split(" | ", 1))
            continue
        if rows:
            out += '<table class="kv"><tbody>' + "".join(f"<tr><th scope=\"row\">{e(r[0])}</th><td>{e(r[-1])}</td></tr>" for r in rows) + "</tbody></table>"
            rows = []
        if not a:
            continue
        if a.startswith("## "):
            out += f"<h2>{e(a[3:])}</h2>"
        elif a.startswith("> "):
            q, _, c = a[2:].partition(" | ")
            out += f'<blockquote class="pq"><p>{e(q)}</p>' + (f"<cite>{e(c)}</cite>" if c else "") + "</blockquote>"
        else:
            out += f"<p>{e(a)}</p>"
    return out


def story_links(kind, key):
    # long reads that list this person / place / event (fields people=, places=, events= in a story)
    return [x for x in F.STORIES if key in x.get(kind, [])]


def story_feature(kind, key):
    xs = story_links(kind, key)
    return section(f'<div class="s-grid">{"".join(story_card(x, True) for x in xs)}</div>', "The full story", "Y stori lawn") if xs else ""


def prose_bi(en, cy, cls="prose"):
    return f'<div class="{cls} l-en" lang="en">{prose(en)}</div><div class="{cls} l-cy" lang="cy">{prose(cy)}</div>'


def story_card(x, lead=False):
    return (f'<a class="s-card rv{" lead" if lead else ""}" href="story-{x["id"]}.html" data-era="{x["era"]}"><span class="art">{A.scene(x["art"], COL[x["era"]])}</span>'
            f'<span class="txt"><span class="span">{bi("Long read", "Erthygl")} · {x["mins"]} {bi("min", "mun")}</span><h3>{bi(x["en"], x["cy"])}</h3><p>{bi(x["sumEn"], x["sumCy"])}</p>'
            f'<span class="go">{bi("Read", "Darllen")} →</span></span></a>')


def legend_card(x):
    return (f'<a class="l-card rv" href="legend-{x["id"]}.html" data-era="{x["era"]}"><span class="art">{A.scene(x["art"], COL[x["era"]])}</span>'
            f'<span class="txt"><span class="span">{e(x["place"])}</span><h3>{bi(x["en"], x["cy"])}</h3><p>{bi(x["sumEn"], x["sumCy"])}</p></span></a>')


def story_page(x, i):
    nxt = F.STORIES[(i + 1) % len(F.STORIES)]
    others = [y for y in F.STORIES if y["id"] != x["id"]][:3]
    era = ERA[x["era"]]
    meta = f'<p class="byline"><span>{x["mins"]} {bi("minute read", "munud o ddarllen")}</span><a href="era-{x["era"]}.html">{bi(era["en"], era["cy"])}</a><button type="button" class="copy" data-copy="story-{x["id"]}.html">{bi("Copy link", "Copïo’r ddolen")}</button></p>'
    main = (hero(x["era"], f'<a href="index.html">{SITE}</a> / <a href="stories.html">{bi("Long reads", "Erthyglau")}</a>', "book", "Long read", "Erthygl", x["en"], x["cy"], x["sumEn"], x["sumCy"], art=x["art"])
            + f'<section class="article"><div class="wrap narrow">{meta}{prose_bi(x["pEn"], x["pCy"])}</div></section>'
            + section(f'<div class="s-grid three">{"".join(story_card(y) for y in others)}</div>', "Keep reading", "Daliwch ati i ddarllen")
            + section(f'<div class="pager"><a class="btn" href="stories.html">← {bi("All long reads", "Pob erthygl")}</a><a class="btn solid" href="story-{nxt["id"]}.html">{bi(nxt["en"], nxt["cy"])} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": x["en"], "description": x["sumEn"], "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page(f"story-{x['id']}.html", f'{x["en"]} · History of Wales', x["sumEn"], main, era=x["era"], ld=ld, active="stories.html", track=f"story:{x['id']}")


def stories_index():
    main = (hero("kings", f'<a href="index.html">{SITE}</a>', "book", "Long reads", "Erthyglau", "The stories behind the dates", "Y straeon y tu ôl i’r dyddiadau",
                 "Short essays on the big questions of Welsh history. Each takes about five minutes.", "Erthyglau byr ar gwestiynau mawr hanes Cymru. Tua phum munud yr un.", art="book")
            + section(f'<h2 class="sr-only">{bi("All long reads", "Pob erthygl")}</h2><div class="s-grid">{"".join(story_card(x, k == 0) for k, x in enumerate(F.STORIES))}</div>', top=True))
    return page("stories.html", "Long reads · History of Wales", "Essays on Welsh history: castles, the language, the laws of Hywel Dda, coal, protest and the Welsh across the world.", main, era="kings", og_type="website", active="stories.html")


def legend_page(x, i):
    nxt = F.LEGENDS[(i + 1) % len(F.LEGENDS)]
    main = (hero(x["era"], f'<a href="index.html">{SITE}</a> / <a href="legends.html">{bi("Legends", "Chwedlau")}</a>', "book", x["place"], x["place"], x["en"], x["cy"], x["sumEn"], x["sumCy"], art=x["art"])
            + f'<section class="article"><div class="wrap narrow">{prose_bi(x["pEn"], x["pCy"], "prose tale")}'
              f'<aside class="behind"><p class="eyebrow">{bi("The history behind the legend", "Yr hanes y tu ôl i’r chwedl")}</p><p>{bi(x["hEn"], x["hCy"])}</p></aside>'
              f'<p class="byline"><button type="button" class="copy" data-copy="legend-{x["id"]}.html">{bi("Copy link to share", "Copïo dolen i’w rhannu")}</button></p></div></section>'
            + section(f'<div class="pager"><a class="btn" href="legends.html">← {bi("All legends", "Pob chwedl")}</a><a class="btn solid" href="legend-{nxt["id"]}.html">{bi(nxt["en"], nxt["cy"])} →</a></div>'))
    return page(f"legend-{x['id']}.html", f'{x["en"]} · History of Wales', x["sumEn"], main, era=x["era"], active="legends.html", track=f"legend:{x['id']}")


def legends_index():
    main = (hero("medieval", f'<a href="index.html">{SITE}</a>', "book", "Legends", "Chwedlau", "Legends of Wales", "Chwedlau Cymru",
                 "Seven old tales, retold for reading aloud, each with the real history behind it.", "Saith hen chwedl, wedi’u hadrodd o’r newydd i’w darllen ar goedd, pob un â’r hanes go iawn y tu ôl iddi.", art="dragons")
            + section(f'<h2 class="sr-only">{bi("All legends", "Pob chwedl")}</h2><div class="l-grid">{"".join(legend_card(x) for x in F.LEGENDS)}</div>', top=True)
            + section(f'<div class="pager"><a class="btn" href="symbols.html">{bi("Symbols and traditions", "Symbolau a thraddodiadau")} →</a></div>'))
    return page("legends.html", "Legends · History of Wales", "The legends of Wales retold: the red dragon, Gelert, Cantre’r Gwaelod, Branwen, Blodeuwedd and Taliesin, with the history behind them.", main, era="medieval", og_type="website", active="legends.html")


def symbols_page():
    cards = "".join(f'<article class="sym rv" id="{s[0]}" data-era="{D.ERAS[i % len(D.ERAS)]["id"]}"><span class="sym-n">{i + 1:02d}</span><h2>{bi(s[3], s[1])}</h2>'
                    + (f'<p class="sym-alt">{bi(s[1], s[3])}</p>' if s[1] != s[3] else "") + f'<p>{bi(s[4], s[5])}</p></article>' for i, s in enumerate(F.SYMBOLS))
    main = (hero("modern", f'<a href="index.html">{SITE}</a>', "harp", "Symbols and traditions", "Symbolau a thraddodiadau", "The dragon, the leek and the grey mare", "Y ddraig, y genhinen a’r Fari Lwyd",
                 "Where the emblems and customs of Wales come from. Some are a thousand years old; some are younger than they look.", "O ble daw arwyddluniau ac arferion Cymru. Mae rhai’n fil o flynyddoedd oed; mae rhai’n iau nag y maent yn edrych.", art="dragons")
            + section(f'<div class="sym-grid">{cards}</div>', top=True)
            + section(f'<div class="pager"><a class="btn" href="legends.html">← {bi("Legends", "Chwedlau")}</a><a class="btn solid" href="stories.html">{bi("Long reads", "Erthyglau")} →</a></div>'))
    return page("symbols.html", "Symbols and traditions · History of Wales", "The red dragon, the leek, the daffodil, the harp, the Eisteddfod, lovespoons, the Mari Lwyd and more: where the symbols of Wales come from.", main, era="modern", og_type="website")


def gallery_page():
    figs = ""
    for pl in D.PLACES:
        ph = PH.PLACE_PHOTOS.get(pl["id"])
        if ph:
            figs += (f'<a class="g-item" href="place-{pl["id"]}.html" data-era="{pl["era"]}"><img src="{photo_url(ph[0], 800)}" alt="{e(ph[1])}" loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.closest(\'a\').remove()">'
                     f'<span class="cap"><b>{bi(pl["en"], pl["cy"])}</b><span>{e(pl["year"])}</span></span></a>')
    for p in D.PEOPLE:
        ph = PH.PERSON_PHOTOS.get(p[0])
        if ph:
            figs += (f'<a class="g-item tall" href="person-{p[0]}.html" data-era="{p[1]}"><img src="{photo_url(ph[0], 800)}" alt="{e(ph[1])}" loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.closest(\'a\').remove()">'
                     f'<span class="cap"><b>{bi(p[3], p[4])}</b><span>{e(p[2])}</span></span></a>')
    main = (hero("industrial", f'<a href="index.html">{SITE}</a>', "castle", "Photo gallery", "Oriel luniau", "Wales in pictures", "Cymru mewn lluniau",
                 "Castles, cromlechs, quarries and faces. Choose a picture to read its story.", "Cestyll, cromlechi, chwareli ac wynebau. Dewiswch lun i ddarllen ei stori.", art="castle")
            + section(f'<div class="gallery">{figs}</div><p class="muted" style="margin-top:1.5rem">{bi("Photographs from Wikimedia Commons under free licences. The photographer and licence are credited on each picture’s own page.", "Ffotograffau o Wikimedia Commons dan drwyddedau rhydd. Mae’r ffotograffydd a’r drwydded wedi’u cydnabod ar dudalen pob llun.")}</p>', top=True))
    return page("gallery.html", "Photo gallery · History of Wales", "Photographs of the historic places and people of Wales.", main, era="industrial", og_type="website")


GAMES = [
 ("daily.html", "daily", "Daily challenge", "Her y dydd", "One event, six guesses to find the year. A new one every day, and a streak to keep.", "Un digwyddiad, chwe chynnig i ddyfalu’r flwyddyn. Un newydd bob dydd, a rhediad i’w gadw.", "Every day", "Bob dydd", "medieval"),
 ("quiz.html", "quiz", "The quiz", "Y cwis", "Ten questions drawn from the timeline and the people. Every round is different.", "Deg cwestiwn o’r llinell amser a’r bobl. Mae pob rownd yn wahanol.", "10 questions", "10 cwestiwn", "kings"),
 ("map-game.html", "map", "Where in Wales?", "Ble yng Nghymru?", "Put castles, towns and battlefields on a blank map. How close can you get?", "Rhowch gestyll, trefi a meysydd brwydr ar fap gwag. Pa mor agos allwch chi fynd?", "5 rounds", "5 rownd", "modern"),
 ("quiz.html#game", "order", "Timeline challenge", "Her y llinell amser", "Put five events in order, oldest first.", "Rhowch bum digwyddiad yn eu trefn, yr hynaf yn gyntaf.", "3 rounds", "3 rownd", "industrial"),
 ("names.html", "names", "Welsh names", "Enwau Cymraeg", "What does your surname mean? And what would you have been called in the age of the princes?", "Beth yw ystyr eich cyfenw? A beth fyddai eich enw yn oes y tywysogion?", "Try your name", "Rhowch gynnig ar eich enw", "saints"),
 ("hero.html", "hero", "Which figure from history are you?", "Pa ffigwr o hanes ydych chi?", "Six questions to find your match among the people who shaped Wales.", "Chwe chwestiwn i ganfod eich tebyg ymhlith y bobl a luniodd Gymru.", "6 questions", "6 chwestiwn", "ancient"),
 ("pairs.html", "pairs", "Word pairs", "Parau geiriau", "A memory game for younger visitors: match the Welsh word to its meaning.", "Gêm gof i ymwelwyr iau: parwch y gair Cymraeg â’i ystyr.", "For children", "I blant", "modern"),
]


def play_cards():
    return "".join(f'<a class="p-card rv p-{g[1]}" href="{g[0]}" data-era="{g[8]}"><span class="tag">{bi(g[6], g[7])}</span><h3>{bi(g[2], g[3])}</h3><p>{bi(g[4], g[5])}</p><span class="go">{bi("Play", "Chwarae")} →</span></a>' for g in GAMES)


PLAY_DATA = dict(
    EV=[[ev[1], ev[2], ev[5], ev[6], ev[0], ev[7], ev[8], i] for i, ev in enumerate(D.EVENTS)],
    PL=[[p["id"], p["en"], p["cy"], p["lat"], p["lon"], p["era"]] for p in D.PLACES],
    TW=[list(t) for t in TW.TOWNS if t[0] not in ("Chester", "Shrewsbury", "Hereford")],
    MAPC=dict(minx=geo["minx"], maxy=geo["maxy"], k=geo["k"], sc=geo["sc"]),
    HEROES={k: [v[0], v[1], v[2], v[3], PERSON[k][3], PERSON[k][4], PERSON[k][2]] for k, v in F.HEROES.items()},
    HQ=[[q[0], q[1], [list(a) for a in q[2]]] for q in F.HERO_QS],
)


def game_page(path, kind, era, title_en, title_cy, sub_en, sub_cy, art, desc, with_map=False):
    data = dict(PLAY_DATA)
    if with_map:
        data["OUT"] = geo["outline"]
    main = (hero(era, f'<a href="index.html">{SITE}</a> / <a href="play.html">{bi("Play", "Chwarae")}</a>', "book", "Play", "Chwarae", title_en, title_cy, sub_en, sub_cy, art=art)
            + f'<section class="game-sec"><div class="wrap narrow"><div class="g-root" id="g-root" data-game="{kind}"><noscript>This game needs JavaScript.</noscript></div>'
              f'<p class="more-row"><a class="btn" href="play.html">← {bi("All games", "Pob gêm")}</a></p></div></section>')
    extra = f'<script>var PLAY={json.dumps(data, ensure_ascii=False, separators=(",", ":"))};</script>\n<script src="play.js" defer></script>\n'
    return page(path, f"{title_en} · History of Wales", desc, main, era=era, og_type="website", active="play.html", extra=extra)


def play_index():
    main = (hero("medieval", f'<a href="index.html">{SITE}</a>', "book", "Play", "Chwarae", "Test yourself", "Profwch eich hun",
                 "Seven games drawn from the history on this site. Scores, streaks and badges are kept on your own device.", "Saith gêm wedi’u seilio ar yr hanes ar y wefan hon. Cedwir sgoriau, rhediadau a bathodynnau ar eich dyfais eich hun.", art="dragons")
            + section(f'<h2 class="sr-only">{bi("All games", "Pob gêm")}</h2><div class="play-grid">{play_cards()}</div>', top=True)
            + section(f'<div class="pager"><a class="btn" href="journey.html">{bi("See your journey and badges", "Gweld eich taith a’ch bathodynnau")} →</a></div>'))
    return page("play.html", "Play · History of Wales", "Games on the history of Wales: a daily year challenge, quiz, map game, Welsh names and more.", main, era="medieval", og_type="website", active="play.html")


def journey_page():
    groups = [
        dict(k="era", en="Ages", cy="Oesoedd", items=[[x["id"], x["en"], x["cy"], f'era-{x["id"]}.html'] for x in D.ERAS]),
        dict(k="story", en="Long reads", cy="Erthyglau", items=[[x["id"], x["en"], x["cy"], f'story-{x["id"]}.html'] for x in F.STORIES]),
        dict(k="legend", en="Legends", cy="Chwedlau", items=[[x["id"], x["en"], x["cy"], f'legend-{x["id"]}.html'] for x in F.LEGENDS]),
        dict(k="person", en="People", cy="Pobl", items=[[p[0], p[3], p[4], f"person-{p[0]}.html"] for p in D.PEOPLE]),
        dict(k="place", en="Places", cy="Lleoedd", items=[[p["id"], p["en"], p["cy"], f'place-{p["id"]}.html'] for p in D.PLACES]),
    ]
    main = (hero("kings", f'<a href="index.html">{SITE}</a>', "crown", "Your journey", "Eich taith", "Your journey through Welsh history", "Eich taith drwy hanes Cymru",
                 "Every age, person, place, legend and essay you read is ticked off here, and games earn badges. Nothing leaves your device.", "Mae pob oes, person, lle, chwedl ac erthygl a ddarllenwch yn cael ei thicio yma, ac mae gemau’n ennill bathodynnau. Nid oes dim yn gadael eich dyfais.", art="sword")
            + f'<section><div class="wrap"><div id="journey-root"><noscript>Your journey needs JavaScript.</noscript></div></div></section>')
    extra = f'<script>var JOURNEY={json.dumps(groups, ensure_ascii=False, separators=(",", ":"))};</script>\n'
    return page("journey.html", "Your journey · History of Wales", "Track what you have read and the badges you have earned on History of Wales.", main, era="kings", og_type="website", extra=extra)


# ---------- kings and princes (src/royal.py) ----------
REALM = {r["id"]: r for r in RY.REALMS}


def cy_dates(s):
    return s.replace("fl. c. ", "fl. tua ").replace("c. ", "tua ").replace("d. ", "m. ")


def realm_title(r):
    return (f"Kings and princes of {r['en']}", f"Brenhinoedd a thywysogion {r['cy']}")


# person and place pages link back to every kingdom list they appear in
REALMS_OF = {}
for _r in RY.REALMS:
    for _x in _r["rulers"]:
        if _x["k"] == "r" and _x["link"]:
            REALMS_OF.setdefault(_x["link"], []).append(_r["id"])
    for _pid in _r["places"]:
        REALMS_OF.setdefault(f"place-{_pid}.html", []).append(_r["id"])


def realm_links(href):
    ids = list(dict.fromkeys(REALMS_OF.get(href, [])))
    if not ids:
        return ""
    return "".join(f'<a href="kings-{i}.html">{bi(*realm_title(REALM[i]))} →</a>' for i in ids)


def ruler_li(x, chips=""):
    link = x["link"]
    more = ""
    if link:
        lab = ("Read more", "Darllen mwy") if link.startswith(("person-", "legend-")) else ("See more", "Gweld mwy")
        more = f'<a class="src" href="{link}">{bi(*lab)} →</a>'
    note = f'<p>{bi(x["en"], x["cy"])}</p>' if x["en"] else ""
    links = f'<div class="links">{more}{chips}</div>' if (more or chips) else ""
    return (f'<li class="{"key" if x["key"] else ""}"><time>{bi(x["dates"], cy_dates(x["dates"]))}</time>'
            f'<div><h3>{e(x["name"])}</h3>{note}{links}</div></li>')


def ruler_list(items):
    out, cur = "", []
    def flush():
        return f'<ol class="era-events royal">{"".join(cur)}</ol>' if cur else ""
    for x in items:
        if x["k"] == "h":
            out += flush(); cur = []
            out += f'<h2 class="sub-h royal-h">{bi(x["en"], x["cy"])}</h2>'
        elif x["k"] == "n":
            cur.append(f'<li class="gap"><time aria-hidden="true">· · ·</time><div><p>{bi(x["en"], x["cy"])}</p></div></li>')
        else:
            cur.append(ruler_li(x))
    return out + flush()


def realm_tile(r):
    n = sum(1 for x in r["rulers"] if x["k"] == "r")
    return (f'<a href="kings-{r["id"]}.html" data-era="{r["era"]}"><svg aria-hidden="true"><use href="#i-crown"/></svg>'
            f'<span><b>{bi(r["en"], r["cy"])}</b><span>{bi(r["span"] + f" · {n} rulers", cy_dates(r["span"]) + f" · {n} o reolwyr")}</span></span></a>')


ROYAL_NOTE = bi("Dates marked c. are approximate. For the earliest kings the old royal genealogies and the charters of the Book of Llandaff are the main witnesses, and their dates are estimates. Where kings shared a kingdom, both are listed.",
                "Dyddiadau bras yw’r rhai a nodir ‘tua’. I’r brenhinoedd cynharaf, yr hen achau brenhinol a siarteri Llyfr Llandaf yw’r prif dystion, ac amcangyfrif yw eu dyddiadau. Lle rhannodd brenhinoedd deyrnas, rhestrir y ddau.")
ROYAL_CSS = """
.royal-h { margin-top: 2.6rem }
.era-events.royal li.gap { padding: .7rem 0 }
.era-events.royal li.gap p { font-style: italic; color: var(--muted) }
.era-events.royal li.gap time { color: var(--muted) }
.era-events .links .chip { font-family: var(--f-mono); font-size: .75rem; color: var(--muted); border: 1px solid var(--line); border-radius: 99px; padding: .1rem .6rem; text-decoration: none }
.era-events .links .chip:hover { color: var(--ink); border-color: var(--c) }
.one-king { margin-top: 0 }
.one-king h2 { font-family: var(--f-display); font-weight: 400; font-size: clamp(1.8rem, 4vw, 2.6rem); line-height: 1.1 }
.one-king .go { font-weight: 700 }
.realm-links { display: flex; flex-wrap: wrap; gap: .5rem 1.2rem; margin: -.8rem 0 1.5rem; font-size: .95rem }
"""
style += ROYAL_CSS
CY_ORD = {5: "5ed", 6: "6ed", 7: "7fed", 8: "8fed", 9: "9fed", 10: "10fed", 11: "11eg", 12: "12fed", 13: "13eg", 14: "14eg", 15: "15fed"}


def realm_page(r, i):
    t_en, t_cy = realm_title(r)
    nxt = RY.REALMS[(i + 1) % len(RY.REALMS)]
    places = [PLACE[p] for p in r["places"] if p in PLACE]
    main = (hero(r["era"], f'<a href="index.html">{SITE}</a> / <a href="kings.html">{bi("Kings and princes", "Brenhinoedd a thywysogion")}</a>', "crown",
                 r["span"], cy_dates(r["span"]), t_en, t_cy, r["subEn"], r["subCy"], art=r["art"])
            + section(paras(r["introEn"], r["introCy"]) + ft_link_for_realm(r["id"]), top=True)
            + section(ruler_list(r["rulers"]) + f'<p class="note-box" style="margin-top:2rem">{ROYAL_NOTE}</p>', *(() if r["rulers"][0]["k"] == "h" else ("The rulers, in order", "Y rheolwyr, yn eu trefn")))
            + (section(f'<div class="era-places">{"".join(place_tile(p) for p in places)}</div>', "Places to visit", "Lleoedd i ymweld â nhw") if places else "")
            + section(f'<div class="pager"><a class="btn" href="kings.html">← {bi("All the kings and princes of Wales", "Holl frenhinoedd a thywysogion Cymru")}</a>'
                      f'<a class="btn solid" href="kings-{nxt["id"]}.html">{bi(nxt["en"], nxt["cy"])} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": t_en, "description": r["subEn"], "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page(f"kings-{r['id']}.html", f"{t_en} · History of Wales", f"Every king and prince of {r['en']}, in order with their dates. {r['subEn']}", main, era=r["era"], ld=ld, active="kings.html", track=f"kings:{r['id']}")


# where a ruler held several kingdoms, the entry shown in the combined list
HOME_REALM = {"Cunedda Wledig": "gwynedd", "Hywel Dda": "deheubarth", "Maredudd ab Owain": "deheubarth", "Rhydderch ab Iestyn": "glywysing", "Gruffudd ap Rhydderch": "gwent"}


def all_rulers():
    """Every ruler from every kingdom, once each, oldest first, with the kingdoms they ruled."""
    seen = {}
    for r in RY.REALMS:
        for x in r["rulers"]:
            if x["k"] != "r":
                continue
            k = x["name"]
            if k in seen:
                if r["id"] not in seen[k][1]:
                    seen[k][1].append(r["id"])
                if HOME_REALM.get(k) == r["id"]:
                    seen[k][0] = x
            else:
                seen[k] = [x, [r["id"]]]
    return sorted(seen.values(), key=lambda v: v[0]["y"])


def kings_page():
    def lst(items):
        return f'<ol class="era-events royal">{"".join(ruler_li(x) for x in items)}</ol>'
    every = ""
    cent = None
    cur = []
    for x, rids in all_rulers():
        c = int(x["y"]) // 100 + 1
        if c != cent:
            if cur:
                every += f'<ol class="era-events royal">{"".join(cur)}</ol>'
            cur = []
            cent = c
            every += f'<h3 class="sub-h royal-h" style="font-size:1.5rem">{bi(f"{c}th century", f"Y {CY_ORD.get(c, str(c))} ganrif")}</h3>'
        chips = "".join(f'<a class="chip" href="kings-{i}.html">{bi(REALM[i]["en"], REALM[i]["cy"])}</a>' for i in rids)
        cur.append(ruler_li(x, chips))
    every += f'<ol class="era-events royal">{"".join(cur)}</ol>' if cur else ""
    n_all = len(all_rulers())
    one = (f'<aside class="behind one-king"><p class="eyebrow">{bi("1055–1063 · One king of all Wales", "1055–1063 · Un brenin ar Gymru gyfan")}</p>'
           f'<h2>{bi("Gruffudd ap Llywelyn, King of Wales", "Gruffudd ap Llywelyn, Brenin Cymru")}</h2>'
           + paras(RY.GRUFFUDD["en"], RY.GRUFFUDD["cy"]) +
           f'<p><a class="go" href="person-gruffudd-ap-llywelyn.html">{bi("Read his story", "Darllen ei hanes")} →</a> &nbsp; <a class="go" href="index.html#map">{bi("See his Wales on the kingdoms map", "Gweld ei Gymru ar fap y teyrnasoedd")} →</a></p></aside>')
    main = (hero("kings", f'<a href="index.html">{SITE}</a>', "crown", "c. 450–1415", "tua 450–1415", "Kings and princes of Wales", "Brenhinoedd a thywysogion Cymru",
                 "For a thousand years Wales was a land of kingdoms. Great kings brought most of it together, one king ruled it all, and its princes carried the title Prince of Wales.",
                 "Am fil o flynyddoedd gwlad o deyrnasoedd oedd Cymru. Daeth brenhinoedd mawr â’r rhan fwyaf ohoni ynghyd, rheolodd un brenin y cyfan, a dygodd ei thywysogion y teitl Tywysog Cymru.", art="castle")
            + section(one, top=True)
            + section(lst(RY.MOST), "Kings who ruled most of Wales", "Brenhinoedd a reolodd y rhan fwyaf o Gymru")
            + section('<span id="princes"></span>' + lst(RY.PRINCES) + f'<p class="lede" style="margin-top:1.5rem">{bi(RY.CODA["en"], RY.CODA["cy"])} <a href="person-harri-tudur.html">{bi("Harri Tudur", "Harri Tudur")} →</a></p>', "Princes of Wales", "Tywysogion Cymru")
            + section(f'<aside class="behind one-king"><p class="eyebrow">{bi("Rhodri Mawr to Harri Tudur", "Rhodri Mawr i Harri Tudur")}</p><h2>{bi("Royal family trees", "Coed teulu brenhinol")}</h2>'
                      f'<p>{bi("The royal houses of Wales were one great family. See how Gwynedd, Deheubarth, Powys and Gwent married into one another, and how their blood came to the throne at Bosworth with Harri Tudur. Tap anyone to light up their line.", "Un teulu mawr oedd tai brenhinol Cymru. Gwelwch sut y priododd Gwynedd, Deheubarth, Powys a Gwent â’i gilydd, a sut y daeth eu gwaed i’r orsedd yn Bosworth gyda Harri Tudur. Tapiwch unrhyw un i oleuo’i linach.")}</p>'
                      f'<p><a class="go" href="family-trees.html">{bi("See the family trees", "Gweld y coed teulu")} →</a></p></aside>')
            + section(f'<div class="era-places">{"".join(realm_tile(r) for r in RY.REALMS if r.get("group") != "north")}</div>', "The kingdoms, one by one", "Y teyrnasoedd, fesul un")
            + section(f'<span id="old-north"></span><p class="lede" style="margin-bottom:1.5rem">{bi(RY.NORTH_INTRO["en"], RY.NORTH_INTRO["cy"])}</p><div class="era-places">{"".join(realm_tile(r) for r in RY.REALMS if r.get("group") == "north")}</div>', "The Old North: Yr Hen Ogledd", "Yr Hen Ogledd")
            + section(f'<p class="lede">{bi(f"All {n_all} kings, princes and lords on this site, from every kingdom, oldest first. Tap a kingdom to see its own line.", f"Pob un o’r {n_all} o frenhinoedd, tywysogion ac arglwyddi ar y wefan hon, o bob teyrnas, yr hynaf yn gyntaf. Tapiwch deyrnas i weld ei llinach ei hun.")}</p>'
                      + every + f'<p class="note-box" style="margin-top:2rem">{ROYAL_NOTE}</p>', "Every king and prince, in order", "Pob brenin a thywysog, yn eu trefn"))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": "Kings and princes of Wales", "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page("kings.html", "Kings and princes of Wales · History of Wales",
                "Every king and prince of Wales, kingdom by kingdom: Gwynedd, Powys, Deheubarth, Dyfed, Gwent, Glywysing and more, and Gruffudd ap Llywelyn, king of all Wales.",
                main, era="kings", ld=ld, og_type="website", active="kings.html", track="kings:all")


# ---------- royal family trees (src/trees.py) ----------
import re as _re


def _ft_slug(s):
    s = s.lower().replace("ŵ", "w").replace("â", "a").replace("ô", "o").replace("’", "")
    return _re.sub(r"[^a-z0-9]+", "-", s).strip("-")


FT_IDS = {}       # node id -> node
FT_PERSON = {}    # person-x.html -> node id (first place the person appears with a link)
FT_TREE_OF = {}   # node id -> tree id


def _ft_index():
    def walk(n, tid):
        n["id"] = n["id"] or _ft_slug(n["name"][0])
        assert n["id"] not in FT_IDS, n["id"]
        FT_IDS[n["id"]] = n
        FT_TREE_OF[n["id"]] = tid
        if n["link"]:
            FT_PERSON.setdefault(n["link"], n["id"])
        for k in n["kids"]:
            walk(k, tid)
    for t in TR.TREES:
        walk(t["root"], t["id"])


_ft_index()
FT_GEN = {"glyndyfrdwy": 2, "gwent-kings": 0}  # gap rows: how many generations they stand for (0 = not known)


def ft_href(a):
    a = a.lstrip("#")
    return f"#ft-{a}" if a in FT_IDS else f"#{a}"


def ft_card(n):
    crown = '<svg class="ft-crown" aria-hidden="true"><use href="#i-crown"/></svg>' if n["crown"] else ""
    d = f'<span class="ft-d">{bi(n["dates"], cy_dates(n["dates"]))}</span>' if n["dates"] else ""
    role = f'<span class="ft-role">{bi(*n["role"])}</span>' if n["role"][0] else ""
    note = f'<p class="ft-note">{bi(*n["note"])}</p>' if n["note"][0] else ""
    links = ""
    if n["link"]:
        links += f'<a href="{n["link"]}">{bi("Read more", "Darllen mwy")} →</a>'
    if n["goto"]:
        a, en, cy = n["goto"]
        links += f'<a class="ft-go" href="{ft_href(a)}">↪ {bi(en, cy)}</a>'
    links = f'<span class="ft-links">{links}</span>' if links else ""
    g = FT_GEN.get(n["id"], 1)
    return (f'<div class="ft-card{" crown" if n["crown"] else ""}{" gap" if n["gap"] else ""}" id="ft-{n["id"]}" data-en="{e(n["name"][0])}" data-cy="{e(n["name"][1])}" data-g="{g}">'
            f'{d}<button type="button" class="ft-nm" aria-label="{e(n["name"][0])}: show the line / dangos y llinach">{crown}{bi(*n["name"])}</button>{role}{note}{links}</div>')


def ft_node(n):
    kids = n["kids"]
    sub = ""
    if kids:
        sub = f'<ul class="ft-kids{" one" if len(kids) == 1 else ""}">{"".join(ft_node(k) for k in kids)}</ul>'
    return f'<li class="ft-n">{ft_card(n)}{sub}</li>'


FT_CSS = """
.ft-jump { display: flex; flex-wrap: wrap; gap: .5rem; margin-top: 1.4rem }
.ft-jump a { font: 500 .8rem var(--f-mono); color: var(--ink); text-decoration: none; border: 1px solid var(--line); border-radius: 99px; padding: .35rem .85rem; background: var(--card) }
.ft-jump a:hover { border-color: var(--gold); color: var(--gold) }
.ft-how { display: flex; flex-wrap: wrap; gap: .4rem 1.4rem; margin-top: 1.2rem; font-size: .9rem; color: var(--muted) }
.ft-how svg { width: 1em; height: 1em; vertical-align: -.12em; fill: var(--gold); color: var(--gold) }
.ft-sec .lede { max-width: 46rem }
.ft-tog { background: transparent; color: var(--ink); border: 1px solid var(--line); border-radius: 99px; padding: .2rem .8rem; font: inherit; font-size: .85rem; cursor: pointer }
.ft-tog[aria-pressed="true"] { border-color: var(--gold); color: var(--gold) }
.ft-compact .ft-note, .ft-compact .ft-role { display: none }
.ft-sec .realm-links { margin: .2rem 0 1.6rem }
.ft-tree { --ind: .3rem; --arm: .75rem; margin-top: 1.4rem }
.ft, .ft-kids { list-style: none; margin: 0; padding: 0 }
.ft-kids { padding-left: var(--ind) }
.ft-kids > li { position: relative; padding: .55rem 0 0 var(--arm) }
.ft-kids > li::before { content: ""; position: absolute; left: 0; top: 0; bottom: 0; border-left: 2px solid color-mix(in srgb, var(--c) 45%, var(--line)) }
.ft-kids > li:last-child::before { bottom: auto; height: 1.75rem }
.ft-kids > li::after { content: ""; position: absolute; left: 0; top: 1.75rem; width: var(--arm); border-top: 2px solid color-mix(in srgb, var(--c) 45%, var(--line)) }
.ft-kids.one { padding-left: 0 }
.ft-kids.one > li { padding: 1.1rem 0 0 }
.ft-kids.one > li::before { left: calc(var(--ind) + var(--arm) / 2); height: 1.1rem; bottom: auto }
.ft-kids.one > li::after { display: none }
.ft-card { position: relative; max-width: 36rem; background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: .65rem .9rem .7rem; cursor: pointer;
  transition: opacity .3s, border-color .3s, box-shadow .3s; scroll-margin-top: 6rem }
.ft-card.crown { border-left: 3px solid var(--c) }
.ft-card.gap { background: transparent; border-style: dashed }
.ft-card.gap .ft-nm { font-style: italic; color: var(--muted) }
.ft-d { display: block; font: 500 .7rem var(--f-mono); letter-spacing: .05em; color: var(--muted) }
.ft-nm { all: unset; display: inline; cursor: pointer; font-family: var(--f-display); font-size: 1.22rem; line-height: 1.2; color: var(--ink); word-spacing: .04em }
.ft-nm:focus-visible { outline: 2px solid var(--gold); outline-offset: 3px; border-radius: 4px }
.ft-crown { width: .9em; height: .9em; margin-right: .3em; vertical-align: -.08em; color: var(--gold); fill: var(--gold) }
.ft-role { display: block; font-size: .85rem; color: var(--c); margin-top: .1rem }
.ft-note { margin: .35rem 0 0; font-size: .9rem; line-height: 1.55; color: #c9ccd4 }
.ft-links { display: flex; flex-wrap: wrap; gap: .2rem 1rem; margin-top: .4rem; font-size: .85rem }
.ft-links a { font-weight: 600 }
.ft-tree.tracing .ft-card:not(.lit) { opacity: .4 }
.ft-card.lit { border-color: var(--gold); box-shadow: 0 0 0 1px var(--gold), 0 6px 26px rgba(232,198,90,.18) }
.ft-card.me { box-shadow: 0 0 0 2px var(--gold), 0 8px 34px rgba(232,198,90,.3) }
.ft-card:target { animation: ftpulse 2.2s var(--ease) 1 }
@keyframes ftpulse { 0%, 60% { box-shadow: 0 0 0 3px var(--gold) } 100% { box-shadow: none } }
.ft-bar { position: fixed; left: 50%; bottom: max(1rem, env(safe-area-inset-bottom)); transform: translateX(-50%); z-index: 40; width: min(34rem, calc(100% - 2rem));
  display: flex; gap: .8rem; align-items: center; background: #1d2333; border: 1px solid var(--gold); border-radius: 16px; padding: .7rem .8rem .7rem 1rem; box-shadow: 0 10px 40px rgba(0,0,0,.5); font-size: .92rem }
.ft-bar[hidden] { display: none }
.ft-bar p { margin: 0; flex: 1; line-height: 1.4 }
.ft-bar button { flex: none; background: transparent; color: var(--ink); border: 1px solid var(--line); border-radius: 99px; padding: .3rem .8rem; font: inherit; cursor: pointer }
.ft-wed { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 16rem), 1fr)); gap: .9rem; margin-top: 1.2rem }
.ft-wed a { display: grid; gap: .45rem; align-content: start; text-decoration: none; color: var(--ink); background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.1rem; transition: transform .3s var(--ease), border-color .2s }
.ft-wed a:hover { transform: translateY(-3px); border-color: var(--gold) }
.ft-wed .hs { display: flex; align-items: center; gap: .45rem; font: 600 .7rem var(--f-mono); letter-spacing: .06em; text-transform: uppercase; color: var(--gold) }
.ft-wed .hs i { font-style: normal; color: var(--muted) }
.ft-wed p { margin: 0; font-size: .92rem; line-height: 1.55; color: #c9ccd4 }
.road { display: grid; gap: 0 1.2rem; margin-top: 1.6rem; grid-template-columns: 1fr;
  grid-template-areas: "t" "r" "j1" "m" "l" "j2" "e" }
.rd-col h3 { font: 600 .72rem var(--f-mono); letter-spacing: .06em; text-transform: uppercase; color: var(--gold); margin: 1.4rem 0 .6rem; text-align: center }
.rd-chain { list-style: none; margin: 0 auto; padding: 0; max-width: 21rem; display: grid; gap: 1.2rem }
.rd-chain li { position: relative; background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: .5rem .8rem; text-align: center }
.rd-chain li + li::before { content: ""; position: absolute; left: 50%; top: -1.25rem; height: 1.2rem; border-left: 2px solid var(--gold); opacity: .7 }
.rd-chain li.gap { background: transparent; border-style: dashed; font-style: italic; color: var(--muted); font-size: .88rem }
.rd-chain b { display: block; font-family: var(--f-display); font-weight: 400; font-size: 1.1rem; line-height: 1.2 }
.rd-chain b a { color: var(--ink); text-decoration: none; border-bottom: 1px solid color-mix(in srgb, var(--gold) 55%, transparent) }
.rd-chain .dt { display: block; font: 500 .68rem var(--f-mono); color: var(--muted) }
.rd-chain small { display: block; font-size: .8rem; color: #c9ccd4; margin-top: .1rem }
.rd-join { position: relative; text-align: center; padding: 1.4rem 0 1.2rem; color: var(--gold); font-size: .9rem; font-style: italic }
.rd-join::before { content: "↓"; display: block; font-style: normal; font-size: 1.2rem; line-height: 1; margin-bottom: .3rem }
.rd-end { text-align: center; margin-top: .4rem; background: radial-gradient(ellipse at 50% 0, rgba(232,198,90,.14), transparent 70%), var(--card); border: 1px solid var(--gold); border-radius: 20px; padding: 1.4rem 1.2rem }
.rd-end h3 { font-family: var(--f-display); font-weight: 400; font-size: clamp(1.5rem, 3.4vw, 2.2rem); line-height: 1.15; margin: 0 0 .5rem }
.rd-end p { max-width: 40rem; margin: .4rem auto 0; color: #d0d3da; line-height: 1.65 }
.rd-kids { display: flex; flex-wrap: wrap; justify-content: center; gap: .6rem; margin-top: 1rem }
.rd-kids > span { border: 1px solid var(--line); border-radius: 99px; padding: .3rem .9rem; font-size: .88rem; background: var(--slate) }
@media (min-width: 860px) {
  .ft-tree { --ind: 1.1rem; --arm: 1.3rem }
  .road { grid-template-columns: 1fr 1fr 1fr 1fr; grid-template-areas: "t r l l" "j1 j1 l l" "m m l l" "j2 j2 j2 j2" "e e e e" }
  .rd-join { padding-top: 2.6rem }
  .rd-join::before { content: ""; position: absolute; top: 0; left: 25%; right: 25%; height: 1.1rem; margin: 0; border: 2px solid var(--gold); border-top: 0; border-radius: 0 0 14px 14px; opacity: .8 }
  .rd-join::after { content: ""; position: absolute; top: 1.1rem; left: 50%; height: 1.3rem; border-left: 2px solid var(--gold); opacity: .8 }
  .rd-join.j2 { padding-top: 3rem }
  .rd-join.j2::after { height: 1.7rem }
  .rd-col.l .rd-chain { gap: 1.2rem }
}
@media print { .ft-bar { display: none !important } .ft-tree.tracing .ft-card { opacity: 1 } }
"""
style += FT_CSS

FT_JS = r"""<script>(function(){var bar=document.getElementById("ft-bar"),msg=document.getElementById("ft-msg"),cur=null;
function cy(){return document.documentElement.classList.contains("cy")}
function clear(){document.querySelectorAll(".ft-tree.tracing").forEach(function(t){t.classList.remove("tracing")});document.querySelectorAll(".ft-card.lit").forEach(function(c){c.classList.remove("lit","me")});bar.hidden=true;cur=null}
function trace(c,quiet){clear();var t=c.closest(".ft-tree");if(!t)return;var li=c.parentElement,n=0,known=true,root=c;c.classList.add("me");
while(li&&li.classList.contains("ft-n")){var k=li.firstElementChild;k.classList.add("lit");root=k;if(k!==c){var g=+k.dataset.g;if(!g)known=false;n+=g}li=li.parentElement.closest(".ft-n")}
t.classList.add("tracing");cur=c;var w=cy(),nm=c.dataset[w?"cy":"en"],rn=root.dataset[w?"cy":"en"];
msg.textContent=c===root?(w?nm+": sylfaenydd y llinach hon.":nm+": the founder of this line."):(known?(w?nm+": "+n+" cenhedlaeth ar ôl "+rn+".":nm+": "+n+(n===1?" generation":" generations")+" from "+rn+"."):(w?nm+", o linach "+rn+".":nm+", of the line of "+rn+"."));
bar.hidden=false}
document.addEventListener("click",function(ev){var tg=ev.target.closest("#ft-compact");if(tg){var on=document.body.classList.toggle("ft-compact");tg.setAttribute("aria-pressed",on);return}if(ev.target.closest("#ft-clear")){clear();return}if(ev.target.closest("a"))return;var c=ev.target.closest(".ft-card");if(c){if(c===cur){clear()}else trace(c)}});
document.addEventListener("keydown",function(ev){if(ev.key==="Escape"&&cur)clear()});
function fromHash(){var h=location.hash.slice(1);if(!h)return;var c=document.getElementById(h);if(c&&c.classList.contains("ft-card"))trace(c)}
addEventListener("hashchange",fromHash);fromHash();
var lb=document.getElementById("lang-cy"),le=document.getElementById("lang-en");[lb,le].forEach(function(b){b&&b.addEventListener("click",function(){if(cur)trace(cur)})});})();</script>
"""


def ft_road():
    R = TR.ROAD
    def step(s):
        en, cy, dates, nen, ncy, link = s
        if dates is None:
            return f'<li class="gap">{bi(en, cy)}</li>'
        nm = bi(en, cy)
        if link:
            nm = f'<a href="{ft_href(link) if link.startswith("#") else link}">{nm}</a>'
        return (f'<li><b>{nm}</b>' + (f'<span class="dt">{bi(dates, cy_dates(dates))}</span>' if dates else "")
                + (f'<small>{bi(nen, ncy)}</small>' if nen else "") + "</li>")
    def col(key, area):
        c = R[key]
        return f'<div class="rd-col {area}" style="grid-area:{area}"><h3>{bi(c["en"], c["cy"])}</h3><ol class="rd-chain">{"".join(step(s) for s in c["steps"])}</ol></div>'
    joined = f'<div class="rd-col m" style="grid-area:m"><ol class="rd-chain">{"".join(step(s) for s in R["joined"])}</ol></div>'
    j1 = f'<p class="rd-join" style="grid-area:j1">{bi("Tudur ap Goronwy married Marged ferch Tomas", "Priododd Tudur ap Goronwy â Marged ferch Tomas")}</p>'
    j2 = f'<p class="rd-join j2" style="grid-area:j2">{bi("Harri Tudur married Elizabeth of York, 18 January 1486", "Priododd Harri Tudur ag Elisabeth o Efrog, 18 Ionawr 1486")}</p>'
    kids = [("Arthur, Prince of Wales", "Arthur, Tywysog Cymru"), ("Margaret, Queen of Scots", "Marged, Brenhines yr Alban"), ("Henry VIII", "Harri VIII"), ("Mary, Queen of France", "Mari, Brenhines Ffrainc")]
    end = (f'<div class="rd-end" style="grid-area:e"><h3>{bi("Three lines meet on the throne", "Tair llinach yn cwrdd ar yr orsedd")}</h3>'
           f'<p>{bi("In the children of Harri Tudur and Elizabeth of York, the blood of Llywelyn Fawr, of the Lord Rhys and of Ednyfed Fychan came together. Their daughter Margaret was the great-grandmother of James VI and I, and every king and queen since 1603 descends from her, and so from the royal houses of Wales.", "Ym mhlant Harri Tudur ac Elisabeth o Efrog, daeth gwaed Llywelyn Fawr, yr Arglwydd Rhys ac Ednyfed Fychan ynghyd. Eu merch Marged oedd hen fam-gu Iago VI a I, ac mae pob brenin a brenhines ers 1603 yn disgyn ohoni hi, ac felly o dai brenhinol Cymru.")}</p>'
           f'<div class="rd-kids">{"".join(f"<span>{bi(a, b)}</span>" for a, b in kids)}</div></div>')
    return f'<div class="road">{col("tudur", "t")}{col("rhys", "r")}{j1}{joined}{col("llywelyn", "l")}{j2}{end}</div>'


FT_REALM_TREE = {"gwynedd": "gwynedd", "deheubarth": "deheubarth", "ceredigion": "deheubarth", "powys": "powys", "glywysing": "gwent", "gwent": "gwent"}
FT_TREE = {t["id"]: t for t in TR.TREES}


def ft_link_for_realm(rid):
    t = FT_TREE.get(FT_REALM_TREE.get(rid, ""))
    if not t:
        return ""
    return f'<p class="realm-links" style="margin-top:1.4rem"><a href="family-trees.html#tree-{t["id"]}">{bi("Family tree of " + t["en"].split(": ")[-1], "Coeden deulu " + t["cy"].split(": ")[-1])} →</a></p>'


def ft_link_for_person(href):
    i = FT_PERSON.get(href)
    return f'<a href="family-trees.html#ft-{i}">{bi("In the royal family trees", "Yn y coed teulu brenhinol")} →</a>' if i else ""


def family_trees_page():
    jump = "".join(f'<a href="#tree-{t["id"]}">{bi(t["en"].split(":")[0], t["cy"].split(":")[0])}</a>' for t in TR.TREES)
    jump += f'<a href="#marriages">{bi("The marriages", "Y priodasau")}</a><a href="#bosworth">{bi("The road to Bosworth", "Y ffordd i Bosworth")}</a>'
    how = (f'<p class="ft-how"><span><svg aria-hidden="true"><use href="#i-crown"/></svg> {bi("ruled a kingdom", "rheolodd deyrnas")}</span>'
           f'<span>{bi("Tap a name to light up the line back to the founder", "Tapiwch enw i oleuo’r llinach yn ôl at y sylfaenydd")}</span>'
           f'<span>↪ {bi("the same family in another tree", "yr un teulu mewn coeden arall")}</span>'
           f'<button type="button" class="ft-tog" id="ft-compact" aria-pressed="false">{bi("Names only", "Enwau yn unig")}</button></p>')
    intro = paras(["Wales was ruled for six hundred years by a handful of royal houses, and they were one great family. Rhodri Mawr’s sons founded the houses of Gwynedd and Deheubarth; his great-great-granddaughter Angharad was the mother of the first king of the house of Powys. Princes married princesses from the other kingdoms again and again, so that Llywelyn Fawr, the Lord Rhys and Owain Glyndŵr were all cousins many times over.",
                   "Then, in 1485, a grandson of Owain Tudur of Ynys Môn, with the blood of Deheubarth in his veins, won the crown at Bosworth under the red dragon. These trees follow the lines that carried the crown, from Rhodri Mawr to Harri Tudur."],
                  ["Am chwe chan mlynedd rheolwyd Cymru gan lond llaw o dai brenhinol, ac un teulu mawr oedden nhw. Sefydlodd meibion Rhodri Mawr dai Gwynedd a Deheubarth; ei or-or-wyres Angharad oedd mam brenin cyntaf tŷ Powys. Priododd tywysogion â thywysogesau o’r teyrnasoedd eraill dro ar ôl tro, fel bod Llywelyn Fawr, yr Arglwydd Rhys ac Owain Glyndŵr i gyd yn gefndryd lawer gwaith drosodd.",
                   "Yna, yn 1485, enillodd ŵyr i Owain Tudur o Ynys Môn, a gwaed Deheubarth yn ei wythiennau, y goron yn Bosworth dan y ddraig goch. Mae’r coed hyn yn dilyn y llinachau a ddygodd y goron, o Rhodri Mawr i Harri Tudur."])
    trees = ""
    for t in TR.TREES:
        kl = f'<p class="realm-links"><a href="kings-{t["realm"]}.html">{bi(*realm_title(REALM[t["realm"]]))}, {bi("in order", "yn eu trefn")} →</a></p>' if t["realm"] else ""
        trees += (f'<section class="tight ft-sec" id="tree-{t["id"]}" data-era="{t["era"]}"><div class="wrap"><h2 class="sub-h">{bi(t["en"], t["cy"])}</h2>'
                  f'<p class="lede">{bi(t["introEn"], t["introCy"])}</p>{kl}<div class="ft-tree"><ul class="ft">{ft_node(t["root"])}</ul></div></div></section>')
    wed = "".join(f'<a href="{ft_href(a)}"><span class="hs">{e(x)} <i>+</i> {e(y)}</span><p>{bi(en, cy)}</p></a>' for x, y, en, cy, a in TR.MARRIAGES)
    note = bi("The trees follow the medieval Welsh royal genealogies, such as those in Harley MS 3859 and Jesus College MS 20, and the chronicles. For the early generations they are the only witness, and dates marked c. are estimates. Not every child is shown: the trees follow the lines that carried the crown and the marriages that joined the houses.",
              "Mae’r coed yn dilyn achau brenhinol Cymreig yr Oesoedd Canol, megis y rhai yn llawysgrif Harley 3859 a llawysgrif Coleg Iesu 20, a’r croniclau. I’r cenedlaethau cynnar hwy yw’r unig dyst, ac amcangyfrif yw’r dyddiadau a nodir ‘tua’. Ni ddangosir pob plentyn: mae’r coed yn dilyn y llinachau a ddygodd y goron a’r priodasau a unodd y tai.")
    main = (hero("kings", f'<a href="index.html">{SITE}</a> / <a href="kings.html">{bi("Kings and princes", "Brenhinoedd a thywysogion")}</a>', "crown",
                 "c. 825–1603", "tua 825–1603", "Royal family trees of Wales", "Coed teulu brenhinol Cymru",
                 "From Rhodri Mawr to Harri Tudur: how the royal houses of Gwynedd, Deheubarth and Powys ran on for six hundred years, married into one another, and came to the throne at Bosworth.",
                 "O Rhodri Mawr i Harri Tudur: sut y parhaodd tai brenhinol Gwynedd, Deheubarth a Phowys am chwe chan mlynedd, priodi â’i gilydd, a dod i’r orsedd yn Bosworth.", art="castle")
            + section(intro + how + f'<nav class="ft-jump" aria-label="Trees">{jump}</nav>', top=True)
            + trees
            + f'<section class="tight" id="marriages"><div class="wrap"><h2 class="sub-h">{bi("One family: the marriages that joined the houses", "Un teulu: y priodasau a unodd y tai")}</h2>'
              f'<p class="lede">{bi("Tap a marriage to find it in the trees.", "Tapiwch briodas i’w chanfod yn y coed.")}</p><div class="ft-wed">{wed}</div></div></section>'
            + f'<section class="tight" id="bosworth" data-era="tudor"><div class="wrap"><h2 class="sub-h">{bi("The road to Bosworth", "Y ffordd i Bosworth")}</h2>'
              f'<p class="lede">{bi("Three Welsh lines that met in Harri Tudur and his children: the Tudors of Penmynydd, the house of Dinefwr, and Llywelyn Fawr’s daughter Gwladus Ddu.", "Tair llinach Gymreig a gyfarfu yn Harri Tudur a’i blant: Tuduriaid Penmynydd, tŷ Dinefwr, a Gwladus Ddu, merch Llywelyn Fawr.")}</p>{ft_road()}</div></section>'
            + section(f'<p class="note-box">{note}</p>')
            + section(f'<div class="pager"><a class="btn" href="kings.html">← {bi("Kings and princes of Wales", "Brenhinoedd a thywysogion Cymru")}</a>'
                      f'<a class="btn solid" href="person-harri-tudur.html">{bi("Harri Tudur", "Harri Tudur")} →</a></div>')
            + f'<div class="ft-bar" id="ft-bar" role="status" hidden><p id="ft-msg"></p><button type="button" id="ft-clear">{bi("Clear", "Clirio")}</button></div>')
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": "Royal family trees of Wales", "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page("family-trees.html", "Royal family trees of Wales · History of Wales",
                "Family trees of the royal houses of Wales: Gwynedd, Deheubarth, Powys, Gwent and the Tudors, from Rhodri Mawr to Harri Tudur, and the marriages that joined them.",
                main, era="kings", ld=ld, og_type="website", active="kings.html", track="kings:trees", extra=FT_JS)


# ---------- index ----------
FEATURED = ["dewi-sant", "hywel-dda", "gwenllian", "llywelyn-fawr", "llywelyn-ap-gruffudd", "dafydd-ap-gwilym", "owain-glyndwr", "harri-tudur", "william-morgan", "lloyd-george", "aneurin-bevan", "betty-campbell"]
DATA = dict(
    ERAS=D.ERAS, EVENTS=D.EVENTS, PLACES=[dict(p, ph=[photo_url(PH.PLACE_PHOTOS[p['id']][0], 640), COMMONS + 'File:' + _q(PH.PLACE_PHOTOS[p['id']][0], safe=''), PH.PLACE_PHOTOS[p['id']][1], PH.PLACE_PHOTOS[p['id']][2]] if p['id'] in PH.PLACE_PHOTOS else None) for p in D.PLACES], PEOPLE=D.PEOPLE, READING=D.READING, ONLINE=D.ONLINE,
    CENSUS=D.CENSUS, KINGDOMS=D.KINGDOMS, LA=la, DICT=D.DICT, SAMPLES=D.SAMPLES, WORDS=D.WORDS,
    TRAILS=[dict(id=t["id"], en=t["en"], cy=t["cy"], ill=t["ill"], n=len(t["items"]), introEn=t["introEn"][0], introCy=t["introCy"][0]) for t in L.TRAILS],
    AUDIO=sorted(f[:-4] for f in os.listdir(os.path.join(SRC, 'static', 'audio')) if f.endswith('.mp3')) if os.path.isdir(os.path.join(SRC, 'static', 'audio')) else [],
    MAPC=dict(minx=geo["minx"], maxy=geo["maxy"], k=geo["k"], sc=geo["sc"]),
    SL={i: x["id"] for i, ev in enumerate(D.EVENTS) for x in story_links("events", ev[5])},
    KGLINK={"Gwynedd": "kings-gwynedd.html", "Powys": "kings-powys.html", "Ceredigion": "kings-ceredigion.html", "Dyfed": "kings-dyfed.html", "Brycheiniog": "kings-brycheiniog.html",
            "Rhwng Gwy a Hafren": "kings-gwy-a-hafren.html", "Glywysing": "kings-glywysing.html", "Morgannwg": "kings-glywysing.html", "Gwent": "kings-gwent.html", "Deheubarth": "kings-deheubarth.html",
            "Rhodri Mawr": "person-rhodri-mawr.html", "Hywel Dda": "person-hywel-dda.html", "Gruffudd ap Llywelyn": "kings.html", "Principality of Wales": "kings.html#princes",
            "Owain Glyndŵr, Prince of Wales": "person-owain-glyndwr.html"},
    FACTS=F.FACTS, FEATURED=FEATURED, PPH={k: photo_url(v[0], 240) for k, v in PH.PERSON_PHOTOS.items()},
)
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
AGES_HTML = "".join(
    f'<a class="poster" href="era-{x["id"]}.html" data-era="{x["id"]}">{A.scene(ERA_ART[x["id"]], COL[x["id"]])}<span class="shade"></span><span class="rn">{ROMAN[i]}</span>'
    f'<span class="txt"><span class="span">{bi(x["spanEn"], x["spanCy"])}</span><h3>{bi(x["en"], x["cy"])}</h3><p>{bi(x["blurbEn"], x["blurbCy"])}</p><span class="go">{bi("Read the chapter", "Darllen y bennod")} →</span></span></a>'
    for i, x in enumerate(D.ERAS))
MARQ = [("Castles", "Cestyll", "story-castles.html"), ("Poets", "Beirdd", "person-dafydd-ap-gwilym.html"), ("Saints", "Seintiau", "era-saints.html"),
        ("Princes", "Tywysogion", "era-medieval.html"), ("Dragons", "Dreigiau", "legend-dragons.html"), ("Coal", "Glo", "story-coal.html"),
        ("Slate", "Llechi", "place-dinorwig.html"), ("Song", "Cân", "trail-song.html"), ("Rebels", "Gwrthryfelwyr", "story-protest.html"), ("Legends", "Chwedlau", "legends.html")]
# two copies so the strip can loop for ever; the second copy is hidden from screen readers and the Tab key
MARQUEE = "".join(f'<a href="{u}" draggable="false">{bi(a, b)}</a><i aria-hidden="true">✦</i>' for a, b, u in MARQ) + \
    "".join(f'<a href="{u}" draggable="false" tabindex="-1" aria-hidden="true">{bi(a, b)}</a><i aria-hidden="true">✦</i>' for a, b, u in MARQ)


def _letters(text):
    """Each letter in its own box so the opening words can drop in and glint one by one, like "Cymru"."""
    out, i = [], 0
    for w in text.split(" "):
        out.append('<span class="w">' + "".join(f'<b style="--i:{i + k}">{e(ch)}</b>' for k, ch in enumerate(w)) + "</span>")
        i += len(w)
    return " ".join(out)


HERO_NAME = (f'<p class="hero-name"><span class="l-en" lang="en" aria-label="History of Wales">{_letters("History of Wales")}</span>'
             f'<span class="l-cy" lang="cy" aria-label="Hanes Cymru">{_letters("Hanes Cymru")}</span></p>')


def fill(fragment, active="", skip="#chapters", home=False):
    return (fragment.replace("__NAV__", nav(active, skip, home)).replace("__HERONAME__", HERO_NAME).replace("__FOOTER__", footer()).replace("__AGES__", AGES_HTML).replace("__MARQUEE__", MARQUEE)
            .replace("__STORIES__", "".join(story_card(x, k == 0) for k, x in enumerate(F.STORIES)))
            .replace("__LEGENDS__", "".join(legend_card(x) for x in F.LEGENDS[:4])).replace("__PLAY__", play_cards()))


index_head = head.replace("</style>", extra_css + PRINT_CSS + EXTRA_PAGE_CSS + "\n</style>", 1)
index_head = re.sub(r"<title>.*?</title>\n", "", index_head, count=1)
index_head = re.sub(r'<meta name="description"[^>]*>\n', "", index_head, count=1)
_bare_head = index_head
index_head = head_tags("History of Wales", "The history of Wales, from the first people in the caves to the Senedd: an interactive timeline, map, people, legends and games, in English and Cymraeg.", "", "website") + index_head
_body_filled = (body.replace("__WALES__", geo["outline"])
                .replace("__DATA__", json.dumps(DATA, ensure_ascii=False, separators=(",", ":")))
                .replace("__TOWNS__", json.dumps(TW.TOWNS, ensure_ascii=False, separators=(",", ":")))
                .replace("__APP__", app)
                .replace("</body>", "") + TAIL_JS)
index_fragment = fill(index_head + _body_filled, home=True)  # no document skeleton


def app_page(path, title, desc, hero_html, section_file, active, skip):
    """A page that reuses the home page's script with only one of its sections (timeline, quiz)."""
    h = re.sub(r'<header class="hero" id="top">.*?</header>', lambda m: hero_html, _bare_head, count=1, flags=re.S)
    h = head_tags(title, desc, path) + h
    b = "<main>\n" + read(section_file) + "</main>\n" + _body_filled[_body_filled.index("__FOOTER__"):]
    return fill(h + b, active, skip)


_tl_hero = (f'<header class="era-hero has-art" id="top" data-era="kings"><div class="hero-art">{A.scene("arches", COL["kings"])}</div><div class="wrap"><p class="crumbs"><a href="index.html" data-cy="Hanes Cymru">History of Wales</a></p>'
            '<p class="span" data-cy="230,000 CC – heddiw">230,000 BC – today</p>'
            '<h1 data-cy="Llinell amser">Timeline</h1><p class="lede" data-cy="Holl hanes Cymru mewn dyddiadau. Sgroliwch drwy’r oesoedd neu dewiswch un.">The whole history of Wales in dates. Scroll through the ages, or pick one.</p></div></header>')
tl_fragment = app_page("timeline.html", "Timeline · History of Wales", "Every date in the history of Wales, from 230,000 BC to today, in English and Cymraeg.", _tl_hero, "timeline_section.html", "timeline.html", "#timeline")
_qz_hero = (f'<header class="era-hero has-art" id="top" data-era="kings"><div class="hero-art">{A.scene("book", COL["kings"])}</div><div class="wrap"><p class="crumbs"><a href="index.html" data-cy="Hanes Cymru">History of Wales</a> / <a href="play.html" data-cy="Chwarae">Play</a></p>'
            '<p class="span" data-cy="Cwis">Quiz</p>'
            '<h1 data-cy="Faint wyddoch chi?">How much do you know?</h1><p class="lede" data-cy="Deg cwestiwn o’r llinell amser a’r bobl. Mae pob cwis yn wahanol.">Ten questions drawn from the timeline and the people. Every round is different.</p></div></header>')
quiz_fragment = app_page("quiz.html", "Quiz · History of Wales", "A quiz on the history of Wales: ten questions, different every time, plus the timeline challenge.", _qz_hero, "quiz_section.html", "play.html", "#quiz")


def wrap_doc(fragment):
    i = fragment.index("</style>") + len("</style>")
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + LANG_BOOT + "\n" + fragment[:i] + "\n</head>\n<body>\n" + fragment[i:] + "\n</body>\n</html>\n")


def search_index():
    def yl(ev):
        return [year_label(ev), year_label(ev, True)]
    items = [dict(k="era", t=x["en"], c=x["cy"], u=f"era-{x['id']}.html", y=[x["spanEn"], x["spanCy"]], b=[x["blurbEn"], x["blurbCy"]], e=x["id"]) for x in D.ERAS]
    items += [dict(k="person", t=p[3], c=p[4], u=f"person-{p[0]}.html", y=[p[2], p[2]], b=[p[5] + ". " + p[7], p[6] + ". " + p[8]], e=p[1]) for p in D.PEOPLE]
    items += [dict(k="place", t=p["en"], c=p["cy"], u=f"place-{p['id']}.html", y=[p["year"], p["year"]], b=[p["dEn"], p["dCy"]], e=p["era"]) for p in D.PLACES]
    items += [dict(k="event", t=ev[5], c=ev[6], u=f"era-{ev[0]}.html#e{i}", y=yl(ev), b=[ev[7], ev[8]], e=ev[0]) for i, ev in enumerate(D.EVENTS)]
    items += [dict(k="trail", t=t["en"], c=t["cy"], u=f"trail-{t['id']}.html", y=["Trail", "Llwybr"], b=[t["introEn"][0], t["introCy"][0]], e="medieval") for t in L.TRAILS]
    items += [dict(k="story", t=x["en"], c=x["cy"], u=f"story-{x['id']}.html", y=[f"{x['mins']} min", f"{x['mins']} mun"], b=[x["sumEn"], x["sumCy"]], e=x["era"]) for x in F.STORIES]
    items += [dict(k="legend", t=x["en"], c=x["cy"], u=f"legend-{x['id']}.html", y=[x["place"], x["place"]], b=[x["sumEn"], x["sumCy"]], e=x["era"]) for x in F.LEGENDS]
    items += [dict(k="page", t=s[3], c=s[1], u=f"symbols.html#{s[0]}", y=["Symbol", "Symbol"], b=[s[4], s[5]], e="modern") for s in F.SYMBOLS]
    items += [dict(k="page", t=g[2], c=g[3], u=g[0], y=["Game", "Gêm"], b=[g[4], g[5]], e=g[8]) for g in GAMES]
    items.append(dict(k="page", t="Kings and princes of Wales", c="Brenhinoedd a thywysogion Cymru", u="kings.html", y=["Kings", "Brenhinoedd"], b=["Every king and prince of Wales, and Gruffudd ap Llywelyn, king of all Wales", "Pob brenin a thywysog yng Nghymru, a Gruffudd ap Llywelyn, brenin Cymru gyfan"], e="kings"))
    items += [dict(k="page", t=realm_title(r)[0], c=realm_title(r)[1], u=f"kings-{r['id']}.html", y=[r["span"], cy_dates(r["span"])], b=[r["subEn"] + " " + ", ".join(x["name"] for x in r["rulers"] if x["k"] == "r"), r["subCy"]], e=r["era"]) for r in RY.REALMS]
    items.append(dict(k="page", t="Royal family trees of Wales", c="Coed teulu brenhinol Cymru", u="family-trees.html", y=["Family trees", "Coed teulu"], b=["From Rhodri Mawr to Harri Tudur: the royal houses of Gwynedd, Deheubarth, Powys and Gwent, the Tudors, and the marriages that joined them. " + ", ".join(n["name"][0] for n in FT_IDS.values() if not n["gap"]), "O Rhodri Mawr i Harri Tudur: tai brenhinol Gwynedd, Deheubarth, Powys a Gwent, y Tuduriaid, a’r priodasau a’u hunodd."], e="kings"))
    items += [dict(k="page", t=t["en"], c=t["cy"], u=f"family-trees.html#tree-{t['id']}", y=["Family tree", "Coeden deulu"], b=[t["introEn"], t["introCy"]], e=t["era"]) for t in TR.TREES]
    items.append(dict(k="page", t="For teachers", c="I athrawon", u="teachers.html", y=["", ""], b=["Lesson ideas and printable quizzes", "Syniadau gwersi a chwisiau i’w hargraffu"], e="industrial"))
    return items


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    out = os.path.join(ROOT, "_site")
    shutil.rmtree(out, ignore_errors=True)
    pages = {"index.html": wrap_doc(index_fragment), "timeline.html": wrap_doc(tl_fragment), "quiz.html": wrap_doc(quiz_fragment)}
    for i, era in enumerate(D.ERAS):
        pages[f"era-{era['id']}.html"] = era_page(i, era)
    for p in D.PEOPLE:
        pages[f"person-{p[0]}.html"] = person_page(p)
    for pl in D.PLACES:
        pages[f"place-{pl['id']}.html"] = place_page(pl)
    pages["trails.html"] = trails_index()
    for i, t in enumerate(L.TRAILS):
        pages[f"trail-{t['id']}.html"] = trail_page(t, i)
    pages["teachers.html"] = teachers_page()
    pages["stories.html"] = stories_index()
    for i, x in enumerate(F.STORIES):
        pages[f"story-{x['id']}.html"] = story_page(x, i)
    pages["legend-arthur.html"] = '<!doctype html><html lang="en"><meta charset="utf-8"><title>Arthur, King of the Britons</title><link rel="canonical" href="story-arthur.html"><meta http-equiv="refresh" content="0; url=story-arthur.html"><a href="story-arthur.html">Arthur, King of the Britons</a></html>'
    pages["legends.html"] = legends_index()
    for i, x in enumerate(F.LEGENDS):
        pages[f"legend-{x['id']}.html"] = legend_page(x, i)
    pages["kings.html"] = kings_page()
    for i, r in enumerate(RY.REALMS):
        pages[f"kings-{r['id']}.html"] = realm_page(r, i)
    pages["family-trees.html"] = family_trees_page()
    pages["symbols.html"] = symbols_page()
    pages["gallery.html"] = gallery_page()
    pages["play.html"] = play_index()
    pages["journey.html"] = journey_page()
    pages["daily.html"] = game_page("daily.html", "daily", "medieval", "Daily challenge", "Her y dydd", "One event from Welsh history. Six guesses to find the year.", "Un digwyddiad o hanes Cymru. Chwe chynnig i ddyfalu’r flwyddyn.", "castle", "A daily history challenge: guess the year of an event from Welsh history in six tries.")
    pages["map-game.html"] = game_page("map-game.html", "map", "modern", "Where in Wales?", "Ble yng Nghymru?", "Tap the map where you think each place is. Five rounds, 100 points each.", "Tapiwch y map lle credwch fod pob lle. Pum rownd, 100 pwynt yr un.", "senedd", "A map game: place the castles, towns and historic sites of Wales on a blank map.", with_map=True)
    pages["names.html"] = game_page("names.html", "names", "saints", "Welsh names", "Enwau Cymraeg", "Jones, Powell, Lloyd, Vaughan: Welsh surnames are history in miniature. Look yours up, then find your name as the princes would have said it.", "Jones, Powell, Lloyd, Vaughan: mae cyfenwau Cymru’n hanes ar raddfa fach. Chwiliwch am eich un chi, yna gweld eich enw fel y byddai’r tywysogion wedi’i ddweud.", "cross", "What Welsh surnames mean and where they come from, and a patronymic name maker.")
    pages["hero.html"] = game_page("hero.html", "hero", "ancient", "Which figure from history are you?", "Pa ffigwr o hanes ydych chi?", "Six quick questions.", "Chwe chwestiwn cyflym.", "torch", "A short personality quiz: which figure from Welsh history are you most like?")
    pages["pairs.html"] = game_page("pairs.html", "pairs", "modern", "Word pairs", "Parau geiriau", "Turn over two cards at a time and match each Welsh word to its meaning.", "Trowch ddau gerdyn ar y tro a pharu pob gair Cymraeg â’i ystyr.", "owl", "A memory game: match Welsh words to their meanings.")
    for name, text in pages.items():
        write(os.path.join(out, name), text)
    for f in os.listdir(os.path.join(SRC, "static")):
        sp = os.path.join(SRC, "static", f)
        (shutil.copytree if os.path.isdir(sp) else shutil.copy)(sp, os.path.join(out, f))
    write(os.path.join(out, "search.json"), json.dumps(search_index(), ensure_ascii=False, separators=(",", ":")))
    write(os.path.join(out, ".nojekyll"), "")
    write(os.path.join(out, "robots.txt"), f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}sitemap.xml\n")
    write(os.path.join(out, "sitemap.xml"), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{xesc(BASE_URL + ('' if p == 'index.html' else p))}</loc></url>\n" for p in pages) + "</urlset>\n")
    if "--artifact" in sys.argv:
        a = os.path.join(ROOT, "_artifact")
        shutil.rmtree(a, ignore_errors=True)
        write(os.path.join(a, "index.html"), index_fragment)
        for p in pages:
            if p != "index.html":
                shutil.copy(os.path.join(out, p), os.path.join(a, p))
        for f in os.listdir(os.path.join(SRC, "static")):
            if f.endswith((".png", ".svg", ".js")) and f != "sw.js":
                shutil.copy(os.path.join(SRC, "static", f), os.path.join(a, f))
        shutil.copy(os.path.join(out, "search.json"), os.path.join(a, "search.json"))
    print(f"Built {len(pages)} pages -> {out}")


if __name__ == "__main__":
    main()
