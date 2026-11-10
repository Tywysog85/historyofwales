#!/usr/bin/env python3
"""Build History of Wales into a static site.

Usage:  python3 build.py            -> writes _site/ (for GitHub Pages)
        python3 build.py --artifact -> also writes _artifact/ (preview without a document skeleton)

Environment:
  SITE_URL     public address of the site, ending in /   (default: the GitHub Pages address)
  GOATCOUNTER  your GoatCounter code, e.g. "hanescymru", to switch on visitor statistics
"""
import html, json, os, re, sys, shutil
from xml.sax.saxutils import escape as xesc

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)
import data as D  # noqa: E402
import long as L  # noqa: E402

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
extra_css = read("extra.css")
geo = json.loads(read("geo", "map.json"))
la = json.loads(read("geo", "la.json"))

style = head[head.index("<style>") + 7: head.index("</style>")] + extra_css
symbols = head[head.index('<svg width="0"'): head.index("</svg>", head.index('<svg width="0"')) + 6]
fonts = "".join(re.findall(r'<link [^>]+>', head))

ERA = {x["id"]: x for x in D.ERAS}
PERSON = {p[0]: p for p in D.PEOPLE}
PLACE = {p["id"]: p for p in D.PLACES}
EVENT_BY_TITLE = {ev[5]: ev for ev in D.EVENTS}


def bi(en, cy, tag="span", cls=""):
    if en == cy:
        return e(en)
    c = f" {cls}" if cls else ""
    return f'<{tag} class="l-en{c}" lang="en">{e(en)}</{tag}><{tag} class="l-cy{c}" lang="cy">{e(cy)}</{tag}>'


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


TAIL_JS = ('<script>if("serviceWorker" in navigator&&location.protocol==="https:"){addEventListener("load",function(){navigator.serviceWorker.register("sw.js").catch(function(){})})}</script>\n'
           + (f'<script data-goatcounter="https://{GOATCOUNTER}.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>\n' if GOATCOUNTER else ""))

LANG_BOOT = '<script>try{if(localStorage.getItem("hc-lang")==="cy"){document.documentElement.classList.add("cy");document.documentElement.lang="cy"}}catch(e){}</script>'
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


def nav(active=""):
    items = [("index.html", "Home", "Hafan"), ("index.html#timeline", "Timeline", "Llinell amser"), ("index.html#map", "Map", "Map"),
             ("trails.html", "Trails", "Llwybrau"), ("teachers.html", "Teachers", "Athrawon")]
    lis = "".join(f'<li><a href="{h}"{" class=on" if active == h else ""}>{bi(a, b)}</a></li>' for h, a, b in items)
    return (f'<a class="skip" href="#main">{bi("Skip to content", "Neidio i’r cynnwys")}</a>'
            f'<nav class="nav" aria-label="Main"><div class="wrap"><a class="brand" href="index.html"><svg aria-hidden="true"><use href="#i-mtn"/></svg>{bi("History of Wales", "Hanes Cymru")}</a>'
            f'<ul>{lis}</ul><div class="lang" role="group" aria-label="Language / Iaith"><button type="button" id="lang-en" aria-pressed="true">EN</button>'
            '<button type="button" id="lang-cy" aria-pressed="false">CY</button></div></div></nav>')


def footer():
    eras = "".join(f'<a href="era-{x["id"]}.html">{bi(x["en"], x["cy"])}</a>' for x in D.ERAS)
    return (f'<footer><div class="wrap"><p class="big">Diolch.</p><nav aria-label="{e("Site")}">{eras}<a href="trails.html">{bi("Trails", "Llwybrau")}</a>'
            f'<a href="teachers.html">{bi("For teachers", "I athrawon")}</a><a href="index.html#sources">{bi("Sources", "Ffynonellau")}</a></nav>'
            f'<span>{bi("Links go to Wikipedia, which lists academic sources. Dates marked c. are approximate.", "Mae’r dolenni’n mynd i Wicipedia, sy’n rhestru ffynonellau academaidd. Dyddiadau bras yw’r rhai a nodir c.")}</span></div></footer>')


def page(path, title, desc, main_html, era=None, og_type="article", ld=None, active=""):
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
<body{f' data-era="{era}"' if era else ""}>
{symbols}
{nav(active)}
<main id="main">
{main_html}
</main>
{footer()}
{LANG_JS}
{TAIL_JS}</body>
</html>
'''


def hero(era_id, crumbs, ill, eyebrow_en, eyebrow_cy, h_en, h_cy, sub_en="", sub_cy=""):
    return (f'<header class="era-hero" data-era="{era_id}"><div class="wrap"><p class="crumbs">{crumbs}</p>'
            f'<svg class="ill" aria-hidden="true"><use href="#i-{ill}"/></svg><p class="span">{bi(eyebrow_en, eyebrow_cy)}</p>'
            f'<h1>{bi(h_en, h_cy)}</h1>' + (f'<p class="lede">{bi(sub_en, sub_cy)}</p>' if sub_en else "") + "</div></header>")


def section(inner, title_en=None, title_cy=None, top=False):
    h = f'<h2 class="sub-h">{bi(title_en, title_cy)}</h2>' if title_en else ""
    cls = "" if top else ' class="tight"'
    return f'<section{cls}><div class="wrap">{h}{inner}</div></section>'


def event_li(ev, k=0):
    links = (f'<a class="src" href="place-{ev[10]}.html">{bi("The place", "Y lle")} →</a>' if ev[10] else "") + src(ev[11])
    return (f'<li class="{"key" if ev[9] else ""}" data-era="{ev[0]}"><time>{bi(year_label(ev), year_label(ev, True))}</time>'
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
    main = (hero(eid, f'<a href="index.html">{SITE}</a> / {bi("Chapter", "Pennod")} {i + 1}', era["ill"], era["spanEn"], era["spanCy"], era["en"], era["cy"], era["blurbEn"], era["blurbCy"])
            + section(paras(era["storyEn"], era["storyCy"]), top=True)
            + section(f'<ol class="era-events">{"".join(event_li(ev) for ev in evs)}</ol>', "Timeline", "Llinell amser")
            + section(f'<div class="people">{"".join(plaque(p) for p in ppl)}</div>', "People", "Pobl")
            + (section(f'<div class="era-places">{"".join(place_tile(p) for p in plc)}</div>', "Places to visit", "Lleoedd i ymweld â nhw") if plc else "")
            + section(f'<div class="pager">{pager}</div>'))
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": era["en"], "inLanguage": ["en", "cy"], "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": BASE_URL}}
    return page(f"era-{eid}.html", f'{era["en"]} · History of Wales', era["blurbEn"], main, era=eid, ld=ld)


# ---------- person pages ----------
def person_page(p):
    slug, eid = p[0], p[1]
    era = ERA[eid]
    long_en, long_cy = L.PEOPLE_LONG[slug]
    related = [ev for ev in D.EVENTS if p[3] in ev[7] or p[3] in ev[5] or (slug == "dewi-sant" and "Dewi" in ev[7])]
    same = [x for x in D.PEOPLE if x[1] == eid and x[0] != slug][:4]
    idx = D.PEOPLE.index(p)
    prev_p, next_p = D.PEOPLE[idx - 1] if idx > 0 else None, D.PEOPLE[idx + 1] if idx + 1 < len(D.PEOPLE) else None
    pager = (f'<a class="btn" href="person-{prev_p[0]}.html">← {bi(prev_p[3], prev_p[4])}</a>' if prev_p else f'<a class="btn" href="era-{eid}.html">← {bi(era["en"], era["cy"])}</a>') + \
            (f'<a class="btn solid" href="person-{next_p[0]}.html">{bi(next_p[3], next_p[4])} →</a>' if next_p else '<a class="btn solid" href="index.html#people">' + bi("All people", "Pawb") + " →</a>")
    meta = (f'<div class="person-meta"><span>{e(p[2])}</span><span>{bi(p[5], p[6])}</span><a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a></div>')
    main = (hero(eid, f'<a href="index.html">{SITE}</a> / <a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a>', era["ill"], p[2], p[2], p[3], p[4], p[7], p[8])
            + section(meta + paras(long_en, long_cy) + f'<p class="share no-print"><button type="button" class="btn" data-copy="person-{slug}.html">{bi("Copy link to share", "Copïo dolen i’w rhannu")}</button> {src(p[9])}</p>', top=True)
            + (section(f'<ol class="era-events">{"".join(event_li(ev) for ev in related)}</ol>', "On the timeline", "Ar y llinell amser") if related else "")
            + section(f'<div class="people">{"".join(plaque(x) for x in same)}</div>', "Also in this age", "Hefyd yn yr oes hon")
            + section(f'<div class="pager">{pager}</div>'))
    ld = {"@context": "https://schema.org", "@type": "Person", "name": p[3], "alternateName": p[4], "description": p[7], "sameAs": WIKI + p[9]}
    return page(f"person-{slug}.html", f"{p[3]} · History of Wales", p[7], main, era=eid, ld=ld, og_type="profile")


# ---------- place pages ----------
def place_page(pl):
    pid, eid = pl["id"], pl["era"]
    era = ERA[eid]
    long_en, long_cy = L.PLACE_LONG[pid]
    related = [ev for ev in D.EVENTS if ev[10] == pid]
    near = sorted([x for x in D.PLACES if x["id"] != pid], key=lambda x: (x["lat"] - pl["lat"]) ** 2 + ((x["lon"] - pl["lon"]) * 0.61) ** 2)[:3]
    osm = f'https://www.openstreetmap.org/?mlat={pl["lat"]}&mlon={pl["lon"]}#map=14/{pl["lat"]}/{pl["lon"]}'
    meta = (f'<div class="person-meta"><span>{e(pl["year"])}</span><span>{pl["lat"]:.3f}° N, {abs(pl["lon"]):.3f}° W</span>'
            f'<a href="{osm}" target="_blank" rel="noopener">{bi("Open in a map", "Agor mewn map")} ↗</a><a href="index.html#lle-{pid}">{bi("On our map", "Ar ein map")} →</a></div>')
    main = (hero(eid, f'<a href="index.html">{SITE}</a> / <a href="era-{eid}.html">{bi(era["en"], era["cy"])}</a>', pl["ill"], era["en"], era["cy"], pl["en"], pl["cy"], pl["dEn"], pl["dCy"])
            + section(meta + paras(long_en, long_cy) + f'<p class="share no-print">{src(pl["src"])}</p>', top=True)
            + (section(f'<ol class="era-events">{"".join(event_li(ev) for ev in related)}</ol>', "What happened here", "Beth ddigwyddodd yma") if related else "")
            + section(f'<div class="era-places">{"".join(place_tile(x) for x in near)}</div>', "Nearby", "Gerllaw"))
    ld = {"@context": "https://schema.org", "@type": "TouristAttraction", "name": pl["en"], "alternateName": pl["cy"], "description": pl["dEn"],
          "geo": {"@type": "GeoCoordinates", "latitude": pl["lat"], "longitude": pl["lon"]}}
    return page(f"place-{pid}.html", f'{pl["en"]} · History of Wales', pl["dEn"], main, era=eid, ld=ld, og_type="place")


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
    main = (hero("medieval", f'<a href="index.html">{SITE}</a> / <a href="trails.html">{bi("Trails", "Llwybrau")}</a>', t["ill"], "Trail", "Llwybr", t["en"], t["cy"])
            + section(paras(t["introEn"], t["introCy"]), top=True)
            + section(f'<ol class="era-events trail">{"".join(trail_item(k, r) for k, r in t["items"])}</ol>', "Stops on the trail", "Arosfannau ar y llwybr")
            + section(f'<div class="pager"><a class="btn" href="trails.html">← {bi("All trails", "Pob llwybr")}</a><a class="btn solid" href="trail-{nxt["id"]}.html">{bi(nxt["en"], nxt["cy"])} →</a></div>'))
    return page(f"trail-{t['id']}.html", f'{t["en"]} · History of Wales', t["introEn"][0], main, era="medieval", active="trails.html")


def trails_index():
    cards = "".join(f'<a class="chap" href="trail-{t["id"]}.html" data-era="{D.ERAS[i % 4]["id"]}"><svg aria-hidden="true"><use href="#i-{t["ill"]}"/></svg>'
                    f'<span class="span">{len(t["items"])} {bi("stops", "arhosfan")}</span><h3>{bi(t["en"], t["cy"])}</h3><p>{bi(t["introEn"][0], t["introCy"][0])}</p>'
                    f'<span class="go">{bi("Follow the trail →", "Dilyn y llwybr →")}</span></a>' for i, t in enumerate(L.TRAILS))
    main = (hero("modern", f'<a href="index.html">{SITE}</a>', "mtn", "Themed trails", "Llwybrau thema", "Trails through Welsh history", "Llwybrau drwy hanes Cymru",
                 "Follow one thread through the centuries.", "Dilynwch un edefyn drwy’r canrifoedd.")
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
                 "Lesson ideas, enquiry questions and printable quiz sheets for each age.", "Syniadau gwersi, cwestiynau ymholi a thaflenni cwis i’w hargraffu ar gyfer pob oes.")
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

# ---------- index ----------
DATA = dict(
    ERAS=D.ERAS, EVENTS=D.EVENTS, PLACES=D.PLACES, PEOPLE=D.PEOPLE, READING=D.READING, ONLINE=D.ONLINE,
    CENSUS=D.CENSUS, KINGDOMS=D.KINGDOMS, LA=la, DICT=D.DICT, SAMPLES=D.SAMPLES, WORDS=D.WORDS,
    TRAILS=[dict(id=t["id"], en=t["en"], cy=t["cy"], ill=t["ill"], n=len(t["items"]), introEn=t["introEn"][0], introCy=t["introCy"][0]) for t in L.TRAILS],
    MAPC=dict(minx=geo["minx"], maxy=geo["maxy"], k=geo["k"], sc=geo["sc"]),
)
index_head = head.replace("</style>", extra_css + PRINT_CSS + "\n</style>", 1)
index_head = index_head.replace(
    '<li><a href="#language" data-cy="Iaith">Language</a></li>',
    '<li><a href="#language" data-cy="Iaith">Language</a></li>\n      <li><a href="#quiz" data-cy="Cwis">Quiz</a></li>')
index_head = index_head.replace('<nav class="nav" aria-label="Main">', '<a class="skip" href="#chapters" data-cy="Neidio i’r cynnwys">Skip to content</a>\n<nav class="nav" aria-label="Main">', 1)
index_head = re.sub(r"<title>.*?</title>\n", "", index_head, count=1)
index_head = re.sub(r'<meta name="description"[^>]*>\n', "", index_head, count=1)
index_head = head_tags("History of Wales", "The history of Wales, from the first people in the caves to the Senedd: an interactive timeline, map, people and language, in English and Cymraeg.", "", "website") + index_head
index_body = (body.replace("__WALES__", geo["outline"])
              .replace("__DATA__", json.dumps(DATA, ensure_ascii=False, separators=(",", ":")))
              .replace("__APP__", app)
              .replace("</body>", "") + TAIL_JS)
index_fragment = index_head + index_body  # no document skeleton


def wrap_doc(fragment):
    i = fragment.index("</style>") + len("</style>")
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + LANG_BOOT + "\n" + fragment[:i] + "\n</head>\n<body>\n" + fragment[i:] + "\n</body>\n</html>\n")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    out = os.path.join(ROOT, "_site")
    shutil.rmtree(out, ignore_errors=True)
    pages = {"index.html": wrap_doc(index_fragment)}
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
    for name, text in pages.items():
        write(os.path.join(out, name), text)
    for f in os.listdir(os.path.join(SRC, "static")):
        shutil.copy(os.path.join(SRC, "static", f), os.path.join(out, f))
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
            if f.endswith((".png", ".svg")):
                shutil.copy(os.path.join(SRC, "static", f), os.path.join(a, f))
    print(f"Built {len(pages)} pages -> {out}")


if __name__ == "__main__":
    main()
