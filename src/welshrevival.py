# Yma o Hyd: how the Welsh language came back (story-welsh-revival.html).
# features.py adds STORY to the long reads. build.py puts the census chart in at "!! chart" (revival_chart()).
# Asked for by Ifan, 13 November 2026, from the home page chart "A century of decline, and a fight back": "Make this
# clickable and have a page on the language making a revival". The home chart card is now one link to this page.
# Told from the revival's side: the people and the campaigns that brought Welsh back. It goes on from the Welsh Not
# long read (src/welshnot.py), which tells how the state tried to push the language out; keep the two from repeating
# each other at length. Nothing negative about Welsh figures (EDITORIAL.md).
# Sources opened and read November 2026 (each is a wr-* entry in src/cites.py):
# - Census: ONS, "Welsh language, Wales: Census 2021" (538,000, 17.8%; 2011 562,000, 19.0%); Amgueddfa Cymru,
#   "The Welsh language today" (2001: first rise for over a century, 508,000 / 18.7% in 1991 to 582,000 / 20.8%,
#   credited to Welsh-medium schools and adult learners). Annual Population Survey, year to June 2026: 27.4%,
#   about 845,200; ages 3 to 15 48.3%. The Welsh Government says the survey is not to be compared with the census,
#   so the text gives it as a separate, yearly survey and never sets the two side by side as a trend.
# - Schools: Wikipedia, Ysgol Gymraeg Aberystwyth (1939, private, seven pupils, Norah Isaac first head); Ysgol Gymraeg
#   Dewi Sant, Llanelli (1 March 1947, first Welsh-medium school run by a local authority); Ysgol Glan Clwyd (1956,
#   first Welsh-medium secondary school in Wales, Rhyl, moved to St Asaph 1969); Mudiad Meithrin (1971, over 650
#   groups by 1996). Dictionary of Welsh Biography, Sir Ifan ab Owen Edwards (Cymru'r Plant letter January 1922,
#   camp at Llanuwchllyn 1928, Llangrannog 1932, Urdd eisteddfod 1929, the Welsh school at Aberystwyth 1939).
#   wales.com on the Urdd (more than 55,000 members; Gwilym Davies's Message of Peace and Goodwill, 1922, 18 May).
# - Broadcasting: Wikipedia, BBC Radio Cymru (3 January 1977, an extended news bulletin first; Radio Cymru 2, 2018);
#   Timeline of S4C (1979 promises; the new government decides against; civil disobedience; October 1980 reversal
#   after, among other things, Gwynfor Evans's threat of a hunger strike; 1 November 1982 at 6pm; Newyddion, Pobol y Cwm).
# - The law: legislation.gov.uk, Welsh Language Act 1993 long title ("treated on a basis of equality", a Board);
#   Welsh Government, Welsh Language and Education (Wales) Act 2025 (passed 13 May 2025, Royal Assent 7 July 2025;
#   a million-speaker target in law; all pupils independent Welsh users by the end of school; a National Institute
#   for Learning Welsh). Cymraeg 2050 launch, gov.wales, 11 July 2017 (daily use 10% to 20%; Welsh-medium year groups
#   22% to 30% by 2031 and 40% by 2050; 150 more nursery groups).
# - Music: Wikipedia, Sain (1969, Cardiff, Dafydd Iwan, Huw Jones, Brian Morgan Edwards; studio near Llandwrog 1975);
#   Dafydd Iwan (prison 1970 over road-sign fines; Yma o Hyd 1983 with Ar Log; UK iTunes number one January 2020;
#   sung at Cardiff City Stadium before the 2022 World Cup play-offs; Wales's first World Cup since 1958);
#   Mwng (15 May 2000, number 11, first Welsh-language album in the top 20).
# - The web: National Library of Wales, Welsh Wikipedia reaches 100,000 articles (28 March 2018, founded 2003,
#   the most widely used Welsh-language website); Nominet, first .cymru and .wales sites live (launch 30 September 2014).
#   Nant Gwrtheyrn's own page on Dr Carl Clowes (founder, first chairman of the trust; died 4 December 2021).
# Paragraph codes (see prose() in build.py): "## Heading", "> Quote | Source", "|| Left | Right", "!! picture key".

_CC0 = ("CC0", "https://creativecommons.org/publicdomain/zero/1.0/")
_BYSA4 = ("CC BY-SA 4.0", "https://creativecommons.org/licenses/by-sa/4.0/")
_BYSA3 = ("CC BY-SA 3.0", "https://creativecommons.org/licenses/by-sa/3.0/")
_BY2 = ("CC BY 2.0", "https://creativecommons.org/licenses/by/2.0/")
_BYSA2 = ("CC BY-SA 2.0", "https://creativecommons.org/licenses/by-sa/2.0/")

# Pictures from Wikimedia Commons (found with tools/commons_research.py): file, maker, licence, licence link,
# caption EN, caption CY, width, height. "chart" is filled in by build.py (the census chart, revival_chart()).
FIGS = {
    "urdd": ("Bathodyn Yr Urdd (tua 1946).jpg", "MairEdwards", *_BYSA4,
             "An Urdd badge, sewn on a member’s blazer about 1946: the red dragon and the Urdd’s promise, ‘Er mwyn Cymru’, for the sake of Wales.",
             "Bathodyn yr Urdd a wnïwyd ar flaser aelod tua 1946: y ddraig goch ac addewid yr Urdd, ‘Er mwyn Cymru’.", 1023, 1017),
    "plaque": ("Llechan Plac - Memorial Plaque- Cymdeithas yr Iaith Protest.jpg", "Rupertmaesglas", *_CC0,
               "The slate plaque on Trefechan Bridge, Aberystwyth: ‘On this bridge Cymdeithas yr Iaith Gymraeg held its first non-violent protest for equality for the Welsh language. Saturday, 2 February 1963.’",
               "Y llechen ar Bont Trefechan, Aberystwyth: ‘Ar y bont hon cynhaliodd Cymdeithas yr Iaith Gymraeg ei phrotest ddi-drais gyntaf dros gydraddoldeb i’r iaith Gymraeg. Dydd Sadwrn, 2 Chwefror 1963.’", 4096, 3072),
    "chepstow": ("National Boundary - Wales sign - geograph.org.uk - 947469.jpg", "Roger, geograph.org.uk", *_BYSA2,
                 "Croeso i Gymru: the sign at the border on the bridge over the Wye at Chepstow, in both languages.",
                 "Croeso i Gymru: yr arwydd ar y ffin ar y bont dros afon Gwy yng Nghas-gwent, yn y ddwy iaith.", 640, 480),
    "nant": ("Awyrlun o Gwm Nant Gwrtheyrn Mai 2023, Gwynedd, Wales 02.jpg", "Llywelyn2000", *_BYSA4,
             "Nant Gwrtheyrn from the air, May 2023: the old quarry village under the cliffs of Llŷn, now the national centre for the Welsh language.",
             "Nant Gwrtheyrn o’r awyr, Mai 2023: hen bentref y chwarel dan glogwyni Llŷn, canolfan genedlaethol yr iaith Gymraeg heddiw.", 4032, 3024),
}

STORY = dict(id="welsh-revival", era="modern", art="book", mins=16, figs=FIGS,
  people=["ifan-ab-owen-edwards", "saunders-lewis", "eileen-beasley", "gwynfor-evans", "dafydd-iwan", "om-edwards"],
  events=["Tynged yr Iaith", "Protest at Trefechan Bridge", "Welsh Language Act", "Gwynfor and S4C", "S4C goes on air", "Welsh made official"],
  links=[("story-welsh-not.html", "The Welsh Not: how they tried to wipe out our language", "Y Welsh Not: sut y ceisiwyd difa ein hiaith"),
         ("story-revival.html", "Gwynfor, Plaid Cymru and the channel a fast won", "Gwynfor, Plaid Cymru a’r sianel a enillwyd drwy ympryd"),
         ("story-tryweryn.html", "Cofiwch Dryweryn: the drowning of Capel Celyn", "Cofiwch Dryweryn: boddi Capel Celyn"),
         ("story-language.html", "How the Welsh language survived", "Sut y goroesodd y Gymraeg"),
         ("person-saunders-lewis.html", "Saunders Lewis", "Saunders Lewis"),
         ("person-gwynfor-evans.html", "Gwynfor Evans", "Gwynfor Evans"),
         ("person-dafydd-iwan.html", "Dafydd Iwan", "Dafydd Iwan"),
         ("person-ifan-ab-owen-edwards.html", "Sir Ifan ab Owen Edwards", "Syr Ifan ab Owen Edwards"),
         ("topic-language.html", "The Welsh language: a guide", "Yr iaith Gymraeg: canllaw"),
         ("welsh.html", "Learn Welsh: beginner’s phrases", "Dysgu Cymraeg: ymadroddion i ddechreuwyr")],
  en="Yma o Hyd: how the Welsh language came back",
  cy="Yma o Hyd: sut y daeth y Gymraeg yn ôl",
  sumEn="In 1962 Saunders Lewis warned that Welsh would be dead by the new century. Instead a school of seven children, a youth movement, a protest on a bridge, a fast, a television channel, a song and a whole people turned the tide. This is the story of the fight back.",
  sumCy="Yn 1962 rhybuddiodd Saunders Lewis y byddai’r Gymraeg wedi marw erbyn y ganrif newydd. Yn hytrach, trodd ysgol o saith o blant, mudiad ieuenctid, protest ar bont, ympryd, sianel deledu, cân a chenedl gyfan y llanw. Dyma stori’r frwydr yn ôl.",
  pEn=[
   "In February 1962 the writer Saunders Lewis told the people of Wales, over the radio, that their language would be dead as a living tongue by about the beginning of the twenty-first century unless they fought for it.[[cite:wn-tynged]] The twenty-first century came. Welsh did not die. It is the official language of Wales, spoken in the Senedd and the courts, taught in Welsh-medium schools in every county, on the air every day on S4C and Radio Cymru, and sung by the whole nation at the football matches. This is the story of how it came back, and of the people who brought it back.",
   "|| 1922 | Ifan ab Owen Edwards founds Urdd Gobaith Cymru",
   "|| 1939 | Ysgol Gymraeg Aberystwyth opens with seven pupils",
   "|| 1947 | Ysgol Dewi Sant, Llanelli: the first Welsh-medium school run by a council",
   "|| 1956 | Ysgol Glan Clwyd, the first Welsh-medium secondary school",
   "|| 1962 | Tynged yr Iaith, and the birth of Cymdeithas yr Iaith",
   "|| 1963 | The sit-down on Trefechan Bridge",
   "|| 1967 | The first Welsh Language Act",
   "|| 1969 | Sain records is founded",
   "|| 1971 | Mudiad Ysgolion Meithrin, the Welsh nursery movement",
   "|| 1977 | Radio Cymru goes on the air",
   "|| 1982 | S4C goes on the air",
   "|| 1993 | Welsh and English to be treated on a basis of equality",
   "|| 2001 | The census counts more Welsh speakers, the first rise for over a century",
   "|| 2011 | Welsh has official status in Wales",
   "|| 2017 | Cymraeg 2050: the aim of a million speakers",
   "|| 2025 | The million-speaker target is written into law",
   "## The long fall",
   "When the first census asked about the language, in 1891, just over half the people of Wales spoke Welsh. Seventy years later only a quarter did, and by 1981 fewer than one in five. Behind those numbers lay the Welsh Not and the Blue Books, schools that taught only in English, the flood of new people into the coalfield, two world wars, and a radio and a cinema that spoke only English. Many parents who spoke Welsh themselves did not pass it on to their children, because they had been taught that English was the road to getting on.",
   "!! chart",
   "But look again at the right-hand end of the line. The fall slows in the 1980s, stops, and in 2001 turns up for the first time in more than a century. That turn was not luck. It was the work of a few stubborn people who would not let the language go, and of tens of thousands who followed them.",
   "## A youth movement and a school of seven",
   "It began with the children. In January 1922 Ifan ab Owen Edwards, son of Sir O. M. Edwards, wrote a letter in his father’s magazine for children, Cymru’r Plant, asking the young people of Wales to join a new movement for their language and their country. That letter founded Urdd Gobaith Cymru.[[cite:wr-ifan-dwb]] He held the first Urdd camp at Llanuwchllyn in 1928, began the Urdd Eisteddfod in 1929 and opened the camp at Llangrannog in 1932. The same year, 1922, the Reverend Gwilym Davies sent out the first Urdd Message of Peace and Goodwill from the children of Wales to the children of the world, and it has gone out every 18 May since. Within five years the Urdd had 5,000 members. Today it has more than 55,000.[[cite:wr-urdd]]",
   "!! urdd",
   "Then Ifan ab Owen Edwards did something bolder. In 1939 he opened a small private school in Aberystwyth where every lesson was in Welsh. Ysgol Gymraeg Aberystwyth began with seven pupils, and its first head was the young teacher and dramatist Norah Isaac.[[cite:wr-ysgolgymraeg,wr-ifan-dwb]] It was the first Welsh-medium school in Wales, and everything that followed grew from it.",
   "On St David’s Day, 1 March 1947, Ysgol Dewi Sant opened in Llanelli, the first Welsh-medium school to be run by a local council.[[cite:wr-dewisant]] In 1956 Ysgol Glan Clwyd opened in Rhyl as the first Welsh-medium secondary school in Wales; it moved to St Asaph in 1969.[[cite:wr-glanclwyd]] Rhydfelen followed in the south in 1962. Many of the first families to choose these schools did not speak Welsh at home. They wanted their children to have what had been taken from them.",
   "In 1971 Mudiad Ysgolion Meithrin was formed to set up Welsh-medium playgroups for the very young, so that a child could be speaking Welsh before starting school. By 1996 more than 650 groups were running across Wales.[[cite:wr-meithrin]] Today the Cylch Meithrin, the Welsh nursery in the chapel vestry or the village hall, is where many thousands of children hear their first words of Cymraeg.",
   "## Tynged yr Iaith",
   "In Llangennech, near Llanelli, a miner, Trefor Beasley, and his wife Eileen, a teacher, had refused from 1952 to pay their rates until the council sent them a bill in Welsh. The bailiffs took their furniture again and again. In 1960 the council gave way.[[cite:wn-beasley]] Saunders Lewis held up the Beasleys as the example to follow in his BBC radio lecture of 13 February 1962, Tynged yr Iaith, the Fate of the Language. The language could be saved, he said, only by making it impossible for local and central government to carry on their business without Welsh.[[cite:wn-tynged,wn-beasley]]",
   "## Cymdeithas yr Iaith",
   "Wales listened. That summer, on 4 August 1962 at Pontarddulais, young people founded Cymdeithas yr Iaith Gymraeg, the Welsh Language Society. On 2 February 1963 about seventy of them sat down on Trefechan Bridge in Aberystwyth and stopped the traffic for half an hour. It was the first of thousands of peaceful protests.[[cite:wn-cymdeithas]]",
   "!! plaque",
   "They asked for Welsh on tax discs, forms and summonses, and when it was refused they went to court rather than give in. They painted out English-only road signs, and in 1970 the singer Dafydd Iwan was sent to prison for refusing to pay the fines.[[cite:wr-iwan]] More than a thousand people have stood in court for the Society’s campaigns.[[cite:wn-cymdeithas]] They won. The road signs of Wales now speak both languages, from Holyhead to Chepstow, and every visitor who crosses the border sees at once that this is a country with its own tongue.",
   "!! chepstow",
   "## Equal in law",
   "The law began to move. The Welsh Language Act of 1967 gave Welsh ‘equal validity’ with English and let anyone use it in any court in Wales.[[cite:wn-act1967]] The Welsh Language Act of 1993 went further: in the business of public bodies and the courts in Wales, the English and Welsh languages were to be treated on a basis of equality, and a Welsh Language Board was set up to promote the language.[[cite:wr-act1993]]",
   "In 2011 came the words that every campaigner since the Beasleys had worked for:",
   "> The Welsh language has official status in Wales. | Welsh Language (Wales) Measure 2011, section 1",
   "The Measure made a Welsh Language Commissioner to make sure that public bodies keep their duties to Welsh speakers.[[cite:wn-measure]] And in 2025 the Senedd passed the Welsh Language and Education (Wales) Act. It writes into law the target of at least a million Welsh speakers by 2050, aims for every pupil in Wales to leave school able to use Welsh independently, and creates a National Institute for Learning Welsh for people of every age.[[cite:wr-act2025]]",
   "## On the air",
   "For years radio and television were the language’s greatest enemy: English came into every home, every evening. Wales won the airwaves back. BBC Radio Cymru began on 3 January 1977, opening with an extended news bulletin, and a second station, Radio Cymru 2, followed in 2018.[[cite:wr-radiocymru]]",
   "Television was harder won. At the election of 1979 both main parties promised a Welsh-language fourth channel. Within months the new government decided against it. Wales answered with civil disobedience: people refused to pay their licence fees and sat in at BBC and HTV studios. Then Gwynfor Evans, Plaid Cymru’s first member of Parliament, said that he would fast unto death unless the promise was kept. In 1980 the government gave way.[[cite:wr-s4c]] At six o’clock in the evening of 1 November 1982, Sianel Pedwar Cymru, S4C, went on the air, with Newyddion for the news and Pobol y Cwm, which had moved over from BBC Wales.[[cite:wr-s4c]] The first night’s preview brought the children of Wales a new hero, SuperTed.[[cite:wr-s4c-launch]]",
   "## Yma o hyd",
   "Music carried the language to the young. In 1969 Dafydd Iwan, Huw Jones and Brian Morgan Edwards founded Sain, a record company for Welsh music, first in Cardiff and then near Caernarfon, where they opened their studio near Llandwrog in 1975.[[cite:wr-sain]] Protest songs, folk, rock and pop poured out of it.",
   "In 1983 Dafydd Iwan, with the band Ar Log, recorded Yma o Hyd, Still Here. It runs through the whole history of Wales, from Macsen Wledig leaving in 383 to the singer’s own day, and every chorus ends with the same defiance:",
   "> Er gwaetha pawb a phopeth, ry’n ni yma o hyd. | Dafydd Iwan, Yma o Hyd (1983): ‘In spite of everyone and everything, we are still here.’",
   "In January 2020 the song went to number one in the UK iTunes chart. In 2022 Dafydd Iwan sang it on the pitch at Cardiff City Stadium before the World Cup play-offs, with the team and the whole crowd singing with him, and Wales went to its first World Cup since 1958.[[cite:wr-iwan]] Two decades earlier, Super Furry Animals had taken their all-Welsh album Mwng to number 11 in the UK album charts in 2000, the first Welsh-language album ever to reach the top twenty.[[cite:wr-mwng]] Welsh had become cool.",
   "## The tide turns",
   "In 2001 the census brought the news the campaigners had waited for. For the first time in more than a century, both the number and the share of Welsh speakers had risen, from 508,000 (18.7 per cent) in 1991 to 582,000 (20.8 per cent). Amgueddfa Cymru put it down to two things: the success of Welsh-medium schools, and the adults who had set out to learn.[[cite:wr-census2001]] The young were leading the way: more of them spoke Welsh at each of the last three censuses.",
   "The census of 2021 counted 538,000 people in Wales aged three and over who can speak Welsh, 17.8 per cent.[[cite:wr-census2021]] The Welsh Government also asks every year, in its Annual Population Survey, and that survey finds far more. In the year to June 2026, 27.4 per cent of people said they could speak Welsh, about 845,000, and almost half of all children aged three to fifteen.[[cite:wr-aps]] Whichever count you take, more than half a million people in Wales speak the language that was to have been dead by now.",
   "## Learners, and Welsh on the web",
   "The revival is not only for those born to the language. Thousands of adults learn Welsh every year, in evening classes, on residential courses and online. At Nant Gwrtheyrn, an empty quarry village on the cliffs of Llŷn, the doctor Carl Clowes had a vision: to bring the village back to life as a national centre for the Welsh language. He founded the trust that did it, and today learners from all over the world come to the Nant to learn Welsh by the sea.[[cite:wr-nant]]",
   "!! nant",
   "The language that was kept out of the schoolroom now lives on the internet. Wicipedia, the Welsh Wikipedia, began in 2003 and passed 100,000 articles in March 2018, the most widely used Welsh-language website.[[cite:wr-wicipedia]] In 2014 Wales got web addresses of its own, .cymru and .wales, and the first sites went live that September.[[cite:wr-domain]] This site lives at one of them: historyofwales.cymru.",
   "## Cymraeg 2050",
   "On 11 July 2017 the Welsh Government set its course: a million Welsh speakers by 2050, and twice as many people using Welsh every day, from one in ten to one in five. To get there it set out to put more children in Welsh-medium education, from 22 per cent of each year group to 30 per cent by 2031 and 40 per cent by 2050, with 150 new Welsh nursery groups in the first ten years.[[cite:wr-2050]] Since 2025 the million is no longer only a hope. It is written into law.[[cite:wr-act2025]]",
   "## Still here",
   "In 1536 an Act of Parliament set out to root the language out. In 1847 a government report called it a vast drawback. In 1962 its greatest writer feared he was writing its obituary. Every one of them was wrong. The language of Aneirin and Taliesin, of Hywel Dda’s laws and William Morgan’s Bible, is the official language of Wales. It is spoken by children in schools that did not exist eighty years ago, on a television channel won by a man ready to give his life for it, on road signs painted over by young people who went to prison for them, and in a song that a whole stadium sings. Er gwaetha pawb a phopeth, mae’r Gymraeg yma o hyd.",
  ],
  pCy=[
   "Ym mis Chwefror 1962 dywedodd y llenor Saunders Lewis wrth bobl Cymru, ar y radio, y byddai eu hiaith wedi darfod fel iaith fyw tua dechrau’r unfed ganrif ar hugain oni bai eu bod yn ymladd drosti.[[cite:wn-tynged]] Daeth yr unfed ganrif ar hugain. Ni fu farw’r Gymraeg. Hi yw iaith swyddogol Cymru. Fe’i siaredir yn y Senedd ac yn y llysoedd, fe’i dysgir mewn ysgolion Cymraeg ym mhob sir, mae hi ar yr awyr bob dydd ar S4C a Radio Cymru, ac mae’r genedl gyfan yn ei chanu yn y gemau pêl-droed. Dyma stori sut y daeth hi’n ôl, a stori’r bobl a ddaeth â hi’n ôl.",
   "|| 1922 | Ifan ab Owen Edwards yn sefydlu Urdd Gobaith Cymru",
   "|| 1939 | Ysgol Gymraeg Aberystwyth yn agor gyda saith o ddisgyblion",
   "|| 1947 | Ysgol Dewi Sant, Llanelli: yr ysgol Gymraeg gyntaf i’w rhedeg gan gyngor",
   "|| 1956 | Ysgol Glan Clwyd, yr ysgol uwchradd Gymraeg gyntaf",
   "|| 1962 | Tynged yr Iaith, a geni Cymdeithas yr Iaith",
   "|| 1963 | Yr eistedd i lawr ar Bont Trefechan",
   "|| 1967 | Deddf yr Iaith Gymraeg gyntaf",
   "|| 1969 | Sefydlu cwmni recordiau Sain",
   "|| 1971 | Mudiad Ysgolion Meithrin",
   "|| 1977 | Radio Cymru yn mynd ar yr awyr",
   "|| 1982 | S4C yn mynd ar yr awyr",
   "|| 1993 | Trin y Gymraeg a’r Saesneg ar y sail eu bod yn gyfartal",
   "|| 2001 | Y cyfrifiad yn cyfrif mwy o siaradwyr Cymraeg, y cynnydd cyntaf ers dros ganrif",
   "|| 2011 | Statws swyddogol i’r Gymraeg yng Nghymru",
   "|| 2017 | Cymraeg 2050: y nod o filiwn o siaradwyr",
   "|| 2025 | Y targed o filiwn o siaradwyr yn dod yn rhan o’r gyfraith",
   "## Y cwymp hir",
   "Pan holodd y cyfrifiad am yr iaith am y tro cyntaf, yn 1891, roedd ychydig dros hanner pobl Cymru’n siarad Cymraeg. Saith deg mlynedd yn ddiweddarach dim ond chwarter oedd yn ei siarad, ac erbyn 1981 llai nag un o bob pump. Y tu ôl i’r ffigurau hynny roedd y Welsh Not a’r Llyfrau Gleision, ysgolion a ddysgai drwy’r Saesneg yn unig, y llif o bobl newydd i’r maes glo, dau ryfel byd, a radio a sinema a siaradai Saesneg yn unig. Ni throsglwyddodd llawer o rieni a siaradai Gymraeg eu hunain yr iaith i’w plant, am iddynt gael eu dysgu mai’r Saesneg oedd y ffordd i ddod ymlaen yn y byd.",
   "!! chart",
   "Ond edrychwch eto ar ben de’r llinell. Mae’r cwymp yn arafu yn yr 1980au, yn peidio, ac yn 2001 yn troi i fyny am y tro cyntaf ers dros ganrif. Nid lwc oedd y tro hwnnw. Gwaith ychydig o bobl benderfynol na fynnent ollwng yr iaith ydoedd, a’r degau o filoedd a’u dilynodd.",
   "## Mudiad ieuenctid ac ysgol o saith",
   "Gyda’r plant y dechreuodd. Ym mis Ionawr 1922 ysgrifennodd Ifan ab Owen Edwards, mab Syr O. M. Edwards, lythyr yng nghylchgrawn plant ei dad, Cymru’r Plant, yn gofyn i bobl ifanc Cymru ymuno â mudiad newydd dros eu hiaith a’u gwlad. Y llythyr hwnnw a sefydlodd Urdd Gobaith Cymru.[[cite:wr-ifan-dwb]] Cynhaliodd wersyll cyntaf yr Urdd yn Llanuwchllyn yn 1928, dechreuodd Eisteddfod yr Urdd yn 1929 ac agorodd y gwersyll yn Llangrannog yn 1932. Yr un flwyddyn, 1922, anfonodd y Parchedig Gwilym Davies Neges Heddwch ac Ewyllys Da gyntaf yr Urdd oddi wrth blant Cymru at blant y byd, ac mae hi wedi mynd allan bob 18 Mai byth oddi ar hynny. O fewn pum mlynedd roedd gan yr Urdd 5,000 o aelodau. Heddiw mae ganddi dros 55,000.[[cite:wr-urdd]]",
   "!! urdd",
   "Yna gwnaeth Ifan ab Owen Edwards rywbeth mwy beiddgar. Yn 1939 agorodd ysgol breifat fach yn Aberystwyth lle’r oedd pob gwers yn Gymraeg. Dechreuodd Ysgol Gymraeg Aberystwyth gyda saith o ddisgyblion, a’i phrifathrawes gyntaf oedd yr athrawes a’r ddramodydd ifanc Norah Isaac.[[cite:wr-ysgolgymraeg,wr-ifan-dwb]] Hon oedd yr ysgol Gymraeg gyntaf yng Nghymru, ac ohoni hi y tyfodd popeth a ddilynodd.",
   "Ar Ddydd Gŵyl Dewi, 1 Mawrth 1947, agorodd Ysgol Dewi Sant yn Llanelli, yr ysgol Gymraeg gyntaf i’w rhedeg gan gyngor lleol.[[cite:wr-dewisant]] Yn 1956 agorodd Ysgol Glan Clwyd yn y Rhyl, yr ysgol uwchradd Gymraeg gyntaf yng Nghymru; symudodd i Lanelwy yn 1969.[[cite:wr-glanclwyd]] Dilynodd Rhydfelen yn y de yn 1962. Nid oedd llawer o’r teuluoedd cyntaf a ddewisodd yr ysgolion hyn yn siarad Cymraeg gartref. Roeddent am i’w plant gael yr hyn a gymerwyd oddi arnynt hwy.",
   "Yn 1971 ffurfiwyd Mudiad Ysgolion Meithrin i sefydlu cylchoedd chwarae Cymraeg i’r rhai bach, er mwyn i blentyn fod yn siarad Cymraeg cyn dechrau’r ysgol. Erbyn 1996 roedd dros 650 o gylchoedd ar waith ledled Cymru.[[cite:wr-meithrin]] Heddiw y Cylch Meithrin, yn festri’r capel neu yn neuadd y pentref, yw’r lle y mae miloedd lawer o blant yn clywed eu geiriau Cymraeg cyntaf.",
   "## Tynged yr Iaith",
   "Yn Llangennech, ger Llanelli, roedd glöwr, Trefor Beasley, a’i wraig Eileen, athrawes, wedi gwrthod o 1952 ymlaen dalu eu trethi nes i’r cyngor anfon bil atynt yn Gymraeg. Dro ar ôl tro cariodd y beilïaid eu dodrefn i ffwrdd. Yn 1960 ildiodd y cyngor.[[cite:wn-beasley]] Cyfeiriodd Saunders Lewis at y Beasleys fel esiampl i’w dilyn yn ei ddarlith radio i’r BBC ar 13 Chwefror 1962, Tynged yr Iaith. Dim ond drwy ei gwneud yn amhosibl i lywodraeth leol a chanolog fynd ymlaen â’u busnes heb y Gymraeg, meddai, y gellid achub yr iaith.[[cite:wn-tynged,wn-beasley]]",
   "## Cymdeithas yr Iaith",
   "Gwrandawodd Cymru. Yr haf hwnnw, ar 4 Awst 1962 ym Mhontarddulais, sefydlodd pobl ifanc Gymdeithas yr Iaith Gymraeg. Ar 2 Chwefror 1963 eisteddodd tua saith deg ohonynt i lawr ar Bont Trefechan yn Aberystwyth gan atal y drafnidiaeth am hanner awr. Hon oedd y gyntaf o filoedd o brotestiadau heddychlon.[[cite:wn-cymdeithas]]",
   "!! plaque",
   "Gofynasant am y Gymraeg ar ddisgiau treth, ffurflenni a gwysion, a phan wrthodwyd hynny aethant i’r llys yn hytrach nag ildio. Peintiasant dros arwyddion ffyrdd uniaith Saesneg, ac yn 1970 anfonwyd y canwr Dafydd Iwan i’r carchar am wrthod talu’r dirwyon.[[cite:wr-iwan]] Mae mwy na mil o bobl wedi sefyll yn y llys dros ymgyrchoedd y Gymdeithas.[[cite:wn-cymdeithas]] Enillwyd y frwydr. Mae arwyddion ffyrdd Cymru’n siarad y ddwy iaith heddiw, o Gaergybi i Gas-gwent, ac mae pob ymwelydd sy’n croesi’r ffin yn gweld ar unwaith mai gwlad â’i hiaith ei hun yw hon.",
   "!! chepstow",
   "## Yn gyfartal yn y gyfraith",
   "Dechreuodd y gyfraith symud. Rhoddodd Deddf yr Iaith Gymraeg 1967 ‘ddilysrwydd cyfartal’ i’r Gymraeg â’r Saesneg, a chaniatáu i unrhyw un ei defnyddio mewn unrhyw lys yng Nghymru.[[cite:wn-act1967]] Aeth Deddf yr Iaith Gymraeg 1993 ymhellach: ym musnes cyrff cyhoeddus a’r llysoedd yng Nghymru, roedd y Saesneg a’r Gymraeg i’w trin ar y sail eu bod yn gyfartal, a sefydlwyd Bwrdd yr Iaith Gymraeg i hybu’r iaith.[[cite:wr-act1993]]",
   "Yn 2011 daeth y geiriau y bu pob ymgyrchydd er dyddiau’r Beasleys yn gweithio amdanynt:",
   "> Mae statws swyddogol i’r Gymraeg yng Nghymru. | Mesur y Gymraeg (Cymru) 2011, adran 1",
   "Creodd y Mesur Gomisiynydd y Gymraeg i sicrhau bod cyrff cyhoeddus yn cyflawni eu dyletswyddau i siaradwyr Cymraeg.[[cite:wn-measure]] Ac yn 2025 pasiodd y Senedd Ddeddf y Gymraeg ac Addysg (Cymru). Mae’n gosod yn y gyfraith y targed o o leiaf filiwn o siaradwyr Cymraeg erbyn 2050, yn anelu at sicrhau bod pob disgybl yng Nghymru yn gadael yr ysgol yn gallu defnyddio’r Gymraeg yn annibynnol, ac yn creu Athrofa Dysgu Cymraeg Genedlaethol i bobl o bob oed.[[cite:wr-act2025]]",
   "## Ar yr awyr",
   "Am flynyddoedd radio a theledu oedd gelyn pennaf yr iaith: deuai’r Saesneg i bob cartref, bob nos. Enillodd Cymru’r tonfeddi’n ôl. Dechreuodd BBC Radio Cymru ar 3 Ionawr 1977, gyda bwletin newyddion estynedig, a dilynodd ail orsaf, Radio Cymru 2, yn 2018.[[cite:wr-radiocymru]]",
   "Anos oedd ennill y teledu. Yn etholiad 1979 addawodd y ddwy brif blaid bedwaredd sianel Gymraeg. O fewn misoedd penderfynodd y llywodraeth newydd yn ei herbyn. Atebodd Cymru ag anufudd-dod sifil: gwrthododd pobl dalu am eu trwyddedau teledu a chynnal protestiadau eistedd i mewn yn stiwdios y BBC a HTV. Yna dywedodd Gwynfor Evans, Aelod Seneddol cyntaf Plaid Cymru, y byddai’n ymprydio hyd angau oni chedwid yr addewid. Yn 1980 ildiodd y llywodraeth.[[cite:wr-s4c]] Am chwech o’r gloch nos 1 Tachwedd 1982 aeth Sianel Pedwar Cymru, S4C, ar yr awyr, gyda Newyddion a Pobol y Cwm, a symudodd draw o BBC Cymru.[[cite:wr-s4c]] Daeth rhaglen ragflas y noson gyntaf ag arwr newydd i blant Cymru, SuperTed.[[cite:wr-s4c-launch]]",
   "## Yma o hyd",
   "Cariodd cerddoriaeth yr iaith at yr ifanc. Yn 1969 sefydlodd Dafydd Iwan, Huw Jones a Brian Morgan Edwards Sain, cwmni recordiau i gerddoriaeth Gymraeg, yng Nghaerdydd i ddechrau ac yna ger Caernarfon, lle’r agorwyd eu stiwdio ger Llandwrog yn 1975.[[cite:wr-sain]] Llifodd caneuon protest, canu gwerin, roc a phop ohoni.",
   "Yn 1983 recordiodd Dafydd Iwan, gyda’r grŵp Ar Log, Yma o Hyd. Mae’n rhedeg drwy holl hanes Cymru, o Facsen Wledig yn gadael yn 383 hyd ddyddiau’r canwr ei hun, ac mae pob cytgan yn gorffen â’r un her:",
   "> Er gwaetha pawb a phopeth, ry’n ni yma o hyd. | Dafydd Iwan, Yma o Hyd (1983)",
   "Ym mis Ionawr 2020 aeth y gân i rif un yn siart iTunes y Deyrnas Unedig. Yn 2022 canodd Dafydd Iwan hi ar y cae yn Stadiwm Dinas Caerdydd cyn gemau ail gyfle Cwpan y Byd, gyda’r tîm a’r dorf gyfan yn canu gydag ef, ac aeth Cymru i’w Chwpan y Byd cyntaf ers 1958.[[cite:wr-iwan]] Ddau ddegawd ynghynt roedd y Super Furry Animals wedi mynd â’u halbwm Cymraeg, Mwng, i rif 11 yn siart albymau’r Deyrnas Unedig yn 2000, yr albwm Cymraeg cyntaf erioed i gyrraedd yr ugain uchaf.[[cite:wr-mwng]] Roedd y Gymraeg wedi mynd yn cŵl.",
   "## Y llanw’n troi",
   "Yn 2001 daeth y cyfrifiad â’r newyddion y bu’r ymgyrchwyr yn aros amdanynt. Am y tro cyntaf ers dros ganrif roedd nifer a chyfran y siaradwyr Cymraeg wedi codi, o 508,000 (18.7 y cant) yn 1991 i 582,000 (20.8 y cant). Rhoddodd Amgueddfa Cymru y clod i ddau beth: llwyddiant yr ysgolion Cymraeg, a’r oedolion a aeth ati i ddysgu.[[cite:wr-census2001]] Yr ifanc oedd yn arwain y ffordd: roedd mwy ohonynt yn siarad Cymraeg ym mhob un o’r tri chyfrifiad diwethaf.",
   "Cyfrifodd cyfrifiad 2021 538,000 o bobl yng Nghymru, yn dair oed a hŷn, sy’n gallu siarad Cymraeg, 17.8 y cant.[[cite:wr-census2021]] Mae Llywodraeth Cymru hefyd yn holi bob blwyddyn, yn yr Arolwg Blynyddol o’r Boblogaeth, ac mae’r arolwg hwnnw’n cael llawer mwy. Yn y flwyddyn hyd fis Mehefin 2026 dywedodd 27.4 y cant o bobl eu bod yn gallu siarad Cymraeg, tua 845,000, a bron hanner yr holl blant rhwng tair a phymtheg oed.[[cite:wr-aps]] Pa gyfrif bynnag a gymerwch, mae mwy na hanner miliwn o bobl yng Nghymru’n siarad yr iaith a ddylai fod wedi marw erbyn hyn.",
   "## Dysgwyr, a’r Gymraeg ar y we",
   "Nid i’r rhai a aned iddi yn unig y mae’r adfywiad. Mae miloedd o oedolion yn dysgu Cymraeg bob blwyddyn, mewn dosbarthiadau nos, ar gyrsiau preswyl ac ar-lein. Yn Nant Gwrtheyrn, pentref chwarel gwag ar glogwyni Llŷn, cafodd y meddyg Carl Clowes weledigaeth: dod â’r pentref yn ôl yn fyw fel canolfan genedlaethol i’r iaith Gymraeg. Sefydlodd yr ymddiriedolaeth a wnaeth hynny, a heddiw daw dysgwyr o bob cwr o’r byd i’r Nant i ddysgu Cymraeg ar lan y môr.[[cite:wr-nant]]",
   "!! nant",
   "Mae’r iaith a gadwyd allan o’r ystafell ddosbarth yn byw ar y rhyngrwyd bellach. Dechreuodd Wicipedia, y Wikipedia Cymraeg, yn 2003 a phasio 100,000 o erthyglau ym mis Mawrth 2018, y wefan Gymraeg a ddefnyddir fwyaf.[[cite:wr-wicipedia]] Yn 2014 cafodd Cymru ei chyfeiriadau gwe ei hun, .cymru a .wales, ac aeth y gwefannau cyntaf yn fyw y mis Medi hwnnw.[[cite:wr-domain]] Mae’r wefan hon yn byw ar un ohonynt: historyofwales.cymru.",
   "## Cymraeg 2050",
   "Ar 11 Gorffennaf 2017 gosododd Llywodraeth Cymru ei chwrs: miliwn o siaradwyr Cymraeg erbyn 2050, a dwywaith cymaint o bobl yn defnyddio’r Gymraeg bob dydd, o un o bob deg i un o bob pump. I gyrraedd yno aeth ati i roi mwy o blant mewn addysg Gymraeg, o 22 y cant o bob grŵp blwyddyn i 30 y cant erbyn 2031 a 40 y cant erbyn 2050, gyda 150 o gylchoedd meithrin newydd yn y deng mlynedd cyntaf.[[cite:wr-2050]] Er 2025 nid gobaith yn unig yw’r miliwn. Mae wedi’i ysgrifennu yn y gyfraith.[[cite:wr-act2025]]",
   "## Yma o hyd",
   "Yn 1536 aeth Deddf Seneddol ati i ddiwreiddio’r iaith. Yn 1847 galwodd adroddiad gan y llywodraeth hi’n anfantais enfawr. Yn 1962 ofnai ei llenor mwyaf ei fod yn ysgrifennu ei marwnad. Roedd pob un ohonynt yn anghywir. Iaith Aneirin a Thaliesin, cyfreithiau Hywel Dda a Beibl William Morgan, yw iaith swyddogol Cymru. Fe’i siaredir gan blant mewn ysgolion nad oeddent yn bod wyth deg mlynedd yn ôl, ar sianel deledu a enillwyd gan ŵr a oedd yn barod i roi ei fywyd drosti, ar arwyddion ffyrdd y bu pobl ifanc yn y carchar am beintio drostynt, ac mewn cân y mae stadiwm cyfan yn ei chanu. Er gwaetha pawb a phopeth, mae’r Gymraeg yma o hyd.",
  ],
)
