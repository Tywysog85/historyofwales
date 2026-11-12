"""The reference pages: the look-it-up desk (reference.html), the A–Z (a-z.html) and the pages that join it.

build.py calls setup(globals()) once, then pages() for the HTML and search_items() for search.json.
The content lives in the ref_*.py files; this file only lays it out. Every page here works in English and Cymraeg
through bi(), like the rest of the site.
"""
import json
import re

import ref_az as AZ
import ref_faq as FAQ
import ref_towns as TWN
import os

g = {}  # build.py's helpers (bi, e, page, hero, section ...), filled by setup()


def setup(build_globals):
    g.update(build_globals)


def bi(en, cy, *a, **k):
    return g["bi"](en, cy, *a, **k)


def e(s):
    return g["e"](s)


# ---------- links between pages ----------
_GENERAL = {
    "laws.html": ("The Laws of Hywel Dda", "Cyfreithiau Hywel Dda"), "kings.html": ("Kings and princes", "Brenhinoedd a thywysogion"),
    "castles.html": ("Castles map", "Map y cestyll"), "saints.html": ("Saints of Wales", "Seintiau Cymru"), "family-trees.html": ("Royal family trees", "Coed teulu brenhinol"),
    "mabinogion.html": ("The Mabinogion", "Y Mabinogion"), "symbols.html": ("Symbols and traditions", "Symbolau a thraddodiadau"), "welsh.html": ("Learn Welsh", "Dysgu Cymraeg"),
    "names.html": ("Welsh names", "Enwau Cymraeg"), "firsts.html": ("Welsh world firsts", "Cymru oedd y cyntaf"), "timeline.html": ("Timeline", "Llinell amser"),
    "onthisday.html": ("On this day", "Ar y dydd hwn"), "gallery.html": ("Photo gallery", "Oriel luniau"), "stories.html": ("Long reads", "Erthyglau"),
    "legends.html": ("Legends", "Chwedlau"), "wales-in-10.html": ("Wales in 10 minutes", "Cymru mewn 10 munud"), "trails.html": ("Themed trails", "Llwybrau thema"),
    "literature.html": ("The literature of Wales", "Llenyddiaeth Cymru"), "books.html": ("The old books of Wales", "Hen lyfrau Cymru"), "triads.html": ("The Welsh Triads", "Trioedd Ynys Prydain"),
    "a-z.html": ("The A–Z of Welsh history", "A–Y hanes Cymru"), "questions.html": ("Quick answers", "Atebion cyflym"), "towns.html": ("Towns and villages", "Trefi a phentrefi"),
    "battles.html": ("Battles of Wales", "Brwydrau Cymru"), "documents.html": ("Key documents", "Dogfennau allweddol"), "sites.html": ("Historic sites map", "Map safleoedd hanesyddol"),
    "maps.html": ("Maps through time", "Mapiau drwy’r oesoedd"), "reference.html": ("Look it up", "Chwilio’r hanes"),
}
TITLES = {}  # href -> (English, Welsh), filled in pages()
MISSING = set()


def _titles():
    if TITLES:
        return
    TITLES.update(_GENERAL)
    for p in g["D"].PEOPLE:
        TITLES[f"person-{p[0]}.html"] = (p[3], p[4])
    for p in g["D"].PLACES:
        TITLES[f"place-{p['id']}.html"] = (p["en"], p["cy"])
    for x in g["F"].STORIES:
        TITLES[f"story-{x['id']}.html"] = (x["en"], x["cy"])
    for x in g["F"].LEGENDS:
        TITLES[f"legend-{x['id']}.html"] = (x["en"], x["cy"])
    for x in g["L"].TRAILS:
        TITLES[f"trail-{x['id']}.html"] = (x["en"], x["cy"])
    for x in g["D"].ERAS:
        TITLES[f"era-{x['id']}.html"] = (x["en"], x["cy"])
    for r in g["RY"].REALMS:
        TITLES[f"kings-{r['id']}.html"] = g["realm_title"](r)
    for r in g["SA"].REGIONS:
        TITLES[f"saints-{r['id']}.html"] = (("Saints of " + r["en"]) if r["realm"] else "Saints across the sea", ("Seintiau " + r["cy"]) if r["realm"] else "Saint dros y môr")


def exists(href, have):
    return href.split("#")[0] in have


def link_chips(hrefs, have, cls="ref-see"):
    """A row of small links to other pages. Links to pages the site does not have (yet) are left out, and listed by the build."""
    out = []
    for h in hrefs:
        if not exists(h, have):
            MISSING.add(h)
            continue
        t = TITLES.get(h.split("#")[0])
        if not t:
            MISSING.add(h)
            continue
        out.append(f'<a href="{h}">{bi(*t)}</a>')
    return f'<p class="{cls}">{"".join(out)}</p>' if out else ""


def ld_article(title, desc):
    return {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "inLanguage": ["en", "cy"],
            "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": g["BASE_URL"]}}


def crumbs(here_en=None, here_cy=None):
    c = f'<a href="index.html">{g["SITE"]}</a> / <a href="reference.html">{bi("Look it up", "Chwilio’r hanes")}</a>'
    return c


FILTER_JS = r"""<script>(function(){var box=document.querySelector("[data-ref-filter]");if(!box)return;
var items=[].slice.call(document.querySelectorAll("[data-ref-item]")),groups=[].slice.call(document.querySelectorAll("[data-ref-group]")),
none=document.querySelector("[data-ref-none]"),norm=function(s){return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g,"").replace(/[’']/g,"")};
items.forEach(function(x){x._t=norm(x.textContent)});
box.addEventListener("input",function(){var q=norm(box.value.trim()),n=0;items.forEach(function(x){var on=!q||x._t.indexOf(q)>=0;x.hidden=!on;if(on)n++});
groups.forEach(function(gr){gr.hidden=!gr.querySelector("[data-ref-item]:not([hidden])")});if(none)none.hidden=n>0});
if(location.hash){var t=document.getElementById(location.hash.slice(1));if(t&&t.tagName==="DETAILS")t.open=true}})();</script>
"""

REF_CSS = """
.ref-tools{display:flex;flex-wrap:wrap;gap:.8rem;align-items:center;margin:0 0 1.4rem}
.ref-filter{flex:1 1 16rem;min-width:0;background:var(--slate);border:1px solid var(--line);border-radius:12px;color:var(--ink);font:inherit;font-size:1.05rem;padding:.75rem 1rem}
.ref-filter:focus{outline:2px solid var(--gold,#e8c65a);outline-offset:2px}
.ref-letters{display:flex;flex-wrap:wrap;gap:.3rem;margin:0 0 1.6rem;padding:0;list-style:none}
.ref-letters a{display:inline-grid;place-items:center;min-width:2.2rem;height:2.2rem;border:1px solid var(--line);border-radius:8px;text-decoration:none;color:var(--ink);font:600 .9rem var(--f-mono)}
.ref-letters a:hover{border-color:var(--gold,#e8c65a);color:var(--gold,#e8c65a)}
.ref-group{margin:0 0 2.2rem;scroll-margin-top:5rem}
.ref-group>h2{font:600 2.2rem var(--f-display);color:var(--gold,#e8c65a);margin:0 0 .6rem;border-bottom:1px solid var(--line);padding-bottom:.3rem}
.ref-list{display:grid;gap:.2rem;margin:0}
.ref-item{padding:1rem 0 1.1rem;border-bottom:1px solid var(--line);scroll-margin-top:5.5rem}
.ref-item:target{background:color-mix(in srgb,var(--gold,#e8c65a) 9%,transparent);border-radius:10px;padding-left:.8rem;padding-right:.8rem}
.ref-item dt{font:600 1.25rem/1.25 var(--f-display);margin:0 0 .35rem}
.ref-item dt small{font:500 .78rem var(--f-mono);color:var(--muted);letter-spacing:.03em;margin-left:.5rem}
.ref-item dd{margin:0;color:var(--ink);line-height:1.6;max-width:46rem}
.ref-see{display:flex;flex-wrap:wrap;gap:.4rem;margin:.6rem 0 0}
.ref-see a{font:500 .8rem var(--f-body);border:1px solid var(--line);border-radius:999px;padding:.25rem .75rem;text-decoration:none;color:var(--muted)}
.ref-see a:hover{border-color:var(--gold,#e8c65a);color:var(--ink)}
.ref-none{color:var(--muted);padding:1rem 0}
.ref-desk{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,16rem),1fr));gap:1rem}
.ref-desk a{display:grid;gap:.4rem;align-content:start;background:var(--slate);border:1px solid var(--line);border-left:3px solid var(--c,var(--gold,#e8c65a));border-radius:12px;padding:1.1rem 1.2rem 1.2rem;text-decoration:none;color:var(--ink);transition:border-color .2s,transform .2s}
.ref-desk a:hover{transform:translateY(-2px);border-color:var(--gold,#e8c65a)}
.ref-desk b{font:600 1.3rem/1.2 var(--f-display)}
.ref-desk span.n{font:500 .74rem var(--f-mono);color:var(--muted);letter-spacing:.05em;text-transform:uppercase}
.ref-desk span.d{color:var(--muted);font-size:.95rem;line-height:1.5}
.ref-jump{display:flex;flex-wrap:wrap;gap:.4rem;list-style:none;margin:0 0 2rem;padding:0}
.ref-jump a{display:inline-block;font:500 .85rem var(--f-body);border:1px solid var(--line);border-radius:999px;padding:.35rem .9rem;text-decoration:none;color:var(--ink)}
.ref-jump a:hover{border-color:var(--gold,#e8c65a)}
.ref-gh{font:600 1.7rem var(--f-display);margin:0 0 .5rem;border-bottom:1px solid var(--line);padding-bottom:.4rem}
.ref-q{border-bottom:1px solid var(--line);scroll-margin-top:5.5rem}
.ref-q summary{cursor:pointer;list-style:none;padding:1rem 2.2rem 1rem 0;font:600 1.12rem/1.35 var(--f-body);position:relative}
.ref-q summary::-webkit-details-marker{display:none}
.ref-q summary::after{content:"+";position:absolute;right:.3rem;top:.85rem;font:400 1.5rem var(--f-mono);color:var(--gold,#e8c65a)}
.ref-q[open] summary::after{content:"−"}
.ref-q summary:hover{color:var(--gold,#e8c65a)}
.ref-a{padding:0 0 1.2rem;max-width:46rem;line-height:1.65}
.ref-a p{margin:0}
.ref-q:target{background:color-mix(in srgb,var(--gold,#e8c65a) 8%,transparent);border-radius:10px;padding:0 .8rem}
.ref-big-search{display:flex;gap:.6rem;align-items:center;width:100%;max-width:40rem;background:var(--slate);border:1px solid var(--line);border-radius:14px;padding:.95rem 1.1rem;color:var(--muted);font:inherit;font-size:1.1rem;cursor:text;text-align:left;margin-top:1.2rem}
.ref-big-search svg{width:1.2rem;height:1.2rem;flex:none}
"""


# ---------- the A–Z ----------
def _letter(s):
    c = re.sub(r"[^A-Za-z]", "", s.replace("Ŵ", "W").replace("Ŷ", "Y"))[:1].upper()
    return c or "#"


def az_page(have):
    def key(t):
        s = t["en"][4:] if t["en"].lower().startswith("the ") else t["en"]
        return re.sub(r"[^a-z0-9 ]", "", s.lower().replace("ŵ", "w").replace("â", "a"))
    terms = sorted(AZ.TERMS, key=key)
    ids = [t["id"] for t in terms]
    assert len(ids) == len(set(ids)), "two A–Z entries share an id"
    groups = {}
    for t in terms:
        groups.setdefault(_letter(key(t)), []).append(t)
    letters = sorted(groups)
    bar = '<ul class="ref-letters">' + "".join(f'<li><a href="#az-{c}">{c}</a></li>' for c in letters) + "</ul>"
    body = ""
    for c in letters:
        items = ""
        for t in groups[c]:
            sub = f'<small class="l-en" lang="en">{e(t["cy"])}</small>' if t["cy"] != t["en"] else ""
            items += (f'<div class="ref-item" id="az-{t["id"]}" data-ref-item><dt>{bi(t["en"], t["cy"])}{sub}</dt>'
                      f'<dd>{bi(t["dEn"], t["dCy"])}{link_chips(t["see"], have)}</dd></div>')
        body += f'<div class="ref-group" id="az-{c}" data-ref-group><h2>{c}</h2><dl class="ref-list">{items}</dl></div>'
    tools = (f'<div class="ref-tools"><input class="ref-filter" type="search" data-ref-filter placeholder="Find a word… / Chwilio am air…" aria-label="Filter the A–Z / Hidlo’r A–Y" autocomplete="off"></div>'
             + bar)
    n = len(terms)
    main = (g["hero"]("kings", crumbs(), "book", "Reference", "Cyfeirlyfr", "The A–Z of Welsh history", "A–Y hanes Cymru",
                      f"{n} words, laws, places and ideas from Welsh history, each explained in a few lines, with links to read more.",
                      f"{n} o eiriau, cyfreithiau, lleoedd a syniadau o hanes Cymru, pob un wedi’i egluro mewn ychydig linellau, gyda dolenni i ddarllen mwy.", art="book")
            + g["section"](tools + body + f'<p class="ref-none" data-ref-none hidden>{bi("Nothing in the A–Z matches that. Try the search button at the top of the page.", "Does dim yn yr A–Y yn cyfateb. Rhowch gynnig ar y botwm chwilio ar frig y dudalen.")}</p>', top=True))
    ld = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "The A–Z of Welsh history", "url": g["BASE_URL"] + "a-z.html", "inLanguage": ["en", "cy"],
          "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t["en"], "description": t["dEn"], "url": g["BASE_URL"] + f"a-z.html#az-{t['id']}"} for t in terms]}
    return g["page"]("a-z.html", "The A–Z of Welsh history · History of Wales",
                     f"{n} words and ideas from Welsh history explained in plain English and Welsh: cantref, uchelwyr, the March, the Acts of Union, the Blue Books, cynghanedd and more.",
                     main, era="kings", ld=ld, active="reference.html", track="page:a-z", extra=FILTER_JS)


# ---------- quick answers ----------
def questions_page(have):
    n = sum(len(gr["qs"]) for gr in FAQ.GROUPS)
    ids = [q["id"] for gr in FAQ.GROUPS for q in gr["qs"]]
    assert len(ids) == len(set(ids)), "two questions share an id"
    jump = '<ul class="ref-jump">' + "".join(f'<li><a href="#qs-{gr["id"]}">{bi(gr["en"], gr["cy"])}</a></li>' for gr in FAQ.GROUPS) + "</ul>"
    body = ""
    for gr in FAQ.GROUPS:
        qs = "".join(f'<details class="ref-q" id="q-{q["id"]}" data-ref-item><summary>{bi(q["qEn"], q["qCy"])}</summary>'
                     f'<div class="ref-a"><p>{bi(q["aEn"], q["aCy"])}</p>{link_chips(q["see"], have)}</div></details>' for q in gr["qs"])
        body += f'<div class="ref-group" id="qs-{gr["id"]}" data-ref-group><h2 class="ref-gh">{bi(gr["en"], gr["cy"])}</h2>{qs}</div>'
    tools = (f'<div class="ref-tools"><input class="ref-filter" type="search" data-ref-filter placeholder="Find a question… / Chwilio am gwestiwn…" aria-label="Filter the questions / Hidlo’r cwestiynau" autocomplete="off">'
             f'<button type="button" class="btn" data-ref-open>{bi("Open all", "Agor y cyfan")}</button></div>' + jump)
    main = (g["hero"]("today", crumbs(), "book", "Reference", "Cyfeirlyfr", "Quick answers", "Atebion cyflym",
                      f"{n} questions people ask about the history of Wales, each answered in a few lines. Tap a question to open it.",
                      f"{n} o gwestiynau y mae pobl yn eu gofyn am hanes Cymru, pob un wedi’i ateb mewn ychydig linellau. Tapiwch gwestiwn i’w agor.", art="book")
            + g["section"](tools + body + f'<p class="ref-none" data-ref-none hidden>{bi("No question matches that. Try the search button at the top of the page, or the A–Z.", "Does dim cwestiwn yn cyfateb. Rhowch gynnig ar y botwm chwilio ar frig y dudalen, neu’r A–Y.")}</p>', top=True))
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": "en",
          "mainEntity": [{"@type": "Question", "name": q["qEn"], "acceptedAnswer": {"@type": "Answer", "text": q["aEn"]}} for gr in FAQ.GROUPS for q in gr["qs"]]}
    return g["page"]("questions.html", "Quick answers on Welsh history · History of Wales",
                     f"{n} questions about the history of Wales answered in plain words: who was the last Prince of Wales, why so many castles, how Welsh survived, and more.",
                     main, era="today", ld=ld, active="reference.html", track="page:questions", extra=FILTER_JS + OPEN_JS)


OPEN_JS = r"""<script>(function(){var b=document.querySelector("[data-ref-open]");if(!b)return;b.addEventListener("click",function(){var d=[].slice.call(document.querySelectorAll("details.ref-q")),o=d.some(function(x){return !x.open});d.forEach(function(x){x.open=o})})})();</script>
"""


# ---------- towns and villages ----------
def slug(s):
    s = s.lower()
    for a, b in (("ŵ", "w"), ("ŷ", "y"), ("â", "a"), ("ô", "o"), ("ê", "e"), ("î", "i"), ("û", "u"), ("ï", "i"), ("’", ""), ("'", "")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def town_rows():
    geo_file = os.path.join(g["SRC"], "towns_geo.json")
    found = json.load(open(geo_file)) if os.path.exists(geo_file) else {}
    rows = []
    for la, towns in TWN.TOWNS.items():
        for t in towns:
            ll = t["geo"] or found.get(t["en"])
            assert ll, f"No map position for {t['en']}: run python3 tools/towns_geo.py"
            rows.append(dict(t, la=la, laCy=g["CS"].LA_CY[la], id="town-" + slug(t["en"]), lat=ll[0], lon=ll[1]))
    ids = [r["id"] for r in rows]
    assert len(ids) == len(set(ids)), "two towns share a name"
    return rows


def wales_xy(lat, lon):
    G = g["geo"]
    return (lon - G["minx"]) * G["k"] * G["sc"], (G["maxy"] - lat) * G["sc"]


def towns_map(rows):
    dots = ""
    for r in rows:
        x, y = wales_xy(r["lat"], r["lon"])
        dots += (f'<a href="#{r["id"]}" class="tw-dot" aria-label="{e(r["cy"])} / {e(r["en"])}"><g transform="translate({x:.1f} {y:.1f})"><circle class="h" r="12"/><circle class="d" r="4.5"/></g>'
                 f'<title>{e(r["cy"])}{" / " + e(r["en"]) if r["cy"] != r["en"] else ""}: {e(r["mEn"])}</title></a>')
    return (f'<svg class="tw-map" viewBox="-20 -20 640 711" role="group" aria-label="Map of Wales: tap a town to read about it">'
            f'<path class="land" d="{g["geo"]["outline"]}"/>{dots}</svg>')


def town_card(r, have):
    sub = f'<span class="tw-en">{e(r["en"])}</span>' if r["en"] != r["cy"] else ""
    return (f'<article class="tw-card" id="{r["id"]}" data-ref-item><h3><span class="tw-cy" lang="cy">{e(r["cy"])}</span>{sub}</h3>'
            f'<p class="tw-m"><b>{bi("Means", "Ystyr")}:</b> {bi(r["mEn"], r["mCy"])}</p><p>{bi(r["hEn"], r["hCy"])}</p>{link_chips(r["see"], have)}</article>')


DECODER_JS = r"""<script>(function(){var box=document.getElementById("tw-in"),out=document.getElementById("tw-out");if(!box)return;
var EL=JSON.parse(document.getElementById("tw-el").textContent),TW=JSON.parse(document.getElementById("tw-towns").textContent);
var cy=function(){return document.documentElement.classList.contains("cy")};
var norm=function(s){return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g,"").replace(/[’'.]/g,"")};
var esc=function(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})};
var keys=Object.keys(EL).sort(function(a,b){return b.length-a.length});
function split(word){var parts=[],i=0,rest="";while(i<word.length){var hit=null;for(var k=0;k<keys.length;k++){if(keys[k].length>1&&word.substr(i,keys[k].length)===keys[k]){hit=keys[k];break}}
if(hit){if(rest){parts.push([rest,null]);rest=""}parts.push([hit,EL[hit]]);i+=hit.length}else{rest+=word[i];i++}}if(rest)parts.push([rest,null]);return parts}
function run(){var q=norm(box.value.trim());if(!q){out.innerHTML="";return}
var t=TW.filter(function(x){return norm(x[0])===q||norm(x[1])===q})[0],html="";
if(t)html+='<p class="tw-hit"><a href="#'+t[4]+'"><b>'+esc(t[1])+(t[0]!==t[1]?" / "+esc(t[0]):"")+"</b></a>: "+esc(cy()?t[3]:t[2])+"</p>";
var words=q.split(/[\s-]+/).filter(Boolean),chips="";
words.forEach(function(w){if(EL[w]){chips+='<li><b>'+esc(w)+"</b><span>"+esc(cy()?EL[w][1]:EL[w][0])+"</span></li>";return}
split(w).forEach(function(p){chips+=p[1]?'<li><b>'+esc(p[0])+"</b><span>"+esc(cy()?p[1][1]:p[1][0])+"</span></li>":'<li class="un"><b>'+esc(p[0])+"</b><span>"+(cy()?"enw sant, person, afon neu air arall":"a saint, person, river or other word")+"</span></li>"})});
out.innerHTML=html+'<ul class="tw-parts">'+chips+"</ul>"}
box.addEventListener("input",run);document.addEventListener("click",function(ev){if(ev.target.closest("#lang-en,#lang-cy"))setTimeout(run,0)});
[].slice.call(document.querySelectorAll("[data-tw-try]")).forEach(function(b){b.addEventListener("click",function(){box.value=b.textContent;run();box.focus()})})})();</script>
"""


def towns_page(have):
    rows = town_rows()
    els = {}
    for w, en, cy in TWN.ELEMENTS:
        els.setdefault(w, [en, cy])
    data = (f'<script type="application/json" id="tw-el">{json.dumps(els, ensure_ascii=False)}</script>'
            f'<script type="application/json" id="tw-towns">{json.dumps([[r["en"], r["cy"], r["mEn"], r["mCy"], r["id"]] for r in rows], ensure_ascii=False)}</script>')
    tries = "".join(f'<button type="button" class="chip" data-tw-try>{w}</button>' for w in ("Aberystwyth", "Llanfair Pwllgwyngyll", "Pen-y-bont", "Bryn-coch", "Abertawe", "Pontypridd", "Maesteg", "Dolgellau"))
    decoder = (f'<div class="tw-dec"><label for="tw-in" class="tw-lab">{bi("What does the name mean? Type any Welsh place name.", "Beth yw ystyr yr enw? Teipiwch unrhyw enw lle Cymraeg.")}</label>'
               f'<input id="tw-in" class="ref-filter" type="search" autocomplete="off" spellcheck="false" placeholder="e.g. Aberdaugleddau, Pen-y-groes, Llanelli">'
               f'<p class="tw-try">{bi("Try:", "Rhowch gynnig ar:")} {tries}</p><div id="tw-out" aria-live="polite"></div>{data}</div>')
    groups = ""
    for la in g["CS"].LA_ORDER:
        rs = [r for r in rows if r["la"] == la]
        if not rs:
            continue
        rs.sort(key=lambda r: slug(r["cy"]))
        groups += (f'<div class="ref-group" id="tw-{slug(la)}" data-ref-group><h2 class="ref-gh">{bi(la, g["CS"].LA_CY[la])}</h2>'
                   f'<div class="tw-grid">{"".join(town_card(r, have) for r in rs)}</div></div>')
    jump = '<ul class="ref-jump">' + "".join(f'<li><a href="#tw-{slug(la)}">{bi(la, g["CS"].LA_CY[la])}</a></li>' for la in g["CS"].LA_ORDER if any(r["la"] == la for r in rows)) + "</ul>"
    seen, words = set(), []
    for w, en, cy in TWN.ELEMENTS:
        if w in seen:
            continue
        seen.add(w)
        words.append(f'<div><dt lang="cy">{e(w)}</dt><dd>{bi(en, cy)}</dd></div>')
    gloss = f'<dl class="tw-words">{"".join(words)}</dl>'
    n = len(rows)
    main = (g["hero"]("saints", crumbs(), "book", "Reference", "Cyfeirlyfr", "Towns and villages of Wales", "Trefi a phentrefi Cymru",
                      f"What {n} Welsh place names mean, and what happened there. Or type any name into the decoder to see what its parts mean.",
                      f"Beth yw ystyr {n} o enwau lleoedd Cymru, a beth ddigwyddodd yno. Neu teipiwch unrhyw enw i’r datgodiwr i weld ystyr ei rannau.", art="cross")
            + g["section"](decoder, top=True)
            + g["section"](f'<div class="tw-top"><div class="tw-mapbox">{towns_map(rows)}</div><div><p>{bi("Tap a dot on the map to jump to that place, or pick a county.", "Tapiwch ddot ar y map i neidio i’r lle hwnnw, neu dewiswch sir.")}</p>{jump}'
                           f'<input class="ref-filter" type="search" data-ref-filter placeholder="Find a town… / Chwilio am dref…" aria-label="Filter the towns / Hidlo’r trefi" autocomplete="off"></div></div>'
                           + groups + f'<p class="ref-none" data-ref-none hidden>{bi("No town in the list matches. Try the decoder above, which works for any name.", "Does dim tref yn y rhestr yn cyfateb. Rhowch gynnig ar y datgodiwr uchod, sy’n gweithio i unrhyw enw.")}</p>',
                           "The places", "Y lleoedd")
            + g["section"](gloss, "The words in Welsh place names", "Y geiriau mewn enwau lleoedd"))
    return g["page"]("towns.html", "Welsh place names: what they mean · History of Wales",
                     f"What Welsh place names mean: {n} towns and villages with their history, a name decoder for any place in Wales, and the words that make up the names.",
                     main, era="saints", ld=ld_article("Towns and villages of Wales", "What Welsh place names mean"), active="reference.html", track="page:towns", extra=FILTER_JS + DECODER_JS)


TOWN_CSS = """
.tw-dec{background:var(--slate);border:1px solid var(--line);border-radius:16px;padding:1.3rem 1.3rem 1.1rem;max-width:50rem}
.tw-lab{display:block;font:600 1.2rem var(--f-display);margin:0 0 .7rem}
.tw-dec .ref-filter{width:100%;box-sizing:border-box;background:var(--night)}
.tw-try{display:flex;flex-wrap:wrap;gap:.35rem;align-items:center;margin:.8rem 0 0;color:var(--muted);font-size:.9rem}
.tw-parts{list-style:none;padding:0;margin:1rem 0 0;display:flex;flex-wrap:wrap;gap:.5rem}
.tw-parts li{display:grid;gap:.1rem;background:var(--night);border:1px solid var(--line);border-top:3px solid var(--gold,#e8c65a);border-radius:10px;padding:.5rem .8rem}
.tw-parts li b{font:600 1.1rem var(--f-display)}.tw-parts li span{font-size:.85rem;color:var(--muted)}
.tw-parts li.un{border-top-color:var(--line)}
.tw-hit{margin:1rem 0 0}.tw-hit a{color:var(--gold,#e8c65a)}
.tw-top{display:grid;grid-template-columns:minmax(0,1fr);gap:1.4rem;margin:0 0 2rem}
@media(min-width:800px){.tw-top{grid-template-columns:minmax(0,22rem) minmax(0,1fr);align-items:start}}
.tw-mapbox{max-width:24rem}
.tw-map{width:100%;height:auto;display:block}.tw-map .land{fill:var(--slate);stroke:var(--line);stroke-width:1.2}
.tw-dot .d{fill:var(--gold,#e8c65a)}.tw-dot .h{fill:transparent}.tw-dot:hover .d,.tw-dot:focus .d{fill:var(--red,#e2453d)}
.tw-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,19rem),1fr));gap:1rem;margin-bottom:1rem}
.tw-card{background:var(--slate);border:1px solid var(--line);border-radius:12px;padding:1rem 1.1rem 1.1rem;scroll-margin-top:5.5rem}
.tw-card:target{border-color:var(--gold,#e8c65a);box-shadow:0 0 0 2px color-mix(in srgb,var(--gold,#e8c65a) 35%,transparent)}
.tw-card h3{margin:0 0 .4rem;display:flex;flex-wrap:wrap;gap:.2rem .6rem;align-items:baseline}
.tw-cy{font:600 1.35rem/1.2 var(--f-display)}.tw-en{font:500 .8rem var(--f-mono);color:var(--muted)}
.tw-card p{margin:.35rem 0 0;line-height:1.55;font-size:.95rem}.tw-m{color:var(--gold,#e8c65a)}.tw-m b{color:var(--muted);font-weight:500}
.tw-words{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,13rem),1fr));gap:.3rem 1rem;margin:0}
.tw-words div{display:flex;gap:.6rem;align-items:baseline;padding:.35rem 0;border-bottom:1px solid var(--line)}
.tw-words dt{font:600 1.05rem var(--f-display);min-width:5rem}.tw-words dd{margin:0;color:var(--muted);font-size:.9rem}
"""


# ---------- the look-it-up desk ----------
DESK = [  # href, English, Welsh, English line, Welsh line, era colour
    ("a-z.html", "The A–Z", "Yr A–Y", "Words, laws and ideas, each explained in a few lines.", "Geiriau, cyfreithiau a syniadau, pob un wedi’i egluro mewn ychydig linellau.", "kings"),
    ("questions.html", "Quick answers", "Atebion cyflym", "The questions people ask most about Welsh history, answered.", "Y cwestiynau a ofynnir amlaf am hanes Cymru, wedi’u hateb.", "today"),
    ("towns.html", "Towns and villages", "Trefi a phentrefi", "What every place name means, and what happened there.", "Beth mae pob enw lle’n ei olygu, a beth ddigwyddodd yno.", "saints"),
    ("battles.html", "Battles of Wales", "Brwydrau Cymru", "Every battle from Catraeth to Fishguard, on a map.", "Pob brwydr o Gatraeth i Abergwaun, ar fap.", "medieval"),
    ("documents.html", "Key documents", "Dogfennau allweddol", "The words of the treaties, letters and laws that shaped Wales.", "Geiriau’r cytundebau, y llythyrau a’r deddfau a luniodd Gymru.", "tudor"),
    ("sites.html", "Historic sites map", "Map safleoedd hanesyddol", "Hillforts, burial chambers, standing stones, Roman forts, abbeys and holy wells.", "Bryngaerau, cromlechi, meini hirion, caerau Rhufeinig, abatai a ffynhonnau sanctaidd.", "ancient"),
    ("maps.html", "Maps through time", "Mapiau drwy’r oesoedd", "Watch the map of Wales change from the four peoples to today.", "Gwyliwch fap Cymru’n newid o’r pedwar llwyth hyd heddiw.", "roman"),
    ("topics.html", "Topic guides", "Canllawiau pwnc", "Faith, industry, law, music, women, war and the Welsh abroad.", "Ffydd, diwydiant, cyfraith, cerddoriaeth, menywod, rhyfel a’r Cymry ar wasgar.", "industrial"),
    ("kings.html", "Kings and princes", "Brenhinoedd a thywysogion", "Every ruler of every Welsh kingdom, in order.", "Pob rheolwr ym mhob teyrnas Gymreig, yn eu trefn.", "kings"),
    ("family-trees.html", "Royal family trees", "Coed teulu brenhinol", "From Rhodri Mawr to Harri Tudur.", "O Rhodri Mawr i Harri Tudur.", "kings"),
    ("castles.html", "Castles map", "Map y cestyll", "All 827 castle sites in Wales and who built them.", "Pob un o’r 827 o safleoedd cestyll yng Nghymru a phwy a’u cododd.", "medieval"),
    ("saints.html", "Saints of Wales", "Seintiau Cymru", "The saints, their feast days and the llannau named after them.", "Y seintiau, eu gwyliau a’r llannau a enwyd ar eu hôl.", "saints"),
    ("timeline.html", "The timeline", "Y llinell amser", "Over 400 events from 230,000 years ago to today.", "Dros 400 o ddigwyddiadau o 230,000 o flynyddoedd yn ôl hyd heddiw.", "modern"),
    ("index.html#people", "Famous people", "Pobl enwog", "322 people from every age of Welsh history.", "322 o bobl o bob oes yn hanes Cymru.", "industrial"),
    ("laws.html", "The Laws of Hywel Dda", "Cyfreithiau Hywel Dda", "The law of Wales for six hundred years.", "Cyfraith Cymru am chwe chan mlynedd.", "kings"),
    ("onthisday.html", "On this day", "Ar y dydd hwn", "What happened on every day of the year.", "Beth ddigwyddodd ar bob diwrnod o’r flwyddyn.", "medieval"),
    ("names.html", "Welsh surnames", "Cyfenwau Cymraeg", "What Welsh surnames mean and where they come from.", "Beth mae cyfenwau Cymraeg yn ei olygu ac o ble maent yn dod.", "saints"),
    ("symbols.html", "Symbols and traditions", "Symbolau a thraddodiadau", "The dragon, the leek, the harp, the Mari Lwyd and more.", "Y ddraig, y genhinen, y delyn, y Fari Lwyd a rhagor.", "modern"),
]


def desk_page(have):
    cards = ""
    for h, en, cy, den, dcy, era in DESK:
        if not exists(h, have):
            continue
        cards += (f'<a href="{h}" style="--c:{g["COL"][era]}"><span class="n">{bi("Look up", "Chwilio")}</span><b>{bi(en, cy)}</b>'
                  f'<span class="d">{bi(den, dcy)}</span></a>')
    big = (f'<button type="button" class="ref-big-search" data-search>{g["SEARCH_SVG"]}'
           f'{bi("Search everything: people, kings, places, castles, battles, words…", "Chwilio popeth: pobl, brenhinoedd, lleoedd, cestyll, brwydrau, geiriau…")}</button>')
    main = (g["hero"]("kings", f'<a href="index.html">{g["SITE"]}</a>', "book", "Reference", "Cyfeirlyfr", "Look it up", "Chwilio’r hanes",
                      "Everything on Welsh history in one place: search the whole site, or open the A–Z, the quick answers, the maps and the lists below.",
                      "Popeth am hanes Cymru mewn un lle: chwiliwch y wefan gyfan, neu agorwch yr A–Y, yr atebion cyflym, y mapiau a’r rhestrau isod.", art="book", extra=big)
            + g["section"](f'<div class="ref-desk">{cards}</div>', top=True))
    return g["page"]("reference.html", "Look it up: the Welsh history reference desk · History of Wales",
                     "Look up anything in Welsh history: an A–Z, quick answers, towns and their names, battles, key documents, historic sites, maps, kings, castles and saints.",
                     main, era="kings", og_type="website", ld=ld_article("Look it up", "The Welsh history reference desk"), active="reference.html", track="page:reference")


# ---------- what build.py calls ----------
def pages(have):
    """have: the set of page names build.py is making (so links to pages that do not exist yet are left out)."""
    _titles()
    have = set(have) | set(PAGE_NAMES)
    out = {"a-z.html": az_page(have), "questions.html": questions_page(have), "towns.html": towns_page(have), "reference.html": desk_page(have)}
    return out


PAGE_NAMES = ["a-z.html", "questions.html", "towns.html", "reference.html"]


def search_items():
    items = [dict(k="term", t=t["en"], c=t["cy"], u=f"a-z.html#az-{t['id']}", y=["A–Z", "A–Y"], b=[t["dEn"], t["dCy"]], e="kings") for t in AZ.TERMS]
    items += [dict(k="question", t=q["qEn"], c=q["qCy"], u=f"questions.html#q-{q['id']}", y=["Quick answer", "Ateb cyflym"], b=[q["aEn"], q["aCy"]], e="today") for gr in FAQ.GROUPS for q in gr["qs"]]
    items += [dict(k="town", t=r["cy"], c=r["cy"], u=f"towns.html#{r['id']}", y=[r["en"] if r["en"] != r["cy"] else r["la"], r["laCy"]], b=[r["mEn"].capitalize() + ". " + r["hEn"], r["mCy"].capitalize() + ". " + r["hCy"]], e="saints", a=r["en"]) for r in town_rows()]
    items.append(dict(k="page", t="Towns and villages: what Welsh place names mean", c="Trefi a phentrefi: ystyr enwau lleoedd", u="towns.html", y=["Place names", "Enwau lleoedd"],
                      b=["What Welsh place names mean, with a decoder for any name: aber, llan, caer, pen, tre and more.", "Ystyr enwau lleoedd Cymru, gyda datgodiwr i unrhyw enw: aber, llan, caer, pen, tre a rhagor."], e="saints"))
    items.append(dict(k="page", t="The A–Z of Welsh history", c="A–Y hanes Cymru", u="a-z.html", y=["Reference", "Cyfeirlyfr"],
                      b=["Words, laws, places and ideas from Welsh history, each explained in a few lines.", "Geiriau, cyfreithiau, lleoedd a syniadau o hanes Cymru, pob un wedi’i egluro mewn ychydig linellau."], e="kings"))
    items.append(dict(k="page", t="Look it up: the reference desk", c="Chwilio’r hanes: y ddesg gyfeirio", u="reference.html", y=["Reference", "Cyfeirlyfr"],
                      b=["Every way to look up Welsh history on this site in one place.", "Pob ffordd o chwilio hanes Cymru ar y wefan hon mewn un lle."], e="kings"))
    return items
