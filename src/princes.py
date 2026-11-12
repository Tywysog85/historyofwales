# The kings and princes of Wales (November 2026): full-length person pages for the great rulers of Wales,
# from Merfyn Frych and Rhodri Mawr to Llywelyn ap Gruffudd, his daughter Gwenllian and Owain Lawgoch.
# Ifan asked (12 November 2026) for "Llywelyn the Great etc" and "Rhodri the Great etc": as many of the medieval
# kings and princes as possible, with real pictures, sources beside the key claims, and the pages linked together.
#
# House rules (EDITORIAL.md): proud, nothing negative about the people of Welsh history, and kings are kings:
# every ruler before about 1100 is a king (brenin); "prince" (tywysog) only for those who took that title.
#
# What is here:
#   LONG    slug -> (English paragraphs, Welsh paragraphs): the long text for a person page that is already on the
#           site with a short text. long.py puts these over the short ones.
#   PEOPLE  new people, in the people2a.py format (people2.py adds them to the site).
#   GROUPS  the "Kings and princes of Wales" block shown on every page of the set (build.py, princes_circle()).
#   LINKS   the pages that go with the block.
#
# Paragraph codes (see prose() in build.py): "## Heading", "> Quote | Source", "|| Left | Right" (a fact table).
# Sources beside the claims: [[cite:key]] after the full stop (src/cites.py); the keys for these pages are in CITES below.
#
# Sources used and checked (November 2026): the Annales Cambriae (ed. Phillimore, Y Cymmrodor 9, 1888); Brut y
# Tywysogion, Peniarth MS 20 version (tr. Thomas Jones, 1952); the Annals of Ulster; Asser, Life of King Alfred,
# ch. 80; Gerald of Wales, Description of Wales I.2; T. M. Charles-Edwards, Wales and the Britons 350-1064 (Oxford,
# 2013); J. E. Lloyd, A History of Wales (1911); Kari Maund, The Welsh Kings (2006); the Dictionary of Welsh Biography.
from people2a import P

LONG = {}

# ---------------------------------------------------------------- the age of Rhodri Mawr

LONG["merfyn-frych"] = (
 ["Merfyn Frych, Merfyn the Freckled, became king of Gwynedd in 825 and founded the royal house that ruled Wales for the next four and a half centuries. His son was Rhodri Mawr; his line ran on through Hywel Dda, Gruffudd ap Cynan and Owain Gwynedd to the two Llywelyns. The chronicle of the Welsh records his death in 844, and the scholars of his own court called him king of the Britons.",
  "|| King of Gwynedd | 825–844",
  "|| Father | Gwriad ab Elidyr",
  "|| Mother | Esyllt, daughter of King Cynan Dindaethwy of Gwynedd",
  "|| Wife | Nest, of the royal house of Powys",
  "|| Son | Rhodri Mawr",
  "|| Died | 844",
  "## From the land of Manaw",
  "Welsh tradition remembers Merfyn as a man who came from over the sea. An old poem in the Red Book of Hergest calls him ‘Merfyn Frych from the land of Manaw’, and Manaw is the Welsh name of the Isle of Man. On Man there is still a stone cross carved with the name of a Gwriad, the name of Merfyn’s father. His family traced its line back to Llywarch Hen and the kings of the Old North, the Britons of the north who had fought the English in the age of Urien and Taliesin.[[cite:merfyn-wiki]]",
  "Merfyn came to the throne of Gwynedd through his mother, Esyllt, the daughter of King Cynan Dindaethwy, of the old line of Cunedda. When Cynan’s house had worn itself out, Gwynedd turned to his grandson. Merfyn married Nest of the royal house of Powys, so that his son would carry the blood of both kingdoms.",
  "## A court of learning",
  "Merfyn’s court was one of the places of learning of its age. Irish scholars travelling to the courts of the Continent stopped there on their way. One of them left behind a puzzle, a message written in Greek letters standing for Latin, set as a test of learning for the scholars who came to the court of ‘Merfyn, king of the Britons’. A copy was found centuries later at Bamberg in Germany, and is known as the Bamberg Cryptogram. It shows that a Welsh king’s hall was known to the learned men of Europe.[[cite:merfyn-wiki]]",
  "It was in Merfyn’s reign, too, that the Historia Brittonum, the History of the Britons, was put together. The writer, remembered as Nennius, gathered the history of the island from Brutus and the Romans to the wars against the English, and the book contains the list of the twelve battles of Arthur. One copy is dated by ‘the fourth year of King Merfyn’. It was written to show the Britons that their history was long and great, and that the island had been theirs.[[cite:historia-brittonum,merfyn-wiki]]",
  "## The founder of a line",
  "Merfyn ruled for nineteen years. The Annales Cambriae set down his death in 844 in two words, ‘Mermin moritur’, Merfyn dies. His son Rhodri took the kingdom and made it the greatest power in Wales. The descendants of Merfyn are called after him, the Merfynion, and every king and prince of Gwynedd from Rhodri Mawr to Llywelyn ap Gruffudd came from his line.[[cite:ac-wales]]"],
 ["Daeth Merfyn Frych yn frenin Gwynedd yn 825, a sefydlodd y tŷ brenhinol a reolodd Gymru am y pedair canrif a hanner nesaf. Ei fab oedd Rhodri Mawr; rhedodd ei linach ymlaen drwy Hywel Dda, Gruffudd ap Cynan ac Owain Gwynedd hyd y ddau Lywelyn. Mae cronicl y Cymry yn cofnodi ei farw yn 844, ac ysgolheigion ei lys ei hun a’i galwodd yn frenin y Brythoniaid.",
  "|| Brenin Gwynedd | 825–844",
  "|| Tad | Gwriad ab Elidyr",
  "|| Mam | Esyllt, merch y Brenin Cynan Dindaethwy o Wynedd",
  "|| Gwraig | Nest, o dŷ brenhinol Powys",
  "|| Mab | Rhodri Mawr",
  "|| Bu farw | 844",
  "## O dir Manaw",
  "Mae traddodiad Cymru yn cofio Merfyn fel gŵr a ddaeth dros y môr. Mae hen gerdd yn Llyfr Coch Hergest yn ei alw’n ‘Merfyn Frych o dir Manaw’, a Manaw yw’r enw Cymraeg ar Ynys Manaw. Ar Ynys Manaw mae croes garreg o hyd ag enw Gwriad wedi’i naddu arni, sef enw tad Merfyn. Olrheiniai ei deulu ei linach yn ôl at Lywarch Hen a brenhinoedd yr Hen Ogledd, Brythoniaid y gogledd a ymladdodd y Saeson yn oes Urien a Thaliesin.[[cite:merfyn-wiki]]",
  "Daeth Merfyn i orsedd Gwynedd drwy ei fam, Esyllt, merch y Brenin Cynan Dindaethwy, o hen linach Cunedda. Pan ddaeth tŷ Cynan i ben, trodd Gwynedd at ei ŵyr. Priododd Merfyn â Nest o dŷ brenhinol Powys, fel y byddai gwaed y ddwy deyrnas yn ei fab.",
  "## Llys dysg",
  "Roedd llys Merfyn yn un o fannau dysg ei oes. Arhosai ysgolheigion o Iwerddon yno ar eu ffordd i lysoedd y Cyfandir. Gadawodd un ohonynt bos ar ei ôl, neges mewn llythrennau Groeg yn sefyll am Ladin, yn brawf ar ddysg yr ysgolheigion a ddeuai i lys ‘Merfyn, brenin y Brythoniaid’. Cafwyd copi ganrifoedd yn ddiweddarach yn Bamberg yn yr Almaen, a’i enw yw Cryptogram Bamberg. Mae’n dangos bod neuadd brenin o Gymro yn hysbys i wŷr dysgedig Ewrop.[[cite:merfyn-wiki]]",
  "Yn nheyrnasiad Merfyn hefyd y lluniwyd yr Historia Brittonum, Hanes y Brythoniaid. Casglodd yr awdur, a gofir fel Nennius, hanes yr ynys o Frutus a’r Rhufeiniaid hyd y rhyfeloedd yn erbyn y Saeson, ac yn y llyfr mae rhestr deuddeg brwydr Arthur. Mae un copi wedi’i ddyddio wrth ‘bedwaredd flwyddyn y Brenin Merfyn’. Fe’i hysgrifennwyd i ddangos i’r Brythoniaid fod eu hanes yn hir ac yn fawr, ac mai eu hynys hwy oedd hi.[[cite:historia-brittonum,merfyn-wiki]]",
  "## Sylfaenydd llinach",
  "Teyrnasodd Merfyn am bedair blynedd ar bymtheg. Mae’r Annales Cambriae yn cofnodi ei farw yn 844 mewn dau air, ‘Mermin moritur’, bu farw Merfyn. Cymerodd ei fab Rhodri y deyrnas a’i gwneud yn rym mwyaf Cymru. Gelwir disgynyddion Merfyn ar ei ôl, y Merfyniaid, a deuai pob brenin a thywysog yng Ngwynedd o Rodri Mawr hyd Lywelyn ap Gruffudd o’i linach ef.[[cite:ac-wales]]"])

LONG["rhodri-mawr"] = (
 ["Rhodri ap Merfyn is one of only two rulers of Wales whom the Welsh have called Mawr, the Great. He inherited Gwynedd in 844, gained Powys in 855, and through his wife Angharad brought Seisyllwg, the lands of Ceredigion and Ystrad Tywi, into his family. For the first time since the Romans, most of Wales answered to one king. He beat the Vikings when the rest of Britain was falling to them, and the annals of Ireland called him king of the Britons. From his sons came the royal houses of Gwynedd, Deheubarth and Powys.",
  "|| Born | about 820",
  "|| Father | Merfyn Frych, king of Gwynedd",
  "|| Mother | Nest, of the royal house of Powys",
  "|| Wife | Angharad, sister of King Gwgon of Ceredigion",
  "|| King of Gwynedd | 844–878",
  "|| King of Powys | from 855",
  "|| Great victory | over the Danes on Ynys Môn, 856, when he killed their leader Horm",
  "|| Died | 878, fighting the English",
  "|| Sons | Anarawd, Cadell, Merfyn, Gwriad and others",
  "## Three kingdoms",
  "Rhodri came to the throne of Gwynedd when his father Merfyn Frych died in 844. His mother Nest was of the royal house of Powys, and when her brother, King Cyngen of Powys, died on pilgrimage in Rome in 855, Powys came to Rhodri. Cyngen was the king who raised the Pillar of Eliseg near Llangollen, and with Powys Rhodri took up a line of kings as old as his own.",
  "Rhodri married Angharad, the sister of Gwgon, king of Ceredigion. When Gwgon was drowned in 871, Seisyllwg, the kingdom of Ceredigion and Ystrad Tywi, passed to Rhodri’s family, and later to his son Cadell. From the mountains of Eryri to the valley of the Tywi, the land was ruled by Rhodri and his house.[[cite:ac-wales,brut-jones]]",
  "## The king who beat the Vikings",
  "Rhodri’s reign was the age of the great Viking armies. The Danes raided every coast of Britain and Ireland, and in the 860s and 870s their Great Army broke the English kingdoms of Northumbria, East Anglia and Mercia one after another. Ynys Môn, the heart of Gwynedd, lay open to their ships.",
  "In 856 a Danish fleet landed on Môn. Rhodri met them and beat them, and killed their leader, Horm. The victory was so great that it was set down in Ireland, in the Annals of Ulster, which name the killer of Horm as Rhodri son of Merfyn, king of Wales. Many historians believe that the Irish poet Sedulius Scottus, at the court of Liège across the sea, wrote his Latin verses on a great victory over the Northmen in honour of Rhodri’s.[[cite:au-856,charles-edwards-2013]]",
  "> Horm, chief of the dark foreigners, was killed by Rhodri son of Mervyn, king of Wales. | Annals of Ulster, 856",
  "## Exile and return",
  "In 877 the Danes came back in force. The Welsh chronicle remembers ‘the Sunday battle on Môn’, Gwaith Dydd Sul, and after it Rhodri crossed to Ireland. The Annals of Ulster record his coming: Rhodri son of Merfyn, king of the Britons, had come to Ireland, fleeing from the Black Foreigners. He did not stay. The next year he was back in Gwynedd, and in 878 he fell fighting the English of Mercia, with his son Gwriad beside him.[[cite:ac-wales,au-877,au-878]]",
  "## Dial Rhodri: Rhodri’s vengeance",
  "His sons did not let it rest. In 881 the Mercians came again, and at the mouth of the river Conwy Anarawd ap Rhodri and his brothers broke them. The Annales Cambriae call the battle ‘the vengeance for Rhodri, by God’, and it has been remembered ever since as Dial Rhodri. No English army took Gwynedd for two hundred years.[[cite:ac-wales]]",
  "## Rhodri the Great",
  "Only two rulers of Wales have been called Mawr: Rhodri, and Llywelyn ab Iorwerth, Llywelyn Fawr. Rhodri earned it by bringing most of Wales under one house, and by holding it against the Vikings when the kingdoms around him fell. Wales would be united again, by his descendants Hywel Dda and Gruffudd ap Llywelyn, but it was Rhodri who first showed it could be done.",
  "## The father of the royal houses",
  "Gerald of Wales wrote three hundred years later that Rhodri divided Wales among his three sons, Merfyn, Anarawd and Cadell, and that the south was Cadell’s share. Gerald names the three royal seats of Wales: Aberffraw in the north, Dinefwr in the south, and Pengwern in Powys. Aberffraw became the seat of Anarawd’s line and Dinefwr the seat of Cadell’s, and the princes of Gwynedd, Deheubarth and Powys were all proud to be called the line of Rhodri.[[cite:gerald-desc-2,gerald-desc-4]]",
  "From Anarawd came Gruffudd ap Cynan, Owain Gwynedd, Llywelyn Fawr and Llywelyn ap Gruffudd. From Cadell came Hywel Dda and the Lord Rhys. Owain Glyndŵr carried the blood of Rhodri on both sides, and through the line of the Lord Rhys so did the Tudors. Almost every great name in the story of medieval Wales goes back to Rhodri Mawr."],
 ["Rhodri ap Merfyn yw un o ddim ond dau reolwr yng Nghymru a alwyd yn Fawr gan y Cymry. Etifeddodd Wynedd yn 844, cafodd Bowys yn 855, a thrwy ei wraig Angharad daeth â Seisyllwg, tiroedd Ceredigion ac Ystrad Tywi, i’w deulu. Am y tro cyntaf ers y Rhufeiniaid, atebai’r rhan fwyaf o Gymru i un brenin. Trechodd y Llychlynwyr pan oedd gweddill Prydain yn syrthio iddynt, a galwodd blwyddnodion Iwerddon ef yn frenin y Brythoniaid. O’i feibion y daeth tai brenhinol Gwynedd, Deheubarth a Phowys.",
  "|| Ganwyd | tua 820",
  "|| Tad | Merfyn Frych, brenin Gwynedd",
  "|| Mam | Nest, o dŷ brenhinol Powys",
  "|| Gwraig | Angharad, chwaer y Brenin Gwgon o Geredigion",
  "|| Brenin Gwynedd | 844–878",
  "|| Brenin Powys | o 855",
  "|| Buddugoliaeth fawr | dros y Daniaid ar Ynys Môn, 856, pan laddodd eu harweinydd Horm",
  "|| Bu farw | 878, yn ymladd y Saeson",
  "|| Meibion | Anarawd, Cadell, Merfyn, Gwriad ac eraill",
  "## Tair teyrnas",
  "Daeth Rhodri i orsedd Gwynedd pan fu farw ei dad, Merfyn Frych, yn 844. Roedd ei fam Nest o dŷ brenhinol Powys, a phan fu farw ei brawd hi, y Brenin Cyngen o Bowys, ar bererindod yn Rhufain yn 855, daeth Powys i Rodri. Cyngen oedd y brenin a gododd Golofn Eliseg ger Llangollen, a chyda Phowys cymerodd Rhodri at linach o frenhinoedd mor hen â’i linach ei hun.",
  "Priododd Rhodri ag Angharad, chwaer Gwgon, brenin Ceredigion. Pan foddodd Gwgon yn 871, aeth Seisyllwg, teyrnas Ceredigion ac Ystrad Tywi, i deulu Rhodri, ac yn ddiweddarach i’w fab Cadell. O fynyddoedd Eryri hyd ddyffryn Tywi, Rhodri a’i dŷ a reolai’r tir.[[cite:ac-wales,brut-jones]]",
  "## Y brenin a drechodd y Llychlynwyr",
  "Teyrnasiad Rhodri oedd oes byddinoedd mawr y Llychlynwyr. Ysbeiliai’r Daniaid bob glan ym Mhrydain ac Iwerddon, ac yn y 860au a’r 870au drylliodd eu Byddin Fawr deyrnasoedd Seisnig Northumbria, East Anglia a Mersia y naill ar ôl y llall. Roedd Ynys Môn, calon Gwynedd, yn agored i’w llongau.",
  "Yn 856 glaniodd llynges Ddanaidd ar Fôn. Aeth Rhodri i’w cyfarfod a’u trechu, a lladd eu harweinydd, Horm. Roedd y fuddugoliaeth mor fawr nes ei chofnodi yn Iwerddon, ym Mlwyddnodion Ulster, sy’n enwi lladdwr Horm fel Rhodri fab Merfyn, brenin Cymru. Cred llawer o haneswyr mai er clod i fuddugoliaeth Rhodri yr ysgrifennodd y bardd Gwyddelig Sedulius Scottus, yn llys Liège dros y môr, ei gerddi Lladin ar fuddugoliaeth fawr dros y Gwŷr o’r Gogledd.[[cite:au-856,charles-edwards-2013]]",
  "> Lladdwyd Horm, pennaeth y Duon Estron, gan Rodri fab Merfyn, brenin Cymru. | Blwyddnodion Ulster, 856",
  "## Alltudiaeth a dychwelyd",
  "Yn 877 daeth y Daniaid yn ôl yn eu nerth. Mae cronicl Cymru yn cofio ‘gwaith dydd Sul ym Môn’, ac wedi hynny croesodd Rhodri i Iwerddon. Mae Blwyddnodion Ulster yn cofnodi ei ddyfodiad: roedd Rhodri fab Merfyn, brenin y Brythoniaid, wedi dod i Iwerddon ar ffo rhag y Duon Estron. Nid arhosodd. Y flwyddyn wedyn roedd yn ôl yng Ngwynedd, ac yn 878 syrthiodd yn ymladd Saeson Mersia, a’i fab Gwriad wrth ei ochr.[[cite:ac-wales,au-877,au-878]]",
  "## Dial Rhodri",
  "Ni adawodd ei feibion i bethau fod. Yn 881 daeth y Mersiaid eto, ac yn aber afon Conwy drylliodd Anarawd ap Rhodri a’i frodyr hwy. Mae’r Annales Cambriae yn galw’r frwydr yn ‘ddial Rhodri gan Dduw’, ac fe’i cofiwyd byth wedyn fel Dial Rhodri. Ni chipiodd yr un fyddin Seisnig Wynedd am ddau gan mlynedd.[[cite:ac-wales]]",
  "## Rhodri Fawr",
  "Dim ond dau reolwr yng Nghymru a alwyd yn Fawr: Rhodri, a Llywelyn ab Iorwerth, Llywelyn Fawr. Enillodd Rhodri yr enw drwy ddod â’r rhan fwyaf o Gymru dan un tŷ, a thrwy ei dal yn erbyn y Llychlynwyr pan syrthiodd y teyrnasoedd o’i gwmpas. Byddai Cymru’n cael ei huno eto, gan ei ddisgynyddion Hywel Dda a Gruffudd ap Llywelyn, ond Rhodri a ddangosodd gyntaf y gellid ei wneud.",
  "## Tad y tai brenhinol",
  "Ysgrifennodd Gerallt Gymro dri chan mlynedd yn ddiweddarach fod Rhodri wedi rhannu Cymru rhwng ei dri mab, Merfyn, Anarawd a Chadell, ac mai’r de oedd cyfran Cadell. Mae Gerallt yn enwi tair prif sedd frenhinol Cymru: Aberffraw yn y gogledd, Dinefwr yn y de, a Phengwern ym Mhowys. Daeth Aberffraw yn sedd llinach Anarawd a Dinefwr yn sedd llinach Cadell, ac roedd tywysogion Gwynedd, Deheubarth a Phowys i gyd yn falch o gael eu galw’n llinach Rhodri.[[cite:gerald-desc-2,gerald-desc-4]]",
  "O Anarawd y daeth Gruffudd ap Cynan, Owain Gwynedd, Llywelyn Fawr a Llywelyn ap Gruffudd. O Gadell y daeth Hywel Dda a’r Arglwydd Rhys. Roedd gwaed Rhodri yn Owain Glyndŵr o’r ddwy ochr, a thrwy linach yr Arglwydd Rhys yn y Tuduriaid hefyd. Mae bron pob enw mawr yn hanes Cymru’r Oesoedd Canol yn mynd yn ôl at Rodri Mawr."])

LONG["anarawd"] = (
 ["Anarawd ap Rhodri was the eldest son of Rhodri Mawr and king of Gwynedd from 878 to 916. Three years after the English killed his father, he beat them at the mouth of the Conwy, the victory remembered as Dial Rhodri, Rhodri’s vengeance. He held Gwynedd safe for almost forty years, dealt with King Alfred of Wessex as a king, and from him came every later king and prince of Gwynedd. When he died, the chronicle of the Welsh called him king of the Britons.",
  "|| King of Gwynedd | 878–916",
  "|| Father | Rhodri Mawr",
  "|| Great victory | the battle of Conwy, 881, ‘the vengeance for Rhodri’",
  "|| Son | Idwal Foel, king of Gwynedd",
  "|| Died | 916",
  "## The vengeance for Rhodri",
  "In 878 Rhodri Mawr and his son Gwriad fell fighting the Mercians. Anarawd, the eldest of the surviving sons, took up the kingdom of Gwynedd, and his brothers stood with him. In 881 the Mercians came into Gwynedd again, sure that the kingdom of Rhodri was broken. At the mouth of the river Conwy Anarawd and his brothers met them and routed them.[[cite:ac-wales]]",
  "The chronicle of the Welsh named the battle ‘the vengeance for Rhodri, by God’, and the Welsh have called it Dial Rhodri ever since. It was the last time for two centuries that an English army tried to conquer Gwynedd.",
  "## The sons of Rhodri",
  "Asser, the Welsh scholar of St Davids who wrote the life of King Alfred, tells how strong the house of Rhodri had become. The kings of Dyfed, Brycheiniog and Gwent, he writes, turned to Alfred for protection because they were ‘driven by the might’ of the sons of Rhodri. Anarawd and his brothers Cadell and Merfyn now held Gwynedd, Seisyllwg and Powys, most of Wales.[[cite:asser-giles]]",
  "## King to king with Alfred",
  "Anarawd made an alliance first with the Danish kings of York. Then, in the 890s, he came with his brothers to the court of Alfred himself. Asser tells how Alfred received him with honour, stood beside him at his confirmation and took him as his own son in the faith, and sent him home with rich gifts. Anarawd came into Alfred’s friendship on the same terms as Æthelred, the lord of the Mercians: as a king, with his kingdom his own.[[cite:asser-giles]]",
  "## The line of Aberffraw",
  "Anarawd died in 916. The Annales Cambriae mark it with three words, ‘Anaraut rex Brittonum moritur’, Anarawd, king of the Britons, dies. His son Idwal Foel followed him at Aberffraw, the royal seat of Gwynedd, and from Idwal came Iago, Cynan, Gruffudd ap Cynan, Owain Gwynedd and the two Llywelyns. The princes of Gwynedd were proud to be his heirs.[[cite:ac-wales]]"],
 ["Anarawd ap Rhodri oedd mab hynaf Rhodri Mawr a brenin Gwynedd o 878 hyd 916. Dair blynedd wedi i’r Saeson ladd ei dad, trechodd hwy yn aber Conwy, y fuddugoliaeth a gofir fel Dial Rhodri. Cadwodd Wynedd yn ddiogel am bron i ddeugain mlynedd, deliodd â’r Brenin Alffred o Wessex fel brenin, ac ohono ef y daeth pob brenin a thywysog diweddarach yng Ngwynedd. Pan fu farw, galwodd cronicl y Cymry ef yn frenin y Brythoniaid.",
  "|| Brenin Gwynedd | 878–916",
  "|| Tad | Rhodri Mawr",
  "|| Buddugoliaeth fawr | brwydr Conwy, 881, ‘dial Rhodri’",
  "|| Mab | Idwal Foel, brenin Gwynedd",
  "|| Bu farw | 916",
  "## Dial Rhodri",
  "Yn 878 syrthiodd Rhodri Mawr a’i fab Gwriad yn ymladd y Mersiaid. Cymerodd Anarawd, yr hynaf o’r meibion a oedd yn fyw, deyrnas Gwynedd, a safodd ei frodyr gydag ef. Yn 881 daeth y Mersiaid i Wynedd eto, yn sicr fod teyrnas Rhodri wedi’i thorri. Yn aber afon Conwy aeth Anarawd a’i frodyr i’w cyfarfod a’u chwalu.[[cite:ac-wales]]",
  "Galwodd cronicl y Cymry y frwydr yn ‘ddial Rhodri gan Dduw’, ac mae’r Cymry wedi’i galw’n Ddial Rhodri byth ers hynny. Dyna’r tro olaf am ddwy ganrif i fyddin Seisnig geisio gorchfygu Gwynedd.",
  "## Meibion Rhodri",
  "Mae Asser, ysgolhaig Cymreig Tyddewi a ysgrifennodd fuchedd y Brenin Alffred, yn dweud mor gryf oedd tŷ Rhodri wedi mynd. Trodd brenhinoedd Dyfed, Brycheiniog a Gwent at Alffred am nawdd, meddai, am eu bod ‘wedi’u gyrru gan nerth’ meibion Rhodri. Daliai Anarawd a’i frodyr Cadell a Merfyn Wynedd, Seisyllwg a Phowys bellach, y rhan fwyaf o Gymru.[[cite:asser-giles]]",
  "## Brenin wrth frenin gydag Alffred",
  "Gwnaeth Anarawd gynghrair yn gyntaf â brenhinoedd Danaidd Efrog. Yna, yn y 890au, daeth gyda’i frodyr i lys Alffred ei hun. Mae Asser yn adrodd sut y derbyniodd Alffred ef yn anrhydeddus, sefyll wrth ei ochr yn ei fedydd esgob a’i gymryd yn fab iddo yn y ffydd, a’i anfon adref ag anrhegion drud. Daeth Anarawd i gyfeillgarwch Alffred ar yr un telerau ag Æthelred, arglwydd y Mersiaid: fel brenin, a’i deyrnas yn eiddo iddo’i hun.[[cite:asser-giles]]",
  "## Llinach Aberffraw",
  "Bu farw Anarawd yn 916. Mae’r Annales Cambriae yn ei nodi mewn pedwar gair, ‘Anaraut rex Brittonum moritur’, bu farw Anarawd, brenin y Brythoniaid. Dilynodd ei fab Idwal Foel ef yn Aberffraw, sedd frenhinol Gwynedd, ac o Idwal y daeth Iago, Cynan, Gruffudd ap Cynan, Owain Gwynedd a’r ddau Lywelyn. Roedd tywysogion Gwynedd yn falch o fod yn etifeddion iddo.[[cite:ac-wales]]"])

LONG["hywel-dda"] = (
 ["Hywel ap Cadell, the grandson of Rhodri Mawr, is the only king in the history of Wales to be called Da, the Good. He joined Dyfed and Seisyllwg into the kingdom of Deheubarth, and in 942 added Gwynedd and Powys, ruling almost the whole of Wales. He went on pilgrimage to Rome, dealt as an equal with the English king Æthelstan, struck his own silver penny, and gave his name to the law of Wales, Cyfraith Hywel, which the Welsh lived by for six hundred years. When he died in 950, the annals of Wales called him king of the Britons.",
  "|| Born | about 880",
  "|| Father | Cadell ap Rhodri, king of Seisyllwg",
  "|| Grandfather | Rhodri Mawr",
  "|| Wife | Elen, daughter of Llywarch ap Hyfaidd, king of Dyfed",
  "|| King of Deheubarth | from about 920",
  "|| King of Gwynedd and Powys | 942–950",
  "|| Pilgrimage to Rome | 928",
  "|| Died | 950",
  "|| Sons | Owain, Rhodri, Edwin and Einion",
  "## The making of Deheubarth",
  "Hywel was the son of Cadell ap Rhodri, and with his brother Clydog he took up his father’s kingdom of Seisyllwg, Ceredigion and Ystrad Tywi, when Cadell died in 909. He married Elen, the daughter of Llywarch, king of Dyfed, and through her the old kingdom of Dyfed came to him. When Clydog died in 920 Hywel ruled the whole of the south-west, and he made Seisyllwg and Dyfed one kingdom, Deheubarth, the Southern Land, with its chief court at Dinefwr above the Tywi.",
  "## A king among kings",
  "In 928, the Annales Cambriae record, ‘King Hywel went to Rome’. Few kings of his age made that long journey, through France and over the Alps, and Hywel came home with the learning of Christendom fresh in his mind.[[cite:ac-wales,hywel-wiki-coin]]",
  "He dealt with Æthelstan, the first king of all England, as one king with another. His name stands on Æthelstan’s charters among the kings, and he kept his people out of the wars that burned across Britain in his time. He is the only Welsh king known to have had his own coin: a silver penny, struck for him at Chester with the words HOWAEL REX, King Hywel. It is kept today in the British Museum.",
  "## King of almost all Wales",
  "In 942 Idwal Foel, king of Gwynedd, fell fighting the English. Hywel took Gwynedd and Powys too, and from Môn to Dyfed the land of Wales answered to one king, as it had in the days of his grandfather Rhodri. He ruled it in peace for eight years.[[cite:ac-wales,brut-jones]]",
  "## The law of Hywel",
  "Hywel’s great gift to Wales was its law. The lawbooks tell how he called to Whitland, Tŷ Gwyn ar Daf, six men from every cantref of Wales, with the bishops and the learned men of the church, and how they spent Lent together setting the law of the Welsh in order. The clerk Blegywryd wrote it down. The law of Hywel was fair to women, merciful to the hungry, and built on making peace: a killing was answered with galanas, a payment to the family of the dead, not with a feud. It was the law of Wales until the Acts of Union, six hundred years later.[[cite:laws-jenkins]]",
  "## Hywel the Good",
  "Hywel died in 950. The Annales Cambriae wrote ‘Hywel, king of the Britons, died’. His sons Owain, Rhodri and Edwin followed him in Deheubarth, and from Owain came Maredudd ab Owain, the Lord Rhys and the princes of the south. Of all the kings of Wales, he is the one remembered for wisdom and justice rather than for war. His statue stands in the Marble Hall of Cardiff City Hall among the heroes of Wales, and the health board of west Wales carries his name.[[cite:ac-wales]]"],
 ["Hywel ap Cadell, ŵyr Rhodri Mawr, yw’r unig frenin yn hanes Cymru a alwyd yn Dda. Unodd Ddyfed a Seisyllwg yn deyrnas Deheubarth, ac yn 942 ychwanegodd Wynedd a Phowys, gan reoli bron y cyfan o Gymru. Aeth ar bererindod i Rufain, deliodd fel un cydradd ag Æthelstan, brenin Lloegr, bathodd ei geiniog arian ei hun, a rhoddodd ei enw i gyfraith Cymru, Cyfraith Hywel, a fu’n gyfraith i’r Cymry am chwe chan mlynedd. Pan fu farw yn 950, galwodd blwyddnodion Cymru ef yn frenin y Brythoniaid.",
  "|| Ganwyd | tua 880",
  "|| Tad | Cadell ap Rhodri, brenin Seisyllwg",
  "|| Taid | Rhodri Mawr",
  "|| Gwraig | Elen, merch Llywarch ap Hyfaidd, brenin Dyfed",
  "|| Brenin Deheubarth | o tua 920",
  "|| Brenin Gwynedd a Phowys | 942–950",
  "|| Pererindod i Rufain | 928",
  "|| Bu farw | 950",
  "|| Meibion | Owain, Rhodri, Edwin ac Einion",
  "## Creu Deheubarth",
  "Mab Cadell ap Rhodri oedd Hywel, a chyda’i frawd Clydog cymerodd at deyrnas ei dad, Seisyllwg, sef Ceredigion ac Ystrad Tywi, pan fu farw Cadell yn 909. Priododd ag Elen, merch Llywarch, brenin Dyfed, a thrwyddi hi daeth hen deyrnas Dyfed iddo. Pan fu farw Clydog yn 920 rheolai Hywel y de-orllewin i gyd, a gwnaeth Seisyllwg a Dyfed yn un deyrnas, Deheubarth, a’i phrif lys yn Ninefwr uwchben afon Tywi.",
  "## Brenin ymhlith brenhinoedd",
  "Yn 928, medd yr Annales Cambriae, ‘aeth y Brenin Hywel i Rufain’. Ychydig o frenhinoedd ei oes a wnaeth y daith hir honno, drwy Ffrainc a thros yr Alpau, a daeth Hywel adref â dysg y byd Cristnogol yn fyw yn ei feddwl.[[cite:ac-wales,hywel-wiki-coin]]",
  "Deliodd ag Æthelstan, brenin cyntaf Lloegr gyfan, fel un brenin ag un arall. Saif ei enw ar siarteri Æthelstan ymhlith y brenhinoedd, a chadwodd ei bobl allan o’r rhyfeloedd a losgai ar draws Prydain yn ei amser. Ef yw’r unig frenin Cymreig y gwyddys fod ganddo ei ddarn arian ei hun: ceiniog arian, a fathwyd iddo yng Nghaer â’r geiriau HOWAEL REX, y Brenin Hywel. Fe’i cedwir heddiw yn yr Amgueddfa Brydeinig.",
  "## Brenin bron y cyfan o Gymru",
  "Yn 942 syrthiodd Idwal Foel, brenin Gwynedd, yn ymladd y Saeson. Cymerodd Hywel Wynedd a Phowys hefyd, ac o Fôn i Ddyfed atebai tir Cymru i un brenin, fel yn nyddiau ei daid Rhodri. Rheolodd ef mewn heddwch am wyth mlynedd.[[cite:ac-wales,brut-jones]]",
  "## Cyfraith Hywel",
  "Rhodd fawr Hywel i Gymru oedd ei chyfraith. Mae’r llyfrau cyfraith yn adrodd sut y galwodd i Hendy-gwyn, Tŷ Gwyn ar Daf, chwe gŵr o bob cantref yng Nghymru, gyda’r esgobion a gwŷr dysgedig yr eglwys, a sut y treuliasant y Grawys gyda’i gilydd yn rhoi trefn ar gyfraith y Cymry. Y clerc Blegywryd a’i hysgrifennodd. Roedd Cyfraith Hywel yn deg i fenywod, yn drugarog wrth y newynog, ac wedi’i hadeiladu ar wneud heddwch: atebid lladd â galanas, tâl i deulu’r marw, nid â dial. Hi oedd cyfraith Cymru hyd y Deddfau Uno, chwe chan mlynedd yn ddiweddarach.[[cite:laws-jenkins]]",
  "## Hywel Dda",
  "Bu farw Hywel yn 950. Ysgrifennodd yr Annales Cambriae ‘bu farw Hywel, brenin y Brythoniaid’. Dilynodd ei feibion Owain, Rhodri ac Edwin ef yn Neheubarth, ac o Owain y daeth Maredudd ab Owain, yr Arglwydd Rhys a thywysogion y de. O holl frenhinoedd Cymru, ef yw’r un a gofir am ddoethineb a chyfiawnder yn hytrach nag am ryfel. Saif ei gerflun yn Neuadd Farmor Neuadd y Ddinas Caerdydd ymhlith arwyr Cymru, ac mae bwrdd iechyd gorllewin Cymru yn dwyn ei enw.[[cite:ac-wales]]"])

LONG["owain-ap-hywel"] = (
 ["Owain ap Hywel, the son of Hywel Dda, ruled Deheubarth for almost forty years, from 950 until his death in 988. In his time, and very likely at his court, the oldest chronicle of Wales and the oldest collection of the pedigrees of its kings were written down. Much of what we know of Wales before the year 1000 has come to us because Owain’s scholars set it in writing.",
  "|| King of Deheubarth | 950–988",
  "|| Father | Hywel Dda",
  "|| Sons | Einion and Maredudd ab Owain",
  "|| Died | 988",
  "## The son of Hywel Dda",
  "When Hywel Dda died in 950, his sons Owain, Rhodri and Edwin took up the kingdom of Deheubarth together. Rhodri died in 953 and Edwin the year after, and from then on Owain ruled alone, from the chief court at Dinefwr above the Tywi. Gwynedd went back to the sons of Idwal Foel, and the land settled into two great kingdoms, north and south, each ruled by a line of Rhodri Mawr.[[cite:ac-wales]]",
  "## The king who kept the record",
  "In the middle of the tenth century, in Owain’s Deheubarth, someone gathered the annals of the Welsh into one chronicle, year by year from the fifth century, and put with it a long collection of the pedigrees of the kings of Wales and the Old North. The first pedigree in the collection is Owain’s own. It begins ‘Owain son of Hywel son of Cadell son of Rhodri son of Merfyn’, and runs back through the kings of the Britons for generation after generation. The pedigree of his mother’s house of Dyfed is set beside it.[[cite:ac-wales,charles-edwards-2013]]",
  "This was the work of the scholars of St Davids, in Owain’s kingdom, and most historians believe it was made for him. It was copied again about the year 1100 into the manuscript that survives today in the British Library. Arthur’s battles of Badon and Camlan, the deaths of Maelgwn Gwynedd and Cadwaladr, the victories of Rhodri Mawr: all of it reaches us through the chronicle of Owain’s time.",
  "## A long reign",
  "Owain ruled Deheubarth through hard years. Viking fleets were back on the coasts of Wales, and the English pressed on the borders. In his last years, when he was old, his sons fought for him: Einion, who fell in 984, and Maredudd, who in 986 won Gwynedd and joined it to his father’s kingdom. Owain died in 988, and Maredudd ab Owain became the greatest king in Wales.[[cite:brut-jones]]"],
 ["Rheolodd Owain ap Hywel, mab Hywel Dda, Ddeheubarth am bron i ddeugain mlynedd, o 950 hyd ei farw yn 988. Yn ei amser ef, ac yn fwy na thebyg yn ei lys, yr ysgrifennwyd cronicl hynaf Cymru a’r casgliad hynaf o achau ei brenhinoedd. Mae llawer o’r hyn a wyddom am Gymru cyn y flwyddyn 1000 wedi dod atom am fod ysgolheigion Owain wedi’i roi ar glawr.",
  "|| Brenin Deheubarth | 950–988",
  "|| Tad | Hywel Dda",
  "|| Meibion | Einion a Maredudd ab Owain",
  "|| Bu farw | 988",
  "## Mab Hywel Dda",
  "Pan fu farw Hywel Dda yn 950, cymerodd ei feibion Owain, Rhodri ac Edwin deyrnas Deheubarth gyda’i gilydd. Bu farw Rhodri yn 953 ac Edwin y flwyddyn wedyn, ac o hynny ymlaen rheolodd Owain ar ei ben ei hun, o’r prif lys yn Ninefwr uwchben afon Tywi. Aeth Gwynedd yn ôl i feibion Idwal Foel, a setlodd y wlad yn ddwy deyrnas fawr, gogledd a de, pob un dan linach o Rodri Mawr.[[cite:ac-wales]]",
  "## Y brenin a gadwodd y cofnod",
  "Yng nghanol y ddegfed ganrif, yn Neheubarth Owain, casglodd rhywun flwyddnodion y Cymry yn un cronicl, flwyddyn wrth flwyddyn o’r bumed ganrif, a rhoi gydag ef gasgliad hir o achau brenhinoedd Cymru a’r Hen Ogledd. Ach Owain ei hun yw’r gyntaf yn y casgliad. Mae’n dechrau ‘Owain fab Hywel fab Cadell fab Rhodri fab Merfyn’, ac yn rhedeg yn ôl drwy frenhinoedd y Brythoniaid am genhedlaeth ar ôl cenhedlaeth. Rhoddir ach tŷ ei fam, Dyfed, wrth ei hochr.[[cite:ac-wales,charles-edwards-2013]]",
  "Gwaith ysgolheigion Tyddewi, yn nheyrnas Owain, oedd hyn, a chred y rhan fwyaf o haneswyr mai iddo ef y’i gwnaed. Fe’i copïwyd eto tua’r flwyddyn 1100 i’r llawysgrif sydd wedi goroesi heddiw yn y Llyfrgell Brydeinig. Brwydrau Arthur ym Maddon a Chamlan, marw Maelgwn Gwynedd a Chadwaladr, buddugoliaethau Rhodri Mawr: daw’r cyfan atom drwy gronicl amser Owain.",
  "## Teyrnasiad hir",
  "Rheolodd Owain Ddeheubarth drwy flynyddoedd caled. Roedd llynges y Llychlynwyr yn ôl ar lannau Cymru, a’r Saeson yn pwyso ar y ffiniau. Yn ei flynyddoedd olaf, pan oedd yn hen, ymladdodd ei feibion drosto: Einion, a syrthiodd yn 984, a Maredudd, a enillodd Wynedd yn 986 a’i huno â theyrnas ei dad. Bu farw Owain yn 988, a daeth Maredudd ab Owain yn frenin mwyaf Cymru.[[cite:brut-jones]]"])

LONG["maredudd-ab-owain"] = (
 ["Maredudd ab Owain, the grandson of Hywel Dda, was the greatest Welsh king of the late tenth century. He ruled Deheubarth after his father Owain, won Gwynedd and Powys in 986, and held the rule of most of Wales until his death in 999. He stood between his people and the Viking fleets, and paid with his own treasure to free the Welsh they had carried off. The Chronicle of the Princes called him the most renowned king of the Britons.",
  "|| King of Gwynedd | 986–999",
  "|| King of Deheubarth | 988–999",
  "|| Father | Owain ap Hywel Dda",
  "|| Grandfather | Hywel Dda",
  "|| Daughter | Angharad, mother of Gruffudd ap Llywelyn, king of all Wales",
  "|| Died | 999",
  "## The warrior son",
  "Maredudd was the younger son of Owain ap Hywel. While his father grew old at Dinefwr, Maredudd and his elder brother Einion led the warband of Deheubarth. When Einion fell in 984, Maredudd took up the fight alone. In 986 he marched north, overthrew the king of Gwynedd, and took the kingdom of Rhodri Mawr. Two years later his father died, and Maredudd ruled north and south together, as his grandfather Hywel Dda had done.[[cite:brut-jones]]",
  "## Against the Northmen",
  "These were the worst years of the Viking raids on Wales. St Davids, Llanbadarn, Llanilltud and Llancarfan were plundered, and in 987 Godfrey son of Harold, a Viking king of the isles, fell on Ynys Môn and carried away two thousand people as captives. Maredudd gathered the people who were left and brought them south to safety in Ceredigion and Dyfed.[[cite:brut-jones]]",
  "Then, the chronicle records, Maredudd paid the Black Host a tribute of a penny for every person. Historians read it as the price of his people’s freedom: the king paid from his own treasure to ransom the captives and to keep the raiders from the land.[[cite:brut-jones]]",
  "## The most renowned king of the Britons",
  "Maredudd also carried the war to the English border, and for thirteen years no other Welsh king could match him. When he died in 999, the Chronicle of the Princes gave him a farewell it gave to few: Maredudd ab Owain, the most renowned king of the Britons.",
  "> Maredudd ab Owain, the most renowned king of the Britons, died. | Brut y Tywysogion, 999",
  "## His daughter and his grandson",
  "Maredudd’s daughter Angharad married Llywelyn ap Seisyll, who ruled Gwynedd and Deheubarth in a time the chronicle remembers as one of plenty. Their son was Gruffudd ap Llywelyn, who in 1055 became the only king ever to rule all of Wales. Through his daughter, the greatness of Maredudd came down to the greatest of the kings."],
 ["Maredudd ab Owain, ŵyr Hywel Dda, oedd brenin Cymreig mwyaf diwedd y ddegfed ganrif. Rheolodd Ddeheubarth ar ôl ei dad Owain, enillodd Wynedd a Phowys yn 986, a daliodd y rhan fwyaf o Gymru hyd ei farw yn 999. Safodd rhwng ei bobl a llynges y Llychlynwyr, a thalodd o’i drysor ei hun i ryddhau’r Cymry a gludwyd ganddynt. Galwodd Brut y Tywysogion ef yn frenin clodforusaf y Brytaniaid.",
  "|| Brenin Gwynedd | 986–999",
  "|| Brenin Deheubarth | 988–999",
  "|| Tad | Owain ap Hywel Dda",
  "|| Taid | Hywel Dda",
  "|| Merch | Angharad, mam Gruffudd ap Llywelyn, brenin Cymru gyfan",
  "|| Bu farw | 999",
  "## Y mab rhyfelgar",
  "Maredudd oedd mab ieuengaf Owain ap Hywel. Tra heneiddiai ei dad yn Ninefwr, arweiniai Maredudd a’i frawd hŷn Einion osgordd Deheubarth. Pan syrthiodd Einion yn 984, cymerodd Maredudd y frwydr ar ei ben ei hun. Yn 986 gorymdeithiodd i’r gogledd, bwrw brenin Gwynedd i lawr, a chymryd teyrnas Rhodri Mawr. Ddwy flynedd yn ddiweddarach bu farw ei dad, a rheolodd Maredudd y gogledd a’r de gyda’i gilydd, fel y gwnaethai ei daid Hywel Dda.[[cite:brut-jones]]",
  "## Yn erbyn y Gwŷr o’r Gogledd",
  "Dyma flynyddoedd gwaethaf cyrchoedd y Llychlynwyr ar Gymru. Ysbeiliwyd Tyddewi, Llanbadarn, Llanilltud a Llancarfan, ac yn 987 disgynnodd Godfrey fab Harold, brenin Llychlynnaidd yr ynysoedd, ar Ynys Môn a chludo dwy fil o bobl yn gaethion. Casglodd Maredudd y bobl a oedd ar ôl a’u dwyn i’r de i ddiogelwch yng Ngheredigion a Dyfed.[[cite:brut-jones]]",
  "Yna, medd y cronicl, talodd Maredudd deyrnged i’r Llu Du o geiniog am bob person. Mae haneswyr yn ei darllen fel pris rhyddid ei bobl: talodd y brenin o’i drysor ei hun i brynu’r caethion yn rhydd ac i gadw’r ysbeilwyr o’r tir.[[cite:brut-jones]]",
  "## Brenin clodforusaf y Brytaniaid",
  "Aeth Maredudd â’r rhyfel i ffin Lloegr hefyd, ac am dair blynedd ar ddeg ni allai’r un brenin Cymreig arall ddod yn agos ato. Pan fu farw yn 999, rhoddodd Brut y Tywysogion ffarwél iddo na roddodd i lawer: Maredudd ab Owain, brenin clodforusaf y Brytaniaid.",
  "> Bu farw Maredudd ab Owain, brenin clodforusaf y Brytaniaid. | Brut y Tywysogion, 999",
  "## Ei ferch a’i ŵyr",
  "Priododd Angharad, merch Maredudd, â Llywelyn ap Seisyll, a reolodd Wynedd a Deheubarth mewn cyfnod a gofia’r cronicl fel un o lawnder. Eu mab oedd Gruffudd ap Llywelyn, a ddaeth yn 1055 yr unig frenin erioed i reoli Cymru gyfan. Drwy ei ferch, daeth mawredd Maredudd i lawr i’r mwyaf o’r brenhinoedd."])

PEOPLE = [
 P("cadell-ap-rhodri", "kings", "d. 909", "Cadell ap Rhodri", "Cadell ap Rhodri", "King of Seisyllwg, father of Hywel Dda", "Brenin Seisyllwg, tad Hywel Dda", "Cadell_ap_Rhodri", "rulers",
   "Son of Rhodri Mawr and Angharad, who ruled Seisyllwg, the land of Ceredigion and Ystrad Tywi. From him came Hywel Dda, the house of Dinefwr and the Lord Rhys.",
   "Mab Rhodri Mawr ac Angharad, a reolodd Seisyllwg, tir Ceredigion ac Ystrad Tywi. Ohono ef y daeth Hywel Dda, tŷ Dinefwr a’r Arglwydd Rhys.",
   ["Cadell ap Rhodri was a son of Rhodri Mawr and of Angharad, the sister of King Gwgon of Ceredigion. When Gwgon was drowned in 871, his kingdom of Seisyllwg, Ceredigion and Ystrad Tywi, passed through Angharad to her husband’s house, and after Rhodri fell in 878 it was Cadell who ruled it. He was king of Seisyllwg until his death in 909.",
    "|| King of Seisyllwg | 878–909",
    "|| Father | Rhodri Mawr",
    "|| Mother | Angharad, sister of King Gwgon of Ceredigion",
    "|| Sons | Hywel Dda and Clydog",
    "|| Died | 909",
    "## The might of the sons of Rhodri",
    "Cadell and his brothers Anarawd and Merfyn held most of Wales between them. Their neighbours felt it: Asser of St Davids, the Welsh scholar at the court of King Alfred, wrote that Hyfaidd, king of Dyfed, and the kings of Brycheiniog and Gwent turned to Alfred for protection because they were driven by the might of the sons of Rhodri.[[cite:asser-giles]]",
    "## Dinefwr",
    "Gerald of Wales, writing three hundred years later, tells that Rhodri divided Wales among his sons, and that the south was the share of Cadell. Gerald names Dinefwr as the royal seat of the south. Whether Cadell himself held court on the rock above the Tywi or not, the house that came from him was the house of Dinefwr, and its kings and princes were proud to call him their forefather.[[cite:gerald-desc-2,gerald-desc-4]]",
    "## Father of Hywel Dda",
    "The Annales Cambriae record Cadell’s death in 909. His sons Hywel and Clydog took up his kingdom together, and when Clydog died, Hywel joined Seisyllwg to Dyfed and made the kingdom of Deheubarth. Hywel became Hywel Dda, the lawgiver of Wales, and through Hywel the line of Cadell ran on to Maredudd ab Owain, Rhys ap Tewdwr and the Lord Rhys.[[cite:ac-wales]]"],
   ["Mab i Rodri Mawr ac Angharad, chwaer y Brenin Gwgon o Geredigion, oedd Cadell ap Rhodri. Pan foddodd Gwgon yn 871, aeth ei deyrnas, Seisyllwg, sef Ceredigion ac Ystrad Tywi, drwy Angharad i dŷ ei gŵr, ac wedi i Rodri syrthio yn 878 Cadell a’i rheolodd. Bu’n frenin Seisyllwg hyd ei farw yn 909.",
    "|| Brenin Seisyllwg | 878–909",
    "|| Tad | Rhodri Mawr",
    "|| Mam | Angharad, chwaer y Brenin Gwgon o Geredigion",
    "|| Meibion | Hywel Dda a Chlydog",
    "|| Bu farw | 909",
    "## Nerth meibion Rhodri",
    "Rhwng Cadell a’i frodyr Anarawd a Merfyn, daliasant y rhan fwyaf o Gymru. Teimlai eu cymdogion hynny: ysgrifennodd Asser o Dyddewi, yr ysgolhaig Cymreig yn llys y Brenin Alffred, fod Hyfaidd, brenin Dyfed, a brenhinoedd Brycheiniog a Gwent wedi troi at Alffred am nawdd am eu bod wedi’u gyrru gan nerth meibion Rhodri.[[cite:asser-giles]]",
    "## Dinefwr",
    "Mae Gerallt Gymro, wrth ysgrifennu dri chan mlynedd yn ddiweddarach, yn adrodd bod Rhodri wedi rhannu Cymru rhwng ei feibion, ac mai’r de oedd cyfran Cadell. Mae Gerallt yn enwi Dinefwr fel sedd frenhinol y de. Boed Cadell ei hun yn cynnal llys ar y graig uwchben afon Tywi neu beidio, tŷ Dinefwr oedd y tŷ a ddaeth ohono, ac roedd ei frenhinoedd a’i dywysogion yn falch o’i alw’n gyndad iddynt.[[cite:gerald-desc-2,gerald-desc-4]]",
    "## Tad Hywel Dda",
    "Mae’r Annales Cambriae yn cofnodi marw Cadell yn 909. Cymerodd ei feibion Hywel a Chlydog ei deyrnas gyda’i gilydd, a phan fu farw Clydog, unodd Hywel Seisyllwg â Dyfed a chreu teyrnas Deheubarth. Daeth Hywel yn Hywel Dda, deddfwr Cymru, a thrwy Hywel rhedodd llinach Cadell ymlaen at Faredudd ab Owain, Rhys ap Tewdwr a’r Arglwydd Rhys.[[cite:ac-wales]]"]),
 P("idwal-foel", "kings", "d. 942", "Idwal Foel", "Idwal Foel", "King of Gwynedd who fell fighting the English", "Brenin Gwynedd a syrthiodd yn ymladd y Saeson", "Idwal_Foel", "rulers",
   "Son of Anarawd and grandson of Rhodri Mawr, king of Gwynedd from 916. He fell fighting the English in 942, and from him came Gruffudd ap Cynan, Owain Gwynedd and the two Llywelyns.",
   "Mab Anarawd ac ŵyr Rhodri Mawr, brenin Gwynedd o 916. Syrthiodd yn ymladd y Saeson yn 942, ac ohono ef y daeth Gruffudd ap Cynan, Owain Gwynedd a’r ddau Lywelyn.",
   ["Idwal Foel, Idwal the Bald, was the son of Anarawd ap Rhodri and the grandson of Rhodri Mawr. He followed his father as king of Gwynedd in 916, and ruled from Aberffraw for twenty-six years, in the age when the kings of Wessex were making themselves kings of all England.",
    "|| King of Gwynedd | 916–942",
    "|| Father | Anarawd ap Rhodri",
    "|| Grandfather | Rhodri Mawr",
    "|| Sons | Iago, Ieuaf and Meurig",
    "|| Died | 942, fighting the English",
    "## In the age of Æthelstan",
    "In 927 Æthelstan of Wessex took York and made himself the first king of all England. The kings of Wales came to his court, and Idwal’s name stands with Hywel Dda’s on Æthelstan’s charters, among the kings. It was in these years, most scholars believe, that a poet of Wales made Armes Prydein, the Prophecy of Britain, in the Book of Taliesin. It calls on the Cymry to stand together with the men of Ireland, Dublin, Cornwall, Brittany and the Britons of the north, and to drive the English back across the sea: the voice of the Welsh who would not bow.[[cite:armes-williams]]",
    "## The king who fell for Gwynedd",
    "After Æthelstan died in 939, Idwal took up arms. In 942, the Annales Cambriae record, Idwal was killed by the English, and Elisedd with him. Hywel Dda then held Gwynedd for eight years, but when Hywel died in 950 Idwal’s sons Iago and Ieuaf came back and took their father’s kingdom again.[[cite:ac-wales,brut-jones]]",
    "## Forefather of the princes",
    "From Idwal Foel the kingship of Gwynedd ran down through his son Meurig and grandson Idwal to Iago ab Idwal, to Iago’s son Cynan, and to Cynan’s son Gruffudd ap Cynan, who won Gwynedd back at Mynydd Carn in 1081. Owain Gwynedd, Llywelyn Fawr and Llywelyn ap Gruffudd were all of the line of Idwal Foel."],
   ["Mab Anarawd ap Rhodri ac ŵyr Rhodri Mawr oedd Idwal Foel. Dilynodd ei dad yn frenin Gwynedd yn 916, a theyrnasodd o Aberffraw am chwe blynedd ar hugain, yn yr oes pan oedd brenhinoedd Wessex yn gwneud eu hunain yn frenhinoedd Lloegr gyfan.",
    "|| Brenin Gwynedd | 916–942",
    "|| Tad | Anarawd ap Rhodri",
    "|| Taid | Rhodri Mawr",
    "|| Meibion | Iago, Ieuaf a Meurig",
    "|| Bu farw | 942, yn ymladd y Saeson",
    "## Yn oes Æthelstan",
    "Yn 927 cipiodd Æthelstan o Wessex Efrog a gwneud ei hun yn frenin cyntaf Lloegr gyfan. Daeth brenhinoedd Cymru i’w lys, a saif enw Idwal gydag enw Hywel Dda ar siarteri Æthelstan, ymhlith y brenhinoedd. Yn y blynyddoedd hyn, yn ôl y rhan fwyaf o ysgolheigion, y canodd un o feirdd Cymru Armes Prydein yn Llyfr Taliesin. Mae’n galw ar y Cymry i sefyll gyda gwŷr Iwerddon, Dulyn, Cernyw, Llydaw a Brythoniaid y gogledd, ac i yrru’r Saeson yn ôl dros y môr: llais y Cymry na fynnent blygu.[[cite:armes-williams]]",
    "## Y brenin a syrthiodd dros Wynedd",
    "Wedi i Æthelstan farw yn 939, cododd Idwal arfau. Yn 942, medd yr Annales Cambriae, lladdwyd Idwal gan y Saeson, ac Elisedd gydag ef. Daliodd Hywel Dda Wynedd wedyn am wyth mlynedd, ond pan fu farw Hywel yn 950 daeth meibion Idwal, Iago ac Ieuaf, yn ôl a chymryd teyrnas eu tad eto.[[cite:ac-wales,brut-jones]]",
    "## Cyndad y tywysogion",
    "O Idwal Foel rhedodd brenhiniaeth Gwynedd i lawr drwy ei fab Meurig a’i ŵyr Idwal at Iago ab Idwal, at Gynan fab Iago, ac at Ruffudd ap Cynan, mab Cynan, a enillodd Wynedd yn ôl ym Mynydd Carn yn 1081. Roedd Owain Gwynedd, Llywelyn Fawr a Llywelyn ap Gruffudd i gyd o linach Idwal Foel."]),
]

# ---------------------------------------------------------------- sources beside the claims
# [[cite:...]] keys used on these pages (see src/cites.py); cites.py adds them to its list. Each one opened and read.
CITES = {
    "ac-wales": dict(
        short=("Annales Cambriae", "Annales Cambriae"),
        t="Annales Cambriae (The Annals of Wales), the Harleian text, 447–954",
        by=("English translation, Internet Medieval Sourcebook, Fordham University", "Cyfieithiad Saesneg, Internet Medieval Sourcebook, Prifysgol Fordham"),
        note=("The chronicle of the Welsh, year by year: “Merfyn dies”; “Rhodri and his son Gwriad is killed by the Saxons”; “The battle of Conwy. Vengeance for Rhodri at God’s hand”; “King Cadell son of Rhodri dies”; “Anarawd king of the Britons dies”; “Hywel journeyed to Rome”; “Hywel king of the Britons called the Good died”. Its years can run a year behind the dates historians use.",
              "Cronicl y Cymry, flwyddyn wrth flwyddyn: “Bu farw Merfyn”; “Lladdwyd Rhodri a’i fab Gwriad gan y Saeson”; “Gwaith Conwy. Dial Rhodri gan Dduw”; “Bu farw’r Brenin Cadell fab Rhodri”; “Bu farw Anarawd brenin y Brythoniaid”; “Aeth Hywel i Rufain”; “Bu farw Hywel brenin y Brythoniaid, a elwir y Da”. Gall ei flynyddoedd fod flwyddyn y tu ôl i’r dyddiadau a ddefnyddia haneswyr."),
        url="https://sourcebooks.web.fordham.edu/source/annalescambriae.asp", lang="en"),
    "au-856": dict(
        short=("Annals of Ulster, 856", "Blwyddnodion Ulster, 856"),
        t="The Annals of Ulster, year 856", by=("Corpus of Electronic Texts (CELT), University College Cork", "Corpus of Electronic Texts (CELT), Coleg Prifysgol Corc"),
        note=("“Horm, chief of the dark foreigners, was killed by Rhodri son of Mervyn, king of Wales.” (U856.6)",
              "“Lladdwyd Horm, pennaeth y Duon Estron, gan Rodri fab Merfyn, brenin Cymru.” (U856.6)"),
        url="https://celt.ucc.ie/published/T100001A/text426.html", lang="en"),
    "au-877": dict(
        short=("Annals of Ulster, 877", "Blwyddnodion Ulster, 877"),
        t="The Annals of Ulster, year 877", by=("Corpus of Electronic Texts (CELT), University College Cork", "Corpus of Electronic Texts (CELT), Coleg Prifysgol Corc"),
        note=("“Rhodri son of Merfyn, king of the Britons, came in flight from the dark foreigners to Ireland.” (U877.3)",
              "“Daeth Rhodri fab Merfyn, brenin y Brythoniaid, i Iwerddon ar ffo rhag y Duon Estron.” (U877.3)"),
        url="https://celt.ucc.ie/published/T100001A/text447.html", lang="en"),
    "au-878": dict(
        short=("Annals of Ulster, 878", "Blwyddnodion Ulster, 878"),
        t="The Annals of Ulster, year 878", by=("Corpus of Electronic Texts (CELT), University College Cork", "Corpus of Electronic Texts (CELT), Coleg Prifysgol Corc"),
        note=("“Rhodri son of Merfyn, king of the Britons, was killed by the Saxons.” (U878.1) A verse lament follows: “Rhodri of Manu, splendid here”.",
              "“Lladdwyd Rhodri fab Merfyn, brenin y Brythoniaid, gan y Saeson.” (U878.1) Daw marwnad ar gân ar ei ôl: “Rhodri o Fanaw, ysblennydd yma”."),
        url="https://celt.ucc.ie/published/T100001A/text448.html", lang="en"),
    "asser-giles": dict(
        short=("Asser, Life of Alfred", "Asser, Buchedd Alffred"),
        t="Asser’s Life of King Alfred: the Welsh kings", by=("Asser of St Davids, about 893; translated by J. A. Giles, 1848; Internet Medieval Sourcebook, Fordham University", "Asser o Dyddewi, tua 893; cyfieithiad Saesneg J. A. Giles, 1848; Internet Medieval Sourcebook, Prifysgol Fordham"),
        note=("Hyfaidd of Dyfed and the kings of the south turned to Alfred because of “the violence of the six sons of Rotri”. Alfred received Anarawd “as his son by confirmation from the bishop’s hand, and presented him with many gifts”, on the same terms as Æthelred of Mercia.",
              "Trodd Hyfaidd o Ddyfed a brenhinoedd y de at Alffred oherwydd nerth chwe mab Rhodri. Derbyniodd Alffred Anarawd yn fab iddo yn ei fedydd esgob, a rhoi iddo lawer o roddion, ar yr un telerau ag Æthelred o Fersia."),
        url="https://sourcebooks.web.fordham.edu/source/Asser-lifeofalfred-welshprinces.asp", lang="en"),
    "gerald-desc-2": dict(
        short=("Gerald of Wales", "Gerallt Gymro"),
        t="The Description of Wales, book I, chapter 2: Of the ancient division of Wales", by=("Gerald of Wales, 1194; A Vision of Britain through Time", "Gerallt Gymro, 1194; A Vision of Britain through Time"),
        note=("Rhodri the Great divided Wales among his three sons: “North Wales fell to the lot of Mervin”, Powys to Anarawd, and South Wales to Cadell.",
              "Rhannodd Rhodri Mawr Gymru rhwng ei dri mab: y Gogledd i Ferfyn, Powys i Anarawd, a’r De i Gadell."),
        url="https://www.visionofbritain.org.uk/travellers/Cambrensis_Desc/4", lang="en"),
    "gerald-desc-4": dict(
        short=("Gerald of Wales", "Gerallt Gymro"),
        t="The Description of Wales, book I, chapter 4: Cantreds, royal palaces and cathedrals", by=("Gerald of Wales, 1194; A Vision of Britain through Time", "Gerallt Gymro, 1194; A Vision of Britain through Time"),
        note=("The three royal seats of Wales: “Dinevor, in South Wales”, “Aberfraw, in North Wales”, “and Pengwern, in Powys”.",
              "Tair sedd frenhinol Cymru: Dinefwr yn y De, Aberffraw yn y Gogledd, a Phengwern ym Mhowys."),
        url="https://www.visionofbritain.org.uk/travellers/Cambrensis_Desc/6", lang="en"),
    "brut-jones": dict(
        short=("Brut y Tywysogion", "Brut y Tywysogion"),
        t="Brut y Tywysogyon or The Chronicle of the Princes, Peniarth MS. 20 version", by=("translated by Thomas Jones, University of Wales Press, 1952", "cyfieithiad Thomas Jones, Gwasg Prifysgol Cymru, 1952"),
        note=("The chronicle of the princes, kept by the monks of Wales and carried on to 1282. It records the deeds of each king and prince year by year, and how each died.",
              "Cronicl y tywysogion, a gadwyd gan fynachod Cymru hyd 1282. Mae’n cofnodi gweithredoedd pob brenin a thywysog flwyddyn wrth flwyddyn, a sut y bu farw pob un."),
        url=None, lang="en"),
    "merfyn-wiki": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Merfyn Frych", by=("Wikipedia, citing Phillimore, Skene, Kermode, Stokes and Lloyd", "Wikipedia, yn dyfynnu Phillimore, Skene, Kermode, Stokes a Lloyd"),
        note=("“Meruin vrych o dir manaw” in the Red Book of Hergest; the Crux Guriat found on the Isle of Man; the Bamberg Cryptogram naming “Mermin Britannorum regis”, published by Whitley Stokes in 1892.",
              "“Meruin vrych o dir manaw” yn Llyfr Coch Hergest; y Crux Guriat a gafwyd ar Ynys Manaw; Cryptogram Bamberg sy’n enwi “Mermin Britannorum regis”, a gyhoeddwyd gan Whitley Stokes yn 1892."),
        url="https://en.wikipedia.org/wiki/Merfyn_Frych", lang="en"),
    "charles-edwards-2013": dict(
        short=("Charles-Edwards, 2013", "Charles-Edwards, 2013"),
        t="Wales and the Britons, 350–1064", by=("T. M. Charles-Edwards, Oxford University Press, 2013", "T. M. Charles-Edwards, Gwasg Prifysgol Rhydychen, 2013"),
        note=("The history of Wales from the Romans to Gruffudd ap Llywelyn: Merfyn and Rhodri, the Viking wars, the Annales Cambriae and the Harleian pedigrees made in Owain ap Hywel’s time.",
              "Hanes Cymru o’r Rhufeiniaid hyd Ruffudd ap Llywelyn: Merfyn a Rhodri, rhyfeloedd y Llychlynwyr, yr Annales Cambriae ac achau Harley a luniwyd yn amser Owain ap Hywel."),
        url=None, lang="en"),
    "laws-jenkins": dict(
        short=("Dafydd Jenkins, 1986", "Dafydd Jenkins, 1986"),
        t="The Law of Hywel Dda: Law Texts from Mediaeval Wales", by=("Dafydd Jenkins (trans. and ed.), Gomer, 1986", "Dafydd Jenkins (cyf. a gol.), Gomer, 1986"),
        note=("The lawbooks in English, with the prologue that tells how Hywel called men from every cantref to Tŷ Gwyn ar Daf to set the law in order.",
              "Y llyfrau cyfraith yn Saesneg, gyda’r rhagymadrodd sy’n adrodd sut y galwodd Hywel wŷr o bob cantref i’r Tŷ Gwyn ar Daf i roi trefn ar y gyfraith."),
        url=None, lang="en"),
    "armes-williams": dict(
        short=("Armes Prydein, 1955", "Armes Prydein, 1955"),
        t="Armes Prydein o Lyfr Taliesin", by=("Ifor Williams (ed.), University of Wales Press, 1955", "Ifor Williams (gol.), Gwasg Prifysgol Cymru, 1955"),
        note=("The great prophecy poem from the Book of Taliesin, calling the Cymry and their allies to drive out the English. Sir Ifor Williams dated it to about 930, in the time of Æthelstan.",
              "Y gerdd ddarogan fawr o Lyfr Taliesin, sy’n galw ar y Cymry a’u cynghreiriaid i yrru’r Saeson allan. Dyddiodd Syr Ifor Williams hi tua 930, yn amser Æthelstan."),
        url=None),
    "hywel-wiki-coin": dict(
        short=("Wikipedia", "Wikipedia"),
        t="Hywel Dda", by=("Wikipedia", "Wikipedia"),
        note=("Hywel’s pilgrimage to Rome in 928, his place among the kings in Æthelstan’s charters, and his silver penny struck at Chester, the only known coin of a Welsh king.",
              "Pererindod Hywel i Rufain yn 928, ei le ymhlith y brenhinoedd yn siarteri Æthelstan, a’i geiniog arian a fathwyd yng Nghaer, yr unig ddarn arian hysbys gan frenin Cymreig."),
        url="https://en.wikipedia.org/wiki/Hywel_Dda", lang="en"),
}

# Batch 2 (Gruffudd ap Llywelyn, Gruffudd ap Cynan, the Llywelyns and the Dafydds) lives in princes2.py.
import princes2 as _P2X  # noqa: E402
LONG.update(_P2X.LONG)
CITES.update(_P2X.CITES)
# Batch 3 (Siwan, the two Gwenllians, Owain Lawgoch) lives in princes3.py.
import princes3 as _P3X  # noqa: E402
LONG.update(_P3X.LONG)
CITES.update(_P3X.CITES)
# Batch 4 (Powys and Deheubarth: Owain Cyfeiliog, Gwenwynwyn, Madog ap Gruffudd Maelor, Maelgwn ap Rhys, Rhys Gryg) lives in princes4.py.
import princes4 as _P4X  # noqa: E402
LONG.update(_P4X.LONG)
PEOPLE = PEOPLE + _P4X.PEOPLE
CITES.update(_P4X.CITES)

# ---------------------------------------------------------------- the block on every page of the set
# Only people with a page on the site are shown, so ids for pages still to come can be listed already.
GROUPS = [
 ("The age of Rhodri Mawr: the first royal house of Wales", "Oes Rhodri Mawr: tŷ brenhinol cyntaf Cymru",
  ["merfyn-frych", "rhodri-mawr", "anarawd", "cadell-ap-rhodri", "idwal-foel", "hywel-dda", "owain-ap-hywel", "maredudd-ab-owain",
   "llywelyn-ap-seisyll", "gruffudd-ap-llywelyn"]),
 ("The princes of Gwynedd", "Tywysogion Gwynedd",
  ["gruffudd-ap-cynan", "owain-gwynedd", "llywelyn-fawr", "siwan", "gruffudd-ap-llywelyn-fawr", "dafydd-ap-llywelyn", "llywelyn-ap-gruffudd", "eleanor-de-montfort",
   "dafydd-ap-gruffudd", "gwenllian-ferch-llywelyn", "madog-ap-llywelyn", "owain-lawgoch"]),
 ("The princes of Deheubarth", "Tywysogion Deheubarth",
  ["rhys-ap-tewdwr", "nest", "gruffudd-ap-rhys", "gwenllian", "yr-arglwydd-rhys", "maelgwn-ap-rhys", "rhys-gryg"]),
 ("The kings of Morgannwg and Gwent", "Brenhinoedd Morgannwg a Gwent",
  ["morgan-hen", "iestyn-ap-gwrgant"]),
 ("The kings and princes of Powys", "Brenhinoedd a thywysogion Powys",
  ["elisedd", "cyngen", "bleddyn-ap-cynfyn", "madog-ap-maredudd", "owain-cyfeiliog", "gwenwynwyn", "madog-ap-gruffudd-maelor"]),
]

LINKS = [
 ("kings.html", "The kings and princes of every kingdom", "Brenhinoedd a thywysogion pob teyrnas"),
 ("story-hywel.html", "Long read: Hywel Dda and the laws of Wales", "Erthygl: Hywel Dda a chyfraith Cymru"),
 ("laws.html", "The Laws of Hywel Dda", "Cyfreithiau Hywel Dda"),
 ("story-rhys.html", "Long read: the Lord Rhys", "Erthygl: yr Arglwydd Rhys"),
 ("story-nest.html", "Long read: Nest ferch Rhys", "Erthygl: Nest ferch Rhys"),
 ("story-unconquered.html", "Long read: the land that would not be conquered", "Erthygl: y wlad na fynnai ei gorchfygu"),
 ("family-trees.html", "Family trees", "Coed teulu"),
]

ALL_IDS = list(dict.fromkeys(s for _, _, ids in GROUPS for s in ids))
