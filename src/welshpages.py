"""Welsh pages with their own addresses: every page also goes up in Welsh at cy/<page>.html.

Until November 2026 each page held both languages and a button swapped them, so search engines saw one mixed page with an
English title. Now build.py hands every finished page to split(), which makes two:

- the English page (<page>.html): the Welsh copies of the words are taken out, the title stays English;
- the Welsh page (cy/<page>.html): the English copies are taken out, and it gets a Welsh <title> and description
  (from its own heading and opening line), lang="cy", og:locale cy_GB, and its own canonical address.

Both carry hreflang links to each other (x-default is English), so Google shows Welsh searchers the Welsh page.
Text marked with bi() (class l-en / l-cy) is what gets taken out; text a script writes later still follows the page's language.

The Welsh pages sit one folder down. <base href="../"> keeps every picture, script and style pointing at the one shared
copy; links between pages are rewritten to stay in cy/, and a small script does the same for links that scripts make.
The EN / CY switch is a pair of links to the other page, so each language has an address that can be shared and opens
in that language for anyone. The reader's choice is remembered, but only ever offered, never forced (see HOME_PREF).
"""
import html as _html
import re

SKIP = {"404.html"}  # pages with no Welsh twin (the Google check file is not built here)
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
_RAW = re.compile(r"<(script|style|textarea|template)\b.*?</\1\s*>", re.S | re.I)
_TAG = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9-]*)\b([^>]*?)(/?)>", re.S)


def _strip_lang(doc, drop):
    """Remove every element whose class list holds `drop` ("l-en" or "l-cy"), with all it contains."""
    keep, pos = [], 0
    raws = [(m.start(), m.end()) for m in _RAW.finditer(doc)]
    ri = 0
    want = re.compile(r'\bclass="(?:[^"]*\s)?' + drop + r'(?:\s[^"]*)?"')
    i = 0
    while True:
        m = _TAG.search(doc, i)
        if not m:
            break
        # jump over script, style and textarea bodies
        while ri < len(raws) and raws[ri][1] <= m.start():
            ri += 1
        if ri < len(raws) and raws[ri][0] <= m.start() < raws[ri][1]:
            i = raws[ri][1]
            continue
        close, name, attrs, selfc = m.group(1), m.group(2).lower(), m.group(3), m.group(4)
        if close or not want.search(attrs):
            i = m.end()
            continue
        # found an element to drop: find where it ends
        if selfc or name in VOID:
            end = m.end()
        else:
            depth, j, end = 1, m.end(), None
            same = re.compile(r"<(/?)" + re.escape(name) + r"\b[^>]*?(/?)>", re.I)
            while depth:
                n = same.search(doc, j)
                if not n:
                    end = len(doc)
                    break
                if n.group(1):
                    depth -= 1
                elif not n.group(2):
                    depth += 1
                j = n.end()
            end = end if end is not None else j
        keep.append(doc[pos:m.start()])
        pos = i = end
    keep.append(doc[pos:])
    return "".join(keep)


def _text(fragment):
    t = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", _html.unescape(t)).strip()


def _first(doc, pattern):
    m = re.search(pattern, doc, re.S)
    return _text(m.group(1)) if m else ""


# A reader's remembered language ("hc-lang") is saved only when they press EN or CY (or the "read this in…" link), never just
# by opening a page. It never overrides an address: an English link opens in English and a cy/ link opens in Cymraeg, for
# everyone. The one exception is the bare home page (typing historyofwales.cymru), which takes a reader who chose Cymraeg
# to cy/, unless they came from another page of the site. On any other page a small bar offers the page in their language.
_STORED_OLD = 'try{if(localStorage.getItem("hc-lang")==="cy"){h.classList.add("cy");h.lang="cy"}}catch(e){}'
HOME_PREF = ('<script>(function(){try{var r=document.referrer;if(localStorage.getItem("hc-lang")==="cy"&&!(r&&r.indexOf(location.origin+"/")===0))'
             'location.replace(location.pathname.replace(/\\/(index\\.html)?$/,"/cy/")+location.search+location.hash)}catch(e){}})()</script>')
CY_HEAD = ('<base href="../">\n<script>(function(){var P=location.pathname,S=location.search,H=history,rs=H.replaceState,ps=H.pushState;'
           'function fx(u){return typeof u==="string"&&u.charAt(0)==="#"?P+S+u:u}'
           'H.replaceState=function(s,t,u){return rs.call(H,s,t,fx(u))};H.pushState=function(s,t,u){return ps.call(H,s,t,fx(u))};'
           'document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest("a[href]");if(!a||a.hasAttribute("hreflang"))return;var h=a.getAttribute("href")||"";'
           'if(h.charAt(0)==="#"){a.setAttribute("href",P+S+h);return}'
           'if(/^[^:\\/?#]+\\.html([?#].*)?$/.test(h))a.setAttribute("href","cy/"+h)},true)})()</script>\n')

# EN / CY are real links to the other page's address (so they can be copied, opened in a new tab and followed by search
# engines). Pressing one remembers the choice and keeps the reader's place (#…) on the other page.
SWITCH_BUTTONS = ('<button type="button" id="lang-en" aria-pressed="true">EN</button>'
                  '<button type="button" id="lang-cy" aria-pressed="false">CY</button>')


def _switch(en_href, cy_href, here):
    def one(code, label, href, lang, title):
        cur = ' aria-current="true"' if code == here else ""
        return (f'<a id="lang-{code}" href="{href}" hreflang="{lang}" lang="{lang}" data-lang="{code}" title="{title}"{cur}>{label}</a>')
    return one("en", "EN", en_href, "en", "Read this page in English") + one("cy", "CY", cy_href, "cy", "Darllen y dudalen hon yn Gymraeg")


SWITCH_JS = ('<script>(function(){var d=document,here=d.documentElement.lang==="cy"?"cy":"en",want=null;'
             'try{want=localStorage.getItem("hc-lang")}catch(e){}'
             'd.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest("a[data-lang]");if(!a)return;'
             'try{localStorage.setItem("hc-lang",a.dataset.lang)}catch(x){}'
             'if(a.dataset.lang!==here&&location.hash&&a.getAttribute("href").indexOf("#")<0)a.setAttribute("href",a.getAttribute("href")+location.hash)});'
             'var o=d.getElementById("lang-"+want);'
             'if(!o||want===here)return;try{if(sessionStorage.getItem("hc-hint"))return}catch(e){}'
             'var cy=want==="cy",b=d.createElement("div");b.className="lang-hint no-print";b.lang=want;'
             'b.innerHTML=\'<div class="wrap"><span>\'+(cy?"Mae’r dudalen hon ar gael yn Gymraeg.":"This page is also in English.")+\'</span>\''
             '+\'<a data-lang="\'+want+\'" hreflang="\'+want+\'" href="\'+o.getAttribute("href")+\'">\'+(cy?"Darllen yn Gymraeg":"Read it in English")+\' →</a>\''
             '+\'<button type="button" aria-label="\'+(cy?"Cau":"Close")+\'">×</button></div>\';'
             'b.querySelector("button").onclick=function(){b.remove();try{sessionStorage.setItem("hc-hint","1")}catch(e){}};'
             'var m=d.getElementById("main")||d.querySelector("main");if(m)m.parentNode.insertBefore(b,m)})()</script>')

def _with_switch_js(doc):
    """The home, timeline, people and map pages are built without LANG_JS: give them the switch script too."""
    if SWITCH_JS in doc:
        return doc
    i = doc.rfind("</body>")
    return doc[:i] + SWITCH_JS + "\n" + doc[i:] if i >= 0 else doc + SWITCH_JS


_LINK = re.compile(r'(\shref=")([^"]*)(")')


def _cy_links(doc, name):
    def fix(m):
        h = m.group(2)
        if h.startswith("#"):
            return m.group(1) + "cy/" + name + h + m.group(3)
        if re.match(r"^[^:/?#]+\.html([?#].*)?$", h):
            return m.group(1) + "cy/" + h + m.group(3)
        return m.group(0)
    # only rewrite links outside scripts (scripts are handled by the click helper)
    out, pos = [], 0
    for r in _RAW.finditer(doc):
        out.append(_LINK.sub(fix, doc[pos:r.start()]))
        out.append(doc[r.start():r.end()])
        pos = r.end()
    out.append(_LINK.sub(fix, doc[pos:]))
    return "".join(out)


def _swap_data_cy(doc):
    """Elements whose words a script swaps (data-cy="…") start out in Welsh on the Welsh page."""
    return re.sub(r'<([a-zA-Z0-9]+)(\s(?:[^<>]*?\s)?data-cy="([^"]*)"[^<>]*)>([^<]*)</\1>',
                  lambda m: f"<{m.group(1)}{m.group(2)}>{m.group(3)}</{m.group(1)}>", doc)


def split(pages, base_url, lang_boot, lang_js, tidy_title, tidy_desc):
    """Return the pages with Welsh twins added under cy/. `pages` maps file name to finished HTML."""
    out = {}
    boot = lang_boot.replace(_STORED_OLD, "")
    assert boot != lang_boot, "LANG_BOOT changed: update _STORED_OLD in welshpages.py"
    boot_en, boot_cy = boot, boot.replace('h.classList.add("js");', 'h.classList.add("js","cy");h.lang="cy";')
    for name, doc in pages.items():
        if name in SKIP or "/" in name or not doc.lstrip().lower().startswith("<!doctype html"):
            out[name] = doc
            continue
        en_url, cy_url = base_url + name, base_url + "cy/" + name
        if name == "index.html":
            en_url, cy_url = base_url, base_url + "cy/"
        # the switch's links: on the English page they are relative to it; the Welsh page has <base href="../">
        en_href = cy_href = en_href_from_cy = name if name != "index.html" else "./"
        cy_href_from_en = cy_href = "cy/" + (name if name != "index.html" else "")
        alt = (f'<link rel="alternate" hreflang="en" href="{en_url}">\n<link rel="alternate" hreflang="cy" href="{cy_url}">\n'
               f'<link rel="alternate" hreflang="x-default" href="{en_url}">\n')

        # English
        en = _strip_lang(doc, "l-cy")
        en = re.sub(r'(<link rel="canonical" href="[^"]*">\n)', lambda m: m.group(1) + alt, en, count=1)
        en = en.replace(lang_boot, boot_en + (HOME_PREF if name == "index.html" else ""), 1).replace(lang_js, SWITCH_JS, 1)
        en = _with_switch_js(en.replace(SWITCH_BUTTONS, _switch(en_href, cy_href_from_en, "en"), 1))
        en = en.replace('<meta property="og:locale:alternate" content="cy_GB">\n', "", 1)
        out[name] = en

        # Cymraeg
        cy = _strip_lang(doc, "l-en")
        cy = _swap_data_cy(cy)
        h1 = _first(cy, r"<h1\b[^>]*>(.*?)</h1>")
        lede = _first(cy, r'<p class="lede"[^>]*>(.*?)</p>') or _first(cy, r'<main id="main">.*?<p\b[^>]*>(.{80,}?)</p>')
        en_title = _first(doc, r"<title>(.*?)</title>")
        if name == "index.html" or not h1:
            title = en_title.replace("History of Wales", "Hanes Cymru") if name != "index.html" else "Hanes Cymru: hanes Cymru o’r dechrau hyd heddiw"
        else:
            title = h1 if "Hanes Cymru" in h1 else f"{h1} · Hanes Cymru"
        title = tidy_title(title)
        desc = tidy_desc(lede) if lede else None
        if name == "index.html":
            desc = ("Hanes Cymru o’r bobl gyntaf hyd y Senedd: brenhinoedd, tywysogion, cestyll, seintiau a beirdd, "
                    "gyda llinell amser, map a gemau. Yn Gymraeg ac yn Saesneg.")  # under 160 characters, so Google shows it all
        cy = re.sub(r"<html lang=\"en\"([^>]*)>", lambda m: '<html lang="cy" class="cy"' + m.group(1) + ">", cy, count=1)
        cy = re.sub(r"<title>.*?</title>", lambda m: f"<title>{_html.escape(title, quote=False)}</title>", cy, count=1, flags=re.S)
        cy = re.sub(r'<meta property="og:title" content="[^"]*">', lambda m: f'<meta property="og:title" content="{_html.escape(title)}">', cy, count=1)
        if desc:
            cy = re.sub(r'<meta name="description" content="[^"]*">', lambda m: f'<meta name="description" content="{_html.escape(desc)}">', cy, count=1)
            cy = re.sub(r'<meta property="og:description" content="[^"]*">', lambda m: f'<meta property="og:description" content="{_html.escape(desc)}">', cy, count=1)
        cy = cy.replace('<meta property="og:locale" content="en_GB">\n<meta property="og:locale:alternate" content="cy_GB">',
                        '<meta property="og:locale" content="cy_GB">', 1)
        cy = cy.replace(f'<meta property="og:url" content="{en_url}">', f'<meta property="og:url" content="{cy_url}">', 1)
        cy = cy.replace(f'"{base_url}{name}"', f'"{cy_url}"').replace('"inLanguage":["en","cy"]', '"inLanguage":"cy"').replace('"inLanguage": ["en", "cy"]', '"inLanguage": "cy"')
        cy = cy.replace(lang_boot, boot_cy, 1).replace(lang_js, SWITCH_JS, 1)
        cy = re.sub(r'<link rel="canonical" href="[^"]*">\n', lambda m: f'<link rel="canonical" href="{cy_url}">\n' + alt, cy, count=1)
        cy = re.sub(r'<meta property="og:image:alt" content="[^"]*">', lambda m: f'<meta property="og:image:alt" content="{_html.escape(title)}">', cy, count=1)
        if name == "index.html":  # the home page's own entry in the structured data (the site-wide entries stay as they are)
            cy = cy.replace(f'"@id":"{base_url}#webpage","url":"{base_url}","name":"History of Wales · Hanes Cymru"',
                            f'"@id":"{cy_url}#webpage","url":"{cy_url}","name":"Hanes Cymru · History of Wales"', 1)
            cy = cy.replace('"inLanguage":["en-GB","cy"],"primaryImageOfPage"', '"inLanguage":"cy","primaryImageOfPage"', 1)
            cy = cy.replace('aria-label="Cymru: the history of Wales"><em class="sr-only">The history of Wales: </em>', 'aria-label="Cymru: hanes Cymru"><em class="sr-only">Hanes Cymru: </em>', 1)
        cy = _cy_links(cy, name)
        cy = _with_switch_js(cy.replace(SWITCH_BUTTONS, _switch(en_href_from_cy, cy_href, "cy"), 1))  # after _cy_links, so EN stays English
        cy = cy.replace("<head>\n", "<head>\n" + CY_HEAD, 1)
        out["cy/" + name] = cy
    return out
