#!/usr/bin/env python3
"""Build Hanes Cymru into a static site.

Usage:  python3 build.py            -> writes _site/ (for GitHub Pages)
        python3 build.py --artifact -> also writes _artifact/ (preview without a document skeleton)
"""
import html, json, os, re, sys, shutil
from xml.sax.saxutils import escape as xesc

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)
import data as D  # noqa: E402

BASE_URL = os.environ.get("SITE_URL", "https://tywysog85.github.io/Hanes-Cymru/")
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

# ---------- shared pieces ----------
style = head[head.index("<style>") + 7: head.index("</style>")] + extra_css
symbols = head[head.index('<svg width="0"'): head.index("</svg>", head.index('<svg width="0"')) + 6]
fonts = re.findall(r'<link [^>]+>', head)


def lang_toggle():
    return ('<div class="lang" role="group" aria-label="Language / Iaith">'
            '<button type="button" id="lang-en" aria-pressed="true">EN</button>'
            '<button type="button" id="lang-cy" aria-pressed="false">CY</button></div>')


def bi(en, cy, tag="span"):
    if en == cy:
        return e(en)
    return f'<{tag} class="l-en" lang="en">{e(en)}</{tag}><{tag} class="l-cy" lang="cy">{e(cy)}</{tag}>'


def year_label(ev, cy=False):
    y, c, end = ev[1], ev[2], ev[3]
    pre = "c. " if c else ""
    if y < 0:
        return f"{pre}{abs(y):,} {'CC' if cy else 'BC'}"
    if y < 1000:
        return f"{pre}{y} {'OC' if cy else 'AD'}"
    return f"{pre}{y}" + (f"–{end}" if end else "")


def src(s):
    return f'<a class="src" href="{WIKI}{s}" target="_blank" rel="noopener">{bi("Source", "Ffynhonnell")} ↗</a>' if s else ""


# ---------- index ----------
DATA = dict(
    ERAS=D.ERAS, EVENTS=D.EVENTS, PLACES=D.PLACES, PEOPLE=D.PEOPLE, READING=D.READING, ONLINE=D.ONLINE,
    CENSUS=D.CENSUS, KINGDOMS=D.KINGDOMS, LA=la, DICT=D.DICT, SAMPLES=D.SAMPLES, WORDS=D.WORDS,
    MAPC=dict(minx=geo["minx"], maxy=geo["maxy"], k=geo["k"], sc=geo["sc"]),
)
index_head = head.replace("</style>", extra_css + "\n</style>", 1)
index_head = index_head.replace(
    '<li><a href="#language" data-cy="Iaith">Language</a></li>',
    '<li><a href="#language" data-cy="Iaith">Language</a></li>\n      <li><a href="#quiz" data-cy="Cwis">Quiz</a></li>')
meta = (f'<link rel="canonical" href="{BASE_URL}">\n<meta property="og:title" content="Hanes Cymru">\n'
        '<meta property="og:description" content="The history of Wales, from the first people in the caves to the Senedd.">\n'
        f'<meta property="og:type" content="website">\n<meta property="og:url" content="{BASE_URL}">\n'
        '<link rel="alternate" hreflang="cy" href="' + BASE_URL + '">\n')
index_head = index_head.replace('<link rel="preconnect"', meta + '<link rel="preconnect"', 1)
index_body = body.replace("__WALES__", geo["outline"]).replace("__DATA__", json.dumps(DATA, ensure_ascii=False, separators=(",", ":"))).replace("__APP__", app)
index_fragment = index_head + index_body  # no document skeleton

# ---------- era pages ----------
LANG_BOOT = ('<script>try{if(localStorage.getItem("hc-lang")==="cy"){document.documentElement.classList.add("cy");document.documentElement.lang="cy"}}catch(e){}</script>')
LANG_JS = '''<script>(function(){var d=document.documentElement;function s(l){d.classList.toggle("cy",l==="cy");d.lang=l;document.getElementById("lang-en").setAttribute("aria-pressed",l==="en");document.getElementById("lang-cy").setAttribute("aria-pressed",l==="cy");try{localStorage.setItem("hc-lang",l)}catch(e){}}
s(d.classList.contains("cy")?"cy":"en");document.getElementById("lang-en").onclick=function(){s("en")};document.getElementById("lang-cy").onclick=function(){s("cy")};
document.addEventListener("click",function(ev){var b=ev.target.closest("[data-copy]");if(!b)return;var u=new URL(b.dataset.copy,location.href).href,o=b.innerHTML;try{navigator.clipboard.writeText(u).then(function(){b.textContent=d.classList.contains("cy")?"Wedi copïo":"Copied";setTimeout(function(){b.innerHTML=o},1600)})}catch(e){}});})();</script>'''


def era_page(i, era):
    eid = era["id"]
    prev_e = D.ERAS[i - 1] if i > 0 else None
    next_e = D.ERAS[i + 1] if i + 1 < len(D.ERAS) else None
    evs = [ev for ev in D.EVENTS if ev[0] == eid]
    ppl = [p for p in D.PEOPLE if p[1] == eid]
    plc = [p for p in D.PLACES if p["era"] == eid]
    title_en = f'{era["en"]} · Hanes Cymru'
    desc = era["blurbEn"]
    story = "".join(f'<p class="l-en" lang="en">{e(a)}</p>' for a in era["storyEn"]) + "".join(f'<p class="l-cy" lang="cy">{e(a)}</p>' for a in era["storyCy"])
    story_en = "".join(f"<p>{e(a)}</p>" for a in era["storyEn"])
    story_cy = "".join(f"<p>{e(a)}</p>" for a in era["storyCy"])
    events_html = "".join(
        f'<li class="{"key" if ev[9] else ""}" id="{e(ev[1])}-{k}"><time>{bi(year_label(ev), year_label(ev, True))}</time>'
        f'<div><h3>{bi(ev[5], ev[6])}</h3><p>{bi(ev[7], ev[8])}</p><div class="links" style="display:flex;gap:1rem;flex-wrap:wrap;margin-top:.3rem">'
        + (f'<a class="src" href="index.html#lle-{ev[10]}">{bi("On the map", "Ar y map")} →</a>' if ev[10] else "")
        + f'{src(ev[11])}</div></div></li>' for k, ev in enumerate(evs))
    people_html = "".join(
        f'<article class="plaque" id="{p[0]}" data-era="{eid}"><span class="dates">{e(p[2])}</span><h3>{bi(p[3], p[4])}</h3>'
        f'<span class="epi">{bi(p[5], p[6])}</span><p>{bi(p[7], p[8])}</p><div class="links">'
        f'<button type="button" class="copy" data-copy="#{p[0]}">{bi("Copy link", "Copïo’r ddolen")}</button>{src(p[9])}</div></article>' for p in ppl)
    places_html = "".join(
        f'<a href="index.html#lle-{p["id"]}" data-era="{eid}"><svg aria-hidden="true"><use href="#i-{p["ill"]}"/></svg><span><b>{bi(p["en"], p["cy"])}</b><span>{e(p["year"])}</span></span></a>' for p in plc)
    pager = (f'<a class="btn" href="era-{prev_e["id"]}.html">← {bi(prev_e["en"], prev_e["cy"])}</a>' if prev_e else '<a class="btn" href="index.html">← Hanes Cymru</a>') + \
            (f'<a class="btn solid" href="era-{next_e["id"]}.html">{bi(next_e["en"], next_e["cy"])} →</a>' if next_e else '<a class="btn solid" href="index.html#quiz">' + bi("Take the quiz", "Gwneud y cwis") + " →</a>")
    nav_links = "".join(f'<li><a href="era-{x["id"]}.html"{" class=on" if x["id"] == eid else ""}>{bi(x["en"], x["cy"])}</a></li>' for x in D.ERAS)
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": era["en"], "inLanguage": ["en", "cy"],
          "about": "History of Wales", "isPartOf": {"@type": "WebSite", "name": "Hanes Cymru", "url": BASE_URL}}
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title_en)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{BASE_URL}era-{eid}.html">
<meta property="og:title" content="{e(title_en)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="article">
{LANG_BOOT}
{"".join(fonts)}
<style>{style}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body data-era="{eid}">
{symbols}
<nav class="nav" aria-label="Main"><div class="wrap">
<a class="brand" href="index.html"><svg aria-hidden="true"><use href="#i-mtn"/></svg><span>Hanes Cymru</span></a>
<ul>{nav_links}</ul>
{lang_toggle()}
</div></nav>
<header class="era-hero" data-era="{eid}"><div class="wrap">
<p class="crumbs"><a href="index.html">Hanes Cymru</a> / {bi("Chapter", "Pennod")} {i + 1}</p>
<svg class="ill" aria-hidden="true"><use href="#i-{era["ill"]}"/></svg>
<p class="span">{bi(era["spanEn"], era["spanCy"])}</p>
<h1>{bi(era["en"], era["cy"])}</h1>
<p style="color:var(--muted);max-width:40rem;font-size:1.15rem">{bi(era["blurbEn"], era["blurbCy"])}</p>
</div></header>
<main>
<section><div class="wrap"><div class="story l-en" lang="en">{story_en}</div><div class="story l-cy" lang="cy">{story_cy}</div></div></section>
<section style="padding-top:0"><div class="wrap">
<h2 class="sub-h">{bi("Timeline", "Llinell amser")}</h2>
<ol class="era-events">{events_html}</ol>
</div></section>
<section style="padding-top:0"><div class="wrap">
<h2 class="sub-h">{bi("People", "Pobl")}</h2>
<div class="people">{people_html}</div>
</div></section>
{f'<section style="padding-top:0"><div class="wrap"><h2 class="sub-h">{bi("Places to visit", "Lleoedd i ymweld â nhw")}</h2><div class="era-places">{places_html}</div></div></section>' if plc else ""}
<section style="padding-top:0"><div class="wrap"><div class="pager">{pager}</div></div></section>
</main>
<footer><div class="wrap"><p class="big">Diolch.</p><nav aria-label="Ages">{"".join(f'<a href="era-{x["id"]}.html">{bi(x["en"], x["cy"])}</a>' for x in D.ERAS)}<a href="index.html#sources">{bi("Sources", "Ffynonellau")}</a></nav>
<span>{bi("Links go to Wikipedia, which lists academic sources. Dates marked c. are approximate.", "Mae’r dolenni’n mynd i Wicipedia, sy’n rhestru ffynonellau academaidd. Dyddiadau bras yw’r rhai a nodir c.")}</span></div></footer>
{LANG_JS}
</body>
</html>
'''


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
    write(os.path.join(out, "index.html"), wrap_doc(index_fragment))
    pages = ["index.html"]
    for i, era in enumerate(D.ERAS):
        name = f"era-{era['id']}.html"
        write(os.path.join(out, name), era_page(i, era))
        pages.append(name)
    write(os.path.join(out, ".nojekyll"), "")
    write(os.path.join(out, "robots.txt"), f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}sitemap.xml\n")
    write(os.path.join(out, "sitemap.xml"), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{xesc(BASE_URL + ('' if p == 'index.html' else p))}</loc></url>\n" for p in pages) + "</urlset>\n")
    if "--artifact" in sys.argv:
        a = os.path.join(ROOT, "_artifact")
        shutil.rmtree(a, ignore_errors=True)
        write(os.path.join(a, "index.html"), index_fragment)
        for p in pages[1:]:
            shutil.copy(os.path.join(out, p), os.path.join(a, p))
    print(f"Built {len(pages)} pages, {len(D.EVENTS)} events, {len(D.PEOPLE)} people, {len(D.PLACES)} places -> {out}")


if __name__ == "__main__":
    main()
