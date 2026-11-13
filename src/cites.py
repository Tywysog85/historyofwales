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
    # ---------- the Britons in Brittany (story-brittany.html) ----------
    "gildas-giles": dict(
        short=("Gildas", "Gildas"),
        t="On the Ruin of Britain (De Excidio Britanniae), by Gildas", by=("translated by J. A. Giles, Project Gutenberg", "cyfieithiad Saesneg J. A. Giles, Project Gutenberg"),
        note=("Gildas, a pupil of Illtud, writing in the sixth century: chapter 14 on the men who went with Maximus and never returned, chapter 25 on the Britons who sailed beyond the seas.",
              "Gildas, disgybl Illtud, yn ysgrifennu yn y chweched ganrif: pennod 14 am y gwŷr a aeth gyda Maximus ac na ddaethant yn ôl, pennod 25 am y Brythoniaid a hwyliodd dros y moroedd."),
        url="https://www.gutenberg.org/ebooks/1949", lang="en"),
    "jordanes-mierow": dict(
        short=("Jordanes", "Jordanes"),
        t="The Origin and Deeds of the Goths (Getica), by Jordanes, sections 237–238", by=("translated by Charles C. Mierow, 1915; text at the Celtic Literature Collective", "cyfieithiad Saesneg Charles C. Mierow, 1915"),
        note=("Written about 551: Riotimus, king of the Brittones, came with twelve thousand men by way of the Ocean to help the emperor Anthemius against Euric.",
              "Ysgrifennwyd tua 551: daeth Riotimus, brenin y Brythoniaid, â deuddeng mil o wŷr ar hyd y Cefnfor i gynorthwyo’r ymerawdwr Anthemius yn erbyn Euric."),
        url="https://maryjones.us/ctexts/jordanes.html", lang="en"),
    "tours-461": dict(
        short=("Council of Tours, 461", "Cyngor Tours, 461"),
        t="Council of Tours", by=("Wikipedia, from the acts of the council", "Wikipedia, o weithredoedd y cyngor"),
        note=("The last of the eight bishops to sign the canons of 461 was Mansuetus, episcopus Britannorum, bishop of the Britons.",
              "Yr olaf o’r wyth esgob i lofnodi canonau 461 oedd Mansuetus, episcopus Britannorum, esgob y Brythoniaid."),
        url="https://en.wikipedia.org/wiki/Council_of_Tours", lang="en"),
    "riothamus-wiki": dict(
        short=("Riothamus", "Riothamus"),
        t="Riothamus", by=("Wikipedia, with the texts of Jordanes, Sidonius Apollinaris (Letters III.9) and Gregory of Tours (Histories II.18)", "Wikipedia, gyda thestunau Jordanes, Sidonius Apollinaris (Llythyrau III.9) a Gregori o Tours (Hanesion II.18)"),
        note=("The letter of Sidonius to Riothamus, the twelve thousand men, and the Britons driven from Bourges with many killed at Déols.",
              "Llythyr Sidonius at Riothamus, y deuddeng mil o wŷr, a’r Brythoniaid a yrrwyd o Bourges a llawer wedi’u lladd yn Déols."),
        url="https://en.wikipedia.org/wiki/Riothamus", lang="en"),
    "samson-life": dict(
        short=("Life of Samson", "Buchedd Samson"),
        t="Samson of Dol", by=("Wikipedia, from the Life of Samson (written between about 610 and 820)", "Wikipedia, o Fuchedd Samson (a ysgrifennwyd rhwng tua 610 ac 820)"),
        note=("His parents Amon of Dyfed and Anna of Gwent, Illtud’s school, the abbacy of Caldey, Cornwall, Dol, his plea to Childebert for Iudual, and the council in Paris.",
              "Ei rieni, Amon o Ddyfed ac Anna o Went, ysgol Illtud, abadaeth Ynys Bŷr, Cernyw, Dol, ei ble at Childebert dros Iudual, a’r cyngor ym Mharis."),
        url="https://en.wikipedia.org/wiki/Samson_of_Dol", lang="en"),
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

    # ---------- Tryweryn and Capel Celyn (story-tryweryn.html) ----------
    "hansard-tryweryn": dict(
        short=("Hansard, 1957", "Hansard, 1957"),
        t="Liverpool Corporation Bill [Lords] (By Order), House of Commons, 3 July 1957", by=("Hansard, Parliamentary Debates, volume 572", "Hansard, Dadleuon Seneddol, cyfrol 572"),
        note=("T. W. Jones, member for Merioneth, moves that the House “declines to give a Second Reading to a Bill which proposes to uproot an entire community”, and says the people of Wales have never felt so intense on any subject this century.",
              "Mae T. W. Jones, aelod Meirionnydd, yn cynnig bod y Tŷ yn gwrthod rhoi Ail Ddarlleniad i fesur sy’n bwriadu diwreiddio cymuned gyfan, ac yn dweud na fu pobl Cymru erioed yn teimlo mor gryf am unrhyw bwnc yn y ganrif hon."),
        url="https://api.parliament.uk/historic-hansard/commons/1957/jul/03/liverpool-corporation-bill-lords-by-order", lang="en"),
    "nlw-tryweryn": dict(
        short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"),
        t="Tryweryn: learning resource", by=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"),
        note=("The Library’s timeline of the drowning: the Liverpool Daily Post of 22 December 1955, the march through Liverpool on 21 November 1956 and the council’s vote of 95 to 1, the third reading on 31 July 1957 by a majority of 96, the work begun on 2 August 1960, the chapel taken down in June 1964, the opening on 21 October 1965, and the vote of 1997.",
              "Llinell amser y Llyfrgell o’r boddi: Liverpool Daily Post 22 Rhagfyr 1955, yr orymdaith drwy Lerpwl ar 21 Tachwedd 1956 a phleidlais y cyngor o 95 i 1, y trydydd darlleniad ar 31 Gorffennaf 1957 o fwyafrif o 96, dechrau’r gwaith ar 2 Awst 1960, tynnu’r capel i lawr ym Mehefin 1964, yr agoriad ar 21 Hydref 1965, a phleidlais 1997."),
        url="https://www.library.wales/discover-learn/education/learning-resources/tryweryn", lang="en"),
    "dwb-watkin-jones": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"),
        t="Jones (Mrowiec), Elizabeth May Watkin (1907–1965), teacher and campaigner", by=("Ffion Mair Jones, Dictionary of Welsh Biography, 2022", "Ffion Mair Jones, Y Bywgraffiadur Cymreig, 2022"),
        note=("Teacher at Capel Celyn school and secretary of the Capel Celyn Defence Committee, formed on 23 March 1956 with Dafydd Roberts as chairman; her letters, meetings and television appearances; the march through Liverpool led by Gwynfor Evans on 21 November 1956; her death on 21 June 1965.",
              "Athrawes yn ysgol Capel Celyn ac ysgrifennydd Pwyllgor Amddiffyn Capel Celyn, a ffurfiwyd ar 23 Mawrth 1956 gyda Dafydd Roberts yn gadeirydd; ei llythyrau, ei chyfarfodydd a’i hymddangosiadau ar y teledu; yr orymdaith drwy Lerpwl dan arweiniad Gwynfor Evans ar 21 Tachwedd 1956; ei marw ar 21 Mehefin 1965."),
        url="https://biography.wales/article/s14-JONE-WAT-1907", url_cy="https://bywgraffiadur.cymru/article/s14-JONE-WAT-1907"),
    "dwb-dafydd-roberts": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"),
        t="Roberts, Dafydd (1892–1965), chairman of Capel Celyn Defence Committee", by=("John Lewis Jones, Dictionary of Welsh Biography, 2001", "John Lewis Jones, Y Bywgraffiadur Cymreig, 2001"),
        note=("Born at Weirglodd-ddu, later farmed Cae Fadog; a postman for more than forty years and a chapel elder; chairman of the Defence Committee to the end; died 11 October 1965, shortly before the opening of the reservoir, and buried at Llanycil.",
              "Ganed yn Weirglodd-ddu, ffermiodd Gae Fadog yn ddiweddarach; postmon am fwy na deugain mlynedd a blaenor; cadeirydd y Pwyllgor Amddiffyn hyd y diwedd; bu farw 11 Hydref 1965, ychydig cyn agor y gronfa, a’i gladdu yn Llanycil."),
        url="https://biography.wales/article/s2-ROBE-DAF-1892", url_cy="https://bywgraffiadur.cymru/article/s2-ROBE-DAF-1892"),
    "bbc-tryweryn-2005": dict(
        short=("BBC News, 2005", "BBC News, 2005"),
        t="Official apology over Tryweryn", by=("BBC News, 19 October 2005", "BBC News, 19 Hydref 2005"),
        note=("Liverpool City Council votes unanimously for the apology, quoted in full; the First Minister Rhodri Morgan welcomes it, and Elfyn Llwyd says it should be accepted in the way it is offered.",
              "Mae Cyngor Dinas Lerpwl yn pleidleisio’n unfrydol dros yr ymddiheuriad, a ddyfynnir yn llawn; mae’r Prif Weinidog Rhodri Morgan yn ei groesawu, a dywed Elfyn Llwyd y dylid ei dderbyn yn y ffordd y’i cynigir."),
        url="https://news.bbc.co.uk/2/hi/uk_news/wales/4354256.stm", lang="en"),
    "bbc-tryweryn-roderick": dict(
        short=("BBC News, 2005", "BBC News, 2005"),
        t="City’s apology for drowned valley", by=("BBC News, 11 October 2005, with Vaughan Roderick", "BBC News, 11 Hydref 2005, gyda Vaughan Roderick"),
        note=("Mike Storey: “What happened to the people in the valleys was wrong and I think now is the right time to say sorry.” Vaughan Roderick: “It would not be an exaggeration to say that the road to the National Assembly for Wales began in Tryweryn.”",
              "Mike Storey: roedd yr hyn a ddigwyddodd i bobl y cymoedd yn anghywir, a nawr yw’r amser i ddweud sori. Vaughan Roderick: ni fyddai’n gor-ddweud mai yn Nhryweryn y dechreuodd y ffordd i Gynulliad Cenedlaethol Cymru."),
        url="https://news.bbc.co.uk/2/hi/uk_news/wales/4331812.stm", lang="en"),
    "pcw-cofiwch": dict(
        short=("People’s Collection Wales", "Casgliad y Werin"),
        t="Cofiwch Dryweryn: one hundred and counting!", by=("People’s Collection Wales", "Casgliad y Werin Cymru"),
        note=("Meic Stephens painted the first Cofiwch Dryweryn at Llanrhystud; after the wall was attacked in 2019, more than a hundred new murals were painted across Wales.",
              "Meic Stephens a baentiodd y Cofiwch Dryweryn cyntaf yn Llanrhystud; wedi i’r wal gael ei difrodi yn 2019, paentiwyd mwy na chant o furluniau newydd ledled Cymru."),
        url="https://www.peoplescollection.wales/blogs/cofiwch-dryweryn-%E2%80%93-one-hundred-and-counting", lang="en"),

    # ---------- How Wales moved the world: the industrial revolution (src/industry.py) ----------
    "unesco-blaenavon": dict(
        short=('UNESCO', 'UNESCO'),
        t='Blaenavon Industrial Landscape', by=('UNESCO World Heritage List, inscribed 2000', 'Rhestr Treftadaeth y Byd UNESCO, 2000'),
        note=('It shows “the pre-eminence of South Wales as the world’s major producer of iron and coal in the 19th century”.',
              'Mae’n dangos mai de Cymru oedd prif gynhyrchydd haearn a glo y byd yn y 19eg ganrif.'),
        url='https://whc.unesco.org/en/list/984', lang='en'),
    "guinness-loco": dict(
        short=('Guinness World Records', 'Guinness World Records'),
        t='First steam locomotive to run on rails', by=('Guinness World Records', 'Guinness World Records'),
        note=('The first steam locomotive to run on rails was Richard Trevithick’s, built at the Penydarren ironworks, Merthyr Tydfil; it first ran on 21 February 1804.',
              'Injan Richard Trevithick, a adeiladwyd yng ngwaith haearn Penydarren, Merthyr Tudful, oedd yr injan stêm gyntaf i redeg ar gledrau; rhedodd gyntaf ar 21 Chwefror 1804.'),
        url='https://www.guinnessworldrecords.com/world-records/454107-first-steam-locomotive-to-run-on-rails', lang='en'),
    "graces-penydarren": dict(
        short=('Grace’s Guide', 'Grace’s Guide'),
        t='Richard Trevithick: Merthyr Tramroad Trial', by=('Grace’s Guide to British Industrial History', 'Grace’s Guide, hanes diwydiannol Prydain'),
        note=('Homfray bet Crawshay 500 guineas; on 21 February 1804 the engine took 10 tons of iron in five wagons and 70 men the 9¾ miles from Penydarren to Abercynon in 4 hours 5 minutes.',
              'Rhoddodd Homfray fet o 500 gini â Crawshay; ar 21 Chwefror 1804 cariodd yr injan 10 tunnell o haearn mewn pum wagen a 70 o ddynion y 9¾ milltir o Benydarren i Abercynon mewn 4 awr a 5 munud.'),
        url='https://gracesguide.co.uk/Richard_Trevithick:_Merthyr_Tramroad_Trial', lang='en'),
    "tfw-trevithick": dict(
        short=('Transport for Wales', 'Trafnidiaeth Cymru'),
        t='Richard Trevithick', by=('Transport for Wales, Railway 200', 'Trafnidiaeth Cymru, Rheilffordd 200'),
        note=('Trevithick’s locomotive, built for Samuel Homfray, hauled 10 tonnes of iron the nine miles from Penydarren to Abercynon on 21 February 1804.',
              'Tynnodd injan Trevithick, a adeiladwyd i Samuel Homfray, 10 tunnell o haearn y naw milltir o Benydarren i Abercynon ar 21 Chwefror 1804.'),
        url='https://tfw.wales/railway-200/richard-trevithick', lang='en'),
    "guinness-mumbles": dict(
        short=('Guinness World Records', 'Guinness World Records'),
        t='First regular passenger railway service', by=('Guinness World Records', 'Guinness World Records'),
        note=('The first regular passenger railway service began on the Oystermouth Railway, Swansea, on 25 March 1807, run by Benjamin French for £20 a year.',
              'Dechreuodd y gwasanaeth teithwyr rheolaidd cyntaf ar reilffordd ar Reilffordd Ystumllwynarth, Abertawe, ar 25 Mawrth 1807, dan ofal Benjamin French am £20 y flwyddyn.'),
        url='https://www.guinnessworldrecords.com/world-records/114288-first-regular-passenger-railway-service', lang='en'),
    "cadw-dowlais": dict(
        short=('Cadw landscape survey', 'Arolwg tirwedd Cadw'),
        t='Merthyr Tydfil historic landscape: Dowlais', by=('Historic landscape characterisation for Cadw (Glamorgan-Gwent Archaeological Trust, now Heneb)', 'Nodweddu tirwedd hanesyddol i Cadw (Ymddiriedolaeth Archaeolegol Morgannwg-Gwent, Heneb bellach)'),
        note=('Dowlais became “the largest ironworks in the world” in the 19th century; the rails for the Stockton and Darlington Railway were made there in 1821.',
              'Daeth Dowlais yn waith haearn mwyaf y byd yn y bedwaredd ganrif ar bymtheg; yno y gwnaed cledrau Rheilffordd Stockton a Darlington yn 1821.'),
        url='https://heneb.org.uk/archive/ggat/cadw/historic_landscape/Merthyr_Tydfil/English/Merthyr_008.htm', lang='en'),
    "graces-dowlais": dict(
        short=('Grace’s Guide', 'Grace’s Guide'),
        t='Dowlais Ironworks', by=('Grace’s Guide to British Industrial History', 'Grace’s Guide, hanes diwydiannol Prydain'),
        note=('In 1845 the works had 18 furnaces and 7,300 workers and made about 89,000 tons of iron a year; Lady Charlotte Guest helped run it.',
              'Yn 1845 roedd gan y gwaith 18 ffwrnais a 7,300 o weithwyr a gwnâi tua 89,000 tunnell o haearn y flwyddyn; helpodd yr Arglwyddes Charlotte Guest i’w redeg.'),
        url='https://www.gracesguide.co.uk/Dowlais_Ironworks', lang='en'),
    "wiki-dowlais": dict(
        short=('Wikipedia', 'Wikipedia'),
        t='Dowlais Ironworks', by=('Wikipedia, with its sources', 'Wikipedia, gyda’i ffynonellau'),
        note=('Foreign orders in 1835–36 included rails for the Berlin and Leipzig Railway and the St Petersburg line; Dowlais was the first to license the Bessemer process and made steel from 1865.',
              'Roedd archebion tramor 1835–36 yn cynnwys cledrau i Reilffordd Berlin a Leipzig a lein St Petersburg; Dowlais oedd y cyntaf i gymryd trwydded proses Bessemer a gwnâi ddur o 1865.'),
        url='https://en.wikipedia.org/wiki/Dowlais_Ironworks', lang='en'),
    "wiki-cyfarthfa": dict(
        short=('Wikipedia', 'Wikipedia'),
        t='Cyfarthfa Ironworks', by=('Wikipedia, with its sources', 'Wikipedia, gyda’i ffynonellau'),
        note=('Cyfarthfa made cannon for the Board of Ordnance; Nelson visited in 1802, and its iron rails drew a representative from the Tsar of Russia.',
              'Gwnâi Cyfarthfa ynnau mawr i’r Bwrdd Ordnans; ymwelodd Nelson yn 1802, a denodd ei gledrau haearn gynrychiolydd Tsar Rwsia.'),
        url='https://en.wikipedia.org/wiki/Cyfarthfa_Ironworks', lang='en'),
    "wiki-gilchrist": dict(
        short=('Wikipedia', 'Wikipedia'),
        t='Sidney Gilchrist Thomas', by=('Wikipedia, with its sources', 'Wikipedia, gyda’i ffynonellau'),
        note=('His cousin Percy Gilchrist, chemist at Blaenavon, proved the method; it was announced in 1878 and was “especially valuable on the continent of Europe”.',
              'Profodd ei gefnder Percy Gilchrist, cemegydd ym Mlaenafon, y dull; fe’i cyhoeddwyd yn 1878 ac roedd yn arbennig o werthfawr ar gyfandir Ewrop.'),
        url='https://en.wikipedia.org/wiki/Sidney_Gilchrist_Thomas', lang='en'),
    "wiki-glamcanal": dict(
        short=('Wikipedia', 'Wikipedia'),
        t='Glamorganshire Canal', by=('Wikipedia, with its sources', 'Wikipedia, gyda’i ffynonellau'),
        note=('Opened to Cardiff on 10 February 1794, about 25 miles with some 50 locks; the sea lock opened in June 1798 with a naval procession and ships’ guns.',
              'Agorodd i Gaerdydd ar 10 Chwefror 1794, tua 25 milltir gyda rhyw 50 o lociau; agorodd y loc môr ym mis Mehefin 1798 gyda gorymdaith lyngesol a gynnau llongau.'),
        url='https://en.wikipedia.org/wiki/Glamorganshire_Canal', lang='en'),
    "unesco-pontcysyllte": dict(
        short=('UNESCO', 'UNESCO'),
        t='Pontcysyllte Aqueduct and Canal', by=('UNESCO World Heritage List, inscribed 2009', 'Rhestr Treftadaeth y Byd UNESCO, 2009'),
        note=('Telford’s aqueduct is “a pioneering masterpiece of engineering”.',
              'Mae traphont ddŵr Telford yn gampwaith peirianneg arloesol.'),
        url='https://whc.unesco.org/en/list/1303', lang='en'),
    "museum-cardiff": dict(
        short=('Amgueddfa Cymru', 'Amgueddfa Cymru'),
        t='Cardiff: Coal and Shipping Metropolis of the World', by=('Amgueddfa Cymru, National Museum Wales', 'Amgueddfa Cymru'),
        note=('Cardiff exported about 2 million tons of coal in 1862 and 10.7 million in 1913; before 1914 its cargo tonnage “outstripped that of either London or Liverpool”; about 250 tramp steamers were owned there in 1910.',
              'Allforiodd Caerdydd tua 2 filiwn tunnell o lo yn 1862 a 10.7 miliwn yn 1913; cyn 1914 roedd ei thunelledd cargo yn fwy na Llundain neu Lerpwl; roedd tua 250 o longau tramp yn eiddo iddi yn 1910.'),
        url='https://museum.wales/articles/1034/Cardiff--Coal-and-Shipping-Metropolis-of-the-World', lang='en'),
    "agor-coal": dict(
        short=('AGOR timeline', 'Llinell amser AGOR'),
        t='South Wales Coalfield timeline', by=('AGOR, the South Wales Coalfield collection', 'AGOR, casgliad Maes Glo De Cymru'),
        note=('1840: the first cargo of coal shipped abroad, Cardiff to Nantes. 1851: an Admiralty report finds south Wales steam coal most suitable for the Royal Navy. 1855: the first train of Rhondda steam coal reaches Cardiff.',
              '1840: y llwyth glo cyntaf i fynd dramor, Caerdydd i Nantes. 1851: adroddiad i’r Morlys yn barnu mai glo ager de Cymru yw’r mwyaf addas i’r Llynges Frenhinol. 1855: y trên cyntaf o lo ager y Rhondda yn cyrraedd Caerdydd.'),
        url='https://www.agor.org.uk/cwm/timeline.asp', lang='en'),
    "vicsoc-exchange": dict(
        short=('Victorian Society', 'Y Gymdeithas Fictoraidd'),
        t='Cardiff Coal Exchange', by=('The Victorian Society, Top Ten Endangered Buildings', 'Y Gymdeithas Fictoraidd, y deg adeilad mwyaf mewn perygl'),
        note=('Built in 1884–86 by Seward and Thomas, Grade II* listed; the world’s coal prices were set there, and the first £1 million cheque was signed there in 1904.',
              'Codwyd yn 1884–86 gan Seward a Thomas, rhestredig Gradd II*; yno y pennid prisiau glo’r byd, ac yno y llofnodwyd y siec £1 miliwn gyntaf yn 1904.'),
        url='https://www.victoriansociety.org.uk/endangered-buildings/cardiff-coal-exchange-on-victorian-societys-top-ten-endangered-buildings-list-for-the-second-time/', lang='en'),
    "pcw-cheque": dict(
        short=('People’s Collection Wales', 'Casgliad y Werin'),
        t='The Coal Exchange, Cardiff', by=('People’s Collection Wales', 'Casgliad y Werin Cymru'),
        note=('Records the world’s first recorded £1m cheque, written at the Coal Exchange in 1904 to sign a deal.',
              'Yn cofnodi siec £1m gyntaf y byd i’w chofnodi, a ysgrifennwyd yn y Gyfnewidfa Lo yn 1904 i selio bargen.'),
        url='https://www.peoplescollection.wales/items/546926', lang='en'),
    "cbh-cheque": dict(
        short=('Cardiff Bay Heritage', 'Treftadaeth Bae Caerdydd'),
        t='Commerce', by=('Cardiff Bay Heritage', 'Treftadaeth Bae Caerdydd'),
        note=('The Coal Exchange, “the hub for trade in coal”, opened in 1888; the first £1m cheque “was written here in 1904”.',
              'Agorodd y Gyfnewidfa Lo, canolbwynt y fasnach lo, yn 1888; ysgrifennwyd y siec £1m gyntaf yma yn 1904.'),
        url='https://cardiffbayheritage.org.uk/en/commerce', lang='en'),
    "wiki-exchange": dict(
        short=('Wikipedia', 'Wikipedia'),
        t='Coal Exchange', by=('Wikipedia, with its sources', 'Wikipedia, gyda’i ffynonellau'),
        note=('“At one time the price of the world’s coal was determined here”; up to 200 men on the floor at the midday peak and some 10,000 people a day; the first £1,000,000 deal was agreed here in 1904.',
              'Ar un adeg pennid pris glo’r byd yma; hyd at 200 o ddynion ar y llawr yn yr awr brysuraf a rhyw 10,000 o bobl y dydd; cytunwyd y fargen £1,000,000 gyntaf yma yn 1904.'),
        url='https://en.wikipedia.org/wiki/Coal_Exchange', lang='en'),
    "bbc-exchange": dict(
        short=('BBC Wales History', 'Hanes Cymru y BBC'),
        t='Cardiff Coal Exchange: economic centre to entertainment venue', by=('Phil Carradice, BBC Wales History blog, 2012', 'Phil Carradice, blog Hanes Cymru y BBC, 2012'),
        note=('Opened on 1 February 1886; this telling dates the first £1 million deal to 1901.',
              'Agorwyd ar 1 Chwefror 1886; mae’r fersiwn hwn yn dyddio’r fargen £1 miliwn gyntaf i 1901.'),
        url='https://www.bbc.co.uk/blogs/waleshistory/2012/01/cardiff_coal_exchange_economic_centre_entertainment_venue.html', lang='en'),
    "wiki-barry": dict(
        short=('Wikipedia', 'Wikipedia'),
        t='Barry Docks', by=('Wikipedia, citing W. Minchinton (2013) and others', 'Wikipedia, yn dyfynnu W. Minchinton (2013) ac eraill'),
        note=('Water first admitted 29 June 1889, opened 18 July 1889, promoted by David Davies and John Cory; in 1913 Barry exported 11.05 million tons and was the busiest coal port in the world, ahead of Cardiff’s 10.6 million.',
              'Daeth y dŵr i mewn gyntaf 29 Mehefin 1889, agorwyd 18 Gorffennaf 1889, dan arweiniad David Davies a John Cory; yn 1913 allforiodd y Barri 11.05 miliwn tunnell a hi oedd porthladd glo prysuraf y byd, o flaen 10.6 miliwn Caerdydd.'),
        url='https://en.wikipedia.org/wiki/Barry_Docks', lang='en'),
    "port-fuelling": dict(
        short=('University of Portsmouth', 'Prifysgol Portsmouth'),
        t='Fuelling mobility: coal and Britain’s naval power, c. 1870–1914', by=('Research paper, University of Portsmouth', 'Papur ymchwil, Prifysgol Portsmouth'),
        note=('Welsh steam coal was “universally agreed to be of the highest quality for steam engines”; the Admiralty kept a list of approved collieries from the 1840s, with a naval captain at Cardiff; in 1889 the First Lord called Welsh coal the only home fuel fit for the navy; Welsh merchants traded with foreign navies in peacetime.',
              'Cytunid yn gyffredinol mai glo ager Cymru oedd o’r ansawdd gorau i injans stêm; cadwai’r Morlys restr o lofeydd o’r 1840au, gyda chapten llynges yng Nghaerdydd; yn 1889 galwodd yr Arglwydd Cyntaf lo Cymru yr unig danwydd cartref addas i’r llynges; masnachai masnachwyr Cymru â llyngesau tramor adeg heddwch.'),
        url='https://pure.port.ac.uk/ws/portalfiles/portal/7282023/Fuelling_mobility.pdf', lang='en'),
    "museum-maritime": dict(
        short=('Amgueddfa Cymru', 'Amgueddfa Cymru'),
        t='Wales, a modern maritime nation', by=('Amgueddfa Cymru, National Museum Wales', 'Amgueddfa Cymru'),
        note=('South Wales steam coal had the place oil has today; ships that burned it no longer depended on the wind and arrived sooner and more reliably.',
              'Roedd gan lo ager y de y lle sydd gan olew heddiw; nid oedd llongau a’i llosgai yn dibynnu ar y gwynt mwyach, a chyrhaeddent yn gynt ac yn fwy dibynadwy.'),
        url='https://museum.wales/blog/1063/Wales--a-modern-maritime-nation/', lang='en'),
    "museum-antarctic": dict(
        short=('Amgueddfa Cymru', 'Amgueddfa Cymru'),
        t='Fuelling Antarctic exploration: The Crown Patent Fuel Company in Cardiff', by=('Amgueddfa Cymru, National Museum Wales', 'Amgueddfa Cymru'),
        note=('Scott made Cardiff the Terra Nova’s home port; the Crown Patent Fuel Company gave 300 tons of fuel blocks and south Wales coal companies 100 tons of steam coal.',
              'Gwnaeth Scott Gaerdydd yn borthladd cartref y Terra Nova; rhoddodd Cwmni Crown Patent Fuel 300 tunnell o flociau tanwydd a chwmnïau glo’r de 100 tunnell o lo ager.'),
        url='https://museum.wales/articles/1133/Fuelling-Antarctic-exploration-The-Crown-Patent-Fuel-Company-in-Cardiff', lang='en'),
    "swansea-copper": dict(
        short=('Swansea Council', 'Cyngor Abertawe'),
        t='Lower Swansea Valley', by=('City and County of Swansea', 'Dinas a Sir Abertawe'),
        note=('In the 19th century Swansea was the world’s leading centre for smelting copper ore, and smelted about 90% of the UK’s copper.',
              'Yn y bedwaredd ganrif ar bymtheg Abertawe oedd prif ganolfan toddi mwyn copr y byd, a thoddai tua 90% o gopr y Deyrnas Unedig.'),
        url='https://www.swansea.gov.uk/lowerswanseavalley', lang='en'),
    "ref-copperopolis": dict(
        short=('Swansea University', 'Prifysgol Abertawe'),
        t='Copperopolis: Regenerating and Transforming an Industrial Landscape in the Lower Swansea Valley', by=('Swansea University, REF impact case study', 'Prifysgol Abertawe, astudiaeth achos REF'),
        note=('The Lower Swansea Valley was a world centre for copper smelting by the end of the 1700s, and Swansea led the world until the 1870s; the Hafod works was built in 1810.',
              'Roedd Cwm Tawe Isaf yn ganolfan toddi copr byd-eang erbyn diwedd y 1700au, ac Abertawe ar flaen y byd hyd y 1870au; codwyd gwaith yr Hafod yn 1810.'),
        url='https://impact.ref.ac.uk/casestudies/CaseStudy.aspx?Id=5913', lang='en'),
    "vsb-hafod": dict(
        short=('Visit Swansea Bay', 'Croeso Bae Abertawe'),
        t='Hafod Copperworks', by=('Visit Swansea Bay', 'Croeso Bae Abertawe'),
        note=('The Hafod works, run by the Vivians from 1810 to 1924, was perhaps the largest and most up-to-date copperworks in the world; ore came from Cornwall, then Chile and Australia, and Captain David Morgan brought ore from Chile.',
              'Gwaith yr Hafod, dan y Vivianiaid o 1810 hyd 1924, oedd efallai’r gwaith copr mwyaf a mwyaf modern yn y byd; deuai mwyn o Gernyw, yna Chile ac Awstralia.'),
        url='https://www.visitswanseabay.com/blog/post/discover-with-jo-hafod-copperworks/', lang='en'),
    "wiki-slate": dict(
        short=('Wikipedia', 'Wikipedia'),
        t='Slate industry in Wales', by=('Wikipedia, with its sources', 'Wikipedia, gyda’i ffynonellau'),
        note=('Output peaked at over half a million tons in 1898 with about 17,000 men; Penrhyn and Dinorwig were the two largest slate quarries in the world and the Oakeley the largest slate mine; Germany became a market after the Hamburg fire of 1842; Porthmadog built 201 ships between 1836 and 1880.',
              'Cyrhaeddodd y cynnyrch dros hanner miliwn tunnell yn 1898 gyda thua 17,000 o ddynion; Penrhyn a Dinorwig oedd dwy chwarel lechi fwyaf y byd a’r Oakeley y gloddfa lechi fwyaf; daeth yr Almaen yn farchnad wedi tân Hamburg yn 1842; adeiladodd Porthmadog 201 o longau rhwng 1836 a 1880.'),
        url='https://en.wikipedia.org/wiki/Slate_industry_in_Wales', lang='en'),
    "festrail-history": dict(
        short=('Ffestiniog Railway', 'Rheilffordd Ffestiniog'),
        t='History of the Ffestiniog Railway', by=('Ffestiniog and Welsh Highland Railways', 'Rheilffyrdd Ffestiniog ac Eryri'),
        note=('Incorporated 1832 and worked by gravity and horses; Princess and Mountaineer entered service in October 1863; passenger trains from 1864, the first on a narrow gauge in Britain; Little Wonder was shown in 1870 before engineers including the Imperial Russian Commission.',
              'Corfforwyd yn 1832 a gweithiai gyda disgyrchiant a cheffylau; daeth Princess a Mountaineer i wasanaeth ym mis Hydref 1863; trenau teithwyr o 1864, y cyntaf ar gledrau cul ym Mhrydain; dangoswyd Little Wonder yn 1870 o flaen peirianwyr gan gynnwys Comisiwn Ymerodrol Rwsia.'),
        url='https://www.festrail.co.uk/?p=14945', lang='en'),
    "wiki-littlewonder": dict(
        short=('Wikipedia', 'Wikipedia'),
        t='Festiniog Railway Little Wonder', by=('Wikipedia, with its sources', 'Wikipedia, gyda’i ffynonellau'),
        note=('In the 1870 trials, watched by the Imperial Russian Commissioners and the Commissioners of the Indian Government, Little Wonder hauled 112 wagons (206 tons) at an average of 12.5 mph.',
              'Yn nhreialon 1870, o flaen Comisiynwyr Ymerodrol Rwsia a Chomisiynwyr Llywodraeth India, tynnodd Little Wonder 112 o wagenni (206 tunnell) ar gyfartaledd o 12.5 milltir yr awr.'),
        url='https://en.wikipedia.org/wiki/Festiniog_Railway_Little_Wonder', lang='en'),
    # ---------- the Welsh Not long read (src/welshnot.py), each source opened and read November 2026 ----------
    "wn-hop": dict(
        short=("History of Parliament", "Hanes y Senedd"),
        t="St David’s Day: Parliament and the Welsh Language (Part One)", by=("The History of Parliament Trust, 1 March 2018", "Ymddiriedolaeth Hanes y Senedd, 1 Mawrth 2018"),
        note=("The 1536 Act said the Welsh “daily use a speech nothing like nor consonant to the natural mother tongue used within this realm”, imposed English in the courts and barred those who spoke only Welsh from public office.",
              "Dywedai Deddf 1536 fod y Cymry’n arfer “iaith nad yw’n debyg nac yn gydnaws â’r famiaith naturiol”, gosododd y Saesneg yn y llysoedd a gwahardd y rhai a siaradai Gymraeg yn unig rhag swyddi cyhoeddus."),
        url="https://historyofparliament.com/2018/03/01/st-davids-day-parliament-and-the-welsh-language-part-one/", lang="en"),
    "wn-act1536": dict(
        short=("legislation.gov.uk", "legislation.gov.uk"),
        t="Laws in Wales Act 1535 (27 Hen. 8 c. 26)", by=("The National Archives, legislation.gov.uk", "Yr Archifau Cenedlaethol, legislation.gov.uk"),
        note=("The Act’s record: repealed on 21 December 1993 by the Welsh Language Act 1993.",
              "Cofnod y Ddeddf: fe’i diddymwyd ar 21 Rhagfyr 1993 gan Ddeddf yr Iaith Gymraeg 1993."),
        url="https://www.legislation.gov.uk/aep/Hen8/27/26/contents", lang="en"),
    "wn-courts1942": dict(
        short=("Welsh Courts Act 1942", "Deddf Llysoedd Cymru 1942"),
        t="Welsh Courts Act 1942, section 1", by=("The National Archives, legislation.gov.uk", "Yr Archifau Cenedlaethol, legislation.gov.uk"),
        note=("“Section seventeen of the statute 27 Hen. 8. c. 26 … is hereby repealed”, and Welsh “may be used in any court in Wales by any party or witness who considers that he would otherwise be at any disadvantage”.",
              "Diddymwyd adran 17 o Ddeddf 27 Harri VIII p. 26, a chaniatawyd defnyddio’r Gymraeg “mewn unrhyw lys yng Nghymru” gan unrhyw un a fyddai fel arall dan anfantais."),
        url="https://www.legislation.gov.uk/ukpga/Geo6/5-6/40/section/1/enacted", lang="en"),
    "wn-symons": dict(
        short=("Blue Books, 1847", "Y Llyfrau Gleision, 1847"),
        t="Reports of the Commissioners of Inquiry into the State of Education in Wales (1847): J. C. Symons on the Welsh language", by=("Transcribed by GENUKI", "Trawsgrifiad gan GENUKI"),
        note=("Symons’s own words: “The Welsh language is a vast drawback to Wales, and a manifold barrier to the moral progress and commercial prosperity of the people. It is not easy to over-estimate its evil effects.”",
              "Geiriau Symons ei hun: “The Welsh language is a vast drawback to Wales…” (yr anfantais enfawr), a “Nid hawdd gorbwysleisio ei heffeithiau drwg.”"),
        url="https://www.genuki.org.uk/big/wal/CGN/CommsEnq", lang="en"),
    "wn-nlw-bluebooks": dict(
        short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"),
        t="The Blue Books of 1847", by=("National Library of Wales, digital gallery", "Llyfrgell Genedlaethol Cymru, oriel ddigidol"),
        note=("The three commissioners, Lingen, Symons and Johnson, Anglicans who spoke no Welsh; the furore that named the reports Brad y Llyfrau Gleision; and Kenneth O. Morgan’s words, “the Glencoe and the Amritsar of Welsh history”.",
              "Y tri chomisiynydd, Lingen, Symons a Johnson, Anglicaniaid di-Gymraeg; y cynnwrf a roddodd yr enw Brad y Llyfrau Gleision; a geiriau Kenneth O. Morgan, “Glencoe ac Amritsar hanes Cymru”."),
        url="https://www.library.wales/discover/digital-gallery/printed-material/the-blue-books-of-1847/", lang="en"),
    "wn-welshnot": dict(
        short=("Welsh Not, Wikipedia", "Welsh Not, Wikipedia"),
        t="Welsh Not", by=("Wikipedia, drawing on Martin Johnes, Welsh Not (University of Wales Press, 2024)", "Wikipedia, ar sail Martin Johnes, Welsh Not (Gwasg Prifysgol Cymru, 2024)"),
        note=("Its many names; used from the 1790s to about 1900, most of all in the first half of the 1800s; brought in by teachers, not by any government; and Johnes’s finding that schools which shut Welsh out were poor at teaching English.",
              "Ei enwau niferus; fe’i defnyddiwyd o’r 1790au hyd tua 1900, yn bennaf yn hanner cyntaf y 1800au; athrawon a’i cyflwynodd, nid llywodraeth; a chanfyddiad Johnes fod ysgolion a gaeai’r Gymraeg allan yn wael am ddysgu Saesneg."),
        url="https://en.wikipedia.org/wiki/Welsh_Not", url_cy="https://cy.wikipedia.org/wiki/Welsh_Not"),
    "wn-trysorfa": dict(
        short=("Trysorfa y Plant, 1879", "Trysorfa y Plant, 1879"),
        t="“Y Welsh Note”, Trysorfa y Plant, October 1879", by=("Scan on Wikimedia Commons", "Sgan ar Wikimedia Commons"),
        note=("The page itself, with its picture: “forty or fifty years ago the children of the day schools of Wales knew well what the Welsh Note was.”",
              "Y dudalen ei hun, a’i llun: “ddeugain a hanner can’ mlynedd yn ol, gwyddai plant ysgolion dyddiol Cymru yn dda beth oedd Welsh Note.”"),
        url="https://commons.wikimedia.org/wiki/File:%22Y_Welsh_Note%22._Trysorfa_y_Plant.png"),
    "wn-did": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"),
        t="Davies, Dan Isaac (1839–1887), a pioneer of the teaching of Welsh in schools", by=("Dictionary of Welsh Biography, National Library of Wales", "Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
        note=("The society founded at the Aberdare National Eisteddfod in 1885; Tair Miliwn o Gymry Dwyieithawg; Welsh made a grant-earning subject in 1886; his evidence to the royal commission, which took up his ideas in 1888.",
              "Y gymdeithas a sefydlwyd yn Eisteddfod Genedlaethol Aberdâr yn 1885; Tair Miliwn o Gymry Dwyieithawg; y Gymraeg yn bwnc a enillai grant yn 1886; ei dystiolaeth i’r comisiwn brenhinol, a fabwysiadodd ei syniadau yn 1888."),
        url="https://biography.wales/article/s-DAVI-ISA-1839", url_cy="https://bywgraffiadur.cymru/article/s-DAVI-ISA-1839"),
    "wn-beasley": dict(
        short=("IWA, 2012", "IWA, 2012"),
        t="The Rosa Parks of the Welsh language movement", by=("Institute of Welsh Affairs, Agenda, October 2012", "Sefydliad Materion Cymreig, Agenda, Hydref 2012"),
        note=("Trefor and Eileen Beasley of Llangennech refused English-only rate demands from 1952 to 1960; bailiffs took their furniture, piano and food; Saunders Lewis praised them in Tynged yr Iaith.",
              "Gwrthododd Trefor ac Eileen Beasley o Langennech filiau trethi uniaith Saesneg o 1952 hyd 1960; aeth y beilïaid â’u dodrefn, eu piano a’u bwyd; canmolodd Saunders Lewis hwy yn Tynged yr Iaith."),
        url="https://www.iwa.wales/agenda/2012/10/the-rosa-parks-of-the-welsh-language-movement/", lang="en"),
    "wn-tynged": dict(
        short=("Tynged yr Iaith", "Tynged yr Iaith"),
        t="Tynged yr Iaith", by=("Wikipedia", "Wikipedia"),
        note=("Broadcast on 13 February 1962; Welsh would end as a living language “about the beginning of the twenty-first century” if the trend went on; the Beasleys held up as the model.",
              "Fe’i darlledwyd ar 13 Chwefror 1962; byddai’r Gymraeg yn darfod fel iaith fyw “tua dechrau’r unfed ganrif ar hugain” pe parhâi’r duedd; y Beasleys yn batrwm."),
        url="https://en.wikipedia.org/wiki/Tynged_yr_Iaith", url_cy="https://cy.wikipedia.org/wiki/Tynged_yr_Iaith"),
    "wn-cymdeithas": dict(
        short=("Cymdeithas yr Iaith", "Cymdeithas yr Iaith"),
        t="Welsh Language Society", by=("Wikipedia", "Wikipedia"),
        note=("Founded at Pontarddulais on 4 August 1962; the first protest on Trefechan Bridge, where about seventy people stopped the traffic for half an hour; over a thousand in court for its campaigns; S4C and the 2011 Measure.",
              "Fe’i sefydlwyd ym Mhontarddulais ar 4 Awst 1962; y brotest gyntaf ar Bont Trefechan, lle ataliodd tua saith deg o bobl y drafnidiaeth am hanner awr; dros fil yn y llys dros ei hymgyrchoedd; S4C a Mesur 2011."),
        url="https://en.wikipedia.org/wiki/Welsh_Language_Society", url_cy="https://cy.wikipedia.org/wiki/Cymdeithas_yr_Iaith_Gymraeg"),
    "wn-act1967": dict(
        short=("Welsh Language Act 1967", "Deddf yr Iaith 1967"),
        t="Welsh Language Act 1967", by=("Wikipedia", "Wikipedia"),
        note=("Royal Assent on 27 July 1967; Welsh in the courts and on official forms; the 1746 rule that ‘England’ included Wales repealed; partly based on the Hughes Parry report of 1965.",
              "Cydsyniad Brenhinol ar 27 Gorffennaf 1967; y Gymraeg yn y llysoedd ac ar ffurflenni swyddogol; diddymu rheol 1746 fod ‘England’ yn cynnwys Cymru; yn rhannol ar sail adroddiad Hughes Parry yn 1965."),
        url="https://en.wikipedia.org/wiki/Welsh_Language_Act_1967", lang="en"),
    "wn-measure": dict(
        short=("Welsh Language Measure 2011", "Mesur y Gymraeg 2011"),
        t="Welsh Language (Wales) Measure 2011, section 1", by=("The National Archives, legislation.gov.uk", "Yr Archifau Cenedlaethol, legislation.gov.uk"),
        note=("“(1) The Welsh language has official status in Wales.”", "“(1) Mae statws swyddogol i’r Gymraeg yng Nghymru.”"),
        url="https://www.legislation.gov.uk/mwa/2011/1/section/1", lang="en"),
    # ---------- the full pages behind the home page facts (src/factplaces.py) ----------
    "orme-visitwales": dict(
        short=("Visit Wales", "Croeso Cymru"),
        t="Great Orme Mines", by=("Visit Wales, Welsh Government", "Croeso Cymru, Llywodraeth Cymru"),
        note=("The Great Cavern, “the largest prehistoric underground excavation in the world”, in “the oldest metal mine open to the public anywhere in the world”; open mid-March to the end of October.",
              "Yr Ogof Fawr, y cloddiad tanddaearol cynhanesyddol mwyaf yn y byd, yn y mwynglawdd metel hynaf ar agor i’r cyhoedd yn unman yn y byd; ar agor o ganol Mawrth hyd ddiwedd Hydref."),
        url="https://www.visitwales.com/attraction/historic-site/great-orme-mines-527987", lang="en"),
    "orme-liverpool": dict(
        short=("University of Liverpool", "Prifysgol Lerpwl"),
        t="Britain’s earliest mining boom revealed", by=("University of Liverpool news, 15 October 2019", "Newyddion Prifysgol Lerpwl, 15 Hydref 2019"),
        note=("The Orme gave “enough copper to dominate Britain’s metal supply for about two centuries”, with a golden age about 1600–1400 BC.",
              "Rhoddodd y Gogarth ddigon o gopr i reoli cyflenwad metel Prydain am tua dwy ganrif, gydag oes aur tua 1600–1400 CC."),
        url="https://news.liverpool.ac.uk/2019/10/15/britains-earliest-mining-boom-revealed/", lang="en"),
    "orme-subbrit": dict(
        short=("Subterranea Britannica", "Subterranea Britannica"),
        t="Great Orme Mines", by=("Subterranea Britannica, the society for underground sites", "Subterranea Britannica, y gymdeithas safleoedd tanddaearol"),
        note=("“Discovered in 1987 during a landscaping project”; a self-guided tour of a 200 m underground section.",
              "Fe’i darganfuwyd yn 1987 yn ystod cynllun tirlunio; taith hunandywys drwy ran danddaearol 200 m."),
        url="https://www.subbrit.org.uk/sites/great-orme-mines/", lang="en"),
    "llanfair-bangor": dict(
        short=("Bangor University", "Prifysgol Bangor"),
        t="Archive of the month: the Women’s Institute", by=("Bangor University Archives", "Archifau Prifysgol Bangor"),
        note=("“The First British WI was started in Llanfair PG, Anglesey on September 16th, 1915.”",
              "Dechreuwyd Sefydliad y Merched cyntaf Prydain yn Llanfair PG, Ynys Môn, ar 16 Medi 1915."),
        url="https://bangor.ac.uk/news/archive/archive-of-the-month-17963", lang="en"),
    "llanfair-coflein": dict(
        short=("Coflein", "Coflein"),
        t="Llanfair PG Women’s Institute Hall", by=("Coflein, Royal Commission on the Ancient and Historical Monuments of Wales", "Coflein, Comisiwn Brenhinol Henebion Cymru"),
        note=("“Established in September 1915, the branch of the Women’s Institute in Llanfairpwllgwyngyll is the oldest in Britain.” It met first in a cottage, then in the iron hall by the tollhouse.",
              "Sefydlwyd y gangen ym mis Medi 1915, a hi yw’r hynaf ym Mhrydain. Cyfarfu gyntaf mewn bwthyn, yna yn y neuadd haearn wrth y tollty."),
        url="https://coflein.gov.uk/en/site/420753"),
    "bethlehem-wikishire": dict(
        short=("Wikishire", "Wikishire"),
        t="Bethlehem, Carmarthenshire", by=("Wikishire", "Wikishire"),
        note=("Once Dyffryn Ceidrich; named after its chapel in the Methodist revival; the Christmas postmark gained national attention around 1965; Carn Goch hillfort above.",
              "Dyffryn Ceidrych gynt; cafodd ei enw gan ei gapel yn y diwygiad Methodistaidd; daeth y stamp Nadolig i sylw’r genedl tua 1965; bryngaer Carn Goch uwchben."),
        url="https://wikishire.co.uk/wiki/Bethlehem,_Carmarthenshire", lang="en"),
    "pyg-wiki": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Pen-y-Gwryd", by=("Wikipedia", "Wikipedia"),
        note=("The farmhouse of 1811 and the inn; Henry and Ann Owen; the Climbers’ Club founded here in May 1898; the 1953 Everest and 1955 Kangchenjunga signatures on the ceiling; the Roman marching camp.",
              "Ffermdy 1811 a’r dafarn; Henry ac Ann Owen; sefydlu’r Climbers’ Club yma ym mis Mai 1898; llofnodion Everest 1953 a Kangchenjunga 1955 ar y nenfwd; y gwersyll ymdaith Rhufeinig."),
        url="https://en.wikipedia.org/wiki/Pen-y-Gwryd", lang="en"),
    "lavernock-wiki": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Lavernock", by=("Wikipedia, drawing on George Kemp’s diary", "Wikipedia, ar sail dyddiadur George Kemp"),
        note=("Day by day, 10 to 13 May 1897: Preece’s apparatus on Flat Holm, Marconi’s at Lavernock, the longer aerial, and the messages ‘Are you ready?’, ‘Can you hear me?’, ‘Yes, loud and clear.’",
              "Ddydd wrth ddydd, 10 i 13 Mai 1897: offer Preece ar Ynys Echni, offer Marconi yn Larnog, yr erial hirach, a’r negeseuon ‘Are you ready?’, ‘Can you hear me?’, ‘Yes, loud and clear.’"),
        url="https://en.wikipedia.org/wiki/Lavernock", lang="en"),
    "marconi-urban75": dict(
        short=("urban75", "urban75"),
        t="St Lawrence Church, Lavernock: Marconi and the birth of radio", by=("urban75", "urban75"),
        note=("The church and the bronze plaque put up by the Cardiff Rotary Club in 1948, with photographs.",
              "Yr eglwys a’r plac efydd a godwyd gan Glwb Rotari Caerdydd yn 1948, gyda lluniau."),
        url="https://www.urban75.org/blog/st-lawrence-church-lavernock-south-wales-marconi-and-the-birth-of-radio/", lang="en"),
    "dwb-preece": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"),
        t="Preece, Sir William Henry (1834–1913), electrical engineer", by=("Dictionary of Welsh Biography, National Library of Wales", "Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
        note=("Born at Caernarfon; engineer-in-chief of the Post Office from 1892; in 1892 he sent messages through the air across the Bristol Channel between Penarth and Flat Holm.",
              "Ganed yng Nghaernarfon; prif beiriannydd y Swyddfa Bost o 1892; yn 1892 anfonodd negeseuon drwy’r awyr ar draws Môr Hafren rhwng Penarth ac Ynys Echni."),
        url="https://biography.wales/article/s-PREE-HEN-1834", url_cy="https://bywgraffiadur.cymru/article/s-PREE-HEN-1834"),
    "preece-wiki": dict(
        short=("Wikipedia", "Wikipedia"),
        t="William Henry Preece", by=("Wikipedia", "Wikipedia"),
        note=("“Preece became one of Marconi’s most ardent supporters” and gained help from the Post Office for his work.",
              "Daeth Preece yn un o gefnogwyr mwyaf brwd Marconi ac ennill cymorth y Swyddfa Bost i’w waith."),
        url="https://en.wikipedia.org/wiki/William_Henry_Preece", lang="en"),

    # ---------- World firsts badges on person pages ----------
    "dwb-parryjones": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"),
        t="Jones, Thomas Parry (1935–2013), inventor", by=("Dictionary of Welsh Biography, National Library of Wales", "Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
        note=("In 1974 his company produced the first breathalyser with an electrochemical sensor.",
              "Yn 1974 cynhyrchodd ei gwmni’r anadliedydd cyntaf â synhwyrydd electrocemegol."),
        url="https://biography.wales/article/s12-JONE-PAR-1935", url_cy="https://bywgraffiadur.cymru/article/s12-JONE-PAR-1935"),
    "dwb-wallace": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"),
        t="Wallace, Alfred Russel (1823–1913), naturalist", by=("Dictionary of Welsh Biography, National Library of Wales", "Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
        note=("His theory of natural selection was “identical with that being developed by Darwin but independent of him”; their papers were read together at the Linnean Society on 1 July 1858.",
              "Roedd ei ddamcaniaeth am ddethol naturiol yr un fath ag un Darwin ond yn annibynnol arni; darllenwyd eu papurau gyda’i gilydd yng Nghymdeithas Linnaeus ar 1 Gorffennaf 1858."),
        url="https://biography.wales/article/s6-WALL-RUS-1823", url_cy="https://bywgraffiadur.cymru/article/s6-WALL-RUS-1823"),
    "wiki-dillwyn": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Mary Dillwyn", by=("Wikipedia", "Wikipedia"),
        note=("“She is also credited with taking the first known photograph of a snowman, circa 1853.”",
              "Hi sy’n cael y clod am dynnu’r ffotograff cyntaf y gwyddys amdano o ddyn eira, tua 1853."),
        url="https://en.wikipedia.org/wiki/Mary_Dillwyn", lang="en"),
    "wiki-iroberts": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Isaac Roberts", by=("Wikipedia", "Wikipedia"),
        note=("His photograph of the Great Nebula in Andromeda, taken on 29 December 1888, “revealed that the nebula had a spiral structure, which was quite unexpected at the time.”",
              "Dangosodd ei ffotograff o Nifwl Mawr Andromeda, a dynnwyd ar 29 Rhagfyr 1888, fod gan y nifwl siâp troellog, peth annisgwyl iawn ar y pryd."),
        url="https://en.wikipedia.org/wiki/Isaac_Roberts", lang="en"),
    "wiki-josephson": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Brian Josephson", by=("Wikipedia", "Wikipedia"),
        note=("As a PhD student in 1962 he did the research that led to the Josephson effect; Nobel Prize in Physics 1973.",
              "Fel myfyriwr PhD yn 1962 gwnaeth yr ymchwil a arweiniodd at effaith Josephson; Gwobr Nobel mewn Ffiseg 1973."),
        url="https://en.wikipedia.org/wiki/Brian_Josephson", lang="en"),
    "wiki-cooke": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Nicole Cooke", by=("Wikipedia", "Wikipedia"),
        note=("In 2008 she became the first cyclist, man or woman, to be road race World Champion and Olympic gold medallist in the same year.",
              "Yn 2008 hi oedd y beiciwr cyntaf, yn ddyn neu’n fenyw, i fod yn Bencampwr y Byd yn y ras ffordd ac yn enillydd medal aur Olympaidd yn yr un flwyddyn."),
        url="https://en.wikipedia.org/wiki/Nicole_Cooke", lang="en"),
    "wiki-awjones": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Alun Wyn Jones", by=("Wikipedia", "Wikipedia"),
        note=("“He is the world’s most-capped rugby union player, with 158 caps for Wales and 12 for the British & Irish Lions.”",
              "Ef yw’r chwaraewr rygbi’r undeb â’r mwyaf o gapiau yn y byd: 158 i Gymru a 12 i’r Llewod."),
        url="https://en.wikipedia.org/wiki/Alun_Wyn_Jones", lang="en"),
    "wiki-wilde": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Jimmy Wilde", by=("Wikipedia", "Wikipedia"),
        note=("“He was the first official world flyweight champion”, holding the title from 1916 to 1923.",
              "Ef oedd pencampwr pwysau pry swyddogol cyntaf y byd, a daliodd y teitl o 1916 hyd 1923."),
        url="https://en.wikipedia.org/wiki/Jimmy_Wilde", lang="en"),
    "wiki-cjackson": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Colin Jackson", by=("Wikipedia", "Wikipedia"),
        note=("He set the 110 metres hurdles world record, 12.91 s, on 20 August 1993; it stood for nearly thirteen years, until 11 July 2006.",
              "Gosododd record y byd yn y 110 metr dros y clwydi, 12.91 eiliad, ar 20 Awst 1993; safodd am bron i dair blynedd ar ddeg, tan 11 Gorffennaf 2006."),
        url="https://en.wikipedia.org/wiki/Colin_Jackson", lang="en"),
    "wiki-rprice": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Richard Price", by=("Wikipedia", "Wikipedia"),
        note=("“He edited Bayes’s major work An Essay Towards Solving a Problem in the Doctrine of Chances (1763).”",
              "Ef a olygodd brif waith Bayes, An Essay Towards Solving a Problem in the Doctrine of Chances (1763)."),
        url="https://en.wikipedia.org/wiki/Richard_Price", lang="en"),
    "wiki-ejwilliams": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Evan James Williams", by=("Wikipedia", "Wikipedia"),
        note=("“Williams was the first person who experimentally detected muon decay and managed to photograph it”, working with a cloud chamber at Aberystwyth.",
              "Williams oedd y cyntaf i ganfod dadfeiliad mwon mewn arbrawf a llwyddo i’w ffotograffu, gyda siambr gwmwl yn Aberystwyth."),
        url="https://en.wikipedia.org/wiki/Evan_James_Williams", lang="en"),
    "wiki-thomas-splint": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Thomas splint", by=("Wikipedia", "Wikipedia"),
        note=("Introduced by Hugh Owen Thomas; with it “the mortality rate dropped from 80% to 15.6%” for broken thigh bones.",
              "Hugh Owen Thomas a’i cyflwynodd; gydag ef gostyngodd y gyfradd marwolaethau o 80% i 15.6% am glun wedi torri."),
        url="https://en.wikipedia.org/wiki/Thomas_splint", lang="en"),
    "wiki-rjones-surgeon": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Robert Jones (surgeon)", by=("Wikipedia", "Wikipedia"),
        note=("In 1896 he took an X-ray of a boy’s wrist to find a bullet; published in The Lancet in February 1896, “the first published clinical radiograph”.",
              "Yn 1896 tynnodd belydr-X o arddwrn bachgen i ddod o hyd i fwled; cyhoeddwyd yn The Lancet ym mis Chwefror 1896, y radiograff clinigol cyntaf i’w gyhoeddi."),
        url="https://en.wikipedia.org/wiki/Robert_Jones_(surgeon)", lang="en"),
    "wiki-ernestjones": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Ernest Jones", by=("Wikipedia", "Wikipedia"),
        note=("“Jones was the first English-speaking practitioner of psychoanalysis”; he first met Freud in 1908.",
              "Jones oedd y seicdreiddiwr cyntaf yn y byd Saesneg ei iaith; cyfarfu â Freud gyntaf yn 1908."),
        url="https://en.wikipedia.org/wiki/Ernest_Jones_(psychoanalyst)", lang="en"),
}

# person id -> sources for the World first / Welsh first badge on that person's page
FIRST_CITES = {
    "robert-recorde": "dwb-recorde", "william-jones": "dwb-wjones",
    "pryce-pryce-jones": "pryce-storipowys,dwb-pryce", "william-grove": "grove-aps,dwb-grove",
    "william-preece": "lavernock-wiki,preece-wiki", "red-lady-of-paviland": "paviland-museum,paviland-oumnh",
    "madog": "powel-1584", "tom-parry-jones": "dwb-parryjones", "alfred-russel-wallace": "dwb-wallace",
    "mary-dillwyn": "wiki-dillwyn", "isaac-roberts": "wiki-iroberts", "brian-josephson": "wiki-josephson",
    "nicole-cooke": "wiki-cooke", "alun-wyn-jones": "wiki-awjones", "jimmy-wilde": "wiki-wilde",
    "colin-jackson": "wiki-cjackson", "richard-price": "wiki-rprice", "evan-james-williams": "wiki-ejwilliams",
    "hugh-owen-thomas": "wiki-thomas-splint", "robert-jones-surgeon": "wiki-rjones-surgeon",
    "ernest-jones": "wiki-ernestjones",
}

from princes import CITES as _PRINCES  # noqa: E402  (the kings and princes of Wales, src/princes.py)
S.update(_PRINCES)
from writers import CITES as _WRITERS  # noqa: E402  (the writers who recorded early Wales, src/writers.py)
S.update(_WRITERS)
from bruts import CITES as _BRUTS  # noqa: E402  (the Bruts, src/bruts.py)
S.update(_BRUTS)
from oldbooks import CITES as _OLDBOOKS  # noqa: E402  (the old books of Wales, src/oldbooks.py)
S.update(_OLDBOOKS)
from onthisday import CITES as _OTD  # noqa: E402  (the sources of On this day, src/onthisday.py)
S.update(_OTD)
from epynt import CITES as _EPYNT  # noqa: E402  (the clearing of Epynt, src/epynt.py)
S.update(_EPYNT)

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
    # a real button (it opens the card; the card holds the links), so Space and Enter both work and screen readers hear "button, collapsed"
    return (f'<span class="cite-w"><button type="button" class="cite" aria-expanded="false" aria-controls="{pid}" aria-label="{e(aria)}" data-cite>{e(label)}</button>'
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


def linked(text, href, cy=False, js=False):
    """A sentence as a link to its full page, with its source chips after the link (a chip can't sit inside a link).
    js=True: chips already turned into HTML, for text a script puts on the page; otherwise the markers are kept for render()."""
    words = _html.escape(strip(text), quote=False)
    marks = "".join(m.group(0) for m in MARK.finditer(text))
    if js:
        marks = "".join(chip(keys(m.group(1)), cy, "citej") for m in MARK.finditer(text))
    return f'<a class="fact-a" href="{_html.escape(href)}">{words}</a>{marks}'


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
  color: var(--muted); background: rgba(255,255,255,.03); text-decoration: none; white-space: nowrap; cursor: pointer; -webkit-appearance: none; appearance: none; font-style: normal; text-transform: none }
.cite::before { content: "§"; margin-right: .3em; color: var(--dragon) }
.cite:hover, .cite[aria-expanded="true"] { color: var(--ink); border-color: var(--dragon) }
.cite:focus-visible { outline: 2px solid var(--dragon); outline-offset: 2px }
.cite-pop { position: absolute; z-index: 60; left: 0; top: calc(100% + .45rem); width: min(22rem, calc(100vw - 2rem)); white-space: normal;
  display: grid; gap: .7rem; padding: .9rem 2.2rem .95rem 1rem; text-align: left;
  background: var(--slate-2); border: 1px solid var(--line); border-radius: 12px; box-shadow: 0 14px 40px rgba(0,0,0,.45);
  font-family: var(--f-body); font-size: .86rem; line-height: 1.45; font-weight: 400; letter-spacing: 0; word-spacing: 0; color: var(--ink) }
.cite-pop[hidden] { display: none }
.cite-h { font-family: var(--f-mono); font-size: .75rem; text-transform: uppercase; letter-spacing: .1em; color: var(--muted) }
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
  .cite { font-size: .75rem; padding: .28em .7em .32em; vertical-align: .1em }
  .cite-pop { position: fixed; left: .75rem; right: .75rem; top: auto; bottom: .75rem; width: auto; max-height: 70vh; overflow: auto }
}
@media print { .cite-pop { display: none !important } .cite { border: 0; padding: 0 } }
"""
