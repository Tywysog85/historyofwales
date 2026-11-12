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



# ======================================================================================================
# Batch 2: saints, abbeys and holy places
# ======================================================================================================
NEW += [
 P("vallecrucis", "Valle Crucis Abbey", "Abaty Glyn y Groes", "medieval", 52.985, -3.187, "1201", "cross", "Valle_Crucis_Abbey",
   "The Cistercian abbey of the princes of northern Powys, founded in 1201 near Llangollen and named after the Pillar of Eliseg. Poets praised its feasts, and Guto’r Glyn spent his last years here.",
   "Abaty Sistersaidd tywysogion gogledd Powys, a sefydlwyd yn 1201 ger Llangollen ac a enwyd ar ôl Colofn Eliseg. Canmolai’r beirdd ei wleddoedd, a threuliodd Guto’r Glyn ei flynyddoedd olaf yma."),
 P("penmon", "Penmon Priory and St Seiriol’s Well", "Priordy Penmon a Ffynnon Seiriol", "saints", 53.305, -4.056, "6th century", "cross", "Penmon_Priory",
   "Saint Seiriol founded a monastery here at the eastern tip of Ynys Môn in the 500s. His holy well, a carved cross of the 900s and a church of the 1100s still stand.",
   "Sefydlodd Seiriol Sant fynachlog yma ym mhen dwyreiniol Ynys Môn yn y 500au. Mae ei ffynnon sanctaidd, croes gerfiedig o’r 900au ac eglwys o’r 1100au yn dal i sefyll."),
 P("talley", "Talley Abbey", "Abaty Talyllychau", "medieval", 51.977, -3.990, "1180s", "cross", "Talley_Abbey",
   "The abbey founded by the Lord Rhys in the 1180s between two lakes north of Llandeilo, the only house of the White Canons in Wales.",
   "Yr abaty a sefydlodd yr Arglwydd Rhys yn yr 1180au rhwng dau lyn i’r gogledd o Landeilo, yr unig dŷ o’r Canoniaid Gwyn yng Nghymru."),
 P("basingwerk", "Basingwerk Abbey", "Abaty Dinas Basing", "medieval", 53.287, -3.209, "1131", "cross", "Basingwerk_Abbey",
   "A Cistercian abbey near Holywell, founded in 1131, which cared for the pilgrims to St Winefride’s Well. Today it is the start of the North Wales Pilgrim’s Way to Enlli.",
   "Abaty Sistersaidd ger Treffynnon, a sefydlwyd yn 1131, a ofalai am y pererinion at Ffynnon Gwenffrewi. Heddiw dyma fan cychwyn Llwybr Pererinion Gogledd Cymru i Enlli."),
 P("margam", "Margam Stones", "Meini Margam", "kings", 51.563, -3.728, "500s–900s", "cross", "Margam_Stones_Museum",
   "Nearly thirty carved stones and crosses from the first Christian centuries of Glamorgan, gathered in an old school beside Margam Abbey church.",
   "Bron i ddeg ar hugain o feini a chroesau cerfiedig o ganrifoedd Cristnogol cyntaf Morgannwg, wedi’u casglu mewn hen ysgol wrth ymyl eglwys Abaty Margam."),
 P("stnons", "St Non’s Chapel", "Capel Non", "saints", 51.873, -5.268, "6th century", "cross", "St_Non%27s_Chapel",
   "On the clifftop south of St Davids, the place where, Welsh tradition holds, Non gave birth to Dewi during a great storm. Her holy well still flows beside the path.",
   "Ar ben y clogwyn i’r de o Dyddewi, y lle y ganed Dewi i Non, yn ôl traddodiad Cymru, yn ystod storm fawr. Mae ei ffynnon sanctaidd yn dal i lifo wrth ymyl y llwybr."),
 P("caergybi", "Caer Gybi, Holyhead", "Caer Gybi", "roman", 53.311, -4.633, "200s", "arches", "Caer_Gybi_(fort)",
   "A Roman fort by the harbour at Holyhead, with walls still four metres high. Welsh tradition holds that Maelgwn Gwynedd gave it to Saint Cybi, whose church stands inside it.",
   "Caer Rufeinig ger yr harbwr yng Nghaergybi, a’i muriau’n dal yn bedwar metr o uchder. Yn ôl traddodiad Cymru rhoddodd Maelgwn Gwynedd hi i Gybi Sant, y mae ei eglwys yn sefyll y tu mewn iddi."),
 P("neathabbey", "Neath Abbey", "Abaty Nedd", "medieval", 51.661, -3.826, "1130", "cross", "Neath_Abbey",
   "One of the richest abbeys in Wales, praised by Lewys Morgannwg as the fairest in the land. Its ruins are among the finest monastic remains in south Wales.",
   "Un o abatai cyfoethocaf Cymru, a ganmolwyd gan Lewys Morgannwg fel y tecaf yn y wlad. Mae ei adfeilion ymhlith olion mynachaidd gorau de Cymru."),
 P("llanthony", "Llanthony Priory", "Priordy Llanddewi Nant Hodni", "medieval", 51.945, -3.036, "1118", "cross", "Llanthony_Priory",
   "A priory in the Vale of Ewyas in the Black Mountains, begun at a hermit’s chapel of Saint David. Gerald of Wales called it truly suited to the monastic life.",
   "Priordy yn Nyffryn Ewias yn y Mynyddoedd Duon, a ddechreuodd mewn capel meudwy i Ddewi Sant. Dywedodd Gerallt Gymro ei fod yn wir addas i’r bywyd mynachaidd."),
 P("cymer", "Cymer Abbey", "Abaty Cymer", "medieval", 52.757, -3.885, "1198", "cross", "Cymer_Abbey",
   "A small Cistercian abbey near Dolgellau where the Mawddach meets the Wnion, founded in 1198 under the princes of Gwynedd.",
   "Abaty Sistersaidd bychan ger Dolgellau lle mae afon Mawddach yn cwrdd ag afon Wnion, a sefydlwyd yn 1198 dan dywysogion Gwynedd."),
 P("nanhyfer", "Nevern", "Nanhyfer", "saints", 52.025, -4.795, "6th century", "cross", "Nevern",
   "Saint Brynach’s church in a wooded valley in Pembrokeshire, with one of the finest carved crosses in Wales, stones inscribed in Latin and ogham, and a ‘bleeding’ yew.",
   "Eglwys Brynach Sant mewn cwm coediog yn Sir Benfro, gydag un o’r croesau cerfiedig gorau yng Nghymru, meini ag arysgrifau Lladin ac ogam, ac ywen sy’n ‘gwaedu’."),
 P("clynnog", "Clynnog Fawr", "Clynnog Fawr", "saints", 53.022, -4.366, "7th century", "cross", "St_Beuno%27s_Church,_Clynnog_Fawr",
   "The great church of Saint Beuno on the coast of Arfon, where pilgrims on their way to Enlli stopped to pray at his grave.",
   "Eglwys fawr Beuno Sant ar arfordir Arfon, lle arhosai pererinion ar eu ffordd i Enlli i weddïo wrth ei fedd."),
 P("pennantmelangell", "Pennant Melangell", "Pennant Melangell", "saints", 52.825, -3.451, "c. 600", "cross", "Pennant_Melangell",
   "The church at the head of a valley in the Berwyn where Melangell sheltered a hare from the hounds of Brochwel Ysgithrog. Her shrine of the 1100s is the oldest of its kind in northern Europe.",
   "Yr eglwys ym mhen cwm yn y Berwyn lle cysgododd Melangell ysgyfarnog rhag cŵn Brochwel Ysgithrog. Ei chysegrfa o’r 1100au yw’r hynaf o’i bath yng ngogledd Ewrop."),
 P("llanddewibrefi", "Llanddewi Brefi", "Llanddewi Brefi", "saints", 52.180, -3.957, "c. 545", "cross", "Llanddewi_Brefi",
   "Here, Welsh tradition holds, the ground rose beneath Dewi Sant as he preached to the great synod of Brefi, so that all could see and hear him.",
   "Yma, yn ôl traddodiad Cymru, cododd y tir dan draed Dewi Sant wrth iddo bregethu i synod fawr Brefi, fel y gallai pawb ei weld a’i glywed."),
 P("llancarfan", "Llancarfan", "Llancarfan", "saints", 51.430, -3.358, "6th century", "cross", "Llancarfan",
   "Saint Cadog’s monastery in the Vale of Glamorgan, famed for its learning. Its church hides some of the finest medieval wall paintings in Wales.",
   "Mynachlog Cadog Sant ym Mro Morgannwg, a oedd yn enwog am ei dysg. Mae ei heglwys yn cuddio rhai o’r paentiadau wal canoloesol gorau yng Nghymru."),
 P("llanbadarn", "Llanbadarn Fawr", "Llanbadarn Fawr", "saints", 52.408, -4.065, "6th century", "cross", "St_Padarn%27s_Church,_Llanbadarn_Fawr",
   "Saint Padarn’s church above Aberystwyth, one of the leading centres of learning of early Wales, where Sulien and his sons wrote and copied books in the 1000s.",
   "Eglwys Padarn Sant uwchben Aberystwyth, un o brif ganolfannau dysg Cymru gynnar, lle bu Sulien a’i feibion yn ysgrifennu a chopïo llyfrau yn yr 1000au."),
 P("bangor", "Bangor Cathedral", "Eglwys Gadeiriol Bangor", "saints", 53.227, -4.129, "c. 530", "cross", "Bangor_Cathedral",
   "Founded by Saint Deiniol about 530 on land given by Maelgwn Gwynedd, and the burial place of Gruffudd ap Cynan and Owain Gwynedd.",
   "Sefydlwyd gan Ddeiniol Sant tua 530 ar dir a roddwyd gan Faelgwn Gwynedd, a dyma fan claddu Gruffudd ap Cynan ac Owain Gwynedd."),
 P("llandaf", "Llandaff Cathedral", "Eglwys Gadeiriol Llandaf", "saints", 51.495, -3.218, "6th century", "cross", "Llandaff_Cathedral",
   "The cathedral of the saints Dyfrig, Teilo and Euddogwy beside the Taf in Cardiff. Its Book of Llandaf traces the church back to King Lleurwg.",
   "Eglwys gadeiriol y saint Dyfrig, Teilo ac Euddogwy ger afon Taf yng Nghaerdydd. Mae ei Llyfr Llandaf yn olrhain yr eglwys yn ôl i’r Brenin Lleurwg."),
 P("llanelwy", "St Asaph Cathedral", "Eglwys Gadeiriol Llanelwy", "saints", 53.257, -3.442, "6th century", "cross", "St_Asaph_Cathedral",
   "The smallest ancient cathedral in Britain, founded by Saint Cyndeyrn, where Bishop William Morgan, who gave Wales the Bible in Welsh, is remembered.",
   "Yr eglwys gadeiriol hynafol leiaf ym Mhrydain, a sefydlwyd gan Gyndeyrn Sant, lle cofir yr Esgob William Morgan, a roddodd y Beibl yn Gymraeg i Gymru."),
 P("carewcross", "Carew Cross", "Croes Caeriw", "kings", 51.698, -4.828, "c. 1035", "cross", "Carew_Cross",
   "A tall carved cross of the 1000s raised for Maredudd ab Edwin, king of Deheubarth and descendant of Hywel Dda, who fell in battle in 1035.",
   "Croes gerfiedig dal o’r 1000au a godwyd er cof am Faredudd ab Edwin, brenin Deheubarth a disgynnydd Hywel Dda, a syrthiodd mewn brwydr yn 1035."),
]

LONG.update({
 "strataflorida": (
  ["## The Westminster Abbey of Wales",
   "Strata Florida, Ystrad Fflur, the Vale of Flowers, has stood on the meadows beside the Teifi since 1184. Its white-robed Cistercian monks came under the protection of the Lord Rhys, and the abbey soon became the most famous church in Wales after St Davids.[[cite:pl-cadw-strataflorida]] The Dictionary of Welsh Biography calls it virtually his creation.[[cite:pl-dwb-rhys]]",
   "Generations of the princes of Deheubarth were buried here, and the abbey has been called the Westminster Abbey of Wales.[[cite:pl-cadw-strataflorida]] In 1238 Llywelyn the Great called the princes of Wales to Strata Florida to swear loyalty to his son Dafydd, the first time all Wales was asked to recognise one heir.",
   "## Books and poets",
   "The monks kept a chronicle of Welsh history, and Strata Florida is linked with Brut y Tywysogion, the Chronicle of the Princes, and with the copying of Welsh books. Dafydd ap Gwilym, the greatest poet of medieval Wales, is said to be buried under a yew in the churchyard.[[cite:pl-cadw-strataflorida]]",
   "## Visiting",
   "The great west doorway still stands, and the floor tiles of the 1300s include the Man with the Mirror. Cadw cares for the ruins, and the farmhouse next door, Mynachlog Fawr, is being restored by the Strata Florida Trust."],
  ["## Abaty Westminster Cymru",
   "Mae Ystrad Fflur, Strata Florida, Dyffryn y Blodau, wedi sefyll ar y dolydd ger afon Teifi ers 1184. Daeth ei fynachod Sistersaidd mewn gwisg wen dan nawdd yr Arglwydd Rhys, a buan y daeth yr abaty’n eglwys enwocaf Cymru ar ôl Tyddewi.[[cite:pl-cadw-strataflorida]] Mae’r Bywgraffiadur yn ei alw bron yn greadigaeth iddo.[[cite:pl-dwb-rhys]]",
   "Claddwyd cenedlaethau o dywysogion Deheubarth yma, a galwyd yr abaty’n Abaty Westminster Cymru.[[cite:pl-cadw-strataflorida]] Yn 1238 galwodd Llywelyn Fawr dywysogion Cymru i Ystrad Fflur i dyngu llw o ffyddlondeb i’w fab Dafydd, y tro cyntaf y gofynnwyd i Gymru gyfan gydnabod un etifedd.",
   "## Llyfrau a beirdd",
   "Cadwai’r mynachod gronicl o hanes Cymru, a chysylltir Ystrad Fflur â Brut y Tywysogion ac â chopïo llyfrau Cymraeg. Dywedir bod Dafydd ap Gwilym, bardd mwyaf Cymru’r Oesoedd Canol, wedi’i gladdu dan ywen yn y fynwent.[[cite:pl-cadw-strataflorida]]",
   "## Ymweld",
   "Mae’r drws gorllewinol mawr yn dal i sefyll, ac mae teils llawr y 1300au yn cynnwys y Dyn â’r Drych. Cadw sy’n gofalu am yr adfeilion, ac mae’r ffermdy drws nesaf, Mynachlog Fawr, yn cael ei adfer gan Ymddiriedolaeth Ystrad Fflur."]),

 "llanilltud": (
  ["## The oldest centre of learning in Britain",
   "Llanilltud Fawr, Llantwit Major, lies in a hollow near the coast of the Vale of Glamorgan. Here, around the year 500, Saint Illtud founded a monastery and school. Welsh tradition holds that Dewi Sant, Samson of Dol, Gildas and Paulinus all studied under him, and the Life of Samson, written within a century or so of his death, calls Illtud the most learned of all the Britons.",
   "From this school the saints went out to Wales, Cornwall and Brittany, and Llanilltud is counted the oldest centre of learning in Britain.",
   "## The stones of the kings",
   "In the Galilee Chapel at the west end of St Illtud’s Church stands a remarkable group of carved stones. One cross was raised by Hywel ap Rhys, king of Glywysing in the 800s, for the soul of his father Rhys; another bears the name of Samson. They show that this was a place where kings chose to be remembered.",
   "## Visiting",
   "St Illtud’s Church is open most days, and the stones are shown in the restored Galilee Chapel. The town keeps its medieval streets, and the coast path runs close by."],
  ["## Canolfan ddysg hynaf Prydain",
   "Mae Llanilltud Fawr mewn pant ger arfordir Bro Morgannwg. Yma, tua’r flwyddyn 500, sefydlodd Illtud Sant fynachlog ac ysgol. Yn ôl traddodiad Cymru astudiodd Dewi Sant, Samson o Dol, Gildas a Pheulin i gyd dano, ac mae Buchedd Samson, a ysgrifennwyd o fewn canrif neu ddwy i’w farw, yn galw Illtud y mwyaf dysgedig o’r holl Frythoniaid.",
   "O’r ysgol hon aeth y saint allan i Gymru, Cernyw a Llydaw, a chyfrifir Llanilltud yn ganolfan ddysg hynaf Prydain.",
   "## Meini’r brenhinoedd",
   "Yng Nghapel Galilea ym mhen gorllewinol Eglwys Illtud saif casgliad hynod o feini cerfiedig. Codwyd un groes gan Hywel ap Rhys, brenin Glywysing yn yr 800au, er enaid ei dad Rhys; mae enw Samson ar un arall. Maent yn dangos mai dyma le y dewisai brenhinoedd gael eu cofio.",
   "## Ymweld",
   "Mae Eglwys Illtud ar agor y rhan fwyaf o ddyddiau, a dangosir y meini yng Nghapel Galilea a adferwyd. Mae’r dref yn cadw ei strydoedd canoloesol, ac mae llwybr yr arfordir gerllaw."]),

 "enlli": (
  ["Ynys Enlli, Bardsey, lies two miles off the tip of Llŷn across a fierce tide race. Saint Cadfan is said to have founded a monastery here in the 500s, and Welsh tradition holds that twenty thousand saints are buried on the island.",
   "For centuries pilgrims walked the length of Llŷn to Aberdaron and crossed to Enlli. In the Middle Ages three pilgrimages to Enlli were counted equal to one to Rome. The ruined tower of the abbey of St Mary still stands near the island’s farmhouses.",
   "The island is cared for by the Bardsey Island Trust. Boats sail from Porth Meudwy near Aberdaron in good weather; you can go for the day or stay in one of the island’s cottages."],
  ["Mae Ynys Enlli ddwy filltir oddi ar ben Llŷn, dros swnt o lanw ffyrnig. Dywedir i Gadfan Sant sefydlu mynachlog yma yn y 500au, ac yn ôl traddodiad Cymru mae ugain mil o saint wedi’u claddu ar yr ynys.",
   "Am ganrifoedd cerddai pererinion hyd Llŷn i Aberdaron a chroesi i Enlli. Yn yr Oesoedd Canol cyfrifid tair pererindod i Enlli yn gyfwerth ag un i Rufain. Mae tŵr adfeiliedig abaty Santes Fair yn dal i sefyll ger ffermdai’r ynys.",
   "Ymddiriedolaeth Ynys Enlli sy’n gofalu am yr ynys. Mae cychod yn hwylio o Borth Meudwy ger Aberdaron pan fo’r tywydd yn deg; gallwch fynd am y dydd neu aros yn un o fythynnod yr ynys."]),

 "treffynnon": (
  ["The story is told that in the 600s Gwenffrewi (Winefride) was struck down by Caradog when she refused him, and where her head fell a spring burst from the ground. Her uncle Saint Beuno brought her back to life, and she lived on as an abbess at Gwytherin.",
   "The well has been a place of pilgrimage since at least 1115, and it is reputed to be the oldest continually visited pilgrim site in Britain.[[cite:pl-cadw-treffynnon]] The beautiful chapel over the spring was built in the late 1400s, and pilgrims still bathe in the pool.",
   "The chapel is in Cadw’s care; the well and its small museum are run by St Winefride’s Well shrine. Basingwerk Abbey, whose monks cared for the pilgrims, is a short walk down the valley."],
  ["Adroddir i Wenffrewi, yn y 600au, gael ei tharo i lawr gan Garadog pan wrthododd hi ef, ac yn y fan lle syrthiodd ei phen tarddodd ffynnon o’r ddaear. Adferodd ei hewythr Beuno Sant hi’n fyw, a bu fyw wedyn yn abades yng Ngwytherin.",
   "Bu’r ffynnon yn gyrchfan pererinion ers o leiaf 1115, a dywedir mai hi yw’r safle pererindod hynaf ym Mhrydain a gafodd ymwelwyr yn ddi-dor.[[cite:pl-cadw-treffynnon]] Codwyd y capel hardd dros y ffynnon ar ddiwedd y 1400au, ac mae pererinion yn dal i ymdrochi yn y pwll.",
   "Mae’r capel yng ngofal Cadw; cysegrfa Ffynnon Gwenffrewi sy’n rhedeg y ffynnon a’i hamgueddfa fach. Mae Abaty Dinas Basing, y gofalai ei fynachod am y pererinion, dro byr i lawr y cwm."]),

 "eliseg": (
  ["The Pillar of Eliseg stands on an ancient burial mound near Valle Crucis. It was put up in the first half of the 800s by Cyngen, king of Powys, in memory of his great-grandfather Elisedd, who drove the English out of this part of Wales.[[cite:pl-cadw-eliseg]]",
   "Its long Latin inscription, now worn away, was copied in 1696 by Edward Lhuyd. It named the kings of Powys and traced their line back to Gwrtheyrn and to Macsen Wledig. It used the language of law and was probably meant to be read aloud, perhaps at the place where the kings of Powys were made.[[cite:pl-cadw-eliseg]]",
   "Only the round lower shaft survives, but it gave its name to the valley and to the abbey: Valle Crucis, Glyn y Groes, the Valley of the Cross. Cadw cares for it, and it is free to visit."],
  ["Saif Colofn Eliseg ar hen domen gladdu ger Glyn y Groes. Fe’i codwyd yn hanner cyntaf yr 800au gan Gyngen, brenin Powys, er cof am ei hen daid Elisedd, a yrrodd y Saeson allan o’r rhan hon o Gymru.[[cite:pl-cadw-eliseg]]",
   "Copïwyd ei harysgrif Ladin hir, sydd wedi treulio erbyn hyn, yn 1696 gan Edward Lhuyd. Enwai frenhinoedd Powys gan olrhain eu llinach yn ôl i Wrtheyrn ac i Facsen Wledig. Defnyddiai iaith y gyfraith ac roedd i’w darllen yn uchel, mae’n debyg, efallai yn y fan lle gwneid brenhinoedd Powys.[[cite:pl-cadw-eliseg]]",
   "Dim ond rhan isaf grwn y golofn sydd ar ôl, ond rhoddodd ei henw i’r cwm ac i’r abaty: Valle Crucis, Glyn y Groes. Cadw sy’n gofalu amdani, ac mae am ddim i ymweld â hi."]),

 "maenachwyfan": (
  ["Maen Achwyfan stands in a field near Whitford in Flintshire: at nearly three and a half metres, the tallest wheel-headed cross in Britain. It probably dates from the late 900s and was raised in memory of a person or event now forgotten.[[cite:pl-cadw-maenachwyfan]]",
   "Its carving of knots and plaits shows the influence of the Norse seafarers who knew this coast, side by side with the Christian art of Wales.[[cite:pl-cadw-maenachwyfan]] It is free to visit, a short walk from the lane."],
  ["Saif Maen Achwyfan mewn cae ger Chwitffordd yn Sir y Fflint: bron yn dri metr a hanner o uchder, y groes olwyn dalaf ym Mhrydain. Mae’n dyddio o ddiwedd y 900au yn ôl pob tebyg, ac fe’i codwyd er cof am berson neu ddigwyddiad sydd wedi’i anghofio.[[cite:pl-cadw-maenachwyfan]]",
   "Mae ei cherfiadau o glymau a phlethau yn dangos dylanwad morwyr Llychlyn a adwaenai’r arfordir hwn, ochr yn ochr â chelfyddyd Gristnogol Cymru.[[cite:pl-cadw-maenachwyfan]] Mae am ddim i ymweld â hi, dro byr o’r lôn."]),

 "tintern": (
  ["Tintern was founded in 1131 by Cistercian monks, who made do with timber buildings at first. In 1269 they began the great abbey church whose walls still stand, one of the finest Gothic buildings in Britain.[[cite:pl-cadw-tintern]]",
   "The abbey surrendered in 1536, in the first round of the closing of the monasteries, and slowly became a ruin.[[cite:pl-cadw-tintern]] Two hundred years later it drew poets and painters to the Wye valley: Wordsworth wrote his Lines Composed a Few Miles above Tintern Abbey in 1798, and Turner painted it.",
   "Cadw cares for the abbey; see the official page for times and prices."],
  ["Sefydlwyd Tyndyrn yn 1131 gan fynachod Sistersaidd, a fodlonai ar adeiladau pren ar y dechrau. Yn 1269 dechreuasant godi’r eglwys abaty fawr y mae ei muriau’n dal i sefyll, un o adeiladau Gothig gorau Prydain.[[cite:pl-cadw-tintern]]",
   "Ildiodd yr abaty yn 1536, yn y don gyntaf o gau’r mynachlogydd, ac aeth yn adfail yn araf.[[cite:pl-cadw-tintern]] Ddau gan mlynedd yn ddiweddarach denodd feirdd ac arlunwyr i ddyffryn Gwy: ysgrifennodd Wordsworth ei gerdd Lines Composed a Few Miles above Tintern Abbey yn 1798, a pheintiodd Turner ef.",
   "Cadw sy’n gofalu am yr abaty; gweler y dudalen swyddogol am amseroedd a phrisiau."]),

 "vallecrucis": (
  ["Valle Crucis, Glyn y Groes, was founded in 1201 by Madog ap Gruffudd Maelor, prince of northern Powys, for Cistercian monks, and it was truly Welsh from the moment it was founded. Its name, the Valley of the Cross, comes from the Pillar of Eliseg up the road.[[cite:pl-cadw-vallecrucis]]",
   "Its monks had names like Tudur and Hywel, and the families of the rulers of northern Powys were buried in its church; the grave slab of Madog himself survives.[[cite:pl-cadw-vallecrucis]] The poets loved it. They praised feasts served on silver and ale that flowed like a river, and Guto’r Glyn, one of the greatest of them, spent his last years here as the guest of Abbot Dafydd ab Ieuan.",
   "When the abbey was closed in 1537, only Tintern in Wales was richer. It has the only surviving monastic fishpond in Wales.[[cite:pl-cadw-vallecrucis]] Cadw cares for it, and it is free to visit."],
  ["Sefydlwyd Glyn y Groes yn 1201 gan Fadog ap Gruffudd Maelor, tywysog gogledd Powys, i fynachod Sistersaidd, ac roedd yn wirioneddol Gymreig o’r dechrau. Daw ei enw, Valle Crucis, Glyn y Groes, o Golofn Eliseg i fyny’r ffordd.[[cite:pl-cadw-vallecrucis]]",
   "Roedd gan ei fynachod enwau fel Tudur a Hywel, a chladdwyd teuluoedd rheolwyr gogledd Powys yn ei eglwys; mae carreg fedd Madog ei hun wedi goroesi.[[cite:pl-cadw-vallecrucis]] Carai’r beirdd y lle. Canmolent wleddoedd ar lestri arian a chwrw’n llifo fel afon, a threuliodd Guto’r Glyn, un o’r mwyaf ohonynt, ei flynyddoedd olaf yma yn westai i’r Abad Dafydd ab Ieuan.",
   "Pan gaewyd yr abaty yn 1537, dim ond Tyndyrn yng Nghymru oedd yn gyfoethocach. Yma mae’r unig bysgodlyn mynachaidd sydd wedi goroesi yng Nghymru.[[cite:pl-cadw-vallecrucis]] Cadw sy’n gofalu amdano, ac mae am ddim i ymweld ag ef."]),

 "penmon": (
  ["At Penmon, on the eastern tip of Ynys Môn looking out to Ynys Seiriol, Saint Seiriol founded a monastery in the 500s. His holy well, with its healing waters, is thought to go back to his time, though the little building over it is much later.[[cite:pl-cadw-penmon]]",
   "Welsh tradition tells of Seiriol and his friend Cybi of Holyhead meeting each week in the middle of the island. Cybi walked east in the morning and west in the evening with the sun in his face, and was called Cybi Felyn, the tanned; Seiriol walked with the sun behind him and was Seiriol Wyn, the fair.",
   "The priory ruins date mostly from the 1200s, when it became a house of Augustinian canons. Inside the church stands the Penmon Cross of the 900s, carved with frets and plaits, and nearby is a great dovecote of the 1400s.[[cite:pl-cadw-penmon]] All are free to visit."],
  ["Ym Mhenmon, ym mhen dwyreiniol Ynys Môn yn edrych allan at Ynys Seiriol, sefydlodd Seiriol Sant fynachlog yn y 500au. Credir bod ei ffynnon sanctaidd, â’i dyfroedd iachusol, yn mynd yn ôl i’w amser ef, er bod yr adeilad bach drosti yn llawer diweddarach.[[cite:pl-cadw-penmon]]",
   "Mae traddodiad Cymru yn sôn am Seiriol a’i gyfaill Cybi o Gaergybi yn cwrdd bob wythnos yng nghanol yr ynys. Cerddai Cybi tua’r dwyrain yn y bore a thua’r gorllewin gyda’r hwyr a’r haul yn ei wyneb, a’i alw’n Gybi Felyn; cerddai Seiriol a’r haul y tu ôl iddo, a’i alw’n Seiriol Wyn.",
   "Mae adfeilion y priordy’n dyddio’n bennaf o’r 1200au, pan ddaeth yn dŷ i ganoniaid Awstinaidd. Y tu mewn i’r eglwys saif Croes Penmon o’r 900au, wedi’i cherfio â phlethau, a gerllaw mae colomendy mawr o’r 1400au.[[cite:pl-cadw-penmon]] Mae’r cyfan am ddim i ymweld ag ef."]),

 "talley": (
  ["Talley lies between two lakes in the hills north of Llandeilo; its Welsh name, Talyllychau, means the head of the lakes. The Lord Rhys founded the abbey in the 1180s for the White Canons, the Premonstratensians, and it was the first and only abbey of that order in Wales.[[cite:pl-cadw-talley]] The Dictionary of Welsh Biography calls it his special and unique foundation.[[cite:pl-dwb-rhys]]",
   "The money ran short and the church was never finished as planned, but one great wall of its tower stands almost to its full height, and the footings show how ambitious it was meant to be.[[cite:pl-cadw-talley]] Cadw cares for it, and it is free to visit."],
  ["Mae Talyllychau rhwng dau lyn yn y bryniau i’r gogledd o Landeilo; ystyr yr enw yw pen y llynnoedd. Sefydlodd yr Arglwydd Rhys yr abaty yn yr 1180au i’r Canoniaid Gwyn, y Premonstratensiaid, a dyma’r cyntaf a’r unig abaty o’r urdd honno yng Nghymru.[[cite:pl-cadw-talley]] Mae’r Bywgraffiadur yn ei alw’n sefydliad arbennig ac unigryw iddo.[[cite:pl-dwb-rhys]]",
   "Aeth yr arian yn brin ac ni orffennwyd yr eglwys fel y bwriadwyd, ond mae un mur mawr o’i thŵr yn sefyll bron i’w lawn uchder, ac mae’r sylfeini’n dangos mor uchelgeisiol y bwriadwyd iddi fod.[[cite:pl-cadw-talley]] Cadw sy’n gofalu amdano, ac mae am ddim i ymweld ag ef."]),

 "basingwerk": (
  ["Basingwerk Abbey stands at the foot of the Greenfield valley below Holywell. It was founded in 1131 and later joined the Cistercians, part of a network of their abbeys across Wales; it was remodelled in the 1200s.[[cite:pl-cadw-basingwerk]]",
   "Its monks cared for the pilgrims who came to St Winefride’s Well, and the Welsh poets praised the welcome of its abbots. The oldest part is the chapter house of the 1100s, and the finest room is the monks’ dining hall.[[cite:pl-cadw-basingwerk]]",
   "Today the abbey is the start of the North Wales Pilgrim’s Way, which runs 130 miles to Enlli, the island of twenty thousand saints.[[cite:pl-cadw-basingwerk]] It is free to visit, beside the Greenfield Valley Heritage Park."],
  ["Saif Abaty Dinas Basing wrth droed Dyffryn Maes-glas islaw Treffynnon. Fe’i sefydlwyd yn 1131 ac yn ddiweddarach ymunodd â’r Sistersiaid, yn rhan o rwydwaith o’u habatai ledled Cymru; fe’i hailwampiwyd yn y 1200au.[[cite:pl-cadw-basingwerk]]",
   "Gofalai ei fynachod am y pererinion a ddeuai i Ffynnon Gwenffrewi, a chanmolai beirdd Cymru groeso ei abadau. Y rhan hynaf yw’r cabidyldy o’r 1100au, a’r ystafell orau yw ffreutur y mynachod.[[cite:pl-cadw-basingwerk]]",
   "Heddiw yr abaty yw man cychwyn Llwybr Pererinion Gogledd Cymru, sy’n rhedeg 130 milltir i Enlli, ynys yr ugain mil o saint.[[cite:pl-cadw-basingwerk]] Mae am ddim i ymweld ag ef, wrth ymyl Parc Treftadaeth Dyffryn Maes-glas."]),

 "margam": (
  ["In an old school beside the church of Margam Abbey, Cadw keeps nearly thirty carved stones and crosses. Some date from the first days of Christianity in Wales in the 500s. Several began life as milestones on Roman roads, and were later carved again to remember the local rulers.[[cite:pl-cadw-margam]]",
   "The great disc-headed and wheel crosses of the 800s and 900s are among the finest in Wales, among them the Cross of Cynfelin with its hunting scene. Upstairs are carvings from Margam Abbey itself, including a knight of the 1300s with a small dragon at the foot of his shield.[[cite:pl-cadw-margam]]",
   "The museum opens on set days in summer only; check Cadw’s page before you go. Margam Country Park, with the abbey ruins and the orangery, is next door."],
  ["Mewn hen ysgol wrth ymyl eglwys Abaty Margam, mae Cadw yn cadw bron i ddeg ar hugain o feini a chroesau cerfiedig. Mae rhai’n dyddio o ddyddiau cyntaf Cristnogaeth yng Nghymru yn y 500au. Dechreuodd sawl un fel cerrig milltir ar ffyrdd Rhufeinig, a’u cerfio eto wedyn er cof am reolwyr lleol.[[cite:pl-cadw-margam]]",
   "Mae croesau olwyn a chroesau pen disg mawr yr 800au a’r 900au ymhlith y gorau yng Nghymru, yn eu plith Croes Cynfelin â’i golygfa hela. Ar y llawr uchaf mae cerfiadau o Abaty Margam ei hun, gan gynnwys marchog o’r 1300au gyda draig fach wrth droed ei darian.[[cite:pl-cadw-margam]]",
   "Dim ond ar ddyddiau penodol yn yr haf y mae’r amgueddfa ar agor; edrychwch ar dudalen Cadw cyn mynd. Mae Parc Gwledig Margam, gydag adfeilion yr abaty a’r orendy, drws nesaf."]),

 "stnons": (
  ["On the cliffs a short walk south of St Davids, the ruin of a small chapel stands in a field above the sea. It is named after Non, mother of Dewi Sant, and Welsh tradition holds that Dewi was born here in the 500s, during a great storm.[[cite:pl-cadw-stnons]]",
   "Its few walls are of uncertain date, but the place has drawn pilgrims ever since. Beside the path is Non’s holy well, believed to have healing powers.[[cite:pl-cadw-stnons]] A later chapel to Our Lady and St Non stands nearby. The ruin is cared for by Cadw and free to visit at any time."],
  ["Ar y clogwyni, dro byr i’r de o Dyddewi, saif adfail capel bach mewn cae uwchben y môr. Fe’i henwir ar ôl Non, mam Dewi Sant, ac yn ôl traddodiad Cymru ganed Dewi yma yn y 500au, yn ystod storm fawr.[[cite:pl-cadw-stnons]]",
   "Ansicr yw oed ei ychydig furiau, ond mae’r lle wedi denu pererinion byth ers hynny. Wrth ymyl y llwybr mae ffynnon sanctaidd Non, y credir bod ganddi rym i iacháu.[[cite:pl-cadw-stnons]] Saif capel diweddarach i Fair a Non gerllaw. Cadw sy’n gofalu am yr adfail, ac mae am ddim i ymweld ag ef ar unrhyw adeg."]),

 "caergybi": (
  ["## A Roman fort",
   "Caer Gybi is a small Roman fort of the 200s on the cliff above Holyhead harbour. Its walls are remarkably well preserved, up to four metres high and a metre and a half thick, with round towers at the corners. It was probably part of a chain of coastal defences against raiders from the sea, linked with the watchtower on top of Holyhead Mountain.[[cite:pl-cadw-caergybi]]",
   "## Cybi’s church",
   "Welsh tradition holds that in the 500s Maelgwn Gwynedd gave the empty fort to Saint Cybi, who founded a monastery inside its walls. The town’s Welsh name, Caergybi, means Cybi’s fort, and St Cybi’s church still stands within the Roman walls. The fort is free to visit, in the town centre."],
  ["## Caer Rufeinig",
   "Caer Rufeinig fechan o’r 200au yw Caer Gybi, ar y clogwyn uwchben harbwr Caergybi. Mae ei muriau mewn cyflwr rhyfeddol, hyd at bedwar metr o uchder a metr a hanner o drwch, gyda thyrau crwn yn y corneli. Roedd yn rhan, mae’n debyg, o gadwyn o amddiffynfeydd arfordirol rhag ysbeilwyr o’r môr, ynghyd â’r tŵr gwylio ar ben Mynydd Twr.[[cite:pl-cadw-caergybi]]",
   "## Eglwys Cybi",
   "Yn ôl traddodiad Cymru rhoddodd Maelgwn Gwynedd y gaer wag i Gybi Sant yn y 500au, a sefydlodd ef fynachlog o fewn ei muriau. Ystyr enw’r dref yw caer Cybi, ac mae eglwys Cybi yn dal i sefyll o fewn y muriau Rhufeinig. Mae’r gaer am ddim i ymweld â hi, yng nghanol y dref."]),

 "neathabbey": (
  ["Neath Abbey was founded in 1130, and by the late 1200s it was one of the wealthiest abbeys in Wales, with some fifty monks and many more lay brothers working its lands.[[cite:pl-cadw-neathabbey]] In the 1500s the poet Lewys Morgannwg praised it as the fairest abbey in all Wales.",
   "Long after the monks left it was turned into a copper works, with furnaces and workers’ houses, and an ironworks was built next door, yet it survived. Almost the whole plan of the abbey can still be seen, and with Tintern and Llanthony its ruins are the finest monastic remains in south Wales.[[cite:pl-cadw-neathabbey]] It is free to visit."],
  ["Sefydlwyd Abaty Nedd yn 1130, ac erbyn diwedd y 1200au roedd yn un o abatai cyfoethocaf Cymru, gyda thua hanner cant o fynachod a llawer mwy o frodyr lleyg yn gweithio’i diroedd.[[cite:pl-cadw-neathabbey]] Yn y 1500au canmolodd y bardd Lewys Morgannwg ef fel yr abaty tecaf yng Nghymru gyfan.",
   "Ymhell wedi i’r mynachod adael, troed ef yn waith copr, gyda ffwrneisi a thai gweithwyr, a chodwyd gwaith haearn drws nesaf, ond goroesodd. Gellir gweld bron holl gynllun yr abaty o hyd, a chyda Thyndyrn a Llanddewi Nant Hodni ei adfeilion yw olion mynachaidd gorau de Cymru.[[cite:pl-cadw-neathabbey]] Mae am ddim i ymweld ag ef."]),

 "llanthony": (
  ["Llanthony lies deep in the Vale of Ewyas in the Black Mountains. Its full Welsh name, Llanddewi Nant Hodni, remembers a chapel of Saint David by the Honddu stream, where the knight William de Lacy gave up war to live as a hermit. By 1118 it had become a priory of Augustinian canons.[[cite:pl-cadw-llanthony]]",
   "Gerald of Wales, who knew it well, called it truly suited to the monastic life, a wilderness far from the bustle of mankind.[[cite:pl-cadw-llanthony]] The tall arches of its church still frame the hills. It was closed in 1539, and the view has changed little since. It is free to visit."],
  ["Mae Llanddewi Nant Hodni yn ddwfn yn Nyffryn Ewias yn y Mynyddoedd Duon. Mae’r enw’n cofio capel i Ddewi Sant ger nant Hodni, lle rhoddodd y marchog William de Lacy y gorau i ryfel i fyw fel meudwy. Erbyn 1118 roedd wedi dod yn briordy i ganoniaid Awstinaidd.[[cite:pl-cadw-llanthony]]",
   "Dywedodd Gerallt Gymro, a’i hadwaenai’n dda, ei fod yn wir addas i’r bywyd mynachaidd, yn anialwch ymhell o brysurdeb dynion.[[cite:pl-cadw-llanthony]] Mae bwâu tal ei eglwys yn dal i fframio’r bryniau. Caewyd ef yn 1539, ac ychydig a newidiodd yr olygfa ers hynny. Mae am ddim i ymweld ag ef."]),

 "cymer": (
  ["Cymer Abbey stands where the Mawddach and the Wnion meet, just outside Dolgellau. It was founded in 1198 by the princes of Gwynedd for Cistercian monks, one of the smaller houses of the order.[[cite:pl-cadw-cymer]] The Cistercians were farmers as well as monks, pioneers of sheep farming in the Welsh hills.",
   "The abbey suffered greatly in the wars between Wales and England in the 1200s, and its church was never finished, but substantial parts of it still stand.[[cite:pl-cadw-cymer]] It is free to visit."],
  ["Saif Abaty Cymer lle mae afon Mawddach ac afon Wnion yn cwrdd, ychydig y tu allan i Ddolgellau. Fe’i sefydlwyd yn 1198 gan dywysogion Gwynedd i fynachod Sistersaidd, un o dai lleiaf yr urdd.[[cite:pl-cadw-cymer]] Roedd y Sistersiaid yn ffermwyr yn ogystal â mynachod, arloeswyr ffermio defaid ym mryniau Cymru.",
   "Dioddefodd yr abaty’n fawr yn rhyfeloedd Cymru a Lloegr yn y 1200au, ac ni orffennwyd ei eglwys erioed, ond mae rhannau sylweddol ohoni’n dal i sefyll.[[cite:pl-cadw-cymer]] Mae am ddim i ymweld ag ef."]),

 "nanhyfer": (
  ["Nevern church, in a wooded valley below the Preseli hills, was founded by Saint Brynach in the 500s. It was a stopping place for pilgrims on their way to St Davids, and a cross carved in the rock on the path nearby is known as the Pilgrims’ Cross.",
   "In the churchyard stands the Great Cross of Nevern, some four metres tall and covered in knotwork, one of the finest carved crosses in Wales, from around the year 1000. Near the porch is the Vitalianus stone, inscribed in both Latin and ogham in the 400s or 500s, and inside the church another stone carries the name Maglocunus, son of Clutorius, in both scripts.",
   "One of the old yews in the avenue to the church weeps a red sap, and the story is told that it will bleed until a Welshman again rules Nevern castle. The church is usually open in daytime."],
  ["Sefydlwyd eglwys Nanhyfer, mewn cwm coediog islaw’r Preseli, gan Frynach Sant yn y 500au. Roedd yn fan aros i bererinion ar eu ffordd i Dyddewi, a gelwir croes a gerfiwyd yn y graig ar y llwybr gerllaw yn Groes y Pererinion.",
   "Yn y fynwent saif Croes Fawr Nanhyfer, tua phedwar metr o uchder ac wedi’i gorchuddio â chlymwaith, un o’r croesau cerfiedig gorau yng Nghymru, o tua’r flwyddyn 1000. Ger y porth mae carreg Vitalianus, ag arysgrif mewn Lladin ac ogam o’r 400au neu’r 500au, ac y tu mewn i’r eglwys mae carreg arall ag enw Maglocunus fab Clutorius yn y ddwy wyddor.",
   "Mae un o’r hen ywennod yn y rhodfa at yr eglwys yn wylo nodd coch, ac adroddir y bydd yn gwaedu nes y bydd Cymro eto’n rheoli castell Nanhyfer. Mae’r eglwys ar agor fel arfer yn ystod y dydd."]),

 "clynnog": (
  ["Saint Beuno, the great saint of north Wales in the 600s, founded a clas, a community of clergy, at Clynnog Fawr on the coast of Arfon, and he was buried here.[[cite:pl-wiki-clynnog]] His tomb made Clynnog one of the main stopping places for pilgrims on the road to Enlli.",
   "The church that stands today was built around 1480 to 1500, large and full of light, the finest late medieval church in Gwynedd.[[cite:pl-wiki-clynnog]] A passage joins it to St Beuno’s Chapel, on the site of his grave. Just outside the village is Ffynnon Beuno, his holy well. The church is usually open in daytime."],
  ["Sefydlodd Beuno Sant, sant mawr gogledd Cymru yn y 600au, glas, cymuned o glerigwyr, yng Nghlynnog Fawr ar arfordir Arfon, ac fe’i claddwyd yma.[[cite:pl-wiki-clynnog]] Gwnaeth ei fedd Glynnog yn un o brif fannau aros pererinion ar y ffordd i Enlli.",
   "Codwyd yr eglwys bresennol tua 1480 i 1500, yn fawr ac yn llawn goleuni, yr eglwys orau o ddiwedd yr Oesoedd Canol yng Ngwynedd.[[cite:pl-wiki-clynnog]] Mae rhodfa’n ei chysylltu â Chapel Beuno, ar safle ei fedd. Ychydig y tu allan i’r pentref mae Ffynnon Beuno, ei ffynnon sanctaidd. Mae’r eglwys ar agor fel arfer yn ystod y dydd."]),

 "pennantmelangell": (
  ["At the head of the Tanat valley in the Berwyn mountains stands the little church of Pennant Melangell. The story is told that Melangell, a king’s daughter from Ireland, lived here alone in prayer for fifteen years. One day Brochwel Ysgithrog, king of Powys, was hunting, and his hounds chased a hare into a thicket. There he found Melangell at prayer with the hare safe under the hem of her dress, and the hounds would not go near. Moved, he gave her the valley as a place of refuge for ever.[[cite:pl-wiki-melangell]]",
   "Her shrine, carved in the 1100s, is the oldest surviving Romanesque shrine in northern Europe; it was pieced together again from fragments in the 1950s and restored once more in 1991.[[cite:pl-wiki-melangell]] For centuries no one in the parish would kill a hare, and hares are still called Melangell’s lambs. The church is open daily, a peaceful place at the end of a long lane."],
  ["Ym mhen dyffryn Tanat ym mynyddoedd y Berwyn saif eglwys fach Pennant Melangell. Adroddir i Felangell, merch i frenin o Iwerddon, fyw yma ar ei phen ei hun mewn gweddi am bymtheng mlynedd. Un diwrnod roedd Brochwel Ysgithrog, brenin Powys, yn hela, ac erlidiodd ei gŵn ysgyfarnog i lwyn. Yno cafodd Felangell yn gweddïo a’r ysgyfarnog yn ddiogel dan odre ei gwisg, ac nid âi’r cŵn yn agos. Wedi’i gyffwrdd, rhoddodd y cwm iddi yn noddfa am byth.[[cite:pl-wiki-melangell]]",
   "Ei chysegrfa, a gerfiwyd yn y 1100au, yw’r gysegrfa Romanésg hynaf sydd wedi goroesi yng ngogledd Ewrop; fe’i hailosodwyd o ddarnau yn y 1950au a’i hadfer eto yn 1991.[[cite:pl-wiki-melangell]] Am ganrifoedd ni laddai neb yn y plwyf ysgyfarnog, a gelwir ysgyfarnogod o hyd yn ŵyn Melangell. Mae’r eglwys ar agor bob dydd, yn lle tawel ym mhen lôn hir."]),

 "llanddewibrefi": (
  ["Llanddewi Brefi lies in the Teifi valley below the hills of Ceredigion. In the 500s, the story goes, the bishops and clergy of Wales met here in the great synod of Brefi. The crowd was so large that no one could hear the speakers, until Dewi rose to preach and the ground beneath him lifted into a hill, so that all could see and hear him.[[cite:pl-wiki-brefi]]",
   "The church of St David stands on that hill, a place of worship since at least the 600s. Bishop Thomas Bek of St Davids made it a college of priests in 1287, and stones from the old church and from a Roman fort nearby are built into it.[[cite:pl-wiki-brefi]] The church is usually open in daytime."],
  ["Mae Llanddewi Brefi yn nyffryn Teifi islaw bryniau Ceredigion. Yn y 500au, yn ôl y stori, cyfarfu esgobion a chlerigwyr Cymru yma yn synod fawr Brefi. Roedd y dyrfa mor fawr fel na allai neb glywed y siaradwyr, nes i Ddewi godi i bregethu a’r tir dano’n codi’n fryn, fel y gallai pawb ei weld a’i glywed.[[cite:pl-wiki-brefi]]",
   "Saif eglwys Dewi ar y bryn hwnnw, man addoli ers o leiaf y 600au. Gwnaeth yr Esgob Thomas Bek o Dyddewi hi’n goleg o offeiriaid yn 1287, ac mae cerrig o’r hen eglwys ac o gaer Rufeinig gerllaw wedi’u codi i mewn iddi.[[cite:pl-wiki-brefi]] Mae’r eglwys ar agor fel arfer yn ystod y dydd."]),

 "llancarfan": (
  ["Llancarfan, in a quiet valley of the Vale of Glamorgan, is the site of Saint Cadog’s monastery of the 500s, famed for its learning.[[cite:pl-wiki-llancarfan]] Cadog, son of King Gwynllyw and Gwladys, was one of the greatest of the Welsh saints, and Welsh tradition holds that Gildas taught and wrote here. In the 1100s Caradog of Llancarfan wrote lives of the saints here.",
   "In 2008, under layers of whitewash in St Cadoc’s church, workmen found medieval wall paintings, among them a great Saint George, one of only three in the churches of Wales. They were fully uncovered by 2013.[[cite:pl-wiki-llancarfan]] The church is usually open in daytime."],
  ["Llancarfan, mewn cwm tawel ym Mro Morgannwg, yw safle mynachlog Cadog Sant o’r 500au, a oedd yn enwog am ei dysg.[[cite:pl-wiki-llancarfan]] Roedd Cadog, mab y Brenin Gwynllyw a Gwladys, yn un o’r mwyaf o saint Cymru, ac yn ôl traddodiad Cymru bu Gildas yn dysgu ac yn ysgrifennu yma. Yn y 1100au ysgrifennodd Caradog o Lancarfan fucheddau’r saint yma.",
   "Yn 2008, dan haenau o wyngalch yn eglwys Cadog, daeth gweithwyr o hyd i baentiadau wal canoloesol, yn eu plith San Siôr mawr, un o ddim ond tri yn eglwysi Cymru. Datgelwyd hwy’n llawn erbyn 2013.[[cite:pl-wiki-llancarfan]] Mae’r eglwys ar agor fel arfer yn ystod y dydd."]),

 "llanbadarn": (
  ["Saint Padarn founded a church at Llanbadarn Fawr in the early 500s, and it became one of the leading clasau, communities of learned clergy, of early Wales.[[cite:pl-wiki-llanbadarn]]",
   "In the 1000s Sulien, twice bishop of St Davids, made Llanbadarn a home of scholarship. His son Rhygyfarch wrote here the Life of Saint David, around 1090, and the beautiful Psalter of Rhygyfarch was made here around 1079.[[cite:pl-wiki-llanbadarn]] In the 1300s Dafydd ap Gwilym wrote his poem The Girls of Llanbadarn, complaining that not one of them would look at him in church.",
   "The church that stands today was rebuilt in the 1200s, and two carved stone crosses of the 900s and 1000s stand inside.[[cite:pl-wiki-llanbadarn]] It is usually open in daytime."],
  ["Sefydlodd Padarn Sant eglwys yn Llanbadarn Fawr ar ddechrau’r 500au, a daeth yn un o brif glasau, cymunedau o glerigwyr dysgedig, Cymru gynnar.[[cite:pl-wiki-llanbadarn]]",
   "Yn yr 1000au gwnaeth Sulien, esgob Tyddewi ddwywaith, Lanbadarn yn gartref dysg. Ysgrifennodd ei fab Rhygyfarch Fuchedd Dewi Sant yma tua 1090, a gwnaed Sallwyr hardd Rhygyfarch yma tua 1079.[[cite:pl-wiki-llanbadarn]] Yn y 1300au ysgrifennodd Dafydd ap Gwilym ei gerdd Merched Llanbadarn, yn cwyno na edrychai’r un ohonynt arno yn yr eglwys.",
   "Ailgodwyd yr eglwys bresennol yn y 1200au, ac mae dwy groes garreg gerfiedig o’r 900au a’r 1000au y tu mewn iddi.[[cite:pl-wiki-llanbadarn]] Mae ar agor fel arfer yn ystod y dydd."]),

 "bangor": (
  ["Saint Deiniol founded a monastery at Bangor around 530, on land given by Maelgwn Gwynedd, and he is said to have been consecrated its first bishop.[[cite:pl-wiki-bangor]] The word bangor itself means a wattled fence, the kind that ringed an early monastery. Christians have worshipped on this site ever since.",
   "Gruffudd ap Cynan, who won back Gwynedd, was buried by the high altar in 1137, and his son Owain Gwynedd was laid beside him.[[cite:pl-wiki-bangor]] The oldest parts of the present cathedral date from the 1120s; the nave was rebuilt in the 1300s and the tower finished in 1532. It is usually open to visitors in daytime."],
  ["Sefydlodd Deiniol Sant fynachlog ym Mangor tua 530, ar dir a roddwyd gan Faelgwn Gwynedd, a dywedir iddo gael ei gysegru’n esgob cyntaf yno.[[cite:pl-wiki-bangor]] Ystyr y gair bangor yw clawdd plethedig, y math a amgylchynai fynachlog gynnar. Mae Cristnogion wedi addoli ar y safle hwn byth ers hynny.",
   "Claddwyd Gruffudd ap Cynan, a enillodd Wynedd yn ôl, ger yr allor fawr yn 1137, a gosodwyd ei fab Owain Gwynedd wrth ei ymyl.[[cite:pl-wiki-bangor]] Mae rhannau hynaf yr eglwys gadeiriol bresennol yn dyddio o’r 1120au; ailgodwyd corff yr eglwys yn y 1300au a gorffennwyd y tŵr yn 1532. Mae ar agor i ymwelwyr fel arfer yn ystod y dydd."]),

 "llandaf": (
  ["Llandaff Cathedral stands in a hollow by the River Taf in north Cardiff, dedicated to Saints Peter and Paul and to three Welsh saints: Dyfrig, Teilo and Euddogwy.[[cite:pl-wiki-llandaf]] The Book of Llandaf, written in the 1100s, gathers the charters and lives of these saints, and Welsh tradition, as the Book tells it, holds that King Lleurwg sent to Rome in the 100s for teachers of the faith, and that the first church here grew from his time.",
   "The present cathedral was begun in 1120 by Bishop Urban. On 2 January 1941 a German parachute mine blew the roof off the nave; it was rebuilt and back in use by 1958, with Jacob Epstein’s great figure of Christ in Majesty raised above the nave on a concrete arch.[[cite:pl-wiki-llandaf]] It is open daily."],
  ["Saif Eglwys Gadeiriol Llandaf mewn pant ger afon Taf yng ngogledd Caerdydd, wedi’i chysegru i Bedr a Paul ac i dri sant o Gymru: Dyfrig, Teilo ac Euddogwy.[[cite:pl-wiki-llandaf]] Mae Llyfr Llandaf, a ysgrifennwyd yn y 1100au, yn casglu siarteri a bucheddau’r saint hyn, ac mae traddodiad Cymru, fel yr adroddir yn y Llyfr, yn dal i’r Brenin Lleurwg anfon i Rufain yn y 100au am athrawon y ffydd, ac i’r eglwys gyntaf yma dyfu o’i amser ef.",
   "Dechreuwyd yr eglwys gadeiriol bresennol yn 1120 gan yr Esgob Urban. Ar 2 Ionawr 1941 chwythodd ffrwydryn parasiwt Almaenig do corff yr eglwys i ffwrdd; fe’i hailgodwyd ac roedd yn cael ei defnyddio eto erbyn 1958, gyda ffigwr mawr Jacob Epstein o Grist mewn Mawrhydi wedi’i godi uwchben corff yr eglwys ar fwa concrit.[[cite:pl-wiki-llandaf]] Mae ar agor bob dydd."]),

 "llanelwy": (
  ["St Asaph, Llanelwy, by the River Elwy in Denbighshire, has one of the oldest bishoprics in Wales. Welsh tradition holds that Saint Cyndeyrn (Kentigern) founded a monastery here in the 500s and left it to his pupil Asaph, after whom the town is named in English.",
   "Its cathedral, the smallest ancient cathedral in Britain, holds a special place in the story of the Welsh language. William Morgan, who translated the whole Bible into Welsh in 1588, was bishop here from 1601 to 1604. Outside stands the Translators’ Memorial of 1888, honouring him and the others who gave Wales its Bible. The cathedral is open daily."],
  ["Mae gan Lanelwy, ger afon Elwy yn Sir Ddinbych, un o esgobaethau hynaf Cymru. Yn ôl traddodiad Cymru sefydlodd Cyndeyrn Sant fynachlog yma yn y 500au a’i gadael i’w ddisgybl Asa, y caiff y dref ei henw Saesneg ar ei ôl.",
   "Mae gan ei heglwys gadeiriol, yr eglwys gadeiriol hynafol leiaf ym Mhrydain, le arbennig yn hanes yr iaith Gymraeg. Roedd William Morgan, a gyfieithodd y Beibl cyfan i’r Gymraeg yn 1588, yn esgob yma o 1601 hyd 1604. Y tu allan saif Cofeb y Cyfieithwyr o 1888, sy’n ei anrhydeddu ef a’r lleill a roddodd ei Beibl i Gymru. Mae’r eglwys gadeiriol ar agor bob dydd."]),

 "carewcross": (
  ["Carew Cross stands beside the road at the entrance to Carew Castle in Pembrokeshire, more than four metres tall and carved with knots and plaits. It is believed to be the memorial of a fallen Welsh king.[[cite:pl-cadw-carewcross]]",
   "Its Latin inscription reads ‘the cross of Margiteut son of Etguin’: Maredudd ab Edwin, a descendant of the lawgiver Hywel Dda, who ruled Deheubarth and died in battle in 1035.[[cite:pl-cadw-carewcross]] Its shape inspired Cadw’s own badge. It is free to see at any time."],
  ["Saif Croes Caeriw wrth ymyl y ffordd wrth fynedfa Castell Caeriw yn Sir Benfro, dros bedwar metr o uchder ac wedi’i cherfio â chlymau a phlethau. Credir mai cofeb brenin o Gymro a syrthiodd mewn brwydr yw hi.[[cite:pl-cadw-carewcross]]",
   "Mae ei harysgrif Ladin yn darllen ‘croes Margiteut fab Etguin’: Maredudd ab Edwin, disgynnydd Hywel Dda y deddfwr, a reolai Ddeheubarth ac a fu farw mewn brwydr yn 1035.[[cite:pl-cadw-carewcross]] Ei siâp a ysbrydolodd fathodyn Cadw ei hun. Mae am ddim i’w gweld ar unrhyw adeg."]),
})

PEOPLE.update({
 "strataflorida": ["yr-arglwydd-rhys", "llywelyn-fawr", "dafydd-ap-llywelyn", "dafydd-ap-gwilym"],
 "llanilltud": ["illtud", "samson", "gildas", "dewi-sant"],
 "enlli": ["cadfan", "dyfrig", "beuno"],
 "treffynnon": ["gwenfrewi", "beuno"],
 "eliseg": ["elisedd", "cyngen", "macsen-wledig", "edward-lhuyd"],
 "vallecrucis": ["guto-r-glyn", "elisedd"],
 "penmon": ["seiriol", "cybi"],
 "talley": ["yr-arglwydd-rhys"],
 "basingwerk": ["gwenfrewi"],
 "stnons": ["non", "dewi-sant"],
 "caergybi": ["cybi", "maelgwn-gwynedd", "seiriol"],
 "llanthony": ["gerallt-gymro", "dewi-sant"],
 "nanhyfer": ["brynach", "dewi-sant"],
 "clynnog": ["beuno", "gwenfrewi"],
 "pennantmelangell": ["melangell", "brochwel-ysgithrog"],
 "llanddewibrefi": ["dewi-sant"],
 "llancarfan": ["cadog", "gwynllyw", "gwladys", "gildas"],
 "llanbadarn": ["padarn", "sulien", "rhygyfarch", "dafydd-ap-gwilym"],
 "bangor": ["deiniol", "maelgwn-gwynedd", "gruffudd-ap-cynan", "owain-gwynedd"],
 "llandaf": ["dyfrig", "teilo", "euddogwy", "lleurwg"],
 "llanelwy": ["cyndeyrn", "william-morgan"],
 "carewcross": ["hywel-dda"],
})

LINKS.update({
 "eliseg": [("kings-powys.html", "The kings of Powys", "Brenhinoedd Powys")],
 "treffynnon": [("legend-gwenffrewi.html", "The legend of Gwenffrewi", "Chwedl Gwenffrewi")],
 "llanilltud": [("story-learning.html", "The oldest centre of learning", "Y ganolfan ddysg hynaf")],
})

CITES.update(dict([
 _cadw("pl-cadw-strataflorida", "Strata Florida Abbey", "Abaty Ystrad Fflur", "strata-florida-abbey",
       "Cadw’s page: on the banks of the Teifi since 1184; soon the most famous church in Wales after St Davids; resting place of generations of Welsh princes, the ‘Westminster Abbey of Wales’; Dafydd ap Gwilym said to lie under a yew in the churchyard.",
       "Tudalen Cadw: ar lannau Teifi ers 1184; buan yr eglwys enwocaf yng Nghymru ar ôl Tyddewi; gorweddfan cenedlaethau o dywysogion; ‘Abaty Westminster Cymru’; dywedir bod Dafydd ap Gwilym dan ywen yn y fynwent."),
 _cadw("pl-cadw-vallecrucis", "Valle Crucis Abbey", "Abaty Glyn y Groes", "valle-crucis-abbey",
       "Cadw’s page: founded in 1201 by Prince Madog ap Gruffydd, truly Welsh from the start; named after the Pillar of Eliseg; feasts praised by poets; only Tintern richer in 1537; the only surviving monastic fishpond in Wales.",
       "Tudalen Cadw: sefydlwyd yn 1201 gan y Tywysog Madog ap Gruffudd, yn Gymreig o’r dechrau; enwyd ar ôl Colofn Eliseg; gwleddoedd a ganmolwyd gan feirdd; dim ond Tyndyrn yn gyfoethocach yn 1537; yr unig bysgodlyn mynachaidd sydd ar ôl yng Nghymru."),
 _cadw("pl-cadw-penmon", "Penmon Priory, Cross and St Seiriol’s Well", "Priordy, Croes a Ffynnon Seiriol, Penmon", "penmon-priory-cross-and-st-seiriols-well",
       "Cadw’s page: a monastery founded by St Seiriol in the 500s; his holy well; priory ruins of the 1200s; the Penmon Cross of the 900s; the dovecote of the 1400s.",
       "Tudalen Cadw: mynachlog a sefydlwyd gan Seiriol yn y 500au; ei ffynnon sanctaidd; adfeilion priordy o’r 1200au; Croes Penmon o’r 900au; colomendy o’r 1400au."),
 _cadw("pl-cadw-talley", "Talley Abbey", "Abaty Talyllychau", "talley-abbey",
       "Cadw’s page: founded in the 1180s by Rhys ap Gruffydd, the Lord Rhys, the first and only Premonstratensian abbey in Wales; never completed; the tower stands almost to full height.",
       "Tudalen Cadw: sefydlwyd yn yr 1180au gan Rys ap Gruffudd, yr Arglwydd Rhys, yr abaty Premonstratensaidd cyntaf ac unig yng Nghymru; ni orffennwyd; mae’r tŵr bron yn ei lawn uchder."),
 _cadw("pl-cadw-basingwerk", "Basingwerk Abbey", "Abaty Dinas Basing", "basingwerk-abbey",
       "Cadw’s page: founded in 1131, part of the Cistercian network in Wales, remodelled in the 1200s; the chapter house of the 1100s and the monks’ dining hall; start of the North Wales Pilgrim’s Way to Bardsey.",
       "Tudalen Cadw: sefydlwyd yn 1131, yn rhan o rwydwaith y Sistersiaid yng Nghymru, ailwampiwyd yn y 1200au; cabidyldy’r 1100au a ffreutur y mynachod; man cychwyn Llwybr Pererinion Gogledd Cymru i Enlli."),
 _cadw("pl-cadw-margam", "Margam Stones Museum", "Amgueddfa Meini Margam", "margam-stones-museum",
       "Cadw’s page: nearly 30 inscribed stones and crosses, some from the 500s, some first used as Roman milestones; disc-headed and wheel crosses of the 800s and 900s, the Cross of Cynfelin; a knight of the 1300s.",
       "Tudalen Cadw: bron i 30 o feini a chroesau ag arysgrifau, rhai o’r 500au, rhai’n gerrig milltir Rhufeinig yn gyntaf; croesau pen disg ac olwyn o’r 800au a’r 900au, Croes Cynfelin; marchog o’r 1300au."),
 _cadw("pl-cadw-stnons", "St Non’s Chapel", "Capel Non", "st-nons-chapel",
       "Cadw’s page: said to be the birthplace of St David in the 500s, named after his mother St Non; walls of uncertain date; still a place of pilgrimage, with a holy well.",
       "Tudalen Cadw: dywedir mai yma y ganed Dewi Sant yn y 500au, ac fe’i henwir ar ôl ei fam Non; muriau o oed ansicr; yn dal yn gyrchfan pererinion, gyda ffynnon sanctaidd."),
 _cadw("pl-cadw-treffynnon", "St Winefride’s Chapel and Well", "Capel a Ffynnon Gwenffrewi", "st-winefrides-chapel-and-well",
       "Cadw’s page: a place of pilgrimage since at least 1115; the spring rises where St Beuno brought Winefride back to life; the chapel dates from the late 1400s; reputedly the oldest continually visited pilgrim site in Britain.",
       "Tudalen Cadw: cyrchfan pererinion ers o leiaf 1115; mae’r ffynnon yn tarddu lle’r adferodd Beuno Wenffrewi’n fyw; mae’r capel o ddiwedd y 1400au; dywedir mai dyma’r safle pererindod hynaf ym Mhrydain a gafodd ymwelwyr yn ddi-dor."),
 _cadw("pl-cadw-eliseg", "Eliseg’s Pillar", "Colofn Eliseg", "elisegs-pillar",
       "Cadw’s page: raised in the first half of the 800s by Cyngen in memory of his great-grandfather Eliseg, who drove the English out of this part of Wales; the inscription named the rulers of Powys and was probably read aloud; it gave Valle Crucis its name.",
       "Tudalen Cadw: codwyd yn hanner cyntaf yr 800au gan Gyngen er cof am ei hen daid Eliseg, a yrrodd y Saeson allan o’r rhan hon o Gymru; enwai’r arysgrif reolwyr Powys ac roedd i’w darllen yn uchel; rhoddodd ei enw i Lyn y Groes."),
 _cadw("pl-cadw-maenachwyfan", "Maen Achwyfan Cross", "Croes Maen Achwyfan", "maen-achwyfan-cross",
       "Cadw’s page: probably late 900s, made in commemoration of a person or event; its design heavily influenced by Viking seafarers on this coast.",
       "Tudalen Cadw: diwedd y 900au yn ôl pob tebyg, er cof am berson neu ddigwyddiad; ei chynllun dan ddylanwad trwm morwyr Llychlyn ar yr arfordir hwn."),
 _cadw("pl-cadw-tintern", "Tintern Abbey", "Abaty Tyndyrn", "tintern-abbey",
       "Cadw’s page: founded in 1131 by Cistercian monks; the new abbey church begun in 1269; surrendered in 1536 in the first round of the dissolution.",
       "Tudalen Cadw: sefydlwyd yn 1131 gan fynachod Sistersaidd; dechreuwyd yr eglwys abaty newydd yn 1269; ildiodd yn 1536 yn y don gyntaf o ddiddymu’r mynachlogydd."),
 _cadw("pl-cadw-caergybi", "Caer Gybi Roman Fort", "Caer Rufeinig Caergybi", "caer-gybi-roman-fort",
       "Cadw’s page: a fort of the 200s, part of a coastal network of defences, perhaps linked to the watchtower on Holyhead Mountain; walls up to 4 m high and 1.5 m thick, with four corner towers.",
       "Tudalen Cadw: caer o’r 200au, yn rhan o rwydwaith o amddiffynfeydd arfordirol, efallai’n gysylltiedig â’r tŵr gwylio ar Fynydd Twr; muriau hyd at 4 m o uchder a 1.5 m o drwch, gyda phedwar tŵr cornel."),
 _cadw("pl-cadw-neathabbey", "Neath Abbey", "Abaty Nedd", "neath-abbey",
       "Cadw’s page: founded in 1130; one of Wales’s wealthiest abbeys by the late 1200s, with about 50 monks; later a copper smelting works; with Llanthony and Tintern the most important monastic remains in south Wales.",
       "Tudalen Cadw: sefydlwyd yn 1130; un o abatai cyfoethocaf Cymru erbyn diwedd y 1200au, gyda thua 50 o fynachod; gwaith toddi copr yn ddiweddarach; gyda Llanddewi Nant Hodni a Thyndyrn, yr olion mynachaidd pwysicaf yn ne Cymru."),
 _cadw("pl-cadw-llanthony", "Llanthony Priory", "Priordy Llanddewi Nant Hodni", "llanthony-priory",
       "Cadw’s page: William de Lacy founded a hermitage here; a priory of Augustinian canons by 1118; Gerald of Wales called it truly suited to the monastic life; suppressed in 1539.",
       "Tudalen Cadw: sefydlodd William de Lacy feudwyfa yma; priordy i ganoniaid Awstinaidd erbyn 1118; dywedodd Gerallt Gymro ei fod yn wir addas i’r bywyd mynachaidd; diddymwyd yn 1539."),
 _cadw("pl-cadw-cymer", "Cymer Abbey", "Abaty Cymer", "cymer-abbey",
       "Cadw’s page: founded in 1198, one of the lesser Cistercian houses; suffered greatly in the wars between Wales and England in the 1200s; substantial remains of the church survive.",
       "Tudalen Cadw: sefydlwyd yn 1198, un o dai lleiaf y Sistersiaid; dioddefodd yn fawr yn rhyfeloedd Cymru a Lloegr yn y 1200au; mae rhannau sylweddol o’r eglwys wedi goroesi."),
 _cadw("pl-cadw-carewcross", "Carew Cross", "Croes Caeriw", "carew-cross",
       "Cadw’s page: believed to be the memorial of a fallen Welsh king; inscribed ‘the cross of Margiteut son of Etguin’, Maredudd, descendant of Hywel Dda, who ruled Deheubarth and died in battle in 1035; it inspired the Cadw logo.",
       "Tudalen Cadw: credir mai cofeb brenin o Gymro a syrthiodd mewn brwydr yw hi; arysgrif ‘croes Margiteut fab Etguin’, Maredudd, disgynnydd Hywel Dda, a reolai Ddeheubarth ac a fu farw mewn brwydr yn 1035; ysbrydolodd logo Cadw."),
]))


def _wiki(key, title, slug, note_en, note_cy):
    return key, dict(short=("Wikipedia", "Wikipedia"), t=title, by=("Wikipedia, drawing on Cadw’s listing and the Coflein record", "Wikipedia, yn seiliedig ar restriad Cadw a chofnod Coflein"),
                     note=(note_en, note_cy), url="https://en.wikipedia.org/wiki/" + slug, lang="en")


CITES.update(dict([
 _wiki("pl-wiki-clynnog", "St Beuno’s Church, Clynnog Fawr", "St_Beuno%27s_Church,_Clynnog_Fawr",
       "Beuno founded a clas on the site and was buried there; the chancel and transepts c. 1480 to 1486, the nave c. 1500; St Beuno’s Chapel joined to the church; Ffynnon Beuno near the village.",
       "Sefydlodd Beuno glas ar y safle a’i gladdu yno; y gangell a’r croesfreichiau tua 1480 i 1486, corff yr eglwys tua 1500; Capel Beuno ynghlwm wrth yr eglwys; Ffynnon Beuno ger y pentref."),
 _wiki("pl-wiki-melangell", "Pennant Melangell", "Pennant_Melangell",
       "Melangell and the hare under her hem, and Prince Brochwel’s gift of the land; the shrine of c. 1160 to 1170, the oldest surviving Romanesque shrine in northern Europe; rebuilt in 1958 and restored in 1991.",
       "Melangell a’r ysgyfarnog dan ei gwisg, a rhodd Brochwel o’r tir; y gysegrfa o tua 1160 i 1170, y gysegrfa Romanésg hynaf sydd wedi goroesi yng ngogledd Ewrop; ailgodwyd yn 1958 a’i hadfer yn 1991."),
 _wiki("pl-wiki-brefi", "Llanddewi Brefi", "Llanddewi_Brefi",
       "The synod of Brefi in the 500s, when the ground rose under David so that all could hear him; worship on the site since the 600s; Bishop Thomas Bek’s collegiate church; Roman stones from the nearby fort.",
       "Synod Brefi yn y 500au, pan gododd y tir dan Ddewi fel y gallai pawb ei glywed; addoli ar y safle ers y 600au; eglwys golegol yr Esgob Thomas Bek; cerrig Rhufeinig o’r gaer gerllaw."),
 _wiki("pl-wiki-llancarfan", "Llancarfan", "Llancarfan",
       "The site of St Cadoc’s 6th-century clas, famed for its learning; medieval wall paintings found under whitewash in 2008, including one of only three depictions of St George in Welsh churches, uncovered by 2013.",
       "Safle clas Cadog o’r chweched ganrif, a oedd yn enwog am ei dysg; paentiadau wal canoloesol a gafwyd dan wyngalch yn 2008, gan gynnwys un o ddim ond tri llun o San Siôr yn eglwysi Cymru, wedi’u datgelu erbyn 2013."),
 _wiki("pl-wiki-llanbadarn", "St Padarn’s Church, Llanbadarn Fawr", "St_Padarn%27s_Church,_Llanbadarn_Fawr",
       "Founded in the early 500s, probably by Padarn; one of the leading clasau of early Wales; Sulien and his son Rhygyfarch, who wrote the Life of St David; the Psalter made here c. 1079; two carved crosses; rebuilt in the 1200s.",
       "Sefydlwyd ar ddechrau’r 500au, gan Badarn yn ôl pob tebyg; un o brif glasau Cymru gynnar; Sulien a’i fab Rhygyfarch, awdur Buchedd Dewi; y Sallwyr a wnaed yma tua 1079; dwy groes gerfiedig; ailgodwyd yn y 1200au."),
 _wiki("pl-wiki-bangor", "Bangor Cathedral", "Bangor_Cathedral",
       "Deiniol’s monastery of about 530 on land given by Maelgwn Gwynedd; Gruffudd ap Cynan buried by the high altar in 1137 and Owain Gwynedd beside him; building from the 1120s, nave of the 1300s, tower 1532.",
       "Mynachlog Deiniol tua 530 ar dir a roddwyd gan Faelgwn Gwynedd; claddwyd Gruffudd ap Cynan ger yr allor fawr yn 1137 ac Owain Gwynedd wrth ei ymyl; adeiladu o’r 1120au, corff yr eglwys o’r 1300au, y tŵr 1532."),
 _wiki("pl-wiki-llandaf", "Llandaff Cathedral", "Llandaff_Cathedral",
       "Dedicated to Saints Peter and Paul and to Dyfrig, Teilo and Euddogwy; the Book of Llandaf of the 1100s; begun under Bishop Urban in 1120; the parachute mine of 2 January 1941; Epstein’s Christ in Majesty; back in use in 1958.",
       "Wedi’i chysegru i Bedr a Paul ac i Ddyfrig, Teilo ac Euddogwy; Llyfr Llandaf o’r 1100au; dechreuwyd dan yr Esgob Urban yn 1120; ffrwydryn parasiwt 2 Ionawr 1941; Crist mewn Mawrhydi gan Epstein; yn ôl mewn defnydd yn 1958."),
]))


# Every batch above adds to CITES; this hands them all to src/cites.py, so it must stay at the end.
import cites as _CITES  # noqa: E402
for _k in CITES:
    if _k in _CITES.S and _CITES.S[_k] is not CITES[_k]:
        raise SystemExit(f"src/places3.py: source key {_k} is already used in src/cites.py")
_CITES.S.update(CITES)
