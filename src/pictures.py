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
    britons="g:place-castellhenllys",
    roman="g:place-caerleon",
    saints="g:place-stdavids",
    kings="g:place-eliseg",
    medieval="g:place-dolbadarn",
    glyndwr="g:place-harlech",
    tudor="g:place-rhaglan",
    revival="g:place-ybala",
    industrial="g:place-pontcysyllte",
    modern="g:place-celyn",
    today="g:place-senedd",
)

PAGE = {
    # pages that had no picture of their own, so their What's new lines had none (Ifan, 14 November 2026)
    "story-rhys.html": "g:person-yr-arglwydd-rhys@50% 22%",
    "story-nest.html": "g:cast-cilgerran",
    "books.html": "g:trea-st-chad@50% 30%",
    "firsts.html": "g:place-pontcysyllte",
    # The Druids long read (src/druids.py)
    "story-druids.html": "g:druid-teaching@50% 30%",
    # the princes of Powys and Deheubarth (src/princes4.py)
    "person-gwenwynwyn.html": "g:cast-powis",
    "person-madog-ap-gruffudd-maelor.html": "g:holy-valle-crucis",
    "person-maelgwn-ap-rhys.html": "g:place-strataflorida",
    "person-rhys-gryg.html": "g:place-dinefwr",
    # historic places of importance (src/places3.py)
    "place-garthcelyn.html": "g:person-siwan",
    "place-dolwyddelan.html": "g:cast-dolwyddelan",
    "place-dinasemrys.html": "g:land-dinas-emrys",
    "place-llysrhosyr.html": "g:anci-llys-rhosyr",
    "place-cricieth.html": "g:cast-criccieth",
    "place-dolforwyn.html": "g:person-llywelyn-ap-gruffudd",
    "place-dryslwyn.html": "g:cast-dryslwyn",
    "place-carregcennen.html": "g:cast-carreg-cennen",
    "place-ewloe.html": "g:cast-ewloe",
    "place-dinasbran.html": "g:cast-dinas-bran",
    "place-cwmhir.html": "g:holy-cwmhir",
    "place-powis.html": "g:cast-powis",
    "place-kidwelly.html": "g:cast-kidwelly",
    "place-vallecrucis.html": "g:holy-valle-crucis",
    "place-penmon.html": "g:holy-penmon",
    "place-talley.html": "g:holy-talley",
    "place-basingwerk.html": "g:holy-basingwerk",
    "place-margam.html": "g:holy-margam",
    "place-neathabbey.html": "g:holy-neath-abbey",
    "place-llanthony.html": "g:holy-llanthony",
    "place-pennantmelangell.html": "g:holy-pennant-melangell",
    "place-llanbadarn.html": "g:holy-llanbadarn",
    "place-bangor.html": "g:holy-bangor",
    "place-llandaf.html": "g:holy-llandaff",
    "place-llanelwy.html": "g:holy-st-asaph",
    "place-stnons.html": "g:person-dewi-sant",
    "place-llanddewibrefi.html": "g:person-dewi-sant",
    "place-llancarfan.html": "g:person-cadog",
    "place-carewcross.html": "g:cast-carew",
    "place-ygaer.html": "g:anci-y-gaer",
    "place-tomenymur.html": "g:anci-tomen-y-mur",
    "place-dinlligwy.html": "g:anci-din-lligwy",
    "place-barclodiad.html": "g:anci-barclodiad",
    "place-tinkinswood.html": "g:anci-tinkinswood",
    "place-maenceti.html": "g:anci-maen-ceti",
    "place-parclebreos.html": "g:anci-parc-le-breos",
    "place-carregsamson.html": "g:anci-carreg-samson",
    "place-tymawr.html": "g:land-south-stack",
    "place-pilleth.html": "g:person-owain-glyndwr",
    "place-pennal.html": "g:trea-pennal-letter",
    "place-chirk.html": "g:cast-chirk",
    "place-plasmawr.html": "g:buil-plas-mawr",
    "place-erddig.html": "g:buil-erddig",
    "place-penrhyn.html": "g:cast-penrhyn",
    "place-bigpit.html": "g:indu-big-pit-winding",
    "place-llanystumdwy.html": "g:person-lloyd-george",
    "place-wmc.html": "g:buil-wmc",
    # long reads
    "story-castles.html": "g:place-caernarfon",
    "story-language.html": "g:trea-bible-1588",
    "story-hywel.html": "g:trea-laws-hywel",
    "story-coal.html": "g:place-blaenavon",
    "story-protest.html": "g:place-westgate",
    "story-world.html": "c:Gaiman, Chubut ca.1911.jpg",
    "story-arthur.html": "g:person-arthur",
    "story-glyndwr.html": "g:trea-pennal-letter",
    "story-longbow.html": "c:Longbowmen.jpg",
    "story-learning.html": "g:place-llanilltud",
    "story-unconquered.html": "g:cast-dolwyddelan",
    "story-firsts.html": "g:place-merthyr",
    "person-gwenole.html": "c:Abbaye de Landévennec.jpg",
    "story-brittany.html": "c:Procession des saints de Bretagne - diocèse de Rennes, cathédrale saint Pierre, Rennes, France.jpg",
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
    "story-mac.html": "g:peop-cofia-1282",
    "story-fwa.html": "g:peop-celyn-protest",
    "person-john-barnard-jenkins.html": "g:peop-liverpool-steals@50% 40%",
    "person-dennis-coslett.html": "g:peop-celyn-line",
    "story-lucius.html": "g:holy-llandaff",
    "story-bran.html": "g:place-harlech",
    "story-joseph.html": "c:Glastonbury Abbey Ruins 2.JPG",
    "story-aberfan.html": "g:place-aberfan",
    "story-patrick.html": "g:place-stdavids",
    "story-tryweryn.html": "g:place-celyn@50% 55%",
    "story-epynt.html": "g:place-epynt",
    "story-welsh-not.html": "l:iaith-1966",  # Cymdeithas yr Iaith at Llangefni, 1966 (Geoff Charles), src/art.py LEGEND_PHOTOS
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
    "kings-ystrad-clud.html": "c:Castle from pier, Dumbarton, Scotland-LCCN2001705975.jpg",
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
    "topic-abroad.html": "c:Vista de Gaiman.JPG",
    "topic-countryside.html": "g:place-stfagans",
    "topic-faith.html": "g:holy-soar-y-mynydd",
    "family-history.html": "g:holy-soar-y-mynydd",
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
    "trail-kings.html": "g:person-llywelyn-fawr",
    "trail-arthur.html": "g:person-arthur",
    "trail-saints.html": "g:place-treffynnon",
    "trail-language.html": "g:trea-bible-1588",
    "trail-castles.html": "g:cast-carreg-cennen",
    "trail-roman.html": "g:place-caerleon",
    "trail-mabinogi.html": "g:anci-tomen-y-mur",
    "trail-rebels.html": "g:place-machynlleth",
    "trail-poets.html": "g:place-yrysgwrn",
    "trail-world.html": "g:place-llangollen",
    "trail-first-peoples.html": "g:place-brynceliddu",
    "trail-firsts.html": "g:person-robert-recorde",
    "trail-tudors.html": "g:place-penfro",
    "trail-sport.html": "g:place-stadiwm",
    # index pages and the rest
    "stories.html": "g:trea-black-book",
    "legends.html": "g:land-dinas-emrys",
    "mabinogion.html": "g:trea-red-book",
    "literature.html": "g:trea-book-aneirin",
    "books-and-authors.html": "g:place-library",
    "further-reading.html": "g:place-library",
    "online-sources.html": "g:place-library",
    "documents.html": "g:trea-llywelyn-seal",
    "symbols.html": "g:trea-lovespoon",
    "play.html": "g:place-caerleon",
    "quiz.html": "g:place-conwy",
    "weekly-quiz.html": "g:place-harlech",
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
    "court-sycharth.html": "g:place-sycharth",  # the courts in 3D (src/courts.py)
    "court-aber.html": "g:person-siwan",
    "story-mabinogi.html": "g:trea-red-book",
    # the Mabinogi tale guides (src/mabinogi_tales.py)
    "mabinogi-pwyll.html": "c:Narberth castle pembrokeshire.jpg@50% 55%",
    "mabinogi-branwen.html": "c:Branwen drudwy.JPG@50% 40%",
    "mabinogi-manawydan.html": "c:DV405 no.86 Narberth Castle.png",
    "mabinogi-math.html": "c:Dinas Dinlle.jpg",
    # the people of the Mabinogi (src/mabinogi_people.py): the country of their tale
    "person-pwyll.html": "g:anci-carn-ingli",
    "person-rhiannon.html": "g:anci-carn-ingli",
    "person-pryderi.html": "g:anci-carn-ingli",
    "person-arawn.html": "g:anci-carn-ingli",
    "person-cigfa.html": "g:anci-gors-fawr",
    "person-teyrnon.html": "g:place-caerwent",
    "person-branwen.html": "g:place-harlech",
    "person-manawydan.html": "g:place-harlech",
    "person-matholwch.html": "g:place-harlech",
    "person-efnysien.html": "g:place-harlech",
    "person-math.html": "g:anci-tomen-y-mur",
    "person-gwydion.html": "g:anci-tomen-y-mur",
    "person-gilfaethwy.html": "g:anci-tomen-y-mur",
    "person-goewin.html": "g:anci-tomen-y-mur",
    "person-arianrhod.html": "g:anci-tomen-y-mur",
    "person-dylan-ail-don.html": "g:anci-tomen-y-mur",
    "person-lleu.html": "g:anci-tomen-y-mur",
    "person-blodeuwedd.html": "g:anci-tomen-y-mur",
    "person-gronw-pebr.html": "g:land-llyn-tegid",
    "person-rhydderch-ab-ieuan-llwyd.html": "g:place-strataflorida",
    "person-hywel-fychan.html": "g:trea-red-book",
    "person-tegid.html": "g:land-llyn-tegid",
    "person-carnhuanawc.html": "g:place-library",
    "mabinogi-culhwch.html": "g:anci-carn-ingli",
    "mabinogi-macsen.html": "g:place-segontium",
    "mabinogi-lludd.html": "g:land-dinas-emrys",
    "mabinogi-rhonabwy.html": "g:cast-powis",
    "mabinogi-owain.html": "g:place-caerleon",
    "mabinogi-peredur.html": "g:land-brecon-beacons",
    "mabinogi-geraint.html": "g:place-caerleon",
    "mabinogi-taliesin.html": "g:land-llyn-tegid",
    "person-llwyd-fab-cil-coed.html": "g:anci-carn-ingli",
    "person-ysbaddaden.html": "g:anci-carn-ingli",
    "person-beli-mawr.html": "g:land-dinas-emrys",
    "person-lludd.html": "g:land-dinas-emrys",
    "person-llefelys.html": "g:land-dinas-emrys",
    "person-cynan-meiriadog.html": "g:place-segontium",
    "person-rhonabwy.html": "g:cast-powis",
    "person-luned.html": "g:place-caerleon",
    "person-cynon-ap-clydno.html": "g:place-caerleon",
    "person-ceridwen.html": "g:land-llyn-tegid",
    "person-elis-gruffydd.html": "g:place-library",
}

import ages12 as _A12  # the places of the Age of Revival (src/ages12.py)
PAGE.update(_A12.PICTURES)

# More pictures, found on Commons for this (tools/commons_research.py) and kept on the site by tools/fetch_photos.py.
# Commons file -> (author, licence, licence link, what it shows EN, CY). Use them as "c:<Commons file>".
_BY = "https://creativecommons.org/licenses/by/"
_BYSA = "https://creativecommons.org/licenses/by-sa/"
_PD = "https://creativecommons.org/publicdomain/mark/1.0/"
EXTRA = {
    # the Britons in Brittany (src/brittany.py)
    "Abbaye de Landévennec.jpg": ("Rolf Krahl", "CC BY 4.0", "https://creativecommons.org/licenses/by/4.0",
           "The ruins of the abbey of Landévennec, founded by Gwenole", "Adfeilion abaty Landevenneg, a sefydlwyd gan Gwenole"),
    "Procession des saints de Bretagne - diocèse de Rennes, cathédrale saint Pierre, Rennes, France.jpg": ("Alphonse Le Hénaff", "Public domain", _PD,
           "The Procession of the Saints of Brittany, painted for the cathedral of Rennes", "Gorymdaith Saint Llydaw, a baentiwyd i eglwys gadeiriol Roazhon"),
    # the Mabinogi tale guides (src/mabinogi_tales.py)
    "Narberth castle pembrokeshire.jpg": ("WestWalesP", "CC BY-SA 3.0", _BYSA + "3.0",
           "The ruins of Narberth Castle, Arberth, where tradition places the court of Pwyll", "Adfeilion Castell Arberth, lle mae traddodiad yn gosod llys Pwyll"),
    "DV405 no.86 Narberth Castle.png": ("Alphonse Dousseau", "CC0", "https://creativecommons.org/publicdomain/zero/1.0/",
           "Narberth Castle on its hill, painted by Alphonse Dousseau", "Castell Arberth ar ei fryn, gan Alphonse Dousseau"),
    "Branwen drudwy.JPG": ("W. Williams", "Public domain", _PD,
           "Branwen with her starling in the court of Matholwch", "Branwen a’i drudwy yn llys Matholwch"),
    "Dinas Dinlle.jpg": ("Dwalad", "CC BY-SA 4.0", _BYSA + "4.0",
           "Sunset seen from the hillfort of Dinas Dinlle, Lleu’s fort, on the coast of Arfon", "Machlud o fryngaer Dinas Dinlle, caer Lleu, ar arfordir Arfon"),
    "Longbowmen.jpg": ("Luttrell Psalter, British Library", "Public domain", _PD,
                       "Archers at practice with the longbow, from the Luttrell Psalter of about 1325", "Saethwyr yn ymarfer â’r bwa hir, o Sallwyr Luttrell, tua 1325"),
    "Gaiman, Chubut ca.1911.jpg": ("Unknown photographer", "Public domain", _PD,
                                   "Gaiman, in the Welsh settlement of Y Wladfa in Patagonia, about 1911", "Y Gaiman, yn y Wladfa ym Mhatagonia, tua 1911"),
    "Vista de Gaiman.JPG": ("Gastón Cuello", "CC BY-SA 3.0", _BYSA + "3.0/",
                            "Gaiman in the Chubut valley, Patagonia, founded by Welsh settlers", "Y Gaiman yn nyffryn Camwy, Patagonia, a sefydlwyd gan wladfawyr o Gymru"),
    "Glastonbury Abbey Ruins 2.JPG": ("Mimihitam", "CC BY-SA 3.0", _BYSA + "3.0/",
                                      "The ruins of Glastonbury Abbey, Ynys Wydrin", "Adfeilion Abaty Glastonbury, Ynys Wydrin"),
    "Castle from pier, Dumbarton, Scotland-LCCN2001705975.jpg": ("Detroit Publishing Co., Library of Congress", "Public domain", _PD,
                                                                 "Dumbarton Rock, Alt Clut, the old fortress of the kings of Ystrad Clud, about 1895", "Craig Dumbarton, Alclud, hen gaer brenhinoedd Ystrad Clud, tua 1895"),
}

# The writers who recorded early Wales (src/writers.py): their pictures, and the long read's.
EXTRA["Ricemarch Psalter, Psalm 1.JPG"] = ("Ithael and Ieuan ap Sulien, Llanbadarn Fawr; Trinity College Dublin", "Public domain", _PD,
                                         "The opening of Psalm 1 in the Rhygyfarch Psalter, made at Llanbadarn Fawr about 1080",
                                         "Dechrau Salm 1 yn Sallwyr Rhygyfarch, a wnaed yn Llanbadarn Fawr tua 1080")
PAGE.update({
    "story-writers.html": "c:Ricemarch Psalter, Psalm 1.JPG@50% 20%",
    "person-gerallt-gymro.html": "g:person-gerallt-gymro",
    "person-asser.html": "g:person-asser",
    "person-nennius.html": "g:land-dinas-emrys",
    "person-rhygyfarch.html": "g:holy-llanbadarn",
    "person-ieuan-ap-sulien.html": "c:Ricemarch Psalter, Psalm 1.JPG@50% 20%",
    "person-elfoddw.html": "g:holy-bangor",
    "person-lifris.html": "g:holy-llandaff",
    "person-caradog-llancarfan.html": "c:Glastonbury Abbey Ruins 2.JPG",
    "person-walter-map.html": "l:lady",
    "person-adam-of-usk.html": "g:trea-pennal-letter",
    "person-gutun-owain.html": "g:holy-basingwerk",
})

# The Bruts (src/bruts.py) and the old books of Wales, one page each (src/oldbooks.py): the picture at the top of each page.
_CC0 = "https://creativecommons.org/publicdomain/zero/1.0/"
EXTRA.update({
    "Jesus-College-MS-111 00115 58r (cropped) Brut y Tywysogion.jpg": ("Hywel Fychan ap Hywel Goch and others; Jesus College, Oxford", "CC BY 4.0", _BY + "4.0/",
        "The chronicle of the princes in the Red Book of Hergest, written about 1400", "Cronicl y tywysogion yn Llyfr Coch Hergest, a ysgrifennwyd tua 1400"),
    "Chronical of the Princes (f.260).jpg": ("Medieval scribe; National Library of Wales, Peniarth MS 20", "CC0", _CC0,
        "A page of Brut y Tywysogion in Peniarth 20", "Tudalen o Frut y Tywysogion yn Peniarth 20"),
    "Catgualart fili' catguolaum obiit.png": ("Medieval scribe; British Library, Harley MS 3859", "Public domain", _PD,
        "The Annals of Wales in Harley 3859, the oldest copy of the History of the Britons", "Anodau Cymru yn Harley 3859, y copi hynaf o Hanes y Brythoniaid"),
    "Liber Landavensis binding.png": ("Medieval craftsman; National Library of Wales", "CC0", _CC0,
        "The binding of the Book of Llandaf", "Rhwymiad Llyfr Llandaf"),
    "Llyfr Gwyn Rhydderch f. 45 r. Beginning of Macsen Wledig.png": ("Medieval scribe; National Library of Wales", "CC0", _CC0,
        "The opening of the Dream of Macsen Wledig in the White Book of Rhydderch", "Dechrau Breuddwyd Macsen Wledig yn Llyfr Gwyn Rhydderch"),
    "Hendregadredd Manuscript-small.jpg": ("Medieval scribe; National Library of Wales", "Public domain", _PD,
        "A page of the Hendregadredd Manuscript", "Tudalen o Lawysgrif Hendregadredd"),
    "Jesus-College-MS-119 00007 2r.jpg": ("Jesus College, Oxford; photograph by the Bodleian Libraries", "CC BY 4.0", _BY + "4.0/",
        "A later owner’s note in the Book of the Anchorite: it was written for Gruffudd ap Llywelyn of Cantref Mawr in 1346", "Nodyn gan berchennog diweddarach yn Llyfr Ancr: fe’i hysgrifennwyd i Ruffudd ap Llywelyn o’r Cantref Mawr yn 1346"),
    "Llyfr du Basing (4401103).jpg": ("Gutun Owain and an earlier scribe; National Library of Wales", "CC0", _CC0,
        "A page of the Black Book of Basingwerk", "Tudalen o Lyfr Du Basing"),
    "Peniarth, Merionethshire 06.jpeg": ("Thomas Nicholls", "Public domain", _PD,
        "Peniarth, near Tywyn, home of the Peniarth manuscripts until 1904", "Peniarth, ger Tywyn, cartref llawysgrifau Peniarth hyd 1904"),
    "Yny_Lhyvyr_hwnn_title_page.jpg": ("Sir John Price; National Library of Wales", "CC0", _CC0,
        "The title page of Yny lhyvyr hwnn, 1546, the first book printed in Welsh", "Wyneb-ddalen Yny lhyvyr hwnn, 1546, y llyfr cyntaf a argraffwyd yn Gymraeg"),
    "WYNNE, Ellis (1671-1734). Gweledigaetheu y bardd cwsc. London; E. Powell, 1703.jpg": ("Ellis Wynne; photograph by Christie’s", "Public domain", _PD,
        "The title page of the first edition of the Visions of the Sleeping Bard, 1703", "Wyneb-ddalen argraffiad cyntaf Gweledigaetheu y Bardd Cwsc, 1703"),
    "Drych y Prif Oesoedd Ab Owen (Carreg Arthur, Abertawe).jpg": ("From O. M. Edwards’s edition of Drych y Prif Oesoedd", "Public domain", _PD,
        "Carreg Arthur on Gower, from O. M. Edwards’s edition of Drych y Prif Oesoedd", "Carreg Arthur ar Benrhyn Gŵyr, o argraffiad O. M. Edwards o Ddrych y Prif Oesoedd"),
})
PAGE.update({
    "story-bruts.html": "c:Jesus-College-MS-111 00115 58r (cropped) Brut y Tywysogion.jpg",
    "book-llandeilo.html": "g:trea-st-chad",
    "book-juvencus.html": "c:Ricemarch Psalter, Psalm 1.JPG@50% 20%",
    "book-historia.html": "c:Catgualart fili' catguolaum obiit.png",
    "book-llandaf.html": "c:Liber Landavensis binding.png",
    "book-black.html": "g:trea-black-book",
    "book-aneirin.html": "g:trea-book-aneirin",
    "book-taliesin.html": "g:trea-book-taliesin",
    "book-red.html": "g:trea-red-book",
    "book-white.html": "c:Llyfr Gwyn Rhydderch f. 45 r. Beginning of Macsen Wledig.png",
    "book-hendregadredd.html": "c:Hendregadredd Manuscript-small.jpg",
    "book-laws.html": "g:trea-laws-hywel",
    "book-brut-tywysogion.html": "c:Chronical of the Princes (f.260).jpg@50% 30%",
    "book-brut-brenhinedd.html": "p:cadwallon",
    "book-llyfr-ancr.html": "c:Jesus-College-MS-119 00007 2r.jpg",
    "book-basingwerk.html": "c:Llyfr du Basing (4401103).jpg",
    "book-peniarth.html": "c:Peniarth, Merionethshire 06.jpeg",
    "book-yny.html": "c:Yny_Lhyvyr_hwnn_title_page.jpg",
    "book-testament.html": "p:william-salesbury",
    "book-bible.html": "g:trea-bible-1588",
    "book-bardd-cwsc.html": "c:WYNNE, Ellis (1671-1734). Gweledigaetheu y bardd cwsc. London; E. Powell, 1703.jpg",
    "book-drych.html": "c:Drych y Prif Oesoedd Ab Owen (Carreg Arthur, Abertawe).jpg",
    "book-myvyrian.html": "g:person-iolo-morganwg",
})

# Yr Hen Ogledd, the Old North: the long read and the Men of the North (src/hen_ogledd.py)
EXTRA.update({
    "Castle Rock Edinburgh.jpg": ("Scglossop1", "CC BY-SA 4.0", _BYSA + "4.0",
        "Castle Rock in Edinburgh, Din Eidyn, the stronghold of Mynyddog Mwynfawr and the Gododdin", "Craig y Castell yng Nghaeredin, Din Eidyn, cadarnle Mynyddog Mwynfawr a’r Gododdin"),
    "Dumbarton Castle from the south.JPG": ("Rosser1954", "CC BY-SA 4.0", _BYSA + "4.0",
        "Dumbarton Rock, Alt Clut, the Rock of the Clyde, seat of the kings of Ystrad Clud", "Craig Dumbarton, Alclud, Craig y Clud, sedd brenhinoedd Ystrad Clud"),
    "Dumbarton Castle and rock, south-east view.JPG": ("Rosser1954", "CC BY-SA 4.0", _BYSA + "4.0",
        "The twin peaks of Dumbarton Rock, Alt Clut, which King Arthgal held against the Vikings in 870", "Dau gopa Craig Dumbarton, Alclud, a ddaliodd y Brenin Arthgal yn erbyn y Llychlynwyr yn 870"),
    "Traprain Law from the north.JPG": ("Kim Traynor", "CC BY-SA 3.0", _BYSA + "3.0",
        "Traprain Law, the great hill fort of the Votadini, the Gododdin of Roman times", "Traprain Law, bryngaer fawr y Votadini, Gododdin oes Rhufain"),
    "LindisfarneCastleHolyIsland.jpg": ("Matthew Hunt", "CC BY 2.0", _BY + "2.0",
        "Lindisfarne, Ynys Metcaud, where Urien and the kings of the Britons besieged the Angles for three days and three nights", "Lindisfarne, Ynys Fedcawd, lle gwarchaeodd Urien a brenhinoedd y Brythoniaid ar yr Eingl am dri diwrnod a thair noson"),
    "Lindisfarne Castle, Holy Island, Northumberland MET DP821127.jpg": ("Thomas Girtin; Metropolitan Museum of Art", "CC0", "https://creativecommons.org/publicdomain/zero/1.0/",
        "Lindisfarne, Holy Island, drawn by Thomas Girtin in 1796–97", "Lindisfarne, Ynys Fedcawd, gan Thomas Girtin yn 1796–97"),
    "Arthuret Church and tower, Longtown, Cumbria, England.jpg": ("Rosser1954", "CC BY-SA 4.0", _BYSA + "4.0",
        "Arthuret church by the river Esk, near the field of Arfderydd", "Eglwys Arthuret ger afon Esk, ger maes Arfderydd"),
    "Carved sarcophagus in Govan Old Church.jpg": ("Joedkins", "CC BY-SA 3.0", _BYSA + "3.0",
        "The carved sarcophagus of Govan, made for a king or saint of Strathclyde in the age of its last kings", "Arch gerfiedig Govan, a wnaed i frenin neu sant o Ystrad Clud yn oes ei frenhinoedd olaf"),
    "Castle from pier, Dumbarton, Scotland-LCCN2001705975.jpg": ("Photochrom Print Collection, Library of Congress", "Public domain", _PD,
        "Dumbarton Rock, Alt Clut, from the pier, about 1895", "Craig Dumbarton, Alclud, o’r pier, tua 1895"),
})
PAGE.update({
    "story-hen-ogledd.html": "c:Castle Rock Edinburgh.jpg",
    "person-cynfarch-oer.html": "g:trea-book-taliesin",
    "person-rhun-ab-urien.html": "c:LindisfarneCastleHolyIsland.jpg",
    "person-rhiainfellt.html": "c:Lindisfarne Castle, Holy Island, Northumberland MET DP821127.jpg",
    "person-dyfnwal-hen.html": "c:Dumbarton Castle from the south.JPG",
    "person-nudd-hael.html": "g:trea-red-book",
    "person-mordaf-hael.html": "g:trea-red-book",
    "person-elidir-mwynfawr.html": "g:place-caernarfon",
    "person-dunod-fawr.html": "g:holy-bangor",
    "person-eliffer-gosgorddfawr.html": "c:Arthuret Church and tower, Longtown, Cumbria, England.jpg",
    "person-ceredig-ap-gwallog.html": "g:trea-book-taliesin",
    "person-owain-ap-beli.html": "c:Castle from pier, Dumbarton, Scotland-LCCN2001705975.jpg",
    "person-arthgal.html": "c:Dumbarton Castle and rock, south-east view.JPG",
    "person-owain-foel.html": "c:Carved sarcophagus in Govan Old Church.jpg",
    "person-talhaearn.html": "g:trea-book-taliesin",
    "person-gwenddolau.html": "c:Arthuret Church and tower, Longtown, Cumbria, England.jpg",
    "person-mynyddog-mwynfawr.html": "c:Castle Rock Edinburgh.jpg",
})

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
    if kind == "c":
        by, lic, licu, en, cy = EXTRA[key]
        loc = _LOCAL.get(key)
        if loc:
            return dict(src=f"photos/{loc[0]}.webp", small=f"photos/{loc[0]}-s.webp", w=loc[1], h=loc[2], file=key, by=by, lic=lic, licu=licu, en=en, cy=cy,
                        pos="50% 30%" if loc[2] > loc[1] * .9 else "50% 50%")
        u = COMMONS + "Special:FilePath/" + _q(key, safe="")  # until tools/fetch_photos.py has kept a copy on the site
        return dict(src=u + "?width=1280", small=u + "?width=600", w=1280, h=853, file=key, by=by, lic=lic, licu=licu, en=en, cy=cy, pos="50% 50%", remote=True)
    if kind == "l":
        ph = A.LEGEND_PHOTOS[key]
        return dict(src=f"legends/{key}.webp", small=f"legends/{key}-s.webp", w=1280, h=853, file=ph[0], by=ph[1], lic=ph[2], licu=ph[3], en=ph[4], cy=ph[5], pos=ph[6])
    raise KeyError(ref)


def check():
    """Stop the build if a picture named here is missing (a typo, or a gallery picture taken out)."""
    for ref in list(ERA.values()) + list(PAGE.values()) + W10:
        p = _parse(ref)
        if p.get("remote"):
            continue
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


def card_img(path, era=None, sizes="(max-width: 700px) 100vw, 40vw"):
    """The picture for a card that links to a page (a long read, a legend, an age), or None.
    sizes tells the browser how wide the card is drawn, so phones fetch the 600 px picture when that is enough."""
    ref = for_page(path, era)
    if not ref:
        return None
    p = _parse(ref)
    return (f'<img class="scene photo" src="{p["small"]}" srcset="{p["small"]} 600w, {p["src"]} {p["w"]}w" sizes="{sizes}" '
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


# The medieval manuscripts of Wales (src/manuscripts.py): page tops, with the credits from its FIGS.
import manuscripts as _MSS  # noqa: E402
EXTRA.update({f[0]: (f[1], f[2], f[3], f[4], f[5]) for f in _MSS.FIGS.values() if f[0] not in EXTRA})
PAGE.update({
    "manuscripts.html": "c:" + _MSS.FIGS["llb-king"][0] + "@50% 25%",
    "book-classbook.html": "c:" + _MSS.FIGS["classbook"][0] + "@50% 30%",
    "book-martianus.html": "g:place-stdavids",
    "book-computus.html": "c:" + _MSS.FIGS["computus-easter"][0] + "@50% 30%",
    "book-ricemarch-psalter.html": "c:Ricemarch Psalter, Psalm 1.JPG@50% 20%",
    "book-de-trinitate.html": "g:holy-llanbadarn",
    "book-annales.html": "c:Catgualart fili' catguolaum obiit.png",
    "book-vespasian.html": "g:place-llanilltud",
    "book-chirk.html": "c:ChirkCodex.png@50% 30%",
    "book-peniarth-28.html": "c:Laws of Hywel Dda (f.1.v) King Hywel cropped.jpg@50% 30%",
    "book-boston.html": "c:Boston Welsh Law Ms (f.6.v).jpg@50% 30%",
    "book-peniarth-6.html": "c:Branwen drudwy.JPG@50% 40%",
    "book-peniarth-16.html": "c:" + _MSS.FIGS["macsen"][0] + "@50% 30%",
    "book-peniarth-17.html": "g:person-gruffudd-ap-cynan",
    "book-llanstephan-1.html": "c:" + _MSS.FIGS["pen44"][0] + "@50% 30%",
    "book-jesus-20.html": "g:place-dinefwr",
    "book-talgarth.html": "g:trea-red-book",
    "book-myddfai.html": "g:land-llyn-y-fan",
    "book-llanbeblig.html": "c:" + _MSS.FIGS["llb-annunciation"][0] + "@50% 30%",
    "book-cwta-cyfarwydd.html": "c:" + _MSS.FIGS["cwta"][0] + "@50% 30%",
    "book-lewys-glyn-cothi.html": "g:place-rhaglan",
    "book-gwyn-hergest.html": "c:" + _MSS.FIGS["hergest"][0],
})


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

# Yma o Hyd: how the Welsh language came back (src/welshrevival.py)
EXTRA["Dafydd Iwan, Caerfyrddin, 2023, Cymdeithas yr Iaith.jpg"] = ("Cwmcafit", "CC BY-SA 4.0", _BYSA + "4.0",
    "Dafydd Iwan sings Yma o Hyd to the Cymdeithas yr Iaith census rally in Carmarthen, January 2023",
    "Dafydd Iwan yn canu Yma o Hyd i rali cyfrifiad Cymdeithas yr Iaith yng Nghaerfyrddin, Ionawr 2023")
PAGE["story-welsh-revival.html"] = "c:Dafydd Iwan, Caerfyrddin, 2023, Cymdeithas yr Iaith.jpg@50% 40%"

# the photo of each town, for its own page (src/town_pics.py, src/townpages.py)
import town_pics as _TP  # noqa: E402
EXTRA.update({k: v for k, v in _TP.EXTRA.items() if k not in EXTRA})
