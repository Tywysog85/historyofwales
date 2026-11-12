# Historic places of real importance: the royal seats, the castles of the princes, the abbeys and saints' places,
# Roman forts, hillforts, and the places of later Wales (November 2026). Ifan asked for Dinefwr "and other places of
# importance", the places cared for by Cadw and the National Trust, and for people to be able to visit them.
#
#   NEW     new places (same shape as src/places2.py); data.py adds them to PLACES at the end
#   LONG    the longer text for a place page (new places, and fuller text for existing ones); long.py merges it
#           into PLACE_LONG. "## " starts a sub-heading. Sources go beside the claims with [[cite:key]] (src/cites.py);
#           the keys used here are in CITES at the bottom and are added to cites.S.
#   PEOPLE  person slugs linked with each place. A slug with no page yet is skipped, so it lights up by itself
#           when another thread adds that person. Person pages list these places back.
#   LINKS   other pages on the site about the place (legends, long reads, 3D)
# Visiting details (who looks after it, the official link, postcode, entry) are in src/visit.py.
# Each new page's picture is one line in PAGE in src/pictures.py.


def P(id, en, cy, era, lat, lon, year, ill, wiki, dEn, dCy):
    return dict(id=id, en=en, cy=cy, era=era, lat=lat, lon=lon, year=year, ill=ill, src=wiki, dEn=dEn, dCy=dCy)


NEW = [
 # ---------- the courts and castles of the princes ----------
 P("garthcelyn", "Garth Celyn, Abergwyngregyn", "Garth Celyn, Abergwyngregyn", "medieval", 53.238, -4.019, "1200s", "crown", "Aber,_Gwynedd",
   "The court of the princes of Gwynedd at Aber, looking out over the Menai Strait. Siwan died here, and here Llywelyn ap Gruffudd’s daughter Gwenllian was born in 1282.",
   "Llys tywysogion Gwynedd yn Aber, yn edrych dros y Fenai. Yma y bu farw Siwan, ac yma y ganed Gwenllian, merch Llywelyn ap Gruffudd, yn 1282."),
 P("dolwyddelan", "Dolwyddelan Castle", "Castell Dolwyddelan", "medieval", 53.053, -3.908, "c. 1210", "castle", "Dolwyddelan_Castle",
   "Llywelyn the Great’s tower on a rock above the Lledr valley, guarding the mountain road through the heart of Gwynedd.",
   "Tŵr Llywelyn Fawr ar graig uwchben dyffryn Lledr, yn gwarchod y ffordd fynydd drwy galon Gwynedd."),
 P("dinasemrys", "Dinas Emrys", "Dinas Emrys", "saints", 53.022, -4.090, "5th century", "mtn", "Dinas_Emrys",
   "The hill near Beddgelert where, in the old story, Gwrtheyrn’s tower kept falling, and the boy Emrys showed the red and white dragons fighting beneath it.",
   "Y bryn ger Beddgelert lle, yn yr hen stori, roedd tŵr Gwrtheyrn yn dal i syrthio, a lle dangosodd y bachgen Emrys y ddraig goch a’r ddraig wen yn ymladd oddi tano."),
 P("llysrhosyr", "Llys Rhosyr", "Llys Rhosyr", "medieval", 53.162, -4.366, "1200s", "crown", "Llys_Rhosyr",
   "The only court of the Welsh princes whose walls you can walk among today, at Newborough on Ynys Môn. A great storm buried it in sand in 1332.",
   "Yr unig lys o eiddo tywysogion Cymru y gallwch gerdded ymysg ei furiau heddiw, yn Niwbwrch ar Ynys Môn. Claddwyd ef dan dywod gan storm fawr yn 1332."),
 P("cricieth", "Criccieth Castle", "Castell Cricieth", "medieval", 52.916, -4.232, "c. 1230", "castle", "Criccieth_Castle",
   "A castle of the princes of Gwynedd on a headland above Tremadog Bay. Llywelyn the Great built its great gatehouse and his grandson Llywelyn ap Gruffudd made it larger.",
   "Castell tywysogion Gwynedd ar bentir uwchben Bae Tremadog. Llywelyn Fawr a gododd ei borthdy mawr, a gwnaeth ei ŵyr Llywelyn ap Gruffudd ef yn fwy."),
 P("dolforwyn", "Dolforwyn Castle", "Castell Dolforwyn", "medieval", 52.546, -3.252, "1273", "castle", "Dolforwyn_Castle",
   "Llywelyn ap Gruffudd’s castle above the Severn, built in 1273. When the king told him to stop, Llywelyn answered that he needed no one’s leave to build on his own land.",
   "Castell Llywelyn ap Gruffudd uwchben afon Hafren, a godwyd yn 1273. Pan orchmynnodd y brenin iddo roi’r gorau iddi, atebodd Llywelyn nad oedd angen caniatâd neb arno i adeiladu ar ei dir ei hun."),
 P("dryslwyn", "Dryslwyn Castle", "Castell Dryslwyn", "medieval", 51.862, -4.102, "1200s", "castle", "Dryslwyn_Castle",
   "A castle of the princes of Deheubarth on a lone hill in the Tywi valley. In 1287 Rhys ap Maredudd held it against an army of eleven thousand.",
   "Castell tywysogion Deheubarth ar fryn unig yn nyffryn Tywi. Yn 1287 daliodd Rhys ap Maredudd ef yn erbyn byddin o un fil ar ddeg."),
 P("carregcennen", "Carreg Cennen Castle", "Castell Carreg Cennen", "medieval", 51.854, -3.936, "c. 1280", "castle", "Carreg_Cennen_Castle",
   "A castle on a limestone cliff at the edge of the Black Mountain, in the old lands of Deheubarth. Voted the most romantic ruin in Wales.",
   "Castell ar glogwyn calchfaen ar ymyl y Mynydd Du, yn hen diroedd Deheubarth. Pleidleisiwyd mai hwn yw’r adfail mwyaf rhamantus yng Nghymru."),
 P("ewloe", "Ewloe Castle", "Castell Ewloe", "medieval", 53.200, -3.067, "c. 1210", "castle", "Ewloe_Castle",
   "A Welsh castle hidden in a wooded hollow in Flintshire, close to where Owain Gwynedd ambushed the army of Henry II in 1157.",
   "Castell Cymreig ynghudd mewn pant coediog yn Sir y Fflint, yn agos i’r fan lle ymosododd Owain Gwynedd ar fyddin Harri II yn 1157."),
 P("deganwy", "Deganwy", "Degannwy", "saints", 53.297, -3.825, "c. 530", "crown", "Deganwy_Castle",
   "Twin hills above the mouth of the Conwy where, in Welsh tradition, Maelgwn Gwynedd kept his court and the young Taliesin out-sang his bards.",
   "Dau fryn uwchben aber afon Conwy lle, yn ôl traddodiad Cymru, y cadwai Maelgwn Gwynedd ei lys, ac y canodd y Taliesin ifanc yn well na’i feirdd."),
 P("dinasbran", "Castell Dinas Brân", "Castell Dinas Brân", "medieval", 52.979, -3.159, "c. 1260", "castle", "Castell_Dinas_Br%C3%A2n",
   "The castle of the princes of Powys Fadog, high on a hill above Llangollen, inside a far older hillfort.",
   "Castell tywysogion Powys Fadog, yn uchel ar fryn uwchben Llangollen, o fewn bryngaer lawer hŷn."),
 P("cwmhir", "Abbey Cwmhir", "Abaty Cwm-hir", "medieval", 52.331, -3.390, "1176", "cross", "Cwmhir_Abbey",
   "A Cistercian abbey in a quiet valley of Maelienydd. Here, by long tradition, the monks buried the body of Llywelyn ap Gruffudd in December 1282.",
   "Abaty Sistersaidd mewn cwm tawel ym Maelienydd. Yma, yn ôl hen draddodiad, y claddodd y mynachod gorff Llywelyn ap Gruffudd ym mis Rhagfyr 1282."),
 P("powis", "Powis Castle", "Castell Powys", "medieval", 52.650, -3.157, "1200s", "castle", "Powis_Castle",
   "The red castle of the princes of Powys Wenwynwyn above Welshpool, lived in ever since and now famous for its terraced gardens.",
   "Castell coch tywysogion Powys Wenwynwyn uwchben y Trallwng, sydd wedi bod yn gartref byth ers hynny ac sy’n enwog heddiw am ei erddi teras."),
 P("kidwelly", "Kidwelly Castle", "Castell Cydweli", "medieval", 51.740, -4.308, "1136", "castle", "Kidwelly_Castle",
   "Near this castle in 1136 Gwenllian, daughter of Gruffudd ap Cynan, led an army against its Norman lord and gave her life. The Lord Rhys took the castle in 1159.",
   "Ger y castell hwn yn 1136 arweiniodd Gwenllian, merch Gruffudd ap Cynan, fyddin yn erbyn ei arglwydd Normanaidd a rhoi ei bywyd. Cipiodd yr Arglwydd Rhys y castell yn 1159."),
 P("llanymddyfri", "Llandovery", "Llanymddyfri", "medieval", 51.995, -3.796, "1401", "castle", "Llywelyn_ap_Gruffydd_Fychan",
   "Before the castle gate here in 1401, Llywelyn ap Gruffudd Fychan of Caeo was put to death for leading the king’s army astray to save Owain Glyndŵr. His statue stands beside it.",
   "O flaen porth y castell yma yn 1401, rhoddwyd Llywelyn ap Gruffudd Fychan o Gaeo i farwolaeth am arwain byddin y brenin ar gyfeiliorn i achub Owain Glyndŵr. Mae ei gerflun yn sefyll gerllaw."),
]


LONG = {
 # ---------- the royal seats ----------
 "dinefwr": (
  ["## The seat of the south",
   "Dinefwr stands on a wooded hill above the River Tywi, close to Llandeilo. It was the chief court of Deheubarth, the kingdom of the south-west. Welsh tradition holds that Rhodri Mawr shared his lands among his sons, giving Aberffraw to Anarawd, Dinefwr to Cadell and Mathrafal to Merfyn, and from Cadell came the kings of the south.",
   "Gerald of Wales, writing in the 1190s, named three royal seats of Wales: Dinefwr in the south, Aberffraw in the north and Pengwern in Powys. He wrote that the royal seat of the south had moved to Dinefwr from Caerleon.[[cite:pl-gerald-seats]]",
   "## The Lord Rhys",
   "Hywel Dda, the lawgiver king, was Cadell’s son. From the same line came Rhys ap Tewdwr, king of Deheubarth, and his grandson Rhys ap Gruffudd, the Lord Rhys, who ruled the south from 1155 until his death in 1197. At Dinefwr, the ancient capital, Rhys began a castle in the new style, in stone.[[cite:pl-dwb-rhys]]",
   "His years brought a rare peace to the south, and Welsh music and poetry flowered.[[cite:pl-cadw-dinefwr]] He held the famous eisteddfod at Cardigan in 1176, made Strata Florida Abbey almost his own creation and founded Talley Abbey, a few miles from Dinefwr.[[cite:pl-dwb-rhys]]",
   "## Held through hard years",
   "After Rhys died, his sons and grandsons held Dinefwr through long struggles with one another and with the English. It fell into the hands of the English crown in 1287, and in 1403 Owain Glyndŵr’s army came to win it back.[[cite:pl-cadw-dinefwr]]",
   "The family of Sir Rhys ap Thomas, who helped Harri Tudur to the crown in 1485, made their home at Dinefwr, and in the 1600s they built Newton House in the park below the castle.",
   "## Dinefwr today",
   "The castle is cared for by Cadw on land owned by the National Trust, which looks after the deer park, the old cattle herd and Newton House.[[cite:pl-nt-dinefwr]] From the walls you can see far along the Tywi valley, the heart of the old kingdom, and Dryslwyn and the Black Mountain beyond."],
  ["## Llys y de",
   "Saif Dinefwr ar fryn coediog uwchben afon Tywi, yn ymyl Llandeilo. Dyma brif lys Deheubarth, teyrnas y de-orllewin. Yn ôl traddodiad Cymru rhannodd Rhodri Mawr ei diroedd rhwng ei feibion, gan roi Aberffraw i Anarawd, Dinefwr i Gadell a Mathrafal i Ferfyn, ac o Gadell y daeth brenhinoedd y de.",
   "Yn y 1190au enwodd Gerallt Gymro dri llys brenhinol Cymru: Dinefwr yn y de, Aberffraw yn y gogledd a Phengwern ym Mhowys. Ysgrifennodd fod llys brenhinol y de wedi symud i Ddinefwr o Gaerllion.[[cite:pl-gerald-seats]]",
   "## Yr Arglwydd Rhys",
   "Roedd Hywel Dda, y brenin a roddodd y gyfraith, yn fab i Gadell. O’r un llinach y daeth Rhys ap Tewdwr, brenin Deheubarth, a’i ŵyr Rhys ap Gruffudd, yr Arglwydd Rhys, a reolodd y de o 1155 hyd ei farw yn 1197. Yn Ninefwr, yr hen brifddinas, dechreuodd Rhys godi castell yn y dull newydd, o gerrig.[[cite:pl-dwb-rhys]]",
   "Daeth ei flynyddoedd â heddwch prin i’r de, a blodeuodd cerddoriaeth a barddoniaeth Gymraeg.[[cite:pl-cadw-dinefwr]] Cynhaliodd yr eisteddfod enwog yn Aberteifi yn 1176, gwnaeth Abaty Ystrad Fflur bron yn greadigaeth iddo’i hun, a sefydlodd Abaty Talyllychau, ychydig filltiroedd o Ddinefwr.[[cite:pl-dwb-rhys]]",
   "## Ei ddal drwy flynyddoedd caled",
   "Wedi marw Rhys, daliodd ei feibion a’i wyrion Ddinefwr drwy frwydrau hir â’i gilydd ac â’r Saeson. Syrthiodd i ddwylo coron Lloegr yn 1287, ac yn 1403 daeth byddin Owain Glyndŵr i’w ennill yn ôl.[[cite:pl-cadw-dinefwr]]",
   "Gwnaeth teulu Syr Rhys ap Thomas, a helpodd Harri Tudur i’r goron yn 1485, eu cartref yn Ninefwr, ac yn y 1600au codasant Dŷ Newton yn y parc islaw’r castell.",
   "## Dinefwr heddiw",
   "Cadw sy’n gofalu am y castell, ar dir sy’n eiddo i’r Ymddiriedolaeth Genedlaethol, sy’n gofalu am y parc ceirw, yr hen fuches wartheg a Thŷ Newton.[[cite:pl-nt-dinefwr]] O’r muriau gallwch weld ymhell ar hyd dyffryn Tywi, calon yr hen deyrnas, a Dryslwyn a’r Mynydd Du y tu hwnt."]),

 "aberffraw": (
  ["## The chief court of Gwynedd",
   "Aberffraw, a village by the sea on the south-west coast of Ynys Môn, was the chief court of the kings of Gwynedd. Gerald of Wales named it as the royal seat of the north, one of the three royal seats of Wales.[[cite:pl-gerald-seats]] Welsh tradition holds that Rhodri Mawr left Aberffraw to his son Anarawd, and Anarawd’s line ruled Gwynedd for the next four hundred years.",
   "Here the kings and princes kept their hall, their law court and their household of officers, the steward, the judge, the chief poet and the rest, as the Laws of Hywel Dda describe them. From the 1230s Llywelyn the Great called himself Prince of Aberffraw and Lord of Snowdon, and the name of this small place stood for the whole of Gwynedd.",
   "## In the Mabinogi",
   "In the Second Branch of the Mabinogi, Branwen daughter of Llŷr is married to Matholwch, king of Ireland, at Aberffraw, and the wedding feast is held here in tents, because no house could hold Bendigeidfran.",
   "## What became of the court",
   "After the conquest of 1283 the court fell out of use, and in 1317 its buildings were taken down to provide materials for Caernarfon Castle across the Menai. No one knows today exactly where the hall stood. The church of St Beuno, with stonework of the 1100s, is the oldest building in the village.",
   "Today Aberffraw is a quiet village with a sandy bay. Walk down to the old bridge over the Ffraw and look out over the dunes: this was the centre of power in north Wales for four centuries."],
  ["## Prif lys Gwynedd",
   "Aberffraw, pentref ger y môr ar arfordir de-orllewin Ynys Môn, oedd prif lys brenhinoedd Gwynedd. Enwodd Gerallt Gymro ef yn llys brenhinol y gogledd, un o dri llys brenhinol Cymru.[[cite:pl-gerald-seats]] Yn ôl traddodiad Cymru gadawodd Rhodri Mawr Aberffraw i’w fab Anarawd, a llinach Anarawd a reolodd Wynedd am y pedwar can mlynedd nesaf.",
   "Yma y cadwai’r brenhinoedd a’r tywysogion eu neuadd, eu llys barn a’u teulu o swyddogion, y distain, yr ynad, y pencerdd a’r lleill, fel y mae Cyfreithiau Hywel Dda yn eu disgrifio. O’r 1230au galwai Llywelyn Fawr ei hun yn Dywysog Aberffraw ac Arglwydd Eryri, a daeth enw’r lle bychan hwn i olygu Gwynedd gyfan.",
   "## Yn y Mabinogi",
   "Yn Ail Gainc y Mabinogi, priodir Branwen ferch Llŷr â Matholwch, brenin Iwerddon, yn Aberffraw, a chynhelir y wledd yma mewn pebyll, am na allai unrhyw dŷ ddal Bendigeidfran.",
   "## Beth ddaeth o’r llys",
   "Wedi’r goncwest yn 1283 aeth y llys yn segur, ac yn 1317 tynnwyd ei adeiladau i lawr i gael defnyddiau i Gastell Caernarfon dros y Fenai. Ni ŵyr neb heddiw yn union ble safai’r neuadd. Eglwys Beuno, gyda gwaith maen o’r 1100au, yw’r adeilad hynaf yn y pentref.",
   "Heddiw mae Aberffraw yn bentref tawel gyda bae tywodlyd. Cerddwch i lawr at yr hen bont dros afon Ffraw ac edrych allan dros y twyni: dyma ganolfan grym gogledd Cymru am bedair canrif."]),

 "mathrafal": (
  ["## The court of Powys",
   "Mathrafal lies where the River Banwy meets the Vyrnwy, a few miles from Meifod. It was the seat of the kings and princes of Powys, probably from the 800s. Welsh tradition holds that Rhodri Mawr gave Mathrafal to his son Merfyn, and counts it, with Aberffraw and Dinefwr, among the three chief courts of Wales.",
   "Gerald of Wales named Pengwern, where Shrewsbury now stands, as the old royal seat of Powys.[[cite:pl-gerald-seats]] As the border moved west, Mathrafal became the heart of the kingdom. The princes of Powys, descended from Bleddyn ap Cynfyn, ruled from here, and the poet Cynddelw Brydydd Mawr sang to his heirs.",
   "## The castle of 1212",
   "In 1212 King John’s commander Robert de Vieuxpont built a castle at Mathrafal. Llywelyn the Great and Gwenwynwyn of Powys besieged it together, and when King John came to relieve it, the castle was destroyed. The court was never rebuilt.",
   "## What you can see",
   "The site is a square enclosure about 90 metres across, with a bank and ditch on three sides and the river on the fourth, and a castle mound in one corner. It is on private farmland, but you can see it from the lane. Nearby Meifod church, where the princes of Powys were buried, is open to visitors."],
  ["## Llys Powys",
   "Mae Mathrafal lle mae afon Banwy yn cwrdd ag afon Efyrnwy, ychydig filltiroedd o Feifod. Dyma lys brenhinoedd a thywysogion Powys, o’r 800au yn ôl pob tebyg. Yn ôl traddodiad Cymru rhoddodd Rhodri Mawr Fathrafal i’w fab Merfyn, ac mae’n ei gyfrif, gydag Aberffraw a Dinefwr, yn un o dri phrif lys Cymru.",
   "Enwodd Gerallt Gymro Bengwern, lle saif Amwythig heddiw, yn hen lys brenhinol Powys.[[cite:pl-gerald-seats]] Wrth i’r ffin symud tua’r gorllewin, daeth Mathrafal yn galon y deyrnas. Oddi yma y rheolai tywysogion Powys, disgynyddion Bleddyn ap Cynfyn, a chanodd y bardd Cynddelw Brydydd Mawr i’w etifeddion.",
   "## Castell 1212",
   "Yn 1212 cododd Robert de Vieuxpont, cadlywydd y Brenin John, gastell ym Mathrafal. Gwarchaeodd Llywelyn Fawr a Gwenwynwyn o Bowys arno gyda’i gilydd, a phan ddaeth y Brenin John i’w achub, dinistriwyd y castell. Ni chodwyd y llys byth eto.",
   "## Beth welwch chi",
   "Mae’r safle’n lloc sgwâr tua 90 metr ar draws, gyda chlawdd a ffos ar dair ochr a’r afon ar y bedwaredd, a thomen castell mewn un gornel. Mae ar dir fferm preifat, ond gallwch ei weld o’r lôn. Mae eglwys Meifod gerllaw, lle claddwyd tywysogion Powys, ar agor i ymwelwyr."]),

 "garthcelyn": (
  ["## The princes’ court at Aber",
   "Abergwyngregyn, Aber for short, lies between the mountains and the sea where the old road from Conwy came down to the shore across from Ynys Môn. The princes of Gwynedd had a court here, which they called Garth Celyn.",
   "Siwan, wife of Llywelyn the Great and daughter of King John, died at Aber in 1237, and Llywelyn founded a friary at Llanfaes across the water in her memory. His grandson Llywelyn ap Gruffudd made Garth Celyn one of his chief homes.",
   "## 1282",
   "Here, on 19 June 1282, Eleanor de Montfort, Llywelyn’s wife, died after giving birth to their daughter Gwenllian.[[cite:pl-dwb-eleanor]] Six months later Llywelyn was killed near Builth, and in June 1283 his brother Dafydd was taken in the mountains above the village.",
   "## The site today",
   "Where exactly the court stood is still argued over. A mound in the valley floor, Pen y Mwd, and a large stone building found by excavation nearby may belong to it. Pen y Bryn, a house on the hill to the east, stands within old banks that many hold to be Garth Celyn itself; it is a private home.",
   "The village is the start of the walk up the valley to Rhaeadr Fawr, the Aber Falls, the same path the princes’ people would have known."],
  ["## Llys y tywysogion yn Aber",
   "Mae Abergwyngregyn, neu Aber, rhwng y mynyddoedd a’r môr lle deuai’r hen ffordd o Gonwy i lawr at y lan gyferbyn ag Ynys Môn. Roedd gan dywysogion Gwynedd lys yma, a’i alw’n Garth Celyn.",
   "Bu farw Siwan, gwraig Llywelyn Fawr a merch y Brenin John, yn Aber yn 1237, a sefydlodd Llywelyn frodordy yn Llan-faes dros y dŵr er cof amdani. Gwnaeth ei ŵyr Llywelyn ap Gruffudd Garth Celyn yn un o’i brif gartrefi.",
   "## 1282",
   "Yma, ar 19 Mehefin 1282, bu farw Elinor de Montfort, gwraig Llywelyn, ar ôl geni eu merch Gwenllian.[[cite:pl-dwb-eleanor]] Chwe mis yn ddiweddarach lladdwyd Llywelyn ger Llanfair-ym-Muallt, ac ym Mehefin 1283 daliwyd ei frawd Dafydd yn y mynyddoedd uwchben y pentref.",
   "## Y safle heddiw",
   "Mae dadlau o hyd am union safle’r llys. Gall tomen yng ngwaelod y dyffryn, Pen y Mwd, ac adeilad carreg mawr a gafwyd wrth gloddio gerllaw berthyn iddo. Saif Pen y Bryn, tŷ ar y bryn i’r dwyrain, o fewn hen gloddiau y mae llawer yn credu mai Garth Celyn ei hun ydynt; cartref preifat yw.",
   "Mae’r pentref yn fan cychwyn y daith gerdded i fyny’r dyffryn at Raeadr Fawr, yr un llwybr ag a adwaenai pobl y tywysogion."]),

 "llysrhosyr": (
  ["## A court of the princes",
   "The princes of Gwynedd moved around their land with their household, staying at a llys, a royal court, in each commote. Llys Rhosyr was the court of the commote of Menai, beside the village now called Newborough.",
   "Gwynedd Archaeological Trust began to dig here in 1992 and found a walled enclosure with three large buildings: probably the great hall, the prince’s chamber and storehouses. It is the only undefended court of the Welsh princes that excavation has confirmed, and the only one with walls you can visit.[[cite:pl-cadw-llysrhosyr]]",
   "## Buried by the sand",
   "In the winter of 1332 a great storm blew the dunes over the fields and buildings of Rhosyr, and the court was lost under the sand until our own time.",
   "## See it rebuilt",
   "St Fagans National Museum of History has rebuilt the hall and chamber of Llys Rhosyr full size, as Llys Llywelyn, opened in 2018. On this site you can also walk through the court in 3D: see the link below."],
  ["## Un o lysoedd y tywysogion",
   "Symudai tywysogion Gwynedd o gwmpas eu tir gyda’u llys, gan aros mewn llys brenhinol ym mhob cwmwd. Llys Rhosyr oedd llys cwmwd Menai, ger y pentref a elwir heddiw yn Niwbwrch.",
   "Dechreuodd Ymddiriedolaeth Archaeolegol Gwynedd gloddio yma yn 1992 a chael lloc â mur o’i gwmpas a thri adeilad mawr: y neuadd fawr, ystafell y tywysog a stordai, yn ôl pob tebyg. Dyma’r unig lys diamddiffyn o eiddo tywysogion Cymru a gadarnhawyd drwy gloddio, a’r unig un â muriau y gallwch ymweld â nhw.[[cite:pl-cadw-llysrhosyr]]",
   "## Dan y tywod",
   "Yn ystod gaeaf 1332 chwythodd storm fawr y twyni dros gaeau ac adeiladau Rhosyr, a chollwyd y llys dan y tywod hyd ein hamser ni.",
   "## Ei weld wedi’i ailgodi",
   "Mae Sain Ffagan Amgueddfa Werin Cymru wedi ailgodi neuadd ac ystafell Llys Rhosyr maint llawn, fel Llys Llywelyn, a agorwyd yn 2018. Ar y wefan hon gallwch hefyd gerdded drwy’r llys mewn 3D: gweler y ddolen isod."]),

 # ---------- castles of the princes ----------
 "dolbadarn": (
  ["Dolbadarn stands on a rock between the two lakes of Llanberis, Llyn Padarn and Llyn Peris, beneath Yr Wyddfa. It guarded the road from Caernarfon over the mountains to the upper Conwy valley, one of the main ways into the heart of Gwynedd.[[cite:pl-cadw-dolbadarn]]",
   "Llywelyn the Great most likely built it in the early 1200s. Its round tower, 15 metres high, is one of the finest towers built by a Welsh prince, and Llywelyn seems to have taken the idea from the castles of his rivals in the southern March, then built it better.[[cite:pl-cadw-dolbadarn]]",
   "His grandson Llywelyn ap Gruffudd held it, and in 1283 it was among the last strongholds of his brother Dafydd. Five hundred years later its tower drew the painters: J. M. W. Turner painted Dolbadarn in 1800, and it became a picture of Wales known across Europe.",
   "The castle is cared for by Cadw and is free to visit, a short walk from Llanberis."],
  ["Saif Dolbadarn ar graig rhwng dau lyn Llanberis, Llyn Padarn a Llyn Peris, dan yr Wyddfa. Gwarchodai’r ffordd o Gaernarfon dros y mynyddoedd i ddyffryn Conwy uchaf, un o’r prif ffyrdd i galon Gwynedd.[[cite:pl-cadw-dolbadarn]]",
   "Llywelyn Fawr a’i cododd, yn ôl pob tebyg, ar ddechrau’r 1200au. Mae ei dŵr crwn, 15 metr o uchder, yn un o’r tyrau gorau a godwyd gan dywysog o Gymro, ac mae’n ymddangos i Lywelyn gymryd y syniad o gestyll ei gystadleuwyr yn y Mers deheuol, ac yna ei godi’n well.[[cite:pl-cadw-dolbadarn]]",
   "Daliodd ei ŵyr Llywelyn ap Gruffudd ef, ac yn 1283 roedd ymhlith cadarnleoedd olaf ei frawd Dafydd. Bum can mlynedd yn ddiweddarach denodd ei dŵr yr arlunwyr: peintiodd J. M. W. Turner Ddolbadarn yn 1800, a daeth yn llun o Gymru a adwaenid ar draws Ewrop.",
   "Cadw sy’n gofalu am y castell, ac mae am ddim i ymweld ag ef, dro byr o Lanberis."]),

 "ybere": (
  ["Castell y Bere rises from a rock in the Dysynni valley, under Cadair Idris. Llywelyn the Great began it in 1221 to guard the southern border of Gwynedd.[[cite:pl-cadw-ybere]]",
   "Its Welsh builders gave it an entrance through two gatehouses with drawbridges, extremely advanced for its day, even by the standards of English castles. Carved stone found here shows how fine its buildings once were.[[cite:pl-cadw-ybere]]",
   "In the war of 1282 to 1283, after Llywelyn ap Gruffudd was killed, his brother Dafydd carried on the fight. Castell y Bere held out until April 1283, the last castle of the Welsh princes to fall.",
   "Down the valley at Llanfihangel-y-Pennant is the ruined cottage of Mary Jones, who in 1800 walked some 25 miles to Bala to buy a Welsh Bible. The castle is cared for by Cadw and free to visit."],
  ["Mae Castell y Bere yn codi o graig yn nyffryn Dysynni, dan Gadair Idris. Dechreuodd Llywelyn Fawr ei godi yn 1221 i warchod ffin ddeheuol Gwynedd.[[cite:pl-cadw-ybere]]",
   "Rhoddodd ei adeiladwyr Cymreig fynedfa iddo drwy ddau borthdy â phontydd codi, yn hynod o ddatblygedig yn ei ddydd, hyd yn oed o’i gymharu â chestyll Lloegr. Mae cerrig cerfiedig a gafwyd yma’n dangos mor gain oedd ei adeiladau ar un adeg.[[cite:pl-cadw-ybere]]",
   "Yn rhyfel 1282 i 1283, wedi lladd Llywelyn ap Gruffudd, parhaodd ei frawd Dafydd â’r frwydr. Daliodd Castell y Bere ei dir tan fis Ebrill 1283, castell olaf tywysogion Cymru i syrthio.",
   "I lawr y dyffryn yn Llanfihangel-y-Pennant mae adfail bwthyn Mary Jones, a gerddodd tua 25 milltir i’r Bala yn 1800 i brynu Beibl Cymraeg. Cadw sy’n gofalu am y castell, ac mae am ddim i ymweld ag ef."]),

 "dolwyddelan": (
  ["Dolwyddelan Castle stands on a ridge above the Lledr valley, on the old road between Meirionnydd and the Conwy valley. It was one of the castles built to hold the mountain passes of Gwynedd, and it is a lasting memorial to Llywelyn the Great, ruler of Gwynedd from 1201 to 1240.[[cite:pl-cadw-dolwyddelan]]",
   "Welsh tradition holds that Llywelyn himself was born nearby, at the older castle on the rocky knoll of Tomen Castell in the valley floor, in about 1173.",
   "The castle stayed in Welsh hands until January 1283, when it was taken by the army of Edward I.[[cite:pl-cadw-dolwyddelan]] In the 1800s Lord Willoughby de Eresby gave the keep new battlements, but Llywelyn’s own stonework can still be told apart from the later work.",
   "The castle is cared for by Cadw and free to visit; the ground around it belongs to the farm below, and the keep itself is open on set days."],
  ["Saif Castell Dolwyddelan ar grib uwchben dyffryn Lledr, ar yr hen ffordd rhwng Meirionnydd a dyffryn Conwy. Roedd yn un o’r cestyll a godwyd i ddal bylchau mynydd Gwynedd, ac mae’n gofeb barhaol i Lywelyn Fawr, rheolwr Gwynedd o 1201 hyd 1240.[[cite:pl-cadw-dolwyddelan]]",
   "Yn ôl traddodiad Cymru ganed Llywelyn ei hun gerllaw, yn yr hen gastell ar y bryncyn creigiog Tomen Castell yng ngwaelod y dyffryn, tua 1173.",
   "Arhosodd y castell yn nwylo’r Cymry tan fis Ionawr 1283, pan gipiwyd ef gan fyddin Edward I.[[cite:pl-cadw-dolwyddelan]] Yn y 1800au rhoddodd yr Arglwydd Willoughby de Eresby fylchfuriau newydd ar y gorthwr, ond gellir adnabod gwaith maen Llywelyn ei hun o hyd.",
   "Cadw sy’n gofalu am y castell ac mae am ddim i ymweld ag ef; mae’r tir o’i gwmpas yn eiddo i’r fferm islaw, ac mae’r gorthwr ei hun ar agor ar ddyddiau penodol."]),

 "dinasemrys": (
  ["## The tower that would not stand",
   "Dinas Emrys is a steep wooded hill in Nant Gwynant, near Beddgelert. The History of the Britons, written in Gwynedd about 829, tells how King Gwrtheyrn (Vortigern) tried to build a stronghold here, but each night the building materials vanished.[[cite:pl-historia-brittonum]]",
   "A boy named Emrys (Ambrosius) told the king what lay beneath the hill: a pool, and in it two dragons, one red and one white. When the pool was opened the dragons woke and fought, and at last the red dragon drove out the white. The boy said that the red dragon was the people of Britain and the white the invaders, who would one day be driven out.[[cite:pl-historia-brittonum]] The red dragon has been the sign of Wales ever since.[[cite:pl-nt-dinasemrys]]",
   "## What was found",
   "When archaeologists dug on the hill in the 1900s, they found that people had lived on it from the Iron Age on, and inside the enclosure they found a pool, just as the story says.[[cite:pl-nt-dinasemrys]] The base of a stone tower on the summit is thought to be part of a castle of the princes of Gwynedd.",
   "## Walking there",
   "The hill belongs to the National Trust, and a waymarked path leads up to it from Craflwyn, just outside Beddgelert. The climb is short but steep and rough underfoot."],
  ["## Y tŵr na safai",
   "Bryn coediog serth yn Nant Gwynant, ger Beddgelert, yw Dinas Emrys. Mae Hanes y Brytaniaid, a ysgrifennwyd yng Ngwynedd tua 829, yn adrodd sut y ceisiodd y Brenin Gwrtheyrn godi caer yma, ond bob nos diflannai’r defnyddiau adeiladu.[[cite:pl-historia-brittonum]]",
   "Dywedodd bachgen o’r enw Emrys wrth y brenin beth oedd dan y bryn: llyn, ac ynddo ddwy ddraig, un goch ac un wen. Pan agorwyd y llyn deffrôdd y dreigiau ac ymladd, ac o’r diwedd gyrrodd y ddraig goch y ddraig wen allan. Dywedodd y bachgen mai pobl Prydain oedd y ddraig goch a’r goresgynwyr oedd y wen, ac y byddent un dydd yn cael eu gyrru allan.[[cite:pl-historia-brittonum]] Bu’r ddraig goch yn arwydd Cymru byth ers hynny.[[cite:pl-nt-dinasemrys]]",
   "## Yr hyn a gafwyd",
   "Pan gloddiodd archaeolegwyr ar y bryn yn y 1900au, cawsant fod pobl wedi byw arno o Oes yr Haearn ymlaen, ac o fewn y lloc cawsant lyn, yn union fel y dywed y stori.[[cite:pl-nt-dinasemrys]] Credir bod sylfaen tŵr carreg ar y copa yn rhan o gastell tywysogion Gwynedd.",
   "## Cerdded yno",
   "Mae’r bryn yn eiddo i’r Ymddiriedolaeth Genedlaethol, ac mae llwybr wedi’i arwyddo’n arwain ato o Graflwyn, ychydig y tu allan i Feddgelert. Mae’r dringo’n fyr ond yn serth ac yn arw dan draed."]),

 "cricieth": (
  ["Criccieth Castle crowns a headland between two beaches, looking across Tremadog Bay to Harlech. Llywelyn the Great built its great gatehouse, flanked by two D-shaped towers, and his grandson Llywelyn ap Gruffudd added the outer ward, the curtain walls and two new towers.[[cite:pl-cadw-cricieth]]",
   "After 1283 Edward I held it, with a stone-throwing engine on its north tower. In 1404 the castle was still in English hands when the army of Owain Glyndŵr took it and burned its towers red, and after that the town became entirely Welsh once more.[[cite:pl-cadw-cricieth]]",
   "J. M. W. Turner painted the ruin, and a mile away at Llanystumdwy grew up David Lloyd George. The castle is cared for by Cadw, with a visitor centre at the foot of the hill."],
  ["Mae Castell Cricieth yn coroni pentir rhwng dau draeth, gan edrych ar draws Bae Tremadog at Harlech. Llywelyn Fawr a gododd ei borthdy mawr, rhwng dau dŵr siâp D, ac ychwanegodd ei ŵyr Llywelyn ap Gruffudd y ward allanol, y llenfuriau a dau dŵr newydd.[[cite:pl-cadw-cricieth]]",
   "Wedi 1283 daliodd Edward I ef, gyda pheiriant taflu cerrig ar ei dŵr gogleddol. Yn 1404 roedd y castell yn nwylo’r Saeson o hyd pan gipiodd byddin Owain Glyndŵr ef a llosgi ei dyrau’n goch, ac wedi hynny daeth y dref yn gwbl Gymreig unwaith eto.[[cite:pl-cadw-cricieth]]",
   "Peintiodd J. M. W. Turner yr adfail, a filltir i ffwrdd yn Llanystumdwy y magwyd David Lloyd George. Cadw sy’n gofalu am y castell, gyda chanolfan ymwelwyr wrth droed y bryn."]),

 "dolforwyn": (
  ["## Built in defiance",
   "In 1273 Llywelyn ap Gruffudd, Prince of Wales, began a castle on a ridge above the Severn valley, near Abermule, and founded a new town beside it.[[cite:pl-dwb-llywelyn]] Dolforwyn was meant to hold the middle March and to show who ruled there.",
   "Edward I wrote to forbid him to go on building. Llywelyn answered that he did not need the king’s permission to build on his own land, and carried on.[[cite:pl-cadw-dolforwyn]] It is one of the proudest replies in Welsh history.",
   "## The siege of 1277",
   "In the war of 1277 the Marcher lord Roger Mortimer took Dolforwyn after a two-week siege. The castle was abandoned in the 1300s, and its walls were lost under turf until excavation uncovered them in our own time.[[cite:pl-cadw-dolforwyn]]",
   "Today it is cared for by Cadw and free to visit. A steep path climbs to the ridge, with wide views over the Severn towards Montgomery."],
  ["## Ei godi er gwaethaf y brenin",
   "Yn 1273 dechreuodd Llywelyn ap Gruffudd, Tywysog Cymru, godi castell ar grib uwchben dyffryn Hafren, ger Aber-miwl, a sefydlu tref newydd wrth ei ymyl.[[cite:pl-dwb-llywelyn]] Bwriad Dolforwyn oedd dal canol y Mers a dangos pwy oedd yn rheoli yno.",
   "Ysgrifennodd Edward I i’w wahardd rhag parhau i adeiladu. Atebodd Llywelyn nad oedd angen caniatâd y brenin arno i adeiladu ar ei dir ei hun, a daliodd ati.[[cite:pl-cadw-dolforwyn]] Dyma un o’r atebion balchaf yn hanes Cymru.",
   "## Gwarchae 1277",
   "Yn rhyfel 1277 cipiodd Roger Mortimer, un o arglwyddi’r Mers, Ddolforwyn ar ôl gwarchae o bythefnos. Gadawyd y castell yn y 1300au, a chollwyd ei furiau dan y dywarchen nes i gloddio eu datguddio yn ein hamser ni.[[cite:pl-cadw-dolforwyn]]",
   "Heddiw Cadw sy’n gofalu amdano, ac mae am ddim i ymweld ag ef. Mae llwybr serth yn dringo i’r grib, gyda golygfeydd eang dros Hafren tuag at Drefaldwyn."]),

 "dryslwyn": (
  ["Dryslwyn stands on a lonely hill in the middle of the Tywi valley, between Llandeilo and Carmarthen. It was founded in the 1200s by the princes of Deheubarth, the heirs of the Lord Rhys, and was one of their chief seats.[[cite:pl-cadw-dryslwyn]] A small walled town grew up beside it.",
   "In 1287 Rhys ap Maredudd, lord of Dryslwyn, rose against the English crown. Eleven thousand men were sent to besiege him. For two weeks his castle held out against siege engines and miners, until a great part of the walls was brought down.[[cite:pl-cadw-dryslwyn]] Rhys himself escaped and carried on the fight for some years.",
   "From the top of the hill you can see Dinefwr to the east and Paxton’s Tower to the west. The castle is cared for by Cadw and free to visit."],
  ["Saif Dryslwyn ar fryn unig yng nghanol dyffryn Tywi, rhwng Llandeilo a Chaerfyrddin. Fe’i sefydlwyd yn y 1200au gan dywysogion Deheubarth, etifeddion yr Arglwydd Rhys, ac roedd yn un o’u prif lysoedd.[[cite:pl-cadw-dryslwyn]] Tyfodd tref fechan â mur o’i chwmpas wrth ei ymyl.",
   "Yn 1287 cododd Rhys ap Maredudd, arglwydd Dryslwyn, yn erbyn coron Lloegr. Anfonwyd un fil ar ddeg o ddynion i warchae arno. Am bythefnos daliodd ei gastell yn erbyn peiriannau gwarchae a chloddwyr, nes dymchwel rhan fawr o’r muriau.[[cite:pl-cadw-dryslwyn]] Dihangodd Rhys ei hun a pharhau â’r frwydr am rai blynyddoedd.",
   "O ben y bryn gallwch weld Dinefwr i’r dwyrain a Thŵr Paxton i’r gorllewin. Cadw sy’n gofalu am y castell, ac mae am ddim i ymweld ag ef."]),

 "carregcennen": (
  ["Carreg Cennen sits on a sheer limestone crag nearly 100 metres above the River Cennen, on the western edge of the Black Mountain. It was in the lands of Deheubarth, and there was a Welsh castle here before the one you see now.",
   "The present castle was probably built at the end of the 1200s by John Giffard, one of Edward I’s barons.[[cite:pl-cadw-carregcennen]] In 1403 the army of Owain Glyndŵr besieged it, and in the Wars of the Roses it was held for the House of Lancaster until it was pulled apart in 1462.",
   "A passage cut into the cliff leads down by candlelight to a cave under the castle, where a spring rises. Readers of a national poll voted Carreg Cennen the most romantic ruin in Wales.[[cite:pl-cadw-carregcennen]]",
   "The castle is in Cadw’s care but is reached through the farm at its foot, which runs the ticket office and tea room."],
  ["Mae Carreg Cennen ar glogwyn calchfaen serth bron i 100 metr uwchben afon Cennen, ar ymyl orllewinol y Mynydd Du. Roedd yn nhiroedd Deheubarth, ac roedd castell Cymreig yma cyn yr un a welwch heddiw.",
   "John Giffard, un o farwniaid Edward I, a gododd y castell presennol ar ddiwedd y 1200au, yn ôl pob tebyg.[[cite:pl-cadw-carregcennen]] Yn 1403 gwarchaeodd byddin Owain Glyndŵr arno, ac yn Rhyfeloedd y Rhosynnau daliwyd ef dros Dŷ Lancaster nes ei dynnu’n ddarnau yn 1462.",
   "Mae llwybr wedi’i dorri i’r clogwyn yn arwain i lawr, yng ngolau cannwyll, i ogof dan y castell lle mae ffynnon yn codi. Pleidleisiodd darllenwyr arolwg cenedlaethol mai Carreg Cennen yw’r adfail mwyaf rhamantus yng Nghymru.[[cite:pl-cadw-carregcennen]]",
   "Mae’r castell yng ngofal Cadw ond fe’i cyrhaeddir drwy’r fferm wrth ei droed, sy’n cadw’r swyddfa docynnau a’r ystafell de."]),

 "ewloe": (
  ["Ewloe is a castle of the Welsh princes in an unusual place: not on a crag but in a hollow in thick woodland near Hawarden, in the borderlands that the Welsh and English fought over for centuries.[[cite:pl-cadw-ewloe]]",
   "In 1157 Owain Gwynedd ambushed the army of Henry II in the woods near here, and the king himself was nearly killed. The D-shaped stone tower, so typical of Welsh castles, was probably built by Llywelyn the Great some time after 1210, and his grandson Llywelyn ap Gruffudd added the curtain walls and the round western tower nearly sixty years later.[[cite:pl-cadw-ewloe]]",
   "The castle is cared for by Cadw and free to visit, along a woodland path from the road."],
  ["Mae Ewloe yn gastell o eiddo tywysogion Cymru mewn lle anarferol: nid ar graig ond mewn pant mewn coedwig drwchus ger Penarlâg, yn y gororau y bu’r Cymry a’r Saeson yn ymladd drostynt am ganrifoedd.[[cite:pl-cadw-ewloe]]",
   "Yn 1157 ymosododd Owain Gwynedd ar fyddin Harri II yn y coed gerllaw, a bu bron i’r brenin ei hun gael ei ladd. Llywelyn Fawr, yn ôl pob tebyg, a gododd y tŵr carreg siâp D, mor nodweddiadol o gestyll Cymreig, rywbryd ar ôl 1210, ac ychwanegodd ei ŵyr Llywelyn ap Gruffudd y llenfuriau a’r tŵr crwn gorllewinol bron i drigain mlynedd yn ddiweddarach.[[cite:pl-cadw-ewloe]]",
   "Cadw sy’n gofalu am y castell, ac mae am ddim i ymweld ag ef, ar hyd llwybr drwy’r coed o’r ffordd."]),

 "deganwy": (
  ["## Maelgwn’s court",
   "The two rocky hills of Deganwy, the Faerdre, look across the mouth of the Conwy to Conwy town. Welsh tradition holds that Maelgwn Gwynedd, the great king of the 500s, kept his court here. When Leslie Alcock dug on the hill from 1961 to 1966, he found pieces of pottery brought from the Mediterranean in that very age, the sign of a royal household with links across the seas.",
   "In the tale of Taliesin, the boy poet came to Maelgwn’s court at Deganwy to free his master Elffin, and with his song struck Maelgwn’s twenty-four bards dumb.",
   "## Fought over for centuries",
   "The Annals of Wales record the fortress destroyed in the early 800s. The Normans built a castle here in the 1080s, the Welsh princes took it back, and Henry III built a great new castle in the 1240s. Llywelyn ap Gruffudd destroyed it in 1263, and when Edward I came he built Conwy Castle across the river instead and left Deganwy in ruins.",
   "Footpaths from the town lead up to the two summits, with some of the finest views in north Wales."],
  ["## Llys Maelgwn",
   "Mae dau fryn creigiog Degannwy, y Faerdre, yn edrych ar draws aber afon Conwy at dref Conwy. Yn ôl traddodiad Cymru y cadwai Maelgwn Gwynedd, brenin mawr y 500au, ei lys yma. Pan gloddiodd Leslie Alcock ar y bryn rhwng 1961 a 1966, cafodd ddarnau o grochenwaith a ddygwyd o fôr y Canoldir yn yr union oes honno, arwydd o lys brenhinol â chysylltiadau dros y moroedd.",
   "Yn chwedl Taliesin, daeth y bardd ifanc i lys Maelgwn yn Negannwy i ryddhau ei feistr Elffin, a thrwy ei gân gwnaeth bedwar bardd ar hugain Maelgwn yn fud.",
   "## Ymladd drosto am ganrifoedd",
   "Mae Annales Cambriae yn cofnodi dinistrio’r gaer ar ddechrau’r 800au. Cododd y Normaniaid gastell yma yn yr 1080au, cipiodd tywysogion Cymru ef yn ôl, a chododd Harri III gastell mawr newydd yn y 1240au. Dinistriodd Llywelyn ap Gruffudd ef yn 1263, a phan ddaeth Edward I cododd Gastell Conwy dros yr afon yn ei le a gadael Degannwy’n adfail.",
   "Mae llwybrau o’r dref yn arwain i fyny i’r ddau gopa, gyda rhai o’r golygfeydd gorau yng ngogledd Cymru."]),

 "dinasbran": (
  ["Castell Dinas Brân crowns a steep hill above Llangollen and the Dee. Around 600 BC the people of this land built a hillfort on the summit, with a bank and a deep ditch.",
   "In the 1260s Gruffudd ap Madog, prince of Powys Fadog, built a stone castle inside it, with a great hall, a keep and a gatehouse. In 1277, when Edward I’s army came, its Welsh defenders set it alight themselves rather than let it be taken whole.",
   "The castle is linked with the love of the poet Hywel ab Einion for Myfanwy Fychan of Dinas Brân in the 1300s. The story inspired Ceiriog’s poem Myfanwy Fychan and Joseph Parry’s song Myfanwy, still sung by male voice choirs across the world.",
   "Denbighshire County Council looks after the castle with Cadw’s help. It is open all year and free, but the paths up are steep and exposed, so wear good shoes."],
  ["Mae Castell Dinas Brân yn coroni bryn serth uwchben Llangollen ac afon Dyfrdwy. Tua 600 CC cododd pobl y wlad hon fryngaer ar y copa, gyda chlawdd a ffos ddofn.",
   "Yn y 1260au cododd Gruffudd ap Madog, tywysog Powys Fadog, gastell carreg y tu mewn iddi, gyda neuadd fawr, gorthwr a phorthdy. Yn 1277, pan ddaeth byddin Edward I, rhoddodd ei amddiffynwyr Cymreig ef ar dân eu hunain yn hytrach na’i adael yn gyfan i’r gelyn.",
   "Cysylltir y castell â chariad y bardd Hywel ab Einion at Fyfanwy Fychan o Ddinas Brân yn y 1300au. Ysbrydolodd y stori gerdd Ceiriog, Myfanwy Fychan, a chân Joseph Parry, Myfanwy, sy’n dal i gael ei chanu gan gorau meibion ar draws y byd.",
   "Cyngor Sir Ddinbych sy’n gofalu am y castell gyda help Cadw. Mae ar agor drwy’r flwyddyn ac am ddim, ond mae’r llwybrau i fyny’n serth ac yn agored, felly gwisgwch esgidiau da."]),

 "cwmhir": (
  ["Abbey Cwmhir lies in a quiet valley in the hills of Maelienydd, between Rhaeadr and Llandrindod. Cadwallon ap Madog, lord of Maelienydd, founded it for Cistercian monks in 1176. In the 1200s the monks began a church on the scale of a cathedral, with a nave of fourteen bays, as long as many a cathedral’s.",
   "After Llywelyn ap Gruffudd was killed beside the Irfon in December 1282, his body was buried by the Cistercians of Cwm Hir.[[cite:pl-dwb-llywelyn]] His head was taken to London. A slate slab laid in the ruins in modern times marks his resting place, and people still leave flowers there.",
   "The abbey suffered in the rising of Owain Glyndŵr from 1401 and was closed in 1536. Some of its arches were carried to Llanidloes, where they still stand in St Idloes’ church.",
   "The ruins are open to visit, free, in the grounds beside Abbey Cwmhir Hall and the village church."],
  ["Mae Abaty Cwm-hir mewn cwm tawel ym mryniau Maelienydd, rhwng Rhaeadr a Llandrindod. Sefydlodd Cadwallon ap Madog, arglwydd Maelienydd, ef i fynachod Sistersaidd yn 1176. Yn y 1200au dechreuodd y mynachod godi eglwys ar raddfa eglwys gadeiriol, gyda chorff o bedwar bae ar ddeg, cyhyd â chorff llawer eglwys gadeiriol.",
   "Wedi i Lywelyn ap Gruffudd gael ei ladd ger afon Irfon ym mis Rhagfyr 1282, claddwyd ei gorff gan Sistersiaid Cwm Hir.[[cite:pl-dwb-llywelyn]] Aed â’i ben i Lundain. Mae llechen a osodwyd yn yr adfeilion yn ein hoes ni yn nodi ei orweddfan, ac mae pobl yn dal i adael blodau yno.",
   "Dioddefodd yr abaty yng ngwrthryfel Owain Glyndŵr o 1401 ymlaen, a chaewyd ef yn 1536. Cludwyd rhai o’i fwâu i Lanidloes, lle maent yn dal i sefyll yn eglwys Idloes.",
   "Mae’r adfeilion ar agor i ymwelwyr, am ddim, yn y tir ger Neuadd Abaty Cwm-hir ac eglwys y pentref."]),

 "powis": (
  ["Powis Castle stands on a rock above Welshpool, built of the red stone that gave it its Welsh name, Castell Coch. It was raised in the 1200s by the princes of Powys Wenwynwyn, the southern half of the old kingdom of Powys, whose line went back to Bleddyn ap Cynfyn.",
   "Unlike almost every other castle of the Welsh princes, it never fell to ruin. The princes’ heirs, and after them the Herbert family, lived in it without a break, and turned it into a great house. In the late 1600s its famous terraced gardens were cut into the hillside below.",
   "The National Trust cares for the castle, its collections and gardens. It is ticketed; see the official page for times and prices."],
  ["Saif Castell Powys ar graig uwchben y Trallwng, wedi’i godi o’r garreg goch a roddodd iddo ei enw Cymraeg, Castell Coch. Fe’i codwyd yn y 1200au gan dywysogion Powys Wenwynwyn, hanner deheuol hen deyrnas Powys, y deuai eu llinach o Fleddyn ap Cynfyn.",
   "Yn wahanol i bron bob castell arall o eiddo tywysogion Cymru, ni aeth erioed yn adfail. Bu etifeddion y tywysogion, ac ar eu hôl teulu’r Herbertiaid, yn byw ynddo heb fwlch, gan ei droi’n blasty mawr. Ar ddiwedd y 1600au torrwyd ei erddi teras enwog i ochr y bryn islaw.",
   "Yr Ymddiriedolaeth Genedlaethol sy’n gofalu am y castell, ei gasgliadau a’i erddi. Rhaid prynu tocyn; gweler y dudalen swyddogol am amseroedd a phrisiau."]),

 "kidwelly": (
  ["## Gwenllian’s battle",
   "In 1136, while her husband Gruffudd ap Rhys was away in Gwynedd seeking help, Gwenllian, daughter of Gruffudd ap Cynan, led an army against Maurice de Londres, the Norman lord of Kidwelly. She fell in battle near the castle, at the place still called Maes Gwenllian. Her death stirred all Wales, and Welsh tradition holds that for years after, Welsh soldiers went into battle with the cry ‘Revenge for Gwenllian!’",
   "Her son, the Lord Rhys, took the castle in 1159.[[cite:pl-cadw-kidwelly]]",
   "## The castle",
   "Kidwelly began in the early 1100s as a Norman ringwork of earth and timber. By the 1280s the Chaworth brothers had built the stone castle within a castle that stands today, and later the great gatehouse was added. In the rising of Owain Glyndŵr his forces besieged it.[[cite:pl-cadw-kidwelly]]",
   "A memorial to Gwenllian stands near the castle. The castle is cared for by Cadw; see the official page for times and prices."],
  ["## Brwydr Gwenllian",
   "Yn 1136, tra oedd ei gŵr Gruffudd ap Rhys i ffwrdd yng Ngwynedd yn ceisio cymorth, arweiniodd Gwenllian, merch Gruffudd ap Cynan, fyddin yn erbyn Maurice de Londres, arglwydd Normanaidd Cydweli. Syrthiodd mewn brwydr ger y castell, yn y lle a elwir o hyd yn Faes Gwenllian. Cynhyrfodd ei marwolaeth Gymru gyfan, ac yn ôl traddodiad Cymru âi milwyr Cymru i’r frwydr am flynyddoedd wedyn gyda’r gri ‘Dial am Wenllian!’",
   "Cipiodd ei mab, yr Arglwydd Rhys, y castell yn 1159.[[cite:pl-cadw-kidwelly]]",
   "## Y castell",
   "Dechreuodd Cydweli ar ddechrau’r 1100au fel cylchfur Normanaidd o bridd a phren. Erbyn yr 1280au roedd y brodyr Chaworth wedi codi’r castell carreg o fewn castell sy’n sefyll heddiw, ac ychwanegwyd y porthdy mawr yn ddiweddarach. Yng ngwrthryfel Owain Glyndŵr gwarchaeodd ei luoedd arno.[[cite:pl-cadw-kidwelly]]",
   "Mae cofeb i Wenllian ger y castell. Cadw sy’n gofalu am y castell; gweler y dudalen swyddogol am amseroedd a phrisiau."]),

 "llanymddyfri": (
  ["## Llywelyn ap Gruffudd Fychan",
   "In 1401 Henry IV marched into the Tywi valley hunting Owain Glyndŵr. Llywelyn ap Gruffudd Fychan of Caeo, a landowner known for his open-handed household, agreed to guide the king’s army to Owain. Instead he led it for days through the hills of Deheubarth, while Owain got away to Gwynedd.",
   "When the trick was found out, Llywelyn was put to death before the castle gate at Llandovery on 9 October 1401, with the king looking on. Adam of Usk, who wrote at the time, said that he willingly chose death rather than betray his lord.[[cite:pl-adam-usk-caeo]]",
   "## The statue",
   "Six hundred years later, the people of Llandovery raised a memorial to him. Toby and Gideon Petersen’s figure, nearly five metres high, of empty armour and a cloak, stands on a stone base brought from Caeo, beside the castle mound.",
   "## The town",
   "Llandovery is also the town of Rhys Prichard, the Old Vicar, whose plain Welsh verses, Canwyll y Cymry, were read in homes across Wales for two hundred years. The castle mound is open to all, free, in the centre of the town."],
  ["## Llywelyn ap Gruffudd Fychan",
   "Yn 1401 gorymdeithiodd Harri IV i ddyffryn Tywi yn hela Owain Glyndŵr. Cytunodd Llywelyn ap Gruffudd Fychan o Gaeo, tirfeddiannwr a oedd yn adnabyddus am ei aelwyd hael, i dywys byddin y brenin at Owain. Yn hytrach, arweiniodd hi am ddyddiau drwy fryniau Deheubarth, tra dihangodd Owain i Wynedd.",
   "Pan ddaeth y tric i’r golwg, rhoddwyd Llywelyn i farwolaeth o flaen porth y castell yn Llanymddyfri ar 9 Hydref 1401, a’r brenin yn edrych arno. Dywedodd Adda o Frynbuga, a ysgrifennai ar y pryd, iddo ddewis marw o’i wirfodd yn hytrach na bradychu ei arglwydd.[[cite:pl-adam-usk-caeo]]",
   "## Y cerflun",
   "Chwe chan mlynedd yn ddiweddarach, cododd pobl Llanymddyfri gofeb iddo. Saif ffigwr Toby a Gideon Petersen, bron yn bum metr o uchder, o arfwisg wag a chlogyn, ar sylfaen o garreg a ddygwyd o Gaeo, ger tomen y castell.",
   "## Y dref",
   "Llanymddyfri hefyd yw tref Rhys Prichard, yr Hen Ficer, y bu ei benillion Cymraeg syml, Canwyll y Cymry, yn cael eu darllen ar aelwydydd ledled Cymru am ddau gan mlynedd. Mae tomen y castell ar agor i bawb, am ddim, yng nghanol y dref."]),

 "cilmeri": (
  ["## 11 December 1282",
   "Llywelyn ap Gruffudd, Prince of Wales, came south in the winter of 1282 to raise the men of Builth and the middle March. On 11 December, on the banks of the Irfon near here, he was killed by a soldier who did not know who he was.[[cite:pl-dwb-llywelyn]] His head was sent to Edward I and carried to London; his body was buried by the monks of Abbey Cwmhir.",
   "The poet Gruffudd ab yr Ynad Coch mourned him in one of the greatest poems in the Welsh language, asking whether the world itself was ending: ‘Poni welwch-chwi hynt y gwynt a’r glaw? Poni welwch-chwi’r deri’n ymdaraw?’ (Do you not see the rush of the wind and the rain? Do you not see the oaks beating together?)",
   "## The memorial",
   "The memorial stone, a block of granite from Trefor in Llŷn, was set up in 1956. Every December people gather here to remember Llywelyn, the last Welsh-born Prince of Wales. Nearby is a spring where, tradition says, his head was washed after his death.",
   "The memorial stands beside the main road at Cilmeri, open at all times and free."],
  ["## 11 Rhagfyr 1282",
   "Daeth Llywelyn ap Gruffudd, Tywysog Cymru, i’r de yn ystod gaeaf 1282 i godi gwŷr Buallt a chanol y Mers. Ar 11 Rhagfyr, ar lan afon Irfon gerllaw, lladdwyd ef gan filwr nad oedd yn gwybod pwy ydoedd.[[cite:pl-dwb-llywelyn]] Anfonwyd ei ben at Edward I a’i gludo i Lundain; claddwyd ei gorff gan fynachod Abaty Cwm-hir.",
   "Galarodd y bardd Gruffudd ab yr Ynad Coch amdano yn un o’r cerddi mwyaf yn yr iaith Gymraeg, gan ofyn ai diwedd y byd ei hun oedd hwn: ‘Poni welwch-chwi hynt y gwynt a’r glaw? Poni welwch-chwi’r deri’n ymdaraw?’",
   "## Y gofeb",
   "Codwyd y garreg goffa, bloc o wenithfaen o Drefor yn Llŷn, yn 1956. Bob mis Rhagfyr mae pobl yn ymgynnull yma i gofio Llywelyn, Tywysog Cymru olaf a aned yng Nghymru. Gerllaw mae ffynnon lle, yn ôl traddodiad, y golchwyd ei ben ar ôl ei farw.",
   "Saif y gofeb wrth ymyl y briffordd yng Nghilmeri, ar agor bob amser ac am ddim."]),

 "cardigan": (
  ["## The Lord Rhys’s castle",
   "Cardigan stands where the Teifi meets the sea. The Normans held a castle here from the 1090s, but in 1166 the Lord Rhys took it, and in 1171 he began a new castle in stone.[[cite:pl-dwb-rhys]]",
   "## The first eisteddfod",
   "At Christmas 1176 Rhys held a great festival at his castle, with contests for poets and for musicians, proclaimed a year ahead throughout Wales and beyond. The chair for poetry went to a poet of Gwynedd, and the prize for music to a young man of Rhys’s own court. It is the first eisteddfod on record.[[cite:pl-dwb-rhys]]",
   "## Saved",
   "Over the centuries the castle fell into ruin and was hidden behind a Regency house. After a long campaign by local people it was restored and reopened in 2015 as a heritage centre, with a festival field that honours the eisteddfod of 1176. It is run by a local trust; see the official page for times and prices."],
  ["## Castell yr Arglwydd Rhys",
   "Saif Aberteifi lle mae afon Teifi yn cwrdd â’r môr. Daliai’r Normaniaid gastell yma o’r 1090au, ond yn 1166 cipiodd yr Arglwydd Rhys ef, ac yn 1171 dechreuodd godi castell newydd o gerrig.[[cite:pl-dwb-rhys]]",
   "## Yr eisteddfod gyntaf",
   "Adeg y Nadolig 1176 cynhaliodd Rhys ŵyl fawr yn ei gastell, gyda chystadlaethau i feirdd ac i gerddorion, wedi’i chyhoeddi flwyddyn ymlaen llaw drwy Gymru a thu hwnt. Aeth cadair y beirdd i fardd o Wynedd, a gwobr y gerddoriaeth i ŵr ifanc o lys Rhys ei hun. Dyma’r eisteddfod gyntaf a gofnodwyd.[[cite:pl-dwb-rhys]]",
   "## Ei achub",
   "Dros y canrifoedd aeth y castell yn adfail a’i guddio y tu ôl i dŷ Rhaglywiaeth. Ar ôl ymgyrch hir gan bobl leol fe’i hadferwyd a’i ailagor yn 2015 fel canolfan dreftadaeth, gyda maes gŵyl sy’n anrhydeddu eisteddfod 1176. Ymddiriedolaeth leol sy’n ei redeg; gweler y dudalen swyddogol am amseroedd a phrisiau."]),
}


PEOPLE = {
 "dinefwr": ["rhodri-mawr", "hywel-dda", "rhys-ap-tewdwr", "nest", "yr-arglwydd-rhys", "gwenllian", "owain-glyndwr", "rhys-ap-thomas"],
 "aberffraw": ["rhodri-mawr", "anarawd", "gruffudd-ap-cynan", "owain-gwynedd", "llywelyn-fawr", "llywelyn-ap-gruffudd"],
 "mathrafal": ["rhodri-mawr", "bleddyn-ap-cynfyn", "owain-cyfeiliog", "cynddelw", "llywelyn-fawr"],
 "garthcelyn": ["llywelyn-fawr", "siwan", "llywelyn-ap-gruffudd", "gwenllian-ferch-llywelyn", "dafydd-ap-gruffudd"],
 "llysrhosyr": ["llywelyn-fawr", "llywelyn-ap-gruffudd"],
 "dolbadarn": ["llywelyn-fawr", "llywelyn-ap-gruffudd", "dafydd-ap-gruffudd"],
 "ybere": ["llywelyn-fawr", "llywelyn-ap-gruffudd", "dafydd-ap-gruffudd", "mary-jones"],
 "dolwyddelan": ["llywelyn-fawr", "llywelyn-ap-gruffudd"],
 "dinasemrys": ["emrys-wledig", "myrddin", "nennius"],
 "cricieth": ["llywelyn-fawr", "llywelyn-ap-gruffudd", "owain-glyndwr", "lloyd-george"],
 "dolforwyn": ["llywelyn-ap-gruffudd"],
 "dryslwyn": ["yr-arglwydd-rhys"],
 "carregcennen": ["owain-glyndwr"],
 "ewloe": ["owain-gwynedd", "llywelyn-fawr", "llywelyn-ap-gruffudd"],
 "deganwy": ["maelgwn-gwynedd", "taliesin", "llywelyn-ap-gruffudd"],
 "dinasbran": ["joseph-parry"],
 "cwmhir": ["llywelyn-ap-gruffudd", "owain-glyndwr"],
 "powis": ["bleddyn-ap-cynfyn", "owain-cyfeiliog"],
 "kidwelly": ["gwenllian", "gruffudd-ap-cynan", "yr-arglwydd-rhys", "owain-glyndwr"],
 "llanymddyfri": ["owain-glyndwr", "rhys-prichard"],
 "cilmeri": ["llywelyn-ap-gruffudd", "dafydd-ap-gruffudd", "gwenllian-ferch-llywelyn"],
 "cardigan": ["yr-arglwydd-rhys"],
 "sycharth": ["owain-glyndwr", "iolo-goch"],
 "machynlleth": ["owain-glyndwr"],
}


LINKS = {
 "dinasemrys": [("legend-dragons.html", "The red and the white dragon", "Y ddraig goch a’r ddraig wen")],
 "aberffraw": [("legend-branwen.html", "Branwen daughter of Llŷr", "Branwen ferch Llŷr"), ("laws.html", "The Laws of Hywel Dda", "Cyfreithiau Hywel Dda")],
 "llysrhosyr": [("llys-rhosyr.html", "Walk through Llys Rhosyr in 3D", "Cerdded drwy Lys Rhosyr mewn 3D")],
 "deganwy": [("legend-taliesin.html", "The tale of Taliesin", "Hanes Taliesin")],
 "dinefwr": [("laws.html", "The Laws of Hywel Dda", "Cyfreithiau Hywel Dda")],
}


# Sources beside the claims (merged into cites.S). Every one of these was opened and read when the text was written.
def _cadw(key, name_en, name_cy, slug, note_en, note_cy):
    return key, dict(short=("Cadw", "Cadw"), t=name_en, by=("Cadw, the Welsh Government’s historic environment service", "Cadw, gwasanaeth amgylchedd hanesyddol Llywodraeth Cymru"),
                     note=(note_en, note_cy), url="https://cadw.gov.wales/visit/places-to-visit/" + slug)


CITES = dict([
 _cadw("pl-cadw-dinefwr", "Castell Dinefwr", "Castell Dinefwr", "castell-dinefwr",
       "Cadw’s page on the castle: seat of Deheubarth, held by the Lord Rhys, a rare period of peace with a flowering of Welsh culture, music and poetry; in English hands from 1287; Glyndŵr’s attempt to win it back in 1403.",
       "Tudalen Cadw am y castell: llys Deheubarth, yn nwylo’r Arglwydd Rhys, cyfnod prin o heddwch pan flodeuodd diwylliant, cerddoriaeth a barddoniaeth Gymraeg; yn nwylo’r Saeson o 1287; ymgais Glyndŵr i’w ennill yn ôl yn 1403."),
 _cadw("pl-cadw-dolwyddelan", "Castell Dolwyddelan", "Castell Dolwyddelan", "castell-dolwyddelan",
       "Cadw’s page: a lasting memorial to Llywelyn the Great, ruler of Gwynedd from 1201 to 1240; taken by Edward I in 1283; the keep restored in the 1800s by Lord Willoughby de Eresby.",
       "Tudalen Cadw: cofeb barhaol i Lywelyn Fawr, rheolwr Gwynedd o 1201 hyd 1240; cipiwyd gan Edward I yn 1283; adferwyd y gorthwr yn y 1800au gan yr Arglwydd Willoughby de Eresby."),
 _cadw("pl-cadw-dolbadarn", "Castell Dolbadarn", "Castell Dolbadarn", "castell-dolbadarn",
       "Cadw’s page: most likely built by Llywelyn the Great; guarded the route inland from Caernarfon to the upper Conwy valley; its 15-metre round tower probably inspired by castles in the southern March.",
       "Tudalen Cadw: Llywelyn Fawr a’i cododd yn ôl pob tebyg; gwarchodai’r ffordd o Gaernarfon i ddyffryn Conwy uchaf; ei dŵr crwn 15 metr wedi’i ysbrydoli, mae’n debyg, gan gestyll y Mers deheuol."),
 _cadw("pl-cadw-ybere", "Castell y Bere", "Castell y Bere", "castell-y-bere",
       "Cadw’s page: begun by Llywelyn the Great in 1221 to protect Gwynedd’s southern frontier; its double gatehouse entrance extremely advanced for its time.",
       "Tudalen Cadw: dechreuwyd gan Lywelyn Fawr yn 1221 i warchod ffin ddeheuol Gwynedd; ei fynedfa drwy ddau borthdy yn hynod ddatblygedig yn ei ddydd."),
 _cadw("pl-cadw-cricieth", "Castell Cricieth", "Castell Cricieth", "castell-cricieth",
       "Cadw’s page: Llywelyn the Great built the gatehouse; Llywelyn ap Gruffudd added the outer ward, walls and two towers; in 1404 Owain Glyndŵr burned its towers and the town became entirely Welsh once more.",
       "Tudalen Cadw: Llywelyn Fawr a gododd y porthdy; ychwanegodd Llywelyn ap Gruffudd y ward allanol, y muriau a dau dŵr; yn 1404 llosgodd Owain Glyndŵr ei dyrau a daeth y dref yn gwbl Gymreig unwaith eto."),
 _cadw("pl-cadw-dolforwyn", "Castell Dolforwyn", "Castell Dolforwyn", "castell-dolforwyn",
       "Cadw’s page: built by Llywelyn ap Gruffudd in 1273; Edward I wrote forbidding him to continue and Llywelyn replied that he did not need the king’s permission to build on his own land; taken by Roger Mortimer in 1277 after a two-week siege.",
       "Tudalen Cadw: codwyd gan Lywelyn ap Gruffudd yn 1273; ysgrifennodd Edward I i’w wahardd ac atebodd Llywelyn nad oedd angen caniatâd y brenin arno i adeiladu ar ei dir ei hun; cipiwyd gan Roger Mortimer yn 1277 ar ôl gwarchae o bythefnos."),
 _cadw("pl-cadw-dryslwyn", "Castell Dryslwyn", "Castell Dryslwyn", "castell-dryslwyn",
       "Cadw’s page: founded in the 1200s, an important seat of Deheubarth; in 1287, after the rising of Rhys ap Maredudd, 11,000 English troops besieged it for two weeks.",
       "Tudalen Cadw: sefydlwyd yn y 1200au, un o lysoedd pwysig Deheubarth; yn 1287, wedi gwrthryfel Rhys ap Maredudd, bu 11,000 o filwyr Lloegr yn gwarchae arno am bythefnos."),
 _cadw("pl-cadw-carregcennen", "Castell Carreg Cennen", "Castell Carreg Cennen", "castell-carreg-cennen",
       "Cadw’s page: probably built by Edward I’s baron John Giffard at the end of the 1200s; voted the most romantic ruin in Wales; jointly managed with the farm.",
       "Tudalen Cadw: John Giffard, un o farwniaid Edward I, a’i cododd ar ddiwedd y 1200au yn ôl pob tebyg; pleidleisiwyd mai dyma’r adfail mwyaf rhamantus yng Nghymru; yn cael ei reoli ar y cyd â’r fferm."),
 _cadw("pl-cadw-ewloe", "Castell Ewloe", "Castell Ewloe", "castell-ewloe",
       "Cadw’s page: the D-shaped tower probably built by Llywelyn the Great some time after 1210; walls and western tower added by Llywelyn ap Gruffudd nearly 60 years later; a woodland hollow in contested borderland.",
       "Tudalen Cadw: Llywelyn Fawr a gododd y tŵr siâp D rywbryd ar ôl 1210 yn ôl pob tebyg; ychwanegodd Llywelyn ap Gruffudd y muriau a’r tŵr gorllewinol bron i 60 mlynedd yn ddiweddarach; pant coediog mewn gororau y bu ymladd drostynt."),
 _cadw("pl-cadw-llysrhosyr", "Llys Rhosyr", "Llys Rhosyr", "llys-rhosyr",
       "Cadw’s page: an important court of the princes of Gwynedd, the only one with visible remains open to the public, and the only undefended llys confirmed by excavation.",
       "Tudalen Cadw: un o lysoedd pwysig tywysogion Gwynedd, yr unig un ag olion gweladwy sydd ar agor i’r cyhoedd, a’r unig lys diamddiffyn a gadarnhawyd drwy gloddio."),
 _cadw("pl-cadw-kidwelly", "Kidwelly Castle", "Castell Cydweli", "kidwelly-castle",
       "Cadw’s page: a Norman ringwork of the early 1100s; captured by the Lord Rhys in 1159; the stone castle built by the Chaworth brothers by the 1280s; Owain Glyndŵr’s forces could not break through.",
       "Tudalen Cadw: cylchfur Normanaidd o ddechrau’r 1100au; cipiwyd gan yr Arglwydd Rhys yn 1159; y castell carreg wedi’i godi gan y brodyr Chaworth erbyn yr 1280au; ni allodd lluoedd Owain Glyndŵr dorri drwodd."),
 ("pl-gerald-seats", dict(short=("Gerald of Wales", "Gerallt Gymro"), t="The Description of Wales, Book I, chapter 4",
       by=("Gerald of Wales (Giraldus Cambrensis), 1194; translated by Sir Richard Colt Hoare, on A Vision of Britain Through Time", "Gerallt Gymro, 1194; cyfieithiad Saesneg Syr Richard Colt Hoare, ar A Vision of Britain Through Time"),
       note=("“There were three royal seats ... Dinevor, in South Wales, removed from Caerleon; Aberfraw, in North Wales; and Pengwern, in Powys.”",
             "“Roedd tri llys brenhinol ... Dinefwr, yn Ne Cymru, a symudwyd o Gaerllion; Aberffraw, yng Ngogledd Cymru; a Phengwern, ym Mhowys.”"),
       url="https://visionofbritain.org.uk/travellers/Cambrensis_Desc/6", lang="en")),
 ("pl-dwb-rhys", dict(short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"), t="Rhys ap Gruffydd (1132–1197), ‘Yr Arglwydd Rhys’",
       by=("Thomas Jones Pierce, Dictionary of Welsh Biography, National Library of Wales", "Thomas Jones Pierce, Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
       note=("Sole ruler of Deheubarth from 1155; at Dinefwr, the ancient capital, a castle in the new style was begun; the eisteddfod of 1176 at Cardigan; Strata Florida virtually his creation and Talley his own foundation; died 28 April 1197.",
             "Unig reolwr Deheubarth o 1155; yn Ninefwr, yr hen brifddinas, dechreuwyd castell yn y dull newydd; eisteddfod 1176 yn Aberteifi; Ystrad Fflur bron yn greadigaeth iddo a Thalyllychau yn sefydliad iddo’i hun; bu farw 28 Ebrill 1197."),
       url="https://biography.wales/article/s-RHYS-APG-1132", url_cy="https://bywgraffiadur.cymru/article/s-RHYS-APG-1132")),
 ("pl-dwb-llywelyn", dict(short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"), t="Llywelyn ap Gruffydd (‘Llywelyn the Last’), Prince of Wales (died 1282)",
       by=("Thomas Jones Pierce, Dictionary of Welsh Biography, National Library of Wales", "Thomas Jones Pierce, Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
       note=("Recognised as Prince of Wales in the peace of Montgomery (1267); built Dolforwyn and founded the borough of Abermule; killed on the banks of the Irfon on 11 December 1282 and buried by the Cistercians of Cwm Hir.",
             "Cydnabuwyd yn Dywysog Cymru yng nghytundeb Trefaldwyn (1267); cododd Ddolforwyn a sefydlu bwrdeistref Aber-miwl; lladdwyd ar lan Irfon ar 11 Rhagfyr 1282 a’i gladdu gan Sistersiaid Cwm Hir."),
       url="https://biography.wales/article/s-LLYW-APG-1200", url_cy="https://bywgraffiadur.cymru/article/s-LLYW-APG-1200")),
 ("pl-dwb-eleanor", dict(short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"), t="Eleanor de Montfort (c. 1258–1282), princess and diplomat",
       by=("Danna R. Messer, Dictionary of Welsh Biography, National Library of Wales", "Danna R. Messer, Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
       note=("Eleanor died in childbirth on 19 June 1282 and was buried at the Franciscan friary of Llan-faes; her daughter was Gwenllian.",
             "Bu farw Elinor wrth eni plentyn ar 19 Mehefin 1282 a’i chladdu ym mrodordy’r Ffransisiaid yn Llan-faes; ei merch oedd Gwenllian."),
       url="https://biography.wales/article/s11-ELEA-WRL-1200", url_cy="https://bywgraffiadur.cymru/article/s11-ELEA-WRL-1200")),
 ("pl-nt-dinefwr", dict(short=("National Trust", "Yr Ymddiriedolaeth Genedlaethol"), t="Dinefwr", by=("National Trust", "Yr Ymddiriedolaeth Genedlaethol"),
       note=("The National Trust’s page for Dinefwr park and Newton House, which says the castle is cared for by Cadw.",
             "Tudalen yr Ymddiriedolaeth Genedlaethol am barc Dinefwr a Thŷ Newton, sy’n dweud mai Cadw sy’n gofalu am y castell."),
       url="https://www.nationaltrust.org.uk/visit/wales/dinefwr", lang="en")),
 ("pl-nt-dinasemrys", dict(short=("National Trust", "Yr Ymddiriedolaeth Genedlaethol"), t="Discover the legend of two dragons",
       by=("National Trust, Craflwyn and Beddgelert", "Yr Ymddiriedolaeth Genedlaethol, Craflwyn a Beddgelert"),
       note=("The story of the red and white dragons at Dinas Emrys, the red dragon celebrated ever since, and the excavation that found a pool and the ruins of a fortress rebuilt several times.",
             "Stori’r ddraig goch a’r ddraig wen yn Ninas Emrys, y ddraig goch a ddathlwyd byth ers hynny, a’r cloddio a gafodd lyn ac adfeilion caer a ailgodwyd sawl gwaith."),
       url="https://www.nationaltrust.org.uk/visit/wales/craflwyn-and-beddgelert/discover-the-legend-of-two-dragons", lang="en")),
])

CITES["pl-historia-brittonum"] = dict(short=("Historia Brittonum", "Historia Brittonum"), t="History of the Britons (Historia Brittonum), chapters 40–42",
    by=("translated by J. A. Giles, Project Gutenberg", "cyfieithiad Saesneg J. A. Giles, Project Gutenberg"),
    note=("The History of the Britons, gathered in Gwynedd about 829: Vortigern’s fortress in Snowdonia, the boy Ambrosius, the pool and the red and white dragons.",
          "Hanes y Brytaniaid, a gasglwyd yng Ngwynedd tua 829: caer Gwrtheyrn yn Eryri, y bachgen Emrys, y llyn a’r ddraig goch a’r ddraig wen."),
    url="https://www.gutenberg.org/ebooks/1972", lang="en")
CITES["pl-adam-usk-caeo"] = dict(short=("Adam of Usk", "Adda o Frynbuga"), t="Chronicon Adae de Usk, A.D. 1377–1421",
    by=("Edward Maunde Thompson (ed. and trans.), London, 1904", "Edward Maunde Thompson (gol. a chyf.), Llundain, 1904"),
    note=("Adam of Usk, writing at the time, tells of Llywelyn ap Gruffudd Fychan of Caeo, put to death at Llandovery in 1401, who willingly preferred death to treachery.",
          "Mae Adda o Frynbuga, a ysgrifennai ar y pryd, yn adrodd hanes Llywelyn ap Gruffudd Fychan o Gaeo, a roddwyd i farwolaeth yn Llanymddyfri yn 1401, ac a ddewisodd farw o’i wirfodd yn hytrach na bradychu."),
    url="https://archive.org/details/chroniconadaedeu00adamuoft", lang="en")

import cites as _CITES  # noqa: E402
for _k in CITES:
    if _k in _CITES.S and _CITES.S[_k] is not CITES[_k]:
        raise SystemExit(f"src/places3.py: source key {_k} is already used in src/cites.py")
_CITES.S.update(CITES)
