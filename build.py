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
import eventpages as EP  # noqa: E402
import welshpages as WP  # noqa: E402
import cites as CITE  # noqa: E402  (sources beside the claims: [[cite:...]] markers, src/cites.py)
import llys as LLYS  # noqa: E402  (Llys Rhosyr in 3D: llys-rhosyr.html, src/llys.py, tools/llys3d.src.js -> src/static/llys3d.js)
import ride as RIDE  # noqa: E402  (Ride with Glyndŵr, 1400: ride-glyndwr.html, src/ride.py, src/static/ride.js)
import teachpacks as TPK  # noqa: E402  (teacher packs: pack-<age>.html, src/teachpacks.py)  (every page also in Welsh at cy/<page>.html: src/welshpages.py)  (a page for every timeline event: src/eventpages.py)
import gallery as G  # noqa: E402
import gallery_photos as GP  # noqa: E402
import ages as AG  # noqa: E402
import features as F  # noqa: E402
import art as A  # noqa: E402
import places3 as PL3  # noqa: E402  (historic places of importance: their people and links, src/places3.py)
import visit as VS  # noqa: E402  (the Visiting box on place pages and the map card, src/visit.py)
import pictures as PX  # noqa: E402  (a real picture at the top of every page and on its card: src/pictures.py)
PX.check()
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
import literature as LT  # noqa: E402  (literature.html, books.html, triads.html)
import laws as LW  # noqa: E402  (the Laws of Hywel Dda page, laws.html)
import people2 as P2  # noqa: E402
import princes as PRN  # noqa: E402  (the kings and princes of Wales: the block on each of their pages)
import arthur_circle as AC  # noqa: E402  (Arthur's circle: the block on every page of the people of Arthur's story)
import mabinogi_tales as MT  # noqa: E402  (a guide page for each tale of the Mabinogion, mabinogi-<id>.html)
import mabinogi_people as MP  # noqa: E402  (the people of the Mabinogi: the block on each of their pages)
import sets as SETS  # noqa: E402
import seo as SEO  # noqa: E402  (search engine extras for every page)
import added as AD  # noqa: E402  (when each item was added: newest first, "Just added" strips, "New" badges)
import refs as REF  # noqa: E402  (further reading and references for every long read)
import refs2 as REF2  # noqa: E402  (the same for every other content page)
import christianity as _CHR  # noqa: E402
REF.REFS.update(_CHR.REFS)  # reading lists for the four long reads on the coming of Christianity
import patrick as _PTR  # noqa: E402
REF.REFS.update(_PTR.REFS)  # reading list for the Saint Patrick long read
import mac as _MACR  # noqa: E402
REF.REFS.update(_MACR.REFS)  # reading lists for the MAC and Free Wales Army long reads
import writers as WRT  # noqa: E402  (the writers who recorded early Wales: their block, long read and reading list)
REF.REFS.update(WRT.REFS)
import bruts as BRT  # noqa: E402  (the Bruts, the chronicles of Wales: long read and reading list)
REF.REFS.update(BRT.REFS)
import oldbooks as OB  # noqa: E402  (the old books of Wales: a page for every book, book-<id>.html)
REF2.PAGES.update(OB.REFS)
import authors as AU  # noqa: E402  (the authors on the Books and authors page)
import ylolfa as YLF  # noqa: E402  (Y Lolfa books: the "Y Lolfa" section of the Books and authors page)
F.STORIES = AD.newest("story", F.STORIES)  # long reads: the newest first everywhere (index, home page, "Keep reading")
L.TEACH.update(AG9.TEACH)
from urllib.parse import quote as _q

BASE_URL = os.environ.get("SITE_URL", "https://tywysog85.github.io/historyofwales/")
GOATCOUNTER = os.environ.get("GOATCOUNTER", "").strip()
# The weekly email sign-up: the link to the sign-up form made at brevo.com (see SKILLS.md, "The weekly email"). Once it is
# set, a sign-up box appears on the home page, the What's new page and the foot of every page. Empty: the box is not shown.
EMAIL_FORM = os.environ.get("EMAIL_FORM", "").strip() or ""
# Share pictures (tools/cards.py): one per page, made when Pillow is installed (the GitHub build installs it). CARDS=0 skips them.
try:
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import cards as CARDS  # noqa: E402
    CARDS_ON = os.environ.get("CARDS", "1") != "0"
except ImportError:
    CARDS_ON = False
CARD_JOBS = {}
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
    The real old borders, along the Wye and the hills, come from src/geo/shires.json (made by tools/split_shires.py).
    Without that file, straight lines of latitude and longitude are used."""
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

    shires = os.path.join(SRC, "geo", "shires.json")
    if os.path.exists(shires):   # the real old borders, along the Wye and the hills (made by tools/split_shires.py)
        la.pop("Powys"), la.pop("Gwynedd")
        la.update(json.load(open(shires, encoding="utf-8")))
        return
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


# ---------- read further: the Dictionary of Welsh Biography, Coflein and Welsh Wikipedia (tools/fetch_sources.py) ----------
SOURCE_LINKS = json.loads(read("source_links.json")) if os.path.exists(os.path.join(SRC, "source_links.json")) else {}


def _two(href_en, href_cy, en, cy):
    """One link in English and one in Welsh (each shown in its own language)."""
    if href_en == href_cy and en == cy:
        return f'<a href="{e(href_en)}" target="_blank" rel="noopener">{e(en)} ↗</a>'
    return (f'<a class="l-en" lang="en" href="{e(href_en)}" target="_blank" rel="noopener">{e(en)} ↗</a>'
            f'<a class="l-cy" lang="cy" href="{e(href_cy)}" target="_blank" rel="noopener">{e(cy)} ↗</a>')


# The sources tools/fetch_sources.py finds for a person, place or event, in the order they are shown (Wikipedia comes last).
# key: (English name, Welsh name, how to make the Welsh-language address, or None to use the same one)
SOURCES = {
    "dwb": ("Dictionary of Welsh Biography", "Y Bywgraffiadur Cymreig", lambda u: u.replace("://biography.wales/", "://bywgraffiadur.cymru/")),
    "odnb": ("Oxford Dictionary of National Biography", "Oxford Dictionary of National Biography (Saesneg)", None),
    "histparl": ("The History of Parliament", "The History of Parliament (Saesneg)", None),
    "ukparl": ("UK Parliament", "Senedd y DU (Saesneg)", None),
    "coflein": ("Coflein: the national record of this site", "Coflein: cofnod cenedlaethol y safle hwn", None),
    "cadwm": ("Cadw: scheduled monument record", "Cadw: cofnod yr heneb gofrestredig", None),
    "cadwb": ("Cadw: listed building record", "Cadw: cofnod yr adeilad rhestredig", None),
    "artuk": ("Art UK: their paintings", "Art UK: eu paentiadau (Saesneg)", None),
    "olympedia": ("Olympedia", "Olympedia (Saesneg)", None),
    "athletics": ("World Athletics", "World Athletics (Saesneg)", None),
    "britannica": ("Encyclopaedia Britannica", "Encyclopaedia Britannica (Saesneg)", None),
}


def further(key, wiki):
    rec = SOURCE_LINKS.get(key, {})
    links = []
    for k, (en, cy, to_cy) in SOURCES.items():
        if rec.get(k):
            u = rec[k]
            links.append(_two(u, to_cy(u) if to_cy else u, en, cy))
    if wiki:
        cyw = f'https://cy.wikipedia.org/wiki/{_q(rec["cy"].replace(" ", "_"), safe="")}' if rec.get("cy") else WIKI + wiki
        links.append(_two(WIKI + wiki, cyw, "Wikipedia", "Wicipedia" if rec.get("cy") else "Wikipedia (Saesneg)"))
    if not links:
        return ""
    return f'<div class="further no-print"><p class="eyebrow">{bi("Sources and further reading", "Ffynonellau a darllen pellach")}</p><p>{"".join(links)}</p></div>'


# ---------- shared head tags ----------
def head_tags(title, desc, path, og_type="website", image=None):
    url = BASE_URL + path
    title, desc = SEO.tidy_title(SEO.title_for(path, title)), SEO.tidy_desc(desc)
    t = (f'<title>{e(title)}</title>\n<meta name="description" content="{e(desc)}">\n<link rel="canonical" href="{url}">\n'
         '<meta name="theme-color" content="#0e1118">\n<link rel="icon" href="favicon.svg" type="image/svg+xml">\n'
         '<link rel="apple-touch-icon" href="apple-touch-icon.png">\n<link rel="manifest" href="manifest.webmanifest">\n'
         f'<meta property="og:title" content="{e(title)}">\n<meta property="og:description" content="{e(desc)}">\n'
         f'<meta property="og:type" content="{og_type}">\n<meta property="og:url" content="{url}">\n<meta property="og:site_name" content="History of Wales">\n'
         f'<meta property="og:image" content="{BASE_URL}{image or "og.png"}">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta property="og:image:alt" content="{e(title)}">\n'
         '<meta property="og:locale" content="en_GB">\n<meta property="og:locale:alternate" content="cy_GB">\n'
         '<meta name="twitter:card" content="summary_large_image">\n'
         f'<link rel="alternate" type="application/atom+xml" title="History of Wales: what’s new and on this day" href="{BASE_URL}feed.xml">\n')
    return t


def _static_fp(name):
    """A fingerprint of a file in src/static, for its ?v= number: it changes whenever the file does, so a browser that
    kept the old copy fetches the new one at once (a fixed number left people seeing old text for up to ten minutes)."""
    import hashlib
    with open(os.path.join(SRC, "static", name), "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()[:10]


TAIL_JS = (f'<script src="site.js?v={_static_fp("site.js")}" defer></script>\n<script src="search.js?v={_static_fp("search.js")}" defer></script>\n'
           '<script>if("serviceWorker" in navigator&&location.protocol==="https:"){addEventListener("load",function(){navigator.serviceWorker.register("sw.js").catch(function(){})})}</script>\n'
           + (f'<script data-goatcounter="https://{GOATCOUNTER}.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>\n' if GOATCOUNTER else ""))

LANG_BOOT = '<script>(function(){var h=document.documentElement;h.classList.add("js");setTimeout(function(){if(!window.__site)h.classList.add("rv-all")},2500);try{if(localStorage.getItem("hc-lang")==="cy"){h.classList.add("cy");h.lang="cy"}}catch(e){}})()</script>'
# LANG_TOGGLE swaps the words in place. Only pages without a Welsh twin keep it (the 404 page); welshpages.split() swaps it
# for links to the other language's address. The choice is saved only when a reader presses a button, never just by visiting.
LANG_TOGGLE = '''<script>(function(){var d=document.documentElement;function s(l,k){d.classList.toggle("cy",l==="cy");d.lang=l;document.getElementById("lang-en").setAttribute("aria-pressed",l==="en");document.getElementById("lang-cy").setAttribute("aria-pressed",l==="cy");if(k)try{localStorage.setItem("hc-lang",l)}catch(e){}}
s(d.classList.contains("cy")?"cy":"en");document.getElementById("lang-en").onclick=function(){s("en",1)};document.getElementById("lang-cy").onclick=function(){s("cy",1)}})()</script>'''
LANG_JS = LANG_TOGGLE + '''
<script>(function(){var d=document.documentElement;
document.addEventListener("click",function(ev){var p=ev.target.closest("[data-print]");if(p){window.print();return}var b=ev.target.closest("[data-copy]");if(!b)return;var u=new URL(b.dataset.copy,location.href).href,o=b.innerHTML;try{navigator.clipboard.writeText(u).then(function(){b.textContent=d.classList.contains("cy")?"Wedi copïo":"Copied";setTimeout(function(){b.innerHTML=o},1600)})}catch(e){}});})();</script>'''

PRINT_CSS = """
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap }
.skip { position: absolute; left: -9999px; top: 0; z-index: 50; background: var(--ink); color: var(--night); padding: .6rem 1rem; border-radius: 0 0 8px 0 }
.skip:focus { left: 0 }
@media print {
  :root { --night: #fff; --slate: #fff; --slate-2: #f2f2f2; --ink: #111; --muted: #444; --line: #bbb; color-scheme: light }
  body { background: #fff; color: #111; font-size: 11pt }
  .nav, footer, .no-print, .pager, .era-hero svg.ill, .toast { display: none !important }
  section { padding-block: 12pt !important; break-inside: avoid-page }
  .sheet-print { break-before: page }
  a { color: #111; text-decoration: none }
}
"""


NAV_MAIN = [("timeline.html", "Timeline", "Llinell amser"), ("index.html#chapters", "Ages", "Oesoedd"), ("map.html", "Map", "Map"),
            ("people.html", "People", "Pobl"), ("stories.html", "Long reads", "Erthyglau"), ("legends.html", "Legends", "Chwedlau"), ("play.html", "Play", "Chwarae"),
            ("welsh.html", "Cymraeg", "Cymraeg")]
# the row of links in the top bar on wide screens; the rest of the site is in the Menu, in groups
NAV_TOP = NAV_MAIN  # Ifan wants the same links along the top bar as in the big Menu list
# the Menu's side panel: (heading EN, heading CY, links)
NAV_GROUPS = [
    # the nine ages, each with its dates, so a newcomer can tell the Age of Kings from the Age of Princes (Ifan, 2026-11-12)
    ("The nine ages", "Y naw oes", [(f'era-{x["id"]}.html', x["en"], x["cy"], x["spanEn"], x["spanCy"]) for x in D.ERAS]),
    ("Explore", "Archwilio", [("reference.html", "Look it up", "Chwilio’r hanes"), ("kings.html", "Kings and princes", "Brenhinoedd a thywysogion"), ("family-trees.html", "Royal family trees", "Coed teulu brenhinol"),
                              ("castles.html", "Castles map", "Map y cestyll"), ("saints.html", "Saints of Wales", "Seintiau Cymru"), ("firsts.html", "Welsh world firsts", "Cymru oedd y cyntaf"),
                              ("trails.html", "Themed trails", "Llwybrau thema"), ("gallery.html", "Photo gallery", "Oriel luniau"), ("onthisday.html", "On this day", "Ar y dydd hwn")]),
    ("Read", "Darllen", [("wales-in-10.html", "Wales in 10 minutes", "Cymru mewn 10 munud"), ("laws.html", "The Laws of Hywel Dda", "Cyfreithiau Hywel Dda"), ("mabinogion.html", "The Mabinogion", "Y Mabinogion"),
                         ("literature.html", "Literature and old books", "Llên a hen lyfrau"), ("triads.html", "The Welsh Triads", "Trioedd Ynys Prydain"), ("symbols.html", "Symbols and traditions", "Symbolau a thraddodiadau"),
                         ("books-and-authors.html", "Books and authors", "Llyfrau ac awduron"), ("whatsnew.html", "What’s new", "Beth sy’n newydd")]),
    ("Cymraeg", "Cymraeg", [("index.html#language", "The Welsh language", "Yr iaith Gymraeg"), ("welsh.html", "Learn Welsh", "Dysgu Cymraeg")]),
    ("You", "Chi", [("journey.html", "Your journey", "Eich taith"), ("teachers.html", "For teachers", "I athrawon"), ("index.html#sources", "Sources", "Ffynonellau"), ("about.html", "About this site", "Am y wefan hon")]),
]
NAV_MORE = [x[:3] for g in NAV_GROUPS for x in g[2]]  # the same links as one flat list
SEARCH_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.5 15.5 21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'


# ---------- what's new, the email sign-up and the news feed (src/whatsnew.py) ----------
def _news_date(d, cy=False):
    y, m, dd = (int(x) for x in d.split("-"))
    if cy:
        return f"{dd} {MONTHS_CY[m - 1]} {y}"
    return f"{dd} {datetime.date(y, m, dd).strftime('%B')} {y}"


MONTHS_CY = ["Ionawr", "Chwefror", "Mawrth", "Ebrill", "Mai", "Mehefin", "Gorffennaf", "Awst", "Medi", "Hydref", "Tachwedd", "Rhagfyr"]


def follow_box(where):
    """The weekly email sign-up when a Brevo form is set; otherwise the ways to follow that need no account.

    The sign-up happens right here on the page: site.js sends the form to Brevo in the background and shows the thank-you
    in its place, so nobody is taken to Brevo's own page. Without JavaScript the form still posts to Brevo the plain way.
    email_address_check is Brevo's trap for robots (people never see it, so it stays empty)."""
    if EMAIL_FORM:
        return (f'<div class="follow follow-{where}"><p class="f-h">{bi("This week in Welsh history", "Yr wythnos hon yn hanes Cymru")}</p>'
                f'<p class="f-sub">{bi("One short email every Monday: the anniversaries of the week ahead and anything new on the site. Free, and you can leave at any time.", "Un e-bost byr bob dydd Llun: pen-blwyddi’r wythnos i ddod ac unrhyw beth newydd ar y wefan. Am ddim, a gallwch adael unrhyw bryd.")}</p>'
                f'<form class="f-form" action="{e(EMAIL_FORM)}" method="post" data-signup>'
                f'<div class="f-row"><label class="f-field"><span class="vh">{bi("Your email address", "Eich cyfeiriad e-bost")}</span>'
                f'<input type="email" name="EMAIL" required autocomplete="email" inputmode="email" placeholder="you@example.com"></label>'
                f'<input class="f-trap" type="text" name="email_address_check" value="" tabindex="-1" autocomplete="off" aria-hidden="true">'
                f'<input type="hidden" name="locale" value="en">'
                f'<button class="btn solid" type="submit">{bi("Sign up", "Ymuno")}</button></div>'
                f'<p class="f-msg" role="status" aria-live="polite"></p></form>'
                f'<a class="f-more" href="whatsnew.html">{bi("See what’s new on the site", "Gweld beth sy’n newydd ar y wefan")} →</a></div>')
    return (f'<div class="follow follow-{where}"><p class="f-h">{bi("Keep up with the site", "Dilynwch y wefan")}</p>'
            f'<p class="f-sub">{bi("New history is added every week. See what has arrived, or follow the news feed in any feed reader.", "Mae hanes newydd yn cael ei ychwanegu bob wythnos. Gwelwch beth sydd wedi cyrraedd, neu dilynwch y ffrwd newyddion mewn unrhyw ddarllenydd ffrydiau.")}</p>'
            f'<div class="f-row"><a class="btn solid" href="whatsnew.html">{bi("What’s new", "Beth sy’n newydd")}</a><a class="btn" href="feed.xml">{bi("News feed", "Ffrwd newyddion")}</a></div></div>')


def news_item(n, big=False):
    d, te, tc, se, sc, link = n
    return (f'<li class="news-item" data-date="{d}"><a href="{link}"><span class="n-date">{bi(_news_date(d), _news_date(d, True))}</span>'
            f'<span class="n-t">{bi(te, tc)}</span>' + (f'<span class="n-s">{bi(se, sc)}</span>' if big else "") + "</a></li>")


def news_strip():
    return (f'<div class="news-row one rv"><div class="news-box"><p class="eyebrow">{bi("New on the site", "Newydd ar y wefan")}</p>'
            f'<ul class="news-list">{"".join(news_item(n) for n in WN.NEWS[:3])}</ul>'
            f'<a class="n-all" href="whatsnew.html">{bi("Everything that is new", "Popeth sy’n newydd")} →</a></div></div>')  # "Keep up with the site" is in the footer of every page, so not here as well


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
        entries.append(("On this day in Welsh history: " + f"{now.day} {now.strftime('%B')}", BASE_URL + "onthisday.html", f"{BASE_URL}onthisday.html#{now.strftime('%Y-%m-%d')}", stamp, body))
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

    def li_more(h, a, b, de=None, dc=None):
        if de is None:
            return li(h, a, b)
        return f'<li><a href="{h}"{" class=on aria-current=page" if active == h else ""}>{bi(a, b)} <span class="m-dates">{bi(de, dc)}</span></a></li>'
    main = "".join(li(*x) for x in NAV_TOP)
    big = li("index.html", "Home", "Hafan", 1) + "".join(li(h, a, b, i + 2) for i, (h, a, b) in enumerate(NAV_MAIN))
    more = "".join(f'<div class="menu-group{" mg-ages" if links and len(links[0]) == 5 else ""}"><p class="eyebrow">{bi(ge, gc)}</p><ul class="menu-more">' + "".join(li_more(*x) for x in links) + "</ul></div>" for ge, gc, links in NAV_GROUPS)
    return (f'<a class="skip" href="{skip}">{bi("Skip to content", "Neidio i’r cynnwys")}</a><div class="progress" aria-hidden="true"><i id="progress"></i></div>'
            f'<nav class="nav" aria-label="Main"><div class="wrap">' + f'<a class="brand" href="index.html">{bi("History of Wales", "Hanes Cymru")}</a>' +
            f'<ul class="nav-inline">{main}</ul>' +
            f'<a class="journey-chip" href="journey.html" id="journey-chip" data-total="{JOURNEY_TOTAL}" title="Your journey: pages you have read / Eich taith: y tudalennau a ddarllenoch" aria-label="0 pages read: your journey / Eich taith"><span class="jc-ring"><svg viewBox="0 0 36 36" aria-hidden="true"><circle cx="18" cy="18" r="15" class="tr"/><circle cx="18" cy="18" r="15" class="fg" id="journey-ring" pathLength="100" stroke-dasharray="0 100"/></svg><b id="journey-n">0</b></span><span class="jc-l" aria-hidden="true">{bi("read", "wedi’u darllen")}</span></a>'
            f'<button type="button" class="search-btn" data-search aria-label="Search / Chwilio">{SEARCH_SVG}</button>'
             '<div class="lang" role="group" aria-label="Language / Iaith"><button type="button" id="lang-en" aria-pressed="true">EN</button><button type="button" id="lang-cy" aria-pressed="false">CY</button></div>'
            f'<button type="button" class="menu-btn" id="menu-btn" aria-expanded="false" aria-controls="menu" aria-label="Menu / Dewislen" data-news="{WN.NEWS[0][0]}"><span class="bars" aria-hidden="true"><i></i><i></i></span>{bi("Menu", "Dewislen")}</button></div></nav>'
            f'<div class="menu" id="menu" hidden><div class="wrap"><ul class="menu-big">{big}</ul><div class="menu-side"><div class="menu-groups">{more}</div>'
            f'<p class="menu-note">{bi("230,000 years of history, in English and Cymraeg.", "230,000 o flynyddoedd o hanes, yn Gymraeg ac yn Saesneg.")}</p></div></div></div>')


# Name shown in the copyright line at the bottom of every page.
COPYRIGHT_OWNER = "History of Wales"
COPYRIGHT_OWNER_CY = "Hanes Cymru"


def footer():
    def col(title_en, title_cy, links):
        return f'<details class="fcol" open><summary class="eyebrow">{bi(title_en, title_cy)}</summary><ul>' + "".join(f'<li><a href="{h}">{bi(a, b)}</a></li>' for h, a, b in links) + "</ul></details>"
    # Each list is a <details>, open in the HTML so every link shows on wide screens and without JavaScript.
    # On phones site.js closes them, so the footer is four tappable headings instead of 1,600 px of links.
    eras_col = (f'<details class="fcol" open><summary class="eyebrow">{bi("The nine ages", "Y naw oes")}</summary><ul>' + "".join(
        f'<li><a href="era-{x["id"]}.html">{bi(x["en"], x["cy"])} <span class="m-dates">{bi(x["spanEn"], x["spanCy"])}</span></a></li>' for x in D.ERAS) + "</ul></details>")
    explore = [("timeline.html", "Timeline", "Llinell amser"), ("map.html", "Map of Wales", "Map Cymru"), ("people.html", "People", "Pobl"), ("firsts.html", "Welsh world firsts", "Cymru oedd y cyntaf"), ("kings.html", "Kings and princes", "Brenhinoedd a thywysogion"), ("family-trees.html", "Royal family trees", "Coed teulu brenhinol"), ("saints.html", "Saints of Wales", "Seintiau Cymru"), ("castles.html", "Castles of Wales", "Cestyll Cymru"), ("trails.html", "Themed trails", "Llwybrau thema"),
               ("gallery.html", "Photo gallery", "Oriel luniau"), ("onthisday.html", "On this day", "Ar y dydd hwn"), ("index.html#language", "The Welsh language", "Yr iaith Gymraeg"), ("welsh.html", "Learn Welsh", "Dysgu Cymraeg")]
    read = [("whatsnew.html", "What’s new", "Beth sy’n newydd"), ("stories.html", "Long reads", "Erthyglau"), ("legends.html", "Legends", "Chwedlau"), ("mabinogion.html", "The Mabinogion", "Y Mabinogion"), ("laws.html", "The Laws of Hywel Dda", "Cyfreithiau Hywel Dda"), ("literature.html", "Welsh literature", "Llenyddiaeth Gymraeg"), ("books.html", "The great books of Wales", "Llyfrau mawr Cymru"), ("triads.html", "The Welsh Triads", "Trioedd Ynys Prydain"), ("symbols.html", "Symbols and traditions", "Symbolau a thraddodiadau"),
            ("teachers.html", "For teachers", "I athrawon"), ("index.html#sources", "Sources", "Ffynonellau"),
            ("about.html", "About this site", "Am y wefan hon"), ("about.html#corrections", "Report a mistake", "Rhoi gwybod am gamgymeriad")]
    play = [("daily.html", "Daily challenge", "Her y dydd"), ("quiz.html", "Quiz", "Cwis"), ("map-game.html", "Where in Wales?", "Ble yng Nghymru?"), ("names.html", "Welsh names", "Enwau Cymraeg"),
            ("play.html", "All games", "Pob gêm"), ("journey.html", "Your journey", "Eich taith")]
    yr = datetime.date.today().year
    yrs = "2026" if yr <= 2026 else f"2026–{yr}"
    # The text is shared under Creative Commons BY-NC 4.0 so schools and teachers may reuse it; photos and the 3D dragon keep their own licences.
    cc = '<a rel="license noopener" href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">'  # the copy lines below are HTML, not escaped
    copy_en = (f"© {yrs} {COPYRIGHT_OWNER}. The text of this site is shared under a {cc}Creative Commons Attribution-NonCommercial 4.0 licence (CC BY-NC 4.0)</a>: "
               f"you may copy, print and adapt it for any non-commercial use, such as in schools, as long as you credit {COPYRIGHT_OWNER} and link to the page. "
               "Photographs and the 3D dragon belong to their own creators and are used under their own licences, shown with each one.")
    copy_cy = (f"© {yrs} {COPYRIGHT_OWNER_CY}. Rhennir testun y wefan hon dan {cc}drwydded Creative Commons Cydnabyddiaeth-AnFasnachol 4.0 (CC BY-NC 4.0)</a>: "
               f"gallwch ei gopïo, ei argraffu a’i addasu at unrhyw ddefnydd anfasnachol, megis mewn ysgolion, cyn belled â’ch bod yn cydnabod {COPYRIGHT_OWNER_CY} ac yn rhoi dolen i’r dudalen. "
               "Mae’r ffotograffau a’r ddraig 3D yn eiddo i’w crewyr eu hunain ac fe’u defnyddir dan eu trwyddedau eu hunain, a ddangosir gyda phob un.")
    return ('<footer class="site-foot"><div class="wrap"><div class="foot-top"><p class="big">Diolch<span>.</span></p>'
            f'<p class="foot-tag">{bi("Thank you for reading. Wales is a small country with a long memory; this site is a way in.", "Diolch am ddarllen. Gwlad fach â chof hir yw Cymru; ffordd i mewn yw’r wefan hon.")}</p>{follow_box("foot")}</div>'
            f'<div class="foot-cols">{eras_col}{col("Explore", "Archwilio", explore)}{col("Read", "Darllen", read)}{col("Play", "Chwarae", play)}</div>'
            f'<div class="foot-base"><span>{bi("History of Wales · Hanes Cymru", "Hanes Cymru · History of Wales")}</span>'
            f'<span>{bi("Event links go to Wikipedia, which lists academic sources. Dates marked c. are approximate. Original illustrations; photographs from Wikimedia Commons, credited on each page.", "Mae dolenni’r digwyddiadau’n mynd i Wicipedia, sy’n rhestru ffynonellau academaidd. Dyddiadau bras yw’r rhai a nodir c. Darluniau gwreiddiol; ffotograffau o Wikimedia Commons, gyda chydnabyddiaeth ar bob tudalen.")}</span></div><p class="foot-copy"><span class="l-en" lang="en">{copy_en}</span><span class="l-cy" lang="cy">{copy_cy}</span></p></div></footer>'
            f'<button type="button" class="to-top" id="to-top" aria-label="Back to top / Yn ôl i’r brig" hidden><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>')


def page(path, title, desc, main_html, era=None, og_type="article", ld=None, active="", track="", extra=""):
    main_html = PX.dress(path, era, main_html)
    card = None
    if CARDS_ON and path != "404.html":
        CARD_JOBS[path] = (title, desc, era)
        card = "cards/" + path[:-5] + ".jpg"
    first = first_published(path)
    ld_html = SEO.ld_script(SEO.page_ld(BASE_URL, path, title, desc, og_type, ld, main_html, card, published=first))
    rk, rintro = page_refs(path)
    if rk and not path.startswith("story-") and path != "wales-in-10.html":
        main_html += f'<section class="tight page-refs"><div class="wrap narrow">{refs_block(rk, rintro)}</div></section>'
    if path != "404.html":
        main_html += AB.page_info(path, title, first)   # written by, first published, last updated, report a mistake (src/about.py)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
{head_tags(title, desc, path, og_type, card)}{LANG_BOOT}
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


FIRST_KIND = (("story-", "story"), ("legend-", "legend"), ("person-", "person"), ("place-", "place"))


# src/added.json was filled in from git history, which only goes back to 11 November 2026: items already on the site
# then all carry that first time, which is not their real first day, so they show no "First published" date.
ADDED_BASELINE = min((w for d in AD.DATA.values() for w in d.values()), default="")


def first_published(path):
    """The date a long read, legend, person or place first went up (src/added.json), or None for other pages."""
    for pre, kind in FIRST_KIND:
        if path.startswith(pre):
            when = AD.DATA.get(kind, {}).get(path[len(pre):-5])
            return when[:10] if when and when != ADDED_BASELINE else None
    return None


def hero(era_id, crumbs, ill, eyebrow_en, eyebrow_cy, h_en, h_cy, sub_en="", sub_cy="", art=None, extra="", photo=False):
    bg = f'<div class="hero-art">{(photo and A.photo_scene(art)) or A.scene(art, COL[era_id])}</div>' if art else ""
    icon = "" if art else f'<svg class="ill" aria-hidden="true"><use href="#i-{ill}"/></svg>'
    return (f'<header class="era-hero{" has-art" if art else ""}" data-era="{era_id}">{bg}<div class="wrap"><p class="crumbs">{crumbs}</p>'
            f'{icon}<p class="span">{bi(eyebrow_en, eyebrow_cy)}</p>'
            f'<h1>{bi(h_en, h_cy)}</h1>' + (f'<p class="lede">{bi(sub_en, sub_cy)}</p>' if sub_en else "") + extra + SHARE_BTN + "</div></header>")


SHARE_BTN = ('<p class="share-row"><button type="button" class="share-btn" data-share><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12v7a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-7M12 3v12M7 8l5-5 5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
             + bi("Share", "Rhannu") + "</button></p>")


def section(inner, title_en=None, title_cy=None, top=False):
    h = f'<h2 class="sub-h">{bi(title_en, title_cy)}</h2>' if title_en else ""
    cls = "" if top else ' class="tight"'
    return f'<section{cls}><div class="wrap">{h}{inner}</div></section>'


EVI = {ev: i for i, ev in enumerate(D.EVENTS)}
COMMONS = "https://commons.wikimedia.org/wiki/"


# Photos kept on the site by tools/fetch_photos.py: Commons file name -> [id, width, height]
LOCAL_PHOTOS = json.loads(read("photo_files.json")) if os.path.exists(os.path.join(SRC, "photo_files.json")) else {}


def photo_url(f, w=1200):
    if f in LOCAL_PHOTOS:  # our own copy: faster, and it can never disappear from Wikimedia
        return f"photos/{LOCAL_PHOTOS[f][0]}{'-s' if w <= 640 else ''}.webp"
    return f"{COMMONS}Special:FilePath/{_q(f, safe='')}?width={w}"


def place_ph(pid):
    """Picture for a place on the home page map: [image, Commons page, caption EN, caption CY] or None."""
    g = GP.GALLERY.get("place-" + pid)
    if g:
        return [f"gallery/place-{pid}-s.webp", COMMONS + "File:" + _q(g[0], safe=""), g[4], g[5]]
    ph = PH.PLACE_PHOTOS.get(pid)
    if ph:
        return [photo_url(ph[0], 640), COMMONS + "File:" + _q(ph[0], safe=""), ph[1], ph[2]]
    ref = PX.PAGE.get(f"place-{pid}.html", "")
    if ref.startswith("g:") and ref[2:].split("@")[0] in GP.GALLERY:  # a new place's own picture (src/pictures.py)
        k = ref[2:].split("@")[0]
        g = GP.GALLERY[k]
        return [f"gallery/{k}-s.webp", COMMONS + "File:" + _q(g[0], safe=""), g[4], g[5]]
    return None


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


def event_li(ev, k=0, title_link=False):
    links = ((f'<a class="src" href="laws.html">{bi("The Laws of Hywel Dda: the big page", "Cyfreithiau Hywel Dda: y dudalen fawr")} →</a>' if ev[5] == "The laws of Hywel Dda" else "")
             + "".join(f'<a class="src" href="story-{x["id"]}.html">{bi("Read the long read", "Darllen yr erthygl")} →</a>' for x in story_links("events", ev[5]))
             + (f'<a class="src" href="place-{ev[10]}.html">{bi("The place", "Y lle")} →</a>' if ev[10] else ""))
    links = f'<a class="wl" href="{EP.href(ev)}">{bi(ev[5], ev[6])}</a>' + (f'<div class="links">{links}</div>' if links else "")
    title = f'<a href="{EP.href(ev)}">{bi(ev[5], ev[6])}</a>' if title_link else bi(ev[5], ev[6])
    return (f'<li id="e{EVI[ev]}" class="wl-card{" key" if ev[9] else ""}" data-era="{ev[0]}"><time>{bi(year_label(ev), year_label(ev, True))}</time>'
            f'<div><h3>{title}</h3><p>{bi(ev[7], ev[8])}</p>{links}</div></li>')


def plaque(p, link=True):
    return (f'<article class="plaque{" wl-card" if link else ""}" id="{p[0]}" data-era="{p[1]}"><span class="dates">{bi(p[2], date_cy(p[2]))}</span><h3>{bi(p[3], p[4])}</h3>'
            f'<span class="epi">{bi(p[5], p[6])}</span><p>{bi(p[7], p[8])}</p>'
            + (f'<a class="wl" href="person-{p[0]}.html">{bi(p[3], p[4])}</a>' if link else "")
            + '</article>')


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
    pager = (f'<a class="btn" href="era-{prev_e["id"]}.html">← {bi(prev_e["en"], prev_e["cy"])} <span class="m-dates">{bi(prev_e["spanEn"], prev_e["spanCy"])}</span></a>' if prev_e else f'<a class="btn" href="index.html">← {bi("History of Wales", "Hanes Cymru")}</a>') + \
            (f'<a class="btn solid" href="era-{next_e["id"]}.html">{bi(next_e["en"], next_e["cy"])} <span class="m-dates">{bi(next_e["spanEn"], next_e["spanCy"])}</span> →</a>' if next_e else f'<a class="btn solid" href="trails.html">{bi("Follow a trail", "Dilyn llwybr")} →</a>')
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
    def nm(n, link):
        return f'<a href="person-{link}.html">{e(n)}</a>' if link and link in PERSON else e(n)
    line = "".join(f'<li{him_cls if him else ""}><b>{nm(n, link)}</b><span>{bi(a, c)}</span></li>' for n, a, c, him, link in AR.LINE)
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
        more = f'<a class="wl" href="{link}">{bi(en, cy)}</a>' if link else ""
        items += f'<li id="ar-{i}"{' class="wl-card"' if link else ""}><b>{bi(en, cy)}</b><p>{bi(ten, tcy)}{more}</p></li>'
    svg = (f'<svg class="ar-map" viewBox="-10 -10 630 691" role="img" aria-label="Map of places in Wales linked to Arthur / Map o leoedd yng Nghymru sy’n gysylltiedig ag Arthur">'
           f'<path class="land" d="{geo["outline"]}"/>{pins}</svg>')
    intro = bi("Nineteen places in Wales, and in Ergyng on the old border, that carry Arthur’s name or his story. Tap a number to read about it.",
               "Pedwar ar bymtheg o leoedd yng Nghymru, ac yn Ergyng ar yr hen ffin, sy’n dwyn enw Arthur neu ei hanes. Tapiwch rif i ddarllen amdano.")
    return (section(line_html, "The line of Arthur", "Llinach Arthur")
            + section(f'<p class="lede">{intro}</p><div class="ar-grid"><div class="ar-mapbox">{svg}</div><ol class="ar-list">{items}</ol></div>', "Arthur’s Wales", "Cymru Arthur"))


PERSON_EXTRA = {"arthur": arthur_extra}


def date_cy(d):
    """The Welsh side of a person's dates, where it differs (most dates read the same in both languages)."""
    return {"Age of Arthur": "Oes Arthur", "The Four Branches": "Y Pedair Cainc", "1st century BC": "y ganrif gyntaf CC", "12th century": "y 12fed ganrif", "4th century": "y 4edd ganrif"}.get(d, d)


def arthur_circle(slug):
    """Arthur's circle (src/arthur_circle.py): every person of Arthur's story, on Arthur's page and on each of theirs."""
    if slug not in AC.ALL_IDS:
        return ""
    out = ""
    for en, cy, ids in AC.GROUPS:
        chips = ""
        for s in ids:
            c = lit_person_chip(s)
            chips += c.replace("<a ", '<a aria-current="page" ', 1) if s == slug else c
        out += f'<h3 class="sub-h">{bi(en, cy)}</h3><div class="ppl">{chips}</div>'
    more = " ".join(f'<a class="btn" href="{u}">{bi(a, b)} →</a>' for u, a, b in AC.LINKS if u != f"person-{slug}.html")
    lead = bi(f"{len(AC.ALL_IDS)} people of Arthur’s story in Welsh tradition, each with a page of their own: his line in the charters of Llandaff, his family and warriors in the poems, the Triads and the tales, and the saints and bards who knew him.",
              f"{len(AC.ALL_IDS)} o bobl hanes Arthur yn nhraddodiad Cymru, pob un â’i dudalen ei hun: ei linach yn siarteri Llandaf, ei deulu a’i ryfelwyr yn y cerddi, y Trioedd a’r chwedlau, a’r saint a’r beirdd a’i hadwaenai.")
    return section(f'<div class="ar-circle"><p class="lede">{lead}</p>{out}<p class="ar-more">{more}</p></div>', "Arthur’s circle", "Cylch Arthur")


def princes_circle(slug):
    """The kings and princes of Wales (src/princes.py): the whole set, on each of their pages. Only people with a page are shown."""
    if slug not in PRN.ALL_IDS:
        return ""
    out = ""
    for en, cy, ids in PRN.GROUPS:
        ids = [s for s in ids if s in PERSON]
        if not ids:
            continue
        chips = ""
        for s in ids:
            c = lit_person_chip(s)
            chips += c.replace("<a ", '<a aria-current="page" ', 1) if s == slug else c
        out += f'<h3 class="sub-h">{bi(en, cy)}</h3><div class="ppl">{chips}</div>'
    more = " ".join(f'<a class="btn" href="{u}">{bi(a, b)} →</a>' for u, a, b in PRN.LINKS)
    lead = bi("The kings and princes of Wales, from Merfyn Frych and Rhodri Mawr to Llywelyn ein Llyw Olaf, each with a page of their own.",
              "Brenhinoedd a thywysogion Cymru, o Ferfyn Frych a Rhodri Mawr hyd Lywelyn ein Llyw Olaf, pob un â’i dudalen ei hun.")
    return section(f'<div class="ar-circle"><p class="lede">{lead}</p>{out}<p class="ar-more">{more}</p></div>', "Kings and princes of Wales", "Brenhinoedd a thywysogion Cymru")


def mabinogi_circle(slug):
    """The people of the Mabinogi (src/mabinogi_people.py): the block on each of their pages."""
    if slug not in MP.ALL_IDS or slug == "arthur":
        return ""
    out = ""
    for en, cy, ids in MP.GROUPS:
        chips = ""
        for s in ids:
            c = lit_person_chip(s)
            chips += c.replace("<a ", '<a aria-current="page" ', 1) if s == slug else c
        out += f'<h3 class="sub-h">{bi(en, cy)}</h3><div class="ppl">{chips}</div>'
    tales = [t for t in MT.TALES if slug in t["people"]]
    more = " ".join(f'<a class="btn" href="mabinogi-{t["id"]}.html">{bi("The tale: " + t["en"], "Y chwedl: " + t["cy"])} →</a>' for t in tales)
    more += f' <a class="btn" href="mabinogion.html">{bi("All the tales of the Mabinogion", "Holl chwedlau’r Mabinogion")} →</a> <a class="btn" href="story-mabinogi.html">{bi("Long read: the books that kept the tales", "Erthygl: y llyfrau a gadwodd y chwedlau")} →</a>'
    n = sum(1 for s in MP.ALL_IDS if s in PERSON)
    lead = bi(f"{n} people of the Mabinogi, each with a page of their own: the lords and ladies of Dyfed, the children of Llŷr and of Dôn, the heroes of the other tales, and the people who kept the tales alive.",
              f"{n} o bobl y Mabinogi, pob un â’i dudalen ei hun: arglwyddi ac arglwyddesau Dyfed, plant Llŷr a phlant Dôn, arwyr y chwedlau eraill, a’r bobl a gadwodd y chwedlau’n fyw.")
    return section(f'<div class="ar-circle"><p class="lede">{lead}</p>{out}<p class="ar-more">{more}</p></div>', "People of the Mabinogi", "Pobl y Mabinogi")


NUDGES = [(0, 0)] + [(round(r * c), round(r * s_)) for r in (30, 56, 84) for c, s_ in ((1, 0), (-1, 0), (0, -1), (0, 1), (.7, -.7), (-.7, -.7), (.7, .7), (-.7, .7))]


def pin_map(places, pre, label):
    """A numbered map of Wales with a list beside it (the look of Arthur's Wales). places: (en, cy, lat, lon, note en, note cy, link);
    a place with lat None is listed but has no pin (it lies outside Wales or is not known)."""
    sc, k, minx, maxy = geo["sc"], geo["k"], geo["minx"], geo["maxy"]
    pins, items, seen = "", "", []
    for i, (en, cy, lat, lon, ten, tcy, link) in enumerate(places, 1):
        if lat is not None:
            x0, y0 = (lon - minx) * k * sc, (maxy - lat) * sc
            x, y = x0, y0
            for dx, dy in NUDGES:  # a pin that would sit on another moves aside, with a short line back to the real spot
                if all((px - x0 - dx) ** 2 + (py - y0 - dy) ** 2 >= 27 ** 2 for px, py in seen):
                    x, y = x0 + dx, y0 + dy
                    break
            if (x, y) != (x0, y0):
                pins += f'<circle class="ar-dot" cx="{x0:.0f}" cy="{y0:.0f}" r="3" fill="#d43c34"/><line class="ar-lead" x1="{x0:.0f}" y1="{y0:.0f}" x2="{x:.0f}" y2="{y:.0f}"/>'
            seen.append((x, y))
            pins += (f'<a href="#{pre}-{i}" class="ar-pin"><circle cx="{x:.0f}" cy="{y:.0f}" r="13"/>'
                     f'<text x="{x:.0f}" y="{y + 5:.0f}">{i}</text><title>{e(en)}</title></a>')
        more = f'<a class="wl" href="{link}">{bi(en, cy)}</a>' if link else ""
        items += f'<li id="{pre}-{i}"{' class="wl-card"' if link else ""}><b>{bi(en, cy)}</b><p>{bi(ten, tcy)}{more}</p></li>'
    svg = (f'<svg class="ar-map" viewBox="-10 -10 630 691" role="img" aria-label="{e(label)}">'
           f'<path class="land" d="{geo["outline"]}"/>{pins}</svg>')
    return f'<div class="ar-grid"><div class="ar-mapbox">{svg}</div><ol class="ar-list">{items}</ol></div>'


def tale_page(t, i):
    """A guide to one tale of the Mabinogion (src/mabinogi_tales.py): the facts, the whole tale, its people and its places."""
    tl = MT.TALES
    prev_t, next_t = (tl[i - 1] if i > 0 else None), (tl[i + 1] if i + 1 < len(tl) else None)
    grp = next(g for g in MT.GROUPS if g[0] == t["group"])
    crumbs = f'<a href="index.html">{SITE}</a> / <a href="legends.html">{bi("Legends", "Chwedlau")}</a> / <a href="mabinogion.html">{bi("The Mabinogion", "Y Mabinogion")}</a>'
    ppl = "".join(lit_person_chip(s) for s in t["people"])
    links = ""
    if t["legend"]:
        lg = LEGEND.get(t["legend"][7:-5])
        if lg:
            links += f'<a class="btn solid" href="{t["legend"]}">{bi("Read the tale retold: " + lg["en"], "Darllen y chwedl: " + lg["cy"])} →</a> '
    links += (f'<a class="btn" href="story-mabinogi.html">{bi("The books that kept the tales", "Y llyfrau a gadwodd y chwedlau")} →</a> '
              f'<a class="btn" href="mabinogion.html">{bi("All the tales", "Pob chwedl")} →</a>')
    body = (f'<section class="article"><div class="wrap narrow"><p class="byline">{AB.byline_top()}<span>{bi(grp[1], grp[2])}</span></p>'
            f'{prose_bi(t["pEn"], t["pCy"], "story prose")}<p class="l-links">{links}</p></div></section>')
    who = section(f'<div class="ar-circle"><div class="ppl">{ppl}</div></div>', "People of the tale", "Pobl y chwedl") if ppl else ""
    hero_ref = PX.PAGE.get(f'mabinogi-{t["id"]}.html', "")
    hero_file = hero_ref[2:].split("@")[0] if hero_ref.startswith("c:") else None
    figs = "".join(lit_fig(f) for f in t.get("figs", []) if f[0] != hero_file)  # the picture at the top is not shown twice
    figs = section(f'<div class="mb-figs">{figs}</div>', "Pictures of the tale", "Lluniau’r chwedl") if figs else ""
    pins = sum(1 for x in t["places"] if x[2] is not None)
    where = section(f'<p class="lede">{bi(f"{pins} places in Wales where the tale happens. Tap a number to read about it.", f"{pins} o leoedd yng Nghymru lle mae’r chwedl yn digwydd. Tapiwch rif i ddarllen amdano.")}</p>'
                    + pin_map(t["places"], "lle", f'Map of the places of {t["en"]} / Map o leoedd {t["cy"]}'), "The places of the tale", "Lleoedd y chwedl") if t["places"] else ""
    pager = ((f'<a class="btn" href="mabinogi-{prev_t["id"]}.html">← {bi(prev_t["en"], prev_t["cy"])}</a>' if prev_t else f'<a class="btn" href="mabinogion.html">← {bi("The Mabinogion", "Y Mabinogion")}</a>')
             + (f'<a class="btn solid" href="mabinogi-{next_t["id"]}.html">{bi(next_t["en"], next_t["cy"])} →</a>' if next_t else f'<a class="btn solid" href="mabinogion.html">{bi("The Mabinogion", "Y Mabinogion")} →</a>'))
    main = (hero(t["era"], crumbs, "book", t["n"][0], t["n"][1], t["en"], t["cy"], t["sumEn"], t["sumCy"], art="book")
            + body + figs + who + where + section(f'<div class="pager">{pager}</div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": f'{t["cy"]} ({t["en"]})', "description": t["sumEn"], "inLanguage": ["en", "cy"],
          "about": {"@type": "Book", "name": t["cy"], "alternateName": t["en"], "inLanguage": "cy"}, "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page(f'mabinogi-{t["id"]}.html', f'{t["cy"]}: {t["en"]} · History of Wales', t["sumEn"], main, era=t["era"], ld=ld, active="legends.html", track=f'mabinogi:{t["id"]}')


def writers_circle(slug):
    """The writers who recorded early Wales (src/writers.py): the whole set, on each of their pages. Only people with a page are shown."""
    if slug not in WRT.ALL_IDS:
        return ""
    out = ""
    for en, cy, ids in WRT.GROUPS:
        ids = [s for s in ids if s in PERSON]
        if not ids:
            continue
        chips = ""
        for s in ids:
            c = lit_person_chip(s)
            chips += c.replace("<a ", '<a aria-current="page" ', 1) if s == slug else c
        out += f'<h3 class="sub-h">{bi(en, cy)}</h3><div class="ppl">{chips}</div>'
    built = {f'story-{x["id"]}.html' for x in F.STORIES}
    more = " ".join(f'<a class="btn" href="{u}">{bi(a, b)} →</a>' for u, a, b in WRT.LINKS if not u.startswith("story-") or u in built)
    lead = bi("The monks, scholars, storytellers and scribes who wrote down the history of early Wales, from Gildas to the soldier of Calais, each with a page of their own.",
              "Y mynachod, yr ysgolheigion, y storïwyr a’r copïwyr a ysgrifennodd hanes Cymru gynnar, o Gildas hyd filwr Calais, pob un â’i dudalen ei hun.")
    return section(f'<div class="ar-circle"><p class="lede">{lead}</p>{out}<p class="ar-more">{more}</p></div>', "Writers who recorded early Wales", "Awduron a gofnododd Gymru gynnar")


def person_page(p):
    slug, eid = p[0], p[1]
    era = ERA[eid]
    long_en, long_cy = L.PEOPLE_LONG.get(slug) or D.PEOPLE_EXTRA_LONG[slug]
    related = [ev for ev in D.EVENTS if p[3] in ev[7] or p[3] in ev[5] or (slug == "dewi-sant" and "Dewi" in ev[7])]
    same = [x for x in D.PEOPLE if x[1] == eid and x[0] != slug][:4]
    idx = D.PEOPLE.index(p)
    prev_p, next_p = D.PEOPLE[idx - 1] if idx > 0 else None, D.PEOPLE[idx + 1] if idx + 1 < len(D.PEOPLE) else None
    pager = (f'<a class="btn" href="person-{prev_p[0]}.html">← {bi(prev_p[3], prev_p[4])}</a>' if prev_p else f'<a class="btn" href="era-{eid}.html">← {bi(era["en"], era["cy"])}</a>') + \
            (f'<a class="btn solid" href="person-{next_p[0]}.html">{bi(next_p[3], next_p[4])} →</a>' if next_p else '<a class="btn solid" href="people.html">' + bi("All people", "Pawb") + " →</a>")
    fld = FIELD_LABEL.get(P2.FIELD.get(slug))
    meta = (f'<div class="person-meta"><span>{bi(p[2], date_cy(p[2]))}</span><span>{bi(p[5], p[6])}</span><a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a>'
            + (f'<a href="people.html?field={P2.FIELD[slug]}">{bi(*fld)}</a>' if fld else "") + '</div>' + first_badge(slug))
    rl = realm_links(f"person-{slug}.html") + ft_link_for_person(f"person-{slug}.html") + saints_links(f"person-{slug}.html") + lit_link(slug)
    meta += f'<p class="realm-links">{rl}</p>' if rl else ""
    coded = any(a.startswith(("## ", "> ", "|| ")) for a in long_en)
    body = prose_bi(long_en, long_cy, cls="story prose") if coded else paras(long_en, long_cy)
    main = (hero(eid, f'<a href="index.html">{SITE}</a> / <a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a>', era["ill"], p[2], date_cy(p[2]), p[3], p[4], p[7], p[8], art=ERA_ART[eid])
            + section(meta + photo_fig(PH.PERSON_PHOTOS.get(slug), "portrait", "person-" + slug) + body + f'<p class="share no-print"><button type="button" class="btn" data-copy="person-{slug}.html">{bi("Copy link to share", "Copïo dolen i’w rhannu")}</button></p>' + further(f"person:{slug}", p[9]), top=True)
            + PERSON_EXTRA.get(slug, lambda: "")()
            + arthur_circle(slug)
            + mabinogi_circle(slug)
            + princes_circle(slug)
            + writers_circle(slug)
            + story_feature("people", slug)
            + person_places(slug)
            + (section(f'<ol class="era-events">{"".join(event_li(ev) for ev in related)}</ol>', "On the timeline", "Ar y llinell amser") if related else "")
            + set_block(f"person:{slug}")
            + section(f'<div class="people">{"".join(plaque(x) for x in same)}</div>', "Also in this age", "Hefyd yn yr oes hon")
            + section(f'<div class="pager">{pager}</div>'))
    ld = {"@context": "https://schema.org", "@type": "Person", "name": p[3], "alternateName": p[4], "description": p[7]}
    if p[9]:
        ld["sameAs"] = WIKI + p[9]
    return page(f"person-{slug}.html", f"{p[3]} · History of Wales", p[7], main, era=eid, ld=ld, og_type="profile", track=f"person:{slug}")


# ---------- place pages ----------
def directions_url(pl):
    return f'https://www.google.com/maps/dir/?api=1&destination={pl["lat"]},{pl["lon"]}'


def visit_info(pid):
    """(who en, who cy, official url, entry en, entry cy, postcode) for a place, or None (src/visit.py)."""
    v = VS.VISIT.get(pid)
    if not v:
        return None
    who = v["who"] if isinstance(v["who"], tuple) else VS.WHO[v["who"]]
    ent = VS.ENTRY[v["entry"]]
    return who[0], who[1], v["url"], ent[0], ent[1], v["pc"]


def map_visit(p):
    """The visiting line on the map card: [who en, who cy, official url, entry en, entry cy, postcode, directions url]."""
    v = visit_info(p["id"])
    return list(v) + [directions_url(p)] if v else None


def visit_box(pl):
    """The Visiting box: who looks after the place, the official page for times and prices, entry, postcode, directions."""
    pid = pl["id"]
    v = VS.VISIT.get(pid)
    if not v:
        return ""
    who_en, who_cy, url, ent_en, ent_cy, pc = visit_info(pid)
    off = (f' <a href="{e(url)}" target="_blank" rel="noopener">{bi("Opening times and prices", "Amseroedd agor a phrisiau")} ↗</a>' if url else "")
    rows = f'<div><dt>{bi("Looked after by", "Yng ngofal")}</dt><dd>{bi(e(who_en[0].upper() + who_en[1:]), e(who_cy[0].upper() + who_cy[1:]))}{off}</dd></div>'
    for w, u, wen, wcy in v["also"]:
        wn = w if isinstance(w, tuple) else VS.WHO[w]
        rows += (f'<div><dt>{bi("Also", "Hefyd")}</dt><dd>{bi(e(wn[0][0].upper() + wn[0][1:] + ": " + wen), e(wn[1][0].upper() + wn[1][1:] + ": " + wcy))}'
                 + (f' <a href="{e(u)}" target="_blank" rel="noopener">{bi("Their page", "Eu tudalen")} ↗</a>' if u else "") + "</dd></div>")
    rows += f'<div><dt>{bi("Entry", "Mynediad")}</dt><dd>{bi(ent_en, ent_cy)}</dd></div>'
    where = (f'{bi("Postcode", "Cod post")} <b>{e(pc)}</b> · ' if pc else "") + \
        (f'<a href="{directions_url(pl)}" target="_blank" rel="noopener">{bi("Directions", "Cyfarwyddiadau")} ↗</a> · '
         f'<a href="map.html#lle-{pid}">{bi("On our map", "Ar ein map")} →</a>')
    rows += f'<div><dt>{bi("Getting there", "Cyrraedd")}</dt><dd>{where}</dd></div>'
    note = f'<p class="visit-note">{bi(*v["note"])}</p>' if v.get("note") else ""
    return (f'<aside class="visit-box" aria-label="Visiting / Ymweld"><h2>{bi("Visiting", "Ymweld")}</h2><dl>{rows}</dl>{note}'
            f'<p class="visit-small">{bi("Check the official page before you travel: times change, and some sites close in winter.", "Edrychwch ar y dudalen swyddogol cyn teithio: mae amseroedd yn newid, ac mae rhai safleoedd yn cau yn y gaeaf.")}</p></aside>')


def place_people(pid):
    """Links to the people of a place (src/places3.py PEOPLE). Slugs with no page yet are left out until they have one."""
    xs = [PERSON[s] for s in PL3.PEOPLE.get(pid, []) if s in PERSON]
    links = [(href, en, cy) for href, en, cy in PL3.LINKS.get(pid, [])]
    if not xs and not links:
        return ""
    out = ""
    if xs:
        out += (f'<p class="eyebrow">{bi("People of this place", "Pobl y lle hwn")}</p><p class="pl-people">'
                + "".join(f'<a href="person-{x[0]}.html">{bi(x[3], x[4])}</a>' for x in xs) + "</p>")
    if links:
        out += (f'<p class="eyebrow">{bi("More on this site", "Mwy ar y wefan hon")}</p><p class="pl-people">'
                + "".join(f'<a href="{h}">{bi(en, cy)} →</a>' for h, en, cy in links) + "</p>")
    return f'<div class="pl-links">{out}</div>'


# person -> the places linked with them (src/places3.py PEOPLE), for "Places to visit" on person pages
PERSON_PLACES = {}
for _pid, _slugs in PL3.PEOPLE.items():
    for _s in _slugs:
        PERSON_PLACES.setdefault(_s, []).append(_pid)


def person_places(slug):
    xs = [PLACE[x] for x in PERSON_PLACES.get(slug, []) if x in PLACE]
    return section(f'<div class="era-places">{"".join(place_tile(x) for x in xs)}</div>', "Places to visit", "Lleoedd i ymweld â nhw") if xs else ""


def place_page(pl):
    pid, eid = pl["id"], pl["era"]
    era = ERA[eid]
    long_en, long_cy = L.PLACE_LONG.get(pid, ([], []))
    related = [ev for ev in D.EVENTS if ev[10] == pid]
    near = sorted([x for x in D.PLACES if x["id"] != pid], key=lambda x: (x["lat"] - pl["lat"]) ** 2 + ((x["lon"] - pl["lon"]) * 0.61) ** 2)[:3]
    osm = f'https://www.openstreetmap.org/?mlat={pl["lat"]}&mlon={pl["lon"]}#map=14/{pl["lat"]}/{pl["lon"]}'
    meta = (f'<div class="person-meta"><span>{e(pl["year"])}</span><span>{pl["lat"]:.3f}° N, {abs(pl["lon"]):.3f}° W</span>'
            f'<a href="{osm}" target="_blank" rel="noopener">{bi("Open in a map", "Agor mewn map")} ↗</a><a href="map.html#lle-{pid}">{bi("On our map", "Ar ein map")} →</a></div>')
    rl = realm_links(f"place-{pid}.html") + saints_links(f"place-{pid}.html")
    meta += f'<p class="realm-links">{rl}</p>' if rl else ""
    coded = any(a.startswith(("## ", "> ", "|| ")) for a in long_en)
    body = prose_bi(long_en, long_cy, cls="story prose") if coded else paras(long_en, long_cy)
    main = (hero(eid, f'<a href="index.html">{SITE}</a> / <a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a>', pl["ill"], era["en"], era["cy"], pl["en"], pl["cy"], pl["dEn"], pl["dCy"], art=ERA_ART[eid])
            + section(meta + photo_fig(PH.PLACE_PHOTOS.get(pid), "", "place-" + pid) + body + visit_box(pl) + place_people(pid) + further(f"place:{pid}", pl["src"]), top=True)
            + story_feature("places", pid)
            + (section(f'<ol class="era-events">{"".join(event_li(ev) for ev in related)}</ol>', "What happened here", "Beth ddigwyddodd yma") if related else "")
            + set_block(f"place:{pid}")
            + section(f'<div class="era-places">{"".join(place_tile(x) for x in near)}</div>', "Nearby", "Gerllaw"))
    ld = {"@context": "https://schema.org", "@type": "TouristAttraction", "name": pl["en"], "alternateName": pl["cy"], "description": pl["dEn"],
          "geo": {"@type": "GeoCoordinates", "latitude": pl["lat"], "longitude": pl["lon"]}}
    return page(f"place-{pid}.html", f'{pl["en"]} · History of Wales', pl["dEn"], main, era=eid, ld=ld, og_type="place", track=f"place:{pid}")


# ---------- trails ----------
# A stop is ("event", title) | ("person", slug) | ("place", id) | ("story", id) | ("legend", id)
# | ("page", href, era, dateEn, dateCy, titleEn, titleCy, textEn, textCy). A story, legend or page may add
# its own date label: ("story", id, dateEn, dateCy). A story that is not on the site yet is left out until it is,
# so a trail can name a long read another thread is still writing. Every stop links to its full page.
STORY_BY_ID = {x["id"]: x for x in F.STORIES}
LEGEND_BY_ID = {x["id"]: x for x in F.LEGENDS}


def trail_stops(t):
    return [it for it in t["items"] if (it[0] != "story" or it[1] in STORY_BY_ID) and (it[0] != "legend" or it[1] in LEGEND_BY_ID)]


def _stop(era, date_en, date_cy, href, en, cy, text_en, text_cy, extra=""):
    full = f'<a class="wl" href="{href}">{bi(en, cy)}</a>'
    return (f'<li class="wl-card" data-era="{era}"><time>{bi(date_en, date_cy)}</time><div><h3><a href="{href}">{bi(en, cy)}</a></h3>'
            f'<p>{bi(text_en, text_cy)}</p>{full}{f'<div class="links">{extra}</div>' if extra else ""}</div></li>')


def _reads(kind, key):
    return "".join(f'<a class="src" href="story-{x["id"]}.html">{bi("Long read: " + x["en"], "Erthygl: " + x["cy"])} →</a>' for x in sorted(story_links(kind, key), key=lambda x: len(x.get(kind, [])))[:1])


def trail_item(item):
    kind, ref = item[0], item[1]
    if kind == "person":
        p = PERSON[ref]
        return _stop(p[1], p[2], date_cy(p[2]), f"person-{ref}.html", p[3], p[4], p[7], p[8], _reads("people", ref))
    if kind == "place":
        p = PLACE[ref]
        return _stop(p["era"], p["year"], p["year"], f"place-{ref}.html", p["en"], p["cy"], p["dEn"], p["dCy"], _reads("places", ref))
    if kind == "story":
        x = STORY_BY_ID[ref]
        d = item[2:4] if len(item) > 2 else (f'{x["mins"]} min read', f'{x["mins"]} munud')
        return _stop(x["era"], d[0], d[1], f"story-{ref}.html", x["en"], x["cy"], x["sumEn"], x["sumCy"])
    if kind == "legend":
        x = LEGEND_BY_ID[ref]
        d = item[2:4] if len(item) > 2 else ("Welsh tradition", "Traddodiad Cymru")
        return _stop(x["era"], d[0], d[1], f"legend-{ref}.html", x["en"], x["cy"], x["sumEn"], x["sumCy"])
    if kind == "page":
        href, era, den, dcy, en, cy, ten, tcy = item[1:]
        return _stop(era, den, dcy, href, en, cy, ten, tcy)
    ev = EVENT_BY_TITLE[ref]
    return event_li(ev, title_link=True)


def trail_page(t, i):
    nxt = L.TRAILS[(i + 1) % len(L.TRAILS)]
    main = (hero("medieval", f'<a href="index.html">{SITE}</a> / <a href="trails.html">{bi("Trails", "Llwybrau")}</a>', t["ill"], "Trail", "Llwybr", t["en"], t["cy"], art=TRAIL_ART.get(t["id"], "castle"))
            + section(paras(t["introEn"], t["introCy"]), top=True)
            + section(f'<ol class="era-events trail">{"".join(trail_item(it) for it in trail_stops(t))}</ol>', "Stops on the trail", "Arosfannau ar y llwybr")
            + section(f'<div class="pager"><a class="btn" href="trails.html">← {bi("All trails", "Pob llwybr")}</a><a class="btn solid" href="trail-{nxt["id"]}.html">{bi(nxt["en"], nxt["cy"])} →</a></div>'))
    return page(f"trail-{t['id']}.html", f'{t["en"]} · History of Wales', t["introEn"][0], main, era="medieval", active="trails.html")


def trails_index():
    cards = "".join(f'<a class="chap" href="trail-{t["id"]}.html" data-era="{D.ERAS[i % len(D.ERAS)]["id"]}"><svg aria-hidden="true"><use href="#i-{t["ill"]}"/></svg>'
                    f'<span class="span">{len(trail_stops(t))} {bi("stops", "arhosfan")}</span><h3>{bi(t["en"], t["cy"])}</h3><p>{bi(t["introEn"][0], t["introCy"][0])}</p>'
                    f'</a>' for i, t in enumerate(L.TRAILS))
    main = (hero("modern", f'<a href="index.html">{SITE}</a>', "mtn", "Themed trails", "Llwybrau thema", "Trails through Welsh history", "Llwybrau drwy hanes Cymru",
                 "Follow one thread through the centuries.", "Dilynwch un edefyn drwy’r canrifoedd.", art="arches")
            + section(f'<h2 class="sr-only">{bi("All trails", "Pob llwybr")}</h2><div class="chapters">{cards}</div>', top=True))
    return page("trails.html", "Trails · History of Wales", f"{len(L.TRAILS)} themed trails through Welsh history: kings and princes, Arthur, saints, the language, castles, rebels, poets, women, the sea, chapel and song, iron and coal, and more.", main, era="modern", og_type="website", active="trails.html")


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
                "The text is shared under a Creative Commons BY-NC 4.0 licence, so you may copy, print and adapt it for lessons and worksheets, as long as you credit History of Wales and link to the page. Photographs keep their own licences, shown with each one.",
                "The ideas below fit the Humanities Area of Learning and Experience in the Curriculum for Wales, with its focus on cynefin, enquiry and the diverse stories of Wales. Adapt them freely."]
    intro_cy = ["Mae Hanes Cymru am ddim i’w ddefnyddio yn y dosbarth. Mae pob tudalen yn gweithio yn Gymraeg ac yn Saesneg, ac mae pob digwyddiad yn cysylltu â ffynhonnell, fel y gall disgyblion ymarfer gwirio tystiolaeth.",
                "Rhennir y testun dan drwydded Creative Commons BY-NC 4.0, felly gallwch ei gopïo, ei argraffu a’i addasu ar gyfer gwersi a thaflenni gwaith, cyn belled â’ch bod yn cydnabod Hanes Cymru ac yn rhoi dolen i’r dudalen. Mae gan y ffotograffau eu trwyddedau eu hunain, a ddangosir gyda phob un.",
                "Mae’r syniadau isod yn addas ar gyfer Maes Dysgu a Phrofiad y Dyniaethau yng Nghwricwlwm i Gymru, gyda’i bwyslais ar gynefin, ymholi a straeon amrywiol Cymru. Addaswch nhw fel y mynnwch."]
    main = (hero("industrial", f'<a href="index.html">{SITE}</a>', "book", "For teachers", "I athrawon", "History of Wales in the classroom", "Hanes Cymru yn y dosbarth",
                 "Nine free teacher packs for the Curriculum for Wales, lesson ideas, enquiry questions and printable quiz sheets for each age.", "Naw pecyn athrawon am ddim ar gyfer y Cwricwlwm i Gymru, syniadau gwersi, cwestiynau ymholi a thaflenni cwis i’w hargraffu ar gyfer pob oes.", art="book")
            + section(paras(intro_en, intro_cy), top=True)
            + section(TPK.packs_grid(), "Teacher packs, one for each age", "Pecynnau athrawon, un ar gyfer pob oes")
            + section(f'<div class="lessons">{blocks}</div>', "Lesson ideas", "Syniadau gwersi")
            + section(f'<p class="no-print"><button type="button" class="btn solid" data-print="1">{bi("Print the quiz sheets", "Argraffu’r taflenni cwis")}</button> '
                      f'<span class="muted">{bi("Prints in whichever language is selected. Answers are hidden until opened.", "Yn argraffu yn yr iaith a ddewiswyd. Mae’r atebion yn gudd nes eu hagor.")}</span></p>{sheets}', "Printable quiz sheets", "Taflenni cwis i’w hargraffu")
            + section("<p>" + AB.rbi(f"Spotted a mistake, or have a resource to share? Email {AB.mail_link()}.", f"Wedi gweld camgymeriad, neu am rannu adnodd? Anfonwch e-bost at {AB.mail_link()}.") + "</p>"))
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
EXTRA_PAGE_CSS += read("laws.css")  # laws.html
style += EXTRA_PAGE_CSS

# ---------- new feature pages ----------
JOURNEY_TOTAL = len(D.ERAS) + len(D.PEOPLE) + len(D.PLACES) + len(F.STORIES) + len(F.LEGENDS)
STORY = {x["id"]: x for x in F.STORIES}


def prose(pars, cls="prose", figs=None):
    # "## " sub-heading, "> quote | source" pull quote, "|| left | right" table row (rows in a run make one table),
    # "!! key" a credited picture: from the long read's own figs={key: Commons tuple} (see lit_fig), or a gallery id
    # (src/gallery_photos.py)
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
        if a.startswith("!! ") and a[3:].strip() in (figs or {}):  # a picture from the long read's own list (see lit_fig)
            out += lit_fig(figs[a[3:].strip()], "lr-fig")
        elif a.startswith("!! "):  # a picture from the gallery, with its full credit (see photo_fig)
            if a[3:].strip() not in GP.GALLERY:
                raise SystemExit(f"prose(): unknown gallery picture '{a[3:].strip()}' (see src/gallery_photos.py)")
            g = GP.GALLERY[a[3:].strip()]
            out += photo_fig(None, "in-text portrait" if g[7] > g[6] else "in-text", a[3:].strip())  # tall pictures keep their faces
        elif a.startswith("## "):
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


LAW_LINKED = {"people": {"hywel-dda", "llywelyn-ap-gruffudd"}, "places": {"hendygwyn", "library", "dinefwr", "aberffraw"}}


def laws_card():
    return (f'<a class="s-card rv lead" href="laws.html" data-era="kings"><span class="art">{PX.card_img("laws.html") or A.scene("book", COL["kings"])}</span>'
            f'<span class="txt"><span class="span">{bi("The big page", "Y dudalen fawr")} · {bi("15 chapters, pictures and a quiz", "15 pennod, lluniau a chwis")}</span><h3>{bi("The Laws of Hywel Dda", "Cyfreithiau Hywel Dda")}</h3>'
            f'<p>{bi("Everything about Cyfraith Hywel: the gathering at Whitland, the three lawbooks, galanas and sarhaed, women and marriage, the worth of everything, and the manuscripts with their pictures.", "Popeth am Gyfraith Hywel: y cynulliad yn Hendy-gwyn, y tri llyfr cyfraith, galanas a sarhaed, menywod a phriodas, gwerth pob peth, a’r llawysgrifau a’u lluniau.")}</p>'
            f'</span></a>')


def story_feature(kind, key):
    xs = story_links(kind, key)
    law = laws_card() if key in LAW_LINKED.get(kind, ()) else ""
    return section(f'<div class="s-grid">{"".join(story_card(x, True) for x in xs)}{law}</div>', "The full story", "Y stori lawn") if xs or law else ""


def prose_bi(en, cy, cls="prose", figs=None):
    return f'<div class="{cls} l-en" lang="en">{prose(en, figs=figs)}</div><div class="{cls} l-cy" lang="cy">{prose(cy, figs=figs)}</div>'


def story_card(x, lead=False):
    return (f'<a class="s-card rv{" lead" if lead else ""}" href="story-{x["id"]}.html" data-era="{x["era"]}"><span class="art">{PX.card_img(f"story-{x['id']}.html", x["era"]) or A.scene(x["art"], COL[x["era"]])}</span>'
            f'<span class="txt"><span class="span">{bi("Long read", "Erthygl")} · {x["mins"]} {bi("min", "mun")}{new_tag("story", x["id"])}</span><h3>{bi(x["en"], x["cy"])}</h3><p>{bi(x["sumEn"], x["sumCy"])}</p>'
            f'</span></a>')


def new_tag(kind, i, ids=None):
    """A small "New" badge for one of the newest things added in the last two weeks (src/added.py)."""
    return f' <span class="new-tag">{bi("New", "Newydd")}</span>' if AD.is_new(kind, i, ids) else ""


def added_date(kind, i, cy=False):
    return _news_date(AD.when(kind, i)[:10], cy)


def just_added(kind, items, href, title, key=lambda x: x["id"], n=4, h_en="Just added", h_cy="Newydd ei ychwanegu"):
    """A "Just added" strip for the top of a list whose own order means something (by date, A to Z, by section):
    the newest few items, with the day each went up. Nothing at all until something is added after the list began."""
    xs = AD.recent(kind, items, key, n)
    if not xs:
        return ""
    lis = "".join(f'<li><a href="{href(x)}"><b>{bi(*title(x))}</b><small class="ja-d">{bi(added_date(kind, key(x)), added_date(kind, key(x), True))}</small></a></li>' for x in xs)
    return f'<section class="just-added" aria-label="{h_en} / {h_cy}"><h2>{bi(h_en, h_cy)}</h2><ul>{lis}</ul></section>'


def legend_card(x):
    return (f'<a class="l-card rv" href="legend-{x["id"]}.html" data-era="{x["era"]}"><span class="art">{A.photo_scene(x["art"], small=True) or PX.card_img(f"legend-{x['id']}.html", x["era"]) or A.scene(x["art"], COL[x["era"]])}</span>'
            f'<span class="txt"><span class="span">{e(x["place"])}{new_tag("legend", x["id"])}</span><h3>{bi(x["en"], x["cy"])}</h3><p>{bi(x["sumEn"], x["sumCy"])}</p></span></a>')


def story_more_links(x):
    # optional links=[(href, en, cy)] on a long read: buttons at the end of the text. A story- link whose long read
    # is not built (yet) is left out, so threads can link to each other's pages in any order.
    ids = {y["id"] for y in F.STORIES}
    ls = [(h, en, cy) for h, en, cy in x.get("links", []) if not h.startswith("story-") or h[6:-5] in ids]
    return (f'<p class="l-links">' + " ".join(f'<a class="btn" href="{h}">{bi(en, cy)} →</a>' for h, en, cy in ls) + '</p>') if ls else ""


REF_KINDS = [("p", "Old sources and records", "Hen ffynonellau a chofnodion"), ("b", "Books by historians", "Llyfrau gan haneswyr"), ("w", "Online", "Ar-lein")]


REF_AGE_INTRO = ("Books on this age of Welsh history, for anyone who wants to go further. Any library in Wales can find them for you.",
                 "Llyfrau ar yr oes hon yn hanes Cymru, i unrhyw un sydd am fynd ymhellach. Gall unrhyw lyfrgell yng Nghymru eu cael i chi.")


def refs_block(key, intro=None):
    """The "Further reading and references" list (src/refs.py for long reads, src/refs2.py for other pages), with the
    Dictionary of Welsh Biography articles for the people in it. Prints for teachers too."""
    r = REF.REFS.get(key) or REF2.PAGES.get(key)
    if not r:
        return ""
    out = []
    for kind, en, cy in REF_KINDS:
        lis = []
        for it in r["items"]:
            if it[0] != kind:
                continue
            _, who, title, det, nen, ncy = it[:6]
            url = it[6] if len(it) > 6 else ""
            t = f'<a href="{e(url)}" target="_blank" rel="noopener"><cite>{e(title)}</cite> ↗</a>' if url else f"<cite>{e(title)}</cite>"
            lis.append(f'<li><span class="ref-w">{e(who)}</span>, {t} <span class="ref-d">({e(det)})</span><span class="ref-n">{bi(nen, ncy)}</span></li>')
        if kind == "w":
            for pid in r.get("dwb", []):
                rec = SOURCE_LINKS.get("person:" + pid, {})
                if rec.get("dwb"):
                    name = PERSON[pid][3] if pid in PERSON else rec.get("cy", pid)
                    u = rec["dwb"]
                    lis.append(f'<li><span class="ref-w">{bi("Dictionary of Welsh Biography", "Y Bywgraffiadur Cymreig")}</span>, '
                               f'<a class="l-en" lang="en" href="{e(u)}" target="_blank" rel="noopener"><cite>{e(name)}</cite> ↗</a>'
                               f'<a class="l-cy" lang="cy" href="{e(u.replace("://biography.wales/", "://bywgraffiadur.cymru/"))}" target="_blank" rel="noopener"><cite>{e(rec.get("cy") or name)}</cite> ↗</a></li>')
        if lis:
            out.append(f'<h3>{bi(en, cy)}</h3><ul>{"".join(lis)}</ul>')
    if not out:
        return ""
    return (f'<aside class="refs" id="references" aria-labelledby="refs-h"><h2 id="refs-h">{bi("Further reading and references", "Darllen pellach a chyfeiriadau")}</h2>'
            f'<p class="refs-i">{bi(*(intro or ("The old texts and the historians’ books behind this page, for anyone who wants to go further. Any library in Wales can find them for you.", "Yr hen destunau a llyfrau’r haneswyr y tu ôl i’r dudalen hon, i unrhyw un sydd am fynd ymhellach. Gall unrhyw lyfrgell yng Nghymru eu cael i chi.")))}</p>'
            + "".join(out) + f'<p class="refs-all"><a href="books-and-authors.html">{bi("Every book on the site, with its authors", "Pob llyfr ar y wefan, gyda’u hawduron")} →</a></p></aside>')


def page_refs(path):
    """Which reference list (and intro) a page gets at its foot. Long reads carry theirs inside the article."""
    name = path[:-5] if path.endswith(".html") else path
    kind, _, rest = name.partition("-")
    if name in REF2.PAGES:
        return name, None
    if name in REF2.GENERAL:
        return "general", None
    if kind == "person" and rest in AC.ALL_IDS and rest != "arthur" and "arthur-circle" in REF2.PAGES:
        return "arthur-circle", None
    if kind == "person" and rest in MP.OWN_IDS and "mabinogi-people" in REF2.PAGES:
        return "mabinogi-people", None
    if kind == "book":  # the old books (src/oldbooks.py): a book's own list, or the list for all the books
        return ("books" if name not in REF2.PAGES else name), None
    if kind == "mabinogi" and f"mabinogi-{rest}" in REF2.PAGES:  # a tale with its own reading list (src/refs2.py)
        return f"mabinogi-{rest}", None
    if kind == "mabinogi" and "mabinogi-tales" in REF2.PAGES:
        return "mabinogi-tales", None
    if kind in ("person", "place"):
        rec = PERSON.get(rest) if kind == "person" else PLACE.get(rest)
        era = (rec[1] if kind == "person" else rec["era"]) if rec else None
        return (f"era-{era}", REF_AGE_INTRO) if era and f"era-{era}" in REF2.PAGES else (None, None)
    if kind == "kings":
        return REF2.KINGS_GROUP.get(rest, "kings"), None
    if kind == "saints":
        return "saints", None
    return None, None


# ---------- the Bookshelf (bookshelf.html): every work from every reading list, gathered and grouped ----------
SHELF = [  # (id, heading EN, heading CY, the reading lists whose works it takes; the first section to claim a work keeps it)
    ("start", "Start here: the whole story", "Dechrau yma: yr hanes cyfan", ["general", "wales-in-10"]),
    ("britons", "The Britons and Rome", "Y Brythoniaid a Rhufain", ["era-ancient", "era-roman", "celts", "brutus", "caradog", "macsen"]),
    ("kings", "Kings, kingdoms and the Old North", "Brenhinoedd, teyrnasoedd a’r Hen Ogledd", ["era-saints", "era-kings", "kings", "kings-*", "family-trees", "arthur", "arthur-circle", "wilson-blackett", "unconquered"]),
    ("law", "The laws of Hywel Dda", "Cyfreithiau Hywel Dda", ["laws", "hywel", "topic-law"]),
    ("saints", "Saints, learning and faith", "Seintiau, dysg a ffydd", ["christianity", "joseph", "lucius", "patrick", "saints", "saints-*", "learning", "brittany", "topic-faith"]),
    ("princes", "Princes, castles and Owain Glyndŵr", "Tywysogion, cestyll ac Owain Glyndŵr", ["era-medieval", "castles", "glyndwr", "longbow", "battles", "documents", "topic-war", "nest", "rhys"]),
    ("lit", "Poets, old books and legends", "Beirdd, hen lyfrau a chwedlau", ["literature", "books", "triads", "mabinogion", "mabinogi", "mabinogi-tales", "mabinogi-people", "mabinogi-*", "legends", "legend-*", "bran", "symbols", "iolo", "topic-music", "trail-song"]),
    ("tudor", "From the Tudors to the Methodists", "O’r Tuduriaid i’r Methodistiaid", ["era-tudor"]),
    ("industry", "Iron, coal, slate and the sea", "Haearn, glo, llechi a’r môr", ["era-industrial", "industry", "coal", "aberfan", "protest", "topic-industry", "trail-coal", "trail-sea", "firsts", "topic-science"]),
    ("modern", "Modern Wales and the Welsh abroad", "Cymru fodern a’r Cymry ar wasgar", ["era-modern", "era-today", "revival", "mac", "fwa", "world", "madog", "tryweryn", "topic-abroad", "topic-sport"]),
    ("lang", "The Welsh language, names and places", "Yr iaith Gymraeg, enwau a lleoedd", ["language", "welsh-not", "topic-language", "welsh", "names", "towns", "maps", "sites"]),
    ("life", "Women and everyday life", "Menywod a bywyd bob dydd", ["topic-women", "trail-women", "topic-countryside"]),
]


next(g for g in SHELF if g[0] == "lit")[3].extend(["writers", "bruts", "book-*"])  # the writers, the Bruts and the old books (src/writers.py, bruts.py, oldbooks.py)
SHELF_ORDER = ["start", "britons", "kings", "saints", "law", "princes", "tudor", "industry", "modern", "lit", "lang", "life"]  # the order on the page: by period, then the themes


def _shelf_pages():
    """Every reading list, as (key, page it appears on, title EN, title CY)."""
    out = [(x["id"], f'story-{x["id"]}.html', x["en"], x["cy"]) for x in F.STORIES]
    out.append(("wales-in-10", "wales-in-10.html", "Wales in 10 minutes", "Cymru mewn 10 munud"))
    out += [(f'legend-{x["id"]}', f'legend-{x["id"]}.html', x["en"], x["cy"]) for x in F.LEGENDS]
    out += [(f'era-{x["id"]}', f'era-{x["id"]}.html', x["en"], x["cy"]) for x in D.ERAS]
    out += [(f'topic-{t["id"]}', f'topic-{t["id"]}.html', t["en"], t["cy"]) for t in RP.TP.TOPICS]
    out += [(f'trail-{t["id"]}', f'trail-{t["id"]}.html', t["en"], t["cy"]) for t in L.TRAILS]
    named = {"laws": ("The Laws of Hywel Dda", "Cyfreithiau Hywel Dda"), "mabinogion": ("The Mabinogion", "Y Mabinogion"), "kings": ("Kings and princes of Wales", "Brenhinoedd a thywysogion Cymru"),
             "saints": ("Saints of Wales", "Seintiau Cymru"), "literature": ("The literature of Wales", "Llenyddiaeth Cymru"), "books": ("The great books of Wales", "Llyfrau mawr Cymru"),
             "triads": ("The Welsh Triads", "Trioedd Ynys Prydain"), "symbols": ("Symbols and traditions", "Symbolau a thraddodiadau"), "firsts": ("Welsh world firsts", "Cymru oedd y cyntaf"),
             "castles": ("The castles of Wales", "Cestyll Cymru"), "family-trees": ("Royal family trees", "Coed teulu brenhinol"), "battles": ("Battles of Wales", "Brwydrau Cymru"),
             "documents": ("Key documents", "Dogfennau allweddol"), "towns": ("Towns and villages", "Trefi a phentrefi"), "sites": ("Historic sites map", "Map safleoedd hanesyddol"),
             "maps": ("Maps through time", "Mapiau drwy’r oesoedd"), "welsh": ("Learn Welsh", "Dysgu Cymraeg"), "names": ("Welsh names", "Enwau Cymraeg"), "legends": ("Legends", "Chwedlau")}
    out += [(k, f"{k}.html", en, cy) for k, (en, cy) in named.items()]
    out += [(g, "kings.html", "Kings and princes of Wales", "Brenhinoedd a thywysogion Cymru") for g in sorted(set(REF2.KINGS_GROUP.values()))]
    out.append(("saints-llydaw", "saints-llydaw.html", "Saints of Brittany", "Seintiau Llydaw"))
    return out


def bookshelf_old_writers():
    """A box near the top of Books and authors: the old writers of Wales, with links to their pages and the long reads."""
    built = {f'story-{x["id"]}.html' for x in F.STORIES}
    links = [("story-writers.html", "Long read: the writers who recorded early Wales", "Erthygl: yr awduron a gofnododd Gymru gynnar"),
             ("person-gerallt-gymro.html", "Gerald of Wales", "Gerallt Gymro"),
             ("person-nennius.html", "Nennius", "Nennius"),
             ("person-geoffrey-of-monmouth.html", "Geoffrey of Monmouth", "Sieffre o Fynwy"),
             ("story-bruts.html", "The Bruts: the chronicles of Wales", "Y Brutiau: croniclau Cymru"),
             ("books.html", "The old books of Wales", "Hen lyfrau Cymru")]
    btns = " ".join(f'<a class="btn{" solid" if i == 0 else ""}" href="{u}">{bi(a, b)} →</a>' for i, (u, a, b) in enumerate(links) if not u.startswith("story-") or u in built)
    return (f'<div class="old-writers" style="margin:2.4rem 0 2.6rem"><h2 class="sub-h" style="font-size:clamp(1.5rem,3.2vw,2.1rem)">{bi("The first writers of Wales", "Awduron cyntaf Cymru")}</h2>'
            f'<p>{bi("Before the historians came the writers they all rely on: Gildas, Nennius, Asser, Rhygyfarch, Geoffrey of Monmouth, Walter Map, Gerald of Wales and the monks who kept the chronicle of the princes. Each has a page of their own.", "Cyn yr haneswyr daeth yr awduron y mae pob un ohonynt yn dibynnu arnynt: Gildas, Nennius, Asser, Rhygyfarch, Sieffre o Fynwy, Gwallter Map, Gerallt Gymro a’r mynachod a gadwodd gronicl y tywysogion. Mae gan bob un ei dudalen ei hun.")}</p>'
            f'<p class="l-links">{btns}</p></div>')


def bookshelf_page():
    import fnmatch
    lists = {}
    for k, v in list(REF.REFS.items()) + list(REF2.PAGES.items()):
        if v:
            lists[k] = v
    where = {}   # work -> pages that cite it
    for key, href, en, cy in _shelf_pages():
        for it in (lists.get(key) or {}).get("items", []):
            w = where.setdefault((it[1], it[2]), [])
            if href not in [h for h, _, _ in w]:
                w.append((href, en, cy))
    works, taken = {}, set()
    for sid, *_ , keys in SHELF:
        works[sid] = []
        for key in [k for pat in keys for k in lists if fnmatch.fnmatch(k, pat)]:
            for it in lists[key]["items"]:
                wid = (it[1], it[2])
                if it[0] == "w" or wid in taken:
                    continue
                taken.add(wid)
                works[sid].append(it)
    for sid, extra in REF2.SHELF_EXTRA.items():   # more good books that no page lists yet
        for it in extra:
            if (it[1], it[2]) not in taken:
                taken.add((it[1], it[2]))
                works[sid].append(it)
    online, seen = [], set()
    for v in lists.values():
        for it in v["items"]:
            if it[0] == "w" and it[2] not in seen:
                seen.add(it[2])
                online.append(it)
    missing = [k for v in lists.values() for k in [(it[1], it[2]) for it in v["items"]] if k not in taken and k[1] not in seen]
    if missing:
        print("WARNING: bookshelf leaves out", sorted(set(missing))[:5], "- add their list to SHELF in build.py")

    def li(it):
        _, who, title, det, nen, ncy = it[:6]
        url = it[6] if len(it) > 6 else ""
        t = f'<a href="{e(url)}" target="_blank" rel="noopener"><cite>{e(title)}</cite> ↗</a>' if url else f"<cite>{e(title)}</cite>"
        on = where.get((who, title), [])
        more = (f'<span class="ref-on">{bi("On this site:", "Ar y wefan hon:")} ' + ", ".join(f'<a href="{h}">{bi(en, cy)}</a>' for h, en, cy in on[:4])
                + (f' {bi(f"and {len(on) - 4} more", f"a {len(on) - 4} arall")}' if len(on) > 4 else "") + "</span>") if on else ""
        return f'<li id="{bid(it)}"><span class="ref-w">{e(who)}</span>, {t} <span class="ref-d">({e(det)})</span><span class="ref-n">{bi(nen, ncy)}</span>{more}</li>'

    def slug(x, n):
        return re.sub(r"[^a-z0-9]+", "-", x.lower())[:n].strip("-")
    title_n = {}
    for v in list(works.values()) + [online]:
        for it in v:
            title_n[slug(it[2], 48)] = title_n.get(slug(it[2], 48), 0) + 1

    def bid(it):   # one anchor per book; two books with the same title (three Mabinogions) get the author too
        t = slug(it[2], 48)
        return "b-" + t + ("-" + slug(it[1], 24) if title_n[t] > 1 else "")

    def group(items):
        out = ""
        for kind, en, cy in REF_KINDS:
            xs = [it for it in items if it[0] == kind]
            if xs:
                out += f'<h3>{bi(en, cy)}</h3><ul>{"".join(li(it) for it in xs)}</ul>'
        return out

    total = sum(len(v) for v in works.values())
    shelf_items = [(sid, it) for sid in works for it in works[sid]]
    order = [x[0] for x in sorted(SHELF, key=lambda x: SHELF_ORDER.index(x[0]))]
    cards = {sid: [] for sid in order}
    for a in AU.AUTHORS:
        mine = [(sid, it) for sid, it in shelf_items if any(m in it[1] for m in a["match"])]
        if not mine:
            print(f"WARNING: author {a['name']} has no books on the shelf")
            continue
        home = a.get("shelf") or max(order, key=lambda sid: (sum(1 for s2, _ in mine if s2 == sid), -order.index(sid)))
        nm = f'<a href="{a["link"]}">{e(a["name"])}</a>' if a["link"] else e(a["name"])
        books = "".join(f'<li><a href="#{bid(it)}"><cite>{e(it[2])}</cite></a></li>' for _, it in mine)
        cards[home].append(f'<article class="author" id="a-{a["id"]}"><h3>{nm}</h3>' + (f'<p class="au-d">{e(a["dates"])}</p>' if a["dates"] else "")
                           + f'<p>{bi(a["en"], a["cy"])}</p><p class="au-b">{bi("Their books here", "Eu llyfrau yma")}</p><ul>{books}</ul></article>')
    n_auth = sum(len(v) for v in cards.values())
    heads = {sid: (en, cy) for sid, en, cy, _ in SHELF}

    def shelf_sec(sid):
        en, cy = heads[sid]
        au = (f'<h3 class="shelf-sub">{bi("The authors", "Yr awduron")}</h3><div class="author-grid">{"".join(cards[sid])}</div>' if cards[sid] else "")
        return (f'<section class="refs shelf" id="{sid}" aria-labelledby="h-{sid}"><h2 id="h-{sid}">{bi(en, cy)}</h2>{au}'
                + f'{group(works[sid])}</section>')
    # Y Lolfa, the Talybont press (src/ylolfa.py): every book on the shelf with a ylolfa.com link, each pointing to its place below
    yl = [(sid, it) for sid in order for it in works[sid] if len(it) > 6 and "ylolfa.com/" in it[6]]
    yl_lis = "".join(f'<li><span class="ref-w">{e(it[1])}</span>, <a href="{e(it[6])}" target="_blank" rel="noopener"><cite>{e(it[2])}</cite> ↗</a> '
                     f'<span class="ref-d">({e(it[3])})</span><span class="ref-n">{bi(it[4], it[5])}</span>'
                     f'<span class="ref-on">{bi("On this page:", "Ar y dudalen hon:")} <a href="#{bid(it)}">{bi(*heads[sid])}</a></span></li>' for sid, it in yl)
    yl_sec = (f'<section class="refs shelf" id="ylolfa" aria-labelledby="h-ylolfa"><h2 id="h-ylolfa">{bi(*YLF.SECTION)}</h2>'
              f'<p class="refs-i">{bi(*YLF.INTRO)}</p><p><a class="btn" href="https://www.ylolfa.com/" target="_blank" rel="noopener">ylolfa.com ↗</a></p>'
              f'<h3>{bi(f"{len(yl)} books from Y Lolfa on this page", f"{len(yl)} o lyfrau’r Lolfa ar y dudalen hon")}</h3><ul>{yl_lis}</ul></section>') if yl else ""
    yl_chip = f'<a class="chip" href="#ylolfa">{bi("Y Lolfa", "Y Lolfa")}</a>' if yl else ""
    chips = "".join(f'<a class="chip" href="#{sid}">{bi(*heads[sid])}</a>' + (yl_chip if sid == "start" else "") for sid in order if works[sid]) + f'<a class="chip" href="#online">{bi("Online", "Ar-lein")}</a>'
    body = "".join(shelf_sec(sid) + (yl_sec if sid == "start" else "") for sid in order if works[sid])
    body += f'<section class="refs shelf" id="online" aria-labelledby="h-online"><h2 id="h-online">{bi("Online", "Ar-lein")}</h2>{group(online)}</section>'
    intro = bi(f"{n_auth} writers who told the story of Wales and {total} books and old texts, from the Britons to today, grouped by period. In each period you meet the authors first, then their books. Under a book you will find the pages of this site that use it. Any library in Wales can find them for you.",
               f"{n_auth} o awduron a adroddodd stori Cymru a {total} o lyfrau a hen destunau, o’r Brythoniaid hyd heddiw, wedi’u trefnu fesul cyfnod. Ym mhob cyfnod fe gwrddwch â’r awduron yn gyntaf, ac yna eu llyfrau. O dan lyfr fe welwch dudalennau’r wefan hon sy’n ei ddefnyddio. Gall unrhyw lyfrgell yng Nghymru eu cael i chi.")
    main = (hero("tudor", f'<a href="index.html">{SITE}</a>', "book", "Books and authors", "Llyfrau ac awduron", "Books and authors of Welsh history", "Llyfrau ac awduron hanes Cymru",
                 "The old sources and the historians’ books behind this site, chosen to read next.", "Yr hen ffynonellau a llyfrau’r haneswyr y tu ôl i’r wefan hon, i’w darllen nesaf.", art="book")
            + section(f'<div class="narrow"><p class="lede">{intro}</p>{bookshelf_old_writers()}<nav class="chips shelf-chips" aria-label="{bi("Sections", "Adrannau", "span")}">{chips}</nav>{body}</div>', top=True))
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Books and authors of Welsh history", "inLanguage": ["en", "cy"],
          "hasPart": [{"@type": "Book" if it[0] == "b" else "CreativeWork", "name": it[2], "author": it[1]} for v in works.values() for it in v]}
    return page("books-and-authors.html", "Books and authors of Welsh history · History of Wales",
                f"Every book and old source in the reading lists of History of Wales, {total} in all, from John Davies and R. R. Davies to the Mabinogion and the laws of Hywel Dda.", main, era="tudor", ld=ld, track="books-and-authors")


def refs_ld(key):
    """The same list for search engines: schema.org citation entries."""
    r = REF.REFS.get(key) or REF2.PAGES.get(key) or {}
    return [{"@type": "CreativeWork", "name": it[2], "author": it[1]} for it in r.get("items", []) if it[0] in "pb"]


def story_page(x, i):
    nxt = F.STORIES[(i + 1) % len(F.STORIES)]
    others = [y for y in F.STORIES if y["id"] != x["id"]][:3]
    era = ERA[x["era"]]
    meta = f'<p class="byline">{AB.byline_top()}<span>{x["mins"]} {bi("minute read", "munud o ddarllen")}</span><a href="era-{x["era"]}.html">{bi(era["en"], era["cy"])}</a><button type="button" class="copy" data-copy="story-{x["id"]}.html">{bi("Copy link", "Copïo’r ddolen")}</button></p>'
    main = (hero(x["era"], f'<a href="index.html">{SITE}</a> / <a href="stories.html">{bi("Long reads", "Erthyglau")}</a>', "book", "Long read", "Erthygl", x["en"], x["cy"], x["sumEn"], x["sumCy"], art=x["art"])
            + f'<section class="article"><div class="wrap narrow">{meta}{prose_bi(x["pEn"], x["pCy"], figs=x.get("figs"))}' + (f'<p><a class="btn solid" href="firsts.html">★ {bi("Every Welsh world first, with the people behind them", "Pob un o’r pethau a wnaeth Cymru gyntaf, a’r bobl y tu ôl iddynt")} →</a></p>' if x["id"] == "firsts" else "")
              + story_more_links(x)
              + (f'<p><a class="btn solid" href="laws.html">{bi("Much more on the law: the big page on the Laws of Hywel Dda, with the manuscripts and a quiz", "Llawer mwy am y gyfraith: y dudalen fawr ar Gyfreithiau Hywel Dda, gyda’r llawysgrifau a chwis")} →</a></p>' if x["id"] == "hywel" else "") + refs_block(x["id"]) + '</div></section>'
            + (section(f'<div class="mb-figs">{"".join(lit_fig(f) for f in x["figs"])}</div>', "Pictures", "Lluniau") if x.get("figs") else "")
            + section(f'<div class="s-grid three">{"".join(story_card(y) for y in others)}</div>', "Keep reading", "Daliwch ati i ddarllen")
            + section(f'<div class="pager"><a class="btn" href="stories.html">← {bi("All long reads", "Pob erthygl")}</a><a class="btn solid" href="story-{nxt["id"]}.html">{bi(nxt["en"], nxt["cy"])} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": x["en"], "description": x["sumEn"], "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    if refs_ld(x["id"]):
        ld["citation"] = refs_ld(x["id"])
    return page(f"story-{x['id']}.html", f'{x["en"]} · History of Wales', x["sumEn"], main, era=x["era"], ld=ld, active="stories.html", track=f"story:{x['id']}")


def stories_index():
    main = (hero("kings", f'<a href="index.html">{SITE}</a>', "book", "Long reads", "Erthyglau", "The stories behind the dates", "Y straeon y tu ôl i’r dyddiadau",
                 "Short essays on the big questions of Welsh history. Each takes about five minutes.", "Erthyglau byr ar gwestiynau mawr hanes Cymru. Tua phum munud yr un.", art="book")
            + section(f'<h2 class="sr-only">{bi("All long reads", "Pob erthygl")}</h2><div class="s-grid">{"".join(story_card(x, k == 0) for k, x in enumerate(F.STORIES))}</div>', top=True))
    return page("stories.html", "Long reads · History of Wales", "Essays on Welsh history: castles, the language, the laws of Hywel Dda, coal, protest and the Welsh across the world.", main, era="kings", og_type="website", active="stories.html")


def legend_credit(art):
    ph = A.LEGEND_PHOTOS.get(art)
    if not ph:
        return ""
    return (f'<p class="ph-credit">{bi("Picture", "Llun")}: {bi(ph[4], ph[5])}. {bi("Photo", "Ffotograff")}: <a href="{COMMONS}File:{_q(ph[0].replace(" ", "_"), safe="")}" rel="noopener">{e(ph[1])}</a>, '
            f'<a href="{ph[3]}" rel="noopener license">{ph[2]}</a>, Wikimedia Commons.</p>')


def legend_page(x, i):
    nxt = F.LEGENDS[(i + 1) % len(F.LEGENDS)]
    main = (hero(x["era"], f'<a href="index.html">{SITE}</a> / <a href="legends.html">{bi("Legends", "Chwedlau")}</a>', "book", x["place"], x["place"], x["en"], x["cy"], x["sumEn"], x["sumCy"], art=x["art"], photo=True)
            + f'<section class="article"><div class="wrap narrow">{prose_bi(x["pEn"], x["pCy"], "prose tale")}'
              f'<div class="behind"><p class="eyebrow">{bi(x.get("hLabelEn", "The history behind the legend"), x.get("hLabelCy", "Yr hanes y tu ôl i’r chwedl"))}</p><p>{bi(x["hEn"], x["hCy"])}</p></div>'
              + (f'<p class="l-links">' + "".join(f'<a class="btn" href="{h}">{bi(en, cy)} →</a>' for h, en, cy in x["links"]) + '</p>' if x.get("links") else "") +
              f'<p class="byline"><button type="button" class="copy" data-copy="legend-{x["id"]}.html">{bi("Copy link to share", "Copïo dolen i’w rhannu")}</button></p>{legend_credit(x["art"])}</div></section>'
            + set_block(f"legend:{x['id']}")
            + section(f'<div class="pager"><a class="btn" href="legends.html">← {bi("All legends", "Pob chwedl")}</a><a class="btn solid" href="legend-{nxt["id"]}.html">{bi(nxt["en"], nxt["cy"])} →</a></div>'))
    return page(f"legend-{x['id']}.html", f'{x["en"]} · History of Wales', x["sumEn"], main, era=x["era"], active="legends.html", track=f"legend:{x['id']}")


def legends_index():
    main = (hero("medieval", f'<a href="index.html">{SITE}</a>', "book", "Legends", "Chwedlau", "Legends of Wales", "Chwedlau Cymru",
                 f"{len(F.LEGENDS)} old tales, retold for reading aloud, each with the real history behind it.", f"{len(F.LEGENDS)} o hen chwedlau, wedi’u hadrodd o’r newydd i’w darllen ar goedd, pob un â’r hanes go iawn y tu ôl iddi.", art="dragons",
                 extra='<nav class="chips l-jump" aria-label="Sections / Adrannau">' + "".join(f'<a class="chip" href="#{g["ids"][0]}-set">{bi(g["en"], g["cy"])}</a>' for g in F.LEGEND_GROUPS) + '</nav>')
            + (section(just_added("legend", F.LEGENDS, lambda x: f'legend-{x["id"]}.html', lambda x: (x["en"], x["cy"]), h_en="Newest legends", h_cy="Y chwedlau diweddaraf"), top=True) if AD.recent("legend", F.LEGENDS) else "")
            + "".join(f'<section{"" if k == 0 else " class=\"tight\""} id="{g["ids"][0]}-set"><div class="wrap"><h2 class="sub-h">{bi(g["en"], g["cy"])}</h2><p class="l-sum">{bi(g["sumEn"], g["sumCy"])}</p>'
                      f'<div class="l-grid">{"".join(legend_card(x) for x in g["items"])}</div>'
                      + (f'<p class="l-links"><a class="btn" href="mabinogion.html">{bi("About the Mabinogion: the books, the translation and all eleven tales", "Am y Mabinogion: y llyfrau, y cyfieithiad a’r un chwedl ar ddeg")} →</a></p>' if g["ids"][0] == "pwyll" else "")
                      + (f'<p class="l-links"><a class="btn" href="story-brutus.html">{bi("Lludd, Macsen and the kings of the Brut: the story of Brutus of Troy, father of the Britons", "Lludd, Macsen a brenhinoedd y Brut: stori Brutus o Gaerdroea, tad y Brythoniaid")} →</a></p>' if g["ids"][0] == "dragons" else "")
                      + '</div></section>' for k, g in enumerate(F.LEGEND_GROUPS))
            + section(f'<div class="pager"><a class="btn" href="symbols.html">{bi("Symbols and traditions", "Symbolau a thraddodiadau")} →</a></div>'))
    return page("legends.html", "Legends · History of Wales", "The legends of Wales retold: the tales of King Arthur, the red dragon, Gelert, the Four Branches of the Mabinogi, Macsen Wledig, Culhwch and Olwen, Dwynwen, Melangell, the Tylwyth Teg and more, with the history behind them.", main, era="medieval", og_type="website", active="legends.html")


MT_BY_CY = {t["cy"]: t for t in MT.TALES}


def mabinogion_page():
    # src/mabinogion.py: the eleven tales, the White Book and the Red Book, Lady Charlotte Guest
    def tale(t, era):
        g = MT_BY_CY.get(t["cy"])
        main = f'mabinogi-{g["id"]}.html' if g else t["link"]
        go = f'<a class="wl" href="{main}">{e(t["cy"])}</a>' if main else ""
        go += (f'<a class="btn" href="{t["link"]}">{bi("Read it retold", "Darllen y chwedl")} →</a>' if g and t["link"] else "")
        return (f'<article class="mab-tale rv{" wl-card" if main else ""}" data-era="{era}"><h3 lang="cy">{e(t["cy"])}</h3><p class="mab-en l-en" lang="en">{e(t["en"])}</p>'
                f'<p>{bi(t["sumEn"], t["sumCy"])}</p>{go}</article>')
    groups = "".join(f'<section class="tight" id="mab-{k + 1}"><div class="wrap"><h2 class="sub-h">{bi(g["en"], g["cy"])}</h2><p class="l-sum">{bi(g["sumEn"], g["sumCy"])}</p>'
                     f'<div class="mab-grid">{"".join(tale(t, g["era"]) for t in g["tales"])}</div></div></section>' for k, g in enumerate(MB.GROUPS))
    jump = '<nav class="chips l-jump" aria-label="Sections / Adrannau">' + "".join(f'<a class="chip" href="#mab-{k + 1}">{bi(g["en"], g["cy"])}</a>' for k, g in enumerate(MB.GROUPS)) + '</nav>'
    main = (hero("medieval", f'<a href="index.html">{SITE}</a> / <a href="legends.html">{bi("Legends", "Chwedlau")}</a>', "book", "Eleven tales", "Un chwedl ar ddeg", "The Mabinogion", "Y Mabinogion",
                 "The great tales of medieval Wales: the Four Branches of the Mabinogi, the native tales and the three romances, kept for six hundred years in the White Book and the Red Book.",
                 "Chwedlau mawr Cymru’r Oesoedd Canol: Pedair Cainc y Mabinogi, y chwedlau brodorol a’r tair rhamant, a gadwyd am chwe chan mlynedd yn y Llyfr Gwyn a’r Llyfr Coch.", art="book", extra=jump)
            + f'<section class="article"><div class="wrap narrow">{prose_bi(MB.INTRO_EN, MB.INTRO_CY)}'
              f'<p class="l-links"><a class="btn solid" href="story-mabinogi.html">{bi("Long read: the books that kept the tales, and the woman who translated them", "Erthygl: y llyfrau a gadwodd y chwedlau, a’r wraig a’u cyfieithodd")} →</a> '
              f'<a class="btn" href="person-arthur.html">{bi("Arthur, King of the Britons", "Arthur, Brenin y Brythoniaid")} →</a> '
              f'<a class="btn" href="books.html#white">{bi("The White Book and the Red Book", "Y Llyfr Gwyn a’r Llyfr Coch")} →</a> '
              f'<a class="btn" href="triads.html">{bi("The Welsh Triads", "Trioedd Ynys Prydain")} →</a></p></div></section>'
            + groups
            + section("".join(f'<h3 class="sub-h">{bi(en, cy)}</h3><div class="ppl">{"".join(lit_person_chip(s) for s in ids)}</div>' for en, cy, ids in MP.GROUPS).join(['<div class="ar-circle">', '</div>']), "People of the Mabinogi", "Pobl y Mabinogi")
            + section(f'<div class="pager"><a class="btn" href="legends.html">← {bi("All legends", "Pob chwedl")}</a><a class="btn solid" href="mabinogi-pwyll.html">{bi("Begin with the First Branch", "Dechrau â’r Gainc Gyntaf")} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": "The Mabinogion", "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page("mabinogion.html", "The Mabinogion · History of Wales", "The Mabinogion: the eleven great tales of medieval Wales, the White Book of Rhydderch and the Red Book of Hergest, and Lady Charlotte Guest’s translation, in English and Cymraeg.",
                main, era="medieval", ld=ld, active="legends.html", track="page:mabinogion")


# ---------- the Laws of Hywel Dda (laws.html): text, pictures, worth table, quiz and words in src/laws.py ----------
def law_fig(key, cls="", w=1200):
    f, by, lic, licu, cen, ccy = LW.FIGS[key]
    return (f'<figure class="lw-fig {cls}"><img src="{photo_url(f, w)}" alt="{e(cen)}" loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.closest(\'figure\').remove()">'
            f'<figcaption>{bi(cen, ccy)}<span class="lw-cr">{bi("Picture", "Llun")}: {e(by)} · <a href="{licu}" target="_blank" rel="noopener license">{e(lic)}</a> · '
            f'<a href="{COMMONS}File:{_q(f.replace(" ", "_"), safe="")}" target="_blank" rel="noopener">Wikimedia Commons</a></span></figcaption></figure>')


MARGIN_ART = [("F. 24r. Dragon with a fish tail.jpg", "A dragon with a fish’s tail", "Draig â chynffon pysgodyn"),
              ("F. 24v. Mermaid.jpg", "A mermaid", "Môr-forwyn"),
              ("F. 29r. Winged lion (symbol of Mark's Gospel.jpg", "A winged lion", "Llew asgellog"),
              ("F. 40r. Peacock.jpg", "A peacock", "Paun"),
              ("F. 65r. Dragon.jpg", "A dragon’s head", "Pen draig"),
              ("F. 71r. Man with spear.jpg", "A man with a spear", "Gŵr â gwaywffon")]

LAW_MSS = [("king", "Peniarth 28", "Latin · about 1250", "Lladin · tua 1250"),
           ("chirk", "Peniarth 29 · Llyfr Du’r Waun", "Welsh · about 1250 · the law of Gwynedd", "Cymraeg · tua 1250 · cyfraith Gwynedd"),
           ("welsh29", "NLW MS 20143A", "Welsh · fourteenth century · in its medieval wooden boards", "Cymraeg · y bedwaredd ganrif ar ddeg · yn ei chloriau pren canoloesol"),
           ("boston", "NLW MS 24029A · Llawysgrif Boston", "Welsh · fourteenth century · Llyfr Blegywryd", "Cymraeg · y bedwaredd ganrif ar ddeg · Llyfr Blegywryd"),
           ("pen38", "Peniarth 38", "Welsh · a lawyer’s copy", "Cymraeg · copi cyfreithiwr"),
           ("pen36", "Peniarth 36", "Welsh · a lawyer’s copy", "Cymraeg · copi cyfreithiwr")]


def laws_page():
    def prose_at(ch, cut_en, cut_cy, extra):
        # the chapter's paragraphs, with `extra` placed after the paragraph that ends with cut_en / cut_cy (or at the end)
        def cut(ps, mark):
            k = next((i + 1 for i, a in enumerate(ps) if mark and a.endswith(mark)), len(ps))
            return ps[:k], ps[k:]
        a1, a2 = cut(ch["pEn"], cut_en)
        b1, b2 = cut(ch["pCy"], cut_cy)
        return prose_bi(a1, b1) + extra + (prose_bi(a2, b2) if a2 or b2 else "")

    def books():
        return '<div class="lw-books">' + "".join(
            f'<article class="lw-book rv"><p class="eyebrow">{bi(b["whereEn"], b["whereCy"])}</p><h3 lang="cy">{e(b["cy"])}</h3><p class="lw-sub l-en" lang="en">{e(b["en"])}</p><p>{bi(b["tEn"], b["tCy"])}</p></article>'
            for b in LW.BOOKS) + "</div>"

    def officers():
        return ('<div class="lw-officers">' + "".join(f'<div class="lw-off rv"><b lang="cy">{e(n)}</b><span>{bi(en, cy)}</span></div>' for n, en, cy in LW.OFFICERS)
                + "</div>")

    def split():
        head, rows = LW.SPLIT[0], LW.SPLIT[1:]
        th = f'<thead><tr><th scope="col">{bi(head[0], head[2])}</th><th scope="col">{bi(head[1], head[3])}</th></tr></thead>'
        return (f'<table class="lw-split">{th}<tbody>' + "".join(f'<tr><td>{bi(r[0], r[2])}</td><td>{bi(r[1], r[3])}</td></tr>' for r in rows) + "</tbody></table>")

    def worth():
        chips = (f'<div class="chips lw-wchips" role="group" aria-label="Show / Dangos"><button type="button" class="chip on" data-g="all" aria-pressed="true">{bi("Everything", "Popeth")}</button>'
                 + "".join(f'<button type="button" class="chip" data-g="{k}" aria-pressed="false">{bi(g[0], g[1])}</button>' for k, g in enumerate(LW.WORTH)) + "</div>")
        rows = "".join(f'<tr data-g="{k}"><th scope="row">{bi(r[0], r[1])}</th><td>{bi(r[2], r[3])}</td></tr>' for k, g in enumerate(LW.WORTH) for r in g[2])
        note = bi("A penny was a silver penny. A ‘small penny’ was a lesser coin. Cows were the great measure of wealth: a pound was 240 pence.",
                  "Ceiniog arian oedd ceiniog. Darn llai oedd ‘ceiniog cwta’. Gwartheg oedd mesur mawr cyfoeth: roedd punt yn 240 ceiniog.")
        return (f'<div class="lw-worth" id="worth-table"><h3>{bi("Hywel’s price list", "Rhestr brisiau Hywel")}</h3>{chips}'
                f'<table class="lw-wt"><thead><tr><th scope="col">{bi("What", "Beth")}</th><th scope="col">{bi("Its worth in law", "Ei werth yn y gyfraith")}</th></tr></thead><tbody>{rows}</tbody></table>'
                f'<p class="lw-note">{note}</p></div>')

    def gallery():
        cards = "".join(f'<div class="lw-ms rv">{law_fig(key, "lw-ms-fig", 960)}<p class="lw-ms-t"><b>{e(t)}</b><span>{bi(en, cy)}</span></p></div>' for key, t, en, cy in LAW_MSS)
        art = "".join(f'<figure class="lw-mart"><img src="{photo_url(f, 640)}" alt="{e(en)}" loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.closest(\'figure\').remove()">'
                      f'<figcaption>{bi(en, cy)}</figcaption></figure>' for f, en, cy in MARGIN_ART)
        return (f'</div><div class="wrap"><div class="lw-mss">{cards}</div>'
                f'<h3 class="lw-h3">{bi("Pictures in the margins", "Lluniau ar yr ymylon")}</h3>'
                f'<p class="lw-lede">{bi("The scribe of NLW MS 20143A filled the bottom of his pages with creatures in red and green ink, drawn beside the laws they decorate.", "Llanwodd ysgrifydd NLW MS 20143A waelod ei dudalennau â chreaduriaid mewn inc coch a gwyrdd, wedi’u tynnu wrth ymyl y cyfreithiau a addurnant.")}</p>'
                f'<div class="lw-marts">{art}</div><p class="lw-cr">{bi("Pictures", "Lluniau")}: {e(NLW_CREDIT)}, <a href="https://creativecommons.org/publicdomain/zero/1.0/" target="_blank" rel="noopener license">CC0</a>, '
                f'<a href="{COMMONS}Category:NLW_MS_20143A" target="_blank" rel="noopener">Wikimedia Commons</a></p></div><div class="wrap narrow">')

    def chapter(ch, n):
        figs = "".join(law_fig(k, "side" if len(ch["figs"]) > 1 else "") for k in ch["figs"])
        figs = f'<div class="lw-figs n{len(ch["figs"])}">{figs}</div>' if ch["figs"] else ""
        if ch.get("split"):
            body = prose_at(ch, "item by item:", "fesul eitem:", split())
        else:
            extra = (books() if ch.get("books") else "") + (officers() if ch.get("officers") else "") + (worth() if ch.get("worth") else "") + (gallery() if ch.get("gallery") else "")
            body = prose_bi(ch["pEn"], ch["pCy"]) + extra
        return (f'<section class="article lw-ch" id="{ch["id"]}"><div class="wrap narrow"><p class="lw-n">{n:02d}</p><h2 class="lw-h">{bi(ch["en"], ch["cy"])}</h2>'
                f'{figs}{body}</div></section>')

    def dates():
        def ycy(y):
            fixed = {"late 1100s": "diwedd y 1100au", "early 1200s": "dechrau’r 1200au", "1300s and 1400s": "y 1300au a’r 1400au"}
            return fixed.get(y) or y.replace("about ", "tua ").replace(" to ", " i ").replace(" and ", " a ")
        return ('<ol class="lw-dates">' + "".join(f'<li class="rv"><b>{bi(y, ycy(y))}</b><span>{bi(en, cy)}</span></li>' for y, en, cy in LW.DATES) + "</ol>")

    def quiz():
        qs = ""
        for k, (qen, qcy, ans, ok, wen, wcy) in enumerate(LW.QUIZ):
            btns = "".join(f'<button type="button" class="lw-a" data-ok="{1 if j == ok else 0}">{bi(a, b)}</button>' for j, (a, b) in enumerate(ans))
            qs += (f'<div class="lw-q" data-q="{k}"{"" if k == 0 else " hidden"}><p class="eyebrow">{bi(f"Case {k + 1} of {len(LW.QUIZ)}", f"Achos {k + 1} o {len(LW.QUIZ)}")}</p>'
                   f'<h3>{bi(qen, qcy)}</h3><div class="lw-as">{btns}</div><p class="lw-why" hidden>{bi(wen, wcy)}</p>'
                   f'<button type="button" class="btn solid lw-next" hidden>{bi("Next case", "Yr achos nesaf")} →</button></div>')
        end = (f'<div class="lw-end" hidden><p class="eyebrow">{bi("Your verdict", "Eich dyfarniad")}</p><p class="lw-score"><span class="lw-s">0</span> / {len(LW.QUIZ)}</p>'
               f'<p class="lw-rank"></p><button type="button" class="btn lw-again">{bi("Judge again", "Barnu eto")}</button></div>')
        return f'<div class="lw-quiz" id="quiz-box">{qs}{end}</div>'

    def words():
        return ('<dl class="lw-words">' + "".join(f'<div class="rv"><dt><span lang="cy">{e(w)}</span>{hear_btn(w, g)}</dt><dd>{bi(en, cy)}<span class="lw-say">{e(g)}</span></dd></div>'
                                            for w, en, cy, g in LW.WORDS) + "</dl>")

    jump = ('<nav class="chips l-jump" aria-label="Chapters / Penodau">' + "".join(f'<a class="chip" href="#{c["id"]}">{bi(c["en"], c["cy"])}</a>' for c in LW.CHAPTERS)
            + f'<a class="chip" href="#quiz">{bi("Quiz", "Cwis")}</a><a class="chip" href="#words">{bi("Words of the law", "Geiriau’r gyfraith")}</a></nav>')
    main = (hero("kings", f'<a href="index.html">{SITE}</a> / <a href="kings.html">{bi("Kings and princes", "Brenhinoedd a thywysogion")}</a>', "book", "Cyfraith Hywel", "Cyfraith Hywel",
                 "The Laws of Hywel Dda", "Cyfreithiau Hywel Dda",
                 "The law that held Wales together for six hundred years: made at Whitland, carried in the books of the lawyers, fair to women, merciful to the hungry, and built on making peace.",
                 "Y gyfraith a ddaliodd Gymru ynghyd am chwe chan mlynedd: wedi’i llunio yn Hendy-gwyn, wedi’i chario yn llyfrau’r cyfreithwyr, yn deg i fenywod, yn drugarog wrth y newynog, ac wedi’i hadeiladu ar wneud heddwch.",
                 art="book", extra=jump)
            + f'<section class="article lw-top"><div class="wrap narrow">{law_fig("kingc", "lead")}{prose_bi(LW.FACTS_EN, LW.FACTS_CY)}{prose_bi(LW.INTRO_EN, LW.INTRO_CY)}'
              f'<p class="l-links"><a class="btn" href="story-hywel.html">{bi("Hywel’s own story: the long read", "Stori Hywel ei hun: yr erthygl")} →</a> <a class="btn" href="person-hywel-dda.html">{bi("Hywel Dda", "Hywel Dda")} →</a> '
              f'<a class="btn" href="place-hendygwyn.html">{bi("Whitland", "Hendy-gwyn ar Daf")} →</a></p></div></section>'
            + section(dates(), "The law in dates", "Y gyfraith mewn dyddiadau")
            + "".join(chapter(c, n + 1) for n, c in enumerate(LW.CHAPTERS))
            + f'<section class="tight lw-quiz-sec" id="quiz"><div class="wrap narrow"><h2 class="sub-h">{bi("What would Hywel’s law say?", "Beth fyddai cyfraith Hywel yn ei ddweud?")}</h2>'
              f'<p class="lw-lede">{bi("You are the judge. Twelve cases from the lawbooks: choose the judgement the law of Hywel would give.", "Chi yw’r ynad. Deuddeg achos o’r llyfrau cyfraith: dewiswch y dyfarniad a roddai cyfraith Hywel.")}</p>{quiz()}</div></section>'
            + f'<section class="tight" id="words"><div class="wrap"><h2 class="sub-h">{bi("Words of the law", "Geiriau’r gyfraith")}</h2>'
              f'<p class="lw-lede">{bi("The Welsh words the lawyers used. Tap the speaker to hear each one.", "Y geiriau Cymraeg a ddefnyddiai’r cyfreithwyr. Tapiwch y seinydd i glywed pob un.")}</p>{words()}</div></section>'
            + section(f'<p class="note-box">{bi(LW.SOURCES_EN, LW.SOURCES_CY)}</p>' + set_block("page:laws")
                      + f'<div class="pager" style="margin-top:2rem"><a class="btn" href="story-hywel.html">← {bi("Hywel Dda and the laws of Wales", "Hywel Dda a chyfraith Cymru")}</a><a class="btn solid" href="kings.html">{bi("Kings and princes of Wales", "Brenhinoedd a thywysogion Cymru")} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": "The Laws of Hywel Dda", "alternativeHeadline": "Cyfraith Hywel", "inLanguage": ["en", "cy"],
          "image": f"{COMMONS}Special:FilePath/{_q(LW.FIGS['kingc'][0], safe='')}", "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page("laws.html", "The Laws of Hywel Dda · History of Wales",
                "The Laws of Hywel Dda, Cyfraith Hywel: the gathering at Whitland, the three lawbooks, galanas and sarhaed, the king’s court, women and marriage, land, the worth of everything, the manuscripts and their pictures, and a quiz.",
                main, era="kings", ld=ld, active="kings.html", track="page:laws", extra=LAWS_JS + WELSH_SCRIPT)


NLW_CREDIT = "Unknown scribe, National Library of Wales (NLW MS 20143A)"
LAWS_JS = r"""<script>(function(){
var c=document.querySelector(".lw-wchips");if(c){c.onclick=function(ev){var b=ev.target.closest("button");if(!b)return;var g=b.dataset.g;
[].forEach.call(c.querySelectorAll("button"),function(x){var on=x===b;x.classList.toggle("on",on);x.setAttribute("aria-pressed",on)});
[].forEach.call(document.querySelectorAll(".lw-wt tbody tr"),function(r){r.hidden=g!=="all"&&r.dataset.g!==g})}}
var box=document.getElementById("quiz-box");if(!box)return;var qs=box.querySelectorAll(".lw-q"),end=box.querySelector(".lw-end"),score=0;
function cy(){return document.documentElement.classList.contains("cy")}
box.onclick=function(ev){var a=ev.target.closest(".lw-a"),q=ev.target.closest(".lw-q");
if(a&&q&&!q.dataset.done){q.dataset.done=1;var ok=a.dataset.ok==="1";if(ok)score++;a.classList.add(ok?"right":"wrong");
[].forEach.call(q.querySelectorAll(".lw-a"),function(x){x.disabled=true;if(x.dataset.ok==="1")x.classList.add("right")});
q.querySelector(".lw-why").hidden=false;q.querySelector(".lw-next").hidden=false;q.querySelector(".lw-next").focus();return}
if(ev.target.closest(".lw-next")&&q){q.hidden=true;var n=q.nextElementSibling;if(n&&n.classList.contains("lw-q")){n.hidden=false;n.querySelector(".lw-a").focus()}else{
end.hidden=false;end.querySelector(".lw-s").textContent=score;var r=score>=11?["A master of law, worthy of Blegywryd himself.","Athro yn y gyfraith, yn deilwng o Flegywryd ei hun."]:score>=8?["A judge of the king’s court. Hywel would give you the gaming board.","Ynad llys y brenin. Byddai Hywel yn rhoi’r bwrdd chwarae i chi."]:score>=5?["A good landowner of the south: you may sit with the judges.","Tirfeddiannwr da o’r de: cewch eistedd gyda’r ynadon."]:["Keep studying the Test Book before you judge again!","Daliwch ati i astudio Llyfr Prawf Ynad cyn barnu eto!"];
end.querySelector(".lw-rank").innerHTML='<span class="l-en" lang="en">'+r[0]+'</span><span class="l-cy" lang="cy">'+r[1]+'</span>';end.querySelector(".lw-again").focus();
try{if(window.goatcounter&&goatcounter.count)goatcounter.count({path:"quiz-laws-"+score,title:"Laws quiz score",event:true})}catch(e){}}return}
if(ev.target.closest(".lw-again")){score=0;end.hidden=true;[].forEach.call(qs,function(x,k){x.hidden=k>0;delete x.dataset.done;x.querySelector(".lw-why").hidden=true;x.querySelector(".lw-next").hidden=true;
[].forEach.call(x.querySelectorAll(".lw-a"),function(b){b.disabled=false;b.classList.remove("right","wrong")})});qs[0].querySelector(".lw-a").focus()}}})()</script>
"""


# ---------- the literature of Wales: literature.html, books.html, triads.html (src/literature.py) ----------
LIT_CSS = """
.lit-doors{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,15rem),1fr));gap:1rem;margin-top:1.6rem}
.lit-door{display:grid;grid-template-rows:auto 1fr;background:var(--slate);border:1px solid var(--line);border-radius:12px;overflow:hidden;text-decoration:none;color:inherit;transition:border-color .2s,transform .2s}
.lit-door:hover{border-color:var(--gold,#d4a72c);transform:translateY(-2px)}
.lit-door img{width:100%;height:9.5rem;object-fit:cover;display:block;background:#11151f}
.lit-door span.t{display:grid;gap:.35rem;padding:1rem 1.1rem 1.2rem}
.lit-door b{font-family:var(--f-display,inherit);font-size:1.35rem;line-height:1.15}
.lit-door small{color:var(--muted);font-size:.92rem}
.lit-age{display:grid;gap:2rem;align-items:start}
@media (min-width:60rem){.lit-age{grid-template-columns:minmax(0,1.5fr) minmax(0,1fr)}.lit-age .lit-side{position:sticky;top:5.5rem}}
.lit-age .span{font-family:var(--f-mono);font-size:.8rem;color:var(--c);letter-spacing:.06em}
.lit-age h2{margin:.2rem 0 1rem}
.lit-side figure.photo{margin:0}
.lit-side figure.photo img{width:100%;height:auto;max-height:34rem;object-fit:contain;background:#0d1018;border-radius:10px}
.lit-people{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1rem}
.lit-people a{display:inline-flex;align-items:center;gap:.5rem;padding:.3rem .8rem .3rem .3rem;border:1px solid var(--line);border-radius:999px;text-decoration:none;color:inherit;font-size:.92rem;background:var(--slate)}
.lit-people a:hover{border-color:var(--c)}
.lit-people .ava{width:2rem;height:2rem;border-radius:50%;overflow:hidden;background:#232a3d;display:grid;place-items:center;font-size:.75rem;flex:none}
.lit-people .ava img{width:100%;height:100%;object-fit:cover}
.lit-q{margin:1.6rem 0;padding:1rem 1.3rem;border-left:3px solid var(--c,#c8102e);background:var(--slate);border-radius:0 10px 10px 0}
.lit-q .cyq{font-family:var(--f-display,inherit);font-size:1.3rem;line-height:1.35;margin:0 0 .4rem;font-style:italic}
.lit-q .enq{margin:0 0 .4rem;color:var(--muted)}
.lit-q cite{font-family:var(--f-mono);font-size:.75rem;color:var(--muted);font-style:normal}
.cyng{background:var(--slate);border:1px solid var(--line);border-radius:12px;padding:1.4rem 1.5rem}
.cyng-line{font-family:var(--f-display,inherit);font-size:clamp(1.5rem,5vw,2.4rem);line-height:1.3;margin:1.2rem 0 .3rem;display:flex;flex-wrap:wrap;gap:.2rem 1.2rem}
.cyng-line b{color:var(--gold,#d4a72c);text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:5px}
.cyng-line .bar{color:var(--muted)}
.cyng-key{font-family:var(--f-mono);font-size:.78rem;color:var(--muted)}
.bk-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,21rem),1fr));gap:1.2rem}
.bk{background:var(--slate);border:1px solid var(--line);border-top:3px solid var(--c);border-radius:12px;overflow:hidden;display:grid;align-content:start}
.bk figure.photo{margin:0}
.bk figure.photo img{width:100%;height:15rem;object-fit:cover;object-position:50% 20%;display:block;background:#0d1018}
.bk figure.photo figcaption{padding:.5rem 1.2rem 0;font-size:.78rem}
.bk .in{padding:1rem 1.2rem 1.3rem;display:grid;gap:.6rem}
.bk h3{font-size:1.45rem;line-height:1.15;margin:0}
.bk .alt{color:var(--muted);margin:-.3rem 0 0;font-style:italic}
.bk .meta{font-family:var(--f-mono);font-size:.75rem;color:var(--c);display:flex;flex-wrap:wrap;gap:.2rem 1rem}
.bk .meta span:last-child{color:var(--muted)}
.bk p{margin:0}
.bk .pic2 img{height:auto;max-height:9rem;object-fit:contain;background:#efe6d2}
.tri-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,22rem),1fr));gap:1rem;align-items:start}
details.tri{background:var(--slate);border:1px solid var(--line);border-radius:12px;padding:0;overflow:hidden}
details.tri[open]{border-color:var(--gold,#d4a72c)}
details.tri summary{list-style:none;cursor:pointer;padding:1.1rem 1.2rem;display:grid;gap:.3rem}
details.tri summary::-webkit-details-marker{display:none}
details.tri summary .n{font-family:var(--f-display,inherit);font-size:2.4rem;line-height:1;color:var(--gold,#d4a72c)}
details.tri summary h3{font-size:1.3rem;margin:0;line-height:1.2}
details.tri summary .en{color:var(--muted);margin:0}
details.tri summary .tap{font-family:var(--f-mono);font-size:.75rem;color:var(--c,#c8102e);margin-top:.3rem}
details.tri[open] summary .tap{display:none}
details.tri .body{padding:0 1.2rem 1.2rem;display:grid;gap:.7rem}
details.tri ol{margin:0;padding-left:1.4rem;display:grid;gap:.5rem}
details.tri ol li::marker{color:var(--gold,#d4a72c);font-weight:700}
details.tri .more{font-style:italic;margin:0}
details.tri .note{color:var(--muted);font-size:.95rem;margin:0;border-top:1px solid var(--line);padding-top:.7rem}
.tri-today{border:1px solid var(--gold,#d4a72c);border-radius:14px;padding:1.2rem;background:linear-gradient(135deg,rgba(212,167,44,.08),transparent)}
.tri-today .eyebrow{margin:0 0 .6rem}
"""


def lit_fig(pic, cls=""):
    """A picture with its full credit: a gallery id (stored on the site) or a Commons file tuple from src/literature.py."""
    if not pic:
        return ""
    if isinstance(pic, str):
        return photo_fig(None, cls, pic)
    f, by, lic, licu, cen, ccy, w, h = pic
    src_ = photo_url(f.replace(" ", "_") if f not in LOCAL_PHOTOS and f.replace(" ", "_") in LOCAL_PHOTOS else f)
    return (f'<figure class="photo {cls}"><img src="{src_}" width="{w}" height="{h}" alt="{e(cen)}" loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.closest(\'figure\').remove()">'
            f'<figcaption>{bi(cen, ccy)} · {bi("Picture", "Llun")}: {e(by)}, <a href="{e(licu)}" target="_blank" rel="noopener license">{e(lic)}</a>, '
            f'<a href="{COMMONS}File:{_q(f, safe="")}" target="_blank" rel="noopener">Wikimedia Commons</a></figcaption></figure>')


def lit_prose(en, cy):
    """prose_bi(), but a quote written '> Welsh — English | source' shows the Welsh words with the English beneath."""
    def one(pars, lang):
        out, run = "", []
        for a in pars:
            if a.startswith("> "):
                q, _, c = a[2:].partition(" | ")
                cyq, _, enq = q.partition(" — ")
                out += prose(run)
                run = []
                out += (f'<blockquote class="lit-q"><p class="cyq" lang="cy">{e(cyq)}</p>' + (f'<p class="enq">{e(enq)}</p>' if enq else "")
                        + (f"<cite>{e(c)}</cite>" if c else "") + "</blockquote>")
            else:
                run.append(a)
        return f'<div class="prose l-{lang}" lang="{lang}">{out + prose(run)}</div>'
    return one(en, "en") + one(cy, "cy")


def lit_person_chip(slug):
    p = PERSON.get(slug)
    if not p:
        return ""
    ph = f"gallery/person-{slug}-s.webp" if ("person-" + slug) in GP.GALLERY else (photo_url(PH.PERSON_PHOTOS[slug][0], 240) if slug in PH.PERSON_PHOTOS else "")
    ini = e(p[3][0])
    img = f'<img src="{ph}" alt="" loading="lazy" referrerpolicy="no-referrer" onerror="this.remove()">' if ph else ""
    return f'<a href="person-{slug}.html"><span class="ava" aria-hidden="true">{ini}{img}</span>{bi(p[3], p[4])}</a>'


LIT_AGE_OF = {s: a for a in LT.AGES for s in a["people"] if s not in ("gruffudd-ap-cynan", "owain-gwynedd", "yr-arglwydd-rhys", "llywelyn-fawr", "llywelyn-ap-gruffudd", "owain-glyndwr")}


def lit_link(slug):
    a = LIT_AGE_OF.get(slug)
    return f'<a href="literature.html#{a["id"]}">{bi("Welsh literature: " + a["en"], "Llenyddiaeth Gymraeg: " + a["cy"])} →</a>' if a else ""


def lit_door(d):
    href, en, cy, len_, lcy, gid = d
    return (f'<a class="lit-door rv" href="{href}"><img src="gallery/{gid}-s.webp" alt="" loading="lazy">'
            f'<span class="t"><b>{bi(en, cy)}</b><small>{bi(len_, lcy)}</small></span></a>')


def cynghanedd_box():
    def half(parts):
        return "".join(f"<b>{e(t)}</b>" if on else e(t) for t, on in parts)
    a, b = LT.CYNG_LINE
    return (f'<div class="cyng">{prose_bi(LT.CYNG_EN, LT.CYNG_CY)}'
            f'<p class="cyng-line" lang="cy"><span>{half(a)}</span><span class="bar" aria-hidden="true">|</span><span>{half(b)}</span></p>'
            f'<p class="cyng-key">b · r · dd · t · r &nbsp;=&nbsp; b · r · dd · t · r &nbsp;·&nbsp; R. Williams Parry, ‘Hedd Wyn’</p></div>')


def literature_page():
    jump = '<nav class="chips l-jump" aria-label="Sections / Adrannau">' + "".join(f'<a class="chip" href="#{a["id"]}">{bi(a["en"], a["cy"])}</a>' for a in LT.AGES) + '</nav>'
    ages = ""
    for a in LT.AGES:
        people = "".join(lit_person_chip(s) for s in a["people"])
        ages += (f'<section class="tight" id="{a["id"]}" data-era="{a["era"]}"><div class="wrap"><div class="lit-age"><div>'
                 f'<p class="span">{bi(a["span"], a["spanCy"])}</p><h2 class="sub-h">{bi(a["en"], a["cy"])}</h2>{lit_prose(a["pEn"], a["pCy"])}'
                 + (f'<p class="eyebrow" style="margin-top:1.4rem">{bi("Read more about them", "Darllen mwy amdanynt")}</p><div class="lit-people">{people}</div>' if people else "")
                 + f'</div><div class="lit-side">{lit_fig(a["pic"])}</div></div>'
                 + (f'<div style="margin-top:2.4rem" id="cynghanedd"><h3 class="sub-h">{bi("What is cynghanedd?", "Beth yw cynghanedd?")}</h3>{cynghanedd_box()}</div>' if a["id"] == "uchelwyr" else "")
                 + '</div></section>')
    main = (hero("medieval", f'<a href="index.html">{SITE}</a>', "book", "From c. 600 to today", "O tua 600 hyd heddiw", "The literature of Wales", "Llenyddiaeth Cymru",
                 "Fourteen hundred years of poetry and prose: the first poets of the Old North, the bards of the princes, Dafydd ap Gwilym, the Bible of 1588, the hymns and the chair poems of today.",
                 "Pedwar can mlynedd ar ddeg o farddoniaeth a rhyddiaith: beirdd cyntaf yr Hen Ogledd, beirdd y tywysogion, Dafydd ap Gwilym, Beibl 1588, yr emynau a cherddi’r gadair heddiw.", art="book", extra=jump)
            + f'<style>{LIT_CSS}</style>'
            + section(paras(LT.HUB_EN, LT.HUB_CY) + f'<div class="lit-doors">{"".join(lit_door(d) for d in LT.DOORS)}</div>', top=True)
            + ages
            + section(f'<div class="pager"><a class="btn" href="triads.html">{bi("The Welsh Triads", "Trioedd Ynys Prydain")} →</a><a class="btn solid" href="books.html">{bi("The old books of Wales", "Hen lyfrau Cymru")} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": "The literature of Wales", "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page("literature.html", "The literature of Wales · History of Wales",
                "Fourteen centuries of Welsh literature: Taliesin and Aneirin, the Poets of the Princes, Dafydd ap Gwilym and the cywyddwyr, cynghanedd, the 1588 Bible, the hymns and the Eisteddfod, in English and Cymraeg.",
                main, era="medieval", ld=ld, og_type="website", active="literature.html", track="page:literature")


def book_card(b, era):
    alt = b["cy"] if b["cy"] != b["en"] else ""
    where = bi(b["whereEn"], b["whereCy"]) if b["whereEn"] else ""
    link = (f'<p><a class="go" href="{b["link"][0]}">{bi(b["link"][1], b["link"][2])} →</a></p>' if b.get("link") else "")
    return (f'<article class="bk rv" id="{b["id"]}" data-era="{era}">{lit_fig(b["pic"])}<div class="in">'
            f'<p class="meta"><span>{bi(b["date"], b["dateCy"])}</span>{f"<span>{where}</span>" if where else ""}</p>'
            f'<h3><a href="book-{b["id"]}.html">{bi(b["en"], b["cy"])}</a></h3>' + (f'<p class="alt l-en" lang="cy">{e(alt)}</p>' if alt else "")
            + f'<p>{bi(b["en_t"], b["cy_t"])}</p>{lit_fig(b.get("pic2"), "pic2")}'
            + f'<p><a class="go" href="book-{b["id"]}.html">{bi("The whole story of the book", "Stori gyfan y llyfr")} →</a></p>{link}</div></article>')


def books_page():
    eras = BOOK_ERAS
    jump = '<nav class="chips l-jump" aria-label="Sections / Adrannau">' + "".join(f'<a class="chip" href="#{g["id"]}">{bi(g["en"], g["cy"])}</a>' for g in LT.BOOK_GROUPS) + '</nav>'
    groups = "".join(f'<section class="tight" id="{g["id"]}"><div class="wrap"><h2 class="sub-h">{bi(g["en"], g["cy"])}</h2>'
                     f'<div class="bk-grid">{"".join(book_card(b, eras[g["id"]]) for b in g["books"])}</div></div></section>' for g in LT.BOOK_GROUPS)
    main = (hero("medieval", f'<a href="index.html">{SITE}</a> / <a href="literature.html">{bi("Literature", "Llenyddiaeth")}</a>', "book", "c. 800–1807", "tua 800–1807",
                 "The old books of Wales", "Hen lyfrau Cymru",
                 "The Black Book of Carmarthen, the Books of Aneirin and Taliesin, the Red Book of Hergest, the White Book of Rhydderch, and the first printed books: the treasures that kept the memory of Wales alive.",
                 "Llyfr Du Caerfyrddin, Llyfrau Aneirin a Thaliesin, Llyfr Coch Hergest, Llyfr Gwyn Rhydderch, a’r llyfrau printiedig cyntaf: y trysorau a gadwodd gof Cymru’n fyw.", art="arches", extra=jump)
            + f'<style>{LIT_CSS}</style>'
            + section(paras(LT.BOOKS_INTRO_EN, LT.BOOKS_INTRO_CY) + f'<p class="lede">{bi(OB.INTRO_EN, OB.INTRO_CY)}</p>'
                      + f'<p class="l-links"><a class="btn" href="story-writers.html">{bi("The writers who recorded early Wales", "Yr awduron a gofnododd Gymru gynnar")} →</a> '
                      + f'<a class="btn" href="story-bruts.html">{bi("The Bruts: the chronicles of Wales", "Y Brutiau: croniclau Cymru")} →</a> '
                      + f'<a class="btn" href="triads.html">{bi("The Welsh Triads", "Trioedd Ynys Prydain")} →</a></p>', top=True)
            + groups
            + section(prose_bi(LT.WHERE_EN, LT.WHERE_CY) + f'<p class="l-links"><a class="btn" href="place-library.html">{bi("The National Library of Wales", "Llyfrgell Genedlaethol Cymru")} →</a> '
                      f'<a class="btn" href="https://www.library.wales" rel="noopener">{bi("See the manuscripts online", "Gweld y llawysgrifau ar-lein")} ↗</a></p>')
            + section(f'<div class="pager"><a class="btn" href="literature.html">← {bi("The literature of Wales", "Llenyddiaeth Cymru")}</a><a class="btn solid" href="triads.html">{bi("The Welsh Triads", "Trioedd Ynys Prydain")} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": "The old books of Wales", "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page("books.html", "The old books of Wales · History of Wales",
                "The old books of Wales, each with a page of its own: the Four Ancient Books (the Black Book of Carmarthen, the Book of Aneirin, the Book of Taliesin, the Red Book of Hergest), the White Book of Rhydderch, the Hendregadredd Manuscript, Brut y Tywysogion and the 1588 Bible.",
                main, era="medieval", ld=ld, og_type="website", active="literature.html", track="page:books")


LT.BOOK_GROUPS.insert(next(i for i, g in enumerate(LT.BOOK_GROUPS) if g["id"] == "great") + 1, OB.NEW_GROUP)  # three more treasures (src/oldbooks.py)
BOOK_ERAS = {"earliest": "saints", "four": "medieval", "great": "medieval", "more": "medieval", "print": "tudor"}
ALL_BOOKS = [(b, g) for g in LT.BOOK_GROUPS for b in g["books"]]


def book_page(i):
    """One old book of Wales (src/oldbooks.py): its facts, its whole story, its pictures, its people and where to read more."""
    b, g = ALL_BOOKS[i]
    era = BOOK_ERAS[g["id"]]
    pg = OB.PAGES[b["id"]]
    prev_b = ALL_BOOKS[i - 1][0] if i > 0 else None
    next_b = ALL_BOOKS[i + 1][0] if i + 1 < len(ALL_BOOKS) else None
    crumbs = (f'<a href="index.html">{SITE}</a> / <a href="literature.html">{bi("Literature", "Llenyddiaeth")}</a> / '
              f'<a href="books.html">{bi("The old books of Wales", "Hen lyfrau Cymru")}</a>')
    first = lambda t: t.split(". ")[0].rstrip(".") + "."
    alt = f'<p class="byline"><span lang="cy">{e(b["cy"])}</span></p>' if b["cy"] != b["en"] else ""
    where = f'<p class="byline"><span>{bi(g["en"], g["cy"])}</span>' + (f'<span>{bi(b["whereEn"], b["whereCy"])}</span>' if b["whereEn"] else "") + '</p>'
    links = [(f'{u}', a, c) for u, a, c in pg.get("links", [])]
    if b.get("link") and b["link"][0] not in {u for u, _, _ in links}:
        links.insert(0, b["link"])
    btns = " ".join(f'<a class="btn" href="{u}">{bi(a, c)} →</a>' for u, a, c in links)
    body = (f'<section class="article"><div class="wrap narrow">{where}{alt}'
            f'{prose_bi(pg["pEn"], pg["pCy"], "story prose", figs=OB.FIGS)}{lit_fig(b.get("pic2"), "lr-fig")}'
            f'<p class="l-links">{btns}</p></div></section>')
    ppl = "".join(lit_person_chip(s) for s in pg.get("people", []))
    who = section(f'<div class="ar-circle"><div class="ppl">{ppl}</div></div>', "People of the book", "Pobl y llyfr") if ppl else ""
    pager = ((f'<a class="btn" href="book-{prev_b["id"]}.html">← {bi(prev_b["en"], prev_b["cy"])}</a>' if prev_b else f'<a class="btn" href="books.html">← {bi("The old books of Wales", "Hen lyfrau Cymru")}</a>')
             + (f'<a class="btn solid" href="book-{next_b["id"]}.html">{bi(next_b["en"], next_b["cy"])} →</a>' if next_b else f'<a class="btn solid" href="books.html">{bi("The old books of Wales", "Hen lyfrau Cymru")} →</a>'))
    main = (hero(era, crumbs, "book", b["date"], b["dateCy"], b["en"], b["cy"] if b["cy"] != b["en"] else b["en"], first(b["en_t"]), first(b["cy_t"]), art="book")
            + body + who + section(f'<div class="pager">{pager}</div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": b["en"], "description": first(b["en_t"]), "inLanguage": ["en", "cy"],
          "about": {"@type": "Book", "name": b["en"], "alternateName": b["cy"]}, "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page(f'book-{b["id"]}.html', f'{b["en"]} · The old books of Wales · History of Wales', first(b["en_t"]), main, era=era, ld=ld, active="literature.html", track=f'book:{b["id"]}')


def triad_card(t, k):
    items = "".join(f"<li>{bi(en, cy)}</li>" for en, cy in t["three"])
    more = f'<p class="more">{bi(*t["more"])}</p>' if t.get("more") else ""
    note = f'<p class="note">{bi(*t["note"])}</p>' if t.get("note") else ""
    return (f'<details class="tri" id="tri-{k}"><summary><span class="n" aria-hidden="true">III</span><h3 lang="cy">{e(t["cy"])}</h3>'
            f'<p class="en l-en" lang="en">{e(t["en"])}</p><span class="tap">{bi("Can you name the three? Tap to see", "Allwch chi enwi’r tri? Tapiwch i weld")}</span></summary>'
            f'<div class="body"><ol>{items}</ol>{more}{note}</div></details>')


def triads_page():
    k, groups = 0, ""
    for g in LT.TRIAD_GROUPS:
        cards = ""
        for t in g["triads"]:
            cards += triad_card(t, k)
            k += 1
        groups += f'<section class="tight"><div class="wrap"><h2 class="sub-h">{bi(g["en"], g["cy"])}</h2><div class="tri-grid">{cards}</div></div></section>'
    today = (f'<div class="tri-today no-print" id="tri-today" hidden><p class="eyebrow">{bi("Triad of the day", "Triawd y dydd")}</p><div class="tri-slot"></div></div>')
    js = ("<script>(function(){var c=document.querySelectorAll('details.tri');var box=document.getElementById('tri-today');if(!c.length||!box)return;"
          "var d=new Date(),n=Math.floor((d-new Date(d.getFullYear(),0,0))/864e5);var t=c[n%c.length].cloneNode(true);t.removeAttribute('id');t.open=false;"
          "box.querySelector('.tri-slot').appendChild(t);box.hidden=false;})();</script>")
    main = (hero("saints", f'<a href="index.html">{SITE}</a> / <a href="literature.html">{bi("Literature", "Llenyddiaeth")}</a>', "book", "Trioedd Ynys Prydain", "Trioedd Ynys Prydain",
                 "The Welsh Triads", "Trioedd Ynys Prydain",
                 "The memory of a nation in threes: kings, heroes, war bands, horses and the secrets of the Island of Britain, kept by the bards for a thousand years.",
                 "Cof cenedl fesul tri: brenhinoedd, arwyr, gosgorddion, meirch a chyfrinachau Ynys Prydain, a gadwyd gan y beirdd am fil o flynyddoedd.", art="gorsedd")
            + f'<style>{LIT_CSS}</style>'
            + section(f'<div class="lit-age"><div>{prose_bi(LT.TRIADS_INTRO_EN, LT.TRIADS_INTRO_CY)}</div><div class="lit-side">{today}{lit_fig("trea-red-book")}</div></div>', top=True)
            + groups
            + section(f'<div class="lit-age"><div>{prose_bi(LT.TRIADS_MORE_EN, LT.TRIADS_MORE_CY)}<p class="l-links"><a class="btn" href="laws.html#inside">{bi("The Laws of Hywel Dda", "Cyfraith Hywel Dda")} →</a> <a class="btn" href="story-iolo.html">{bi("Iolo Morganwg", "Iolo Morganwg")} →</a> <a class="btn" href="story-bruts.html">{bi("The Bruts: the chronicles of Wales", "Y Brutiau: croniclau Cymru")} →</a> <a class="btn" href="story-writers.html">{bi("The writers who recorded early Wales", "Yr awduron a gofnododd Gymru gynnar")} →</a> <a class="btn" href="books.html">{bi("The old books of Wales", "Hen lyfrau Cymru")} →</a></p></div>'
                      f'<div class="lit-side">{lit_fig(LT.WHITE_BOOK_PAGE)}</div></div>')
            + section(f'<div class="pager"><a class="btn" href="literature.html">← {bi("The literature of Wales", "Llenyddiaeth Cymru")}</a><a class="btn solid" href="mabinogion.html">{bi("The Mabinogion", "Y Mabinogion")} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": "The Welsh Triads (Trioedd Ynys Prydain)", "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page("triads.html", "The Welsh Triads · History of Wales",
                "Trioedd Ynys Prydain, the Welsh Triads: the Three Generous Men, the Three Faithful War Bands, the Three Fortunate Concealments, Arthur’s court, the legal triads and Iolo Morganwg’s triads, in English and Cymraeg.",
                main, era="saints", ld=ld, og_type="website", active="literature.html", track="page:triads", extra=js)


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
    return {c: AD.newest("gallery", v, ties="keep") for c, v in items.items()}  # newly added pictures first in each group


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
 ("llys-rhosyr.html", "llys", "Llys Rhosyr in 3D", "Llys Rhosyr mewn 3D", "Walk through a royal court of the princes of Gwynedd: the great hall, the hearth, the prince’s seat.", "Cerddwch drwy un o lysoedd brenhinol tywysogion Gwynedd: y neuadd fawr, yr aelwyd, sedd y tywysog.", "Explore in 3D", "Crwydro mewn 3D", "medieval"),
 ("ride-glyndwr.html", "ride", "Ride with Glyndŵr, 1400", "Marchogaeth gyda Glyndŵr, 1400", "Answer Owain Glyndŵr’s call as an archer, a bard or a rider, and choose your way through the rising.", "Atebwch alwad Owain Glyndŵr fel saethydd, bardd neu farchog, a dewiswch eich ffordd drwy’r gwrthryfel.", "A story you choose", "Stori rydych chi’n ei dewis", "medieval"),
 ("daily.html", "daily", "Daily challenge", "Her y dydd", "One event, six guesses to find the year. A new one every day, and a streak to keep.", "Un digwyddiad, chwe chynnig i ddyfalu’r flwyddyn. Un newydd bob dydd, a rhediad i’w gadw.", "Every day", "Bob dydd", "medieval"),
 ("quiz.html", "quiz", "The quiz", "Y cwis", "Ten questions drawn from the timeline and the people. Every round is different.", "Deg cwestiwn o’r llinell amser a’r bobl. Mae pob rownd yn wahanol.", "10 questions", "10 cwestiwn", "kings"),
 ("map-game.html", "map", "Where in Wales?", "Ble yng Nghymru?", "Put castles, towns and battlefields on a blank map. How close can you get?", "Rhowch gestyll, trefi a meysydd brwydr ar fap gwag. Pa mor agos allwch chi fynd?", "5 rounds", "5 rownd", "modern"),
 ("quiz.html#game", "order", "Timeline challenge", "Her y llinell amser", "Put five events in order, oldest first.", "Rhowch bum digwyddiad yn eu trefn, yr hynaf yn gyntaf.", "3 rounds", "3 rownd", "industrial"),
 ("names.html", "names", "Welsh names", "Enwau Cymraeg", "What does your surname mean? And what would you have been called in the age of the princes?", "Beth yw ystyr eich cyfenw? A beth fyddai eich enw yn oes y tywysogion?", "Try your name", "Rhowch gynnig ar eich enw", "saints"),
 ("hero.html", "hero", "Which figure from history are you?", "Pa ffigwr o hanes ydych chi?", "Six questions to find your match among the people who shaped Wales.", "Chwe chwestiwn i ganfod eich tebyg ymhlith y bobl a luniodd Gymru.", "6 questions", "6 chwestiwn", "ancient"),
 ("pairs.html", "pairs", "Word pairs", "Parau geiriau", "A memory game for younger visitors: match the Welsh word to its meaning.", "Gêm gof i ymwelwyr iau: parwch y gair Cymraeg â’i ystyr.", "For children", "I blant", "modern"),
]

GAMES = AD.newest("game", GAMES, key=lambda g: g[0], ties="keep")  # a new game goes at the top


GAME_ICON = {"llys": "3D", "ride": "♞", "daily": "?", "quiz": "10", "map": "⌖", "order": "1→5", "names": "ap", "hero": "♛", "pairs": "Aa"}


def play_card(g):
    """One game: its real picture (src/pictures.py), a badge, what kind of game, its name and one line. The card is one link."""
    pic = PX.card_img(g[0] if "#" not in g[0] else "", g[8]) or ""  # the timeline game (quiz.html#game) takes its age's picture
    return (f'<a class="p-card rv p-{g[1]}" href="{g[0]}" data-era="{g[8]}"><span class="p-pic">{pic}</span>'
            f'<span class="p-ico" aria-hidden="true">{GAME_ICON.get(g[1], "")}</span><span class="tag">{bi(g[6], g[7])}</span>'
            f'<div class="p-txt"><h3>{bi(g[2], g[3])}</h3><p>{bi(g[4], g[5])}</p></div></a>')


def play_cards(home=False):
    """The games. On the home page the Daily challenge already has its own card beside On this day, so it is left out here,
    and the last tile leads to all the games."""
    games = [g for g in GAMES if not (home and g[1] == "daily")]
    out = "".join(play_card(g) for g in games)
    if home:
        faces = "".join(f'<span>{PX.card_img(g[0] if "#" not in g[0] else "", g[8]) or ""}</span>' for g in GAMES[:5])
        out += (f'<a class="p-card p-all rv" href="play.html"><span class="p-faces" aria-hidden="true">{faces}</span>'
                f'<div class="p-txt"><h3>{bi(f"All {len(GAMES)} games", f"Pob un o’r {len(GAMES)} gêm")}</h3>'
                f'<p>{bi("Quizzes, a map game, Welsh names and more, with badges to collect.", "Cwisiau, gêm fap, enwau Cymraeg a mwy, gyda bathodynnau i’w casglu.")}</p></div>'
                f'<span class="ar" aria-hidden="true">→</span></a>')
    return out


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
                 "Games and adventures drawn from the history on this site. Scores, streaks and badges are kept on your own device.", "Gemau ac anturiaethau wedi’u seilio ar yr hanes ar y wefan hon. Cedwir sgoriau, rhediadau a bathodynnau ar eich dyfais eich hun.", art="dragons")
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
                 "Every page you read is ticked off here, every person, place and legend is a card to collect in sets, and games earn badges. Nothing leaves your device.", "Mae pob tudalen a ddarllenwch yn cael ei thicio yma, mae pob person, lle a chwedl yn gerdyn i’w gasglu mewn setiau, ac mae gemau’n ennill bathodynnau. Nid oes dim yn gadael eich dyfais.", art="sword")
            + f'<section><div class="wrap"><div id="journey-root"><noscript>Your journey needs JavaScript.</noscript></div></div></section>' + cards_section())
    extra = f'<script>var JOURNEY={json.dumps(groups, ensure_ascii=False, separators=(",", ":"))};</script>\n'
    return page("journey.html", "Your journey · History of Wales", "Track what you have read and the badges you have earned on History of Wales.", main, era="kings", og_type="website", extra=extra)



# ---------- collectable cards (src/sets.py) ----------
# Every person, place and legend page is a card; reading the page collects it. Sets are shown on the journey page and on
# each page that belongs to one. Which cards someone has is worked out in site.js from the journey kept on their device.
LEGEND = {x["id"]: x for x in F.LEGENDS}


def _card_info(key):
    kind, ref = key.split(":", 1)
    if kind == "person":
        p = PERSON[ref]
        g = GP.GALLERY.get("person-" + ref)
        ph = PH.PERSON_PHOTOS.get(ref)
        img = f"gallery/person-{ref}-s.webp" if g else (photo_url(ph[0], 240) if ph else None)
        return p[3], p[4], p[2], p[1], f"person-{ref}.html", img
    if kind == "place":
        pl = PLACE[ref]
        ph = place_ph(ref)
        return pl["en"], pl["cy"], pl["year"], pl["era"], f"place-{ref}.html", ph[0] if ph else None
    x = LEGEND[ref]
    img = f'legends/{x["art"]}-s.webp' if x["art"] in A.LEGEND_PHOTOS else None
    return x["en"], x["cy"], x["place"], x["era"], f"legend-{ref}.html", img


CARD_INFO = {}
for _s in SETS.SETS:
    for _k in _s[5]:
        try:
            CARD_INFO[_k] = _card_info(_k)
        except KeyError:
            raise SystemExit(f"src/sets.py: set '{_s[0]}' has a card that does not exist: {_k}")
SET_OF = {}
for _s in SETS.SETS:
    for _k in _s[5]:
        SET_OF.setdefault(_k, []).append(_s)
CARD_TOTAL = len(CARD_INFO)


def _initials(n):
    w = [x for x in re.sub(r"\b(ap|ab|ferch|the|of|yr|y|St|Saint)\b", " ", n).split() if x[:1].isalpha()]
    return ((w[0][0] + (w[-1][0] if len(w) > 1 else "")) if w else n[:1]).upper()


def card_html(key, n, total, here=False):
    en, cy, sub, era, link, img = CARD_INFO[key]
    pic = f'<img src="{img}" alt="" loading="lazy" decoding="async">' if img else ""
    if not img and key.startswith("legend:"):
        pic = PX.card_img(f"legend-{key[7:]}.html") or A.scene(LEGEND[key[7:]]["art"], COL[era])
    return (f'<a class="cc{" here" if here else ""}" href="{link}" data-k="{key}" data-era="{era}">'
            f'<span class="cc-img"><i aria-hidden="true">{e(_initials(en))}</i>{pic}</span><span class="cc-no">{n}/{total}</span>'
            f'<span class="cc-t"><b>{bi(en, cy)}</b><small>{e(sub)}</small></span></a>')


def set_html(st, here=None, tag="div"):
    sid, en, cy, den, dcy, keys = st
    cards = "".join(card_html(k, i + 1, len(keys), k == here) for i, k in enumerate(keys))
    return (f'<{tag} class="cset" data-set="{sid}"><div class="cset-h"><h3>{bi(en, cy)}</h3><span class="cset-n"><b>0</b> / {len(keys)}</span>'
            f'<p>{bi(den, dcy)}</p><div class="j-bar"><i style="width:0"></i></div></div><div class="cc-row">{cards}</div></{tag}>')


def set_block(key):
    sets = SET_OF.get(key)
    if not sets:
        return ""
    return section('<p class="cset-lead">' + bi("Reading this page collects its card. Collect every card in the set.", "Mae darllen y dudalen hon yn casglu ei cherdyn. Casglwch bob cerdyn yn y set.")
                   + f' <a href="journey.html#cards">{bi("All your cards", "Eich holl gardiau")} →</a></p>'
                   + "".join(set_html(st, key) for st in sets), "Collect the set" if len(sets) == 1 else "Collect the sets", "Casglwch y set" if len(sets) == 1 else "Casglwch y setiau")


def cards_section():
    return (f'<section class="tight" id="cards"><div class="wrap"><h2 class="j-h">{bi("Your cards", "Eich cardiau")}</h2>'
            f'<p class="cset-lead" id="cards-sum" data-total="{CARD_TOTAL}" data-sets="{len(SETS.SETS)}">'
            + bi(f"Every person, place and legend you read is a card. There are {CARD_TOTAL} cards in {len(SETS.SETS)} sets.",
                 f"Mae pob person, lle a chwedl a ddarllenwch yn gerdyn. Mae {CARD_TOTAL} o gardiau mewn {len(SETS.SETS)} set.")
            + '</p>' + "".join(set_html(st) for st in SETS.SETS) + '</div></section>')


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


def otd_pic(link, era, place=None):
    """A small picture for an On this day row (home page panel): the person's or place's own photo,
    else the linked page's picture (src/pictures.py), else the event's place, else the picture of its age."""
    path = (link or "").split("#")[0]
    stem = path[:-5] if path.endswith(".html") else ""
    if stem.startswith("saints-") and "#s-" in (link or ""):
        stem = "person-" + link.split("#s-")[1]  # a saint who also has a person page or portrait
    if stem in GP.GALLERY:
        return f"gallery/{stem}-s.webp"
    if stem.startswith("person-") and stem[7:] in PH.PERSON_PHOTOS:
        return photo_url(PH.PERSON_PHOTOS[stem[7:]][0], 240)
    if stem.startswith("place-") and stem[6:] in PH.PLACE_PHOTOS:
        return photo_url(PH.PLACE_PHOTOS[stem[6:]][0], 240)
    if place and "place-" + place in GP.GALLERY:
        return f"gallery/place-{place}-s.webp"
    ref = PX.for_page(path) if path else None  # a saint without a portrait takes the picture of their region's saints page
    ref = ref or PX.ERA.get(era) or PX.ERA["medieval"]
    return PX._parse(ref)["small"]


OTD_SRC = {}  # (MM-DD, year, English title) -> "[[cite:...]]" keys, filled by otd_rows()


def otd_rows():
    """Every dated entry: [MM-DD, year or None, kind, titleEn, titleCy, lineEn, lineCy, link, era, picture]."""
    rows, seen = [], set()
    for i, ev in enumerate(D.EVENTS):
        if ev[4]:
            st = story_links("events", ev[5])
            link = f'story-{st[0]["id"]}.html' if st else EP.href(ev)  # the long read that tells it, or the event's own page
            rows.append([ev[4], ev[1], "ev", ev[5], ev[6], ev[7], ev[8], link, ev[0], otd_pic(link, ev[0], ev[10])])
            seen.add((ev[4], ev[1], ev[5]))
    covered = {r[7][6:] for r in OTD.OTD if r[7].startswith("saint:")}
    for md, y, k, te, tc, le, lc, link, *src in OTD.OTD:
        if (md, y, te) in seen:  # the same day already comes from the timeline (11 November 1918 was in twice)
            continue
        if src:  # the row's sources (an optional 9th field): a § chip after its line on onthisday.html
            OTD_SRC[(md, y, te)] = src[0]
        if link.startswith("saint:"):
            link = saint_href(link[6:])
        era = era_of_year(y) if y is not None else "saints" if k == "feast" else "modern"
        rows.append([md, y, k, te, tc, le, lc, link, era, otd_pic(link, era)])
    for sid, (x, r) in SAINT.items():  # every other saint with a feast day on the Saints of Wales page
        if x["feast"] and sid not in covered:
            first = lambda t: t.split(". ")[0].rstrip(".") + "."
            link = saint_href(sid)
            rows.append([f'{x["feast"][1]:02d}-{x["feast"][0]:02d}', None, "feast", x["en"], x["cy"], first(x["nEn"]), first(x["nCy"]), link, "saints", otd_pic(link, "saints")])
    rows.sort(key=lambda r: (r[0], OTD_ORDER[r[2]], r[1] if r[1] is not None else -10 ** 6))
    return rows


def otd_item(r):
    md, y, k, te, tc, le, lc, link, era = r[:9]
    tag = OTD_TAG.get(k)
    when = (f'<span class="y">{y}</span>' if y is not None else "") + (f'<span class="k">{bi(*tag)}</span>' if tag else "")
    title = bi(te, tc)
    if link:
        title = f'<a href="{e(link)}">{title}</a>'
    src = OTD_SRC.get((md, y, te))
    cite = f"[[cite:{src}]]" if src else ""  # the build turns it into a § source chip (src/cites.py)
    return f'<li data-era="{era}" class="k-{k}"><p class="when">{when}</p><div><h4>{title}</h4><p>{bi(le, lc)}{cite}</p></div></li>'


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
            + f'<section class="tight otd-jump"><div class="wrap"><div class="otd-chips"><a class="chip solid" id="otd-today" href="#">{bi("Today", "Heddiw")}</a>{jump}</div><p class="otd-share"><a href="today.html">{bi("Today’s picture to share on social media", "Llun heddiw i’w rannu ar y cyfryngau cymdeithasol")} →</a></p></div></section>'
            + months)
    extra = ('<script>(function(){var n=new Date(),md=("0"+(n.getMonth()+1)).slice(-2)+"-"+("0"+n.getDate()).slice(-2),el=document.getElementById("d-"+md),b=document.getElementById("otd-today");'
             'if(!el){var all=[].slice.call(document.querySelectorAll(".otd-day"));el=all.filter(function(a){return a.id.slice(2)>=md})[0]||all[0]}'
             'if(el){el.classList.add("is-today");b.href="#"+el.id}else b.hidden=true})()</script>\n')
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "On this day in Welsh history", "inLanguage": ["en", "cy"], "url": BASE_URL + "onthisday.html"}
    return page("onthisday.html", "On this day in Welsh history · History of Wales", "What happened on each day of the year in the history of Wales: events, saints’ days, traditions, births and deaths, in English and Cymraeg.",
                main, era="medieval", og_type="website", ld=ld, extra=extra)

# ---------- today's picture: the daily "On this day" post for social media (remade by the daily rebuild) ----------
def _today():
    try:
        from zoneinfo import ZoneInfo
        return datetime.datetime.now(ZoneInfo("Europe/London")).date()
    except Exception:  # noqa: BLE001
        return datetime.date.today()


TODAY = _today()
_KIND_RANK = {"ev": 0, "born": 1, "died": 2, "feast": 3, "custom": 3}


def today_pick():
    """Today's entries (or the next day that has some), best first: events with a page and a photo lead."""
    rows = otd_rows()
    md = TODAY.strftime("%m-%d")
    days = sorted({r[0] for r in rows})
    day = next((x for x in days if x >= md), days[0])
    todays = [r for r in rows if r[0] == day]
    todays.sort(key=lambda r: (_KIND_RANK.get(r[2], 4), not r[7], not (r[7] and card_photo(r[7].split("#")[0])), r[1] is None))
    return day, todays


def _today_text(day, r, lang):
    m, dnum = int(day[:2]), int(day[3:])
    mon = MONTHS[m - 1][0 if lang == "en" else 1]
    y = f" {r[1]}" if r[1] is not None else ""
    title, line = (r[3], r[5]) if lang == "en" else (r[4], r[6])
    url = BASE_URL + (r[7] if r[7] else "onthisday.html")
    if lang == "en":
        return f"On this day in Welsh history, {dnum} {mon}{y}: {title}.\n\n{line}\n\nRead more: {url}\n\n#WelshHistory #OnThisDay #HanesCymru #Wales"
    return f"Ar y dydd hwn yn hanes Cymru, {dnum} {mon}{y}: {title}.\n\n{line}\n\nDarllenwch fwy: {url}\n\n#HanesCymru #ArYDyddHwn #Cymru #WelshHistory"


def today_page():
    day, todays = today_pick()
    r = todays[0]
    m, dnum = int(day[:2]), int(day[3:])
    stamp = TODAY.isoformat()

    def fig(lang, label):
        txt = _today_text(day, r, lang)
        return (f'<figure class="today-fig"><img src="cards/today-{lang}.jpg?d={stamp}" width="1080" height="1080" alt="{e(txt.split(chr(10))[0])}" loading="lazy">'
                f'<figcaption><p class="eyebrow">{label}</p><textarea readonly rows="7" id="cap-{lang}" aria-label="{e(label)}" lang="{"en" if lang == "en" else "cy"}">{e(txt)}</textarea>'
                f'<p class="more-row"><a class="btn solid" href="cards/today-{lang}.jpg?d={stamp}" download="hanes-cymru-{day}-{lang}.jpg">{bi("Download the picture", "Lawrlwytho’r llun")}</a>'
                f'<button type="button" class="btn" data-copytext="cap-{lang}">{bi("Copy the words", "Copïo’r geiriau")}</button></p></figcaption></figure>')
    more = "".join(otd_item(x) for x in todays[1:])
    main = (hero(r[8] if r[8] in ERA else "medieval", f'<a href="index.html">{SITE}</a> / <a href="onthisday.html">{bi("On this day", "Ar y dydd hwn")}</a>', "book",
                 f"{dnum} {MONTHS[m - 1][0]}", f"{dnum} {MONTHS[m - 1][1]}", "Today’s picture to share", "Llun heddiw i’w rannu",
                 "A new picture every morning from On this day in Welsh history, in English and in Cymraeg, with the words ready to paste. Share it on Facebook, Instagram, X or WhatsApp.",
                 "Llun newydd bob bore o Ar y dydd hwn yn hanes Cymru, yn Saesneg ac yn Gymraeg, gyda’r geiriau’n barod i’w gludo. Rhannwch ef ar Facebook, Instagram, X neu WhatsApp.", art="book")
            + section(f'<div class="today-grid">{fig("en", "English")}{fig("cy", "Cymraeg")}</div>', top=True)
            + (section(f'<ul class="otd-list">{more}</ul>', "Also on this day", "Hefyd ar y dydd hwn") if more else "")
            + section(f'<div class="pager"><a class="btn" href="onthisday.html">← {bi("The whole year", "Y flwyddyn gyfan")}</a></div>'))
    extra = ('<script>document.addEventListener("click",function(e){var b=e.target.closest("[data-copytext]");if(!b)return;var t=document.getElementById(b.dataset.copytext);'
             't.select();(navigator.clipboard?navigator.clipboard.writeText(t.value):Promise.reject()).catch(function(){document.execCommand("copy")});'
             'var o=b.innerHTML;b.textContent=document.documentElement.classList.contains("cy")?"Wedi’i gopïo ✓":"Copied ✓";setTimeout(function(){b.innerHTML=o},1800)})</script>\n')
    return page("today.html", "Today’s picture to share · History of Wales", "A new picture every morning from On this day in Welsh history, ready to share on social media, in English and Cymraeg.",
                main, era=r[8] if r[8] in ERA else "medieval", og_type="website", extra=extra)


def make_today(out):
    day, todays = today_pick()
    r = todays[0]
    m, dnum = int(day[:2]), int(day[3:])
    photo = card_photo(r[7].split("#")[0]) if r[7] else None
    dragon = os.path.join(SRC, "static", "dragon-red.webp")
    col = COL.get(r[8], "#f26a62")
    for lang in ("en", "cy"):
        title, line = (r[3], r[5]) if lang == "en" else (r[4], r[6])
        eyebrow = ("On this day" if lang == "en" else "Ar y dydd hwn") + (f" · {r[1]}" if r[1] is not None else "")
        CARDS.make_square(os.path.join(out, "cards", f"today-{lang}.jpg"), eyebrow, f"{dnum} {MONTHS[m - 1][0 if lang == 'en' else 1]}", title, line, col, photo, dragon,
                          name="History of Wales" if lang == "en" else "Hanes Cymru")


# ---------- Wales in 10 minutes (src/story10.py): the whole story beside the changing map ----------
import story10 as S10  # noqa: E402

PLACE_BY_ID = {p["id"]: p for p in D.PLACES}


def _soften(d, step=7.0):
    """Turn the long straight cuts (the shire lines drawn by _split_la) into gently wandering borders, so the map looks drawn by
    hand. Each long edge is split into short pieces and nudged sideways by an amount that depends only on the edge's two ends,
    so the two areas either side of a border move it in exactly the same way and no gap opens between them."""
    import math
    out = []
    for poly in re.findall(r"M([^MZ]+)Z", d):
        p = [(float(a), float(b)) for a, b in re.findall(r"(-?[\d.]+) (-?[\d.]+)", poly)]
        res = []
        for i, a in enumerate(p):
            b = p[(i + 1) % len(p)]
            res.append(a)
            L = math.dist(a, b)
            if L < 24:
                continue
            c0, c1 = (a, b) if a <= b else (b, a)
            h = (c0[0] * 12.9898 + c0[1] * 78.233 + c1[0] * 37.719 + c1[1] * 4.581) % 6.2832
            nx, ny = -(c1[1] - c0[1]) / L, (c1[0] - c0[0]) / L
            n = int(L // step)
            amp = min(7.0, L * 0.05)
            pts = []
            for j in range(1, n):
                t = j / n
                w = math.sin(math.pi * t) * amp * (0.65 * math.sin(t * 9.1 + h) + 0.35 * math.sin(t * 23.7 + 2 * h))
                pts.append((c0[0] + (c1[0] - c0[0]) * t + nx * w, c0[1] + (c1[1] - c0[1]) * t + ny * w))
            res.extend(pts if a == c0 else pts[::-1])
        out.append("M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in res) + " Z")
    return " ".join(out)


def wales_in_10_page():
    sc, k, minx, maxy = geo["sc"], geo["k"], geo["minx"], geo["maxy"]
    kg = {x["id"]: x for x in D.KINGDOMS}
    stages = {"land": dict(en="Wales", cy="Cymru", groups=[["Wales", "Cymru", "#3d7a55", "*", ["", ""]]]),
              "first": dict(en="The oldest places", cy="Y lleoedd hynaf", groups=[["Wales", "Cymru", "#3d7a55", "*", ["", ""]]])}
    for st in S10.STEPS:
        if st[0] not in stages:
            if st[0] not in kg:
                raise SystemExit(f"src/story10.py: unknown map stage {st[0]!r}")
            x = kg[st[0]]
            stages[st[0]] = dict(en=x["en"], cy=x["cy"], groups=x["groups"])
    pins = {}
    for i, ids in S10.PINS.items():
        out = []
        for pid in ids:
            if pid not in PLACE_BY_ID:
                raise SystemExit(f"src/story10.py: unknown place {pid!r} in PINS")
            p = PLACE_BY_ID[pid]
            out.append([round((p["lon"] - minx) * k * sc), round((maxy - p["lat"]) * sc), p["en"], p["cy"], f"place-{pid}.html"])
        pins[i] = out
    n = len(S10.STEPS)
    steps = ""
    for i, (stage, when, ten, tcy, pen, pcy, links) in enumerate(S10.STEPS):
        h = "h1" if i == 0 else "h2"
        body = "".join(f"<p>{bi(a, b)}</p>" for a, b in zip(pen, pcy))
        more = "".join(f'<a href="{u}">{bi(a, b)} →</a>' for u, a, b in links)
        eyebrow = (f'<p class="eyebrow">{bi(when, when.replace("BC", "CC").replace("AD ", "").replace("today", "heddiw").replace("c. ", "tua "))}</p>' if when
                   else f'<p class="eyebrow">{bi("Wales in 10 minutes", "Cymru mewn 10 munud")}</p>')
        steps += (f'<article class="w10-step{" on" if i == 0 else ""}" data-i="{i}" data-stage="{stage}"><div class="w10-card">'
                  f'<span class="w10-n">{i + 1} / {n}</span>{eyebrow}<{h}>{bi(ten, tcy)}</{h}>{PX.small_fig(PX.W10[i]) if i < len(PX.W10) else ""}{body}'
                  + (f'<p class="w10-more">{more}</p>' if more else "")
                  + ('<p class="w10-hint" aria-hidden="true">↓ ' + bi("Scroll", "Sgroliwch") + "</p>" if i == 0 else "")
                  + "</div></article>")
    soft = {name: _soften(d) for name, d in la.items()}
    xs, ys = [], []
    for d in soft.values():
        for a, b in re.findall(r"(-?[\d.]+) (-?[\d.]+)", d):
            xs.append(float(a)); ys.append(float(b))
    x0, y0, x1, y1 = min(xs) - 70, min(ys) - 45, max(xs) + 70, max(ys) + 45
    vb = f"{x0:.0f} {y0:.0f} {x1 - x0:.0f} {y1 - y0:.0f}"
    las = "".join(f'<path class="la" data-la="{e(name)}" d="{d}"/>' for name, d in soft.items())
    shapes = "".join(f'<path d="{d}"/>' for d in soft.values())
    sea_l = "".join(f'<text class="w10-sea-l" x="{x:.0f}" y="{y:.0f}">' + bi(en, cy, "tspan") + "</text>" for x, y, en, cy in [
        (x0 + 85, y0 + 40, "Irish Sea", "Môr Iwerddon"), (x0 + 95, (y0 + y1) / 2 + 20, "Cardigan Bay", "Bae Ceredigion"),
        (x0 + 150, y1 - 22, "Bristol Channel", "Môr Hafren"), (x1 - 62, (y0 + y1) / 2 - 60, "England", "Lloegr")])
    svg = (f'<svg class="w10-svg" viewBox="{vb}" role="img" aria-label="Map of Wales / Map o Gymru"><defs>'
           f'<radialGradient id="w10-sea" cx="35%" cy="40%" r="80%"><stop offset="0" stop-color="#1d3346"/><stop offset="1" stop-color="#0d1621"/></radialGradient>'
           f'<pattern id="w10-waves" width="46" height="22" patternUnits="userSpaceOnUse"><path d="M0 11 q11.5 -7 23 0 t23 0" fill="none" stroke="#9cc3e0" stroke-opacity=".08" stroke-width="1.4"/></pattern>'
           f'<filter id="w10-blur" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="9"/></filter>'
           f'<filter id="w10-grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".035 .05" numOctaves="4" seed="7"/>'
           f'<feColorMatrix values="0 0 0 0 1  0 0 0 0 .95  0 0 0 0 .85  0 0 0 -1.4 1.05"/></filter>'
           f'<clipPath id="w10-clip">{shapes}</clipPath></defs>'
           f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" fill="url(#w10-sea)"/>'
           f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" fill="url(#w10-waves)"/>{sea_l}'
           f'<g class="w10-glow" filter="url(#w10-blur)">{shapes}</g><g class="w10-shore">{shapes}</g>'
           f'<g class="w10-coast">{shapes}</g><g id="w10-las">{las}</g>'
           f'<rect class="w10-tex" clip-path="url(#w10-clip)" x="{x0:.0f}" y="{y0:.0f}" width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" filter="url(#w10-grain)"/>'
           f'<g id="w10-pins"></g><g id="w10-labels"></g>'
           f'<g class="w10-compass" transform="translate({x1 - 42:.0f} {y0 + 48:.0f})"><path d="M0 -26 L7 0 L0 26 L-7 0Z"/><path class="n" d="M0 -26 L7 0 L-7 0Z"/><text y="-32">N</text></g></svg>')
    end = (f'<article class="w10-step w10-end" data-i="{n - 1}" data-stage="{S10.STEPS[-1][0]}"><div class="w10-card"><p class="eyebrow">{bi("You made it", "Da iawn")}</p>'
           f'<h2>{bi("Now go deeper", "Nawr ewch yn ddyfnach")}</h2><p>{bi("Every age has its own page, with the people, the places and the stories in full.", "Mae gan bob oes ei thudalen ei hun, gyda’r bobl, y lleoedd a’r straeon yn llawn.")}</p>'
           f'<p class="w10-more"><a href="timeline.html">{bi("The timeline", "Y llinell amser")} →</a><a href="index.html#chapters">{bi("The nine ages", "Y naw oes")} →</a>'
           f'<a href="quiz.html">{bi("Test yourself", "Profwch eich hun")} →</a></p>{SHARE_BTN}</div></article>')
    main = (f'<div class="w10"><p class="crumbs wrap"><a href="index.html">{SITE}</a> / {bi("Wales in 10 minutes", "Cymru mewn 10 munud")}</p>'
            f'<div class="w10-grid"><div class="w10-map" aria-hidden="false"><div class="w10-bar"><i id="w10-bar"></i></div>{svg}'
            f'<p class="w10-stage" id="w10-stage" aria-live="polite"></p><p class="w10-places" id="w10-places"></p></div>'
            f'<div class="w10-steps">{steps}{end}</div></div></div>'
            f'<section class="tight w10-refs"><div class="wrap narrow">{refs_block("wales-in-10")}</div></section>')
    data = json.dumps(dict(stages=stages, pins=pins), ensure_ascii=False, separators=(",", ":"))
    extra = "<script>window.W10=" + data.replace("</", "<\\/") + ";</script><script>" + read("wales10.js") + "</script>\n"
    return page("wales-in-10.html", "Wales in 10 minutes · History of Wales",
                "The whole story of Wales in seventeen short steps, from the first people to the Senedd, told beside a map that changes as you scroll.",
                main, era="medieval", extra=extra)


style += read("wales10.css")


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


def ruler_li(x, chips="", rid=""):
    link = x["link"]
    more = ""
    if link:
        more = f'<a class="wl" href="{link}">{e(x["name"])}</a>'
    note = f'<p>{bi(x["en"], x["cy"])}</p>' if x["en"] else ""
    links = more + (f'<div class="links">{chips}</div>' if chips else "")
    return (f'<li{f' id="{rid}"' if rid else ""} class="{" ".join(c for c in ("wl-card" if link else "", "key" if x["key"] else "") if c)}"><time>{bi(x["dates"], cy_dates(x["dates"]))}</time>'
            f'<div><h3>{e(x["name"])}</h3>{note}{links}</div></li>')


def ruler_anchor(name, seen):
    """The anchor of a ruler on a kingdom page (kings-gwynedd.html#k-cadfan-ap-iago); search links to it."""
    a = "k-" + _ft_slug(name)
    n = 2
    while a in seen:
        a = f"k-{_ft_slug(name)}-{n}"
        n += 1
    seen.add(a)
    return a


def ruler_list(items):
    out, cur, seen = "", [], set()
    def flush():
        return f'<ol class="era-events royal">{"".join(cur)}</ol>' if cur else ""
    for x in items:
        if x["k"] == "h":
            out += flush(); cur = []
            out += f'<h2 class="sub-h royal-h">{bi(x["en"], x["cy"])}</h2>'
        elif x["k"] == "n":
            cur.append(f'<li class="gap"><time aria-hidden="true">· · ·</time><div><p>{bi(x["en"], x["cy"])}</p></div></li>')
        else:
            cur.append(ruler_li(x, rid=ruler_anchor(x["name"], seen)))
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
.era-events.royal li:target { scroll-margin-top: 6rem; background: color-mix(in srgb, var(--gold, #e8c65a) 12%, transparent); border-radius: 10px; outline: 1px solid color-mix(in srgb, var(--gold, #e8c65a) 45%, transparent); outline-offset: 4px }
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
    one = (f'<div class="behind one-king"><p class="eyebrow">{bi("1055–1063 · One king of all Wales", "1055–1063 · Un brenin ar Gymru gyfan")}</p>'
           f'<h2>{bi("Gruffudd ap Llywelyn, King of Wales", "Gruffudd ap Llywelyn, Brenin Cymru")}</h2>'
           + paras(RY.GRUFFUDD["en"], RY.GRUFFUDD["cy"]) +
           f'<p><a class="go" href="person-gruffudd-ap-llywelyn.html">{bi("Read his story", "Darllen ei hanes")} →</a> &nbsp; <a class="go" href="map.html#kingdoms">{bi("See his Wales on the kingdoms map", "Gweld ei Gymru ar fap y teyrnasoedd")} →</a></p></div>')
    main = (hero("kings", f'<a href="index.html">{SITE}</a>', "crown", "c. 450–1415", "tua 450–1415", "Kings and princes of Wales", "Brenhinoedd a thywysogion Cymru",
                 "For a thousand years Wales was a land of kingdoms. Great kings brought most of it together, one king ruled it all, and its princes carried the title Prince of Wales.",
                 "Am fil o flynyddoedd gwlad o deyrnasoedd oedd Cymru. Daeth brenhinoedd mawr â’r rhan fwyaf ohoni ynghyd, rheolodd un brenin y cyfan, a dygodd ei thywysogion y teitl Tywysog Cymru.", art="castle")
            + section(one, top=True)
            + section(lst(RY.MOST), "Kings who ruled most or all of Wales", "Brenhinoedd a reolodd y rhan fwyaf o Gymru neu’r cyfan ohoni")
            + section('<span id="princes"></span>' + lst(RY.PRINCES) + f'<p class="lede" style="margin-top:1.5rem">{bi(RY.CODA["en"], RY.CODA["cy"])} <a href="person-harri-tudur.html">{bi("Harri Tudur", "Harri Tudur")} →</a></p>', "Princes of Wales", "Tywysogion Cymru")
            + section(f'<div class="behind one-king wl-card"><p class="eyebrow">{bi("Rhodri Mawr to Harri Tudur", "Rhodri Mawr i Harri Tudur")}</p><h2>{bi("Royal family trees", "Coed teulu brenhinol")}</h2>'
                      f'<p>{bi("The royal houses of Wales were one great family. See how Gwynedd, Deheubarth, Powys and Gwent married into one another, and how their blood came to the throne at Bosworth with Harri Tudur. Tap anyone to light up their line.", "Un teulu mawr oedd tai brenhinol Cymru. Gwelwch sut y priododd Gwynedd, Deheubarth, Powys a Gwent â’i gilydd, a sut y daeth eu gwaed i’r orsedd yn Bosworth gyda Harri Tudur. Tapiwch unrhyw un i oleuo’i linach.")}</p>'
                      f'<a class="wl" href="family-trees.html">{bi("Royal family trees", "Coed teulu brenhinol")}</a></div>')
            + section(f'<div class="behind one-king wl-card"><p class="eyebrow">{bi("Cyfraith Hywel · about 945 to 1543", "Cyfraith Hywel · tua 945 i 1543")}</p><h2>{bi("The Laws of Hywel Dda", "Cyfreithiau Hywel Dda")}</h2>'
                      f'<p>{bi("The kings of Wales ruled by a law of their own for six hundred years. Read how it was made at Whitland, what it said about crime, honour, marriage and land, and see the manuscripts that carried it.", "Rheolai brenhinoedd Cymru dan eu cyfraith eu hunain am chwe chan mlynedd. Darllenwch sut y’i lluniwyd yn Hendy-gwyn, beth a ddywedai am drosedd, anrhydedd, priodas a thir, a gwelwch y llawysgrifau a’i cariodd.")}</p>'
                      f'<a class="wl" href="laws.html">{bi("The Laws of Hywel Dda", "Cyfreithiau Hywel Dda")}</a></div>')
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
WELSH_JS_VER = 3  # raise whenever src/welsh.js changes, so browsers fetch the new copy
AUDIO_DIR = os.path.join(SRC, "static", "audio")
AUDIO_FILES = sorted(f[:-4] for f in os.listdir(AUDIO_DIR) if f.endswith(".mp3")) if os.path.isdir(AUDIO_DIR) else []
LL_CREDITS = json.loads(read("audio_credits.json")) if os.path.exists(os.path.join(SRC, "audio_credits.json")) else {}
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
    if LL_CREDITS:  # real speakers (tools/fetch_audio.py), grouped by speaker; then the Welsh voice (tools/make_voice.py)
        by, made = {}, []
        for k, c in LL_CREDITS.items():
            if k not in AUDIO_FILES:
                continue
            if c.get("kind") == "voice":
                made.append(c)
            else:
                by.setdefault((c["speaker"], c["licence"]), []).append(c)
        n = sum(len(v) for v in by.values())
        if by:
            credits += ("<details class=\"cyw-credits\" id=\"voices\" open><summary>" + bi(f"Real Welsh voices: {n} recordings from Lingua Libre, with thanks to the speakers",
                                                                         f"Lleisiau Cymraeg go iawn: {n} o recordiadau o Lingua Libre, gyda diolch i’r siaradwyr") + "</summary><p>"
                        + "</p><p>".join(f'<b>{e(who)}</b> ({e(lic)}): ' + ", ".join(f'<a href="{e(c["page"])}" lang="cy">{e(c["text"])}</a>' for c in sorted(cs, key=lambda c: c["text"].lower()))
                                         for (who, lic), cs in sorted(by.items(), key=lambda x: -len(x[1]))) + "</p>")
            if made:
                c0 = made[0]
                credits += ("<p>" + bi(f"The other {len(made)} words and phrases are spoken by a Welsh computer voice trained by Bangor University’s language technology unit (techiaith), run with the open Piper speech engine",
                                       f"Mae’r {len(made)} o eiriau ac ymadroddion eraill yn cael eu dweud gan lais cyfrifiadur Cymraeg a hyfforddwyd gan Uned Technolegau Iaith Prifysgol Bangor (techiaith), drwy’r peiriant lleferydd agored Piper")
                            + f' (<a href="https://huggingface.co/datasets/techiaith/bu-tts-cy-en">BU-TTS</a>, {e(c0.get("licence", "").replace("CC-BY", "CC BY"))}; <a href="{e(c0["page"])}">Piper</a>). '
                            + bi("A real speaker’s recording replaces it whenever one is shared on Lingua Libre.", "Daw recordiad siaradwr go iawn yn ei le pan rennir un ar Lingua Libre.") + "</p>")
            credits += "</details>"
    note = (f'<div class="cyw-note"><p>{bi("Every speaker button plays real Welsh: a Welsh speaker’s own recording where one has been shared on Lingua Libre, and otherwise Bangor University’s Welsh voice. You hear the same sound on every phone and computer.", "Mae pob botwm sain yn chwarae Cymraeg go iawn: recordiad siaradwr Cymraeg lle mae un wedi’i rannu ar Lingua Libre, a llais Cymraeg Prifysgol Bangor fel arall. Rydych chi’n clywed yr un sain ar bob ffôn a chyfrifiadur.")}</p>'
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
        more = f'<a class="wl" href="{link}">{bi(x["en"], x["cy"])}</a>'
    feast = f'<p class="feast">{bi("Feast day " + feast_txt(x["feast"])[0], "Dydd gŵyl " + feast_txt(x["feast"])[1])}</p>' if x["feast"] else ""
    places = "".join(ll_chip(n) for n in x["places"])
    places = f'<div class="ll-chips" aria-label="Places named after them">{places}</div>' if places else ""
    links = more + (f'<div class="links">{chips}</div>' if chips else "")
    return (f'<li id="s-{x["id"]}" class="{" ".join(c for c in ("wl-card" if link else "", "key" if x["key"] else "") if c)}"><time>{bi(x["dates"], cy_dates(x["dates"]))}</time>'
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
.today-card h3, .today-card h2 { margin: 0; font: 400 clamp(1.8rem, 4.5vw, 2.6rem)/1.05 var(--f-display) }
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
    lead = (f'<div class="behind one-king"><p class="eyebrow">{bi("Feast day 1 March · Patron saint of Wales", "Dydd gŵyl 1 Mawrth · Nawddsant Cymru")}</p>'
            f'<h2>{bi("Dewi Sant, Saint David", "Dewi Sant")}</h2>' + paras(SA.DEWI["en"], SA.DEWI["cy"]) +
            f'<p><a class="go" href="person-dewi-sant.html">{bi("Read his story", "Darllen ei hanes")} →</a> &nbsp; <a class="go" href="saints-dyfed.html">{bi("The saints of Dyfed", "Seintiau Dyfed")} →</a> &nbsp; <a class="go" href="place-stdavids.html">{bi("Visit St Davids", "Ymweld â Thyddewi")} →</a></p></div>')
    today = (f'<div class="today-card" id="today-saint"><p class="eyebrow">{bi("The saints’ calendar", "Calendr y saint")}</p>'
             f'<h2 class="h3">{bi(dewi["en"], dewi["cy"])}</h2><p>{bi("Every saint on this page has a feast day. Their days are listed in the calendar at the foot of the page.", "Mae gan bob sant ar y dudalen hon ddydd gŵyl. Rhestrir eu dyddiau yn y calendr ar waelod y dudalen.")}</p></div>')
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
    badge = f'<a class="first-badge" href="firsts.html#f-{slug}" data-kind="{f[0]}"><b>★ {bi(*lab)}</b> {bi(f[1], f[2])}</a>'
    src = CITE.FIRST_CITES.get(slug)
    if not src:
        return badge
    # a chip can't sit inside the badge link, so it goes beside it
    return f'<div class="first-row">{badge}<span class="first-src">[[cite:{src}]]</span></div>'


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
            f'<p><a class="go" href="story-firsts.html">{bi("Read the long read: Wales did it first", "Darllen yr erthygl: Cymru oedd y cyntaf")} →</a> &nbsp; <a class="go" href="people.html?field=first">{bi("See them among all the famous Welsh people", "Eu gweld ymhlith holl enwogion Cymru")} →</a></p>')
    note = bi("Some firsts are firsts for the world, some for Britain, and some are records. Where a claim rests on tradition, as with Madog, we say so. Tap any card to read the full story.",
              "Mae rhai’n bethau cyntaf i’r byd, rhai i Brydain, a rhai’n recordiau. Lle mae honiad yn dibynnu ar draddodiad, fel gyda Madog, rydym yn dweud hynny. Tapiwch unrhyw gerdyn i ddarllen yr hanes llawn.")
    main = (hero("industrial", f'<a href="index.html">{SITE}</a> / <a href="people.html">{bi("People", "Pobl")}</a>', "book", "From c. 410 to today", "O tua 410 hyd heddiw",
                 "Welsh world firsts", "Cymru oedd y cyntaf", "The things Wales and the Welsh gave the world first, and the people who did them.",
                 "Y pethau a roddodd Cymru a’r Cymry i’r byd gyntaf, a’r bobl a’u gwnaeth.", art="terrace")
            + section(lede + chips, top=True)
            + section(world, "World firsts and records", "Pethau cyntaf a recordiau’r byd")
            + section(home, "Firsts for Wales, and Welsh firsts abroad", "Pethau cyntaf i Gymru, a Chymry cyntaf dramor")
            + section(f'<p class="note-box">{note}</p><div class="pager" style="margin-top:2rem"><a class="btn" href="story-firsts.html">← {bi("Wales did it first", "Cymru oedd y cyntaf")}</a><a class="btn solid" href="people.html">{bi("All the people", "Yr holl bobl")} →</a></div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": "Welsh world firsts", "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    js = ("<script>(function(){var b=document.querySelector('.firsts-filter');if(!b)return;b.onclick=function(ev){var c=ev.target.closest('.chip');if(!c)return;var v=c.dataset.v;"
          "b.querySelectorAll('.chip').forEach(function(x){x.setAttribute('aria-pressed',x===c)});"
          "document.querySelectorAll('.first-card').forEach(function(a){a.hidden=v!=='all'&&a.dataset.field!==v});};})();</script>")
    return page("firsts.html", "Welsh world firsts · History of Wales",
                "Everything Wales and the Welsh did first: the equals sign, π, the fuel cell, the microphone, the first steam locomotive, mail order, packet switching, the spare wheel and more.",
                main, era="industrial", ld=ld, og_type="website", active="firsts.html", track="firsts", extra=js)


# ---------- index ----------
HOME_STORIES = 6  # long reads shown on the home page; the rest are on stories.html
N_CASTLES = len(json.loads(read("castles_data.json")))  # the castle sites on castles.html, also the figure in the home page's opening
FEATURED = ["dewi-sant", "hywel-dda", "gwenllian", "llywelyn-fawr", "llywelyn-ap-gruffudd", "dafydd-ap-gwilym", "owain-glyndwr", "harri-tudur", "william-morgan", "lloyd-george", "aneurin-bevan", "betty-campbell"]
DATA = dict(
    ERAS=D.ERAS, EVENTS=D.EVENTS, PLACES=[dict(p, ph=place_ph(p['id']), vis=map_visit(p)) for p in D.PLACES], PEOPLE=D.PEOPLE, READING=D.READING, ONLINE=D.ONLINE,
    CENSUS=D.CENSUS, KINGDOMS=D.KINGDOMS, LA=la, DICT=D.DICT, SAMPLES=D.SAMPLES, WORDS=D.WORDS,
    TRAILS=[dict(id=t["id"], en=t["en"], cy=t["cy"], ill=t["ill"], n=len(trail_stops(t)), introEn=t["introEn"][0], introCy=t["introCy"][0]) for t in L.TRAILS],
    AUDIO=sorted(f[:-4] for f in os.listdir(os.path.join(SRC, 'static', 'audio')) if f.endswith('.mp3')) if os.path.isdir(os.path.join(SRC, 'static', 'audio')) else [],
    MAPC=dict(minx=geo["minx"], maxy=geo["maxy"], k=geo["k"], sc=geo["sc"]),
    SL={i: x["id"] for i, ev in enumerate(D.EVENTS) for x in story_links("events", ev[5])},
    EVS=EP.SLUG,  # the page of each event: event-<slug>.html (src/eventpages.py)
    KGLINK={"Gwynedd": "kings-gwynedd.html", "Powys": "kings-powys.html", "Ceredigion": "kings-ceredigion.html", "Dyfed": "kings-dyfed.html", "Brycheiniog": "kings-brycheiniog.html",
            "Rhwng Gwy a Hafren": "kings-gwy-a-hafren.html", "Glywysing": "kings-glywysing.html", "Morgannwg": "kings-glywysing.html", "Gwent": "kings-gwent.html", "Deheubarth": "kings-deheubarth.html",
            "Rhodri Mawr": "person-rhodri-mawr.html", "Hywel Dda": "person-hywel-dda.html", "Gruffudd ap Llywelyn": "kings.html", "Principality of Wales": "kings.html#princes",
            "Owain Glyndŵr, Prince of Wales": "person-owain-glyndwr.html"},
    FACTS=[[CITE.linked(en, h, js=True), CITE.linked(cy, h, cy=True, js=True), h] for en, cy, h in F.FACTS], FEATURED=FEATURED, PPH=dict({k: photo_url(v[0], 240) for k, v in PH.PERSON_PHOTOS.items()}, **{k[7:]: f'gallery/{k}-s.webp' for k in GP.GALLERY if k.startswith('person-')}),
    PFIELDS=P2.FIELDS, PFIELD=P2.FIELD, PFIRST={k: [v[0], v[1], v[2]] for k, v in P2.FIRSTS.items()},
)
# ---------- home page, map and people: content built into the HTML, so it shows without JavaScript ----------
# (search engines, link previews and people with scripts off see it; app.js then redraws the same boxes when it runs)
def _initials(n):
    w = re.sub(r"\b(ap|ab|ferch|the|of|yr|y)\b", " ", n, flags=re.I).split()
    return (w[0][0] + (w[-1][0] if len(w) > 1 else "")).upper() if w else ""


def ssr_person(p):
    """One person card, the same markup app.js draws."""
    slug = p[0]
    other = p[4] if p[4] != p[3] else ""
    ph = DATA["PPH"].get(slug)
    first = P2.FIRSTS.get(slug)
    return (f'<article class="plaque wl-card" data-era="{p[1]}"><div class="top-row"><span class="ava" aria-hidden="true">{e(_initials(p[3]))}'
            + (f'<img src="{e(ph)}" alt="" width="96" height="96" loading="lazy" referrerpolicy="no-referrer" onerror="this.remove()">' if ph else "")
            + f'</span><div><span class="dates">{bi(p[2], date_cy(p[2]))}</span><h3>{bi(p[3], p[4])}</h3></div></div>'
            f'<span class="epi">{bi(p[5], p[6])}{(" · " + e(other)) if other else ""}</span>'
            + (f'<span class="first-tag">★ {bi(first[1], first[2])}</span>' if first else "")
            + f'<p>{bi(p[7], p[8])}</p><a class="wl" href="person-{slug}.html">{bi(p[3], p[4])}</a></article>')


def ssr_people(slugs=None):
    ppl = {p[0]: p for p in D.PEOPLE}
    return "".join(ssr_person(ppl[s]) for s in slugs if s in ppl) if slugs else "".join(ssr_person(p) for p in D.PEOPLE)


def ssr_fact():
    days = (datetime.datetime.now(datetime.timezone.utc) - datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)).days
    f = F.FACTS[days % len(F.FACTS)]  # the same fact app.js picks for today
    return (f'<span class="l-en" lang="en">{CITE.linked(f[0], f[2])}</span><span class="l-cy" lang="cy">{CITE.linked(f[1], f[2], cy=True)}</span>')


def ssr_fact_href():
    days = (datetime.datetime.now(datetime.timezone.utc) - datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)).days
    return F.FACTS[days % len(F.FACTS)][2]


WEEKDAYS = [("Mon", "Llun"), ("Tue", "Maw"), ("Wed", "Mer"), ("Thu", "Iau"), ("Fri", "Gwe"), ("Sat", "Sad"), ("Sun", "Sul")]


def otd_home_row(r, show_date):
    """One row of the home page On this day panel: a picture, when, the title and one line. The whole row is a link (app.js draws the same)."""
    md, y, k, te, tc, le, lc, link, era, pic = r
    tag = OTD_TAG.get(k)
    m = int(md[:2]) - 1
    bits = []
    if show_date:
        bits.append(f'<span class="dt">{int(md[3:])} {bi(MONTHS[m][0][:3], MONTHS[m][1])}</span>')
    if y is not None:
        bits.append(f'<span class="y">{y}</span>')
    if tag:
        bits.append(f'<span class="k">{bi(*tag)}</span>')
    href = link or f"onthisday.html#d-{md}"
    return (f'<li class="otd-row wl-card" data-era="{era}"><span class="otd-pic"><img src="{e(pic)}" alt="" width="96" height="96" loading="lazy" decoding="async"></span>'
            f'<div class="otd-txt"><p class="otd-meta">{"".join(bits)}</p><h3>{bi(te, tc)}</h3><p>{bi(le, lc)}</p></div>'
            f'<a class="wl" href="{e(href)}">{bi(te, tc)}</a></li>')


def ssr_today():
    """On this day: the build day's anniversaries (the site is rebuilt every morning). app.js redraws it with the visitor's own date."""
    day = _today()
    md = day.strftime("%m-%d")
    rows = otd_rows()
    by_day = {}
    for r in rows:
        by_day.setdefault(r[0], []).append(r)
    hit = by_day.get(md, [])
    near = False
    if not hit:  # nothing on this exact day: the closest dates either side
        for k in range(1, 200):
            a = (day - datetime.timedelta(days=k)).strftime("%m-%d")
            b = (day + datetime.timedelta(days=k)).strftime("%m-%d")
            if a in by_day or b in by_day:
                hit = by_day.get(a, [])[:2] + by_day.get(b, [])[:2]
                break
        near = True
    shown = hit[:3]
    m = int(md[:2]) - 1
    week = ""
    for k in range(-3, 4):
        d = day + datetime.timedelta(days=k)
        dm = d.strftime("%m-%d")
        n = len(by_day.get(dm, []))
        wd = WEEKDAYS[d.weekday()]
        week += (f'<button type="button" class="otd-wd{" on" if k == 0 else ""}{" has" if n else ""}" data-otd-day="{dm}" aria-pressed="{"true" if k == 0 else "false"}">'
                 f'<span class="w">{bi(*wd)}</span><span class="n">{d.day}</span><i aria-hidden="true">{"".join("<b></b>" for _ in range(min(n, 3)))}</i></button>')
    pic = shown[0][9] if shown else PX._parse(PX.ERA["medieval"])["small"]
    note = (f'<p class="otd-near">{bi("Nothing we know of happened on exactly this day. Here are the nearest dates.", "Ni wyddom am ddim a ddigwyddodd ar union y diwrnod hwn. Dyma’r dyddiadau agosaf.")}</p>' if near else "")
    more = (f'<button type="button" class="otd-more" data-otd="more">+{len(hit) - len(shown)} {bi("more on this day", "arall ar y dydd hwn")}</button>' if len(hit) > len(shown) else "")
    return (f'<div class="otd-head"><img class="otd-bg" src="{e(pic)}" alt="" loading="lazy" decoding="async">'
            f'<p class="otd-date"><span class="d">{day.day}</span><span class="m">{bi(*MONTHS[m])}</span><span class="lab">{bi("Today", "Heddiw")}</span></p>'
            f'<span class="otd-nav"><button type="button" data-otd="-1" aria-label="{bi("Day before", "Y diwrnod cynt")}">‹</button><button type="button" data-otd="1" aria-label="{bi("Next day", "Y diwrnod nesaf")}">›</button></span></div>'
            f'<div class="otd-week" role="group" aria-label="{bi("Choose a day", "Dewiswch ddiwrnod")}">{week}</div>'
            f'<div class="otd-body" aria-live="polite">{note}<ul class="otd-rows">{"".join(otd_home_row(r, near) for r in shown)}</ul>{more}</div>'
            f'<a class="otd-year" href="onthisday.html#d-{shown[0][0] if shown else md}"><span class="ic" aria-hidden="true"><b>{len(rows)}</b></span>'
            f'<span class="t"><b>{bi("The whole year", "Y flwyddyn gyfan")}</b><small>{bi(f"{len(rows)} dates, day by day", f"{len(rows)} o ddyddiadau, fesul diwrnod")}</small></span><span class="ar" aria-hidden="true">→</span></a>')


def ssr_tl_teaser():
    counts = {}
    for ev in D.EVENTS:
        counts[ev[0]] = counts.get(ev[0], 0) + 1
    return (f'<a class="chip" href="timeline.html">{bi("All", "Y cyfan")} <span style="opacity:.7">{len(D.EVENTS)}</span></a>'
            + "".join(f'<a class="chip" data-era="{x["id"]}" href="timeline.html#era-{x["id"]}"><i></i>{bi(x["en"], x["cy"])} <span class="c-dates">{bi(x["spanEn"], x["spanCy"])}</span></a>' for x in D.ERAS))


def ssr_chart():
    """The census chart as a picture in the page (app.js draws the same one)."""
    C, w, h, l, r, t, b, x0, x1, ymax = D.CENSUS, 560, 260, 34, 16, 18, 28, 1891, 2021, 60
    X = lambda y: l + (y - x0) / (x1 - x0) * (w - l - r)
    Y = lambda v: t + (1 - v / ymax) * (h - t - b)
    n = lambda v: f"{v:.1f}".rstrip("0").rstrip(".")
    s = (f'<svg class="chart" viewBox="0 0 {w} {h}" width="100%" style="min-width:420px" role="img" aria-label="Line chart: Welsh speakers fell from {C[0][1]}% in {C[0][0]} to {C[-1][1]}% in {C[-1][0]}">'
         '<defs><linearGradient id="gArea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2453d" stop-opacity=".35"/><stop offset="1" stop-color="#e2453d" stop-opacity="0"/></linearGradient></defs>')
    for v in (0, 20, 40, 60):
        s += f'<line class="grid" x1="{l}" x2="{w - r}" y1="{n(Y(v))}" y2="{n(Y(v))}"/><text x="{l - 6}" y="{n(Y(v) + 3.5)}" text-anchor="end">{v}%</text>'
    for yv in (1891, 1921, 1951, 1981, 2021):
        s += f'<text x="{n(X(yv))}" y="{h - 8}" text-anchor="middle">{yv}</text>'
    pts = [f"{X(c[0]):.1f},{Y(c[1]):.1f}" for c in C]
    s += f'<path class="area" d="M{" L".join(pts)} L{n(X(2021))},{n(Y(0))} L{n(X(1891))},{n(Y(0))}Z"/><polyline class="ln" points="{" ".join(pts)}"/>'
    for i, c in enumerate(C):
        end = i == 0 or i == len(C) - 1
        s += f'<circle class="{"end" if end else ""}" cx="{n(X(c[0]))}" cy="{n(Y(c[1]))}" r="{4.5 if end else 3}"><title>{c[0]}: {c[1]}%</title></circle>'
        if end or c[0] == 2001:
            s += f'<text class="val" x="{n(X(c[0]) + (8 if i == 0 else -6))}" y="{n(Y(c[1]) - 10)}" text-anchor="{"start" if i == 0 else "end"}">{c[1]}%</text>'
    return s + "</svg>"


def ssr_books():
    def title(r):
        return f'<a href="{e(r["u"])}" target="_blank" rel="noopener"><b>{e(r["t"])}</b></a>' if r.get("u") else f"<b>{e(r['t'])}</b>"
    return "".join(f"<li>{title(r)}<span>{bi(r['n'], r['nCy'])}</span></li>" for r in D.READING)


def ssr_online():
    def short(u):
        return re.sub(r"/$", "", re.sub(r"^https://(www[.])?", "", u))
    def li(r):
        cy = r.get("uCy") or r["u"]
        if cy == r["u"]:
            return f'<li><a href="{e(r["u"])}" target="_blank" rel="noopener"><b>{bi(r["t"], r.get("tCy", r["t"]))}</b></a><span>{e(short(r["u"]))}</span></li>'
        return (f'<li><a class="l-en" lang="en" href="{e(r["u"])}" target="_blank" rel="noopener"><b>{e(r["t"])}</b></a>'
                f'<a class="l-cy" lang="cy" href="{e(cy)}" target="_blank" rel="noopener"><b>{e(r.get("tCy", r["t"]))}</b></a>'
                f'<span>{bi(short(r["u"]), short(cy))}</span></li>')
    return "".join(li(r) for r in D.ONLINE)


def ssr_words():
    return "".join(f'<li><b>{e(w[0])}</b><span class="say">{e(w[1])}</span><span>{bi(w[2], w[3])}</span></li>' for w in D.WORDS)


def _proj(lat, lon):
    return ((lon - geo["minx"]) * geo["k"] * geo["sc"], (geo["maxy"] - lat) * geo["sc"])


def ssr_grat():
    g = ""
    for la in (51.5, 52, 52.5, 53):
        y = _proj(la, 0)[1]
        g += f'<path class="grat" d="M-30 {y:.1f}H640"/><text class="grat-l" x="640" y="{y - 5:.1f}" text-anchor="end">{la:.1f}°N</text>'
    for lo in (-5, -4, -3):
        x = _proj(52, lo)[0]
        g += f'<path class="grat" d="M{x:.1f} -20V700"/><text class="grat-l" x="{x + 5:.1f}" y="-12">{abs(lo)}°W</text>'
    return g


def ssr_pins(sel="caernarfon", links=True, labels=True):
    """Every place on the map. With links, each pin opens its own page when scripts are off."""
    out = ""
    for p in D.PLACES:
        x, y = _proj(p["lat"], p["lon"])
        right = x > 430
        lbl = f'<text class="lbl" x="{-14 if right else 14}" y="4" text-anchor="{"end" if right else "start"}">{e(p["en"])}</text>' if labels else ""
        g = (f'<g class="pin{" sel" if p["id"] == sel else ""}" data-era="{p["era"]}" data-pid="{p["id"]}" transform="translate({x:.1f} {y:.1f})">'
             f'<circle class="halo" r="20"/><circle class="dot" r="7"/>{lbl}</g>')
        out += f'<a href="place-{p["id"]}.html" aria-label="{e(p["en"])}">{g}</a>' if links else g
    return out


def ssr_visit_line(p):
    v = map_visit(p)
    if not v:
        return ""
    return (f'<p class="pc-visit"><b>{bi("Visit", "Ymweld")}:</b> {bi(e(v[0][0].upper() + v[0][1:]), e(v[1][0].upper() + v[1][1:]))} · {bi(v[3], v[4])}'
            + (f' · {e(v[5])}' if v[5] else "")
            + (f' · <a href="{e(v[2])}" target="_blank" rel="noopener">{bi("Times and prices", "Amseroedd a phrisiau")} ↗</a>' if v[2] else "")
            + f' · <a href="{e(v[6])}" target="_blank" rel="noopener">{bi("Directions", "Cyfarwyddiadau")} ↗</a></p>')


def ssr_place_card(pid="caernarfon"):
    p = next(x for x in D.PLACES if x["id"] == pid)
    E = ERA[p["era"]]
    ph = place_ph(pid)
    art = (f'<div class="art has-photo"><img src="{e(ph[0])}" alt="{e(ph[2])}" referrerpolicy="no-referrer"></div>' if ph
           else f'<div class="art"><svg aria-hidden="true"><use href="#i-{p["ill"]}"/></svg></div>')
    return (art + f'<div style="display:grid;gap:.3rem"><h3>{bi(p["en"], p["cy"])}</h3></div>'
            f'<div class="meta"><span><b>{bi(E["en"], E["cy"])}</b></span><span>{e(p["year"])}</span><span>{p["lat"]:.3f}° N, {abs(p["lon"]):.3f}° W</span></div>'
            f'<p class="desc">{bi(p["dEn"], p["dCy"])}</p>{ssr_visit_line(p)}<div style="display:flex;gap:1.2rem;flex-wrap:wrap;align-items:center">'
            f'<a class="wl" href="place-{p["id"]}.html">{bi(p["en"], p["cy"])}</a></div>')


MAP_LABELS = [("caernarfon", "Caernarfon", "Caernarfon"), ("harlech", "Harlech", "Harlech"), ("machynlleth", "Machynlleth", "Machynlleth"),
              ("stdavids", "St Davids", "Tyddewi"), ("senedd", "Cardiff", "Caerdydd"), ("conwy", "Conwy", "Conwy"), ("tintern", "Tintern", "Tyndyrn")]


def ssr_map_teaser():
    """The home page's map: Wales, every place, a few names, and a "You" pin the town finder moves (app.js). One link to the full map."""
    lbl = ""
    for pid, en, cy in MAP_LABELS:
        p = next((x for x in D.PLACES if x["id"] == pid), None)
        if not p:
            continue
        x, y = _proj(p["lat"], p["lon"])
        right = x > 420
        lbl += (f'<g class="mlab" transform="translate({x:.1f} {y:.1f})"><circle r="11"/><text x="{-18 if right else 18}" y="7" text-anchor="{"end" if right else "start"}">'
                f'<tspan class="l-en" lang="en">{e(en)}</tspan><tspan class="l-cy" lang="cy">{e(cy)}</tspan></text></g>')
    return (f'<a class="map-teaser" href="map.html" aria-label="Open the map of Wales / Agor map Cymru">'
            f'<svg viewBox="-40 -30 680 735" aria-hidden="true" focusable="false"><path class="land" d="{geo["outline"]}"/>'
            f'<g class="pins">{ssr_pins(None, links=False, labels=False)}</g><g class="mlabs">{lbl}</g><g class="you" id="mh-you" hidden></g></svg></a>')


def map_link_cards():
    """Three whole-card links under the home page map, each with a real picture."""
    cards = [("map.html", "map.html", f"{len(D.PLACES)} historic places", f"{len(D.PLACES)} o leoedd hanesyddol", "The map of Wales", "Map Cymru",
              "Every place with its story, its age and how to visit.", "Pob lle gyda’i stori, ei oes a sut i ymweld.", "medieval"),
             ("map.html#kingdoms", "era-kings.html", f"{len(D.KINGDOMS)} moments in time", f"{len(D.KINGDOMS)} adeg mewn amser", "The kingdoms", "Y teyrnasoedd",
              "Gwynedd, Powys, Deheubarth and the rest, as the borders changed.", "Gwynedd, Powys, Deheubarth a’r lleill, wrth i’r ffiniau newid.", "kings"),
             ("castles.html", "castles.html", f"{N_CASTLES:,} castles", f"{N_CASTLES:,} o gestyll", "The castles", "Y cestyll",
              "Every castle in Wales, Welsh-built and Norman, on one map.", "Pob castell yng Nghymru, rhai Cymreig a Normanaidd, ar un map.", "tudor")]
    out = ""
    for href, pic, n_en, n_cy, t_en, t_cy, d_en, d_cy, era in cards:
        out += (f'<a class="mh-card" href="{href}" data-era="{era}"><span class="mh-pic">{PX.card_img(pic, era) or ""}</span>'
                f'<span class="mh-n">{bi(n_en, n_cy)}</span><span class="mh-t"><b>{bi(t_en, t_cy)}</b><small>{bi(d_en, d_cy)}</small></span><span class="ar" aria-hidden="true">→</span></a>')
    return out


def stories_more():
    """The tile under the long reads on the home page: a fan of their pictures and how many there are."""
    faces = "".join(f'<span>{PX.card_img(f"story-{x["id"]}.html", x.get("era")) or ""}</span>' for x in F.STORIES[HOME_STORIES:HOME_STORIES + 4])
    n = len(F.STORIES)
    return (f'<a class="more-tile rv" href="stories.html"><span class="p-faces" aria-hidden="true">{faces}</span>'
            f'<span class="t"><b>{bi(f"All {n} long reads", f"Pob un o’r {n} erthygl")}</b><small>{bi("Five-minute stories on the big questions of Welsh history.", "Straeon pum munud ar gwestiynau mawr hanes Cymru.")}</small></span>'
            f'<span class="ar" aria-hidden="true">→</span></a>')


ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
# One short question for each age on the home page, so a newcomer knows what each chapter answers (Ifan, 2026-11-12).
# Keep them proud and within EDITORIAL.md: kings are kings, the people are Britons or the Cymry.
ERA_Q = {
    "ancient": ("Who raised the great stone tombs and hillforts of Wales?", "Pwy a gododd feddrodau cerrig a bryngaerau mawr Cymru?"),
    "roman": ("How did the Britons of Wales hold out against Rome for thirty years?", "Sut y daliodd Brythoniaid Cymru eu tir yn erbyn Rhufain am ddeng mlynedd ar hugain?"),
    "saints": ("Who were the saints who gave their names to hundreds of Welsh places?", "Pwy oedd y seintiau a roddodd eu henwau i gannoedd o leoedd yng Nghymru?"),
    "kings": ("How did Rhodri Mawr and Hywel Dda draw the kingdoms of Wales together?", "Sut y tynnodd Rhodri Mawr a Hywel Dda deyrnasoedd Cymru ynghyd?"),
    "medieval": ("How did Gwynedd’s rulers come to claim authority across Wales?", "Sut y daeth rheolwyr Gwynedd i hawlio awdurdod ledled Cymru?"),
    "tudor": ("How did the Welsh Bible of 1588 help the language survive?", "Sut y helpodd Beibl Cymraeg 1588 yr iaith i oroesi?"),
    "industrial": ("How did Welsh coal, iron and slate come to power the world?", "Sut y daeth glo, haearn a llechi Cymru i bweru’r byd?"),
    "modern": ("How did the people of Wales fight to save their language?", "Sut y brwydrodd pobl Cymru i achub eu hiaith?"),
    "today": ("What has Wales done with a parliament of its own?", "Beth y mae Cymru wedi’i wneud â’i senedd ei hun?"),
}
assert set(ERA_Q) == {x["id"] for x in D.ERAS}, "every age needs a question in ERA_Q"
# On phones the nine age cards are thin strips with the picture behind a dark veil, so the 600 px picture is plenty.
# "200px" makes even a 3x phone screen (200 x 3 = 600) fetch it;
# without it phones fetched the 1400 px pictures, about 1.5 MB for the nine. Wide screens still use 40vw.
POSTER_SIZES = "(max-width: 700px) 200px, 40vw"
AGES_HTML = "".join(
    f'<a class="poster" href="era-{x["id"]}.html" data-era="{x["id"]}">{PX.card_img(f"era-{x['id']}.html", sizes=POSTER_SIZES) or A.scene(ERA_ART[x["id"]], COL[x["id"]])}<span class="shade"></span><span class="rn"><span class="vh">{bi("Age", "Oes")} </span>{ROMAN[i]}<span class="vh">: </span></span>'
    f'<span class="txt"><span class="span">{bi(x["spanEn"], x["spanCy"])}</span><h3>{bi(x["en"], x["cy"])}</h3><span class="q">{bi(*ERA_Q[x["id"]])}</span><p>{bi(x["blurbEn"], x["blurbCy"])}</p></span></a>'
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
            .replace("__STORIES__", "".join(story_card(x, k == 0) for k, x in enumerate(F.STORIES[:HOME_STORIES])))
            .replace("__NSTORIES__", str(len(F.STORIES))).replace("__NPEOPLE__", str(len(D.PEOPLE))).replace("__NPLACES__", str(len(D.PLACES)))
            .replace("__NCASTLES_FMT__", f"{N_CASTLES:,}").replace("__NCASTLES__", str(N_CASTLES))
            .replace("__TODAY__", ssr_today()).replace("__FACT__", ssr_fact()).replace("__FACTHREF__", ssr_fact_href()).replace("__TLTEASER__", ssr_tl_teaser()).replace("__CHART__", ssr_chart())
            .replace("__BOOKS__", ssr_books()).replace("__ONLINE__", ssr_online()).replace("__WORDS__", ssr_words())
            .replace("__PEOPLEHOME__", ssr_people(FEATURED[:6])).replace("__PEOPLEALL__", ssr_people()).replace("__MAPTEASER__", ssr_map_teaser()).replace("__MAPCARDS__", map_link_cards()).replace("__STORIESMORE__", stories_more())
            .replace("__WALES__", geo["outline"]).replace("__GRAT__", ssr_grat()).replace("__PINS__", ssr_pins()).replace("__PLACECARD__", ssr_place_card())
            .replace("__NEWS__", news_strip()).replace("__LEGENDS__", "".join(legend_card(x) for x in F.LEGENDS_HOME)).replace("__PLAY__", play_cards(home=True)))


index_head = head.replace("</style>", extra_css + PRINT_CSS + EXTRA_PAGE_CSS + "\n</style>", 1)
_home_style = index_head[index_head.index("<style>") + 7: index_head.index("</style>")]
index_head = re.sub(r"<title>.*?</title>\n", "", index_head, count=1)
index_head = re.sub(r'<meta name="description"[^>]*>\n', "", index_head, count=1)
_bare_head = index_head
index_head = (head_tags("History of Wales · Hanes Cymru: Welsh history, people and places",
                        "Welsh history from the first people to the Senedd: kings, princes, castles, saints and poets, with a timeline, map and games. In English and Cymraeg.",
                        "", "website") + SEO.ld_script(SEO.home_ld(BASE_URL)) + "\n" + index_head)
_body_filled = (body.replace("__WALES__", geo["outline"]).replace("__WELSHV__", str(WELSH_JS_VER))
                .replace("__DATA__", json.dumps(DATA, ensure_ascii=False, separators=(",", ":")))
                .replace("__TOWNS__", json.dumps(TW.TOWNS, ensure_ascii=False, separators=(",", ":")))
                .replace("__APP__", app)
                .replace("</body>", "") + TAIL_JS)
index_fragment = fill(index_head + _body_filled, home=True)  # no document skeleton


def app_page(path, title, desc, hero_html, section_file, active, skip):
    """A page that reuses the home page's script with only one of its sections (timeline, quiz)."""
    hero_html = PX.dress(path, None, hero_html)
    h = re.sub(r'<header class="hero" id="top">.*?</header>', lambda m: hero_html, _bare_head, count=1, flags=re.S)
    h = head_tags(title, desc, path) + SEO.ld_script(SEO.page_ld(BASE_URL, path, title, desc, "website", None, hero_html)) + "\n" + h
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
_pp_hero = (f'<header class="era-hero has-art" id="top" data-era="industrial"><div class="hero-art">{A.scene("terrace", COL["industrial"])}</div><div class="wrap"><p class="crumbs"><a href="index.html" data-cy="Hanes Cymru">History of Wales</a></p>'
            '<p class="span" data-cy="O tua 31,000 CC hyd heddiw">From c. 31,000 BC to today</p>'
            '<h1 data-cy="Y rhai a luniodd Gymru">The people who shaped Wales</h1>'
            f'<p class="lede"><span class="l-en" lang="en">{len(D.PEOPLE)} people from every age: kings and princes, poets, saints, scientists, inventors, explorers, singers, actors, sporting heroes and reformers. Each one has a page of their own and a link you can share.</span>'
            f'<span class="l-cy" lang="cy">{len(D.PEOPLE)} o bobl o bob oes: brenhinoedd a thywysogion, beirdd, seintiau, gwyddonwyr, dyfeiswyr, fforwyr, cantorion, actorion, arwyr y campau a diwygwyr. Mae gan bob un ei dudalen ei hun a dolen y gallwch ei rhannu.</span></p></div></header>')
people_fragment = app_page("people.html", "Famous Welsh people · History of Wales", f"{len(D.PEOPLE)} famous Welsh people from every age of Welsh history: kings, princes, poets, saints, scientists, inventors, singers and sporting heroes, each with their own page.",
                           _pp_hero, "people_section.html", "people.html", "#people")
_mp_hero = (f'<header class="era-hero has-art" id="top" data-era="medieval"><div class="hero-art">{A.scene("castle", COL["medieval"])}</div><div class="wrap"><p class="crumbs"><a href="index.html" data-cy="Hanes Cymru">History of Wales</a></p>'
            '<p class="span" data-cy="Map">Map</p>'
            '<h1 data-cy="Lle digwyddodd">Where it happened</h1>'
            f'<p class="lede"><span class="l-en" lang="en">{len(D.PLACES)} historic places on one map of Wales. Choose a pin to read the story behind the place, switch to Kingdoms to watch the map of Wales change, or type your town to find the history near you.</span>'
            f'<span class="l-cy" lang="cy">{len(D.PLACES)} o leoedd hanesyddol ar un map o Gymru. Dewiswch bin i ddarllen y stori y tu ôl i’r lle, newidiwch i’r teyrnasoedd i weld map Cymru’n newid, neu teipiwch eich tref i ganfod yr hanes yn eich ymyl.</span></p></div></header>')
map_fragment = app_page("map.html", "Map of Wales · History of Wales", f"An interactive map of Welsh history: {len(D.PLACES)} historic places with their stories, the kingdoms of Wales through time, and the history near you.",
                        _mp_hero, "map_section.html", "map.html", "#map")


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
    items += EP.search_items()  # every event, each to its own page (src/eventpages.py)
    items += [dict(k="trail", t=t["en"], c=t["cy"], u=f"trail-{t['id']}.html", y=["Trail", "Llwybr"], b=[t["introEn"][0], t["introCy"][0]], e="medieval") for t in L.TRAILS]
    items += [dict(k="story", t=x["en"], c=x["cy"], u=f"story-{x['id']}.html", y=[f"{x['mins']} min", f"{x['mins']} mun"], b=[x["sumEn"], x["sumCy"]], e=x["era"]) for x in F.STORIES]
    items += [dict(k="legend", t=x["en"], c=x["cy"], u=f"legend-{x['id']}.html", y=[x["place"], x["place"]], b=[x["sumEn"], x["sumCy"]], e=x["era"]) for x in F.LEGENDS]
    items.append(dict(k="page", t="About this site", c="Am y wefan hon", u="about.html", y=["About", "Amdanom"],
                      b=["Who writes History of Wales, how it is written, and how to report a mistake or a correction.", "Pwy sy’n ysgrifennu Hanes Cymru, sut y caiff ei hysgrifennu, a sut i roi gwybod am gamgymeriad neu gywiriad."], e="today"))
    items.append(dict(k="page", t="The Mabinogion", c="Y Mabinogion", u="mabinogion.html", y=["Eleven tales", "Un chwedl ar ddeg"],
                      b=["The eleven great tales of medieval Wales, the White Book and the Red Book, and Lady Charlotte Guest.", "Un chwedl fawr ar ddeg Cymru’r Oesoedd Canol, y Llyfr Gwyn a’r Llyfr Coch, a’r Arglwyddes Charlotte Guest."], e="medieval"))
    items += [dict(k="page", t=t["cy"], c=t["cy"], u="mabinogion.html#mab-" + str(k + 1), y=[t["en"], g["cy"]], b=[t["sumEn"], t["sumCy"]], e=g["era"]) for k, g in enumerate(MB.GROUPS) for t in g["tales"] if not t["link"] and t["cy"] not in MT_BY_CY]
    items += [dict(k="page", t=t["cy"], c=t["cy"], u=f'mabinogi-{t["id"]}.html', y=[t["en"], t["n"][1]], b=[t["sumEn"], t["sumCy"]], e=t["era"]) for t in MT.TALES]
    items.append(dict(k="page", t="The Laws of Hywel Dda", c="Cyfreithiau Hywel Dda", u="laws.html", y=["Cyfraith Hywel", "Cyfraith Hywel"],
                      b=["The law of Wales for six hundred years: Whitland, the three lawbooks, galanas and sarhaed, women and marriage, land, the worth of everything, the manuscripts, and a quiz.",
                         "Cyfraith Cymru am chwe chan mlynedd: Hendy-gwyn, y tri llyfr cyfraith, galanas a sarhaed, menywod a phriodas, tir, gwerth pob peth, y llawysgrifau, a chwis."], e="kings"))
    items += [dict(k="page", t=c["en"], c=c["cy"], u=f'laws.html#{c["id"]}', y=["Cyfraith Hywel", "Cyfraith Hywel"], b=[c["pEn"][0][:160], c["pCy"][0][:160]], e="kings") for c in LW.CHAPTERS]
    items.append(dict(k="page", t="The literature of Wales", c="Llenyddiaeth Cymru", u="literature.html", y=["c. 600–today", "tua 600–heddiw"],
                      b=["Fourteen centuries of Welsh poetry and prose: Taliesin, Aneirin, the Poets of the Princes, Dafydd ap Gwilym, cynghanedd, the Bible and the Eisteddfod.", "Pedair canrif ar ddeg o farddoniaeth a rhyddiaith Gymraeg."], e="medieval"))
    items += [dict(k="page", t=a["en"], c=a["cy"], u=f"literature.html#{a['id']}", y=[a["span"], a["spanCy"]], b=[a["pEn"][0], a["pCy"][0]], e=a["era"]) for a in LT.AGES]
    items.append(dict(k="page", t="Cynghanedd", c="Cynghanedd", u="literature.html#cynghanedd", y=["Poetry", "Barddoniaeth"], b=[LT.CYNG_EN[0], LT.CYNG_CY[0]], e="medieval"))
    items.append(dict(k="page", t="The great books of Wales", c="Llyfrau mawr Cymru", u="books.html", y=["Manuscripts", "Llawysgrifau"],
                      b=["The Four Ancient Books of Wales, the White Book of Rhydderch, the Hendregadredd Manuscript, the chronicles and the first printed books.", "Pedwar Llyfr Hynafol Cymru, Llyfr Gwyn Rhydderch, Llawysgrif Hendregadredd, y croniclau a’r llyfrau printiedig cyntaf."], e="medieval"))
    items += [dict(k="page", t=b["en"], c=b["cy"], u=f"books.html#{b['id']}", y=[b["date"], b["dateCy"]], b=[b["en_t"], b["cy_t"]], e="medieval") for g in LT.BOOK_GROUPS for b in g["books"]]
    items.append(dict(k="page", t="The Welsh Triads", c="Trioedd Ynys Prydain", u="triads.html", y=["Triads", "Trioedd"],
                      b=["The memory of the Island of Britain in threes: the Three Generous Men, the Three Faithful War Bands, the Three Fortunate Concealments and more.", "Cof Ynys Prydain fesul tri."], e="saints"))
    items += [dict(k="page", t=t["en"], c=t["cy"], u="triads.html", y=["Triad", "Triawd"], b=["; ".join(x[0] for x in t["three"]), "; ".join(x[1] for x in t["three"])], e="saints") for g in LT.TRIAD_GROUPS for t in g["triads"]]
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
    items.append(dict(k="page", t="Famous Welsh people", c="Pobl enwog Cymru", u="people.html", y=["People", "Pobl"], b=[f"All {len(D.PEOPLE)} people who shaped Wales, from every age, with filters by age and field", f"Pob un o’r {len(D.PEOPLE)} o bobl a luniodd Gymru, o bob oes, gyda hidlwyr yn ôl oes a maes"], e="industrial"))
    items.append(dict(k="page", t="Map of Wales: where it happened", c="Map Cymru: lle digwyddodd", u="map.html", y=["Map", "Map"], b=[f"{len(D.PLACES)} historic places on one map, the kingdoms through time, and history near you", f"{len(D.PLACES)} o leoedd hanesyddol ar un map, y teyrnasoedd drwy amser, a hanes yn eich ymyl"], e="medieval"))
    items.append(dict(k="page", t="The castles of Wales: the map", c="Cestyll Cymru: y map", u="castles.html", y=["Map", "Map"], b=[f"All {len(CASTLES)} castle sites in Wales on one map, with who built them", f"Pob un o’r {len(CASTLES)} o safleoedd cestyll yng Nghymru ar un map, gyda phwy a’u cododd"], e="medieval"))
    items += [dict(k="place", t=r["en"], c=r["cy"], u=f'castles.html#castle-{r["q"]}', y=[r["d"], castle_date_cy(r["d"])], b=[r["cur"][1] + ". " + r["cur"][4], r["cur"][2] + ". " + r["cur"][5]], e="medieval") for r in castle_rows() if r["cur"]]
    for r in RY.REALMS:  # every king and prince, linked to their line on the kingdom page
        seen = set()
        for x in r["rulers"]:
            if x["k"] != "r":
                continue
            a = ruler_anchor(x["name"], seen)
            if (x["link"] or "").startswith("person-"):
                continue  # the person page is already in the index
            items.append(dict(k="ruler", t=x["name"], c=x["name"], u=f"kings-{r['id']}.html#{a}", y=[x["dates"], cy_dates(x["dates"])],
                              b=[(x["en"] + " " if x["en"] else "") + f"Ruler of {realm_title(r)[0].replace('Kings and princes of ', '')}.",
                                 (x["cy"] + " " if x["cy"] else "") + f"Rheolwr {r['cy']}."], e=r["era"]))
    for r in castle_rows():  # every castle site, not only the ones with a story
        if r["cur"]:
            continue
        kd = CS.KINDS.get(r["kind"], ("Castle", "Castell"))
        items.append(dict(k="place", t=r["en"], c=r["cy"] or r["en"], u=f'castles.html#castle-{r["q"]}', y=[r["d"], castle_date_cy(r["d"])],
                          b=[f'{kd[0]}, {r["la"]}. On the castles map.', f'{kd[1]}, {CS.LA_CY.get(r["la"], r["la"])}. Ar fap y cestyll.'], e="medieval"))
    items.append(dict(k="page", t="Welsh world firsts", c="Cymru oedd y cyntaf", u="firsts.html", y=["Firsts", "Y cyntaf"], b=["The equals sign, π, the fuel cell, the microphone, packet switching, mail order and more: everything Wales and the Welsh did first. " + ", ".join(PERSON[k][3] for k in P2.FIRSTS if k in PERSON), "Yr hafalnod, π, y gell danwydd, y meicroffon, newid pecynnau, archebu drwy’r post a rhagor: popeth a wnaeth Cymru a’r Cymry gyntaf."], e="industrial"))
    items += RP.search_items()  # the reference pages (src/refpages.py)
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
              f'<div class="cm-side"><div id="cm-card" class="cm-card" aria-live="polite" tabindex="0">'
              f'<p class="eyebrow">{bi(f"{n_all} castle sites", f"{n_all} o safleoedd cestyll")}</p>'
              f'<h2>{bi("Choose a castle", "Dewiswch gastell")}</h2><p class="muted">{bi("Tap any dot on the map, search by name, or find the castles nearest to you. The red dots are castles built by the Welsh.", "Tapiwch unrhyw ddot ar y map, chwiliwch yn ôl enw, neu dewch o hyd i’r cestyll agosaf atoch. Cestyll a godwyd gan y Cymry yw’r dotiau coch.")}</p>'
              f'<ul class="cm-legend">{legend}</ul></div></div></div>')

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
    extra = (f'<script>var CASTLES={json.dumps(payload, ensure_ascii=False, separators=(",", ":"))};</script>\n<script src="castles.js?v=3" defer></script>\n')
    ld = {"@context": "https://schema.org", "@type": "Map", "name": "The castles of Wales", "inLanguage": ["en", "cy"], "description": f"An interactive map of {n_all} castle sites in Wales, with who built them.",
          "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page("castles.html", "The castles of Wales: interactive map · History of Wales",
                f"An interactive map of {n_all} castles in Wales, from Caernarfon and Harlech to the castles of the Welsh princes: Dolwyddelan, Castell y Bere, Dinas Brân. Who built each one, and its story.",
                main, era="medieval", ld=ld, og_type="website", active="castles.html", track="castles", extra=extra)


def write(path, text):
    text = CITE.strip(text)  # a [[cite:...]] marker that was not turned into a chip never reaches a file
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


# ---------- share pictures (tools/cards.py) ----------
CARD_KIND = [("person-", "Person", "Person"), ("event-", "On the timeline", "Ar y llinell amser"), ("place-", "Place", "Lle"), ("legend-", "Legend", "Chwedl"), ("story-", "Long read", "Erthygl"),
             ("era-", "An age of Welsh history", "Oes yn hanes Cymru"), ("kings", "Kings and princes", "Brenhinoedd"), ("saints", "Saints of Wales", "Seintiau"),
             ("trail-", "Trail", "Llwybr"), ("family-trees", "Royal family trees", "Coed teulu"), ("castles", "Castles of Wales", "Cestyll"),
             ("onthisday", "On this day", "Ar y dydd hwn"), ("firsts", "Welsh world firsts", "Y cyntaf"), ("mabinogion", "The Mabinogion", "Y Mabinogion"),
             ("literature", "The literature of Wales", "Llenyddiaeth Cymru"), ("books", "The great books of Wales", "Llyfrau mawr Cymru"), ("triads", "The Welsh Triads", "Trioedd Ynys Prydain")]
CARD_GALLERY = {"literature": "trea-book-aneirin", "books": "trea-black-book", "triads": "trea-red-book"}
GAME_PAGES = {"llys-rhosyr.html", "ride-glyndwr.html", "daily.html", "map-game.html", "names.html", "hero.html", "pairs.html", "play.html", "quiz.html"}


def card_photo(path):
    stem = path[:-5]
    stem = CARD_GALLERY.get(stem, stem)
    if stem in GP.GALLERY:
        return os.path.join(SRC, "static", "gallery", stem + ".webp")
    f = None
    if stem.startswith("person-"):
        f = (PH.PERSON_PHOTOS.get(stem[7:]) or [None])[0]
    elif stem.startswith("place-"):
        f = (PH.PLACE_PHOTOS.get(stem[6:]) or [None])[0]
    if f and f in LOCAL_PHOTOS:
        return os.path.join(SRC, "static", "photos", LOCAL_PHOTOS[f][0] + ".webp")
    return None


def make_cards(out):
    done = 0
    dragon = os.path.join(SRC, "static", "dragon-red.webp")
    for path, (title, desc, era) in CARD_JOBS.items():
        name = html.unescape(re.sub(r"\s*·\s*History of Wales$", "", title))
        kind = "Play" if path in GAME_PAGES else next((k[1] for k in CARD_KIND if path.startswith(k[0])), "History of Wales")
        if path.startswith("era-") and era in ERA:
            kind = "The ages of Wales · " + ERA[era]["spanEn"]
        elif era in ERA and kind in ("Person", "Place", "Legend", "Long read"):
            kind += " · " + ERA[era]["en"]
        CARDS.make(os.path.join(out, "cards", path[:-5] + ".jpg"), kind, CITE.strip(name), CITE.strip(html.unescape(desc)), COL.get(era or "medieval", "#f26a62"), card_photo(path), dragon)
        done += 1
    return done


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
                text = text[:m.start()] + f'<script src="data.js?v={_fp(data_js)}" defer></script>\n<script src="app.js?v={_fp(app_js)}" defer></script>' + text[m.end():]
        pages[name] = text
    if data_js is not None:
        files["data.js"] = data_js
        files["app.js"] = app_js
    return files


# ---------- the page for addresses that do not exist ----------
def not_found_page():
    base = re.sub(r"^https?://[^/]+", "", BASE_URL) or "/"
    links = [("timeline.html", "The timeline", "Y llinell amser"), ("people.html", "The people", "Y bobl"), ("map.html", "The map", "Y map"),
             ("stories.html", "Long reads", "Erthyglau"), ("legends.html", "Legends", "Chwedlau"), ("daily.html", "Today’s challenge", "Her heddiw")]
    main = (hero("medieval", f'<a href="index.html">{SITE}</a>', "book", "Page not found", "Heb ddod o hyd i’r dudalen", "This page has wandered off", "Mae’r dudalen hon wedi crwydro",
                 "Like the lost land of Cantre’r Gwaelod, it may be under the sea. The rest of Welsh history is still here.",
                 "Fel Cantre’r Gwaelod, efallai ei bod o dan y môr. Mae gweddill hanes Cymru yma o hyd.", art="ship")
            + section('<p class="lede" style="margin-bottom:1.2rem">' + bi("Try a search, or start from one of these:", "Rhowch gynnig ar chwilio, neu dechreuwch o un o’r rhain:") + '</p>'
                      + '<p style="display:flex;flex-wrap:wrap;gap:.6rem"><button type="button" class="btn solid" data-search>' + bi("Search the site", "Chwilio’r wefan") + "</button>"
                      + "".join(f'<a class="btn" href="{h}">{bi(a, b)}</a>' for h, a, b in links) + "</p>", top=True))
    doc = page("404.html", "Page not found · History of Wales", "This page could not be found. Search the history of Wales, or start from the timeline, the people or the map.", main, era="medieval", og_type="website")
    return doc.replace("<head>\n", f'<head>\n<base href="{base}">\n<meta name="robots" content="noindex">\n', 1)


import refpages as RP  # noqa: E402  (the reference pages: reference.html, a-z.html ...)
RP.setup(globals())
EP.setup(globals())
style += EP.CSS
TPK.setup(globals())
RIDE.setup(globals())
LLYS.setup(globals())
style += LLYS.CSS
style += RIDE.CSS
style += TPK.CSS
import about as AB  # noqa: E402  (the About page, the author and "last updated" lines, reporting a mistake)
AB.setup(globals())
SEO.AUTHOR = AB.author()[0] if AB.AUTHOR_EN else None
style += AB.CSS
style += CITE.CSS
style += VS.CSS
style += RP.REF_CSS + RP.TOWN_CSS + RP.BATTLE_CSS + RP.DOC_CSS + RP.TOPIC_CSS + RP.MAP_CSS


def main():
    out = os.path.join(ROOT, "_site")
    shutil.rmtree(out, ignore_errors=True)
    pages = {"index.html": wrap_doc(index_fragment), "timeline.html": wrap_doc(tl_fragment), "quiz.html": wrap_doc(quiz_fragment),
             "people.html": wrap_doc(people_fragment), "map.html": wrap_doc(map_fragment)}
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
        if x["id"] not in REF.REFS:
            print(f"WARNING: long read '{x['id']}' has no reference list. Add one to src/refs.py (real books only).")
    pages["legends.html"] = legends_index()
    pages["mabinogion.html"] = mabinogion_page()
    for i, t in enumerate(MT.TALES):
        pages[f'mabinogi-{t["id"]}.html'] = tale_page(t, i)
    pages["literature.html"] = literature_page()
    pages["books.html"] = books_page()
    for i, (b, _g) in enumerate(ALL_BOOKS):
        pages[f'book-{b["id"]}.html'] = book_page(i)
    pages["books-and-authors.html"] = bookshelf_page()
    pages["triads.html"] = triads_page()
    pages["laws.html"] = laws_page()
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
    pages["today.html"] = today_page()
    pages["wales-in-10.html"] = wales_in_10_page()
    pages["daily.html"] = game_page("daily.html", "daily", "medieval", "Daily challenge", "Her y dydd", "One event from Welsh history. Six guesses to find the year.", "Un digwyddiad o hanes Cymru. Chwe chynnig i ddyfalu’r flwyddyn.", "castle", "A daily history challenge: guess the year of an event from Welsh history in six tries.")
    pages["map-game.html"] = game_page("map-game.html", "map", "modern", "Where in Wales?", "Ble yng Nghymru?", "Tap the map where you think each place is. Five rounds, 100 points each.", "Tapiwch y map lle credwch fod pob lle. Pum rownd, 100 pwynt yr un.", "senedd", "A map game: place the castles, towns and historic sites of Wales on a blank map.", with_map=True)
    pages["names.html"] = game_page("names.html", "names", "saints", "Welsh names", "Enwau Cymraeg", "Jones, Powell, Lloyd, Vaughan: Welsh surnames are history in miniature. Look yours up, then find your name as the princes would have said it.", "Jones, Powell, Lloyd, Vaughan: mae cyfenwau Cymru’n hanes ar raddfa fach. Chwiliwch am eich un chi, yna gweld eich enw fel y byddai’r tywysogion wedi’i ddweud.", "cross", "What Welsh surnames mean and where they come from, and a patronymic name maker.")
    pages["hero.html"] = game_page("hero.html", "hero", "ancient", "Which figure from history are you?", "Pa ffigwr o hanes ydych chi?", "Six quick questions.", "Chwe chwestiwn cyflym.", "torch", "A short personality quiz: which figure from Welsh history are you most like?")
    pages["welsh.html"] = welsh_page()
    pages["pairs.html"] = game_page("pairs.html", "pairs", "modern", "Word pairs", "Parau geiriau", "Turn over two cards at a time and match each Welsh word to its meaning.", "Trowch ddau gerdyn ar y tro a pharu pob gair Cymraeg â’i ystyr.", "owl", "A memory game: match Welsh words to their meanings.")
    pages["404.html"] = not_found_page()
    pages["whatsnew.html"] = whatsnew_page()
    pages["about.html"] = AB.about_page()
    pages["llys-rhosyr.html"] = LLYS.page()  # Llys Rhosyr in 3D (src/llys.py)
    pages["ride-glyndwr.html"] = RIDE.page()  # Ride with Glyndŵr, 1400 (src/ride.py)
    pages.update(TPK.pages())  # teacher packs, one for each age (src/teachpacks.py)
    pages.update(EP.pages())  # a page for every event on the timeline (src/eventpages.py)
    pages.update(RP.pages(pages.keys()))  # the reference pages: look-it-up desk, A–Z and the rest (src/refpages.py)
    if RP.MISSING:
        print("Reference pages: links left out because the page does not exist:", ", ".join(sorted(RP.MISSING)))
    shared_files = shared_assets(pages)
    pages = WP.split(pages, BASE_URL, LANG_BOOT, LANG_TOGGLE, SEO.tidy_title, SEO.tidy_desc)  # English pages and their Welsh twins in cy/
    pages = {name: CITE.render(text, cy=name.startswith("cy/")) for name, text in pages.items()}  # sources beside the claims
    sm, marks = SEO.sitemap(BASE_URL, pages)   # every page, with the date it last changed and its pictures
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    for name in pages:   # "Last updated" on each page, and dateModified for search engines (src/about.py)
        pages[name] = AB.fill_dates(pages[name], marks.get(name, [None, today])[1])
    for name, text in pages.items():
        write(os.path.join(out, name), text)
    for name, text in shared_files.items():
        write(os.path.join(out, name), text)
    if CARDS_ON:
        print(f"Made {make_cards(out)} share pictures")
        make_today(out)
    for f in os.listdir(os.path.join(SRC, "static")):
        sp = os.path.join(SRC, "static", f)
        (shutil.copytree if os.path.isdir(sp) else shutil.copy)(sp, os.path.join(out, f))
    write(os.path.join(out, "welsh.js"), welsh_js())
    write(os.path.join(out, "onthisday.json"), json.dumps(otd_rows(), ensure_ascii=False, separators=(",", ":")))
    write(os.path.join(out, "feed.xml"), feed_xml(otd_rows()))
    write(os.path.join(out, "whatsnew.json"), json.dumps(WN.NEWS, ensure_ascii=False))
    write(os.path.join(out, "search.json"), json.dumps(search_index(), ensure_ascii=False, separators=(",", ":")))
    write(os.path.join(out, ".nojekyll"), "")
    write(os.path.join(out, "robots.txt"), SEO.robots(BASE_URL))
    write(os.path.join(out, "sitemap.xml"), sm)
    write(os.path.join(out, SEO.LASTMOD_FILE), json.dumps(marks, separators=(",", ":"), sort_keys=True))
    write(os.path.join(out, SEO.INDEXNOW_KEY + ".txt"), SEO.INDEXNOW_KEY)   # lets Bing know the site is ours (tools/indexnow.py)
    if "--artifact" in sys.argv:
        a = os.path.join(ROOT, "_artifact")
        shutil.rmtree(a, ignore_errors=True)
        write(os.path.join(a, "index.html"), index_fragment)
        for p in pages:
            if p != "index.html" and "/" not in p:
                shutil.copy(os.path.join(out, p), os.path.join(a, p))
        for f in os.listdir(os.path.join(SRC, "static")):
            if f.endswith((".png", ".svg", ".js")) and f != "sw.js":
                shutil.copy(os.path.join(SRC, "static", f), os.path.join(a, f))
        shutil.copy(os.path.join(out, "search.json"), os.path.join(a, "search.json"))
        shutil.copy(os.path.join(out, "welsh.js"), os.path.join(a, "welsh.js"))
        shutil.copy(os.path.join(out, "onthisday.json"), os.path.join(a, "onthisday.json"))
    # note when anything new first appeared (src/added.json), so the lists can show it first next time too
    AD.track("person", [p[0] for p in D.PEOPLE])
    AD.track("place", [p["id"] for p in D.PLACES])
    AD.track("set", [s[0] for s in SETS.SETS])
    for kind, xs in (("story", F.STORIES), ("legend", F.LEGENDS), ("gallery", GP.GALLERY), ("game", [g[0] for g in GAMES])):
        AD.track(kind, [x if isinstance(x, str) else x["id"] for x in xs])
    RP.track_added()
    fresh = AD.save()
    if fresh:
        print(f"New on the site, stamped in src/added.json (commit it): {', '.join(fresh[:12])}{' …' if len(fresh) > 12 else ''}")
    print(f"Built {len(pages)} pages -> {out}")


if __name__ == "__main__":
    main()
