# Visiting: who looks after each place, its official page, postcode and how to get in (November 2026).
# Ifan asked that people can visit these places. Each place page shows a "Visiting" box, and the map card shows
# a short line with the official link and directions.
#
# We never copy opening times or prices: they change. We link the official page instead, and say only what is
# stable (free, ticketed, open land, private). Postcodes come from the official pages; leave pc="" when there is none.
#
# V(who, url, pc, entry, also=[...], note=(en, cy))
#   who    a key of WHO below, or (English, Welsh) for anyone else
#   url    the official page for opening times and prices ("" if there is none)
#   pc     postcode for satnav
#   entry  a key of ENTRY below
#   also   other bodies on the same site: [(who, url, what en, what cy)]
#   note   one short line that helps a visitor (optional)

WHO = {
    "cadw": ("Cadw", "Cadw"),
    "nt": ("the National Trust", "yr Ymddiriedolaeth Genedlaethol"),
    "amg": ("Amgueddfa Cymru – Museum Wales", "Amgueddfa Cymru"),
    "church": ("the parish church", "yr eglwys blwyf"),
    "council": ("the local council", "y cyngor lleol"),
    "nrw": ("Natural Resources Wales", "Cyfoeth Naturiol Cymru"),
    "private": ("private owners", "perchnogion preifat"),
    "town": ("the town, open to all", "y dref, yn agored i bawb"),
    "land": ("open land; the monument is protected by Cadw", "tir agored; mae’r heneb wedi’i gwarchod gan Cadw"),
}

ENTRY = {
    "free": ("Free entry", "Mynediad am ddim"),
    "ticket": ("Paid entry: see the official page for prices", "Tâl mynediad: gweler y dudalen swyddogol am brisiau"),
    "open": ("Open land: free, at any reasonable time", "Tir agored: am ddim, ar unrhyw adeg resymol"),
    "outside": ("Private land: see it from the road or public footpath", "Tir preifat: gwelwch ef o’r ffordd neu’r llwybr cyhoeddus"),
    "partfree": ("Grounds free; some parts paid", "Y tir am ddim; tâl am rai rhannau"),
    "church": ("Free; open in daytime, services permitting", "Am ddim; ar agor yn ystod y dydd, pan nad oes gwasanaeth"),
}

CADW = "https://cadw.gov.wales/visit/places-to-visit/"
NT = "https://www.nationaltrust.org.uk/visit/wales/"


def V(who, url, pc, entry, also=(), note=None):
    return dict(who=who, url=url, pc=pc, entry=entry, also=list(also), note=note)


VISIT = {
    # ---------- royal seats and castles of the princes ----------
    "dinefwr": V("cadw", CADW + "castell-dinefwr", "SA19 6RT", "free",
                 also=[("nt", NT + "dinefwr", "the park, the car park and Newton House (paid)", "y parc, y maes parcio a Thŷ Newton (tâl)")],
                 note=("Park at the National Trust car park and walk up through the deer park.", "Parciwch ym maes parcio’r Ymddiriedolaeth Genedlaethol a cherdded i fyny drwy’r parc ceirw.")),
    "aberffraw": V("town", "", "", "open", note=("The court has gone; walk to the old bridge and St Beuno’s church.", "Mae’r llys wedi mynd; cerddwch at yr hen bont ac eglwys Beuno.")),
    "mathrafal": V("private", "", "", "outside", note=("The earthworks are by the junction of the A495 and B4389, near Meifod.", "Mae’r cloddiau ger cyffordd yr A495 a’r B4389, ger Meifod.")),
    "garthcelyn": V("town", "", "", "open", note=("Pen y Bryn is a private house. The village and the path to Aber Falls are open to all.", "Tŷ preifat yw Pen y Bryn. Mae’r pentref a’r llwybr i Raeadr Fawr yn agored i bawb.")),
    "llysrhosyr": V("cadw", CADW + "llys-rhosyr", "LL61 6SG", "free"),
    "dolbadarn": V("cadw", CADW + "castell-dolbadarn", "LL55 4UB", "free"),
    "ybere": V("cadw", CADW + "castell-y-bere", "LL36 9TS", "free"),
    "dolwyddelan": V("cadw", CADW + "castell-dolwyddelan", "LL25 0JD", "free",
                     note=("The keep is open on set days; the grounds belong to the farm below.", "Mae’r gorthwr ar agor ar ddyddiau penodol; mae’r tir yn eiddo i’r fferm islaw.")),
    "dinasemrys": V("nt", NT + "craflwyn-and-beddgelert", "LL55 4NG", "open",
                    note=("Start from the National Trust car park at Craflwyn; the path is steep and rough.", "Dechreuwch o faes parcio’r Ymddiriedolaeth Genedlaethol yng Nghraflwyn; mae’r llwybr yn serth ac yn arw.")),
    "cricieth": V("cadw", CADW + "castell-cricieth", "LL52 0DP", "ticket"),
    "dolforwyn": V("cadw", CADW + "castell-dolforwyn", "", "free"),
    "dryslwyn": V("cadw", CADW + "castell-dryslwyn", "", "free"),
    "carregcennen": V("cadw", CADW + "castell-carreg-cennen", "SA19 6UA", "ticket",
                      note=("Tickets from Castell Farm at the foot of the hill, which runs the site with Cadw.", "Tocynnau o Fferm y Castell wrth droed y bryn, sy’n rhedeg y safle gyda Cadw.")),
    "ewloe": V("cadw", CADW + "castell-ewloe", "CH5 3BZ", "free"),
    "deganwy": V("town", "", "", "open", note=("Footpaths climb to the two summits from the town.", "Mae llwybrau’n dringo i’r ddau gopa o’r dref.")),
    "dinasbran": V(("Denbighshire County Council, with Cadw", "Cyngor Sir Ddinbych, gyda Cadw"), "", "", "open",
                   note=("A steep, exposed climb from Llangollen: wear good shoes.", "Dringfa serth ac agored o Langollen: gwisgwch esgidiau da.")),
    "cwmhir": V(("Abbey Cwmhir Hall and the village", "Neuadd Abaty Cwm-hir a’r pentref"), "", "", "open"),
    "powis": V("nt", NT + "powis-castle-and-garden", "SY21 8RF", "ticket"),
    "kidwelly": V("cadw", CADW + "kidwelly-castle", "SA17 5BQ", "ticket"),
    "llanymddyfri": V("town", "", "", "open", note=("The castle mound and the statue are beside the main car park.", "Mae tomen y castell a’r cerflun wrth ymyl y prif faes parcio.")),
    "cilmeri": V("town", "", "", "open", note=("The memorial is beside the A483 at Cilmeri, west of Builth Wells.", "Mae’r gofeb wrth ymyl yr A483 yng Nghilmeri, i’r gorllewin o Lanfair-ym-Muallt.")),
    "cardigan": V(("Cardigan Castle (Cadwgan Building Preservation Trust)", "Castell Aberteifi (Ymddiriedolaeth Cadwgan)"), "https://www.cardigancastle.com", "SA43 1JA", "ticket"),

    # ---------- saints, abbeys and holy places ----------
    "strataflorida": V("cadw", CADW + "strata-florida-abbey", "SY25 6ES", "free",
                       note=("The princes of Deheubarth lie here; Dafydd ap Gwilym is said to lie under a yew in the churchyard next door.", "Yma y gorwedd tywysogion Deheubarth; dywedir bod Dafydd ap Gwilym yn gorwedd dan ywen ym mynwent yr eglwys drws nesaf.")),
    "vallecrucis": V("cadw", CADW + "valle-crucis-abbey", "LL20 8DD", "free",
                     note=("Eliseg’s Pillar stands in a field a short walk up the valley.", "Saif Colofn Eliseg mewn cae ychydig i fyny’r cwm.")),
    "eliseg": V("cadw", CADW + "elisegs-pillar", "LL20 8DD", "free",
                note=("A short walk from Valle Crucis Abbey; see both in one visit.", "Taith gerdded fer o Abaty Glyn y Groes; gwelwch y ddau mewn un ymweliad.")),
    "penmon": V("cadw", CADW + "penmon-priory-cross-and-st-seiriols-well", "LL58 8RW", "free",
                note=("The priory church is still used for worship; Seiriol’s well is a short walk behind it.", "Mae eglwys y priordy’n dal i gael ei defnyddio i addoli; mae ffynnon Seiriol ychydig gamau y tu ôl iddi.")),
    "talley": V("cadw", CADW + "talley-abbey", "SA19 7YY", "free"),
    "basingwerk": V("cadw", CADW + "basingwerk-abbey", "CH8 7GH", "free",
                    note=("The abbey sits in Greenfield Valley; a path leads up the valley to St Winefride’s Well.", "Mae’r abaty yn Nyffryn Maes Glas; mae llwybr yn arwain i fyny’r cwm i Ffynnon Gwenffrewi.")),
    "treffynnon": V("cadw", CADW + "st-winefrides-chapel-and-well", "CH8 7PN", "ticket",
                    note=("A living place of pilgrimage, cared for day to day by St Winefride’s Shrine.", "Man pererindod byw, sy’n cael ei warchod o ddydd i ddydd gan Gysegrfa Gwenffrewi.")),
    "maenachwyfan": V("cadw", CADW + "maen-achwyfan-cross", "CH8 9DD", "free"),
    "margam": V("cadw", CADW + "margam-stones-museum", "SA13 2TA", "free",
                note=("The stones museum opens on set days; the abbey church beside it is still a parish church.", "Mae amgueddfa’r cerrig ar agor ar ddyddiau penodol; mae eglwys yr abaty wrth ei hymyl yn dal yn eglwys blwyf.")),
    "neathabbey": V("cadw", CADW + "neath-abbey", "SA10 7DW", "free"),
    "tintern": V("cadw", CADW + "tintern-abbey", "NP16 6SE", "ticket"),
    "llanthony": V("cadw", CADW + "llanthony-priory", "NP7 7NN", "free",
                   note=("Deep in the Black Mountains; the road up the Vale of Ewyas is narrow.", "Yn ddwfn yn y Mynydd Du; mae’r ffordd i fyny Dyffryn Ewias yn gul.")),
    "cymer": V("cadw", CADW + "cymer-abbey", "LL40 2HE", "free"),
    "stnons": V("cadw", CADW + "st-nons-chapel", "SA62 6BN", "open",
                note=("A short walk from St Davids along the coast path; St Non’s holy well is beside the chapel.", "Taith gerdded fer o Dyddewi ar hyd llwybr yr arfordir; mae ffynnon Non wrth ymyl y capel.")),
    "carewcross": V("cadw", CADW + "carew-cross", "", "open",
                    note=("The cross stands by the road at the entrance to Carew Castle.", "Saif y groes wrth y ffordd wrth fynedfa Castell Caeriw.")),
    "caergybi": V("cadw", CADW + "caer-gybi-roman-fort", "LL65 1UB", "free",
                  note=("The Roman walls wrap round St Cybi’s church in the middle of Holyhead.", "Mae’r muriau Rhufeinig yn amgylchynu eglwys Cybi yng nghanol Caergybi.")),
    "enlli": V(("the Bardsey Island Trust", "Ymddiriedolaeth Ynys Enlli"), "https://enlli.org/visit", "", "ticket",
               note=("Boats run from Porth Meudwy, April to October, when the weather allows; there is a landing fee.", "Mae cychod yn mynd o Borth Meudwy, Ebrill i Hydref, pan fydd y tywydd yn caniatáu; mae tâl glanio.")),
    "pennantmelangell": V("church", "https://stmelangell.org/the-shrine-church-of-saint-melangell/", "SY10 0HQ", "church",
                          note=("At the head of the Tanat valley beyond Llangynog; the road ends at the church.", "Ym mhen draw Cwm Tanad y tu hwnt i Langynog; mae’r ffordd yn gorffen wrth yr eglwys.")),
    "llandaf": V(("Llandaff Cathedral", "Eglwys Gadeiriol Llandaf"), "https://www.llandaffcathedral.org.uk", "", "church"),
    "llanelwy": V(("St Asaph Cathedral", "Eglwys Gadeiriol Llanelwy"), "https://stasaphcathedral.wales/", "", "church"),
    "bangor": V(("Bangor Cathedral", "Eglwys Gadeiriol Bangor"), "", "", "church"),
    "llanilltud": V("church", "", "", "church",
                    note=("St Illtud’s church keeps the carved stones of the old monastery in its Galilee chapel.", "Mae eglwys Illtud yn cadw cerrig cerfiedig yr hen fynachlog yn ei chapel Galilea.")),
    "nanhyfer": V("church", "", "", "church",
                  note=("See the great cross and the bleeding yew in the churchyard.", "Gwelwch y groes fawr a’r ywen waedlyd yn y fynwent.")),
    "clynnog": V("church", "", "", "church"),
    "llanddewibrefi": V("church", "", "", "church"),
    "llancarfan": V("church", "", "", "church"),
    "llanbadarn": V("church", "", "", "church"),

    # ---------- Roman Wales, hillforts and tombs ----------
    "caerleon": V("cadw", CADW + "caerleon-roman-fortress-and-baths", "NP18 1AE", "ticket",
                  also=[("amg", "https://museum.wales/roman/", "the National Roman Legion Museum (free)", "Amgueddfa Lleng Rufeinig Cymru (am ddim)")],
                  note=("The amphitheatre and barracks are free to walk round; the baths are paid.", "Mae’r amffitheatr a’r barics am ddim; mae tâl am y baddonau.")),
    "caerwent": V("cadw", CADW + "caerwent-roman-town", "NP26 5BA", "free"),
    "segontium": V("cadw", CADW + "segontium-roman-fort", "LL55 2LN", "free",
                   note=("Parking is limited to a few spaces on the main road beside the fort.", "Dim ond ychydig o leoedd parcio sydd ar y brif ffordd wrth ymyl y gaer.")),
    "dolaucothi": V("nt", NT + "dolaucothi", "SA19 8US", "ticket",
                    note=("The mine closes in winter; the woodland walks stay open all year.", "Mae’r gloddfa ar gau yn y gaeaf; mae’r llwybrau coed ar agor drwy’r flwyddyn.")),
    "ygaer": V("cadw", CADW + "brecon-gaer-roman-fort", "LD3 9NT", "free",
               note=("On a working farm with no car park: walk in along the lane.", "Ar fferm weithiol heb faes parcio: cerddwch i mewn ar hyd y lôn.")),
    "tomenymur": V("land", "", "", "open",
                   note=("A one-mile waymarked walk starts from the small car park on a lane off the A487.", "Mae taith filltir ag arwyddion yn dechrau o’r maes parcio bach ar lôn oddi ar yr A487.")),
    "moridunum": V("council", "", "", "open", note=("The amphitheatre is on Priory Street, east of the town centre.", "Mae’r amffitheatr ar Heol y Prior, i’r dwyrain o ganol y dref.")),
    "dinlligwy": V("cadw", CADW + "din-lligwy-hut-group", "", "free",
                   note=("Off the A5025 about a mile north of Llanallgo; Capel Lligwy and the Lligwy tomb are a few minutes’ walk.", "Oddi ar yr A5025 tua milltir i’r gogledd o Lanallgo; mae Capel Lligwy a siambr Lligwy ychydig funudau o gerdded.")),
    "llanmelin": V("cadw", CADW + "llanmelin-wood-hillfort", "NP16 6LN", "free"),
    "caerytwr": V("cadw", CADW + "caer-y-twr", "", "open",
                  note=("A climb to the summit of Holyhead Mountain from the South Stack road.", "Dringfa i gopa Mynydd Twr o ffordd Ynys Lawd.")),
    "tymawr": V("cadw", CADW + "holyhead-mountain-hut-circles", "LL65 1YH", "free"),
    "caerdrewyn": V("private", "", "", "outside"),
    "trerceiri": V("land", "", "", "open",
                   note=("A steep path from the B4417 between Llanaelhaearn and Llithfaen. Please don’t move any stones.", "Llwybr serth o’r B4417 rhwng Llanaelhaearn a Llithfaen. Peidiwch â symud cerrig, os gwelwch yn dda.")),
    "castellhenllys": V(("the Pembrokeshire Coast National Park Authority", "Awdurdod Parc Cenedlaethol Arfordir Penfro"),
                        "https://www.pembrokeshirecoast.wales/castell-henllys/about-castell-henllys", "SA41 3UR", "ticket"),
    "brynceliddu": V("cadw", CADW + "bryn-celli-ddu-burial-chamber", "LL61 6EQ", "free"),
    "pentreifan": V("cadw", CADW + "pentre-ifan-burial-chamber", "SA41 3TZ", "free"),
    "barclodiad": V("cadw", CADW + "barclodiad-y-gawres-burial-chamber", "LL63 5TE", "free",
                    note=("Park at Porth Trecastell. You can see the tomb from outside all year; Cadw opens it for guided tours on some summer days.", "Parciwch ym Mhorth Trecastell. Gallwch weld y siambr o’r tu allan drwy’r flwyddyn; mae Cadw’n ei hagor ar gyfer teithiau tywys ar rai dyddiau yn yr haf.")),
    "tinkinswood": V("cadw", CADW + "tinkinswood-burial-chamber", "CF5 6TA", "free"),
    "parclebreos": V("cadw", CADW + "parc-le-breos-burial-chamber", "SA3 2HA", "free"),
    "maenceti": V("land", "", "", "open", note=("On common land on Cefn Bryn, a short walk north from the Reynoldston road.", "Ar dir comin ar Gefn Bryn, taith fer i’r gogledd o ffordd Reynoldston.")),
    "carregsamson": V("private", "", "", "open", note=("Near the Coast Path, about half a mile west of Abercastle.", "Ger Llwybr yr Arfordir, tua hanner milltir i’r gorllewin o Abercastell.")),
    "mold": V("town", "", "", "outside",
              note=("The cape is in the British Museum in London; small pieces are at the Daniel Owen Centre in Mold.", "Mae’r fantell yn yr Amgueddfa Brydeinig yn Llundain; mae darnau bach yng Nghanolfan Daniel Owen yn yr Wyddgrug.")),
    "cerrigbach": V("amg", "", "", "outside",
                    note=("The finds are at National Museum Cardiff (free).", "Mae’r darganfyddiadau yn Amgueddfa Genedlaethol Caerdydd (am ddim).")),

    # ---------- Glyndŵr, the Tudors, industry and today ----------
    "sycharth": V("cadw", "", "", "open",
                  note=("A small car park with information boards on the lane near the B4580, south of Llansilin.", "Maes parcio bach gyda byrddau gwybodaeth ar y lôn ger y B4580, i’r de o Lansilin.")),
    "pilleth": V("church", "", "", "church",
                 note=("The Wellingtonia trees on the hillside mark where the dead of Bryn Glas are said to lie.", "Mae’r coed Wellingtonia ar y llethr yn nodi lle dywedir bod meirw Bryn Glas yn gorwedd.")),
    "pennal": V("church", "", "", "church"),
    "conwy": V("cadw", CADW + "conwy-castle", "LL32 8AY", "ticket",
               note=("You can walk long stretches of the town walls.", "Gallwch gerdded darnau hir o furiau’r dref.")),
    "plasmawr": V("cadw", CADW + "plas-mawr", "LL32 8DE", "ticket",
                  note=("Closed in winter: open from March to the start of November.", "Ar gau yn y gaeaf: ar agor o fis Mawrth hyd ddechrau Tachwedd.")),
    "beaumaris": V("cadw", CADW + "beaumaris-castle", "LL58 8AP", "ticket"),
    "caernarfon": V("cadw", CADW + "caernarfon-castle", "LL55 2AY", "ticket"),
    "harlech": V("cadw", CADW + "harlech-castle", "LL46 2YH", "ticket"),
    "rhuddlan": V("cadw", CADW + "rhuddlan-castle", "LL18 5AB", "ticket"),
    "caerffili": V("cadw", CADW + "caerphilly-castle", "CF83 1JD", "ticket"),
    "rhaglan": V("cadw", CADW + "raglan-castle", "NP15 2BT", "ticket"),
    "chepstow": V("cadw", CADW + "chepstow-castle", "NP16 5EY", "ticket"),
    "tretower": V("cadw", CADW + "tretower-court-and-castle", "NP8 1RF", "ticket"),
    "blaenavon": V("cadw", CADW + "blaenavon-ironworks", "NP4 9RN", "ticket",
                   also=[("amg", "https://museum.wales/bigpit/", "Big Pit National Coal Museum (free)", "Amgueddfa Lofaol Cymru, y Pwll Mawr (am ddim)")]),
    "penfro": V(("Pembroke Castle Trust", "Ymddiriedolaeth Castell Penfro"), "https://pembrokecastle.co.uk/history/birthplace-of-henry-vii/", "SA71 4LA", "ticket",
                note=("Free guided tours at 11am and 1pm.", "Teithiau tywys am ddim am 11am ac 1pm.")),
    "penmynydd": V("private", "", "", "outside", note=("Plas Penmynydd is a private house; the church and almshouses are in the village.", "Tŷ preifat yw Plas Penmynydd; mae’r eglwys a’r elusendai yn y pentref.")),
    "chirk": V("nt", NT + "chirk-castle", "LL14 5AF", "partfree"),
    "erddig": V("nt", NT + "erddig", "LL13 0YT", "partfree"),
    "penrhyn": V("nt", NT + "penrhyn-castle-and-garden", "LL57 4HT", "ticket"),
    "tymawrwybrnant": V("nt", NT + "ty-mawr-wybrnant", "LL25 0HJ", "free",
                        note=("Satnav: use LL24 0UG for Penmachno and follow the brown signs. The house opens on set days, April to September.", "Llywio lloeren: defnyddiwch LL24 0UG ar gyfer Penmachno a dilynwch yr arwyddion brown. Mae’r tŷ ar agor ar ddyddiau penodol, Ebrill i Fedi.")),
    "bigpit": V("amg", "https://museum.wales/bigpit/", "NP4 9XP", "free",
                note=("A small charge for the underground tour; book ahead in busy times.", "Tâl bach am y daith dan ddaear; archebwch o flaen llaw ar adegau prysur.")),
    "stfagans": V("amg", "https://museum.wales/stfagans/", "CF5 6XB", "free"),
    "llanystumdwy": V("council", "https://www.gwynedd.llyw.cymru/en-gb/libraries-archives-and-culture/museums-and-the-arts/the-lloyd-george-museum", "LL52 0SH", "ticket",
                      note=("The museum opens from April to October.", "Mae’r amgueddfa ar agor o Ebrill i Hydref.")),
    "yrysgwrn": V(("the Eryri National Park Authority", "Awdurdod Parc Cenedlaethol Eryri"), "https://www.snowdonia.gov.wales/visiting/yr-ysgwrn", "", "ticket"),
    "wmc": V(("Wales Millennium Centre", "Canolfan Mileniwm Cymru"), "https://www.wmc.org.uk/en/what-we-do/our-building-and-people/our-building", "CF10 5AL", "free",
             note=("The building is open to walk into; shows are ticketed.", "Gallwch gerdded i mewn i’r adeilad; mae tocynnau i’r sioeau.")),
    "botanic": V(("the National Botanic Garden of Wales", "Gardd Fotaneg Genedlaethol Cymru"), "", "", "ticket"),
    # ---------- the other places on the map ----------
    "pontnewydd": V("private", "", "", "outside", note=("The cave is not open to visitors.", "Nid yw’r ogof ar agor i ymwelwyr.")),
    "paviland": V("land", "", "", "open", note=("Reached only at low tide over rough rocks below the Gower cliffs: check the tide times and take great care.", "Dim ond ar drai y gellir ei chyrraedd, dros greigiau garw dan glogwyni Gŵyr: gwiriwch amser y llanw a byddwch yn ofalus iawn.")),
    "orme": V(("Great Orme Mines", "Mwyngloddiau’r Gogarth"), "", "", "ticket", note=("The mines are on the Great Orme above Llandudno; the tramway stops nearby.", "Mae’r mwyngloddiau ar y Gogarth uwchben Llandudno; mae’r tramffordd yn aros gerllaw.")),
    "stdavids": V(("St Davids Cathedral", "Eglwys Gadeiriol Tyddewi"), "https://stdavidscathedral.org.uk/visit-us", "", "church",
                  also=[("cadw", CADW + "st-davids-bishops-palace", "the Bishop’s Palace next door (paid)", "Llys yr Esgob drws nesaf (tâl)")]),
    "machynlleth": V("town", "", "", "open", note=("Owain Glyndŵr’s Parliament House is on Heol Maengwyn in the town centre.", "Mae Senedd-dy Owain Glyndŵr ar Heol Maengwyn yng nghanol y dref.")),
    "dale": V("land", "", "", "open", note=("Walk to Mill Bay on the Pembrokeshire Coast Path from Dale.", "Cerddwch i Fae’r Felin ar Lwybr Arfordir Penfro o Dale.")),
    "llanrhaeadr": V("church", "", "", "church", note=("William Morgan was vicar here while he translated the Bible. Pistyll Rhaeadr is four miles up the valley.", "Roedd William Morgan yn ficer yma tra oedd yn cyfieithu’r Beibl. Mae Pistyll Rhaeadr bedair milltir i fyny’r cwm.")),
    "fishguard": V("land", "", "", "open", note=("A memorial stone stands on the headland, on the Pembrokeshire Coast Path.", "Saif carreg goffa ar y pentir, ar Lwybr Arfordir Penfro.")),
    "pontcysyllte": V("town", "", "", "open", note=("Free to walk across on the towpath; boats cross it too.", "Am ddim i’w groesi ar y llwybr tynnu; mae cychod yn ei groesi hefyd.")),
    "merthyr": V("town", "", "", "open"),
    "dinorwig": V("amg", "https://museum.wales/slate/", "", "free", note=("The National Slate Museum at Llanberis is closed for redevelopment: check before you go.", "Mae Amgueddfa Lechi Cymru yn Llanberis ar gau i’w hailddatblygu: gwiriwch cyn mynd.")),
    "celyn": V("town", "", "", "open", note=("The memorial chapel stands on the shore of Llyn Celyn beside the A4212.", "Saif y capel coffa ar lan Llyn Celyn wrth ymyl yr A4212.")),
    "aberfan": V("town", "", "", "open", note=("The memorial garden and the cemetery are in the village. Please visit quietly.", "Mae’r ardd goffa a’r fynwent yn y pentref. Ymwelwch yn dawel, os gwelwch yn dda.")),
    "menai": V("town", "", "", "open", note=("Walk across the bridge on its footpaths.", "Cerddwch dros y bont ar ei llwybrau troed.")),
    "library": V(("the National Library of Wales", "Llyfrgell Genedlaethol Cymru"), "https://www.library.wales", "", "free"),
    "epynt": V("private", "", "", "outside", note=("Much of Epynt is an army training range: keep to the public roads.", "Mae llawer o Epynt yn faes ymarfer y fyddin: cadwch at y ffyrdd cyhoeddus.")),
    "llangollen": V("town", "", "", "open"),
    "offasdyke": V("land", "", "", "open", note=("The Offa’s Dyke Path National Trail follows it from Chepstow to Prestatyn.", "Mae Llwybr Cenedlaethol Clawdd Offa yn ei ddilyn o Gas-gwent i Brestatyn.")),
    "hendygwyn": V("town", "", "", "open", note=("The Hywel Dda Centre and its garden are in the town.", "Mae Canolfan Hywel Dda a’i gardd yn y dref.")),
    "llanfaches": V("town", "", "", "open"),
    "ybala": V("town", "", "", "open"),
    "parys": V("land", "", "", "open", note=("Waymarked trails cross the copper mountain: keep to the paths.", "Mae llwybrau ag arwyddion yn croesi’r mynydd copr: cadwch at y llwybrau.")),
    "hafod": V("town", "", "", "open", note=("Paths run among the ruins of the copperworks by the river Tawe.", "Mae llwybrau’n rhedeg ymysg adfeilion y gwaith copr ger afon Tawe.")),
    "westgate": V("town", "", "", "open"),
    "tonypandy": V("town", "", "", "open"),
    "senghennydd": V("town", "", "", "open", note=("The Welsh National Mining Memorial stands in the village.", "Saif Cofeb Genedlaethol Glowyr Cymru yn y pentref.")),
    "penyberth": V("private", "", "", "outside"),
    "talacharn": V("town", "", "", "open", note=("Dylan Thomas’s Boathouse and writing shed are on the cliff path above the estuary.", "Mae Tŷ Cychod Dylan Thomas a’i sied ysgrifennu ar lwybr y clogwyn uwchben yr aber.")),
    "stadiwm": V(("the Principality Stadium", "Stadiwm Principality"), "", "", "ticket", note=("Matches and stadium tours are ticketed.", "Mae tocynnau i’r gemau a’r teithiau o amgylch y stadiwm.")),
    "trefflemin": V("church", "", "", "church"),
    "llanfairpwll": V("town", "", "", "open"),
    "bethlehem": V("town", "", "", "open"),
    "lavernock": V("land", "", "", "open"),
    "senedd": V(("the Senedd", "y Senedd"), "https://senedd.wales/visit/our-estate/plan-your-visit/", "", "free",
                note=("Open to visitors, with security checks at the door.", "Ar agor i ymwelwyr, gyda gwiriadau diogelwch wrth y drws.")),
}

import ages12 as _A12  # the places of the Age of Revival (src/ages12.py)
for _k, (_who, _url, _pc, _entry, _note) in _A12.VISIT.items():
    VISIT[_k] = V(_who, _url, _pc, _entry, note=_note)


CSS = """
.visit-box{margin:2rem 0 0;padding:1.2rem 1.3rem 1rem;border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:14px;background:var(--card)}
.visit-box h2{margin:0 0 .7rem;font-size:1.2rem}
.visit-box dl{margin:0;display:grid;gap:.55rem}
.visit-box dl>div{display:grid;grid-template-columns:9.5rem 1fr;gap:.2rem 1rem}
.visit-box dt{font-weight:700;color:var(--muted);font-size:.9rem}
.visit-box dd{margin:0}
.visit-box a{color:var(--gold)}
.visit-box b{letter-spacing:.03em}
.visit-note{margin:.8rem 0 0}
.visit-small{margin:.6rem 0 0;font-size:.85rem;color:var(--muted)}
@media(max-width:560px){.visit-box dl>div{grid-template-columns:1fr}}
.pl-links{margin-top:1.6rem;display:grid;gap:.5rem}
.pl-links .eyebrow{margin:0}
.pl-people{display:flex;flex-wrap:wrap;gap:.5rem;margin:0}
.pl-people a{display:inline-flex;padding:.45rem .8rem;border:1px solid var(--line);border-radius:999px;color:var(--ink);text-decoration:none;font-size:.9rem;font-weight:600;background:var(--card)}
.pl-people a:hover{border-color:var(--gold);color:var(--gold)}
.pc-visit{font-size:.88rem;margin:.2rem 0 .6rem;color:var(--muted)}
.pc-visit a{color:var(--gold)}
"""
