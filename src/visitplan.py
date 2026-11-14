"""Plan a day out (visit.html) and the ready-made days out (visit-<area>.html). Ifan, 14 November 2026.

Pick a town, an area or your own location, say how long you have and what you like, and the planner makes a day's
route of historic places you can visit: the order to see them in, the drive between each, how long to spend at each,
who looks after it, how you get in, and a link to the official page for opening times. It prints, with its map.

Where the stops come from
  - every place on the map that has a Visiting box (src/data.py places, src/visit.py), linked to its own page;
  - the sites Cadw looks after that have no place page yet (tools/data/sites_guardian.json), linked to Cadw's own page
    (CADW_SLUG below; the slugs come from cadw.gov.wales/visit/places-to-visit/find-a-place-to-visit/map);
  - a few great houses, castles and museums run by others (EXTRA below).
Opening times and prices are never copied (they change): every stop links its official page.

How a day is made (the same steps in plan() here and in src/static/visitplan.js; tools/visit_check.js checks they agree)
  1. Drive times are estimates: the straight-line distance times 1.3 for winding roads, at 48 km/h, plus 5 minutes to park,
     rounded to 5 minutes. An estuary with no bridge near its mouth (BARRIERS) sends the line round by its first bridge.
  2. Candidates are the sites within reach (RADIUS) that match the chosen interests and entry.
  3. Stops are added one at a time where they cost least: each try scores weight^1.5 / (minutes there + 3 x extra driving + 20), and the best
     that still fits the day is kept, until the day is full or has its most stops.
  4. The order is then tidied (2-opt) so the drive is as short as it can be, and the day ends back at the start.
A ready-made day (AREAS) is the plan for a full day from the area's town, with every interest, starting at 10:00.
"""
import json
import math
import os

g = {}


def setup(build_globals):
    g.update(build_globals)


# ---------- what people like: the interest chips ----------
KINDS = [
    ("castles", "Castles and courts", "Cestyll a llysoedd", "castle"),
    ("faith", "Saints, churches and abbeys", "Seintiau, eglwysi ac abatai", "cross"),
    ("early", "Tombs, stones and hillforts", "Beddrodau, meini a bryngaerau", "dolmen"),
    ("roman", "Roman Wales", "Cymru Rufeinig", "arches"),
    ("work", "Industry, slate and coal", "Diwydiant, llechi a glo", "wheel"),
    ("culture", "Great houses, museums and modern Wales", "Plastai, amgueddfeydd a Chymru fodern", "harp"),
]
KIX = {k[0]: i for i, k in enumerate(KINDS)}

LENGTHS = {  # key: (English, Welsh, minutes of driving and visiting, most stops, how far to look in km, lunch)
    "half": ("Half a day", "Hanner diwrnod", 210, 3, 25, False),
    "day": ("A full day", "Diwrnod cyfan", 360, 5, 40, True),
    "long": ("A long day", "Diwrnod hir", 480, 7, 55, True),
}
LUNCH = 45
ROAD, KMH, PARK = 1.3, 48.0, 5.0

# Estuaries with no road across near the mouth: (lat, lon of the mouth), (lat, lon of the head), and the bridges round it.
BARRIERS = [
    ((52.530, -4.075), (52.586, -3.870), [(52.596, -3.855)]),                      # Dyfi: round by Machynlleth
    ((52.712, -4.060), (52.745, -3.945), [(52.7465, -3.937), (52.743, -3.886)]),   # Mawddach: Penmaenpool or Dolgellau
    ((52.900, -4.140), (52.940, -4.010), [(52.931, -4.066)]),                      # Dwyryd: Pont Briwet
    ((51.735, -4.380), (51.848, -4.305), [(51.854, -4.305)]),                      # Tywi: Carmarthen
    ((51.745, -4.430), (51.815, -4.495), [(51.818, -4.497)]),                      # Taf: St Clears
    ((51.620, -4.300), (51.660, -4.080), [(51.664, -4.076)]),                      # Llwchwr: Loughor
    ((51.695, -5.160), (51.708, -4.945), [(51.709, -4.943)]),                      # Milford Haven: the Cleddau Bridge
    ((52.115, -4.700), (52.084, -4.663), [(52.083, -4.660)]),                      # Teifi: Cardigan
    ((53.300, -3.850), (53.226, -3.817), [(53.281, -3.827), (53.226, -3.812)]),    # Conwy: Conwy or Tal-y-cafn
    ((53.130, -4.330), (53.310, -4.030), [(53.222, -4.163), (53.216, -4.186)]),    # Menai: the two bridges
]


# ---------- the Cadw sites with no place page yet: Cadw's own page for each ----------
CADW_SLUG = {
    "Bodowyr Burial Chamber": "bodowyr-chambered-tomb", "Bronllys Castle": "castell-bronllys", "Bryntail Lead Mine": "bryn-tail-leadworks",
    "Bulwarks Camp": "bulwarks-prehistoric-enclosure", "Caer Leb": "caer-leb-romano-british-farm", "Caergwrle Castle": "castell-caergwrle",
    "Capel Garmon Burial Chamber": "capel-garmon-chambered-tomb", "Carreg Coetan Burial Chamber": "carreg-coetan-arthur-chambered-tomb",
    "Carswell Old House": "carswell-medieval-house", "Castell Bryn-Gwyn": "castell-bryngwyn-prehistoric-enclosure", "Castell Coch": "castell-coch",
    "Churchyard Cross, Derwen": "derwen-cross", "Cilgerran Castle": "castell-cilgerran", "Coity Castle": "castell-coety",
    "Denbigh Castle and Medieval Town": "denbigh-castle", "Denbigh Friary": "denbigh-friary-church", "Denbigh Town Wall": "denbigh-town-walls",
    "Din Dryfol Burial Chamber": "din-dryfol-chambered-tomb", "Dyffryn Burial Chamber": "dyffryn-ardudwy-chambered-tomb",
    "Dyfi Blast Furnace and Charcoal Store": "dyfi-furnace", "Ewenny Priory": "ewenni-priory", "Ffynnon Gybi": "st-cybis-well",
    "Flint Castle": "flint-castle", "Grosmont Castle": "grosmont-castle", "Gwydir Uchaf Chapel": "capel-gwydir-uchaf",
    "Hafoty Old Farm House": "hafoty-medieval-house", "Haverfordwest Priory": "haverfordwest-priory", "Hen Gwrt Moated Site": "hen-gwrt-medieval-moated-site",
    "Lamphey Palace": "lamphey-bishops-palace", "Leicester's Church": "earl-leicesters-church", "Llangar Old Parish Church & Churchyard": "llangar-old-church",
    "Llansteffan Castle": "castell-llansteffan", "Llawhaden Castle": "llawhaden-castle", "Loughor Castle": "loughor-castle",
    "Monmouth Castle": "monmouth-castle", "Montgomery Castle": "montgomery-castle", "Newcastle Castle": "newcastle-castle", "Ogmore Castle": "ogmore-castle",
    "Old Beaupre Castle": "old-beaupre-castle", "Oxwich Castle": "castell-oxwich", "Penarth Fawr Medieval Hall": "pennarth-fawr",
    "Penrhos Feilw Standing Stones": "penrhosfeilw-standing-stones", "Pen-y-Wyrlod Long Barrow": "", "Pont Minllyn": "pont-minllyn",
    "Presaddfed Burial Chamber": "presaddfed-chambered-tomb", "Rug Chapel": "rug-chapel", "Runston Medieval Village Site & Runston Chapel": "runston-church",
    "Skenfrith Castle": "skenfrith-castle", "St Dogmaels Abbey": "st-dogmaels-abbey-and-coach-house", "St Hilary's Chapel Tower": "st-hilarys-chapel",
    "St Lythan's Burial Chamber": "st-lythans-chambered-tomb", "St Quintin's Castle": "llanblethian-castle", "Swansea Castle": "swansea-castle",
    "Trefignath Burial Chamber": "trefignath-chambered-tomb", "Tregwehelydd Standing Stone": "tregwehelydd-standing-stone",
    "Ty-Mawr Standing Stone": "ty-mawr-standing-stone", "Ty-Newydd Burial Chamber": "ty-newydd-chambered-tomb", "Castell Weobley": "weobley-castle",
    "White Castle": "white-castle", "Wiston Castle": "wiston-castle", "Cae'r Gors": "caer-gors",
}
# Cadw sites already on the map under another name, or not open (left out)
CADW_SKIP = {"Cymer Abbey", "Maen Achwyfan", "The Gaer, Brecon", "Heritage Cottage", "Caerau Roman Site", "Ogmore Stepping Stones", "Fedw-Deg Old House"}
# their pictures, from the gallery (src/gallery_photos.py)
CADW_PIC = {"Castell Coch": "cast-castell-coch", "Cilgerran Castle": "cast-cilgerran", "Denbigh Castle and Medieval Town": "cast-denbigh",
            "Flint Castle": "cast-flint", "Llansteffan Castle": "cast-llansteffan", "White Castle": "cast-white-castle", "Presaddfed Burial Chamber": "anci-presaddfed"}
CADW_KIND = {"burial": "early", "stones": "early", "forts": "early", "roman": "roman", "crosses": "faith", "faith": "faith", "castles": "castles",
             "dykes": "early", "industry": "work", "war": "culture", "other": "culture"}
CADW_NAME_FIX = {"Castell Weobley": ("Weobley Castle", "Castell Weble"), "Leicester's Church": ("The Earl of Leicester’s Church, Denbigh", None),
                 "Churchyard Cross, Derwen": ("Derwen Cross", "Croes Derwen"), "Denbigh Castle and Medieval Town": ("Denbigh Castle", None)}

# ---------- great houses, castles and museums run by others ----------
NT = "https://www.nationaltrust.org.uk/visit/wales/"
# id: (English, Welsh, lat, lon, kind, who (en, cy), official page, postcode, entry, line en, line cy, gallery picture, minutes, weight)
EXTRA = {
    "x-cardiffcastle": ("Cardiff Castle", "Castell Caerdydd", 51.4822, -3.1812, "castles", ("Cardiff Council", "Cyngor Caerdydd"), "https://www.cardiffcastle.com/",
                        "CF10 3RB", "ticket", "A Roman fort, a Norman keep and a Victorian dream palace in the heart of the capital.",
                        "Caer Rufeinig, gorthwr Normanaidd a phalas breuddwydiol o oes Victoria yng nghanol y brifddinas.", "cast-cardiff-castle", 120, 4),
    "x-museumcardiff": ("National Museum Cardiff", "Amgueddfa Genedlaethol Caerdydd", 51.4858, -3.1774, "culture", ("Amgueddfa Cymru – Museum Wales", "Amgueddfa Cymru"),
                        "https://museum.wales/cardiff/", "CF10 3NP", "free", "The treasures of the nation, from the gold of the Bronze Age to the art of Wales.",
                        "Trysorau’r genedl, o aur Oes yr Efydd i gelf Cymru.", "buil-national-museum", 120, 3),
    "x-plasnewydd": ("Plas Newydd, Anglesey", "Plas Newydd, Ynys Môn", 53.2047, -4.2149, "culture", ("the National Trust", "yr Ymddiriedolaeth Genedlaethol"),
                     NT + "plas-newydd-house-and-garden", "LL61 6DQ", "ticket", "The home of the Marquesses of Anglesey on the Menai Strait, with Rex Whistler’s great painted room.",
                     "Cartref Ardalyddion Môn ar lan Afon Menai, gydag ystafell fawr Rex Whistler wedi’i pheintio.", None, 120, 3),
    "x-tredegar": ("Tredegar House", "Tŷ Tredegar", 51.5627, -3.0310, "culture", ("the National Trust", "yr Ymddiriedolaeth Genedlaethol"),
                   NT + "tredegar-house/index", "NP10 8YW", "ticket", "The red-brick mansion of the Morgans of Tredegar, one of the great families of Wales.",
                   "Plasty brics coch Morganiaid Tredegar, un o deuluoedd mawr Cymru.", "buil-tredegar-house", 105, 3),
    "x-aberdulais": ("Aberdulais Tin Works and Waterfall", "Gwaith Tun a Rhaeadr Aberdulais", 51.6806, -3.7743, "work", ("the National Trust", "yr Ymddiriedolaeth Genedlaethol"),
                     NT + "aberdulais", "SA10 8EU", "ticket", "Works driven by the waterfall: copper was smelted here from 1584, and tinplate made later.",
                     "Gweithfeydd a yrrwyd gan y rhaeadr: toddwyd copr yma o 1584, a gwnaed tunplat yn ddiweddarach.", None, 75, 2.5),
    "x-llanerchaeron": ("Llanerchaeron", "Llanerchaeron", 52.2167, -4.2183, "culture", ("the National Trust", "yr Ymddiriedolaeth Genedlaethol"),
                        NT + "llanerchaeron", "SA48 8DG", "ticket", "A Welsh gentry estate of the 1790s by John Nash, with its home farm and walled gardens.",
                        "Ystâd bonedd Cymreig o’r 1790au gan John Nash, gyda’i fferm a’i gerddi muriog.", None, 105, 2.5),
    "x-carew": ("Carew Castle", "Castell Caeriw", 51.6985, -4.8302, "castles", ("the Pembrokeshire Coast National Park", "Parc Cenedlaethol Arfordir Penfro"),
                "https://www.pembrokeshirecoast.wales/carew-castle/", "SA70 8SL", "ticket",
                "A castle that became a great Tudor house: Sir Rhys ap Thomas held his famous tournament here in 1507.",
                "Castell a ddaeth yn blasty Tuduraidd mawr: cynhaliodd Syr Rhys ap Thomas ei dwrnamaint enwog yma yn 1507.", "cast-carew", 90, 3),
    "x-manorbier": ("Manorbier Castle", "Castell Maenorbŷr", 51.6451, -4.7987, "castles", ("private owners", "perchnogion preifat"), "https://www.manorbiercastle.co.uk/",
                    "SA70 7SY", "ticket", "The birthplace of Gerald of Wales, who called it the pleasantest spot in all Wales.",
                    "Man geni Gerallt Gymro, a’i galwodd y llecyn mwyaf dymunol yng Nghymru gyfan.", "cast-manorbier", 75, 3),
    "x-waterfront": ("National Waterfront Museum", "Amgueddfa Genedlaethol y Glannau", 51.6173, -3.9396, "work", ("Amgueddfa Cymru – Museum Wales", "Amgueddfa Cymru"),
                     "https://museum.wales/swansea/", "SA1 3RD", "free", "Three hundred years of Welsh industry and invention, on Swansea’s waterfront.",
                     "Tri chan mlynedd o ddiwydiant a dyfeisgarwch Cymru, ar lan y dŵr yn Abertawe.", None, 90, 2.5),
    "x-wool": ("National Wool Museum", "Amgueddfa Wlân Cymru", 52.0283, -4.3929, "work", ("Amgueddfa Cymru – Museum Wales", "Amgueddfa Cymru"),
               "https://museum.wales/wool/", "SA44 5UP", "free", "In the Teifi valley, once the heart of the Welsh woollen trade, in a mill that still weaves.",
               "Yn nyffryn Teifi, a fu’n galon y fasnach wlân Gymreig, mewn melin sy’n dal i wehyddu.", None, 75, 2.5),
}

# Places on the map that a day out cannot include (a boat to book, private land with nothing to see, no visit at all)
NOT_A_STOP = {"enlli", "epynt", "penygwryd", "cerrigbach", "pontnewydd", "offasdyke"}
# How long to spend, where the rule of thumb is wrong (minutes)
MINS = {"dinasemrys": 75, "trerceiri": 90, "caerytwr": 75, "carregcennen": 90, "stfagans": 180, "bigpit": 150, "caernarfon": 105, "conwy": 105,
        "caerffili": 105, "treffynnon": 45, "rhaglan": 90, "tintern": 75, "stdavids": 90, "blaenavon": 75, "orme": 75, "dolaucothi": 105, "castellhenllys": 90,
        "botanic": 120, "library": 60, "dinorwig": 60, "senedd": 45, "wmc": 30, "stadiwm": 75, "dinasbran": 75, "pontcysyllte": 45, "yrysgwrn": 75}
# The best known: these win a place in a day before smaller sites nearby
FLAGSHIP = {"caernarfon", "conwy", "harlech", "beaumaris", "caerffili", "stdavids", "tintern", "rhaglan", "stfagans", "bigpit", "pentreifan",
            "brynceliddu", "chepstow", "pembroke", "penfro", "carregcennen", "strataflorida", "powis", "chirk", "penrhyn", "kidwelly", "caerleon",
            "dinefwr", "llandaf", "valle", "vallecrucis", "dolwyddelan", "ybere", "plasmawr", "blaenavon", "pontcysyllte", "segontium", "tinkinswood"}

# ---------- the ready-made days out ----------
# id, English, Welsh, start (English, Welsh, lat, lon), a line about the area (en, cy), its picture (a place id), its stops (stop ids;
# the planner puts them in the best order and works out the times)
AREAS = [
    ("mon", "Anglesey", "Ynys Môn", ("Llangefni", "Llangefni", 53.256, -4.311),
     "Môn Mam Cymru: tombs older than the pyramids, the courts of the princes of Gwynedd and the last of Edward I’s castles.",
     "Môn Mam Cymru: beddrodau hŷn na’r pyramidiau, llysoedd tywysogion Gwynedd a’r olaf o gestyll Edward I.", "brynceliddu", "brynceliddu llysrhosyr beaumaris penmon"),
    ("eryri", "Caernarfon and Eryri", "Caernarfon ac Eryri", ("Caernarfon", "Caernarfon", 53.140, -4.273),
     "The Roman fort of Segontium, the castles of the princes in the mountains, and the slate that roofed the world.",
     "Caer Rufeinig Segontium, cestyll y tywysogion yn y mynyddoedd, a’r llechi a doiodd y byd.", "dolbadarn", "caernarfon segontium dolbadarn dinorwig"),
    ("llyn", "Llŷn and Eifionydd", "Llŷn ac Eifionydd", ("Criccieth", "Cricieth", 52.918, -4.233),
     "The pilgrims’ road to Enlli, the hillfort town of Tre’r Ceiri, and Cricieth on its rock above the bay.",
     "Ffordd y pererinion i Enlli, tref fryngaer Tre’r Ceiri, a Chricieth ar ei chraig uwchben y bae.", "cricieth", "cricieth llanystumdwy clynnog trerceiri"),
    ("conwy", "Conwy and the north coast", "Conwy a’r arfordir", ("Conwy", "Conwy", 53.280, -3.829),
     "A walled town and its castle, Plas Mawr, the court of Garth Celyn and the Bronze Age mines of the Great Orme.",
     "Tref gaerog a’i chastell, Plas Mawr, llys Garth Celyn a mwyngloddiau Oes yr Efydd ar y Gogarth.", "conwy", "conwy plasmawr garthcelyn orme"),
    ("clwyd", "Denbigh and the Vale of Clwyd", "Dinbych a Dyffryn Clwyd", ("Denbigh", "Dinbych", 53.184, -3.420),
     "Dafydd ap Gruffudd’s Denbigh, the cathedral of St Asaph, Rhuddlan and the holy well of St Winefride.",
     "Dinbych Dafydd ap Gruffudd, eglwys gadeiriol Llanelwy, Rhuddlan a ffynnon sanctaidd Gwenfrewi.", "rhuddlan", "c-denbigh-castle llanelwy rhuddlan treffynnon basingwerk"),
    ("llangollen", "Llangollen and the Dee", "Llangollen a’r Ddyfrdwy", ("Llangollen", "Llangollen", 52.970, -3.170),
     "Castell Dinas Brân, the Pillar of Eliseg, Valle Crucis, Glyndŵr’s Sycharth and Telford’s aqueduct.",
     "Castell Dinas Brân, Piler Eliseg, Glyn y Groes, Sycharth Glyndŵr a thraphont ddŵr Telford.", "dinasbran", "dinasbran vallecrucis eliseg pontcysyllte chirk"),
    ("meirionnydd", "Meirionnydd", "Meirionnydd", ("Dolgellau", "Dolgellau", 52.743, -3.885),
     "Harlech and Castell y Bere, the abbey of Cymer, and the old farmhouses and tombs of Ardudwy.",
     "Harlech a Chastell y Bere, abaty Cymer, a hen ffermdai a beddrodau Ardudwy.", "ybere", "cymer ybere harlech c-dyffryn-ardudwy-chambered-tomb"),
    ("maldwyn", "Montgomeryshire", "Maldwyn", ("Welshpool", "Y Trallwng", 52.660, -3.147),
     "Powis Castle, Dolforwyn of Llywelyn ap Gruffudd, Mathrafal of the kings of Powys and the shrine of Melangell.",
     "Castell Powis, Dolforwyn Llywelyn ap Gruffudd, Mathrafal brenhinoedd Powys a chysegrfa Melangell.", "powis", "powis c-montgomery-castle dolforwyn pennantmelangell"),
    ("ceredigion", "Aberystwyth and Ceredigion", "Aberystwyth a Cheredigion", ("Aberystwyth", "Aberystwyth", 52.415, -4.083),
     "The National Library, Llanbadarn Fawr, Strata Florida of the princes and poets, and Llangeitho of the Revival.",
     "Y Llyfrgell Genedlaethol, Llanbadarn Fawr, Ystrad Fflur y tywysogion a’r beirdd, a Llangeitho’r Diwygiad.", "strataflorida", "library llanbadarn strataflorida llangeitho"),
    ("teifi", "Cardigan and the Teifi", "Aberteifi a Dyffryn Teifi", ("Cardigan", "Aberteifi", 52.083, -4.660),
     "Where the first eisteddfod was held in 1176, with Cilgerran, St Dogmaels, Nevern and the Iron Age village of Castell Henllys.",
     "Lle cynhaliwyd yr eisteddfod gyntaf yn 1176, gyda Chilgerran, Llandudoch, Nanhyfer a phentref Oes yr Haearn Castell Henllys.", "cardigan", "cardigan c-castell-cilgerran c-st-dogmaels-abbey-and-coach-house castellhenllys pentreifan"),
    ("stdavids", "St Davids and north Pembrokeshire", "Tyddewi a gogledd Sir Benfro", ("St Davids", "Tyddewi", 51.882, -5.266),
     "The city of Dewi Sant, St Non’s chapel, Pentre Ifan and the coast where the last invasion of Britain landed.",
     "Dinas Dewi Sant, capel Non, Pentre Ifan a’r arfordir lle glaniodd y goresgyniad olaf ar Brydain.", "stdavids", "stdavids stnons carregsamson fishguard"),
    ("penfro", "Pembroke and the south", "Penfro a’r de", ("Pembroke", "Penfro", 51.674, -4.915),
     "Pembroke, where Henry Tudor was born, the Carew Cross of King Maredudd, Manorbier and the bishops’ palace at Lamphey.",
     "Penfro, lle ganwyd Harri Tudur, Croes Caeriw y Brenin Maredudd, Maenorbŷr a llys yr esgobion yn Llandyfái.", "penfro", "penfro c-lamphey-bishops-palace carewcross x-carew x-manorbier"),
    ("tywi", "Llandeilo and the Tywi valley", "Llandeilo a Dyffryn Tywi", ("Llandeilo", "Llandeilo", 51.884, -3.993),
     "Dinefwr, the seat of the princes of Deheubarth, with Dryslwyn, Carreg Cennen and the abbey of Talley.",
     "Dinefwr, llys tywysogion Deheubarth, gyda Dryslwyn, Carreg Cennen ac abaty Talyllychau.", "dinefwr", "dinefwr dryslwyn carregcennen talley"),
    ("brecon", "Brecon and the Black Mountains", "Aberhonddu a’r Mynyddoedd Duon", ("Brecon", "Aberhonddu", 51.947, -3.391),
     "The Roman fort of Y Gaer, Tretower Court, Llanthony Priory and Trefeca of Howell Harris.",
     "Caer Rufeinig Y Gaer, Llys Tretŵr, Priordy Llanddewi Nant Hodni a Threfeca Howell Harris.", "tretower", "ygaer tretower llanthony trefeca"),
    ("gower", "Swansea and Gower", "Abertawe a Gŵyr", ("Swansea", "Abertawe", 51.620, -3.944),
     "Paviland, Maen Ceti and Parc le Breos, the castles of Gower and the copperworks that made Swansea ‘Copperopolis’.",
     "Pafiland, Maen Ceti a Pharc le Breos, cestyll Gŵyr a’r gweithfeydd copr a wnaeth Abertawe’n ‘Copperopolis’.", "maenceti", "hafod parclebreos maenceti c-weobley-castle c-castell-oxwich"),
    ("cardiff", "Cardiff and the Vale", "Caerdydd a’r Fro", ("Cardiff", "Caerdydd", 51.481, -3.179),
     "The capital’s castle and museums, St Fagans, Llandaf, Tinkinswood and the old schools of Llanilltud Fawr.",
     "Castell ac amgueddfeydd y brifddinas, Sain Ffagan, Llandaf, Tinkinswood a hen ysgolion Llanilltud Fawr.", "stfagans", "x-cardiffcastle llandaf stfagans"),
    ("valleys", "The Valleys", "Y Cymoedd", ("Merthyr Tydfil", "Merthyr Tudful", 51.746, -3.378),
     "The iron and coal that made the modern world: Merthyr, Big Pit, Blaenavon, and the castle of Caerphilly.",
     "Yr haearn a’r glo a wnaeth y byd modern: Merthyr, y Pwll Mawr, Blaenafon, a chastell Caerffili.", "bigpit", "merthyr aberfan bigpit blaenavon"),
    ("gwent", "Monmouth and the Wye", "Trefynwy a Gwy", ("Monmouth", "Trefynwy", 51.811, -2.716),
     "Raglan, Tintern, the Three Castles, Chepstow, and Roman Caerwent and Caerleon.",
     "Rhaglan, Tyndyrn, y Tri Chastell, Cas-gwent, a Chaer-went a Chaerllion Rhufeinig.", "rhaglan", "rhaglan tintern c-white-castle c-skenfrith-castle"),
]


# ---------- the planner: the same steps as src/static/visitplan.js ----------
def _km(a, b):
    """Great-circle distance in km between (lat, lon) pairs."""
    la1, lo1, la2, lo2 = (math.radians(x) for x in (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 12742.0 * math.asin(min(1.0, math.sqrt(h)))


def _cross(p, q, r, s):
    """Do the segments p-q and r-s cross? (on a flat map with longitude squeezed)"""
    def o(a, b, c):
        return (b[1] * .61 - a[1] * .61) * (c[0] - a[0]) - (b[0] - a[0]) * (c[1] * .61 - a[1] * .61)
    return (o(p, q, r) > 0) != (o(p, q, s) > 0) and (o(r, s, p) > 0) != (o(r, s, q) > 0)


def road_km(a, b):
    d = _km(a, b)
    for m, hd, bridges in BARRIERS:
        if _cross(a, b, m, hd):
            d = min(_km(a, x) + _km(x, b) for x in bridges)
            break
    return d * ROAD


def r5(x):
    return math.floor(x / 5.0 + 0.5) * 5


def drive(a, b):
    return r5(road_km(a, b) / KMH * 60.0 + PARK)


def plan(sites, start, length="day", kinds=None, free=False, outside=False, exclude=(), first=None, pins=(), fill=True):
    """The stops of a day (indexes into sites, in order). sites: dicts with lat, lon, k (kind), m (minutes), w (weight),
    e (entry key), id. start: (lat, lon). first: a site that is the start and the first stop. pins: sites the day must
    include (a ready-made day, or the stops kept when one is swapped). fill: add more stops while the day has room."""
    budget, most, radius, _ = LENGTHS[length][2:]
    kinds = set(kinds) if kinds else set(range(len(KINDS)))
    ex = set(exclude)
    pos = [(s["lat"], s["lon"]) for s in sites]
    route = [first] if first is not None else []
    for j in pins:
        if j not in route and sites[j]["id"] not in ex:
            route.append(j)
    cand = []
    for i, s in enumerate(sites):
        if i in route or s["id"] in ex or s["k"] not in kinds:
            continue
        if s["e"] == "outside" and not outside:
            continue
        if free and s["e"] == "ticket":
            continue
        if _km(start, pos[i]) > radius:
            continue
        cand.append(i)
    P = lambda j: start if j < 0 else pos[j]
    lo = 1 if first is not None else 0

    def total(rt):
        t, prev = 0, -1
        for j in rt:
            t += drive(P(prev), P(j)) + sites[j]["m"]
            prev = j
        return t + drive(P(prev), start)

    def tidy(rt):   # 2-opt: reverse a stretch whenever that makes the day shorter
        better = True
        while better:
            better = False
            for i in range(lo, len(rt) - 1):
                for j in range(i + 1, len(rt)):
                    r2 = rt[:i] + rt[i:j + 1][::-1] + rt[j + 1:]
                    if total(r2) < total(rt):
                        rt, better = r2, True
        return rt

    route = tidy(route)
    cur = total(route)
    while fill and len(route) < most:
        best, bs = None, -1.0
        for c in cand:
            if c in route:
                continue
            for k in range(lo, len(route) + 1):
                a = P(route[k - 1]) if k > 0 else start
                b = P(route[k]) if k < len(route) else start
                dd = drive(a, P(c)) + drive(P(c), b) - drive(a, b)
                add = dd + sites[c]["m"]
                if cur + add > budget:
                    continue
                w = sites[c]["w"]
                sc = w * math.sqrt(w) / (sites[c]["m"] + 3.0 * dd + 20.0)
                if sc > bs + 1e-9:
                    best, bs = (c, k, add), sc
        if not best:
            break
        route.insert(best[1], best[0])
        cur += best[2]
    return tidy(route)


# ---------- the stops ----------
def _place_kind(p):
    i, era = p["ill"], p["era"]
    if era == "roman":
        return "roman"
    if p["id"] in ("plasmawr", "erddig", "penmynydd", "penrhyn", "library", "stfagans", "tymawrwybrnant", "llanystumdwy", "yrysgwrn"):
        return "culture"
    if i in ("castle", "crown"):
        return "castles"
    if i in ("cross", "chapel") or (i == "arches" and era != "industrial"):
        return "faith"
    if i in ("dolmen", "cave", "stone", "mtn") and era in ("ancient", "britons"):
        return "early"
    if i in ("wheel", "slate", "ship") or era == "industrial":
        return "work"
    if p["id"] in ("dinasemrys", "eliseg", "carewcross", "margam", "maenachwyfan"):
        return "faith" if p["id"] != "dinasemrys" else "castles"
    return "culture"


def _mins_weight(pid, who, entry, kind):
    big = who in ("cadw", "nt", "amg") or (isinstance(who, tuple))
    if entry == "outside":
        m, w = 10, .6
    elif entry == "ticket":
        m, w = (120, 3) if who in ("nt", "amg") else (90, 3)
    elif entry == "church":
        m, w = 30, 1.5
    elif entry in ("free", "partfree"):
        m, w = (45, 2) if big else (40, 1.5)
        if who in ("nt", "amg"):
            m, w = 120, 3
    elif who == "town":
        m, w = 40, 1.2
    else:  # open land
        m, w = (30, 1.5) if kind == "early" else (40, 1.5)
    if pid in MINS:
        m = MINS[pid]
    if pid in FLAGSHIP:
        w = 4
    return m, w


def stops():
    """Every place a day out can include: [dict] with what the planner, the page and the map need."""
    D, VS, ST = g["D"], g["VS"], g["ST"]
    card_pic, TH, e = g["card_pic"], g["TH"], g["e"]
    out = []
    for p in D.PLACES:
        pid = p["id"]
        v = VS.VISIT.get(pid)
        if not v or pid in NOT_A_STOP:
            continue
        who = v["who"]
        wn = who if isinstance(who, tuple) else VS.WHO[who]
        kind = _place_kind(p)
        m, w = _mins_weight(pid, who, v["entry"], kind)
        pic = card_pic(f"place-{pid}.html")
        out.append(dict(id=pid, en=p["en"], cy=p["cy"], lat=p["lat"], lon=p["lon"], k=KIX[kind], m=m, w=w + .3, e=v["entry"],
                        who=list(wn), url=v["url"], pc=v["pc"], href=f"place-{pid}.html", dEn=p["dEn"], dCy=p["dCy"],
                        pic=TH.thumb(pic[0]) if pic else "", ill=p["ill"], note=list(v["note"]) if v.get("note") else None))
    # the Cadw sites with no place page yet
    root = os.path.dirname(g["SRC"])
    gp = os.path.join(root, "tools", "data", "sites_guardian.json")
    cadw_rows = {}
    cp = os.path.join(root, "tools", "data", "sites_cadw.json")
    if os.path.exists(cp):
        for x in json.load(open(cp, encoding="utf-8")):
            cadw_rows[str(x["p"].get("SAMNumber", "")).strip()] = x["p"]
    taken = [(s["lat"], s["lon"]) for s in out]
    if os.path.exists(gp):
        for x in json.load(open(gp, encoding="utf-8")):
            n = x["n"]
            if n in CADW_SKIP or n not in CADW_SLUG:
                continue
            if any(abs(a - x["lat"]) < .005 and abs(b - x["lon"]) < .008 for a, b in taken):
                continue
            pp = x["p"]
            row = cadw_rows.get(str(pp.get("sm_number", "")).strip(), {})
            typ, per = row.get("SiteType", pp.get("site_type", "")), row.get("Period", "")
            typ_cy = row.get("SiteType_cy") or typ
            cat = ST.classify(typ, per, row.get("BroadClass") or pp.get("broad_clas"))
            kind = CADW_KIND.get(cat, "culture")
            en, cy = CADW_NAME_FIX.get(n, (n, None))
            cy = cy or pp.get("name_cy") or en
            free = "Free" in str(pp.get("paidstatus", ""))
            entry = "free" if free else "ticket"
            big = typ in ("Castle", "Abbey", "Priory", "Palace") or "Castle" in en
            m = (75 if not free else 45) if big else 25
            w = (3 if not free else 2.2) if big else 1.2
            pk = CADW_PIC.get(n)
            pic = TH.thumb(f"gallery/{pk}-s.webp") if pk and pk in g["GP"].GALLERY else ""
            per_cy = ST.PERIOD_CY.get(per, per)
            line_en = f"{typ}{', ' + per.lower() if per and per != 'Unknown' else ''}, in the care of Cadw."
            line_cy = f"{typ_cy}{', ' + per_cy.lower() if per and per != 'Unknown' else ''}, yng ngofal Cadw."
            slug = CADW_SLUG[n]
            out.append(dict(id="c-" + slug if slug else "c-" + str(pp.get("sm_number", "")).lower(), en=en, cy=cy, lat=x["lat"], lon=x["lon"], k=KIX[kind], m=m, w=w,
                            e=entry, who=["Cadw", "Cadw"], url=("https://cadw.gov.wales/visit/places-to-visit/" + slug) if slug else "", pc="",
                            href="", dEn=line_en, dCy=line_cy, pic=pic, ill=KINDS[KIX[kind]][3], note=None))
    for xid, x in EXTRA.items():
        en, cy, la, lo, kind, who, url, pc, entry, den, dcy, pk, m, w = x
        pic = TH.thumb(f"gallery/{pk}-s.webp") if pk and pk in g["GP"].GALLERY else ""
        out.append(dict(id=xid, en=en, cy=cy, lat=la, lon=lo, k=KIX[kind], m=m, w=w, e=entry, who=list(who), url=url, pc=pc, href="",
                        dEn=den, dCy=dcy, pic=pic, ill=KINDS[KIX[kind]][3], note=None))
    ids = [s["id"] for s in out]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        raise SystemExit(f"visitplan: the same stop id twice: {sorted(dup)}")
    return out


def towns():
    """Every town a day can start from: [English, Welsh, lat, lon], from the place-name pages and src/towns.py."""
    RT, TW = g["RT"], g["TW"]
    geo = json.load(open(os.path.join(g["SRC"], "towns_geo.json"), encoding="utf-8"))
    seen, out = set(), []
    for _la, ts in RT.TOWNS.items():
        for t in ts:
            ll = t["geo"] or geo.get(t["en"])
            if ll and t["en"] not in seen:
                seen.add(t["en"])
                out.append([t["en"], t["cy"], round(ll[0], 4), round(ll[1], 4)])
    for t in TW.TOWNS:
        if t[0] not in seen:
            seen.add(t[0])
            out.append([t[0], t[1], t[2], t[3]])
    for a in AREAS:
        s = a[3]
        if s[0] not in seen:
            seen.add(s[0])
            out.append([s[0], s[1], s[2], s[3]])
    return sorted(out, key=lambda t: t[0])


# ---------- a day, laid out (the same rows as render() in src/static/visitplan.js) ----------
ENTRY = {"free": ("Free entry", "Mynediad am ddim"), "ticket": ("Paid entry", "Tâl mynediad"), "open": ("Open land, free", "Tir agored, am ddim"),
         "outside": ("Seen from the road or path", "I’w weld o’r ffordd neu’r llwybr"), "partfree": ("Grounds free, some parts paid", "Y tir am ddim, tâl am rai rhannau"),
         "church": ("Free, open in daytime", "Am ddim, ar agor yn ystod y dydd")}


def hm(t):
    return f"{t // 60:02d}:{t % 60:02d}"


def dur(m, cy=False):
    h, mm = divmod(int(m), 60)
    if cy:
        return (f"{h} awr" if h else "") + (" " if h and mm else "") + (f"{mm} munud" if mm or not h else "")
    return (f"{h} h" if h else "") + (" " if h and mm else "") + (f"{mm} min" if mm or not h else "")


def miles(km):
    return max(1, int(math.floor(km / 1.609344 + .5)))


def timeline(sites, route, start, t0=600, length="day"):
    """The day as rows: ("leave", t), ("stop", i, arrive, leave, drive min, miles), ("lunch", t), ("back", t, drive, miles),
    plus the total minutes on the road and miles."""
    rows, t, prev = [("leave", t0)], t0, start
    road, mi, lunch = 0, 0, LENGTHS[length][5]
    for j in route:
        p = (sites[j]["lat"], sites[j]["lon"])
        d, k = drive(prev, p), road_km(prev, p)
        t += d
        road += d
        mi += miles(k)
        rows.append(("stop", j, t, t + sites[j]["m"], d, miles(k)))
        t += sites[j]["m"]
        if lunch and t >= 735:
            rows.append(("lunch", t))
            t += LUNCH
            lunch = False
        prev = p
    d, k = drive(prev, start), road_km(prev, start)
    t += d
    road += d
    mi += miles(k)
    rows.append(("back", t, d, miles(k)))
    return rows, road, mi


def gmaps(start, pts):
    o = f"{start[0]:.5f},{start[1]:.5f}"
    w = "|".join(f"{a:.5f},{b:.5f}" for a, b in pts[:9])
    return f"https://www.google.com/maps/dir/?api=1&origin={o}&destination={o}&travelmode=driving" + (f"&waypoints={w.replace('|', '%7C')}" if w else "")


def directions(s):
    return f'https://www.google.com/maps/dir/?api=1&destination={s["lat"]},{s["lon"]}'


def map_svg(sites, route, start, start_name, town_list):
    """A map of the day: the relief of Wales, nearby towns, the order of the stops (straight lines) and numbered pins."""
    geo, e = g["geo"], g["e"]
    sc, k, minx, maxy, W, H = geo["sc"], geo["k"], geo["minx"], geo["maxy"], geo["W"], geo["H"]
    X = lambda lon: (lon - minx) * k * sc
    Y = lambda lat: (maxy - lat) * sc
    pts = [(X(start[1]), Y(start[0]))] + [(X(sites[j]["lon"]), Y(sites[j]["lat"])) for j in route]
    x0, x1 = min(p[0] for p in pts), max(p[0] for p in pts)
    y0, y1 = min(p[1] for p in pts), max(p[1] for p in pts)
    w, h = max(x1 - x0, 30) * 1.3 + 10, max(y1 - y0, 22) * 1.3 + 10
    if w / h < 4 / 3:
        w = h * 4 / 3
    else:
        h = w * 3 / 4
    cx, cy_ = (x0 + x1) / 2, (y0 + y1) / 2
    vx, vy = cx - w / 2, cy_ - h / 2
    u = w / 100.0   # one hundredth of the width: sizes scale with the view
    out = [f'<svg class="vp-svg" viewBox="{vx:.1f} {vy:.1f} {w:.1f} {h:.1f}" role="img" aria-label="Map of the day / Map o’r diwrnod" preserveAspectRatio="xMidYMid slice">',
           f'<rect x="{vx - w:.1f}" y="{vy - h:.1f}" width="{w * 3:.1f}" height="{h * 3:.1f}" fill="#121a2a"/>',
           f'<image href="relief-3600.webp" x="0" y="0" width="{W}" height="{H}" preserveAspectRatio="none"/>']
    labels = []
    for t in town_list:
        tx, ty = X(t[3]), Y(t[2])
        if vx + 4 * u < tx < vx + w - 4 * u and vy + 3 * u < ty < vy + h - 2 * u and (t[0] != start_name[0]):
            if all((tx - p[0]) ** 2 + (ty - p[1]) ** 2 > (6 * u) ** 2 for p in pts) and all(abs(tx - a) > 16 * u or abs(ty - b) > 3.4 * u for a, b in labels):
                labels.append((tx, ty))
                out.append(f'<g class="vp-town"><circle cx="{tx:.1f}" cy="{ty:.1f}" r="{.5 * u:.2f}"/><text x="{tx + u:.1f}" y="{ty + .9 * u:.1f}" font-size="{2.4 * u:.2f}">'
                           f'{g["bi"](t[0], t[1], "tspan")}</text></g>')
    d = "M" + " L".join(f"{p[0]:.1f} {p[1]:.1f}" for p in pts + [pts[0]])
    out.append(f'<path class="vp-line" d="{d}" stroke-width="{.55 * u:.2f}" stroke-dasharray="{1.6 * u:.2f} {1.1 * u:.2f}"/>')
    sx, sy = pts[0]
    out.append(f'<g class="vp-home"><rect x="{sx - 2.1 * u:.1f}" y="{sy - 2.1 * u:.1f}" width="{4.2 * u:.1f}" height="{4.2 * u:.1f}" rx="{.8 * u:.1f}" stroke-width="{.4 * u:.2f}"/>'
               f'<path d="M{sx - 1.2 * u:.1f} {sy + .1 * u:.1f} L{sx:.1f} {sy - 1.1 * u:.1f} L{sx + 1.2 * u:.1f} {sy + .1 * u:.1f} M{sx - .8 * u:.1f} {sy - .2 * u:.1f} V{sy + 1.2 * u:.1f} H{sx + .8 * u:.1f} V{sy - .2 * u:.1f}" stroke-width="{.35 * u:.2f}"/></g>')
    placed = [pts[0]]
    for n, (px, py) in enumerate(pts[1:], 1):
        tx_, ty_ = px, py   # a pin on top of another moves aside, with a short line back to the real spot
        for ang in (0, -45, 45, -135, 135, -90, 90, 180):
            if ang:
                tx_, ty_ = px + 4.8 * u * math.sin(math.radians(ang)), py - 4.8 * u * math.cos(math.radians(ang))
            if all((tx_ - a) ** 2 + (ty_ - b) ** 2 >= (4.4 * u) ** 2 for a, b in placed):
                break
        placed.append((tx_, ty_))
        if (tx_, ty_) != (px, py):
            out.append(f'<path class="vp-lead" d="M{px:.1f} {py:.1f} L{tx_:.1f} {ty_:.1f}" stroke-width="{.3 * u:.2f}"/><circle class="vp-dot" cx="{px:.1f}" cy="{py:.1f}" r="{.7 * u:.2f}"/>')
            px, py = tx_, ty_
        out.append(f'<g class="vp-pin"><circle cx="{px:.1f}" cy="{py:.1f}" r="{2.3 * u:.2f}" stroke-width="{.4 * u:.2f}"/>'
                   f'<text x="{px:.1f}" y="{py + .95 * u:.1f}" font-size="{2.7 * u:.2f}">{n}</text></g>')
    out.append("</svg>")
    return "".join(out)


def day_html(sites, route, start, start_name, t0=600, length="day", town_list=()):
    """The finished day: summary, map and the list of stops, as on a ready-made day's page."""
    bi, e, row_pic, TH = g["bi"], g["e"], g["row_pic"], g["TH"]
    rows, road, mi = timeline(sites, route, start, t0, length)
    n = len(route)
    back = rows[-1][1]
    summ = (f'<p class="vp-sum"><b>{bi(f"{n} stops", f"{n} arhosfan")}</b><span>{bi(f"{dur(road)} on the road, about {mi} miles", f"{dur(road, True)} ar y ffordd, tua {mi} milltir")}</span>'
            f'<span>{bi(f"Leave at {hm(t0)}, back by about {hm(back)}", f"Gadael am {hm(t0)}, yn ôl erbyn tua {hm(back)}")}</span></p>')
    lis = []
    for r in rows:
        if r[0] == "leave":
            lis.append(f'<li class="vp-mark"><time>{hm(r[1])}</time><span>{bi(f"Leave {start_name[0]}", f"Gadael {start_name[1]}")}</span></li>')
        elif r[0] == "lunch":
            lis.append(f'<li class="vp-mark vp-lunch"><time>{hm(r[1])}</time><span>{bi(f"Lunch break, {LUNCH} min", f"Egwyl ginio, {LUNCH} munud")}</span></li>')
        elif r[0] == "back":
            lis.append(f'<li class="vp-drive">{bi(f"{r[2]} min drive, about {r[3]} mile{'s' if r[3] > 1 else ''}", f"{r[2]} munud yn y car, tua {r[3]} milltir")}</li>'
                       f'<li class="vp-mark"><time>{hm(r[1])}</time><span>{bi(f"Back at {start_name[0]}", f"Yn ôl i’r man cychwyn, {start_name[1]}")}</span></li>')
        else:
            _, j, ta, tl, d, m = r
            s = sites[j]
            lis.append(f'<li class="vp-drive">{bi(f"{d} min drive, about {m} mile{'s' if m > 1 else ''}", f"{d} munud yn y car, tua {m} milltir")}</li>')
            lis.append(stop_li(s, route.index(j) + 1, ta, tl))
    return (f'<div class="vp-day">{summ}<div class="vp-cols"><figure class="vp-map">{map_svg(sites, route, start, start_name, town_list)}'
            f'<figcaption>{bi("The lines show the order of the day, not the roads.", "Mae’r llinellau’n dangos trefn y diwrnod, nid y ffyrdd.")}</figcaption></figure>'
            f'<ul class="vp-plan">{"".join(lis)}</ul></div></div>'), [(sites[j]["lat"], sites[j]["lon"]) for j in route]


def stop_li(s, n, ta, tl):
    bi, e, TH = g["bi"], g["e"], g["TH"]
    ent = ENTRY[s["e"]]
    who = s["who"]
    meta = bi(f'{who[0][0].upper() + who[0][1:]} · {ent[0]}', f'{who[1][0].upper() + who[1][1:]} · {ent[1]}') + (f' · <b>{e(s["pc"])}</b>' if s["pc"] else "")
    links = ((f'<a href="{e(s["url"])}" target="_blank" rel="noopener">{bi("Opening times and prices", "Amseroedd agor a phrisiau")} ↗</a>' if s["url"] else "")
             + f'<a href="{directions(s)}" target="_blank" rel="noopener">{bi("Directions", "Cyfarwyddiadau")} ↗</a>')
    note = f'<p class="vp-note">{bi(s["note"][0], s["note"][1])}</p>' if s.get("note") else ""
    if s["href"]:
        wl = f'<a class="wl" href="{s["href"]}">{bi(s["en"], s["cy"])}</a>'
    elif s["url"]:
        wl = f'<a class="wl" href="{e(s["url"])}" target="_blank" rel="noopener">{bi(s["en"], s["cy"])}</a>'
    else:
        wl = ""
    pic = (f'<span class="vp-pic" aria-hidden="true"><img src="{e(s["pic"])}" alt="" width="96" height="96" loading="lazy" decoding="async"></span>' if s["pic"]
           else f'<span class="vp-pic ic" aria-hidden="true"><svg><use href="#i-{s["ill"]}"/></svg></span>')
    return (f'<li class="vp-stop{" wl-card" if wl else ""}" data-k="{s["k"]}"><span class="vp-n">{n}</span><div class="vp-b">'
            f'<p class="vp-time"><time>{hm(ta)}</time> – <time>{hm(tl)}</time> · {bi(f"about {dur(s["m"])} here", f"tua {dur(s["m"], True)} yma")}</p>'
            f'<h3>{bi(s["en"], s["cy"])}</h3><p class="vp-d">{bi(s["dEn"], s["dCy"])}</p><p class="vp-meta">{meta}</p>{note}<p class="vp-links">{links}</p></div>{pic}{wl}</li>')


# ---------- the pages ----------
NOTE_EN = ("Drive times are our estimate from the distance, for an ordinary car on Welsh roads: allow more in summer and on mountain roads. "
           "Check the official page of each place before you travel: times change, and some sites close in winter or on certain days.")
NOTE_CY = ("Ein hamcangyfrif ni o’r pellter yw’r amseroedd gyrru, ar gyfer car cyffredin ar ffyrdd Cymru: caniatewch fwy yn yr haf ac ar ffyrdd mynydd. "
           "Edrychwch ar dudalen swyddogol pob lle cyn teithio: mae amseroedd yn newid, ac mae rhai safleoedd yn cau yn y gaeaf neu ar ddyddiau penodol.")


def _area_pic(a):
    pic = g["card_pic"](f"place-{a[6]}.html")
    return pic


def area_cards(skip=None):
    bi, ban_pic = g["bi"], g["ban_pic"]
    out = ""
    for a in AREAS:
        if a[0] == skip:
            continue
        n = len(a[7].split())
        out += (f'<a class="chap vp-area" href="visit-{a[0]}.html">{ban_pic(_area_pic(a))}<span class="span">{bi(f"From {a[3][0]} · {n} stops", f"O {a[3][1]} · {n} arhosfan")}</span>'
                f'<h3>{bi(a[1], a[2])}</h3><p>{bi(a[4], a[5])}</p></a>')
    return f'<div class="chapters vp-areas">{out}</div>'


def _payload(S, T):
    geo = g["geo"]
    return dict(s=[[s["id"], s["en"], s["cy"], s["lat"], s["lon"], s["k"], s["m"], s["w"], s["e"], s["who"][0], s["who"][1], s["url"], s["pc"], s["href"],
                    s["dEn"], s["dCy"], s["pic"], s["ill"], *(s["note"] or ["", ""])] for s in S],
                t=T, K=[[k[1], k[2]] for k in KINDS], L={k: list(v) for k, v in LENGTHS.items()}, B=[[list(m), list(h), [list(x) for x in br]] for m, h, br in BARRIERS],
                E={k: list(v) for k, v in ENTRY.items()}, G=[geo["minx"], geo["maxy"], geo["k"], geo["sc"], geo["W"], geo["H"]],
                sp=g.get("SPRITE_URL", "sprite.svg"), C=[ROAD, KMH, PARK, LUNCH], A=[[a[0], a[1], a[2], a[3][0]] for a in AREAS])


def pages():
    bi, e, section, hero, SITE, page = g["bi"], g["e"], g["section"], g["hero"], g["SITE"], g["page"]
    S = stops()
    T = towns()
    ix = {s["id"]: i for i, s in enumerate(S)}
    out = {}
    crumbs = f'<a href="index.html">{SITE}</a> / <a href="map.html">{bi("Map", "Map")}</a>'
    # the planner
    kinds = "".join(f'<label class="vp-chip"><input type="checkbox" name="k" value="{i}" checked><span><svg aria-hidden="true"><use href="#i-{k[3]}"/></svg>{bi(k[1], k[2])}</span></label>'
                    for i, k in enumerate(KINDS))
    lens = "".join(f'<label class="vp-chip"><input type="radio" name="len" value="{k}"{" checked" if k == "day" else ""}><span>{bi(v[0], v[1])}</span></label>'
                   for k, v in LENGTHS.items())
    times = "".join(f'<option value="{t}"{" selected" if t == 600 else ""}>{hm(t)}</option>' for t in (540, 570, 600, 630, 660, 720, 780))
    opts = "".join(f'<option value="{e(t[0])}">' + (f'<option value="{e(t[1])}">' if t[1] != t[0] else "") for t in T)
    opts += "".join(f'<option value="{e(s["en"])}">' + (f'<option value="{e(s["cy"])}">' if s["cy"] != s["en"] else "") for s in S)
    form = (f'<form class="vp-form" id="vp-form" autocomplete="off"><div class="vp-from"><label for="vp-q">{bi("Where will you start?", "O ble byddwch chi’n cychwyn?")}</label>'
            f'<div class="vp-in"><input id="vp-q" name="from" list="vp-list" type="text" required placeholder="A town, or a historic place" data-ph-cy="Tref, neu le hanesyddol" data-ph-en="A town, or a historic place">'
            f'<button type="button" class="btn" id="vp-loc">{bi("Use my location", "Defnyddio fy lleoliad")}</button></div><datalist id="vp-list">{opts}</datalist>'
            f'<p class="vp-err" id="vp-err" hidden></p></div>'
            f'<fieldset><legend>{bi("How long have you got?", "Faint o amser sydd gennych chi?")}</legend><div class="vp-chips">{lens}</div></fieldset>'
            f'<fieldset><legend>{bi("What would you like to see?", "Beth hoffech chi ei weld?")}</legend><div class="vp-chips">{kinds}</div></fieldset>'
            f'<div class="vp-opts"><label><input type="checkbox" name="free"> {bi("Free entry only", "Mynediad am ddim yn unig")}</label>'
            f'<label><input type="checkbox" name="out"> {bi("Include places you can only see from the road", "Cynnwys lleoedd y gallwch eu gweld o’r ffordd yn unig")}</label>'
            f'<label>{bi("Set off at", "Cychwyn am")} <select name="t">{times}</select></label></div>'
            f'<p class="vp-go"><button type="submit" class="btn solid">{bi("Plan my day", "Cynllunio fy niwrnod")} →</button></p></form>'
            f'<noscript><p class="muted">{bi("The planner needs JavaScript. The ready-made days below work without it.", "Mae angen JavaScript ar y cynlluniwr. Mae’r diwrnodau parod isod yn gweithio hebddo.")}</p></noscript>'
            f'<div id="vp-out" class="vp-out" aria-live="polite"></div>')
    n_all = len(S)
    intro = bi(f"Choose where you start and how long you have, and we will plan a day among {n_all} castles, courts, abbeys, tombs, Roman forts and museums you can visit: the best order, the drive between each, how long to spend, how you get in, and the official page for opening times. Print it, or open the route in your maps app.",
               f"Dewiswch o ble rydych chi’n cychwyn a faint o amser sydd gennych, ac fe gynlluniwn ddiwrnod i chi ymhlith {n_all} o gestyll, llysoedd, abatai, beddrodau, caerau Rhufeinig ac amgueddfeydd y gallwch ymweld â nhw: y drefn orau, y daith rhwng pob un, faint o amser i’w dreulio, sut i fynd i mewn, a’r dudalen swyddogol am amseroedd agor. Argraffwch ef, neu agorwch y daith yn eich ap mapiau.")
    main = (hero("medieval", crumbs, "castle", "Plan a visit", "Cynllunio ymweliad", "Plan a day out", "Cynlluniwch ddiwrnod allan",
                 "A day among the castles, courts and holy places of Wales, planned for you.", "Diwrnod ymhlith cestyll, llysoedd a mannau sanctaidd Cymru, wedi’i gynllunio i chi.", art="castle")
            + section(f'<p class="lede vp-intro">{intro}</p>{form}<p class="muted vp-small">{bi(NOTE_EN, NOTE_CY)}</p>', top=True)
            + section(area_cards(), "Ready-made days out", "Diwrnodau allan parod"))
    data = json.dumps(_payload(S, T), ensure_ascii=False, separators=(",", ":"))
    extra = f'<script>var VPD={data};</script>\n<script src="visitplan.js?v={g["_static_fp"]("visitplan.js")}" defer></script>\n'
    out["visit.html"] = page("visit.html", "Plan a day out: castles and historic places of Wales · History of Wales",
                             f"Plan a day out among {n_all} castles, courts, abbeys, tombs and museums of Wales: the best order, drive times, how to get in and a printable map, in English and Welsh.",
                             main, era="medieval", og_type="website", active="visit.html", extra=extra)
    # the ready-made days
    for a in AREAS:
        aid, en, cy, st, len_, lcy, _pic, picks = a
        start = (st[2], st[3])
        bad = [x for x in picks.split() if x not in ix]
        if bad:
            raise SystemExit(f"visitplan: area {aid} names stops that do not exist: {bad}")
        route = plan(S, start, "day", pins=[ix[x] for x in picks.split()], fill=False)
        day, pts = day_html(S, route, start, (st[0], st[1]), 600, "day", T)
        ids = ",".join(S[j]["id"] for j in route)
        from_q = st[0].replace(" ", "+")
        acts = (f'<p class="vp-acts no-print"><a class="btn solid" href="{e(gmaps(start, pts))}" target="_blank" rel="noopener">{bi("Open the route in Google Maps", "Agor y daith yn Google Maps")} ↗</a>'
                f'<button type="button" class="btn" data-print="1">{bi("Print this day", "Argraffu’r diwrnod")}</button>'
                f'<a class="btn" href="visit.html?from={e(from_q)}&amp;p={ids}&amp;nf=1">{bi("Change this day", "Newid y diwrnod")} →</a></p>')
        others = sorted((i for i, s in enumerate(S) if i not in route and s["e"] != "outside" and _km(start, (s["lat"], s["lon"])) <= 30),
                        key=lambda i: _km(start, (S[i]["lat"], S[i]["lon"])))[:12]
        more = "".join(f'<li class="vp-near{" wl-card" if (S[i]["href"] or S[i]["url"]) else ""}"><b>{bi(S[i]["en"], S[i]["cy"])}</b><span>{bi(f"{miles(road_km(start, (S[i]["lat"], S[i]["lon"])))} miles · {ENTRY[S[i]["e"]][0]}", f"{miles(road_km(start, (S[i]["lat"], S[i]["lon"])))} milltir · {ENTRY[S[i]["e"]][1]}")}</span>'
                       + (f'<a class="wl" href="{S[i]["href"]}">{bi(S[i]["en"], S[i]["cy"])}</a>' if S[i]["href"] else
                          f'<a class="wl" href="{e(S[i]["url"])}" target="_blank" rel="noopener">{bi(S[i]["en"], S[i]["cy"])}</a>' if S[i]["url"] else "") + "</li>" for i in others)
        lede_en = f"A day out from {st[0]}: {len(route)} historic places in the best order, with drive times, how to get in, and a map to print."
        lede_cy = f"Diwrnod allan o {st[1]}: {len(route)} o leoedd hanesyddol yn y drefn orau, gydag amseroedd gyrru, sut i fynd i mewn, a map i’w argraffu."
        body = (hero("medieval", f'{crumbs} / <a href="visit.html">{bi("Plan a day out", "Cynllunio diwrnod allan")}</a>', "castle", "A day out", "Diwrnod allan", en, cy, len_, lcy, art="castle")
                + section(f'<p class="lede">{bi(lede_en, lede_cy)}</p>{day}{acts}<p class="muted vp-small">{bi(NOTE_EN, NOTE_CY)}</p>', top=True)
                + (section(f'<ul class="vp-nears">{more}</ul>', "More to see nearby", "Mwy i’w weld gerllaw") if more else "")
                + section(area_cards(skip=aid), "More days out", "Mwy o ddiwrnodau allan"))
        ld = {"@context": "https://schema.org", "@type": "TouristTrip", "name": f"A day out in {en}", "description": len_,
              "itinerary": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": n + 1, "item": {"@type": "TouristAttraction", "name": S[j]["en"],
                                                                     "geo": {"@type": "GeoCoordinates", "latitude": S[j]["lat"], "longitude": S[j]["lon"]}}} for n, j in enumerate(route)]}}
        out[f"visit-{aid}.html"] = page(f"visit-{aid}.html", f"A day out in {en}: historic places to visit · History of Wales",
                                        f"A day out among the historic places of {en}, from {st[0]}: " + ", ".join(S[j]["en"] for j in route) + ". Drive times, entry and a printable map.",
                                        body, era="medieval", ld=ld, active="visit.html", track=f"visit:{aid}")
    return out


CSS = """
.vp-intro { max-width: 46rem; margin-bottom: 1.4rem }
.vp-small { font-size: .85rem; max-width: 46rem; margin-top: 1rem }
.vp-form { display: grid; gap: 1.1rem; background: var(--slate); border: 1px solid var(--line); border-radius: 14px; padding: 1.3rem 1.4rem }
.vp-form fieldset { border: 0; padding: 0; margin: 0; min-width: 0 }
.vp-form legend, .vp-from > label { font-family: var(--f-mono); font-size: .75rem; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); margin-bottom: .5rem; display: block }
.vp-in { display: flex; gap: .6rem; flex-wrap: wrap }
.vp-in input { flex: 1 1 16rem; min-width: 0; font: inherit; font-size: 1.05rem; padding: .7rem .9rem; border-radius: 10px; border: 1px solid var(--line); background: var(--night); color: var(--ink) }
.vp-in input:focus-visible { outline: 2px solid var(--gold); outline-offset: 2px }
.vp-err { color: #f2a19b; margin: .5rem 0 0 }
.vp-chips { display: flex; flex-wrap: wrap; gap: .5rem }
.vp-chip { position: relative; cursor: pointer }
.vp-chip input { position: absolute; opacity: 0; inset: 0; margin: 0; cursor: pointer }
.vp-chip > span { display: inline-flex; align-items: center; gap: .45rem; min-height: 44px; padding: .45rem .95rem; border-radius: 999px; border: 1px solid var(--line); color: var(--muted); font-size: .95rem; transition: background-color .2s, color .2s, border-color .2s }
.vp-chip > span > svg { width: 1.1rem; height: 1.1rem; flex: none }
.vp-chip input:checked + span { background: color-mix(in srgb, var(--gold) 18%, transparent); border-color: var(--gold); color: var(--ink) }
.vp-chip input:focus-visible + span { outline: 2px solid var(--gold); outline-offset: 2px }
.vp-opts { display: flex; flex-wrap: wrap; gap: .7rem 1.6rem; color: var(--muted); font-size: .95rem }
.vp-opts label { display: inline-flex; align-items: center; gap: .45rem; min-height: 44px }
.vp-opts input[type=checkbox] { width: 1.15rem; height: 1.15rem; accent-color: var(--gold) }
.vp-opts select { font: inherit; padding: .35rem .5rem; border-radius: 8px; background: var(--night); color: var(--ink); border: 1px solid var(--line) }
.vp-go { margin: 0 }
.vp-out:empty { display: none }
.vp-out { margin-top: 1.6rem; scroll-margin-top: 5rem }
.vp-day { display: grid; gap: 1rem }
.vp-sum { display: flex; flex-wrap: wrap; gap: .3rem 1.4rem; align-items: baseline; margin: 0; font-size: 1.02rem }
.vp-sum b { font-family: var(--f-display, inherit); font-size: 1.5rem; color: var(--gold) }
.vp-sum span { color: var(--muted) }
.vp-cols { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.1fr); gap: 1.6rem; align-items: start }
.vp-map { margin: 0; position: sticky; top: 5rem }
.vp-svg { display: block; width: 100%; aspect-ratio: 4 / 3; border-radius: 14px; border: 1px solid var(--line); background: #121a2a }
.vp-map figcaption { font-size: .8rem; color: var(--muted); margin-top: .45rem }
.vp-line { fill: none; stroke: #f0c75e; stroke-linecap: round; stroke-linejoin: round; opacity: .9 }
.vp-pin circle { fill: #e2453d; stroke: #fff }
.vp-pin text { fill: #fff; text-anchor: middle; font-family: var(--f-mono, monospace); font-weight: 700 }
.vp-lead { stroke: #fff; opacity: .8 } .vp-dot { fill: #fff }
.vp-home rect { fill: #10141d; stroke: #f0c75e }
.vp-home path { fill: none; stroke: #f0c75e; stroke-linecap: round; stroke-linejoin: round }
.vp-town circle { fill: rgba(236,233,225,.75) }
.vp-town text { fill: rgba(236,233,225,.85); paint-order: stroke; stroke: rgba(10,13,20,.85); stroke-width: .35px; font-family: var(--f-body, sans-serif) }
html.cy .vp-town .l-en, html:not(.cy) .vp-town .l-cy { display: none }
.vp-plan { list-style: none; margin: 0; padding: 0; display: grid; gap: .35rem }
.vp-mark { display: flex; gap: .8rem; align-items: baseline; padding: .55rem .2rem; font-weight: 600 }
.vp-mark time, .vp-time time { font-family: var(--f-mono, monospace); color: var(--gold) }
.vp-lunch { color: var(--muted); font-weight: 400 }
.vp-drive { font-size: .85rem; color: var(--muted); padding: .1rem 0 .1rem 2.6rem; position: relative }
.vp-drive::before { content: ""; position: absolute; left: 1.05rem; top: -.35rem; bottom: -.35rem; border-left: 2px dashed color-mix(in srgb, var(--gold) 55%, transparent) }
.vp-stop { display: grid; grid-template-columns: 2.2rem minmax(0, 1fr) auto; gap: .8rem; align-items: start; background: var(--slate); border: 1px solid var(--line); border-radius: 14px; padding: .95rem 1rem; transition: box-shadow .25s }
.vp-stop.wl-card:hover { box-shadow: 0 0 0 1px color-mix(in srgb, var(--gold) 55%, transparent) }
.vp-n { width: 2.2rem; height: 2.2rem; border-radius: 50%; background: #e2453d; color: #fff; display: grid; place-items: center; font-family: var(--f-mono, monospace); font-weight: 700 }
.vp-b > * { margin: 0 } .vp-b { display: grid; gap: .3rem }
.vp-b h3 { font-size: 1.35rem; line-height: 1.2 }
.vp-time { font-size: .85rem; color: var(--muted) }
.vp-d { color: #cfd2d8; font-size: .95rem }
.vp-meta { font-size: .85rem; color: var(--muted) } .vp-meta b { color: var(--ink); font-family: var(--f-mono, monospace); font-weight: 500 }
.vp-note { font-size: .85rem; color: #f0c75e }
.vp-links { display: flex; flex-wrap: wrap; gap: .2rem 1.1rem; font-size: .9rem }
.vp-links a, .vp-links button { color: var(--ink); min-height: 44px; display: inline-flex; align-items: center }
.vp-links button { background: none; border: 0; padding: 0; font: inherit; text-decoration: underline; text-underline-offset: 3px; cursor: pointer; color: var(--muted) }
.vp-pic { width: 76px; height: 76px; border-radius: 10px; overflow: hidden; flex: none; background: var(--slate-2) }
.vp-pic img { width: 100%; height: 100%; object-fit: cover; display: block }
.vp-pic.ic { display: grid; place-items: center } .vp-pic.ic svg { width: 2.2rem; height: 2.2rem; color: var(--muted) }
.vp-acts { display: flex; flex-wrap: wrap; gap: .6rem; margin: 1.4rem 0 0 }
.vp-add { display: flex; flex-wrap: wrap; gap: .6rem; align-items: center; margin-top: 1rem }
.vp-add input { flex: 1 1 14rem; min-width: 0; font: inherit; padding: .6rem .8rem; border-radius: 10px; border: 1px solid var(--line); background: var(--night); color: var(--ink) }
.vp-nears { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 16rem), 1fr)); gap: .6rem }
.vp-near { background: var(--slate); border: 1px solid var(--line); border-radius: 12px; padding: .75rem .9rem; display: grid; gap: .15rem }
.vp-near span { font-size: .85rem; color: var(--muted) }
.vp-near.wl-card:hover { box-shadow: 0 0 0 1px color-mix(in srgb, var(--gold) 55%, transparent) }
.vp-areas .card-ban { aspect-ratio: 16 / 8 }
@media (max-width: 860px) {
  .vp-cols { grid-template-columns: 1fr }
  .vp-map { position: static }
  .vp-stop { grid-template-columns: 2rem minmax(0, 1fr); padding: .85rem .85rem }
  .vp-n { width: 2rem; height: 2rem }
  .vp-pic { display: none }
  .vp-form { padding: 1.05rem 1rem }
  .vp-chips { flex-wrap: nowrap; overflow-x: auto; scrollbar-width: none; margin-inline: -1rem; padding-inline: 1rem; scroll-padding-inline: 1rem }
  .vp-chips::-webkit-scrollbar { display: none }
  .vp-chip { flex: none }
}
@media print {
  .vp-form, .vp-acts, .vp-add, .vp-links button, .vp-areas, .vp-nears, .share-row, .vp-intro, section:has(.vp-areas), section:has(.vp-nears) { display: none !important }
  section:has(.vp-day), section:has(.vp-form) { break-inside: auto }
  .vp-cols { grid-template-columns: 1fr }
  .vp-map { position: static; break-inside: avoid }
  .vp-svg { aspect-ratio: 4 / 3; max-height: 12cm; border-color: #999 }
  .vp-stop { break-inside: avoid; border-color: #bbb; background: #fff }
  .vp-pic img { print-color-adjust: exact; -webkit-print-color-adjust: exact }
  .vp-n, .vp-pin circle { print-color-adjust: exact; -webkit-print-color-adjust: exact }
  .vp-links a { text-decoration: none }
  .vp-links a::after { content: none }
  .vp-sum b, .vp-mark time, .vp-time time { color: #111 }
  .vp-d, .vp-note { color: #333 }
  .vp-drive::before { border-color: #999 }
  .era-hero { padding-block: 0 !important; min-height: 0 !important }
  .era-hero .hero-art { display: none }
}
"""
