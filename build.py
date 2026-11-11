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
import gallery as G  # noqa: E402
import gallery_photos as GP  # noqa: E402
import ages as AG  # noqa: E402
import features as F  # noqa: E402
import art as A  # noqa: E402
L.TEACH.update(AG.TEACH)
import ages9 as AG9
import whatsnew as WN  # noqa: E402
import royal as RY  # noqa: E402
import trees as TR  # noqa: E402
import cymraeg as CYM  # noqa: E402
import saints as SA  # noqa: E402
import onthisday as OTD  # noqa: E402
import arthur as AR  # noqa: E402
import mabinogion as MB  # noqa: E402
import people2 as P2  # noqa: E402
L.TEACH.update(AG9.TEACH)
from urllib.parse import quote as _q

BASE_URL = os.environ.get("SITE_URL", "https://tywysog85.github.io/historyofwales/")
GOATCOUNTER = os.environ.get("GOATCOUNTER", "").strip()
# The email sign-up. Set to the number of the sign-up form made at kit.com (see SKILLS.md, "The weekly email") and the
# sign-up box appears on the home page, the What's new page and the foot of every page. Empty: the box is not shown.
KIT_FORM = os.environ.get("KIT_FORM", "").strip()
WIKI = "https://en.wikipedia.org/wiki/"


def read(*p):
    with open(os.path.join(SRC, *p), encoding="utf-8") as f:
        return f.read()


def e(s):
    return html.escape(str(s), quote=True)


head = read("head.html")
body = read("body.html")
app = read("app.js")
extra_css = read("extra.css") + read("v6.css") + read("onthisday.css") + read("people2.css")
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
         '<meta name="twitter:card" content="summary_large_image">\n'
         f'<link rel="alternate" type="application/atom+xml" title="History of Wales: what’s new and on this day" href="{BASE_URL}feed.xml">\n')
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
NAV_MORE = [("whatsnew.html", "What’s new", "Beth sy’n newydd"), ("kings.html", "Kings and princes", "Brenhinoedd a thywysogion"), ("castles.html", "Castles map", "Map y cestyll"), ("saints.html", "Saints of Wales", "Seintiau Cymru"), ("firsts.html", "Welsh world firsts", "Cymru oedd y cyntaf"), ("family-trees.html", "Royal family trees", "Coed teulu brenhinol"), ("mabinogion.html", "The Mabinogion", "Y Mabinogion"), ("symbols.html", "Symbols and traditions", "Symbolau a thraddodiadau"), ("trails.html", "Themed trails", "Llwybrau thema"), ("gallery.html", "Photo gallery", "Oriel luniau"), ("onthisday.html", "On this day", "Ar y dydd hwn"),
            ("index.html#language", "The Welsh language", "Yr iaith Gymraeg"), ("welsh.html", "Learn Welsh", "Dysgu Cymraeg"), ("journey.html", "Your journey", "Eich taith"), ("teachers.html", "For teachers", "I athrawon"),
            ("index.html#sources", "Sources", "Ffynonellau")]
# extra links for the top bar (shown on every page, beside the site name)
NAV_HOME_MORE = [("symbols.html", "Symbols", "Symbolau"), ("trails.html", "Trails", "Llwybrau"), ("gallery.html", "Gallery", "Oriel"), ("index.html#language", "Language", "Iaith")]
SEARCH_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.5 15.5 21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'


# ---------- what's new, the email sign-up and the news feed (src/whatsnew.py) ----------
def _news_date(d, cy=False):
    y, m, dd = (int(x) for x in d.split("-"))
    if cy:
        return f"{dd} {MONTHS_CY[m - 1]} {y}"
    return f"{dd} {datetime.date(y, m, dd).strftime('%B')} {y}"


MONTHS_CY = ["Ionawr", "Chwefror", "Mawrth", "Ebrill", "Mai", "Mehefin", "Gorffennaf", "Awst", "Medi", "Hydref", "Tachwedd", "Rhagfyr"]


def follow_box(where):
    """The email sign-up when a Kit form is set; otherwise the ways to follow that need no account."""
    if KIT_FORM:
        return (f'<form class="follow follow-{where}" action="https://app.kit.com/forms/{e(KIT_FORM)}/subscriptions" method="post" target="_blank">'
                f'<p class="f-h">{bi("This week in Welsh history", "Yr wythnos hon yn hanes Cymru")}</p>'
                f'<p class="f-sub">{bi("One short email every Monday: the anniversaries of the week ahead and anything new on the site. Free, and you can leave at any time.", "Un e-bost byr bob dydd Llun: pen-blwyddi’r wythnos i ddod ac unrhyw beth newydd ar y wefan. Am ddim, a gallwch adael unrhyw bryd.")}</p>'
                f'<div class="f-row"><label class="sr-only" for="f-email-{where}">{bi("Your email address", "Eich cyfeiriad e-bost")}</label>'
                f'<input id="f-email-{where}" name="email_address" type="email" required autocomplete="email" placeholder="you@example.com">'
                f'<button type="submit" class="btn solid">{bi("Sign up", "Ymuno")}</button></div></form>')
    return (f'<div class="follow follow-{where}"><p class="f-h">{bi("Keep up with the site", "Dilynwch y wefan")}</p>'
            f'<p class="f-sub">{bi("New history is added every week. See what has arrived, or follow the news feed in any feed reader.", "Mae hanes newydd yn cael ei ychwanegu bob wythnos. Gwelwch beth sydd wedi cyrraedd, neu dilynwch y ffrwd newyddion mewn unrhyw ddarllenydd ffrydiau.")}</p>'
            f'<div class="f-row"><a class="btn solid" href="whatsnew.html">{bi("What’s new", "Beth sy’n newydd")}</a><a class="btn" href="feed.xml">{bi("News feed", "Ffrwd newyddion")}</a></div></div>')


def news_item(n, big=False):
    d, te, tc, se, sc, link = n
    return (f'<li class="news-item" data-date="{d}"><a href="{link}"><span class="n-date">{bi(_news_date(d), _news_date(d, True))}</span>'
            f'<span class="n-t">{bi(te, tc)}</span>' + (f'<span class="n-s">{bi(se, sc)}</span>' if big else "") + "</a></li>")


def news_strip():
    return (f'<div class="news-row rv"><div class="news-box"><p class="eyebrow">{bi("New on the site", "Newydd ar y wefan")}</p>'
            f'<ul class="news-list">{"".join(news_item(n) for n in WN.NEWS[:3])}</ul>'
            f'<a class="n-all" href="whatsnew.html">{bi("Everything that is new", "Popeth sy’n newydd")} →</a></div>{follow_box("home")}</div>')


def whatsnew_page():
    main = (hero("today", f'<a href="index.html">{SITE}</a>', "book", "What’s new", "Beth sy’n newydd", "New on History of Wales", "Newydd ar Hanes Cymru",
                 "Every page, long read, legend and game added to the site, newest first.", "Pob tudalen, erthygl, chwedl a gêm a ychwanegwyd at y wefan, y mwyaf newydd yn gyntaf.", art="senedd")
            + section(f'<div class="news-page"><ul class="news-list big">{"".join(news_item(n, True) for n in WN.NEWS)}</ul>{follow_box("page")}</div>', top=True))
    return page("whatsnew.html", "What’s new · History of Wales", "Everything new on History of Wales: new pages, long reads, legends, people and games, newest first.", main,
                era="today", og_type="website", active="whatsnew.html")


def feed_xml(otd):
    """An Atom feed: today's anniversaries (the site is rebuilt every morning) and everything new, for feed readers and email services."""
    now = datetime.datetime.now(datetime.timezone.utc)
    md = now.strftime("%m-%d")
    today = [r for r in otd if r[0] == md]
    entries = []
    if today:
        body = "".join(f"<p><b>{xesc(str(r[1]) + ': ' if r[1] is not None else '')}{xesc(r[3])}.</b> {xesc(r[5])}</p>" for r in today)
        stamp = now.strftime("%Y-%m-%dT06:00:00Z")
        entries.append(("On this day in Welsh history: " + now.strftime("%-d %B"), BASE_URL + "onthisday.html", f"{BASE_URL}onthisday.html#{now.strftime('%Y-%m-%d')}", stamp, body))
    for d, te, tc, se, sc, link in WN.NEWS:
        entries.append((te, BASE_URL + link, f"{BASE_URL}whatsnew.html#{d}-{link}", d + "T12:00:00Z", f"<p>{xesc(se)}</p>"))
    updated = max(x[3] for x in entries)
    out = ['<?xml version="1.0" encoding="utf-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en-GB">',
           "<title>History of Wales</title>", "<subtitle>New on the site, and this day in Welsh history</subtitle>",
           f'<link href="{BASE_URL}"/>', f'<link rel="self" href="{BASE_URL}feed.xml"/>', f"<id>{BASE_URL}</id>", f"<updated>{updated}</updated>",
           "<author><name>History of Wales</name></author>", f"<icon>{BASE_URL}icon-192.png</icon>"]
    for t, link, i, when, body in entries:
        out.append(f'<entry><title>{xesc(t)}</title><link href="{xesc(link)}"/><id>{xesc(i)}</id><updated>{when}</updated><content type="html">{xesc(body)}</content></entry>')
    return "\n".join(out) + "\n</feed>\n"


def nav(active="", skip="#main", home=False):
    def li(h, a, b, n=None):
        num = f'<span class="n">{n:02d}</span>' if n else ""
        return f'<li><a href="{h}"{" class=on aria-current=page" if active == h else ""}>{num}{bi(a, b)}</a></li>'
    main = "".join(li(*x) for x in NAV_MAIN)
    main += "".join(li(*x) for x in NAV_HOME_MORE)  # every page shows every topic
    big = li("index.html", "Home", "Hafan", 1) + "".join(li(h, a, b, i + 2) for i, (h, a, b) in enumerate(NAV_MAIN))
    more = "".join(li(*x) for x in NAV_MORE)
    return (f'<a class="skip" href="{skip}">{bi("Skip to content", "Neidio i’r cynnwys")}</a><div class="progress" aria-hidden="true"><i id="progress"></i></div>'
            f'<nav class="nav" aria-label="Main"><div class="wrap">' + f'<a class="brand" href="index.html">{bi("History of Wales", "Hanes Cymru")}</a>' +
            f'<ul class="nav-inline">{main}</ul>' +
            f'<a class="journey-chip" href="journey.html" id="journey-chip" data-total="{JOURNEY_TOTAL}" aria-label="0 pages read: your journey / Eich taith"><svg viewBox="0 0 36 36" aria-hidden="true"><circle cx="18" cy="18" r="15" class="tr"/><circle cx="18" cy="18" r="15" class="fg" id="journey-ring" pathLength="100" stroke-dasharray="0 100"/></svg><b id="journey-n">0</b></a>'
            f'<button type="button" class="search-btn" data-search aria-label="Search / Chwilio">{SEARCH_SVG}</button>'
             '<div class="lang" role="group" aria-label="Language / Iaith"><button type="button" id="lang-en" aria-pressed="true">EN</button><button type="button" id="lang-cy" aria-pressed="false">CY</button></div>'
            f'<button type="button" class="menu-btn" id="menu-btn" aria-expanded="false" aria-controls="menu" aria-label="Menu / Dewislen" data-news="{WN.NEWS[0][0]}"><span class="bars" aria-hidden="true"><i></i><i></i></span>{bi("Menu", "Dewislen")}</button></div></nav>'
            f'<div class="menu" id="menu" hidden><div class="wrap"><ul class="menu-big">{big}</ul><div class="menu-side"><p class="eyebrow">{bi("More", "Rhagor")}</p><ul class="menu-more">{more}</ul>'
            f'<p class="menu-note">{bi("230,000 years of history, in English and Cymraeg.", "230,000 o flynyddoedd o hanes, yn Gymraeg ac yn Saesneg.")}</p></div></div></div>')


# Name shown in the copyright line at the bottom of every page.
COPYRIGHT_OWNER = "History of Wales"
COPYRIGHT_OWNER_CY = "Hanes Cymru"


def footer():
    def col(title_en, title_cy, links):
        return f'<div><p class="eyebrow">{bi(title_en, title_cy)}</p><ul>' + "".join(f'<li><a href="{h}">{bi(a, b)}</a></li>' for h, a, b in links) + "</ul></div>"
    eras = [(f'era-{x["id"]}.html', x["en"], x["cy"]) for x in D.ERAS]
    explore = [("timeline.html", "Timeline", "Llinell amser"), ("index.html#map", "Map of Wales", "Map Cymru"), ("index.html#people", "People", "Pobl"), ("firsts.html", "Welsh world firsts", "Cymru oedd y cyntaf"), ("kings.html", "Kings and princes", "Brenhinoedd a thywysogion"), ("family-trees.html", "Royal family trees", "Coed teulu brenhinol"), ("saints.html", "Saints of Wales", "Seintiau Cymru"), ("castles.html", "Castles of Wales", "Cestyll Cymru"), ("trails.html", "Themed trails", "Llwybrau thema"),
               ("gallery.html", "Photo gallery", "Oriel luniau"), ("onthisday.html", "On this day", "Ar y dydd hwn"), ("index.html#language", "The Welsh language", "Yr iaith Gymraeg"), ("welsh.html", "Learn Welsh", "Dysgu Cymraeg")]
    read = [("whatsnew.html", "What’s new", "Beth sy’n newydd"), ("stories.html", "Long reads", "Erthyglau"), ("legends.html", "Legends", "Chwedlau"), ("mabinogion.html", "The Mabinogion", "Y Mabinogion"), ("symbols.html", "Symbols and traditions", "Symbolau a thraddodiadau"),
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
            f'<p class="foot-tag">{bi("Thank you for reading. Wales is a small country with a long memory; this site is a way in.", "Diolch am ddarllen. Gwlad fach â chof hir yw Cymru; ffordd i mewn yw’r wefan hon.")}</p>{follow_box("foot")}</div>'
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


def place_ph(pid):
    """Picture for a place on the home page map: [image, Commons page, caption EN, caption CY] or None."""
    g = GP.GALLERY.get("place-" + pid)
    if g:
        return [f"gallery/place-{pid}-s.webp", COMMONS + "File:" + _q(g[0], safe=""), g[4], g[5]]
    ph = PH.PLACE_PHOTOS.get(pid)
    return [photo_url(ph[0], 640), COMMONS + "File:" + _q(ph[0], safe=""), ph[1], ph[2]] if ph else None


def photo_fig(ph, cls="", gid=None):
    g = GP.GALLERY.get(gid) if gid else None
    if g:  # a checked picture from the gallery, stored on the site, with its full credit
        f, by, lic, licu, wen, wcy, w, h = g
        return (f'<figure class="photo {cls}"><img src="gallery/{gid}.webp" width="{w}" height="{h}" alt="{e(wen)}" loading="lazy" decoding="async">'
                f'<figcaption>{bi(wen, wcy)} · {bi("Picture", "Llun")}: {e(by)}, <a href="{e(licu)}" target="_blank" rel="noopener license">{e(lic)}</a>, '
                f'<a href="{COMMONS}File:{_q(f, safe="")}" target="_blank" rel="noopener">Wikimedia Commons</a> · <a href="gallery.html">{bi("More in the gallery", "Mwy yn yr oriel")}</a></figcaption></figure>')
    if not ph:
        return ""
    f, cen, ccy = ph[:3]
    cr = ph[3] if len(ph) > 3 else ""
    cr = bi(cr, cr.replace("Public domain", "Parth cyhoeddus").replace("No known restrictions", "Dim cyfyngiadau hysbys")) if cr else ""
    return (f'<figure class="photo {cls}"><img src="{photo_url(f)}" alt="{e(cen)}" loading="lazy" decoding="async" referrerpolicy="no-referrer" '
            f'onerror="this.closest(\'figure\').remove()">'
            f'<figcaption>{bi(cen, ccy)} · <a href="{COMMONS}File:{_q(f, safe="")}" target="_blank" rel="noopener">{bi("Photo: Wikimedia Commons", "Llun: Wikimedia Commons")}</a>{" · " + cr if cr else ""}</figcaption></figure>')


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
            + (section(f'<p class="lede">{bi("Dewi, Teilo, Illtud, Cadog, Beuno, Melangell and sixty more: every saint region by region, with the llannau that carry their names.", "Dewi, Teilo, Illtud, Cadog, Beuno, Melangell a thrigain arall: pob sant fesul rhanbarth, gyda’r llannau sy’n dwyn eu henwau.")}</p><p><a class="btn solid" href="saints.html">{bi("Meet the saints of Wales", "Cwrdd â seintiau Cymru")} →</a></p>', "The saints of Wales", "Seintiau Cymru") if eid == "saints" else "")
            + section(f'<div class="pager">{pager}</div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": era["en"], "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page(f"era-{eid}.html", f'{era["en"]} · History of Wales', era["blurbEn"], main, era=eid, ld=ld, track=f"era:{eid}")


# ---------- person pages ----------
def arthur_extra():
    # Arthur's line and the map of Arthur's Wales (src/arthur.py)
    him_cls = ' class="him"'
    line = "".join(f'<li{him_cls if him else ""}><b>{e(n)}</b><span>{bi(a, c)}</span></li>' for n, a, c, him in AR.LINE)
    links = ft_link_for_person("person-arthur.html") + realm_links("person-arthur.html")
    line_html = (f'<ol class="ar-line">{line}</ol>' + (f'<p class="realm-links">{links}</p>' if links else ""))
    sc, k, minx, maxy = geo["sc"], geo["k"], geo["minx"], geo["maxy"]
    pins, items = "", ""
    for i, (en, cy, lat, lon, ten, tcy, link) in enumerate(AR.PLACES, 1):
        x0, y0 = (lon - minx) * k * sc, (maxy - lat) * sc
        dx, dy = AR.NUDGE.get(i, (0, 0))   # move a crowded pin aside, with a short line back to the real spot
        x, y = x0 + dx, y0 + dy
        if dx or dy:
            pins += f'<circle class="ar-dot" cx="{x0:.0f}" cy="{y0:.0f}" r="3" fill="#d43c34"/><line class="ar-lead" x1="{x0:.0f}" y1="{y0:.0f}" x2="{x:.0f}" y2="{y:.0f}"/>'
        pins += (f'<a href="#ar-{i}" class="ar-pin"><circle cx="{x:.0f}" cy="{y:.0f}" r="13"/>'
                 f'<text x="{x:.0f}" y="{y + 5:.0f}">{i}</text><title>{e(en)}</title></a>')
        more = f' <a class="src" href="{link}">{bi("More", "Mwy")} →</a>' if link else ""
        items += f'<li id="ar-{i}"><b>{bi(en, cy)}</b><p>{bi(ten, tcy)}{more}</p></li>'
    svg = (f'<svg class="ar-map" viewBox="-10 -10 630 691" role="img" aria-label="Map of places in Wales linked to Arthur / Map o leoedd yng Nghymru sy’n gysylltiedig ag Arthur">'
           f'<path class="land" d="{geo["outline"]}"/>{pins}</svg>')
    intro = bi("Nineteen places in Wales, and in Ergyng on the old border, that carry Arthur’s name or his story. Tap a number to read about it.",
               "Pedwar ar bymtheg o leoedd yng Nghymru, ac yn Ergyng ar yr hen ffin, sy’n dwyn enw Arthur neu ei hanes. Tapiwch rif i ddarllen amdano.")
    return (section(line_html, "The line of Arthur", "Llinach Arthur")
            + section(f'<p class="lede">{intro}</p><div class="ar-grid"><div class="ar-mapbox">{svg}</div><ol class="ar-list">{items}</ol></div>', "Arthur’s Wales", "Cymru Arthur"))


PERSON_EXTRA = {"arthur": arthur_extra}


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
    fld = FIELD_LABEL.get(P2.FIELD.get(slug))
    meta = (f'<div class="person-meta"><span>{e(p[2])}</span><span>{bi(p[5], p[6])}</span><a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a>'
            + (f'<a href="index.html?field={P2.FIELD[slug]}#people">{bi(*fld)}</a>' if fld else "") + '</div>' + first_badge(slug))
    rl = realm_links(f"person-{slug}.html") + ft_link_for_person(f"person-{slug}.html") + saints_links(f"person-{slug}.html")
    meta += f'<p class="realm-links">{rl}</p>' if rl else ""
    coded = any(a.startswith(("## ", "> ", "|| ")) for a in long_en)
    body = prose_bi(long_en, long_cy, cls="story prose") if coded else paras(long_en, long_cy)
    main = (hero(eid, f'<a href="index.html">{SITE}</a> / <a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a>', era["ill"], p[2], p[2], p[3], p[4], p[7], p[8], art=ERA_ART[eid])
            + section(meta + photo_fig(PH.PERSON_PHOTOS.get(slug), "portrait", "person-" + slug) + body + f'<p class="share no-print"><button type="button" class="btn" data-copy="person-{slug}.html">{bi("Copy link to share", "Copïo dolen i’w rhannu")}</button> {src(p[9])}</p>', top=True)
            + PERSON_EXTRA.get(slug, lambda: "")()
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
    rl = realm_links(f"place-{pid}.html") + saints_links(f"place-{pid}.html")
    meta += f'<p class="realm-links">{rl}</p>' if rl else ""
    coded = any(a.startswith(("## ", "> ", "|| ")) for a in long_en)
    body = prose_bi(long_en, long_cy, cls="story prose") if coded else paras(long_en, long_cy)
    main = (hero(eid, f'<a href="index.html">{SITE}</a> / <a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a>', pl["ill"], era["en"], era["cy"], pl["en"], pl["cy"], pl["dEn"], pl["dCy"], art=ERA_ART[eid])
            + section(meta + photo_fig(PH.PLACE_PHOTOS.get(pid), "", "place-" + pid) + paras(long_en, long_cy) + f'<p class="share no-print">{src(pl["src"])}</p>', top=True)
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
EXTRA_PAGE_CSS += read("welsh.css")
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
            + f'<section class="article"><div class="wrap narrow">{meta}{prose_bi(x["pEn"], x["pCy"])}' + (f'<p><a class="btn solid" href="firsts.html">★ {bi("Every Welsh world first, with the people behind them", "Pob un o’r pethau a wnaeth Cymru gyntaf, a’r bobl y tu ôl iddynt")} →</a></p>' if x["id"] == "firsts" else "") + '</div></section>'
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
              f'<aside class="behind"><p class="eyebrow">{bi(x.get("hLabelEn", "The history behind the legend"), x.get("hLabelCy", "Yr hanes y tu ôl i’r chwedl"))}</p><p>{bi(x["hEn"], x["hCy"])}</p></aside>'
              + (f'<p class="l-links">' + "".join(f'<a class="btn" href="{h}">{bi(en, cy)} →</a>' for h, en, cy in x["links"]) + '</p>' if x.get("links") else "") +
              f'<p class="byline"><button type="button" class="copy" data-copy="legend-{x["id"]}.html">{bi("Copy link to share", "Copïo dolen i’w rhannu")}</button></p></div></section>'
            + section(f'<div class="pager"><a class="btn" href="legends.html">← {bi("All legends", "Pob chwedl")}</a><a class="btn solid" href="legend-{nxt["id"]}.html">{bi(nxt["en"], nxt["cy"])} →</a></div>'))
    return page(f"legend-{x['id']}.html", f'{x["en"]} · History of Wales', x["sumEn"], main, era=x["era"], active="legends.html", track=f"legend:{x['id']}")


def legends_index():
    main = (hero("medieval", f'<a href="index.html">{SITE}</a>', "book", "Legends", "Chwedlau", "Legends of Wales", "Chwedlau Cymru",
                 f"{len(F.LEGENDS)} old tales, retold for reading aloud, each with the real history behind it.", f"{len(F.LEGENDS)} o hen chwedlau, wedi’u hadrodd o’r newydd i’w darllen ar goedd, pob un â’r hanes go iawn y tu ôl iddi.", art="dragons",
                 extra='<nav class="chips l-jump" aria-label="Sections / Adrannau">' + "".join(f'<a class="chip" href="#{g["ids"][0]}-set">{bi(g["en"], g["cy"])}</a>' for g in F.LEGEND_GROUPS) + '</nav>')
            + "".join(f'<section{"" if k == 0 else " class=\"tight\""} id="{g["ids"][0]}-set"><div class="wrap"><h2 class="sub-h">{bi(g["en"], g["cy"])}</h2><p class="l-sum">{bi(g["sumEn"], g["sumCy"])}</p>'
                      f'<div class="l-grid">{"".join(legend_card(x) for x in g["items"])}</div>'
                      + (f'<p class="l-links"><a class="btn" href="mabinogion.html">{bi("About the Mabinogion: the books, the translation and all eleven tales", "Am y Mabinogion: y llyfrau, y cyfieithiad a’r un chwedl ar ddeg")} →</a></p>' if g["ids"][0] == "pwyll" else "")
                      + '</div></section>' for k, g in enumerate(F.LEGEND_GROUPS))
            + section(f'<div class="pager"><a class="btn" href="symbols.html">{bi("Symbols and traditions", "Symbolau a thraddodiadau")} →</a></div>'))
    return page("legends.html", "Legends · History of Wales", "The legends of Wales retold: the tales of King Arthur, the red dragon, Gelert, the Four Branches of the Mabinogi, Macsen Wledig, Culhwch and Olwen, Dwynwen, Melangell, the Tylwyth Teg and more, with the history behind them.", main, era="medieval", og_type="website", active="legends.html")


def mabinogion_page():
    # src/mabinogion.py: the eleven tales, the White Book and the Red Book, Lady Charlotte Guest
    def tale(t, era):
        go = (f'<a class="btn" href="{t["link"]}">{bi("Read the tale", "Darllen y chwedl")} →</a>' if t["link"] else "")
        return (f'<article class="mab-tale rv" data-era="{era}"><h3 lang="cy">{e(t["cy"])}</h3><p class="mab-en l-en" lang="en">{e(t["en"])}</p>'
                f'<p>{bi(t["sumEn"], t["sumCy"])}</p>{go}</article>')
    groups = "".join(f'<section class="tight" id="mab-{k + 1}"><div class="wrap"><h2 class="sub-h">{bi(g["en"], g["cy"])}</h2><p class="l-sum">{bi(g["sumEn"], g["sumCy"])}</p>'
                     f'<div class="mab-grid">{"".join(tale(t, g["era"]) for t in g["tales"])}</div></div></section>' for k, g in enumerate(MB.GROUPS))
    jump = '<nav class="chips l-jump" aria-label="Sections / Adrannau">' + "".join(f'<a class="chip" href="#mab-{k + 1}">{bi(g["en"], g["cy"])}</a>' for k, g in enumerate(MB.GROUPS)) + '</nav>'
    main = (hero("medieval", f'<a href="index.html">{SITE}</a> / <a href="legends.html">{bi("Legends", "Chwedlau")}</a>', "book", "Eleven tales", "Un chwedl ar ddeg", "The Mabinogion", "Y Mabinogion",
                 "The great tales of medieval Wales: the Four Branches of the Mabinogi, the native tales and the three romances, kept for six hundred years in the White Book and the Red Book.",
                 "Chwedlau mawr Cymru’r Oesoedd Canol: Pedair Cainc y Mabinogi, y chwedlau brodorol a’r tair rhamant, a gadwyd am chwe chan mlynedd yn y Llyfr Gwyn a’r Llyfr Coch.", art="book", extra=jump)
            + f'<section class="article"><div class="wrap narrow">{prose_bi(MB.INTRO_EN, MB.INTRO_CY)}'
              f'<p class="l-links"><a class="btn" href="person-arthur.html">{bi("Arthur, King of the Britons", "Arthur, Brenin y Brythoniaid")} →</a></p></div></section>'
            + groups
            + section(f'<div class="pager"><a class="btn" href="legends.html">← {bi("All legends", "Pob chwedl")}</a><a class="btn solid" href="legend-pwyll.html">{bi("Begin with the First Branch", "Dechrau â’r Gainc Gyntaf")} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": "The Mabinogion", "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page("mabinogion.html", "The Mabinogion · History of Wales", "The Mabinogion: the eleven great tales of medieval Wales, the White Book of Rhydderch and the Red Book of Hergest, and Lady Charlotte Guest’s translation, in English and Cymraeg.",
                main, era="medieval", ld=ld, active="legends.html", track="page:mabinogion")


def symbols_page():
    cards = "".join(f'<article class="sym rv" id="{s[0]}" data-era="{D.ERAS[i % len(D.ERAS)]["id"]}"><span class="sym-n">{i + 1:02d}</span><h2>{bi(s[3], s[1])}</h2>'
                    + (f'<p class="sym-alt">{bi(s[1], s[3])}</p>' if s[1] != s[3] else "") + f'<p>{bi(s[4], s[5])}</p></article>' for i, s in enumerate(F.SYMBOLS))
    main = (hero("modern", f'<a href="index.html">{SITE}</a>', "harp", "Symbols and traditions", "Symbolau a thraddodiadau", "The dragon, the leek and the grey mare", "Y ddraig, y genhinen a’r Fari Lwyd",
                 "Where the emblems and customs of Wales come from. Some are a thousand years old; some are younger than they look.", "O ble daw arwyddluniau ac arferion Cymru. Mae rhai’n fil o flynyddoedd oed; mae rhai’n iau nag y maent yn edrych.", art="dragons")
            + section(f'<div class="sym-grid">{cards}</div>', top=True)
            + section(f'<div class="pager"><a class="btn" href="legends.html">← {bi("Legends", "Chwedlau")}</a><a class="btn solid" href="stories.html">{bi("Long reads", "Erthyglau")} →</a></div>'))
    return page("symbols.html", "Symbols and traditions · History of Wales", "The red dragon, the leek, the daffodil, the harp, the Eisteddfod, lovespoons, the Mari Lwyd and more: where the symbols of Wales come from.", main, era="modern", og_type="website")


def gallery_items():
    """Every gallery picture as a dict, grouped by category, in page order."""
    items = {c: [] for c in G.CAT_IDS}

    def add(gid, cat, en, cy, sub, link):
        ph = GP.GALLERY.get(gid)
        if ph:
            items[cat].append(dict(id=gid, en=en, cy=cy, sub=sub, link=link, ph=ph))
    order = {x["id"]: i for i, x in enumerate(D.ERAS)}
    for pl in sorted(D.PLACES, key=lambda x: order.get(x["era"], 0)):
        add("place-" + pl["id"], G.PLACE_CAT.get(pl["id"], "buildings"), pl["en"], pl["cy"], pl["year"], f'place-{pl["id"]}.html')
    for gid, (cat, en, cy, link) in G.EXTRA.items():
        add(gid, cat, en, cy, "", link)
    for p in D.PEOPLE:
        add("person-" + p[0], "people", p[3], p[4], p[2], f"person-{p[0]}.html")
    return items


def gallery_page():
    items = gallery_items()
    total = sum(len(v) for v in items.values())

    def tile(it):
        f, by, lic, licu, wen, wcy, w, h = it["ph"]
        tall = h > w * 1.05
        ratio = max(0.75, min(1.6, w / h))
        th = round(600 / ratio)
        return (f'<a class="g-item{" tall" if tall else ""}" href="{it["link"] or "gallery/" + it["id"] + ".webp"}" data-full="gallery/{it["id"]}.webp"'
                f' data-go="{it["link"] or ""}" data-by="{e(by)}" data-lic="{e(lic)}" data-licu="{e(licu)}" data-file="{e(COMMONS + "File:" + _q(f, safe=""))}"'
                f' data-wen="{e(wen)}" data-wcy="{e(wcy)}" style="--ar:{ratio:.3f}">'
                f'<img src="gallery/{it["id"]}-s.webp" width="600" height="{th}" alt="{e(wen)}" loading="lazy" decoding="async">'
                f'<span class="cap"><b>{bi(it["en"], it["cy"])}</b>' + (f'<span>{e(it["sub"])}</span>' if it["sub"] else "") + '</span></a>')

    chips = (f'<button type="button" class="g-chip on" data-cat="all" aria-pressed="true">{bi("All", "Y cyfan")} <i>{total}</i></button>'
             + "".join(f'<button type="button" class="g-chip" data-cat="{c[0]}" aria-pressed="false">{bi(c[1], c[2])} <i>{len(items[c[0]])}</i></button>' for c in G.CATS if items[c[0]]))
    secs = "".join(f'<section class="g-sec" id="{c[0]}" data-cat="{c[0]}"><div class="g-head"><h2>{bi(c[1], c[2])}</h2><span class="g-cnt">{len(items[c[0]])}</span></div>'
                   f'<p class="muted g-blurb">{bi(c[3], c[4])}</p><div class="gallery">{"".join(tile(it) for it in items[c[0]])}</div></section>' for c in G.CATS if items[c[0]])
    credits = "".join(f'<li><b>{bi(it["en"], it["cy"])}</b>: {e(it["ph"][1])}, <a href="{e(it["ph"][3])}" target="_blank" rel="noopener license">{e(it["ph"][2])}</a>, '
                      f'<a href="{COMMONS}File:{_q(it["ph"][0], safe="")}" target="_blank" rel="noopener">{bi("Wikimedia Commons", "Wikimedia Commons")}</a></li>'
                      for c in G.CAT_IDS for it in items[c])
    box = ('<dialog class="g-box" id="g-box" aria-label="Picture / Llun"><div class="g-stage"><img alt=""><button type="button" class="g-x" data-x aria-label="Close / Cau">×</button>'
           '<button type="button" class="g-prev" aria-label="Previous / Blaenorol">‹</button><button type="button" class="g-next" aria-label="Next / Nesaf">›</button></div>'
           '<div class="g-info"><p class="g-count"></p><h3></h3><p class="g-what"></p><p class="g-cred"></p><a class="btn solid g-go" href="#">' + bi("Read the story", "Darllen y stori") + ' →</a></div></dialog>')
    main = (hero("industrial", f'<a href="index.html">{SITE}</a>', "castle", "Photo gallery", "Oriel luniau", "Wales in pictures", "Cymru mewn lluniau",
                 f"{total} photographs of the castles, churches, ancient stones, mountains, treasures and people of Wales. Choose a picture to see it large.",
                 f"{total} o ffotograffau o gestyll, eglwysi, hen feini, mynyddoedd, trysorau a phobl Cymru. Dewiswch lun i’w weld yn fawr.", art="castle")
            + f'<div class="g-bar"><div class="wrap"><div class="g-chips" role="toolbar" aria-label="Categories / Categorïau">{chips}</div></div></div>'
            + f'<div class="g-secs"><div class="wrap">{secs}</div></div>'
            + section(f'<details class="g-credits"><summary>{bi("Picture credits", "Cydnabyddiaeth y lluniau")}</summary>'
                      f'<p class="muted">{bi("Every photograph is from Wikimedia Commons under a free licence. Thank you to each photographer.", "Daw pob ffotograff o Wikimedia Commons dan drwydded rydd. Diolch i bob ffotograffydd.")}</p><ol>{credits}</ol></details>')
            + box)
    return page("gallery.html", "Photo gallery · History of Wales", f"{total} photographs of the castles, churches, ancient sites, landscapes, treasures and people of Wales.", main,
                era="industrial", og_type="website", extra='<script src="gallery.js?v=1" defer></script>\n')


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



# ---------- On this day (src/onthisday.py + the dated EVENTS) ----------
OTD_ORDER = {"feast": 0, "custom": 0, "ev": 1, "born": 2, "died": 2}
OTD_TAG = {"born": ("Born", "Ganed"), "died": ("Died", "Bu farw"), "feast": ("Feast day", "Dydd gŵyl"), "custom": ("Tradition", "Traddodiad")}
MONTHS = [("January", "Ionawr"), ("February", "Chwefror"), ("March", "Mawrth"), ("April", "Ebrill"), ("May", "Mai"), ("June", "Mehefin"),
          ("July", "Gorffennaf"), ("August", "Awst"), ("September", "Medi"), ("October", "Hydref"), ("November", "Tachwedd"), ("December", "Rhagfyr")]
_DAYS_IN = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def era_of_year(y):
    for lim, eid in ((48, "ancient"), (410, "roman"), (800, "saints"), (1100, "kings"), (1485, "medieval"), (1750, "tudor"), (1914, "industrial"), (1997, "modern")):
        if y < lim:
            return eid
    return "today"


def otd_rows():
    """Every dated entry: [MM-DD, year or None, kind, titleEn, titleCy, lineEn, lineCy, link, era]."""
    rows = []
    for i, ev in enumerate(D.EVENTS):
        if ev[4]:
            st = story_links("events", ev[5])
            rows.append([ev[4], ev[1], "ev", ev[5], ev[6], ev[7], ev[8], f'story-{st[0]["id"]}.html' if st else f"era-{ev[0]}.html#e{i}", ev[0]])
    covered = {r[7][6:] for r in OTD.OTD if r[7].startswith("saint:")}
    for md, y, k, te, tc, le, lc, link in OTD.OTD:
        if link.startswith("saint:"):
            link = saint_href(link[6:])
        rows.append([md, y, k, te, tc, le, lc, link, era_of_year(y) if y is not None else "saints" if k == "feast" else "modern"])
    for sid, (x, r) in SAINT.items():  # every other saint with a feast day on the Saints of Wales page
        if x["feast"] and sid not in covered:
            first = lambda t: t.split(". ")[0].rstrip(".") + "."
            rows.append([f'{x["feast"][1]:02d}-{x["feast"][0]:02d}', None, "feast", x["en"], x["cy"], first(x["nEn"]), first(x["nCy"]), saint_href(sid), "saints"])
    rows.sort(key=lambda r: (r[0], OTD_ORDER[r[2]], r[1] if r[1] is not None else -10 ** 6))
    return rows


def otd_item(r):
    md, y, k, te, tc, le, lc, link, era = r
    tag = OTD_TAG.get(k)
    when = (f'<span class="y">{y}</span>' if y is not None else "") + (f'<span class="k">{bi(*tag)}</span>' if tag else "")
    title = bi(te, tc)
    if link:
        title = f'<a href="{e(link)}">{title}</a>'
    return f'<li data-era="{era}" class="k-{k}"><p class="when">{when}</p><div><h4>{title}</h4><p>{bi(le, lc)}</p></div></li>'


def onthisday_page():
    rows = otd_rows()
    by_day = {}
    for r in rows:
        by_day.setdefault(r[0], []).append(r)
    months = ""
    for m, (en, cy) in enumerate(MONTHS):
        days = ""
        for d in range(1, _DAYS_IN[m] + 1):
            md = f"{m + 1:02d}-{d:02d}"
            if md in by_day:
                days += (f'<article class="otd-day" id="d-{md}"><h3><span class="dn">{d}</span> {bi(en, cy)}</h3>'
                         f'<ul class="otd-list">{"".join(otd_item(r) for r in by_day[md])}</ul></article>')
        months += f'<section class="otd-month" id="m-{m + 1:02d}" aria-labelledby="mh-{m + 1:02d}"><div class="wrap"><h2 class="sub-h" id="mh-{m + 1:02d}">{bi(en, cy)}</h2><div class="otd-days">{days}</div></div></section>'
    jump = "".join(f'<a class="chip" href="#m-{m + 1:02d}">{bi(en[:3], cy)}</a>' for m, (en, cy) in enumerate(MONTHS))
    n_days = len(by_day)
    main = (hero("medieval", f'<a href="index.html">{SITE}</a>', "book", "A year of Welsh history", "Blwyddyn o hanes Cymru", "On this day in Welsh history", "Ar y dydd hwn yn hanes Cymru",
                 f"{len(rows)} dates from the history of Wales, across {n_days} days of the year: battles and treaties, saints’ days and old customs, and the births of the people who made Wales.",
                 f"{len(rows)} o ddyddiadau o hanes Cymru, ar draws {n_days} o ddyddiau’r flwyddyn: brwydrau a chytundebau, gwyliau’r saint a hen arferion, a geni’r bobl a wnaeth Gymru.", art="book")
            + f'<section class="tight otd-jump"><div class="wrap"><div class="otd-chips"><a class="chip solid" id="otd-today" href="#">{bi("Today", "Heddiw")}</a>{jump}</div></div></section>'
            + months)
    extra = ('<script>(function(){var n=new Date(),md=("0"+(n.getMonth()+1)).slice(-2)+"-"+("0"+n.getDate()).slice(-2),el=document.getElementById("d-"+md),b=document.getElementById("otd-today");'
             'if(!el){var all=[].slice.call(document.querySelectorAll(".otd-day"));el=all.filter(function(a){return a.id.slice(2)>=md})[0]||all[0]}'
             'if(el){el.classList.add("is-today");b.href="#"+el.id}else b.hidden=true})()</script>\n')
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "On this day in Welsh history", "inLanguage": ["en", "cy"], "url": BASE_URL + "onthisday.html"}
    return page("onthisday.html", "On this day in Welsh history · History of Wales", "What happened on each day of the year in the history of Wales: events, saints’ days, traditions, births and deaths, in English and Cymraeg.",
                main, era="medieval", og_type="website", ld=ld, extra=extra)

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
CY_ORD = {1: "1af", 2: "2il", 3: "3ydd", 4: "4ydd", 5: "5ed", 6: "6ed", 7: "7fed", 8: "8fed", 9: "9fed", 10: "10fed", 11: "11eg", 12: "12fed",
          13: "13eg", 14: "14eg", 15: "15fed", 16: "16eg", 17: "17eg", 18: "18fed", 19: "19eg", 20: "20fed"}


def saints_btn(realm_id):
    reg = [x for x in SA.REGIONS if x["realm"] == realm_id]
    return "".join(f'<a class="btn" href="saints-{x["id"]}.html">{bi("Saints of " + x["en"], "Seintiau " + x["cy"])} →</a>' for x in reg)


def realm_page(r, i):
    t_en, t_cy = realm_title(r)
    nxt = RY.REALMS[(i + 1) % len(RY.REALMS)]
    places = [PLACE[p] for p in r["places"] if p in PLACE]
    main = (hero(r["era"], f'<a href="index.html">{SITE}</a> / <a href="kings.html">{bi("Kings and princes", "Brenhinoedd a thywysogion")}</a>', "crown",
                 r["span"], cy_dates(r["span"]), t_en, t_cy, r["subEn"], r["subCy"], art=r["art"])
            + section(paras(r["introEn"], r["introCy"]) + ft_link_for_realm(r["id"]), top=True)
            + section(ruler_list(r["rulers"]) + f'<p class="note-box" style="margin-top:2rem">{ROYAL_NOTE}</p>', *(() if r["rulers"][0]["k"] == "h" else ("The rulers, in order", "Y rheolwyr, yn eu trefn")))
            + (section(f'<div class="era-places">{"".join(place_tile(p) for p in places)}</div>', "Places to visit", "Lleoedd i ymweld â nhw") if places else "")
            + section(f'<div class="pager"><a class="btn" href="kings.html">← {bi("All the kings and princes of Wales", "Holl frenhinoedd a thywysogion Cymru")}</a>{saints_btn(r["id"])}'
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

# ---------- Welsh word of the day and beginner's phrases (src/cymraeg.py, src/welsh.js) ----------
WELSH_JS_VER = 1
AUDIO_DIR = os.path.join(SRC, "static", "audio")
AUDIO_FILES = sorted(f[:-4] for f in os.listdir(AUDIO_DIR) if f.endswith(".mp3")) if os.path.isdir(AUDIO_DIR) else []
HEAR_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4z" fill="currentColor"/>'
            '<path d="M16 8.5a5 5 0 0 1 0 7M18.5 6a8.5 8.5 0 0 1 0 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>')
WELSH_SCRIPT = f'<script src="welsh.js?v={WELSH_JS_VER}" defer></script>\n'


def welsh_js():
    """The daily word: every word, a fixed shuffled order for ordinary days, and the fixed days."""
    import random
    ids = [w[0] for w in CYM.WORDS]
    assert len(set(ids)) == len(ids), "word ids in src/cymraeg.py must be unique"
    idx = {k: i for i, k in enumerate(ids)}
    fixed = {d: idx[k] for d, k in CYM.FIXED_DAYS.items()}
    order = [i for i in range(len(ids)) if i not in set(fixed.values())]
    random.Random(1176).shuffle(order)  # seeded, so the order only changes when words are added
    data = dict(W=[list(w) for w in CYM.WORDS], ORDER=order, DAYS=fixed, AUDIO=AUDIO_FILES)
    return "var CYW = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n" + read("welsh.js")


def hear_btn(text, guide):
    return f'<button type="button" class="hear" data-hear="{e(text)}" data-guide="{e(guide)}" aria-label="{e("Hear / Clywed: " + text)}">{HEAR_SVG}</button>'


def welsh_page():
    jump = "".join(f'<a class="chip" href="#{s[0]}">{bi(s[1], s[2])}</a>' for s in CYM.PHRASES)
    secs = ""
    for sid, ten, tcy, ien, icy, items in CYM.PHRASES:
        lis = "".join(f'<li><b lang="cy">{e(cy)}</b><span class="say">{e(say)}</span><span class="mean" lang="en">{e(en)}</span>{hear_btn(cy, say)}</li>' for cy, say, en in items)
        secs += (f'<div class="cyw-sec" id="{sid}"><h3>{bi(ten, tcy)}</h3><p>{bi(ien, icy)}</p>'
                 f'<ul class="phr{" nums" if sid in ("numbers", "days") else ""}">{lis}</ul></div>')
    letters = "".join(f'<div><b lang="cy">{e(l)}</b><p><span>{bi(en, cy)}</span><em>{bi("as in", "fel yn")} <i lang="cy">{e(ex)}</i></em></p></div>' for l, en, cy, ex in CYM.LETTERS)
    credits = ""
    if CYM.AUDIO_CREDITS:
        credits = "<p>" + bi("Recordings:", "Recordiadau:") + " " + "; ".join(f'{e(f)}: <a href="{e(u)}">{e(who)}</a>, {e(lic)}' for f, (who, lic, u) in CYM.AUDIO_CREDITS.items()) + "</p>"
    note = (f'<div class="cyw-note"><p>{bi("Where a real recording of a word is available, the speaker button plays it. Otherwise your device reads the word aloud: devices with a Welsh voice installed, such as Microsoft Edge on Windows, speak real Welsh, and others read the sound guide in English.", "Lle mae recordiad go iawn o air ar gael, mae’r botwm sain yn ei chwarae. Fel arall mae eich dyfais yn darllen y gair yn uchel: mae dyfeisiau sydd â llais Cymraeg, fel Microsoft Edge ar Windows, yn siarad Cymraeg go iawn, ac mae eraill yn darllen y canllaw sain yn Saesneg.")}</p>'
            f'<p>{bi("In the sound guides, capital letters show the stressed syllable, kh is the ch of loch, and hl is the Welsh ll.", "Yn y canllawiau sain, mae priflythrennau’n dangos y sillaf acennog, kh yw ch yn loch, a hl yw’r ll Gymraeg.")}</p>{credits}</div>')
    main = (hero("modern", f'<a href="index.html">{SITE}</a> / <a href="index.html#language">{bi("Language", "Iaith")}</a>', "book", "Learn Welsh", "Dysgu Cymraeg",
                 "Speak a little Cymraeg", "Siaradwch ychydig o Gymraeg",
                 "The language of Taliesin, Hywel Dda and Glyndŵr is spoken every day in Wales. Start with a word a day and the phrases every visitor needs.",
                 "Mae iaith Taliesin, Hywel Dda a Glyndŵr i’w chlywed bob dydd yng Nghymru. Dechreuwch gyda gair y dydd a’r ymadroddion y mae pob ymwelydd eu hangen.", art="book")
            + section('<div class="wotd" data-wotd aria-live="polite"><noscript>Word of the day needs JavaScript.</noscript></div>', top=True)
            + section(f'<ul class="cyw-week" data-wotd-week></ul>', "The last seven days", "Y saith diwrnod diwethaf")
            + section(f'<p class="lede" style="margin-bottom:1.4rem">{bi("Welsh is spelt the way it sounds. Learn these few letters and you can say any place name in Wales. The stress almost always falls on the last syllable but one.", "Mae’r Gymraeg yn cael ei sillafu fel y mae’n swnio. Dysgwch y llythrennau hyn a gallwch ddweud unrhyw enw lle yng Nghymru. Mae’r acen bron bob amser ar y sillaf olaf ond un.")}</p><div class="letters">{letters}</div>',
                      "How Welsh sounds", "Sut mae’r Gymraeg yn swnio")
            + section(f'<div class="chips cyw-jump">{jump}</div>{secs}', "Beginner’s phrases", "Ymadroddion i ddechreuwyr")
            + section(note + f'<p class="more-row" style="margin-top:2rem"><a class="btn" href="index.html#language">{bi("Place-name decoder", "Datgodiwr enwau lleoedd")} →</a> '
                      f'<a class="btn" href="story-language.html">{bi("How the language survived", "Sut y goroesodd yr iaith")} →</a> <a class="btn" href="pairs.html">{bi("Word pairs game", "Gêm parau geiriau")} →</a></p>'))
    return page("welsh.html", "Learn Welsh · History of Wales", "A Welsh word of the day with its history, and the beginner’s phrases every visitor to Wales needs, with sound guides.",
                main, era="modern", og_type="website", active="welsh.html", extra=WELSH_SCRIPT)
# ---------- saints of Wales (src/saints.py) ----------
SREG = {r["id"]: r for r in SA.REGIONS}
SAINT = {x["id"]: (x, r) for r in SA.REGIONS for x in r["saints"]}
MONTHS = [("January", "Ionawr"), ("February", "Chwefror"), ("March", "Mawrth"), ("April", "Ebrill"), ("May", "Mai"), ("June", "Mehefin"),
          ("July", "Gorffennaf"), ("August", "Awst"), ("September", "Medi"), ("October", "Hydref"), ("November", "Tachwedd"), ("December", "Rhagfyr")]
# Llan places that have their own page on the site
LL_PAGE = {"Tyddewi": "stdavids", "Llanilltud Fawr": "llanilltud", "Ynys Enlli": "enlli", "Treffynnon": "treffynnon", "Llanrhaeadr-ym-Mochnant": "llanrhaeadr",
           "Llangollen": "llangollen", "Tyndyrn": "tintern", "Caer-went": "caerwent", "Llanfaches": "llanfaches", "Sain Ffagan": "stfagans",
           "Aberffraw": "aberffraw", "Pumsaint": "dolaucothi", "Merthyr Tudful": "merthyr"}
LL_PAGE = {k: v for k, v in LL_PAGE.items() if v in PLACE}


def feast_txt(f):
    d, m = f
    return (f"{d} {MONTHS[m - 1][0]}", f"{d} {MONTHS[m - 1][1]}")


def saint_href(sid):
    return f'saints-{SAINT[sid][1]["id"]}.html#s-{sid}'


def ll_chip(name):
    lat, lon, en, away = SA.LL[name]
    sub = f'<small class="l-en" lang="en"> · {e(en)}</small>' if en else ""
    inner = f'{e(name)}{sub}'
    cls = "chip ll" + (" away" if away else "")
    if name in LL_PAGE:
        return f'<a class="{cls}" href="place-{LL_PAGE[name]}.html">{inner}</a>'
    return f'<span class="{cls}">{inner}</span>'


def saint_li(x, r=None, chips=""):
    link = x["link"]
    more = ""
    if link:
        lab = ("Read more", "Darllen mwy") if link.startswith("person-") else ("See the kings", "Gweld y brenhinoedd")
        more = f'<a class="src" href="{link}">{bi(*lab)} →</a>'
    feast = f'<p class="feast">{bi("Feast day " + feast_txt(x["feast"])[0], "Dydd gŵyl " + feast_txt(x["feast"])[1])}</p>' if x["feast"] else ""
    places = "".join(ll_chip(n) for n in x["places"])
    places = f'<div class="ll-chips" aria-label="Places named after them">{places}</div>' if places else ""
    links = f'<div class="links">{more}{chips}</div>' if (more or chips) else ""
    return (f'<li id="s-{x["id"]}" class="{"key" if x["key"] else ""}"><time>{bi(x["dates"], cy_dates(x["dates"]))}</time>'
            f'<div><h3>{bi(x["en"], x["cy"])}</h3>{feast}<p>{bi(x["nEn"], x["nCy"])}</p>{places}{links}</div></li>')


def saints_map(focus=None):
    """Every llan on the map of Wales, one dot per place, coloured by the region of its saint. focus: a region id to pick out."""
    sc, k, minx, maxy = geo["sc"], geo["k"], geo["minx"], geo["maxy"]
    at = {}
    for r in SA.REGIONS:
        for x in r["saints"]:
            for n in x["places"]:
                at.setdefault(n, []).append((x, r))
    dots = []
    for n, who in at.items():
        lat, lon, en, away = SA.LL[n]
        if away:
            continue
        cx, cy = (lon - minx) * k * sc, (maxy - lat) * sc
        reg = who[0][1]
        on = focus is None or any(rr["id"] == focus for _, rr in who)
        ids = " ".join(x["id"] for x, _ in who)
        dots.append((not on, f'<g class="sm-dot{"" if on else " dim"}" tabindex="0" role="button" data-n="{e(n)}" data-en="{e(en or "")}" data-s="{ids}" data-r="{reg["id"]}" style="--c:{reg["col"]}" transform="translate({cx:.1f} {cy:.1f})">'
                     f'<circle class="h" r="15"/><circle class="d" r="6"/><title>{e(n)}: {e(", ".join(x["en"] for x, _ in who))}</title></g>'))
    dots.sort(key=lambda d: d[0], reverse=True)  # dimmed dots first, so the region's own sit on top
    return (f'<svg class="sm-map" viewBox="-20 -20 640 711" role="group" aria-label="Map of Wales showing the llannau named after the saints">'
            f'<text class="sea-l" x="40" y="430">{bi("CARDIGAN BAY", "BAE CEREDIGION", "tspan")}</text><text class="sea-l" x="80" y="680">{bi("BRISTOL CHANNEL", "MÔR HAFREN", "tspan")}</text>'
            f'<path class="land" d="{geo["outline"]}"/>{"".join(d[1] for d in dots)}</svg>')


def saints_map_block(focus=None):
    opts = "".join(f'<optgroup label="{e(r["en"])} / {e(r["cy"])}">' + "".join(f'<option value="{x["id"]}">{e(x["en"])} / {e(x["cy"])}</option>' for x in r["saints"] if any(not SA.LL[n][3] for n in x["places"])) + "</optgroup>"
                   for r in SA.REGIONS if focus in (None, r["id"]))
    legend = "" if focus else '<div class="chips sm-legend" role="group" aria-label="Regions">' + "".join(
        f'<a class="chip" href="saints-{r["id"]}.html" style="--c:{r["col"]}"><i></i>{bi(r["en"], r["cy"])}</a>' for r in SA.REGIONS) + "</div>"
    return (f'<div class="sm-grid"><div class="sm-box">{saints_map(focus)}</div><div class="sm-side">'
            f'<label class="sm-pick"><span>{bi("Show the churches of", "Dangos eglwysi")}</span><select id="sm-saint"><option value="">{e("All the saints / Yr holl saint")}</option>{opts}</select></label>'
            f'<div class="sm-card" id="sm-card" aria-live="polite"><p class="muted">{bi("Tap a dot to see whose llan it is.", "Tapiwch ddot i weld llan pwy yw hi.")}</p></div>{legend}</div></div>')


def llan_decoder():
    rows = "".join(f'<div class="mut"><b>{e(a)}</b><span>{e(b)}</span><i>{e(c)}</i></div>' for a, b, c in SA.MUTATIONS)
    known = {}
    for r in SA.REGIONS:
        for x in r["saints"]:
            for n in x["places"]:
                if not SA.LL[n][3]:
                    known.setdefault(n.split(" (")[0], [])
                    if x["id"] not in known[n.split(" (")[0]]:
                        known[n.split(" (")[0]].append(x["id"])
    saints = {sid: [x["en"], x["cy"], saint_href(sid), r["en"], r["cy"]] for sid, (x, r) in SAINT.items()}
    other = {a: [b, c, d] for a, b, c, d in SA.OTHER_LLAN}
    data = json.dumps(dict(k=known, s=saints, o=other), ensure_ascii=False, separators=(",", ":"))
    names = sorted(set(list(known) + list(other)))
    return (f'<div class="mut-grid" aria-label="How llan changes a name">{rows}</div>'
            f'<form class="ll-dec" id="ll-dec" autocomplete="off"><label for="ll-in">{bi("Unpick a place name", "Datod enw lle")}</label>'
            f'<div class="near-form"><input id="ll-in" type="text" list="ll-names" placeholder="e.g. Llangollen" data-cy-ph="e.e. Llangollen">'
            f'<datalist id="ll-names">{"".join(f"<option value=\"{e(n)}\">" for n in names)}</datalist><button type="submit" class="btn">{bi("Who is it?", "Pwy yw e?")}</button></div>'
            f'<div class="ll-out" id="ll-out" aria-live="polite"></div></form><script>var LLDEC={data};</script>')


def saints_calendar():
    by = {m: [] for m in range(1, 13)}
    for sid, (x, r) in SAINT.items():
        if x["feast"]:
            by[x["feast"][1]].append((x["feast"][0], x))
    cells = ""
    for m in range(1, 13):
        items = "".join(f'<li data-d="{d}" data-m="{m}"><b>{d}</b><a href="{saint_href(x["id"])}">{bi(x["en"], x["cy"])}</a></li>' for d, x in sorted(by[m], key=lambda t: t[0]))
        cells += f'<div class="cal-m"><h3>{bi(*MONTHS[m - 1])}</h3><ol>{items}</ol></div>'
    return f'<div class="cal">{cells}</div>'


def feasts_json():
    out = [[x["feast"][1], x["feast"][0], x["en"], x["cy"], saint_href(sid), x["nEn"].split(". ")[0] + ".", x["nCy"].split(". ")[0] + "."] for sid, (x, r) in SAINT.items() if x["feast"]]
    return json.dumps(sorted(out), ensure_ascii=False, separators=(",", ":"))


SAINTS_JS = '<script src="saints.js?v=2" defer></script>\n'
SAINTS_CSS = """
.ll-chips { display: flex; flex-wrap: wrap; gap: .35rem; margin-top: .6rem }
.chip.ll { font: 500 .8rem var(--f-body); padding: .22rem .7rem; cursor: default; color: var(--ink); border-color: color-mix(in srgb, var(--c) 45%, var(--line)) }
.chip.ll small { color: var(--muted); font-size: .74rem }
a.chip.ll { cursor: pointer } a.chip.ll:hover { border-color: var(--c) }
.chip.ll.away { border-style: dashed }
.era-events .feast { font: 500 .78rem var(--f-mono); color: var(--c); letter-spacing: .04em; margin-top: .15rem }
.sm-grid { display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr); gap: 2rem; align-items: start }
.sm-map { width: 100%; height: auto; display: block; overflow: visible }
.sm-map .sea-l { font-size: 15px }
.sm-dot { cursor: pointer; outline: none }
.sm-dot .d { fill: var(--c); stroke: var(--night); stroke-width: 2; transition: r .2s, opacity .2s }
.sm-dot .h { fill: var(--c); opacity: 0; transition: opacity .2s }
.sm-dot:hover .h, .sm-dot:focus-visible .h { opacity: .3 }
.sm-dot.sel .h { opacity: .35; animation: pulse 2.2s ease-out infinite }
.sm-dot.sel .d { r: 8 }
.sm-dot.dim { opacity: .2 }
.sm-dot.hit .d { r: 7.5 }
.sm-side { display: grid; gap: 1.2rem }
.sm-pick { display: grid; gap: .4rem; font: 500 .8rem var(--f-mono); color: var(--muted); text-transform: uppercase; letter-spacing: .08em }
.sm-pick select { font: 500 1rem var(--f-body); color: var(--ink); background: var(--slate); border: 1px solid var(--line); border-radius: 12px; padding: .7rem .9rem; text-transform: none; letter-spacing: 0; width: 100% }
.sm-card { background: var(--slate); border: 1px solid var(--line); border-left: 4px solid var(--c, var(--e-saints)); border-radius: 0 16px 16px 0; padding: 1.1rem 1.3rem; min-height: 6rem; display: grid; gap: .5rem; align-content: start }
.sm-card h3 { font-family: var(--f-display); font-weight: 400; font-size: 1.7rem; line-height: 1.1 }
.sm-card .en { color: var(--muted); font-size: .9rem }
.sm-card ul { list-style: none; padding: 0; margin: 0; display: grid; gap: .35rem }
.sm-card .go { font-weight: 700 }
.sm-legend { display: flex; flex-wrap: wrap; gap: .45rem }
.sm-legend .chip { font-size: .82rem; padding: .3rem .8rem }
.mut-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(46%, 12.5rem), 1fr)); gap: .7rem; margin: 1.6rem 0 }
.mut { display: grid; grid-template-columns: auto 1fr; gap: .1rem .8rem; align-items: baseline; background: var(--slate); border: 1px solid var(--line); border-radius: 14px; padding: .8rem 1rem }
.mut b { font: 500 .85rem var(--f-mono); color: var(--muted) } .mut b::before { content: "Llan + " }
.mut span { grid-column: 1 / -1; font: 400 clamp(1.25rem, 4.2vw, 1.6rem)/1.1 var(--f-display); color: var(--ink) }
.mut i { grid-column: 1 / -1; font: 500 .75rem var(--f-mono); font-style: normal; color: var(--c) }
.ll-dec { display: grid; gap: .6rem; margin-top: 1rem }
.ll-dec > label { font: 500 .8rem var(--f-mono); color: var(--muted); text-transform: uppercase; letter-spacing: .08em }
.ll-out:empty { display: none }
.ll-out { background: var(--slate); border: 1px solid var(--line); border-left: 4px solid var(--c); border-radius: 0 16px 16px 0; padding: 1.1rem 1.3rem; display: grid; gap: .4rem; animation: up .4s var(--ease) both }
.ll-out .eq { font: 400 clamp(1.5rem, 4vw, 2.2rem)/1.15 var(--f-display) } .ll-out .eq em { color: var(--c); font-style: normal }
.today-card { margin-top: 2rem; display: grid; gap: .4rem; background: radial-gradient(120% 140% at 100% 0%, color-mix(in srgb, var(--e-saints) 22%, transparent), transparent 60%), var(--slate); border: 1px solid color-mix(in srgb, var(--e-saints) 40%, var(--line)); border-radius: 18px; padding: 1.3rem 1.5rem }
.today-card .eyebrow { color: var(--e-saints) }
.today-card h3 { font: 400 clamp(1.8rem, 4.5vw, 2.6rem)/1.05 var(--f-display) }
.today-card p { color: var(--muted) }
.cal { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 15rem), 1fr)); gap: 1rem }
.cal-m { background: var(--slate); border: 1px solid var(--line); border-radius: 14px; padding: 1rem 1.1rem }
.cal-m h3 { font: 500 .8rem var(--f-mono); text-transform: uppercase; letter-spacing: .1em; color: var(--e-saints); margin-bottom: .5rem }
.cal-m ol { list-style: none; margin: 0; padding: 0; display: grid; gap: .3rem }
.cal-m li { display: grid; grid-template-columns: 1.8rem 1fr; gap: .5rem; align-items: baseline }
.cal-m li b { font: 500 .85rem var(--f-mono); color: var(--muted) }
.cal-m li a { color: var(--ink); text-decoration: none } .cal-m li a:hover { text-decoration: underline }
.cal-m li.today { background: color-mix(in srgb, var(--e-saints) 18%, transparent); border-radius: 8px; margin: 0 -.4rem; padding: .1rem .4rem }
.cal-m li.today b { color: var(--e-saints) }
.saints-h { margin-top: 2.8rem; display: flex; flex-wrap: wrap; align-items: baseline; gap: .4rem 1rem; font-size: clamp(1.8rem, 4.5vw, 2.4rem) }
.saints-h a { font: 600 .85rem var(--f-body); color: var(--c); text-decoration: none } .saints-h a:hover { text-decoration: underline }
@media (max-width: 820px) { .sm-grid { grid-template-columns: 1fr; gap: 1.2rem } .sm-side { display: contents } .sm-pick { order: -1 } }
"""
style += SAINTS_CSS


def saint_region_tile(r):
    n = len(r["saints"])
    return (f'<a href="saints-{r["id"]}.html" data-era="{r["era"]}" style="--c:{r["col"]}"><svg aria-hidden="true"><use href="#i-{"ship" if not r["realm"] else "cross"}"/></svg>'
            f'<span><b>{bi(r["en"], r["cy"])}</b><span>{bi(f"{n} saints", f"{n} o saint")}</span></span></a>')


# person and place pages link to the saints region that names them
SAINTS_OF = {}
for _r in SA.REGIONS:
    for _x in _r["saints"]:
        if _x["link"] and _x["link"].startswith("person-"):
            SAINTS_OF.setdefault(_x["link"], []).append(_r["id"])
        for _n in _x["places"]:
            if _n in LL_PAGE:
                SAINTS_OF.setdefault(f"place-{LL_PAGE[_n]}.html", []).append(_r["id"])
    for _pid in _r["places"]:
        SAINTS_OF.setdefault(f"place-{_pid}.html", []).append(_r["id"])


def saints_links(href):
    ids = list(dict.fromkeys(SAINTS_OF.get(href, [])))
    return "".join(f'<a href="saints-{i}.html">{bi("Saints of " + SREG[i]["en"], "Seintiau " + SREG[i]["cy"])} →</a>' for i in ids)


def saints_page():
    every = ""
    for r in SA.REGIONS:
        every += (f'<h3 class="sub-h saints-h" style="--c:{r["col"]}">{bi(r["en"], r["cy"])}<a href="saints-{r["id"]}.html">{bi("The region’s page", "Tudalen y rhanbarth")} →</a></h3>'
                  f'<ol class="era-events royal" data-era="{r["era"]}">{"".join(saint_li(x) for x in r["saints"])}</ol>')
    dewi = SAINT["dewi"][0]
    lead = (f'<aside class="behind one-king"><p class="eyebrow">{bi("Feast day 1 March · Patron saint of Wales", "Dydd gŵyl 1 Mawrth · Nawddsant Cymru")}</p>'
            f'<h2>{bi("Dewi Sant, Saint David", "Dewi Sant")}</h2>' + paras(SA.DEWI["en"], SA.DEWI["cy"]) +
            f'<p><a class="go" href="person-dewi-sant.html">{bi("Read his story", "Darllen ei hanes")} →</a> &nbsp; <a class="go" href="saints-dyfed.html">{bi("The saints of Dyfed", "Seintiau Dyfed")} →</a> &nbsp; <a class="go" href="place-stdavids.html">{bi("Visit St Davids", "Ymweld â Thyddewi")} →</a></p></aside>')
    today = (f'<div class="today-card" id="today-saint"><p class="eyebrow">{bi("The saints’ calendar", "Calendr y saint")}</p>'
             f'<h3>{bi(dewi["en"], dewi["cy"])}</h3><p>{bi("Every saint on this page has a feast day. Their days are listed in the calendar at the foot of the page.", "Mae gan bob sant ar y dudalen hon ddydd gŵyl. Rhestrir eu dyddiau yn y calendr ar waelod y dudalen.")}</p></div>')
    n_all = len(SAINT)
    n_ll = len({n for r in SA.REGIONS for x in r["saints"] for n in x["places"] if not SA.LL[n][3]})
    main = (hero("saints", f'<a href="index.html">{SITE}</a>', "cross", "c. 400–700 · The Age of the Saints", "tua 400–700 · Oes y Saint", "Saints of Wales", "Seintiau Cymru",
                 "Before the castles, there were the llannau. The saints of Wales founded the churches that still carry their names, taught at the oldest school in Britain, and carried the faith to Cornwall, Brittany and Ireland.",
                 "Cyn y cestyll, roedd y llannau. Sefydlodd seintiau Cymru’r eglwysi sy’n dwyn eu henwau o hyd, dysgu yn ysgol hynaf Prydain, a chario’r ffydd i Gernyw, Llydaw ac Iwerddon.", art="cross")
            + section(paras(SA.LEAD["en"], SA.LEAD["cy"]) + today, top=True)
            + section(lead)
            + section(paras(SA.LLAN["en"], SA.LLAN["cy"]) + llan_decoder(), "What is a llan?", "Beth yw llan?")
            + section(f'<p class="lede">{bi(f"{n_ll} churches and holy places named after the saints on this page. Pick a saint to see how far their name spread.", f"{n_ll} o eglwysi a lleoedd sanctaidd a enwyd ar ôl y saint ar y dudalen hon. Dewiswch sant i weld pa mor bell yr ymledodd ei enw.")}</p>' + saints_map_block(), "The map of the llannau", "Map y llannau")
            + section(f'<div class="era-places">{"".join(saint_region_tile(r) for r in SA.REGIONS)}</div>', "The saints, region by region", "Y saint, fesul rhanbarth")
            + section(f'<p class="lede">{bi(f"All {n_all} saints on this site, with the places that carry their names.", f"Pob un o’r {n_all} sant ar y wefan hon, gyda’r lleoedd sy’n dwyn eu henwau.")}</p>' + every
                      + f'<p class="note-box" style="margin-top:2rem">{bi(SA.NOTE["en"], SA.NOTE["cy"])}</p>', "Every saint", "Pob sant")
            + section('<span id="cal"></span>' + saints_calendar(), "The saints’ calendar", "Calendr y saint")
            + section(f'<div class="pager"><a class="btn" href="era-saints.html">← {bi("The Age of the Saints", "Oes y Saint")}</a><a class="btn solid" href="kings.html">{bi("Kings and princes of Wales", "Brenhinoedd a thywysogion Cymru")} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": "Saints of Wales", "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    extra = f'<script>var FEASTS={feasts_json()};</script>\n' + SAINTS_JS
    return page("saints.html", "Saints of Wales · History of Wales",
                "The saints of Wales, region by region: Dewi, Teilo, Padarn, Illtud, Cadog, Beuno, Gwenffrewi, Melangell and more, with a map of the llannau named after them.",
                main, era="saints", ld=ld, og_type="website", active="saints.html", track="saints:all", extra=extra)


def saints_region_page(r, i):
    nxt = SA.REGIONS[(i + 1) % len(SA.REGIONS)]
    places = [PLACE[p] for p in r["places"] if p in PLACE]
    t_en, t_cy = ("Saints of " + r["en"], "Seintiau " + r["cy"]) if r["realm"] else ("Saints across the sea", "Saint dros y môr")
    kings = (f'<a class="btn" href="kings-{r["realm"]}.html">{bi("Kings of " + REALM[r["realm"]]["en"], "Brenhinoedd " + REALM[r["realm"]]["cy"])} →</a>' if r["realm"] in REALM else "")
    main = (hero(r["era"], f'<a href="index.html">{SITE}</a> / <a href="saints.html">{bi("Saints of Wales", "Seintiau Cymru")}</a>', "cross",
                 r["span"], cy_dates(r["span"]), t_en, t_cy, r["subEn"], r["subCy"], art=r["art"])
            + section(paras(r["introEn"], r["introCy"]), top=True)
            + section(f'<ol class="era-events royal">{"".join(saint_li(x, r) for x in r["saints"])}</ol><p class="note-box" style="margin-top:2rem">{bi(SA.NOTE["en"], SA.NOTE["cy"])}</p>', "The saints", "Y saint")
            + section(saints_map_block(r["id"]), "Their llannau on the map", "Eu llannau ar y map")
            + (section(f'<div class="era-places">{"".join(place_tile(p) for p in places)}</div>', "Places to visit", "Lleoedd i ymweld â nhw") if places else "")
            + section(f'<div class="pager"><a class="btn" href="saints.html">← {bi("All the saints of Wales", "Holl seintiau Cymru")}</a>{kings}'
                      f'<a class="btn solid" href="saints-{nxt["id"]}.html">{bi(nxt["en"], nxt["cy"])} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": t_en, "description": r["subEn"], "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page(f"saints-{r['id']}.html", f"{t_en} · History of Wales", f"{r['subEn']} " + ", ".join(x["en"] for x in r["saints"]) + ".", main,
                era=r["era"], ld=ld, active="saints.html", track=f"saints:{r['id']}", extra=SAINTS_JS)


# ---------- Welsh world firsts (src/people2.py) ----------
FIELD_LABEL = {k: (en, cy) for k, en, cy in P2.FIELDS}


def first_year(y):
    return f"c. {-y:,} BC" if y < 0 else f"c. {y}" if y < 1000 else str(y)


def first_badge(slug):
    f = P2.FIRSTS.get(slug)
    if not f:
        return ""
    lab = ("World first", "Y cyntaf yn y byd") if f[0] == "world" else ("Welsh first", "Y Cymro cyntaf")
    return (f'<a class="first-badge" href="firsts.html#f-{slug}" data-kind="{f[0]}"><b>★ {bi(*lab)}</b> {bi(f[1], f[2])}</a>')


def first_card(slug=None, other=None):
    if slug:
        p = PERSON[slug]
        kind, en, cy, y = P2.FIRSTS[slug]
        ph = PH.PERSON_PHOTOS.get(slug)
        ini = "".join(w[0] for w in re.sub(r"\b(ap|ab|ferch|the|The|of|Sir|Dame|Lady|Dr)\b", " ", p[3]).split()[:1] + re.sub(r"\b(ap|ab|ferch|the|of)\b", " ", p[3]).split()[-1:]).upper()
        ava = (f'<span class="ava" aria-hidden="true">{e(ini)}' + (f'<img src="{photo_url(ph[0], 240)}" alt="" loading="lazy" referrerpolicy="no-referrer" onerror="this.remove()">' if ph else "") + "</span>")
        return (f'<a class="first-card" id="f-{slug}" href="person-{slug}.html" data-era="{p[1]}" data-kind="{kind}" data-field="{P2.FIELD.get(slug, "")}">'
                f'<span class="fy">{first_year(y)}</span><span class="who">{ava}<span><b>{bi(p[3], p[4])}</b><small>{bi(p[5], p[6])}</small></span></span>'
                f'<span class="what">{bi(en, cy)}</span></a>')
    kind, y, ten, tcy, xen, xcy, link = other
    return (f'<a class="first-card place" href="{link}" data-kind="{kind}"><span class="fy">{first_year(y)}</span>'
            f'<span class="who"><span class="ava" aria-hidden="true">★</span><span><b>{bi(ten, tcy)}</b></span></span><span class="what">{bi(xen, xcy)}</span></a>')


def firsts_page():
    def cards(kind):
        rows = [(v[3], first_card(slug=k)) for k, v in P2.FIRSTS.items() if v[0] == kind and k in PERSON]
        rows += [(o[1], first_card(other=o)) for o in P2.OTHER_FIRSTS if o[0] == kind]
        return len(rows), '<div class="firsts">' + "".join(c for _, c in sorted(rows, key=lambda r: r[0])) + "</div>"
    nw, world = cards("world")
    nh, home = cards("wales")
    chips = ('<div class="chips firsts-filter no-print" role="group" aria-label="Filter firsts by field">'
             f'<button type="button" class="chip" data-v="all" aria-pressed="true">{bi("All", "Y cyfan")}</button>'
             + "".join(f'<button type="button" class="chip" data-v="{k}" aria-pressed="false">{bi(en, cy)}</button>' for k, en, cy in P2.FIELDS
                       if any(P2.FIELD.get(s) == k for s in P2.FIRSTS)) + "</div>")
    lede = (f'<p class="lede">{bi("For a country of three million people, Wales has given the world a remarkable list of firsts: the equals sign and the symbol π, the fuel cell, the microphone, the first steam locomotive, mail order, packet switching that carries the internet, and the spare wheel. Here they all are, in order, with the people who made them.", "I wlad o dair miliwn o bobl, mae Cymru wedi rhoi rhestr ryfeddol o bethau cyntaf i’r byd: yr hafalnod a’r symbol π, y gell danwydd, y meicroffon, y locomotif stêm cyntaf, archebu drwy’r post, newid pecynnau sy’n cario’r rhyngrwyd, a’r olwyn sbâr. Dyma nhw i gyd, yn eu trefn, gyda’r bobl a’u gwnaeth.")}</p>'
            f'<p class="firsts-count"><span><b>{nw}</b> {bi("world firsts and records", "o bethau cyntaf a recordiau byd")}</span><span><b>{nh}</b> {bi("firsts for Wales, and Welsh firsts abroad", "o bethau cyntaf i Gymru, a Chymry cyntaf dramor")}</span></p>'
            f'<p><a class="go" href="story-firsts.html">{bi("Read the long read: Wales did it first", "Darllen yr erthygl: Cymru oedd y cyntaf")} →</a> &nbsp; <a class="go" href="index.html?field=first#people">{bi("See them among all the famous Welsh people", "Eu gweld ymhlith holl enwogion Cymru")} →</a></p>')
    note = bi("Some firsts are firsts for the world, some for Britain, and some are records. Where a claim rests on tradition, as with Madog, we say so. Tap any card to read the full story.",
              "Mae rhai’n bethau cyntaf i’r byd, rhai i Brydain, a rhai’n recordiau. Lle mae honiad yn dibynnu ar draddodiad, fel gyda Madog, rydym yn dweud hynny. Tapiwch unrhyw gerdyn i ddarllen yr hanes llawn.")
    main = (hero("industrial", f'<a href="index.html">{SITE}</a> / <a href="index.html#people">{bi("People", "Pobl")}</a>', "book", "From c. 410 to today", "O tua 410 hyd heddiw",
                 "Welsh world firsts", "Cymru oedd y cyntaf", "The things Wales and the Welsh gave the world first, and the people who did them.",
                 "Y pethau a roddodd Cymru a’r Cymry i’r byd gyntaf, a’r bobl a’u gwnaeth.", art="terrace")
            + section(lede + chips, top=True)
            + section(world, "World firsts and records", "Pethau cyntaf a recordiau’r byd")
            + section(home, "Firsts for Wales, and Welsh firsts abroad", "Pethau cyntaf i Gymru, a Chymry cyntaf dramor")
            + section(f'<p class="note-box">{note}</p><div class="pager" style="margin-top:2rem"><a class="btn" href="story-firsts.html">← {bi("Wales did it first", "Cymru oedd y cyntaf")}</a><a class="btn solid" href="index.html#people">{bi("All the people", "Yr holl bobl")} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": "Welsh world firsts", "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    js = ("<script>(function(){var b=document.querySelector('.firsts-filter');if(!b)return;b.onclick=function(ev){var c=ev.target.closest('.chip');if(!c)return;var v=c.dataset.v;"
          "b.querySelectorAll('.chip').forEach(function(x){x.setAttribute('aria-pressed',x===c)});"
          "document.querySelectorAll('.first-card').forEach(function(a){a.hidden=v!=='all'&&a.dataset.field!==v});};})();</script>")
    return page("firsts.html", "Welsh world firsts · History of Wales",
                "Everything Wales and the Welsh did first: the equals sign, π, the fuel cell, the microphone, the first steam locomotive, mail order, packet switching, the spare wheel and more.",
                main, era="industrial", ld=ld, og_type="website", active="firsts.html", track="firsts", extra=js)


# ---------- index ----------
FEATURED = ["dewi-sant", "hywel-dda", "gwenllian", "llywelyn-fawr", "llywelyn-ap-gruffudd", "dafydd-ap-gwilym", "owain-glyndwr", "harri-tudur", "william-morgan", "lloyd-george", "aneurin-bevan", "betty-campbell"]
DATA = dict(
    ERAS=D.ERAS, EVENTS=D.EVENTS, PLACES=[dict(p, ph=place_ph(p['id'])) for p in D.PLACES], PEOPLE=D.PEOPLE, READING=D.READING, ONLINE=D.ONLINE,
    CENSUS=D.CENSUS, KINGDOMS=D.KINGDOMS, LA=la, DICT=D.DICT, SAMPLES=D.SAMPLES, WORDS=D.WORDS,
    TRAILS=[dict(id=t["id"], en=t["en"], cy=t["cy"], ill=t["ill"], n=len(t["items"]), introEn=t["introEn"][0], introCy=t["introCy"][0]) for t in L.TRAILS],
    AUDIO=sorted(f[:-4] for f in os.listdir(os.path.join(SRC, 'static', 'audio')) if f.endswith('.mp3')) if os.path.isdir(os.path.join(SRC, 'static', 'audio')) else [],
    MAPC=dict(minx=geo["minx"], maxy=geo["maxy"], k=geo["k"], sc=geo["sc"]),
    SL={i: x["id"] for i, ev in enumerate(D.EVENTS) for x in story_links("events", ev[5])},
    KGLINK={"Gwynedd": "kings-gwynedd.html", "Powys": "kings-powys.html", "Ceredigion": "kings-ceredigion.html", "Dyfed": "kings-dyfed.html", "Brycheiniog": "kings-brycheiniog.html",
            "Rhwng Gwy a Hafren": "kings-gwy-a-hafren.html", "Glywysing": "kings-glywysing.html", "Morgannwg": "kings-glywysing.html", "Gwent": "kings-gwent.html", "Deheubarth": "kings-deheubarth.html",
            "Rhodri Mawr": "person-rhodri-mawr.html", "Hywel Dda": "person-hywel-dda.html", "Gruffudd ap Llywelyn": "kings.html", "Principality of Wales": "kings.html#princes",
            "Owain Glyndŵr, Prince of Wales": "person-owain-glyndwr.html"},
    FACTS=F.FACTS, FEATURED=FEATURED, PPH=dict({k: photo_url(v[0], 240) for k, v in PH.PERSON_PHOTOS.items()}, **{k[7:]: f'gallery/{k}-s.webp' for k in GP.GALLERY if k.startswith('person-')}),
    PFIELDS=P2.FIELDS, PFIELD=P2.FIELD, PFIRST={k: [v[0], v[1], v[2]] for k, v in P2.FIRSTS.items()},
)
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
AGES_HTML = "".join(
    f'<a class="poster" href="era-{x["id"]}.html" data-era="{x["id"]}">{A.scene(ERA_ART[x["id"]], COL[x["id"]])}<span class="shade"></span><span class="rn">{ROMAN[i]}</span>'
    f'<span class="txt"><span class="span">{bi(x["spanEn"], x["spanCy"])}</span><h3>{bi(x["en"], x["cy"])}</h3><p>{bi(x["blurbEn"], x["blurbCy"])}</p><span class="go">{bi("Read the chapter", "Darllen y bennod")} →</span></span></a>'
    for i, x in enumerate(D.ERAS))
MARQ = [("Castles", "Cestyll", "story-castles.html"), ("Poets", "Beirdd", "person-dafydd-ap-gwilym.html"), ("Saints", "Seintiau", "saints.html"),
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
            .replace("__NEWS__", news_strip()).replace("__LEGENDS__", "".join(legend_card(x) for x in F.LEGENDS_HOME)).replace("__PLAY__", play_cards()))


index_head = head.replace("</style>", extra_css + PRINT_CSS + EXTRA_PAGE_CSS + "\n</style>", 1)
_home_style = index_head[index_head.index("<style>") + 7: index_head.index("</style>")]
index_head = re.sub(r"<title>.*?</title>\n", "", index_head, count=1)
index_head = re.sub(r'<meta name="description"[^>]*>\n', "", index_head, count=1)
_bare_head = index_head
index_head = head_tags("History of Wales", "The history of Wales, from the first people in the caves to the Senedd: an interactive timeline, map, people, legends and games, in English and Cymraeg.", "", "website") + index_head
_body_filled = (body.replace("__WALES__", geo["outline"]).replace("__WELSHV__", str(WELSH_JS_VER))
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
    items.append(dict(k="page", t="The Mabinogion", c="Y Mabinogion", u="mabinogion.html", y=["Eleven tales", "Un chwedl ar ddeg"],
                      b=["The eleven great tales of medieval Wales, the White Book and the Red Book, and Lady Charlotte Guest.", "Un chwedl fawr ar ddeg Cymru’r Oesoedd Canol, y Llyfr Gwyn a’r Llyfr Coch, a’r Arglwyddes Charlotte Guest."], e="medieval"))
    items += [dict(k="page", t=t["cy"], c=t["cy"], u="mabinogion.html#mab-" + str(k + 1), y=[t["en"], g["cy"]], b=[t["sumEn"], t["sumCy"]], e=g["era"]) for k, g in enumerate(MB.GROUPS) for t in g["tales"] if not t["link"]]
    items += [dict(k="page", t=s[3], c=s[1], u=f"symbols.html#{s[0]}", y=["Symbol", "Symbol"], b=[s[4], s[5]], e="modern") for s in F.SYMBOLS]
    items += [dict(k="page", t=g[2], c=g[3], u=g[0], y=["Game", "Gêm"], b=[g[4], g[5]], e=g[8]) for g in GAMES]
    items.append(dict(k="page", t="Kings and princes of Wales", c="Brenhinoedd a thywysogion Cymru", u="kings.html", y=["Kings", "Brenhinoedd"], b=["Every king and prince of Wales, and Gruffudd ap Llywelyn, king of all Wales", "Pob brenin a thywysog yng Nghymru, a Gruffudd ap Llywelyn, brenin Cymru gyfan"], e="kings"))
    items += [dict(k="page", t=realm_title(r)[0], c=realm_title(r)[1], u=f"kings-{r['id']}.html", y=[r["span"], cy_dates(r["span"])], b=[r["subEn"] + " " + ", ".join(x["name"] for x in r["rulers"] if x["k"] == "r"), r["subCy"]], e=r["era"]) for r in RY.REALMS]
    items.append(dict(k="page", t="Royal family trees of Wales", c="Coed teulu brenhinol Cymru", u="family-trees.html", y=["Family trees", "Coed teulu"], b=["From Rhodri Mawr to Harri Tudur: the royal houses of Gwynedd, Deheubarth, Powys and Gwent, the Tudors, and the marriages that joined them. " + ", ".join(n["name"][0] for n in FT_IDS.values() if not n["gap"]), "O Rhodri Mawr i Harri Tudur: tai brenhinol Gwynedd, Deheubarth, Powys a Gwent, y Tuduriaid, a’r priodasau a’u hunodd."], e="kings"))
    items += [dict(k="page", t=t["en"], c=t["cy"], u=f"family-trees.html#tree-{t['id']}", y=["Family tree", "Coeden deulu"], b=[t["introEn"], t["introCy"]], e=t["era"]) for t in TR.TREES]
    items.append(dict(k="page", t="Learn Welsh", c="Dysgu Cymraeg", u="welsh.html", y=["Language", "Iaith"], b=["A Welsh word of the day and beginner’s phrases with sound guides", "Gair Cymraeg y dydd ac ymadroddion i ddechreuwyr gyda chanllawiau sain"], e="modern"))
    items.append(dict(k="page", t="Saints of Wales", c="Seintiau Cymru", u="saints.html", y=["Saints", "Seintiau"], b=["The saints of Wales region by region, the llannau named after them, a map and a saints’ calendar", "Seintiau Cymru fesul rhanbarth, y llannau a enwyd ar eu hôl, map a chalendr y saint"], e="saints"))
    items += [dict(k="page", t=("Saints of " + r["en"]) if r["realm"] else "Saints across the sea", c=("Seintiau " + r["cy"]) if r["realm"] else "Saint dros y môr", u=f"saints-{r['id']}.html", y=["Saints", "Seintiau"], b=[r["subEn"] + " " + ", ".join(x["en"] for x in r["saints"]), r["subCy"]], e=r["era"]) for r in SA.REGIONS]
    items += [dict(k="page", t=x["en"], c=x["cy"], u=saint_href(sid), y=[x["dates"], cy_dates(x["dates"])], b=[x["nEn"].split(". ")[0] + ". " + " ".join(x["places"]), x["nCy"].split(". ")[0] + "."], e=r["era"]) for sid, (x, r) in SAINT.items()]
    items.append(dict(k="page", t="On this day in Welsh history", c="Ar y dydd hwn yn hanes Cymru", u="onthisday.html", y=["Every day", "Bob dydd"], b=["What happened on each day of the year in Welsh history", "Beth ddigwyddodd ar bob diwrnod o’r flwyddyn yn hanes Cymru"], e="medieval"))
    items.append(dict(k="page", t="The castles of Wales: the map", c="Cestyll Cymru: y map", u="castles.html", y=["Map", "Map"], b=[f"All {len(CASTLES)} castle sites in Wales on one map, with who built them", f"Pob un o’r {len(CASTLES)} o safleoedd cestyll yng Nghymru ar un map, gyda phwy a’u cododd"], e="medieval"))
    items += [dict(k="place", t=r["en"], c=r["cy"], u=f'castles.html#castle-{r["q"]}', y=[r["d"], castle_date_cy(r["d"])], b=[r["cur"][1] + ". " + r["cur"][4], r["cur"][2] + ". " + r["cur"][5]], e="medieval") for r in castle_rows() if r["cur"]]
    items.append(dict(k="page", t="Welsh world firsts", c="Cymru oedd y cyntaf", u="firsts.html", y=["Firsts", "Y cyntaf"], b=["The equals sign, π, the fuel cell, the microphone, packet switching, mail order and more: everything Wales and the Welsh did first. " + ", ".join(PERSON[k][3] for k in P2.FIRSTS if k in PERSON), "Yr hafalnod, π, y gell danwydd, y meicroffon, newid pecynnau, archebu drwy’r post a rhagor: popeth a wnaeth Cymru a’r Cymry gyntaf."], e="industrial"))
    items.append(dict(k="page", t="For teachers", c="I athrawon", u="teachers.html", y=["", ""], b=["Lesson ideas and printable quizzes", "Syniadau gwersi a chwisiau i’w hargraffu"], e="industrial"))
    return items


# ---------- the castles of Wales map (src/castles.py, src/castles_data.json, src/static/castles.js) ----------
import castles as CS  # noqa: E402
CASTLES = json.loads(read("castles_data.json"))
_KIND_RE = [(re.compile(r"ringwork", re.I), "ring"), (re.compile(r"motte|mound|tomen|domen|mwnt|twmp|tump|mount\b", re.I), "motte"),
            (re.compile(r"moat", re.I), "moat"), (re.compile(r"tower|\btwr\b|tŵr", re.I), "tower")]


def castle_kind(c):
    if c["kind"]:
        return c["kind"]
    for rx, k in _KIND_RE:
        if rx.search(c["en"] + " " + c["cy"]):
            return k
    return ""


def castle_group(c, kind):
    if c["q"] in CS.C:
        return CS.C[c["q"]][0]
    if c["wp"]:
        return "welsh"
    if kind in ("house", "tower", "mansion", "moat"):
        return "later"
    return "other"


def _link_label(h):
    if h.startswith("person-"):
        p = PERSON.get(h[7:-5])
        return (p[3], p[4]) if p else None
    if h.startswith("place-"):
        p = PLACE.get(h[6:-5])
        return (p["en"], p["cy"]) if p else None
    if h.startswith("legend-"):
        x = next((x for x in F.LEGENDS if x["id"] == h[7:-5]), None)
        return (x["en"], x["cy"]) if x else None
    if h.startswith("story-"):
        x = next((x for x in F.STORIES if x["id"] == h[6:-5]), None)
        return (x["en"], x["cy"]) if x else None
    return None


def castle_date_cy(s):
    """A castle date such as 'late 12th–13th century' or '1093; keep c. 1200' in Welsh."""
    def part(t):
        t = t.strip()
        t = re.sub(r"(\d+)(?:st|nd|rd|th)", lambda m: CY_ORD.get(int(m.group(1)), m.group(1)), t)
        t = re.sub(r"\b(\d{3,4})s\b", r"\1au", t)
        t = t.replace("c. ", "tua ").replace("keep ", "gorthwr ").replace("(stone tower)", "(tŵr carreg)")
        if t.endswith(" century onwards"):
            return "o’r " + t[:-16] + " ganrif ymlaen"
        m = re.match(r"(early |late )?(.*?) century(.*)$", t)
        if m:
            lead = {"early ": "dechrau’r ", "late ": "diwedd y "}.get(m.group(1) or "", "y ")
            return lead + m.group(2) + " ganrif" + m.group(3)
        for en, cy in (("from ", "o "), ("by ", "erbyn "), ("after ", "wedi "), ("rebuilt ", "ailgodwyd yn y ")):
            if t.startswith(en):
                return cy + t[len(en):]
        return t
    return "; ".join(part(x) for x in s.split(";"))


def castle_rows():
    """Every castle, oldest-known story first within each group, with what the map needs."""
    gi = {g["id"]: i for i, g in enumerate(CS.GROUPS)}
    li = {n: i for i, n in enumerate(CS.LA_ORDER)}
    rows = []
    for c in CASTLES:
        kind = castle_kind(c)
        g = castle_group(c, kind)
        x = round((c["lon"] - geo["minx"]) * geo["k"] * geo["sc"], 1)
        y = round((geo["maxy"] - c["lat"]) * geo["sc"], 1)
        cur = CS.C.get(c["q"])
        rows.append(dict(q=c["q"], en=c["en"], cy=c["cy"], lat=c["lat"], lon=c["lon"], x=x, y=y, g=g, gi=gi[g], kind=kind, la=c["la"], li=li[c["la"]],
                         d=(cur[3] if cur else (c["y"] if c["y"][:1] == "1" else "")), cur=cur, ph=CS.PHOTOS.get(c["q"])))
    return rows


def castle_photo(ph, w=900):
    f, who, lic = ph
    credit_en = "Photo: " + (f"{who}, {lic}, " if who else "") + "Wikimedia Commons"
    credit_cy = "Llun: " + (f"{who}, {lic}, " if who else "") + "Wikimedia Commons"
    return photo_url(f, w), f"{COMMONS}File:{_q(f, safe='')}", credit_en, credit_cy


def county_lines():
    """The old county borders from map.json as joined-up lines, rounded, so they weigh a third as much."""
    segs = re.findall(r"M\s*(-?[\d.]+)[ ,](-?[\d.]+)\s*L\s*(-?[\d.]+)[ ,](-?[\d.]+)", geo["counties"])
    out, end = [], None
    for x1, y1, x2, y2 in segs:
        a, b = (round(float(x1)), round(float(y1))), (round(float(x2)), round(float(y2)))
        if a == b:
            continue
        if a != end:
            out.append(f"M{a[0]} {a[1]}")
        out.append(f"L{b[0]} {b[1]}")
        end = b
    return "".join(out)


def castles_page():
    rows = castle_rows()
    by_q = {r["q"]: r for r in rows}
    # place pages that stand at a castle
    for r in rows:
        r["place"] = next((p["id"] for p in D.PLACES if abs(p["lat"] - r["lat"]) < .006 and abs(p["lon"] - r["lon"]) < .009), None)
    data_rows = [[r["q"], r["en"], r["cy"], r["x"], r["y"], r["gi"], r["kind"], r["d"], r["li"], r["lat"], r["lon"], 1 if r["cur"] else 0] for r in rows]
    det = {}
    for r in rows:
        cur, ph = r["cur"], r["ph"]
        if not (cur or ph or r["place"]):
            continue
        dd = {}
        if cur:
            dd.update(b=cur[1], bc=cur[2], n=cur[4], nc=cur[5])
            links = list(cur[6])
        else:
            links = []
        if r["place"] and f'place-{r["place"]}.html' not in links:
            links.insert(0, f'place-{r["place"]}.html')
        ls = [[h, *_link_label(h)] for h in links if _link_label(h)]
        if ls:
            dd["l"] = ls
        if ph:
            dd["ph"] = list(castle_photo(ph))
        det[r["q"]] = dd
    kinds = {k: [v[0], v[1], v[2], v[3]] for k, v in CS.KINDS.items()}
    payload = dict(c=data_rows, d=det, k=kinds, g=[[g["en"], g["cy"], g["col"]] for g in CS.GROUPS],
                   la=[[n, CS.LA_CY[n]] for n in CS.LA_ORDER], counties=county_lines(), W=geo["W"], H=geo["H"],
                   P=[geo["minx"], geo["maxy"], geo["k"], geo["sc"]],
                   dc={r["d"]: castle_date_cy(r["d"]) for r in rows if r["d"] and castle_date_cy(r["d"]) != r["d"]})
    n_all = len(rows)
    counts = {g["id"]: sum(1 for r in rows if r["g"] == g["id"]) for g in CS.GROUPS}

    chips = "".join(f'<button type="button" class="cm-chip on" data-g="{i}" aria-pressed="true" style="--gc:{g["col"]}"><i></i>{bi(g["en"], g["cy"])} <b>{counts[g["id"]]}</b></button>'
                    for i, g in enumerate(CS.GROUPS))
    gcss = "".join(f".g{i}{{--gc:{g['col']}}}" for i, g in enumerate(CS.GROUPS))
    legend = "".join(f'<li style="--gc:{g["col"]}"><i></i><span>{bi(g["en"], g["cy"])}</span><small>{bi(g["sumEn"], g["sumCy"])}</small></li>' for g in CS.GROUPS)
    tool = (f'<div class="cm-tools">'
            f'<div class="cm-search"><label class="sr-only" for="cm-q">{bi("Find a castle", "Chwilio am gastell")}</label>'
            f'<input id="cm-q" type="search" autocomplete="off" placeholder="Find a castle…" data-ph-cy="Chwilio am gastell…" data-ph-en="Find a castle…">'
            f'<ul id="cm-res" class="cm-res" role="listbox" hidden></ul></div>'
            f'<div class="cm-btns"><button type="button" class="btn" id="cm-near">{bi("Castles near me", "Cestyll yn agos ataf")}</button>'
            f'<button type="button" class="btn ghost" id="cm-rand">{bi("Surprise me", "Synnwch fi")}</button></div>'
            f'<div class="cm-chips" role="group" aria-label="Who built them / Pwy a’u cododd">{chips}</div></div>')
    mapbox = (f'<div class="cm-wrap">{tool}<div class="cm-map" id="cm-map" tabindex="0" aria-label="Map of the castles of Wales / Map o gestyll Cymru">'
              f'<noscript><p>{bi("The map needs JavaScript. Every castle is listed below.", "Mae angen JavaScript ar y map. Rhestrir pob castell isod.")}</p></noscript>'
              f'<div class="cm-zoom"><button type="button" id="cm-in" aria-label="Zoom in / Chwyddo i mewn">+</button><button type="button" id="cm-out" aria-label="Zoom out / Chwyddo allan">−</button>'
              f'<button type="button" id="cm-home" aria-label="Whole of Wales / Cymru gyfan"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5" fill="none" stroke="currentColor" stroke-width="2"/></svg></button></div>'
              f'<p class="cm-hint" id="cm-hint">{bi("Drag to move, pinch or scroll to zoom, tap a castle", "Llusgwch i symud, pinsiwch neu sgroliwch i chwyddo, tapiwch gastell")}</p></div>'
              f'<aside class="cm-side"><div id="cm-card" class="cm-card" aria-live="polite">'
              f'<p class="eyebrow">{bi(f"{n_all} castle sites", f"{n_all} o safleoedd cestyll")}</p>'
              f'<h2>{bi("Choose a castle", "Dewiswch gastell")}</h2><p class="muted">{bi("Tap any dot on the map, search by name, or find the castles nearest to you. The red dots are castles built by the Welsh.", "Tapiwch unrhyw ddot ar y map, chwiliwch yn ôl enw, neu dewch o hyd i’r cestyll agosaf atoch. Cestyll a godwyd gan y Cymry yw’r dotiau coch.")}</p>'
              f'<ul class="cm-legend">{legend}</ul></div></aside></div>')

    def fcard(q):
        r = by_q[q]
        cur = r["cur"]
        img = ""
        if r["ph"]:
            u, fu, ce, cc = castle_photo(r["ph"], 800)
            img = (f'<img src="{u}" alt="{e(r["en"])}" loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.remove()">')
        return (f'<article class="cm-feat rv">{img}<div class="cm-feat-t"><p class="eyebrow">{bi(cur[3], castle_date_cy(cur[3]))}</p><h3>{bi(r["en"], r["cy"])}</h3>'
                f'<p class="cm-by">{bi(cur[1], cur[2])}</p><p>{bi(cur[4], cur[5])}</p>'
                f'<button type="button" class="go cm-show" data-q="{q}">{bi("Show on the map", "Dangos ar y map")} →</button></div></article>')
    feat = "".join(fcard(q) for q in CS.FEATURED)

    lists = ""
    for i, la in enumerate(CS.LA_ORDER):
        rs = sorted([r for r in rows if r["la"] == la], key=lambda r: (-(r["cur"] is not None), r["en"]))
        if not rs:
            continue
        items = "".join(f'<li><button class="cm-show g{r["gi"]}" data-q="{r["q"]}"><i></i>{bi(r["en"], r["cy"])}</button></li>' for r in rs)
        lists += f'<details class="cm-la"><summary>{bi(la, CS.LA_CY[la])} <b>{len(rs)}</b></summary><ul>{items}</ul></details>'

    intro_en = ["Wales is often called the castle capital of the world. More than six hundred castles were raised here in the Middle Ages, more for its size than in any other country in Europe.",
                "Some were built to conquer Wales. Many were built by the Welsh to defend it: the princes of Gwynedd, Powys and Deheubarth raised stone castles in their own style, with D-shaped and round towers, on crags that guard the passes into their lands.",
                "This map shows every castle site we could find in the records, from the great fortresses of Edward I to grassy mounds in a field. Tap a dot to see who built it."]
    intro_cy = ["Gelwir Cymru’n aml yn brifddinas cestyll y byd. Codwyd mwy na chwe chant o gestyll yma yn yr Oesoedd Canol, mwy am ei maint nag mewn unrhyw wlad arall yn Ewrop.",
                "Codwyd rhai i goncro Cymru. Codwyd llawer gan y Cymry i’w hamddiffyn: cododd tywysogion Gwynedd, Powys a Deheubarth gestyll carreg yn eu dull eu hunain, gyda thyrau siâp D a thyrau crwn, ar greigiau sy’n gwarchod y bylchau i mewn i’w tiroedd.",
                "Mae’r map hwn yn dangos pob safle castell y gallem ei ganfod yn y cofnodion, o gaerau mawr Edward I i dwmpathau glaswelltog mewn cae. Tapiwch ddot i weld pwy a’i cododd."]
    note = bi("Castle sites come from Wikidata, which draws on the Cadw and Coflein records of Wales (free CC0 data). Builders and stories are written for this site. Some early dates are approximate. Photographs are from Wikimedia Commons; each is credited beside it. Relief from open elevation data (Mapzen Terrarium).",
              "Daw’r safleoedd cestyll o Wikidata, sy’n tynnu ar gofnodion Cadw a Coflein (data rhydd CC0). Ysgrifennwyd yr adeiladwyr a’r straeon ar gyfer y wefan hon. Mae rhai dyddiadau cynnar yn fras. Daw’r ffotograffau o Wikimedia Commons; mae cydnabyddiaeth wrth bob un. Tirwedd o ddata uchder agored (Mapzen Terrarium).")
    main = (hero("medieval", f'<a href="index.html">{SITE}</a>', "castle", f"{n_all} castle sites", f"{n_all} o safleoedd cestyll", "The castles of Wales", "Cestyll Cymru",
                 "Every castle in Wales on one map: who built it, when, and the story it tells. The castles of the Welsh princes are in red.",
                 "Pob castell yng Nghymru ar un map: pwy a’i cododd, pryd, a’r stori sydd ganddo. Mae cestyll tywysogion Cymru mewn coch.", art="castle")
            + f'<style>{read("castles.css")}{gcss}</style><section class="cm-sec" id="map"><div class="wrap">{mapbox}</div></section>'
            + section(paras(intro_en, intro_cy), top=True)
            + section(f'<p class="lede">{bi("From Dolwyddelan to Dinas Brân, the princes of Wales built in stone to guard their lands. These are the castles they left.", "O Ddolwyddelan i Ddinas Brân, cododd tywysogion Cymru mewn carreg i warchod eu tiroedd. Dyma’r cestyll a adawsant.")}</p><div class="cm-feats">{feat}</div>',
                      "Castles of the Welsh princes", "Cestyll tywysogion Cymru")
            + section(f'<p class="lede">{bi("Every castle site on the map, area by area.", "Pob safle castell ar y map, fesul ardal.")}</p><div class="cm-lists">{lists}</div><p class="note-box" style="margin-top:2rem">{note}</p>',
                      "Every castle, by county", "Pob castell, fesul sir")
            + section(f'<div class="pager"><a class="btn" href="kings.html">← {bi("Kings and princes", "Brenhinoedd a thywysogion")}</a><a class="btn solid" href="map-game.html">{bi("Play: Where in Wales?", "Chwarae: Ble yng Nghymru?")} →</a></div>'))
    extra = (f'<script>var CASTLES={json.dumps(payload, ensure_ascii=False, separators=(",", ":"))};</script>\n<script src="castles.js?v=2" defer></script>\n')
    ld = {"@context": "https://schema.org", "@type": "Map", "name": "The castles of Wales", "inLanguage": ["en", "cy"], "description": f"An interactive map of {n_all} castle sites in Wales, with who built them.",
          "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page("castles.html", "The castles of Wales: interactive map · History of Wales",
                f"An interactive map of {n_all} castles in Wales, from Caernarfon and Harlech to the castles of the Welsh princes: Dolwyddelan, Castell y Bere, Dinas Brân. Who built each one, and its story.",
                main, era="medieval", ld=ld, og_type="website", active="castles.html", track="castles", extra=extra)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


# ---------- shared files: the stylesheet and the home page's data and script are kept in files of their own ----------
# Every page used to carry about 100 KB of the same CSS, and the home page, timeline and quiz each carried 430 KB of the
# same data and script. Now the browser downloads them once and keeps them, so every page after the first opens faster.
# The ?v= number is a fingerprint of the contents: it changes whenever they change, so nobody is left with an old copy.
def _fp(text):
    import hashlib
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:10]


def shared_assets(pages):
    files = {}
    css = style + PRINT_CSS
    css_tag = f'<link rel="stylesheet" href="site.css?v={_fp(css)}">\n'
    files["site.css"] = css
    data_re = re.compile(r'<script>var DATA = (.*?);</script>\n<script>var TOWNS = (.*?);</script>\n<script>(.*?)</script>', re.S)
    data_js = app_js = None
    for name, text in list(pages.items()):
        home_css = "<style>" + _home_style + "</style>"
        if home_css in text:  # the home page, timeline and quiz: the same rules in another order, all inside site.css
            text = text.replace(home_css, css_tag.strip(), 1)
        if "<style>" + css in text:
            text = text.replace("<style>" + css, css_tag + "<style>", 1).replace("<style>\n</style>", "").replace("<style></style>", "")
        m = data_re.search(text)
        if m:
            if data_js is None:
                data_js = f"var DATA = {m.group(1)};\nvar TOWNS = {m.group(2)};\n"
                app_js = m.group(3)
            if data_js == f"var DATA = {m.group(1)};\nvar TOWNS = {m.group(2)};\n" and app_js == m.group(3):
                text = text[:m.start()] + f'<script src="data.js?v={_fp(data_js)}"></script>\n<script src="app.js?v={_fp(app_js)}"></script>' + text[m.end():]
        pages[name] = text
    if data_js is not None:
        files["data.js"] = data_js
        files["app.js"] = app_js
    return files


# ---------- the page for addresses that do not exist ----------
def not_found_page():
    base = re.sub(r"^https?://[^/]+", "", BASE_URL) or "/"
    links = [("timeline.html", "The timeline", "Y llinell amser"), ("index.html#people", "The people", "Y bobl"), ("index.html#map", "The map", "Y map"),
             ("stories.html", "Long reads", "Erthyglau"), ("legends.html", "Legends", "Chwedlau"), ("daily.html", "Today’s challenge", "Her heddiw")]
    main = (hero("medieval", f'<a href="index.html">{SITE}</a>', "book", "Page not found", "Heb ddod o hyd i’r dudalen", "This page has wandered off", "Mae’r dudalen hon wedi crwydro",
                 "Like the lost land of Cantre’r Gwaelod, it may be under the sea. The rest of Welsh history is still here.",
                 "Fel Cantre’r Gwaelod, efallai ei bod o dan y môr. Mae gweddill hanes Cymru yma o hyd.", art="ship")
            + section('<p class="lede" style="margin-bottom:1.2rem">' + bi("Try a search, or start from one of these:", "Rhowch gynnig ar chwilio, neu dechreuwch o un o’r rhain:") + '</p>'
                      + '<p style="display:flex;flex-wrap:wrap;gap:.6rem"><button type="button" class="btn solid" data-search>' + bi("Search the site", "Chwilio’r wefan") + "</button>"
                      + "".join(f'<a class="btn" href="{h}">{bi(a, b)}</a>' for h, a, b in links) + "</p>", top=True))
    doc = page("404.html", "Page not found · History of Wales", "This page could not be found. Search the history of Wales, or start from the timeline, the people or the map.", main, era="medieval", og_type="website")
    return doc.replace("<head>\n", f'<head>\n<base href="{base}">\n<meta name="robots" content="noindex">\n', 1)


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
    pages["legends.html"] = legends_index()
    pages["mabinogion.html"] = mabinogion_page()
    for i, x in enumerate(F.LEGENDS):
        pages[f"legend-{x['id']}.html"] = legend_page(x, i)
    pages["kings.html"] = kings_page()
    pages["castles.html"] = castles_page()
    for i, r in enumerate(RY.REALMS):
        pages[f"kings-{r['id']}.html"] = realm_page(r, i)
    pages["family-trees.html"] = family_trees_page()
    pages["saints.html"] = saints_page()
    pages["firsts.html"] = firsts_page()
    for i, r in enumerate(SA.REGIONS):
        pages[f"saints-{r['id']}.html"] = saints_region_page(r, i)
    pages["symbols.html"] = symbols_page()
    pages["gallery.html"] = gallery_page()
    pages["play.html"] = play_index()
    pages["journey.html"] = journey_page()
    pages["onthisday.html"] = onthisday_page()
    pages["daily.html"] = game_page("daily.html", "daily", "medieval", "Daily challenge", "Her y dydd", "One event from Welsh history. Six guesses to find the year.", "Un digwyddiad o hanes Cymru. Chwe chynnig i ddyfalu’r flwyddyn.", "castle", "A daily history challenge: guess the year of an event from Welsh history in six tries.")
    pages["map-game.html"] = game_page("map-game.html", "map", "modern", "Where in Wales?", "Ble yng Nghymru?", "Tap the map where you think each place is. Five rounds, 100 points each.", "Tapiwch y map lle credwch fod pob lle. Pum rownd, 100 pwynt yr un.", "senedd", "A map game: place the castles, towns and historic sites of Wales on a blank map.", with_map=True)
    pages["names.html"] = game_page("names.html", "names", "saints", "Welsh names", "Enwau Cymraeg", "Jones, Powell, Lloyd, Vaughan: Welsh surnames are history in miniature. Look yours up, then find your name as the princes would have said it.", "Jones, Powell, Lloyd, Vaughan: mae cyfenwau Cymru’n hanes ar raddfa fach. Chwiliwch am eich un chi, yna gweld eich enw fel y byddai’r tywysogion wedi’i ddweud.", "cross", "What Welsh surnames mean and where they come from, and a patronymic name maker.")
    pages["hero.html"] = game_page("hero.html", "hero", "ancient", "Which figure from history are you?", "Pa ffigwr o hanes ydych chi?", "Six quick questions.", "Chwe chwestiwn cyflym.", "torch", "A short personality quiz: which figure from Welsh history are you most like?")
    pages["welsh.html"] = welsh_page()
    pages["pairs.html"] = game_page("pairs.html", "pairs", "modern", "Word pairs", "Parau geiriau", "Turn over two cards at a time and match each Welsh word to its meaning.", "Trowch ddau gerdyn ar y tro a pharu pob gair Cymraeg â’i ystyr.", "owl", "A memory game: match Welsh words to their meanings.")
    pages["404.html"] = not_found_page()
    pages["whatsnew.html"] = whatsnew_page()
    shared_files = shared_assets(pages)
    for name, text in pages.items():
        write(os.path.join(out, name), text)
    for name, text in shared_files.items():
        write(os.path.join(out, name), text)
    for f in os.listdir(os.path.join(SRC, "static")):
        sp = os.path.join(SRC, "static", f)
        (shutil.copytree if os.path.isdir(sp) else shutil.copy)(sp, os.path.join(out, f))
    write(os.path.join(out, "welsh.js"), welsh_js())
    write(os.path.join(out, "onthisday.json"), json.dumps(otd_rows(), ensure_ascii=False, separators=(",", ":")))
    write(os.path.join(out, "feed.xml"), feed_xml(otd_rows()))
    write(os.path.join(out, "whatsnew.json"), json.dumps(WN.NEWS, ensure_ascii=False))
    write(os.path.join(out, "search.json"), json.dumps(search_index(), ensure_ascii=False, separators=(",", ":")))
    write(os.path.join(out, ".nojekyll"), "")
    write(os.path.join(out, "robots.txt"), f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}sitemap.xml\n")
    write(os.path.join(out, "sitemap.xml"), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{xesc(BASE_URL + ('' if p == 'index.html' else p))}</loc></url>\n" for p in pages if p != "404.html") + "</urlset>\n")
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
        shutil.copy(os.path.join(out, "welsh.js"), os.path.join(a, "welsh.js"))
        shutil.copy(os.path.join(out, "onthisday.json"), os.path.join(a, "onthisday.json"))
    print(f"Built {len(pages)} pages -> {out}")


if __name__ == "__main__":
    main()
