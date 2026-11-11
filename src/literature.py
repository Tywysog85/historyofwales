# The literature of Wales: the hub page (literature.html), the great books (books.html) and the Welsh Triads (triads.html).
# Built by literature_pages() in build.py. House rules (EDITORIAL.md): proud voice, nothing negative about the people of
# Welsh history, Arthur is a king (never "myth" or "legend"), Iolo Morganwg is never called a forger.
# Text markers (see prose() in build.py): "## " heading, "> quote | source" pull quote, "|| left | right" fact row.

# ---------------------------------------------------------------- the hub
HUB_EN = [
 "Welsh literature is one of the oldest in Europe. Its first poems were sung about the year 600, before the first poem was made in English, and they can still be read in the language they were made in. For fourteen centuries the line has never broken: from the poets of the Old North to the princes’ bards, from Dafydd ap Gwilym to William Morgan’s Bible, from the hymns of Pantycelyn to the chair poems of the National Eisteddfod today.",
 "It survived because Wales honoured its poets. The law of Hywel Dda gave the chief poet a seat beside the prince. Families paid scribes to copy the old poems onto calfskin. Printers, preachers and teachers put books into every home. Most of all, ordinary people learned the poems by heart and passed them on.",
]
HUB_CY = [
 "Mae llenyddiaeth Gymraeg ymhlith yr hynaf yn Ewrop. Canwyd ei cherddi cyntaf tua’r flwyddyn 600, cyn llunio’r gerdd gyntaf yn Saesneg, a gellir eu darllen o hyd yn yr iaith y’u lluniwyd ynddi. Am bedair canrif ar ddeg ni thorrodd yr edau: o feirdd yr Hen Ogledd i feirdd y tywysogion, o Ddafydd ap Gwilym i Feibl William Morgan, o emynau Pantycelyn i gerddi’r gadair yn yr Eisteddfod Genedlaethol heddiw.",
 "Goroesodd am fod Cymru’n parchu ei beirdd. Rhoddodd cyfraith Hywel Dda sedd i’r pencerdd wrth ochr y tywysog. Talodd teuluoedd i gopïwyr gopïo’r hen gerddi ar femrwn. Rhoddodd argraffwyr, pregethwyr ac athrawon lyfrau ym mhob cartref. Yn fwy na dim, dysgodd pobl gyffredin y cerddi ar eu cof a’u trosglwyddo.",
]

# Doors to the other pages: link, title EN, CY, line EN, CY, gallery picture id
DOORS = [
 ("triads.html", "The Welsh Triads", "Trioedd Ynys Prydain", "The memory of the Island of Britain, kept in threes.", "Cof Ynys Prydain, wedi’i gadw fesul tri.", "trea-red-book"),
 ("books.html", "The great books of Wales", "Llyfrau mawr Cymru", "The Black Book, the Red Book, the Books of Aneirin and Taliesin, and the Bible of 1588.", "Y Llyfr Du, y Llyfr Coch, Llyfrau Aneirin a Thaliesin, a Beibl 1588.", "trea-black-book"),
 ("mabinogion.html", "The Mabinogion", "Y Mabinogion", "Eleven great tales of medieval Wales.", "Un chwedl fawr ar ddeg o Gymru’r Oesoedd Canol.", "trea-book-taliesin"),
 ("laws.html", "The Laws of Hywel Dda", "Cyfraith Hywel Dda", "The law books of Wales, and the place of the poet in them.", "Llyfrau cyfraith Cymru, a lle’r bardd ynddynt.", "trea-laws-hywel"),
]

# The ages of Welsh literature. pic = gallery id (src/gallery_photos.py); people = person pages on this site.
AGES = [
 dict(id="cynfeirdd", era="saints", span="c. 550–1100", spanCy="tua 550–1100", en="The first poets", cy="Y Cynfeirdd", pic="trea-book-aneirin",
  people=["taliesin", "aneirin"],
  pEn=[
   "The story begins in the Old North, Yr Hen Ogledd: the British kingdoms that reached from the Clyde to the Pennines, when the forerunner of Welsh was spoken from Edinburgh to Cornwall. There, about the year 600, two poets made verse that is still read today. Taliesin was the poet of Urien, king of Rheged. Aneirin was the poet of the Gododdin, whose stronghold was Din Eidyn, the fortress that is now Edinburgh.",
   "A history gathered in Gwynedd about 829, the Historia Brittonum, names the great poets of that age: Talhaearn Tad Awen, Aneirin, Taliesin, Blwchfardd and Cian, who ‘were famous at the same time in British verse’. The poems of the other three are lost. Those of Aneirin and Taliesin were carried south to Wales, sung and copied for seven centuries, and written at last into the Book of Aneirin and the Book of Taliesin.",
   "Y Gododdin remembers the war band of Mynyddog Mwynfawr, who feasted in his hall for a year and then rode to Catraeth, Catterick, where almost all of them fell. Each verse honours one warrior. Of one of them, Gwawrddur, the poet says that he fed the black ravens on the rampart of the fort, ‘though he was not Arthur’: one of the earliest mentions of Arthur’s name anywhere.",
   "Taliesin praised Urien as the generous lord of Rheged and the shield of his people in battle, and mourned his son Owain. Several of his poems end with the same promise: until he grew old and died, he would never be happy unless he praised Urien.",
   "Then came the poets of Wales itself. From the ninth and tenth centuries come the englynion of Llywarch Hen and his sons, and the voice of Heledd, princess of Powys, mourning her brother Cynddylan and his burned hall at Pengwern. From the same years comes Armes Prydein, the Prophecy of Britain, which foretold that the Cymry would join with the Irish, the Cornish, the Bretons and the men of the North under Cynan and Cadwaladr, and win back the Island of Britain.",
   "The oldest Welsh poetry written down that still survives is a group of twelve englynion in the margins of a ninth-century Latin book, the Juvencus manuscript, now in Cambridge.",
   "> Gwŷr a aeth Gatraeth oedd ffraeth eu llu, glasfedd eu hancwyn, a gwenwyn fu. — Men went to Catraeth, swift was their host; fresh mead was their feast, and it was bitter. | Aneirin, Y Gododdin",
   "> Stafell Gynddylan ys tywyll heno, heb dân, heb wely. — The hall of Cynddylan is dark tonight, without fire, without bed. | Canu Heledd, ninth or tenth century",
   "## A lullaby fourteen hundred years old",
   "Hidden among the warrior verses of the Book of Aneirin is a little song a mother sings to her child, Dinogad. It tells him of his speckled smock of marten skins, and of his father, who went hunting with his spear and his dogs and never came home without a roebuck, a boar, a stag, a grouse from the mountain or a fish from the falls of Derwennydd. It is one of the oldest lullabies in any language of Europe.",
  ],
  pCy=[
   "Mae’r stori’n dechrau yn yr Hen Ogledd: y teyrnasoedd Brythonig a ymestynnai o afon Clud i’r Pennines, pan siaredid mamiaith y Gymraeg o Gaeredin i Gernyw. Yno, tua’r flwyddyn 600, lluniodd dau fardd gerddi a ddarllenir o hyd. Taliesin oedd bardd Urien, brenin Rheged. Aneirin oedd bardd y Gododdin, a’u caer oedd Din Eidyn, y gaer sydd heddiw’n Gaeredin.",
   "Mae hanes a gasglwyd yng Ngwynedd tua 829, yr Historia Brittonum, yn enwi beirdd mawr yr oes honno: Talhaearn Tad Awen, Aneirin, Taliesin, Blwchfardd a Chian, a oedd ‘yn enwog yr un pryd mewn barddoniaeth Frythoneg’. Collwyd cerddi’r tri arall. Cariwyd rhai Aneirin a Thaliesin i’r de i Gymru, eu canu a’u copïo am saith canrif, a’u hysgrifennu o’r diwedd yn Llyfr Aneirin a Llyfr Taliesin.",
   "Mae’r Gododdin yn cofio gosgordd Mynyddog Mwynfawr, a fu’n gwledda yn ei neuadd am flwyddyn cyn marchogaeth i Gatraeth, lle syrthiodd bron pob un ohonynt. Mae pob pennill yn anrhydeddu un rhyfelwr. Am un ohonynt, Gwawrddur, dywed y bardd iddo borthi brain duon ar fur y gaer, ‘ceni bai ef Arthur’, er nad Arthur ydoedd: un o’r cyfeiriadau cynharaf at enw Arthur yn unman.",
   "Canodd Taliesin fawl i Urien fel arglwydd hael Rheged a tharian ei bobl mewn brwydr, a galarodd am ei fab Owain. Mae sawl un o’i gerddi’n gorffen â’r un addewid: nes iddo heneiddio a marw, ni fyddai’n llawen oni bai ei fod yn moli Urien.",
   "Yna daeth beirdd Cymru ei hun. O’r nawfed a’r ddegfed ganrif daw englynion Llywarch Hen a’i feibion, a llais Heledd, tywysoges Powys, yn galaru am ei brawd Cynddylan a’i neuadd losg ym Mhengwern. O’r un cyfnod daw Armes Prydein, a broffwydodd y byddai’r Cymry’n uno â’r Gwyddyl, y Cernywiaid, y Llydawiaid a gwŷr y Gogledd dan Gynan a Chadwaladr, ac yn ennill Ynys Prydain yn ôl.",
   "Y farddoniaeth Gymraeg hynaf a ysgrifennwyd sydd wedi goroesi yw deuddeg englyn yn ymylon llyfr Lladin o’r nawfed ganrif, llawysgrif Juvencus, sydd heddiw yng Nghaergrawnt.",
   "> Gwŷr a aeth Gatraeth oedd ffraeth eu llu, glasfedd eu hancwyn, a gwenwyn fu. | Aneirin, Y Gododdin",
   "> Stafell Gynddylan ys tywyll heno, heb dân, heb wely. | Canu Heledd, y nawfed neu’r ddegfed ganrif",
   "## Hwiangerdd bedair canrif ar ddeg oed",
   "Yng nghanol penillion y rhyfelwyr yn Llyfr Aneirin mae cân fach y mae mam yn ei chanu i’w phlentyn, Dinogad. Mae’n sôn wrtho am ei bais fraith o grwyn bele, ac am ei dad, a âi i hela â’i waywffon a’i gŵn ac na ddôi byth adref heb iwrch, baedd, carw, grugiar o’r mynydd neu bysgodyn o raeadr Derwennydd. Mae’n un o’r hwiangerddi hynaf mewn unrhyw iaith yn Ewrop.",
  ]),
 dict(id="tywysogion", era="medieval", span="c. 1100–1282", spanCy="tua 1100–1282", en="The Poets of the Princes", cy="Beirdd y Tywysogion", pic="place-cardigan",
  people=["meilyr-brydydd", "cynddelw", "hywel-ab-owain", "gruffudd-ap-cynan", "owain-gwynedd", "yr-arglwydd-rhys", "llywelyn-fawr", "llywelyn-ap-gruffudd"],
  pEn=[
   "When Gruffudd ap Cynan won back Gwynedd, a new age of poetry began with him. His chief poet, Meilyr Brydydd, is the first of the Gogynfeirdd, better called Beirdd y Tywysogion, the Poets of the Princes. For almost two hundred years they served the courts of Gwynedd, Powys and Deheubarth, praising the courage and generosity of their lords in a language that was grand, old and deliberately difficult, like carved stone.",
   "The pencerdd, the chief of song, had a place in the law of Hywel Dda and a seat of honour in the hall. The bardd teulu sang to the war band before battle. A poet trained for years, and knew by heart the history, the family trees and the old tales of the Island of Britain.",
   "Meilyr asked to be buried on Ynys Enlli, the island of the saints, to wait for the resurrection there. His son Gwalchmai sang of Owain Gwynedd’s victories. Cynddelw Brydydd Mawr, ‘the great poet’, served Madog ap Maredudd of Powys, Owain Gwynedd and the Lord Rhys. Two princes were fine poets themselves: Hywel ab Owain Gwynedd, who sang of the beauty of Meirionnydd, and Owain Cyfeiliog of Powys, whose Hirlas Owain names his warriors one by one as the drinking horn goes round.",
   "Prydydd y Moch sang for Llywelyn Fawr; Dafydd Benfras and Bleddyn Fardd for Llywelyn ap Gruffudd. When Llywelyn fell in December 1282, Gruffudd ab yr Ynad Coch made the greatest elegy in the Welsh language, in which the whole world seems to break apart in grief.",
   "> Oni welwch chwi hynt y gwynt a’r glaw? Oni welwch chwi’r deri’n ymdaraw? — Do you not see the path of the wind and the rain? Do you not see the oak trees beating together? | Gruffudd ab yr Ynad Coch, elegy for Llywelyn ap Gruffudd, 1282",
   "## The first eisteddfod, 1176",
   "At Christmas 1176 the Lord Rhys held a great gathering at his new castle at Cardigan. He set two chairs as prizes, one for poetry and one for music, and invited poets and musicians from all over Wales. The chair for poetry went to the poets of Gwynedd, and the chair for music to a young man of Rhys’s own court. It is the first eisteddfod on record, and the chair is still the highest honour a Welsh poet can win.",
   "Most of the poetry of the princes’ age survives because two books gathered it in: the Hendregadredd Manuscript and the Red Book of Hergest.",
  ],
  pCy=[
   "Pan enillodd Gruffudd ap Cynan Wynedd yn ôl, dechreuodd oes newydd o farddoniaeth gydag ef. Ei brif fardd, Meilyr Brydydd, yw’r cyntaf o’r Gogynfeirdd, neu Feirdd y Tywysogion. Am bron i ddau gan mlynedd buont yn gwasanaethu llysoedd Gwynedd, Powys a Deheubarth, gan foli dewrder a haelioni eu harglwyddi mewn iaith fawreddog, hen a bwriadol anodd, fel carreg gerfiedig.",
   "Roedd gan y pencerdd le yng nghyfraith Hywel Dda a sedd anrhydedd yn y neuadd. Canai’r bardd teulu i’r osgordd cyn brwydr. Hyfforddai bardd am flynyddoedd, a gwyddai ar ei gof hanes, achau a hen chwedlau Ynys Prydain.",
   "Gofynnodd Meilyr am gael ei gladdu ar Ynys Enlli, ynys y saint, i aros yno am yr atgyfodiad. Canodd ei fab Gwalchmai am fuddugoliaethau Owain Gwynedd. Gwasanaethodd Cynddelw Brydydd Mawr Fadog ap Maredudd o Bowys, Owain Gwynedd a’r Arglwydd Rhys. Roedd dau dywysog yn feirdd gwych eu hunain: Hywel ab Owain Gwynedd, a ganodd am harddwch Meirionnydd, ac Owain Cyfeiliog o Bowys, y mae ei Hirlas Owain yn enwi ei ryfelwyr fesul un wrth i’r corn yfed fynd o law i law.",
   "Canodd Prydydd y Moch i Lywelyn Fawr; Dafydd Benfras a Bleddyn Fardd i Lywelyn ap Gruffudd. Pan syrthiodd Llywelyn ym mis Rhagfyr 1282, lluniodd Gruffudd ab yr Ynad Coch y farwnad fwyaf yn yr iaith Gymraeg, lle mae’r byd i gyd fel petai’n chwalu gan alar.",
   "> Oni welwch chwi hynt y gwynt a’r glaw? Oni welwch chwi’r deri’n ymdaraw? | Gruffudd ab yr Ynad Coch, marwnad Llywelyn ap Gruffudd, 1282",
   "## Yr eisteddfod gyntaf, 1176",
   "Adeg y Nadolig 1176 cynhaliodd yr Arglwydd Rhys ŵyl fawr yn ei gastell newydd yn Aberteifi. Gosododd ddwy gadair yn wobrau, un am farddoniaeth ac un am gerddoriaeth, a gwahodd beirdd a cherddorion o bob rhan o Gymru. Aeth cadair y beirdd i feirdd Gwynedd, a chadair y gerddoriaeth i ŵr ifanc o lys Rhys ei hun. Dyma’r eisteddfod gyntaf a gofnodwyd, a’r gadair yw’r anrhydedd uchaf y gall bardd Cymraeg ei hennill o hyd.",
   "Goroesodd y rhan fwyaf o farddoniaeth oes y tywysogion am i ddau lyfr ei chasglu: Llawysgrif Hendregadredd a Llyfr Coch Hergest.",
  ]),
 dict(id="uchelwyr", era="medieval", span="c. 1330–1600", spanCy="tua 1330–1600", en="The Poets of the Nobility", cy="Beirdd yr Uchelwyr", pic="person-dafydd-ap-gwilym",
  people=["dafydd-ap-gwilym", "iolo-goch", "lewys-glyn-cothi", "guto-r-glyn", "gwerful-mechain", "owain-glyndwr"],
  pEn=[
   "With the princes gone, the poets found new patrons among the uchelwyr, the Welsh gentry, in their halls and manor houses across the land. For three centuries poets travelled from house to house on their clera, their circuits, at Christmas, Easter and Whitsun, praising, mourning and entertaining, and the houses of Wales rang with poetry.",
   "Their great measure was the cywydd: rhyming couplets of seven-syllable lines, every line bound by cynghanedd. It was brought to its height by the greatest of all Welsh poets, Dafydd ap Gwilym of Brogynin, near Aberystwyth, about 1340. He wrote of love and of the natural world, of the seagull, the wind, the mist, the girls of Llanbadarn and his loves Morfudd and Dyddgu, with a freshness that still delights readers nearly seven hundred years later. Welsh tradition holds that he lies under a yew tree at Strata Florida.",
   "A golden age followed. Iolo Goch sang of Owain Glyndŵr’s court at Sycharth, with its nine halls, its fishpond, its orchard and its doors always open to poets. Siôn Cent turned poetry towards the soul. Lewys Glyn Cothi and Guto’r Glyn sang through the Wars of the Roses, and Lewys wrote one of the most moving poems in any language, his lament for his little son Siôn y Glyn, who died at five years old. Dafydd Nanmor, Tudur Aled and Gutun Owain followed, and Gwerful Mechain of Powys answered the men in their own measures, with wit and daring.",
   "At the eisteddfod held at Carmarthen about 1451, Dafydd ab Edmwnd set down the rules of the twenty-four strict metres and won a silver chair. Those rules are still used: every year at the National Eisteddfod, the chair is given for an awdl in the strict metres.",
   "The poets kept the old learning too: the family trees of the gentry, the Triads, the tales and the history of the Island of Britain. Many of the great manuscripts of the fifteenth and sixteenth centuries were written in poets’ own hands.",
   "> Yr wylan deg ar lanw dioer, unlliw ag eiry neu wenlloer. — Fair seagull on the flowing tide, the colour of snow or the white moon. | Dafydd ap Gwilym, ‘Yr Wylan’ (The Seagull)",
  ],
  pCy=[
   "A’r tywysogion wedi mynd, cafodd y beirdd noddwyr newydd ymhlith yr uchelwyr, bonedd Cymru, yn eu neuaddau a’u plastai ar hyd a lled y wlad. Am dair canrif teithiai’r beirdd o dŷ i dŷ ar eu clera, adeg y Nadolig, y Pasg a’r Sulgwyn, gan foli, galaru a diddanu, ac roedd tai Cymru’n atseinio gan farddoniaeth.",
   "Eu mesur mawr oedd y cywydd: cwpledi odledig o linellau seithsill, a phob llinell wedi’i rhwymo gan gynghanedd. Fe’i codwyd i’w uchelfannau gan y mwyaf o holl feirdd Cymru, Dafydd ap Gwilym o Frogynin, ger Aberystwyth, tua 1340. Canodd am gariad ac am fyd natur, am yr wylan, y gwynt, y niwl, merched Llanbadarn a’i gariadon Morfudd a Dyddgu, gyda ffresni sy’n swyno darllenwyr o hyd bron saith can mlynedd yn ddiweddarach. Yn ôl traddodiad Cymru, gorwedd dan ywen yn Ystrad Fflur.",
   "Dilynodd oes aur. Canodd Iolo Goch i lys Owain Glyndŵr yn Sycharth, â’i naw neuadd, ei bysgodlyn, ei berllan a’i ddrysau ar agor i’r beirdd bob amser. Trodd Siôn Cent farddoniaeth at yr enaid. Canodd Lewys Glyn Cothi a Guto’r Glyn drwy Ryfeloedd y Rhosynnau, ac ysgrifennodd Lewys un o’r cerddi mwyaf teimladwy mewn unrhyw iaith, ei farwnad i’w fab bach Siôn y Glyn, a fu farw’n bump oed. Dilynodd Dafydd Nanmor, Tudur Aled a Gutun Owain, ac atebodd Gwerful Mechain o Bowys y dynion yn eu mesurau eu hunain, yn ffraeth ac yn feiddgar.",
   "Yn yr eisteddfod a gynhaliwyd yng Nghaerfyrddin tua 1451, gosododd Dafydd ab Edmwnd reolau’r pedwar mesur ar hugain ac ennill cadair arian. Defnyddir y rheolau hynny o hyd: bob blwyddyn yn yr Eisteddfod Genedlaethol, rhoddir y gadair am awdl yn y mesurau caeth.",
   "Cadwai’r beirdd yr hen ddysg hefyd: achau’r uchelwyr, y Trioedd, y chwedlau a hanes Ynys Prydain. Ysgrifennwyd llawer o lawysgrifau mawr y bymthegfed a’r unfed ganrif ar bymtheg yn llaw’r beirdd eu hunain.",
   "> Yr wylan deg ar lanw dioer, unlliw ag eiry neu wenlloer. | Dafydd ap Gwilym, ‘Yr Wylan’",
  ]),
 dict(id="argraffu", era="tudor", span="1546–1750", spanCy="1546–1750", en="The printed book and the Bible", cy="Y llyfr printiedig a’r Beibl", pic="trea-bible-1588",
  people=["john-price", "william-salesbury", "william-morgan", "sion-dafydd-rhys", "john-davies-mallwyd", "rhys-prichard", "morgan-llwyd", "ellis-wynne", "theophilus-evans"],
  pEn=[
   "In 1546 Sir John Price of Brecon printed the first book in Welsh. It begins with the words Yny lhyvyr hwnn, ‘in this book’, and holds the alphabet, the calendar, the Creed, the Lord’s Prayer and the Ten Commandments, so that his people could learn them in their own tongue.",
   "In 1567 William Salesbury, with Bishop Richard Davies and Thomas Huet, gave Wales the New Testament and the Book of Common Prayer in Welsh. The same year, in Milan, Gruffydd Robert printed the first part of his Welsh grammar. Then in 1588 came the greatest book of all: the whole Bible in Welsh, translated by William Morgan in his vicarage at Llanrhaeadr-ym-Mochnant. It gave the language a noble standard of prose and carried it into every parish church in the land, and many believe it is the main reason Welsh is still spoken today.",
   "The scholars of the Welsh Renaissance followed. Siôn Dafydd Rhys published his grammar in 1592. Dr John Davies of Mallwyd revised the Bible in 1620 and wrote a great grammar (1621) and dictionary (1632). In 1630 came Y Beibl Bach, the little Bible, cheap enough for families to keep at home. Rhys Prichard, the Old Vicar of Llandovery, put the faith into simple verses that people learned by heart, and Morgan Llwyd of Wrexham wrote the Book of the Three Birds (1653).",
   "In 1703 Ellis Wynne of Y Lasynys published Gweledigaetheu y Bardd Cwsc, the Visions of the Sleeping Bard, some of the finest Welsh prose ever written. In 1716 Theophilus Evans told the story of the Welsh from the very beginning in Drych y Prif Oesoedd, the Mirror of the First Ages, the best-loved history book in Welsh for two hundred years.",
   "> Mynnwch ddysg yn eich iaith. — Insist on learning in your own language. | William Salesbury, 1547",
  ],
  pCy=[
   "Yn 1546 argraffodd Syr John Prys o Aberhonddu y llyfr cyntaf yn Gymraeg. Mae’n dechrau â’r geiriau Yny lhyvyr hwnn, ‘yn y llyfr hwn’, ac mae ynddo’r wyddor, y calendr, y Credo, Gweddi’r Arglwydd a’r Deg Gorchymyn, er mwyn i’w bobl eu dysgu yn eu hiaith eu hunain.",
   "Yn 1567 rhoddodd William Salesbury, gyda’r Esgob Richard Davies a Thomas Huet, y Testament Newydd a’r Llyfr Gweddi Gyffredin yn Gymraeg i Gymru. Yr un flwyddyn, ym Milan, argraffodd Gruffydd Robert ran gyntaf ei ramadeg Cymraeg. Yna yn 1588 daeth y llyfr mwyaf oll: y Beibl cyfan yn Gymraeg, wedi’i gyfieithu gan William Morgan yn ei ficerdy yn Llanrhaeadr-ym-Mochnant. Rhoddodd safon urddasol o ryddiaith i’r iaith a’i chario i bob eglwys blwyf yn y wlad, a chred llawer mai dyma’r prif reswm fod y Gymraeg yn cael ei siarad o hyd.",
   "Dilynodd ysgolheigion y Dadeni Cymreig. Cyhoeddodd Siôn Dafydd Rhys ei ramadeg yn 1592. Diwygiodd Dr John Davies o Fallwyd y Beibl yn 1620 ac ysgrifennu gramadeg mawr (1621) a geiriadur (1632). Yn 1630 daeth y Beibl Bach, yn ddigon rhad i deuluoedd ei gadw gartref. Rhoddodd Rhys Prichard, yr Hen Ficer o Lanymddyfri, y ffydd mewn penillion syml a ddysgai pobl ar eu cof, ac ysgrifennodd Morgan Llwyd o Wrecsam Lyfr y Tri Aderyn (1653).",
   "Yn 1703 cyhoeddodd Ellis Wynne o’r Lasynys Weledigaetheu y Bardd Cwsc, peth o’r rhyddiaith Gymraeg orau a ysgrifennwyd erioed. Yn 1716 adroddodd Theophilus Evans hanes y Cymry o’r dechrau un yn Nrych y Prif Oesoedd, y llyfr hanes anwylaf yn Gymraeg am ddau gan mlynedd.",
   "> Mynnwch ddysg yn eich iaith. | William Salesbury, 1547",
  ]),
 dict(id="emynau", era="industrial", span="1735–1900", spanCy="1735–1900", en="Hymns, scholars and the Eisteddfod", cy="Emynau, ysgolheigion a’r Eisteddfod", pic="person-pantycelyn",
  people=["pantycelyn", "ann-griffiths", "griffith-jones", "lewis-morris", "goronwy-owen", "iolo-morganwg", "lady-charlotte-guest", "daniel-owen"],
  pEn=[
   "In the eighteenth century Wales found a new voice in the hymn. William Williams Pantycelyn wrote hundreds of hymns in Welsh, among them Arglwydd, arwain trwy’r anialwch, sung in English as Guide me, O thou great Jehovah. Ann Griffiths of Dolwar Fach, whose hymns were kept in the memory of her maid Ruth and written down after her death, made some of the greatest religious poetry in any language. Griffith Jones’s circulating schools taught a great part of the nation to read.",
   "The Morris brothers of Anglesey, Lewis, Richard and William, copied old manuscripts and gathered poets around them, and their friend Goronwy Owen raised the classical poetry of Wales to new heights before he sailed to Virginia. In London the Gwyneddigion society, Owain Myfyr and Iolo Morganwg printed the old poetry for the first time in the Myvyrian Archaiology of Wales (1801–07). In 1792, on Primrose Hill, Iolo held the first gathering of the Gorsedd of the Bards of the Island of Britain, which has crowned and chaired the poets of Wales ever since.",
   "In the nineteenth century Welsh became a language of books, newspapers and magazines by the hundred. Lady Charlotte Guest gave the Mabinogion to the world. The eisteddfod grew into a festival of the whole nation, and the first National Eisteddfod of the modern kind was held at Aberdare in 1861. Daniel Owen, the tailor of Mold, wrote the great Welsh novels: Rhys Lewis, Enoc Huws and Gwen Tomos.",
   "> Arglwydd, arwain trwy’r anialwch fi, bererin gwael ei wedd. — Lord, lead me through the wilderness, a pilgrim poor in looks. | William Williams Pantycelyn",
  ],
  pCy=[
   "Yn y ddeunawfed ganrif cafodd Cymru lais newydd yn yr emyn. Ysgrifennodd William Williams Pantycelyn gannoedd o emynau Cymraeg, yn eu plith Arglwydd, arwain trwy’r anialwch, a genir yn Saesneg fel Guide me, O thou great Jehovah. Lluniodd Ann Griffiths o Ddolwar Fach, y cadwyd ei hemynau yng nghof ei morwyn Ruth a’u hysgrifennu wedi ei marw, beth o’r farddoniaeth grefyddol fwyaf mewn unrhyw iaith. Dysgodd ysgolion cylchynol Griffith Jones ran fawr o’r genedl i ddarllen.",
   "Copïodd Morrisiaid Môn, Lewis, Richard a William, hen lawysgrifau a chasglu beirdd o’u cwmpas, a chododd eu cyfaill Goronwy Owen farddoniaeth glasurol Cymru i uchelfannau newydd cyn hwylio i Virginia. Yn Llundain argraffodd cymdeithas y Gwyneddigion, Owain Myfyr ac Iolo Morganwg yr hen farddoniaeth am y tro cyntaf yn y Myvyrian Archaiology of Wales (1801–07). Yn 1792, ar Fryn y Briallu, cynhaliodd Iolo gyfarfod cyntaf Gorsedd Beirdd Ynys Prydain, sydd wedi coroni a chadeirio beirdd Cymru byth ers hynny.",
   "Yn y bedwaredd ganrif ar bymtheg daeth y Gymraeg yn iaith llyfrau, papurau newydd a chylchgronau wrth y cannoedd. Rhoddodd yr Arglwyddes Charlotte Guest y Mabinogion i’r byd. Tyfodd yr eisteddfod yn ŵyl i’r genedl gyfan, a chynhaliwyd yr Eisteddfod Genedlaethol gyntaf o’r math modern yn Aberdâr yn 1861. Ysgrifennodd Daniel Owen, teiliwr yr Wyddgrug, y nofelau Cymraeg mawr: Rhys Lewis, Enoc Huws a Gwen Tomos.",
   "> Arglwydd, arwain trwy’r anialwch fi, bererin gwael ei wedd. | William Williams Pantycelyn",
  ]),
 dict(id="heddiw", era="modern", span="1900–today", spanCy="1900–heddiw", en="The twentieth century and today", cy="Yr ugeinfed ganrif a heddiw", pic="person-hedd-wyn",
  people=["hedd-wyn", "t-h-parry-williams", "kate-roberts", "saunders-lewis", "waldo-williams", "t-llew-jones", "om-edwards", "dylan-thomas", "r-s-thomas"],
  pEn=[
   "The twentieth century was one of the richest in the whole history of Welsh literature. T. Gwynn Jones and R. Williams Parry won chairs with poems of a new beauty, and T. H. Parry-Williams wrote of Rhyd-ddu and Eryri. Hedd Wyn, the shepherd poet of Trawsfynydd, won the chair at Birkenhead in 1917, five weeks after he fell at Passchendaele, and the chair was draped in black.",
   "Kate Roberts, the queen of Welsh prose, wrote of the quarrying people of Rhosgadfan. Saunders Lewis wrote great plays, and his radio lecture Tynged yr Iaith (1962) roused a generation to stand up for Welsh. Waldo Williams sang of Preseli and of peace; Gwenallt, Euros Bowen and Alan Llwyd carried the strict metres on; T. Llew Jones gave the children of Wales their own adventure stories.",
   "Wales has a second great literature too, in English: Dylan Thomas, R. S. Thomas, Gwyn Thomas, Emyr Humphreys, Raymond Williams and many more. And the old crafts are alive and thriving. Cynghanedd is written today at the eisteddfodau, in the Talwrn y Beirdd contests on the radio, and by children in school.",
   "> Beth yw byw? Cael neuadd fawr rhwng cyfyng furiau. — What is living? Having a great hall between narrow walls. | Waldo Williams, ‘Pa beth yw dyn?’",
  ],
  pCy=[
   "Roedd yr ugeinfed ganrif yn un o’r cyfoethocaf yn holl hanes llenyddiaeth Gymraeg. Enillodd T. Gwynn Jones ac R. Williams Parry gadeiriau â cherddi o harddwch newydd, ac ysgrifennodd T. H. Parry-Williams am Ryd-ddu ac Eryri. Enillodd Hedd Wyn, bardd bugail Trawsfynydd, y gadair ym Mhenbedw yn 1917, bum wythnos wedi iddo syrthio yn Passchendaele, a gorchuddiwyd y gadair â lliain du.",
   "Ysgrifennodd Kate Roberts, brenhines rhyddiaith Gymraeg, am bobl y chwareli yn Rhosgadfan. Ysgrifennodd Saunders Lewis ddramâu mawr, a deffrodd ei ddarlith radio Tynged yr Iaith (1962) genhedlaeth i sefyll dros y Gymraeg. Canodd Waldo Williams am y Preseli ac am heddwch; cariodd Gwenallt, Euros Bowen ac Alan Llwyd y mesurau caeth ymlaen; rhoddodd T. Llew Jones eu straeon antur eu hunain i blant Cymru.",
   "Mae gan Gymru ail lenyddiaeth fawr hefyd, yn Saesneg: Dylan Thomas, R. S. Thomas, Gwyn Thomas, Emyr Humphreys, Raymond Williams a llawer mwy. Ac mae’r hen grefftau’n fyw ac yn ffynnu. Ysgrifennir cynghanedd heddiw yn yr eisteddfodau, yn Nhalwrn y Beirdd ar y radio, a chan blant yn yr ysgol.",
   "> Beth yw byw? Cael neuadd fawr rhwng cyfyng furiau. | Waldo Williams, ‘Pa beth yw dyn?’",
  ]),
]

# What is cynghanedd? (a box on the hub page)
CYNG_EN = [
 "Cynghanedd, ‘harmony’, is the chiming of sounds inside a single line of verse. It is the heart of the Welsh strict metres, and no other language has anything quite like it. There are four main kinds:",
 "|| Cynghanedd groes | The consonants of the first half of the line are repeated, in the same order, in the second half.",
 "|| Cynghanedd draws | The same, but a few consonants at the start of the second half are left unanswered, ‘drawn across’.",
 "|| Cynghanedd sain | The line falls into three parts: the first two rhyme, and the second and third chime in their consonants.",
 "|| Cynghanedd lusg | The end of the first part rhymes with the stressed syllable just before the end of the line.",
 "Here is a line by R. Williams Parry, from his englynion in memory of Hedd Wyn. The sounds b, r, dd, t, r of the first half come back in the same order in the second, after the unanswered word ‘dan’: cynghanedd draws.",
]
CYNG_CY = [
 "Cynghanedd yw cyfatebiaeth seiniau o fewn un llinell o farddoniaeth. Hi yw calon y mesurau caeth, ac nid oes gan unrhyw iaith arall ddim byd tebyg iddi. Mae pedwar prif fath:",
 "|| Cynghanedd groes | Mae cytseiniaid hanner cyntaf y llinell yn cael eu hailadrodd, yn yr un drefn, yn yr ail hanner.",
 "|| Cynghanedd draws | Yr un peth, ond mae ambell gytsain ar ddechrau’r ail hanner heb ei hateb, wedi’i ‘thraws’ neidio.",
 "|| Cynghanedd sain | Mae’r llinell yn dair rhan: mae’r ddwy gyntaf yn odli, a’r ail a’r drydedd yn cyfateb yn eu cytseiniaid.",
 "|| Cynghanedd lusg | Mae diwedd y rhan gyntaf yn odli â’r goben, y sillaf acennog ychydig cyn diwedd y llinell.",
 "Dyma linell gan R. Williams Parry, o’i englynion er cof am Hedd Wyn. Mae seiniau b, r, dd, t, r yr hanner cyntaf yn dod yn ôl yn yr un drefn yn yr ail, ar ôl y gair ‘dan’ sydd heb ei ateb: cynghanedd draws.",
]
# the example line: (first half, second half), each a list of (text, is_chiming_consonant)
CYNG_LINE = ([("Y ", 0), ("b", 1), ("a", 0), ("r", 1), ("dd", 1), (" ", 0), ("t", 1), ("r", 1), ("wm", 0)],
             [("dan ", 0), ("b", 1), ("", 0), ("r", 1), ("i", 0), ("dd", 1), (" ", 0), ("t", 1), ("", 0), ("r", 1), ("amor", 0)])

# ---------------------------------------------------------------- the great books (books.html)
# pic: a gallery id (string) or a Commons picture: (file, author, licence, licence link, caption EN, caption CY, width, height)
CC0 = ("CC0", "https://creativecommons.org/publicdomain/zero/1.0/deed.en")
PD = ("Public domain", "https://creativecommons.org/publicdomain/mark/1.0/")
BYSA4 = ("CC BY-SA 4.0", "https://creativecommons.org/licenses/by-sa/4.0")

BOOKS_INTRO_EN = [
 "Almost all of early Welsh literature survives in a few dozen books written by hand between about 1250 and 1500, on vellum made from calfskin. Without them, the poems of Taliesin and Aneirin, the Mabinogion, the Triads, the laws of Hywel Dda and the chronicle of the princes would all be lost.",
 "They were made by scribes in monasteries such as Strata Florida, and paid for by Welsh families who loved the old learning. They passed from house to house for centuries, and were saved by collectors such as Robert Vaughan of Hengwrt, whose great library came to the National Library of Wales in 1909. Four of them are known as the Four Ancient Books of Wales, the name the Scottish scholar William Forbes Skene gave them in 1868.",
]
BOOKS_INTRO_CY = [
 "Mae bron y cwbl o lenyddiaeth gynnar Cymru wedi goroesi mewn ychydig ddwsinau o lyfrau a ysgrifennwyd â llaw rhwng tua 1250 a 1500, ar femrwn o groen llo. Hebddynt byddai cerddi Taliesin ac Aneirin, y Mabinogion, y Trioedd, cyfraith Hywel Dda a chronicl y tywysogion i gyd ar goll.",
 "Fe’u gwnaed gan gopïwyr mewn mynachlogydd fel Ystrad Fflur, a thalwyd amdanynt gan deuluoedd Cymreig a garai’r hen ddysg. Aethant o dŷ i dŷ am ganrifoedd, a’u hachub gan gasglwyr fel Robert Vaughan o’r Hengwrt, y daeth ei lyfrgell fawr i Lyfrgell Genedlaethol Cymru yn 1909. Gelwir pedwar ohonynt yn Bedwar Llyfr Hynafol Cymru, yr enw a roddodd yr ysgolhaig o’r Alban William Forbes Skene arnynt yn 1868.",
]

BOOK_GROUPS = [
 dict(id="earliest", en="The oldest written Welsh", cy="Y Gymraeg ysgrifenedig hynaf", books=[
  dict(id="llandeilo", en="The Llandeilo Gospels", cy="Efengylau Llandeilo", date="8th century", dateCy="yr wythfed ganrif", whereEn="Lichfield Cathedral", whereCy="Eglwys Gadeiriol Caerlwytgoed",
   pic="trea-st-chad",
   en_t="A Latin gospel book that belonged to the church of Teilo at Llandeilo Fawr in the ninth century. In its margins are the earliest written Welsh that survives, among them the Surexit memorandum, the record of a quarrel over land settled peacefully before witnesses. It is now known as the St Chad Gospels.",
   cy_t="Llyfr efengylau Lladin a berthynai i eglwys Teilo yn Llandeilo Fawr yn y nawfed ganrif. Yn ei ymylon mae’r Gymraeg ysgrifenedig hynaf sydd wedi goroesi, yn eu plith y cofnod Surexit, hanes ffrae am dir a setlwyd yn heddychlon o flaen tystion. Fe’i gelwir heddiw yn Efengylau Sant Chad."),
  dict(id="juvencus", en="The Juvencus englynion", cy="Englynion y Juvencus", date="9th century", dateCy="y nawfed ganrif", whereEn="Cambridge University Library", whereCy="Llyfrgell Prifysgol Caergrawnt",
   pic=None,
   en_t="A copy of a Latin poem on the life of Christ by the Spanish poet Juvencus, written in Wales. Scribes added twelve englynion in Welsh to its margins: three in the voice of a grieving warrior who will not talk or laugh tonight, though his war band is about him, and nine in praise of God. They are the oldest Welsh poetry written down that survives.",
   cy_t="Copi o gerdd Ladin ar fywyd Crist gan y bardd Juvencus o Sbaen, a ysgrifennwyd yng Nghymru. Ychwanegodd copïwyr ddeuddeg englyn Cymraeg at ei ymylon: tri yn llais rhyfelwr galarus na fyn siarad na chwerthin heno, er bod ei osgordd o’i gwmpas, a naw yn moli Duw. Dyma’r farddoniaeth Gymraeg ysgrifenedig hynaf sydd wedi goroesi."),
  dict(id="historia", en="The History of the Britons", cy="Historia Brittonum", date="c. 829; copy c. 1100", dateCy="tua 829; copi tua 1100", whereEn="British Library, London", whereCy="Y Llyfrgell Brydeinig, Llundain",
   pic=None,
   en_t="A history of the Island of Britain gathered in Gwynedd in the reign of Merfyn Frych, long known by the name of Nennius. It tells of Arthur and his twelve battles, of Gwrtheyrn and the two dragons at Dinas Emrys, and names the first poets. The oldest copy keeps with it the Annales Cambriae, the Welsh annals, and the family trees of the early Welsh kings.",
   cy_t="Hanes Ynys Prydain a gasglwyd yng Ngwynedd yn nheyrnasiad Merfyn Frych, a adwaenir ers tro wrth enw Nennius. Mae’n sôn am Arthur a’i ddeuddeg brwydr, am Wrtheyrn a’r ddwy ddraig yn Ninas Emrys, ac yn enwi’r beirdd cyntaf. Mae’r copi hynaf yn cadw gydag ef yr Annales Cambriae, cronicl Cymru, ac achau brenhinoedd cynnar Cymru."),
  dict(id="llandaf", en="The Book of Llandaf", cy="Llyfr Llandaf", date="c. 1120–1134", dateCy="tua 1120–1134", whereEn="National Library of Wales", whereCy="Llyfrgell Genedlaethol Cymru",
   pic=("Liber Landavensis binding.png", "Unknown medieval craftsman", *CC0, "The binding of the Book of Llandaf, with the gilded figure on its cover", "Rhwymiad Llyfr Llandaf, gyda’r ddelw euraid ar ei glawr", 1058, 707),
   en_t="Written at Llandaf to tell the story of its church: the lives of the saints Dyfrig, Teilo and Euddogwy, and about a hundred and fifty charters by which kings gave land to the church. Among them are the grants of Meurig ap Tewdrig, king of Glywysing, and of his son Athrwys, who Welsh tradition holds was Arthur. Its boundary clauses, written in Welsh, name streams and hills still known today.",
   cy_t="Fe’i hysgrifennwyd yn Llandaf i adrodd hanes ei heglwys: bucheddau’r saint Dyfrig, Teilo ac Euddogwy, a thua chant a hanner o siarteri lle rhoddodd brenhinoedd dir i’r eglwys. Yn eu plith mae rhoddion Meurig ap Tewdrig, brenin Glywysing, a’i fab Athrwys, sef Arthur yn ôl traddodiad Cymru. Mae ei ffiniau, a ysgrifennwyd yn Gymraeg, yn enwi nentydd a bryniau sy’n hysbys hyd heddiw.",
   link=("person-arthur.html", "Arthur, King of the Britons", "Arthur, Brenin y Brythoniaid")),
 ]),
 dict(id="four", en="The Four Ancient Books of Wales", cy="Pedwar Llyfr Hynafol Cymru", books=[
  dict(id="black", en="The Black Book of Carmarthen", cy="Llyfr Du Caerfyrddin", date="c. 1250", dateCy="tua 1250", whereEn="National Library of Wales (Peniarth MS 1)", whereCy="Llyfrgell Genedlaethol Cymru (Peniarth 1)",
   pic="trea-black-book",
   pic2=("Dormarch in the Black Book of Carmarthen (f. 49 r.).png", "Unknown medieval scribe", *BYSA4, "A scribe’s drawing of the hound Dormarch in the margin of the Black Book", "Llun copïydd o’r ci Dormarch yn ymyl y Llyfr Du", 772, 509),
   en_t="The oldest surviving book written entirely in Welsh, the work of one patient scribe over many years. It holds the poems of Myrddin under his apple tree, Englynion y Beddau, the Stanzas of the Graves, which name the resting places of the heroes of the Island of Britain, the dialogue in which Arthur names his men to the porter Glewlwyd Gafaelfawr, the elegy for Geraint ab Erbin at Llongborth, and poems of praise and of faith. It takes its name from its black binding and from the priory of St John at Carmarthen, where it was kept.",
   cy_t="Y llyfr hynaf sydd wedi goroesi a ysgrifennwyd yn gyfan gwbl yn Gymraeg, gwaith un copïydd amyneddgar dros flynyddoedd lawer. Ynddo mae cerddi Myrddin dan ei afallen, Englynion y Beddau, sy’n enwi beddau arwyr Ynys Prydain, yr ymddiddan lle mae Arthur yn enwi ei wŷr wrth y porthor Glewlwyd Gafaelfawr, y farwnad i Geraint ab Erbin yn Llongborth, a cherddi mawl a ffydd. Daw ei enw o’i rwymiad du ac o briordy Sant Ioan yng Nghaerfyrddin, lle’i cadwyd."),
  dict(id="aneirin", en="The Book of Aneirin", cy="Llyfr Aneirin", date="c. 1265", dateCy="tua 1265", whereEn="National Library of Wales (Cardiff MS 2.81)", whereCy="Llyfrgell Genedlaethol Cymru (Caerdydd 2.81)",
   pic="trea-book-aneirin",
   en_t="A small book of thirty-eight pages that keeps Y Gododdin, Aneirin’s great poem of the warriors who fell at Catraeth, with the four Gorchanau. Two scribes wrote it. The second copied from a far older book, keeping its spellings, and through his pages we can see Welsh as it was written in the ninth century or earlier. Here too is Pais Dinogad, the lullaby of a hunter’s child.",
   cy_t="Llyfr bach o dri deg wyth tudalen sy’n cadw’r Gododdin, cerdd fawr Aneirin i’r rhyfelwyr a syrthiodd yng Nghatraeth, gyda’r pedair Gorchan. Dau gopïydd a’i hysgrifennodd. Copïodd yr ail o lyfr llawer hŷn, gan gadw ei sillafu, a thrwy ei dudalennau gallwn weld y Gymraeg fel yr ysgrifennid hi yn y nawfed ganrif neu’n gynharach. Yma hefyd mae Pais Dinogad, hwiangerdd plentyn yr heliwr.",
   link=("person-aneirin.html", "Aneirin", "Aneirin")),
  dict(id="taliesin", en="The Book of Taliesin", cy="Llyfr Taliesin", date="c. 1325–1350", dateCy="tua 1325–1350", whereEn="National Library of Wales (Peniarth MS 2)", whereCy="Llyfrgell Genedlaethol Cymru (Peniarth 2)",
   pic="trea-book-taliesin",
   en_t="Some sixty poems in the name of Taliesin, chief of bards: the songs of praise to Urien of Rheged and his son Owain, Armes Prydein, the Prophecy of Britain, Preiddeu Annwfn, the voyage of Arthur and his men in the ship Prydwen to the Otherworld, Cad Goddeu, the Battle of the Trees, and poems in the voice of the poet who has lived in every age. Its first pages are lost.",
   cy_t="Tua thrigain o gerddi yn enw Taliesin, pen beirdd: y cerddi mawl i Urien Rheged a’i fab Owain, Armes Prydein, Preiddeu Annwfn, mordaith Arthur a’i wŷr yn y llong Prydwen i Annwn, Cad Goddeu, a cherddi yn llais y bardd a fu’n byw ym mhob oes. Collwyd ei dudalennau cyntaf.",
   link=("person-taliesin.html", "Taliesin", "Taliesin")),
  dict(id="red", en="The Red Book of Hergest", cy="Llyfr Coch Hergest", date="c. 1382–1410", dateCy="tua 1382–1410", whereEn="Jesus College, Oxford (MS 111)", whereCy="Coleg Iesu, Rhydychen (MS 111)",
   pic="trea-red-book",
   en_t="The greatest of all the Welsh books, written mainly by Hywel Fychan ap Hywel Goch of Buellt for Hopcyn ap Tomas of Ynysforgan, near Swansea. In its 362 leaves are the Mabinogion, the history of the kings of Britain, the chronicle of the princes, the poetry of the princes’ age, the englynion of Llywarch Hen and Heledd, the Triads, proverbs, and the remedies of the Physicians of Myddfai. It is named after Hergest Court, near Kington, where it was kept for a time, and has been in Oxford since 1701.",
   cy_t="Y mwyaf o holl lyfrau Cymru, a ysgrifennwyd yn bennaf gan Hywel Fychan ap Hywel Goch o Fuellt i Hopcyn ap Tomas o Ynysforgan, ger Abertawe. Yn ei 362 o ddail mae’r Mabinogion, hanes brenhinoedd Prydain, cronicl y tywysogion, barddoniaeth oes y tywysogion, englynion Llywarch Hen a Heledd, y Trioedd, diarhebion, a meddyginiaethau Meddygon Myddfai. Fe’i henwyd ar ôl Llys Hergest, ger Ceintun, lle’i cadwyd am gyfnod, ac mae yn Rhydychen ers 1701.",
   link=("legend-llynyfan.html", "The Lady of Llyn y Fan Fach", "Arglwyddes Llyn y Fan Fach")),
 ]),
 dict(id="great", en="The other great books", cy="Y llyfrau mawr eraill", books=[
  dict(id="white", en="The White Book of Rhydderch", cy="Llyfr Gwyn Rhydderch", date="c. 1350", dateCy="tua 1350", whereEn="National Library of Wales (Peniarth MSS 4 and 5)", whereCy="Llyfrgell Genedlaethol Cymru (Peniarth 4 a 5)",
   pic=("Llyfr Gwyn Rhydderch f. 45 r. Beginning of Macsen Wledig.png", "Unknown medieval scribe", *CC0, "The opening of the Dream of Macsen Wledig in the White Book of Rhydderch, with its red initial", "Dechrau Breuddwyd Macsen Wledig yn Llyfr Gwyn Rhydderch, gyda’i lythyren goch", 867, 762),
   en_t="Made for Rhydderch ab Ieuan Llwyd of Parc Rhydderch, near Llangeitho, probably by scribes at the abbey of Strata Florida. It holds the oldest complete text of the Four Branches of the Mabinogi and of the other tales, with the lives of saints, the history of the kings of Britain, religious writing and poetry. It is now bound as two books.",
   cy_t="Fe’i gwnaed i Rydderch ab Ieuan Llwyd o Barc Rhydderch, ger Llangeitho, gan gopïwyr yn abaty Ystrad Fflur yn ôl pob tebyg. Ynddo mae’r testun cyflawn hynaf o Bedair Cainc y Mabinogi ac o’r chwedlau eraill, gyda bucheddau saint, hanes brenhinoedd Prydain, ysgrifeniadau crefyddol a barddoniaeth. Mae wedi’i rwymo’n ddau lyfr heddiw.",
   link=("mabinogion.html", "The Mabinogion", "Y Mabinogion")),
  dict(id="hendregadredd", en="The Hendregadredd Manuscript", cy="Llawysgrif Hendregadredd", date="c. 1300 onwards", dateCy="tua 1300 ymlaen", whereEn="National Library of Wales (NLW MS 6680B)", whereCy="Llyfrgell Genedlaethol Cymru (LlGC 6680B)",
   pic=("Hendregadredd Manuscript-small.jpg", "National Library of Wales", *PD, "A page of the Hendregadredd Manuscript", "Tudalen o Lawysgrif Hendregadredd", 376, 500),
   pic2=("Hywel vab Ewein, NLW MS 6680B f. 124r.png", "Medieval scribe", *PD, "‘Hywel vab Ewein’: the name of the poet-prince Hywel ab Owain Gwynedd in red, above one of his love poems", "‘Hywel vab Ewein’: enw’r tywysog-fardd Hywel ab Owain Gwynedd mewn coch, uwchben un o’i gerddi serch", 1955, 256),
   en_t="The great treasury of the Poets of the Princes, begun about 1300, probably at Strata Florida, and added to by many hands. Without it most of the poetry of Meilyr, Gwalchmai, Cynddelw and their fellows would be lost. It was lost to scholars itself for centuries, until it was found in 1910 in a wardrobe at the house of Hendregadredd in Eifionydd. The National Library bought it in 1923. Some scholars believe that a few of its later pages are in the hand of Dafydd ap Gwilym himself.",
   cy_t="Trysorfa fawr Beirdd y Tywysogion, a ddechreuwyd tua 1300, yn Ystrad Fflur yn ôl pob tebyg, ac yr ychwanegodd llawer llaw ati. Hebddi byddai’r rhan fwyaf o farddoniaeth Meilyr, Gwalchmai, Cynddelw a’u cymheiriaid ar goll. Bu ar goll i ysgolheigion ei hun am ganrifoedd, nes ei chael yn 1910 mewn wardrob yn nhŷ Hendregadredd yn Eifionydd. Prynodd y Llyfrgell Genedlaethol hi yn 1923. Cred rhai ysgolheigion fod ambell un o’i thudalennau diweddarach yn llaw Dafydd ap Gwilym ei hun."),
  dict(id="laws", en="The books of the law", cy="Llyfrau’r gyfraith", date="13th century onwards", dateCy="o’r drydedd ganrif ar ddeg ymlaen", whereEn="National Library of Wales and other libraries", whereCy="Llyfrgell Genedlaethol Cymru a llyfrgelloedd eraill",
   pic="trea-laws-hywel",
   en_t="About forty medieval books of the law of Hywel Dda survive, in Welsh and in Latin, small enough for a judge to carry. They set out the law of the land, the rights of women and children, the worth of every animal and the place of the king’s officers, from the chief poet to the court physician.",
   cy_t="Mae tua deugain o lyfrau canoloesol cyfraith Hywel Dda wedi goroesi, yn Gymraeg ac yn Lladin, yn ddigon bach i ynad eu cario. Maent yn gosod cyfraith y wlad, hawliau gwragedd a phlant, gwerth pob anifail a lle swyddogion y brenin, o’r pencerdd i feddyg y llys.",
   link=("laws.html#manuscripts", "The Laws of Hywel Dda and their manuscripts", "Cyfraith Hywel Dda a’i llawysgrifau")),
  dict(id="brut-tywysogion", en="Brut y Tywysogion, the Chronicle of the Princes", cy="Brut y Tywysogion", date="13th–14th century", dateCy="y drydedd a’r bedwaredd ganrif ar ddeg", whereEn="National Library of Wales; the Red Book of Hergest", whereCy="Llyfrgell Genedlaethol Cymru; Llyfr Coch Hergest",
   pic=("Brut y Tywysogion Cyfres y Fil (Porth Ystrad Fflur).jpg", "From O. M. Edwards’s edition (1913)", *PD, "The great west door of Strata Florida, where the chronicle was kept, from O. M. Edwards’s edition of Brut y Tywysogion", "Drws mawr gorllewinol Ystrad Fflur, lle cadwyd y cronicl, o argraffiad O. M. Edwards o Frut y Tywysogion", 986, 865),
   en_t="The history of Wales year by year, from the death of Cadwaladr in 682 to the fall of Llywelyn ap Gruffudd in 1282, told by the monks of Wales. It is a Welsh translation of a Latin chronicle kept at Strata Florida, and it survives in three versions. Much of what we know of the princes, their battles, their castles and their deaths comes from its pages.",
   cy_t="Hanes Cymru flwyddyn wrth flwyddyn, o farw Cadwaladr yn 682 hyd gwymp Llywelyn ap Gruffudd yn 1282, wedi’i adrodd gan fynachod Cymru. Cyfieithiad Cymraeg ydyw o gronicl Lladin a gadwyd yn Ystrad Fflur, ac mae wedi goroesi mewn tri fersiwn. O’i dudalennau y daw llawer o’r hyn a wyddom am y tywysogion, eu brwydrau, eu cestyll a’u marwolaethau.",
   link=("kings.html", "Kings and princes of Wales", "Brenhinoedd a thywysogion Cymru")),
  dict(id="brut-brenhinedd", en="Brut y Brenhinedd, the History of the Kings", cy="Brut y Brenhinedd", date="13th century onwards", dateCy="o’r drydedd ganrif ar ddeg ymlaen", whereEn="Dozens of copies, in many libraries", whereCy="Dwsinau o gopïau, mewn llawer llyfrgell",
   pic="person-maelgwn-gwynedd",
   en_t="The Welsh versions of the History of the Kings of Britain, written about 1136 by Geoffrey of Monmouth, who said that he had turned into Latin ‘a very old book in the British tongue’. It tells the story of the Island from Brutus to Cadwaladr, of Lear and Cymbeline, of Macsen, Gwrtheyrn and Arthur. No book was copied more often in medieval Wales.",
   cy_t="Y fersiynau Cymraeg o Hanes Brenhinoedd Prydain, a ysgrifennwyd tua 1136 gan Sieffre o Fynwy, a ddywedodd iddo droi i’r Lladin ‘hen lyfr yn yr iaith Frythoneg’. Mae’n adrodd hanes yr Ynys o Frutus hyd Gadwaladr, am Lŷr a Chynfelyn, am Facsen, Gwrtheyrn ac Arthur. Ni chopïwyd unrhyw lyfr yn amlach yng Nghymru’r Oesoedd Canol."),
 ]),
 dict(id="print", en="The first printed books", cy="Y llyfrau printiedig cyntaf", books=[
  dict(id="yny", en="Yny lhyvyr hwnn", cy="Yny lhyvyr hwnn", date="1546", dateCy="1546", whereEn="National Library of Wales", whereCy="Llyfrgell Genedlaethol Cymru",
   pic=("Yny Lhyvyr hwnn title page.jpg", "Sir John Price", *CC0, "The title page of Yny lhyvyr hwnn, 1546, the first book printed in Welsh", "Wyneb-ddalen Yny lhyvyr hwnn, 1546, y llyfr cyntaf a argraffwyd yn Gymraeg", 1450, 2253),
   en_t="The first book printed in Welsh, by Sir John Price of Brecon: the alphabet, a calendar, the Creed, the Lord’s Prayer, the Ten Commandments and other lessons, so that his people need not be without them in their own tongue. Its title is simply its first words, ‘In this book’.",
   cy_t="Y llyfr cyntaf a argraffwyd yn Gymraeg, gan Syr John Prys o Aberhonddu: yr wyddor, calendr, y Credo, Gweddi’r Arglwydd, y Deg Gorchymyn a gwersi eraill, fel na fyddai ei bobl hebddynt yn eu hiaith eu hunain. Ei deitl yn syml yw ei eiriau cyntaf, ‘Yn y llyfr hwn’.",
   link=("person-john-price.html", "Sir John Price", "Syr John Prys")),
  dict(id="testament", en="The New Testament and Prayer Book", cy="Y Testament Newydd a’r Llyfr Gweddi", date="1567", dateCy="1567", whereEn="", whereCy="",
   pic=None,
   en_t="The work of William Salesbury of Llansannan, with Bishop Richard Davies of St Davids and Thomas Huet, the precentor of St Davids, who translated the Book of Revelation. For the first time the people of Wales could hear the whole of the New Testament read in their own language in church.",
   cy_t="Gwaith William Salesbury o Lansannan, gyda’r Esgob Richard Davies o Dyddewi a Thomas Huet, cantor Tyddewi, a gyfieithodd Lyfr y Datguddiad. Am y tro cyntaf gallai pobl Cymru glywed y Testament Newydd cyfan yn cael ei ddarllen yn eu hiaith eu hunain yn yr eglwys.",
   link=("person-william-salesbury.html", "William Salesbury", "William Salesbury")),
  dict(id="bible", en="William Morgan’s Bible", cy="Beibl William Morgan", date="1588", dateCy="1588", whereEn="", whereCy="",
   pic="trea-bible-1588",
   en_t="The whole Bible in Welsh, translated by William Morgan, vicar of Llanrhaeadr-ym-Mochnant and later Bishop of St Asaph, and printed in London in 1588, the year of the Armada. A copy was placed in every parish church. Its language became the standard of written Welsh, and many believe it saved the language.",
   cy_t="Y Beibl cyfan yn Gymraeg, wedi’i gyfieithu gan William Morgan, ficer Llanrhaeadr-ym-Mochnant ac yn ddiweddarach Esgob Llanelwy, a’i argraffu yn Llundain yn 1588, blwyddyn yr Armada. Gosodwyd copi ym mhob eglwys blwyf. Daeth ei iaith yn safon y Gymraeg ysgrifenedig, a chred llawer iddo achub yr iaith.",
   link=("person-william-morgan.html", "William Morgan", "William Morgan")),
  dict(id="bardd-cwsc", en="Gweledigaetheu y Bardd Cwsc", cy="Gweledigaetheu y Bardd Cwsc", date="1703", dateCy="1703", whereEn="", whereCy="",
   pic=("WYNNE, Ellis (1671-1734). Gweledigaetheu y bardd cwsc. London; E. Powell, 1703.jpg", "Ellis Wynne; photograph by Christie’s", *PD, "The title page of the first edition of the Visions of the Sleeping Bard, 1703", "Wyneb-ddalen argraffiad cyntaf Gweledigaetheu y Bardd Cwsc, 1703", 1873, 3200),
   en_t="The Visions of the Sleeping Bard, by Ellis Wynne of Y Lasynys, near Harlech. A sleeping poet is carried by an angel through the world, death and the underworld, and sees the follies of the age. Rich, lively and full of the speech of Meirionnydd, it is counted among the masterpieces of Welsh prose.",
   cy_t="Gwaith Ellis Wynne o’r Lasynys, ger Harlech. Cludir bardd sy’n cysgu gan angel drwy’r byd, angau ac uffern, a gwêl ffolinebau’r oes. Yn gyfoethog, yn fywiog ac yn llawn o iaith Meirionnydd, fe’i cyfrifir ymhlith campweithiau rhyddiaith Gymraeg.",
   link=("person-ellis-wynne.html", "Ellis Wynne", "Ellis Wynne")),
  dict(id="drych", en="Drych y Prif Oesoedd", cy="Drych y Prif Oesoedd", date="1716", dateCy="1716", whereEn="", whereCy="",
   pic=("Drych y Prif Oesoedd Ab Owen (Carreg Arthur, Abertawe).jpg", "From O. M. Edwards’s edition (1896)", *PD, "Carreg Arthur on Gower, from O. M. Edwards’s edition of Drych y Prif Oesoedd", "Carreg Arthur ar Benrhyn Gŵyr, o argraffiad O. M. Edwards o Ddrych y Prif Oesoedd", 718, 1186),
   en_t="The Mirror of the First Ages, by Theophilus Evans of Llangamarch: the story of the Welsh from the beginning, of the Britons, their kings and their faith, told with fire and pride. It was read in Welsh homes for two hundred years.",
   cy_t="Gwaith Theophilus Evans o Langamarch: hanes y Cymry o’r dechrau, am y Brythoniaid, eu brenhinoedd a’u ffydd, wedi’i adrodd â thân a balchder. Fe’i darllenwyd ar aelwydydd Cymru am ddau gan mlynedd.",
   link=("person-theophilus-evans.html", "Theophilus Evans", "Theophilus Evans")),
  dict(id="myvyrian", en="The Myvyrian Archaiology of Wales", cy="The Myvyrian Archaiology of Wales", date="1801–1807", dateCy="1801–1807", whereEn="", whereCy="",
   pic=None,
   en_t="Three great volumes in which Owain Myfyr, Iolo Morganwg and William Owen Pughe printed the old poetry and prose of Wales for the first time, from Taliesin and Aneirin to the Poets of the Princes, the chronicles and the Triads. Owain Myfyr, a London furrier from Llanfihangel Glyn Myfyr, paid for it all.",
   cy_t="Tair cyfrol fawr lle argraffodd Owain Myfyr, Iolo Morganwg a William Owen Pughe hen farddoniaeth a rhyddiaith Cymru am y tro cyntaf, o Daliesin ac Aneirin i Feirdd y Tywysogion, y croniclau a’r Trioedd. Owain Myfyr, crwynwr o Lanfihangel Glyn Myfyr yn Llundain, a dalodd am y cyfan.",
   link=("story-iolo.html", "Iolo Morganwg", "Iolo Morganwg")),
 ]),
]

WHERE_EN = [
 "## Where to see them",
 "The National Library of Wales in Aberystwyth keeps the Black Book of Carmarthen, the Books of Aneirin and Taliesin, the White Book of Rhydderch, the Hendregadredd Manuscript, the Book of Llandaf and many of the law books. Some are often on show, and the Library has photographed every page of its great manuscripts so that anyone can read them online.",
 "The Red Book of Hergest belongs to Jesus College, Oxford, and is kept in the Bodleian Library. The Llandeilo Gospels are at Lichfield Cathedral, and the oldest copy of the History of the Britons is in the British Library in London.",
]
WHERE_CY = [
 "## Ble i’w gweld",
 "Mae Llyfrgell Genedlaethol Cymru yn Aberystwyth yn cadw Llyfr Du Caerfyrddin, Llyfrau Aneirin a Thaliesin, Llyfr Gwyn Rhydderch, Llawysgrif Hendregadredd, Llyfr Llandaf a llawer o lyfrau’r gyfraith. Mae rhai i’w gweld yn aml, ac mae’r Llyfrgell wedi tynnu llun o bob tudalen o’i llawysgrifau mawr fel y gall unrhyw un eu darllen ar-lein.",
 "Mae Llyfr Coch Hergest yn eiddo i Goleg Iesu, Rhydychen, ac fe’i cedwir yn Llyfrgell Bodley. Mae Efengylau Llandeilo yn Eglwys Gadeiriol Caerlwytgoed, ac mae’r copi hynaf o Historia Brittonum yn y Llyfrgell Brydeinig yn Llundain.",
]

# ---------------------------------------------------------------- the Welsh Triads (triads.html)
TRIADS_INTRO_EN = [
 "## What is a triad?",
 "A triad gathers three things under one title: the Three Generous Men of the Island of Britain, the Three Faithful War Bands, the Three Fortunate Concealments. The bards of Wales used them as a store for memory. Each name in a triad was a hook on which a whole story hung, and a poet who knew the triads knew the heroes and the history of the Island of Britain.",
 "The oldest collection, Trioedd Ynys Prydain, the Triads of the Island of Britain, is found in a manuscript of the thirteenth century, Peniarth 16, and in the White Book of Rhydderch and the Red Book of Hergest. What they remember is older still. The Poets of the Princes call on them in their poems, and the Mabinogion tells its listeners that a thing in the tale is ‘one of the Three Fortunate Concealments’ or ‘one of the Three Unhappy Blows’. The great modern edition, by the scholar Rachel Bromwich, first came out in 1961 and is still in print.",
 "Triads are found all through Welsh writing: in the laws of Hywel Dda, in the grammars that taught the poets their craft, in collections of wise sayings, and in Iolo Morganwg’s great gathering of the lore of Glamorgan. Other nations made triads too, the Irish among them, but none made more of them than the Welsh.",
 "## The Names of the Island of Britain",
 "Before the triads, the White Book and the Red Book give a short piece called Enwau Ynys Prydain, the Names of the Island of Britain. Its first name, before it was taken or settled, was Clas Myrddin, Myrddin’s Enclosure. After it was settled it was Y Fêl Ynys, the Island of Honey. And after it was won by Prydain son of Aedd the Great, it was called Ynys Prydain, the Island of Britain. It has three chief islands lying off it, Môn, Manaw and Wight, and three chief rivers, the Thames, the Severn and the Humber.",
]
TRIADS_INTRO_CY = [
 "## Beth yw triawd?",
 "Mae triawd yn casglu tri pheth dan un teitl: Tri Hael Ynys Prydain, Tri Diwair Deulu, Tri Matgudd. Defnyddiai beirdd Cymru hwy fel stôr i’r cof. Roedd pob enw mewn triawd yn fachyn i hongian stori gyfan arno, a gwyddai’r bardd a wyddai’r trioedd am arwyr a hanes Ynys Prydain.",
 "Ceir y casgliad hynaf, Trioedd Ynys Prydain, mewn llawysgrif o’r drydedd ganrif ar ddeg, Peniarth 16, ac yn Llyfr Gwyn Rhydderch a Llyfr Coch Hergest. Mae’r hyn a gofiant yn hŷn eto. Mae Beirdd y Tywysogion yn galw arnynt yn eu cerddi, ac mae’r Mabinogion yn dweud wrth ei wrandawyr fod peth yn y chwedl yn ‘un o’r Tri Matgudd’ neu’n ‘un o’r Tri Anfad Balfawd’. Daeth yr argraffiad modern mawr, gan yr ysgolhaig Rachel Bromwich, allan gyntaf yn 1961 ac mae mewn print o hyd.",
 "Ceir trioedd drwy holl lên Cymru: yng nghyfraith Hywel Dda, yn y gramadegau a ddysgai eu crefft i’r beirdd, mewn casgliadau o ddywediadau doeth, ac yng nghasgliad mawr Iolo Morganwg o lên Morgannwg. Gwnaeth cenhedloedd eraill drioedd hefyd, y Gwyddyl yn eu plith, ond ni wnaeth neb fwy ohonynt na’r Cymry.",
 "## Enwau Ynys Prydain",
 "Cyn y trioedd, mae’r Llyfr Gwyn a’r Llyfr Coch yn rhoi darn byr o’r enw Enwau Ynys Prydain. Ei henw cyntaf, cyn ei chymryd na’i chyfanheddu, oedd Clas Myrddin. Wedi ei chyfanheddu, Y Fêl Ynys oedd hi. Ac wedi i Brydain fab Aedd Mawr ei hennill, fe’i galwyd yn Ynys Prydain. Mae tair prif ynys yn gorwedd ger ei glannau, Môn, Manaw a Gwyth, a thair prif afon, Tafwys, Hafren a Humyr.",
]

# Each triad: Welsh title, English title, three items [(EN, CY)], and an optional "and one more" line (EN, CY)
TRIAD_GROUPS = [
 dict(en="Kings and courts", cy="Brenhinoedd a llysoedd", triads=[
  dict(cy="Tri Lleithiclwyth Ynys Prydain", en="The Three Tribal Thrones of the Island of Britain", three=[
    ("Arthur as chief prince at Mynyw, with Dewi as chief bishop and Maelgwn Gwynedd as chief elder", "Arthur yn ben teyrnedd ym Mynyw, a Dewi yn ben esgob, a Maelgwn Gwynedd yn ben hynaf"),
    ("Arthur as chief prince at Celli Wig in Cornwall, with Bishop Bytwini as chief bishop and Caradog Freichfras as chief elder", "Arthur yn ben teyrnedd yng Nghelli Wig yng Nghernyw, a’r Esgob Bytwini yn ben esgob, a Charadog Freichfras yn ben hynaf"),
    ("Arthur as chief prince at Pen Rhionydd in the North, with Cyndeyrn Garthwys as chief bishop and Gwrthmwl Wledig as chief elder", "Arthur yn ben teyrnedd ym Mhen Rhionydd yn y Gogledd, a Chyndeyrn Garthwys yn ben esgob, a Gwrthmwl Wledig yn ben hynaf"),
   ], note=("The first triad in the old collections. It names Arthur as chief prince of the whole Island, holding court at St Davids, in Cornwall and in the North.", "Y triawd cyntaf yn yr hen gasgliadau. Mae’n enwi Arthur yn ben teyrnedd yr Ynys gyfan, yn cynnal llys yn Nhyddewi, yng Nghernyw ac yn y Gogledd.")),
  dict(cy="Tri Hael Ynys Prydain", en="The Three Generous Men of the Island of Britain", three=[
    ("Nudd the Generous, son of Senyllt", "Nudd Hael mab Senyllt"),
    ("Mordaf the Generous, son of Serwan", "Mordaf Hael mab Serwan"),
    ("Rhydderch the Generous, son of Tudwal Tudglyd", "Rhydderch Hael mab Tudwal Tudglyd"),
   ], more=("And Arthur himself was more generous than the three.", "Ac Arthur ei hun oedd haelach na’r tri."),
   note=("Three princes of the Old North. Poets for a thousand years after compared their patrons to them: to be ‘as generous as Nudd’ was the highest praise.", "Tri thywysog o’r Hen Ogledd. Am fil o flynyddoedd wedyn cymharai’r beirdd eu noddwyr â hwy: bod ‘mor hael â Nudd’ oedd y mawl uchaf.")),
  dict(cy="Tair Prif Riain Llys Arthur", en="The Three Great Queens of Arthur’s Court", three=[
    ("Gwenhwyfar, daughter of Cywryd of Gwent", "Gwenhwyfar ferch Gywryd Gwent"),
    ("Gwenhwyfar, daughter of Gwythyr son of Greidiol", "Gwenhwyfar ferch Wythyr fab Greidiol"),
    ("Gwenhwyfar, daughter of Gogfran the Giant", "Gwenhwyfar ferch Ogfran Gawr"),
   ], note=("Three queens, all named Gwenhwyfar. One of them, in this triad, is a daughter of Gwent, the kingdom where Welsh tradition holds that Arthur ruled.", "Tair brenhines, a phob un yn Wenhwyfar. Mae un ohonynt, yn y triawd hwn, yn ferch o Went, y deyrnas lle, yn ôl traddodiad Cymru, y teyrnasai Arthur.")),
 ]),
 dict(en="Heroes and war bands", cy="Arwyr a gosgorddion", triads=[
  dict(cy="Tri Diwair Deulu Ynys Prydain", en="The Three Faithful War Bands of the Island of Britain", three=[
    ("The war band of Cadwallon son of Cadfan, who were with him seven years in Ireland and asked nothing of him in all that time", "Teulu Cadwallon fab Cadfan, a fu gydag ef saith mlynedd yn Iwerddon heb ofyn dim ganddo yn yr holl amser hwnnw"),
    ("The war band of Gafran son of Aeddan, who went to sea with their lord", "Teulu Gafran fab Aeddan, a aeth i’r môr gyda’u harglwydd"),
    ("The war band of Gwenddolau son of Ceidiaw at Arfderydd, who fought on for a fortnight and a month after their lord was slain", "Teulu Gwenddolau fab Ceidiaw yn Arfderydd, a ymladdodd am bythefnos a mis wedi lladd eu harglwydd"),
   ], note=("Loyalty was the highest virtue of a war band. Cadwallon came back from exile to win back Gwynedd and to become one of the greatest kings of the Britons.", "Ffyddlondeb oedd rhinwedd uchaf gosgordd. Daeth Cadwallon yn ôl o alltudiaeth i ennill Gwynedd yn ôl a dod yn un o frenhinoedd mwyaf y Brythoniaid.")),
  dict(cy="Tri Goruchel Garcharor Ynys Prydain", en="The Three Exalted Prisoners of the Island of Britain", three=[
    ("Llŷr Llediaith, imprisoned by Euroswydd", "Llŷr Llediaith, a garcharwyd gan Euroswydd"),
    ("Mabon son of Modron", "Mabon fab Modron"),
    ("Gwair son of Geirioedd", "Gwair fab Geirioedd"),
   ], more=("And one more exalted than the three: Arthur, who was three nights in prison in Caer Oeth and Anoeth, and three nights in the prison under the stone of Echymeint. And one lad set him free each time: Goreu son of Custennin, his cousin.", "Ac un a oedd yn oruchelach na’r tri: Arthur, a fu dair noson yng ngharchar yng Nghaer Oeth ac Anoeth, a thair noson yn y carchar dan lech Echymeint. Ac un gwas a’i rhyddhaodd bob tro: Goreu fab Custennin, ei gefnder."),
   note=("Mabon son of Modron is the prisoner whom Arthur’s men set free in the tale of Culhwch and Olwen, after asking the oldest animals in the world where he was.", "Mabon fab Modron yw’r carcharor a ryddhaodd gwŷr Arthur yn chwedl Culhwch ac Olwen, wedi holi anifeiliaid hynaf y byd ble’r oedd.")),
  dict(cy="Tri Gwrddfeichiad Ynys Prydain", en="The Three Powerful Swineherds of the Island of Britain", three=[
    ("Pryderi son of Pwyll, who kept the swine that came from Annwfn, the Otherworld, at Glyn Cuch in Dyfed", "Pryderi fab Pwyll, a gadwai’r moch a ddaeth o Annwn yng Nglyn Cuch yn Nyfed"),
    ("Drystan son of March, who kept the swine of March while the swineherd took a message to Esyllt", "Drystan fab March, a gadwai foch March tra aeth y meichiad â neges at Esyllt"),
    ("Coll son of Collfrewy, who kept Henwen, the great sow, and followed her across the land", "Coll fab Collfrewy, a gadwai Henwen, yr hwch fawr, a’i dilyn ar draws y wlad"),
   ], note=("Henwen swam the sea and gave the land its gifts as she went: in Gwent, the triad tells, she left a grain of wheat and a bee, and since then the best wheat has grown in Gwent. In Arfon she gave birth to a kitten, which grew into Cath Palug, the great cat of Môn.", "Nofiodd Henwen y môr a rhoi ei rhoddion i’r wlad wrth fynd: yng Ngwent, medd y triawd, gadawodd ronyn o wenith a gwenynen, ac ers hynny y gwenith gorau a dyf yng Ngwent. Yn Arfon esgorodd ar gath fach, a dyfodd yn Gath Palug, cath fawr Môn.")),
 ]),
 dict(en="The secrets of the Island", cy="Cyfrinachau’r Ynys", triads=[
  dict(cy="Tri Matgudd Ynys Prydain", en="The Three Fortunate Concealments of the Island of Britain", three=[
    ("The head of Brân the Blessed, buried in the White Hill in London with its face towards France. While it lay there, no enemy would come to this Island.", "Pen Bendigeidfran, a gladdwyd yn y Gwynfryn yn Llundain a’i wyneb tua Ffrainc. Tra byddai yno, ni ddôi gormes byth i’r Ynys hon."),
    ("The dragons that Lludd son of Beli buried at Dinas Emrys in Eryri", "Y dreigiau a gladdodd Lludd fab Beli yn Ninas Emrys yn Eryri"),
    ("The bones of Gwerthefyr the Blessed, buried in the chief harbours of the Island", "Esgyrn Gwerthefyr Fendigaid, a gladdwyd ym mhrif borthladdoedd yr Ynys"),
   ], more=("And the triad goes on: Arthur himself dug up the head of Brân, because he would have the Island defended by no strength but his own.", "Ac mae’r triawd yn mynd ymlaen: Arthur ei hun a ddatguddiodd ben Brân, am na fynnai i’r Ynys gael ei hamddiffyn gan unrhyw nerth ond ei nerth ei hun."),
   note=("The Second Branch of the Mabinogi ends with the burial of Brân’s head, and calls it the third of the Fortunate Concealments.", "Mae Ail Gainc y Mabinogi yn gorffen â chladdu pen Brân, ac yn ei alw’n drydydd o’r Tri Matgudd.")),
  dict(cy="Tri Anfad Balfawd Ynys Prydain", en="The Three Unhappy Blows of the Island of Britain", three=[
    ("The blow that Matholwch struck on Branwen", "Y balfawd a drawodd Matholwch ar Franwen"),
    ("The blow that Gwenhwyfach struck on Gwenhwyfar, from which came the battle of Camlan", "Y balfawd a drawodd Gwenhwyfach ar Wenhwyfar, ac o’i herwydd y bu gwaith Camlan"),
    ("The blow struck on Cadwaladr the Blessed", "Y balfawd a drawyd ar Gadwaladr Fendigaid"),
   ], note=("The Second Branch tells how Branwen was struck in Ireland, and how her brother Brân crossed the sea with all the Island of Britain to bring her home.", "Mae’r Ail Gainc yn adrodd sut y trawyd Branwen yn Iwerddon, a sut y croesodd ei brawd Brân y môr gydag Ynys Prydain gyfan i’w dwyn adref.")),
 ]),
]

TRIADS_MORE_EN = [
 "## The triads of the law",
 "The law books of Hywel Dda hold collections of legal triads, which set out the law in threes so that a judge could carry it in his head: rules of proof and of witnesses, of land and of family, of the worth of things and of the duties of the king’s court. Short, clear and easy to remember, they were how the law was learned and taught.",
 "## The triads of the horses",
 "One whole set, Trioedd y Meirch, names the horses of the heroes: the swift, the strong and the faithful steeds on which the warriors of the Island rode to battle. A poet needed to know them, for a fine horse given by a patron was praised as warmly as the patron himself.",
 "## Iolo Morganwg’s triads",
 "The Myvyrian Archaiology printed a great new series of triads, from the manuscripts of Glamorgan in Iolo Morganwg’s own account. They tell of Hu Gadarn, who led the Cymry to the Island of Britain from the Summer Country, of the three pillars of the nation, and of the wisdom of the bards. Read and loved across Wales all through the nineteenth century, they gave the Gorsedd much of its language, and its motto, Y Gwir yn erbyn y Byd, the Truth against the World.",
 "## Make your own triad",
 "Try it: choose a title and three things that belong under it. Three best things about my town. Three people I would invite to a feast. Three places in Wales I want to see. It is how the bards trained their memories, and how they taught the young poets who came after them.",
]
TRIADS_MORE_CY = [
 "## Trioedd y gyfraith",
 "Mae llyfrau cyfraith Hywel Dda yn cadw casgliadau o drioedd cyfreithiol, sy’n gosod y gyfraith fesul tri er mwyn i ynad ei chario yn ei ben: rheolau prawf a thystion, tir a theulu, gwerth pethau a dyletswyddau llys y brenin. Yn fyr, yn glir ac yn hawdd eu cofio, dyma sut y dysgid y gyfraith.",
 "## Trioedd y Meirch",
 "Mae un set gyfan, Trioedd y Meirch, yn enwi meirch yr arwyr: y meirch chwim, cryf a ffyddlon y marchogai rhyfelwyr yr Ynys arnynt i’r frwydr. Roedd yn rhaid i fardd eu hadnabod, oherwydd câi march gwych a roddwyd gan noddwr ei foli mor gynnes â’r noddwr ei hun.",
 "## Trioedd Iolo Morganwg",
 "Argraffodd y Myvyrian Archaiology gyfres fawr newydd o drioedd, o lawysgrifau Morgannwg yn ôl tystiolaeth Iolo Morganwg ei hun. Maent yn sôn am Hu Gadarn, a arweiniodd y Cymry i Ynys Prydain o Wlad yr Haf, am dair colofn y genedl, ac am ddoethineb y beirdd. Fe’u darllenwyd a’u caru ledled Cymru drwy’r bedwaredd ganrif ar bymtheg, a rhoesant i’r Orsedd lawer o’i hiaith, a’i harwyddair, Y Gwir yn erbyn y Byd.",
 "## Gwnewch eich triawd eich hun",
 "Rhowch gynnig arni: dewiswch deitl a thri pheth sy’n perthyn iddo. Tri pheth gorau am fy nhref. Tri pherson y byddwn yn eu gwahodd i wledd. Tri lle yng Nghymru yr hoffwn eu gweld. Dyna sut yr hyfforddai’r beirdd eu cof, a sut y dysgent y beirdd ifanc a ddaeth ar eu hôl.",
]

# The full page of the White Book shown beside the last part of the Triads page
WHITE_BOOK_PAGE = ("Llyfr Gwyn Rhydderch f.61.r.png", "Unknown medieval scribe", *CC0, "A page of the White Book of Rhydderch, about 1350, one of the books that keep the Triads", "Tudalen o Lyfr Gwyn Rhydderch, tua 1350, un o’r llyfrau sy’n cadw’r Trioedd", 1597, 2370)
