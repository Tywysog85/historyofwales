# The castles of Wales: the map page (castles.html).
# The list of sites, with their places and Welsh names, is src/castles_data.json, made by
# tools/castles_from_wikidata.py from a Wikidata snapshot. This file adds what a list cannot:
# who built the great castles, a line of their story, a photograph, and the groups on the map.
# Follow EDITORIAL.md: proud, true, nothing negative about the people of Welsh history.

GROUPS = [
 dict(id="welsh", en="Built by the Welsh", cy="Codwyd gan y Cymry", col="#e2453d",
      sumEn="Castles and courts of the princes and lords of Wales, from Dolwyddelan and Castell y Bere to Dinas Brân and Raglan.",
      sumCy="Cestyll a llysoedd tywysogion ac arglwyddi Cymru, o Ddolwyddelan a Chastell y Bere i Ddinas Brân a Rhaglan."),
 dict(id="crown", en="Built by the English Crown", cy="Codwyd gan Goron Lloegr", col="#8fa2f0",
      sumEn="The king’s castles: Edward I’s great ring in the north, and the castles of Henry III and William Rufus.",
      sumCy="Cestyll y brenin: cylch mawr Edward I yn y gogledd, a chestyll Harri III a Gwilym Goch."),
 dict(id="norman", en="Built by Norman and Marcher lords", cy="Codwyd gan arglwyddi’r Normaniaid a’r Mers", col="#c2a3f0",
      sumEn="The lords who pushed into Wales from 1067, and the Marcher lordships they held: Chepstow, Pembroke, Caerphilly and many more.",
      sumCy="Yr arglwyddi a wthiodd i mewn i Gymru o 1067 ymlaen, ac arglwyddiaethau’r Mers a ddaliwyd ganddynt: Cas-gwent, Penfro, Caerffili a llawer mwy."),
 dict(id="later", en="Tower houses and later castles", cy="Tyrau-dai a chestyll diweddarach", col="#5fcfc8",
      sumEn="Fortified houses of the later Middle Ages and the Tudor gentry, and the great castle-houses of the 1800s.",
      sumCy="Tai caerog yr Oesoedd Canol diweddar a’r uchelwyr Tuduraidd, a phlastai castellog mawr y 1800au."),
 dict(id="other", en="Mottes, ringworks and other sites", cy="Mwntiau, cylchfuriau a safleoedd eraill", col="#d6a46c",
      sumEn="Earth and timber castles and smaller sites whose builders were not written down. Normans raised many; Welsh princes and lords raised many too.",
      sumCy="Cestyll pridd a phren a safleoedd llai nad ysgrifennwyd enwau eu hadeiladwyr. Codwyd llawer gan y Normaniaid; codwyd llawer hefyd gan dywysogion ac arglwyddi Cymru."),
]

KINDS = {
 "mb": ("Motte and bailey", "Mwnt a beili",
        "An earth mound (the motte) that carried a timber tower, with a fenced yard (the bailey) below. Most were raised between about 1070 and 1220.",
        "Twmpath pridd (y mwnt) a gariai dŵr pren, gydag iard wedi’i hamgáu (y beili) islaw. Codwyd y rhan fwyaf rhwng tua 1070 a 1220."),
 "motte": ("Motte", "Mwnt",
           "An earth mound that once carried a timber tower. Most were raised between about 1070 and 1220; the timber has gone but the mound remains.",
           "Twmpath pridd a fu unwaith yn cario tŵr pren. Codwyd y rhan fwyaf rhwng tua 1070 a 1220; mae’r pren wedi mynd ond mae’r twmpath yn aros."),
 "ring": ("Ringwork", "Cylchfur",
          "A ring of bank and ditch that enclosed timber buildings: a quicker castle to build than a motte, often from the late 1000s and 1100s.",
          "Cylch o glawdd a ffos o amgylch adeiladau pren: castell cynt i’w godi na mwnt, yn aml o ddiwedd yr 1000au a’r 1100au."),
 "siege": ("Siege castle", "Castell gwarchae",
           "A short-lived earthwork thrown up to besiege a castle nearby.",
           "Gwrthglawdd byrhoedlog a godwyd i warchae ar gastell gerllaw."),
 "tower": ("Tower house", "Tŵr-dŷ",
           "A stone tower house, a lord’s or gentleman’s home built to keep out raiders, mostly from the 1300s to the 1500s.",
           "Tŵr-dŷ carreg, cartref arglwydd neu uchelwr wedi’i godi i gadw ysbeilwyr allan, o’r 1300au i’r 1500au gan amlaf."),
 "house": ("Fortified house", "Tŷ caerog",
           "A manor house with walls, a tower or a moat for defence, the home of a local lord or gentry family.",
           "Maenordy gyda muriau, tŵr neu ffos i’w amddiffyn, cartref arglwydd lleol neu deulu o uchelwyr."),
 "moat": ("Moated site", "Safle â ffos",
          "A house platform ringed by a water-filled ditch, the home of a medieval lord or freeholder.",
          "Llwyfan tŷ wedi’i amgylchynu gan ffos ddŵr, cartref arglwydd neu rydd-ddeiliad yn yr Oesoedd Canol."),
 "mansion": ("Castle-house", "Plasty castellog",
             "A great house built to look like a castle.",
             "Plasty mawr a godwyd i edrych fel castell."),
 "stone": ("Stone castle", "Castell carreg", "", ""),
 "": ("Castle site", "Safle castell",
      "A medieval castle site recorded by the national historic environment record of Wales.",
      "Safle castell canoloesol a gofnodwyd gan gofnod amgylchedd hanesyddol cenedlaethol Cymru."),
}

LA_CY = {"Isle of Anglesey": "Ynys Môn", "Gwynedd": "Gwynedd", "Conwy": "Conwy", "Denbighshire": "Sir Ddinbych", "Flintshire": "Sir y Fflint",
         "Wrexham": "Wrecsam", "Powys": "Powys", "Ceredigion": "Ceredigion", "Pembrokeshire": "Sir Benfro", "Carmarthenshire": "Sir Gaerfyrddin",
         "Swansea": "Abertawe", "Neath Port Talbot": "Castell-nedd Port Talbot", "Bridgend": "Pen-y-bont ar Ogwr", "Vale of Glamorgan": "Bro Morgannwg",
         "Cardiff": "Caerdydd", "Rhondda Cynon Taf": "Rhondda Cynon Taf", "Merthyr Tydfil": "Merthyr Tudful", "Caerphilly": "Caerffili",
         "Blaenau Gwent": "Blaenau Gwent", "Torfaen": "Torfaen", "Monmouthshire": "Sir Fynwy", "Newport": "Casnewydd"}
LA_ORDER = ["Isle of Anglesey", "Gwynedd", "Conwy", "Denbighshire", "Flintshire", "Wrexham", "Powys", "Ceredigion", "Pembrokeshire", "Carmarthenshire",
            "Swansea", "Neath Port Talbot", "Bridgend", "Vale of Glamorgan", "Cardiff", "Rhondda Cynon Taf", "Merthyr Tydfil", "Caerphilly",
            "Blaenau Gwent", "Torfaen", "Monmouthshire", "Newport"]

# Wikidata id -> (group, builder EN, builder CY, date EN, note EN, note CY, [links])
# Dates in Welsh are made from the English ones (c. -> tua).
C = {}


def add(q, g, ben, bcy, d, nen, ncy, links=()):
    C[q] = (g, ben, bcy, d, nen, ncy, list(links))


# ---- built by the Welsh ----
add("Q1048693", "welsh", "Llywelyn ab Iorwerth (Llywelyn Fawr)", "Llywelyn ab Iorwerth (Llywelyn Fawr)", "1221",
    "Built on a rock in the Dysynni valley beneath Cadair Idris to guard the south of Gwynedd. It held out for Dafydd ap Gruffudd until April 1283.",
    "Fe’i codwyd ar graig yn nyffryn Dysynni dan Gadair Idris i warchod de Gwynedd. Daliodd allan dros Ddafydd ap Gruffudd tan Ebrill 1283.",
    ["place-ybere.html", "person-llywelyn-fawr.html"])
add("Q2369922", "welsh", "Llywelyn ab Iorwerth (Llywelyn Fawr)", "Llywelyn ab Iorwerth (Llywelyn Fawr)", "c. 1210–1240",
    "Its square keep guards the old road through Eryri from the Conwy valley. Welsh tradition holds that Llywelyn himself was born close by.",
    "Mae ei orthwr sgwâr yn gwarchod yr hen ffordd drwy Eryri o ddyffryn Conwy. Yn ôl traddodiad Cymru ganed Llywelyn ei hun gerllaw.",
    ["person-llywelyn-fawr.html"])
add("Q13131953", "welsh", "The princes of Gwynedd", "Tywysogion Gwynedd", "12th century",
    "The first castle at Dolwyddelan, a rocky knoll in the valley floor. Welsh tradition holds that Llywelyn ab Iorwerth was born here about 1173.",
    "Castell cyntaf Dolwyddelan, bryncyn creigiog ar lawr y dyffryn. Yn ôl traddodiad Cymru ganed Llywelyn ab Iorwerth yma tua 1173.",
    ["person-llywelyn-fawr.html"])
add("Q2078555", "welsh", "Llywelyn ab Iorwerth (Llywelyn Fawr)", "Llywelyn ab Iorwerth (Llywelyn Fawr)", "c. 1220–1230",
    "Its round tower, built in the Welsh princes’ own style, stands over Llyn Padarn at the foot of the Llanberis Pass. Turner painted it in 1800.",
    "Mae ei dŵr crwn, yn null tywysogion Cymru eu hunain, yn sefyll uwchben Llyn Padarn wrth droed Bwlch Llanberis. Peintiodd Turner ef yn 1800.",
    ["place-dolbadarn.html", "person-llywelyn-fawr.html"])
add("Q1139896", "welsh", "Llywelyn ab Iorwerth, enlarged by Llywelyn ap Gruffudd", "Llywelyn ab Iorwerth, a’i helaethwyd gan Llywelyn ap Gruffudd", "c. 1230–1260s",
    "The twin-towered gatehouse on its headland over Tremadog Bay is the princes’ work. Owain Glyndŵr’s men took the castle in 1404.",
    "Gwaith y tywysogion yw’r porthdy dau dŵr ar y penrhyn uwchben Bae Tremadog. Cipiodd gwŷr Owain Glyndŵr y castell yn 1404.",
    ["person-llywelyn-fawr.html", "person-llywelyn-ap-gruffudd.html"])
add("Q2969121", "welsh", "The princes of Gwynedd; later rebuilt by Henry III", "Tywysogion Gwynedd; fe’i hailgodwyd wedyn gan Harri III", "6th–13th century",
    "Welsh tradition holds that Maelgwn Gwynedd kept his court on these twin hills by the Conwy in the 500s. Llywelyn ap Gruffudd destroyed Henry III’s castle here in 1263.",
    "Yn ôl traddodiad Cymru cadwai Maelgwn Gwynedd ei lys ar y ddau fryn hyn ger afon Conwy yn y 500au. Dinistriodd Llywelyn ap Gruffudd gastell Harri III yma yn 1263.",
    ["person-maelgwn-gwynedd.html", "person-llywelyn-ap-gruffudd.html"])
add("Q354820", "welsh", "The princes of Gwynedd", "Tywysogion Gwynedd", "12th century (stone tower)",
    "The hill where Welsh tradition tells of the red and white dragons found beneath Gwrtheyrn’s tower, and of the boy Emrys who foretold that the red dragon would win.",
    "Y bryn lle mae traddodiad Cymru’n sôn am y ddraig goch a’r ddraig wen dan dŵr Gwrtheyrn, ac am y bachgen Emrys a ragfynegodd mai’r ddraig goch a fyddai’n ennill.",
    ["legend-dragons.html"])
add("Q5043840", "welsh", "The princes of Gwynedd, probably Llywelyn ab Iorwerth", "Tywysogion Gwynedd, Llywelyn ab Iorwerth yn ôl pob tebyg", "early 13th century",
    "A stone castle high on a ridge above Llanuwchllyn, watching the way into Penllyn and Meirionnydd.",
    "Castell carreg yn uchel ar grib uwchben Llanuwchllyn, yn gwylio’r ffordd i mewn i Benllyn a Meirionnydd.")
add("Q20592688", "welsh", "The princes of Gwynedd, probably Llywelyn ab Iorwerth", "Tywysogion Gwynedd, Llywelyn ab Iorwerth yn ôl pob tebyg", "13th century",
    "A Welsh stone tower on a rocky motte near Trawsfynydd, beside the Roman road through the mountains.",
    "Tŵr carreg Cymreig ar fwnt creigiog ger Trawsfynydd, wrth ymyl y ffordd Rufeinig drwy’r mynyddoedd.")
add("Q13126895", "welsh", "Uchdryd ab Edwin, lord of Meirionnydd", "Uchdryd ab Edwin, arglwydd Meirionnydd", "1116",
    "The Welsh chronicle, Brut y Tywysogion, records Uchdryd building this castle in Cymer above the Mawddach.",
    "Mae’r cronicl Cymraeg, Brut y Tywysogion, yn cofnodi Uchdryd yn codi’r castell hwn yng Nghymer uwchben afon Mawddach.")
add("Q13126897", "welsh", "Cadwaladr ap Gruffudd, son of Gruffudd ap Cynan", "Cadwaladr ap Gruffudd, mab Gruffudd ap Cynan", "1147",
    "Brut y Tywysogion records Cadwaladr building a castle at Cynfael in 1147, guarding the coast below Tywyn.",
    "Mae Brut y Tywysogion yn cofnodi Cadwaladr yn codi castell yng Nghynfael yn 1147, i warchod yr arfordir islaw Tywyn.",
    ["person-gruffudd-ap-cynan.html"])
add("Q26722409", "welsh", "The sons of Owain Gwynedd", "Meibion Owain Gwynedd", "by 1188",
    "When Gerallt Gymro passed in 1188 he wrote that the sons of Owain had newly built a stone castle here, high on Garn Fadryn inside an ancient hillfort.",
    "Pan basiodd Gerallt Gymro yn 1188 ysgrifennodd fod meibion Owain newydd godi castell carreg yma, yn uchel ar Garn Fadryn o fewn bryngaer hynafol.",
    ["person-owain-gwynedd.html", "person-gerallt-gymro.html"])
add("Q13126896", "welsh", "The sons of Cynan ab Owain Gwynedd", "Meibion Cynan ab Owain Gwynedd", "by 1188",
    "Gerallt Gymro named a castle of Deudraeth belonging to the sons of Cynan. Today’s Castell Deudraeth is a Victorian house, now part of Portmeirion.",
    "Enwodd Gerallt Gymro gastell yn Neudraeth a berthynai i feibion Cynan. Tŷ Fictoraidd yw Castell Deudraeth heddiw, yn rhan o Bortmeirion.",
    ["person-gerallt-gymro.html"])
add("Q13130661", "welsh", "The princes of Gwynedd", "Tywysogion Gwynedd", "12th–13th century",
    "The motte at Abergwyngregyn, beside the royal court where Llywelyn ab Iorwerth and Siwan lived. Siwan died here in 1237.",
    "Y mwnt yn Abergwyngregyn, wrth ymyl y llys brenhinol lle bu Llywelyn ab Iorwerth a Siwan yn byw. Bu farw Siwan yma yn 1237.",
    ["person-siwan.html", "person-llywelyn-fawr.html"])
add("Q7162120", "welsh", "The princes of Gwynedd (by tradition); the house c. 1600", "Tywysogion Gwynedd (yn ôl traddodiad); y tŷ tua 1600", "13th century",
    "Welsh tradition holds that this house at Abergwyngregyn stands on Garth Celyn, the court of Llywelyn ap Gruffudd.",
    "Yn ôl traddodiad Cymru saif y tŷ hwn yn Abergwyngregyn ar Garth Celyn, llys Llywelyn ap Gruffudd.",
    ["person-llywelyn-ap-gruffudd.html"])
add("Q39006308", "welsh", "The kings and princes of Gwynedd", "Brenhinoedd a thywysogion Gwynedd", "9th–13th century",
    "Aberffraw was the chief court of Gwynedd. Its rulers called themselves Prince of Aberffraw and Lord of Snowdon.",
    "Aberffraw oedd prif lys Gwynedd. Galwai ei rheolwyr eu hunain yn Dywysog Aberffraw ac Arglwydd Eryri.",
    ["place-aberffraw.html"])
add("Q24660280", "welsh", "Ednyfed Fychan, steward of Llywelyn ab Iorwerth (by tradition)", "Ednyfed Fychan, distain Llywelyn ab Iorwerth (yn ôl traddodiad)", "13th century",
    "Welsh tradition places the court of Ednyfed Fychan, Llywelyn Fawr’s chief minister, here on Bryn Euryn. From Ednyfed’s line came the Tudors, and Harri Tudur.",
    "Mae traddodiad Cymru’n gosod llys Ednyfed Fychan, prif weinidog Llywelyn Fawr, yma ar Fryn Euryn. O linach Ednyfed y daeth y Tuduriaid, a Harri Tudur.",
    ["person-harri-tudur.html"])
add("Q5419069", "welsh", "Llywelyn ap Gruffudd", "Llywelyn ap Gruffudd", "from 1257",
    "Hidden in a wooded dell, with a D-shaped Welsh Tower. In Coed Ewloe close by, Owain Gwynedd’s men ambushed the army of Henry II in 1157.",
    "Ynghudd mewn pant coediog, gyda Thŵr Cymreig siâp D. Yng Nghoed Ewloe gerllaw, ymosododd gwŷr Owain Gwynedd ar fyddin Harri II yn 1157.",
    ["person-llywelyn-ap-gruffudd.html", "person-owain-gwynedd.html"])
add("Q3398523", "welsh", "Dafydd ap Gruffudd", "Dafydd ap Gruffudd", "1278–1282",
    "The last castle built by a native prince of Wales. Its round tower looks over the Alun valley towards England.",
    "Y castell olaf a godwyd gan un o dywysogion brodorol Cymru. Mae ei dŵr crwn yn edrych dros ddyffryn Alun tua Lloegr.")
add("Q1226281", "welsh", "Gruffudd ap Madog, prince of Powys Fadog", "Gruffudd ap Madog, tywysog Powys Fadog", "c. 1260",
    "Crowning the hill above Llangollen. Its name, the fortress of Brân, is joined in Welsh tradition to Brân the Blessed.",
    "Ar gopa’r bryn uwchben Llangollen. Mae ei enw, caer Brân, ynghlwm yn nhraddodiad Cymru wrth Fendigeidfran.",
    ["place-llangollen.html", "legend-branwen.html"])
add("Q1235495", "welsh", "Llywelyn ap Gruffudd, Prince of Wales", "Llywelyn ap Gruffudd, Tywysog Cymru", "1273",
    "Built by the Prince of Wales on a ridge above the Severn, with a new Welsh town beside it, in sight of the king’s castle at Montgomery.",
    "Fe’i codwyd gan Dywysog Cymru ar grib uwchben afon Hafren, gyda thref Gymreig newydd wrth ei ymyl, yng ngolwg castell y brenin yn Nhrefaldwyn.",
    ["person-llywelyn-ap-gruffudd.html"])
add("Q1377263", "welsh", "Gruffudd ap Gwenwynwyn, prince of Powys Wenwynwyn", "Gruffudd ap Gwenwynwyn, tywysog Powys Wenwynwyn", "c. 1280s",
    "Castell Coch, the red castle, built by a prince of Powys and lived in ever since: more than 700 years a home, with famous terraced gardens.",
    "Castell Coch, a godwyd gan un o dywysogion Powys ac y bu pobl yn byw ynddo byth ers hynny: yn gartref ers dros 700 mlynedd, gyda gerddi teras enwog.")
add("Q3399905", "welsh", "The kings and princes of Powys", "Brenhinoedd a thywysogion Powys", "9th–13th century",
    "Mathrafal was the chief royal court of Powys. A motte and a great earthwork enclosure mark the site by the Banwy.",
    "Mathrafal oedd prif lys brenhinol Powys. Mae mwnt a chlostir gwrthglawdd mawr yn nodi’r safle ger afon Banwy.",
    ["place-mathrafal.html"])
add("Q7659623", "welsh", "The lords of Glyndyfrdwy; the home of Owain Glyndŵr", "Arglwyddi Glyndyfrdwy; cartref Owain Glyndŵr", "14th century",
    "Iolo Goch’s poem paints Owain’s timber court on this motte: nine halls, a church, a mill, a fishpond, a deer park, and wine always flowing.",
    "Mae cywydd Iolo Goch yn darlunio llys pren Owain ar y mwnt hwn: naw neuadd, eglwys, melin, pysgodlyn, parc ceirw, a gwin yn llifo’n wastad.",
    ["place-sycharth.html", "person-owain-glyndwr.html"])
add("Q13126900", "welsh", "The lords of Glyndyfrdwy", "Arglwyddi Glyndyfrdwy", "12th–14th century",
    "Owain Glyndŵr’s mount in the Dee valley. Here at Glyndyfrdwy, on 16 September 1400, Owain was proclaimed Prince of Wales.",
    "Mwnt Owain Glyndŵr yn nyffryn Dyfrdwy. Yma yng Nglyndyfrdwy, ar 16 Medi 1400, cyhoeddwyd Owain yn Dywysog Cymru.",
    ["person-owain-glyndwr.html"])
add("Q39006486", "welsh", "Owain Glyndŵr", "Owain Glyndŵr", "14th century",
    "The moated platform of Owain Glyndŵr’s house at Glyndyfrdwy, beside his mount.",
    "Llwyfan ffosog tŷ Owain Glyndŵr yng Nglyndyfrdwy, wrth ymyl ei fwnt.",
    ["person-owain-glyndwr.html"])
add("Q13131955", "welsh", "Probably Cadwgan ap Bleddyn, king of Powys", "Cadwgan ap Bleddyn, brenin Powys, yn ôl pob tebyg", "c. 1111",
    "Brut y Tywysogion says Cadwgan was building a castle at Welshpool in 1111. This motte in the town is thought to be it.",
    "Dywed Brut y Tywysogion fod Cadwgan yn codi castell yn y Trallwng yn 1111. Credir mai’r mwnt hwn yn y dref yw hwnnw.")
add("Q13126890", "welsh", "Madog ap Maredudd, king of Powys", "Madog ap Maredudd, brenin Powys", "1156",
    "Brut y Tywysogion records Madog building a castle in Caereinion in 1156.",
    "Mae Brut y Tywysogion yn cofnodi Madog yn codi castell yng Nghaereinion yn 1156.")
add("Q20600781", "welsh", "Owain Gwynedd", "Owain Gwynedd", "1149",
    "Owain Gwynedd raised this motte after he won Iâl from Powys, at the head of the pass between the Clwyd and the Dee.",
    "Cododd Owain Gwynedd y mwnt hwn wedi iddo ennill Iâl oddi ar Bowys, ar ben y bwlch rhwng Clwyd a Dyfrdwy.",
    ["person-owain-gwynedd.html"])
add("Q13126920", "welsh", "Yr Arglwydd Rhys (the Lord Rhys)", "Yr Arglwydd Rhys", "1177",
    "Brut y Tywysogion records the Lord Rhys building the castle of Rhaeadr Gwy in 1177, on a rock above the Wye.",
    "Mae Brut y Tywysogion yn cofnodi’r Arglwydd Rhys yn codi castell Rhaeadr Gwy yn 1177, ar graig uwchben afon Gwy.",
    ["person-yr-arglwydd-rhys.html"])
add("Q4667053", "welsh", "Yr Arglwydd Rhys (the Lord Rhys)", "Yr Arglwydd Rhys", "1156",
    "Raised by the Lord Rhys in 1156 to hold the Dyfi against Owain Gwynedd. Llywelyn Fawr later held a council of the princes at Aberdyfi in 1216.",
    "Fe’i codwyd gan yr Arglwydd Rhys yn 1156 i ddal afon Dyfi yn erbyn Owain Gwynedd. Yn ddiweddarach cynhaliodd Llywelyn Fawr gyngor o’r tywysogion yn Aberdyfi yn 1216.",
    ["person-yr-arglwydd-rhys.html", "person-llywelyn-fawr.html"])
add("Q2713117", "welsh", "Yr Arglwydd Rhys and the princes of Deheubarth", "Yr Arglwydd Rhys a thywysogion Deheubarth", "late 12th–13th century",
    "Welsh tradition holds that Dinefwr was the royal seat of Deheubarth, one of the three chief courts named in the Laws of Hywel Dda.",
    "Yn ôl traddodiad Cymru, Dinefwr oedd prif lys Deheubarth, un o’r tri phrif lys a enwir yng Nghyfraith Hywel Dda.",
    ["place-dinefwr.html", "person-yr-arglwydd-rhys.html", "story-hywel.html"])
add("Q3401324", "welsh", "The princes of Deheubarth, probably Rhys Gryg", "Tywysogion Deheubarth, Rhys Gryg yn ôl pob tebyg", "1220s",
    "On a lone hill above the Tywi, one of the great stone castles of the Welsh princes of the south.",
    "Ar fryn unig uwchben afon Tywi, un o gestyll carreg mawr tywysogion Cymru yn y de.")
add("Q4516540", "welsh", "Maredudd ap Rhys Gryg", "Maredudd ap Rhys Gryg", "c. 1240",
    "One of the few stone castles built by a Welsh lord in the south-west, in a loop of the Teifi. Owain Glyndŵr’s men held it in 1403.",
    "Un o’r ychydig gestyll carreg a godwyd gan arglwydd o Gymro yn y de-orllewin, mewn dolen o afon Teifi. Daliwyd ef gan wŷr Owain Glyndŵr yn 1403.")
add("Q3403691", "welsh", "The princes of Deheubarth; rebuilt in stone after 1283", "Tywysogion Deheubarth; fe’i hailgodwyd mewn carreg wedi 1283", "13th century",
    "On a crag ninety metres above the Cennen, with a passage cut down into a cave. Local tradition holds that the first castle was built by Urien, a knight of Arthur’s court.",
    "Ar graig naw deg metr uwchben afon Cennen, gyda thramwyfa wedi’i thorri i lawr i ogof. Yn ôl traddodiad lleol codwyd y castell cyntaf gan Urien, un o farchogion llys Arthur.",
    ["story-arthur.html"])
add("Q3395294", "welsh", "Yr Arglwydd Rhys rebuilt it in stone", "Yr Arglwydd Rhys a’i hailgododd mewn carreg", "1171",
    "At Christmas 1176 the Lord Rhys held the first recorded eisteddfod here, with a chair for the best poet and another for the best musician.",
    "Adeg Nadolig 1176 cynhaliodd yr Arglwydd Rhys yr eisteddfod gyntaf a gofnodwyd yma, gyda chadair i’r bardd gorau ac un arall i’r cerddor gorau.",
    ["place-cardigan.html", "person-yr-arglwydd-rhys.html"])
add("Q5049668", "welsh", "Seisyll ap Dyfnwal, lord of Gwent Uwch Coed", "Seisyll ap Dyfnwal, arglwydd Gwent Uwch Coed", "12th century",
    "The moated court of Seisyll ap Dyfnwal near Llanofer. Seisyll and his followers were murdered by William de Braose at Abergavenny at Christmas 1175, and Gwent remembered them.",
    "Llys ffosog Seisyll ap Dyfnwal ger Llanofer. Llofruddiwyd Seisyll a’i ddilynwyr gan William de Braose yn y Fenni adeg Nadolig 1175, a chofiodd Gwent amdanynt.")
add("Q38601344", "welsh", "Edwin, lord of Tegeingl (by tradition)", "Edwin, arglwydd Tegeingl (yn ôl traddodiad)", "11th century",
    "Llys Edwin near Northop: Welsh tradition places the hall of Edwin, lord of Tegeingl, on this site.",
    "Llys Edwin ger Llaneurgain: mae traddodiad Cymru’n gosod neuadd Edwin, arglwydd Tegeingl, ar y safle hwn.")
add("Q13126908", "welsh", "The Welsh lords of Gwynllŵg", "Arglwyddi Cymreig Gwynllŵg", "13th century",
    "Castell Meredydd, a stone castle on a rocky ridge above Machen, held by the Welsh lords of Gwynllŵg.",
    "Castell Meredydd, castell carreg ar grib greigiog uwchben Machen, a ddaliwyd gan arglwyddi Cymreig Gwynllŵg.")
add("Q9704504", "welsh", "Builder debated: perhaps the Welsh lords of Senghenydd, perhaps Gilbert de Clare", "Dadleuir pwy a’i cododd: arglwyddi Cymreig Senghenydd efallai, neu Gilbert de Clare", "1260s",
    "An unfinished stone castle on the ridge north of Cardiff, with D-shaped towers in the Welsh style.",
    "Castell carreg anorffenedig ar y grib i’r gogledd o Gaerdydd, gyda thyrau siâp D yn null Cymru.")
add("Q3398574", "welsh", "Maredudd ab Ieuan ap Robert", "Maredudd ab Ieuan ap Robert", "c. 1500",
    "The home of the Wynns of Gwydir, Welsh gentry and patrons of the poets. Sir John Wynn wrote the History of the Gwydir Family here.",
    "Cartref Wyniaid Gwydir, uchelwyr Cymreig a noddwyr y beirdd. Ysgrifennodd Syr John Wynn Hanes Teulu Gwydir yma.")
add("Q2630723", "welsh", "Sir William ap Thomas and his son William Herbert, Earl of Pembroke", "Syr William ap Thomas a’i fab William Herbert, Iarll Penfro", "from 1435",
    "A palace-castle raised by Welsh lords. William ap Thomas was the Blue Knight of Gwent; his son was the first Welshman made an earl, and young Harri Tudur grew up here.",
    "Castell-palas a godwyd gan arglwyddi o Gymry. William ap Thomas oedd y Marchog Glas o Went; ei fab oedd y Cymro cyntaf i’w wneud yn iarll, a magwyd Harri Tudur ifanc yma.",
    ["place-rhaglan.html", "person-harri-tudur.html"])
add("Q7838880", "welsh", "Sir Roger Vaughan", "Syr Roger Vaughan", "15th century",
    "A Welsh gentleman’s courtyard house beside the older castle. The Vaughans of Tretower were patrons of the Welsh poets.",
    "Tŷ cwrt bonheddwr o Gymro wrth ymyl yr hen gastell. Roedd Fychaniaid Tretŵr yn noddwyr i feirdd Cymru.")

# ---- built by the English Crown ----
add("Q756830", "crown", "Edward I, with Master James of St George", "Edward I, gyda Meistr James o St George", "1283–1287",
    "Built in four years with the town walls around it. On Good Friday 1401 the brothers Rhys and Gwilym ap Tudur, cousins of Owain Glyndŵr, took it while the garrison was at church.",
    "Fe’i codwyd mewn pedair blynedd gyda muriau’r dref o’i gwmpas. Ar Ddydd Gwener y Groglith 1401 cipiwyd ef gan y brodyr Rhys a Gwilym ap Tudur, cefndryd Owain Glyndŵr, tra oedd y gwarchodlu yn yr eglwys.",
    ["place-conwy.html", "person-owain-glyndwr.html"])
add("Q275128", "crown", "Edward I, with Master James of St George", "Edward I, gyda Meistr James o St George", "from 1283",
    "Its banded towers echo the walls of Constantinople, beside Segontium, the Roman fort that Welsh tradition linked with Macsen Wledig.",
    "Mae ei dyrau rhesog yn adleisio muriau Caergystennin, wrth ymyl Segontium, y gaer Rufeinig a gysylltai traddodiad Cymru â Macsen Wledig.",
    ["place-caernarfon.html", "place-segontium.html"])
add("Q540964", "crown", "Edward I, with Master James of St George", "Edward I, gyda Meistr James o St George", "1283–1289",
    "Owain Glyndŵr took Harlech in 1404 and made it his home and court. In the Wars of the Roses its garrison held out for seven years, the siege remembered in ‘Men of Harlech’.",
    "Cipiodd Owain Glyndŵr Harlech yn 1404 a’i wneud yn gartref ac yn llys iddo. Yn Rhyfeloedd y Rhosynnau daliodd y gwarchodlu allan am saith mlynedd, gwarchae a gofir yn ‘Rhyfelgyrch Gwŷr Harlech’.",
    ["place-harlech.html", "person-owain-glyndwr.html"])
add("Q756815", "crown", "Edward I, with Master James of St George", "Edward I, gyda Meistr James o St George", "from 1295",
    "Never finished, and the most perfectly planned castle in Britain: walls within walls, built on a marsh by the Menai Strait.",
    "Ni chafodd erioed ei orffen, a dyma’r castell â’r cynllun mwyaf perffaith ym Mhrydain: muriau o fewn muriau, wedi’u codi ar gors ger y Fenai.",
    ["place-beaumaris.html"])
add("Q1585938", "crown", "Edward I", "Edward I", "1277–1282",
    "The river Clwyd was straightened to bring ships to its walls. The Statute of Rhuddlan of 1284 was sealed here.",
    "Sythwyd afon Clwyd i ddod â llongau at ei muriau. Seliwyd Statud Rhuddlan 1284 yma.",
    ["place-rhuddlan.html"])
add("Q1428846", "crown", "Edward I", "Edward I", "from 1277",
    "The first of Edward’s castles in Wales, a day’s march from Chester, with a great tower standing apart from the rest.",
    "Y cyntaf o gestyll Edward yng Nghymru, daith diwrnod o Gaer, gyda thŵr mawr yn sefyll ar wahân i’r gweddill.")
add("Q319745", "crown", "Edward I", "Edward I", "from 1277",
    "Owain Glyndŵr took it in 1404 and held it until 1408. In the Civil War it housed a royal mint for Welsh silver.",
    "Cipiodd Owain Glyndŵr ef yn 1404 a’i ddal tan 1408. Yn y Rhyfel Cartref roedd bathdy brenhinol yma ar gyfer arian Cymru.",
    ["person-owain-glyndwr.html"])
add("Q4986692", "crown", "Edward I, on an earlier Norman motte", "Edward I, ar fwnt Normanaidd cynharach", "1277",
    "Only the great earthworks remain. Llywelyn ap Gruffudd fell at Cilmeri, three miles away, on 11 December 1282.",
    "Dim ond y gwrthgloddiau mawr sy’n aros. Syrthiodd Llywelyn ap Gruffudd yng Nghilmeri, dair milltir i ffwrdd, ar 11 Rhagfyr 1282.",
    ["place-cilmeri.html", "person-llywelyn-ap-gruffudd.html"])
add("Q3400816", "crown", "Henry III", "Harri III", "from 1223",
    "In the Treaty of Montgomery, 1267, Henry III recognised Llywelyn ap Gruffudd as Prince of Wales; Llywelyn did homage at the ford of Rhyd Chwima below.",
    "Yng Nghytundeb Trefaldwyn, 1267, cydnabu Harri III Lywelyn ap Gruffudd yn Dywysog Cymru; talodd Llywelyn wrogaeth wrth ryd Rhyd Chwima islaw.",
    ["person-llywelyn-ap-gruffudd.html"])
add("Q18019468", "crown", "Henry III", "Harri III", "1241",
    "Built on a limestone crag to hold Tegeingl. Llywelyn ap Gruffudd took it and pulled it down in 1263.",
    "Fe’i codwyd ar graig galchfaen i ddal Tegeingl. Cipiodd Llywelyn ap Gruffudd ef a’i dynnu i lawr yn 1263.",
    ["person-llywelyn-ap-gruffudd.html"])
add("Q14906524", "crown", "Henry I and the English kings", "Harri I a brenhinoedd Lloegr", "c. 1106",
    "Llywelyn ab Iorwerth took Carmarthen in 1215, and Owain Glyndŵr in 1403.",
    "Cipiodd Llywelyn ab Iorwerth Gaerfyrddin yn 1215, ac Owain Glyndŵr yn 1403.",
    ["person-llywelyn-fawr.html", "person-owain-glyndwr.html"])
add("Q1985853", "crown", "Rebuilt for the Lord Edward, later Edward I", "Fe’i hailgodwyd i’r Arglwydd Edward, Edward I yn ddiweddarach", "1260s",
    "One of the Three Castles of Gwent, strengthened in the 1260s against Llywelyn ap Gruffudd. Its moat is still full of water.",
    "Un o Dri Chastell Gwent, a gryfhawyd yn y 1260au yn erbyn Llywelyn ap Gruffudd. Mae ei ffos yn llawn dŵr o hyd.")
add("Q12071213", "crown", "Probably William Rufus, inside a Roman fort", "Gwilym Goch yn ôl pob tebyg, o fewn caer Rufeinig", "1095",
    "In the Fourth Branch of the Mabinogi, Mur Castell here is the court of Lleu Llaw Gyffes, where Blodeuwedd lived.",
    "Ym Mhedwaredd Gainc y Mabinogi, Mur Castell yma yw llys Lleu Llaw Gyffes, lle bu Blodeuwedd yn byw.",
    ["legend-blodeuwedd.html"])

# ---- built by Norman and Marcher lords ----
add("Q682601", "norman", "Gilbert de Clare, lord of Glamorgan", "Gilbert de Clare, arglwydd Morgannwg", "1268–1271",
    "The largest castle in Wales, ringed by lakes, built to hold back Llywelyn ap Gruffudd, who attacked the works in 1270. Its south-east tower leans further than Pisa’s.",
    "Castell mwyaf Cymru, wedi’i amgylchynu gan lynnoedd, a godwyd i atal Llywelyn ap Gruffudd, a ymosododd ar y gwaith yn 1270. Mae ei dŵr de-ddwyreiniol yn gwyro’n fwy na thŵr Pisa.",
    ["place-caerffili.html", "person-llywelyn-ap-gruffudd.html"])
add("Q1035742", "norman", "Robert Fitzhamon, inside a Roman fort", "Robert Fitzhamon, o fewn caer Rufeinig", "c. 1081",
    "In 1158 Ifor Bach, Welsh lord of Senghenydd, climbed its walls by night and carried off the Earl of Gloucester and his family until his rights were restored.",
    "Yn 1158 dringodd Ifor Bach, arglwydd Cymreig Senghenydd, ei furiau liw nos a chipio Iarll Caerloyw a’i deulu nes i’w hawliau gael eu hadfer.")
add("Q1070187", "norman", "William FitzOsbern", "William FitzOsbern", "1067",
    "Begun within a year of the Norman conquest of England, on a cliff over the Wye. It is the oldest surviving stone castle in Britain.",
    "Fe’i dechreuwyd o fewn blwyddyn i goncwest Normanaidd Lloegr, ar glogwyn uwchben afon Gwy. Dyma’r castell carreg hynaf sy’n sefyll ym Mhrydain.",
    ["place-chepstow.html"])
add("Q525635", "norman", "William FitzOsbern", "William FitzOsbern", "c. 1067",
    "Henry V was born here in 1386. Geoffrey of Monmouth, who gave the world the story of Arthur, took his name from this town.",
    "Ganed Harri V yma yn 1386. Cymerodd Sieffre o Fynwy, a roddodd stori Arthur i’r byd, ei enw o’r dref hon.",
    ["story-arthur.html"])
add("Q1422235", "norman", "Arnulf de Montgomery; the great keep by William Marshal", "Arnulf de Montgomery; y gorthwr mawr gan William Marshal", "1093; keep c. 1200",
    "Harri Tudur was born here in 1457, the Welshman who became King Henry VII.",
    "Ganed Harri Tudur yma yn 1457, y Cymro a ddaeth yn Frenin Harri VII.",
    ["place-penfro.html", "person-harri-tudur.html"])
add("Q1508342", "norman", "The de Barri family", "Teulu de Barri", "12th century",
    "Birthplace of Gerallt Gymro, Gerald of Wales, about 1146. He called Manorbier the pleasantest spot in Wales.",
    "Man geni Gerallt Gymro tua 1146. Galwodd Faenorbŷr y llecyn hyfrytaf yng Nghymru.",
    ["person-gerallt-gymro.html"])
add("Q752721", "norman", "Gerald of Windsor; rebuilt by the Carews", "Gerallt o Windsor; fe’i hailgodwyd gan deulu Carew", "c. 1100; 1280s",
    "Home of the princess Nest, daughter of Rhys ap Tewdwr. In 1507 Sir Rhys ap Thomas, who helped Harri Tudur to the throne, held a great tournament here.",
    "Cartref y dywysoges Nest, merch Rhys ap Tewdwr. Yn 1507 cynhaliodd Syr Rhys ap Thomas, a helpodd Harri Tudur i’r orsedd, dwrnamaint mawr yma.",
    ["person-nest.html", "person-harri-tudur.html"])
add("Q1774870", "norman", "Gerald of Windsor; rebuilt by William Marshal the younger", "Gerallt o Windsor; fe’i hailgodwyd gan William Marshal yr ieuengaf", "c. 1110; 1223",
    "High over the Teifi gorge. The Lord Rhys took it in 1164, and Turner painted its towers.",
    "Yn uchel uwchben ceunant afon Teifi. Cipiodd yr Arglwydd Rhys ef yn 1164, a pheintiodd Turner ei dyrau.",
    ["person-yr-arglwydd-rhys.html"])
add("Q1585849", "norman", "Roger, Bishop of Salisbury", "Roger, Esgob Caersallog", "1106",
    "In 1136 the princess Gwenllian led a Welsh army against Kidwelly and fell in battle near by, at Maes Gwenllian.",
    "Yn 1136 arweiniodd y dywysoges Gwenllian fyddin Gymreig yn erbyn Cydweli a syrthio mewn brwydr gerllaw, ym Maes Gwenllian.",
    ["person-gwenllian.html"])
add("Q911714", "norman", "Norman lords; made a Tudor mansion by Sir John Perrot", "Arglwyddi Normanaidd; fe’i gwnaed yn blasty Tuduraidd gan Syr John Perrot", "12th century; 1580s",
    "The Lord Rhys met Henry II here in 1172 and was made justice of all south Wales.",
    "Cyfarfu’r Arglwydd Rhys â Harri II yma yn 1172 a’i wneud yn ustus ar holl dde Cymru.",
    ["place-talacharn.html", "person-yr-arglwydd-rhys.html"])
add("Q1936320", "norman", "Norman lords, inside an Iron Age fort", "Arglwyddi Normanaidd, o fewn caer o’r Oes Haearn", "early 12th century",
    "On a headland at the mouth of the Tywi. The Welsh princes Maredudd and Rhys ap Gruffudd took it in 1146.",
    "Ar bentir wrth aber afon Tywi. Cipiodd y tywysogion Maredudd a Rhys ap Gruffudd ef yn 1146.",
    ["person-yr-arglwydd-rhys.html"])
add("Q1493071", "norman", "Richard fitz Pons", "Richard fitz Pons", "c. 1116",
    "Below the castle stands a statue of Llywelyn ap Gruffudd Fychan, put to death here in 1401 because he would not betray Owain Glyndŵr.",
    "O dan y castell saif cerflun o Llywelyn ap Gruffudd Fychan, a ddienyddiwyd yma yn 1401 am na fynnai fradychu Owain Glyndŵr.",
    ["person-owain-glyndwr.html"])
add("Q1107288", "norman", "Payn de Turberville", "Payn de Turberville", "early 12th century",
    "Owain Glyndŵr’s men laid siege to it in 1404 and 1405.",
    "Bu gwŷr Owain Glyndŵr yn gwarchae arno yn 1404 a 1405.")
add("Q1789059", "norman", "William de Londres", "William de Londres", "c. 1106",
    "Reached by stepping stones over the Ewenni river.",
    "Cyrhaeddir ef ar gerrig sarn dros afon Ewenni.")
add("Q2614463", "norman", "Robert, Earl of Gloucester", "Robert, Iarll Caerloyw", "c. 1140",
    "The castle and its town were slowly buried by the sand dunes.",
    "Claddwyd y castell a’i dref yn araf gan y twyni tywod.")
add("Q7653666", "norman", "Henry de Beaumont; the new castle by Bishop Henry de Gower", "Henry de Beaumont; y castell newydd gan yr Esgob Henry de Gower", "1107; 14th century",
    "Its arcaded parapet is the mark of Bishop Gower, who built the same at St Davids.",
    "Mae ei barapet bwaog yn nod yr Esgob Gower, a gododd yr un peth yn Nhyddewi.",
    ["place-stdavids.html"])
add("Q6686227", "norman", "Henry de Beaumont, inside a Roman fort", "Henry de Beaumont, o fewn caer Rufeinig", "c. 1106",
    "Welsh forces took it in 1151, and again in 1215.",
    "Cipiwyd ef gan luoedd Cymru yn 1151, ac eto yn 1215.")
add("Q7116379", "norman", "The lords of Gower (de Londres, then de Braose)", "Arglwyddi Gŵyr (de Londres, yna de Braose)", "12th–14th century",
    "Above Swansea Bay at Mumbles.", "Uwchben Bae Abertawe yn y Mwmbwls.")
add("Q2275648", "norman", "Hugh d’Avranches, Earl of Chester", "Hugh d’Avranches, Iarll Caer", "c. 1088",
    "Gruffudd ap Cynan’s men besieged it and took it in 1094, and Anglesey was Welsh again.",
    "Bu gwŷr Gruffudd ap Cynan yn gwarchae arno a’i gipio yn 1094, ac roedd Môn yn Gymreig eto.",
    ["person-gruffudd-ap-cynan.html"])
add("Q7859519", "norman", "Robert of Rhuddlan", "Robert o Ruddlan", "1073",
    "Before the Normans came, Gruffudd ap Llywelyn, king of all Wales, had his court at Rhuddlan.",
    "Cyn i’r Normaniaid ddod, roedd gan Gruffudd ap Llywelyn, brenin Cymru gyfan, ei lys yn Rhuddlan.",
    ["person-gruffudd-ap-llywelyn.html"])
add("Q1186885", "norman", "Henry de Lacy, Earl of Lincoln", "Henry de Lacy, Iarll Lincoln", "from 1282",
    "Built over the court of Dafydd ap Gruffudd, with a triple-towered gatehouse.",
    "Fe’i codwyd dros lys Dafydd ap Gruffudd, gyda phorthdy tri thŵr.")
add("Q3403676", "norman", "Begun by Dafydd ap Gruffudd; finished by Reginald de Grey", "Dechreuwyd gan Ddafydd ap Gruffudd; fe’i gorffennwyd gan Reginald de Grey", "from 1277",
    "Owain Glyndŵr’s rising began with an attack on Ruthin in September 1400.",
    "Dechreuodd gwrthryfel Owain Glyndŵr gydag ymosodiad ar Ruthun ym Medi 1400.",
    ["person-owain-glyndwr.html"])
add("Q5884534", "norman", "John de Warenne, Earl of Surrey", "John de Warenne, Iarll Surrey", "after 1282",
    "A five-sided castle on a sandstone rock by the Dee; its stone was later carried off to build Eaton Hall.",
    "Castell pum ochr ar graig dywodfaen ger afon Dyfrdwy; cariwyd ei gerrig yn ddiweddarach i godi Eaton Hall.")
add("Q3306356", "norman", "Roger Mortimer of Chirk", "Roger Mortimer o’r Waun", "1295",
    "Still lived in after more than 700 years, with famous gates of wrought iron.",
    "Mae pobl yn byw ynddo o hyd ar ôl dros 700 mlynedd, gyda gatiau haearn gyr enwog.")
add("Q3404121", "norman", "The Normans; rebuilt by Roger de Clifford", "Y Normaniaid; fe’i hailgodwyd gan Roger de Clifford", "after 1282",
    "Dafydd ap Gruffudd’s attack here on Palm Sunday 1282 opened the last war for Welsh independence under the princes.",
    "Ymosodiad Dafydd ap Gruffudd yma ar Sul y Blodau 1282 a agorodd y rhyfel olaf dros annibyniaeth Cymru dan y tywysogion.")
add("Q6895734", "norman", "Robert de Montalt", "Robert de Montalt", "c. 1140",
    "Owain Gwynedd took it in 1146, and Llywelyn ab Iorwerth in 1199.",
    "Cipiodd Owain Gwynedd ef yn 1146, a Llywelyn ab Iorwerth yn 1199.",
    ["person-owain-gwynedd.html", "person-llywelyn-fawr.html", "place-mold.html"])
add("Q13126913", "norman", "Robert fitz Martin; strengthened by the Lord Rhys", "Robert fitz Martin; fe’i cryfhawyd gan yr Arglwydd Rhys", "c. 1108; 1190s",
    "The Lord Rhys took it in 1191 and gave it towers of stone.",
    "Cipiodd yr Arglwydd Rhys ef yn 1191 a rhoi tyrau carreg iddo.",
    ["person-yr-arglwydd-rhys.html"])
add("Q15262178", "norman", "William FitzMartin", "William FitzMartin", "c. 1191",
    "Built after the Lord Rhys took Nevern; the gatehouse is now part of a house.",
    "Fe’i codwyd wedi i’r Arglwydd Rhys gipio Nanhyfer; mae’r porthdy bellach yn rhan o dŷ.")
add("Q8027762", "norman", "Wizo the Fleming", "Wizo’r Ffleming", "c. 1110",
    "Llywelyn ab Iorwerth took it in 1220.", "Cipiodd Llywelyn ab Iorwerth ef yn 1220.",
    ["person-llywelyn-fawr.html"])
add("Q5683760", "norman", "Norman and Flemish lords", "Arglwyddi Normanaidd a Ffleminaidd", "c. 1120",
    "Llywelyn ab Iorwerth burned the town in 1220, but the castle on its rock held.",
    "Llosgodd Llywelyn ab Iorwerth y dref yn 1220, ond daliodd y castell ar ei graig.")
add("Q6965584", "norman", "Norman lords of Narberth", "Arglwyddi Normanaidd Arberth", "13th century",
    "Arberth was the chief court of Pwyll, Prince of Dyfed, in the First Branch of the Mabinogi.",
    "Arberth oedd prif lys Pwyll, Pendefig Dyfed, ym Mhedair Cainc y Mabinogi, yn y Gainc Gyntaf.")
add("Q7699534", "norman", "Norman lords of Pembroke", "Arglwyddi Normanaidd Penfro", "13th century",
    "In 1471 Jasper Tudor and the young Harri Tudur escaped from Tenby by sea to Brittany.",
    "Yn 1471 dihangodd Siasbar Tudur a Harri Tudur ifanc o Ddinbych-y-pysgod ar y môr i Lydaw.",
    ["person-harri-tudur.html"])
add("Q7191106", "norman", "Sir John Wogan", "Syr John Wogan", "c. 1300",
    "Still a family home, lived in by the same family for centuries.", "Mae’n gartref teuluol o hyd, gyda’r un teulu’n byw ynddo ers canrifoedd.")
add("Q2637887", "norman", "The bishops of St Davids", "Esgobion Tyddewi", "12th–14th century",
    "A fortified palace of the bishops of St Davids.", "Palas caerog esgobion Tyddewi.", ["place-stdavids.html"])
add("Q7353760", "norman", "Adam de Rupe", "Adam de Rupe", "13th century",
    "A tower on a volcanic rock, seen for miles across St Brides Bay.", "Tŵr ar graig folcanig, i’w weld am filltiroedd ar draws Bae Sain Ffraid.")
add("Q2968744", "norman", "The de Bohun family; restored in the 1800s", "Teulu de Bohun; fe’i hadferwyd yn y 1800au", "13th–14th century",
    "", "")
add("Q3402778", "norman", "Hubert de Burgh", "Hubert de Burgh", "1220s",
    "One of the Three Castles of Gwent.", "Un o Dri Chastell Gwent.")
add("Q7534629", "norman", "Hubert de Burgh", "Hubert de Burgh", "1220s",
    "One of the Three Castles of Gwent, by the Monnow, with a round keep.", "Un o Dri Chastell Gwent, ger afon Mynwy, gyda gorthwr crwn.")
add("Q4667087", "norman", "Hamelin de Ballon", "Hamelin de Ballon", "c. 1087", "", "")
add("Q7902005", "norman", "The de Clare lords of Usk", "Arglwyddi de Clare Brynbuga", "12th–14th century", "", "")
add("Q13127487", "norman", "The de Clare lords", "Arglwyddi de Clare", "14th century", "", "")
add("Q7018806", "norman", "Hugh Audley, lord of Gwynllŵg", "Hugh Audley, arglwydd Gwynllŵg", "14th century",
    "Its water gate opened straight onto the tidal Usk.", "Agorai ei borth dŵr yn syth ar afon Wysg a’i llanw.")
add("Q15790795", "norman", "The Normans; held by the Welsh lords of Caerleon", "Y Normaniaid; fe’i daliwyd gan arglwyddi Cymreig Caerllion", "1080s",
    "Morgan ab Owain and Hywel ab Iorwerth, Welsh lords of Caerleon, held it in the 1100s, in the town of the Roman legion.",
    "Daliodd Morgan ab Owain a Hywel ab Iorwerth, arglwyddi Cymreig Caerllion, ef yn yr 1100au, yn nhref y lleng Rufeinig.",
    ["place-caerleon.html"])
add("Q15107961", "norman", "Bernard de Neufmarché", "Bernard de Neufmarché", "1093", "", "")
add("Q17743079", "norman", "Norman lords of Bronllys", "Arglwyddi Normanaidd Bronllys", "12th–13th century",
    "A round tower on its motte.", "Tŵr crwn ar ei fwnt.")
add("Q7838881", "norman", "The Picard family", "Teulu Picard", "12th–13th century",
    "A round tower inside an older shell keep.", "Tŵr crwn o fewn gorthwr cragen hŷn.")
add("Q17743117", "norman", "The Pauncefote family", "Teulu Pauncefote", "13th century", "", "")
add("Q15114193", "norman", "William de Braose; a Jacobean house added", "William de Braose; ychwanegwyd tŷ Iagobeaidd", "c. 1200",
    "Now at the heart of Hay, the town of books.", "Yng nghanol y Gelli Gandryll, tref y llyfrau, bellach.")
add("Q24659303", "norman", "Payn fitz John", "Payn fitz John", "c. 1130", "", "")
add("Q5057282", "norman", "Roger Mortimer", "Roger Mortimer", "1240s",
    "Llywelyn ap Gruffudd took it in 1262.", "Cipiodd Llywelyn ap Gruffudd ef yn 1262.", ["person-llywelyn-ap-gruffudd.html"])
add("Q5712905", "norman", "Roger de Montgomery", "Roger de Montgomery", "c. 1070",
    "The timber castle that came before Montgomery, one of the most studied mottes in Britain.", "Y castell pren a ddaeth cyn Trefaldwyn, un o’r mwntiau a astudiwyd fwyaf ym Mhrydain.")
add("Q24661848", "norman", "The de Braose lords", "Arglwyddi de Braose", "12th century",
    "Owain Glyndŵr took it in 1401.", "Cipiodd Owain Glyndŵr ef yn 1401.", ["person-owain-glyndwr.html"])
add("Q4667054", "norman", "Walter Hakelutel", "Walter Hakelutel", "1280s",
    "Welsh tradition holds that Llywelyn ap Gruffudd sheltered in a cave near Aberedw on the eve of his death in December 1282.",
    "Yn ôl traddodiad Cymru cysgododd Llywelyn ap Gruffudd mewn ogof ger Aberedw y noson cyn ei farw yn Rhagfyr 1282.",
    ["person-llywelyn-ap-gruffudd.html", "place-cilmeri.html"])
add("Q7808013", "norman", "The Mortimers", "Teulu Mortimer", "13th century", "", "")
add("Q6912480", "norman", "Gilbert de Clare", "Gilbert de Clare", "1288",
    "Built high on a hillfort above Merthyr, on land claimed by two lords.", "Fe’i codwyd yn uchel ar fryngaer uwchben Merthyr, ar dir a hawliwyd gan ddau arglwydd.")
add("Q21037221", "norman", "The de Clare lords of Glamorgan", "Arglwyddi de Clare Morgannwg", "13th century", "", "")
add("Q6984490", "norman", "Richard de Granville", "Richard de Granville", "12th century", "", "")
add("Q5049671", "norman", "Norman lords, inside an Iron Age hillfort", "Arglwyddi Normanaidd, o fewn bryngaer o’r Oes Haearn", "12th century",
    "At about 450 metres, one of the highest castle sites in Wales.", "Ar tua 450 metr, un o’r safleoedd castell uchaf yng Nghymru.")
add("Q5049674", "norman", "Walter de Bec", "Walter de Bec", "c. 1110", "", "")
add("Q7241757", "norman", "Robert de Banastre", "Robert de Banastre", "1160s",
    "Owain Gwynedd destroyed it in 1167.", "Dinistriodd Owain Gwynedd ef yn 1167.", ["person-owain-gwynedd.html"])
add("Q2614444", "norman", "Norman lords of Glamorgan", "Arglwyddi Normanaidd Morgannwg", "12th century",
    "Its carved Norman doorway is one of the finest in Wales.", "Mae ei ddrws Normanaidd cerfiedig ymhlith y gorau yng Nghymru.")

# ---- tower houses and later castles ----
add("Q2704850", "later", "William Burges for the Marquess of Bute, on medieval ruins", "William Burges i Ardalydd Bute, ar adfeilion canoloesol", "1875–1891",
    "A fairytale castle in the beech woods above Taff’s Well.", "Castell tylwyth teg yn y coed ffawydd uwchben Ffynnon Taf.")
add("Q3402621", "later", "Thomas Hopper for George Hay Dawkins-Pennant", "Thomas Hopper i George Hay Dawkins-Pennant", "1820–1837",
    "A neo-Norman castle built on the wealth of the Penrhyn slate quarry. Inside is a bed carved from slate.",
    "Castell neo-Normanaidd a godwyd ar gyfoeth chwarel lechi’r Penrhyn. Y tu mewn mae gwely wedi’i gerfio o lechen.",
    ["place-dinorwig.html"])
add("Q3395336", "later", "Lloyd Hesketh Bamford-Hesketh", "Lloyd Hesketh Bamford-Hesketh", "1810s", "", "")
add("Q2968597", "later", "The Williams and Hughes families", "Teuluoedd Williams a Hughes", "rebuilt 1830s", "", "")
add("Q4980841", "later", "Built as a castle-style house", "Fe’i codwyd fel plasty ar ddull castell", "1830s", "", "")
add("Q12061481", "later", "Christopher Rice Mansel Talbot", "Christopher Rice Mansel Talbot", "1830s", "", "")
add("Q2970467", "later", "Sir Thomas Morgan", "Syr Thomas Morgan", "1626",
    "One of the last houses in Wales built as a castle.", "Un o’r tai olaf yng Nghymru a godwyd fel castell.")
add("Q1485119", "later", "The Stradling family", "Teulu Stradling", "13th–16th century",
    "Later owned by William Randolph Hearst; now Atlantic College.", "Yn eiddo i William Randolph Hearst yn ddiweddarach; Coleg yr Iwerydd bellach.")
add("Q5465047", "later", "The St John family", "Teulu St John", "13th century onwards", "Still lived in.", "Mae pobl yn byw ynddo o hyd.")
add("Q9706060", "later", "An Elizabethan manor on the site of a castle", "Maenordy Elisabethaidd ar safle castell", "1580s",
    "Now at the heart of St Fagans National Museum of History.", "Yng nghanol Amgueddfa Werin Sain Ffagan bellach.", ["place-stfagans.html"])
add("Q11135409", "later", "The Prichard family, Welsh gentry", "Teulu Prichard, uchelwyr Cymreig", "c. 1540", "", "")
add("Q3403319", "later", "Sir Rice Mansel", "Syr Rice Mansel", "1520s–1530s",
    "A Tudor courtyard house dressed as a castle, above Oxwich Bay.", "Tŷ cwrt Tuduraidd ar wedd castell, uwchben Bae Oxwich.")
add("Q7983096", "later", "The de la Bere family", "Teulu de la Bere", "13th–14th century",
    "A fortified manor looking over the Llwchwr estuary.", "Maenor gaerog yn edrych dros aber afon Llwchwr.")
add("Q15199454", "later", "The bishops of Llandaff", "Esgobion Llandaf", "13th century", "", "")
add("Q17742226", "later", "Built as a castle-style house", "Fe’i codwyd fel plasty ar ddull castell", "1790s", "", "")


# Photos from Wikimedia Commons: Wikidata id -> (file name, photographer or source, licence)
# The first block is the photo Wikidata itself gives for each castle (its "image" property).
PHOTOS = {
 "Q275128": ("Castell_Caernarfon_yn_y_cyfnos_yn_2023_-_Castell_Caernarfon,_Gwynedd,_Wales_at_Dusk_-_2023_10.png", "", ""),
 "Q540964": ("Castell_a_Morfa_Harlech,_Gwynedd,_Mai_2024_-_Parc_Cenedlaethol_Eryri_National_Park_02.jpg", "", ""),
 "Q756830": ("Conwy-Castle-0006.jpg", "", ""),
 "Q756815": ("Castell_Beaumaris_Castle,_Ynys_Mon_(Anglesey),_Wales_44.png", "", ""),
 "Q682601": ("Caerphilly_aerial.jpg", "", ""),
 "Q1422235": ("PembrokeCastle_2007.jpg", "", ""),
 "Q1070187": ("Chepstow_castle_-_panoramio.jpg", "", ""),
 "Q2630723": ("Raglan_Castle,_Monmouthshire_01.JPG", "", ""),
 "Q1585938": ("Rhuddlan_Castle,_May_2012.jpg", "Julie Anne Workman", "CC BY-SA 3.0"),
 "Q1428846": ("YFflintLB04.JPG", "", ""),
 "Q1139896": ("Criccieth_Castle_(14393993760).jpg", "", ""),
 "Q1035742": ("Cardiff_Castle_-_panoramio_(1).jpg", "", ""),
 "Q1186885": ("Castell_Dinbych,_Dinbych,_Sir_Ddinbych_(Denbigh_Castle,_Wales)_-_Grade_1_listed_15.jpg", "", ""),
 "Q1585849": ("Kidwelly_castle_whole.JPG", "Iphrit", "CC BY-SA 3.0"),
 "Q3403691": ("Carreg_Cennen_seen_from_the_southeast_-_geograph.org.uk_-_211604.jpg", "", ""),
 "Q1985853": ("White_Castle,_Cadw_image.jpg", "", ""),
 "Q7116379": ("Oystermouth_Castle_-_geograph.org.uk_-_292767.jpg", "", ""),
 "Q319745": ("Arfordir_Aberystwyth,_Ceredigion_-_Aberystwyth_SAC_Special_Areas_of_Conservation,_West_Wales_Marine_43.jpg", "", ""),
 "Q2369922": ("Dolwyddelan_Castle,_Conwy,_Wales.jpg", "", ""),
 "Q4986692": ("Builth_Wells_Castle_-_geograph.org.uk_-_1566860.jpg", "", ""),
 "Q5419069": ("Ewloe_Castle.JPG", "", ""),
 "Q7534629": ("SKENFRITH_CASTLE.jpg", "", ""),
 "Q1048693": ("Awyrlun_o_Gastell_y_Bere_yn_Hydref_2024_-_Aerial_image_of_Welsh_castle_Castell_y_Bere_near_Tywyn,_Gwynedd,_Wales_50.png", "", ""),
 "Q1508342": ("Manorbier_Castle2.jpg", "", ""),
 "Q752721": ("Carew_Castle_Summer_2018.jpg", "", ""),
 "Q3402778": ("Grosmont_Castle_from_the_south,_2011.jpg", "", ""),
 "Q3306356": ("Castell_y_Waun,_y_Waun,_Sir_Wrecsam_-_Chirk_Castle,_Wrexham_Borough,_Wales_07.jpg", "", ""),
 "Q2713117": ("Dinefwr_Castle_(30551882917).jpg", "", ""),
 "Q1377263": ("PowisCastle.jpg", "", ""),
 "Q2078555": ("Dolbadarn_Castle_Cadw.jpg", "", ""),
 "Q911714": ("Laugharne_Castle.jpg", "", ""),
 # the lead photo of each castle's Wikipedia article
 "Q17742226": ("Amroth_Castle_(geograph_2668806).jpg", "Stuart Logan", "CC BY-SA 2.0"),
 "Q8027762": ("Interior_of_Wiston_Castle,_Pembrokeshire.jpg", "Xyphoid", "CC BY-SA 4.0"),
 "Q3403319": ("Oxwich_castle_entrance_(1294837).jpg", "Percy Benzie Abery", "CC0"),
 "Q7653666": ("Swansea_Castle_2018.jpg", "Tiia Monto", "CC BY-SA 4.0"),
 "Q1107288": ("Coitycastledomesticrange.jpg", "Celia Kozlowski", "CC BY 3.0"),
 "Q3401324": ("Dryslwyn_Castle_and_the_River_Towy_-_geograph.org.uk_-_1812519.jpg", "Ruth Sharville", "CC BY-SA 2.0"),
 "Q3395294": ("Cardigan_Castle_-_south_western_aspect-Geograph-6075948-by-M-J-Roscoe.jpg", "M J Roscoe", "CC BY-SA 2.0"),
 "Q1774870": ("CilgerranCastleH4a.jpg", "Helge Klaus Rieder", "CC0"),
 "Q4516540": ("New_Castle,_in_Emlyn,_Cardiganshire.jpeg", "Richard Salway Booth", "Public domain"),
 "Q26722409": ("Garn_Fadryn.jpg", "Velela", "Public domain"),
 "Q525635": ("Monmouth_Castle_from_above.jpg", "Scribwik", "CC BY-SA 4.0"),
 "Q3400816": ("Montgomery_Castle,_Wales,_Panorama_I.jpg", "Gregg M. Erickson", "CC BY 3.0"),
 "Q1235495": ("Castell_Dolforwyn_-_Dolforwyn_Castle,_Powys,_Cymru_(Wales)_22.jpg", "Llywelyn2000", "CC BY-SA 4.0"),
 "Q3402621": ("Castell_y_Penrhyn_Bangor_Gwynedd_12.JPG", "Llywelyn2000", "CC BY-SA 3.0"),
 "Q3398574": ("Gwydir_Castle,_viewed_from_the_Dutch_Garden.JPG", "Hogyn Lleol", "CC BY-SA 3.0"),
 "Q2969121": ("Castell_Degannwy_Deganwy_Castle_Sir_Ddinbych_Wales_68.JPG", "Llywelyn2000", "CC BY-SA 4.0"),
 "Q3395336": ("Gwrych_Castle,_Denbighshire.jpeg", "Thomas Jeavons, engraver", "Public domain"),
 "Q5884534": ("Holt_Castle_Ruins.jpg", "Gavin Platt", "CC BY-SA 4.0"),
 "Q2968597": ("Bodelwyddan_castle_view2_arp.jpg", "Adrian Pingstone", "Public domain"),
 "Q3403676": ("Castell_Rhuthun_-_adfeilion_y_goresgynwyr_(wel_o_lia_fe_drion_nhw)_27.JPG", "Llywelyn2000", "CC BY-SA 3.0"),
}

# The castles shown as large cards in "Castles of the Welsh princes", in this order.
FEATURED = ["Q1048693", "Q2369922", "Q2078555", "Q1139896", "Q1226281", "Q1235495", "Q2713117", "Q3401324", "Q3395294",
            "Q5419069", "Q3398523", "Q1377263", "Q7659623", "Q354820", "Q2630723", "Q3403691"]
