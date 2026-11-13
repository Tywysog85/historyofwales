"""The old books of Wales: one page for every great book (book-<id>.html), and books.html as their hub.
Ifan asked (2026-11-12) for "all the other old books": every great Welsh manuscript and early printed book with a page of its own.

The cards on books.html are src/literature.py BOOK_GROUPS; NEW_GROUP below adds three more treasures. The full texts are in
src/oldbooks_a.py (oldest Welsh and the Four Ancient Books), src/oldbooks_b.py (the other great books and the new three) and
src/oldbooks_c.py (the first printed books). build.py's book_page() lays each page out; pictures for the top of each page are
in src/pictures.py, and the reading lists (REFS, keyed by page name) join src/refs2.py PAGES.
"""
import oldbooks_a as _A
import oldbooks_b as _B
import oldbooks_c as _C

PAGES = {**_A.PAGES, **_B.PAGES, **_C.PAGES}

_P, _B_, _W = "p", "b", "w"
CC0 = ("CC0", "https://creativecommons.org/publicdomain/zero/1.0/")
BY4 = ("CC BY 4.0", "https://creativecommons.org/licenses/by/4.0/")
BYSA4 = ("CC BY-SA 4.0", "https://creativecommons.org/licenses/by-sa/4.0")
PD = ("Public domain", "https://creativecommons.org/publicdomain/mark/1.0/")

# Pictures inside the pages ("!! key"), as (Commons file, maker, licence, licence link, caption EN, caption CY, width, height)
FIGS = {
    "annals": ("Catgualart fili' catguolaum obiit.png", "Medieval scribe; British Library, Harley MS 3859", *PD,
               "The Annals of Wales in Harley 3859: ‘a great mortality in Britain, in which Cadwaladr son of Cadwallon died’",
               "Anodau Cymru yn Harley 3859: ‘marwolaeth fawr ym Mhrydain, pan fu farw Cadwaladr fab Cadwallon’", 914, 640),
    "dormarch": ("Dormarch in the Black Book of Carmarthen (f. 49 r.).png", "Medieval scribe; National Library of Wales, Peniarth MS 1", *BYSA4,
                 "A scribe’s drawing of the hound Dormarch in the margin of the Black Book", "Llun copïydd o’r ci Dormarch yn ymyl y Llyfr Du", 772, 509),
    "redbook": ("Jesus-College-MS-111 00115 58r (cropped) Brut y Tywysogion.jpg", "Hywel Fychan ap Hywel Goch and others; Jesus College, Oxford", *BY4,
                "A page of the Red Book of Hergest, with the beginning of the chronicle of the princes", "Tudalen o Lyfr Coch Hergest, gyda dechrau cronicl y tywysogion", 743, 791),
    "hywel": ("Hywel vab Ewein, NLW MS 6680B f. 124r.png", "Medieval scribe; National Library of Wales", *PD,
              "‘Hywel vab Ewein’: the name of the poet-prince Hywel ab Owain Gwynedd in red, above one of his poems", "‘Hywel vab Ewein’: enw’r tywysog-fardd Hywel ab Owain Gwynedd mewn coch, uwchben un o’i gerddi", 1280, 168),
    "distain": ("Distain, Peniarth MS 28 f. 3v.png", "Medieval scribe; National Library of Wales, Peniarth MS 28", *PD,
                "The steward of the king’s court, drawn in Peniarth 28", "Distain llys y brenin, wedi’i dynnu yn Peniarth 28", 389, 642),
    "p20": ("Chronical of the Princes (f.260).jpg", "Medieval scribe; National Library of Wales, Peniarth MS 20", *CC0,
            "A page of Brut y Tywysogion in Peniarth 20", "Tudalen o Frut y Tywysogion yn Peniarth 20", 635, 855),
    "cadwallon": ("Cadwallon_ap_Cadfan_Peniarth_MS_23C_(f.99.v)_transparency.png", "Medieval scribe; National Library of Wales, Peniarth MS 23C", *PD,
                  "King Cadwallon, drawn in the margin of a Welsh Brut, Peniarth 23", "Y Brenin Cadwallon, wedi’i dynnu yn ymyl Brut Cymraeg, Peniarth 23", 523, 477),
    "ancr": ("Jesus-College-MS-119 00007 2r.jpg", "Jesus College, Oxford; photograph by the Bodleian Libraries", *BY4,
             "Notes at the front of the Book of the Anchorite, among them the record that it was written for Gruffudd ap Llywelyn of Cantref Mawr in 1346",
             "Nodiadau ar ddechrau Llyfr Ancr, yn eu plith y cofnod iddo gael ei ysgrifennu i Ruffudd ap Llywelyn o’r Cantref Mawr yn 1346", 2320, 3072),
    "basing": ("Llyfr du Basing (4401103).jpg", "Gutun Owain and an earlier scribe; National Library of Wales", *CC0,
               "A page of the Black Book of Basingwerk, with its painted initial", "Tudalen o Lyfr Du Basing, gyda’i lythyren addurnedig", 3121, 4040),
    "peniarth": ("Peniarth, Merionethshire 06.jpeg", "Thomas Nicholls", *PD,
                 "Peniarth, near Tywyn, the house that gave its name to the greatest collection of Welsh manuscripts", "Peniarth, ger Tywyn, y tŷ a roddodd ei enw i’r casgliad mwyaf o lawysgrifau Cymraeg", 594, 408),
}

# Three more treasures, shown on books.html after "The other great books"
NEW_GROUP = dict(id="more", en="More treasures of the manuscripts", cy="Rhagor o drysorau’r llawysgrifau", books=[
  dict(id="llyfr-ancr", en="The Book of the Anchorite", cy="Llyfr Ancr Llanddewibrefi", date="1346", dateCy="1346", whereEn="Jesus College, Oxford (MS 119)", whereCy="Coleg Iesu, Rhydychen (MS 119)",
   pic=FIGS["ancr"],
   en_t="Written in 1346 by a hermit who lived in a cell beside the church of Llanddewibrefi, for a nobleman of Cantref Mawr. It is a library of the faith in Welsh: a book of questions and answers about God and the world, the Food of the Soul, the Vision of Saint Paul and the story of the land of Prester John.",
   cy_t="Ysgrifennwyd yn 1346 gan feudwy a drigai mewn cell wrth eglwys Llanddewibrefi, i uchelwr o’r Cantref Mawr. Llyfrgell o’r ffydd yn Gymraeg ydyw: llyfr o gwestiynau ac atebion am Dduw a’r byd, Ymborth yr Enaid, Breuddwyd Pawl a stori gwlad y Preutur Siôn."),
  dict(id="basingwerk", en="The Black Book of Basingwerk", cy="Llyfr Du Basing", date="15th century", dateCy="y bymthegfed ganrif", whereEn="National Library of Wales (NLW MS 7006D)", whereCy="Llyfrgell Genedlaethol Cymru (LlGC 7006D)",
   pic=FIGS["basing"],
   en_t="The history of the Welsh from the fall of Troy to 1461 in one beautiful book, much of it in the hand of the poet Gutun Owain of Valle Crucis, with letters of gold. It was kept at the abbey of Basingwerk, near Holywell, and still has its medieval wooden boards.",
   cy_t="Hanes y Cymry o gwymp Caerdroea hyd 1461 mewn un llyfr hardd, llawer ohono yn llaw’r bardd Gutun Owain o Lyn y Groes, gyda llythrennau aur. Fe’i cadwyd yn abaty Dinas Basing, ger Treffynnon, ac mae ganddo o hyd ei gloriau pren canoloesol.",
   link=("person-gutun-owain.html", "Gutun Owain", "Gutun Owain")),
  dict(id="peniarth", en="The Peniarth manuscripts", cy="Llawysgrifau Peniarth", date="gathered 17th century", dateCy="casglwyd yn yr 17eg ganrif", whereEn="National Library of Wales", whereCy="Llyfrgell Genedlaethol Cymru",
   pic=FIGS["peniarth"],
   en_t="The greatest collection of Welsh manuscripts ever made, gathered by Robert Vaughan of Hengwrt in the seventeenth century and kept at Peniarth, near Tywyn. Its numbers are the names of the treasures: Peniarth 1 is the Black Book, Peniarth 2 the Book of Taliesin, Peniarth 20 the chronicle of the princes.",
   cy_t="Y casgliad mwyaf o lawysgrifau Cymraeg a wnaed erioed, a gasglwyd gan Robert Vaughan o’r Hengwrt yn yr ail ganrif ar bymtheg ac a gadwyd ym Mheniarth, ger Tywyn. Ei rifau yw enwau’r trysorau: Peniarth 1 yw’r Llyfr Du, Peniarth 2 Llyfr Taliesin, Peniarth 20 cronicl y tywysogion.",
   link=("place-library.html", "The National Library of Wales", "Llyfrgell Genedlaethol Cymru")),
])

INTRO_EN = "Every one of these books has a page of its own: tap a book’s name to read its whole story, where it was made, what it keeps and how it came down to us."
INTRO_CY = "Mae gan bob un o’r llyfrau hyn dudalen ei hun: tapiwch enw llyfr i ddarllen ei stori gyfan, ble y’i gwnaed, beth mae’n ei gadw a sut y daeth i lawr atom."

_NLW_MS = "https://www.library.wales/discover/digital-gallery/manuscripts/the-middle-ages/"
CITES = {
    "nlw-black": dict(short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"), t="The Black Book of Carmarthen",
        by=("National Library of Wales, which keeps the manuscript (Peniarth MS 1)", "Llyfrgell Genedlaethol Cymru, sy’n cadw’r llawysgrif (Peniarth 1)"),
        note=("Written by one scribe “at different periods of his life before and about the year 1250”; found by Sir John Price with the treasurer of St Davids; at Hengwrt, then Peniarth; bought by Sir John Williams in 1904 for £5,500.",
              "Ysgrifennwyd gan un copïydd ar wahanol adegau yn ei fywyd, cyn tua 1250 ac o’i gwmpas; cafwyd gan Syr John Prys gyda thrysorydd Tyddewi; yn yr Hengwrt, yna Peniarth; prynwyd gan Syr John Williams yn 1904 am £5,500."),
        url=_NLW_MS + "theblackbookofcarmarthen/", lang="en"),
    "nlw-aneirin": dict(short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"), t="The Book of Aneirin",
        by=("National Library of Wales (Cardiff MS 2.81)", "Llyfrgell Genedlaethol Cymru (Caerdydd 2.81)"),
        note=("Thirty-eight pages, written about 1250–1300 by two scribes, perhaps at Aberconwy; owned by Dafydd Nanmor and Gwilym Tew; at Hengwrt; bought by Cardiff Free Library in 1896.",
              "Tri deg wyth o dudalennau, a ysgrifennwyd tua 1250–1300 gan ddau gopïydd, efallai yn Aberconwy; yn eiddo i Ddafydd Nanmor a Gwilym Tew; yn yr Hengwrt; prynwyd gan Lyfrgell Rydd Caerdydd yn 1896."),
        url=_NLW_MS + "book-of-aneirin", lang="en"),
    "nlw-taliesin": dict(short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"), t="The Book of Taliesin",
        by=("National Library of Wales (Peniarth MS 2)", "Llyfrgell Genedlaethol Cymru (Peniarth 2)"),
        note=("Copied by a single scribe in the first half of the fourteenth century, probably in Glamorgan; its first leaf lost; transcribed by John Davies of Mallwyd 1631–34; at Hengwrt by 1655.",
              "Copïwyd gan un copïydd yn hanner cyntaf y bedwaredd ganrif ar ddeg, ym Morgannwg yn ôl pob tebyg; collwyd ei ddalen gyntaf; trawsgrifiwyd gan John Davies o Fallwyd 1631–34; yn yr Hengwrt erbyn 1655."),
        url=_NLW_MS + "book-of-taliesin", lang="en"),
    "nlw-white": dict(short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"), t="The White Book of Rhydderch",
        by=("National Library of Wales (Peniarth MSS 4 and 5)", "Llyfrgell Genedlaethol Cymru (Peniarth 4 a 5)"),
        note=("Mid fourteenth century, five scribes, probably at Strata Florida, for Rhydderch ab Ieuan Llwyd; later at Rhiwedog, with John Jones of Gellilyfdy, Hengwrt and Peniarth.",
              "Canol y bedwaredd ganrif ar ddeg, pump o gopïwyr, yn Ystrad Fflur yn ôl pob tebyg, i Rydderch ab Ieuan Llwyd; yn ddiweddarach yn Rhiwedog, gyda John Jones o Gellilyfdy, yr Hengwrt a Pheniarth."),
        url=_NLW_MS + "white-book-of-rhydderch", lang="en"),
    "nlw-hendregadredd": dict(short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"), t="The Hendregadredd Manuscript",
        by=("National Library of Wales (NLW MS 6680B)", "Llyfrgell Genedlaethol Cymru (LlGC 6680B)"),
        note=("The anthology of the Poets of the Princes, begun after 1282, probably at Strata Florida; found in a wardrobe at Hendregadredd in 1910; bought for the Library in 1923.",
              "Blodeugerdd Beirdd y Tywysogion, a ddechreuwyd wedi 1282, yn Ystrad Fflur yn ôl pob tebyg; cafwyd mewn wardrob yn Hendregadredd yn 1910; prynwyd i’r Llyfrgell yn 1923."),
        url="https://www.library.wales/discover-learn/digital-exhibitions/manuscripts/the-middle-ages/hendregadredd-manuscript", lang="en"),
    "nlw-chronicle": dict(short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"), t="The Chronicle of the Princes",
        by=("National Library of Wales (Peniarth MS 20)", "Llyfrgell Genedlaethol Cymru (Peniarth 20)"),
        note=("The Welsh translation of the lost Latin Cronica Principium Wallie, probably kept at Strata Florida; Peniarth 20 is the fuller of the two main versions, the other being in the Red Book of Hergest.",
              "Y cyfieithiad Cymraeg o’r Cronica Principium Wallie Lladin coll, a gadwyd yn Ystrad Fflur yn ôl pob tebyg; Peniarth 20 yw’r llawnaf o’r ddau brif fersiwn, a’r llall yn Llyfr Coch Hergest."),
        url=_NLW_MS + "chronicle-of-the-princes/", lang="en"),
    "nlw-basingwerk": dict(short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"), t="The Black Book of Basingwerk",
        by=("National Library of Wales (NLW MS 7006D)", "Llyfrgell Genedlaethol Cymru (LlGC 7006D)"),
        note=("Copied at Valle Crucis; pages 89–308 in the hand of Gutun Owain, whose continuation runs to 1461; Ystoria Dared, Brut y Brenhinedd, Brenhinedd y Saesson and Brut y Tywysogion; its medieval wooden boards survive.",
              "Copïwyd yng Nglyn y Groes; tudalennau 89–308 yn llaw Gutun Owain, y mae ei barhad yn rhedeg hyd 1461; Ystoria Dared, Brut y Brenhinedd, Brenhinedd y Saesson a Brut y Tywysogion; mae ei gloriau pren canoloesol wedi goroesi."),
        url=_NLW_MS + "black-book-of-basingwerk", lang="en"),
    "wiki-red-book": dict(short=("Wikipedia", "Wicipedia"), t="Red Book of Hergest", by=("Wikipedia", "Wicipedia"),
        note=("362 leaves, written shortly after 1382 by Hywel Fychan and others for Hopcyn ap Tomas; at Tretower, Hergest, Margam; given to Jesus College by Thomas Wilkins the younger on 17 February 1701.",
              "362 o ddail, a ysgrifennwyd yn fuan wedi 1382 gan Hywel Fychan ac eraill i Hopcyn ap Tomas; yn Nhretŵr, Hergest, Margam; rhoddwyd i Goleg Iesu gan Thomas Wilkins yr ieuengaf ar 17 Chwefror 1701."),
        url="https://en.wikipedia.org/wiki/Red_Book_of_Hergest", lang="en"),
    "wiki-chad": dict(short=("Wikipedia", "Wicipedia"), t="St Chad Gospels", by=("Wikipedia", "Wicipedia"),
        note=("An eighth-century gospel book; a marginal note records that Gelhi bought it for his best horse and gave it to God on the altar of St Teilo; at Lichfield by the end of the tenth century.",
              "Llyfr efengylau o’r wythfed ganrif; mae nodyn ymyl yn cofnodi i Gelhi ei brynu am ei farch gorau a’i roi i Dduw ar allor Teilo; yng Nghaerlwytgoed erbyn diwedd y ddegfed ganrif."),
        url="https://en.wikipedia.org/wiki/St_Chad_Gospels", lang="en"),
    "wiki-yny": dict(short=("Wikipedia", "Wicipedia"), t="Yny lhyvyr hwnn", by=("Wikipedia", "Wicipedia"),
        note=("The first book printed in Welsh, by Sir John Price, printed in London by Edward Whitchurch in 1546; one copy known, given to the National Library of Wales by Sir John Williams in 1908.",
              "Y llyfr cyntaf a argraffwyd yn Gymraeg, gan Syr John Prys, a argraffwyd yn Llundain gan Edward Whitchurch yn 1546; un copi hysbys, a roddwyd i Lyfrgell Genedlaethol Cymru gan Syr John Williams yn 1908."),
        url="https://en.wikipedia.org/wiki/Yny_lhyvyr_hwnn", lang="en"),
    "wiki-ancr": dict(short=("Wikipedia", "Wicipedia"), t="Book of the Anchorite of Llanddewibrefi", by=("Wikipedia", "Wicipedia"),
        note=("Jesus College MS 119, dated 1346 by its colophon, written by an anchorite for Gruffudd ap Llywelyn ap Phylip ap Trahaearn of Cantref Mawr; the Elucidarium, Ymborth yr Enaid, Breuddwyd Pawl and the Land of Prester John.",
              "Coleg Iesu MS 119, a ddyddiwyd 1346 gan ei goloffon, a ysgrifennwyd gan ancr i Ruffudd ap Llywelyn ap Phylip ap Trahaearn o’r Cantref Mawr; yr Elucidarium, Ymborth yr Enaid, Breuddwyd Pawl a Gwlad y Preutur Siôn."),
        url="https://en.wikipedia.org/wiki/Book_of_the_Anchorite_of_Llanddewibrefi", lang="en"),
    "wiki-peniarth28": dict(short=("Wikipedia", "Wicipedia"), t="Peniarth 28", by=("Wikipedia", "Wicipedia"),
        note=("A Latin text of the laws of Hywel Dda from the second half of the thirteenth century, with pictures of King Hywel, a judge, a hawker and others.",
              "Testun Lladin o gyfraith Hywel Dda o ail hanner y drydedd ganrif ar ddeg, gyda lluniau o’r Brenin Hywel, ynad, hebogydd ac eraill."),
        url="https://en.wikipedia.org/wiki/Peniarth_28", lang="en"),
    "wiki-triads": dict(short=("Wikipedia", "Wicipedia"), t="Welsh Triads", by=("Wikipedia", "Wicipedia"),
        note=("Peniarth 16, the earliest collection, from the third quarter of the thirteenth century, keeps 46 of the 96 triads in Rachel Bromwich’s edition; Peniarth 45 was written about 1275.",
              "Mae Peniarth 16, y casgliad cynharaf, o drydydd chwarter y drydedd ganrif ar ddeg, yn cadw 46 o’r 96 triawd yn argraffiad Rachel Bromwich; ysgrifennwyd Peniarth 45 tua 1275."),
        url="https://en.wikipedia.org/wiki/Welsh_Triads", lang="en"),
}

_HUWS = (_B_, "Daniel Huws", "Medieval Welsh Manuscripts", "University of Wales Press and the National Library of Wales, 2000",
         "The great modern study of the Welsh books written by hand, by the National Library’s keeper of manuscripts.",
         "Yr astudiaeth fodern fawr o’r llyfrau Cymraeg a ysgrifennwyd â llaw, gan geidwad llawysgrifau’r Llyfrgell Genedlaethol.")
_NLW = (_W, "National Library of Wales", "Medieval manuscripts in the digital gallery", "library.wales",
        "Every page of the great Welsh manuscripts, photographed, to read online.", "Pob tudalen o lawysgrifau mawr Cymru, wedi’u ffotograffu, i’w darllen ar-lein.",
        "https://www.library.wales/discover/digital-gallery/manuscripts/the-middle-ages")
REFS = {
 "book-red": dict(dwb=["hopcyn-ap-tomos", "hywel-fychan"], items=[
   (_P, "John Rhŷs and J. Gwenogvryn Evans (eds)", "The Text of the Mabinogion and Other Welsh Tales from the Red Book of Hergest", "Oxford, 1887",
    "The prose of the Red Book in print, page for page.", "Rhyddiaith y Llyfr Coch mewn print, dudalen am dudalen."),
   _HUWS, _NLW]),
 "book-llyfr-ancr": dict(items=[
   (_P, "J. Morris Jones and John Rhŷs (eds)", "The Elucidarium and Other Tracts in Welsh from Llyvyr Agkyr Llandewivrevi, A.D. 1346", "Clarendon Press, Oxford, 1894",
    "The whole book in print, with its Latin sources. Free to read online.", "Y llyfr cyfan mewn print, gyda’i ffynonellau Lladin. Am ddim i’w ddarllen ar-lein.",
    "https://archive.org/details/elucidariumother00joneuoft"),
   _HUWS]),
 "book-basingwerk": dict(dwb=["gutun-owain"], items=[
   (_P, "Thomas Jones (ed. and trans.)", "Brenhinedd y Saesson, or The Kings of the Saxons", "University of Wales Press, 1971",
    "The chronicle of the Black Book of Basingwerk, in Welsh and English.", "Cronicl Llyfr Du Basing, yn Gymraeg ac yn Saesneg."),
   _HUWS, _NLW]),
 "book-peniarth": dict(dwb=["sir-john-williams"], items=[
   (_P, "J. Gwenogvryn Evans", "Report on Manuscripts in the Welsh Language, volume I", "Historical Manuscripts Commission, London, 1898–99",
    "The list of the Peniarth manuscripts that gave each its number.", "Y rhestr o lawysgrifau Peniarth a roddodd ei rif i bob un."),
   _HUWS, _NLW]),
}

# The medieval Welsh manuscripts (src/manuscripts.py): 21 more books, four new groups and the manuscripts.html list.
import manuscripts as MSS
PAGES.update(MSS.PAGES)
FIGS.update({k: v for k, v in MSS.FIGS.items() if k not in FIGS})
CITES.update({k: v for k, v in MSS.CITES.items() if k not in CITES})
REFS.update(MSS.REFS)
