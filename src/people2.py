# More famous Welsh people (Nov 2026): gathers parts A–D, adds a field for every person on the site,
# and the Welsh firsts. data.py adds PEOPLE_NEW to the people list, long.py adds PEOPLE_LONG,
# build.py uses FIELDS, FIELD, FIRSTS and OTHER_FIRSTS for the people filter, person badges and firsts.html.
import people2a as _A, people2b as _B, people2c as _C, people2d as _D, people2e as _E, people2f as _F, people2g as _G
import arthur_circle as _AC, sixth_century as _SC

import christianity as _CH  # Brân Fendigaid and King Lleurwg (src/christianity.py)

ALL = _A.PEOPLE + _B.PEOPLE + _C.PEOPLE + _D.PEOPLE + _E.PEOPLE + _F.PEOPLE + _AC.PEOPLE + _CH.PEOPLE + _SC.PEOPLE + _G.PEOPLE

# tuples in the site's people format: (slug, era, dates, nameEn, nameCy, epithetEn, epithetCy, bioEn, bioCy, wikipediaTitle)
PEOPLE_NEW = [(p["id"], p["era"], p["d"], p["en"], p["cy"], p["eEn"], p["eCy"], p["bEn"], p["bCy"], p["w"]) for p in ALL]
PEOPLE_LONG = {p["id"]: (p["lEn"], p["lCy"]) for p in ALL}
PEOPLE_LONG.update(_SC.LONG)  # full pages for Illtud and Dewi Sant (src/sixth_century.py)

# What each person is famous for. Order here is the order of the chips.
FIELDS = [
 ("rulers", "Kings, princes and rulers", "Brenhinoedd, tywysogion a rheolwyr"),
 ("faith", "Saints and faith", "Saint a ffydd"),
 ("words", "Poets and writers", "Beirdd ac awduron"),
 ("learning", "Scholars and teachers", "Ysgolheigion ac athrawon"),
 ("science", "Science, medicine and invention", "Gwyddoniaeth, meddygaeth a dyfeisio"),
 ("explore", "Explorers and adventurers", "Fforwyr ac anturiaethwyr"),
 ("heroes", "Folk heroes", "Arwyr gwerin"),
 ("politics", "Politics and campaigns", "Gwleidyddiaeth ac ymgyrchu"),
 ("enterprise", "Industry and enterprise", "Diwydiant a menter"),
 ("art", "Art and design", "Celf a chynllunio"),
 ("music", "Music", "Cerddoriaeth"),
 ("stage", "Stage and screen", "Llwyfan a sgrin"),
 ("sport", "Sport", "Chwaraeon"),
]

FIELD = {p["id"]: p["f"] for p in ALL}
FIELD.update({
 "caratacus": "rulers", "cadog": "faith", "maelgwn-gwynedd": "rulers", "illtud": "faith", "dewi-sant": "faith", "aneirin": "words",
 "taliesin": "words", "arthur": "rulers", "rhodri-mawr": "rulers", "asser": "learning", "hywel-dda": "rulers", "gruffudd-ap-llywelyn": "rulers",
 "gruffudd-ap-cynan": "rulers", "nest": "rulers", "gwenllian": "rulers", "owain-gwynedd": "rulers", "yr-arglwydd-rhys": "rulers",
 "gerallt-gymro": "words", "llywelyn-fawr": "rulers", "siwan": "rulers", "llywelyn-ap-gruffudd": "rulers", "dafydd-ap-gwilym": "words",
 "owain-lawgoch": "rulers", "owain-glyndwr": "rulers", "guto-r-glyn": "words", "harri-tudur": "rulers", "robert-recorde": "science",
 "william-morgan": "faith", "edward-lhuyd": "learning", "william-jones": "science", "griffith-jones": "learning", "howell-harris": "faith",
 "pantycelyn": "faith", "iolo-morganwg": "words", "jemima-nicholas": "heroes", "robert-owen": "politics", "ann-griffiths": "faith",
 "mary-jones": "faith", "betsi-cadwaladr": "science", "william-price": "science", "lady-llanover": "art", "dic-penderyn": "heroes",
 "william-grove": "science", "henry-richard": "politics", "michael-d-jones": "politics", "alfred-russel-wallace": "science",
 "cranogwen": "words", "joseph-parry": "music", "evan-roberts": "faith", "lloyd-george": "politics", "gwen-john": "art",
 "hedd-wyn": "words", "jim-griffiths": "politics", "kate-roberts": "words", "saunders-lewis": "words", "ifan-ab-owen-edwards": "learning",
 "aneurin-bevan": "politics", "megan-lloyd-george": "politics", "gwynfor-evans": "politics", "r-s-thomas": "words", "dylan-thomas": "words",
 "elaine-morgan": "words", "richard-burton": "stage", "john-charles": "sport", "betty-campbell": "learning", "shirley-bassey": "music",
 "anthony-hopkins": "stage", "tom-jones": "music", "gareth-edwards": "sport", "rhodri-morgan": "politics", "tanni-grey-thompson": "sport",
 "twm-sion-cati": "heroes",
})

# slug -> (kind, textEn, textCy, year). kind "world" = a first (or record) for the whole world; "wales" = a first for Wales, or for Britain, or abroad.
FIRSTS = {p["id"]: p["first"] for p in ALL if p["first"]}
FIRSTS.update({
 "robert-recorde": ("world", "Invented the equals sign, 1557", "Dyfeisiodd yr hafalnod, 1557", 1557),
 "william-jones": ("world", "First to use π for the ratio of a circle, 1706", "Y cyntaf i ddefnyddio π am gymhareb cylch, 1706", 1706),
 "edward-lhuyd": ("world", "First to show that Welsh, Cornish, Breton, Irish and Gaelic are one family of languages, 1707", "Y cyntaf i ddangos fod y Gymraeg, y Gernyweg, y Llydaweg, y Wyddeleg a’r Aeleg yn un teulu o ieithoedd, 1707", 1707),
 "william-grove": ("world", "Built the first fuel cell, 1842", "Adeiladodd y gell danwydd gyntaf, 1842", 1842),
 "alfred-russel-wallace": ("world", "Discovered evolution by natural selection, alongside Darwin, 1858", "Darganfu esblygiad drwy ddethol naturiol, ochr yn ochr â Darwin, 1858", 1858),
 "aneirin": ("world", "Y Gododdin: the oldest poetry of Britain in a language still spoken, c. 600", "Y Gododdin: barddoniaeth hynaf Prydain mewn iaith a siaredir o hyd, tua 600", 600),
 "lloyd-george": ("wales", "Brought in Britain’s first state old-age pensions, 1908", "Cyflwynodd bensiynau henoed cyntaf y wladwriaeth ym Mhrydain, 1908", 1908),
 "aneurin-bevan": ("world", "Founded the NHS, 1948: health care free to everyone at the point of use", "Sefydlodd y Gwasanaeth Iechyd, 1948: gofal iechyd am ddim i bawb pan fo’i angen", 1948),
 "yr-arglwydd-rhys": ("wales", "Held the first recorded eisteddfod, Cardigan 1176", "Cynhaliodd yr eisteddfod gyntaf y gwyddys amdani, Aberteifi 1176", 1176),
 "gruffudd-ap-llywelyn": ("wales", "The only king ever to rule the whole of Wales, from 1055", "Yr unig frenin erioed i reoli Cymru gyfan, o 1055", 1055),
 "william-morgan": ("wales", "The first complete Bible in Welsh, 1588", "Y Beibl Cymraeg cyflawn cyntaf, 1588", 1588),
 "iolo-morganwg": ("wales", "Held the first Gorsedd of the Bards, 1792", "Cynhaliodd Orsedd gyntaf y Beirdd, 1792", 1792),
 "robert-owen": ("wales", "Opened the first infant school in Britain, 1816", "Agorodd yr ysgol fabanod gyntaf ym Mhrydain, 1816", 1816),
 "joseph-parry": ("wales", "Blodwen, the first opera in Welsh, 1878", "Blodwen, yr opera Gymraeg gyntaf, 1878", 1878),
 "william-price": ("wales", "His trial made cremation legal in Britain, 1884", "Gwnaeth ei achos llys amlosgi’n gyfreithlon ym Mhrydain, 1884", 1884),
 "megan-lloyd-george": ("wales", "The first woman MP for a Welsh seat, 1929", "Yr AS benywaidd cyntaf dros sedd yng Nghymru, 1929", 1929),
 "ifan-ab-owen-edwards": ("wales", "Opened the first Welsh-medium school, 1939", "Agorodd yr ysgol Gymraeg gyntaf, 1939", 1939),
 "jim-griffiths": ("wales", "The first Secretary of State for Wales, 1964", "Ysgrifennydd Gwladol cyntaf Cymru, 1964", 1964),
 "gwynfor-evans": ("wales", "Plaid Cymru’s first MP, 1966", "AS cyntaf Plaid Cymru, 1966", 1966),
 "betty-campbell": ("wales", "Wales’s first Black head teacher", "Prifathrawes ddu gyntaf Cymru", 1970),
 "rhodri-morgan": ("wales", "The first to hold the title First Minister of Wales, 2000", "Y cyntaf i ddal y teitl Prif Weinidog Cymru, 2000", 2000),
})

# Firsts that belong to a place or to the nation rather than to one person: (kind, year, titleEn, titleCy, textEn, textCy, link)
OTHER_FIRSTS = [
 ("world", 1804, "The first steam locomotive", "Y locomotif stêm cyntaf",
  "At Penydarren in Merthyr Tydfil, Trevithick’s engine hauled ten tons of iron and seventy men to Abercynon: the first time a steam locomotive pulled a load on rails anywhere in the world.",
  "Ym Mhenydarren, Merthyr Tudful, tynnodd injan Trevithick ddeg tunnell o haearn a saith deg o ddynion i Abercynon: y tro cyntaf yn y byd i locomotif stêm dynnu llwyth ar gledrau.", "place-merthyr.html"),
 ("world", 1807, "The first passenger railway", "Y rheilffordd deithwyr gyntaf",
  "The Swansea and Mumbles Railway carried the first fare-paying railway passengers in the world, along the shore of Swansea Bay.",
  "Cludodd Rheilffordd Abertawe a’r Mwmbwls y teithwyr rheilffordd cyntaf yn y byd i dalu am eu taith, ar hyd glan Bae Abertawe.", "story-firsts.html"),
 ("world", 1826, "The greatest suspension bridge of its day", "Pont grog fwyaf ei hoes",
  "Telford’s bridge over the Menai Strait opened as the largest suspension bridge in the world, carrying the road to Holyhead high enough for tall ships to sail beneath.",
  "Agorwyd pont Telford dros Afon Menai fel y bont grog fwyaf yn y byd, yn cario’r ffordd i Gaergybi’n ddigon uchel i longau tal hwylio oddi tani.", "place-menai.html"),
 ("world", 1863, "Steam on the narrow gauge", "Stêm ar y lein gul",
  "The Ffestiniog Railway, built to carry slate from Blaenau to Porthmadog, proved in 1863 that steam engines could run on rails less than two feet apart, and carried passengers from 1865. Little railways across the world followed its lead.",
  "Profodd Rheilffordd Ffestiniog, a godwyd i gludo llechi o Flaenau i Borthmadog, yn 1863 y gallai injans stêm redeg ar gledrau llai na dwy droedfedd oddi wrth ei gilydd, a chludodd deithwyr o 1865. Dilynodd rheilffyrdd bach ledled y byd ei hesiampl.", "story-firsts.html"),
 ("world", 1894, "The oldest record shop in the world", "Y siop recordiau hynaf yn y byd",
  "Spillers Records in Cardiff opened in 1894, selling phonograph cylinders. It is still trading, the oldest record shop on earth.",
  "Agorodd Spillers Records yng Nghaerdydd yn 1894, yn gwerthu silindrau ffonograff. Mae’n dal i fasnachu, y siop recordiau hynaf ar y ddaear.", "story-firsts.html"),
 ("wales", 2001, "A champion for children", "Llais i blant",
  "Wales appointed the first Children’s Commissioner in the United Kingdom, an independent voice for every child.",
  "Penododd Cymru Gomisiynydd Plant cyntaf y Deyrnas Unedig, llais annibynnol i bob plentyn.", "era-today.html"),
 ("world", 2008, "The first Fair Trade Nation", "Y Genedl Masnach Deg gyntaf",
  "Wales became the first country in the world to be named a Fair Trade Nation.",
  "Cymru oedd y wlad gyntaf yn y byd i’w henwi’n Genedl Masnach Deg.", "story-firsts.html"),
 ("wales", 2011, "Paying for plastic bags", "Talu am fagiau plastig",
  "Wales was the first part of the United Kingdom to charge for carrier bags. Bag use fell by around three-quarters, and the rest of the UK followed.",
  "Cymru oedd y rhan gyntaf o’r Deyrnas Unedig i godi tâl am fagiau siopa. Syrthiodd y defnydd o fagiau tua thri chwarter, a dilynodd gweddill y DU.", "era-today.html"),
 ("world", 2015, "A law for future generations", "Deddf i genedlaethau’r dyfodol",
  "The Well-being of Future Generations Act made Wales the first country in the world to require its public bodies, by law, to think of the people not yet born.",
  "Gwnaeth Deddf Llesiant Cenedlaethau’r Dyfodol Gymru’r wlad gyntaf yn y byd i fynnu, drwy gyfraith, fod ei chyrff cyhoeddus yn meddwl am y bobl sydd heb eu geni eto.", "story-firsts.html"),
 ("wales", 2015, "Opt-out organ donation", "Rhoi organau drwy optio allan",
  "Wales became the first part of the United Kingdom where everyone is counted as an organ donor unless they say otherwise. England and Scotland followed.",
  "Cymru oedd y rhan gyntaf o’r Deyrnas Unedig lle cyfrifir pawb yn rhoddwr organau oni bai eu bod yn dweud yn wahanol. Dilynodd Lloegr a’r Alban.", "era-today.html"),
]
