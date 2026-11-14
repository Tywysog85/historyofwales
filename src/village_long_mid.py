"""The stories of the villages of mid and west Wales, batch 2 (see src/villages.py and src/town_long.py).
Powys, Ceredigion, Carmarthenshire and Pembrokeshire. The one-line history on towns.html comes first on each page, so
these paragraphs carry the story on from it."""

LONG = {
 # ---------- Powys ----------
 "town-guilsfield": dict(era="ancient", en=[
    "The hoard was turned up by a farm worker in a boggy field in 1862: more than a hundred pieces of bronze, many of them broken spearheads, sword pieces and socketed axes, buried together about 3,000 years ago. Some think it was a smith’s store of metal for melting, others an offering to the waters, and it is kept in the National Museum.",
    "Above the village stands the great hill fort of Gaer Fawr, one of the finest in mid Wales, with its ramparts in the woods. The church of Aelhaearn grew rich as the mother church of a wide parish, and its carved roof of the 1400s is one of the treasures of the Welsh March.",
 ], cy=[
    "Daeth gwas fferm o hyd i’r celc mewn cae corslyd yn 1862: mwy na chant o ddarnau efydd, llawer ohonynt yn bennau gwaywffyn wedi’u torri, darnau cleddyfau a bwyeill socedog, wedi’u claddu gyda’i gilydd tua 3,000 o flynyddoedd yn ôl. Mae rhai’n meddwl mai stôr gof o fetel i’w doddi oedd hi, eraill mai offrwm i’r dyfroedd, ac mae’n cael ei chadw yn yr Amgueddfa Genedlaethol.",
    "Uwchben y pentref mae bryngaer fawr y Gaer Fawr, un o’r gorau yng nghanolbarth Cymru, gyda’i rhagfuriau yn y coed. Tyfodd eglwys Aelhaearn yn gyfoethog fel mameglwys plwyf eang, ac mae ei tho cerfiedig o’r 1400au yn un o drysorau’r Gororau.",
 ]),
 "town-llanymynech": dict(era="roman", en=[
    "The Ogof, a cave in the hill, is a copper mine that was worked in the Roman period and perhaps long before, and Roman coins have been found deep inside it. Around it lies one of the largest hill forts in Britain, its ramparts enclosing some 140 acres of the hilltop.",
    "In the 1800s limestone was burnt in kilns by the canal to make lime for the fields, and the Hoffmann kiln of 1899, a great ring of chambers that burnt day and night, is one of the few left in Britain. The village pub once stood across the border, so that drinkers in one bar were in Wales and in the other in England.",
 ], cy=[
    "Mwynglawdd copr yw’r Ogof, ogof yn y bryn, a weithiwyd yn y cyfnod Rhufeinig ac efallai ymhell cyn hynny, a darganfuwyd darnau arian Rhufeinig yn ddwfn y tu mewn iddi. O’i chwmpas mae un o fryngaerau mwyaf Prydain, ei rhagfuriau’n cau tua 140 erw o ben y bryn.",
    "Yn yr 1800au llosgid calchfaen mewn odynau wrth y gamlas i wneud calch i’r caeau, ac mae odyn Hoffmann o 1899, cylch mawr o siambrau a losgai ddydd a nos, yn un o’r ychydig sydd ar ôl ym Mhrydain. Safai tafarn y pentref ar draws y ffin unwaith, fel bod yfwyr mewn un bar yng Nghymru ac yn y llall yn Lloegr.",
 ]),
 "town-abermule": dict(era="medieval", en=[
    "Dolforwyn was built close under the nose of the king’s castle at Montgomery, and Edward I forbade it in 1273; Llywelyn answered that he needed no leave to build on his own land. It was the last castle he built, and in the war of 1277 it was taken after a short siege.",
    "The village grew by the Severn, the road and later the Montgomeryshire Canal and the railway. In January 1921 two trains met head-on on the single line just west of the village, and the Abermule disaster led to safer ways of working single lines across Britain.",
 ], cy=[
    "Codwyd Dolforwyn o dan drwyn castell y brenin yn Nhrefaldwyn, a gwaharddodd Edward I ef yn 1273; atebodd Llywelyn nad oedd angen caniatâd arno i godi ar ei dir ei hun. Hwn oedd y castell olaf a gododd, ac yn rhyfel 1277 cipiwyd ef wedi gwarchae byr.",
    "Tyfodd y pentref wrth Hafren, y ffordd ac yn ddiweddarach Camlas Sir Drefaldwyn a’r rheilffordd. Ym mis Ionawr 1921 cyfarfu dau drên ben wrth ben ar y lein sengl ychydig i’r gorllewin o’r pentref, ac arweiniodd trychineb Abermiwl at ffyrdd mwy diogel o weithio leiniau sengl ar draws Prydain.",
 ]),
 "town-tregynon": dict(era="modern", en=[
    "Gwendoline and Margaret Davies, granddaughters of the Llandinam industrialist David Davies, bought Gregynog in 1920 to make it a centre for the arts in Wales. They brought musicians, artists and craftsmen there, held the Gregynog Festival of music, and set up a press whose hand-printed books, with wood engravings, are among the most beautiful made in Wales.",
    "Their collection of paintings by Monet, Cézanne, Renoir, Van Gogh and others was left to the National Museum of Wales, and it is one of the great collections of Impressionist art in Britain. Margaret gave Gregynog itself to the University of Wales in 1960, and the hall, with its black and white front, is still a place of music and learning.",
 ], cy=[
    "Prynodd Gwendoline a Margaret Davies, wyresau’r diwydiannwr David Davies o Landinam, Gregynog yn 1920 i’w wneud yn ganolfan i’r celfyddydau yng Nghymru. Daethant â cherddorion, artistiaid a chrefftwyr yno, cynnal Gŵyl Gerdd Gregynog, a sefydlu gwasg y mae ei llyfrau a argraffwyd â llaw, gyda’u hysgythriadau pren, ymhlith y harddaf a wnaed yng Nghymru.",
    "Gadawyd eu casgliad o luniau gan Monet, Cézanne, Renoir, Van Gogh ac eraill i Amgueddfa Genedlaethol Cymru, ac mae’n un o gasgliadau mawr celf Argraffiadol Prydain. Rhoddodd Margaret Gregynog ei hun i Brifysgol Cymru yn 1960, ac mae’r neuadd, gyda’i ffrynt du a gwyn, yn dal yn lle i gerddoriaeth a dysg.",
 ]),
 "town-llanwddyn": dict(era="industrial", en=[
    "The Vyrnwy dam was the first large masonry dam built in Britain, and the lake it made, nearly five miles long, still sends water to Liverpool through a pipeline of almost seventy miles. Its straining tower, with a pointed roof like a castle turret, stands in the water near the shore.",
    "Some 37 houses, two chapels, three inns and the church of the old village went under the water, and the dead were moved from the churchyard to the new church built above the dam. In a dry summer the old walls and the line of the road still show in the mud, a reminder of a Welsh valley given up for an English city, as Tryweryn would be later.",
 ], cy=[
    "Argae Efyrnwy oedd yr argae maen mawr cyntaf a godwyd ym Mhrydain, ac mae’r llyn a wnaeth, bron i bum milltir o hyd, yn dal i anfon dŵr i Lerpwl drwy bibell o bron i saith deg milltir. Mae ei dŵr hidlo, â tho pigfain fel tyred castell, yn sefyll yn y dŵr ger y lan.",
    "Aeth rhyw 37 o dai, dau gapel, tair tafarn ac eglwys yr hen bentref o dan y dŵr, a symudwyd y meirw o’r fynwent i’r eglwys newydd a godwyd uwchben yr argae. Mewn haf sych mae’r hen furiau a llinell y ffordd yn dal i ddangos yn y llaid, i’n hatgoffa am gwm Cymreig a roddwyd i ddinas yn Lloegr, fel y byddai Tryweryn yn ddiweddarach.",
 ]),
 "town-meifod": dict(era="kings", en=[
    "Gwyddfarch founded the first church here in the 500s, and Tysilio, son of Brochwel Ysgithrog, king of Powys, made Meifod his home. The church of Tysilio and Mary that stands now keeps a carved grave slab of the 1100s, perhaps the tomb of a prince, covered with a cross and Welsh knotwork.",
    "Madog ap Maredudd, the last king of all Powys, was buried here in 1160, and the poets called Meifod the burial place of the kings of Powys. Cynddelw Brydydd Mawr sang of its church as a place of light. Mathrafal’s earthworks stand by the river Banwy, and the National Eisteddfod was held in the fields of Meifod in 2003 and 2015.",
 ], cy=[
    "Sefydlodd Gwyddfarch yr eglwys gyntaf yma yn y 500au, a gwnaeth Tysilio, mab Brochwel Ysgithrog, brenin Powys, Feifod yn gartref iddo. Mae eglwys Tysilio a Mair sy’n sefyll heddiw yn cadw slab bedd cerfiedig o’r 1100au, bedd tywysog efallai, wedi’i orchuddio â chroes a chlymwaith Cymreig.",
    "Claddwyd Madog ap Maredudd, brenin olaf Powys gyfan, yma yn 1160, a galwai’r beirdd Feifod yn fan claddu brenhinoedd Powys. Canodd Cynddelw Brydydd Mawr i’w heglwys fel lle o oleuni. Saif gwrthgloddiau Mathrafal wrth afon Banwy, a chynhaliwyd yr Eisteddfod Genedlaethol yng nghaeau Meifod yn 2003 a 2015.",
 ]),
 "town-llanfihangel-yng-ngwynfa": dict(era="revival", en=[
    "Ann Thomas was a farmer’s daughter who loved dancing and the harp until she heard a sermon in Llanfyllin in 1796 and was converted. She married Thomas Griffiths of Meifod and died at twenty-nine after the birth of her daughter, leaving about seventy verses that she had sung aloud to her maid, Ruth Evans, who remembered them.",
    "Her hymns are some of the greatest poetry in Welsh, full of wonder at ‘the wonders’ of grace, and they are sung across Wales still. The walk of Llwybr Ann Griffiths runs from Dolwar Fach to Pont Llogel, and a memorial chapel stands at Dolanog by the river Efyrnwy.",
 ], cy=[
    "Merch fferm oedd Ann Thomas a garai ddawnsio a’r delyn nes iddi glywed pregeth yn Llanfyllin yn 1796 a chael tröedigaeth. Priododd Thomas Griffiths o Feifod a bu farw yn naw ar hugain oed wedi geni ei merch, gan adael tua saith deg o benillion a ganasai’n uchel i’w morwyn, Ruth Evans, a’u cofiodd.",
    "Mae ei hemynau ymhlith barddoniaeth fwyaf y Gymraeg, yn llawn rhyfeddod at ‘ryfeddodau’ gras, ac maent yn dal i gael eu canu ar draws Cymru. Mae Llwybr Ann Griffiths yn rhedeg o Ddolwar Fach i Bont Llogel, ac mae capel coffa yn sefyll yn Nolanog wrth afon Efyrnwy.",
 ]),
 # ---------- Ceredigion ----------
 "town-borth": dict(era="ancient", en=[
    "The forest is a wood of oak, pine, birch and hazel that grew on the land behind the shore until rising seas drowned it more than 4,000 years ago; a wooden trackway of the Bronze Age was found among the stumps after the storms of 2014. The story of Cantre’r Gwaelod, with its sixteen fair towns and its bells that ring under the sea, is one of the best-loved in Wales.",
    "Borth grew as a village of fishermen and sailors on a long shingle bank between the sea and the bog of Cors Fochno, one of the largest raised bogs in Britain. The railway came in 1863 and made it a seaside village, and the Dyfi estuary and its dunes at Ynyslas lie to the north.",
 ], cy=[
    "Coedwig o dderw, pinwydd, bedw a chyll yw’r goedwig a dyfai ar y tir y tu ôl i’r lan nes i’r môr yn codi ei boddi fwy na 4,000 o flynyddoedd yn ôl; darganfuwyd llwybr pren o Oes yr Efydd ymhlith y bonion wedi stormydd 2014. Mae stori Cantre’r Gwaelod, gyda’i un ar bymtheg o drefi teg a’i chlychau sy’n canu o dan y môr, yn un o’r rhai mwyaf annwyl yng Nghymru.",
    "Tyfodd y Borth yn bentref pysgotwyr a morwyr ar fanc hir o raean rhwng y môr a Chors Fochno, un o gyforgorsydd mwyaf Prydain. Daeth y rheilffordd yn 1863 a’i gwneud yn bentref glan môr, ac mae aber y Ddyfi a’i thwyni yn Ynys-las i’r gogledd.",
 ]),
 "town-llanddewi-brefi": dict(era="saints", en=[
    "The Synod was called to answer the teaching of Pelagius, and Dewi, the Life says, was sent for from Mynyw and spoke so well that he was made the leader of the church of Wales. A white dove settled on his shoulder as he preached. The church is a large one for so small a village, as befits a place of pilgrimage.",
    "In its walls are early Christian stones, among them part of the Idnert stone of the 600s or 700s, which tells of a man killed for defending the church of the holy Dewi, one of the earliest writings to name him. The village sits in the green valley of the Teifi, at the edge of the hills of Elenydd.",
 ], cy=[
    "Galwyd y Synod i ateb dysgeidiaeth Pelagius, ac anfonwyd am Ddewi o Fynyw, medd y Fuchedd, a siaradodd mor dda nes ei wneud yn arweinydd eglwys Cymru. Disgynnodd colomen wen ar ei ysgwydd wrth iddo bregethu. Mae’r eglwys yn un fawr i bentref mor fach, fel sy’n gweddu i le pererindod.",
    "Yn ei muriau mae meini Cristnogol cynnar, yn eu plith ran o garreg Idnert o’r 600au neu’r 700au, sy’n sôn am ddyn a laddwyd wrth amddiffyn eglwys y sanctaidd Dewi, un o’r ysgrifeniadau cynharaf i’w enwi. Saif y pentref yn nyffryn gwyrdd y Teifi, ar ymyl bryniau Elenydd.",
 ]),
 "town-pontrhydfendigaid": dict(era="medieval", en=[
    "Strata Florida was the heart of Welsh learning in the age of the princes: the Brut y Tywysogion, the chronicle of the princes, was most probably kept there, and Llywelyn the Great called the princes of Wales together at the abbey in 1238 to swear loyalty to his son Dafydd. Its great west doorway, carved like a looped rope, still stands.",
    "The village grew around the bridge over the Teifi, on the old road to the abbey and to the bogs of Cors Caron. It holds a famous eisteddfod each year in its large pavilion, and the poet Dafydd ap Gwilym, greatest of the medieval poets, is remembered by a memorial under the yew at the abbey.",
 ], cy=[
    "Ystrad Fflur oedd calon dysg Gymraeg yn oes y tywysogion: cadwyd Brut y Tywysogion, cronicl y tywysogion, yno yn fwy na thebyg, a galwodd Llywelyn Fawr dywysogion Cymru ynghyd yn yr abaty yn 1238 i dyngu teyrngarwch i’w fab Dafydd. Mae ei ddrws gorllewinol mawr, wedi’i gerfio fel rhaff ddolennog, yn dal i sefyll.",
    "Tyfodd y pentref o gwmpas y bont dros y Teifi, ar yr hen ffordd i’r abaty ac i Gors Caron. Mae’n cynnal eisteddfod enwog bob blwyddyn yn ei bafiliwn mawr, a chofir y bardd Dafydd ap Gwilym, y mwyaf o feirdd yr Oesoedd Canol, gan gofeb o dan yr ywen yn yr abaty.",
 ]),
 "town-llangrannog": dict(era="modern", en=[
    "Caranog was a saint of the 500s whose cave is said to be in the cliffs above the beach, and the great rock of Carreg Bica stands on the sand, a giant’s tooth in the local story. Little ships were built on the beach and traded along the coast, and the village was home to many sea captains.",
    "The Urdd camp has been a first taste of life in Welsh for children from all over Wales, with its horses, ski slope and nights of songs. The coast path runs north to the headland of Ynys Lochtyn.",
 ], cy=[
    "Sant o’r 500au oedd Caranog y dywedir bod ei ogof yn y clogwyni uwchben y traeth, ac mae craig fawr Carreg Bica yn sefyll ar y tywod, dant cawr yn ôl y stori leol. Adeiladwyd llongau bach ar y traeth a masnachent ar hyd yr arfordir, ac roedd y pentref yn gartref i lawer o gapteiniaid llongau.",
    "Mae gwersyll yr Urdd wedi bod yn flas cyntaf ar fywyd yn Gymraeg i blant o bob rhan o Gymru, gyda’i geffylau, ei lethr sgïo a’i nosweithiau o ganu. Mae llwybr yr arfordir yn rhedeg i’r gogledd at bentir Ynys Lochtyn.",
 ]),
 "town-llangeitho": dict(era="revival", en=[
    "On a Communion Sunday thousands came to Llangeitho, some walking for days from Gwynedd and Morgannwg, and the crowds were so great that Rowland preached in the open air. Among those who heard him was the young Thomas Charles, who wrote that it was the day of his salvation, and who went on to make Bala the centre of the Methodist movement in the north.",
    "Rowland was put out of the Church of England in 1763, and his followers built him a large chapel in the village. His statue, unveiled in 1883, stands in front of the chapel, and his grave is in the churchyard of Ceitho.",
 ], cy=[
    "Ar Sul Cymun deuai miloedd i Langeitho, rhai’n cerdded am ddyddiau o Wynedd a Morgannwg, ac roedd y torfeydd mor fawr nes i Rowland bregethu yn yr awyr agored. Ymhlith y rhai a’i clywodd roedd y Thomas Charles ifanc, a ysgrifennodd mai hwnnw oedd dydd ei iachawdwriaeth, ac a aeth ymlaen i wneud y Bala’n ganolfan y mudiad Methodistaidd yn y gogledd.",
    "Trowyd Rowland allan o Eglwys Loegr yn 1763, a chododd ei ddilynwyr gapel mawr iddo yn y pentref. Mae ei gerflun, a ddadorchuddiwyd yn 1883, yn sefyll o flaen y capel, ac mae ei fedd ym mynwent Ceitho.",
 ]),
 # ---------- Carmarthenshire ----------
 "town-pencader": dict(era="kings", en=[
    "Gerald set down the old man’s words in his Description of Wales: ‘This nation, O king, may now, as in former times, be harassed, weakened and destroyed by your and other powers, but it will never be totally subdued by the wrath of man, unless the wrath of God shall concur. Nor do I think that any other nation than this of Wales, or any other language, whatever may hereafter come to pass, shall on the day of severe examination before the Supreme Judge, answer for this corner of the earth.’",
    "A stone memorial of 1952 in the village carries his words. The earthworks of a castle mound of the 1100s stand in the village.",
 ], cy=[
    "Cofnododd Gerallt eiriau’r hen ŵr yn ei Ddisgrifiad o Gymru: ‘Gall y genedl hon, O frenin, gael ei gormesu, ei gwanhau a’i difetha gennych chi a nerthoedd eraill, fel yn yr hen amser, ond ni chaiff fyth ei llwyr orchfygu gan lid dyn, oni bai fod llid Duw yn cytuno. Ac nid wyf yn meddwl mai unrhyw genedl arall na hon o Gymru, nac unrhyw iaith arall, beth bynnag a ddigwydd wedi hyn, a fydd, ar ddydd yr archwiliad mawr gerbron y Barnwr Goruchaf, yn ateb dros y gornel hon o’r ddaear.’",
    "Mae cofeb garreg o 1952 yn y pentref yn dwyn ei eiriau. Saif gwrthgloddiau tomen castell o’r 1100au yn y pentref.",
 ]),
 "town-llansteffan": dict(era="medieval", en=[
    "The young Rhys ap Gruffudd, later the Lord Rhys, fought beside his brothers Cadell and Maredudd when they stormed the castle, and Maredudd threw down the ladders of the Normans who came to take it back. The great gatehouse that stands now was built in the late 1200s, and the castle looks across the Tywi to Ferryside and down to Carmarthen Bay.",
    "Below the castle the village has a long sandy beach, and the old ferry crossed the estuary to Glanyfferi. Dylan Thomas walked these shores from his home across the water at Laugharne, and St Anthony’s Well, an old holy well, lies in the woods by the shore.",
 ], cy=[
    "Ymladdodd y Rhys ap Gruffudd ifanc, yr Arglwydd Rhys yn ddiweddarach, ochr yn ochr â’i frodyr Cadell a Maredudd pan ymosodasant ar y castell, a thaflodd Maredudd ysgolion y Normaniaid a ddaeth i’w gipio’n ôl i lawr. Codwyd y porthdy mawr sy’n sefyll heddiw ar ddiwedd y 1200au, ac mae’r castell yn edrych ar draws y Tywi at Lanyfferi ac i lawr at Fae Caerfyrddin.",
    "O dan y castell mae gan y pentref draeth tywodlyd hir, a chroesai’r hen fferi’r aber i Lanyfferi. Cerddodd Dylan Thomas y glannau hyn o’i gartref yr ochr draw i’r dŵr yn Nhalacharn, ac mae Ffynnon Antwn, hen ffynnon sanctaidd, yn y coed ger y lan.",
 ]),
 "town-myddfai": dict(era="medieval", en=[
    "Rhiwallon was physician to Rhys Gryg, lord of Dinefwr, in the 1230s, and with his sons Cadwgan, Gruffudd and Einion he wrote down cures from herbs, honey and the plants of the hills. The family went on as doctors in the parish for some five hundred years, and the last of the line are remembered in the church.",
    "The story says their mother rose from Llyn y Fan Fach under the Black Mountain, married a farmer of Myddfai and went back into the lake with her cattle when he struck her three times without cause; before she left she taught her sons the secrets of healing. Myddfai today has a visitor centre and is famous for its honey and its herbs.",
 ], cy=[
    "Roedd Rhiwallon yn feddyg i Rys Gryg, arglwydd Dinefwr, yn yr 1230au, a chyda’i feibion Cadwgan, Gruffudd ac Einion ysgrifennodd feddyginiaethau o lysiau, mêl a phlanhigion y bryniau. Parhaodd y teulu’n feddygon yn y plwyf am ryw bum can mlynedd, a chofir yr olaf o’r llinach yn yr eglwys.",
    "Medd y stori i’w mam godi o Lyn y Fan Fach o dan y Mynydd Du, priodi ffermwr o Fyddfai a dychwelyd i’r llyn gyda’i gwartheg pan drawodd ef hi deirgwaith heb achos; cyn iddi fynd dysgodd gyfrinachau iacháu i’w meibion. Mae gan Fyddfai heddiw ganolfan ymwelwyr ac mae’n enwog am ei mêl a’i pherlysiau.",
 ]),
 "town-talley": dict(era="medieval", en=[
    "The abbey was planned on a great scale, but the canons never had the money to finish it, and only part of its church was built. The tall fragment of the central tower still stands over the ruins, with the two lakes glinting beyond it, one of the most peaceful places in Wales.",
    "The abbey was the burial place of some of the house of Dinefwr, and Welsh tradition holds that Dafydd ap Gwilym was buried at Talley, as others say Strata Florida. The church of the village stands beside the ruins, with its old box pews, and the lakes are now a nature reserve.",
 ], cy=[
    "Cynlluniwyd yr abaty ar raddfa fawr, ond ni chafodd y canoniaid fyth yr arian i’w orffen, a dim ond rhan o’i eglwys a godwyd. Mae darn uchel o’r tŵr canol yn dal i sefyll dros yr adfeilion, gyda’r ddau lyn yn disgleirio y tu hwnt, un o’r mannau mwyaf heddychlon yng Nghymru.",
    "Roedd yr abaty’n fan claddu rhai o dŷ Dinefwr, ac yn ôl traddodiad Cymreig claddwyd Dafydd ap Gwilym yn Nhalyllychau, fel y dywed eraill yn Ystrad Fflur. Saif eglwys y pentref wrth ymyl yr adfeilion, gyda’i hen gorau bocs, ac mae’r llynnoedd yn warchodfa natur heddiw.",
 ]),
 "town-llanarthne": dict(era="today", en=[
    "Dryslwyn was raised on a rock in the Tywi valley by the princes of Deheubarth in the 1220s, and it was the stronghold of Rhys ap Maredudd, who rose against the king in 1287. Paxton’s Tower, a folly of the early 1800s, was built by Sir William Paxton in honour of Nelson, and the views from it take in seven counties.",
    "The Botanic Garden was made on the old estate of Middleton Hall, which Paxton owned. Its Great Glasshouse, designed by Norman Foster, holds plants from the Mediterranean climates of the world, and the garden is a centre for saving the rare plants of Wales.",
 ], cy=[
    "Codwyd Dryslwyn ar graig yn nyffryn Tywi gan dywysogion Deheubarth yn yr 1220au, a hwn oedd cadarnle Rhys ap Maredudd, a gododd yn erbyn y brenin yn 1287. Codwyd Tŵr Paxton, ffoli o ddechrau’r 1800au, gan Syr William Paxton er anrhydedd i Nelson, ac mae’r golygfeydd ohono’n cynnwys saith sir.",
    "Gwnaed yr Ardd Fotaneg ar hen ystâd Neuadd Middleton, a oedd yn eiddo i Paxton. Mae ei Thŷ Gwydr Mawr, a gynlluniwyd gan Norman Foster, yn dal planhigion o hinsoddau Môr y Canoldir y byd, ac mae’r ardd yn ganolfan i achub planhigion prin Cymru.",
 ]),
 # ---------- Pembrokeshire ----------
 "town-st-dogmaels": dict(era="saints", en=[
    "Dogfael was a grandson of Cunedda, the forefather of the kings of Gwynedd, and his church here was a Welsh clas before the Normans brought the monks of Tiron. The abbey ruins stand in the heart of the village, with its north porch and the carved figures of its walls, and the Sagranus stone stands in the church beside it.",
    "The Ogham on the Sagranus stone and its Latin say the same thing, the name of Sagranus son of Cunotamus, so the stone worked like a Rosetta Stone for the Ogham alphabet. The village looks across the Teifi to Cardigan, and Poppit Sands lies at the river mouth, where the Pembrokeshire Coast Path begins.",
 ], cy=[
    "Roedd Dogfael yn ŵyr i Gunedda, cyndad brenhinoedd Gwynedd, a chlas Cymreig oedd ei eglwys yma cyn i’r Normaniaid ddod â mynaich Tiron. Saif adfeilion yr abaty yng nghanol y pentref, gyda’i gyntedd gogleddol a delwau cerfiedig ei furiau, ac mae Carreg Sagranus yn sefyll yn yr eglwys wrth ei ymyl.",
    "Mae’r Ogam ar Garreg Sagranus a’r Lladin yn dweud yr un peth, enw Sagranus fab Cunotamus, felly gweithiodd y garreg fel Carreg Rosetta i’r wyddor Ogam. Mae’r pentref yn edrych ar draws y Teifi at Aberteifi, ac mae Traeth Poppit yng ngheg yr afon, lle mae Llwybr Arfordir Penfro’n dechrau.",
 ]),
 "town-nevern": dict(era="saints", en=[
    "Brynach, an Irish saint and friend of Dewi, founded his church here in the 500s, and the Life of Brynach says he talked with angels on Carn Ingli, the mountain above Newport. The cross, nearly 13 feet tall, is carved all over with knotwork, and the Maglocunus stone in the church, in Latin and Ogham, names a man called Maglocunus son of Clutorius.",
    "On the castle hill above the village stand the earthworks of the castle of the Lord Rhys, which he took from the Normans in 1191. The bleeding yew in the avenue to the church weeps a red sap, and the pilgrims’ cross cut into the rock on the old path to St Davids marks Nevern as a stop on the road to Mynyw.",
 ], cy=[
    "Sefydlodd Brynach, sant Gwyddelig a chyfaill i Ddewi, ei eglwys yma yn y 500au, ac mae Buchedd Brynach yn dweud iddo siarad ag angylion ar Garn Ingli, y mynydd uwchben Trefdraeth. Mae’r groes, bron i 13 troedfedd o uchder, wedi’i cherfio drosti â chlymwaith, ac mae carreg Maglocunus yn yr eglwys, yn Lladin ac Ogam, yn enwi dyn o’r enw Maglocunus fab Clutorius.",
    "Ar fryn y castell uwchben y pentref saif gwrthgloddiau castell yr Arglwydd Rhys, a gipiodd ef oddi ar y Normaniaid yn 1191. Mae’r ywen sy’n gwaedu yn y rhodfa at yr eglwys yn wylo sudd coch, ac mae croes y pererinion a dorrwyd yn y graig ar yr hen lwybr i Dyddewi yn nodi Nanhyfer fel arhosfan ar y ffordd i Fynyw.",
 ]),
 "town-manorbier": dict(era="medieval", en=[
    "Gerald’s father was a Norman lord, William de Barri, and his mother Angharad was a granddaughter of Rhys ap Tewdwr, king of Deheubarth, through the princess Nest. He wrote that from the castle you could see the ships, the sea, the fishpond, the orchard and the church, and that of all the lands of Wales, Dyfed was the most beautiful, and Manorbier the most delightful part of Dyfed.",
    "The castle is still lived in and stands almost complete above the beach. On the cliff to the east lies the King’s Quoit, a Stone Age burial chamber, and the church on the far side of the valley has a tall, thin medieval tower.",
 ], cy=[
    "Arglwydd Normanaidd oedd tad Gerallt, William de Barri, ac roedd ei fam Angharad yn wyres i Rys ap Tewdwr, brenin Deheubarth, drwy’r dywysoges Nest. Ysgrifennodd y gallech weld o’r castell y llongau, y môr, y pysgodlyn, y berllan a’r eglwys, ac mai Dyfed oedd y harddaf o holl diroedd Cymru, a Maenorbŷr y rhan hyfrytaf o Ddyfed.",
    "Mae pobl yn dal i fyw yn y castell ac mae’n sefyll bron yn gyfan uwchben y traeth. Ar y clogwyn i’r dwyrain gorwedd Coetan y Brenin, siambr gladdu o Oes y Cerrig, ac mae gan yr eglwys ar ochr draw’r cwm dŵr canoloesol uchel, main.",
 ]),
 "town-carew": dict(era="kings", en=[
    "The cross stands nearly 14 feet high, and its Latin inscription reads ‘Margiteut Rex Etg(uin) filius’, Maredudd the king, son of Edwin. Maredudd was a descendant of Hywel Dda and ruled Deheubarth with his brother until he was killed in battle in 1035; it is one of the finest early crosses in Wales.",
    "The castle grew from a Norman fort into a Tudor palace, and Rhys ap Thomas, who had helped Henry Tudor win at Bosworth, held his great feast and tournament of St George there in 1507, with jousting, music and hundreds of guests. The tidal mill by the castle, the only one restored in Wales, ground corn with the ebb of the tide.",
 ], cy=[
    "Saif y groes bron i 14 troedfedd o uchder, ac mae ei harysgrif Ladin yn darllen ‘Margiteut Rex Etg(uin) filius’, Maredudd y brenin, mab Edwin. Roedd Maredudd yn un o ddisgynyddion Hywel Dda a theyrnasai dros Ddeheubarth gyda’i frawd nes iddo gael ei ladd mewn brwydr yn 1035; mae’n un o groesau cynnar gorau Cymru.",
    "Tyfodd y castell o gaer Normanaidd yn blas Tuduraidd, a chynhaliodd Rhys ap Thomas, a helpodd Harri Tudur i ennill yn Bosworth, ei wledd fawr a’i dwrnamaint Gŵyl Sant Siôr yno yn 1507, gyda thwrneimant, cerddoriaeth a channoedd o westeion. Malai’r felin lanw wrth y castell, yr unig un a adferwyd yng Nghymru, ŷd gyda thrai’r llanw.",
 ]),
}

PEOPLE = {
 "town-llanfihangel-yng-ngwynfa": ["person-ann-griffiths"],
 "town-llangeitho": ["person-daniel-rowland", "person-thomas-charles"],
 "town-manorbier": ["person-gerallt-gymro"],
 "town-pencader": ["person-gerallt-gymro"],
 "town-meifod": ["person-madog-ap-maredudd"],
 "town-myddfai": ["person-meddygon-myddfai"],
 "town-carew": ["person-rhys-ap-thomas"],
 "town-nevern": ["person-brynach"],
}
