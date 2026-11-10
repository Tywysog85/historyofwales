# Nine ages: adds Roman Wales, Tudor and Stuart Wales and Wales Today, and reshapes their neighbours.
# Applied by data.py after ages.py. To add or move an age, edit here; build.py needs a colour (COL) and a picture (ERA_ART) for each id.

ROMAN = dict(id="roman", en="Roman Wales", cy="Cymru Rufeinig", spanEn="AD 48 – 410", spanCy="48 – 410 OC", ill="arches",
  blurbEn="Legions, forts, roads and gold: three and a half centuries on the edge of an empire.",
  blurbCy="Llengoedd, caerau, ffyrdd ac aur: tair canrif a hanner ar ymyl ymerodraeth.",
  storyEn=[
    "The Roman army reached the borders of Wales in AD 48 and found the hardest fighting of the whole conquest of Britain. Caratacus led the Silures and Ordovices until his defeat in 51, the druids of Ynys Môn were attacked in 60, and it took until about 78 to subdue the last of the tribes. To hold the country Rome built two great legionary fortresses on its edges, at Caerleon and Chester, and tied them together with a net of roads and smaller forts such as Segontium at Caernarfon.",
    "Behind the soldiers came towns, trade and new ways of living. Caerwent and Carmarthen became tribal capitals with markets, baths and temples, villas spread across the fertile south, and gold was mined at Dolaucothi. Latin left hundreds of words in Welsh, among them pont, ffenestr, llyfr and eglwys, and Christianity arrived with the martyrs Julius and Aaron at Caerleon. In 383 Magnus Maximus, the Macsen Wledig of later legend, took troops from Britain to seize the empire, and by 410 Roman rule was over. The kings who followed liked to claim him as their ancestor."],
  storyCy=[
    "Cyrhaeddodd byddin Rhufain ffiniau Cymru yn 48 OC, ac yma y cafwyd ymladd caletaf holl goncwest Prydain. Arweiniodd Caradog y Silwriaid a’r Ordofigiaid nes iddo gael ei drechu yn 51, ymosodwyd ar dderwyddon Ynys Môn yn 60, a chymerodd tan tua 78 i ddarostwng yr olaf o’r llwythau. I ddal y wlad cododd Rhufain ddwy gaer fawr i’r llengoedd ar ei hymylon, yng Nghaerllion a Chaer, a’u cysylltu â rhwydwaith o ffyrdd a chaerau llai fel Segontium yng Nghaernarfon.",
    "Ar ôl y milwyr daeth trefi, masnach a ffyrdd newydd o fyw. Daeth Caer-went a Chaerfyrddin yn brifddinasoedd llwythol gyda marchnadoedd, baddonau a themlau, lledodd filâu ar draws tiroedd ffrwythlon y de, a chloddiwyd aur yn Nolaucothi. Gadawodd y Lladin gannoedd o eiriau yn y Gymraeg, yn eu plith pont, ffenestr, llyfr ac eglwys, a chyrhaeddodd Cristnogaeth gyda’r merthyron Iŵl ac Aaron yng Nghaerllion. Yn 383 aeth Magnus Maximus, Macsen Wledig y chwedlau diweddarach, â milwyr o Brydain i gipio’r ymerodraeth, ac erbyn 410 roedd rheolaeth Rhufain ar ben. Hoffai’r brenhinoedd a’i dilynodd honni mai ef oedd eu cyndad."])

TUDOR = dict(id="tudor", en="Tudor and Stuart Wales", cy="Cymru’r Tuduriaid a’r Stiwartiaid", spanEn="1485 – 1750", spanCy="1485 – 1750", ill="book",
  blurbEn="A Welsh king, union with England, a Bible in Welsh, civil war and a nation learning to read.",
  blurbCy="Brenin o Gymro, uno â Lloegr, Beibl Cymraeg, rhyfel cartref a chenedl yn dysgu darllen.",
  storyEn=[
    "Henry Tudor, born at Pembroke, landed near Dale in 1485 and marched through Wales to win the English crown at Bosworth. Many Welsh people saw the old prophecy of a Welsh king fulfilled. His son Henry VIII went further: the Acts of 1536 and 1543 made Wales part of the English realm, divided it into shires, gave it members of parliament and made English the only language of law and office. The monasteries were closed, and the gentry who prospered under the new order looked more and more to London.",
    "Yet the same century saved the language. Parliament ordered a Welsh translation of scripture in 1563, William Salesbury’s New Testament followed in 1567 and William Morgan’s complete Bible in 1588, giving Welsh a standard that every parish heard each Sunday. Wales was mostly for the king in the Civil War, and the Royalists’ defeat at St Fagans in 1648 was probably the largest battle ever fought on Welsh soil. Dissenters founded their first chapel at Llanfaches in 1639, and Quakers left for Pennsylvania. From 1731 the circulating schools of Griffith Jones taught perhaps 200,000 people to read, and the Methodist revival that began in 1735 changed Welsh life for two hundred years."],
  storyCy=[
    "Glaniodd Harri Tudur, a aned ym Mhenfro, ger Dale yn 1485 a gorymdeithio drwy Gymru i ennill coron Lloegr ym Mosworth. Gwelodd llawer o Gymry wireddu’r hen broffwydoliaeth am frenin o Gymro. Aeth ei fab Harri VIII ymhellach: gwnaeth Deddfau 1536 a 1543 Gymru’n rhan o deyrnas Lloegr, ei rhannu’n siroedd, rhoi aelodau seneddol iddi a gwneud Saesneg yn unig iaith y gyfraith a swyddi. Caewyd y mynachlogydd, a throdd y bonedd a ffynnodd dan y drefn newydd fwyfwy at Lundain.",
    "Eto, yr un ganrif a achubodd yr iaith. Gorchmynnodd y Senedd gyfieithu’r ysgrythur i’r Gymraeg yn 1563, daeth Testament Newydd William Salesbury yn 1567 a Beibl cyflawn William Morgan yn 1588, gan roi i’r Gymraeg safon a glywai pob plwyf bob Sul. Roedd Cymru gan mwyaf o blaid y brenin yn y Rhyfel Cartref, a threchu’r Brenhinwyr yn Sain Ffagan yn 1648 oedd y frwydr fwyaf, mae’n debyg, a ymladdwyd erioed ar dir Cymru. Sefydlodd Ymneilltuwyr eu capel cyntaf yn Llanfaches yn 1639, a gadawodd Crynwyr am Bensylfania. O 1731 ymlaen dysgodd ysgolion cylchynol Griffith Jones efallai 200,000 o bobl i ddarllen, a newidiodd y diwygiad Methodistaidd a ddechreuodd yn 1735 fywyd Cymru am ddau gan mlynedd."])

TODAY = dict(id="today", en="Wales Today", cy="Cymru Heddiw", spanEn="1997 – today", spanCy="1997 – heddiw", ill="senedd",
  blurbEn="A parliament of its own, new laws, a million-speaker goal and a nation finding its voice again.",
  blurbCy="Senedd ei hun, cyfreithiau newydd, nod o filiwn o siaradwyr a chenedl yn canfod ei llais eto.",
  storyEn=[
    "On 18 September 1997 Wales voted for its own assembly by 6,721 votes, the narrowest of margins. The National Assembly met for the first time in 1999 with sixty members and limited powers. It grew quickly: a new building opened in Cardiff Bay in 2006, a second referendum in 2011 gave it the power to make laws without asking Westminster, and in 2020 it took the name Senedd Cymru, the Welsh Parliament. Sixteen-year-olds voted for the first time in 2021, and in 2026 the Senedd grew to ninety-six members.",
    "The Wales it governs has changed. The last deep coal mine, Tower Colliery, closed in 2008, and work now lies in services, manufacturing, universities and energy from wind and tide. Laws made in Cardiff have charted a separate course, among them the Well-being of Future Generations Act of 2015. The government has set a target of a million Welsh speakers by 2050; the 2021 census counted 538,300. On the football field Wales reached the semi-final of Euro 2016 and returned to the World Cup in 2022 after sixty-four years. One of the oldest living languages in Europe is heard in a parliament of its own again."],
  storyCy=[
    "Ar 18 Medi 1997 pleidleisiodd Cymru o blaid ei chynulliad ei hun o 6,721 o bleidleisiau, y mwyafrif lleiaf posibl bron. Cyfarfu’r Cynulliad Cenedlaethol am y tro cyntaf yn 1999 gyda thrigain aelod a phwerau cyfyngedig. Tyfodd yn gyflym: agorodd adeilad newydd ym Mae Caerdydd yn 2006, rhoddodd ail refferendwm yn 2011 y grym iddo ddeddfu heb ofyn i San Steffan, ac yn 2020 cymerodd yr enw Senedd Cymru. Pleidleisiodd pobl ifanc un ar bymtheg oed am y tro cyntaf yn 2021, ac yn 2026 tyfodd y Senedd i naw deg chwech o aelodau.",
    "Mae’r Gymru y mae’n ei llywodraethu wedi newid. Caeodd y pwll glo dwfn olaf, Glofa’r Tŵr, yn 2008, ac mae gwaith bellach mewn gwasanaethau, gweithgynhyrchu, prifysgolion ac ynni o’r gwynt a’r llanw. Mae cyfreithiau a wnaed yng Nghaerdydd wedi dilyn llwybr gwahanol, yn eu plith Deddf Llesiant Cenedlaethau’r Dyfodol 2015. Mae’r llywodraeth wedi gosod nod o filiwn o siaradwyr Cymraeg erbyn 2050; cyfrifodd cyfrifiad 2021 538,300. Ar y cae pêl-droed cyrhaeddodd Cymru rownd gynderfynol Ewro 2016 a dychwelyd i Gwpan y Byd yn 2022 ar ôl chwe deg pedair o flynyddoedd. Mae un o ieithoedd byw hynaf Ewrop i’w chlywed yn ei senedd ei hun unwaith eto."])

# reshaped neighbours
ANCIENT = dict(spanEn="230,000 BC – AD 48", spanCy="230,000 CC – 48 OC",
  blurbEn="Ice-age hunters, tomb builders, copper miners and the tribes of the hillforts.",
  blurbCy="Helwyr oes yr iâ, codwyr beddrodau, mwynwyr copr a llwythau’r bryngaerau.",
  cutEn="Rome needed", endEn="When the Roman army arrived in AD 48 it met farmers, smiths and warriors with a thousand years of hillfort life behind them.",
  cutCy="Cymerodd Rhufain", endCy="Pan gyrhaeddodd byddin Rhufain yn 48 OC, cyfarfu â ffermwyr, gofaint a rhyfelwyr a chanddynt fil o flynyddoedd o fywyd y bryngaerau y tu ôl iddynt.")

INDUSTRIAL = dict(en="Industrial Wales", cy="Y Gymru Ddiwydiannol", spanEn="1750 – 1914", spanCy="1750 – 1914",
  blurbEn="Iron, coal, slate and chapel; risings, riots and a nation remade in a single century.",
  blurbCy="Haearn, glo, llechi a chapel; gwrthryfeloedd, terfysgoedd a chenedl wedi’i hail-lunio mewn un ganrif.",
  p2En="Industry remade the people as well as the land. The population grew from under 600,000 in 1801 to nearly two and a half million in 1911, and the chapel became the centre of Welsh-speaking life. When a government report of 1847, the Blue Books, sneered at the language and morals of the Welsh, the anger it caused fed a new national feeling. The National Eisteddfod took its modern form in 1861, settlers sailed for Patagonia in 1865, a university college opened at Aberystwyth in 1872, and by 1907 Wales had a national library and a national museum of its own.",
  p2Cy="Ail-luniodd diwydiant y bobl yn ogystal â’r tir. Tyfodd y boblogaeth o lai na 600,000 yn 1801 i bron i ddwy filiwn a hanner yn 1911, a daeth y capel yn ganolbwynt bywyd Cymraeg. Pan wawdiodd adroddiad y llywodraeth yn 1847, y Llyfrau Gleision, iaith a moesau’r Cymry, porthodd y dicter a achosodd deimlad cenedlaethol newydd. Cymerodd yr Eisteddfod Genedlaethol ei ffurf fodern yn 1861, hwyliodd ymfudwyr am Batagonia yn 1865, agorodd coleg prifysgol yn Aberystwyth yn 1872, ac erbyn 1907 roedd gan Gymru lyfrgell genedlaethol ac amgueddfa genedlaethol ei hun.")

MODERN = dict(en="Twentieth-Century Wales", cy="Cymru’r Ugeinfed Ganrif", spanEn="1914 – 1997", spanCy="1914 – 1997",
  blurbEn="War, depression, the NHS, drowned valleys and the fight for the language.",
  blurbCy="Rhyfel, dirwasgiad, y Gwasanaeth Iechyd, cymoedd a foddwyd a’r frwydr dros yr iaith.")

ROMAN_PEOPLE = {"caratacus"}
TUDOR_PEOPLE = {"harri-tudur", "william-morgan", "edward-lhuyd", "griffith-jones", "howell-harris"}
TODAY_PEOPLE = {"rhodri-morgan", "tanni-grey-thompson"}
PLACE_ERA = dict(caerleon="roman", dolaucothi="roman", dale="tudor", llanrhaeadr="tudor", stfagans="tudor", senedd="today")


def age(era, y):
    if era == "ancient" and y >= 48:
        return "roman"
    if era == "industrial" and y < 1750:
        return "tudor"
    if era == "modern" and y >= 1997:
        return "today"
    return era


TEACH = {
 "roman": dict(qEn="What did the Romans change in Wales, and what did they leave untouched?", qCy="Beth newidiodd y Rhufeiniaid yng Nghymru, a beth adawsant heb ei gyffwrdd?",
  aEn=["Use the map to find the Roman fort, road or town nearest your school, and work out why it was built there.", "Collect ten Welsh words that came from Latin, such as pont, ffenestr and llyfr. What do they tell us about what the Romans brought?", "Debate: was Caratacus right to fight, or would peace with Rome have been better for his people?"],
  aCy=["Defnyddiwch y map i ddod o hyd i’r gaer, y ffordd neu’r dref Rufeinig agosaf at eich ysgol, a cheisiwch esbonio pam y’i codwyd yno.", "Casglwch ddeg gair Cymraeg a ddaeth o’r Lladin, fel pont, ffenestr a llyfr. Beth maen nhw’n ei ddweud am yr hyn a ddaeth gyda’r Rhufeiniaid?", "Dadl: oedd Caradog yn iawn i ymladd, neu a fyddai heddwch â Rhufain wedi bod yn well i’w bobl?"]),
 "tudor": dict(qEn="Did the Tudors help Wales or harm it?", qCy="Ai helpu Cymru neu ei niweidio wnaeth y Tuduriaid?",
  aEn=["Compare the Acts of Union with the Welsh Bible of 1588: one pushed Welsh out of the courts, the other put it in every church. Which mattered more?", "Find out how Griffith Jones’s circulating schools worked, and plan a three-month school of your own.", "Write a letter home from a Welsh soldier after the battle of St Fagans in 1648."],
  aCy=["Cymharwch y Deddfau Uno â Beibl Cymraeg 1588: gwthiodd y naill y Gymraeg o’r llysoedd, a rhoddodd y llall hi ym mhob eglwys. Pa un oedd bwysicaf?", "Darganfyddwch sut roedd ysgolion cylchynol Griffith Jones yn gweithio, a chynlluniwch eich ysgol dri mis eich hun.", "Ysgrifennwch lythyr adref gan filwr o Gymro ar ôl brwydr Sain Ffagan yn 1648."]),
 "today": dict(qEn="What difference has devolution made to Wales?", qCy="Pa wahaniaeth mae datganoli wedi’i wneud i Gymru?",
  aEn=["Find one law made in the Senedd that affects your daily life, and explain it to the class.", "Compare the referendum results of 1979, 1997 and 2011. Why did opinion change?", "Hold your own Senedd debate: what one new law would you pass for Wales?"],
  aCy=["Dewch o hyd i un gyfraith a wnaed yn y Senedd sy’n effeithio ar eich bywyd bob dydd, a’i hesbonio i’r dosbarth.", "Cymharwch ganlyniadau refferenda 1979, 1997 a 2011. Pam newidiodd y farn?", "Cynhaliwch eich dadl Senedd eich hun: pa un gyfraith newydd fyddech chi’n ei phasio i Gymru?"]),
}
