"""Search engine extras, added to every page automatically by build.py.

Nothing here needs filling in by hand. Any page made with page() in build.py gets:
  * a tidy title and description (shortened if Google would cut them off),
  * structured data (JSON-LD) that tells Google what the page is: the page's own
    data (Person, Place, Article...) plus the site name and a breadcrumb trail,
    read from the "History of Wales / Legends" crumbs shown at the top of the page,
  * an entry in sitemap.xml with the date the page last really changed, and its pictures.

The home page also says, in structured data, that the site is called
"History of Wales" (Hanes Cymru), so Google can show that name in results.
"""
import hashlib, html, json, os, re, time, urllib.request, datetime

SITE_EN = "History of Wales"
SITE_CY = "Hanes Cymru"
SUFFIX = " · History of Wales"
INDEXNOW_KEY = "0f018dbe52162810deccbb68ce860fd8"   # public by design: the key file sits at the site root
LASTMOD_FILE = "seo-lastmod.json"                    # page -> [content fingerprint, date it last changed]
AUTHOR = None   # the author's name (set by build.py from src/about.py); None: articles are credited to the site


def _strip(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


# Hub pages get titles in the words people type into Google ("Welsh history timeline", "Welsh legends").
# The page itself is unchanged; only the title in the browser tab and in search results.
TITLES = {
    "timeline.html": "Welsh history timeline: 230,000 BC to today",
    "quiz.html": "Welsh history quiz",
    "people.html": "Famous Welsh people from every age",
    "map.html": "Map of Welsh history: historic places and kingdoms",
    "play.html": "Welsh history games and quizzes",
    "daily.html": "Daily Welsh history challenge",
    "stories.html": "Long reads on Welsh history",
    "legends.html": "Welsh legends, myths and folk tales",
    "trails.html": "Welsh history trails",
    "gallery.html": "Pictures of Welsh history: the gallery",
    "teachers.html": "Welsh history for teachers and schools",
    "names.html": "Welsh surnames and what they mean",
    "symbols.html": "Welsh symbols and traditions",
    "map-game.html": "Where in Wales? A Welsh history map game",
    "era-ancient.html": "Ancient Wales: Stone Age to Iron Age (230,000 BC–AD 48)",
    "era-roman.html": "Roman Wales (AD 48–410)",
    "era-saints.html": "The Age of Saints in Wales (410–800)",
    "era-kings.html": "The Age of Kings in Wales (800–1100)",
    "era-medieval.html": "The Age of the Welsh Princes (1100–1485)",
    "era-tudor.html": "Tudor and Stuart Wales (1485–1750)",
    "era-industrial.html": "Industrial Wales (1750–1914)",
    "era-modern.html": "Twentieth-century Wales (1914–1997)",
    "era-today.html": "Wales today: devolution and the Senedd (1997–today)",
}


def title_for(path, title):
    """The page's search title: a better-worded one for hub pages, otherwise the page's own."""
    if path in TITLES:
        return TITLES[path] + SUFFIX
    return title


ENDINGS = (SUFFIX, " · Hanes Cymru", " · The old books of Wales", " · Hen lyfrau Cymru")


def tidy_title(title, limit=65):
    """Google shows about 60 characters. Long titles lose the ' · History of Wales' (or ' · Hanes Cymru') ending first.
    One still too long is cut at its last natural break (a comma, a colon or "and") that fits, so the long reads'
    titles read whole in search results: "The Welsh Not: how they tried to wipe out our language"."""
    title = title.strip()
    for end in ENDINGS:   # in this order, so "… · The old books of Wales · History of Wales" can lose both
        if len(title) > limit and title.endswith(end):
            title = title[: -len(end)]
    if len(title) > limit + 1:
        cuts = [m.start() for m in re.finditer(r"(?:, |: | and )(?=[a-zà-ÿŵŷ’])", title) if 20 <= m.start() <= limit]  # not inside a list of names
        if cuts:
            title = title[: max(cuts)]
    return title


def tidy_desc(desc, limit=160):
    """Google shows about 155-160 characters of a description; cut at a word, not mid-word."""
    desc = re.sub(r"\s+", " ", desc or "").strip()
    if len(desc) <= limit:
        return desc
    cut = desc[: limit - 1]
    cut = cut[: cut.rfind(" ")] if " " in cut else cut
    return cut.rstrip(" ,;:–—-") + "…"


# The site's own text is shared under Creative Commons BY-NC 4.0 (see footer() in build.py); photos keep their own licences.
LICENSE = "https://creativecommons.org/licenses/by-nc/4.0/"


def website_ld(base):
    return {"@type": "WebSite", "@id": base + "#website", "name": SITE_EN, "alternateName": [SITE_CY, "historyofwales.cymru"],
            "url": base, "inLanguage": ["en-GB", "cy"],
            "description": "Welsh history from the first people to the present day, in English and Cymraeg.",
            "publisher": {"@id": base + "#org"}, "license": LICENSE}


def org_ld(base):
    return {"@type": "Organization", "@id": base + "#org", "name": SITE_EN, "alternateName": SITE_CY, "url": base,
            "logo": {"@type": "ImageObject", "url": base + "icon-512.png", "width": 512, "height": 512}}


def home_ld(base):
    return {"@context": "https://schema.org", "@graph": [website_ld(base), org_ld(base),
            {"@type": "WebPage", "@id": base + "#webpage", "url": base, "name": "History of Wales · Hanes Cymru",
             "isPartOf": {"@id": base + "#website"}, "about": {"@type": "Country", "name": "Wales", "alternateName": "Cymru",
                                                               "sameAs": "https://en.wikipedia.org/wiki/Wales"},
             "inLanguage": ["en-GB", "cy"], "primaryImageOfPage": {"@type": "ImageObject", "url": base + "og.png"}, "license": LICENSE}]}


def _crumbs(base, path, main_html, title):
    """The breadcrumb trail already shown on the page (<p class="crumbs">), as structured data."""
    m = re.search(r'<p class="crumbs">(.*?)</p>', main_html, re.S)
    items = []
    if m:
        for href, inner in re.findall(r'<a href="([^"]+)">(.*?)</a>', m.group(1), re.S):
            en = re.search(r'class="l-en[^"]*" lang="en">(.*?)</span>', inner, re.S)
            name = _strip(en.group(1) if en else inner)
            url = base if href in ("index.html", "./", "") else base + href
            if name and "#" not in href:
                items.append((name, url))
    if not items or items[0][1] != base:
        items.insert(0, (SITE_EN, base))
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", main_html, re.S)
    here = None
    if h1:
        en = re.search(r'class="l-en[^"]*" lang="en">(.*?)</span>', h1.group(1), re.S)
        here = _strip(en.group(1) if en else h1.group(1))
    here = here or (title[: -len(SUFFIX)] if title.endswith(SUFFIX) else title)
    items.append((here, base + path))
    seen, out = set(), []
    for n, u in items:
        if u not in seen:
            seen.add(u)
            out.append((n, u))
    if len(out) < 2:
        return None
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(out)]}


def first_image(base, main_html):
    """The page's main picture: the first content picture that has a description (alt text)."""
    for tag in re.findall(r"<img\b[^>]*>", main_html):
        src = re.search(r'\ssrc="([^"]+)"', tag)
        alt = re.search(r'\salt="([^"]+)"', tag)
        if src and alt and not src.group(1).startswith(("http", "data:")):
            return base + src.group(1)
    return None


def author_ld(base):
    if not AUTHOR:
        return {"@id": base + "#org"}
    return {"@type": "Person", "@id": base + "#author", "name": AUTHOR, "url": base + "about.html"}


def page_ld(base, path, title, desc, og_type, ld, main_html, card=None, published=None):
    """Structured data for one page: its own data, filled out, plus the site and the breadcrumb trail."""
    url = base + path
    title = title_for(path, title)
    if ld and "@graph" not in ld:
        main = {k: v for k, v in ld.items() if k != "@context"}
    else:
        kind = {"article": "Article", "profile": "ProfilePage", "place": "WebPage"}.get(og_type, "WebPage")
        if path in ("play.html", "gallery.html", "stories.html", "legends.html", "trails.html", "whatsnew.html"):
            kind = "CollectionPage" if kind == "WebPage" else kind
        main = {"@type": kind, ("headline" if kind == "Article" else "name"): title[: -len(SUFFIX)] if title.endswith(SUFFIX) else title}
    main.setdefault("description", desc)
    main.setdefault("url", url)
    main.setdefault("inLanguage", ["en-GB", "cy"])
    main["dateModified"] = "@@LM@@"   # build.py puts in the date the page last really changed (sitemap() below)
    if published:
        main.setdefault("datePublished", published)
    img = first_image(base, main_html) or (base + card if card else None)
    if img:
        main.setdefault("image", img)
    if main.get("@type") in ("Article",):
        main.setdefault("mainEntityOfPage", url)
        main.setdefault("author", author_ld(base))
        main.setdefault("publisher", {"@id": base + "#org"})
        main["isPartOf"] = {"@id": base + "#website"}
    elif main.get("@type") in ("WebPage", "CollectionPage", "ProfilePage", "Map", "AboutPage"):
        main["isPartOf"] = {"@id": base + "#website"}
        if AUTHOR:
            main.setdefault("author", author_ld(base))
    else:  # a Person, a Place...: say which page of ours is about them
        main.setdefault("mainEntityOfPage", url)
    if main.get("@type") in ("Article", "WebPage", "CollectionPage", "ProfilePage", "Map"):
        main.setdefault("license", LICENSE)
    graph = [main, website_ld(base), org_ld(base)]
    bc = _crumbs(base, path, main_html, title)
    if bc:
        graph.append(bc)
    return {"@context": "https://schema.org", "@graph": graph}


def ld_script(obj):
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'<script type="application/ld+json">{s}</script>'


# ---------- sitemap with real "last changed" dates ----------
def _fingerprint(doc):
    """What a reader sees: the <main> part (or the body), without the scripts. Menus and styles don't count."""
    m = re.search(r"<main\b.*?</main>", doc, re.S) or re.search(r"<body\b.*?</body>", doc, re.S)
    s = m.group(0) if m else doc
    s = re.sub(r"<script\b.*?</script>", "", s, flags=re.S)
    s = re.sub(r"<!--pi-->.*?<!--/pi-->", "", s, flags=re.S)       # the author and date lines (src/about.py)
    s = re.sub(r' <span class="new-tag">.*?</span></span>', "", s)  # "New" badges come off by themselves after two weeks
    s = re.sub(r"\?v=[0-9a-f]+", "", s)
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:16]


def _previous(base):
    """The dates from the live site, so unchanged pages keep their old date."""
    if os.environ.get("SEO_OFFLINE"):
        return {}
    # Tried three times: if it can't be read, every page would show today as its "Last updated" date.
    for wait in (0, 5, 15):
        time.sleep(wait)
        try:
            req = urllib.request.Request(base + LASTMOD_FILE, headers={"User-Agent": "historyofwales-build"})
            with urllib.request.urlopen(req, timeout=10) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception:
            continue
    print("Could not read the live " + LASTMOD_FILE + ": every page is dated today")
    return {}


def sitemap(base, pages, skip=("404.html",)):
    """Returns (sitemap.xml text, {page: [fingerprint, date it last changed]})."""
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    prev = _previous(base)
    marks, rows = {}, []
    for p, doc in pages.items():
        if p in skip or 'name="robots" content="noindex' in doc:
            continue
        fp = _fingerprint(doc)
        old = prev.get(p)
        when = old[1] if old and old[0] == fp else today
        marks[p] = [fp, when]
        imgs = []
        m = re.search(r"<main\b.*?</main>", doc, re.S)
        for tag in re.findall(r"<img\b[^>]*>", m.group(0) if m else doc):
            src = re.search(r'\ssrc="([^"]+)"', tag)
            alt = re.search(r'\salt="([^"]+)"', tag)
            if src and alt and not src.group(1).startswith(("http", "data:")):
                u = base + src.group(1)
                if u not in imgs:
                    imgs.append(u)
        loc = base + re.sub(r"(^|/)index\.html$", r"\1", p)   # the home pages are / and /cy/, as their canonical says
        img_xml = "".join(f"<image:image><image:loc>{_x(u)}</image:loc></image:image>" for u in imgs[:30])
        rows.append(f"  <url><loc>{_x(loc)}</loc><lastmod>{when}</lastmod>{img_xml}</url>\n")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "".join(rows) + "</urlset>\n")
    return xml, marks


def _x(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def robots(base):
    return f"User-agent: *\nAllow: /\nDisallow: /{LASTMOD_FILE}\n\nSitemap: {base}sitemap.xml\n"
