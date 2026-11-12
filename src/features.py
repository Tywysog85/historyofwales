# Long reads, legends, symbols and quick facts. build.py turns these into pages.
# Text uses curly quotes ‘ ’ so it never clashes with code quotes.
# Each long read / legend: id, era (for colour), art (a scene in art.py), titles, a one-line
# summary, minutes to read, and paragraphs in English and Welsh. A paragraph that starts with
# "## " is a sub-heading.

import hywel as _HY  # Hywel Dda long read (src/hywel.py)

STORIES = [
 dict(id="castles", era="medieval", art="castle", mins=5,
  en="Why does Wales have so many castles?", cy="Pam mae cymaint o gestyll yng Nghymru?",
  sumEn="More than 800 castle sites in a country you can drive across in an afternoon. Each one is a record of somebody trying to take Wales, or to hold it.",
  sumCy="Mwy nag 800 o safleoedd cestyll mewn gwlad y gallwch yrru ar ei thraws mewn prynhawn. Mae pob un yn gofnod o rywun yn ceisio cipio Cymru, neu ei dal.",
  pEn=["Wales is often said to have more castles for its size than any other country in Europe: more than 800 sites (our castles map shows 827), from grassy mounds in farmers’ fields to the great stone fortresses of the north. They were not built for show. Almost every one marks a moment when control of the land was in doubt.",
   "## The Normans arrive",
   "Within a year of the Battle of Hastings, William fitzOsbern began a stone keep on the cliff at Chepstow, the first of its kind in Wales. Behind him came the Marcher lords, who were given a free hand to conquer what they could. Their tool was the motte and bailey: a mound of earth with a timber tower, which a few hundred labourers could raise in weeks. Hundreds were thrown up across the south and the borders, and many were later rebuilt in stone.",
   "## The princes build back",
   "The Welsh learned quickly. By the thirteenth century the princes of Gwynedd were building stone castles of their own, sited to guard mountain passes and cattle pastures: Dolwyddelan, Dolbadarn, Castell y Bere and Cricieth. In the south the Lord Rhys rebuilt Cardigan in stone, and Dinefwr stood as the seat of Deheubarth. Welsh castles tend to be smaller and more irregular than Norman ones, with a distinctive D-shaped tower.",
   "## Edward’s ring of stone",
   "After the death of Llywelyn ap Gruffudd in 1282, Edward I set out to make conquest permanent. His architect, Master James of St George from Savoy, raised Conwy, Caernarfon, Harlech and finally Beaumaris, each with a walled town planted beside it for English settlers. The programme was among the most expensive building projects of medieval Europe and came close to emptying the royal treasury. Beaumaris was never finished.",
   "The largest castle in Wales, though, was built by a Marcher lord. Gilbert de Clare began Caerphilly in 1268 to block Llywelyn’s advance, surrounding it with artificial lakes. In all of Britain only Windsor covers more ground.",
   "## From fortress to ruin",
   "Owain Glyndŵr captured Harlech and Aberystwyth in 1404 and held court in them. The last sieges came in the Civil War; Raglan fell in 1646 and Parliament ordered many castles to be ‘slighted’ so they could never be defended again. What remained became quarries, then romantic ruins for painters such as Turner, and finally monuments. In 1986 the castles and town walls of Edward I in Gwynedd were made a UNESCO World Heritage Site: buildings raised to subdue Wales have become one of its best-known symbols."],
  pCy=["Dywedir yn aml fod gan Gymru fwy o gestyll o ystyried ei maint nag unrhyw wlad arall yn Ewrop: mwy nag 800 o safleoedd (mae 827 ar ein map cestyll), o domenni glaswelltog mewn caeau fferm i gaerau cerrig mawr y gogledd. Nid er mwyn sioe y codwyd hwy. Mae bron pob un yn nodi cyfnod pan oedd rheolaeth ar y tir yn y fantol.",
   "## Dyfodiad y Normaniaid",
   "O fewn blwyddyn i Frwydr Hastings, dechreuodd William fitzOsbern godi tŵr cerrig ar y clogwyn yng Nghas-gwent, y cyntaf o’i fath yng Nghymru. Ar ei ôl daeth arglwyddi’r Mers, a gafodd ryddid i goncro’r hyn a allent. Eu harf oedd y castell mwnt a beili: tomen o bridd a thŵr pren arni, y gallai ychydig gannoedd o lafurwyr ei chodi mewn wythnosau. Codwyd cannoedd ar draws y de a’r gororau, ac ailgodwyd llawer ohonynt mewn carreg yn ddiweddarach.",
   "## Y tywysogion yn adeiladu",
   "Dysgodd y Cymry’n gyflym. Erbyn y drydedd ganrif ar ddeg roedd tywysogion Gwynedd yn codi eu cestyll cerrig eu hunain, wedi’u gosod i warchod bylchau’r mynyddoedd a phorfeydd y gwartheg: Dolwyddelan, Dolbadarn, Castell y Bere a Chricieth. Yn y de ailgododd yr Arglwydd Rhys gastell Aberteifi mewn carreg, a safai Dinefwr yn brif lys Deheubarth. Mae cestyll y Cymry’n tueddu i fod yn llai ac yn fwy afreolaidd na rhai’r Normaniaid, gyda thŵr nodweddiadol ar ffurf D.",
   "## Cylch cerrig Edward",
   "Ar ôl marwolaeth Llywelyn ap Gruffudd yn 1282, aeth Edward I ati i wneud y goncwest yn barhaol. Cododd ei bensaer, Meistr James o St George o Safwy, gestyll Conwy, Caernarfon, Harlech ac yn olaf Biwmares, pob un â thref gaerog wrth ei ochr ar gyfer ymsefydlwyr o Loegr. Roedd y rhaglen ymhlith prosiectau adeiladu drutaf Ewrop yr Oesoedd Canol, a bu bron iddi wagio trysorlys y brenin. Ni orffennwyd Biwmares erioed.",
   "Ond un o arglwyddi’r Mers a gododd gastell mwyaf Cymru. Dechreuodd Gilbert de Clare godi Caerffili yn 1268 i atal Llywelyn rhag symud ymlaen, gan ei amgylchynu â llynnoedd artiffisial. Ym Mhrydain gyfan, dim ond Windsor sy’n fwy ei arwynebedd.",
   "## O gaer i adfail",
   "Cipiodd Owain Glyndŵr Harlech ac Aberystwyth yn 1404 a chynnal ei lys ynddynt. Daeth y gwarchaeau olaf yn y Rhyfel Cartref; syrthiodd Rhaglan yn 1646 a gorchmynnodd y Senedd ddifrodi llawer o gestyll fel na ellid eu hamddiffyn byth eto. Aeth yr hyn oedd ar ôl yn chwareli, yna’n adfeilion rhamantaidd i arlunwyr fel Turner, ac yn y pen draw yn henebion. Yn 1986 gwnaed cestyll a muriau trefi Edward I yng Ngwynedd yn Safle Treftadaeth y Byd UNESCO: mae adeiladau a godwyd i ddarostwng Cymru bellach ymhlith ei symbolau mwyaf adnabyddus."]),

 dict(id="language", era="saints", art="book", mins=6,
  links=[("story-tryweryn.html", "Cofiwch Dryweryn: the drowning of Capel Celyn", "Cofiwch Dryweryn: boddi Capel Celyn")],
  en="How the Welsh language survived", cy="Sut y goroesodd y Gymraeg",
  sumEn="Banned from the courts, beaten out of schoolchildren and written off by government inspectors, Welsh is still spoken by more than half a million people. How?",
  sumCy="Fe’i gwaharddwyd o’r llysoedd, ei churo o blant ysgol a’i diystyru gan arolygwyr y llywodraeth, ond mae mwy na hanner miliwn yn dal i siarad Cymraeg. Sut?",
  pEn=["Welsh is one of the oldest living languages in Europe. It grew out of Brittonic, the speech of the Britons, spoken across most of Britain before the Romans came, and by the sixth century it was recognisably its own language. The poems linked to Aneirin and Taliesin come from that time, which gives Welsh one of the longest unbroken literary traditions on the continent.",
   "## A language without a state",
   "For centuries Welsh was the language of law, poetry and princely courts. That changed with the Laws in Wales Acts of 1536 and 1543, which declared that only English could be used in the courts and that no one using Welsh could hold public office. The gentry, with careers to make, turned to English. The language of nine tenths of the people had lost its place in government.",
   "## Saved by a book",
   "What rescued it was religion. Elizabeth I’s government wanted Wales to be Protestant, and the quickest way was to give people scripture they could understand. William Morgan’s Bible of 1588 gave Welsh a standard, dignified written form at exactly the moment it might have broken into dialects. In the eighteenth century Griffith Jones’s circulating schools taught perhaps half the population to read it. Wales became one of the most literate countries in Europe, and it did so in Welsh.",
   "## The Blue Books and the Welsh Not",
   "In 1847 a government report on education in Wales, written by three English commissioners who spoke no Welsh, described the language as a barrier to moral and commercial progress. The ‘Treachery of the Blue Books’ caused lasting anger. In some schools a child caught speaking Welsh was made to wear a piece of wood, the Welsh Not, and the last child wearing it at the end of the day was punished. At the same time industry was drawing hundreds of thousands of English speakers into the coalfield. In 1891 just over half the people of Wales spoke Welsh; by 1961 it was a quarter.",
   "## The fight back",
   "In February 1962 the writer Saunders Lewis gave a radio lecture, Tynged yr Iaith (The Fate of the Language), warning that Welsh would be dead by the twenty-first century unless people were prepared to break the law for it. Cymdeithas yr Iaith was founded that summer. Its members painted out English-only road signs, refused to pay bills and went to prison. Parents demanded Welsh-medium schools. In 1980 Gwynfor Evans threatened to fast to death unless the government kept its promise of a Welsh television channel; S4C began broadcasting in 1982.",
   "Welsh has had official status in Wales since 2011, and around a quarter of children are now taught through it. The 2021 census counted 538,300 speakers, 17.8 per cent of the population, and the Welsh Government’s target is a million by 2050. The language is not safe. But it has outlived every prediction of its death so far."],
  pCy=["Mae’r Gymraeg yn un o ieithoedd byw hynaf Ewrop. Tyfodd o’r Frythoneg, iaith y Brythoniaid, a siaredid ar draws y rhan fwyaf o Brydain cyn dyfod y Rhufeiniaid, ac erbyn y chweched ganrif roedd yn iaith ar wahân. O’r cyfnod hwnnw y daw’r cerddi a gysylltir ag Aneirin a Thaliesin, sy’n rhoi i’r Gymraeg un o’r traddodiadau llenyddol di-dor hwyaf ar y cyfandir.",
   "## Iaith heb wladwriaeth",
   "Am ganrifoedd y Gymraeg oedd iaith y gyfraith, barddoniaeth a llysoedd y tywysogion. Newidiodd hynny gyda’r Deddfau Uno yn 1536 a 1543, a ddatganodd mai Saesneg yn unig a ddefnyddid yn y llysoedd ac na châi neb a ddefnyddiai’r Gymraeg ddal swydd gyhoeddus. Trodd y boneddigion, â’u bryd ar yrfa, at y Saesneg. Roedd iaith naw o bob deg o’r bobl wedi colli ei lle mewn llywodraeth.",
   "## Achubwyd gan lyfr",
   "Crefydd a’i hachubodd. Roedd llywodraeth Elisabeth I am i Gymru fod yn Brotestannaidd, a’r ffordd gyflymaf oedd rhoi’r ysgrythur i’r bobl mewn iaith a ddeallent. Rhoddodd Beibl William Morgan yn 1588 ffurf ysgrifenedig safonol ac urddasol i’r Gymraeg ar yr union adeg y gallasai chwalu’n dafodieithoedd. Yn y ddeunawfed ganrif dysgodd ysgolion cylchynol Griffith Jones efallai hanner y boblogaeth i’w ddarllen. Daeth Cymru’n un o wledydd mwyaf llythrennog Ewrop, a hynny yn Gymraeg.",
   "## Y Llyfrau Gleision a’r Welsh Not",
   "Yn 1847 disgrifiodd adroddiad y llywodraeth ar addysg yng Nghymru, a luniwyd gan dri chomisiynydd o Saeson di-Gymraeg, yr iaith fel rhwystr i gynnydd moesol a masnachol. Achosodd ‘Brad y Llyfrau Gleision’ ddicter parhaol. Mewn rhai ysgolion gorfodid plentyn a ddaliwyd yn siarad Cymraeg i wisgo darn o bren, y Welsh Not, a chosbid y plentyn olaf i’w wisgo ar ddiwedd y dydd. Ar yr un pryd roedd diwydiant yn denu cannoedd o filoedd o siaradwyr Saesneg i’r maes glo. Yn 1891 roedd ychydig dros hanner pobl Cymru’n siarad Cymraeg; erbyn 1961, chwarter.",
   "## Taro’n ôl",
   "Ym mis Chwefror 1962 traddododd y llenor Saunders Lewis ddarlith radio, Tynged yr Iaith, gan rybuddio y byddai’r Gymraeg wedi marw erbyn yr unfed ganrif ar hugain oni bai fod pobl yn barod i dorri’r gyfraith drosti. Sefydlwyd Cymdeithas yr Iaith yr haf hwnnw. Peintiodd ei haelodau dros arwyddion ffyrdd uniaith Saesneg, gwrthod talu biliau a mynd i’r carchar. Mynnodd rhieni ysgolion Cymraeg. Yn 1980 bygythiodd Gwynfor Evans ymprydio hyd farwolaeth oni bai fod y llywodraeth yn cadw ei haddewid i sefydlu sianel deledu Gymraeg; dechreuodd S4C ddarlledu yn 1982.",
   "Mae gan y Gymraeg statws swyddogol yng Nghymru er 2011, ac mae tua chwarter y plant bellach yn cael eu haddysg drwyddi. Cyfrifodd cyfrifiad 2021 538,300 o siaradwyr, 17.8 y cant o’r boblogaeth, a tharged Llywodraeth Cymru yw miliwn erbyn 2050. Nid yw’r iaith yn ddiogel. Ond mae wedi goroesi pob darogan am ei thranc hyd yma."]),

 _HY.STORY,

 dict(id="coal", era="industrial", art="pit", mins=6,
  links=[("story-aberfan.html", "Aberfan, 21 October 1966: the village that never forgot its children", "Aberfan, 21 Hydref 1966: y pentref nad anghofiodd ei blant")],
  en="Coal: the fuel of an empire, and its price", cy="Glo: tanwydd ymerodraeth, a’i bris",
  sumEn="In 1913 the valleys of south Wales powered navies and railways across the world. A century later the last deep mine had closed. This is what coal built, and what it cost.",
  sumCy="Yn 1913 roedd cymoedd y de’n gyrru llyngesau a rheilffyrdd ledled y byd. Ganrif yn ddiweddarach roedd y pwll dwfn olaf wedi cau. Dyma’r hyn a adeiladodd glo, a’r hyn a gostiodd.",
  pEn=["In 1851 fewer than a thousand people lived in the two Rhondda valleys, a place travellers praised for its woods and clear rivers. By 1911 there were more than 150,000. Nothing in Welsh history happened faster than coal.",
   "## Black gold",
   "South Wales steam coal burned hot and with little smoke, which made it the preferred fuel of the Royal Navy and of steamships everywhere. Railways carried it down the valleys to docks at Cardiff, Barry, Newport and Swansea. In 1913, the peak year, the coalfield raised about 57 million tons and employed some 232,000 men, and Barry shipped more coal than any other port in the world. The price of coal was set on the floor of the Coal Exchange in Cardiff, where the first cheque for a million pounds is said to have been signed.",
   "People poured in from rural Wales, from the west of England, Ireland, Italy and Spain. For a generation south Wales drew in migrants at a rate matched only by the United States.",
   "## The cost",
   "The work was among the most dangerous in Britain. On 14 October 1913 an explosion at the Universal Colliery in Senghenydd killed 439 men and boys, the worst mining disaster in British history. The owners were fined £24. At Gresford near Wrexham, 266 died in 1934. Thousands more were killed one or two at a time by roof falls, and many who survived had their lungs destroyed by dust.",
   "## What the miners built",
   "Out of that danger came an extraordinary culture of self-help. Miners paid a few pence a week to build institutes with libraries, theatres and billiard halls. They founded choirs, brass bands and rugby clubs. Their union, ‘the Fed’, formed in 1898, became a force in British politics. In Tredegar the Workmen’s Medical Aid Society gave free health care to almost the whole town in return for a weekly contribution. A young miner who sat on its committee, Aneurin Bevan, later said that in founding the National Health Service he was ‘Tredegar-ising’ Britain.",
   "## Decline",
   "The world turned to oil after the First World War, and the coalfield collapsed. In parts of the valleys more than half the men were out of work in the early 1930s, and over 400,000 people left Wales between the wars. The mines were nationalised in 1947, but closures continued. In 1966 a colliery waste tip slid onto the village school at Aberfan and killed 116 children and 28 adults. The year-long strike of 1984–85 failed to stop the closures. Tower Colliery, bought by its own miners in 1995, was the last deep mine in Wales when it shut in 2008.",
   "The pitheads have mostly gone and the valleys are green again. Big Pit at Blaenavon, now the National Coal Museum, still takes visitors 90 metres underground, guided by men who once worked the seams."],
  pCy=["Yn 1851 roedd llai na mil o bobl yn byw yn nau gwm y Rhondda, ardal a ganmolid gan deithwyr am ei choedydd a’i hafonydd clir. Erbyn 1911 roedd yno fwy na 150,000. Ni ddigwyddodd dim yn hanes Cymru’n gyflymach na glo.",
   "## Yr aur du",
   "Roedd glo ager y de’n llosgi’n boeth heb fawr o fwg, ac felly dyma hoff danwydd y Llynges Frenhinol ac agerlongau ym mhobman. Cludai’r rheilffyrdd ef i lawr y cymoedd i ddociau Caerdydd, y Barri, Casnewydd ac Abertawe. Yn 1913, y flwyddyn anterth, cododd y maes glo tua 57 miliwn tunnell gan gyflogi rhyw 232,000 o ddynion, ac allforiodd y Barri fwy o lo nag unrhyw borthladd arall yn y byd. Pennid pris glo ar lawr y Gyfnewidfa Lo yng Nghaerdydd, lle dywedir i’r siec gyntaf am filiwn o bunnoedd gael ei llofnodi.",
   "Llifodd pobl i mewn o gefn gwlad Cymru, o orllewin Lloegr, Iwerddon, yr Eidal a Sbaen. Am genhedlaeth, denai’r de fewnfudwyr ar raddfa nad oedd ond yr Unol Daleithiau’n cystadlu â hi.",
   "## Y gost",
   "Roedd y gwaith ymhlith y mwyaf peryglus ym Mhrydain. Ar 14 Hydref 1913 lladdodd ffrwydrad yng Nglofa’r Universal yn Senghennydd 439 o ddynion a bechgyn, y drychineb lofaol waethaf yn hanes Prydain. Cafodd y perchnogion ddirwy o £24. Yng Ngresffordd ger Wrecsam, bu farw 266 yn 1934. Lladdwyd miloedd eraill fesul un neu ddau gan gwympiadau, a dinistriwyd ysgyfaint llawer o’r rhai a oroesodd gan y llwch.",
   "## Yr hyn a adeiladodd y glowyr",
   "O’r perygl hwnnw daeth diwylliant hunangymorth rhyfeddol. Talai’r glowyr ychydig geiniogau’r wythnos i godi neuaddau gweithwyr â llyfrgelloedd, theatrau a byrddau biliards. Sefydlasant gorau, bandiau pres a chlybiau rygbi. Daeth eu hundeb, ‘y Ffed’, a ffurfiwyd yn 1898, yn rym yng ngwleidyddiaeth Prydain. Yn Nhredegar rhoddai Cymdeithas Cymorth Meddygol y Gweithwyr ofal iechyd am ddim i bron y dref gyfan yn gyfnewid am gyfraniad wythnosol. Dywedodd glöwr ifanc a fu ar ei phwyllgor, Aneurin Bevan, yn ddiweddarach mai ‘Tredegareiddio’ Prydain yr oedd wrth sefydlu’r Gwasanaeth Iechyd Gwladol.",
   "## Dirywiad",
   "Trodd y byd at olew ar ôl y Rhyfel Byd Cyntaf, a chwalodd y maes glo. Mewn rhannau o’r cymoedd roedd mwy na hanner y dynion yn ddi-waith ar ddechrau’r 1930au, a gadawodd dros 400,000 o bobl Gymru rhwng y ddau ryfel. Gwladolwyd y pyllau yn 1947, ond parhau wnaeth y cau. Yn 1966 llithrodd tomen wastraff glofa ar ben ysgol y pentref yn Aberfan gan ladd 116 o blant a 28 o oedolion. Methodd streic blwyddyn 1984–85 ag atal y cau. Glofa’r Tŵr, a brynwyd gan ei glowyr ei hun yn 1995, oedd y pwll dwfn olaf yng Nghymru pan gaeodd yn 2008.",
   "Mae’r rhan fwyaf o’r pennau pyllau wedi mynd ac mae’r cymoedd yn wyrdd eto. Mae Pwll Mawr ym Mlaenafon, sydd bellach yn Amgueddfa Lofaol Cymru, yn dal i fynd ag ymwelwyr 90 metr dan ddaear, dan arweiniad dynion a fu unwaith yn gweithio’r gwythiennau."]),

 dict(id="protest", era="medieval", art="torch", mins=5,
  en="A nation of protest", cy="Cenedl o brotestwyr",
  sumEn="A red flag in Merthyr, farmers in petticoats smashing tollgates, an army of Chartists marching on Newport. Nineteenth-century Wales did not go quietly.",
  sumCy="Baner goch ym Merthyr, ffermwyr mewn peisiau’n malu tollbyrth, byddin o Siartwyr yn gorymdeithio ar Gasnewydd. Nid aeth Cymru’r bedwaredd ganrif ar bymtheg yn dawel.",
  pEn=["Between 1831 and 1843 Wales saw three of the most dramatic popular risings in modern British history. They had different causes and different leaders, but each was a response to a society changing faster than its laws.",
   "## Merthyr, 1831",
   "Merthyr Tydfil was then the largest town in Wales and the iron capital of the world. In June 1831, after wage cuts and with debtors’ goods being seized, thousands of workers took over the town. They ransacked the debtors’ court and marched under a flag soaked in calf’s blood, often described as the first time the red flag was raised as a symbol of workers’ revolt. Soldiers fired into the crowd outside the Castle Inn, killing at least sixteen. A young miner, Richard Lewis, known as Dic Penderyn, was hanged in Cardiff for stabbing a soldier. Few believed he was guilty, and his last words were ‘O Arglwydd, dyma gamwedd’: O Lord, here is injustice.",
   "## Newport, 1839",
   "The Chartists wanted the vote for every man, secret ballots and pay for MPs. On the night of 3 November 1839 several thousand men from the Monmouthshire valleys marched through the rain to Newport, led by John Frost, a former mayor of the town. Soldiers were waiting inside the Westgate Hotel. Around twenty marchers were shot dead in a few minutes. Frost and two others were sentenced to be hanged, drawn and quartered, the last time that sentence was passed in Britain; after a public outcry they were transported to Tasmania instead. Most of what the Chartists asked for is now simply how elections work.",
   "## Rebecca, 1839–43",
   "In rural west Wales the grievance was the tollgate. Small farmers, already squeezed by rents and tithes, had to pay at gate after gate to cart lime to their fields. Beginning at Efailwen in 1839, bands of men with blackened faces and women’s clothes pulled the gates down at night, led each time by a figure called ‘Rebecca’, a name taken from a verse in Genesis. Hundreds of gates were destroyed. The government sent troops and a reporter from The Times, and then did something unusual: it held an inquiry, agreed the farmers had a case, and reformed the turnpike trusts in 1844.",
   "## A habit that lasted",
   "The tradition carried on. Farmers refused to pay tithes to a church they did not attend in the 1880s. The quarrymen of Penrhyn held out for three years from 1900 in one of the longest disputes in British industrial history. In the twentieth century protest took new forms, from the hunger marches of the 1930s to the language campaigns of the 1960s and the miners’ strike of 1984. Arguing with power is one of the oldest threads in the Welsh story."],
  pCy=["Rhwng 1831 a 1843 gwelodd Cymru dri o’r gwrthryfeloedd gwerinol mwyaf dramatig yn hanes modern Prydain. Roedd iddynt achosion ac arweinwyr gwahanol, ond roedd pob un yn ymateb i gymdeithas a oedd yn newid yn gyflymach na’i chyfreithiau.",
   "## Merthyr, 1831",
   "Merthyr Tudful oedd tref fwyaf Cymru ar y pryd a phrifddinas haearn y byd. Ym mis Mehefin 1831, wedi toriadau cyflog a chydag eiddo dyledwyr yn cael ei atafaelu, meddiannodd miloedd o weithwyr y dref. Ysbeiliasant lys y dyledwyr a gorymdeithio dan faner wedi’i throchi mewn gwaed llo, a ddisgrifir yn aml fel y tro cyntaf i’r faner goch gael ei chodi’n symbol o wrthryfel y gweithwyr. Saethodd milwyr i’r dorf y tu allan i Dafarn y Castell, gan ladd o leiaf un ar bymtheg. Crogwyd glöwr ifanc, Richard Lewis, a adwaenid fel Dic Penderyn, yng Nghaerdydd am drywanu milwr. Ychydig a gredai ei fod yn euog, a’i eiriau olaf oedd ‘O Arglwydd, dyma gamwedd’.",
   "## Casnewydd, 1839",
   "Roedd y Siartwyr am gael pleidlais i bob dyn, pleidlais gudd a chyflog i Aelodau Seneddol. Ar noson 3 Tachwedd 1839 gorymdeithiodd rhai miloedd o ddynion o gymoedd Sir Fynwy drwy’r glaw i Gasnewydd, dan arweiniad John Frost, cyn-faer y dref. Roedd milwyr yn disgwyl y tu mewn i Westy’r Westgate. Saethwyd tua ugain o’r gorymdeithwyr yn farw mewn ychydig funudau. Dedfrydwyd Frost a dau arall i’w crogi, eu diberfeddu a’u chwarteru, y tro olaf i’r ddedfryd honno gael ei rhoi ym Mhrydain; wedi protest gyhoeddus fe’u halltudiwyd i Tasmania yn lle hynny. Mae’r rhan fwyaf o’r hyn a fynnai’r Siartwyr bellach yn rhan arferol o bob etholiad.",
   "## Beca, 1839–43",
   "Yng nghefn gwlad y gorllewin, y dollborth oedd y gŵyn. Roedd rhaid i ffermwyr bach, a wasgid eisoes gan renti a degymau, dalu wrth glwyd ar ôl clwyd i gario calch i’w caeau. Gan ddechrau yn Efail-wen yn 1839, tynnai criwiau o ddynion â’u hwynebau wedi’u duo ac mewn dillad menywod y clwydi i lawr liw nos, dan arweiniad ffigwr a elwid ‘Rebeca’ bob tro, enw a gymerwyd o adnod yn Genesis. Dinistriwyd cannoedd o glwydi. Anfonodd y llywodraeth filwyr a gohebydd o’r Times, ac yna gwnaeth rywbeth anarferol: cynhaliodd ymchwiliad, cytunodd fod gan y ffermwyr achos, a diwygiodd yr ymddiriedolaethau tyrpeg yn 1844.",
   "## Arfer a barhaodd",
   "Parhaodd y traddodiad. Gwrthododd ffermwyr dalu’r degwm i eglwys nad oeddent yn ei mynychu yn y 1880au. Daliodd chwarelwyr y Penrhyn eu tir am dair blynedd o 1900 yn un o’r anghydfodau hwyaf yn hanes diwydiannol Prydain. Yn yr ugeinfed ganrif cymerodd protest ffurfiau newydd, o orymdeithiau newyn y 1930au i ymgyrchoedd iaith y 1960au a streic y glowyr yn 1984. Dadlau â grym yw un o’r edafedd hynaf yn stori Cymru."]),

 dict(id="world", era="modern", art="ship", mins=5,
  en="Wales and the wider world", cy="Cymru a’r byd mawr",
  sumEn="Welsh is spoken in Argentina, a city in Ukraine was founded by a man from Merthyr, and Cardiff’s docks drew people from fifty nations. The history of Wales does not stop at its borders.",
  sumCy="Siaredir Cymraeg yn yr Ariannin, sefydlwyd dinas yn Wcráin gan ŵr o Ferthyr, a denodd dociau Caerdydd bobl o hanner cant o wledydd. Nid yw hanes Cymru’n gorffen wrth ei ffiniau.",
  pEn=["Wales is a small country, but its people have rarely stayed put, and the world has rarely left it alone. The story runs in both directions.",
   "## A new Wales in Patagonia",
   "On 28 July 1865 about 150 Welsh settlers stepped off the tea clipper Mimosa onto a bare beach in Patagonia, in southern Argentina. Their leader, Michael D. Jones, wanted a place where Welsh people could keep their language and their chapels without becoming English or American. The early years were desperate, and the colony survived partly through the help of the Tehuelche people. But Y Wladfa endured. It ran its own courts and schools in Welsh, and gave women the vote in local elections decades before Britain did. Welsh is still spoken in the Chubut valley today, with an Argentine accent.",
   "## Across the Atlantic",
   "Far more went to the United States. Welsh Quakers bought a tract of land outside Philadelphia in the 1680s, which is why its suburbs have names like Bryn Mawr and Bala Cynwyd. In the nineteenth century, skilled iron and coal workers were recruited directly from the valleys to Pennsylvania and Ohio. By 1890 there were around 100,000 Welsh-born people in America, and Scranton was said to hold more Welsh speakers than many towns in Wales.",
   "## Iron on the steppe",
   "In 1870 John Hughes, an engineer from Merthyr Tydfil, sailed to the Russian Empire with about a hundred Welsh ironworkers and miners. The works he built grew into a city named after him, Hughesovka or Yuzovka. Today it is Donetsk, in Ukraine. Welsh missionaries also travelled widely: in the Khasi Hills of north-east India, Thomas Jones wrote down the Khasi language for the first time in the 1840s, using Welsh spelling habits that it keeps to this day.",
   "## The world comes to Wales",
   "The traffic came the other way too. Irish families fleeing the famine settled in Cardiff, Newport and Swansea in the 1840s. Italians from the Bardi valley opened cafés in almost every mining town. And around Cardiff’s docks grew Butetown, known as Tiger Bay, where sailors from Somalia, Yemen, the Caribbean, West Africa, Norway and China settled and married local women. By the 1940s people from some fifty nations lived there, one of the oldest multicultural communities in Britain. Betty Campbell, who grew up in Butetown and became the first Black head teacher in Wales, taught its history to her pupils long before it reached any textbook.",
   "A Welsh history that leaves these journeys out is missing half of itself."],
  pCy=["Gwlad fach yw Cymru, ond anaml yr arhosodd ei phobl yn eu hunfan, ac anaml y gadawodd y byd lonydd iddi. Mae’r stori’n rhedeg i’r ddau gyfeiriad.",
   "## Cymru newydd ym Mhatagonia",
   "Ar 28 Gorffennaf 1865 camodd tua 150 o ymfudwyr o Gymru oddi ar y llong de Mimosa ar draeth moel ym Mhatagonia, yn ne’r Ariannin. Roedd eu harweinydd, Michael D. Jones, am gael man lle gallai’r Cymry gadw eu hiaith a’u capeli heb droi’n Saeson nac yn Americanwyr. Bu’r blynyddoedd cynnar yn enbyd, a goroesodd y wladfa’n rhannol drwy gymorth pobl y Tehuelche. Ond daliodd y Wladfa ei thir. Cynhaliai ei llysoedd a’i hysgolion ei hun yn Gymraeg, a rhoddodd y bleidlais i fenywod mewn etholiadau lleol ddegawdau cyn Prydain. Siaredir Cymraeg yn Nyffryn Camwy hyd heddiw, ag acen Archentaidd.",
   "## Ar draws yr Iwerydd",
   "Aeth llawer mwy i’r Unol Daleithiau. Prynodd Crynwyr o Gymru ddarn o dir y tu allan i Philadelphia yn y 1680au, a dyna pam mae gan ei maestrefi enwau fel Bryn Mawr a Bala Cynwyd. Yn y bedwaredd ganrif ar bymtheg recriwtiwyd gweithwyr haearn a glo medrus yn syth o’r cymoedd i Pennsylvania ac Ohio. Erbyn 1890 roedd tua 100,000 o bobl a aned yng Nghymru yn America, a dywedid bod mwy o siaradwyr Cymraeg yn Scranton nag mewn llawer tref yng Nghymru.",
   "## Haearn ar y paith",
   "Yn 1870 hwyliodd John Hughes, peiriannydd o Ferthyr Tudful, i Ymerodraeth Rwsia gyda thua chant o weithwyr haearn a glowyr o Gymru. Tyfodd y gwaith a gododd yn ddinas a enwyd ar ei ôl, Hughesovka neu Yuzovka. Heddiw Donetsk yw hi, yn Wcráin. Teithiodd cenhadon o Gymru ymhell hefyd: ym Mryniau Khasia yng ngogledd-ddwyrain India, Thomas Jones a roddodd yr iaith Khasi ar bapur am y tro cyntaf yn y 1840au, gan ddefnyddio arferion sillafu’r Gymraeg sy’n dal ynddi hyd heddiw.",
   "## Y byd yn dod i Gymru",
   "Daeth y llif y ffordd arall hefyd. Ymgartrefodd teuluoedd o Iwerddon a oedd yn ffoi rhag y newyn yng Nghaerdydd, Casnewydd ac Abertawe yn y 1840au. Agorodd Eidalwyr o ddyffryn Bardi gaffis ym mron pob tref lofaol. Ac o gwmpas dociau Caerdydd tyfodd Butetown, neu Tiger Bay, lle’r ymgartrefodd morwyr o Somalia, Yemen, y Caribî, Gorllewin Affrica, Norwy a Tsieina a phriodi menywod lleol. Erbyn y 1940au roedd pobl o ryw hanner cant o wledydd yn byw yno, un o’r cymunedau amlddiwylliannol hynaf ym Mhrydain. Dysgodd Betty Campbell, a fagwyd yn Butetown ac a ddaeth yn bennaeth ysgol Du cyntaf Cymru, ei hanes i’w disgyblion ymhell cyn iddo gyrraedd unrhyw werslyfr.",
   "Mae hanes Cymru sy’n hepgor y teithiau hyn yn colli ei hanner."]),
]

# Legends: the tale, then "the history behind it".
LEGENDS = [
 dict(id="dragons", era="medieval", art="dragons", place="Dinas Emrys, Gwynedd",
  en="The red dragon and the white", cy="Y ddraig goch a’r ddraig wen",
  sumEn="Why a king’s tower kept falling down, and how Wales got its dragon.", sumCy="Pam y syrthiai tŵr y brenin o hyd, a sut y cafodd Cymru ei draig.",
  pEn=["King Gwrtheyrn, whom the English call Vortigern, fled into the mountains of Eryri to escape the Saxons he had once invited into Britain. On a rocky hill he ordered a tower to be built. Each day his masons raised the walls, and each night the walls fell down.",
   "His wise men said the ground must be sprinkled with the blood of a boy who had no father. Such a boy was found and brought to the hill. But the boy, whose name was Emrys, was not afraid. ‘Dig beneath your tower,’ he said, ‘and you will find a pool. In the pool are two dragons, and it is their fighting that shakes your walls down.’",
   "They dug, and it was so. A red dragon and a white dragon rose from the water and fought across the sky. At first the white dragon had the better of it, but the red dragon rallied and drove it away. ‘The white dragon is the Saxons,’ said Emrys, ‘and the red dragon is your own people, who will one day rise and drive them back.’ The king left the hill to the boy, and it has been called Dinas Emrys ever since."],
  pCy=["Ffodd y Brenin Gwrtheyrn i fynyddoedd Eryri i ddianc rhag y Sacsoniaid yr oedd ef ei hun wedi’u gwahodd i Brydain. Ar fryn creigiog gorchmynnodd godi tŵr. Bob dydd codai ei seiri maen y muriau, a phob nos syrthiai’r muriau.",
   "Dywedodd ei ddoethion fod rhaid taenellu’r tir â gwaed bachgen heb dad. Cafwyd hyd i fachgen felly a’i ddwyn i’r bryn. Ond nid oedd ofn ar y bachgen, a’i enw oedd Emrys. ‘Cloddiwch dan eich tŵr,’ meddai, ‘ac fe gewch lyn. Yn y llyn mae dwy ddraig, a’u hymladd hwy sy’n ysgwyd eich muriau i’r llawr.’",
   "Cloddiwyd, ac felly y bu. Cododd draig goch a draig wen o’r dŵr ac ymladd ar draws yr awyr. Ar y dechrau’r ddraig wen oedd drechaf, ond ymwrolodd y ddraig goch a’i gyrru ymaith. ‘Y Sacsoniaid yw’r ddraig wen,’ meddai Emrys, ‘a’ch pobl chi yw’r ddraig goch, a fydd ryw ddydd yn codi ac yn eu gyrru’n ôl.’ Gadawodd y brenin y bryn i’r bachgen, a Dinas Emrys y’i gelwir byth ers hynny."],
  hEn="The story was first written down around 829 in the Historia Brittonum, and Geoffrey of Monmouth later turned the boy into Merlin. Archaeologists who dug at Dinas Emrys in the 1950s found a real pool inside the fort, and signs that someone important lived there in the fifth century, just when Vortigern is supposed to have ruled. The red dragon has been a Welsh emblem ever since; Henry Tudor carried it to Bosworth in 1485.",
  hCy="Ysgrifennwyd y stori gyntaf tua 829 yn yr Historia Brittonum, ac yn ddiweddarach trodd Sieffre o Fynwy’r bachgen yn Fyrddin. Cafodd archaeolegwyr a gloddiodd yn Ninas Emrys yn y 1950au lyn go iawn y tu mewn i’r gaer, ac arwyddion fod rhywun o bwys yn byw yno yn y bumed ganrif, yr union adeg y dywedir i Wrtheyrn deyrnasu. Mae’r ddraig goch yn arwyddlun Cymreig byth ers hynny; cludodd Harri Tudur hi i Bosworth yn 1485."),

 dict(id="gelert", era="medieval", art="hound", place="Beddgelert, Gwynedd",
  en="Gelert, the faithful hound", cy="Gelert, y ci ffyddlon",
  sumEn="A prince, his favourite hound, and a mistake that could not be undone.", sumCy="Tywysog, ei hoff gi, a chamgymeriad na ellid ei ddadwneud.",
  pEn=["Prince Llywelyn had a hound named Gelert, the swiftest and bravest of all his pack. One morning the prince rode out to hunt, but Gelert was nowhere to be found, and Llywelyn went without him.",
   "When he came home, Gelert bounded out to meet him, and the hound’s jaws were red with blood. The prince ran to the room where his baby son slept. The cradle was overturned, the blankets were torn and bloody, and the child was gone. In grief and rage Llywelyn drew his sword and drove it into the hound’s side.",
   "As Gelert cried out, a baby’s cry answered. Llywelyn lifted the cradle and found his son beneath it, unharmed. Beside him lay the body of a great wolf, killed by Gelert. The prince, it is said, never smiled again. He buried the hound with honour beside the river, and the place is called Beddgelert, Gelert’s grave."],
  pCy=["Roedd gan y Tywysog Llywelyn gi o’r enw Gelert, y cyflymaf a’r dewraf o’i holl helgwn. Un bore aeth y tywysog allan i hela, ond nid oedd golwg o Gelert yn unman, ac aeth Llywelyn hebddo.",
   "Pan ddaeth adref, neidiodd Gelert allan i’w gyfarfod, a safn y ci’n goch gan waed. Rhedodd y tywysog i’r ystafell lle cysgai ei fab bychan. Roedd y crud wedi’i ddymchwel, y blancedi’n rhacs ac yn waedlyd, a’r plentyn wedi mynd. Mewn galar a dicter tynnodd Llywelyn ei gleddyf a’i wthio i ystlys y ci.",
   "Wrth i Gelert udo, atebodd cri baban. Cododd Llywelyn y crud a chael ei fab oddi tano, yn ddianaf. Wrth ei ymyl gorweddai corff blaidd mawr, wedi’i ladd gan Gelert. Ni wenodd y tywysog byth wedyn, meddir. Claddodd y ci’n anrhydeddus ar lan yr afon, a Beddgelert yw enw’r lle."],
  hEn="It is a fine story, and almost certainly a piece of eighteenth-century marketing. The village is probably named after an early saint called Celert. Around 1793 David Prichard, landlord of the Goat Inn, attached an old folk tale to the place and raised the ‘grave’ you can still visit, to bring in the new tourists. The same tale of a faithful animal wrongly killed is told from India to France. Llywelyn Fawr, at least, was real.",
  hCy="Mae’n stori wych, ond bron yn sicr darn o farchnata o’r ddeunawfed ganrif ydyw. Mae’n debyg mai ar ôl sant cynnar o’r enw Celert yr enwyd y pentref. Tua 1793 cysylltodd David Prichard, tafarnwr y Goat, hen chwedl werin â’r lle a chodi’r ‘bedd’ y gallwch ymweld ag ef o hyd, er mwyn denu’r twristiaid newydd. Adroddir yr un stori am anifail ffyddlon a laddwyd ar gam o India i Ffrainc. Roedd Llywelyn Fawr, o leiaf, yn ddyn go iawn."),

 dict(id="cantre", era="saints", art="sunken", place="Bae Ceredigion · Cardigan Bay",
  en="Cantre’r Gwaelod, the drowned kingdom", cy="Cantre’r Gwaelod",
  sumEn="A rich land under Cardigan Bay, lost in a single night because one man forgot to shut a gate.", sumCy="Tir bras dan Fae Ceredigion, a gollwyd mewn un noson am i un dyn anghofio cau llifddor.",
  pEn=["Where the waves of Cardigan Bay now roll there was once a fair, low-lying land called Cantre’r Gwaelod, the Lowland Hundred. It had sixteen cities and belonged to King Gwyddno Garanhir. The sea was kept out by a great wall, with sluice gates that were opened at low tide to drain the fields and shut again before the water rose.",
   "The keeper of the gates was a prince named Seithenyn. One night there was a feast at the king’s court, and Seithenyn drank deep and fell asleep. A storm blew in from the west. The tide rose, the gates stood open, and the sea poured through. By morning Cantre’r Gwaelod was gone, and only a few escaped to the hills along the causeway.",
   "They say that on a still evening, if you stand on the shore at Aberdyfi, you can hear the bells of the drowned churches ringing under the water."],
  pCy=["Lle mae tonnau Bae Ceredigion heddiw, roedd unwaith dir teg, isel o’r enw Cantre’r Gwaelod. Roedd ynddo un ar bymtheg o ddinasoedd, a’r Brenin Gwyddno Garanhir oedd piau ef. Cedwid y môr allan gan forglawdd mawr, â llifddorau a agorid ar y trai i ddraenio’r caeau a’u cau drachefn cyn i’r dŵr godi.",
   "Ceidwad y llifddorau oedd tywysog o’r enw Seithenyn. Un noson roedd gwledd yn llys y brenin, ac yfodd Seithenyn yn drwm a syrthio i gysgu. Chwythodd storm o’r gorllewin. Cododd y llanw, safai’r dorau ar agor, a llifodd y môr drwodd. Erbyn y bore roedd Cantre’r Gwaelod wedi mynd, a dim ond ychydig a ddihangodd i’r bryniau ar hyd y sarn.",
   "Dywedir, ar noson lonydd, os sefwch ar y traeth yn Aberdyfi, y gallwch glywed clychau’r eglwysi a foddwyd yn canu dan y dŵr."],
  hEn="The oldest version, in the thirteenth-century Black Book of Carmarthen, blames a well-maiden called Mererid rather than a drunkard. But the sea really did take this land. At very low tides the stumps of a forest of oak, pine and birch appear in the sand between Borth and Ynyslas, drowned as sea levels rose some 4,500 to 6,000 years ago. Long ridges of stone left by the glaciers, such as Sarn Badrig, run miles out to sea and look very like ruined walls. The legend may be a memory handed down from the people who watched the water come in.",
  hCy="Mae’r fersiwn hynaf, yn Llyfr Du Caerfyrddin o’r drydedd ganrif ar ddeg, yn beio morwyn ffynnon o’r enw Mererid yn hytrach na meddwyn. Ond fe gymerodd y môr y tir hwn go iawn. Ar drai isel iawn daw bonion coedwig o dderw, pinwydd a bedw i’r golwg yn y tywod rhwng y Borth ac Ynys-las, a foddwyd wrth i lefel y môr godi ryw 4,500 i 6,000 o flynyddoedd yn ôl. Mae cefnau hir o gerrig a adawyd gan y rhewlifoedd, fel Sarn Badrig, yn ymestyn filltiroedd i’r môr ac yn edrych yn debyg iawn i furiau adfeiliedig. Efallai mai atgof a drosglwyddwyd gan y bobl a welodd y dŵr yn dod i mewn yw’r chwedl."),

 dict(id="llynyfan", era="kings", art="lady", place="Llyn y Fan Fach, Sir Gaerfyrddin",
  en="The Lady of Llyn y Fan Fach", cy="Morwyn Llyn y Fan Fach",
  sumEn="A farmer wins a wife from the lake, on one condition.", sumCy="Mae ffermwr yn ennill gwraig o’r llyn, ar un amod.",
  pEn=["A young farmer was grazing his mother’s cattle beside Llyn y Fan Fach, under the Black Mountain, when he saw a woman sitting on the surface of the lake, combing her hair. He offered her his bread. Twice she refused it, once because it was baked too hard and once because it was too soft. The third time it was just right, and she agreed to marry him. But she gave a warning: if he struck her three times without cause, she would return to the lake for ever.",
   "They lived happily for many years and had three sons. But three times, without thinking, he tapped her: once to hurry her to a christening, once when she wept at a wedding, once when she laughed at a funeral. At the third touch she walked back to the lake, calling her cattle after her by name, and every beast followed her under the water.",
   "Her sons often walked by the lake hoping to see her. One day she rose and met them, and taught the eldest, Rhiwallon, the healing power of every herb that grew on the mountain. He and his sons became the most famous doctors in Wales."],
  pCy=["Roedd ffermwr ifanc yn pori gwartheg ei fam ar lan Llyn y Fan Fach, dan y Mynydd Du, pan welodd ferch yn eistedd ar wyneb y llyn yn cribo’i gwallt. Cynigiodd ei fara iddi. Ddwywaith gwrthododd hi ef, unwaith am ei fod wedi’i grasu’n rhy galed ac unwaith am ei fod yn rhy feddal. Y trydydd tro roedd yn berffaith, a chytunodd hi i’w briodi. Ond rhoddodd rybudd: pe trawai ef hi dair gwaith heb achos, dychwelai hi i’r llyn am byth.",
   "Buont fyw’n hapus am flynyddoedd lawer a chawsant dri mab. Ond deirgwaith, heb feddwl, fe’i cyffyrddodd: unwaith i’w brysio i fedydd, unwaith pan wylodd mewn priodas, unwaith pan chwarddodd mewn angladd. Ar y trydydd cyffyrddiad cerddodd hi’n ôl i’r llyn, gan alw ei gwartheg ar ei hôl wrth eu henwau, a dilynodd pob anifail hi dan y dŵr.",
   "Cerddai ei meibion yn aml ar lan y llyn gan obeithio’i gweld. Un diwrnod cododd hi a’u cyfarfod, a dysgodd i’r hynaf, Rhiwallon, rym iachaol pob llysieuyn a dyfai ar y mynydd. Daeth ef a’i feibion yn feddygon enwocaf Cymru."],
  hEn="The Physicians of Myddfai were real. Rhiwallon and his sons were doctors to Rhys Gryg, prince of Deheubarth, in the early thirteenth century, and their herbal remedies are preserved in the Red Book of Hergest. Families claiming descent from them practised medicine around Myddfai into the 1800s. The tale gave a line of country doctors an origin worthy of their skill.",
  hCy="Roedd Meddygon Myddfai’n bobl go iawn. Roedd Rhiwallon a’i feibion yn feddygon i Rys Gryg, tywysog Deheubarth, ar ddechrau’r drydedd ganrif ar ddeg, ac mae eu meddyginiaethau llysieuol ar glawr yn Llyfr Coch Hergest. Bu teuluoedd a hawliai eu bod yn ddisgynyddion iddynt yn ymarfer meddygaeth o gwmpas Myddfai hyd at y 1800au. Rhoddodd y chwedl i linach o feddygon gwlad darddiad teilwng o’u dawn."),

 dict(id="branwen", era="ancient", art="bird", place="Harlech · Ynys Môn",
  links=[("story-bran.html", "Brân Fendigaid, the Blessed: the long read", "Bendigeidfran: yr erthygl"), ("person-bran-fendigaid.html", "Brân the Blessed", "Bendigeidfran")],
  en="Branwen and the starling", cy="Branwen a’r ddrudwen",
  sumEn="A marriage meant to bring peace between Wales and Ireland ends in the ruin of both.", sumCy="Mae priodas a oedd i ddod â heddwch rhwng Cymru ac Iwerddon yn gorffen mewn distryw i’r ddwy.",
  pEn=["Bendigeidfran, Brân the Blessed, was king of the Island of the Mighty, and so huge that no house could hold him. From the rock of Harlech he saw the ships of Matholwch, king of Ireland, who had come to ask for the hand of his sister Branwen. The match was made. But Branwen’s half-brother Efnysien, who had not been asked, mutilated the Irish king’s horses in his fury, and though Brân paid for the insult with gifts, it was not forgotten.",
   "In Ireland, Branwen bore a son. Then the old grievance was stirred up, and she was sent to work in the kitchens, where the butcher struck her every day. For three years she endured it. She reared a starling at the edge of her kneading trough, taught it to speak, tied a letter under its wing and sent it over the sea.",
   "Brân came with all his army, wading through the water beside his ships. Where a river barred the way he lay down across it and his men marched over his body, saying, ‘A fo ben, bid bont’: he who would be a leader, let him be a bridge. The war that followed destroyed Ireland. Of the men of Britain only seven came home. Branwen looked back at the two islands laid waste because of her, and her heart broke on the bank of the Alaw."],
  pCy=["Bendigeidfran oedd brenin Ynys y Cedyrn, ac yr oedd mor fawr fel na allai’r un tŷ ei gynnwys. O graig Harlech gwelodd longau Matholwch, brenin Iwerddon, a ddaethai i ofyn am law ei chwaer Branwen. Trefnwyd y briodas. Ond yn ei gynddaredd am na ofynnwyd ei ganiatâd, anffurfiodd Efnysien, hanner brawd Branwen, feirch brenin Iwerddon, ac er i Frân dalu iawn am y sarhad ag anrhegion, nid anghofiwyd mohono.",
   "Yn Iwerddon, ganed mab i Franwen. Yna codwyd yr hen gŵyn drachefn, ac fe’i gyrrwyd i weithio yn y gegin, lle trawai’r cigydd hi bob dydd. Dioddefodd hynny am dair blynedd. Magodd ddrudwen ar ymyl ei chafn tylino, dysgodd iddi siarad, clymodd lythyr dan ei hadain a’i hanfon dros y môr.",
   "Daeth Brân â’i holl fyddin, gan gerdded drwy’r dŵr wrth ochr ei longau. Lle’r oedd afon yn rhwystr, gorweddodd ar ei thraws a cherddodd ei wŷr dros ei gorff, gan ddweud, ‘A fo ben, bid bont’. Dinistriodd y rhyfel a ddilynodd Iwerddon. O wŷr Prydain, saith yn unig a ddaeth adref. Edrychodd Branwen yn ôl ar y ddwy ynys a ddifethwyd o’i hachos, a thorrodd ei chalon ar lan afon Alaw."],
  hEn="This is the Second Branch of the Mabinogi, written down between about 1060 and 1200 from much older oral tales. ‘A fo ben, bid bont’ is still quoted as a Welsh proverb about leadership. On the bank of the Alaw on Ynys Môn is a Bronze Age burial mound called Bedd Branwen, Branwen’s Grave; when it was opened in 1813 it held an urn of cremated bones, some three thousand years old.",
  hCy="Dyma Ail Gainc y Mabinogi, a roddwyd ar femrwn rhwng tua 1060 a 1200 o chwedlau llafar llawer hŷn. Dyfynnir ‘A fo ben, bid bont’ o hyd fel dihareb am arweinyddiaeth. Ar lan afon Alaw ym Môn mae carnedd gladdu o Oes yr Efydd o’r enw Bedd Branwen; pan agorwyd hi yn 1813 roedd ynddi wrn o esgyrn amlosgedig, rhyw dair mil o flynyddoedd oed."),

 dict(id="blodeuwedd", era="modern", art="owl", place="Ardudwy, Gwynedd",
  en="Blodeuwedd, the woman made of flowers", cy="Blodeuwedd",
  sumEn="Two magicians make a wife out of flowers. She turns out to have a will of her own.", sumCy="Mae dau ddewin yn creu gwraig o flodau. Daw’n amlwg fod ganddi ewyllys ei hun.",
  pEn=["Lleu Llaw Gyffes was under a curse: he could never have a wife of any race on earth. So the magicians Math and Gwydion took the flowers of the oak, the broom and the meadowsweet, and from them conjured the fairest woman anyone had seen. They named her Blodeuwedd, ‘flower-face’, and gave her to Lleu.",
   "No one had asked Blodeuwedd. One day while Lleu was away, a hunter named Gronw Pebr came to the door, and the two fell in love. Lleu could not be killed by day or night, indoors or out, riding or walking. Blodeuwedd coaxed the secret from him: he could only be killed at dusk, under a thatched roof with no walls, with one foot on the edge of a bath and the other on a goat’s back, by a spear a year in the making. She arranged it exactly so. Gronw’s spear struck, and Lleu flew up as an eagle and vanished.",
   "Gwydion searched until he found the eagle and sang it down from an oak tree, and made Lleu a man again. Gronw had to stand and take a spear in return, and it passed straight through the stone he hid behind. Blodeuwedd was not killed. Gwydion turned her into an owl, to hunt alone by night, shunned by every other bird."],
  pCy=["Roedd Lleu Llaw Gyffes dan dynged: ni châi byth wraig o unrhyw genedl ar y ddaear. Felly cymerodd y dewiniaid Math a Gwydion flodau’r deri, y banadl a’r erwain, a chreu ohonynt y ferch decaf a welodd neb erioed. Enwyd hi’n Blodeuwedd, a’i rhoi i Leu.",
   "Nid oedd neb wedi gofyn i Flodeuwedd. Un diwrnod tra oedd Lleu oddi cartref, daeth heliwr o’r enw Gronw Pebr at y drws, a syrthiodd y ddau mewn cariad. Ni ellid lladd Lleu na liw dydd na liw nos, nac mewn tŷ nac allan, nac ar farch nac ar droed. Denodd Blodeuwedd y gyfrinach ohono: ni ellid ei ladd ond gyda’r hwyr, dan do gwellt heb furiau, ag un droed ar ymyl cafn ymolchi a’r llall ar gefn bwch gafr, â gwaywffon y bu blwyddyn yn ei gwneud. Trefnodd hi’r cyfan yn union felly. Trawodd gwaywffon Gronw, a hedfanodd Lleu ymaith yn eryr a diflannu.",
   "Chwiliodd Gwydion nes cael hyd i’r eryr a’i ganu i lawr o dderwen, a gwneud Lleu’n ddyn eto. Bu raid i Gronw sefyll a derbyn gwaywffon yn ôl, ac aeth honno’n syth drwy’r llech y cuddiai y tu ôl iddi. Ni laddwyd Blodeuwedd. Trodd Gwydion hi’n dylluan, i hela ar ei phen ei hun liw nos, a phob aderyn arall yn ei herlid."],
  hEn="This is the Fourth Branch of the Mabinogi. In Welsh, ‘blodeuwedd’ is still a word for an owl. A slab of slate with a neat hole through it, Llech Ronw, stands by the river Cynfal near Blaenau Ffestiniog, close to the Roman fort of Tomen y Mur where the tale places Lleu’s court. Modern writers have retold the story with more sympathy for a woman created to order: Saunders Lewis’s play Blodeuwedd (1948) and Alan Garner’s novel The Owl Service (1967) both begin here.",
  hCy="Dyma Bedwaredd Gainc y Mabinogi. Mae ‘blodeuwedd’ yn dal yn air Cymraeg am dylluan. Saif llech ac ynddi dwll crwn, Llech Ronw, ar lan afon Cynfal ger Blaenau Ffestiniog, heb fod ymhell o gaer Rufeinig Tomen y Mur lle mae’r chwedl yn gosod llys Lleu. Mae awduron modern wedi ailadrodd y stori gyda mwy o gydymdeimlad â merch a grëwyd ar archeb: mae drama Saunders Lewis, Blodeuwedd (1948), a nofel Alan Garner, The Owl Service (1967), ill dwy’n dechrau yma."),

 dict(id="arthur", era="kings", art="sword", place="Eryri · Caerllion",
  en="Arthur, the sleeping king", cy="Arthur, y brenin sy’n cysgu",
  sumEn="Before he belonged to the world, Arthur belonged to Wales.", sumCy="Cyn iddo berthyn i’r byd, i Gymru y perthynai Arthur.",
  pEn=["They say Arthur fought his last battle in the mountains of Eryri. He drove his enemies up from Cwm Llan to the pass below the summit of Yr Wyddfa, and there, at Bwlch y Saethau, the Pass of the Arrows, he fell. His knights carried him down to the shore of Llyn Llydaw, where a black boat was waiting, and three women bore him away across the water.",
   "His men did not follow. They climbed the cliffs of Lliwedd, and went into a cave, and the rock closed behind them. There they sleep in their armour, leaning on their shields.",
   "Once, long after, a shepherd looking for a lost sheep squeezed through a gap in the rock and saw them by the light of a lamp: a great company of warriors, asleep. As he turned to go he struck his head on a bell hanging in the passage. It rang, and the sleepers stirred and shouted, ‘Has the day come?’ The shepherd fled, and never found the place again. But they are waiting there still, and when Wales has need of them the bell will ring."],
  pCy=["Dywedir i Arthur ymladd ei frwydr olaf ym mynyddoedd Eryri. Gyrrodd ei elynion i fyny o Gwm Llan at y bwlch dan gopa’r Wyddfa, ac yno, ym Mwlch y Saethau, y syrthiodd. Cludodd ei farchogion ef i lawr at lan Llyn Llydaw, lle’r oedd cwch du’n disgwyl, ac aeth tair gwraig ag ef ymaith dros y dŵr.",
   "Ni ddilynodd ei wŷr. Dringasant glogwyni Lliwedd a mynd i mewn i ogof, a chaeodd y graig ar eu hôl. Yno maent yn cysgu yn eu harfwisg, yn pwyso ar eu tarianau.",
   "Unwaith, ymhell wedyn, gwasgodd bugail a chwiliai am ddafad goll drwy hollt yn y graig a’u gweld yng ngolau lamp: llu mawr o ryfelwyr, ynghwsg. Wrth iddo droi i fynd trawodd ei ben yn erbyn cloch a grogai yn y fynedfa. Canodd hithau, a chyffrôdd y cysgwyr a gweiddi, ‘A ddaeth y dydd?’ Ffodd y bugail, ac ni chafodd hyd i’r lle byth wedyn. Ond maent yno o hyd yn disgwyl, a phan fydd ar Gymru eu hangen fe gân y gloch."],
  hEn="Welsh tradition holds that Arthur was Athrwys ap Meurig, king of Gwent and Glywysing, and the earliest writings about him are all Welsh. A line in Y Gododdin praises a warrior ‘though he was no Arthur’. The Historia Brittonum of about 829 lists his twelve battles. Culhwch ac Olwen, written down around 1100, is the oldest Arthurian tale in any language, and has him hunting a monstrous boar across south Wales. Then, in the 1130s, Geoffrey of Monmouth set Arthur’s court at Caerleon and made him the most famous king in Europe. The knights, the Round Table and the Grail were added later, in France.",
  hCy="Yn ôl traddodiad Cymru, Athrwys ap Meurig, brenin Gwent a Glywysing, oedd Arthur, a Chymreig yw pob un o’r ysgrifau cynharaf amdano. Mae llinell yn Y Gododdin yn canmol rhyfelwr ‘er nad Arthur ydoedd’. Mae’r Historia Brittonum, tua 829, yn rhestru ei ddeuddeg brwydr. Culhwch ac Olwen, a ysgrifennwyd tua 1100, yw’r chwedl Arthuraidd hynaf mewn unrhyw iaith, ac ynddi mae’n hela baedd anferth ar draws y de. Yna, yn y 1130au, gosododd Sieffre o Fynwy lys Arthur yng Nghaerllion a’i wneud yn frenin enwocaf Ewrop. Yn Ffrainc, yn ddiweddarach, yr ychwanegwyd y marchogion, y Ford Gron a’r Greal."),

 dict(id="taliesin", era="saints", art="cauldron", place="Llyn Tegid · Y Bala",
  en="Ceridwen’s cauldron and the birth of Taliesin", cy="Pair Ceridwen a geni Taliesin",
  sumEn="Three drops from a witch’s cauldron turn a servant boy into the greatest of poets.", sumCy="Mae tri diferyn o bair gwrach yn troi gwas bach yn bennaf y beirdd.",
  pEn=["Ceridwen lived beside Llyn Tegid with her son Morfran, who was so ugly that she resolved to make him wise instead. She set a cauldron to boil for a year and a day, filled with herbs gathered by the hours of the planets. At the end, three drops would hold all the knowledge in the world. A boy called Gwion Bach was set to stir it.",
   "On the last day the cauldron spat, and three scalding drops fell on Gwion’s thumb. He put it in his mouth, and at once he knew everything, including that Ceridwen would kill him. He ran. He became a hare, and she a greyhound. He leapt into the river as a fish, and she followed as an otter. He rose as a bird, and she stooped on him as a hawk. At last he dropped into a heap of wheat as a single grain, and she became a black hen and swallowed him.",
   "Nine months later she bore a child so beautiful that she could not kill him. She sewed him into a leather bag and cast him into the sea. On May Eve the bag caught in the fish weir of Gwyddno Garanhir, where the king’s unlucky son Elffin found it. He opened it, saw the shining forehead of a child, and cried, ‘Tal iesin!’: a radiant brow. And the child answered him in verse."],
  pCy=["Roedd Ceridwen yn byw ar lan Llyn Tegid gyda’i mab Morfran, a oedd mor hyll nes iddi benderfynu ei wneud yn ddoeth yn lle hynny. Gosododd bair i ferwi am flwyddyn a diwrnod, yn llawn llysiau a gasglwyd yn ôl oriau’r planedau. Ar y diwedd byddai tri diferyn yn dal holl wybodaeth y byd. Gosodwyd bachgen o’r enw Gwion Bach i’w droi.",
   "Ar y diwrnod olaf poerodd y pair, a syrthiodd tri diferyn berwedig ar fawd Gwion. Rhoddodd ef yn ei geg, ac ar unwaith gwyddai bopeth, gan gynnwys y byddai Ceridwen yn ei ladd. Rhedodd. Aeth yn ysgyfarnog, a hithau’n filiast. Neidiodd i’r afon yn bysgodyn, a dilynodd hithau’n ddyfrgi. Cododd yn aderyn, a disgynnodd hithau arno’n hebog. O’r diwedd syrthiodd i bentwr o wenith yn un gronyn, ac aeth hithau’n iâr ddu a’i lyncu.",
   "Naw mis yn ddiweddarach esgorodd ar blentyn mor hardd fel na allai ei ladd. Gwnïodd ef mewn cwdyn lledr a’i daflu i’r môr. Nos Galan Mai daliwyd y cwdyn yng nghored Gwyddno Garanhir, lle cafodd Elffin, mab anlwcus y brenin, hyd iddo. Agorodd ef, gwelodd dalcen disglair plentyn, a gwaeddodd, ‘Tal iesin!’ Ac atebodd y plentyn ef ar gân."],
  hEn="Taliesin was a real poet of the late sixth century, who sang for King Urien of Rheged in what is now northern England and southern Scotland; a dozen of his poems survive. The magical story of his birth grew up centuries later and was first written down in the 1500s. Its shape-shifting chase is one of the oldest motifs in European storytelling. The National Eisteddfod still honours its best poets in his tradition, and the village of Tre Taliesin in Ceredigion stands near a cairn called his grave.",
  hCy="Bardd go iawn o ddiwedd y chweched ganrif oedd Taliesin, a ganai i’r Brenin Urien Rheged yn yr hyn sydd heddiw’n ogledd Lloegr a de’r Alban; mae dwsin o’i gerddi wedi goroesi. Tyfodd stori hudol ei eni ganrifoedd yn ddiweddarach ac fe’i hysgrifennwyd gyntaf yn y 1500au. Mae’r erlid a’r newid ffurf ynddi’n un o’r motiffau hynaf yn chwedloniaeth Ewrop. Mae’r Eisteddfod Genedlaethol yn dal i anrhydeddu ei beirdd gorau yn ei draddodiad ef, a saif pentref Tre Taliesin yng Ngheredigion ger carnedd a elwir yn fedd iddo."),
]

# Symbols and traditions: (id, icon, EN title, CY title, EN text, CY text)
SYMBOLS = [
 ("dragon", "Y Ddraig Goch", "Y Ddraig Goch", "The red dragon",
  "The red dragon appears as the emblem of the Britons in the Historia Brittonum around 829. Henry Tudor marched under it to Bosworth in 1485 and added the green and white of his family. It became the official flag of Wales only in 1959.",
  "Mae’r ddraig goch yn ymddangos fel arwyddlun y Brythoniaid yn yr Historia Brittonum tua 829. Gorymdeithiodd Harri Tudur oddi tani i Bosworth yn 1485 gan ychwanegu gwyrdd a gwyn ei deulu. Ni ddaeth yn faner swyddogol Cymru tan 1959."),
 ("leek", "Y genhinen", "Y genhinen", "The leek",
  "Tradition says Saint David told Welsh soldiers to wear leeks in their caps so they could tell friend from foe in a battle against the Saxons. Shakespeare’s Fluellen wears one in Henry V, and Welsh regiments still eat a raw leek on 1 March.",
  "Yn ôl traddodiad, dywedodd Dewi Sant wrth filwyr Cymru am wisgo cennin yn eu capiau er mwyn adnabod ei gilydd mewn brwydr yn erbyn y Sacsoniaid. Mae Fluellen Shakespeare yn gwisgo un yn Henry V, ac mae catrodau Cymreig yn dal i fwyta cenhinen amrwd ar 1 Mawrth."),
 ("daffodil", "Y genhinen Bedr", "Y genhinen Bedr", "The daffodil",
  "The daffodil is a newcomer, popular only since the nineteenth century. Its Welsh name means ‘Peter’s leek’, which may be how the two got confused. David Lloyd George preferred it to the leek and wore one at the investiture of 1911.",
  "Newydd-ddyfodiad yw’r genhinen Bedr, sy’n boblogaidd er y bedwaredd ganrif ar bymtheg yn unig. Efallai mai tebygrwydd yr enw i’r genhinen a achosodd y dryswch rhwng y ddwy. Roedd yn well gan David Lloyd George hi na’r genhinen, a gwisgodd un yn arwisgiad 1911."),
 ("harp", "Y delyn", "Y delyn", "The harp",
  "Harpers had a legal place at court under the laws of Hywel Dda. The triple harp, with three rows of strings, arrived from Italy in the 1600s and was adopted so completely that it became known as the Welsh harp. Wales is still called the land of song.",
  "Roedd gan delynorion le cyfreithiol yn y llys dan gyfraith Hywel Dda. Cyrhaeddodd y delyn deires, â thair rhes o dannau, o’r Eidal yn y 1600au ac fe’i mabwysiadwyd mor llwyr nes ei galw’n delyn Gymreig. Gelwir Cymru’n wlad y gân hyd heddiw."),
 ("anthem", "Hen Wlad Fy Nhadau", "Hen Wlad Fy Nhadau", "Land of My Fathers",
  "The national anthem was written in Pontypridd in January 1856 by a weaver, Evan James, to a tune by his son James. It was sung before a rugby international for the first time in 1905, when Wales answered the New Zealand haka with it, and then beat them.",
  "Ysgrifennwyd yr anthem genedlaethol ym Mhontypridd ym mis Ionawr 1856 gan wehydd, Evan James, ar alaw gan ei fab James. Fe’i canwyd cyn gêm rygbi ryngwladol am y tro cyntaf yn 1905, pan atebodd Cymru haka Seland Newydd â hi, ac yna eu curo."),
 ("eisteddfod", "Yr Eisteddfod", "Yr Eisteddfod", "The Eisteddfod",
  "The Lord Rhys held a contest of poets and musicians at Cardigan Castle in 1176, the first known eisteddfod. The modern National Eisteddfod dates from 1861 and moves between north and south each August. Its Gorsedd of bards, in white, blue and green robes, was founded by Iolo Morganwg in 1792.",
  "Cynhaliodd yr Arglwydd Rhys ornest i feirdd a cherddorion yng Nghastell Aberteifi yn 1176, yr eisteddfod gyntaf y gwyddys amdani. Mae’r Eisteddfod Genedlaethol fodern yn dyddio o 1861 ac yn symud rhwng y gogledd a’r de bob mis Awst. Sefydlwyd Gorsedd y Beirdd, yn eu gwisgoedd gwyn, glas a gwyrdd, gan Iolo Morganwg yn 1792."),
 ("lovespoon", "Llwyau caru", "Llwyau caru", "Lovespoons",
  "A young man would carve a wooden spoon for the woman he hoped to marry, working hearts, keys, wheels and chains into the handle to show his skill and his intentions. The oldest dated Welsh lovespoon, from 1667, is at St Fagans.",
  "Byddai dyn ifanc yn cerfio llwy bren i’r ferch y gobeithiai ei phriodi, gan weithio calonnau, allweddi, olwynion a chadwyni i’r goes i ddangos ei fedr a’i fwriad. Mae’r llwy garu Gymreig hynaf â dyddiad arni, o 1667, yn Sain Ffagan."),
 ("dwynwen", "Dydd Santes Dwynwen", "Dydd Santes Dwynwen", "St Dwynwen’s Day",
  "Dwynwen was a fifth-century princess who, unlucky in love herself, became a nun on a tidal island off Ynys Môn and prayed for all true lovers. Her day, 25 January, is the Welsh Valentine’s Day. The ruins of her church stand at Llanddwyn.",
  "Tywysoges o’r bumed ganrif oedd Dwynwen. Wedi siom mewn cariad, aeth yn lleian ar ynys lanw ger Môn a gweddïo dros bob gwir gariad. Ei dydd hi, 25 Ionawr, yw dydd y cariadon yng Nghymru. Saif adfeilion ei heglwys yn Llanddwyn."),
 ("mari", "Y Fari Lwyd", "Y Fari Lwyd", "The Mari Lwyd",
  "In midwinter a horse’s skull on a pole, draped in a white sheet and hung with ribbons, is carried from door to door in parts of south Wales. Her party must win a battle of rhyming insults, the pwnco, before they are let in for food and drink.",
  "Ganol gaeaf cludir penglog ceffyl ar bolyn, dan gynfas wen ac wedi’i haddurno â rhubanau, o ddrws i ddrws mewn rhannau o’r de. Rhaid i’w chriw ennill gornest o benillion pryfoclyd, y pwnco, cyn cael dod i mewn am fwyd a diod."),
 ("costume", "Y wisg Gymreig", "Y wisg Gymreig", "Welsh costume",
  "The red shawl and tall black hat are less ancient than they look. They are the everyday dress of country women in the early 1800s, promoted as a national costume in the 1830s by Lady Llanover, who feared Welsh wool and Welsh identity were both dying out.",
  "Nid yw’r siôl goch a’r het ddu uchel mor hynafol ag y maent yn edrych. Dillad bob dydd gwragedd cefn gwlad ar ddechrau’r 1800au ydynt, a hyrwyddwyd fel gwisg genedlaethol yn y 1830au gan Arglwyddes Llanofer, a ofnai fod gwlân Cymru a hunaniaeth Cymru ill dau’n darfod."),
 ("choir", "Corau meibion", "Corau meibion", "Male voice choirs",
  "Chapel hymn-singing and the crowded industrial valleys produced the male voice choir in the nineteenth century. Choirs of miners and quarrymen competed fiercely at eisteddfodau, and some, such as Treorchy, founded in 1883, are still singing.",
  "Canu emynau’r capeli a chymoedd diwydiannol poblog a roddodd fod i’r côr meibion yn y bedwaredd ganrif ar bymtheg. Cystadlai corau o lowyr a chwarelwyr yn frwd mewn eisteddfodau, ac mae rhai, fel Treorci, a sefydlwyd yn 1883, yn dal i ganu."),
 ("calennig", "Calennig", "Calennig", "Calennig",
  "On New Year’s morning children went from house to house singing for calennig, a small gift of coins or food, sometimes carrying an apple stuck with cloves and sprigs of holly. In Cwm Gwaun, Pembrokeshire, the new year is still kept by the old calendar, on 13 January.",
  "Fore Calan âi plant o dŷ i dŷ i ganu am galennig, sef rhodd fach o arian neu fwyd, weithiau gan gario afal ac ynddo glofs a sbrigyn o gelyn. Yng Nghwm Gwaun, Sir Benfro, cedwir y flwyddyn newydd o hyd yn ôl yr hen galendr, ar 13 Ionawr."),
]

# Quick facts: (English, Welsh, the page that tells the full story). Every fact must link to a full page (Ifan, 12 November 2026).
FACTS = [
 ("The equals sign (=) was invented in 1557 by Robert Recorde, a mathematician from Tenby, because ‘no two things can be more equal’ than two parallel lines.[[cite:dwb-recorde]]",
  "Dyfeisiwyd yr hafalnod (=) yn 1557 gan Robert Recorde, mathemategydd o Ddinbych-y-pysgod, am na all ‘dim dau beth fod yn fwy hafal’ na dwy linell baralel.[[cite:dwb-recorde]]",
  "person-robert-recorde.html"),
 ("William Jones, a farmer’s son from Ynys Môn, was the first person to use the symbol π for the ratio of a circle, in 1706.[[cite:dwb-wjones]]",
  "William Jones, mab fferm o Fôn, oedd y cyntaf i ddefnyddio’r symbol π ar gyfer cymhareb y cylch, yn 1706.[[cite:dwb-wjones]]",
  "person-william-jones.html"),
 ("The world’s first fare-paying passenger railway ran between Swansea and Mumbles from 1807, pulled by horses.[[cite:tfw-mumbles]]",
  "Rhedai rheilffordd deithwyr gyntaf y byd rhwng Abertawe a’r Mwmbwls o 1807 ymlaen, a cheffylau’n ei thynnu.[[cite:tfw-mumbles]]",
  "event-the-mumbles-railway.html"),
 ("The bluestones of Stonehenge were dragged about 240 kilometres from the Preseli hills in Pembrokeshire some 5,000 years ago.[[cite:bluestones-antiquity]]",
  "Llusgwyd cerrig gleision Côr y Cewri tua 240 cilometr o fynyddoedd y Preseli yn Sir Benfro ryw 5,000 o flynyddoedd yn ôl.[[cite:bluestones-antiquity]]",
  "event-the-bluestones-of-preseli.html"),
 ("St Davids, with about 1,800 people, is the smallest city in Britain.[[cite:stdavids-wiki]]",
  "Tyddewi, â thua 1,800 o bobl, yw dinas leiaf Prydain.[[cite:stdavids-wiki]]",
  "place-stdavids.html"),
 ("Guglielmo Marconi sent the first radio message across open sea in 1897, between Lavernock Point near Penarth and the island of Flat Holm. It read: ‘Are you ready?’[[cite:marconi-veterans]]",
  "Anfonodd Guglielmo Marconi y neges radio gyntaf dros fôr agored yn 1897, rhwng Trwyn Larnog ger Penarth ac Ynys Echni. Y neges oedd: ‘Are you ready?’[[cite:marconi-veterans]]",
  "place-lavernock.html"),
 ("The Welsh alphabet has 29 letters. Ch, dd, ff, ng, ll, ph, rh and th each count as a single letter.[[cite:alphabet-parallel]]",
  "Mae 29 llythyren yn yr wyddor Gymraeg. Mae ch, dd, ff, ng, ll, ph, rh a th bob un yn cyfrif fel un llythyren.[[cite:alphabet-parallel]]",
  "topic-language.html"),
 ("Pryce Pryce-Jones of Newtown started the world’s first mail-order business in 1861, selling Welsh flannel by post. Queen Victoria was a customer.[[cite:pryce-storipowys,dwb-pryce]]",
  "Dechreuodd Pryce Pryce-Jones o’r Drenewydd fusnes archebu drwy’r post cyntaf y byd yn 1861, gan werthu gwlanen Gymreig. Roedd y Frenhines Fictoria’n gwsmer.[[cite:pryce-storipowys,dwb-pryce]]",
  "person-pryce-pryce-jones.html"),
 ("The 58-letter name of Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch was made up in the 1860s to bring railway tourists to the village.[[cite:llanfair-nasa]]",
  "Dyfeisiwyd enw 58 llythyren Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch yn y 1860au i ddenu twristiaid y rheilffordd i’r pentref.[[cite:llanfair-nasa]]",
  "place-llanfairpwll.html"),
 ("The Bronze Age copper mines on the Great Orme are among the largest prehistoric mines yet found anywhere in the world.[[cite:orme-antiquity,orme-gsl,orme-guinness]]",
  "Mae mwyngloddiau copr Oes yr Efydd ar y Gogarth ymhlith y mwyngloddiau cynhanesyddol mwyaf a ddarganfuwyd yn unman yn y byd.[[cite:orme-antiquity,orme-gsl,orme-guinness]]",
  "place-orme.html"),
 ("When it opened in 1826, Thomas Telford’s Menai Bridge had the longest span of any suspension bridge in the world.[[cite:menai-graces,menai-ice]]",
  "Pan agorwyd hi yn 1826, Pont y Borth Thomas Telford oedd â’r rhychwant hiraf o unrhyw bont grog yn y byd.[[cite:menai-graces,menai-ice]]",
  "place-menai.html"),
 ("The team that first climbed Everest in 1953 trained on Yr Wyddfa and stayed at the Pen-y-Gwryd Hotel, where their signatures are still on the ceiling.[[cite:everest-pyg]]",
  "Bu’r tîm a ddringodd Everest gyntaf yn 1953 yn ymarfer ar yr Wyddfa gan aros yng Ngwesty Pen-y-Gwryd, lle mae eu llofnodion ar y nenfwd o hyd.[[cite:everest-pyg]]",
  "place-penygwryd.html"),
 ("In the nineteenth century, slate from Gwynedd roofed cities from Hamburg to Melbourne. The quarry landscape became a World Heritage Site in 2021.[[cite:slate-unesco]]",
  "Yn y bedwaredd ganrif ar bymtheg, llechi Gwynedd oedd ar doeau dinasoedd o Hamburg i Melbourne. Daeth tirwedd y chwareli’n Safle Treftadaeth y Byd yn 2021.[[cite:slate-unesco]]",
  "event-the-slate-landscape-world-heritage.html"),
 ("Under the medieval laws of Hywel Dda, a wife who separated from her husband after seven years could take half the household goods.[[cite:hywel-jenkins,hywel-wiki]]",
  "Dan gyfraith Hywel Dda yn yr Oesoedd Canol, gallai gwraig a ymwahanai oddi wrth ei gŵr ar ôl saith mlynedd gymryd hanner eiddo’r cartref.[[cite:hywel-jenkins,hywel-wiki]]",
  "laws.html"),
 ("Roald Dahl was born in Llandaff, Cardiff, in 1916 to Norwegian parents and was christened in the Norwegian Church in Cardiff Bay.[[cite:dahl-visitwales]]",
  "Ganed Roald Dahl yn Llandaf, Caerdydd, yn 1916 i rieni o Norwy, ac fe’i bedyddiwyd yn yr Eglwys Norwyaidd ym Mae Caerdydd.[[cite:dahl-visitwales]]",
  "person-roald-dahl.html"),
 ("Welsh is spoken in Argentina. Settlers from Wales founded a colony in Patagonia in 1865, and their descendants still hold an eisteddfod there every year.[[cite:patagonia-wales]]",
  "Siaredir Cymraeg yn yr Ariannin. Sefydlodd ymfudwyr o Gymru wladfa ym Mhatagonia yn 1865, ac mae eu disgynyddion yn dal i gynnal eisteddfod yno bob blwyddyn.[[cite:patagonia-wales]]",
  "story-world.html"),
 ("Sir William Grove of Swansea built the first working fuel cell in 1842, the technology that now powers hydrogen vehicles.[[cite:grove-aps,dwb-grove]]",
  "Adeiladodd Syr William Grove o Abertawe y gell danwydd weithredol gyntaf yn 1842, y dechnoleg sydd heddiw’n gyrru cerbydau hydrogen.[[cite:grove-aps,dwb-grove]]",
  "person-william-grove.html"),
 ("Caerphilly Castle is the largest castle in Wales and the second largest in Britain. One of its towers leans further than the Tower of Pisa.[[cite:caerphilly-cadw]]",
  "Castell Caerffili yw castell mwyaf Cymru a’r ail fwyaf ym Mhrydain. Mae un o’i dyrau’n gwyro’n fwy na Thŵr Pisa.[[cite:caerphilly-cadw]]",
  "place-caerffili.html"),
 ("The oldest known ceremonial burial in western Europe is the ‘Red Lady’ of Paviland on Gower: in fact a young man, buried about 33,000 years ago.[[cite:paviland-museum,paviland-oumnh]]",
  "Y gladdedigaeth seremonïol hynaf y gwyddys amdani yng ngorllewin Ewrop yw ‘Dynes Goch’ Pafiland ar Benrhyn Gŵyr: dyn ifanc mewn gwirionedd, a gladdwyd tua 33,000 o flynyddoedd yn ôl.[[cite:paviland-museum,paviland-oumnh]]",
  "place-paviland.html"),
 ("Wales has a place called Bethlehem, in Carmarthenshire. Thousands of people send their Christmas cards through its post office for the postmark.[[cite:bethlehem-radio]]",
  "Mae pentref o’r enw Bethlehem yn Sir Gaerfyrddin. Mae miloedd o bobl yn anfon eu cardiau Nadolig drwy ei swyddfa bost er mwyn cael y marc post.[[cite:bethlehem-radio]]",
  "place-bethlehem.html"),
]

# "Which figure from Welsh history are you?": people slugs and what each stands for.
HEROES = {
 "owain-glyndwr": ("The leader", "Yr arweinydd", "You see the big picture and people follow you. Like Owain Glyndŵr, you would rather risk everything for an idea than live comfortably without one.",
                   "Rydych chi’n gweld y darlun mawr ac mae pobl yn eich dilyn. Fel Owain Glyndŵr, byddai’n well gennych fentro popeth dros syniad na byw’n gyfforddus hebddo."),
 "hywel-dda": ("The peacemaker", "Y cymodwr", "You like things fair, orderly and written down. Like Hywel Dda, you would sooner settle an argument than win a fight.",
               "Rydych chi’n hoffi i bethau fod yn deg, yn drefnus ac ar bapur. Fel Hywel Dda, byddai’n well gennych setlo dadl nag ennill brwydr."),
 "gwenllian": ("The fighter", "Yr ymladdwr", "You do not wait for someone else to act. Like Gwenllian, who led an army while her husband was away, you step forward when it matters.",
               "Nid ydych chi’n aros i rywun arall weithredu. Fel Gwenllian, a arweiniodd fyddin tra oedd ei gŵr i ffwrdd, rydych chi’n camu ymlaen pan fo’n cyfrif."),
 "dafydd-ap-gwilym": ("The poet", "Y bardd", "You notice what others walk past, and you are rarely serious for long. Like Dafydd ap Gwilym, you would rather be in the woods than in a meeting.",
                      "Rydych chi’n sylwi ar yr hyn y mae eraill yn cerdded heibio iddo, ac anaml y byddwch o ddifrif yn hir. Fel Dafydd ap Gwilym, byddai’n well gennych fod yn y coed nag mewn cyfarfod."),
 "aneurin-bevan": ("The reformer", "Y diwygiwr", "Unfairness makes you angry, and you are not afraid of an argument. Like Aneurin Bevan, you want to fix the system, not just patch it.",
                   "Mae annhegwch yn eich gwylltio, ac nid oes arnoch ofn dadl. Fel Aneurin Bevan, rydych chi am drwsio’r drefn, nid ei chlytio’n unig."),
 "betsi-cadwaladr": ("The adventurer", "Yr anturiaethwr", "You are practical, restless and hard to shock. Like Betsi Cadwaladr, who sailed the world and then nursed in the Crimea in her sixties, you go where you are needed.",
                     "Rydych chi’n ymarferol, yn aflonydd ac yn anodd eich synnu. Fel Betsi Cadwaladr, a hwyliodd y byd ac yna nyrsio yn y Crimea yn ei chwedegau, rydych chi’n mynd lle mae eich angen."),
}
# Each question: (EN, CY, [(answer EN, answer CY, hero slug), ...])
HERO_QS = [
 ("A free Saturday. Where are you?", "Dydd Sadwrn rhydd. Ble ydych chi?",
  [("Up a mountain, planning something", "Ar ben mynydd, yn cynllunio rhywbeth", "owain-glyndwr"), ("Walking in the woods", "Yn cerdded yn y coed", "dafydd-ap-gwilym"),
   ("At a public meeting", "Mewn cyfarfod cyhoeddus", "aneurin-bevan"), ("Somewhere I have never been", "Rhywle na fûm erioed", "betsi-cadwaladr")]),
 ("Two friends are arguing. You…", "Mae dau ffrind yn dadlau. Rydych chi’n…",
  [("Find a compromise both can accept", "Dod o hyd i gyfaddawd i’r ddau", "hywel-dda"), ("Take the side of whoever is being treated unfairly", "Ochri â’r un sy’n cael cam", "aneurin-bevan"),
   ("Make a joke until they stop", "Gwneud jôc nes iddynt stopio", "dafydd-ap-gwilym"), ("Tell them both, plainly, to sort it out", "Dweud wrth y ddau, yn blaen, am ei sortio", "gwenllian")]),
 ("What would you most like to be remembered for?", "Am beth yr hoffech gael eich cofio fwyaf?",
  [("Standing up when it counted", "Sefyll pan oedd yn cyfrif", "gwenllian"), ("Making life fairer", "Gwneud bywyd yn decach", "aneurin-bevan"),
   ("Something beautiful I made", "Rhywbeth hardd a wneuthum", "dafydd-ap-gwilym"), ("Rules that outlasted me", "Rheolau a barhaodd ar fy ôl", "hywel-dda")]),
 ("Your greatest strength?", "Eich cryfder mwyaf?",
  [("Vision", "Gweledigaeth", "owain-glyndwr"), ("Patience", "Amynedd", "hywel-dda"), ("Courage", "Dewrder", "gwenllian"), ("Stamina", "Dyfalbarhad", "betsi-cadwaladr")]),
 ("And your weakness?", "A’ch gwendid?",
  [("I aim too high", "Rwy’n anelu’n rhy uchel", "owain-glyndwr"), ("I cannot keep my opinions to myself", "Ni allaf gadw fy marn i mi fy hun", "aneurin-bevan"),
   ("I am easily distracted", "Mae’n hawdd tynnu fy sylw", "dafydd-ap-gwilym"), ("I cannot sit still", "Ni allaf eistedd yn llonydd", "betsi-cadwaladr")]),
 ("Pick a place.", "Dewiswch le.",
  [("A castle on a rock", "Castell ar graig", "owain-glyndwr"), ("A quiet abbey library", "Llyfrgell abaty dawel", "hywel-dda"),
   ("A battlefield at dawn", "Maes y gad gyda’r wawr", "gwenllian"), ("The deck of a ship", "Bwrdd llong", "betsi-cadwaladr")]),
]


# ---------- proud history (src/pride.py, src/pride2.py) ----------
import pride as _P, pride2 as _P2
_ar = [x for x in LEGENDS if x["id"] == "arthur"][0]
LEGENDS = [x for x in LEGENDS if x["id"] != "arthur"]
# more legends (src/legends2.py); the Legends page is grouped into sections and LEGENDS follows that order
import legends2 as _L2
_LBY = {x["id"]: x for x in LEGENDS + _L2.LEGENDS}
_ids = [i for g in _L2.GROUPS for i in g["ids"]]
assert sorted(_ids) == sorted(_LBY), (sorted(set(_LBY) - set(_ids)), sorted(set(_ids) - set(_LBY)))
LEGEND_GROUPS = [dict(g, items=[_LBY[i] for i in g["ids"]]) for g in _L2.GROUPS]
LEGENDS = [_LBY[i] for i in _ids]
LEGENDS_HOME = [_LBY[i] for i in ("dragons", "gelert", "cantre", "llynyfan")]
_arthur = dict(_P.ARTHUR, pEn=_P.ARTHUR["pEn"] + _ar["pEn"] + _P.ARTHUR["endEn"], pCy=_P.ARTHUR["pCy"] + _ar["pCy"] + _P.ARTHUR["endCy"])
for _s in STORIES:
    if _s["id"] == "language":
        _s["pEn"] = _s["pEn"][:1] + _P.LATIN_EN + _s["pEn"][1:]
        _s["pCy"] = _s["pCy"][:1] + _P.LATIN_CY + _s["pCy"][1:]
        for _a, _b in _P.LANG_FIX:
            assert any(_a in t for t in _s["pEn"] + _s["pCy"]), _a
            _s["pEn"] = [t.replace(_a, _b) for t in _s["pEn"]]
            _s["pCy"] = [t.replace(_a, _b) for t in _s["pCy"]]
        _s["mins"] = 8
import pride3 as _P3
import iolo as _IO  # Iolo Morganwg long read (src/iolo.py)
import wilson_blackett as _WB  # Alan Wilson and Baram Blackett long read (src/wilson_blackett.py)
import brutus as _BR  # Brutus of Troy and the Britons long read (src/brutus.py)
import celts as _CE  # Britons, not Celts: Edward Lhuyd and the name 'Celtic' (src/celts.py)
import madog as _MD  # Prince Madog's voyage to America and the Welsh Indians (src/madog.py)
import caradog as _CR  # King Caradog (Caratacus) against Rome, and his family in Rome (src/caradog.py)
import patrick as _PT  # Saint Patrick, the Briton from Wales (src/patrick.py)
import christianity as _CH  # The coming of Christianity: the first Christians, Joseph, Lucius, Brân (src/christianity.py)
import macsen as _MX  # Macsen Wledig, the emperor from Britain (src/macsen.py)
import nest as _NS  # Nest ferch Rhys, princess of Deheubarth (src/nest.py)
import rhys as _RH  # Prince Rhys ap Gruffudd, the Lord Rhys (src/rhys.py)
import aberfan as _AF  # The Aberfan disaster, 21 October 1966 (src/aberfan.py)
import mac as _MAC  # MAC and the Free Wales Army (src/mac.py)
import tryweryn as _TW  # Cofiwch Dryweryn: the drowning of Capel Celyn (src/tryweryn.py)
import industry as _IN  # How Wales moved the world: the industrial revolution (src/industry.py)
import writers as _WRT  # The writers who recorded early Wales (src/writers.py)
import welshnot as _WN  # The Welsh Not and how they tried to wipe out the language (src/welshnot.py)
STORIES = STORIES + [_arthur, _P.GLYNDWR] + _P2.STORIES + _P3.STORIES + [_IO.STORY, _WB.STORY, _BR.STORY, _CE.STORY, _MD.STORY, _CR.STORY, _MX.STORY, _NS.STORY, _RH.STORY] + _CH.STORIES + [_PT.STORY, _AF.STORY, _TW.STORY] + _MAC.STORIES + [_WN.STORY] + [_IN.STORY] + [_WRT.STORY]
# the long reads on the language and on protest point on to the Welsh Not long read (src/welshnot.py)
for _s in STORIES:
    if _s["id"] in ("language", "revival", "protest"):
        _s["links"] = _s.get("links", []) + [("story-welsh-not.html", "The Welsh Not: how they tried to wipe out our language", "Y Welsh Not: sut y ceisiwyd difa ein hiaith")]
for _s in STORIES:  # the industrial revolution long read, linked from the long reads beside it
    if _s["id"] in ("coal", "firsts", "world", "protest"):
        _s["links"] = [("story-industry.html", "How Wales moved the world: the industrial revolution", "Sut y symudodd Cymru’r byd: y chwyldro diwydiannol")] + _s.get("links", [])
