# A real picture for every page: the photograph or old artwork behind each page's title, and on its card.
# Ifan (2026-11-12) asked for real pictures instead of the drawn scenes, on every page.
#
# Every picture is one already kept on the site, with its Wikimedia Commons credit:
#   "g:<id>"  a gallery picture (src/gallery_photos.py, files in src/static/gallery/)
#   "p:<id>"  a person's photo (src/photos.py PERSON_PHOTOS, files in src/static/photos/)
#   "l:<key>" a legend photo (src/art.py LEGEND_PHOTOS, files in src/static/legends/)
# To change a page's picture, change its line in PAGE below. Pages not listed take their place's own picture,
# or the picture for their age (ERA below). build.py calls dress() on every page and card_img() for the cards.
import json
import os
import re
from html import escape as _esc
from urllib.parse import quote as _q

import gallery_photos as GP
import photos as PH
import art as A

COMMONS = "https://commons.wikimedia.org/wiki/"
_HERE = os.path.dirname(os.path.abspath(__file__))
_LOCAL = json.load(open(os.path.join(_HERE, "photo_files.json"), encoding="utf-8"))

# One picture for each age: the age's own page, its teacher pack, and any page in that age without its own picture.
ERA = dict(
    ancient="g:place-pentreifan",
    roman="g:place-caerleon",
    saints="g:place-stdavids",
    kings="g:place-eliseg",
    medieval="g:place-harlech",
    tudor="g:place-rhaglan",
    industrial="g:place-pontcysyllte",
    modern="g:place-celyn",
    today="g:place-senedd",
)

PAGE = {
    # long reads
    "story-castles.html": "g:place-caernarfon",
    "story-language.html": "g:trea-bible-1588",
    "story-hywel.html": "g:trea-laws-hywel",
    "story-coal.html": "g:place-blaenavon",
    "story-protest.html": "g:place-westgate",
    "story-world.html": "g:indu-coal-exchange",
    "story-arthur.html": "g:person-arthur",
    "story-glyndwr.html": "g:trea-pennal-letter",
    "story-longbow.html": "g:place-cardigan",
    "story-learning.html": "g:place-llanilltud",
    "story-unconquered.html": "g:cast-dolwyddelan",
    "story-firsts.html": "g:place-merthyr",
    "story-brittany.html": "g:person-cadog",
    "story-revival.html": "g:person-gwynfor-evans",
    "story-iolo.html": "g:person-iolo-morganwg",
    "story-wilson-blackett.html": "g:anci-maen-ceti",
    "story-brutus.html": "g:trea-red-book",
    "story-celts.html": "g:person-edward-lhuyd@50% 15%",
    "story-madog.html": "g:land-south-stack",
    "story-caradog.html": "g:person-caratacus",
    "story-macsen.html": "g:place-segontium",
    "story-christianity.html": "g:holy-margam",
    "story-industry.html": "g:indu-ffestiniog-rly",
    "story-lucius.html": "g:holy-llandaff",
    "story-bran.html": "g:place-harlech",
    "story-joseph.html": "g:person-dewi-sant",
    # legends that have no photograph of their own yet
    "legend-dragons.html": "g:land-dinas-emrys",
    "legend-lludd.html": "g:land-dinas-emrys",
    "legend-macsen.html": "g:place-segontium",
    "legend-pwyll.html": "g:anci-carn-ingli",
    "legend-manawydan.html": "g:anci-gors-fawr",
    "legend-culhwch.html": "g:anci-carreg-samson",
    "legend-dwynwen.html": "g:land-llanddwyn",
    "legend-melangell.html": "g:holy-pennant-melangell",
    "legend-gwenffrewi.html": "g:place-treffynnon",
    "legend-cadair.html": "g:land-cadair-idris",
    "legend-owain.html": "g:holy-valle-crucis",
    "legend-twm.html": "p:twm-sion-cati",
    "legend-afanc.html": "g:land-yr-wyddfa",
    "legend-tylwyth.html": "g:land-llyn-idwal",
    "legend-arthur.html": "g:anci-maen-ceti",
    # the ages of kings and the saints of each kingdom
    "kings.html": "g:place-eliseg",
    "kings-gwynedd.html": "g:place-aberffraw",
    "kings-powys.html": "g:place-mathrafal",
    "kings-deheubarth.html": "g:place-dinefwr",
    "kings-dyfed.html": "g:place-castellhenllys",
    "kings-ceredigion.html": "g:holy-llanbadarn",
    "kings-gwent.html": "g:place-caerwent",
    "kings-glywysing.html": "g:holy-margam",
    "kings-brycheiniog.html": "g:land-pen-y-fan",
    "kings-gwy-a-hafren.html": "g:place-epynt",
    "kings-rhos.html": "g:person-llywelyn-fawr",
    "kings-meirionnydd.html": "g:land-cadair-idris",
    "kings-ergyng.html": "g:holy-llanthony",
    "kings-rheged.html": "g:trea-book-taliesin",
    "kings-gododdin.html": "g:trea-book-aneirin",
    "kings-ystrad-clud.html": "g:person-aneirin",
    "kings-elfed.html": "g:land-tryfan",
    "kings-efrog.html": "g:anci-tomen-y-mur",
    "saints.html": "g:holy-st-govans",
    "saints-dyfed.html": "g:place-stdavids",
    "saints-ystrad-tywi.html": "g:holy-talley",
    "saints-ceredigion.html": "g:holy-llanbadarn",
    "saints-gwynedd.html": "g:place-enlli",
    "saints-rhos.html": "g:holy-llangelynnin",
    "saints-powys.html": "g:holy-pennant-melangell",
    "saints-brycheiniog.html": "g:holy-brecon",
    "saints-morgannwg.html": "g:place-llanilltud",
    "saints-gwent.html": "g:place-caerwent",
    "saints-llydaw.html": "g:person-illtud",
    # topic guides and trails
    "topics.html": "g:place-library",
    "topic-abroad.html": "p:lewis-jones-patagonia",
    "topic-countryside.html": "g:place-stfagans",
    "topic-faith.html": "g:holy-soar-y-mynydd",
    "topic-industry.html": "g:place-dinorwig",
    "topic-language.html": "g:trea-black-book",
    "topic-law.html": "g:place-hendygwyn",
    "topic-music.html": "g:trea-welsh-harp",
    "topic-science.html": "g:person-william-grove",
    "topic-sport.html": "g:place-stadiwm",
    "topic-war.html": "g:place-caerffili",
    "topic-women.html": "g:person-gwenllian",
    "trails.html": "g:place-offasdyke",
    "trail-coal.html": "g:indu-rhondda",
    "trail-sea.html": "g:land-south-stack",
    "trail-song.html": "g:holy-tabernacl",
    "trail-women.html": "g:place-fishguard",
    # index pages and the rest
    "stories.html": "g:trea-black-book",
    "legends.html": "g:land-dinas-emrys",
    "mabinogion.html": "g:trea-red-book",
    "literature.html": "g:trea-book-aneirin",
    "books-and-authors.html": "g:place-library",
    "documents.html": "g:trea-llywelyn-seal",
    "symbols.html": "g:trea-lovespoon",
    "play.html": "g:place-caerleon",
    "quiz.html": "g:place-conwy",
    "pairs.html": "g:cast-carreg-cennen",
    "map-game.html": "g:cast-criccieth",
    "names.html": "g:buil-llanfairpwll",
    "journey.html": "g:land-crib-goch",
    "ride-glyndwr.html": "g:person-owain-glyndwr",
    "timeline.html": "g:place-eliseg",
    "people.html": "g:buil-city-hall",
    "map.html": "g:place-beaumaris",
    "family-trees.html": "g:place-penfro",
    "onthisday.html": "g:place-stfagans",
    "daily.html": "g:land-llyn-ogwen",
    "today.html": "g:land-llyn-ogwen",
    "whatsnew.html": "g:place-senedd",
    "about.html": "g:place-library",
    "teachers.html": "g:buil-old-college",
    "reference.html": "g:place-library",
    "a-z.html": "g:trea-black-book",
    "questions.html": "g:buil-national-museum",
    "battles.html": "g:cast-carreg-cennen",
    "maps.html": "g:place-offasdyke",
    "sites.html": "g:anci-maen-ceti",
    "towns.html": "g:buil-tenby",
    "welsh.html": "g:trea-black-book",
    "wales-in-10.html": "g:land-yr-wyddfa",
    "castles.html": "g:place-harlech",
    "gallery.html": "g:place-conwy",
    "404.html": "g:land-borth-forest",
    "laws.html": "g:trea-laws-hywel",
    "llys-rhosyr.html": "g:anci-llys-rhosyr",
}

# Pages that keep the picture they already have at the top (nothing to replace).
SKIP = {"index.html"}


def _parse(ref):
    """A picture's files, size and credit. A ref may end in "@x% y%" to say where the subject sits in the frame."""
    ref, _, at = ref.partition("@")
    p = _parse1(ref)
    if at:
        p["pos"] = at
    return p


def _parse1(ref):
    kind, key = ref.split(":", 1)
    if kind == "g":
        f, by, lic, licu, en, cy, w, h = GP.GALLERY[key]
        return dict(src=f"gallery/{key}.webp", small=f"gallery/{key}-s.webp", w=w, h=h, file=f, by=by, lic=lic, licu=licu, en=en, cy=cy, pos="50% 30%" if h > w * .9 else "50% 50%")
    if kind == "p":
        ph = PH.PERSON_PHOTOS[key]
        f, en, cy = ph[:3]
        cr = ph[3] if len(ph) > 3 else ""
        loc = _LOCAL[f]
        return dict(src=f"photos/{loc[0]}.webp", small=f"photos/{loc[0]}-s.webp", w=loc[1], h=loc[2], file=f, by=cr, lic="", licu="", en=en, cy=cy, pos="50% 30%")
    if kind == "l":
        ph = A.LEGEND_PHOTOS[key]
        return dict(src=f"legends/{key}.webp", small=f"legends/{key}-s.webp", w=1280, h=853, file=ph[0], by=ph[1], lic=ph[2], licu=ph[3], en=ph[4], cy=ph[5], pos=ph[6])
    raise KeyError(ref)


def check():
    """Stop the build if a picture named here is missing (a typo, or a gallery picture taken out)."""
    for ref in list(ERA.values()) + list(PAGE.values()) + W10:
        p = _parse(ref)
        for f in (p["src"], p["small"]):
            if not os.path.exists(os.path.join(_HERE, "static", f)):
                raise SystemExit(f"src/pictures.py: {ref} has no file {f}")


def for_page(path, era=None):
    if path in SKIP:
        return None
    if path in PAGE:
        return PAGE[path]
    m = re.match(r"place-(.+)\.html$", path)
    if m and "place-" + m.group(1) in GP.GALLERY:
        return "g:place-" + m.group(1)
    m = re.match(r"(?:era|pack)-(.+)\.html$", path)
    if m and m.group(1) in ERA:
        return ERA[m.group(1)]
    return ERA.get(era) if era else None


def _bi(en, cy):
    return f'<span class="l-en" lang="en">{en}</span><span class="l-cy" lang="cy">{cy}</span>'


def credit(ref):
    p = _parse(ref)
    who = _esc(p["by"]) if p["by"] else ""
    lic = f'<a href="{_esc(p["licu"])}" target="_blank" rel="noopener license">{_esc(p["lic"])}</a>' if p["lic"] else ""
    bits = ", ".join(x for x in (who, lic) if x)
    bits = _bi(bits, bits.replace("Public domain", "Parth cyhoeddus")) if bits else ""
    return (f'<p class="hero-credit">{_bi("Picture", "Llun")}: {_bi(_esc(p["en"]), _esc(p["cy"]))}'
            f'{" · " + bits if bits else ""} · <a href="{COMMONS}File:{_q(p["file"].replace(" ", "_"), safe="")}" target="_blank" rel="noopener">Wikimedia Commons</a></p>')


def hero_img(ref):
    p = _parse(ref)
    return (f'<img class="scene photo" src="{p["src"]}" srcset="{p["small"]} 600w, {p["src"]} {p["w"]}w" sizes="100vw" '
            f'width="{p["w"]}" height="{p["h"]}" alt="" decoding="async" fetchpriority="high" style="object-fit:cover;object-position:{p["pos"]}">')


def card_img(path, era=None):
    """The picture for a card that links to a page (a long read, a legend, an age), or None."""
    ref = for_page(path, era)
    if not ref:
        return None
    p = _parse(ref)
    return (f'<img class="scene photo" src="{p["small"]}" srcset="{p["small"]} 600w, {p["src"]} {p["w"]}w" sizes="(max-width: 700px) 100vw, 40vw" '
            f'width="{p["w"]}" height="{p["h"]}" alt="" loading="lazy" decoding="async" style="object-fit:cover;object-position:{p["pos"]}">')


_HDR = re.compile(r'<header class="era-hero([^"]*)"([^>]*)>')
_ART = re.compile(r'<div class="hero-art">.*?</svg></div>', re.S)
_ILL = re.compile(r'<svg class="ill"[^>]*>.*?</svg>', re.S)


def dress(path, era, html):
    """Put the page's picture at the top of the page, in place of the drawn scene, with its credit."""
    m = _HDR.search(html)
    if not m:
        return html
    end = html.find("</header>", m.end())
    seg = html[m.start():end]
    if 'class="scene photo"' in seg:  # a legend with its own photograph already
        return html
    ref = for_page(path, era)
    if not ref:
        return html
    pic = f'<div class="hero-art">{hero_img(ref)}</div>'
    if '<div class="hero-art">' in seg:
        seg = _ART.sub(lambda _: pic, seg, count=1)
    else:
        seg = _ILL.sub("", seg, count=1)
        seg = seg.replace(m.group(0), f'<header class="era-hero has-art{m.group(1)}"{m.group(2)}>{pic}', 1)
    k = seg.rfind("</div>")
    seg = seg[:k] + credit(ref) + seg[k:]
    return html[:m.start()] + seg + html[end:]


# Wales in 10 minutes: one picture on each of the seventeen steps.
W10 = ["g:land-yr-wyddfa", "g:place-pentreifan", "g:person-caratacus", "g:place-caerleon", "g:place-stdavids", "g:person-rhodri-mawr",
       "g:trea-laws-hywel", "g:place-mathrafal", "g:person-gruffudd-ap-llywelyn", "g:place-strataflorida", "g:person-llywelyn-ap-gruffudd",
       "g:place-cilmeri", "g:trea-pennal-letter", "g:trea-bible-1588", "g:place-merthyr", "g:place-celyn", "g:place-senedd"]


def small_fig(ref, cls="w10-pic"):
    """A small picture with its caption and credit, for inside a card or step."""
    p = _parse(ref)
    who = ", ".join(x for x in (_esc(p["by"]), _esc(p["lic"])) if x)
    return (f'<figure class="{cls}"><img src="{p["small"]}" width="{p["w"]}" height="{p["h"]}" alt="{_esc(p["en"])}" loading="lazy" decoding="async" '
            f'style="object-position:{p["pos"]}"><figcaption>{_bi(_esc(p["en"]), _esc(p["cy"]))} · '
            f'<a href="{COMMONS}File:{_q(p["file"].replace(" ", "_"), safe="")}" target="_blank" rel="noopener">{who + ", " if who else ""}Wikimedia Commons</a></figcaption></figure>')
