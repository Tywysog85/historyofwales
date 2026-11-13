# Canonical content for History of Wales. build.py turns this into the site.
# Text inside strings uses curly quotes ‘ ’ so it never clashes with code quotes.

ERAS = [
  dict(id="ancient", en="Ancient Wales", cy="Cymru Hynafol", spanEn="230,000 BC – 600 AD", spanCy="230,000 CC – 600 OC", ill="dolmen",
    blurbEn="Ice-age hunters, tomb builders, hillfort tribes and the long shadow of Rome.",
    blurbCy="Helwyr oes yr iâ, codwyr beddrodau, llwythau’r bryngaerau a chysgod hir Rhufain.",
    storyEn=[
      "People reached the land we call Wales long before it was an island. Neanderthals sheltered at Pontnewydd Cave in Denbighshire around 230,000 years ago, and modern humans buried a young man in red ochre at Paviland on Gower some 33,000 years ago. As the ice retreated, farmers arrived, cleared woodland and raised great stone tombs such as Pentre Ifan and Bryn Celli Ddu.",
      "Bronze Age miners dug kilometres of tunnels for copper on the Great Orme, and by the Iron Age the hills were crowned with forts held by tribes the Romans would name: the Silures, Ordovices, Demetae and Deceangli. Rome needed some thirty years to subdue them, attacking the druids on Ynys Môn in 60 AD. When the legions left, saints such as Dewi founded churches, and the Brittonic speech of these people began to turn into Welsh."],
    storyCy=[
      "Cyrhaeddodd pobl y tir a alwn yn Gymru ymhell cyn iddo fod yn ynys. Cysgododd Neanderthaliaid yn Ogof Bontnewydd yn Sir Ddinbych tua 230,000 o flynyddoedd yn ôl, a chladdodd bodau dynol modern ddyn ifanc mewn ocr coch ym Mhafiland ar Benrhyn Gŵyr tua 33,000 o flynyddoedd yn ôl. Wrth i’r iâ gilio, daeth ffermwyr i glirio’r coedwigoedd a chodi beddrodau mawr o gerrig fel Pentre Ifan a Bryn Celli Ddu.",
      "Cloddiodd mwynwyr Oes yr Efydd gilometrau o dwneli i chwilio am gopr ar y Gogarth, ac erbyn Oes yr Haearn roedd caerau ar ben y bryniau, yn nwylo llwythau y byddai’r Rhufeiniaid yn eu henwi: y Silwriaid, yr Ordofigiaid, y Demetae a’r Deceangli. Cymerodd Rhufain tua deng mlynedd ar hugain i’w trechu, gan ymosod ar y derwyddon ar Ynys Môn yn 60 OC. Pan adawodd y llengoedd, sefydlodd seintiau fel Dewi eglwysi, a dechreuodd iaith Frythoneg y bobl hyn droi’n Gymraeg."]),
  dict(id="medieval", en="The Age of Princes", cy="Oes y Tywysogion", spanEn="600 – 1485", spanCy="600 – 1485", ill="castle",
    blurbEn="Kingdoms, law, poetry and the long struggle against Norman and English power.",
    blurbCy="Teyrnasoedd, cyfraith, barddoniaeth a’r frwydr hir yn erbyn grym y Normaniaid a Lloegr.",
    storyEn=[
      "Early medieval Wales was a patchwork of kingdoms: Gwynedd, Powys, Deheubarth, Morgannwg and others. Strong rulers such as Rhodri Mawr and Hywel Dda brought several together, and Hywel’s name was attached to a body of Welsh law that lasted for centuries. In 1055 Gruffudd ap Llywelyn became the only king ever to rule all of Wales.",
      "The Normans pushed into the south and east after 1066, building castles and lordships in the March. The princes of Gwynedd, Llywelyn Fawr and his grandson Llywelyn ap Gruffudd, came closest to a single Welsh state, until Llywelyn’s death at Cilmeri in 1282 and Edward I’s ring of castles ended independence. A century later Owain Glyndŵr’s great rising briefly revived it, with a parliament at Machynlleth and plans for a Welsh church and universities."],
    storyCy=[
      "Roedd Cymru’r Oesoedd Canol cynnar yn glytwaith o deyrnasoedd: Gwynedd, Powys, Deheubarth, Morgannwg ac eraill. Unodd rheolwyr cryf fel Rhodri Mawr a Hywel Dda sawl un ohonynt, a rhoddwyd enw Hywel ar gorff o gyfraith Gymreig a barhaodd am ganrifoedd. Yn 1055 daeth Gruffudd ap Llywelyn yr unig frenin erioed i reoli Cymru gyfan.",
      "Gwthiodd y Normaniaid i’r de a’r dwyrain ar ôl 1066, gan godi cestyll ac arglwyddiaethau yn y Mers. Daeth tywysogion Gwynedd, Llywelyn Fawr a’i ŵyr Llywelyn ap Gruffudd, agosaf at greu un wladwriaeth Gymreig, nes i farwolaeth Llywelyn yng Nghilmeri yn 1282 a chylch cestyll Edward I roi terfyn ar annibyniaeth. Ganrif yn ddiweddarach, adfywiodd gwrthryfel mawr Owain Glyndŵr y freuddwyd am gyfnod, gyda senedd ym Machynlleth a chynlluniau am eglwys a phrifysgolion Cymreig."]),
  dict(id="industrial", en="Tudors to Industry", cy="Y Tuduriaid a Diwydiant", spanEn="1485 – 1914", spanCy="1485 – 1914", ill="wheel",
    blurbEn="A Welsh king, union with England, a Welsh Bible, then iron, coal and revolt.",
    blurbCy="Brenin o Gymro, uno â Lloegr, Beibl Cymraeg, yna haearn, glo a gwrthryfel.",
    storyEn=[
      "Henry Tudor, born at Pembroke, marched through Wales to take the English crown in 1485, and many Welsh people saw the prophecy of a Welsh king fulfilled. His son’s Acts of Union absorbed Wales into England and made English the language of power. Yet the 1588 Welsh Bible, the circulating schools and the Methodist revival made the Welsh one of the most literate peoples in Europe and kept the language alive in chapel and home.",
      "From the 1750s Wales became an industrial powerhouse. Merthyr Tydfil was the iron capital of the world, slate from Gwynedd roofed cities across the globe, and by 1913 the south Wales coalfield was exporting more coal than anywhere on earth. Industry brought hardship and protest too: the Merthyr Rising, the Chartists at Newport and the Rebecca Riots all shaped a radical Welsh politics."],
    storyCy=[
      "Gorymdeithiodd Harri Tudur, a aned ym Mhenfro, drwy Gymru i gipio coron Lloegr yn 1485, a gwelodd llawer o Gymry wireddu’r broffwydoliaeth am frenin o Gymro. Ymgorfforodd Deddfau Uno ei fab Gymru yn Lloegr a gwneud Saesneg yn iaith grym. Er hynny, gwnaeth Beibl Cymraeg 1588, yr ysgolion cylchynol a’r diwygiad Methodistaidd y Cymry yn un o bobloedd mwyaf llythrennog Ewrop, gan gadw’r iaith yn fyw yn y capel a’r cartref.",
      "O’r 1750au ymlaen daeth Cymru’n bwerdy diwydiannol. Merthyr Tudful oedd prifddinas haearn y byd, toeodd llechi Gwynedd ddinasoedd ar draws y byd, ac erbyn 1913 roedd maes glo’r de yn allforio mwy o lo nag unman arall ar y ddaear. Daeth diwydiant â chaledi a phrotest hefyd: lluniodd Gwrthryfel Merthyr, y Siartwyr yng Nghasnewydd a Helyntion Beca wleidyddiaeth radical Gymreig."]),
  dict(id="modern", en="Modern Wales", cy="Cymru Fodern", spanEn="1914 – today", spanCy="1914 – heddiw", ill="senedd",
    blurbEn="War, depression, the NHS, the fight for the language and the return of a Welsh parliament.",
    blurbCy="Rhyfel, dirwasgiad, y Gwasanaeth Iechyd, yr ymgyrch dros yr iaith a senedd i Gymru unwaith eto.",
    storyEn=[
      "The 20th century began at the peak of coal and ended with almost every pit closed. Wales gave Britain a wartime prime minister in David Lloyd George and, through Aneurin Bevan of Tredegar, the National Health Service. The Depression drove hundreds of thousands to leave, and tragedies at Senghenydd, Gresford and Aberfan are still remembered in every valley.",
      "The drowning of Capel Celyn and Saunders Lewis’s warning about the fate of the language sparked a national movement. Campaigners won Welsh-medium schools, bilingual road signs, S4C and official status for Welsh. After a heavy defeat in 1979, devolution was won by a whisker in 1997, and the Senedd now makes laws for Wales from Cardiff Bay."],
    storyCy=[
      "Dechreuodd yr ugeinfed ganrif ar anterth y diwydiant glo a daeth i ben gyda bron pob pwll wedi cau. Rhoddodd Cymru brif weinidog adeg rhyfel i Brydain yn David Lloyd George ac, drwy Aneurin Bevan o Dredegar, y Gwasanaeth Iechyd Gwladol. Gyrrodd y Dirwasgiad gannoedd o filoedd o bobl i adael, ac mae trychinebau Senghennydd, Gresffordd ac Aberfan yn dal yn y cof ym mhob cwm.",
      "Taniodd boddi Capel Celyn a rhybudd Saunders Lewis am dynged yr iaith fudiad cenedlaethol. Enillodd ymgyrchwyr ysgolion Cymraeg, arwyddion ffyrdd dwyieithog, S4C a statws swyddogol i’r Gymraeg. Ar ôl colli’n drwm yn 1979, enillwyd datganoli o drwch blewyn yn 1997, ac mae’r Senedd bellach yn gwneud cyfreithiau i Gymru o Fae Caerdydd."]),
]

# (era, year, circa, endYear, day 'MM-DD' or '', titleEn, titleCy, bodyEn, bodyCy, key, placeId, wikipediaTitle)
EVENTS = [
 ("ancient",-230000,1,0,"","Neanderthals at Pontnewydd","Neanderthaliaid Pontnewydd",
  "Teeth found in Pontnewydd Cave, Denbighshire, are the oldest human remains in Wales.",
  "Dannedd a gafwyd yn Ogof Bontnewydd, Sir Ddinbych, yw’r olion dynol hynaf yng Nghymru.",1,"pontnewydd","Pontnewydd_Cave"),
 ("ancient",-31000,1,0,"","The Red Lady of Paviland","Dynes Goch Pafiland",
  "A young man is buried in red ochre in a Gower cave. Found in 1823 and first thought to be a woman, he is Britain’s oldest known ceremonial burial.",
  "Claddwyd dyn ifanc mewn ocr coch mewn ogof ar Benrhyn Gŵyr. Cafwyd hyd iddo yn 1823 a thybiwyd i ddechrau mai menyw ydoedd. Dyma’r gladdedigaeth seremonïol hynaf y gwyddys amdani ym Mhrydain.",0,"paviland","Red_Lady_of_Paviland"),
 ("ancient",-3500,1,0,"","Builders of the dolmens","Codwyr y cromlechi",
  "Farming communities raise stone tombs such as Pentre Ifan. Later, bluestones from the Preseli Hills are carried to Stonehenge.",
  "Mae cymunedau amaethyddol yn codi beddrodau cerrig fel Pentre Ifan. Yn ddiweddarach, cludir cerrig gleision o’r Preseli i Gôr y Cewri.",0,"pentreifan","Pentre_Ifan"),
 ("ancient",-2000,1,0,"","Copper from the Great Orme","Copr o’r Gogarth",
  "Bronze Age miners begin digging what becomes one of the largest prehistoric mines in the world.[[cite:orme-antiquity,orme-gsl,orme-guinness]]",
  "Mae mwynwyr Oes yr Efydd yn dechrau cloddio un o’r mwyngloddiau cynhanesyddol mwyaf yn y byd.[[cite:orme-antiquity,orme-gsl,orme-guinness]]",0,"orme","Great_Orme_Mines"),
 ("ancient",-600,1,0,"","The hillfort tribes","Llwythau’r bryngaerau",
  "Iron Age peoples, among them the Silures, Ordovices, Demetae and Deceangli, build hundreds of hillforts across Wales.",
  "Mae pobloedd Oes yr Haearn, yn eu plith y Silwriaid, yr Ordofigiaid, y Demetae a’r Deceangli, yn codi cannoedd o fryngaerau ledled Cymru.",0,"","Prehistoric_Wales"),
 ("ancient",51,0,0,"","Caratacus’s last stand","Brwydr olaf Caradog",
  "The British king, fighting with the Silures and Ordovices, is defeated by Rome and later betrayed.",
  "Mae’r brenin Brythonig, yn ymladd gyda’r Silwriaid a’r Ordofigiaid, yn cael ei drechu gan Rufain ac yna’n cael ei fradychu.",0,"","Caratacus"),
 ("ancient",60,0,0,"","Rome attacks Ynys Môn","Rhufain yn ymosod ar Ynys Môn",
  "Roman troops cross the Menai Strait to destroy the druids’ stronghold. Wales is under Roman control by about 78 AD.",
  "Mae milwyr Rhufain yn croesi’r Fenai i ddinistrio cadarnle’r derwyddon. Erbyn tua 78 OC mae Cymru dan reolaeth Rhufain.",1,"","Wales_in_the_Roman_era"),
 ("ancient",383,0,0,"","Macsen Wledig","Macsen Wledig",
  "Magnus Maximus, a commander in Britain, is proclaimed emperor and becomes a founding figure in Welsh legend.",
  "Cyhoeddir Magnus Maximus, cadlywydd ym Mhrydain, yn ymerawdwr. Daw’n un o arwyr sylfaenol chwedloniaeth Cymru.",0,"","Magnus_Maximus"),
 ("ancient",589,1,0,"03-01","Death of Saint David","Marw Dewi Sant",
  "Dewi dies, traditionally on 1 March, at the monastery that becomes St Davids, the smallest city in Britain.",
  "Bu farw Dewi, yn ôl traddodiad ar 1 Mawrth, yn ei fynachlog, lle saif Tyddewi heddiw, dinas leiaf Prydain.",0,"stdavids","Saint_David"),
 ("medieval",600,1,0,"","Y Gododdin","Y Gododdin",
  "Aneirin’s elegy for warriors who fell at Catraeth, among the oldest poetry in any language of Britain.",
  "Marwnad Aneirin i’r rhyfelwyr a syrthiodd yng Nghatraeth, ymhlith y farddoniaeth hynaf mewn unrhyw iaith ym Mhrydain.",1,"","Y_Gododdin"),
 ("medieval",616,1,0,"","Battle of Chester","Brwydr Caer",
  "Northumbrian victory separates the Britons of Wales from their kin in the north. The Welsh begin calling themselves Cymry, ‘fellow countrymen’.",
  "Mae buddugoliaeth Northumbria yn gwahanu Brythoniaid Cymru oddi wrth eu perthnasau yn y gogledd. Daw’r bobl i alw eu hunain yn Gymry, sef ‘cyd-wladwyr’.",0,"","Battle_of_Chester"),
 ("medieval",784,1,0,"","Offa’s Dyke","Clawdd Offa",
  "The King of Mercia raises an earthwork along the border, marking a line between Welsh and English that still roughly holds.",
  "Mae brenin Mersia yn codi clawdd ar hyd y ffin, gan nodi llinell rhwng y Cymry a’r Saeson sy’n dal yn fras hyd heddiw.",0,"","Offa%27s_Dyke"),
 ("medieval",856,0,0,"","Rhodri Mawr defeats the Vikings","Rhodri Mawr yn trechu’r Llychlynwyr",
  "Rhodri the Great kills the Danish leader Horm on Anglesey and rules much of Wales.",
  "Mae Rhodri Mawr yn lladd yr arweinydd Danaidd Horm ar Ynys Môn ac yn rheoli rhan helaeth o Gymru.",0,"","Rhodri_the_Great"),
 ("medieval",945,1,0,"","The laws of Hywel Dda","Cyfraith Hywel Dda",
  "Welsh law is gathered under Hywel the Good and stays in use for some six hundred years.",
  "Casglir cyfraith Cymru dan Hywel Dda, a bydd yn cael ei defnyddio am ryw chwe chan mlynedd.",1,"hendygwyn","Welsh_law"),
 ("medieval",1055,0,0,"","One king for all Wales","Un brenin i Gymru gyfan",
  "Gruffudd ap Llywelyn becomes the only king ever to unite all of Wales, until his death in 1063.",
  "Mae Gruffudd ap Llywelyn yn uno Cymru gyfan dan ei goron, yr unig frenin erioed i wneud hynny, hyd ei farwolaeth yn 1063.",0,"","Gruffydd_ap_Llywelyn"),
 ("medieval",1081,0,0,"","Battle of Mynydd Carn","Brwydr Mynydd Carn",
  "Gruffudd ap Cynan and Rhys ap Tewdwr win back their kingdoms of Gwynedd and Deheubarth.",
  "Mae Gruffudd ap Cynan a Rhys ap Tewdwr yn adennill eu teyrnasoedd, Gwynedd a Deheubarth.",0,"","Battle_of_Mynydd_Carn"),
 ("medieval",1136,0,0,"","Gwenllian and the Great Revolt","Gwenllian a’r Gwrthryfel Mawr",
  "Princess Gwenllian dies fighting the Normans at Kidwelly. Months later the Welsh rout them at Crug Mawr.",
  "Lladdwyd y Dywysoges Gwenllian wrth ymladd y Normaniaid ger Cydweli. Fisoedd yn ddiweddarach mae’r Cymry’n eu trechu yng Nghrug Mawr.",0,"","Gwenllian_ferch_Gruffydd"),
 ("medieval",1176,0,0,"12-25","The first eisteddfod","Yr eisteddfod gyntaf",
  "At Christmas, the Lord Rhys hosts a contest of poets and musicians at Cardigan Castle.",
  "Adeg y Nadolig, mae’r Arglwydd Rhys yn cynnal cystadleuaeth i feirdd a cherddorion yng Nghastell Aberteifi.",1,"cardigan","Eisteddfod"),
 ("medieval",1188,0,0,"","Gerald’s journey","Taith Gerallt",
  "Gerald of Wales tours the country recruiting for the Crusade and writes the most vivid surviving portrait of medieval Wales.",
  "Mae Gerallt Gymro yn teithio’r wlad yn recriwtio ar gyfer y Groesgad, ac yn ysgrifennu’r darlun mwyaf byw sydd wedi goroesi o Gymru’r Oesoedd Canol.",0,"","Gerald_of_Wales"),
 ("medieval",1218,0,0,"","Llywelyn Fawr supreme","Llywelyn Fawr yn ben",
  "The Treaty of Worcester confirms Llywelyn the Great as the dominant ruler in Wales.",
  "Mae Cytundeb Caerwrangon yn cadarnhau Llywelyn Fawr yn brif reolwr Cymru.",0,"","Llywelyn_the_Great"),
 ("medieval",1267,0,0,"09-29","Treaty of Montgomery","Cytundeb Trefaldwyn",
  "Henry III recognises Llywelyn ap Gruffudd as Prince of Wales.",
  "Mae Harri III yn cydnabod Llywelyn ap Gruffudd yn Dywysog Cymru.",0,"","Treaty_of_Montgomery"),
 ("medieval",1282,0,0,"12-11","Death at Cilmeri","Marwolaeth yng Nghilmeri",
  "Llywelyn is killed in an ambush near Builth on 11 December. Independent native rule ends.",
  "Lladdwyd Llywelyn mewn cyrch ger Llanfair-ym-Muallt ar 11 Rhagfyr. Daw rheolaeth frodorol annibynnol i ben.",1,"cilmeri","Llywelyn_ap_Gruffudd"),
 ("medieval",1283,0,0,"","Edward’s ring of iron","Cylch haearn Edward",
  "Edward I begins Conwy, Caernarfon and Harlech. The Statute of Rhuddlan follows in 1284.",
  "Mae Edward I yn dechrau codi Conwy, Caernarfon a Harlech. Daw Statud Rhuddlan yn 1284.",0,"caernarfon","Castles_and_Town_Walls_of_King_Edward_in_Gwynedd"),
 ("medieval",1301,0,0,"02-07","An English Prince of Wales","Tywysog Cymru o Sais",
  "Edward of Caernarfon, the king’s son, is made Prince of Wales, the first heir to the English throne to hold the title.",
  "Gwneir Edward o Gaernarfon, mab y brenin, yn Dywysog Cymru, yr etifedd cyntaf i orsedd Lloegr i ddal y teitl.",0,"","Edward_II_of_England"),
 ("medieval",1349,0,0,"","The Black Death","Y Pla Du",
  "Plague kills perhaps a third of the people of Wales and shakes the old social order.",
  "Mae’r pla yn lladd efallai draean o bobl Cymru ac yn ysgwyd yr hen drefn gymdeithasol.",0,"","Black_Death"),
 ("medieval",1400,0,0,"09-16","Glyndŵr’s rising","Gwrthryfel Glyndŵr",
  "Owain Glyndŵr is proclaimed Prince of Wales on 16 September and leads a revolt that lasts more than a decade.",
  "Cyhoeddir Owain Glyndŵr yn Dywysog Cymru ar 16 Medi, ac mae’n arwain gwrthryfel sy’n para dros ddeng mlynedd.",1,"harlech","Owain_Glynd%C5%B5r"),
 ("medieval",1404,0,0,"","Parliament at Machynlleth","Senedd Machynlleth",
  "Glyndŵr is crowned and gathers a Welsh parliament. He seeks an alliance with France.",
  "Coronir Glyndŵr ac mae’n galw senedd Gymreig ynghyd. Mae’n ceisio cynghrair â Ffrainc.",0,"machynlleth","Machynlleth"),
 ("industrial",1485,0,0,"08-07","A Welsh king","Brenin o Gymro",
  "Henry Tudor lands near Dale in Pembrokeshire and marches through Wales to win at Bosworth.",
  "Mae Harri Tudur yn glanio ger Dale yn Sir Benfro ac yn gorymdeithio drwy Gymru i ennill ym Mosworth.",1,"dale","Henry_VII_of_England"),
 ("industrial",1536,0,1543,"","The Laws in Wales Acts","Y Deddfau Uno",
  "Wales is annexed to England. English becomes the language of law and office.",
  "Mae Cymru’n cael ei chyfeddiannu i Loegr. Daw Saesneg yn iaith y gyfraith a swyddi cyhoeddus.",1,"","Laws_in_Wales_Acts_1535_and_1542"),
 ("industrial",1546,0,0,"","The first Welsh book","Y llyfr Cymraeg cyntaf",
  "Sir John Price prints ‘Yny lhyvyr hwnn’, a short book of prayers and the alphabet.",
  "Mae Syr John Prys yn argraffu ‘Yny lhyvyr hwnn’, llyfr bach o weddïau a’r wyddor.",0,"","Yny_lhyvyr_hwnn"),
 ("industrial",1567,0,0,"","The New Testament in Welsh","Y Testament Newydd yn Gymraeg",
  "William Salesbury’s translation is published, the first scripture printed in Welsh.",
  "Cyhoeddir cyfieithiad William Salesbury, yr ysgrythur gyntaf i’w hargraffu yn Gymraeg.",0,"","William_Salesbury"),
 ("industrial",1588,0,0,"","The Welsh Bible","Y Beibl Cymraeg",
  "William Morgan’s translation sets the standard for literary Welsh and helps the language survive.",
  "Mae cyfieithiad William Morgan yn gosod safon y Gymraeg lenyddol ac yn helpu’r iaith i oroesi.",1,"llanrhaeadr","William_Morgan_(bishop)"),
 ("industrial",1648,0,0,"05-08","Battle of St Fagans","Brwydr Sain Ffagan",
  "The largest battle of the Civil Wars in Wales ends in defeat for the royalist rising.",
  "Mae brwydr fwyaf y Rhyfeloedd Cartref yng Nghymru yn gorffen gyda threchu gwrthryfel y brenhinwyr.",0,"","Battle_of_St_Fagans"),
 ("industrial",1731,0,0,"","The circulating schools","Yr ysgolion cylchynol",
  "Griffith Jones begins schools that move from parish to parish, teaching many thousands to read Welsh.",
  "Mae Griffith Jones yn dechrau ysgolion sy’n symud o blwyf i blwyf, gan ddysgu miloedd lawer i ddarllen Cymraeg.",0,"","Griffith_Jones_(Llanddowror)"),
 ("industrial",1735,0,0,"","The Methodist revival","Y diwygiad Methodistaidd",
  "Howell Harris and Daniel Rowland start a movement that reshapes Welsh religion, music and politics.",
  "Mae Hywel Harris a Daniel Rowland yn cychwyn mudiad sy’n ail-lunio crefydd, cerddoriaeth a gwleidyddiaeth Cymru.",0,"","Howell_Harris"),
 ("industrial",1759,0,0,"","Iron at Merthyr","Haearn ym Merthyr",
  "The Dowlais ironworks is founded. Within decades Merthyr Tydfil is the largest town in Wales.",
  "Sefydlir gwaith haearn Dowlais. O fewn degawdau, Merthyr Tudful yw tref fwyaf Cymru.",0,"merthyr","Dowlais_Ironworks"),
 ("industrial",1797,0,0,"02-22","The last invasion of Britain","Y goresgyniad olaf",
  "A French force lands near Fishguard and surrenders within two days. Jemima Nicholas becomes a legend.",
  "Mae llu Ffrengig yn glanio ger Abergwaun ac yn ildio o fewn deuddydd. Daw Jemima Nicholas yn chwedl.",0,"fishguard","Battle_of_Fishguard"),
 ("industrial",1805,0,0,"11-26","Pontcysyllte opens","Agor Pontcysyllte",
  "Thomas Telford’s aqueduct carries the canal 38 metres above the River Dee.",
  "Mae traphont ddŵr Thomas Telford yn cario’r gamlas 38 metr uwchben Afon Dyfrdwy.",0,"pontcysyllte","Pontcysyllte_Aqueduct"),
 ("industrial",1831,0,0,"06-03","The Merthyr Rising","Gwrthryfel Merthyr",
  "Workers seize Merthyr and raise the red flag. Dic Penderyn is hanged in Cardiff.",
  "Mae gweithwyr yn cipio Merthyr ac yn codi’r faner goch. Crogir Dic Penderyn yng Nghaerdydd.",1,"merthyr","Merthyr_Rising"),
 ("industrial",1839,0,0,"11-04","Newport and Rebecca","Casnewydd a Merched Beca",
  "Chartists march on Newport and are fired upon. In the west, the Rebecca Rioters, dressed as women, smash tollgates.",
  "Mae’r Siartwyr yn gorymdeithio ar Gasnewydd ac yn cael eu saethu. Yn y gorllewin, mae Merched Beca, wedi’u gwisgo fel menywod, yn chwalu tollbyrth.",0,"","Newport_Rising"),
 ("industrial",1847,0,0,"","The Treachery of the Blue Books","Brad y Llyfrau Gleision",
  "A government report blames Welsh for the people’s supposed backwardness, provoking lasting anger.",
  "Mae adroddiad gan y llywodraeth yn beio’r Gymraeg am ‘anwybodaeth’ honedig y bobl, gan ennyn dicter hirhoedlog.",0,"","Treachery_of_the_Blue_Books"),
 ("industrial",1856,0,0,"","Hen Wlad Fy Nhadau","Hen Wlad Fy Nhadau",
  "Evan and James James of Pontypridd write the song that becomes the national anthem.",
  "Mae Evan a James James o Bontypridd yn cyfansoddi’r gân a ddaw’n anthem genedlaethol.",0,"","Hen_Wlad_Fy_Nhadau"),
 ("industrial",1865,0,0,"07-28","Y Wladfa","Y Wladfa",
  "The Mimosa lands 153 settlers in Patagonia. Welsh is still spoken in Argentina today.",
  "Mae’r Mimosa yn glanio 153 o ymfudwyr ym Mhatagonia. Mae’r Gymraeg yn dal i gael ei siarad yn yr Ariannin heddiw.",0,"","Y_Wladfa"),
 ("industrial",1872,0,0,"","A university for Wales","Prifysgol i Gymru",
  "University College Wales opens at Aberystwyth, paid for partly by the pennies of chapel-goers.",
  "Mae Coleg Prifysgol Cymru yn agor yn Aberystwyth, wedi’i dalu’n rhannol gan geiniogau aelodau’r capeli.",0,"","Aberystwyth_University"),
 ("industrial",1881,0,0,"","Sunday Closing Act","Deddf Cau ar y Sul",
  "The first Act of Parliament to treat Wales as a separate nation since the Tudors.",
  "Y Ddeddf Seneddol gyntaf ers y Tuduriaid i drin Cymru fel cenedl ar wahân.",0,"","Sunday_Closing_(Wales)_Act_1881"),
 ("industrial",1900,0,1903,"","The Penrhyn lockout","Streic Fawr y Penrhyn",
  "Quarrymen at Bethesda stay out for three years, the longest dispute in British industrial history.",
  "Mae chwarelwyr Bethesda allan am dair blynedd, yr anghydfod hiraf yn hanes diwydiannol Prydain.",0,"dinorwig","Penrhyn_Quarry"),
 ("industrial",1904,0,0,"","The great revival","Diwygiad 1904",
  "Evan Roberts leads a religious revival that fills chapels across Wales and spreads abroad.",
  "Mae Evan Roberts yn arwain diwygiad crefyddol sy’n llenwi capeli ledled Cymru ac yn lledu dramor.",0,"","1904%E2%80%931905_Welsh_revival"),
 ("industrial",1905,0,0,"12-16","Wales beat the All Blacks","Cymru’n curo’r Crysau Duon",
  "Wales win 3–0 at Cardiff Arms Park, and Cardiff is made a city the same year.",
  "Mae Cymru’n ennill o 3–0 ar Barc yr Arfau, a daw Caerdydd yn ddinas yr un flwyddyn.",0,"","Wales_national_rugby_union_team"),
 ("industrial",1910,0,0,"11-08","Tonypandy riots","Terfysgoedd Tonypandy",
  "Striking miners clash with police in the Rhondda, and troops are sent into the valleys.",
  "Mae glowyr ar streic yn gwrthdaro â’r heddlu yn y Rhondda, ac anfonir milwyr i’r cymoedd.",0,"","Tonypandy_riots"),
 ("modern",1913,0,0,"10-14","Senghenydd","Senghennydd",
  "An explosion at the Universal Colliery kills 439 men and boys, Britain’s worst mining disaster. Welsh coal output peaks the same year.",
  "Mae ffrwydrad ym Mhwll yr Universal yn lladd 439 o ddynion a bechgyn, y trychineb glofaol gwaethaf ym Mhrydain. Mae cynnyrch glo Cymru ar ei uchaf yr un flwyddyn.",1,"","Senghenydd_colliery_disaster"),
 ("modern",1916,0,0,"12-07","A Welsh prime minister","Prif weinidog o Gymro",
  "David Lloyd George, raised in Llanystumdwy, leads Britain through the end of the First World War.",
  "Mae David Lloyd George, a fagwyd yn Llanystumdwy, yn arwain Prydain drwy ddiwedd y Rhyfel Byd Cyntaf.",0,"","David_Lloyd_George"),
 ("modern",1920,0,0,"03-31","The Church in Wales","Yr Eglwys yng Nghymru",
  "The Anglican church in Wales is disestablished after decades of nonconformist campaigning.",
  "Datgysylltir yr eglwys Anglicanaidd yng Nghymru ar ôl degawdau o ymgyrchu gan yr Anghydffurfwyr.",0,"","Church_in_Wales"),
 ("modern",1922,0,0,"","The Urdd is founded","Sefydlu’r Urdd",
  "Ifan ab Owen Edwards starts Urdd Gobaith Cymru, now one of Europe’s largest youth movements.",
  "Mae Ifan ab Owen Edwards yn sefydlu Urdd Gobaith Cymru, un o fudiadau ieuenctid mwyaf Ewrop erbyn heddiw.",0,"","Urdd_Gobaith_Cymru"),
 ("modern",1925,0,0,"08-05","Plaid Cymru founded","Sefydlu Plaid Cymru",
  "A national party is formed at the eisteddfod in Pwllheli.",
  "Sefydlir plaid genedlaethol yn ystod yr eisteddfod ym Mhwllheli.",0,"","Plaid_Cymru"),
 ("modern",1934,0,0,"09-22","Gresford","Trychineb Gresffordd",
  "An explosion near Wrexham kills 266 miners.",
  "Mae ffrwydrad ger Wrecsam yn lladd 266 o lowyr.",0,"","Gresford_disaster"),
 ("modern",1936,0,0,"09-08","Fire at Penyberth","Tân yn Llŷn",
  "Saunders Lewis, Lewis Valentine and D. J. Williams set fire to an RAF bombing school in Llŷn and are jailed.",
  "Mae Saunders Lewis, Lewis Valentine a D. J. Williams yn rhoi ysgol fomio’r Awyrlu yn Llŷn ar dân, ac yn cael eu carcharu.",0,"","Penyberth"),
 ("modern",1941,0,0,"02-19","The Swansea Blitz","Blitz Abertawe",
  "Three nights of bombing in February destroy the centre of Swansea.",
  "Mae tair noson o fomio ym mis Chwefror yn dinistrio canol Abertawe.",0,"","Swansea_Blitz"),
 ("modern",1948,0,0,"07-05","The NHS","Y Gwasanaeth Iechyd",
  "Aneurin Bevan launches the National Health Service, inspired by the Tredegar Medical Aid Society.",
  "Mae Aneurin Bevan yn lansio’r Gwasanaeth Iechyd Gwladol, wedi’i ysbrydoli gan Gymdeithas Cymorth Meddygol Tredegar.",1,"","Aneurin_Bevan"),
 ("modern",1955,0,0,"12-20","Cardiff named capital","Caerdydd yn brifddinas",
  "Cardiff is proclaimed the capital city of Wales.",
  "Cyhoeddir Caerdydd yn brifddinas Cymru.",0,"","Cardiff"),
 ("modern",1962,0,0,"02-13","Tynged yr Iaith","Tynged yr Iaith",
  "Saunders Lewis’s radio lecture on the fate of the language leads to Cymdeithas yr Iaith, the Welsh Language Society.",
  "Mae darlith radio Saunders Lewis ar dynged yr iaith yn arwain at sefydlu Cymdeithas yr Iaith Gymraeg.",0,"","Tynged_yr_Iaith"),
 ("modern",1964,0,0,"","The Welsh Office","Y Swyddfa Gymreig",
  "Jim Griffiths becomes the first Secretary of State for Wales.",
  "Daw Jim Griffiths yn Ysgrifennydd Gwladol cyntaf Cymru.",0,"","Welsh_Office"),
 ("modern",1965,0,0,"10-21","Tryweryn","Boddi Tryweryn",
  "The village of Capel Celyn is flooded to supply Liverpool with water, despite near-unanimous opposition in Wales.",
  "Boddir pentref Capel Celyn i gyflenwi dŵr i Lerpwl, er gwaethaf gwrthwynebiad bron yn unfrydol yng Nghymru.",1,"celyn","Capel_Celyn"),
 ("modern",1966,0,0,"10-21","Aberfan","Trychineb Aberfan",
  "A coal tip collapses onto a village school on 21 October, killing 144 people, 116 of them children.",
  "Mae tomen lo yn llithro ar ysgol y pentref ar 21 Hydref, gan ladd 144 o bobl, 116 ohonynt yn blant.",1,"aberfan","Aberfan_disaster"),
 ("modern",1966,0,0,"07-14","Gwynfor Evans elected","Ethol Gwynfor Evans",
  "Plaid Cymru wins its first seat in Parliament, at the Carmarthen by-election.",
  "Mae Plaid Cymru yn ennill ei sedd gyntaf yn San Steffan, yn isetholiad Caerfyrddin.",0,"","Gwynfor_Evans"),
 ("modern",1967,0,0,"","Welsh Language Act","Deddf yr Iaith Gymraeg",
  "Welsh may be used in court, and official forms can appear in Welsh.",
  "Caniateir defnyddio’r Gymraeg yn y llys, a gall ffurflenni swyddogol ymddangos yn Gymraeg.",0,"","Welsh_Language_Act_1967"),
 ("modern",1969,0,0,"07-01","Investiture at Caernarfon","Arwisgo yng Nghaernarfon",
  "Prince Charles is invested as Prince of Wales amid protest and celebration.",
  "Arwisgir y Tywysog Charles yn Dywysog Cymru yng nghanol protestio a dathlu.",0,"caernarfon","Caernarfon_Castle"),
 ("modern",1979,0,0,"03-01","Devolution rejected","Gwrthod datganoli",
  "Wales votes four to one against a Welsh Assembly.",
  "Mae Cymru’n pleidleisio o bedwar i un yn erbyn Cynulliad i Gymru.",0,"","1979_Welsh_devolution_referendum"),
 ("modern",1982,0,0,"11-01","S4C goes on air","S4C ar yr awyr",
  "A Welsh-language television channel launches after Gwynfor Evans threatens a hunger strike.",
  "Mae sianel deledu Gymraeg yn dechrau darlledu ar ôl i Gwynfor Evans fygwth ymprydio.",0,"","S4C"),
 ("modern",1984,0,1985,"03-12","The miners’ strike","Streic y glowyr",
  "A year-long strike ends in defeat, and the closure of the coalfield accelerates.",
  "Mae streic a barodd flwyddyn yn gorffen mewn methiant, ac mae cau’r maes glo yn cyflymu.",0,"","UK_miners%27_strike_(1984%E2%80%931985)"),
 ("modern",1993,0,0,"","Welsh Language Act 1993","Deddf yr Iaith Gymraeg 1993",
  "Welsh and English are to be treated equally in public business in Wales.",
  "Mae’r Gymraeg a’r Saesneg i’w trin yn gyfartal mewn busnes cyhoeddus yng Nghymru.",0,"","Welsh_Language_Act_1993"),
 ("modern",1997,0,0,"09-18","Yes to devolution","Ie i ddatganoli",
  "Wales votes by 50.3% to create a National Assembly, which first meets in 1999.",
  "Mae Cymru’n pleidleisio o 50.3% i greu Cynulliad Cenedlaethol, sy’n cyfarfod am y tro cyntaf yn 1999.",1,"","1997_Welsh_devolution_referendum"),
 ("modern",2006,0,0,"03-01","The Senedd building opens","Agor adeilad y Senedd",
  "Richard Rogers’s slate-and-timber debating chamber opens on St David’s Day in Cardiff Bay.",
  "Mae siambr drafod Richard Rogers, o lechi a phren, yn agor ar Ddydd Gŵyl Dewi ym Mae Caerdydd.",0,"senedd","Senedd_building"),
 ("modern",2011,0,0,"03-03","Law-making powers","Pwerau deddfu",
  "A referendum gives the Assembly full law-making powers, and Welsh gains official status in Wales.",
  "Mae refferendwm yn rhoi pwerau deddfu llawn i’r Cynulliad, ac mae’r Gymraeg yn cael statws swyddogol yng Nghymru.",0,"","2011_Welsh_devolution_referendum"),
 ("modern",2020,0,0,"05-06","Senedd Cymru","Senedd Cymru",
  "The Assembly becomes the Welsh Parliament, Senedd Cymru.",
  "Daw’r Cynulliad yn Senedd Cymru.",1,"senedd","Senedd"),
]

PLACES = [
 dict(id="pontnewydd", en="Pontnewydd Cave", cy="Ogof Bontnewydd", era="ancient", lat=53.218, lon=-3.436, year="c. 230,000 BC", ill="cave", src="Pontnewydd_Cave",
  dEn="A limestone cave above the River Elwy where Neanderthal teeth were found, the oldest human remains in Wales and among the oldest in Britain.",
  dCy="Ogof galchfaen uwchben Afon Elwy lle cafwyd dannedd Neanderthal, yr olion dynol hynaf yng Nghymru ac ymhlith yr hynaf ym Mhrydain."),
 dict(id="paviland", en="Paviland Cave", cy="Ogof Pafiland", era="ancient", lat=51.549, lon=-4.255, year="c. 31,000 BC", ill="cave", src="Red_Lady_of_Paviland",
  dEn="Goat’s Hole, a sea cave on Gower, held the ‘Red Lady’, a young man buried with ivory and shells and stained with red ochre.",
  dCy="Yn Ogof yr Afr, ogof fôr ar Benrhyn Gŵyr, roedd ‘Dynes Goch’ Pafiland, dyn ifanc a gladdwyd gydag ifori a chregyn ac wedi’i liwio ag ocr coch."),
 dict(id="pentreifan", en="Pentre Ifan", cy="Pentre Ifan", era="ancient", lat=51.999, lon=-4.770, year="c. 3500 BC", ill="dolmen", src="Pentre_Ifan",
  dEn="A burial chamber whose 16-tonne capstone still balances on three uprights, looking out over the Preseli Hills where Stonehenge’s bluestones were quarried.",
  dCy="Siambr gladdu y mae ei maen capan 16 tunnell yn dal i gydbwyso ar dair carreg, gan edrych dros y Preseli lle chwarelwyd cerrig gleision Côr y Cewri."),
 dict(id="orme", en="Great Orme Mines", cy="Mwyngloddiau’r Gogarth", era="ancient", lat=53.333, lon=-3.851, year="c. 2000 BC", ill="cave", src="Great_Orme_Mines",
  dEn="Bronze Age miners dug kilometres of tunnels for copper ore, using bone and stone tools.[[cite:orme-antiquity,orme-guinness]] Many passages can still be walked.",
  dCy="Cloddiodd mwynwyr Oes yr Efydd gilometrau o dwneli am fwyn copr gydag offer asgwrn a charreg.[[cite:orme-antiquity,orme-guinness]] Gellir cerdded llawer o’r twneli hyd heddiw."),
 dict(id="stdavids", en="St Davids", cy="Tyddewi", era="ancient", lat=51.882, lon=-5.269, year="6th century", ill="cross", src="St_Davids_Cathedral",
  dEn="Dewi Sant founded his monastery here. Two pilgrimages to St Davids were once said to equal one to Rome.",
  dCy="Sefydlodd Dewi Sant ei fynachlog yma. Dywedid gynt fod dwy bererindod i Dyddewi gystal ag un i Rufain."),
 dict(id="cardigan", en="Cardigan Castle", cy="Castell Aberteifi", era="medieval", lat=52.081, lon=-4.661, year="1176", ill="harp", src="Cardigan_Castle",
  dEn="The Lord Rhys held the first recorded eisteddfod here, with a chair for the best poet and another for the best musician.",
  dCy="Cynhaliodd yr Arglwydd Rhys yr eisteddfod gyntaf y gwyddys amdani yma, gyda chadair i’r bardd gorau ac un arall i’r cerddor gorau."),
 dict(id="cilmeri", en="Cilmeri", cy="Cilmeri", era="medieval", lat=52.150, lon=-3.456, year="1282", ill="stone", src="Cilmeri",
  dEn="A granite monolith marks where Llywelyn ap Gruffudd, the last native Prince of Wales, was killed on 11 December 1282.",
  dCy="Mae maen hir o wenithfaen yn nodi’r fan lle lladdwyd Llywelyn ap Gruffudd, tywysog brodorol olaf Cymru, ar 11 Rhagfyr 1282."),
 dict(id="caernarfon", en="Caernarfon Castle", cy="Castell Caernarfon", era="medieval", lat=53.139, lon=-4.277, year="1283", ill="castle", src="Caernarfon_Castle",
  dEn="Edward I’s statement of conquest, with banded walls modelled on Constantinople. A UNESCO World Heritage Site with Conwy, Harlech and Beaumaris.",
  dCy="Datganiad Edward I o’i oruchafiaeth, gyda muriau streipiog yn efelychu Caergystennin. Safle Treftadaeth y Byd UNESCO gyda Chonwy, Harlech a Biwmares."),
 dict(id="harlech", en="Harlech Castle", cy="Castell Harlech", era="medieval", lat=52.860, lon=-4.109, year="1404", ill="castle", src="Harlech_Castle",
  dEn="Captured by Owain Glyndŵr in 1404 and used as his court. During the Wars of the Roses its long siege inspired the song ‘Men of Harlech’.",
  dCy="Cipiwyd gan Owain Glyndŵr yn 1404 a’i ddefnyddio fel ei lys. Yn ystod Rhyfeloedd y Rhosynnau ysbrydolodd ei warchae hir y gân ‘Rhyfelgyrch Gwŷr Harlech’."),
 dict(id="machynlleth", en="Machynlleth", cy="Machynlleth", era="medieval", lat=52.590, lon=-3.851, year="1404", ill="crown", src="Machynlleth",
  dEn="Where Glyndŵr was crowned Prince of Wales and held his parliament. The town still calls itself the ancient capital of Wales.",
  dCy="Yma y coronwyd Glyndŵr yn Dywysog Cymru ac y cynhaliodd ei senedd. Mae’r dref yn dal i alw ei hun yn hen brifddinas Cymru."),
 dict(id="dale", en="Mill Bay, Dale", cy="Mill Bay, Dale", era="industrial", lat=51.700, lon=-5.165, year="1485", ill="ship", src="Henry_VII_of_England",
  dEn="Henry Tudor came ashore here on 7 August 1485 with a small army, gathering Welsh support on the march to Bosworth.",
  dCy="Glaniodd Harri Tudur yma ar 7 Awst 1485 gyda byddin fechan, gan gasglu cefnogaeth Gymreig ar y daith i Bosworth."),
 dict(id="llanrhaeadr", en="Llanrhaeadr-ym-Mochnant", cy="Llanrhaeadr-ym-Mochnant", era="industrial", lat=52.824, lon=-3.300, year="1588", ill="book", src="Llanrhaeadr-ym-Mochnant",
  dEn="William Morgan was vicar here while he translated the whole Bible into Welsh.",
  dCy="William Morgan oedd ficer y plwyf hwn pan gyfieithodd y Beibl cyfan i’r Gymraeg."),
 dict(id="fishguard", en="Carregwastad Point", cy="Carreg Wastad", era="industrial", lat=52.015, lon=-4.986, year="1797", ill="ship", src="Battle_of_Fishguard",
  dEn="About 1,400 French troops landed here in the last invasion of Britain, and surrendered on Goodwick Sands two days later.",
  dCy="Glaniodd tua 1,400 o filwyr Ffrengig yma yn y goresgyniad olaf ar Brydain, gan ildio ar draeth Wdig ddeuddydd yn ddiweddarach."),
 dict(id="pontcysyllte", en="Pontcysyllte Aqueduct", cy="Traphont Pontcysyllte", era="industrial", lat=52.970, lon=-3.088, year="1805", ill="arches", src="Pontcysyllte_Aqueduct",
  dEn="Thomas Telford’s cast-iron trough carries the Llangollen Canal 38 metres above the Dee. A UNESCO World Heritage Site.",
  dCy="Mae cafn haearn bwrw Thomas Telford yn cario Camlas Llangollen 38 metr uwchben Afon Dyfrdwy. Safle Treftadaeth y Byd UNESCO."),
 dict(id="merthyr", en="Merthyr Tydfil", cy="Merthyr Tudful", era="industrial", lat=51.746, lon=-3.378, year="1831", ill="wheel", src="Merthyr_Tydfil",
  dEn="Once the iron capital of the world, home of the Dowlais and Cyfarthfa works, and of the 1831 rising.",
  dCy="Prifddinas haearn y byd ar un adeg, cartref gweithfeydd Dowlais a Chyfarthfa, a gwrthryfel 1831."),
 dict(id="blaenavon", en="Blaenavon", cy="Blaenafon", era="industrial", lat=51.775, lon=-3.085, year="1789", ill="wheel", src="Blaenavon_Industrial_Landscape",
  dEn="Ironworks, quarries and Big Pit coal mine, where former miners lead visitors 90 metres underground. A UNESCO World Heritage Site.",
  dCy="Gwaith haearn, chwareli a Phwll Mawr, lle mae cyn-lowyr yn arwain ymwelwyr 90 metr dan ddaear. Safle Treftadaeth y Byd UNESCO."),
 dict(id="dinorwig", en="The Slate Landscape", cy="Tirwedd Llechi", era="industrial", lat=53.120, lon=-4.113, year="1900", ill="slate", src="Slate_Landscape_of_Northwest_Wales",
  dEn="Quarries at Penrhyn, Dinorwig and Blaenau Ffestiniog roofed the world. Inscribed as a World Heritage Site in 2021.",
  dCy="Toeodd chwareli’r Penrhyn, Dinorwig a Blaenau Ffestiniog y byd. Daeth yn Safle Treftadaeth y Byd yn 2021."),
 dict(id="celyn", en="Capel Celyn", cy="Capel Celyn", era="modern", lat=52.950, lon=-3.700, year="1965", ill="chapel", src="Capel_Celyn",
  dEn="A Welsh-speaking village drowned beneath Llyn Celyn to supply Liverpool. ‘Cofiwch Dryweryn’ is still painted on walls across Wales.",
  dCy="Pentref Cymraeg a foddwyd dan Lyn Celyn i gyflenwi Lerpwl. Mae ‘Cofiwch Dryweryn’ yn dal i gael ei baentio ar waliau ledled Cymru."),
 dict(id="aberfan", en="Aberfan", cy="Aberfan", era="modern", lat=51.694, lon=-3.349, year="1966", ill="stone", src="Aberfan_disaster",
  dEn="A colliery spoil tip slid onto Pantglas Junior School. The memorial garden stands where the school once was.",
  dCy="Llithrodd tomen wastraff glofa ar Ysgol Gynradd Pantglas. Mae’r ardd goffa yn sefyll lle bu’r ysgol."),
 dict(id="senedd", en="The Senedd, Cardiff Bay", cy="Y Senedd, Bae Caerdydd", era="modern", lat=51.464, lon=-3.162, year="2006", ill="senedd", src="Senedd_building",
  dEn="Home of the Welsh Parliament, built of Welsh slate, oak and glass, on the waterfront that once shipped the world’s coal.",
  dCy="Cartref Senedd Cymru, wedi’i godi o lechi Cymreig, derw a gwydr, ar y glannau a fu unwaith yn allforio glo’r byd."),
]

# (slug, era, dates, nameEn, nameCy, epithetEn, epithetCy, bioEn, bioCy, wikipediaTitle)
PEOPLE = [
 ("caratacus","ancient","fl. 1st century","Caratacus","Caradog","British king who fought Rome","Y brenin Brythonig a ymladdodd Rufain",
  "Led British resistance to Rome alongside the Silures and Ordovices. Captured and taken to Rome, he won his freedom with a famous speech.",
  "Arweiniodd y gwrthwynebiad i Rufain gyda’r Silwriaid a’r Ordofigiaid. Ar ôl ei ddal a’i gludo i Rufain, enillodd ei ryddid ag araith enwog.","Caratacus"),
 ("dewi-sant","ancient","d. c. 589","Saint David","Dewi Sant","Patron saint of Wales","Nawddsant Cymru",
  "Founder of the monastery at St Davids. His last words are remembered as ‘Gwnewch y pethau bychain’: do the little things.",
  "Sefydlydd y fynachlog yn Nhyddewi. Cofir ei eiriau olaf: ‘Gwnewch y pethau bychain’.","Saint_David"),
 ("taliesin","ancient","fl. late 6th century","Taliesin","Taliesin","Chief of bards","Pen beirdd",
  "Court poet to Urien of Rheged, honoured for centuries as the greatest of the early bards.",
  "Bardd llys Urien Rheged, a anrhydeddwyd am ganrifoedd fel y mwyaf o’r Cynfeirdd.","Taliesin"),
 ("aneirin","medieval","fl. c. 600","Aneirin","Aneirin","Poet of Y Gododdin","Bardd Y Gododdin",
  "Poet of Y Gododdin, the elegy for the warriors of Catraeth.",
  "Bardd Y Gododdin, y farwnad i ryfelwyr Catraeth.","Aneirin"),
 ("rhodri-mawr","medieval","d. 878","Rhodri Mawr","Rhodri Mawr","Rhodri the Great","Brenin Gwynedd",
  "King of Gwynedd who brought Powys and Seisyllwg under his rule and beat back the Vikings.",
  "Brenin Gwynedd a ddaeth â Phowys a Seisyllwg dan ei reolaeth a gwrthsefyll y Llychlynwyr.","Rhodri_the_Great"),
 ("hywel-dda","medieval","d. 950","Hywel Dda","Hywel Dda","Hywel the Good","Brenin y Deheubarth",
  "His name was given to the native law of Wales, notable for women’s property rights and for compensation in place of vengeance.",
  "Rhoddwyd ei enw ar gyfraith frodorol Cymru, sy’n nodedig am hawliau eiddo i fenywod ac am iawndal yn lle dial.","Hywel_Dda"),
 ("gruffudd-ap-llywelyn","medieval","d. 1063","Gruffudd ap Llywelyn","Gruffudd ap Llywelyn","King of all Wales","Brenin Cymru gyfan",
  "The only king ever to rule the whole of Wales, from 1055 until he was killed by his own men.",
  "Yr unig frenin erioed i reoli Cymru gyfan, o 1055 nes iddo gael ei ladd gan ei wŷr ei hun.","Gruffydd_ap_Llywelyn"),
 ("gwenllian","medieval","c. 1100–1136","Gwenllian ferch Gruffydd","Gwenllian ferch Gruffydd","Princess of Deheubarth","Tywysoges Deheubarth",
  "Led an army against the Normans at Kidwelly and died in battle. Her death sparked the Great Revolt.",
  "Arweiniodd fyddin yn erbyn y Normaniaid ger Cydweli a bu farw yn y frwydr. Taniodd ei marwolaeth y Gwrthryfel Mawr.","Gwenllian_ferch_Gruffydd"),
 ("yr-arglwydd-rhys","medieval","1132–1197","The Lord Rhys","Yr Arglwydd Rhys","Prince Rhys ap Gruffudd of Deheubarth","Y Tywysog Rhys ap Gruffudd o Ddeheubarth",
  "Patron of poets and host of the first recorded eisteddfod, at Cardigan in 1176.",
  "Noddwr beirdd a threfnydd yr eisteddfod gyntaf y gwyddys amdani, yn Aberteifi yn 1176.","Rhys_ap_Gruffydd"),
 ("gerallt-gymro","medieval","c. 1146–c. 1223","Gerald of Wales","Gerallt Gymro","Churchman and writer","Clerigwr ac awdur",
  "His Journey through Wales and Description of Wales still bring the medieval country to life.",
  "Mae ei Daith drwy Gymru a’i Ddisgrifiad o Gymru yn dal i ddod â’r wlad ganoloesol yn fyw.","Gerald_of_Wales"),
 ("llywelyn-fawr","medieval","c. 1173–1240","Llywelyn Fawr","Llywelyn Fawr","Llywelyn the Great","Tywysog Gwynedd",
  "Prince of Gwynedd who dominated Wales for forty years and married Joan, daughter of King John.",
  "Tywysog Gwynedd a fu’n ben ar Gymru am ddeugain mlynedd ac a briododd Siwan, merch y Brenin John.","Llywelyn_the_Great"),
 ("llywelyn-ap-gruffudd","medieval","c. 1223–1282","Llywelyn ap Gruffudd","Llywelyn ap Gruffudd","Our Last Leader","Ein Llyw Olaf",
  "The only native prince recognised by the English crown as Prince of Wales. His death at Cilmeri ended independence.",
  "Yr unig dywysog brodorol a gydnabuwyd gan goron Lloegr yn Dywysog Cymru. Daeth ei farwolaeth yng Nghilmeri ag annibyniaeth i ben.","Llywelyn_ap_Gruffudd"),
 ("dafydd-ap-gwilym","medieval","fl. 1340–1370","Dafydd ap Gwilym","Dafydd ap Gwilym","Poet","Bardd",
  "The greatest poet of medieval Wales, who wrote of love and nature with wit and daring.",
  "Bardd mwyaf Cymru’r Oesoedd Canol, a ganodd am gariad a natur yn ffraeth a beiddgar.","Dafydd_ap_Gwilym"),
 ("owain-glyndwr","medieval","c. 1359–c. 1415","Owain Glyndŵr","Owain Glyndŵr","Prince of Wales","Tywysog Cymru",
  "Led the last great war for independence and held a parliament at Machynlleth. He was never captured, and his fate is unknown.",
  "Arweiniodd y rhyfel mawr olaf dros annibyniaeth a chynnal senedd ym Machynlleth. Ni chafodd ei ddal erioed, ac ni ŵyr neb beth fu ei dynged.","Owain_Glynd%C5%B5r"),
 ("harri-tudur","industrial","1457–1509","Henry VII","Harri Tudur","Founder of the Tudors","Sylfaenydd y Tuduriaid",
  "Born at Pembroke Castle, he landed in Wales in 1485, won at Bosworth and founded the Tudor dynasty.",
  "Fe’i ganed yng Nghastell Penfro. Glaniodd yng Nghymru yn 1485, enillodd ym Mosworth a sefydlu llinach y Tuduriaid.","Henry_VII_of_England"),
 ("william-morgan","industrial","c. 1545–1604","William Morgan","William Morgan","Bishop and translator","Esgob a chyfieithydd",
  "Translated the full Bible into Welsh in 1588. His prose became the standard for written Welsh.",
  "Cyfieithodd y Beibl cyfan i’r Gymraeg yn 1588. Daeth ei ryddiaith yn safon i’r Gymraeg ysgrifenedig.","William_Morgan_(bishop)"),
 ("griffith-jones","industrial","1683–1761","Griffith Jones","Griffith Jones","Of Llanddowror","Llanddowror",
  "His circulating schools taught a large share of the Welsh people to read, in Welsh.",
  "Dysgodd ei ysgolion cylchynol gyfran helaeth o bobl Cymru i ddarllen, a hynny yn Gymraeg.","Griffith_Jones_(Llanddowror)"),
 ("howell-harris","industrial","1714–1773","Howell Harris","Hywel Harris","Revivalist","Diwygiwr",
  "Fiery preacher of the Methodist revival who founded a religious community at Trefeca.",
  "Pregethwr tanbaid y diwygiad Methodistaidd a sefydlodd gymuned grefyddol yn Nhrefeca.","Howell_Harris"),
 ("pantycelyn","industrial","1717–1791","William Williams Pantycelyn","William Williams Pantycelyn","The Sweet Singer","Y Pêr Ganiedydd",
  "Wrote hundreds of hymns, including ‘Arglwydd, arwain trwy’r anialwch’, known in English as ‘Guide me, O thou great Redeemer’.",
  "Ysgrifennodd gannoedd o emynau, gan gynnwys ‘Arglwydd, arwain trwy’r anialwch’.","William_Williams_Pantycelyn"),
 ("iolo-morganwg","industrial","1747–1826","Iolo Morganwg","Iolo Morganwg","Edward Williams","Edward Williams",
  "Stonemason, poet and visionary who founded the Gorsedd of the Bards, saved old Welsh manuscripts and taught Wales to see itself as a nation.",
  "Saer maen, bardd a gweledydd a sefydlodd Orsedd y Beirdd, a achubodd hen lawysgrifau Cymraeg ac a ddysgodd i Gymru ei gweld ei hun yn genedl.","Iolo_Morganwg"),
 ("jemima-nicholas","industrial","c. 1750–1832","Jemima Nicholas","Jemima Nicholas","Jemima Fawr","Jemima Fawr",
  "Fishguard cobbler said to have rounded up French soldiers with a pitchfork during the 1797 invasion.",
  "Crydd o Abergwaun y dywedir iddi gorlannu milwyr Ffrengig â phicfforch yn ystod goresgyniad 1797.","Jemima_Nicholas"),
 ("robert-owen","industrial","1771–1858","Robert Owen","Robert Owen","Of Newtown","Y Drenewydd",
  "Pioneer of co-operation and better factory conditions, he built a model community at New Lanark.",
  "Arloeswr cydweithredu ac amodau gwell mewn ffatrïoedd, a adeiladodd gymuned ddelfrydol yn New Lanark.","Robert_Owen"),
 ("betsi-cadwaladr","industrial","1789–1860","Betsi Cadwaladr","Betsi Cadwaladr","Nurse","Nyrs",
  "From Bala, she nursed soldiers in the Crimean War, clashing at times with Florence Nightingale.",
  "O’r Bala, bu’n nyrsio milwyr yn Rhyfel y Crimea, gan anghytuno weithiau â Florence Nightingale.","Betsi_Cadwaladr"),
 ("lady-llanover","industrial","1802–1896","Lady Llanover","Arglwyddes Llanofer","Augusta Hall","Gwenynen Gwent",
  "Patron of Welsh culture who championed the harp, the language and the Welsh national costume.",
  "Noddwr diwylliant Cymru a hyrwyddodd y delyn, yr iaith a’r wisg Gymreig.","Augusta_Hall,_Baroness_Llanover"),
 ("dic-penderyn","industrial","1808–1831","Dic Penderyn","Dic Penderyn","Richard Lewis","Richard Lewis",
  "Hanged after the Merthyr Rising for a crime many believed he did not commit.",
  "Crogwyd ar ôl Gwrthryfel Merthyr am drosedd y credai llawer na wnaeth ei chyflawni.","Dic_Penderyn"),
 ("henry-richard","industrial","1812–1888","Henry Richard","Henry Richard","Apostle of Peace","Apostol Heddwch",
  "MP for Merthyr who campaigned for international arbitration and for the rights of Welsh tenants.",
  "AS Merthyr a ymgyrchodd dros gyflafareddu rhyngwladol a thros hawliau tenantiaid Cymru.","Henry_Richard"),
 ("lloyd-george","modern","1863–1945","David Lloyd George","David Lloyd George","Prime Minister","Prif Weinidog",
  "Welsh-speaking prime minister from 1916 to 1922 whose 1909 People’s Budget laid foundations for the welfare state.",
  "Prif weinidog Cymraeg ei iaith rhwng 1916 a 1922, y gosododd ei Gyllideb y Bobl yn 1909 seiliau’r wladwriaeth les.","David_Lloyd_George"),
 ("gwen-john","modern","1876–1939","Gwen John","Gwen John","Painter","Arlunydd",
  "Born in Haverfordwest, she painted quiet, intense portraits and is now ranked among the finest artists of her time.",
  "Fe’i ganed yn Hwlffordd. Paentiodd bortreadau tawel, dwys, ac fe’i hystyrir heddiw ymhlith artistiaid gorau ei chyfnod.","Gwen_John"),
 ("saunders-lewis","modern","1893–1985","Saunders Lewis","Saunders Lewis","Dramatist","Dramodydd",
  "Dramatist, co-founder of Plaid Cymru, and author of the 1962 lecture Tynged yr Iaith.",
  "Dramodydd, un o sefydlwyr Plaid Cymru, ac awdur darlith Tynged yr Iaith yn 1962.","Saunders_Lewis"),
 ("ifan-ab-owen-edwards","modern","1895–1970","Ifan ab Owen Edwards","Ifan ab Owen Edwards","Founder of the Urdd","Sylfaenydd yr Urdd",
  "Founded Urdd Gobaith Cymru in 1922 and the first Welsh-medium school in 1939.",
  "Sefydlodd Urdd Gobaith Cymru yn 1922 a’r ysgol Gymraeg gyntaf yn 1939.","Ifan_ab_Owen_Edwards"),
 ("aneurin-bevan","modern","1897–1960","Aneurin Bevan","Aneurin Bevan","Nye","Nye",
  "Miner’s son from Tredegar who, as Minister of Health, founded the National Health Service in 1948.",
  "Mab i löwr o Dredegar a sefydlodd y Gwasanaeth Iechyd Gwladol yn 1948 fel Gweinidog Iechyd.","Aneurin_Bevan"),
 ("megan-lloyd-george","modern","1902–1966","Megan Lloyd George","Megan Lloyd George","MP for Anglesey","AS Môn",
  "The first woman elected for a Welsh constituency, in 1929, and a lifelong campaigner for a Welsh parliament.",
  "Y fenyw gyntaf i’w hethol dros etholaeth yng Nghymru, yn 1929, ac ymgyrchydd oes dros senedd i Gymru.","Megan_Lloyd_George"),
 ("gwynfor-evans","modern","1912–2005","Gwynfor Evans","Gwynfor Evans","Plaid Cymru’s first MP","AS cyntaf Plaid Cymru",
  "Won Plaid Cymru’s first seat in 1966. His 1980 hunger-strike threat secured S4C.",
  "Enillodd sedd gyntaf Plaid Cymru yn 1966. Sicrhaodd ei fygythiad i ymprydio yn 1980 sianel S4C.","Gwynfor_Evans"),
 ("dylan-thomas","modern","1914–1953","Dylan Thomas","Dylan Thomas","Poet","Bardd",
  "Swansea’s poet of ‘Do not go gentle into that good night’ and Under Milk Wood.",
  "Bardd Abertawe, awdur ‘Do not go gentle into that good night’ ac Under Milk Wood.","Dylan_Thomas"),
]

READING = [
 dict(t="John Davies, A History of Wales", n="Penguin, revised 2007. The standard one-volume history.", nCy="Penguin, argraffiad diwygiedig 2007. Y safon mewn un gyfrol."),
 dict(t="Gwynfor Evans, Land of My Fathers: 2000 Years of Welsh History", n="John Penry Press, 1974; now from Y Lolfa. Two thousand years of the story of Wales, told with pride.", nCy="Gwasg John Penry, 1974; bellach gan y Lolfa. Dwy fil o flynyddoedd o stori Cymru, wedi’u hadrodd gyda balchder. Yn Gymraeg: Aros Mae.", u="YL9780862432652/land-of-my-fathers"),
 dict(t="Gwynfor Evans, The Fight for Welsh Freedom", n="Y Lolfa. The long struggle of the Welsh to stay a free nation.", nCy="Y Lolfa. Brwydr hir y Cymry i aros yn genedl rydd.", u="YL9780862435158/the-fight-for-welsh-freedom"),
 dict(t="Gwynfor Evans, For the Sake of Wales: The Memoirs of Gwynfor Evans", n="Welsh Academic Press, 1996; first published in Welsh in 1982. Gwynfor’s own story of his life and his fight for Wales.", nCy="Gwasg Academaidd Cymru, 1996; cyhoeddwyd gyntaf yn Gymraeg yn 1982. Stori Gwynfor ei hun am ei fywyd a’i frwydr dros Gymru.", u="https://openlibrary.org/books/OL596418M/For_the_sake_of_Wales"),
 dict(t="Gwyn A. Williams, When Was Wales?", n="Penguin, 1985. A passionate, provocative history.", nCy="Penguin, 1985. Hanes angerddol a phryfoclyd."),
 dict(t="Geraint H. Jenkins, A Concise History of Wales", n="Cambridge University Press, 2007. The whole story in one short, well-illustrated book.", nCy="Gwasg Prifysgol Caergrawnt, 2007. Yr hanes cyfan mewn un llyfr byr, llawn lluniau."),
 dict(t="Gerald Morgan, A Brief History of Wales", n="Y Lolfa, 2008. The whole story in one short, clear book.", nCy="Y Lolfa, 2008. Yr hanes cyfan mewn un llyfr byr a chlir.", u="YL9781847710185/a-brief-history-of-wales"),
 dict(t="Wendy Davies, Wales in the Early Middle Ages", n="Leicester University Press, 1982. Land, kings, church and people from Rome to the Normans.", nCy="Gwasg Prifysgol Caerlŷr, 1982. Tir, brenhinoedd, eglwys a phobl o Rufain hyd y Normaniaid."),
 dict(t="Roger Turvey, The Welsh Princes, 1063–1283", n="Longman, 2002. The princes of Gwynedd, Powys and Deheubarth and how they ruled.", nCy="Longman, 2002. Tywysogion Gwynedd, Powys a Deheubarth a’u dull o reoli."),
 dict(t="Roger Turvey, The Lord Rhys: Prince of Deheubarth", n="Y Lolfa, 2023. The prince who held the first eisteddfod.", nCy="Y Lolfa, 2023. Y tywysog a gynhaliodd yr eisteddfod gyntaf.", u="YL9781800993143/the-lord-rhys-prince-of-deheubarth"),
 dict(t="Roger Turvey, Llywelyn the Great", n="Y Lolfa, 2023. The prince who ruled almost all of Wales.", nCy="Y Lolfa, 2023. Y tywysog a reolodd bron y cyfan o Gymru.", u="YL9781800993150/llywelyn-the-great"),
 dict(t="J. Beverley Smith, Llywelyn ap Gruffudd, Prince of Wales", n="University of Wales Press, 1998. The great life of the last native Prince of Wales.", nCy="Gwasg Prifysgol Cymru, 1998. Y cofiant mawr i dywysog brodorol olaf Cymru."),
 dict(t="R. R. Davies, The Age of Conquest: Wales 1063–1415", n="Oxford University Press, 1991. The princes and the conquest.", nCy="Gwasg Prifysgol Rhydychen, 1991. Y tywysogion a’r goncwest."),
 dict(t="R. R. Davies, The Revolt of Owain Glyn Dŵr", n="Oxford University Press, 1995.", nCy="Gwasg Prifysgol Rhydychen, 1995."),
 dict(t="R. R. Davies, Owain Glyn Dŵr: Prince of Wales", n="Y Lolfa. Owain’s story in a short book for everyone.", nCy="Y Lolfa. Hanes Owain mewn llyfr byr i bawb.", u="YL9781847711274/owain-glyndwr-prince-of-wales"),
 dict(t="Kenneth O. Morgan, Rebirth of a Nation: Wales 1880–1980", n="Oxford University Press and University of Wales Press, 1981. Modern Wales, from the Liberal age to the eve of devolution.", nCy="Gwasg Prifysgol Rhydychen a Gwasg Prifysgol Cymru, 1981. Cymru fodern, o oes y Rhyddfrydwyr hyd at drothwy datganoli."),
 dict(t="Rhys Evans, Gwynfor Evans: A Portrait of a Patriot", n="Y Lolfa, 2008. The full life of the man who won S4C.", nCy="Y Lolfa, 2008. Cofiant llawn y gŵr a enillodd S4C. Yn Gymraeg: Rhag Pob Brad.", u="YL9780862439187/gwynfor-evans-a-portrait-of-a-patriot"),
 dict(t="Wyn Thomas, Tryweryn: A New Dawn?", n="Y Lolfa. The drowning of Capel Celyn and how it woke a nation.", nCy="Y Lolfa. Boddi Capel Celyn a sut y deffrodd genedl.", u="YL9781912631483/tryweryn-a-new-dawn"),
 dict(t="Martin Johnes, Wales since 1939", n="Manchester University Press, 2012.", nCy="Gwasg Prifysgol Manceinion, 2012."),
 dict(t="Jan Morris, Wales: Epic Views of a Small Country", n="Penguin, 1998. History as travel writing.", nCy="Penguin, 1998. Hanes drwy lenyddiaeth teithio."),
]
import booklinks as _BL  # every other book gets its publisher's (or Open Library's) page
for _r in READING:
    if _r.get("u", "").startswith("YL"):
        _r["u"] = "https://www.ylolfa.com/products/" + _r["u"][2:]
    elif not _r.get("u"):
        _r["u"] = _BL.link(*_r["t"].split(", ", 1))
    _b = _BL.buy(*_r["t"].split(", ", 1))   # where to buy it: Amazon UK and AbeBooks search links
    if _b:
        _r["b"] = list(_b)
ONLINE = [  # u: the English site, uCy: its Welsh address (each checked 2026-11-12)
 dict(t="Dictionary of Welsh Biography", tCy="Y Bywgraffiadur Cymreig", u="https://biography.wales/", uCy="https://bywgraffiadur.cymru/"),
 dict(t="National Library of Wales", tCy="Llyfrgell Genedlaethol Cymru", u="https://www.library.wales/", uCy="https://www.llyfrgell.cymru/"),
 dict(t="Welsh Newspapers", tCy="Papurau Newydd Cymru", u="https://newspapers.library.wales/", uCy="https://papuraunewydd.llyfrgell.cymru/"),
 dict(t="Welsh Journals", tCy="Cylchgronau Cymru", u="https://journals.library.wales/"),
 dict(t="Archives Wales", tCy="Archifau Cymru", u="https://archives.wales/"),
 dict(t="Amgueddfa Cymru – Museum Wales", tCy="Amgueddfa Cymru", u="https://museum.wales/", uCy="https://amgueddfa.cymru/"),
 dict(t="Cadw, historic monuments", tCy="Cadw, henebion", u="https://cadw.gov.wales/", uCy="https://cadw.llyw.cymru/"),
 dict(t="People’s Collection Wales", tCy="Casgliad y Werin Cymru", u="https://www.peoplescollection.wales/", uCy="https://www.casgliadywerin.cymru/"),
 dict(t="Royal Commission on the Ancient and Historical Monuments of Wales", tCy="Comisiwn Brenhinol Henebion Cymru", u="https://rcahmw.gov.uk/", uCy="https://cbhc.gov.uk/"),
 dict(t="Coflein, the national monuments record", tCy="Coflein, cofnod henebion cenedlaethol", u="https://coflein.gov.uk/", uCy="https://coflein.gov.uk/cy/"),
 dict(t="Heneb: the Trust for Welsh Archaeology", tCy="Heneb: Ymddiriedolaeth Archaeoleg Cymru", u="https://heneb.org.uk/", uCy="https://heneb.org.uk/cy/"),  # added 2026-11-13
 dict(t="Cambrian Archaeological Association", tCy="Cymdeithas Hynafiaethau Cymru", u="https://cambrians.org.uk/", uCy="https://cambrians.org.uk/cy/"),
 dict(t="Historic Place Names of Wales", tCy="Enwau Lleoedd Hanesyddol Cymru", u="https://historicplacenames.rcahmw.gov.uk/", uCy="https://enwaulleoeddhanesyddol.cbhc.gov.uk/"),
 dict(t="Seintiau: the saints of Wales", tCy="Seintiau: seintiau Cymru", u="https://saints.wales/"),
 dict(t="Dafydd ap Gwilym: all his poems", tCy="Dafydd ap Gwilym: ei gerddi i gyd", u="https://dafyddapgwilym.net/index_eng.php", uCy="https://dafyddapgwilym.net/index_cym.php"),
 dict(t="Guto’r Glyn and his Wales", tCy="Guto’r Glyn a’i Gymru", u="https://gutorglyn.net/gutoswales/index.php", uCy="https://gutorglyn.net/gutoswales/cy/index.php"),
 dict(t="Welsh Prose 1300–1425: the old tales and laws in their manuscripts", tCy="Rhyddiaith 1300–1425: yr hen chwedlau a’r cyfreithiau yn eu llawysgrifau", u="https://rhyddiaithganoloesol.cardiff.ac.uk/en"),
 dict(t="The Honourable Society of Cymmrodorion, since 1751", tCy="Anrhydeddus Gymdeithas y Cymmrodorion, ers 1751", u="https://www.cymmrodorion.org/", uCy="https://www.cymmrodorion.org/cy/"),
 dict(t="Cymdeithas yr Iaith: its story since 1962", tCy="Cymdeithas yr Iaith: ei hanes ers 1962", u="https://archif.cymdeithas.cymru/what-is-cymdeithas-yr-iaith"),
 dict(t="Y Lolfa, the Talybont press", tCy="Y Lolfa, gwasg Tal-y-bont", u="https://www.ylolfa.com/"),
 dict(t="ffolio: Welsh books from the Books Council of Wales", tCy="ffolio: llyfrau Cymru gan Gyngor Llyfrau Cymru", u="https://www.ffolio.wales/", uCy="https://www.ffolio.cymru/"),
]

CENSUS = [[1891,54.4],[1901,49.9],[1911,43.5],[1921,37.1],[1931,36.8],[1951,28.9],[1961,26.0],[1971,20.8],[1981,18.9],[1991,18.7],[2001,20.8],[2011,19.0],[2021,17.8]]

# Approximate political map, using modern local authorities as building blocks.
KINGDOMS = [
 dict(id="c1000", en="c. 1000: the kingdoms", cy="tua 1000: y teyrnasoedd",
  nEn="Wales was a cluster of kingdoms, each with its own dynasty.", nCy="Clwstwr o deyrnasoedd oedd Cymru, pob un â’i llinach ei hun.",
  groups=[["Gwynedd","Gwynedd","#e2453d",["Isle of Anglesey","Gwynedd","Conwy","Denbighshire"]],
          ["Powys","Powys","#d39a62",["Powys","Wrexham","Flintshire"]],
          ["Deheubarth","Deheubarth","#7cc495",["Ceredigion","Pembrokeshire","Carmarthenshire","Swansea"]],
          ["Morgannwg","Morgannwg","#93a0e0",["Neath Port Talbot","Bridgend","Vale of Glamorgan","Cardiff","Rhondda Cynon Taf","Merthyr Tydfil","Caerphilly"]],
          ["Gwent","Gwent","#c38fd6",["Blaenau Gwent","Torfaen","Monmouthshire","Newport"]]]),
 dict(id="c1057", en="1055–1063: one king", cy="1055–1063: un brenin",
  nEn="Gruffudd ap Llywelyn ruled the whole of Wales, the only king ever to do so.", nCy="Rheolodd Gruffudd ap Llywelyn Gymru gyfan, yr unig frenin erioed i wneud hynny.",
  groups=[["Gruffudd ap Llywelyn","Gruffudd ap Llywelyn","#e2453d","*"]]),
 dict(id="c1200", en="c. 1200: native Wales and the March", cy="tua 1200: Pura Wallia a’r Mers",
  nEn="Normans held the south and east as Marcher lordships. Welsh princes ruled the north and west.", nCy="Daliai’r Normaniaid y de a’r dwyrain fel arglwyddiaethau’r Mers. Rheolai tywysogion Cymru’r gogledd a’r gorllewin.",
  groups=[["Gwynedd","Gwynedd","#e2453d",["Isle of Anglesey","Gwynedd","Conwy","Denbighshire","Flintshire"]],
          ["Powys","Powys","#d39a62",["Powys","Wrexham"]],
          ["Deheubarth","Deheubarth","#7cc495",["Ceredigion","Carmarthenshire"]],
          ["The March (Norman lords)","Y Mers (arglwyddi Normanaidd)","#5b6478",["Pembrokeshire","Swansea","Neath Port Talbot","Bridgend","Vale of Glamorgan","Cardiff","Rhondda Cynon Taf","Merthyr Tydfil","Caerphilly","Blaenau Gwent","Torfaen","Monmouthshire","Newport"]]]),
 dict(id="c1267", en="1267: Llywelyn’s principality", cy="1267: tywysogaeth Llywelyn",
  nEn="At the Treaty of Montgomery, Llywelyn ap Gruffudd’s principality reached its greatest extent.", nCy="Yng Nghytundeb Trefaldwyn, cyrhaeddodd tywysogaeth Llywelyn ap Gruffudd ei maint mwyaf.",
  groups=[["Principality of Wales","Tywysogaeth Cymru","#e2453d",["Isle of Anglesey","Gwynedd","Conwy","Denbighshire","Flintshire","Wrexham","Powys","Ceredigion"]],
          ["Marcher lordships and the Crown","Arglwyddiaethau’r Mers a’r Goron","#5b6478",["Pembrokeshire","Carmarthenshire","Swansea","Neath Port Talbot","Bridgend","Vale of Glamorgan","Cardiff","Rhondda Cynon Taf","Merthyr Tydfil","Caerphilly","Blaenau Gwent","Torfaen","Monmouthshire","Newport"]]]),
 dict(id="c1284", en="1284: the conquest", cy="1284: y goncwest",
  nEn="After 1282 the Statute of Rhuddlan made the princes’ lands Crown counties. The rest stayed with the Marcher lords.", nCy="Wedi 1282 trodd Statud Rhuddlan diroedd y tywysogion yn siroedd y Goron. Arhosodd y gweddill gydag arglwyddi’r Mers.",
  groups=[["Crown principality","Tywysogaeth y Goron","#93a0e0",["Isle of Anglesey","Gwynedd","Conwy","Flintshire","Ceredigion","Carmarthenshire"]],
          ["Marcher lordships","Arglwyddiaethau’r Mers","#5b6478",["Denbighshire","Wrexham","Powys","Pembrokeshire","Swansea","Neath Port Talbot","Bridgend","Vale of Glamorgan","Cardiff","Rhondda Cynon Taf","Merthyr Tydfil","Caerphilly","Blaenau Gwent","Torfaen","Monmouthshire","Newport"]]]),
 dict(id="today", en="Today: 22 local authorities", cy="Heddiw: 22 awdurdod lleol",
  nEn="Since 1996 Wales has been governed locally by 22 councils, and nationally by the Senedd.", nCy="Ers 1996 mae Cymru’n cael ei llywodraethu’n lleol gan 22 cyngor, ac yn genedlaethol gan y Senedd.",
  groups=[["Wales","Cymru","#7cc495","*"]]),
]

WORDS = [
 ["Cymru", "KUM-ree", "Wales", "y wlad"], ["Cymraeg", "kum-RAYG", "the Welsh language", "yr iaith"], ["Croeso", "KROY-so", "welcome", "cyfarchiad"],
 ["Diolch", "DEE-olkh", "thank you", "gair o werthfawrogiad"], ["Hiraeth", "HEER-eyeth", "a longing for home that has no English word", "dyhead am gartref, heb air Saesneg amdano"],
 ["Iechyd da", "YEH-khid DAH", "good health, cheers", "llwncdestun"], ["Cwtch", "kutch", "a cuddle, or a cosy place", "cofleidiad, neu le clyd"],
 ["Eisteddfod", "eye-STETH-vod", "a festival of poetry and music, held since 1176", "gŵyl farddoniaeth a cherddoriaeth, ers 1176"],
 ["Senedd", "SEN-eth", "parliament", "cynulliad deddfu"], ["Cofiwch Dryweryn", "KOV-ee-ookh druh-WER-in", "remember Tryweryn", "slogan ar waliau ledled Cymru"],
]


# ---------- merge round-3 additions (src/more.py) ----------
import re as _re
from more import EVENTS_MORE as _EM, PEOPLE_MORE as _PM, PLACES_MORE as _PLM

EVENTS = sorted(EVENTS + _EM, key=lambda ev: ev[1])
PLACES = PLACES + _PLM
PEOPLE_EXTRA_LONG = {p[0]: ([p[11]], [p[12]]) for p in _PM}
_ERA_ORDER = {e["id"]: i for i, e in enumerate(ERAS)}


def _born(p):
    d = p[2]
    if d == "Age of Arthur":  # people known from the tales of Arthur's court (src/arthur_circle.py): just after Arthur
        return 640
    if d == "The Four Branches":  # people of the Four Branches of the Mabinogi (src/mabinogi_people.py): the age of Brân, before Caradog
        return 1
    if d == "1st century BC":  # Beli Mawr and his sons (src/mabinogi_people2.py): the time of Caswallon and Caesar
        return -50
    m = _re.search(r"([\d,]+) BC", d)
    if m:
        return -int(m.group(1).replace(",", ""))
    m = _re.search(r"AD (\d+)", d)
    if m:
        return int(m.group(1))
    m = _re.search(r"(\d{3,4})", d)
    if m:
        y = int(m.group(1))
        return y - 40 if d.startswith(("d.", "fl.")) else y
    if "1st century" in d:
        return 40
    m = _re.search(r"(\d+)(st|nd|rd|th) century", d)
    return (int(m.group(1)) - 1) * 100 + 50 + (-30 if "early" in d else 30 if "late" in d else 0) if m else 0


PEOPLE = sorted(PEOPLE + [p[:10] for p in _PM], key=lambda p: (_ERA_ORDER[p[1]], _born(p)))


# ---------- six ages (src/ages.py) ----------
import ages as _AG

_anc, _med = ERAS[0], ERAS[1]
_anc["spanEn"], _anc["spanCy"] = "230,000 BC – AD 410", "230,000 CC – 410 OC"
_anc["storyEn"][1] = _anc["storyEn"][1].replace("When the legions left, saints such as Dewi founded churches, and the Brittonic speech of these people began to turn into Welsh.",
                                                "Rome held Wales for more than three centuries, leaving roads, forts, towns and gold mines behind.")
_anc["storyCy"][1] = _anc["storyCy"][1].replace("Pan adawodd y llengoedd, sefydlodd seintiau fel Dewi eglwysi, a dechreuodd iaith Frythoneg y bobl hyn droi’n Gymraeg.",
                                                "Daliodd Rhufain Gymru am dros dair canrif, gan adael ffyrdd, caerau, trefi a mwyngloddiau aur ar ei hôl.")
_med["spanEn"] = _med["spanCy"] = "1100 – 1485"
_med["blurbEn"] = "Castles, poetry and the long struggle against Norman and English power."
_med["blurbCy"] = "Cestyll, barddoniaeth a’r frwydr hir yn erbyn grym y Normaniaid a Lloegr."
_med["storyEn"] = [_AG.PRINCES_P1_EN, _med["storyEn"][1].replace("The Normans pushed into the south and east after 1066, building castles and lordships in the March. ", "")]
_med["storyCy"] = [_AG.PRINCES_P1_CY, _med["storyCy"][1].replace("Gwthiodd y Normaniaid i’r de a’r dwyrain ar ôl 1066, gan godi cestyll ac arglwyddiaethau yn y Mers. ", "")]
ERAS = [ERAS[0], _AG.SAINTS, _AG.KINGS] + ERAS[1:]


def _age(era, y):
    if era in ("ancient", "medieval") and 410 <= y < 800:
        return "saints"
    if era in ("ancient", "medieval") and 800 <= y < 1100:
        return "kings"
    return era


EVENTS = [(_age(ev[0], ev[1]),) + ev[1:] for ev in EVENTS]
PEOPLE = [(p[0], "saints" if p[0] in _AG.SAINTS_PEOPLE else "kings" if p[0] in _AG.KINGS_PEOPLE else p[1]) + p[2:] for p in PEOPLE]
_ERA_ORDER = {e["id"]: i for i, e in enumerate(ERAS)}
PEOPLE = sorted(PEOPLE, key=lambda p: (_ERA_ORDER[p[1]], _born(p)))
PLACES = [dict(pl, era="saints") if pl["id"] == "stdavids" else pl for pl in PLACES] + _AG.NEW_PLACES
_KEYS = {"Death of Saint David", "Y Gododdin", "Offa’s Dyke", "Rhodri Mawr defeats the Vikings", "The laws of Hywel Dda", "One king for all Wales"}
EVENTS = [ev[:9] + (1,) + ev[10:] if ev[5] in _KEYS else ev for ev in EVENTS]


# ---------- nine ages (src/ages9.py) ----------
import ages9 as _A9

_by = {x["id"]: x for x in ERAS}
_a, _i, _m = _by["ancient"], _by["industrial"], _by["modern"]
_tudor_p1 = (_i["storyEn"][0], _i["storyCy"][0])
for _k in ("spanEn", "spanCy", "blurbEn", "blurbCy"):
    _a[_k] = _A9.ANCIENT[_k]
for _lang in ("En", "Cy"):
    _t = _a["story" + _lang][1]
    _cut = _t.index(_A9.ANCIENT["cut" + _lang])
    _a["story" + _lang][1] = _t[:_cut] + _A9.ANCIENT["end" + _lang]
for _k in ("en", "cy", "spanEn", "spanCy", "blurbEn", "blurbCy"):
    _i[_k] = _A9.INDUSTRIAL[_k]
    _m[_k] = _A9.MODERN[_k]
_i["storyEn"] = [_i["storyEn"][1], _A9.INDUSTRIAL["p2En"]]
_i["storyCy"] = [_i["storyCy"][1], _A9.INDUSTRIAL["p2Cy"]]
ERAS = [_a, _A9.ROMAN] + [x for x in ERAS if x["id"] in ("saints", "kings", "medieval")] + [_A9.TUDOR, _i, _m, _A9.TODAY]
EVENTS = [(_A9.age(ev[0], ev[1]),) + ev[1:] for ev in EVENTS]
PEOPLE = [(p[0], "roman" if p[0] in _A9.ROMAN_PEOPLE else "tudor" if p[0] in _A9.TUDOR_PEOPLE else "today" if p[0] in _A9.TODAY_PEOPLE else p[1]) + p[2:] for p in PEOPLE]
_ERA_ORDER = {x["id"]: n for n, x in enumerate(ERAS)}
PEOPLE = sorted(PEOPLE, key=lambda p: (_ERA_ORDER[p[1]], _born(p)))
PLACES = [dict(pl, era=_A9.PLACE_ERA.get(pl["id"], pl["era"])) for pl in PLACES]


# ---------- the changing map (src/kingdoms.py) ----------
from kingdoms import KINGDOMS

# ---------- more historic sites (src/places2.py) ----------
from places2 import MORE_PLACES
PLACES = PLACES + MORE_PLACES

# ---------- historic places of importance: royal seats, abbeys, forts, and places to visit (src/places3.py) ----------
import places3 as _PL3
PLACES = PLACES + _PL3.NEW
# ---------- full pages behind the home page facts (src/factplaces.py) ----------
from factplaces import PLACES as _FACT_PLACES
PLACES = PLACES + _FACT_PLACES


# ---------- proud history (src/pride.py): rewordings, new people and events ----------
import pride as _PR
def _rw(x):
    if isinstance(x, str):
        for _a, _b in _PR.REWORD:
            x = x.replace(_a, _b)
    return x
_all = " ".join(str(f) for row in EVENTS + PEOPLE for f in row) + " ".join(t for v in PEOPLE_EXTRA_LONG.values() for part in v for t in part)
import long as _LG
_all += " ".join(t for v in _LG.PEOPLE_LONG.values() for part in v for t in part)
EVENTS = sorted([tuple(_rw(f) for f in ev) for ev in EVENTS] + _PR.EVENTS_NEW, key=lambda ev: ev[1])
PEOPLE = sorted([tuple(_rw(f) for f in p) for p in PEOPLE] + _PR.PEOPLE_NEW + __import__("pride3").PEOPLE_NEW, key=lambda p: (_ERA_ORDER[p[1]], _born(p)))
PEOPLE_EXTRA_LONG = {k: ([_rw(t) for t in v[0]], [_rw(t) for t in v[1]]) for k, v in PEOPLE_EXTRA_LONG.items()}


# ---------- more famous people and Welsh firsts (src/people2.py) ----------
import people2 as _P2
PEOPLE = sorted(PEOPLE + _P2.PEOPLE_NEW, key=lambda p: (_ERA_ORDER[p[1]], _born(p)))


# ---------- a fuller timeline (src/events2.py) ----------
from events2 import EVENTS2 as _E2
_pids = {p["id"] for p in PLACES}
for _ev in _E2:
    if _ev[10] and _ev[10] not in _pids:
        raise SystemExit(f"src/events2.py: unknown place '{_ev[10]}' in {_ev[5]}")
EVENTS = sorted(EVENTS + _E2, key=lambda ev: ev[1])


# ---------- Brutus of Troy and the History of the Kings of Britain (src/brutus.py) ----------
from brutus import EVENTS as _BRE
EVENTS = sorted(EVENTS + _BRE, key=lambda ev: ev[1])

# ---------- Prince Madog's voyage and the Welsh Indians (src/madog.py) ----------
from madog import EVENTS as _MDE
EVENTS = sorted(EVENTS + _MDE, key=lambda ev: ev[1])

# ---------- How Wales moved the world: the industrial revolution (src/industry.py) ----------
from industry import EVENTS as _INE
EVENTS = sorted(EVENTS + _INE, key=lambda ev: ev[1])

# ---------- King Caradog against Rome (src/caradog.py) ----------
from caradog import EVENTS as _CRE
EVENTS = sorted(EVENTS + _CRE, key=lambda ev: ev[1])

# ---------- Nest ferch Rhys (src/nest.py) ----------
from nest import EVENTS as _NSE
EVENTS = sorted(EVENTS + _NSE, key=lambda ev: ev[1])

# ---------- The coming of Christianity to Britain (src/christianity.py) ----------
from christianity import EVENTS as _CHE
EVENTS = sorted(EVENTS + _CHE, key=lambda ev: ev[1])

# ---------- Saint Patrick, the Briton from Wales (src/patrick.py) ----------
from patrick import EVENTS as _PTE
EVENTS = sorted(EVENTS + _PTE, key=lambda ev: ev[1])

# ---------- The Aberfan disaster, 1966 (src/aberfan.py) ----------
from aberfan import EVENTS as _AFE
EVENTS = sorted(EVENTS + _AFE, key=lambda ev: ev[1])

# ---------- MAC and the Free Wales Army (src/mac.py) ----------
from mac import EVENTS as _MACE
EVENTS = sorted(EVENTS + _MACE, key=lambda ev: ev[1])
# ---------- The drowning of Capel Celyn and Cwm Tryweryn (src/tryweryn.py) ----------
from tryweryn import EVENTS as _TWE
EVENTS = sorted(EVENTS + _TWE, key=lambda ev: ev[1])
# ---------- The Britons in Brittany (src/brittany.py) ----------
from brittany import EVENTS as _BZE
EVENTS = sorted(EVENTS + _BZE, key=lambda ev: ev[1])
# ---------- The clearing of Mynydd Epynt, 1940 (src/epynt.py) ----------
from epynt import EVENTS as _EPE
EVENTS = sorted(EVENTS + _EPE, key=lambda ev: ev[1])
# ---------- The Welsh Not and the fight for the language (src/welshnot.py) ----------
from welshnot import EVENTS as _WNE
EVENTS = sorted(EVENTS + _WNE, key=lambda ev: ev[1])

# ---------- twelve ages (src/ages12.py): last of all, so everything above is moved into the right age ----------
import ages12 as _A12
_A12.apply(globals())

# ---------- no repeats: one entry per person, one title per event ----------
# Two entries for one person put them twice in every list, and two events with one title share a name on the
# timeline and can link to the wrong one on a trail. Give each its own wording instead (Ifan, 13 November 2026).
def _repeats(xs):
    seen, out = set(), []
    for x in xs:
        if x in seen:
            out.append(x)
        seen.add(x)
    return out


if _repeats(p[0] for p in PEOPLE):
    raise SystemExit(f"data.py: the same person is listed twice: {_repeats(p[0] for p in PEOPLE)}")
if _repeats(ev[5] for ev in EVENTS):
    raise SystemExit(f"data.py: two events share a title, give each its own: {_repeats(ev[5] for ev in EVENTS)}")
