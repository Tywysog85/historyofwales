"""The place-name decoder: the words that make up Welsh place names, used by the decoder on the home page and on
towns.html (both run src/placenames.js; build.py writes the data below into _site/placenames.js).

Each entry is (word, English, Welsh). Give the plain, unmutated form only: the decoder works out the mutated forms
itself (soft: pont -> bont, cam -> gam, Mair -> fair; nasal: Buallt -> Muallt, Caer -> Nghaer; aspirate: pen -> phen).
Add a spelling after a "|" when the English spelling differs (e.g. "taf|taff"), and the decoder knows both.

WORDS     ordinary Welsh words in place names (also the word list at the foot of towns.html)
RIVERS    rivers and streams, which name a great many places (Abertawe, Llangammarch, Aberhonddu)
SAINTS    the saints of the llannau, and other people and lands in names (Llandeilo, Caereinion)
ENGLISH   English words in Welsh place names (Builth Wells, Llandudno Junction, Colwyn Bay)
OLDNAMES  English and Norse names of Welsh places, matched as a whole word only (Swansea, Builth, Brecon)

Meanings follow the standard works (Owen and Morgan, Dictionary of the Place-Names of Wales). Where a meaning is argued
over, leave it out or say "probably".
"""

WORDS = [
 ("aber", "river mouth, where waters meet", "ceg afon, cymer"), ("afon", "river", "afon"), ("allt", "hillside, wooded slope", "llethr coediog"),
 ("gallt", "hillside, wooded slope", "llethr coediog"), ("ar", "on", "ar"), ("bach", "small", "bach"), ("ma", "plain, place", "maes, man"), ("bychan", "small", "bychan"),
 ("ban", "peak", "copa"), ("bannau", "peaks", "copaon"), ("banc", "bank, hill", "bryncyn"), ("bedd", "grave", "bedd"), ("beddau", "graves", "beddau"),
 ("bedw", "birches", "coed bedw"), ("bedwen", "birch tree", "bedwen"), ("bendigaid", "blessed", "bendigaid"), ("betws|bettws", "prayer house, chapel", "tŷ gweddi"),
 ("blaen", "head of a valley, source of a stream", "pen cwm, tarddle"), ("blaenau", "uplands, heads of the valleys", "ucheldir"), ("bod", "dwelling", "trigfan"),
 ("braich", "arm, spur of a hill", "braich, ysgwydd mynydd"), ("bro", "vale, region", "bro"), ("bron", "breast of a hill", "bron bryn"), ("brwyn", "rushes", "brwyn"),
 ("bryn", "hill", "bryn"), ("am", "around, near", "am, o gwmpas"), ("bangor", "a wattled fence, the enclosure of a monastery", "ffens blethedig, clawdd mynachlog"), ("bryniau", "hills", "bryniau"), ("buarth", "farmyard, enclosure", "buarth"), ("bwlch", "pass, gap", "bwlch"),
 ("cadair", "chair, seat", "cadair"), ("cae", "field", "cae"), ("caeau", "fields", "caeau"), ("caer", "fort", "caer"), ("cam", "crooked, winding", "cam"),
 ("canol", "middle", "canol"), ("cantref", "a cantref, an old district of a hundred townships", "cantref"), ("capel", "chapel", "capel"),
 ("carn", "cairn, rocky hill", "carn"), ("carnedd", "cairn", "carnedd"), ("carreg", "rock, stone", "carreg"), ("cas", "castle", "castell"), ("castell", "castle", "castell"),
 ("cau", "hollow, enclosed", "cau"), ("cefn", "ridge", "cefn"), ("cellau", "cells, hermits’ huts", "celloedd"), ("celli", "grove", "llwyn"), ("celyn", "holly", "celyn"), ("cerrig", "stones, rocks", "cerrig"),
 ("cil", "nook, retreat", "cilfach"), ("clawdd", "dyke, bank", "clawdd"), ("clun", "meadow", "dôl"), ("cnwc", "hillock", "bryncyn"), ("coch", "red", "coch"),
 ("coed", "wood, trees", "coed"), ("cored", "weir", "cored"), ("cors", "bog", "cors"), ("craig", "rock, crag", "craig"), ("crib", "crest, ridge", "crib"),
 ("croes", "cross, crossroads", "croes"), ("crug", "mound, cairn", "crug"), ("crwys", "cross", "croes"), ("cul", "narrow", "cul"), ("cwm", "valley", "cwm"),
 ("cwrt", "court, yard", "cwrt"), ("cyll", "hazels", "coed cyll"), ("cymer|cymmer", "confluence, where rivers meet", "cymer"), ("dan", "under, below", "dan"),
 ("dau", "two", "dau"), ("deri", "oaks", "coed derw"), ("derw", "oaks", "coed derw"), ("derwen", "oak", "derwen"), ("din", "fort", "caer"),
 ("dinas", "fort, city", "caer, dinas"), ("diserth", "hermitage", "meudwyfa"), ("dôl", "meadow", "dôl"), ("drws", "door, pass", "drws, bwlch"),
 ("du", "black, dark", "du"), ("dwfn", "deep", "dwfn"), ("dŵr", "water", "dŵr"), ("dwy", "two", "dwy"), ("dyffryn", "valley floor", "dyffryn"),
 ("eglwys", "church", "eglwys"), ("eira", "snow", "eira"), ("eithin", "gorse", "eithin"), ("erw", "acre", "erw"), ("esgair", "long ridge", "esgair"),
 ("ffair", "fair", "ffair"), ("ffawydd", "beeches", "ffawydd"), ("ffin", "boundary", "ffin"), ("ffordd", "road", "ffordd"), ("ffos", "ditch", "ffos"),
 ("ffridd", "mountain pasture", "ffridd"), ("ffrwd", "stream, torrent", "ffrwd"), ("ffynnon", "spring, well", "ffynnon"), ("garth", "hill, enclosure", "garth"),
 ("garw", "rough", "garw"), ("gefail", "smithy", "gefail"), ("glan", "bank, shore", "glan"), ("glas", "blue, green", "glas"), ("glyn", "glen, valley", "glyn"),
 ("gro", "gravel", "gro"), ("grug", "heather", "grug"), ("grugog", "heathery", "grugog"), ("gwaelod", "bottom", "gwaelod"), ("gwastad", "level ground", "tir gwastad"), ("gwaun", "moor, meadow", "gwaun"),
 ("gwern", "alder marsh", "gwern"), ("gwyn", "white, fair, holy", "gwyn"), ("gwen", "white, fair, holy", "gwen"), ("gwŷdd", "trees, wood", "gwŷdd"),
 ("hafn", "ravine", "hafn"), ("hafod", "summer dwelling", "hafod"), ("heli", "salt water", "heli"), ("helyg", "willows", "helyg"), ("hen", "old", "hen"),
 ("hendre|hendref", "winter home, the old homestead", "hendref"), ("heol", "road, street", "heol"), ("hir", "long", "hir"), ("hydd", "stag", "hydd"),
 ("is", "below, lower", "is"), ("isaf", "lowest", "isaf"), ("isel", "low", "isel"), ("llain", "strip of land", "llain"), ("llan", "church, holy enclosure", "eglwys, tir sanctaidd caeedig"),
 ("llanerch", "clearing, glade", "llannerch"), ("llawr", "floor, level ground", "llawr"), ("llech", "slate, flat stone", "llech"), ("llechwedd", "hillside", "llechwedd"),
 ("llethr", "slope", "llethr"), ("llidiart", "gate", "llidiart"), ("llwch", "pool, lake", "llwch, llyn"), ("llwyd", "grey", "llwyd"), ("llwyn", "grove, bush", "llwyn"),
 ("llydan", "wide", "llydan"), ("llyn", "lake", "llyn"), ("llys", "court, royal hall", "llys"), ("maen", "stone", "maen"), ("maenor|maenol", "manor", "maenor"),
 ("maes", "field, open land", "maes"), ("march", "stallion, horse", "march"), ("mawn", "peat", "mawn"), ("mawr", "big, great", "mawr"), ("meini", "stones", "meini"),
 ("melin", "mill", "melin"), ("melyn", "yellow", "melyn"), ("merthyr", "martyr’s shrine, church", "merthyr, eglwys sant"), ("moch", "pigs", "moch"),
 ("moel", "bare hill", "moel"), ("môr", "sea", "môr"), ("morfa", "sea marsh", "morfa"), ("mur", "wall", "mur"), ("mwyn", "ore", "mwyn"), ("mynach", "monk", "mynach"),
 ("mynachlog", "monastery", "mynachlog"), ("mynwent", "churchyard", "mynwent"), ("mynydd", "mountain", "mynydd"), ("nant", "stream, small valley", "nant"),
 ("neuadd", "hall", "neuadd"), ("newydd", "new", "newydd"), ("odyn", "kiln", "odyn"), ("ogof", "cave", "ogof"), ("onnen", "ash tree", "onnen"),
 ("pandy", "fulling mill", "pandy"), ("pant", "hollow", "pant"), ("parc", "park, field", "parc"), ("pen", "head, top, end", "pen, copa"),
 ("pennant", "head of a valley", "pen y nant"), ("pentre|pentref", "village", "pentref"), ("pistyll", "spout, waterfall", "pistyll"), ("plas", "mansion, hall", "plas"),
 ("pont", "bridge", "pont"), ("porth", "harbour, gateway", "porthladd, mynedfa"), ("pridd", "earth, soil", "pridd"), ("pwll", "pool, pit, hollow", "pwll"),
 ("rhaeadr", "waterfall", "rhaeadr"), ("rhiw", "slope, hill", "rhiw"), ("rhos", "moor, heath", "rhos"), ("rhudd", "red", "rhudd"), ("rhyd", "ford", "rhyd"),
 ("sarn", "causeway, old road", "sarn"), ("sant", "saint", "sant"), ("santes", "saint (a woman)", "santes"), ("sych", "dry", "sych"), ("tafarn", "inn", "tafarn"),
 ("tal", "end, front", "tal"), ("tan", "below, under", "tan"), ("tarren", "rocky hillside", "tarren"), ("tarw", "bull", "tarw"), ("teg", "fair, beautiful", "teg"),
 ("tir", "land", "tir"), ("tomen", "mound", "tomen"), ("ton", "grassland, lea", "ton, tir glas"), ("traeth", "beach", "traeth"), ("tre|tref", "town, homestead", "tref"),
 ("tri", "three", "tri"), ("trum", "ridge", "trum"), ("trwyn", "point, headland", "trwyn"), ("twyn", "hillock", "twyn"), ("tŷ", "house", "tŷ"),
 ("tyddyn|tyn", "smallholding", "tyddyn"), ("uchaf", "highest, upper", "uchaf"), ("uchel", "high", "uchel"), ("uwch", "above, upper", "uwch"),
 ("ych", "ox", "ych"), ("y|yr|r", "the", "y fannod"), ("n", "in (yn, shortened)", "yn (wedi’i dalfyrru)"), ("yn|ym|yng", "in", "yn"), ("ynys", "island, river meadow", "ynys"),
 ("ysbyty", "hospice (of the Knights of St John)", "ysbyty (Marchogion Sant Ioan)"), ("ysgol", "school", "ysgol"), ("ystrad", "vale floor", "llawr dyffryn"),
 ("ystum", "bend in a river", "tro mewn afon"),
]

# the river, and where a meaning is well agreed, what it means
RIVERS = [
 ("aeron", "", ""), ("afan|avon", "", ""), ("alaw", "", ""), ("aled", "", ""), ("alun|alyn", "", ""), ("aman|amman", "", ""), ("arth", "", ""),
 ("banwy", "", ""), ("bargod|bargoed", "", ""), ("braint", "", ""), ("brân", "", ""), ("brefi", "", ""), ("cain", "", ""), ("cammarch", "", ""),
 ("cefni", "", ""), ("cegin", "", ""), ("ceiriog", "", ""), ("cennen", "", ""), ("ceri", "", ""), ("cleddau", "‘sword’", "‘cleddyf’"), ("clwyd", "", ""),
 ("clydach", "", ""), ("clywedog", "", ""), ("colwyn", "", ""), ("conwy|conway", "", ""), ("cothi", "", ""), ("crai", "", ""), ("cych", "", ""),
 ("cynfal", "", ""), ("cynon", "", ""), ("cywyn", "", ""), ("dâr|dare", "", ""), ("daron", "", ""), ("dulais|dulas", "‘black stream’", "‘nant ddu’"),
 ("dwyfor", "", ""), ("dwyryd", "", ""), ("dyfi|dovey", "", ""), ("dyfrdwy|dee", "‘water of the goddess’", "‘dŵr y dduwies’"), ("dysynni", "", ""),
 ("ebwy|ebbw", "", ""), ("edw", "", ""), ("efyrnwy|vyrnwy", "", ""), ("elái|ely", "", ""), ("elan", "", ""), ("elwy", "", ""), ("erch", "", ""),
 ("ewenni", "", ""), ("ffraw", "", ""), ("gafenni|gavenny", "", ""), ("gele", "", ""), ("glaslyn", "‘blue lake’", "‘llyn glas’"), ("grwyne", "", ""),
 ("gwendraeth", "", ""), ("gwili", "", ""), ("gwy|wye", "", ""), ("gwyrfai", "", ""), ("hafren|severn", "", ""), ("hepste", "", ""), ("honddu", "", ""),
 ("irfon", "", ""), ("ithon|ieithon", "", ""), ("leri", "", ""), ("lledr", "", ""), ("llifon", "", ""), ("llugwy", "", ""), ("llwchwr|loughor", "", ""),
 ("llyfni", "", ""), ("llynfi", "", ""), ("machno", "", ""), ("marteg", "", ""), ("mawddach", "", ""), ("mellte", "", ""), ("menai", "", ""),
 ("mynwy|monnow", "", ""), ("nedd|neath", "", ""), ("nyfer|nevern", "", ""), ("ogwen", "", ""), ("orci|orchy", "", ""), ("ogwr|ogmore", "", ""), ("prysor", "", ""),
 ("rheidol", "", ""), ("rhondda", "‘noisy’", "‘swnllyd’"), ("rhymni|rhymney", "", ""), ("sawdde", "", ""), ("seiont", "", ""), ("senni", "", ""),
 ("sirhywi|sirhowy", "", ""), ("soch", "", ""), ("sychan", "", ""), ("taf|taff", "", ""), ("tanat", "", ""), ("tarell", "", ""), ("tawe", "", ""),
 ("teifi", "", ""), ("tryweryn", "", ""), ("twrch", "‘boar’", "‘baedd’"), ("tyleri|tillery", "", ""), ("tywi|towy", "", ""), ("wnion", "", ""),
 ("wysg|usk", "", ""), ("ysgir", "", ""), ("ystwyth", "‘winding’", "‘troellog’"),
]

# saints, people and old lands: (name, English, Welsh)
SAINTS = [
 ("mair", "Saint Mary", "y Santes Fair"), ("mihangel", "Saint Michael", "Mihangel Sant"), ("dewi", "Saint David", "Dewi Sant"),
 ("pedr", "Saint Peter", "Pedr Sant"), ("padarn", "Saint Padarn", "Padarn Sant"), ("teilo", "Saint Teilo", "Teilo Sant"), ("illtud", "Saint Illtud", "Illtud Sant"),
 ("cadog", "Saint Cadog", "Cadog Sant"), ("catwg", "Saint Cadog (Catwg)", "Catwg Sant"), ("collen", "Saint Collen", "Collen Sant"), ("cybi", "Saint Cybi", "Cybi Sant"),
 ("seiriol", "Saint Seiriol", "Seiriol Sant"), ("tudno", "Saint Tudno", "Tudno Sant"), ("tysul", "Saint Tysul", "Tysul Sant"), ("tysilio", "Saint Tysilio", "Tysilio Sant"),
 ("idloes", "Saint Idloes", "Idloes Sant"), ("curig", "Saint Curig", "Curig Sant"), ("cynog", "Saint Cynog", "Cynog Sant"), ("brynach", "Saint Brynach", "Brynach Sant"),
 ("gwrtud|wrtyd", "Saint Gwrtud", "Gwrtud Sant"), ("garmon", "Saint Garmon (Germanus)", "Garmon Sant"), ("elli", "Saint Elli", "Elli Sant"),
 ("elwedd", "Saint Elwedd", "Elwedd Santes"), ("deiniol", "Saint Deiniol", "Deiniol Sant"), ("beuno", "Saint Beuno", "Beuno Sant"), ("cadfan", "Saint Cadfan", "Cadfan Sant"),
 ("gwenfrewi", "Saint Gwenfrewi (Winefride)", "Gwenfrewi Santes"), ("gwynllyw", "Saint Gwynllyw", "Gwynllyw Sant"), ("tegla", "Saint Tegla", "Tegla Santes"),
 ("trillo", "Saint Trillo", "Trillo Sant"), ("tegai", "Saint Tegai", "Tegai Sant"), ("tegfan", "Saint Tegfan", "Tegfan Sant"), ("non", "Saint Non, mother of Dewi", "Non Santes, mam Dewi"),
 ("sannan", "Saint Sannan", "Sannan Sant"), ("asa", "Saint Asaph (Asa)", "Asa Sant"), ("tudwal", "Saint Tudwal", "Tudwal Sant"), ("pedrog", "Saint Pedrog", "Pedrog Sant"),
 ("rhystud", "Saint Rhystud", "Rhystud Sant"), ("rhidian", "Saint Rhidian", "Rhidian Sant"), ("cenydd", "Saint Cenydd", "Cenydd Sant"), ("madog", "Madog, a man’s name (Porthmadog is named after William Madocks, who built it)", "Madog, enw dyn (enwyd Porthmadog ar ôl William Madocks, a’i hadeiladodd)"),
 ("dingad", "Saint Dingad", "Dingad Sant"), ("cathen", "Saint Cathen", "Cathen Sant"), ("sadwrn", "Saint Sadwrn", "Sadwrn Sant"), ("dwynwen", "Saint Dwynwen", "Dwynwen Santes"),
 ("ffraid|sanffraid", "Saint Ffraid (Bride)", "Ffraid Santes"), ("cristiolus", "Saint Cristiolus", "Cristiolus Sant"), ("maelog", "Saint Maelog", "Maelog Sant"),
 ("eilian|elian", "Saint Eilian", "Eilian Sant"), ("pabo", "Saint Pabo", "Pabo Sant"), ("cwyfan", "Saint Cwyfan", "Cwyfan Sant"), ("berres", "Saint Berres", "Berres Sant"),
 ("tybïe", "Saint Tybïe", "Tybïe Santes"), ("gwyndaf|wnda", "Saint Gwyndaf", "Gwyndaf Sant"), ("cynwyd", "Saint Cynwyd", "Cynwyd Sant"), ("ceitho", "Saint Ceitho", "Ceitho Sant"),
 ("carannog|crannog|grannog", "Saint Carannog", "Carannog Sant"), ("tudful|tydfil", "Saint Tudful", "Tudful Santes"), ("gwynno", "Saint Gwynno", "Gwynno Sant"),
 ("ffagan", "Saint Ffagan", "Ffagan Sant"), ("trindod", "the Holy Trinity", "y Drindod Sanctaidd"), ("andras", "Saint Andrew", "Andras Sant"),
 ("steffan", "Saint Stephen", "Steffan Sant"), ("dyfrig", "Saint Dyfrig", "Dyfrig Sant"), ("ilan", "Saint Ilan", "Ilan Sant"), ("myllin", "Saint Myllin", "Myllin Sant"),
 ("cyngar", "Saint Cyngar", "Cyngar Sant"), ("dogfael", "Saint Dogmael", "Dogfael Sant"), ("tudoch", "Saint Dogmael (Tudoch)", "Tudoch Sant"),
 ("gwyddelan", "Saint Gwyddelan", "Gwyddelan Sant"), ("aelhaearn", "Saint Aelhaearn", "Aelhaearn Sant"), ("dydd", "the Taf, in an old form of the river’s name", "Taf, mewn hen ffurf ar enw’r afon"), ("ffestiniog", "Ffestiniog, ‘Ffestin’s land’", "Ffestiniog, ‘tir Ffestin’"), ("cadwaladr", "Cadwaladr, king of Gwynedd", "Cadwaladr, brenin Gwynedd"),
 ("peblig", "Saint Peblig, son of Macsen", "Peblig Sant, mab Macsen"), ("egryn", "Saint Egryn", "Egryn Sant"), ("idan", "Saint Aidan (Idan)", "Idan Sant"),
 ("cyfelach", "Saint Cyfelach", "Cyfelach Sant"), ("sawel", "Saint Samuel (Sawel)", "Sawel Sant"),
 ("barrwg", "Saint Barrwg", "Barrwg Sant"), ("tathan", "Saint Tathan", "Tathan Sant"), ("silin", "Saint Silin", "Silin Sant"),
 ("peris", "Saint Peris", "Peris Sant"), ("cynlais", "Cynlais, a man’s name", "Cynlais, enw dyn"), ("ffili", "Ffili, a man’s name", "Ffili, enw dyn"),
 ("tegid", "Tegid Foel, of the Taliesin story", "Tegid Foel, o stori Taliesin"), ("cynllaith|chynlleth", "Cynllaith, a man’s name", "Cynllaith, enw dyn"),
 ("ymddyfri", "‘among the waters’", "‘ymhlith y dyfroedd’"), ("harlech", "probably ‘fair rock’ (hardd + llech)", "‘llech hardd’ yn ôl pob tebyg"), ("grwst", "Saint Grwst", "Grwst Sant"), ("wyddgrug", "‘the burial mound’ (gŵydd + crug)", "‘y crug claddu’ (gŵydd + crug)"), ("gelert", "Gelert, Llywelyn’s hound in the story (or a saint, Celert)", "Gelert, ci Llywelyn yn y stori (neu sant, Celert)"),
 ("einion", "Einion, a man’s name", "Einion, enw dyn"), ("tudur", "Tudur, a man’s name", "Tudur, enw dyn"), ("rhys", "Rhys, a man’s name", "Rhys, enw dyn"),
 ("hywel", "Hywel, a man’s name", "Hywel, enw dyn"), ("ceredig", "Ceredig, son of Cunedda", "Ceredig fab Cunedda"), ("brychan", "Brychan, king of Brycheiniog", "Brychan, brenin Brycheiniog"),
 ("myrddin", "Myrddin: Welsh tradition links the name with Myrddin; it comes from the Roman Moridunum, ‘sea fort’", "Myrddin: mae traddodiad yn ei gysylltu â Myrddin; daw o’r Rhufeinig Moridunum, ‘caer y môr’"),
 ("arfon", "Arfon, ‘the land facing Môn’", "Arfon, ‘y tir gyferbyn â Môn’"), ("môn", "Môn (Anglesey)", "Môn"), ("gwent", "Gwent", "Gwent"), ("dyfed", "Dyfed", "Dyfed"),
 ("powys", "Powys", "Powys"), ("gwynedd", "Gwynedd", "Gwynedd"), ("ceredigion", "Ceredigion, ‘Ceredig’s land’", "Ceredigion, ‘tir Ceredig’"),
 ("morgannwg", "Morgannwg, ‘Morgan’s land’", "Morgannwg, ‘tir Morgan’"), ("emlyn", "Emlyn, an old cantref, ‘around the valley’", "Emlyn, hen gantref, ‘am y glyn’"),
 ("buallt", "Buellt, ‘cow pasture’ (old cantref)", "Buellt, ‘porfa gwartheg’ (hen gantref)"),
 ("penfro", "Penfro, ‘land’s end’", "Penfro, ‘pen draw’r tir’"), ("gŵyr", "Gŵyr (Gower)", "Gŵyr"),
 ("mechain", "Mechain, an old cantref", "Mechain, hen gantref"), ("eifionydd", "Eifionydd", "Eifionydd"), ("meirion", "Meirion, grandson of Cunedda", "Meirion, ŵyr Cunedda"),
]

ENGLISH = [
 ("wells", "the spa wells: the mid-Wales spa towns took the word in the 1800s, when visitors came to drink the waters",
  "y ffynhonnau: cymerodd trefi sba canolbarth Cymru’r gair yn yr 1800au, pan ddeuai ymwelwyr i yfed y dŵr"),
 ("well", "a spring", "ffynnon"), ("spa", "a spa, healing springs", "sba, ffynhonnau iachus"),
 ("junction", "a railway junction", "cyffordd rheilffordd"), ("road", "road; often a railway station named after the town it led to", "ffordd; gorsaf drên yn aml, wedi’i henwi ar ôl y dref y’i harweiniai iddi"),
 ("bridge", "bridge", "pont"), ("bay", "bay", "bae"), ("town", "town", "tref"), ("new", "new", "newydd"), ("old", "old", "hen"),
 ("upper", "upper", "uchaf"), ("lower", "lower", "isaf"), ("north", "north", "gogledd"), ("south", "south", "de"), ("east", "east", "dwyrain"),
 ("west", "west", "gorllewin"), ("great", "great", "mawr"), ("little", "little", "bach"), ("saint|st", "saint", "sant"), ("church", "church", "eglwys"),
 ("castle", "castle", "castell"), ("haven", "harbour", "hafan"), ("port", "port", "porthladd"), ("hill", "hill", "bryn"), ("green", "village green", "lawnt y pentref"),
 ("cross", "cross, crossroads", "croes"), ("heath", "heath", "rhos"), ("common", "common land", "tir comin"), ("end", "end", "pen"), ("head", "headland", "pentir"),
 ("mountain", "mountain", "mynydd"), ("island", "island", "ynys"), ("vale", "vale", "bro, dyffryn"), ("valley", "valley", "cwm"), ("sands", "sands", "tywod"),
 ("mill|mills", "mill", "melin"), ("park", "park", "parc"), ("harbour", "harbour", "harbwr"), ("point", "headland", "trwyn"), ("ferry", "ferry", "fferi"),
 ("forge", "forge, ironworks", "gefail, gwaith haearn"), ("marsh", "marsh", "cors"), ("moor", "moor", "gwaun"), ("village", "village", "pentref"),
 ("station", "railway station", "gorsaf"), ("halt", "a small railway halt", "arhosfa fach ar y rheilffordd"), ("quay", "quay", "cei"),
 ("ford", "ford", "rhyd"), ("wood", "wood", "coed"), ("forest", "forest", "fforest"), ("hall", "hall", "neuadd"), ("farm", "farm", "fferm"),
 ("field|fields", "field", "cae"), ("brook", "brook", "nant"), ("street", "street", "stryd"), ("colliery", "coal mine", "glofa"), ("docks|dock", "docks", "dociau"),
 ("on", "on", "ar"), ("by", "by, near", "ger"), ("the", "the", "y"), ("in", "in", "yn"), ("of", "of", "o"), ("and", "and", "a"), ("rock", "rock", "craig"),
]

# English and Norse names of Welsh places, matched only as the whole word: (name, English, Welsh)
OLDNAMES = [
 ("builth", "English form of Buallt (Buellt), ‘cow pasture’; in Welsh the town is Llanfair-ym-Muallt", "ffurf Saesneg ar Buallt (Buellt), ‘porfa gwartheg’; Llanfair-ym-Muallt yw’r dref"),
 ("brecon", "English form of Brychan, from Brycheiniog, ‘Brychan’s land’; in Welsh, Aberhonddu", "ffurf Saesneg ar Brychan, o Brycheiniog; Aberhonddu yn Gymraeg"),
 ("cardiff", "English form of Caerdydd, the fort on the Taf", "ffurf Saesneg ar Caerdydd, y gaer ar afon Taf"),
 ("swansea", "Norse, ‘Sveinn’s island’; in Welsh, Abertawe", "Llychlyneg, ‘ynys Sveinn’; Abertawe yn Gymraeg"),
 ("tenby", "English form of Dinbych, ‘little fort’", "ffurf Saesneg ar Dinbych, ‘din bach’"),
 ("newport", "English, ‘new market town’; in Welsh, Casnewydd, ‘new castle’", "Saesneg, ‘tref farchnad newydd’; Casnewydd yn Gymraeg"),
 ("monmouth", "English form of Mynwy, ‘mouth of the Monnow’; in Welsh, Trefynwy", "ffurf Saesneg, ‘aber Mynwy’; Trefynwy yn Gymraeg"),
 ("chepstow", "Old English, ‘market place’; in Welsh, Cas-gwent", "Hen Saesneg, ‘man marchnad’; Cas-gwent yn Gymraeg"),
 ("fishguard", "Norse, ‘fish yard’; in Welsh, Abergwaun", "Llychlyneg, ‘buarth pysgod’; Abergwaun yn Gymraeg"),
 ("haverfordwest", "English, ‘the ford of the he-goats’, with ‘west’ added; in Welsh, Hwlffordd", "Saesneg, ‘rhyd y bychod’; Hwlffordd yn Gymraeg"),
 ("milford", "Norse, ‘the sandbank inlet’; in Welsh, Aberdaugleddau", "Llychlyneg, ‘y gilfach dywodlyd’; Aberdaugleddau yn Gymraeg"),
 ("pembroke", "English form of Penfro, ‘land’s end’", "ffurf Saesneg ar Penfro, ‘pen draw’r tir’"),
 ("carmarthen", "English form of Caerfyrddin", "ffurf Saesneg ar Caerfyrddin"),
 ("cardigan", "English form of Ceredigion, ‘Ceredig’s land’; the town is Aberteifi", "ffurf Saesneg ar Ceredigion; Aberteifi yw’r dref"),
 ("holyhead", "English, ‘holy headland’; in Welsh, Caergybi, ‘Cybi’s fort’", "Saesneg, ‘pentir sanctaidd’; Caergybi yn Gymraeg"),
 ("anglesey", "Norse, ‘Ongull’s island’; in Welsh, Môn", "Llychlyneg, ‘ynys Ongull’; Môn yn Gymraeg"),
 ("mold", "Norman French mont haut, ‘high hill’; in Welsh, Yr Wyddgrug, ‘the burial mound’", "Ffrangeg Normanaidd, ‘bryn uchel’; Yr Wyddgrug yn Gymraeg"),
 ("wrexham", "Old English, ‘Wryhtel’s meadow’; in Welsh, Wrecsam", "Hen Saesneg, ‘dôl Wryhtel’; Wrecsam yn Gymraeg"),
 ("welshpool", "English, ‘the pool in Wales’; in Welsh, Y Trallwng", "Saesneg, ‘y pwll yng Nghymru’; Y Trallwng yn Gymraeg"),
 ("newcastle", "English, ‘new castle’; in Welsh, Castellnewydd", "Saesneg, ‘castell newydd’; Castellnewydd yn Gymraeg"), ("newtown", "English; in Welsh, Y Drenewydd, ‘the new town’", "Saesneg; Y Drenewydd yn Gymraeg"),
 ("knighton", "English; in Welsh, Tref-y-clawdd, ‘the town on the Dyke’", "Saesneg; Tref-y-clawdd yn Gymraeg"),
 ("presteigne", "English, ‘the priests’ household’; in Welsh, Llanandras, ‘Andrew’s church’", "Saesneg; Llanandras yn Gymraeg"),
 ("hay", "English, ‘enclosed forest’; in Welsh, Y Gelli Gandryll", "Saesneg, ‘coedwig gaeedig’; Y Gelli Gandryll yn Gymraeg"),
 ("rhayader", "English form of Rhaeadr, ‘waterfall’", "ffurf Saesneg ar Rhaeadr"),
 ("crickhowell", "English form of Crucywel, ‘Hywel’s mound’", "ffurf Saesneg ar Crucywel, ‘crug Hywel’"),
 ("caerleon", "English form of Caerllion, ‘fort of the legions’", "ffurf Saesneg ar Caerllion, ‘caer y llengoedd’"),
 ("cowbridge", "English; in Welsh, Y Bont-faen, ‘the stone bridge’", "Saesneg; Y Bont-faen yn Gymraeg"),
 ("bridgend", "English; in Welsh, Pen-y-bont ar Ogwr, ‘end of the bridge on the Ogwr’", "Saesneg; Pen-y-bont ar Ogwr yn Gymraeg"),
 ("kidwelly", "English form of Cydweli", "ffurf Saesneg ar Cydweli"), ("laugharne", "English form of Talacharn", "ffurf Saesneg ar Talacharn"),
 ("lampeter", "English form of Llanbedr, ‘Peter’s church’; in Welsh, Llanbedr Pont Steffan", "ffurf Saesneg ar Llanbedr Pont Steffan"),
 ("denbigh", "English form of Dinbych, ‘little fort’", "ffurf Saesneg ar Dinbych, ‘din bach’"),
 ("ruthin", "English form of Rhuthun, probably ‘red fort’", "ffurf Saesneg ar Rhuthun, ‘din rhudd’ yn ôl pob tebyg"),
 ("barmouth", "English form of Abermaw, from Abermawddach, ‘mouth of the Mawddach’", "ffurf Saesneg ar Abermaw (Abermawddach)"),
 ("towyn", "English spelling of Tywyn, ‘sand dune’", "sillafiad Saesneg ar Tywyn, ‘twyni tywod’"),
 ("dolgelley", "old English spelling of Dolgellau, ‘meadow of the cells’", "hen sillafiad Saesneg ar Dolgellau"),
 ("portmadoc", "old English spelling of Porthmadog", "hen sillafiad Saesneg ar Porthmadog"),
 ("wrecsam", "Welsh spelling of Wrexham, Old English, ‘Wryhtel’s meadow’", "sillafiad Cymraeg ar Wrexham, ‘dôl Wryhtel’"),
 ("rhuthun", "probably ‘red fort’ (rhudd + din)", "‘din rhudd’ yn ôl pob tebyg"), ("flint", "English, ‘hard rock’; in Welsh, Y Fflint", "Saesneg, ‘craig galed’; Y Fflint yn Gymraeg"),
 ("davids", "Saint David (Dewi); in Welsh, Tyddewi, ‘David’s house’", "Dewi Sant; Tyddewi yn Gymraeg"),
 ("asaph", "Saint Asaph (Asa); in Welsh, Llanelwy, ‘church on the Elwy’", "Asa Sant; Llanelwy yn Gymraeg"),
 ("fagans", "Saint Ffagan; in Welsh, Sain Ffagan", "Ffagan Sant; Sain Ffagan yn Gymraeg"),
 ("dogmaels", "Saint Dogmael; in Welsh, Llandudoch", "Dogfael Sant; Llandudoch yn Gymraeg"),
 ("clears", "Saint Clear; in Welsh, Sanclêr", "Sant Clêr; Sanclêr yn Gymraeg"),
 ("athan", "Saint Tathan; in Welsh, Sain Tathan", "Tathan Sant; Sain Tathan yn Gymraeg"),
 ("gower", "English form of Gŵyr", "ffurf Saesneg ar Gŵyr"), ("snowdon", "English, ‘snow hill’; in Welsh, Yr Wyddfa", "Saesneg, ‘bryn yr eira’; Yr Wyddfa yn Gymraeg"),
 ("snowdonia", "English; in Welsh, Eryri", "Saesneg; Eryri yn Gymraeg"),
 ("neath", "English form of Nedd, the river", "ffurf Saesneg ar Nedd"), ("usk", "English form of Wysg, the river", "ffurf Saesneg ar Wysg"),
 ("barry", "English form of Y Barri, probably from Saint Barrwg", "ffurf Saesneg ar Y Barri, o Barrwg Sant yn ôl pob tebyg"),
 ("ebbw", "English form of Ebwy, the river", "ffurf Saesneg ar Ebwy"),
]

# names to try, under the decoder
SAMPLES = ["Llangammarch Wells", "Pontrhydfendigaid", "Betws-y-Coed", "Llanfair Caereinion", "Aberystwyth", "Builth Wells",
           "Llanfairpwllgwyngyll", "Pen-y-bont", "Abergavenny", "Llandrindod Wells", "Caerdydd", "Merthyr Tudful"]


def data(towns=()):
    """Everything placenames.js needs, as plain lists. `towns` is [en, cy, meaning en, meaning cy, id] for whole names."""
    rows = [[w, en, cy, "w"] for w, en, cy in WORDS]
    rows += [[w, en, cy, "r"] for w, en, cy in RIVERS]
    rows += [[w, en, cy, "s"] for w, en, cy in SAINTS if en]
    rows += [[w, en, cy, "e"] for w, en, cy in ENGLISH]
    rows += [[w, en, cy, "n"] for w, en, cy in OLDNAMES]
    return dict(W=rows, T=[list(t) for t in towns], S=SAMPLES)


def glossary():
    """The ordinary words, for the list at the foot of towns.html: (word, English, Welsh), first spelling only."""
    return [(w.split("|")[0], en, cy) for w, en, cy in WORDS]
