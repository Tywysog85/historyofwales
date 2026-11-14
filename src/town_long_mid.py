"""The stories of the towns of mid and west Wales, for their pages (see src/town_long.py).
Powys, Ceredigion, Pembrokeshire and Carmarthenshire. The one-line history on towns.html comes first on each page,
so these paragraphs carry the story on from it."""

LONG = {
 # ---------- Powys ----------
 "town-machynlleth": dict(era="glyndwr", en=[
    "The old Parliament House on Maengwyn Street stands where tradition places Owain’s parliament, and it is now a centre telling his story. For a few years Machynlleth was the capital of a free Wales, with its own prince, its own seal and its own envoys abroad.",
    "In 1973 the Centre for Alternative Technology was founded in an old slate quarry just north of the town, and it has taught people from all over the world how to live more lightly on the land.",
 ], cy=[
    "Saif yr hen Senedd-dy ar Heol Maengwyn lle mae traddodiad yn gosod senedd Owain, ac mae bellach yn ganolfan sy’n adrodd ei stori. Am ychydig flynyddoedd Machynlleth oedd prifddinas Cymru rydd, gyda’i thywysog ei hun, ei sêl ei hun a’i chenhadon ei hun dramor.",
    "Yn 1973 sefydlwyd y Ganolfan Dechnoleg Amgen mewn hen chwarel lechi ychydig i’r gogledd o’r dref, ac mae wedi dysgu pobl o bob cwr o’r byd sut i fyw’n ysgafnach ar y tir.",
 ]),
 "town-brecon": dict(era="kings", en=[
    "Rhys ap Tewdwr, the last king of Deheubarth, fell fighting the Normans near here in 1093, and Bernard de Neufmarché built his castle and priory where the Honddu meets the Usk. Gerald of Wales was archdeacon of Brecon and wrote much of his work here.",
    "The great actress Sarah Siddons was born in the town in 1755, and the priory church became the cathedral of the new diocese of Swansea and Brecon in 1923.",
 ], cy=[
    "Syrthiodd Rhys ap Tewdwr, brenin olaf Deheubarth, yn ymladd yn erbyn y Normaniaid ger y fan hon yn 1093, a chododd Bernard de Neufmarché ei gastell a’i briordy lle mae’r Honddu’n cwrdd â’r Wysg. Bu Gerallt Gymro’n archddiacon Brycheiniog ac ysgrifennodd lawer o’i waith yma.",
    "Ganwyd yr actores fawr Sarah Siddons yn y dref yn 1755, a daeth eglwys y priordy’n eglwys gadeiriol esgobaeth newydd Abertawe ac Aberhonddu yn 1923.",
 ]),
 "town-welshpool": dict(era="medieval", en=[
    "Powis Castle was built in the 1200s by Gruffudd ap Gwenwynwyn, prince of southern Powys, and its red stone gives it its Welsh name, Castell Coch. Its terraced gardens are among the finest in Britain.",
    "Gruffudd gave the town its first charter in the 1200s. Later the Montgomery Canal and the little railway to Llanfair Caereinion carried its trade.",
 ], cy=[
    "Codwyd Castell Powis yn y 1200au gan Ruffudd ap Gwenwynwyn, tywysog de Powys, ac mae ei garreg goch yn rhoi ei enw Cymraeg iddo, Castell Coch. Mae ei erddi ar derasau ymhlith y gorau ym Mhrydain.",
    "Rhoddodd Gruffudd ei siarter gyntaf i’r dref yn y 1200au. Yn ddiweddarach cariodd Camlas Trefaldwyn a’r rheilffordd fach i Lanfair Caereinion ei masnach.",
 ]),
 "town-newtown": dict(era="industrial", en=[
    "The new town was founded in 1279 beside the old church of Llanfair-yng-Nghedewain. In the 1800s its flannel mills made it the ‘Leeds of Wales’.",
    "Pryce Jones’ Royal Welsh Warehouse of 1879 sent Welsh flannel by post to Queen Victoria and Florence Nightingale. Robert Owen came home to die in the town in 1858 and is buried in the old churchyard of St Mary.",
 ], cy=[
    "Sefydlwyd y dref newydd yn 1279 ger hen eglwys Llanfair-yng-Nghedewain. Yn yr 1800au gwnaeth ei melinau gwlanen hi’n ‘Leeds Cymru’.",
    "Anfonodd Warws Cymreig Brenhinol Pryce Jones o 1879 wlanen Gymreig drwy’r post i’r Frenhines Fictoria a Florence Nightingale. Daeth Robert Owen adref i farw yn y dref yn 1858 ac mae wedi’i gladdu yn hen fynwent y Santes Fair.",
 ]),
 "town-llandrindod-wells": dict(era="industrial", en=[
    "The Roman fort of Castell Collen stands by the river Ithon just north of the town, and on the common the Roman army dug a large group of practice camps, where soldiers learned to build forts.",
    "Victorian visitors came on the Central Wales railway, opened in 1865, to drink the waters at the Rock Park pump room, and each August the town dresses up for its Victorian Festival.",
 ], cy=[
    "Saif caer Rufeinig Castell Collen ger afon Ieithon ychydig i’r gogledd o’r dref, ac ar y comin cloddiodd y fyddin Rufeinig grŵp mawr o wersylloedd ymarfer, lle dysgai milwyr godi caerau.",
    "Daeth ymwelwyr oes Fictoria ar reilffordd Calon Cymru, a agorwyd yn 1865, i yfed y dyfroedd yn ystafell bwmp Parc y Graig, a phob mis Awst mae’r dref yn gwisgo i fyny ar gyfer ei Gŵyl Fictoraidd.",
 ]),
 "town-builth-wells": dict(era="medieval", en=[
    "At Cilmeri a great stone of granite from Trefor in Llŷn was raised in 1956 where Llywelyn fell, and people gather there every December to remember the last prince of an independent Wales.",
    "Across the Wye at Llanelwedd, the Royal Welsh Show has had its own showground since 1963, and farmers come from all over Wales for the four days.",
 ], cy=[
    "Yng Nghilmeri codwyd maen mawr o wenithfaen o Drefor yn Llŷn yn 1956 lle syrthiodd Llywelyn, ac mae pobl yn ymgynnull yno bob mis Rhagfyr i gofio tywysog olaf Cymru annibynnol.",
    "Dros yr afon yn Llanelwedd mae gan Sioe Frenhinol Cymru ei maes ei hun ers 1963, a daw ffermwyr o bob rhan o Gymru am y pedwar diwrnod.",
 ]),
 "town-llanidloes": dict(era="industrial", en=[
    "The town grew with the flannel trade and with the lead mines of the Van in the hills to the west, among the richest in Britain in the 1870s.",
    "Its market hall is the only timber-framed market hall in Wales still standing, and the Clywedog reservoir above the town was made in the 1960s.",
 ], cy=[
    "Tyfodd y dref gyda’r fasnach wlanen a gyda mwyngloddiau plwm y Fan yn y bryniau i’r gorllewin, ymhlith y cyfoethocaf ym Mhrydain yn yr 1870au.",
    "Ei neuadd farchnad yw’r unig neuadd farchnad ffrâm bren yng Nghymru sy’n dal i sefyll, a gwnaed cronfa Clywedog uwchben y dref yn yr 1960au.",
 ]),
 "town-montgomery": dict(era="medieval", en=[
    "The Normans built their first castle at Hen Domen, a mile away, in the 1070s, and Henry III began the stone castle on the rock above the town in 1223.",
    "The poet George Herbert was born here in 1593, and Montgomery, the county town of Montgomeryshire, keeps its Georgian square and town hall.",
 ], cy=[
    "Cododd y Normaniaid eu castell cyntaf yn Hen Domen, filltir i ffwrdd, yn yr 1070au, a dechreuodd Harri III y castell carreg ar y graig uwchben y dref yn 1223.",
    "Ganwyd y bardd George Herbert yma yn 1593, ac mae Trefaldwyn, tref sirol Sir Drefaldwyn, yn cadw ei sgwâr a’i neuadd dref Sioraidd.",
 ]),
 "town-hay-on-wye": dict(era="today", en=[
    "The de Braose family built the castle about 1200, and Llywelyn the Great burned the town in 1231 in his war on the March.",
    "Richard Booth opened his first second-hand bookshop here in the 1960s, and soon the old cinema, the castle and half the shops were full of books. The festival now brings writers and readers from all over the world every spring.",
 ], cy=[
    "Cododd teulu de Braose y castell tua 1200, a llosgodd Llywelyn Fawr y dref yn 1231 yn ei ryfel ar y Mers.",
    "Agorodd Richard Booth ei siop lyfrau ail-law gyntaf yma yn yr 1960au, a chyn hir roedd yr hen sinema, y castell a hanner y siopau’n llawn llyfrau. Mae’r ŵyl bellach yn denu awduron a darllenwyr o bob cwr o’r byd bob gwanwyn.",
 ]),
 "town-crickhowell": dict(era="britons", en=[
    "Crug Hywel, the flat-topped Table Mountain above the town, is a hillfort of the Britons. Tretower Court, the home of the Vaughans, who were patrons of the Welsh poets, stands three miles up the valley.",
 ], cy=[
    "Bryngaer y Brythoniaid yw Crug Hywel, y mynydd pen gwastad uwchben y dref. Saif Llys Tretŵr, cartref teulu Vaughan, noddwyr y beirdd Cymraeg, dair milltir i fyny’r dyffryn.",
 ]),
 "town-llanwrtyd-wells": dict(era="revival", en=[
    "In 1732 the Reverend Theophilus Evans, author of Drych y Prif Oesoedd, drank from the sulphur spring called Ffynnon Drewllyd, the stinking well, and was cured of his illness, and the spa was born.",
    "Today the town is famous for its own odd contests, from the Man versus Horse race, first run in 1980, to the World Bog Snorkelling Championships.",
 ], cy=[
    "Yn 1732 yfodd y Parchedig Theophilus Evans, awdur Drych y Prif Oesoedd, o’r ffynnon sylffwr o’r enw Ffynnon Drewllyd, a chafodd wellhad o’i salwch, a ganwyd y sba.",
    "Heddiw mae’r dref yn enwog am ei chystadlaethau rhyfedd ei hun, o’r ras Dyn yn erbyn Ceffyl, a redwyd gyntaf yn 1980, i Bencampwriaethau Snorclo Cors y Byd.",
 ]),
 "town-llanrhaeadr-ym-mochnant": dict(era="tudor", en=[
    "Four miles up the valley, Pistyll Rhaeadr falls 240 feet, the highest single drop in Wales and one of the Seven Wonders of Wales.",
    "A memorial in the churchyard was raised in 1888 to mark three hundred years of Morgan’s Bible, the book that kept Welsh alive.",
 ], cy=[
    "Bedair milltir i fyny’r cwm mae Pistyll Rhaeadr yn disgyn 240 troedfedd, y cwymp unigol uchaf yng Nghymru ac un o Saith Rhyfeddod Cymru.",
    "Codwyd cofeb yn y fynwent yn 1888 i nodi tri chan mlynedd ers Beibl Morgan, y llyfr a gadwodd y Gymraeg yn fyw.",
 ]),
 "town-knighton": dict(era="glyndwr", en=[
    "Some of the finest stretches of Offa’s Dyke run over the hills either side of the town, and the Offa’s Dyke Centre is here. In June 1402 Owain Glyndŵr’s men won the battle of Bryn Glas at Pilleth, a few miles to the south.",
 ], cy=[
    "Mae rhai o rannau gorau Clawdd Offa’n rhedeg dros y bryniau bob ochr i’r dref, ac mae Canolfan Clawdd Offa yma. Ym mis Mehefin 1402 enillodd gwŷr Owain Glyndŵr frwydr Bryn Glas ym Mhilalau, ychydig filltiroedd i’r de.",
 ]),
 "town-presteigne": dict(era="industrial", en=[
    "The Judge’s Lodging, finished in 1829 for the judges of the Radnorshire assizes, is now a museum of Victorian life. The town sits right on the border, on the river Lugg.",
 ], cy=[
    "Mae Llety’r Barnwr, a orffennwyd yn 1829 i farnwyr brawdlys Maesyfed, bellach yn amgueddfa bywyd oes Fictoria. Saif y dref ar y ffin, ar afon Lugg.",
 ]),
 "town-rhayader": dict(era="medieval", en=[
    "West of the town the Elan valley dams were built between 1893 and 1904 to send water to Birmingham, and the waters covered farms, a chapel and Cwm Elan, where the poet Shelley had stayed.",
    "When the red kite vanished from the rest of Britain, a few pairs survived in these hills. Today hundreds of them gather to feed at Gigrin farm outside the town.",
 ], cy=[
    "I’r gorllewin o’r dref codwyd argaeau Cwm Elan rhwng 1893 a 1904 i anfon dŵr i Birmingham, a boddodd y dyfroedd ffermydd, capel a Chwm Elan, lle bu’r bardd Shelley’n aros.",
    "Pan ddiflannodd y barcud coch o weddill Prydain, goroesodd ychydig o barau yn y bryniau hyn. Heddiw mae cannoedd ohonynt yn ymgasglu i fwydo ar fferm Gigrin y tu allan i’r dref.",
 ]),
 "town-llanfyllin": dict(era="revival", en=[
    "French officers held as prisoners of war in the town in 1812 painted murals on the walls of the Council House, which can still be seen.",
    "Ann Griffiths could not write her hymns down herself; her maid Ruth learned them by heart, and Ruth’s husband John Hughes wrote them down, so they are sung throughout Wales today.",
 ], cy=[
    "Peintiodd swyddogion o Ffrainc a gedwid yn garcharorion rhyfel yn y dref yn 1812 furluniau ar furiau Tŷ’r Cyngor, a gellir eu gweld o hyd.",
    "Ni allai Ann Griffiths ysgrifennu ei hemynau ei hun; dysgodd ei morwyn Ruth hwy ar ei chof, ac ysgrifennodd gŵr Ruth, John Hughes, hwy i lawr, fel eu bod yn cael eu canu drwy Gymru heddiw.",
 ]),
 "town-llanfair-caereinion": dict(era="industrial", en=[
    "The light railway was closed in 1956 and saved by volunteers, who have run steam trains along the Banwy valley to Welshpool since 1963.",
 ], cy=[
    "Caewyd y rheilffordd ysgafn yn 1956 a’i hachub gan wirfoddolwyr, sydd wedi rhedeg trenau stêm ar hyd dyffryn Banwy i’r Trallwng ers 1963.",
 ]),
 "town-talgarth": dict(era="revival", en=[
    "Harris was moved to his faith by a sermon in Talgarth church in 1735. At Trefeca he gathered ‘the Family’, a Christian community of farmers and craftsmen, and in 1768 the Countess of Huntingdon opened a college there to train preachers.",
    "Talgarth’s church is named after Gwendolen, said to be one of Brychan’s many daughters.",
 ], cy=[
    "Cyffyrddwyd Harris gan bregeth yn eglwys Talgarth yn 1735. Yn Nhrefeca casglodd ‘y Teulu’, cymuned Gristnogol o ffermwyr a chrefftwyr, ac yn 1768 agorodd Iarlles Huntingdon goleg yno i hyfforddi pregethwyr.",
    "Mae eglwys Talgarth wedi’i henwi ar ôl Gwendolen, y dywedir ei bod yn un o ferched niferus Brychan.",
 ]),
 "town-ystradgynlais": dict(era="industrial", en=[
    "Herman painted the miners walking home at the end of their shift, dark against the evening sky, and his great painting Miners was made for the Festival of Britain in 1951.",
 ], cy=[
    "Paentiodd Herman y glowyr yn cerdded adref ar ddiwedd eu shifft, yn dywyll yn erbyn awyr yr hwyr, a gwnaed ei lun mawr Glowyr ar gyfer Gŵyl Prydain yn 1951.",
 ]),

 # ---------- Ceredigion ----------
 "town-aberystwyth": dict(era="modern", en=[
    "Edward I began the castle in 1277. Owain Glyndŵr took it in 1404 and held it for four years.",
    "The National Library, founded in 1907, keeps the Black Book of Carmarthen, the Book of Taliesin and the Hendregadredd manuscript among the treasures of Wales. In February 1963 Cymdeithas yr Iaith held its first protest on Trefechan bridge, for the right to use Welsh in public life.",
 ], cy=[
    "Dechreuodd Edward I y castell yn 1277. Cipiodd Owain Glyndŵr ef yn 1404 a’i ddal am bedair blynedd.",
    "Mae’r Llyfrgell Genedlaethol, a sefydlwyd yn 1907, yn cadw Llyfr Du Caerfyrddin, Llyfr Taliesin a Llawysgrif Hendregadredd ymhlith trysorau Cymru. Ym mis Chwefror 1963 cynhaliodd Cymdeithas yr Iaith ei phrotest gyntaf ar bont Trefechan, dros yr hawl i ddefnyddio’r Gymraeg mewn bywyd cyhoeddus.",
 ]),
 "town-cardigan": dict(era="medieval", en=[
    "In 1136, at Crug Mawr just north of the town, Owain Gwynedd and his brother Cadwaladr routed a great Norman army, and many of the fleeing Normans drowned in the Teifi. The Lord Rhys rebuilt the castle in stone in 1171, one of the first stone castles raised by a Welsh ruler.",
    "The castle was saved by the town and reopened in 2015 as a centre for Welsh culture, and the eisteddfod has come home to it.",
 ], cy=[
    "Yn 1136, yng Nghrug Mawr ychydig i’r gogledd o’r dref, gyrrodd Owain Gwynedd a’i frawd Cadwaladr fyddin Normanaidd fawr ar ffo, a boddodd llawer o’r Normaniaid yn y Teifi. Ailgododd yr Arglwydd Rhys y castell mewn carreg yn 1171, un o’r cestyll carreg cyntaf a godwyd gan reolwr Cymreig.",
    "Achubwyd y castell gan y dref a’i ailagor yn 2015 yn ganolfan i ddiwylliant Cymru, ac mae’r eisteddfod wedi dod adref ato.",
 ]),
 "town-lampeter": dict(era="revival", en=[
    "Bishop Thomas Burgess founded the college to train clergy for Wales who could not afford Oxford or Cambridge, and it became the first place in Wales to give degrees. Its Old Building, by C. R. Cockerell, is built around a quadrangle like an Oxford college.",
 ], cy=[
    "Sefydlodd yr Esgob Thomas Burgess y coleg i hyfforddi clerigwyr i Gymru na allent fforddio Rhydychen na Chaergrawnt, a hwn oedd y lle cyntaf yng Nghymru i roi graddau. Mae ei Hen Adeilad, gan C. R. Cockerell, wedi’i godi o amgylch cwad fel coleg yn Rhydychen.",
 ]),
 "town-aberaeron": dict(era="revival", en=[
    "The Reverend Alban Thomas Jones Gwynne built the harbour after an Act of Parliament in 1807, and the town was laid out around it in neat squares and terraces.",
 ], cy=[
    "Adeiladodd y Parchedig Alban Thomas Jones Gwynne yr harbwr wedi Deddf Seneddol yn 1807, a chynlluniwyd y dref o’i amgylch mewn sgwariau a therasau taclus.",
 ]),
 "town-new-quay": dict(era="modern", en=[
    "Its stone pier was built in 1835, and the ships built on its beaches sailed all over the world. Today it is one of the best places in Britain to see the dolphins of Cardigan Bay.",
 ], cy=[
    "Codwyd ei harbwr carreg yn 1835, a hwyliodd y llongau a adeiladwyd ar ei thraethau i bob rhan o’r byd. Heddiw mae’n un o’r lleoedd gorau ym Mhrydain i weld dolffiniaid Bae Ceredigion.",
 ]),
 "town-tregaron": dict(era="revival", en=[
    "The drovers gathered their herds here for the long walk over the mountains to England, and the Talbot was their inn. Twm Siôn Cati, the Welsh Robin Hood, was born nearby about 1530.",
    "Henry Richard’s statue stands in the square, and the great bog of Cors Caron stretches north of the town.",
 ], cy=[
    "Casglai’r porthmyn eu gyrroedd yma ar gyfer y daith hir dros y mynyddoedd i Loegr, a’r Talbot oedd eu tafarn. Ganwyd Twm Siôn Cati, Robin Hood Cymru, gerllaw tua 1530.",
    "Saif cerflun Henry Richard yn y sgwâr, ac mae cors fawr Cors Caron yn ymestyn i’r gogledd o’r dref.",
 ]),
 "town-llanbadarn-fawr": dict(era="saints", en=[
    "Rhygyfarch, son of Sulien, wrote the Life of Saint David here about 1090, and his brother Ieuan copied and painted the Ricemarch Psalter.",
    "In the 1300s Dafydd ap Gwilym wrote a famous poem about the girls he watched in Llanbadarn church instead of saying his prayers.",
 ], cy=[
    "Ysgrifennodd Rhygyfarch, mab Sulien, Fuchedd Dewi yma tua 1090, a chopïodd a lliwiodd ei frawd Ieuan Sallwyr Rhygyfarch.",
    "Yn y 1300au ysgrifennodd Dafydd ap Gwilym gerdd enwog am y merched a wyliai yn eglwys Llanbadarn yn lle dweud ei weddïau.",
 ]),
 "town-llandysul": dict(era="industrial", en=[
    "The Teifi valley around the town was the heart of the Welsh woollen industry, with dozens of mills at Drefach Felindre nearby, now the home of the National Wool Museum.",
 ], cy=[
    "Dyffryn Teifi o amgylch y dref oedd calon diwydiant gwlân Cymru, gyda dwsinau o felinau yn Nrefach Felindre gerllaw, cartref Amgueddfa Wlân Cymru heddiw.",
 ]),

 # ---------- Pembrokeshire ----------
 "town-st-davids": dict(era="saints", en=[
    "The cathedral was begun in 1181 in the hollow of Glyn Rhosyn, low enough to hide it from raiders at sea. About 1123 the Pope declared that two pilgrimages to St Davids were worth one to Rome.",
    "Gerald of Wales fought for years to make St Davids the seat of an archbishop for all Wales. On the cliffs south of the city is the well of Saint Non, where tradition holds that Dewi was born in a storm.",
 ], cy=[
    "Dechreuwyd yr eglwys gadeiriol yn 1181 ym mhant Glyn Rhosyn, yn ddigon isel i’w chuddio rhag ysbeilwyr ar y môr. Tua 1123 cyhoeddodd y Pab fod dwy bererindod i Dyddewi’n werth un i Rufain.",
    "Brwydrodd Gerallt Gymro am flynyddoedd i wneud Tyddewi’n sedd archesgob i Gymru gyfan. Ar y clogwyni i’r de o’r ddinas mae ffynnon Non, lle mae traddodiad yn dweud i Ddewi gael ei eni mewn storm.",
 ]),
 "town-pembroke": dict(era="tudor", en=[
    "Arnulf de Montgomery built the first castle here in 1093, and William Marshal raised its great round keep about 1200. Beneath the castle is the Wogan, a huge natural cave.",
    "In the Civil War the town held out for seven weeks in 1648 against Oliver Cromwell himself.",
 ], cy=[
    "Cododd Arnulf de Montgomery y castell cyntaf yma yn 1093, a chododd William Marshal ei orthwr crwn mawr tua 1200. O dan y castell mae’r Wogan, ogof naturiol enfawr.",
    "Yn y Rhyfel Cartref daliodd y dref ei thir am saith wythnos yn 1648 yn erbyn Oliver Cromwell ei hun.",
 ]),
 "town-haverfordwest": dict(era="medieval", en=[
    "The Flemings, settled here by Henry I in the 1100s, made Haverfordwest a busy port and market on the Western Cleddau, and for centuries it was a county in its own right.",
    "By the river are the ruins of an Augustinian priory, whose medieval garden, found by archaeologists, is one of the very few in Britain to survive.",
 ], cy=[
    "Gwnaeth y Ffleminiaid, a osodwyd yma gan Harri I yn y 1100au, Hwlffordd yn borthladd a marchnad brysur ar y Gleddau Wen, ac am ganrifoedd bu’n sir yn ei rhinwedd ei hun.",
    "Ger yr afon mae adfeilion priordy Awstinaidd, ac mae ei ardd ganoloesol, a ddarganfuwyd gan archaeolegwyr, yn un o’r ychydig iawn ym Mhrydain sydd wedi goroesi.",
 ]),
 "town-fishguard": dict(era="revival", en=[
    "The French signed their surrender in the Royal Oak inn, where the table can still be seen. For the two hundredth anniversary in 1997 the people of the town stitched the Last Invasion Tapestry, a hundred feet long, which hangs in the town hall.",
    "The film of Under Milk Wood was made in the Lower Town in 1971, with Richard Burton and Elizabeth Taylor.",
 ], cy=[
    "Arwyddodd y Ffrancwyr eu hildio yn nhafarn y Royal Oak, lle gellir gweld y bwrdd o hyd. Ar gyfer y daucanmlwyddiant yn 1997 pwythodd pobl y dref Dapestri’r Glaniad Olaf, can troedfedd o hyd, sy’n crogi yn neuadd y dref.",
    "Gwnaed ffilm Under Milk Wood yn y Cwm yn 1971, gyda Richard Burton ac Elizabeth Taylor.",
 ]),
 "town-tenby": dict(era="tudor", en=[
    "The town walls of the 1200s still ring the old town, with the Five Arches gate. Robert Recorde, the mathematician who invented the equals sign (=), was born here about 1512.",
    "The painter Augustus John was born in Tenby in 1878, and he and his sister Gwen grew up by its sands.",
 ], cy=[
    "Mae muriau’r dref o’r 1200au’n dal i amgylchynu’r hen dref, gyda phorth y Pum Bwa. Ganwyd Robert Recorde, y mathemategydd a ddyfeisiodd yr arwydd hafal (=), yma tua 1512.",
    "Ganwyd yr arlunydd Augustus John yn Ninbych-y-pysgod yn 1878, a magwyd ef a’i chwaer Gwen ar lan ei thraethau.",
 ]),
 "town-milford-haven": dict(era="industrial", en=[
    "In Shakespeare’s Cymbeline, Imogen asks ‘how far is it to this same blessed Milford?’, and Nelson praised the haven as one of the finest harbours in the world when he came in 1802.",
    "Today it is one of the great energy ports of Britain.",
 ], cy=[
    "Yn Cymbeline gan Shakespeare mae Imogen yn gofyn pa mor bell yw hi i’r ‘Milford fendigaid’ hon, a chanmolodd Nelson yr hafan fel un o borthladdoedd gorau’r byd pan ddaeth yn 1802.",
    "Heddiw mae’n un o borthladdoedd ynni mawr Prydain.",
 ]),
 "town-newport-pembrokeshire": dict(era="saints", en=[
    "William FitzMartin built the castle in the 1190s, after the Lord Rhys took his older castle at Nevern. In the churchyard at Nevern, two miles away, stand one of the finest carved crosses in Wales and the bleeding yew.",
 ], cy=[
    "Cododd William FitzMartin y castell yn yr 1190au, wedi i’r Arglwydd Rhys gipio ei gastell hŷn yn Nanhyfer. Ym mynwent Nanhyfer, ddwy filltir i ffwrdd, saif un o’r croesau cerfiedig gorau yng Nghymru a’r ywen sy’n gwaedu.",
 ]),
 "town-narberth": dict(era="kings", en=[
    "Near his court was the mound of Gorsedd Arberth: whoever sat on it would see a wonder, and there Pwyll first saw Rhiannon ride by on her white horse.",
    "The Rebecca riots began a few miles to the north, at Efail-wen, in 1839.",
 ], cy=[
    "Ger ei lys roedd twmpath Gorsedd Arberth: pwy bynnag a eisteddai arno a welai ryfeddod, ac yno y gwelodd Pwyll Riannon gyntaf yn marchogaeth heibio ar ei cheffyl gwyn.",
    "Dechreuodd helyntion Beca ychydig filltiroedd i’r gogledd, yn Efail-wen, yn 1839.",
 ]),
 "town-crymych": dict(era="ancient", en=[
    "Foel Drygarn above the village is crowned by three great Bronze Age cairns inside an Iron Age hillfort. Along the Preseli ridge are the outcrops where the bluestones of Stonehenge were quarried some five thousand years ago.",
 ], cy=[
    "Ar ben Foel Drygarn uwchben y pentref mae tair carnedd fawr o Oes yr Efydd y tu mewn i fryngaer o Oes yr Haearn. Ar hyd crib y Preseli mae’r brigiadau lle cloddiwyd cerrig gleision Côr y Cewri tua phum mil o flynyddoedd yn ôl.",
 ]),
 "town-mynachlog-ddu": dict(era="modern", en=[
    "The stone circle of Gors Fawr stands on the common, and a memorial stone to Waldo Williams looks out over the hills he wrote about.",
 ], cy=[
    "Saif cylch cerrig Gors Fawr ar y comin, ac mae carreg goffa i Waldo Williams yn edrych dros y bryniau y canodd amdanynt.",
 ]),
 "town-pembroke-dock": dict(era="industrial", en=[
    "The dockyard was guarded by Martello towers and the Defensible Barracks, and it worked until 1926. Its Sunderland flying boats hunted submarines over the Atlantic.",
 ], cy=[
    "Gwarchodid yr iard longau gan dyrau Martello a’r Barics Amddiffynadwy, a bu’n gweithio tan 1926. Bu ei hawyrennau môr Sunderland yn hela llongau tanfor dros Fôr Iwerydd.",
 ]),
 "town-neyland": dict(era="industrial", en=[
    "Its steamers sailed to Waterford and Cork for fifty years, until the Irish service moved to Fishguard in 1906.",
 ], cy=[
    "Hwyliodd ei stemars i Waterford a Chorc am hanner can mlynedd, nes i wasanaeth Iwerddon symud i Abergwaun yn 1906.",
 ]),
 "town-goodwick": dict(era="revival", en=[
    "The French had landed two days earlier at Carregwastad Point on Pen Caer, a short walk west of the village, where a stone marks the spot.",
 ], cy=[
    "Roedd y Ffrancwyr wedi glanio ddeuddydd ynghynt ym Mhwynt Carregwastad ar Ben Caer, ychydig i’r gorllewin o’r pentref, lle mae carreg yn nodi’r fan.",
 ]),
 "town-saundersfoot": dict(era="industrial", en=[
    "A tramway brought the coal from the pits at Stepaside and Kilgetty through tunnels along the shore to the quay.",
 ], cy=[
    "Cariai tramffordd y glo o’r pyllau yn Stepaside a Chilgeti drwy dwneli ar hyd y lan i’r cei.",
 ]),

 # ---------- Carmarthenshire ----------
 "town-carmarthen": dict(era="roman", en=[
    "Moridunum had an amphitheatre, which can still be seen beside Priory Street. The Black Book of Carmarthen is the oldest manuscript written wholly in Welsh.",
    "Myrddin’s oak stood in the town until the 1970s, and a piece of it is kept in the museum. In 1966 Gwynfor Evans won the seat here, the first member of parliament for Plaid Cymru.",
 ], cy=[
    "Roedd gan Moridunum amffitheatr, y gellir ei gweld o hyd ger Heol y Prior. Llyfr Du Caerfyrddin yw’r llawysgrif hynaf a ysgrifennwyd yn gyfan gwbl yn Gymraeg.",
    "Safodd derwen Myrddin yn y dref tan yr 1970au, a chedwir darn ohoni yn yr amgueddfa. Yn 1966 enillodd Gwynfor Evans y sedd yma, aelod seneddol cyntaf Plaid Cymru.",
 ]),
 "town-llandeilo": dict(era="saints", en=[
    "Teilo’s church was one of the great mother churches of Wales. The Gospels of Saint Teilo, now at Lichfield, were kept here, and the notes in their margins hold some of the oldest written Welsh.",
    "Dinefwr castle, Newton House and the deer park with its ancient white cattle stand on the edge of the town.",
 ], cy=[
    "Roedd eglwys Teilo’n un o fam-eglwysi mawr Cymru. Cedwid Efengylau Teilo, sydd bellach yng Nghaerlwytgoed, yma, ac mae’r nodiadau ar eu hymylon yn cynnwys peth o’r Gymraeg ysgrifenedig hynaf.",
    "Saif castell Dinefwr, Tŷ Newydd a’r parc ceirw gyda’i wartheg gwynion hynafol ar gyrion y dref.",
 ]),
 "town-llandovery": dict(era="glyndwr", en=[
    "In 1401 Llywelyn ap Gruffudd Fychan of Caeo led Henry IV’s army astray for days rather than betray Owain Glyndŵr, and he was put to death in the town for it. His tall steel statue stands below the castle.",
    "Llandovery College was founded in 1847 by Thomas Phillips to give boys a good education in Welsh as well as English.",
 ], cy=[
    "Yn 1401 arweiniodd Llywelyn ap Gruffudd Fychan o Gaeo fyddin Harri IV ar gyfeiliorn am ddyddiau yn hytrach na bradychu Owain Glyndŵr, a rhoddwyd ef i farwolaeth yn y dref am hynny. Saif ei gerflun dur tal islaw’r castell.",
    "Sefydlwyd Coleg Llanymddyfri yn 1847 gan Thomas Phillips i roi addysg dda i fechgyn yn Gymraeg yn ogystal â Saesneg.",
 ]),
 "town-kidwelly": dict(era="medieval", en=[
    "Gwenllian was the daughter of Gruffudd ap Cynan and wife of Gruffudd ap Rhys, and her death made ‘Revenge for Gwenllian’ the war cry of the Welsh. Her rising helped begin the great Welsh advance of 1136.",
    "The castle’s great gatehouse was finished in the 1400s, and the town’s tinplate works, begun in the 1730s, were among the oldest in Britain.",
 ], cy=[
    "Roedd Gwenllian yn ferch i Ruffudd ap Cynan ac yn wraig i Ruffudd ap Rhys, a gwnaeth ei marwolaeth ‘Dial am Wenllian’ yn gri ryfel y Cymry. Helpodd ei gwrthryfel i ddechrau ymgyrch fawr y Cymry yn 1136.",
    "Gorffennwyd porth mawr y castell yn y 1400au, ac roedd gwaith tun y dref, a ddechreuwyd yn yr 1730au, ymhlith yr hynaf ym Mhrydain.",
 ]),
 "town-llanelli": dict(era="industrial", en=[
    "The town’s tinplate went into tin cans and cooking pots all over the world, which is why its rugby song is Sosban Fach, the little saucepan, and saucepans once topped the posts at Stradey Park.",
 ], cy=[
    "Aeth tun y dref yn duniau a sosbenni ledled y byd, a dyna pam mai Sosban Fach yw ei chân rygbi, a pham y bu sosbenni ar ben pyst Parc y Strade.",
 ]),
 "town-laugharne": dict(era="modern", en=[
    "Laugharne has kept its own medieval corporation, with a portreeve and its own court, since its charter of about 1290. Turner painted its castle by the Taf estuary.",
 ], cy=[
    "Mae Talacharn wedi cadw ei chorfforaeth ganoloesol ei hun, gyda phortrif a’i llys ei hun, ers ei siarter tua 1290. Paentiodd Turner ei chastell ger aber y Taf.",
 ]),
 "town-whitland": dict(era="kings", en=[
    "The Hywel Dda garden in the town tells the story of the laws. The Cistercian abbey of Whitland, founded in 1140, was the mother house of Strata Florida and other Welsh abbeys, and a favourite of the Lord Rhys.",
 ], cy=[
    "Mae gardd Hywel Dda yn y dref yn adrodd stori’r cyfreithiau. Abaty Sistersaidd Hendy-gwyn, a sefydlwyd yn 1140, oedd mam-dŷ Ystrad Fflur ac abatai Cymreig eraill, ac roedd yn annwyl gan yr Arglwydd Rhys.",
 ]),
 "town-llanddowror": dict(era="revival", en=[
    "Between 1737 and his death in 1761, Griffith Jones’s schools taught more than two hundred thousand people to read the Bible in Welsh, and Wales became one of the most literate nations in Europe.",
 ], cy=[
    "Rhwng 1737 a’i farw yn 1761, dysgodd ysgolion Griffith Jones fwy na dau gan mil o bobl i ddarllen y Beibl yn Gymraeg, a daeth Cymru’n un o’r cenhedloedd mwyaf llythrennog yn Ewrop.",
 ]),
 "town-ammanford": dict(era="modern", en=[
    "Jim Griffiths, a miner from Betws across the river, became the first Secretary of State for Wales in 1964. The National Eisteddfod came to the town in 1922.",
 ], cy=[
    "Daeth Jim Griffiths, glöwr o’r Betws dros yr afon, yn Ysgrifennydd Gwladol cyntaf Cymru yn 1964. Daeth yr Eisteddfod Genedlaethol i’r dref yn 1922.",
 ]),
 "town-llandybie": dict(era="medieval", en=[
    "Carreg Cennen castle stands on a crag three hundred feet above the river Cennen. The princes of Deheubarth held a stronghold here before the stone castle of the late 1200s. The great lime kilns of Cilyrychen fed the farms of the Tywi valley.",
 ], cy=[
    "Saif castell Carreg Cennen ar glogwyn dri chan troedfedd uwchben afon Cennen. Roedd gan dywysogion Deheubarth amddiffynfa yma cyn y castell carreg o ddiwedd y 1200au. Bwydai odynau calch mawr Cilyrychen ffermydd dyffryn Tywi.",
 ]),
 "town-pumsaint": dict(era="roman", en=[
    "The name means five saints: tradition holds that five saintly brothers rested their heads on a stone here, which still bears their marks. The Romans dug for gold at Dolaucothi with great channels of water, and the mine was worked again in the 1930s.",
 ], cy=[
    "Ystyr yr enw yw pum sant: yn ôl traddodiad gorffwysodd pum brawd sanctaidd eu pennau ar garreg yma, sy’n dal i ddwyn eu holion. Cloddiodd y Rhufeiniaid am aur yn Nolaucothi â sianeli mawr o ddŵr, a gweithiwyd y gwaith eto yn yr 1930au.",
 ]),
 "town-newcastle-emlyn": dict(era="tudor", en=[
    "Sir Rhys ap Thomas, who helped Henry Tudor win at Bosworth, made the castle into a fine house about 1500. The town still holds its market by the river Teifi.",
 ], cy=[
    "Gwnaeth Syr Rhys ap Thomas, a helpodd Harri Tudur i ennill ym Mosworth, y castell yn dŷ hardd tua 1500. Mae’r dref yn dal i gynnal ei marchnad ger afon Teifi.",
 ]),
 "town-st-clears": dict(era="revival", en=[
    "The Lord Rhys took the castle in 1189. In the Rebecca riots the farmers, dressed as women, broke the gates again and again, until the turnpike laws were changed in 1844.",
 ], cy=[
    "Cipiodd yr Arglwydd Rhys y castell yn 1189. Yn helyntion Beca torrodd y ffermwyr, wedi’u gwisgo fel merched, y gatiau dro ar ôl tro, nes i gyfreithiau’r tyrpeg gael eu newid yn 1844.",
 ]),
 "town-burry-port": dict(era="modern", en=[
    "Earhart came down in the seaplane Friendship off the harbour, where a memorial stone stands today. Behind the town are the long sands of Cefn Sidan and Pembrey forest.",
 ], cy=[
    "Daeth Earhart i lawr yn yr awyren fôr Friendship oddi ar yr harbwr, lle mae carreg goffa heddiw. Y tu ôl i’r dref mae traeth hir Cefn Sidan a choedwig Pen-bre.",
 ]),
 "town-llanybydder": dict(era="revival", en=[
    "The horse fair is held on the last Thursday of the month, and dealers come from across Wales, England and Ireland.",
 ], cy=[
    "Cynhelir y ffair geffylau ar ddydd Iau olaf y mis, a daw delwyr o bob rhan o Gymru, Lloegr ac Iwerddon.",
 ]),
}

PEOPLE = {
    "town-brecon": ["rhys-ap-tewdwr", "gerallt-gymro", "sarah-siddons"],
    "town-welshpool": [],
    "town-builth-wells": [],
    "town-montgomery": ["george-herbert", "llywelyn-ap-gruffudd"],
    "town-llanwrtyd-wells": ["theophilus-evans"],
    "town-knighton": ["owain-glyndwr"],
    "town-talgarth": [],
    "town-aberystwyth": ["owain-glyndwr", "ifan-ab-owen-edwards"],
    "town-cardigan": ["owain-gwynedd"],
    "town-tregaron": ["twm-sion-cati"],
    "town-llanbadarn-fawr": ["rhygyfarch", "ieuan-ap-sulien", "dafydd-ap-gwilym"],
    "town-st-davids": ["non", "gerallt-gymro"],
    "town-tenby": ["robert-recorde", "augustus-john", "gwen-john"],
    "town-fishguard": [],
    "town-newport-pembrokeshire": ["brynach", "yr-arglwydd-rhys"],
    "town-narberth": ["rhiannon"],
    "town-carmarthen": ["myrddin", "gwynfor-evans"],
    "town-llandovery": ["llywelyn-ap-gruffudd-fychan"],
    "town-kidwelly": ["gruffudd-ap-rhys"],
    "town-whitland": ["hywel-dda", "yr-arglwydd-rhys"],
    "town-ammanford": ["jim-griffiths"],
    "town-newcastle-emlyn": ["rhys-ap-thomas"],
    "town-st-clears": ["yr-arglwydd-rhys"],
}
