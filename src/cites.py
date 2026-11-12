"""Sources beside the claims: a small link next to a sentence that opens the evidence for it.

Every content page already ends with a reading list (refs.py, refs2.py). This adds the source right beside the
claim it supports, starting with the facts the site features, the superlatives ("largest", "first", "oldest") and
the stories that rest on tradition. Asked for by Ifan, 12 November 2026.

HOW TO CITE A SENTENCE
  Put a marker straight after the full stop, with no space:   "...anywhere in the world.[[cite:orme-antiquity,orme-gsl]]"
  Put the same marker in the Welsh sentence too. One marker can name several sources, most important first.
  The build turns the marker into a small chip with the first source's short name ("Antiquity, 2019 +2").
  Tap or click it and a little card opens with every source, who wrote it and what it shows, each linked.
  Without JavaScript the chip is a plain link to the first source.
  In places a chip cannot go (page titles, descriptions, search, feeds, the weekly email, inside a link) the marker
  is quietly removed, so a marker can never show up as text.

RULES (see EDITORIAL.md, "Sources beside the claims")
  - Only real sources, each one opened and read before it goes in. Give the claim's own evidence where there is
    any: the archaeological paper, the museum that holds the find, the old text itself.
  - The source must say what the sentence says. If it says less, change the sentence to match the source.
  - On traditional stories (Arthur as Athrwys, Madog, Brutus) cite the tradition's own sources: the old texts and
    the books that make its case. No debunking sources and no debunking words.
  - Keep "short" to a few words; it is what the chip shows.

Entry: key -> dict(short=(en, cy), t=title, by=(en, cy) who and where, note=(en, cy), url=link or None, url_cy=Welsh page,
                   lang="en" when the source itself is only in English (the Welsh card says so))
"""
import html as _html
import re

S = {
    # ---------- the Great Orme ----------
    "orme-antiquity": dict(
        short=("Antiquity, 2019", "Antiquity, 2019"),
        t="Boom and bust in Bronze Age Britain: major copper production from the Great Orme mine and European trade, c. 1600–1400 BC",
        by=("R. Alan Williams and Cécile Le Carlier de Veslud, Antiquity 93 (2019), pp. 1178–1196", "R. Alan Williams a Cécile Le Carlier de Veslud, Antiquity 93 (2019), tt. 1178–1196"),
        note=("The archaeological study of the mine: radiocarbon dates, several kilometres of workings, and Orme copper traced in metalwork across Europe. It calls the mine one of Europe’s largest.",
              "Astudiaeth archaeolegol o’r mwynglawdd: dyddiadau radiocarbon, sawl cilometr o weithfeydd, a chopr y Gogarth wedi’i olrhain mewn gwaith metel ar draws Ewrop. Mae’n galw’r mwynglawdd yn un o’r mwyaf yn Ewrop."),
        url="https://doi.org/10.15184/aqy.2019.130", lang="en"),
    "orme-gsl": dict(
        short=("Geological Society", "Cymdeithas Ddaearegol"),
        t="Great Orme Bronze Age Mine", by=("The Geological Society of London, Geosites", "Cymdeithas Ddaearegol Llundain, Geosites"),
        note=("“In extent the Great Orme mines are among the largest prehistoric mines in Europe and perhaps the world.”",
              "“O ran eu maint, mae mwyngloddiau’r Gogarth ymhlith mwyngloddiau cynhanesyddol mwyaf Ewrop ac efallai’r byd.”"),
        url="https://geolsoc.org.uk/GeositesGreatOrme", lang="en"),
    "orme-guinness": dict(
        short=("Guinness World Records", "Guinness World Records"),
        t="Largest Bronze Age copper mine", by=("Guinness World Records, 2003", "Guinness World Records, 2003"),
        note=("The record: the Great Orme Mines, with at least 8 km of accessible tunnels, mined from about 1800 BC.",
              "Y record: Mwyngloddiau’r Gogarth, ag o leiaf 8 km o dwneli hygyrch, a gloddiwyd o tua 1800 CC."),
        url="https://www.guinnessworldrecords.com/world-records/79151-largest-bronze-age-copper-mine", lang="en"),

    # ---------- the facts on the home page ----------
    "dwb-recorde": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"),
        t="Recorde, Robert (c. 1510–1558)", by=("Dictionary of Welsh Biography, National Library of Wales", "Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
        note=("Born at Tenby; his algebra book The Whetstone of Witte (1557) brought in the sign =, “because no two things can be more equal”.",
              "Ganed yn Ninbych-y-pysgod; yn ei lyfr algebra The Whetstone of Witte (1557) daeth yr arwydd =, “am na all dim dau beth fod yn fwy hafal”."),
        url="https://biography.wales/article/s11-RECO-ROB-1558", url_cy="https://bywgraffiadur.cymru/article/s11-RECO-ROB-1558"),
    "dwb-wjones": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"),
        t="Jones, William (1675?–1749), mathematician", by=("Dictionary of Welsh Biography, National Library of Wales", "Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
        note=("Born in Llanfihangel Tre’r Beirdd, Môn. The symbol π first appeared in his Synopsis Palmariorum Matheseos, 1706.",
              "Ganed yn Llanfihangel Tre’r Beirdd, Môn. Ymddangosodd y symbol π gyntaf yn ei Synopsis Palmariorum Matheseos, 1706."),
        url="https://biography.wales/article/s-JONE-WIL-1675", url_cy="https://bywgraffiadur.cymru/article/s-JONE-WIL-1675"),
    "tfw-mumbles": dict(
        short=("Transport for Wales", "Trafnidiaeth Cymru"),
        t="Swansea, Oystermouth and Mumbles Railway", by=("Transport for Wales, Railway 200", "Trafnidiaeth Cymru, Rheilffordd 200"),
        note=("“In March 1807, the very first fare paying rail passenger journey took place”, with carriages pulled by horses.",
              "Ym mis Mawrth 1807 y cafwyd y daith reilffordd gyntaf erioed i deithwyr oedd yn talu, a cheffylau’n tynnu’r cerbydau."),
        url="https://tfw.wales/railway-200/swansea-oystermouth-mumbles-railway",
        url_cy="https://trc.cymru/rheilffordd-200/rheilffordd-abertawe-ystumllwynarth-mwmbwls"),
    "bluestones-antiquity": dict(
        short=("Antiquity, 2015", "Antiquity, 2015"),
        t="Craig Rhos-y-felin: a Welsh bluestone megalith quarry for Stonehenge",
        by=("Mike Parker Pearson and others, Antiquity 89 (2015), pp. 1331–1352", "Mike Parker Pearson ac eraill, Antiquity 89 (2015), tt. 1331–1352"),
        note=("The excavation of the bluestone quarry in the Preseli hills, with radiocarbon dates for the stones being taken out in the fourth millennium BC, and the route to Stonehenge.",
              "Cloddio’r chwarel cerrig gleision ym mynyddoedd y Preseli, gyda dyddiadau radiocarbon i’r meini gael eu tynnu yn y bedwaredd fileniwm CC, a’r llwybr i Gôr y Cewri."),
        url="https://doi.org/10.15184/aqy.2015.177", lang="en"),
    "stdavids-wiki": dict(
        short=("Wikipedia", "Wikipedia"),
        t="St Davids", by=("Wikipedia, from the 2021 census", "Wikipedia, o gyfrifiad 2021"),
        note=("St Davids is the United Kingdom’s smallest city by population: 1,751 people in 2021.",
              "Tyddewi yw dinas leiaf y Deyrnas Unedig o ran poblogaeth: 1,751 o bobl yn 2021."),
        url="https://en.wikipedia.org/wiki/St_Davids", url_cy="https://cy.wikipedia.org/wiki/Tyddewi"),
    "marconi-veterans": dict(
        short=("Marconi Veterans", "Marconi Veterans"),
        t="Marconi in South Wales", by=("The Marconi Veterans’ Association newsletter, 2021", "Cylchlythyr Cymdeithas Cyn-weithwyr Marconi, 2021"),
        note=("On 13 May 1897 “Marconi sent the first ever wireless communication over open sea”, across the Bristol Channel between Flat Holm and Lavernock Point. The message: “Are you ready”.",
              "Ar 13 Mai 1897 anfonodd Marconi y neges ddiwifr gyntaf erioed dros fôr agored, ar draws Môr Hafren rhwng Ynys Echni a Thrwyn Larnog. Y neges: “Are you ready”."),
        url="https://www.marconi-veterans.org/index.php/newsletters/2021-newsletter/88-21a10-marconi-in-south-wales", lang="en"),
    "alphabet-parallel": dict(
        short=("Parallel.cymru", "Parallel.cymru"),
        t="Ask Dr Gramadeg: the alphabet", by=("Parallel.cymru, the bilingual Welsh magazine", "Parallel.cymru, y cylchgrawn Cymraeg dwyieithog"),
        note=("The Welsh alphabet letter by letter: “ch, dd, ff, ng, ll, ph, rh and th count as one letter each”.",
              "Yr wyddor Gymraeg fesul llythyren: mae ch, dd, ff, ng, ll, ph, rh a th yn cyfrif fel un llythyren yr un."),
        url="https://parallel.cymru/ask-dr-gramadeg-the-alphabet/"),
    "pryce-storipowys": dict(
        short=("Stori Powys", "Stori Powys"),
        t="Pryce Jones and Britain’s First Mail Order Company", by=("Stori Powys, Powys County Council’s heritage site", "Stori Powys, gwefan dreftadaeth Cyngor Sir Powys"),
        note=("In 1861 Pryce Jones used the new national post to begin “the first ever mail order business”. His customers included Queen Victoria and Florence Nightingale.",
              "Yn 1861 defnyddiodd Pryce Jones y post cenedlaethol newydd i ddechrau’r busnes archebu drwy’r post cyntaf erioed. Ymhlith ei gwsmeriaid roedd y Frenhines Fictoria a Florence Nightingale."),
        url="https://www.storipowys.org.uk/merged-treasures/pryce-jones-and-britains-first-mail-order-company", lang="en"),
    "dwb-pryce": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"),
        t="Pryce-Jones, Sir Pryce (1834–1920), pioneer of mail order business", by=("Dictionary of Welsh Biography, National Library of Wales", "Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
        note=("Newtown flannel sent by post across the world, to more than 300,000 customers, Queen Victoria among them.",
              "Gwlanen y Drenewydd yn cael ei hanfon drwy’r post ar draws y byd, i fwy na 300,000 o gwsmeriaid, y Frenhines Fictoria yn eu plith."),
        url="https://biography.wales/article/s3-PRYC-PRY-1834", url_cy="https://bywgraffiadur.cymru/article/s3-PRYC-PRY-1834"),
    "llanfair-nasa": dict(
        short=("NASA Earth Observatory", "NASA Earth Observatory"),
        t="A Little Town with a Long Name", by=("NASA Earth Observatory", "NASA Earth Observatory"),
        note=("A local man pushed for the longer name in the 1860s, to bring in tourists and give the station the longest name in Britain.",
              "Fe wthiodd gŵr lleol am yr enw hir yn y 1860au, i ddenu twristiaid a rhoi i’r orsaf yr enw hiraf ym Mhrydain."),
        url="https://science.nasa.gov/earth/earth-observatory/a-little-town-with-a-long-name", lang="en"),
    "menai-graces": dict(
        short=("Grace’s Guide", "Grace’s Guide"),
        t="Menai Bridge", by=("Grace’s Guide to British Industrial History", "Grace’s Guide, hanes diwydiannol Prydain"),
        note=("Opened on 30 January 1826; when it was completed “it was the largest suspension bridge in the world”.",
              "Agorwyd ar 30 Ionawr 1826; pan orffennwyd hi, hi oedd y bont grog fwyaf yn y byd."),
        url="https://gracesguide.co.uk/Menai_Bridge", lang="en"),
    "menai-ice": dict(
        short=("Institution of Civil Engineers", "Sefydliad y Peirianwyr Sifil"),
        t="Menai crossings", by=("Institution of Civil Engineers", "Sefydliad y Peirianwyr Sifil"),
        note=("Telford’s chains carry a main span of 577 feet (176 m); work began in 1819.",
              "Mae cadwyni Telford yn cario prif rychwant o 577 troedfedd (176 m); dechreuwyd y gwaith yn 1819."),
        url="https://www.ice.org.uk/what-is-civil-engineering/what-do-civil-engineers-do/menai-crossings", lang="en"),
    "everest-pyg": dict(
        short=("Mark Horrell", "Mark Horrell"),
        t="Snowdon’s Pen-y-Gwryd Hotel: a little piece of Everest history", by=("Mark Horrell, mountaineer and writer, 2015", "Mark Horrell, dringwr ac awdur, 2015"),
        note=("In 1953 the hotel “was home to the British Everest team as they trained and tested equipment”; the signed ceiling is still there.",
              "Yn 1953 y gwesty oedd cartref tîm Everest Prydain wrth iddynt ymarfer a phrofi eu hoffer; mae’r nenfwd â’u llofnodion yno o hyd."),
        url="https://www.markhorrell.com/blog/2015/snowdons-pen-y-gwryd-hotel-a-little-piece-of-everest-history/", lang="en"),
    "slate-unesco": dict(
        short=("UNESCO", "UNESCO"),
        t="The Slate Landscape of Northwest Wales", by=("UNESCO World Heritage List, inscribed 2021", "Rhestr Treftadaeth y Byd UNESCO, 2021"),
        note=("“By the late 19th century, the region produced about a third of the world output of roofing slates.”",
              "Erbyn diwedd y bedwaredd ganrif ar bymtheg, roedd yr ardal yn cynhyrchu tua thraean o lechi to’r byd."),
        url="https://whc.unesco.org/en/list/1633", lang="en"),
    "hywel-jenkins": dict(
        short=("Dafydd Jenkins, 1986", "Dafydd Jenkins, 1986"),
        t="The Law of Hywel Dda: Law Texts from Mediaeval Wales", by=("Dafydd Jenkins (trans. and ed.), Gomer, 1986, pp. 310–311", "Dafydd Jenkins (cyf. a gol.), Gomer, 1986, tt. 310–311"),
        note=("The law of women: if a marriage broke up after seven years, the wife was entitled to half of all they held in common.",
              "Cyfraith y gwragedd: os torrai priodas ar ôl saith mlynedd, roedd hawl gan y wraig i hanner popeth oedd ganddynt yn gyffredin."),
        url=None, lang="en"),
    "hywel-wiki": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Cyfraith Hywel", by=("Wikipedia, citing Dafydd Jenkins", "Wikipedia, yn dyfynnu Dafydd Jenkins"),
        note=("“If the marriage broke up after the end of 7 years, the woman was entitled to half the common pool.”",
              "Os torrai’r briodas ar ôl saith mlynedd, roedd hawl gan y wraig i hanner y cyfan oedd ganddynt yn gyffredin."),
        url="https://en.wikipedia.org/wiki/Cyfraith_Hywel", lang="en"),
    "dahl-visitwales": dict(
        short=("Visit Wales", "Croeso Cymru"),
        t="Roald Dahl’s Wales", by=("Visit Wales, Welsh Government", "Croeso Cymru, Llywodraeth Cymru"),
        note=("Born in 1916 at Villa Marie, Fairwater Road, Llandaff, to a family from Norway, and christened at the Norwegian Church in Cardiff Bay.",
              "Ganed yn 1916 yn Villa Marie, Fairwater Road, Llandaf, i deulu o Norwy, a’i fedyddio yn yr Eglwys Norwyaidd ym Mae Caerdydd."),
        url="https://www.visitwales.com/things-do/culture/cultural-activities/roald-dahls-wales", lang="en"),
    "patagonia-wales": dict(
        short=("Wales.com", "Wales.com"),
        t="The history of the Welsh people in Patagonia", by=("Wales.com, Welsh Government", "Wales.com, Llywodraeth Cymru"),
        note=("The Mimosa brought the settlers in 1865; Welsh is still taught and spoken, and Trelew hosts the annual Eisteddfod.",
              "Daeth y Mimosa â’r ymfudwyr yn 1865; mae’r Gymraeg yn dal i gael ei dysgu a’i siarad, a Threlew sy’n cynnal yr Eisteddfod flynyddol."),
        url="https://www.wales.com/about/language/history-welsh-people-patagonia", lang="en"),
    "grove-aps": dict(
        short=("American Physical Society", "American Physical Society"),
        t="October 1842: William Grove’s letter to Faraday describing a fuel cell", by=("APS News, American Physical Society, 2019", "APS News, American Physical Society, 2019"),
        note=("“Science historians generally deem his invention to be the first bona fide fuel cell.”",
              "Mae haneswyr gwyddoniaeth yn gyffredinol yn ystyried ei ddyfais yn gell danwydd go iawn gyntaf."),
        url="https://aps.org/publications/apsnews/201909/history.cfm", lang="en"),
    "dwb-grove": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"),
        t="Grove, Sir William Robert (1811–1896)", by=("Dictionary of Welsh Biography, National Library of Wales", "Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
        note=("Born in Swansea on 11 July 1811: judge and man of science.", "Ganed yn Abertawe ar 11 Gorffennaf 1811: barnwr a gwyddonydd."),
        url="https://biography.wales/article/s-GROV-ROB-1811", url_cy="https://bywgraffiadur.cymru/article/s-GROV-ROB-1811"),
    "caerphilly-cadw": dict(
        short=("Cadw", "Cadw"),
        t="Caerphilly Castle", by=("Cadw, the Welsh Government’s historic environment service", "Cadw, gwasanaeth amgylchedd hanesyddol Llywodraeth Cymru"),
        note=("“The biggest castle in Wales, second only to Windsor in the whole of Britain”, with a leaning tower “even wonkier than that of Pisa”.",
              "Y castell mwyaf yng Nghymru, yn ail i Windsor yn unig ym Mhrydain gyfan, gyda thŵr sy’n gwyro’n fwy na thŵr Pisa."),
        url="https://cadw.gov.wales/visit/places-to-visit/caerphilly-castle", url_cy="https://cadw.gov.wales/visit/places-to-visit/caerphilly-castle?lang=cy"),
    "paviland-museum": dict(
        short=("Amgueddfa Cymru", "Amgueddfa Cymru"),
        t="Origins: in search of Early Wales", by=("Amgueddfa Cymru – Museum Wales, 2007", "Amgueddfa Cymru, 2007"),
        note=("The new dating of the Red Lady, “the oldest known ceremonial burial in western Europe”, a young man covered in red ochre.",
              "Dyddio newydd ar Ddynes Goch Pafiland, y gladdedigaeth seremonïol hynaf y gwyddys amdani yng ngorllewin Ewrop, sef gŵr ifanc wedi’i orchuddio ag ocr coch."),
        url="https://museum.wales/news/404/Origins-in-search-of-Early-Wales/", lang="en"),
    "paviland-oumnh": dict(
        short=("Oxford Museum of Natural History", "Amgueddfa Hanes Natur Rhydychen"),
        t="The ‘Red Lady’ of Paviland", by=("Oxford University Museum of Natural History, which holds the bones", "Amgueddfa Hanes Natur Prifysgol Rhydychen, sy’n cadw’r esgyrn"),
        note=("“The remains of a young man”; “the bones are around 33–34,000 years old.”",
              "Gweddillion gŵr ifanc; mae’r esgyrn tua 33–34,000 o flynyddoedd oed."),
        url="https://oumnh.ox.ac.uk/node/328621", lang="en"),
    "bethlehem-radio": dict(
        short=("Vatican Radio, 2012", "Radio’r Fatican, 2012"),
        t="Thousands flock to post a Christmas card from Bethlehem", by=("Vatican Radio, 18 December 2012", "Radio’r Fatican, 18 Rhagfyr 2012"),
        note=("People come from all over the UK and abroad to the post office at Bethlehem, Carmarthenshire, for its Christmas handstamp; Royal Mail says thousands use it.",
              "Daw pobl o bob rhan o’r Deyrnas Unedig a thramor i swyddfa bost Bethlehem, Sir Gâr, am ei stamp Nadolig; mae’r Post Brenhinol yn dweud bod miloedd yn ei ddefnyddio."),
        url="https://www.archivioradiovaticana.va/storico/2012/12/18/thousands_flock_to_post_a_christmas_card_from_bethlehem/in2-648766", lang="en"),

    # ---------- the traditions: their own sources ----------
    "llandav-text": dict(
        short=("Book of Llandaff", "Llyfr Llandaf"),
        t="The Text of the Book of Llan Dâv", by=("J. Gwenogvryn Evans with John Rhŷs (eds), Oxford, 1893", "J. Gwenogvryn Evans gyda John Rhŷs (gol.), Rhydychen, 1893"),
        note=("The full text of Liber Landavensis, the charters of the kings of Gwent and Glywysing, in which Athrwys son of Meurig is named. Free to read online.",
              "Testun llawn Liber Landavensis, siarteri brenhinoedd Gwent a Glywysing, lle’r enwir Athrwys fab Meurig. Am ddim i’w ddarllen ar-lein."),
        url="https://archive.org/details/cu31924028051559"),
    "llandav-nlw": dict(
        short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"),
        t="The Book of Llandaff", by=("National Library of Wales, which keeps the manuscript (NLW MS 17110E)", "Llyfrgell Genedlaethol Cymru, sy’n cadw’r llawysgrif (LlGC llsgr. 17110E)"),
        note=("The manuscript itself, written at Llandaff between about 1120 and 1140.",
              "Y llawysgrif ei hun, a ysgrifennwyd yn Llandaf rhwng tua 1120 ac 1140."),
        url="https://www.library.wales/discover-learn/digital-exhibitions/manuscripts/the-middle-ages/the-book-of-llandaff/", lang="en"),
    "holy-kingdom": dict(
        short=("The Holy Kingdom", "The Holy Kingdom"),
        t="The Holy Kingdom", by=("Adrian Gilbert, Alan Wilson and Baram Blackett, Bantam Press, 1998", "Adrian Gilbert, Alan Wilson a Baram Blackett, Bantam Press, 1998"),
        note=("The case for Arthur as Athrwys ap Meurig, king of Gwent and Glamorgan, set out at length.",
              "Yr achos dros Arthur fel Athrwys ap Meurig, brenin Gwent a Morgannwg, wedi’i osod allan yn llawn."),
        url=None, lang="en"),
    "powel-1584": dict(
        short=("Historie of Cambria, 1584", "Historie of Cambria, 1584"),
        t="The Historie of Cambria, now called Wales", by=("Humphrey Llwyd, finished and printed by David Powel, London, 1584", "Humphrey Llwyd, wedi’i orffen a’i argraffu gan David Powel, Llundain, 1584"),
        note=("The first telling of Madog’s voyage in print: he “sought adventures by seas, sailing west … that he came to a land unknown”. Free to read online.",
              "Yr hanes cyntaf mewn print am fordaith Madog: aeth i chwilio am anturiaethau ar y môr, gan hwylio tua’r gorllewin nes dod i wlad anhysbys. Am ddim i’w ddarllen ar-lein."),
        url="https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/A17946", lang="en"),
    "dwb-powel": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"),
        t="Powel, David (c. 1540–1598), cleric and historian", by=("Dictionary of Welsh Biography, National Library of Wales", "Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
        note=("How Powel prepared Humphrey Llwyd’s translation of the Welsh chronicle and printed it in 1584.",
              "Sut y paratôdd Powel gyfieithiad Humphrey Llwyd o’r cronicl Cymraeg a’i argraffu yn 1584."),
        url="https://biography.wales/article/s-POWE-DAV-1540", url_cy="https://bywgraffiadur.cymru/article/s-POWE-DAV-1540"),
    "historia-brittonum": dict(
        short=("Historia Brittonum", "Historia Brittonum"),
        t="History of the Britons (Historia Brittonum)", by=("translated by J. A. Giles, Project Gutenberg", "cyfieithiad Saesneg J. A. Giles, Project Gutenberg"),
        note=("The History of the Britons, gathered in Gwynedd about 829, which tells of Brutus and how Britain took its name from him.",
              "Hanes y Brytaniaid, a gasglwyd yng Ngwynedd tua 829, sy’n adrodd am Brutus a sut y cafodd Prydain ei henw ganddo."),
        url="https://www.gutenberg.org/ebooks/1972", lang="en"),
    "geoffrey-evans": dict(
        short=("Geoffrey of Monmouth", "Sieffre o Fynwy"),
        t="Histories of the Kings of Britain, by Geoffrey of Monmouth", by=("translated by Sebastian Evans, J. M. Dent, 1904", "cyfieithiad Saesneg Sebastian Evans, J. M. Dent, 1904"),
        note=("Geoffrey’s History of the Kings of Britain, about 1136, in the translation quoted here. Free to read online.",
              "Hanes Brenhinoedd Prydain gan Sieffre, tua 1136, yn y cyfieithiad a ddyfynnir yma. Am ddim i’w ddarllen ar-lein."),
        url="https://archive.org/details/geoffreyofmonmou00geofuoft", lang="en"),
    "adam-usk": dict(
        short=("Adam of Usk", "Adda o Frynbuga"),
        t="Chronicon Adae de Usk, A.D. 1377–1421", by=("Edward Maunde Thompson (ed. and trans.), London, 1904", "Edward Maunde Thompson (gol. a chyf.), Llundain, 1904"),
        note=("Adam of Usk copied Owain Glyndŵr’s letter of 1401 to Robert III, King of Scots, into his chronicle. Free to read online.",
              "Copïodd Adda o Frynbuga lythyr Owain Glyndŵr at Robert III, brenin yr Alban, yn 1401 i’w gronicl. Am ddim i’w ddarllen ar-lein."),
        url="https://archive.org/details/chroniconadaedeu00adamuoft", lang="en"),
    # ---------- the Aberfan disaster (story-aberfan.html) ----------
    "aberfan-wiki": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Aberfan disaster", by=("Wikipedia, drawing on the Tribunal report (1967) and McLean and Johnes (2000)", "Wikipedia, ar sail adroddiad y Tribiwnlys (1967) a McLean a Johnes (2000)"),
        note=("The tip, the morning of 21 October 1966, the rescue, the earlier slides and the council’s letters about the “Danger from Coal Slurry being tipped at the rear of the Pantglas Schools”, and the Tribunal’s 76 days and 136 witnesses.",
              "Y domen, bore 21 Hydref 1966, yr achub, y llithriadau cynharach a llythyrau’r cyngor am y perygl o’r slyri glo a domennid y tu cefn i ysgolion Pantglas, a 76 diwrnod a 136 tyst y Tribiwnlys."),
        url="https://en.wikipedia.org/wiki/Aberfan_disaster", url_cy="https://cy.wikipedia.org/wiki/Trychineb_Aberfan"),
    "aberfan-bar": dict(
        short=("British Academy Review", "British Academy Review"),
        t="Lessons from the Aberfan disaster and its aftermath", by=("Iain McLean, British Academy Review", "Iain McLean, British Academy Review"),
        note=("By the historian of the disaster: 109 children and five teachers died in the school, 144 in all; the Tribunal found the Coal Board wholly at fault; the fund reached £1.75m; the Charity Commission’s demands; the £150,000 taken for the tips, returned in 1997, and £1.5m in 2007.",
              "Gan hanesydd y trychineb: bu farw 109 o blant a phump o athrawon yn yr ysgol, 144 i gyd; canfu’r Tribiwnlys mai’r Bwrdd Glo oedd yn llwyr ar fai; cyrhaeddodd y gronfa £1.75m; gofynion y Comisiwn Elusennau; y £150,000 a gymerwyd at y tomenni, a roddwyd yn ôl yn 1997, a £1.5m yn 2007."),
        url="https://www.thebritishacademy.ac.uk/publishing/review/12/lessons-aberfan-disaster-and-its-aftermath/", lang="en"),
    "aberfan-gov": dict(
        short=("Tribunal report, 1967", "Adroddiad y Tribiwnlys, 1967"),
        t="The Aberfan Disaster, 21 October 1966", by=("UK Government, from the Report of the Tribunal (HMSO, 1967)", "Llywodraeth y DU, o Adroddiad y Tribiwnlys (HMSO, 1967)"),
        note=("Quotes the report: “a terrifying tale of bungling ineptitude”, and “Not villains but decent men, led astray by foolishness or by ignorance or by both in combination”.",
              "Yn dyfynnu’r adroddiad: “hanes brawychus am anallu trwsgl”, a “Nid dihirod ond dynion gweddus, wedi’u camarwain gan ffolineb neu gan anwybodaeth neu gan y ddau ynghyd”."),
        url="https://assets.publishing.service.gov.uk/media/5a790a75e5274a2acd18bbf6/InquiriesIncidentTheAberfanDisaster21October1966.pdf", lang="en"),
    "aberfan-1967": dict(
        short=("Commons debate, 1967", "Dadl Tŷ’r Cyffredin, 1967"),
        t="1967 speech on the Aberfan Inquiry", by=("David Gibson-Watt MP, House of Commons", "David Gibson-Watt AS, Tŷ’r Cyffredin"),
        note=("Tells of the 1963 letters from Mr Jones, the Borough Engineer, and quotes the Tribunal’s first finding: “Blame for the disaster rests upon the National Coal Board.”",
              "Yn sôn am lythyrau 1963 gan Mr Jones, Peiriannydd y Fwrdeistref, ac yn dyfynnu canfyddiad cyntaf y Tribiwnlys: ar y Bwrdd Glo Cenedlaethol y mae’r bai am y trychineb."),
        url="https://www.ukpol.co.uk/?p=49575", lang="en"),
    "aberfan-hansard-1997": dict(
        short=("Hansard, 1997", "Hansard, 1997"),
        t="Aberfan: written answers, 31 July 1997", by=("Hansard, House of Commons: Ted Rowlands asks, Ron Davies answers", "Hansard, Tŷ’r Cyffredin: Ted Rowlands yn gofyn, Ron Davies yn ateb"),
        note=("“I shall be making available a grant of £150,000 to repay the sum originally contributed.”",
              "“Byddaf yn rhoi grant o £150,000 i ad-dalu’r swm a gyfrannwyd yn wreiddiol.”"),
        url="https://api.parliament.uk/historic-hansard/written-answers/1997/jul/31/aberfan", lang="en"),
    "aberfan-oxford-2007": dict(
        short=("University of Oxford, 2007", "Prifysgol Rhydychen, 2007"),
        t="Iain McLean, campaigner for Aberfan community, welcomes funding announcement", by=("Department of Politics and International Relations, University of Oxford, 2 February 2007", "Adran Gwleidyddiaeth a Chysylltiadau Rhyngwladol, Prifysgol Rhydychen, 2 Chwefror 2007"),
        note=("£2m from the National Assembly for Wales: £1.5m for the Aberfan Memorial Charity and £500,000 for the Aberfan Education Charity.",
              "£2m gan Gynulliad Cenedlaethol Cymru: £1.5m i Elusen Goffa Aberfan a £500,000 i Elusen Addysg Aberfan."),
        url="https://politics.ox.ac.uk/news/iain-mclean-campaigner-aberfan-community-welcomes-funding-announcment", lang="en"),
    "aberfan-cadw": dict(
        short=("Cadw", "Cadw"),
        t="Aberfan: Cemetery, Garden of Remembrance and Former Tip and Slide Area", by=("Cadw, Register of Parks and Gardens of Special Historic Interest in Wales, grade II*", "Cadw, Cofrestr Parciau a Gerddi o Ddiddordeb Hanesyddol Arbennig yng Nghymru, gradd II*"),
        note=("Low walls of water-worn stone trace the plan of the school in the garden; in the cemetery two long rows of linked white arches mark the graves of 106 of the 144.",
              "Mae waliau isel o gerrig afon yn dilyn cynllun yr ysgol yn yr ardd; yn y fynwent mae dwy res hir o fwâu gwyn ynghlwm yn nodi beddau 106 o’r 144."),
        url="https://cadwpublic-api.azurewebsites.net/reports/parkgarden/FullReport?id=256", lang="en"),
    "aberfan-merthyr-60": dict(
        short=("Merthyr Tydfil council", "Cyngor Merthyr Tudful"),
        t="60th anniversary of the Aberfan disaster: commemorative events", by=("Merthyr Tydfil County Borough Council, 2026", "Cyngor Bwrdeistref Sirol Merthyr Tudful, 2026"),
        note=("The annual memorial service at Aberfan Cemetery at 9.15 on 21 October 2026, and the commemoration at the Memorial Garden.",
              "Y gwasanaeth coffa blynyddol ym Mynwent Aberfan am 9.15 ar 21 Hydref 2026, a’r coffâd yn yr Ardd Goffa."),
        url="https://www.merthyr.gov.uk/resident/60th-anniversary-of-the-aberfan-disaster/commemorative-events/", lang="en"),
    "aberfan-pa-60": dict(
        short=("PA report, 2026", "Adroddiad PA, 2026"),
        t="‘Aberfan will always be in our hearts’, King tells survivors and families", by=("Press Association, in the Irish News, 21 October 2026", "Press Association, yn yr Irish News, 21 Hydref 2026"),
        note=("The King, the Queen and the Prince of Wales at the memorial garden; “We have heard stories of heartbreak, but also of heroism”; the Memorial Tree at Ynysowen school with its clock at 9.13.",
              "Y Brenin, y Frenhines a Thywysog Cymru yn yr ardd goffa; “Rydym wedi clywed straeon am dorcalon, ond hefyd am arwriaeth”; y Goeden Goffa yn ysgol Ynysowen a’i chloc ar 9.13."),
        url="https://www.irishnews.com/news/uk/aberfan-will-always-be-in-our-hearts-king-tells-survivors-and-families-YXIEXH22O5NHFHVJZ5OHF3N77M/", lang="en"),
    # ---------- MAC and the Free Wales Army (story-mac.html, story-fwa.html, src/mac.py) ----------
    "nlw-tryweryn": dict(
        short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"),
        t="Tryweryn",
        by=("National Library of Wales, learning resources", "Llyfrgell Genedlaethol Cymru, adnoddau dysgu"),
        note=("The bill passed on 31 July 1957 with only one Welsh MP voting for it; the villagers marched through Liverpool on 21 November 1956; Llyn Celyn was opened on 21 October 1965.",
              "Pasiwyd y mesur ar 31 Gorffennaf 1957 gyda dim ond un AS o Gymru yn pleidleisio drosto; gorymdeithiodd y pentrefwyr drwy Lerpwl ar 21 Tachwedd 1956; agorwyd Llyn Celyn ar 21 Hydref 1965."),
        url="https://www.llyfrgell.cymru/darganfod-dysgu/addysg/adnoddau-dysgu/tryweryn"),
    "mac-wiki": dict(
        short=("Wikipedia: MAC", "Wikipedia: MAC"),
        t="Mudiad Amddiffyn Cymru",
        by=("Wikipedia, drawing on John Humphries, Freedom Fighters (2008), and Wyn Thomas’s interviews", "Wikipedia, ar sail Freedom Fighters John Humphries (2008) a chyfweliadau Wyn Thomas"),
        note=("MAC’s campaign date by date: Tryweryn and Gellilydan in 1963, Clywedog, the pipelines, the investiture targets, Abergele, the arrests and the trial at Mold.",
              "Ymgyrch MAC fesul dyddiad: Tryweryn a Gellilydan yn 1963, Clywedog, y pibellau, targedau’r Arwisgo, Abergele, yr arestio a’r achos yn yr Wyddgrug."),
        url="https://en.wikipedia.org/wiki/Mudiad_Amddiffyn_Cymru", lang="en"),
    "jenkins-wiki": dict(
        short=("Wikipedia: John Jenkins", "Wikipedia: John Jenkins"),
        t="John Barnard Jenkins",
        by=("Wikipedia, drawing mainly on Wyn Thomas, John Jenkins: The Reluctant Revolutionary? (Y Lolfa, 2019)", "Wikipedia, ar sail John Jenkins: The Reluctant Revolutionary? gan Wyn Thomas (Y Lolfa, 2019) yn bennaf"),
        note=("His life from Cardiff and Penybryn to the army, his reasons, the campaign, the trial, prison and his death in 2020, with his own words to the police and to Wyn Thomas.",
              "Ei fywyd o Gaerdydd a Phen-y-bryn i’r fyddin, ei resymau, yr ymgyrch, yr achos, y carchar a’i farw yn 2020, gyda’i eiriau ei hun wrth yr heddlu ac wrth Wyn Thomas."),
        url="https://en.wikipedia.org/wiki/John_Barnard_Jenkins", lang="en"),
    "temple-wcia": dict(
        short=("WCIA", "WCIA"),
        t="The Bombing of Wales’ Temple of Peace, November 1967",
        by=("Welsh Centre for International Affairs, Cardiff", "Canolfan Materion Rhyngwladol Cymru, Caerdydd"),
        note=("The bomb in the early hours of 17 November 1967, on the day civil servants were to meet there to plan the investiture, and the appeal that restored the building.",
              "Y bom yn oriau mân 17 Tachwedd 1967, ar y diwrnod yr oedd gweision sifil i gwrdd yno i gynllunio’r Arwisgo, a’r apêl a adferodd yr adeilad."),
        url="https://www.wcia.org.uk/?p=45986", lang="en"),
    "post-abergele": dict(
        short=("Daily Post, 2017", "Daily Post, 2017"),
        t="The ‘Abergele Martyrs’ killed in bomb explosion",
        by=("Daily Post, north Wales", "Daily Post, gogledd Cymru"),
        note=("Alwyn Jones, 22, a labourer, and George Taylor, 37, a painter, both council workers; the inquest verdict of accidental death; George Taylor’s family’s doubts.",
              "Alwyn Jones, 22, labrwr, a George Taylor, 37, paentiwr, y ddau’n gweithio i’r cyngor; dyfarniad y cwest mai damwain oedd hi; amheuon teulu George Taylor."),
        url="https://www.dailypost.co.uk/news/north-wales-news/abergele-martyrs-killed-bomb-explosion-14852293", lang="en"),
    "post-plots": dict(
        short=("Daily Post, 2019", "Daily Post, 2019"),
        t="The bizarre plots to stop Prince Charles’s investiture",
        by=("Daily Post, north Wales, for the fiftieth anniversary", "Daily Post, gogledd Cymru, ar yr hanner canmlwyddiant"),
        note=("MAC’s bombs on investiture day, Ian Cox, John Jenkins’s words that the bombs were ‘never planted or timed to hurt people’, and the Free Wales Army’s publicity, march at Machynlleth and 53-day trial.",
              "Bomiau MAC ar ddydd yr Arwisgo, Ian Cox, geiriau John Jenkins na chafodd y bomiau ‘erioed eu gosod na’u hamseru i niweidio pobl’, a chyhoeddusrwydd Byddin Rhyddid Cymru, ei gorymdaith ym Machynlleth a’i hachos 53 diwrnod."),
        url="https://dailypost.co.uk/news/north-wales-news/bizarre-plots-stop-prince-charles-16497777", lang="en"),
    "post-parade-2009": dict(
        short=("Daily Post, 2009", "Daily Post, 2009"),
        t="Parade to commemorate Abergele Martyrs",
        by=("Daily Post, north Wales", "Daily Post, gogledd Cymru"),
        note=("The parade on the fortieth anniversary, and the yearly gatherings at Abergele from 1970 to 1999.",
              "Yr orymdaith ar y deugeinfed pen-blwydd, a’r cynulliadau blynyddol yn Abergele o 1970 hyd 1999."),
        url="https://www.dailypost.co.uk/news/north-wales-news/parade-commemorate-abergele-martyrs-2787304", lang="en"),
    "vittle-review": dict(
        short=("Arwel Vittle, 2023", "Arwel Vittle, 2023"),
        t="Charles and the Welsh Revolt",
        by=("Arwel Vittle, Y Lolfa, 2023; the link is Nation.Cymru’s review", "Arwel Vittle, Y Lolfa, 2023; adolygiad Nation.Cymru yw’r ddolen"),
        note=("The protests against the investiture, peaceful and violent: John Jenkins’s campaign, Ian Cox, the Free Wales Army’s trial, and the police unit set up at Shrewsbury.",
              "Y protestiadau yn erbyn yr Arwisgo, heddychlon a threisgar: ymgyrch John Jenkins, Ian Cox, achos Byddin Rhyddid Cymru, a’r uned heddlu a sefydlwyd yn Amwythig."),
        url="https://nation.cymru/culture/monday-review-charles-and-the-welsh-revolt-by-arwel-vittle", lang="en"),
    "investiture-wiki": dict(
        short=("Wikipedia: the investiture", "Wikipedia: yr Arwisgo"),
        t="Investiture of Charles, Prince of Wales",
        by=("Wikipedia", "Wikipedia"),
        note=("The ceremony of 1 July 1969, its television audience of about 19 million in Britain, and the protests against it, Dafydd Iwan’s Carlo among them.",
              "Seremoni 1 Gorffennaf 1969, ei chynulleidfa deledu o tua 19 miliwn ym Mhrydain, a’r protestiadau yn ei herbyn, gan gynnwys Carlo Dafydd Iwan."),
        url="https://en.wikipedia.org/wiki/Investiture_of_Charles,_Prince_of_Wales", lang="en"),
    "cayo-dwb": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur Cymreig"),
        t="Cayo-Evans, William Edward Julian (1937–1995), political activist",
        by=("Lyn Ebenezer, Dictionary of Welsh Biography, 2016", "Lyn Ebenezer, Y Bywgraffiadur Cymreig, 2016"),
        note=("His life from Glandenys to Silian: Malaya, the horses, the Free Wales Army from Llyn Celyn in 1965 to the trial of 1969, the government papers of 1999, and how he is remembered.",
              "Ei fywyd o Landenys i Silian: Malaya, y ceffylau, Byddin Rhyddid Cymru o Lyn Celyn yn 1965 hyd achos 1969, papurau’r llywodraeth yn 1999, a sut y’i cofir."),
        url="https://biography.wales/article/s10-CAYO-JUL-1937", url_cy="https://bywgraffiadur.cymru/article/s10-CAYO-JUL-1937"),
    "fwa-wiki": dict(
        short=("Wikipedia: the FWA", "Wikipedia: y FWA"),
        t="Free Wales Army",
        by=("Wikipedia, drawing on Humphries (2008), Wyn Thomas (2019, 2022) and Vittle (2023)", "Wikipedia, ar sail Humphries (2008), Wyn Thomas (2019, 2022) a Vittle (2023)"),
        note=("The badge and uniforms, Dublin in 1966, the arms found near Tregaron, the arrests of 26 February 1969, the trial: six convicted and three cleared, and the pub named after Cayo.",
              "Y bathodyn a’r lifrai, Dulyn yn 1966, yr arfau a gafwyd ger Tregaron, arestio 26 Chwefror 1969, yr achos: chwech yn euog a thri’n rhydd, a’r dafarn a enwyd ar ôl Cayo."),
        url="https://en.wikipedia.org/wiki/Free_Wales_Army", lang="en"),
    "coslett-wiki": dict(
        short=("Wikipedia: Dennis Coslett", "Wikipedia: Dennis Coslett"),
        t="Dennis Coslett",
        by=("Wikipedia, drawing on obituaries in The Independent, The Daily Telegraph and The Times, 2004", "Wikipedia, ar sail ysgrifau coffa yn The Independent, The Daily Telegraph a The Times, 2004"),
        note=("His life from Carmarthen and Llangennech to the Free Wales Army, the trial, his books and his funeral.",
              "Ei fywyd o Gaerfyrddin a Llangennech i Fyddin Rhyddid Cymru, yr achos, ei lyfrau a’i angladd."),
        url="https://en.wikipedia.org/wiki/Dennis_Coslett", lang="en"),
}

MARK = re.compile(r"\[\[cite:([a-z0-9,\- ]+)\]\]")

# where a chip can never go: raw text elements, and inside anything that is itself a link or a control
_TOKEN = re.compile(r"(<(script|style|title|textarea|template)\b.*?</\2\s*>|<!--.*?-->|<[^>]*>)", re.S | re.I)
_OPEN = re.compile(r"<(a|button|summary|option|select|label)[\s>]", re.I)
_CLOSE = re.compile(r"</(a|button|summary|option|select|label)\s*>", re.I)

_n = [0]


def keys(marker_body):
    out = [k.strip() for k in marker_body.split(",") if k.strip()]
    missing = [k for k in out if k not in S]
    if missing:
        raise KeyError(f"cites.py: unknown source {missing} in a [[cite:...]] marker")
    return out


def strip(text):
    """Remove every marker (for titles, descriptions, search, feeds, JSON...)."""
    return MARK.sub("", text) if "[[cite:" in text else text


def chip(ks, cy=False, prefix="cite"):
    """The chip and its card, in one language. Safe to put inside a <p>."""
    e = lambda s: _html.escape(s, quote=True)
    srcs = [S[k] for k in ks]
    first = srcs[0]
    i = 0 if not cy else 1
    _n[0] += 1
    pid = f"{prefix}-{_n[0]}"
    link = next((s.get("url_cy") if cy and s.get("url_cy") else s["url"] for s in srcs if s["url"]), None)
    label = first["short"][i] + (f" +{len(srcs) - 1}" if len(srcs) > 1 else "")
    word = ("Ffynhonnell" if len(srcs) == 1 else "Ffynonellau") if cy else ("Source" if len(srcs) == 1 else "Sources")
    aria = f"{word}: " + "; ".join(s["short"][i] for s in srcs)
    items = ""
    for s in srcs:
        url = (s.get("url_cy") or s["url"]) if cy else s["url"]
        title = f'<a href="{e(url)}" target="_blank" rel="noopener">{e(s["t"])} ↗</a>' if url else f'<i>{e(s["t"])}</i>'
        eng = " (Saesneg)" if cy and s.get("lang") == "en" else ""
        items += (f'<span class="cite-i"><span class="cite-t">{title}</span><span class="cite-by">{e(s["by"][i] if isinstance(s["by"], tuple) else s["by"])}{eng}</span>'
                  f'<span class="cite-n">{e(s["note"][i])}</span></span>')
    tag_open = f'<a class="cite" href="{e(link)}" target="_blank" rel="noopener"' if link else '<a class="cite" href="#"'
    return (f'<span class="cite-w">{tag_open} aria-controls="{pid}" aria-label="{e(aria)}" data-cite>{e(label)}</a>'
            f'<span class="cite-pop" id="{pid}" role="note" hidden><span class="cite-h">{e(word)}</span>{items}'
            f'<button type="button" class="cite-x" aria-label="{"Cau" if cy else "Close"}">×</button></span></span>')


def html_text(text, cy=False):
    """Escape a plain sentence and turn its markers into chips (for HTML that scripts put on the page)."""
    out, pos = [], 0
    for m in MARK.finditer(text):
        out.append(_html.escape(text[pos:m.start()], quote=False))
        out.append(chip(keys(m.group(1)), cy, "citej"))
        pos = m.end()
    out.append(_html.escape(text[pos:], quote=False))
    return "".join(out)


def render(doc, cy=False):
    """Turn markers in a finished page into chips; remove the ones that sit where a chip cannot go."""
    if "[[cite:" not in doc:
        return doc
    _n[0] = 0
    out, pos, depth = [], 0, 0

    def text(t):
        if "[[cite:" not in t:
            return t
        return MARK.sub("", t) if depth else MARK.sub(lambda m: chip(keys(m.group(1)), cy), t)

    for m in _TOKEN.finditer(doc):
        out.append(text(doc[pos:m.start()]))
        tok = m.group(0)
        if tok.startswith("<") and not tok.startswith("</") and _OPEN.match(tok) and not tok.endswith("/>"):
            depth += 1
        elif _CLOSE.match(tok):
            depth = max(0, depth - 1)
        out.append(strip(tok))
        pos = m.end()
    out.append(text(doc[pos:]))
    return "".join(out)


CSS = """
.cite-w { position: relative; display: inline; white-space: nowrap }
.cite { display: inline-block; margin-left: .3em; padding: .05em .5em .1em; border: 1px solid var(--line); border-radius: 999px;
  font-family: var(--f-mono); font-size: .62rem; font-weight: 500; line-height: 1.5; letter-spacing: .02em; vertical-align: .2em;
  color: var(--muted); background: rgba(255,255,255,.03); text-decoration: none; white-space: nowrap; cursor: pointer }
.cite::before { content: "§"; margin-right: .3em; color: var(--dragon) }
.cite:hover, .cite[aria-expanded="true"] { color: var(--ink); border-color: var(--dragon) }
.cite:focus-visible { outline: 2px solid var(--dragon); outline-offset: 2px }
.cite-pop { position: absolute; z-index: 60; left: 0; top: calc(100% + .45rem); width: min(22rem, calc(100vw - 2rem)); white-space: normal;
  display: grid; gap: .7rem; padding: .9rem 2.2rem .95rem 1rem; text-align: left;
  background: var(--slate-2); border: 1px solid var(--line); border-radius: 12px; box-shadow: 0 14px 40px rgba(0,0,0,.45);
  font-family: var(--f-body); font-size: .86rem; line-height: 1.45; font-weight: 400; letter-spacing: 0; word-spacing: 0; color: var(--ink) }
.cite-pop[hidden] { display: none }
.cite-h { font-family: var(--f-mono); font-size: .66rem; text-transform: uppercase; letter-spacing: .1em; color: var(--muted) }
.cite-i { display: grid; gap: .2rem }
.cite-i + .cite-i { padding-top: .7rem; border-top: 1px solid var(--line) }
.cite-t { font-weight: 600 }
.cite-t a { color: var(--ink); text-decoration: underline; text-decoration-color: var(--dragon); text-underline-offset: 3px }
.cite-by { color: var(--muted); font-size: .8rem }
.cite-n { font-size: .84rem }
.cite-x { position: absolute; top: .35rem; right: .4rem; width: 2rem; height: 2rem; border: 0; border-radius: 8px; background: none;
  color: var(--muted); font-size: 1.25rem; line-height: 1; cursor: pointer }
.cite-x:hover { color: var(--ink); background: rgba(255,255,255,.06) }
@media (max-width: 640px) {
  .cite { font-size: .7rem; padding: .28em .7em .32em; vertical-align: .1em }
  .cite-pop { position: fixed; left: .75rem; right: .75rem; top: auto; bottom: .75rem; width: auto; max-height: 70vh; overflow: auto }
}
@media print { .cite-pop { display: none !important } .cite { border: 0; padding: 0 } }
"""
