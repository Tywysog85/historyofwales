"""Who writes the site, when each page last changed, and how to report a mistake.

  * about.html: what the site is, who writes it, how it is written, and how to report a mistake (#corrections).
  * At the foot of every page (inside <main>): "Written by ... · First published ... · Last updated ..." and a
    "Spotted a mistake?" link that fills in the page for you.
  * At the top of every long read: "By ..." beside the reading time.

The settings below are the only things that ever need changing by hand.

"Last updated" is not typed in anywhere. The build compares what each page says with what the live site said
(src/seo.py keeps a fingerprint of every page in seo-lastmod.json) and the date moves on only when the words or
pictures on that page really change. Menus, styles, the "New" badges and this author line do not count.
"""
import urllib.parse

# ---------- settings ----------
# The name shown as the author on every page, in English and in Welsh ("By Ifan" / "Gan Ifan").
AUTHOR_EN = "Ifan"   # Ifan's choice (12 November 2026); while empty the byline says "History of Wales"
AUTHOR_CY = "Ifan"
# A line or two about the author for the About page (English, Welsh). Leave empty for none.
BIO_EN = ""
BIO_CY = ""
# How the site is researched (Ifan's words, 12 November 2026), shown under "Who writes it".
METHOD_EN = "It is researched with the help of AI and checked against real sources. These are the ones the site leans on most:"
METHOD_CY = "Caiff ei hymchwilio gyda chymorth deallusrwydd artiffisial (AI) a’i gwirio yn erbyn ffynonellau go iawn. Dyma’r rhai y mae’r wefan yn pwyso arnynt fwyaf:"
# The sources named under METHOD (Ifan asked for more of them, 13 November 2026). Only sources the site really uses.
# (heading EN, heading CY, list EN, list CY); a list may hold HTML links.
SOURCES = [
    ("The old texts of Wales", "Hen destunau Cymru",
     "Gildas, the Historia Brittonum of Nennius, the Welsh Annals (Annales Cambriae), Brut y Tywysogion and Brut y Brenhinedd, Geoffrey of Monmouth, Gerald of Wales, the Laws of Hywel Dda, the Welsh Triads, the Mabinogion, the Book of Llandaf, and the great manuscripts: the Black Book of Carmarthen, the Book of Aneirin, the Book of Taliesin, the Red Book of Hergest and the Peniarth manuscripts.",
     "Gildas, Historia Brittonum Nennius, Annales Cambriae, Brut y Tywysogion a Brut y Brenhinedd, Sieffre o Fynwy, Gerallt Gymro, Cyfraith Hywel Dda, Trioedd Ynys Prydain, y Mabinogion, Llyfr Llandaf, a’r llawysgrifau mawr: Llyfr Du Caerfyrddin, Llyfr Aneirin, Llyfr Taliesin, Llyfr Coch Hergest a llawysgrifau Peniarth."),
    ("Writers from beyond Wales", "Awduron o’r tu hwnt i Gymru",
     "Tacitus, Bede, the Anglo-Saxon Chronicle and Domesday Book.",
     "Tacitus, Beda, Cronicl yr Eingl-Sacsoniaid a Llyfr Domesday."),
    ("Libraries, museums and records", "Llyfrgelloedd, amgueddfeydd a chofnodion",
     "The Dictionary of Welsh Biography and the National Library of Wales (with Welsh Journals and Welsh Newspapers Online), Amgueddfa Cymru – Museum Wales, Cadw, Coflein and the Royal Commission on the Ancient and Historical Monuments of Wales, Heneb: the Trust for Welsh Archaeology, People’s Collection Wales, the National Trust, UNESCO, the Senedd and Hansard.",
     "Y Bywgraffiadur Cymreig a Llyfrgell Genedlaethol Cymru (gyda Chylchgronau Cymru a Phapurau Newydd Cymru Arlein), Amgueddfa Cymru, Cadw, Coflein a Chomisiwn Brenhinol Henebion Cymru, Heneb: Ymddiriedolaeth Archaeoleg Cymru, Casgliad y Werin Cymru, yr Ymddiriedolaeth Genedlaethol, UNESCO, y Senedd a Hansard."),
    ("Historians of Wales", "Haneswyr Cymru",
     "John Davies, R. R. Davies, Gwynfor Evans, Gwyn A. Williams, J. E. Lloyd, Geraint H. Jenkins, Kenneth O. Morgan, T. M. Charles-Edwards, Rachel Bromwich, Ifor Williams, Sioned Davies, Dafydd Jenkins, Thomas Jones, Alan Wilson and Baram Blackett, Adrian Gilbert, and many more on the <a href=\"books-and-authors.html\">Books and authors</a> page.",
     "John Davies, R. R. Davies, Gwynfor Evans, Gwyn A. Williams, J. E. Lloyd, Geraint H. Jenkins, Kenneth O. Morgan, T. M. Charles-Edwards, Rachel Bromwich, Ifor Williams, Sioned Davies, Dafydd Jenkins, Thomas Jones, Alan Wilson a Baram Blackett, Adrian Gilbert, a llawer mwy ar y dudalen <a href=\"books-and-authors.html\">Llyfrau ac awduron</a>."),
    ("Reference works", "Gweithiau cyfeirio",
     "Encyclopaedia Britannica, the BBC, and Wikipedia in English and in Welsh.",
     "Encyclopaedia Britannica, y BBC, a Wicipedia yn Saesneg ac yn Gymraeg."),
]
# How people report a mistake. Set ONE of these:
CORRECTIONS_EMAIL = "hello@historyofwales.cymru"  # Ifan's choice (13 November 2026): forwarded by ImprovMX to Ifan's own inbox
CORRECTIONS_FORM = ""   # or the link to an online form (used only when CORRECTIONS_EMAIL is empty)
# Corrections worth telling readers about, newest first: ("YYYY-MM-DD", page, what changed EN, what changed CY)
CORRECTIONS = []

g = {}   # build.py's helpers (bi, e, hero, section, page ...), filled in by setup()

# Markers around the author and date lines. src/seo.py leaves whatever is between them out of a page's fingerprint,
# so adding or changing them never makes every page look "updated".
OPEN, CLOSE = "<!--pi-->", "<!--/pi-->"
# Filled in by build.py once it knows when each page last changed.
LM_ISO, LM_EN, LM_CY = "@@LM@@", "@@LM_EN@@", "@@LM_CY@@"

CSS = """
.pinfo { padding-block: 2.2rem 2.6rem !important; border-top: 1px solid var(--line) }
.pinfo .wrap { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: .8rem 2rem }
.pinfo p { margin: 0; font: 500 .8rem/1.6 var(--f-mono); letter-spacing: .03em; color: var(--muted) }
.pinfo .pi-who b { color: var(--ink); font-weight: 600 }
.pinfo .pi-sep { opacity: .5; margin-inline: .45rem }
.pinfo .pi-links { display: flex; flex-wrap: wrap; gap: .5rem 1.2rem }
.pinfo a { color: var(--ink); text-decoration: underline; text-decoration-color: color-mix(in srgb, var(--red) 70%, transparent); text-underline-offset: 3px }
.pinfo a:hover { color: var(--gold) }
.about-sec h2 { margin-top: 0 }
.ab-text p { margin: 0; font-size: 1.06rem; line-height: 1.7 } .ab-text p + p { margin-top: 1rem }
.about-facts { display: grid; grid-template-columns: repeat(auto-fill, minmax(9.5rem, 1fr)); gap: .8rem; margin: 1.6rem 0 0; padding: 0; list-style: none }
.about-facts li { background: var(--slate); border: 1px solid var(--line); border-radius: 14px; padding: .9rem 1rem }
.about-facts b { display: block; font-size: 1.5rem; color: var(--gold); line-height: 1.1 }
.about-facts span { font-size: .85rem; color: var(--muted) }
.about-how { margin: 1.2rem 0 0; padding-left: 1.2rem }
.about-how li { margin: .55rem 0 }
.fix-box { background: var(--slate); border: 1px solid var(--line); border-left: 4px solid var(--red); border-radius: 14px; padding: 1.3rem 1.4rem; margin-top: 1.4rem }
.fix-box ol { margin: .6rem 0 0; padding-left: 1.2rem } .fix-box li { margin: .35rem 0 }
.fix-box .btn { margin-top: 1rem }
.fix-log { list-style: none; padding: 0; margin: 1rem 0 0 } .fix-log li { padding: .7rem 0; border-top: 1px solid var(--line) }
.fix-log time { display: block; font: 500 .78rem var(--f-mono); color: var(--muted) }
@media print { .pinfo .pi-links { display: none } }
"""


def setup(build_globals):
    g.update(build_globals)


def bi(en, cy, *a, **k):
    return g["bi"](en, cy, *a, **k)


def e(s):
    return g["e"](s)


def rbi(en, cy):
    """Like bi(), for text that already holds HTML (links, <em>): not escaped again."""
    return f'<span class="l-en" lang="en">{en}</span><span class="l-cy" lang="cy">{cy}</span>'


def author():
    """(English, Welsh) name shown as the author."""
    if AUTHOR_EN:
        return AUTHOR_EN, AUTHOR_CY or AUTHOR_EN
    return "History of Wales", "Hanes Cymru"


def mail_link():
    """The site's email address as a link (hello@...), for "get in touch" lines."""
    return f'<a href="mailto:{e(CORRECTIONS_EMAIL)}">{e(CORRECTIONS_EMAIL)}</a>'


def has_contact():
    return bool(CORRECTIONS_EMAIL or CORRECTIONS_FORM)


def report_href(path="", title=""):
    """A link that opens an email (or the form) with the page already filled in."""
    url = g["BASE_URL"] + path if path else g["BASE_URL"]
    if CORRECTIONS_EMAIL:
        subj = "Correction: " + (title or "History of Wales")
        body = f"Page: {url}\n\nWhat is wrong:\n\n\nWhere I read the right answer (a book, a source or a link), if you have one:\n\n"
        return "mailto:" + CORRECTIONS_EMAIL + "?" + urllib.parse.urlencode({"subject": subj, "body": body}, quote_via=urllib.parse.quote)
    if CORRECTIONS_FORM:
        return CORRECTIONS_FORM
    return "about.html#corrections"


def byline_top():
    """'By ...' for the top of a long read (left out of the page's fingerprint)."""
    en, cy = author()
    return (f'{OPEN}<span>{bi("By " + en, "Gan " + cy)}</span>'
            f'<span>{bi("Updated", "Diweddarwyd")} <time datetime="{LM_ISO}">{bi(LM_EN, LM_CY)}</time></span>{CLOSE}')


def page_info(path, title, first=None):
    """The author, dates and 'Spotted a mistake?' strip at the foot of a page. first: ISO date first published, or None."""
    en, cy = author()
    t = title.replace(" · History of Wales", "")
    sep = '<span class="pi-sep" aria-hidden="true">·</span>'
    who = f'{bi("Written by", "Ysgrifennwyd gan")} <b>{bi(en, cy)}</b>'
    pub = ""
    if first:
        pub = sep + bi("First published", "Cyhoeddwyd gyntaf") + f' <time datetime="{first}">{bi(g["_news_date"](first), g["_news_date"](first, True))}</time>'
    upd = sep + bi("Last updated", "Diweddarwyd ddiwethaf") + f' <time datetime="{LM_ISO}">{bi(LM_EN, LM_CY)}</time>'
    links = ((f'<a href="{e(report_href(path, t))}" rel="nofollow">{bi("Spotted a mistake? Tell us", "Wedi gweld camgymeriad? Rhowch wybod")}</a>' if has_contact() else "")
             + f'<a href="about.html">{bi("About this site", "Am y wefan hon")}</a>')
    if path == "about.html":
        links = ""
    return (f'{OPEN}<section class="pinfo"><div class="wrap"><p class="pi-who">{who}{pub}{upd}</p>'
            f'<p class="pi-links">{links}</p></div></section>{CLOSE}')


def fill_dates(doc, iso):
    """Put the page's real 'last updated' date in place of the markers."""
    nd = g["_news_date"]
    return doc.replace(LM_ISO, iso).replace(LM_EN, nd(iso)).replace(LM_CY, nd(iso, True))


# ---------- the About page ----------
def about_page():
    D, F = g["D"], g["F"]
    en, cy = author()
    site = g["SITE"]
    facts = [(f"{len(D.EVENTS):,}", "events on the timeline", "o ddigwyddiadau ar y llinell amser"),
             (f"{len(D.PEOPLE):,}", "people", "o bobl"), (f"{len(D.PLACES):,}", "historic places", "o leoedd hanesyddol"),
             (f"{len(F.STORIES):,}", "long reads", "o erthyglau"), (f"{len(F.LEGENDS):,}", "legends", "o chwedlau"),
             ("2", "languages, every page", "iaith, ar bob tudalen")]
    facts_html = '<ul class="about-facts">' + "".join(f'<li><b>{n}</b><span>{bi(a, b)}</span></li>' for n, a, b in facts) + "</ul>"

    what = g["paras"](
        ["History of Wales (Hanes Cymru) tells the story of Wales from the first people living in caves 230,000 years ago, to the present day. It is written in both English and in Cymraeg.",
         "It is written for anyone who wants to know the history of Wales. The site is free to read and carries no adverts."],
        ["Mae Hanes Cymru yn adrodd stori Cymru o’r bobl gyntaf a fu’n byw mewn ogofâu 230,000 o flynyddoedd yn ôl, hyd heddiw. Mae wedi’i hysgrifennu yn Gymraeg ac yn Saesneg.",
         "Fe’i hysgrifennwyd ar gyfer unrhyw un sydd am wybod hanes Cymru. Mae’r wefan am ddim i’w darllen ac nid oes hysbysebion arni."], "ab-text")

    who_en = [f"History of Wales is written and looked after by {en}."] if AUTHOR_EN else ["History of Wales is written and looked after by one person, for love of Wales."]
    who_cy = [f"{cy} sy’n ysgrifennu ac yn gofalu am Hanes Cymru."] if AUTHOR_EN else ["Un person sy’n ysgrifennu ac yn gofalu am Hanes Cymru, o gariad at Gymru."]
    if BIO_EN:
        who_en.append(BIO_EN)
        who_cy.append(BIO_CY or BIO_EN)
    if METHOD_EN:
        who_en.append(METHOD_EN)
        who_cy.append(METHOD_CY or METHOD_EN)
    who = g["paras"](who_en, who_cy, "ab-text")
    if SOURCES:
        who += ('<ul class="about-how about-src">' + "".join(
            f"<li>{rbi(f'<b>{e(he)}:</b> {le}', f'<b>{e(hc)}:</b> {lc}')}</li>" for he, hc, le, lc in SOURCES) + "</ul>")
    if CORRECTIONS_EMAIL:
        mail = mail_link()
        who += (f'<div class="ab-text" style="margin-top:1rem"><p>' + rbi(f"To get in touch about anything, email {mail}. Every message is read.",
                f"I gysylltu am unrhyw beth, anfonwch e-bost at {mail}. Caiff pob neges ei darllen.") + "</p></div>")

    how = [("Every page is built on published sources: the Welsh chronicles (Brut y Tywysogion and the Welsh Annals), the Dictionary of Welsh Biography, Coflein and Cadw for places and monuments, and the standard histories of Wales. Many pages end with <em>Read further</em> links to these, so you can check for yourself.",
            "Mae pob tudalen wedi’i seilio ar ffynonellau cyhoeddedig: cronicl Cymru (Brut y Tywysogion ac Annales Cambriae), y Bywgraffiadur Cymreig, Coflein a Cadw ar gyfer lleoedd a henebion, a’r prif lyfrau ar hanes Cymru. Mae llawer o dudalennau’n gorffen â dolenni <em>Darllen ymhellach</em> i’r rhain, er mwyn i chi wirio drosoch eich hun."),
           ("Where Welsh tradition tells us something that the written record cannot prove, we say so plainly: “Welsh tradition holds…”. Those traditions are part of the history of Wales, and we give them their place.",
            "Lle mae traddodiad Cymru yn dweud rhywbeth na all y cofnod ysgrifenedig ei brofi, rydym yn dweud hynny’n blaen: “Yn ôl traddodiad Cymru…”. Mae’r traddodiadau hynny’n rhan o hanes Cymru, ac rydym yn rhoi eu lle iddynt."),
           ("Dates marked c. (circa) are approximate. The early chronicles do not always agree; where they differ, we give the date most historians use.",
            "Dyddiadau bras yw’r rhai a nodir c. (circa). Nid yw’r hen gronicl bob amser yn cytuno; lle maent yn wahanol, rydym yn rhoi’r dyddiad y mae’r rhan fwyaf o haneswyr yn ei ddefnyddio."),
           ("Photographs come from Wikimedia Commons and are credited, with their licences, on the page where they appear.",
            "Daw’r ffotograffau o Wikimedia Commons, a rhoddir cydnabyddiaeth iddynt, gyda’u trwyddedau, ar y dudalen lle maent yn ymddangos."),
           ("Every page shows the date it was last updated. That date moves on only when the words or pictures on the page change.",
            "Mae pob tudalen yn dangos y dyddiad y’i diweddarwyd ddiwethaf. Dim ond pan fydd y geiriau neu’r lluniau ar y dudalen yn newid y bydd y dyddiad hwnnw’n symud.")]
    how_html = '<ul class="about-how">' + "".join(f"<li>{rbi(a, b)}</li>" for a, b in how) + "</ul>"

    if CORRECTIONS_EMAIL:
        tell_en = f'Email <a href="{e(report_href())}">{e(CORRECTIONS_EMAIL)}</a>. Every page also has a <em>Spotted a mistake?</em> link at the bottom that starts the email for you, with the page already filled in.'
        tell_cy = f'Anfonwch e-bost at <a href="{e(report_href())}">{e(CORRECTIONS_EMAIL)}</a>. Mae dolen <em>Wedi gweld camgymeriad?</em> ar waelod pob tudalen hefyd, sy’n dechrau’r e-bost i chi, gyda’r dudalen wedi’i llenwi’n barod.'
        btn = f'<a class="btn solid" href="{e(report_href())}">{bi("Report a mistake", "Rhoi gwybod am gamgymeriad")}</a>'
    elif CORRECTIONS_FORM:
        tell_en = "Fill in the short form. Every page also has a <em>Spotted a mistake?</em> link at the bottom that takes you to it."
        tell_cy = "Llenwch y ffurflen fer. Mae dolen <em>Wedi gweld camgymeriad?</em> ar waelod pob tudalen hefyd sy’n mynd â chi ati."
        btn = f'<a class="btn solid" href="{e(CORRECTIONS_FORM)}" target="_blank" rel="noopener">{bi("Report a mistake", "Rhoi gwybod am gamgymeriad")}</a>'
    else:
        tell_en, tell_cy, btn = "A short form for reporting mistakes will be here very soon.", "Bydd ffurflen fer i roi gwybod am gamgymeriadau yma cyn bo hir.", ""
    fix = (f'<div class="ab-text"><p>{bi("We want every page to be right. If you find a mistake, a wrong date, a misspelt Welsh name or a link that no longer works, please tell us.", "Rydym am i bob tudalen fod yn gywir. Os dewch o hyd i gamgymeriad, dyddiad anghywir, enw Cymraeg wedi’i gamsillafu neu ddolen nad yw’n gweithio mwyach, rhowch wybod i ni.")}</p></div>'
           f'<div class="fix-box"><p><b>{bi("How to tell us", "Sut i roi gwybod")}</b></p><p>{rbi(tell_en, tell_cy)}</p>'
           f'<p style="margin-top:.8rem">{bi("It helps if you can tell us:", "Mae’n help os gallwch ddweud wrthym:")}</p><ol>'
           f'<li>{bi("which page (its address, or its title)", "pa dudalen (ei chyfeiriad, neu ei theitl)")}</li>'
           f'<li>{bi("what is wrong", "beth sy’n anghywir")}</li>'
           f'<li>{bi("where you read the right answer: a book, a source or a link, if you have one", "ble y darllenoch yr ateb cywir: llyfr, ffynhonnell neu ddolen, os oes gennych un")}</li></ol>{btn}</div>'
           f'<div class="ab-text" style="margin-top:1.4rem"><p><b>{bi("What happens next", "Beth sy’n digwydd wedyn")}</b></p>'
           f'<p>{bi("We read every message, check it against the sources and put the page right. When a fix goes up, the page’s “Last updated” date changes. Bigger corrections are listed on this page.", "Rydym yn darllen pob neges, yn ei gwirio yn erbyn y ffynonellau ac yn cywiro’r dudalen. Pan fydd cywiriad yn mynd i fyny, mae dyddiad “Diweddarwyd ddiwethaf” y dudalen yn newid. Rhestrir cywiriadau mwy ar y dudalen hon.")}</p></div>')
    if CORRECTIONS:
        fix += (f'<p class="eyebrow" style="margin-top:1.6rem">{bi("Corrections made", "Cywiriadau a wnaed")}</p><ul class="fix-log">'
                + "".join(f'<li><time datetime="{d}">{bi(g["_news_date"](d), g["_news_date"](d, True))}</time><a href="{p}">{bi(a, b)}</a></li>' for d, p, a, b in CORRECTIONS) + "</ul>")

    privacy = g["paras"](
        ["We count visits with GoatCounter, which uses no cookies and does not track you from site to site. Your progress in the games and your journey through the site are kept only on your own device."],
        ["Rydym yn cyfrif ymweliadau â GoatCounter, nad yw’n defnyddio cwcis nac yn eich dilyn o wefan i wefan. Dim ond ar eich dyfais eich hun y cedwir eich cynnydd yn y gemau a’ch taith drwy’r wefan."], "ab-text")

    def sec(sid, en_h, cy_h, inner, top=False):
        return (f'<section id="{sid}" class="about-sec{"" if top else " tight"}"><div class="wrap narrow">'
                f'<h2 class="sub-h">{bi(en_h, cy_h)}</h2>{inner}</div></section>')

    main = (g["hero"]("today", f'<a href="index.html">{site}</a>', "book", "About", "Amdanom", "About this site", "Am y wefan hon",
                      "Who writes History of Wales, how it is put together, and how to tell us if we have got something wrong.",
                      "Pwy sy’n ysgrifennu Hanes Cymru, sut y caiff ei llunio, a sut i ddweud wrthym os ydym wedi gwneud camgymeriad.", art="book")
            + sec("what", "What this site is", "Beth yw’r wefan hon", what + facts_html, top=True)
            + sec("who", "Who writes it", "Pwy sy’n ei hysgrifennu", who)
            + sec("how", "How it is written", "Sut y caiff ei hysgrifennu", how_html)
            + sec("corrections", "Spotted a mistake?", "Wedi gweld camgymeriad?", fix)
            + sec("privacy", "Your privacy", "Eich preifatrwydd", privacy))
    ld = {"@context": "https://schema.org", "@type": "AboutPage", "name": "About History of Wales", "inLanguage": ["en", "cy"],
          "description": "Who writes History of Wales, how it is written, and how to report a mistake."}
    return g["page"]("about.html", "About this site · History of Wales",
                     "Who writes History of Wales (Hanes Cymru), how the site is written and checked, and how to report a mistake.",
                     main, era="today", og_type="website", ld=ld, active="about.html")
