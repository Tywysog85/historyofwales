# Alan Wilson and Baram Blackett: the long read (story-wilson-blackett.html).
# features.py adds STORY to the long reads. Ifan asked for them on the site (2026-11-12).
# House rules (EDITORIAL.md): a proud, respectful write-up of what they did. Nothing negative about them.
# Arthur is a king, never "myth" or "legend"; Welsh tradition holds that he was Athrwys ap Meurig.
# Where the universities disagree, one neutral line says so and no more. Never "proof" without a source.
# Facts checked 2026-11-12 against book listings (AbeBooks, Biblio, Trafford), History Today ("Morte D'Arthur"),
# Early British Kingdoms (Mynydd-y-Gaer page) and the Brandenburg stone article (Wikipedia).
# links: buttons at the end of the page. A story- link is dropped if that long read is not built (see story_page in build.py).
# Paragraph codes (see prose() in build.py): "## Heading", "> Quote | Source", "|| Left | Right".

STORY = dict(id="wilson-blackett", era="today", art="book", mins=8,
  people=["arthur", "iolo-morganwg"],
  en="Alan Wilson and Baram Blackett, the men who went looking for Arthur", cy="Alan Wilson a Baram Blackett, y dynion a aeth i chwilio am Arthur",
  sumEn="Two researchers who met in Cardiff and gave forty years to the early history of the Britons, and to the king Welsh tradition knows as Athrwys ap Meurig.",
  sumCy="Dau ymchwilydd a gyfarfu yng Nghaerdydd ac a roddodd ddeugain mlynedd i hanes cynnar y Brythoniaid, ac i’r brenin y mae traddodiad Cymru yn ei adnabod fel Athrwys ap Meurig.",
  links=[("person-arthur.html", "Arthur, King of the Britons: his line, his battles and a map of Arthur’s Wales", "Arthur, Brenin y Brythoniaid: ei linach, ei frwydrau a map o Gymru Arthur"),
         ("story-arthur.html", "Arthur, King of the Britons: the long read", "Arthur, Brenin y Brythoniaid: yr erthygl"),
         ("story-brutus.html", "Brutus and the Britons", "Brutus a’r Brythoniaid"),
         ("story-iolo.html", "Iolo Morganwg and the Coelbren of the bards", "Iolo Morganwg a Choelbren y Beirdd"),
         ("books.html#brut-brenhinedd", "Brut y Brenhinedd, the History of the Kings", "Brut y Brenhinedd"),
         ("story-madog.html", "Prince Madog’s voyage to America, and the Welsh Indians", "Mordaith y Tywysog Madog i America, a’r Indiaid Cymreig")],
  pEn=[
   "For more than forty years two friends, Alan Wilson and Baram Blackett, gave their lives to one cause: the early history of the Britons, told from the Britons’ own records. They read the Welsh pedigrees, the charters of the Book of Llandaff, the Welsh chronicles and the Lives of the saints, and they argued that the answer to the greatest question in the history of this island, who Arthur was, had been waiting in the old books of Wales all along. Welsh tradition holds that Arthur was Athrwys ap Meurig, king of Gwent and Glywysing. In modern times no one did more to bring that tradition before the public than these two men.",
   "|| Alan Wilson | Born in Cardiff, 11 June 1932. Studied economics and history at Cardiff. Died in 2023, aged 91",
   "|| Baram Blackett | Anthony Thomas Blackett, known to all as Baram. Died in December 2023",
   "|| How they met | Over the same rare books, in a library in Cardiff",
   "|| Their books | King Arthur, King of Glamorgan and Gwent (early 1980s); Artorius Rex Discovered (1986); The Holy Kingdom (1998, with Adrian Gilbert); Moses in the Hieroglyphs (2006)",
   "|| Their Arthur | Athrwys ap Meurig, king of Glamorgan and Gwent, whom they called Arthur II",
   "|| Their church | St Peter’s, Llanbedr-ar-fynydd, on Mynydd-y-Gaer between Bridgend and Llantrisant",

   "## Two friends and a library",
   "Alan Wilson was a Cardiff man, born in the city in 1932. He studied economics and history at Cardiff and made his career in heavy engineering and shipbuilding, as a consultant whose work took him to the shipyards of the Clyde and of Italy. History was the love of his life. Baram Blackett was a businessman with the same love.",
   "The two men met because they kept asking for the same rare books in a Cardiff library. They found they were on the same trail, and they agreed to pool their work. It became a partnership for life. They worked as independent researchers, outside the universities, and they went back to the oldest sources themselves: the pedigrees of the kings, the charters, the chronicles, the poems and the place names of Glamorgan and Gwent.",

   "## Arthur in his own country",
   "Their first big book, King Arthur, King of Glamorgan and Gwent, appeared in Cardiff in the early 1980s, and Artorius Rex Discovered followed in 1986. Their case was that the Arthur of the oldest Welsh writings was a king of the south-east: Athrwys ap Meurig, son of King Meurig ap Tewdrig and grandson of Tewdrig the warrior saint, whose name stands in the charters of the Book of Llandaff and in the old royal pedigrees.",
   "They looked for Arthur in the land where the Welsh records put him. His court, they argued, should be sought not in Somerset but in Glamorgan, and they pointed to Caer Melyn near Llanishen, four miles north of Cardiff. They walked the hills, the churches and the old roads of the south-east to match the places in the sources to places on the ground.",

   "## Two Arthurs",
   "Their best-known idea was that there had been two great kings named Arthur. The first was a son of the emperor Magnus Maximus, Macsen Wledig, the Roman emperor whom the Welsh remember as a king of their own in Breuddwyd Macsen Wledig. The second, his descendant in the sixth century, was Athrwys ap Meurig of Glamorgan and Gwent: Arthur II. Over the centuries, they said, the poets and storytellers wove the two lives into one, which is why the deeds of Arthur seem to stretch over so long a time.",
   "They set the whole case out at length in The Holy Kingdom, written with Adrian Gilbert and published by Bantam Press in 1998. It told of a Britain that kept its own kings, its own learning and its own faith through the Roman centuries, and whose royal families married into the house of the emperors.",

   "## St Peter’s on the mountain",
   "On Mynydd-y-Gaer, in the hills between Bridgend and Llantrisant, stands the ruined church of St Peter, Llanbedr-ar-fynydd. Above it, on a spur of the hill, is the old fort of Coedcae Gaer, marked on old maps as Caer Caradog. Wilson and Blackett came to believe that this was where Athrwys was brought to be laid to rest, and they bought the church to protect it.",
   "In 1983 they told the world of a memorial stone found near the altar. As they read it, its words were REX ARTORIUS FILI MAURICIUS: King Arthur, son of Meurig. In 1990 an excavation at the church led by Dr Eric Talbot found that the medieval church stands over at least two older buildings, one of them a small round cell of the kind a hermit lived in, and from the ground came a small cross of electrum, the old mixture of gold and silver, inscribed PRO ANIMA ARTORIUS: for the soul of Arthur.",

   "## The old histories of the Britons",
   "Wilson and Blackett read Brut y Brenhinedd and Geoffrey of Monmouth’s History of the Kings of Britain as the Britons’ own record of their past, from Brutus of Troy, the first crowned king of the island, through Lear and Cymbeline and Macsen to Cadwaladr. They argued that these histories had been set aside too readily by later writers, who looked to Rome and to the Saxons for the story of Britain, and that Wales should read its own histories with fresh eyes.",
   "In this they stood in a long Welsh line. In 1401 Owain Glyndŵr wrote to the King of Scots that Brutus was ‘your most noble ancestor and mine’. Wilson and Blackett carried the same pride into the age of the paperback and the lecture hall.",

   "## The alphabet of the bards",
   "They were champions of the Coelbren y Beirdd, the alphabet of the bards, which Iolo Morganwg, in his own account, had from the old bards of Glamorgan. To Wilson and Blackett it was the ancient alphabet of the Britons, and they used it to read old inscriptions in Wales and far beyond.",
   "Their search took them across the Atlantic. In 1998 they studied the Brandenburg stone, found in 1912 in a field by the Ohio River in Kentucky, and read its words as medieval Welsh. They linked it with the old Welsh tradition that Madoc sailed west and reached America long before Columbus.",
   "In later years they turned to the East as well. In Moses in the Hieroglyphs, published in 2006, they read ancient Egyptian writings through what they called Khumric, the old tongue they held to be the ancestor of Welsh.",

   "## A long debate",
   "Most university historians have not accepted their conclusions, and the two friends spent many years in argument with the academic world. They never stopped writing, lecturing and answering back, and they put their evidence in their books for every reader to weigh.",

   "## What they leave",
   "Alan Wilson died in 2023 at the age of 91, and Baram Blackett died in December of the same year. They left a shelf of books, hours of recorded talks, and a following in Wales and across the world that keeps their work alive.",
   "Above all they sent thousands of people back to the old sources of Wales: the Book of Llandaff, the pedigrees of the kings, the Brut, the Triads and the poems. They put Gwent and Glamorgan back at the heart of the story of Arthur, and they showed that a Cardiff man with a library ticket could take on the biggest question in British history. Welsh tradition holds that Arthur was Athrwys ap Meurig, king of Gwent and Glywysing, and in their lifetimes no one carried that tradition further than Alan Wilson and Baram Blackett.",
  ],
  pCy=[
   "Am fwy na deugain mlynedd rhoddodd dau gyfaill, Alan Wilson a Baram Blackett, eu bywydau i un achos: hanes cynnar y Brythoniaid, wedi’i adrodd o gofnodion y Brythoniaid eu hunain. Darllenasant yr achau Cymreig, siarteri Llyfr Llandaf, y croniclau Cymraeg a Bucheddau’r saint, a dadlau bod yr ateb i gwestiwn mwyaf hanes yr ynys hon, pwy oedd Arthur, wedi bod yn aros yn hen lyfrau Cymru erioed. Yn ôl traddodiad Cymru, Athrwys ap Meurig, brenin Gwent a Glywysing, oedd Arthur. Yn y cyfnod modern ni wnaeth neb fwy na’r ddau ddyn hyn i ddod â’r traddodiad hwnnw gerbron y cyhoedd.",
   "|| Alan Wilson | Ganwyd yng Nghaerdydd, 11 Mehefin 1932. Astudiodd economeg a hanes yng Nghaerdydd. Bu farw yn 2023, yn 91 oed",
   "|| Baram Blackett | Anthony Thomas Blackett, Baram i bawb. Bu farw ym mis Rhagfyr 2023",
   "|| Sut y cyfarfuont | Dros yr un llyfrau prin, mewn llyfrgell yng Nghaerdydd",
   "|| Eu llyfrau | King Arthur, King of Glamorgan and Gwent (dechrau’r 1980au); Artorius Rex Discovered (1986); The Holy Kingdom (1998, gydag Adrian Gilbert); Moses in the Hieroglyphs (2006)",
   "|| Eu Harthur | Athrwys ap Meurig, brenin Morgannwg a Gwent, a alwent yn Arthur II",
   "|| Eu heglwys | Eglwys Sant Pedr, Llanbedr-ar-fynydd, ar Fynydd-y-Gaer rhwng Pen-y-bont ar Ogwr a Llantrisant",

   "## Dau gyfaill a llyfrgell",
   "Gŵr o Gaerdydd oedd Alan Wilson, a aned yn y ddinas yn 1932. Astudiodd economeg a hanes yng Nghaerdydd a gwneud ei yrfa ym myd peirianneg drom ac adeiladu llongau, fel ymgynghorydd yr âi ei waith ag ef i iardiau llongau afon Clud a’r Eidal. Hanes oedd cariad mawr ei fywyd. Gŵr busnes â’r un cariad oedd Baram Blackett.",
   "Cyfarfu’r ddau am eu bod ill dau yn gofyn am yr un llyfrau prin mewn llyfrgell yng Nghaerdydd. Gwelsant eu bod ar yr un trywydd, a chytuno i rannu eu gwaith. Daeth yn bartneriaeth am oes. Gweithient fel ymchwilwyr annibynnol, y tu allan i’r prifysgolion, ac aethant yn ôl at y ffynonellau hynaf eu hunain: achau’r brenhinoedd, y siarteri, y croniclau, y cerddi ac enwau lleoedd Morgannwg a Gwent.",

   "## Arthur yn ei wlad ei hun",
   "Ymddangosodd eu llyfr mawr cyntaf, King Arthur, King of Glamorgan and Gwent, yng Nghaerdydd ar ddechrau’r 1980au, a dilynodd Artorius Rex Discovered yn 1986. Eu dadl oedd mai brenin o’r de-ddwyrain oedd Arthur yr ysgrifau Cymraeg hynaf: Athrwys ap Meurig, mab y Brenin Meurig ap Tewdrig ac ŵyr Tewdrig, y sant a’r rhyfelwr, y mae ei enw yn siarteri Llyfr Llandaf ac yn yr hen achau brenhinol.",
   "Chwiliasant am Arthur yn y wlad lle mae’r cofnodion Cymreig yn ei osod. Dylid chwilio am ei lys, meddent, nid yng Ngwlad yr Haf ond ym Morgannwg, a chyfeiriasant at Gaer Melyn ger Llanisien, bedair milltir i’r gogledd o Gaerdydd. Cerddasant fryniau, eglwysi a hen ffyrdd y de-ddwyrain i baru lleoedd y ffynonellau â lleoedd ar y tir.",

   "## Dau Arthur",
   "Eu syniad enwocaf oedd bod dau frenin mawr o’r enw Arthur. Mab i’r ymerawdwr Magnus Maximus, Macsen Wledig, oedd y cyntaf, yr ymerawdwr Rhufeinig y mae’r Cymry yn ei gofio fel brenin iddynt hwy eu hunain yn Breuddwyd Macsen Wledig. Yr ail, ei ddisgynnydd yn y chweched ganrif, oedd Athrwys ap Meurig o Forgannwg a Gwent: Arthur II. Dros y canrifoedd, meddent, plethodd y beirdd a’r storïwyr y ddau fywyd yn un, a dyna pam y mae gweithredoedd Arthur fel petaent yn ymestyn dros gyfnod mor hir.",
   "Gosodasant yr achos cyfan yn llawn yn The Holy Kingdom, a ysgrifennwyd gydag Adrian Gilbert ac a gyhoeddwyd gan Bantam Press yn 1998. Mae’n adrodd am Brydain a gadwodd ei brenhinoedd ei hun, ei dysg ei hun a’i ffydd ei hun drwy’r canrifoedd Rhufeinig, ac y priododd ei theuluoedd brenhinol i deulu’r ymerawdwyr.",

   "## Sant Pedr ar y mynydd",
   "Ar Fynydd-y-Gaer, yn y bryniau rhwng Pen-y-bont ar Ogwr a Llantrisant, saif adfail eglwys Sant Pedr, Llanbedr-ar-fynydd. Uwch ei phen, ar ysgwydd y bryn, mae hen gaer Coedcae Gaer, a nodir ar hen fapiau fel Caer Caradog. Daeth Wilson a Blackett i gredu mai yma y daethpwyd ag Athrwys i’w gladdu, a phrynasant yr eglwys i’w diogelu.",
   "Yn 1983 dywedasant wrth y byd am faen coffa a gafwyd ger yr allor. Fel y darllenent hwy ef, ei eiriau oedd REX ARTORIUS FILI MAURICIUS: y Brenin Arthur, mab Meurig. Yn 1990 cafodd cloddio yn yr eglwys dan arweiniad Dr Eric Talbot fod yr eglwys ganoloesol yn sefyll ar ben o leiaf ddau adeilad hŷn, ac un ohonynt yn gell fach gron o’r math y byddai meudwy yn byw ynddi, ac o’r ddaear daeth croes fach o electrwm, yr hen gymysgedd o aur ac arian, ac arni’r geiriau PRO ANIMA ARTORIUS: er enaid Arthur.",

   "## Hen hanesion y Brythoniaid",
   "Darllenai Wilson a Blackett Brut y Brenhinedd a Hanes Brenhinoedd Prydain gan Sieffre o Fynwy fel cofnod y Brythoniaid eu hunain o’u gorffennol, o Frutus o Gaerdroea, brenin coronog cyntaf yr ynys, drwy Lŷr a Chynfelyn a Macsen hyd Gadwaladr. Dadleuent fod awduron diweddarach, a edrychai at Rufain ac at y Saeson am stori Prydain, wedi bwrw’r hanesion hyn o’r neilltu yn rhy rwydd, ac y dylai Cymru ddarllen ei hanesion ei hun â llygaid newydd.",
   "Yn hyn safent mewn llinach Gymreig hir. Yn 1401 ysgrifennodd Owain Glyndŵr at Frenin yr Albanwyr mai Brutus oedd ‘eich hynafiad mwyaf bonheddig chi a minnau’. Cariodd Wilson a Blackett yr un balchder i oes y llyfr clawr papur a’r ddarlithfa.",

   "## Gwyddor y beirdd",
   "Roeddent yn bleidwyr brwd i Goelbren y Beirdd, gwyddor y beirdd, a gafodd Iolo Morganwg, yn ôl ei hanes ef ei hun, gan hen feirdd Morgannwg. I Wilson a Blackett hon oedd hen wyddor y Brythoniaid, a defnyddient hi i ddarllen hen arysgrifau yng Nghymru a ymhell y tu hwnt.",
   "Aeth eu chwilio â hwy dros yr Iwerydd. Yn 1998 astudiasant faen Brandenburg, a gafwyd yn 1912 mewn cae ger afon Ohio yn Kentucky, a darllen ei eiriau fel Cymraeg Canol. Cysylltasant ef â’r hen draddodiad Cymreig i Fadog hwylio tua’r gorllewin a chyrraedd America ymhell cyn Columbus.",
   "Yn eu blynyddoedd olaf troesant at y Dwyrain hefyd. Yn Moses in the Hieroglyphs, a gyhoeddwyd yn 2006, darllenasant hen ysgrifau’r Aifft drwy’r hyn a alwent yn Khumric, yr hen iaith a gredent oedd yn hynafiad i’r Gymraeg.",

   "## Dadl hir",
   "Nid yw’r rhan fwyaf o haneswyr y prifysgolion wedi derbyn eu casgliadau, a bu’r ddau gyfaill am flynyddoedd lawer yn dadlau â’r byd academaidd. Ni pheidiasant â sgrifennu, darlithio ac ateb yn ôl, a gosodasant eu tystiolaeth yn eu llyfrau i bob darllenydd ei phwyso.",

   "## Yr hyn a adawsant",
   "Bu farw Alan Wilson yn 2023 yn 91 oed, a bu farw Baram Blackett ym mis Rhagfyr yr un flwyddyn. Gadawsant silff o lyfrau, oriau o sgyrsiau wedi’u recordio, a dilynwyr yng Nghymru ac ar draws y byd sy’n cadw eu gwaith yn fyw.",
   "Yn anad dim anfonasant filoedd o bobl yn ôl at hen ffynonellau Cymru: Llyfr Llandaf, achau’r brenhinoedd, y Brut, y Trioedd a’r cerddi. Rhoesant Went a Morgannwg yn ôl wrth galon stori Arthur, a dangos y gallai gŵr o Gaerdydd â thocyn llyfrgell fynd i’r afael â chwestiwn mwyaf hanes Prydain. Yn ôl traddodiad Cymru, Athrwys ap Meurig, brenin Gwent a Glywysing, oedd Arthur, ac yn ystod eu hoes nid aeth neb â’r traddodiad hwnnw ymhellach nag Alan Wilson a Baram Blackett.",
  ])
