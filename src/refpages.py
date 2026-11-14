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
import ref_battles as BT
import ref_docs as DC
import ref_topics as TP
import ref_maps as MP
import ref_sites as ST
import os

g = {}  # build.py's helpers (bi, e, page, hero, section ...), filled by setup()


def track_added():
    """Note every reference item in src/added.json (src/added.py), so new ones are known as new."""
    AD = g["AD"]
    AD.track("az", [t["id"] for t in AZ.TERMS])
    AD.track("faq", [q["id"] for gr in FAQ.GROUPS for q in gr["qs"]])
    AD.track("battle", [b["id"] for b in BT.BATTLES])
    AD.track("doc", [d["id"] for d in DC.DOCS])
    AD.track("topic", [t["id"] for t in TP.TOPICS])


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
    "names.html": ("Welsh names", "Enwau Cymraeg"), "family-history.html": ("Finding your Welsh family", "Dod o hyd i’ch teulu Cymreig"), "firsts.html": ("Welsh world firsts", "Cymru oedd y cyntaf"), "timeline.html": ("Timeline", "Llinell amser"),
    "onthisday.html": ("On this day", "Ar y dydd hwn"), "gallery.html": ("Photo gallery", "Oriel luniau"), "stories.html": ("Long reads", "Erthyglau"),
    "legends.html": ("Legends", "Chwedlau"), "wales-in-10.html": ("Wales in 10 minutes", "Cymru mewn 10 munud"), "trails.html": ("Themed trails", "Llwybrau thema"),
    "literature.html": ("The literature of Wales", "Llenyddiaeth Cymru"), "books.html": ("The old books of Wales", "Hen lyfrau Cymru"), "triads.html": ("The Welsh Triads", "Trioedd Ynys Prydain"),
    "a-z.html": ("The A–Z of Welsh history", "A–Y hanes Cymru"), "questions.html": ("Quick answers", "Atebion cyflym"), "towns.html": ("Towns and villages", "Trefi a phentrefi"),
    "battles.html": ("Battles of Wales", "Brwydrau Cymru"), "documents.html": ("Key documents", "Dogfennau allweddol"), "sites.html": ("Historic sites map", "Map safleoedd hanesyddol"),
    "maps.html": ("Maps through time", "Mapiau drwy’r oesoedd"), "reference.html": ("Look it up", "Chwilio’r hanes"),
    "topics.html": ("Topic guides", "Canllawiau pwnc"),
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
    for t in TP.TOPICS:
        TITLES[f"topic-{t['id']}.html"] = (t["en"], t["cy"])
    # links to one entry on a reference page are named after that entry
    for x in AZ.TERMS:
        TITLES[f"a-z.html#az-{x['id']}"] = (x["en"], x["cy"])
    for x in DC.DOCS:
        TITLES[f"documents.html#doc-{x['id']}"] = (x["en"], x["cy"])
    for x in BT.BATTLES:
        TITLES[f"battles.html#b-{x['id']}"] = (x["en"], x["cy"])
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
        t = TITLES.get(h) or TITLES.get(h.split("#")[0])
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
function op(){if(!location.hash)return;var t=document.getElementById(location.hash.slice(1));if(t&&t.tagName==="DETAILS")t.open=true}op();addEventListener("hashchange",op)})();</script>
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
.ref-desk span.n{font:500 .75rem var(--f-mono);color:var(--muted);letter-spacing:.05em;text-transform:uppercase}
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
            items += (f'<div class="ref-item" id="az-{t["id"]}" data-ref-item><dt>{bi(t["en"], t["cy"])}{g["new_tag"]("az", t["id"])}{sub}</dt>'
                      f'<dd>{bi(t["dEn"], t["dCy"])}{link_chips(t["see"], have)}</dd></div>')
        body += f'<div class="ref-group" id="az-{c}" data-ref-group><h2>{c}</h2><dl class="ref-list">{items}</dl></div>'
    tools = (f'<div class="ref-tools"><input class="ref-filter" type="search" data-ref-filter placeholder="Find a word… / Chwilio am air…" aria-label="Filter the A–Z / Hidlo’r A–Y" autocomplete="off"></div>'
             + bar)
    tools = g["just_added"]("az", terms, lambda t: f'#az-{t["id"]}', lambda t: (t["en"], t["cy"])) + tools
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
        qs = "".join(f'<details class="ref-q" id="q-{q["id"]}" data-ref-item><summary>{bi(q["qEn"], q["qCy"])}{g["new_tag"]("faq", q["id"])}</summary>'
                     f'<div class="ref-a"><p>{bi(q["aEn"], q["aCy"])}</p>{link_chips(q["see"], have)}</div></details>' for q in gr["qs"])
        body += f'<div class="ref-group" id="qs-{gr["id"]}" data-ref-group><h2 class="ref-gh">{bi(gr["en"], gr["cy"])}</h2>{qs}</div>'
    tools = (f'<div class="ref-tools"><input class="ref-filter" type="search" data-ref-filter placeholder="Find a question… / Chwilio am gwestiwn…" aria-label="Filter the questions / Hidlo’r cwestiynau" autocomplete="off">'
             f'<button type="button" class="btn" data-ref-open>{bi("Open all", "Agor y cyfan")}</button></div>' + jump)
    allq = [q for gr in FAQ.GROUPS for q in gr["qs"]]
    tools = g["just_added"]("faq", allq, lambda q: f'#q-{q["id"]}', lambda q: (q["qEn"], q["qCy"])) + tools
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


def town_pic(r):
    """A photo for a town's card: a place on the site with a photo of its own, in or right by the town (2.5 km)."""
    import math
    best = None
    for p in g["D"].PLACES:
        if p.get("lat") is None:
            continue
        d = math.hypot((p["lat"] - r["lat"]) * 111, (p["lon"] - r["lon"]) * 111 * math.cos(math.radians(r["lat"])))
        if d < 2.5 and (best is None or d < best[0]):
            pic = g["card_pic"](f'place-{p["id"]}.html')
            if pic:
                best = (d, pic[0])
    return best[1] if best else None


def town_card(r, have):
    sub = f'<span class="tw-en">{e(r["en"])}</span>' if r["en"] != r["cy"] else ""
    pic = town_pic(r)
    import townpages as TOWNP  # a town with a page of its own (src/townpages.py): the whole card opens it
    own = TOWNP.has_page(r["id"])
    wl = f'<a class="wl" href="{r["id"]}.html">{bi(r["en"], r["cy"])}</a>' if own else ""
    return (f'<article class="tw-card{" pbg" if pic else ""}{" wl-card" if own else ""}" id="{r["id"]}" data-ref-item{g["PN"].bg_style(pic, small=True) if pic else ""}><h3><span class="tw-cy" lang="cy">{e(r["cy"])}</span>{sub}</h3>'
            f'<p class="tw-m"><b>{bi("Means", "Ystyr")}:</b> {bi(r["mEn"], r["mCy"])}</p><p>{bi(r["hEn"], r["hCy"])}</p>{wl}{link_chips(r["see"], have)}</article>')


DECODER_JS = r"""<script>(function(){var box=document.getElementById("tw-in"),out=document.getElementById("tw-out");if(!box)return;
var cy=function(){return document.documentElement.classList.contains("cy")};
var esc=function(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})};
function run(){var P=window.PN;if(!P)return;var r=P.decode(box.value),c=cy(),html="";if(!box.value.trim()){out.innerHTML="";return}
if(r.hit)html+='<p class="tw-hit"><a href="'+esc(P.townLink(r.hit))+'"><b>'+esc(r.hit[1])+(r.hit[0]!==r.hit[1]?" / "+esc(r.hit[0]):"")+"</b></a>: "+esc(c?r.hit[3]:r.hit[2])+"</p>";
html+='<div class="tw-words-out">'+r.words.map(function(w){return'<ul class="tw-parts">'+w.map(function(p){var l=P.label(p,c),eng=l.kind==="e"||l.kind==="n";
return'<li class="'+(l.kind==="u"?"un":eng?"en":"")+'"><b>'+esc(l.t)+"</b><span>"+(eng?"<em>"+(c?"Saesneg":"English")+":</em> ":"")+esc(l.mean)+"</span>"+(l.note?"<small>"+esc(l.note)+"</small>":"")+"</li>"}).join("")+"</ul>"}).join("")+"</div>";
out.innerHTML=html}
box.addEventListener("input",run);document.addEventListener("pn:ready",run);
[].slice.call(document.querySelectorAll("[data-tw-try]")).forEach(function(b){b.addEventListener("click",function(){box.value=b.textContent;run();box.focus()})})})();</script>
"""


def towns_page(have):
    rows = town_rows()
    data = g["PN_SCRIPT"]  # the decoder and its words (src/placenames.py, src/placenames.js)
    tries = "".join(f'<button type="button" class="chip" data-tw-try>{w}</button>' for w in ("Llangammarch Wells", "Aberystwyth", "Llanfair Pwllgwyngyll", "Pontrhydfendigaid", "Builth Wells", "Abertawe", "Betws-y-Coed", "Dolgellau"))
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
    for w, en, cy in g["PNM"].glossary():
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
.tw-parts li.en{border-top-style:dashed}.tw-parts li em{font-style:normal;font-weight:600}
.tw-parts li small{font-size:.76rem;color:var(--muted);font-style:italic}
.tw-words-out{display:flex;flex-wrap:wrap;gap:.6rem 1.1rem;align-items:flex-start}.tw-words-out .tw-parts{margin:0}
#tw-out .tw-hit+.tw-words-out,#tw-out>.tw-words-out:first-child{margin-top:1rem}
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


# ---------- battles of Wales ----------
WIN = {"w": ("Welsh victory", "Buddugoliaeth Gymreig"), "l": ("A Welsh stand", "Safiad Cymreig"), "o": ("Battle or rising", "Brwydr neu wrthryfel")}


def battles_map(rows):
    dots = ""
    for b in rows:
        if not b["geo"]:
            continue
        x, y = wales_xy(*b["geo"])
        dots += (f'<a href="#b-{b["id"]}" class="bt-dot bt-{b["win"]}" data-vs="{" ".join(b["vs"])}" aria-label="{e(b["en"])}, {e(b["dEn"])}"><g transform="translate({x:.1f} {y:.1f})"><circle class="h" r="14"/>'
                 f'<path class="d" d="M-6 -6L6 6M6 -6L-6 6"/></g><title>{e(b["en"])} · {e(b["dEn"])}</title></a>')
    return (f'<svg class="tw-map bt-map" viewBox="-20 -20 640 711" role="group" aria-label="Map of the battles of Wales">'
            f'<path class="land" d="{g["geo"]["outline"]}"/>{dots}</svg>')


def battles_page(have):
    rows = sorted(BT.BATTLES, key=lambda b: b["year"])
    ids = [b["id"] for b in rows]
    assert len(ids) == len(set(ids)), "two battles share an id"
    cards = ""
    for b in rows:
        where = "" if b["geo"] else f'<span class="bt-nomap"> · {bi("not on the map", "nid ar y map")}</span>'
        vs = "".join(f'<span>{bi(*BT.AGAINST[v])}</span>' for v in b["vs"])
        cards += (f'<article class="bt-card bt-{b["win"]}" id="b-{b["id"]}" data-ref-item data-vs="{" ".join(b["vs"])}" style="--c:{g["COL"][b["era"]]}">'
                  f'{g["see_pic"](b["see"], "castle")}<p class="bt-date">{bi(b["dEn"], b["dCy"])} · <span class="bt-k">{bi(*WIN[b["win"]])}</span>{where}{g["new_tag"]("battle", b["id"])}</p>'
                  f'<h3>{bi(b["en"], b["cy"])}</h3><p class="bt-vs"><b>{bi("Against", "Yn erbyn")}:</b> {vs}</p><p class="bt-side">{bi(b["sEn"], b["sCy"])}</p><p>{bi(b["tEn"], b["tCy"])}</p>{link_chips(b["see"], have)}</article>')
    legend = (f'<ul class="bt-legend"><li class="bt-w">{bi(*WIN["w"])}</li><li class="bt-l">{bi(*WIN["l"])}</li><li class="bt-o">{bi(*WIN["o"])}</li></ul>')
    n = len(rows)
    nw = sum(1 for b in rows if b["win"] == "w")
    count = {k: sum(1 for b in rows if k in b["vs"]) for k in BT.AGAINST}
    chips = f'<button type="button" data-vs="" aria-pressed="true">{bi("All", "Y cyfan")} <small>{n}</small></button>' + "".join(
        f'<button type="button" data-vs="{k}" aria-pressed="false">{bi(*lab)} <small>{count[k]}</small></button>' for k, lab in BT.AGAINST.items() if count[k])
    main = (g["hero"]("medieval", crumbs(), "book", "Reference", "Cyfeirlyfr", "Battles of Wales", "Brwydrau Cymru",
                      f"{n} battles, raids, sieges and risings, from the Druids on the Menai to Helmand: who fought, who they fought against, what happened, and where. Where a chronicle names only a region, the date says so.",
                      f"{n} o frwydrau, cyrchoedd, gwarchaeau a gwrthryfeloedd, o’r Derwyddon ar y Fenai i Helmand: pwy a ymladdodd, yn erbyn pwy, beth ddigwyddodd, a ble. Lle mae cronicl yn enwi ardal yn unig, mae’r dyddiad yn dweud hynny.", art="sword")
            + g["section"](g["just_added"]("battle", rows, lambda b: f'#b-{b["id"]}', lambda b: ((b["en"], b["cy"]) if b["dEn"] in b["en"] else (f'{b["en"]} ({b["dEn"]})', f'{b["cy"]} ({b["dCy"]})')))
                           + f'<div class="tw-top"><div class="tw-mapbox">{battles_map(rows)}{legend}</div><div>'
                           f'<p>{bi(f"The Normans took England in five years; Wales held out for 216. Here is every battle the chronicles let us name, against Rome, the Saxons, the Vikings, the Normans, the kings of England and more, {nw} of them Welsh victories. Pick who a battle was against below, or tap a cross on the map.", f"Cymerodd y Normaniaid Loegr mewn pum mlynedd; daliodd Cymru allan am 216. Dyma bob brwydr y mae’r croniclau’n gadael i ni ei henwi, yn erbyn Rhufain, y Saeson, y Llychlynwyr, y Normaniaid, brenhinoedd Lloegr a mwy, {nw} ohonynt yn fuddugoliaethau Cymreig. Dewiswch yn erbyn pwy y bu brwydr isod, neu tapiwch groes ar y map.")}</p>'
                           f'<input class="ref-filter" type="search" data-ref-filter placeholder="Find a battle, a leader or a year… / Chwilio am frwydr, arweinydd neu flwyddyn…" aria-label="Filter the battles / Hidlo’r brwydrau" autocomplete="off">'
                           f'<p style="margin-top:1rem"><a class="btn" href="castles.html">{bi("The castles map", "Map y cestyll")} →</a> <a class="btn" href="story-longbow.html">{bi("The Welsh longbow", "Y bwa hir Cymreig")} →</a></p></div></div>'
                           f'<h2 class="bt-h">{bi("Who the battles were against", "Yn erbyn pwy y bu’r brwydrau")}</h2><nav class="bt-chips" aria-label="Who the battles were against / Yn erbyn pwy">{chips}</nav>'
                           f'<div class="bt-list" data-ref-group>{cards}</div><p class="ref-none" data-ref-none hidden>{bi("No battle matches that.", "Does dim brwydr yn cyfateb.")}</p>', top=True))
    return g["page"]("battles.html", "Battles of Wales: a map and list · History of Wales",
                     f"{n} battles of Welsh history on a map, and who each was against: Romans, Saxons, Vikings, Normans, English kings and more. Catraeth, Crug Mawr, Crogen, Cymerau, Cilmeri, Mynydd Hyddgen, Bryn Glas, Bosworth, Fishguard and the Merthyr and Newport risings.",
                     main, era="medieval", ld=ld_article("Battles of Wales", "The battles of Welsh history on a map"), active="reference.html", track="page:battles", extra=FILTER_JS + VS_JS)


BATTLE_CSS = """
.bt-map .bt-dot .d{stroke:var(--gold,#e8c65a);stroke-width:3.2;stroke-linecap:round;fill:none}.bt-map .bt-dot .h{fill:transparent}
.bt-map .bt-dot.bt-l .d{stroke:#e9d9c6}.bt-map .bt-dot.bt-o .d{stroke:#93a0e0}.bt-map .bt-dot:hover .d,.bt-map .bt-dot:focus .d{stroke:var(--red,#e2453d)}
.bt-legend{list-style:none;padding:0;margin:.6rem 0 0;display:flex;flex-wrap:wrap;gap:.4rem 1rem;font-size:.82rem;color:var(--muted)}
.bt-legend li::before{content:"✕";font-weight:700;margin-right:.35rem;color:var(--gold,#e8c65a)}.bt-legend li.bt-l::before{color:#e9d9c6}.bt-legend li.bt-o::before{color:#93a0e0}
.bt-list{display:grid;gap:1rem;max-width:52rem}
.bt-card{background:var(--slate);border:1px solid var(--line);border-left:4px solid var(--c);border-radius:12px;padding:1rem 1.2rem 1.15rem;scroll-margin-top:5.5rem}
.bt-card:target{border-color:var(--gold,#e8c65a);box-shadow:0 0 0 2px color-mix(in srgb,var(--gold,#e8c65a) 35%,transparent)}
.bt-card h3{font:600 1.4rem/1.2 var(--f-display);margin:.2rem 0 .3rem}
.bt-card p{margin:.35rem 0 0;line-height:1.6}
.bt-date{font:500 .78rem var(--f-mono);color:var(--muted);letter-spacing:.03em;text-transform:uppercase;margin:0!important}
.bt-k{color:var(--gold,#e8c65a)}.bt-l .bt-k{color:#e9d9c6}.bt-o .bt-k{color:#93a0e0}
.bt-nomap{opacity:1}
.tw-top .ref-filter{width:100%;box-sizing:border-box;margin-top:.6rem}
.bt-side{font-weight:600;color:var(--ink)}
.bt-h{font:600 1.5rem var(--f-display);margin:2rem 0 .6rem}
.bt-chips{display:flex;flex-wrap:wrap;gap:.45rem;margin:0 0 1.3rem;max-width:52rem}
.bt-chips button{font:500 .88rem var(--f-body);background:var(--slate);color:var(--ink);border:1px solid var(--line);border-radius:999px;padding:.4rem .85rem;cursor:pointer}
.bt-chips button small{color:var(--muted);font:500 .75rem var(--f-mono);margin-left:.2rem}
.bt-chips button:hover{border-color:var(--gold,#e8c65a)}
.bt-chips button[aria-pressed="true"]{background:var(--gold,#e8c65a);border-color:var(--gold,#e8c65a);color:#1a1a1a}.bt-chips button[aria-pressed="true"] small{color:#1a1a1a}
.bt-vs{font-size:.85rem;color:var(--muted);margin:.25rem 0 0!important}.bt-vs span+span::before{content:" · "}
.bt-off{display:none!important}.bt-map .bt-dot.bt-dim{opacity:.12;pointer-events:none}
"""
VS_JS = r"""<script>(function(){var bs=[].slice.call(document.querySelectorAll(".bt-chips button"));if(!bs.length)return;
var cards=[].slice.call(document.querySelectorAll(".bt-card")),dots=[].slice.call(document.querySelectorAll(".bt-dot"));
function has(x,v){return !v||(" "+x.getAttribute("data-vs")+" ").indexOf(" "+v+" ")>=0}
bs.forEach(function(b){b.addEventListener("click",function(){var v=b.getAttribute("data-vs");bs.forEach(function(o){o.setAttribute("aria-pressed",o===b?"true":"false")});
cards.forEach(function(c){c.classList.toggle("bt-off",!has(c,v))});dots.forEach(function(d){d.classList.toggle("bt-dim",!has(d,v))})})})})();</script>
"""


# ---------- key documents ----------
WORDS = {"quote": ("In its own words", "Yn ei geiriau ei hun"), "welsh": ("In Welsh, with English", "Yn Gymraeg, gyda Saesneg"), "short": ("What it says, in short", "Beth mae’n ei ddweud, yn fyr")}


def doc_words(d):
    kind, en, cy = d["words"]
    label = bi(*WORDS[kind])
    if kind == "welsh":  # the Welsh original is shown in both languages, the English beneath it
        body = f'<blockquote lang="cy">{e(cy)}</blockquote><p class="dc-tr">{bi(en, en)}</p>'
    elif kind == "quote":
        body = f'<blockquote>{bi(en, cy)}</blockquote>'
    else:
        body = f'<p class="dc-short">{bi(en, cy)}</p>'
    return f'<div class="dc-words dc-{kind}"><p class="dc-lab">{label}</p>{body}</div>'


def documents_page(have):
    rows = sorted(DC.DOCS, key=lambda d: d["year"])
    ids = [d["id"] for d in rows]
    assert len(ids) == len(set(ids)), "two documents share an id"
    jump = "".join(f'<a href="#doc-{d["id"]}">{bi(d["en"], d["cy"])}</a>' for d in rows)
    cards = ""
    for d in rows:
        cards += (f'<article class="dc-card" id="doc-{d["id"]}" data-ref-item style="--c:{g["COL"][d["era"]]}">'
                  f'{g["see_pic"](d["see"], "book")}<p class="bt-date">{bi(d["dEn"], d["dCy"])}{g["new_tag"]("doc", d["id"])}</p><h3>{bi(d["en"], d["cy"])}</h3><p>{bi(d["aEn"], d["aCy"])}</p>'
                  f'{doc_words(d)}<p><b>{bi("Why it matters", "Pam mae’n bwysig")}:</b> {bi(d["wEn"], d["wCy"])}</p>'
                  f'<p class="dc-kept">{bi("Where to find it", "Ble i’w chael")}: {bi(d["kEn"], d["kCy"])}</p>{link_chips(d["see"], have)}</article>')
    n = len(rows)
    main = (g["hero"]("tudor", crumbs(), "book", "Reference", "Cyfeirlyfr", "Key documents", "Dogfennau allweddol",
                      f"{n} documents that shaped Wales, from Caesar on the Druids to the Senedd, each with its own words, what it did and where to find it.",
                      f"{n} o ddogfennau a luniodd Gymru, o Gesar ar y Derwyddon i’r Senedd, pob un gyda’i geiriau ei hun, beth a wnaeth a ble i’w chael.", art="book")
            + g["section"](g["just_added"]("doc", rows, lambda d: f'#doc-{d["id"]}', lambda d: ((d["en"], d["cy"]) if d["dEn"] in d["en"] else (f'{d["en"]} ({d["dEn"]})', f'{d["cy"]} ({d["dCy"]})')))
                           + f'<p class="ref-intro">{bi("Where a document’s exact words are known, they are quoted from a published translation. Where they are not, we say what it says in our own words and mark it “in short”. The Laws of Hywel Dda have their own page.", "Lle mae union eiriau dogfen yn hysbys, fe’u dyfynnir o gyfieithiad cyhoeddedig. Lle nad ydynt, rydym yn dweud beth mae’n ei ddweud yn ein geiriau ein hunain ac yn ei nodi’n “yn fyr”. Mae gan Gyfreithiau Hywel Dda eu tudalen eu hunain.")} <a href="laws.html">{bi("The Laws of Hywel Dda", "Cyfreithiau Hywel Dda")} →</a></p>'
                           f'<input class="ref-filter dc-filter" type="search" data-ref-filter placeholder="Find a document, a person or a year… / Chwilio am ddogfen, person neu flwyddyn…" aria-label="Filter the documents / Hidlo’r dogfennau" autocomplete="off">'
                           f'<nav class="dc-jump" aria-label="Documents / Dogfennau">{jump}</nav>'
                           f'<div class="bt-list" data-ref-group>{cards}</div><p class="ref-none" data-ref-none hidden>{bi("No document matches that.", "Does dim dogfen yn cyfateb.")}</p>', top=True))
    return g["page"]("documents.html", "Key documents of Welsh history · History of Wales",
                     f"{n} key documents of Welsh history in their own words: the Treaty of Montgomery, Owain Glyndŵr’s Pennal letter, the Acts of Union, the Blue Books, Hen Wlad fy Nhadau, Tynged yr Iaith and more.",
                     main, era="tudor", ld=ld_article("Key documents of Welsh history", "The treaties, letters and laws that shaped Wales"), active="reference.html", track="page:documents", extra=FILTER_JS)


DOC_CSS = """
.dc-card{background:var(--slate);border:1px solid var(--line);border-left:4px solid var(--c);border-radius:12px;padding:1rem 1.2rem 1.15rem;scroll-margin-top:5.5rem}
.dc-card:target{border-color:var(--gold,#e8c65a)}
.dc-card h3{font:600 1.4rem/1.2 var(--f-display);margin:.2rem 0 .3rem}.dc-card p{margin:.45rem 0 0;line-height:1.6}
.dc-words{margin:.8rem 0 .2rem;padding:.8rem 1rem;border-radius:10px;background:color-mix(in srgb,var(--c) 10%,transparent)}
.dc-lab{font:500 .75rem var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:0!important}
.dc-words blockquote{margin:.4rem 0 0;padding:0;border:0;font:italic 1.08rem/1.6 var(--f-display)}
.dc-words blockquote::before{content:"“"}.dc-words blockquote::after{content:"”"}
.dc-tr{color:var(--muted);font-size:.95rem}.dc-short{font-size:1.02rem}
.dc-kept{font-size:.88rem;color:var(--muted)}
.dc-jump{display:flex;flex-wrap:wrap;gap:.35rem;margin:1rem 0 1.4rem;max-width:52rem}
.dc-jump a{font-size:.8rem;padding:.25rem .6rem;border:1px solid var(--line);border-radius:99px;color:var(--ink);text-decoration:none}
.dc-jump a:hover{border-color:var(--gold,#e8c65a)}
.ref-intro{max-width:52rem;color:var(--muted)}
.dc-filter{width:100%;max-width:52rem;box-sizing:border-box;margin-top:.8rem}
"""


# ---------- topic guides ----------
def _topic_events(t, most=24):
    if not t["ev"]:
        return []
    rx, drop = re.compile(t["ev"]), re.compile(t["xev"]) if t["xev"] else None
    hits = sorted((ev for ev in g["D"].EVENTS if rx.search(ev[5] + " " + ev[7]) and not (drop and drop.search(ev[5]))), key=lambda ev: ev[1])
    if len(hits) > most:  # spread the picks evenly through time, so every age of the topic is shown
        step = (len(hits) - 1) / (most - 1)
        hits = [hits[round(i * step)] for i in range(most)]
    return hits


def topic_page(t, have):
    D = g["D"]
    person = {p[0]: p for p in D.PEOPLE}
    place = {p["id"]: p for p in D.PLACES}
    terms = {x["id"]: x for x in AZ.TERMS}
    qs = {q["id"]: q for gr in FAQ.GROUPS for q in gr["qs"]}
    docs = {d["id"]: d for d in DC.DOCS}
    bats = {b["id"]: b for b in BT.BATTLES}
    col = g["COL"][t["era"]]
    intro = "".join(f"<p>{bi(en, cy)}</p>" for en, cy in zip(t["iEn"], t["iCy"]))
    reads = "".join(f'<a href="{h}"><span class="n">{bi("Read", "Darllen")}</span><b>{bi(*TITLES[h.split("#")[0]])}</b></a>'
                    for h in t["reads"] if exists(h, have) and h.split("#")[0] in TITLES)
    for h in t["reads"]:
        if not exists(h, have):
            MISSING.add(h)
    body = f'<div class="tp-intro">{intro}</div>' + (f'<div class="ref-desk tp-reads">{reads}</div>' if reads else "")
    out = g["section"](body, top=True)
    ppl = [person[s] for s in t["people"] if s in person and exists(f"person-{s}.html", have)]
    if ppl:
        cards = "".join(f'<a href="person-{p[0]}.html" data-era="{p[1]}">{g["see_pic"]([f"person-{p[0]}.html"])}<b>{bi(p[3], p[4])}</b><span class="dt">{g["e"](p[2])}</span><span class="d">{bi(p[5], p[6])}</span></a>' for p in ppl)
        out += g["section"](f'<div class="tp-people">{cards}</div>', "People", "Pobl")
    evs = _topic_events(t)
    if evs:
        lis = "".join(f'<li><time>{bi(g["year_label"](ev), g["year_label"](ev, True))}</time><div><b>{bi(ev[5], ev[6])}</b><p>{bi(ev[7], ev[8])}</p></div></li>' for ev in evs)
        out += g["section"](f'<ol class="tp-ev">{lis}</ol><p><a class="btn" href="timeline.html">{bi("The whole timeline", "Y llinell amser gyfan")} →</a></p>', "Key moments", "Eiliadau allweddol")
    side = ""
    dl = [terms[i] for i in t["az"] if i in terms]
    if dl:
        side += (f'<div><h3 class="tp-h">{bi("Words to know", "Geiriau i’w gwybod")}</h3><dl class="tp-az">'
                 + "".join(f'<dt><a href="a-z.html#az-{x["id"]}">{bi(x["en"], x["cy"])}</a></dt><dd>{bi(x["dEn"], x["dCy"])}</dd>' for x in dl) + "</dl></div>")
    ql = [qs[i] for i in t["faq"] if i in qs]
    if ql:
        side += (f'<div><h3 class="tp-h">{bi("Quick answers", "Atebion cyflym")}</h3>'
                 + "".join(f'<details class="ref-q"><summary>{bi(q["qEn"], q["qCy"])}</summary><div class="ref-a"><p>{bi(q["aEn"], q["aCy"])}</p></div></details>' for q in ql) + "</div>")
    if side:
        out += g["section"](f'<div class="tp-two">{side}</div>', "Look it up", "Chwilio’r hanes")
    more = ""
    dd = [docs[i] for i in t["docs"] if i in docs]
    if dd:
        more += f'<div><h3 class="tp-h">{bi("Key documents", "Dogfennau allweddol")}</h3><p class="ref-see">' + "".join(f'<a href="documents.html#doc-{d["id"]}">{bi(d["en"], d["cy"])} · {bi(d["dEn"], d["dCy"])}</a>' for d in dd) + "</p></div>"
    bb = [bats[i] for i in t["battles"] if i in bats]
    if bb:
        more += f'<div><h3 class="tp-h">{bi("Battles", "Brwydrau")}</h3><p class="ref-see">' + "".join(f'<a href="battles.html#b-{b["id"]}">{bi(b["en"], b["cy"])} · {bi(b["dEn"], b["dCy"])}</a>' for b in bb) + "</p></div>"
    pp = [place[i] for i in t["places"] if i in place and exists(f"place-{i}.html", have)]
    if pp:
        more += f'<div><h3 class="tp-h">{bi("Places to visit", "Lleoedd i ymweld â nhw")}</h3><p class="ref-see">' + "".join(f'<a href="place-{p["id"]}.html">{bi(p["en"], p["cy"])}</a>' for p in pp) + "</p></div>"
    if more:
        out += g["section"](more, "Documents, battles and places", "Dogfennau, brwydrau a lleoedd")
    others = "".join(f'<a href="topic-{o["id"]}.html" style="--c:{g["COL"][o["era"]]}"><b>{bi(o["en"], o["cy"])}</b></a>' for o in TP.TOPICS if o["id"] != t["id"])
    out += g["section"](f'<div class="tp-others">{others}</div>', "More topic guides", "Rhagor o ganllawiau pwnc")
    crumb = crumbs() + f' / <a href="topics.html">{bi("Topic guides", "Canllawiau pwnc")}</a>'
    main = g["hero"](t["era"], crumb, "book", "Topic guide", "Canllaw pwnc", t["en"], t["cy"], t["sEn"], t["sCy"], art=t["art"]) + out
    return g["page"](f"topic-{t['id']}.html", f"{t['en']}: a guide · History of Wales", f"{t['en']} in Welsh history: {t['sEn']} The people, key moments, words, documents and places in one guide.",
                     main, era=t["era"], ld=ld_article(f"{t['en']} in Welsh history", t["sEn"]), active="reference.html", track=f"page:topic-{t['id']}")


def topics_page(have):
    cards = "".join(f'<a href="topic-{t["id"]}.html" style="--c:{g["COL"][t["era"]]}"><span class="n">{bi("Topic guide", "Canllaw pwnc")}{g["new_tag"]("topic", t["id"])}</span><b>{bi(t["en"], t["cy"])}</b><span class="d">{bi(t["sEn"], t["sCy"])}</span></a>' for t in g["AD"].newest("topic", TP.TOPICS, ties="keep"))
    main = (g["hero"]("industrial", crumbs(), "book", "Reference", "Cyfeirlyfr", "Topic guides", "Canllawiau pwnc",
                      "Follow one thread through the whole of Welsh history: the language, faith, law, war, industry, the countryside, women, music and poetry, the Welsh abroad, science and sport.",
                      "Dilynwch un edefyn drwy hanes Cymru i gyd: yr iaith, ffydd, cyfraith, rhyfel, diwydiant, cefn gwlad, menywod, cerdd a barddoniaeth, y Cymry ar wasgar, gwyddoniaeth a chwaraeon.", art="book")
            + g["section"](f'<div class="ref-desk">{cards}</div>', top=True))
    return g["page"]("topics.html", "Topic guides to Welsh history · History of Wales",
                     "Guides to the big themes of Welsh history: the Welsh language, faith, law, war, industry, farming, women, music and poetry, the Welsh abroad, science and sport.",
                     main, era="industrial", og_type="website", ld=ld_article("Topic guides to Welsh history", "The big themes of Welsh history"), active="reference.html", track="page:topics")


TOPIC_CSS = """
.tp-intro{max-width:46rem;font-size:1.12rem;line-height:1.7}.tp-intro p{margin:0 0 1rem}
.tp-reads{margin-top:1.4rem}
.tp-people{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,14rem),1fr));gap:.7rem}
.tp-people a{display:grid;gap:.15rem;align-content:start;background:var(--slate);border:1px solid var(--line);border-radius:10px;padding:.75rem .9rem;text-decoration:none;color:var(--ink)}
.tp-people a:hover{border-color:var(--gold,#e8c65a)}
.tp-people b{font:600 1.05rem/1.25 var(--f-display)}.tp-people .dt{font:500 .75rem var(--f-mono);color:var(--muted)}.tp-people .d{font:400 .85rem/1.4 var(--f-body);color:var(--muted)}
.tp-ev{list-style:none;margin:0 0 1.2rem;padding:0;max-width:52rem;border-left:2px solid var(--line)}
.tp-ev li{display:grid;grid-template-columns:7.5rem 1fr;gap:.2rem 1rem;padding:.7rem 0 .7rem 1rem;position:relative}
.tp-ev li::before{content:"";position:absolute;left:-6px;top:1.05rem;width:10px;height:10px;border-radius:50%;background:var(--gold,#e8c65a)}
.tp-ev time{font:500 .8rem var(--f-mono);color:var(--muted);padding-top:.2rem}.tp-ev b{font:600 1.08rem var(--f-display)}.tp-ev p{margin:.2rem 0 0;line-height:1.55}
@media (max-width:560px){.tp-ev li{grid-template-columns:1fr}}
.tp-two{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,22rem),1fr));gap:2rem;align-items:start}
.tp-h{font:600 1.35rem var(--f-display);margin:0 0 .6rem}
.tp-az dt{font-weight:600;margin:.8rem 0 .15rem}.tp-az dt a{color:var(--ink)}.tp-az dd{margin:0;color:var(--muted);line-height:1.55}
.tp-others{display:flex;flex-wrap:wrap;gap:.5rem}
.tp-others a{border:1px solid var(--line);border-left:3px solid var(--c);border-radius:10px;padding:.5rem .9rem;text-decoration:none;color:var(--ink)}
.tp-others a:hover{border-color:var(--gold,#e8c65a)}
"""


# ---------- maps through time ----------
def _map_stages():
    st = list(g["D"].KINGDOMS)
    i = next(n for n, k in enumerate(st) if k["id"] == "today")
    return st[:i] + MP.MODERN + st[i:]


def _block_centres():
    """Area and centre of each map block (council area), from its outline, for placing names on the maps."""
    out = {}
    for n, d in g["la"].items():
        xs, ys = [], []
        for a, b in re.findall(r"(-?[\d.]+) (-?[\d.]+)", d):
            xs.append(float(a)); ys.append(float(b))
        w, h = max(xs) - min(xs), max(ys) - min(ys)
        out[n] = (w * h, min(xs) + w / 2, min(ys) + h / 2)
    return out


def stage_svg(k, ids, cen):
    names = list(g["la"].keys())
    colour = {}
    for gr in k["groups"]:
        for n in (names if gr[3] == "*" else gr[3]):
            colour[n] = gr[2]
    uses = "".join(f'<use href="#mla-{ids[n]}" fill="{colour.get(n, "#2a3142")}" stroke="{colour.get(n, "#2a3142")}"/>' for n in names)
    labels = ""
    for gr in k["groups"]:
        lab = gr[4] if len(gr) > 4 else [gr[0], gr[1]]
        if not lab[0]:
            continue
        blocks = names if gr[3] == "*" else [n for n in gr[3] if n in cen]
        sa = sum(cen[n][0] for n in blocks)
        if not sa:
            continue
        x = sum(cen[n][0] * cen[n][1] for n in blocks) / sa
        y = sum(cen[n][0] * cen[n][2] for n in blocks) / sa
        labels += f'<text class="kg-label" x="{x:.0f}" y="{y:.0f}"><tspan class="l-en">{g["e"](lab[0])}</tspan><tspan class="l-cy">{g["e"](lab[1])}</tspan></text>'
    return f'<svg class="mp-map" viewBox="-10 -10 620 691" role="img" aria-label="{g["e"](k["en"])}"><g class="mp-la">{uses}</g>{labels}</svg>'


def maps_page(have):
    stages = _map_stages()
    names = list(g["la"].keys())
    ids = {n: i for i, n in enumerate(names)}
    cen = _block_centres()
    defs = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>' + "".join(f'<path id="mla-{ids[n]}" d="{d}"/>' for n, d in g["la"].items()) + "</defs></svg>"
    jump = "".join(f'<a href="#map-{k["id"]}">{bi(k["en"].split(":")[0], k["cy"].split(":")[0])}</a>' for k in stages)
    cards = ""
    for n, k in enumerate(stages):
        legend = "".join(f'<li style="--k:{gr[2]}"><i></i>{bi(gr[0], gr[1])}</li>' for gr in k["groups"])
        nav = ((f'<a href="#map-{stages[n - 1]["id"]}">← {bi("Earlier", "Cynharach")}</a>' if n else "")
               + (f'<a href="#map-{stages[n + 1]["id"]}">{bi("Later", "Diweddarach")} →</a>' if n + 1 < len(stages) else ""))
        cards += (f'<article class="mp-stage" id="map-{k["id"]}">{stage_svg(k, ids, cen)}<div class="mp-text">'
                  f'<p class="bt-date">{bi("Map", "Map")} {n + 1} / {len(stages)}</p><h2>{bi(k["en"], k["cy"])}</h2><p>{bi(k["nEn"], k["nCy"])}</p>'
                  f'<ul class="kg-legend mp-legend">{legend}</ul>{link_chips(MP.SEE.get(k["id"], []), have)}<p class="mp-nav">{nav}</p></div></article>')
    main = (g["hero"]("roman", crumbs(), "book", "Reference", "Cyfeirlyfr", "Maps through time", "Mapiau drwy’r oesoedd",
                      f"{len(stages)} maps of Wales, from the four peoples who faced Rome to the Senedd today: the kingdoms, the princes, the March, the shires and the councils.",
                      f"{len(stages)} o fapiau o Gymru, o’r pedwar llwyth a wynebodd Rufain i’r Senedd heddiw: y teyrnasoedd, y tywysogion, y Mers, y siroedd a’r cynghorau.", art="roman")
            + g["section"](defs + f'<p class="ref-intro">{bi("Scroll down to watch the map of Wales change, or jump to a year. Borders before 1974 are drawn with modern council areas as building blocks, so they are close rather than exact.", "Sgroliwch i lawr i wylio map Cymru’n newid, neu neidiwch i flwyddyn. Mae’r ffiniau cyn 1974 wedi’u llunio gydag ardaloedd cynghorau modern fel blociau adeiladu, felly maent yn agos yn hytrach nag yn union.")}</p>'
                           f'<nav class="dc-jump mp-jump" aria-label="Maps / Mapiau">{jump}</nav>'
                           f'<p><a class="btn" href="map.html">{bi("Play the moving map", "Chwarae’r map symudol")} →</a></p>'
                           f'<div class="mp-list">{cards}</div>', top=True))
    return g["page"]("maps.html", "Maps of Wales through time · History of Wales",
                     "Historical maps of Wales: the four peoples, Roman Wales, the early kingdoms, Rhodri Mawr, Hywel Dda, Gruffudd ap Llywelyn, Pura Wallia and the March, 1267, 1284, Glyndŵr, the 13 shires, 1974, 1996 and today.",
                     main, era="roman", ld=ld_article("Maps of Wales through time", "How the map of Wales changed from the Roman conquest to today"), active="reference.html", track="page:maps")


MAP_CSS = """
.mp-list{display:grid;gap:2.2rem;margin-top:1.6rem}
.mp-stage{display:grid;grid-template-columns:minmax(0,22rem) minmax(0,1fr);gap:1.6rem 2.4rem;align-items:center;padding-top:1.6rem;border-top:1px solid var(--line);scroll-margin-top:5rem}
.mp-stage h2{font:600 clamp(1.5rem,3vw,2.1rem)/1.15 var(--f-display);margin:.2rem 0 .6rem}
.mp-text>p{line-height:1.65;max-width:38rem}
.mp-map{width:100%;height:auto;display:block}
.mp-la use{stroke-width:1.2;stroke-opacity:.9;fill-opacity:.85;stroke-linejoin:round}
.mp-map .kg-label{font-size:22px}
.mp-legend{margin:1rem 0 .4rem;grid-template-columns:repeat(auto-fill,minmax(12rem,1fr))}
.mp-nav{display:flex;gap:1.2rem;font-size:.9rem;margin-top:.8rem}.mp-nav a{color:var(--muted)}
@media (max-width:760px){.mp-stage{grid-template-columns:1fr}.mp-map{max-width:22rem;margin:0 auto}}
"""


# ---------- the historic sites map ----------
def _sites_raw():
    root = os.path.dirname(g["SRC"])
    path = os.path.join(root, "tools", "data", "sites_cadw.json")
    if not os.path.exists(path):
        return [], {}
    rows = json.load(open(path, encoding="utf-8"))
    gp = os.path.join(root, "tools", "data", "sites_guardian.json")
    guard = {}
    if os.path.exists(gp):
        for x in json.load(open(gp, encoding="utf-8")):
            num = str(x["p"].get("sm_number", "")).strip()
            if num:
                guard[num] = x
    return rows, guard


def site_rows():
    raw, guard = _sites_raw()
    geo = g["geo"]
    sc, k, minx, maxy = geo["sc"], geo["k"], geo["minx"], geo["maxy"]
    out = []
    for x in raw:
        p = x["p"]
        num = str(p.get("SAMNumber", "")).strip()
        gd = guard.get(num)
        en = (gd["p"].get("name") if gd else None) or x["n"].strip() or p.get("SiteType", "")
        cy = (gd["p"].get("name_cy") if gd else None) or p.get("Name_cy") or en
        en, cy = str(en).strip(), str(cy).strip()
        # Britons, not Celts (EDITORIAL.md): Cadw's 'Llangan Celtic Cross' is shown as 'Llangan Cross'.
        en, cy = en.replace(" Celtic Cross", " Cross"), cy.replace(" Celtic Cross", " Cross")
        typ, typ_cy = str(p.get("SiteType", "")).strip(), str(p.get("SiteType_cy", "") or p.get("SiteType", "")).strip()
        per = str(p.get("Period", "")).strip()
        cat = ST.classify(typ, per, p.get("BroadClass"))
        out.append(dict(q=str(p.get("RecordNumber", num)), num=num, en=en, cy=cy, typ=typ, typ_cy=typ_cy, per=per, cat=cat,
                        la=str(p.get("UnitaryAuthority", "")).replace("Rhondda Cynon Taff", "Rhondda Cynon Taf"),
                        la_cy=str(p.get("UnitaryAuthority_cy", "")), comm=str(p.get("Community", "")), lat=x["lat"], lon=x["lon"],
                        x=round((x["lon"] - minx) * k * sc, 1), y=round((maxy - x["lat"]) * sc, 1), visit=1 if gd else 0))
    return out


def sites_page(have):
    rows = site_rows()
    if not rows:
        return None
    las = sorted({(r["la"], r["la_cy"] or r["la"]) for r in rows}, key=lambda a: g["CS"].LA_ORDER.index(a[0]) if a[0] in g["CS"].LA_ORDER else 99)
    lai = {a[0]: i for i, a in enumerate(las)}
    kinds = {}
    for r in rows:
        kinds.setdefault(r["typ"], [r["typ"], r["typ_cy"], "", ""])
    places = g["D"].PLACES
    det = {}
    for r in rows:
        pl = next((p["id"] for p in places if abs(p["lat"] - r["lat"]) < .005 and abs(p["lon"] - r["lon"]) < .008), None)
        if pl and exists(f"place-{pl}.html", have):
            det[r["q"]] = {"l": [[f"place-{pl}.html", *TITLES.get(f"place-{pl}.html", (pl, pl))]]}
    data_rows = [[r["q"], r["en"], r["cy"], r["x"], r["y"], ST.CAT_IX[r["cat"]], r["typ"], r["per"], lai[r["la"]], r["lat"], r["lon"], r["visit"]] for r in rows]
    payload = dict(c=data_rows, d=det, k=kinds, g=[[c[1], c[2], c[3]] for c in ST.CATS], la=[list(a) for a in las], counties=g["county_lines"](),
                   W=g["geo"]["W"], H=g["geo"]["H"], P=[g["geo"]["minx"], g["geo"]["maxy"], g["geo"]["k"], g["geo"]["sc"]],
                   dc=ST.PERIOD_CY, order=list(range(len(ST.CATS) - 1, -1, -1)), hi0=False, hp="site-", aria="Map of Wales with its historic sites",
                   rec="http://cadwpublic-api.azurewebsites.net/reports/sam/FullReport?lang={lang}&id={q}",
                   t=dict(rec=["Cadw’s full record", "Cofnod llawn Cadw"],
                          access=["The big dots are sites cared for by Cadw and open to visit. Most other monuments are on private land: please check access first.", "Safleoedd yng ngofal Cadw ac ar agor i ymwelwyr yw’r dotiau mawr. Mae’r rhan fwyaf o henebion eraill ar dir preifat: gwiriwch fynediad yn gyntaf."],
                          none=["No site by that name", "Dim safle o’r enw hwnnw"], near=["The ten historic sites nearest to you", "Y deg safle hanesyddol agosaf atoch"],
                          far=["You look to be a long way from Wales. Here are the nearest sites all the same.", "Mae’n ymddangos eich bod ymhell o Gymru. Dyma’r safleoedd agosaf er hynny."]))
    n_all, n_visit = len(rows), sum(r["visit"] for r in rows)
    counts = [sum(1 for r in rows if r["cat"] == c[0]) for c in ST.CATS]
    chips = "".join(f'<button type="button" class="cm-chip on" data-g="{i}" aria-pressed="true" style="--gc:{c[3]}"><i></i>{bi(c[1], c[2])} <b>{counts[i]:,}</b></button>' for i, c in enumerate(ST.CATS))
    gcss = "".join(f".g{i}{{--gc:{c[3]}}}" for i, c in enumerate(ST.CATS))
    legend = "".join(f'<li style="--gc:{c[3]}"><i></i><span>{bi(c[1], c[2])}</span><small>{bi(c[4], c[5])}</small></li>' for c in ST.CATS)
    tool = (f'<div class="cm-tools"><div class="cm-search"><label class="sr-only" for="cm-q">{bi("Find a site", "Chwilio am safle")}</label>'
            f'<input id="cm-q" type="search" autocomplete="off" placeholder="Find a site…" data-ph-cy="Chwilio am safle…" data-ph-en="Find a site…">'
            f'<ul id="cm-res" class="cm-res" role="listbox" hidden></ul></div>'
            f'<div class="cm-btns"><button type="button" class="btn" id="cm-near">{bi("Sites near me", "Safleoedd yn agos ataf")}</button>'
            f'<button type="button" class="btn ghost" id="cm-rand">{bi("Surprise me", "Synnwch fi")}</button></div>'
            f'<div class="cm-chips" role="group" aria-label="Kinds of site / Mathau o safle">{chips}</div></div>')
    mapbox = (f'<div class="cm-wrap">{tool}<div class="cm-map" id="cm-map" tabindex="0" aria-label="Map of the historic sites of Wales / Map o safleoedd hanesyddol Cymru">'
              f'<noscript><p>{bi("The map needs JavaScript. The sites you can visit are listed below.", "Mae angen JavaScript ar y map. Rhestrir y safleoedd y gallwch ymweld â nhw isod.")}</p></noscript>'
              f'<div class="cm-zoom"><button type="button" id="cm-in" aria-label="Zoom in / Chwyddo i mewn">+</button><button type="button" id="cm-out" aria-label="Zoom out / Chwyddo allan">−</button>'
              f'<button type="button" id="cm-home" aria-label="Whole of Wales / Cymru gyfan"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5" fill="none" stroke="currentColor" stroke-width="2"/></svg></button></div>'
              f'<p class="cm-hint" id="cm-hint">{bi("Drag to move, pinch or scroll to zoom, tap a dot", "Llusgwch i symud, pinsiwch neu sgroliwch i chwyddo, tapiwch ddot")}</p></div>'
              f'<div class="cm-side"><div id="cm-card" class="cm-card" aria-live="polite" tabindex="0">'
              f'<p class="eyebrow">{bi(f"{n_all:,} historic sites", f"{n_all:,} o safleoedd hanesyddol")}</p>'
              f'<h2>{bi("Choose a site", "Dewiswch safle")}</h2><p class="muted">{bi(f"Every scheduled monument in Wales: tap a dot, search by name, or find the sites nearest to you. The {n_visit} big dots are the sites Cadw looks after and opens to visitors.", f"Pob heneb gofrestredig yng Nghymru: tapiwch ddot, chwiliwch yn ôl enw, neu dewch o hyd i’r safleoedd agosaf atoch. Y {n_visit} dot mawr yw’r safleoedd y mae Cadw’n gofalu amdanynt ac yn eu hagor i ymwelwyr.")}</p>'
              f'<ul class="cm-legend">{legend}</ul></div></div></div>')
    visit = [r for r in rows if r["visit"]]
    lists = ""
    for la, la_cy in las:
        rs = sorted([r for r in visit if r["la"] == la], key=lambda r: r["en"])
        if rs:
            items = "".join(f'<li><button class="cm-show g{ST.CAT_IX[r["cat"]]}" data-q="{r["q"]}"><i></i>{bi(r["en"], r["cy"])}</button></li>' for r in rs)
            lists += f'<details class="cm-la"><summary>{bi(la, la_cy)} <b>{len(rs)}</b></summary><ul>{items}</ul></details>'
    intro_en = ["Wales has one of the richest landscapes of monuments in Europe: burial chambers older than the pyramids, stone circles, more than a thousand hillforts, Roman forts, the carved stones of the early kings and saints, abbeys, castles and the works of the first industrial nation.",
                f"This map shows all {n_all:,} scheduled monuments, the sites protected by law as the most important in Wales. Filter by kind, zoom in to your own area, or tap “Sites near me” to find what is on your doorstep."]
    intro_cy = ["Mae gan Gymru un o dirweddau henebion cyfoethocaf Ewrop: siambrau claddu hŷn na’r pyramidiau, cylchoedd cerrig, mwy na mil o fryngaerau, caerau Rhufeinig, cerrig cerfiedig y brenhinoedd a’r seintiau cynnar, abatai, cestyll a gweithfeydd y genedl ddiwydiannol gyntaf.",
                f"Mae’r map hwn yn dangos pob un o’r {n_all:,} o henebion cofrestredig, y safleoedd a warchodir gan y gyfraith fel y pwysicaf yng Nghymru. Hidlwch yn ôl math, chwyddwch i mewn i’ch ardal chi, neu tapiwch “Safleoedd yn agos ataf” i weld beth sydd ar garreg eich drws."]
    note = bi("Contains public sector information licensed under the Open Government Licence v3.0: Cadw’s scheduled monuments and guardianship sites, from DataMapWales. The kinds are grouped for this site. Relief from open elevation data (Mapzen Terrarium).",
              "Yn cynnwys gwybodaeth sector cyhoeddus a drwyddedir dan y Drwydded Llywodraeth Agored v3.0: henebion cofrestredig a safleoedd gwarcheidiaeth Cadw, o MapDataCymru. Grwpiwyd y mathau ar gyfer y wefan hon. Tirwedd o ddata uchder agored (Mapzen Terrarium).")
    main = (g["hero"]("ancient", crumbs(), "dolmen", f"{n_all:,} sites", f"{n_all:,} o safleoedd", "Historic sites map", "Map safleoedd hanesyddol",
                      "Every protected ancient monument in Wales on one map: cromlechs, standing stones, hillforts, Roman forts, carved stones, abbeys, castles and industry.",
                      "Pob heneb hynafol warchodedig yng Nghymru ar un map: cromlechi, meini hirion, bryngaerau, caerau Rhufeinig, cerrig cerfiedig, abatai, cestyll a diwydiant.", art="dolmen")
            + f'<style>{g["read"]("castles.css")}{gcss}</style><section class="cm-sec" id="map"><div class="wrap">{mapbox}</div></section>'
            + g["section"]("".join(f"<p>{bi(a, b)}</p>" for a, b in zip(intro_en, intro_cy)), top=True)
            + g["section"](f'<p class="lede">{bi(f"The {n_visit} sites in the care of Cadw, open to visit, area by area.", f"Y {n_visit} o safleoedd yng ngofal Cadw, ar agor i ymwelwyr, fesul ardal.")}</p><div class="cm-lists">{lists}</div>'
                           f'<p style="margin-top:1.4rem"><a class="btn" href="castles.html">{bi("The castles map", "Map y cestyll")} →</a> <a class="btn" href="maps.html">{bi("Maps through time", "Mapiau drwy’r oesoedd")} →</a></p>'
                           f'<p class="note-box" style="margin-top:2rem">{note}</p>', "Places you can visit", "Lleoedd y gallwch ymweld â nhw"))
    extra = f'<script>var CMAP={json.dumps(payload, ensure_ascii=False, separators=(",", ":"))};</script>\n<script src="castles.js?v=3" defer></script>\n'
    ld = {"@context": "https://schema.org", "@type": "Map", "name": "The historic sites of Wales", "inLanguage": ["en", "cy"],
          "description": f"An interactive map of {n_all} scheduled monuments in Wales.", "isPartOf": {"@type": "WebSite", "name": "History of Wales", "url": g["BASE_URL"]}}
    return g["page"]("sites.html", "Historic sites of Wales: interactive map · History of Wales",
                     f"An interactive map of all {n_all:,} scheduled monuments in Wales: burial chambers, standing stones, hillforts, Roman forts, inscribed stones, abbeys, castles and industrial sites, with the sites near you.",
                     main, era="ancient", ld=ld, og_type="website", active="reference.html", track="page:sites", extra=extra)


# ---------- the look-it-up desk ----------
DESK = [  # href, English, Welsh, English line, Welsh line, era colour
    ("a-z.html", "The A–Z", "Yr A–Y", "Words, laws and ideas, each explained in a few lines.", "Geiriau, cyfreithiau a syniadau, pob un wedi’i egluro mewn ychydig linellau.", "kings"),
    ("questions.html", "Quick answers", "Atebion cyflym", "The questions people ask most about Welsh history, answered.", "Y cwestiynau a ofynnir amlaf am hanes Cymru, wedi’u hateb.", "today"),
    ("towns.html", "Towns and villages", "Trefi a phentrefi", "What every place name means, and what happened there.", "Beth mae pob enw lle’n ei olygu, a beth ddigwyddodd yno.", "saints"),
    ("battles.html", "Battles of Wales", "Brwydrau Cymru", "Every recorded battle and raid, from the Romans to Helmand, and who it was against.", "Pob brwydr a chyrch a gofnodwyd, o’r Rhufeiniaid i Helmand, ac yn erbyn pwy.", "medieval"),
    ("documents.html", "Key documents", "Dogfennau allweddol", "The words of the treaties, letters and laws that shaped Wales.", "Geiriau’r cytundebau, y llythyrau a’r deddfau a luniodd Gymru.", "tudor"),
    ("sites.html", "Historic sites map", "Map safleoedd hanesyddol", "Hillforts, burial chambers, standing stones, Roman forts, abbeys and holy wells.", "Bryngaerau, cromlechi, meini hirion, caerau Rhufeinig, abatai a ffynhonnau sanctaidd.", "ancient"),
    ("maps.html", "Maps through time", "Mapiau drwy’r oesoedd", "Watch the map of Wales change from the four peoples to today.", "Gwyliwch fap Cymru’n newid o’r pedwar llwyth hyd heddiw.", "roman"),
    ("topics.html", "Topic guides", "Canllawiau pwnc", "Faith, industry, law, music, women, war and the Welsh abroad.", "Ffydd, diwydiant, cyfraith, cerddoriaeth, menywod, rhyfel a’r Cymry ar wasgar.", "industrial"),
    ("kings.html", "Kings and princes", "Brenhinoedd a thywysogion", "Every ruler of every Welsh kingdom, in order.", "Pob rheolwr ym mhob teyrnas Gymreig, yn eu trefn.", "kings"),
    ("family-trees.html", "Royal family trees", "Coed teulu brenhinol", "From Rhodri Mawr to Harri Tudur.", "O Rhodri Mawr i Harri Tudur.", "kings"),
    ("castles.html", "Castles map", "Map y cestyll", "All 827 castle sites in Wales and who built them.", "Pob un o’r 827 o safleoedd cestyll yng Nghymru a phwy a’u cododd.", "medieval"),
    ("saints.html", "Saints of Wales", "Seintiau Cymru", "The saints, their feast days and the llannau named after them.", "Y seintiau, eu gwyliau a’r llannau a enwyd ar eu hôl.", "saints"),
    ("timeline.html", "The timeline", "Y llinell amser", "Over 400 events from 230,000 years ago to today.", "Dros 400 o ddigwyddiadau o 230,000 o flynyddoedd yn ôl hyd heddiw.", "modern"),
    ("people.html", "Famous people", "Pobl enwog", "322 people from every age of Welsh history.", "322 o bobl o bob oes yn hanes Cymru.", "industrial"),
    ("laws.html", "The Laws of Hywel Dda", "Cyfreithiau Hywel Dda", "The law of Wales for six hundred years.", "Cyfraith Cymru am chwe chan mlynedd.", "kings"),
    ("onthisday.html", "On this day", "Ar y dydd hwn", "What happened on every day of the year.", "Beth ddigwyddodd ar bob diwrnod o’r flwyddyn.", "medieval"),
    ("names.html", "Welsh surnames", "Cyfenwau Cymraeg", "What Welsh surnames mean and where they come from.", "Beth mae cyfenwau Cymraeg yn ei olygu ac o ble maent yn dod.", "saints"),
    ("family-history.html", "Family history", "Hanes teulu", "Trace your Welsh ancestors: census, parish and chapel books, wills and tithe maps.", "Olrhain eich hynafiaid: y cyfrifiad, llyfrau’r plwyf a’r capel, ewyllysiau a mapiau’r degwm.", "revival"),
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
    out = {"a-z.html": az_page(have), "questions.html": questions_page(have), "towns.html": towns_page(have), "battles.html": battles_page(have), "documents.html": documents_page(have), "topics.html": topics_page(have), "maps.html": maps_page(have), "reference.html": desk_page(have)}
    for t in TP.TOPICS:
        out[f"topic-{t['id']}.html"] = topic_page(t, have)
    sites = sites_page(have)
    if sites:
        out["sites.html"] = sites
    return out


PAGE_NAMES = ["a-z.html", "questions.html", "towns.html", "battles.html", "documents.html", "topics.html", "maps.html", "sites.html", "reference.html"] + [f"topic-{t['id']}.html" for t in TP.TOPICS]


def search_items():
    items = [dict(k="term", t=t["en"], c=t["cy"], u=f"a-z.html#az-{t['id']}", y=["A–Z", "A–Y"], b=[t["dEn"], t["dCy"]], e="kings") for t in AZ.TERMS]
    items += [dict(k="question", t=q["qEn"], c=q["qCy"], u=f"questions.html#q-{q['id']}", y=["Quick answer", "Ateb cyflym"], b=[q["aEn"], q["aCy"]], e="today") for gr in FAQ.GROUPS for q in gr["qs"]]
    items += [dict(k="town", t=r["cy"], c=r["cy"], u=f"towns.html#{r['id']}", y=[r["en"] if r["en"] != r["cy"] else r["la"], r["laCy"]], b=[r["mEn"].capitalize() + ". " + r["hEn"], r["mCy"].capitalize() + ". " + r["hCy"]], e="saints", a=r["en"]) for r in town_rows() if not __import__("townpages").has_page(r["id"])]
    items.append(dict(k="page", t="Towns and villages: what Welsh place names mean", c="Trefi a phentrefi: ystyr enwau lleoedd", u="towns.html", y=["Place names", "Enwau lleoedd"],
                      b=["What Welsh place names mean, with a decoder for any name: aber, llan, caer, pen, tre and more.", "Ystyr enwau lleoedd Cymru, gyda datgodiwr i unrhyw enw: aber, llan, caer, pen, tre a rhagor."], e="saints"))
    items += [dict(k="battle", t=b["en"], c=b["cy"], u=f"battles.html#b-{b['id']}", y=[b["dEn"], b["dCy"]], b=[b["sEn"] + ". " + b["tEn"], b["sCy"] + ". " + b["tCy"]], e=b["era"]) for b in BT.BATTLES]
    items.append(dict(k="page", t="Battles of Wales", c="Brwydrau Cymru", u="battles.html", y=["Map", "Map"], b=["Every battle of Welsh history on a map, from Catraeth to Mametz Wood.", "Pob brwydr yn hanes Cymru ar fap, o Gatraeth i Goed Mametz."], e="medieval"))
    items += [dict(k="doc", t=d["en"], c=d["cy"], u=f"documents.html#doc-{d['id']}", y=[d["dEn"], d["dCy"]], b=[d["aEn"] + " " + d["wEn"], d["aCy"] + " " + d["wCy"]], e=d["era"]) for d in DC.DOCS]
    items.append(dict(k="page", t="Key documents of Welsh history", c="Dogfennau allweddol hanes Cymru", u="documents.html", y=["Reference", "Cyfeirlyfr"], b=["The treaties, letters and laws that shaped Wales, in their own words.", "Y cytundebau, y llythyrau a’r deddfau a luniodd Gymru, yn eu geiriau eu hunain."], e="tudor"))
    items += [dict(k="topic", t=t["en"], c=t["cy"], u=f"topic-{t['id']}.html", y=["Topic guide", "Canllaw pwnc"], b=[t["sEn"], t["sCy"]], e=t["era"]) for t in TP.TOPICS]
    items += [dict(k="map", t=k["en"], c=k["cy"], u=f"maps.html#map-{k['id']}", y=["Maps through time", "Mapiau drwy’r oesoedd"], b=[k["nEn"], k["nCy"]], e="roman") for k in _map_stages()]
    items.append(dict(k="page", t="Maps of Wales through time", c="Mapiau o Gymru drwy’r oesoedd", u="maps.html", y=["Reference", "Cyfeirlyfr"], b=["How the map of Wales changed, from the four peoples who faced Rome to the twenty-two councils and the Senedd.", "Sut y newidiodd map Cymru, o’r pedwar llwyth a wynebodd Rufain i’r dau gyngor ar hugain a’r Senedd."], e="roman"))
    items += [dict(k="site", t=r["en"], c=r["cy"], u=f"sites.html#site-{r['q']}", y=[r["typ"], r["typ_cy"]], b=[f"{r['typ']}, {r['la']}. In the care of Cadw and open to visit.", f"{r['typ_cy']}, {r['la_cy']}. Yng ngofal Cadw ac ar agor i ymwelwyr."], e="ancient") for r in site_rows() if r["visit"]]
    items.append(dict(k="page", t="Historic sites map", c="Map safleoedd hanesyddol", u="sites.html", y=["Map", "Map"], b=["Every scheduled monument in Wales on one map: burial chambers, standing stones, hillforts, Roman forts, carved stones, abbeys and industry.", "Pob heneb gofrestredig yng Nghymru ar un map: siambrau claddu, meini hirion, bryngaerau, caerau Rhufeinig, cerrig cerfiedig, abatai a diwydiant."], e="ancient"))
    items.append(dict(k="page", t="The A–Z of Welsh history", c="A–Y hanes Cymru", u="a-z.html", y=["Reference", "Cyfeirlyfr"],
                      b=["Words, laws, places and ideas from Welsh history, each explained in a few lines.", "Geiriau, cyfreithiau, lleoedd a syniadau o hanes Cymru, pob un wedi’i egluro mewn ychydig linellau."], e="kings"))
    items.append(dict(k="page", t="Look it up: the reference desk", c="Chwilio’r hanes: y ddesg gyfeirio", u="reference.html", y=["Reference", "Cyfeirlyfr"],
                      b=["Every way to look up Welsh history on this site in one place.", "Pob ffordd o chwilio hanes Cymru ar y wefan hon mewn un lle."], e="kings"))
    return items
