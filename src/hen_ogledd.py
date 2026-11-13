# Yr Hen Ogledd, the Old North (November 2026): the long read story-hen-ogledd.html, new pages for the Men of the North
# who had none, fuller pages for Urien Rheged, Aneirin and Cunedda, the map of the Old North and the "Men of the North"
# block on each of their pages.
# Asked for by Ifan, 13 November 2026: "Add a page on Yr Hen Ogledd (The Old North)".
#
# House rules (EDITORIAL.md): proud; nothing negative about the people of Welsh history; the people are Britons and
# Cymry, never "Celts"; kings are kings (every ruler of an Old North kingdom is a king); Arthur is a king, and Welsh
# tradition holds that he was Athrwys ap Meurig; traditions in their own words.
#
# What is here:
#   LONG     slug -> (English paragraphs, Welsh paragraphs): full texts for people already on the site.
#   PEOPLE   new people, in the people2a.py format (people2.py adds them to the site).
#   GROUPS   the "Men of the North" block on each of their pages (build.py, north_circle()).
#   LINKS    the pages that go with the block.
#   MAP      the numbered map of the Old North under the long read (build.py, north_map(); outline in src/geo/north.json,
#            made by tools/north_map.py). REGIONS are the kingdom names drawn on it, ROUTES the journeys south.
#   STORY    the long read story-hen-ogledd.html (features.py adds it to the long reads).
#   REFS     its reading list (build.py merges it into refs.REFS).
#   CITES    the sources beside the claims used here (cites.py adds them to its list).
#
# Sources used and checked (November 2026):
#   Historia Brittonum, tr. J. A. Giles (Project Gutenberg 1972): ch. 57 Oswiu's wife "Riemmelth, the daughter of Royth,
#   son of Rum"; ch. 62 the five poets (Talhaiarn, Neirin, Taliesin, Bluchbard, Cian "who is called Guenith Guaut") and
#   Cunedda coming from Manau Guotodin 146 years before Maelgwn and driving out the Scots; ch. 63 "Against him fought four
#   kings, Urien, and Ryderthen, and Guallauc, and Morcant", Theodric shut up "three days and three nights in the island
#   of Metcaut", Urien slain through envy of his skill in war, "Edwin ... seized on Elmete, and expelled Cerdic, its king",
#   and "it was Rum Map Urbgen" who baptised Edwin and his people.
#   Annales Cambriae (Fordham Medieval Sourcebook): 573 Arfderydd, Gwenddolau fell; 580 Gwrgi and Peredur sons of Eliffer
#   died; 595 death of king Dunod son of Pabo; 613 Chester, Selyf son of Cynan; 616 Ceredig died; 870 "The fortress of
#   Alt Clud was broken by the gentiles".
#   Annals of Ulster (Corpus of Electronic Texts, UCC): U638.1 "the besieging of Eten"; U642.1 Domnall Brecc slain "in the battle of Srath Caruin, by
#   Hoan, king of the Britons"; U870 the siege of Ail Cluaithe by Amlaíb and Ímar, four months.
#   Bonedd Gwŷr y Gogledd (Peniarth 45, late 13th century; maryjones.us): the pedigrees of Urien, Llywarch Hen, Clydno
#   Eidyn, Dunawd, Gwrgi and Peredur, Gwenddolau (with Nudd and Cof), Rhydderch Hael, Mordaf and Elffin, and "the 300
#   swords of the Cynferchyn, and the 300 shields of the Cynwydion, and the 300 spears of the Coeling".
#   Wikipedia: Urien ("gweleis i lyw katraeth tra maeu", "I saw the lord of Catraeth across the plains", Yspeil Taliesin;
#   "penn a borthaf" in the Urien cycle); Cumbric (Lanark = llannerch, Penrith = pen + rhyd, Bathgate, Penicuik, Ecclefechan
#   = eglwys, Blencathra = blaen; Cumbric gone by about the 12th century; the counting scores); Aeron; Battle of Arfderydd
#   (Three Faithful Warbands; Three Futile Battles); Thirteen Treasures of the Island of Britain; Talhaearn Tad Awen; Owain
#   Foel ("rex Clutinensium", Carham 1018); Govan Stones; Dunod Fawr (father of Deiniol, Three Pillars of Battle).
#   Canmore (Historic Environment Scotland), the Yarrow Stone: early 6th century, "the most famous princes Nudus and
#   Dumnogenus ... sons of Liberalis".
#   Gillian Clarke, The Gododdin: Lament for the Fallen (Faber, 2021).
from people2a import P

# ---------------------------------------------------------------- full pages for people already on the site
LONG = {
 "urien-rheged": ([
  "Urien son of Cynfarch was king of Rheged in the second half of the sixth century, and the greatest of the Men of the North. His kingdom lay around the Solway Firth and Caer Liwelydd, Carlisle, and his people spoke the language that became Welsh. The old pedigree of the Men of the North traces his line back through Cynfarch and Meirchion to Coel Hen.[[cite:ho-bonedd]]",
  "## The king of Taliesin’s poems",
  "Taliesin, the first poet of the Welsh language whose words still live, was Urien’s poet. Eight of the oldest poems in the Book of Taliesin were made for him.[[cite:ho-urien-wiki,nlw-taliesin]] They call him the lord of Rheged, of Erechwydd and of Catraeth, a lion in battle and a giver of gold, horses and mead. In Gwaith Gwen Ystrad the men of Catraeth rise at dawn around their king; in Gwaith Argoed Llwyfain he and his son Owain answer the enemy’s demand for hostages with their swords. ‘I saw the lord of Catraeth across the plains,’ the poet sings.",
  "> Ac yny vallwyf i hen, ym dygyn agheu aghen, ny bydif ym dirwen na molwyf i Vryen. | Taliesin: the refrain of the poems to Urien, Book of Taliesin",
  "The refrain means: until I grow old and die in death’s hard need, I shall never be glad unless I praise Urien.",
  "## Lindisfarne",
  "The History of the Britons, gathered in Gwynedd about 829, tells how four kings of the Britons, Urien, Rhydderch Hael, Gwallog and Morgant, fought the Angles of Bernicia, and how Urien and his sons shut the Angles up on the island of Metcaut, Lindisfarne, for three days and three nights.[[cite:ho-hb]] It was the nearest the Britons of the North came to driving the newcomers into the sea. Urien did not fall to the Angles. He was struck down by treachery during the campaign, the History says, out of envy, because his skill in war was greater than any other king’s.",
  "## The head of Urien",
  "The poets of Wales mourned him for centuries. In the old englynion of the Urien cycle a warrior carries his lord’s head home from the battlefield so that no enemy can shame it: ‘Penn a borthaf,’ he says, ‘I carry a head’, the head of the man who cared for him.[[cite:ho-urien-wiki]] His son Owain ruled after him and became one of the great heroes of Welsh story, and Urien himself went on into the romances of Europe as King Uriens. When later poets wanted to praise a prince of Wales, they compared him to Urien.",
 ], [
  "Urien fab Cynfarch oedd brenin Rheged yn ail hanner y chweched ganrif, a’r mwyaf o Wŷr y Gogledd. Gorweddai ei deyrnas o gwmpas Moryd Solway a Chaer Liwelydd, Carlisle, a siaradai ei bobl yr iaith a drodd yn Gymraeg. Mae hen ach Gwŷr y Gogledd yn olrhain ei linach yn ôl drwy Gynfarch a Meirchion at Goel Hen.[[cite:ho-bonedd]]",
  "## Brenin cerddi Taliesin",
  "Taliesin, bardd cyntaf yr iaith Gymraeg y mae ei eiriau’n fyw o hyd, oedd bardd Urien. Lluniwyd wyth o’r cerddi hynaf yn Llyfr Taliesin iddo ef.[[cite:ho-urien-wiki,nlw-taliesin]] Maent yn ei alw’n arglwydd Rheged, Erechwydd a Chatraeth, yn llew mewn brwydr ac yn rhoddwr aur, meirch a medd. Yng Ngwaith Gwen Ystrad mae gwŷr Catraeth yn codi gyda’r wawr o gwmpas eu brenin; yng Ngwaith Argoed Llwyfain mae ef a’i fab Owain yn ateb cais y gelyn am wystlon â’u cleddyfau. ‘Gwelais i lyw Catraeth tra maes,’ medd y bardd.",
  "> Ac yny vallwyf i hen, ym dygyn agheu aghen, ny bydif ym dirwen na molwyf i Vryen. | Taliesin: byrdwn y cerddi i Urien, Llyfr Taliesin",
  "Ystyr y byrdwn yw: hyd nes i mi heneiddio a marw yn angen caled angau, ni fyddaf fyth yn llawen oni folaf i Urien.",
  "## Ynys Fedcawd",
  "Mae Hanes y Brythoniaid, a gasglwyd yng Ngwynedd tua 829, yn adrodd sut yr ymladdodd pedwar o frenhinoedd y Brythoniaid, Urien, Rhydderch Hael, Gwallog a Morgant, yn erbyn Eingl Brynaich, a sut y caeodd Urien a’i feibion yr Eingl ar ynys Metcaut, Lindisfarne, am dri diwrnod a thair noson.[[cite:ho-hb]] Dyna’r agosaf y daeth Brythoniaid y Gogledd at yrru’r dyfodiaid i’r môr. Nid i’r Eingl y syrthiodd Urien. Fe’i trawyd i lawr drwy frad yn ystod yr ymgyrch, medd yr Hanes, o genfigen, am fod ei ddawn mewn rhyfel yn fwy na dawn unrhyw frenin arall.",
  "## Pen Urien",
  "Galarodd beirdd Cymru amdano am ganrifoedd. Yn hen englynion cylch Urien mae rhyfelwr yn cario pen ei arglwydd adref o faes y gad fel na all unrhyw elyn ei gywilyddio: ‘Pen a borthaf,’ meddai, pen y gŵr a ofalodd amdano.[[cite:ho-urien-wiki]] Teyrnasodd ei fab Owain ar ei ôl a dod yn un o arwyr mawr chwedlau Cymru, ac aeth Urien ei hun ymlaen i ramantau Ewrop fel y Brenin Uriens. Pan fynnai beirdd diweddarach ganmol un o dywysogion Cymru, cymharent ef ag Urien.",
 ]),
 "aneirin": ([
  "Aneirin is the poet of Y Gododdin, the great elegy for the warriors who rode from Din Eidyn, Edinburgh, to Catraeth about the year 600. It is the oldest poetry of Britain in a language still spoken, and it was made in the Old North, in the British kingdom of Gododdin around the Firth of Forth.",
  "## One of the five poets",
  "The History of the Britons, gathered in Gwynedd about 829, names him among the five poets who were famous in British verse in the sixth century: Talhaearn Tad Awen, Neirin, Taliesin, Blwchfardd and Cian, ‘who is called Gwenith Gwawd’.[[cite:ho-hb]] Neirin is the old spelling of Aneirin. In Welsh tradition he became Aneirin Gwawdrydd, Aneirin of the flowing verse, and the Triads remember him among the great bards of the Island of Britain.",
  "## The poem",
  "Y Gododdin honours the war band of Mynyddog Mwynfawr, lord of Din Eidyn, who feasted them for a year on mead and then sent them south against the Angles of Deira and Bernicia at Catraeth, Catterick. Verse by verse, Aneirin names each hero and praises his courage: Cynon son of Clydno, Gwawrddur, who fed black ravens on the rampart ‘though he was no Arthur’, Tudfwlch, Cadwal, and many more.",
  "> Gwŷr a aeth Gatraeth, oedd ffraeth eu llu; glasfedd eu hancwyn, a gwenwyn fu. | Aneirin, Y Gododdin",
  "‘Men went to Catraeth, swift was their host; fresh mead was their feast, and it was poison.’ The poem tells that of all who rode out, only a handful came home, and the poet himself was one of them, to sing their names.",
  "## The Book of Aneirin",
  "The poem was carried south to Wales and kept by the bards for more than six centuries. It was written down in the Book of Aneirin, a small book of thirty-eight pages copied in the second half of the thirteenth century, which is now in the National Library of Wales.[[cite:nlw-aneirin]] The great scholar Sir Ifor Williams edited it in Canu Aneirin in 1938, and in 2021 Gillian Clarke, the former National Poet of Wales, gave it new life in English as The Gododdin: Lament for the Fallen.[[cite:ho-clarke]]",
 ], [
  "Aneirin yw bardd Y Gododdin, y farwnad fawr i’r rhyfelwyr a farchogodd o Ddin Eidyn, Caeredin, i Gatraeth tua’r flwyddyn 600. Dyma’r farddoniaeth hynaf ym Mhrydain mewn iaith a siaredir o hyd, ac fe’i lluniwyd yn yr Hen Ogledd, yn nheyrnas Frythonig Gododdin o gwmpas Moryd Forth.",
  "## Un o’r pum bardd",
  "Mae Hanes y Brythoniaid, a gasglwyd yng Ngwynedd tua 829, yn ei enwi ymhlith y pum bardd a oedd yn enwog mewn barddoniaeth Frythoneg yn y chweched ganrif: Talhaearn Tad Awen, Neirin, Taliesin, Blwchfardd a Chian, ‘a elwir Gwenith Gwawd’.[[cite:ho-hb]] Neirin yw hen ffurf yr enw Aneirin. Yn nhraddodiad Cymru daeth yn Aneirin Gwawdrydd, Aneirin y mydr llifeiriol, ac mae’r Trioedd yn ei gofio ymhlith beirdd mawr Ynys Prydain.",
  "## Y gerdd",
  "Mae’r Gododdin yn anrhydeddu gosgordd Mynyddog Mwynfawr, arglwydd Din Eidyn, a’u gwleddodd am flwyddyn ar fedd ac yna eu hanfon i’r de yn erbyn Eingl Deifr a Brynaich yng Nghatraeth, Catterick. Pennill wrth bennill, mae Aneirin yn enwi pob arwr ac yn canmol ei wroldeb: Cynon fab Clydno, Gwawrddur, a borthai frain duon ar fur y gaer ‘ceni bei ef Arthur’, Tudfwlch, Cadwal, a llawer mwy.",
  "> Gwŷr a aeth Gatraeth, oedd ffraeth eu llu; glasfedd eu hancwyn, a gwenwyn fu. | Aneirin, Y Gododdin",
  "Mae’r gerdd yn adrodd mai dim ond dyrnaid o’r holl rai a farchogodd allan a ddaeth adref, a bod y bardd ei hun yn un ohonynt, i ganu eu henwau.",
  "## Llyfr Aneirin",
  "Cariwyd y gerdd i’r de i Gymru a’i chadw gan y beirdd am fwy na chwe chanrif. Fe’i hysgrifennwyd yn Llyfr Aneirin, llyfr bach o dri deg wyth o dudalennau a gopïwyd yn ail hanner y drydedd ganrif ar ddeg, ac sydd heddiw yn Llyfrgell Genedlaethol Cymru.[[cite:nlw-aneirin]] Golygodd yr ysgolhaig mawr Syr Ifor Williams hi yn Canu Aneirin yn 1938, ac yn 2021 rhoddodd Gillian Clarke, cyn-Fardd Cenedlaethol Cymru, fywyd newydd iddi yn Saesneg fel The Gododdin: Lament for the Fallen.[[cite:ho-clarke]]",
 ]),
 "cunedda": ([
  "Cunedda Wledig is the founder of the royal house of Gwynedd, and the link that binds Wales to the Old North. He came from Manaw Gododdin, the land around the head of the Firth of Forth, where the names Clackmannan and Slamannan still carry the old name Manaw.",
  "## The coming south",
  "The History of the Britons, gathered in Gwynedd about 829, tells that Cunedda came from Manaw Gododdin with his sons a hundred and forty-six years before Maelgwn Gwynedd reigned, and drove the Irish out of the land with great slaughter, so that they never came back to live there.[[cite:ho-hb]] Welsh tradition dates his coming to the fifth century, when the legions had gone and the Britons of the North and of Wales stood together.",
  "## The sons of Cunedda",
  "His sons and grandsons gave their names to the lands they won, and the map of Wales still carries them: Ceredig to Ceredigion, Meirion to Meirionnydd, Edern to Edeirnion, Dunod to Dunoding, Rhufon to Rhufoniog, Dogfael to Dogfeiling, Einion to Caereinion. The Triads count his family, with those of Brychan and Caw, as one of the Three Saintly Lineages of the Island of Britain.",
  "## Every prince of Gwynedd",
  "From Cunedda came Cadwallon Lawhir, who won back Ynys Môn, and Maelgwn Gwynedd, the greatest king of his age. When Merfyn Frych took the throne in 825 he did so through his mother Esyllt, of Cunedda’s line, and so Rhodri Mawr, Hywel Dda, Gruffudd ap Cynan, Owain Gwynedd, Llywelyn the Great and Llywelyn the Last all counted Cunedda of Manaw Gododdin as their forefather.",
 ], [
  "Cunedda Wledig yw sylfaenydd tŷ brenhinol Gwynedd, a’r ddolen sy’n clymu Cymru wrth yr Hen Ogledd. Daeth o Fanaw Gododdin, y wlad o gwmpas pen Moryd Forth, lle mae’r enwau Clackmannan a Slamannan yn cadw’r hen enw Manaw o hyd.",
  "## Y dyfodiad i’r de",
  "Mae Hanes y Brythoniaid, a gasglwyd yng Ngwynedd tua 829, yn adrodd i Gunedda ddod o Fanaw Gododdin gyda’i feibion gant pedwar deg a chwech o flynyddoedd cyn teyrnasiad Maelgwn Gwynedd, a gyrru’r Gwyddelod o’r wlad â lladdfa fawr, fel na ddaethant fyth yn ôl i fyw yno.[[cite:ho-hb]] Mae traddodiad Cymru’n gosod ei ddyfodiad yn y bumed ganrif, pan oedd y llengoedd wedi mynd a Brythoniaid y Gogledd a Chymru’n sefyll ynghyd.",
  "## Meibion Cunedda",
  "Rhoddodd ei feibion a’i wyrion eu henwau i’r tiroedd a enillasant, ac mae map Cymru’n eu cadw o hyd: Ceredig i Geredigion, Meirion i Feirionnydd, Edern i Edeirnion, Dunod i Ddunoding, Rhufon i Rufoniog, Dogfael i Ddogfeiling, Einion i Gaereinion. Mae’r Trioedd yn cyfrif ei deulu, gyda theuluoedd Brychan a Chaw, yn un o Dair Gwelygordd Saint Ynys Prydain.",
  "## Pob tywysog o Wynedd",
  "O Gunedda y daeth Cadwallon Lawhir, a enillodd Ynys Môn yn ôl, a Maelgwn Gwynedd, brenin mwyaf ei oes. Pan gymerodd Merfyn Frych yr orsedd yn 825 gwnaeth hynny drwy ei fam Esyllt, o linach Cunedda, ac felly roedd Rhodri Mawr, Hywel Dda, Gruffudd ap Cynan, Owain Gwynedd, Llywelyn Fawr a Llywelyn ein Llyw Olaf i gyd yn cyfrif Cunedda o Fanaw Gododdin yn gyndad iddynt.",
 ]),
}

# ---------------------------------------------------------------- new people
PEOPLE = [
 P("cynfarch-oer", "saints", "fl. mid 6th century", "Cynfarch Oer", "Cynfarch Oer", "King in the North, father of Urien", "Brenin yn y Gogledd, tad Urien", "Cynfarch_Oer", "rulers",
   "A king of the Men of the North, father of Urien Rheged. His descendants, the Cynferching, were famed in the old pedigree for their three hundred swords.",
   "Brenin o Wŷr y Gogledd, tad Urien Rheged. Roedd ei ddisgynyddion, y Cynferching, yn enwog yn yr hen ach am eu trichant cleddyf.",
   ["Cynfarch son of Meirchion was a king of the Britons of the North in the middle of the sixth century, of the line of Coel Hen, and the father of Urien, king of Rheged.[[cite:ho-bonedd]] His name means something like ‘chief horse’, a fitting name for a lord of horsemen.",
    "His family were called after him, the Cynferching, and the old pedigree of the Men of the North sets them beside two other great houses of the North: ‘The three hundred swords of the Cynferchyn, and the three hundred shields of the Cynwydion, and the three hundred spears of the Coeling: whatever errand they went on together, it never failed.’[[cite:ho-bonedd]]"],
   ["Roedd Cynfarch fab Meirchion yn frenin ar Frythoniaid y Gogledd yng nghanol y chweched ganrif, o linach Coel Hen, ac yn dad i Urien, brenin Rheged.[[cite:ho-bonedd]]",
    "Galwyd ei deulu ar ei ôl, y Cynferching, ac mae hen ach Gwŷr y Gogledd yn eu gosod ochr yn ochr â dau dŷ mawr arall o’r Gogledd: ‘Trichant cleddyf Cynferchyn, a thrichant ysgwyd Cynwydion, a thrichant gwaew Coeling: pa neges bynnag yr elynt iddi yn gytûn, ni fethai honno.’[[cite:ho-bonedd]]"]),
 P("rhun-ab-urien", "saints", "fl. early 7th century", "Rhun ab Urien", "Rhun ab Urien", "Son of Urien, who baptised King Edwin", "Mab Urien, a fedyddiodd y Brenin Edwin", "Rhun_ab_Urien", "faith",
   "Son of Urien Rheged. The History of the Britons names him as the man who baptised Edwin, king of Northumbria, and his people, and his great-granddaughter Rhiainfellt became queen of Northumbria.",
   "Mab Urien Rheged. Mae Hanes y Brythoniaid yn ei enwi fel y gŵr a fedyddiodd Edwin, brenin Northumbria, a’i bobl, a daeth ei or-wyres Rhiainfellt yn frenhines Northumbria.",
   ["Rhun was a son of Urien, king of Rheged, and brother of Owain. He lived in the generation after the great wars of his father, when the Britons of the North and the Angles were learning to live side by side.",
    "The History of the Britons, gathered in Gwynedd about 829, tells of the baptism of Edwin, king of Northumbria, at Easter in 627, and says plainly: ‘If any one wishes to know who baptized them, it was Rum Map Urbgen’, Rhun son of Urien, who for forty days baptised the people.[[cite:ho-hb]] The English writer Bede gives the honour to Paulinus, Edwin’s bishop from Kent, but the Welsh book remembers that a son of Urien Rheged brought the faith to the king of the Angles.",
    "His line went on to marry into the royal house of Northumbria itself. His granddaughter’s daughter, Rhiainfellt, daughter of Rhoth son of Rhun, became the wife of Oswiu, king of Northumbria.[[cite:ho-hb]]"],
   ["Mab i Urien, brenin Rheged, a brawd Owain oedd Rhun. Bu fyw yn y genhedlaeth wedi rhyfeloedd mawr ei dad, pan oedd Brythoniaid y Gogledd a’r Eingl yn dysgu byw ochr yn ochr.",
    "Mae Hanes y Brythoniaid, a gasglwyd yng Ngwynedd tua 829, yn adrodd am fedydd Edwin, brenin Northumbria, adeg y Pasg yn 627, ac yn dweud yn blaen mai Rhun fab Urien a’u bedyddiodd, ac iddo fedyddio’r bobl am ddeugain niwrnod.[[cite:ho-hb]] Mae’r awdur Seisnig Beda yn rhoi’r anrhydedd i Paulinus, esgob Edwin o Gaint, ond mae’r llyfr Cymraeg yn cofio mai mab i Urien Rheged a ddaeth â’r ffydd at frenin yr Eingl.",
    "Aeth ei linach ymlaen i briodi i mewn i dŷ brenhinol Northumbria ei hun. Daeth Rhiainfellt, merch Rhoth fab Rhun, yn wraig i Oswiu, brenin Northumbria.[[cite:ho-hb]]"]),
 P("rhiainfellt", "saints", "fl. c. 640", "Rhiainfellt", "Rhiainfellt", "Princess of Rheged, queen of Northumbria", "Tywysoges Rheged, brenhines Northumbria", "Rhieinmelth", "rulers",
   "Great-granddaughter of Urien Rheged and wife of Oswiu, king of Northumbria. Through her the royal line of Rheged passed into the royal house of the Angles.",
   "Gor-wyres Urien Rheged a gwraig Oswiu, brenin Northumbria. Drwyddi hi aeth llinach frenhinol Rheged i mewn i dŷ brenhinol yr Eingl.",
   ["Rhiainfellt was the daughter of Rhoth son of Rhun son of Urien, and so the great-granddaughter of the greatest king of Rheged. Her name means something like ‘lightning maiden’.",
    "The History of the Britons says that Oswiu, king of Northumbria, had two wives: ‘Riemmelth, the daughter of Royth, son of Rum’, and Eanflæd, daughter of King Edwin.[[cite:ho-hb]] Her marriage, about 638, joined the old royal house of Rheged to the new power of the north, and the lands of Rheged seem to have passed with it into Northumbria. She was the first wife of one of the strongest kings of his age, and the blood of Urien Rheged ran in the royal house of the Angles after her."],
   ["Merch Rhoth fab Rhun fab Urien oedd Rhiainfellt, ac felly gor-wyres i frenin mwyaf Rheged.",
    "Dywed Hanes y Brythoniaid fod gan Oswiu, brenin Northumbria, ddwy wraig: Rhiainfellt ferch Rhoth fab Rhun, ac Eanflæd, merch y Brenin Edwin.[[cite:ho-hb]] Unodd ei phriodas, tua 638, hen dŷ brenhinol Rheged â grym newydd y gogledd, ac ymddengys i diroedd Rheged fynd gyda hi i Northumbria. Hi oedd gwraig gyntaf un o frenhinoedd cryfaf ei oes, a rhedai gwaed Urien Rheged yn nhŷ brenhinol yr Eingl ar ei hôl."]),
 P("dyfnwal-hen", "saints", "fl. early 6th century", "Dyfnwal Hen", "Dyfnwal Hen", "Forefather of the kings of the Clyde", "Cyndad brenhinoedd y Clud", "Dyfnwal_Hen", "rulers",
   "A king of the Britons of the Clyde, and in the old pedigree of the Men of the North the forefather of Rhydderch Hael, Mordaf Hael and Elffin son of Gwyddno.",
   "Brenin ar Frythoniaid y Clud, ac yn hen ach Gwŷr y Gogledd cyndad Rhydderch Hael, Mordaf Hael ac Elffin fab Gwyddno.",
   ["Dyfnwal Hen, Dyfnwal the Old, stands at the head of the second great family of the Old North. Where the first family, the Coeling, came from Coel Hen, this one came from Dyfnwal, and its kings ruled from Alt Clut, the Rock of the Clyde.",
    "The old pedigree of the Men of the North traces three famous lines back to him: Rhydderch Hael son of Tudwal Tudglyd son of Cedig son of Dyfnwal Hen; Mordaf son of Serwan son of Cedig son of Dyfnwal Hen; and Elffin son of Gwyddno son of Cawrdaf son of Garmonion son of Dyfnwal Hen.[[cite:ho-bonedd]] Two of the Three Generous Men of the Island of Britain, Rhydderch and Mordaf, were his great-grandsons."],
   ["Saif Dyfnwal Hen ar ben ail deulu mawr yr Hen Ogledd. Lle daeth y teulu cyntaf, y Coeling, o Goel Hen, daeth hwn o Ddyfnwal, a rheolai ei frenhinoedd o Alclud, Craig y Clud.",
    "Mae hen ach Gwŷr y Gogledd yn olrhain tair llinach enwog yn ôl ato: Rhydderch Hael fab Tudwal Tudglyd fab Cedig fab Dyfnwal Hen; Mordaf fab Serwan fab Cedig fab Dyfnwal Hen; ac Elffin fab Gwyddno fab Cawrdaf fab Garmonion fab Dyfnwal Hen.[[cite:ho-bonedd]] Roedd dau o Dri Hael Ynys Prydain, Rhydderch a Mordaf, yn or-wyrion iddo."]),
 P("nudd-hael", "saints", "fl. 6th century", "Nudd Hael", "Nudd Hael", "One of the Three Generous Men", "Un o Dri Hael Ynys Prydain", "Nudd_Hael", "rulers",
   "A king of the Men of the North, one of the Three Generous Men of the Island of Britain. For a thousand years Welsh poets praised their patrons as ‘as generous as Nudd’.",
   "Brenin o Wŷr y Gogledd, un o Dri Hael Ynys Prydain. Am fil o flynyddoedd canmolai beirdd Cymru eu noddwyr fel rhai ‘mor hael â Nudd’.",
   ["Nudd son of Senyllt was a king of the Britons of the North in the sixth century. The Triads name him first among the Three Generous Men of the Island of Britain, with Mordaf and Rhydderch, and his name became a byword: for a thousand years the poets of Wales praised a generous patron by calling him a second Nudd.",
    "He was one of the kings of the North who, the Welsh law books say, rode south to Arfon to avenge Elidir Mwynfawr. In the Yarrow valley in the Borders stands a memorial stone of the early sixth century to ‘the most famous princes Nudus and Dumnogenus’, the two sons of Liberalis.[[cite:ho-yarrow]] Nudus is the Latin form of Nudd, and Liberalis means ‘the generous one’, Hael in Welsh: the stone shows that these names were borne by the princes of the North in the very age of the Men of the North."],
   ["Roedd Nudd fab Senyllt yn frenin ar Frythoniaid y Gogledd yn y chweched ganrif. Mae’r Trioedd yn ei enwi’n gyntaf ymhlith Tri Hael Ynys Prydain, gyda Mordaf a Rhydderch, a daeth ei enw’n ddihareb: am fil o flynyddoedd canmolai beirdd Cymru noddwr hael drwy ei alw’n ail Nudd.",
    "Roedd yn un o frenhinoedd y Gogledd a farchogodd i’r de i Arfon, medd llyfrau’r gyfraith, i ddial am Elidir Mwynfawr. Yn nyffryn Yarrow yn y Gororau saif carreg goffa o ddechrau’r chweched ganrif i ‘y tywysogion enwocaf Nudus a Dumnogenus’, dau fab Liberalis.[[cite:ho-yarrow]] Nudus yw’r ffurf Ladin ar Nudd, ac ystyr Liberalis yw ‘yr un hael’: mae’r garreg yn dangos bod tywysogion y Gogledd yn dwyn yr enwau hyn yn oes Gwŷr y Gogledd ei hun."]),
 P("mordaf-hael", "saints", "fl. 6th century", "Mordaf Hael", "Mordaf Hael", "One of the Three Generous Men", "Un o Dri Hael Ynys Prydain", "Mordaf_Hael", "rulers",
   "A king of the Men of the North, of the line of Dyfnwal Hen, and one of the Three Generous Men of the Island of Britain with Nudd and Rhydderch.",
   "Brenin o Wŷr y Gogledd, o linach Dyfnwal Hen, ac un o Dri Hael Ynys Prydain gyda Nudd a Rhydderch.",
   ["Mordaf son of Serwan was a king of the Britons of the North, a cousin of Rhydderch Hael of the Clyde. The old pedigree traces his line through Serwan and Cedig to Dyfnwal Hen.[[cite:ho-bonedd]]",
    "The Triads count him among the Three Generous Men of the Island of Britain, and the Welsh law books name him with Clydno Eidyn, Nudd Hael and Rhydderch Hael among the kings of the North who came south to Arfon to avenge Elidir Mwynfawr. Generations of Welsh poets compared the princes they praised to Mordaf for open-handedness."],
   ["Roedd Mordaf fab Serwan yn frenin ar Frythoniaid y Gogledd, yn gefnder i Rydderch Hael o’r Clud. Mae’r hen ach yn olrhain ei linach drwy Serwan a Chedig at Ddyfnwal Hen.[[cite:ho-bonedd]]",
    "Mae’r Trioedd yn ei gyfrif ymhlith Tri Hael Ynys Prydain, ac mae llyfrau cyfraith Cymru’n ei enwi gyda Chlydno Eidyn, Nudd Hael a Rhydderch Hael ymhlith brenhinoedd y Gogledd a ddaeth i’r de i Arfon i ddial am Elidir Mwynfawr. Cymharodd cenedlaethau o feirdd Cymru’r tywysogion a folent â Mordaf am eu haelioni."]),
 P("elidir-mwynfawr", "saints", "fl. mid 6th century", "Elidir Mwynfawr", "Elidir Mwynfawr", "Prince of the North who came to Arfon", "Tywysog o’r Gogledd a ddaeth i Arfon", "Elidir_Mwynfawr", "rulers",
   "A prince of the North who fell at Aber Mewydus in Arfon. The kings of the North came south to avenge him, and Rhun ap Maelgwn led the men of Gwynedd all the way to the Forth in answer.",
   "Tywysog o’r Gogledd a syrthiodd yn Aber Mewydus yn Arfon. Daeth brenhinoedd y Gogledd i’r de i ddial amdano, ac arweiniodd Rhun ap Maelgwn wŷr Gwynedd yr holl ffordd i Werydd mewn ateb.",
   ["Elidir Mwynfawr, Elidir the Wealthy, was a prince of the Britons of the North in the middle of the sixth century. Welsh tradition holds that he was married to Eurgain, daughter of Maelgwn Gwynedd, and that after Maelgwn died he came to Gwynedd to claim a share of the kingdom.",
    "The Welsh law books tell what followed, in a passage on the privileges of the men of Arfon. Elidir was killed at Aber Mewydus in Arfon, and the kings of the North, Clydno Eidyn, Nudd Hael, Mordaf Hael and Rhydderch Hael, came south to avenge him and burned Arfon. Rhun son of Maelgwn gathered the men of Gwynedd and marched north through the lands of the Britons as far as the river Forth, and for that long march the men of Arfon won the right to lead the van of the army of Gwynedd for ever.",
    "The Triads remember his horse, Du y Moroedd, the Black of the Seas, among the three great horse-burdens of the Island: it carried seven people and a half from Penllech in the North to Penllech in Môn."],
   ["Roedd Elidir Mwynfawr yn dywysog ar Frythoniaid y Gogledd yng nghanol y chweched ganrif. Yn ôl traddodiad Cymru roedd yn briod ag Eurgain, merch Maelgwn Gwynedd, ac wedi marw Maelgwn daeth i Wynedd i hawlio cyfran o’r deyrnas.",
    "Mae llyfrau cyfraith Cymru’n adrodd yr hyn a ddilynodd, mewn darn am freiniau gwŷr Arfon. Lladdwyd Elidir yn Aber Mewydus yn Arfon, a daeth brenhinoedd y Gogledd, Clydno Eidyn, Nudd Hael, Mordaf Hael a Rhydderch Hael, i’r de i ddial amdano a llosgi Arfon. Casglodd Rhun fab Maelgwn wŷr Gwynedd a gorymdeithio tua’r gogledd drwy diroedd y Brythoniaid hyd at afon Gwerydd, ac am y daith hir honno enillodd gwŷr Arfon yr hawl i arwain blaen byddin Gwynedd am byth.",
    "Mae’r Trioedd yn cofio ei farch, Du y Moroedd, ymhlith tri marchlwyth mawr yr Ynys: cariodd saith dyn a hanner o Benllech yn y Gogledd i Benllech ym Môn."]),
 P("dunod-fawr", "saints", "d. 595", "Dunod Fawr", "Dunod Fawr", "King in the North, a Pillar of Battle", "Brenin yn y Gogledd, un o Dri Phost Cad", "Dunod_Fawr", "rulers",
   "King of the Britons of the Pennines, son of Pabo Post Prydain and father of Saint Deiniol of Bangor. The Triads name him one of the Three Pillars of Battle of the Island of Britain.",
   "Brenin Brythoniaid y Pennines, mab Pabo Post Prydain a thad Sant Deiniol o Fangor. Mae’r Trioedd yn ei enwi’n un o Dri Phost Cad Ynys Prydain.",
   ["Dunod son of Pabo, Dunod Fawr, Dunod the Great, was a king of the Britons of the North in the late sixth century, of the line of Coel Hen.[[cite:ho-bonedd]] His kingdom seems to have lain in the Pennine hills, where an old English life of Saint Wilfrid names a district called Dunutinga, ‘Dunod’s people’.",
    "The Triads name him with Gwallog son of Lleënog and Cynfelyn Drwsgl as the Three Pillars of Battle of the Island of Britain, as his father Pabo had been called the Pillar of Britain. The Welsh Annals record his death in 595: ‘The death of king Dunod son of Pabo.’[[cite:ho-ac]]",
    "His son was Saint Deiniol, who founded the monastery of Bangor on the Menai, and Deiniol’s mother, Welsh tradition holds, was Dwywai, daughter of Lleënog, the sister of Gwallog of Elmet. So a king of the North and a princess of Elmet were the parents of the first bishop of Gwynedd."],
   ["Roedd Dunod fab Pabo, Dunod Fawr, yn frenin ar Frythoniaid y Gogledd ar ddiwedd y chweched ganrif, o linach Coel Hen.[[cite:ho-bonedd]] Ymddengys i’w deyrnas orwedd ym mryniau’r Pennines, lle mae hen fuchedd Saesneg Sant Wilfrid yn enwi ardal o’r enw Dunutinga, ‘pobl Dunod’.",
    "Mae’r Trioedd yn ei enwi gyda Gwallog fab Lleënog a Chynfelyn Drwsgl yn Dri Phost Cad Ynys Prydain, fel y gelwid ei dad Pabo yn Bost Prydain. Mae’r Annales Cambriae yn cofnodi ei farw yn 595: ‘Marw y brenin Dunod fab Pabo.’[[cite:ho-ac]]",
    "Ei fab oedd Sant Deiniol, a sefydlodd fynachlog Bangor ar lan Menai, ac yn ôl traddodiad Cymru mam Deiniol oedd Dwywai, merch Lleënog, chwaer Gwallog o Elfed. Felly brenin o’r Gogledd a thywysoges o Elfed oedd rhieni esgob cyntaf Gwynedd."]),
 P("eliffer-gosgorddfawr", "saints", "fl. mid 6th century", "Eliffer Gosgorddfawr", "Eliffer Gosgorddfawr", "King in the North, father of Gwrgi and Peredur", "Brenin yn y Gogledd, tad Gwrgi a Pheredur", "Eliffer", "rulers",
   "Eliffer of the Great Retinue, a king of the Men of the North and father of Gwrgi and Peredur, kings of Efrog, whose deaths the Welsh Annals record in 580.",
   "Eliffer Gosgorddfawr, brenin o Wŷr y Gogledd a thad Gwrgi a Pheredur, brenhinoedd Efrog, y mae’r Annales Cambriae yn cofnodi eu marw yn 580.",
   ["Eliffer son of Arthwys was a king of the Britons of the North in the sixth century, of the line of Coel Hen.[[cite:ho-bonedd]] He was called Gosgorddfawr, ‘of the great retinue’, for the size of the war band that rode with him.",
    "His sons Gwrgi and Peredur were kings in the North, linked by tradition with Efrog, York. The Welsh Annals name them at the battle of Arfderydd in 573, and record in 580: ‘Gwrgi and Peredur, sons of Eliffer, died.’[[cite:ho-ac]] Welsh story kept the name of Peredur alive: the hero of the romance Peredur son of Efrog, the first knight of the Grail, carries it, and his father’s name is the Welsh name of York."],
   ["Roedd Eliffer fab Arthwys yn frenin ar Frythoniaid y Gogledd yn y chweched ganrif, o linach Coel Hen.[[cite:ho-bonedd]] Fe’i gelwid yn Osgorddfawr am faint y llu a farchogai gydag ef.",
    "Roedd ei feibion Gwrgi a Pheredur yn frenhinoedd yn y Gogledd, a chysylltir hwy gan draddodiad ag Efrog. Mae’r Annales Cambriae yn eu henwi ym mrwydr Arfderydd yn 573, ac yn cofnodi yn 580: ‘Bu farw Gwrgi a Pheredur, meibion Eliffer.’[[cite:ho-ac]] Cadwodd chwedlau Cymru enw Peredur yn fyw: mae arwr y rhamant Peredur fab Efrog, marchog cyntaf y Greal, yn ei ddwyn, ac enw ei dad yw enw Cymraeg Efrog."]),
 P("ceredig-ap-gwallog", "saints", "d. 616", "Ceredig ap Gwallog", "Ceredig ap Gwallog", "The last king of Elfed", "Brenin olaf Elfed", "Ceredig_of_Elmet", "rulers",
   "The last king of Elfed, Elmet, the British kingdom around Leeds, which kept its freedom among the kingdoms of the Angles until his day.",
   "Brenin olaf Elfed, y deyrnas Frythonig o gwmpas Leeds, a gadwodd ei rhyddid ymhlith teyrnasoedd yr Eingl hyd ei ddydd ef.",
   ["Ceredig son of Gwallog was the last king of Elfed, Elmet, in the valleys of west Yorkshire. His father Gwallog had been praised by Taliesin and named by the Triads one of the Three Pillars of Battle, and Ceredig kept the kingdom free for a generation more, an island of the Britons among the kingdoms of the Angles.",
    "The Welsh Annals record in 616: ‘Ceredig died.’[[cite:ho-ac]] The History of the Britons says that Edwin of Northumbria ‘seized on Elmete, and expelled Cerdic, its king’.[[cite:ho-hb]] With him the last free kingdom of the Britons east of the Pennines came to an end, but its name did not: Sherburn-in-Elmet and Barwick-in-Elmet carry it still."],
   ["Ceredig fab Gwallog oedd brenin olaf Elfed, yng nghymoedd gorllewin Swydd Efrog. Roedd ei dad Gwallog wedi’i ganmol gan Daliesin a’i enwi gan y Trioedd yn un o Dri Phost Cad, a chadwodd Ceredig y deyrnas yn rhydd am genhedlaeth arall, ynys o Frythoniaid ymhlith teyrnasoedd yr Eingl.",
    "Mae’r Annales Cambriae yn cofnodi yn 616: ‘Bu farw Ceredig.’[[cite:ho-ac]] Dywed Hanes y Brythoniaid i Edwin o Northumbria gipio Elfed a gyrru allan Ceredig, ei brenin.[[cite:ho-hb]] Gydag ef daeth teyrnas rydd olaf y Brythoniaid i’r dwyrain o’r Pennines i ben, ond nid ei henw: mae Sherburn-in-Elmet a Barwick-in-Elmet yn ei gadw o hyd."]),
 P("owain-ap-beli", "saints", "fl. 642", "Owain ap Beli", "Owain ap Beli", "King of Strathclyde, victor of Strathcarron", "Brenin Ystrad Clud, buddugwr Srath Caruin", "Owen_I_of_Strathclyde", "rulers",
   "King of the Britons of the Clyde, who won the battle of Strathcarron in 642. A verse added to Y Gododdin rejoices in his victory.",
   "Brenin Brythoniaid y Clud, a enillodd frwydr Srath Caruin yn 642. Mae pennill a ychwanegwyd at Y Gododdin yn gorfoleddu yn ei fuddugoliaeth.",
   ["Owain son of Beli ruled the Britons of the Clyde from Alt Clut, the Rock of Dumbarton, in the middle of the seventh century. In December 642 Domnall Brecc, king of the Gaels of Dál Riata, marched against him, and fell. The Annals of Ulster record it: Domnall Brecc ‘was slain at the end of the year, in December, in the battle of Srath Caruin, by Hoan, king of the Britons’.[[cite:ho-au642]]",
    "The victory was sung by the Britons. A verse was added to Y Gododdin that tells of the men who came from Kintyre, and of the head of Dyfnwal Frych, Domnall Brecc, gnawed by the ravens.",
    "His family were great in the North for another generation. His brother’s son, or by some accounts his brother, Bridei son of Beli, became king of the Picts and beat the Northumbrians at Dun Nechtain in 685, a battle that saved the north of Britain from the Angles."],
   ["Teyrnasai Owain fab Beli ar Frythoniaid y Clud o Alclud, Craig Dumbarton, yng nghanol y seithfed ganrif. Ym mis Rhagfyr 642 gorymdeithiodd Domnall Brecc, brenin Gwyddelod Dál Riata, yn ei erbyn, a syrthio. Mae Annalau Ulster yn ei gofnodi: lladdwyd Domnall Brecc ar ddiwedd y flwyddyn, ym mis Rhagfyr, ym mrwydr Srath Caruin, gan Hoan, brenin y Brythoniaid.[[cite:ho-au642]]",
    "Canodd y Brythoniaid am y fuddugoliaeth. Ychwanegwyd pennill at Y Gododdin sy’n sôn am y gwŷr a ddaeth o Gintyre, ac am ben Dyfnwal Frych, Domnall Brecc, yn cael ei gnoi gan y brain.",
    "Bu ei deulu’n fawr yn y Gogledd am genhedlaeth arall. Daeth Bridei fab Beli, ei frawd yn ôl rhai, yn frenin y Pictiaid a threchu Northumbria yn Dun Nechtain yn 685, brwydr a achubodd ogledd Prydain rhag yr Eingl."]),
 P("arthgal", "kings", "d. 872", "Arthgal ap Dyfnwal", "Arthgal ap Dyfnwal", "King of Strathclyde who held the Rock", "Brenin Ystrad Clud a ddaliodd y Graig", "Arthgal_ap_Dyfnwal", "rulers",
   "King of the Britons of the Clyde, who held Alt Clut, the Rock of Dumbarton, for four months against the Viking kings of Dublin in 870.",
   "Brenin Brythoniaid y Clud, a ddaliodd Alclud, Craig Dumbarton, am bedwar mis yn erbyn brenhinoedd Llychlynnaidd Dulyn yn 870.",
   ["Arthgal son of Dyfnwal was king of the Britons of the Clyde in the ninth century, ruling from Alt Clut, the great rock above the river at Dumbarton that had been the seat of his forefathers for four hundred years.",
    "In 870 the two most feared Viking kings of the age, Olaf and Ivar of Dublin, came against him with their fleets. The Annals of Ulster record that they laid siege to the fortress of Ail Cluaithe, and the siege lasted four months, until the well on the rock ran dry.[[cite:ho-au870]] The Welsh Annals mourn it in one line: ‘The fortress of Alt Clud was broken by the gentiles.’[[cite:ho-ac]]",
    "Arthgal died in 872, but his kingdom did not die with him. His son Rhun and the kings after him ruled from Govan, further up the Clyde, and the kingdom of Strathclyde lasted for a hundred and fifty years more."],
   ["Roedd Arthgal fab Dyfnwal yn frenin ar Frythoniaid y Clud yn y nawfed ganrif, yn teyrnasu o Alclud, y graig fawr uwchben yr afon yn Dumbarton a fu’n sedd ei gyndadau am bedwar can mlynedd.",
    "Yn 870 daeth dau frenin Llychlynnaidd mwyaf ofnus yr oes, Olaf ac Ivar o Ddulyn, yn ei erbyn â’u llynges. Mae Annalau Ulster yn cofnodi iddynt warchae ar gaer Ail Cluaithe, a pharhaodd y gwarchae bedwar mis, nes i’r ffynnon ar y graig sychu.[[cite:ho-au870]] Mae’r Annales Cambriae yn galaru amdano mewn un llinell: ‘Torrwyd caer Alclud gan y paganiaid.’[[cite:ho-ac]]",
    "Bu farw Arthgal yn 872, ond ni fu farw ei deyrnas gydag ef. Teyrnasodd ei fab Rhun a’r brenhinoedd ar ei ôl o Govan, ymhellach i fyny’r Clud, a pharhaodd teyrnas Ystrad Clud am gant a hanner o flynyddoedd eto."]),
 P("owain-foel", "kings", "fl. 1018", "Owain Foel", "Owain Foel", "The last king of Strathclyde", "Brenin olaf Ystrad Clud", "Owain_Foel", "rulers",
   "Owain the Bald, the last known king of the Britons of Strathclyde, who fought beside the king of Scots and won the battle of Carham on the Tweed in 1018.",
   "Owain Foel, brenin olaf hysbys Brythoniaid Ystrad Clud, a ymladdodd ochr yn ochr â brenin yr Alban ac ennill brwydr Carham ar afon Tweed yn 1018.",
   ["Owain Foel, Owain the Bald, is the last king of the Britons of the North whose name we know. He ruled Strathclyde, the kingdom of the Clyde that reached south into Cumbria, more than six hundred years after the legions left Britain.",
    "In 1018 he marched with Malcolm, king of Scots, against the Northumbrians, and they won a great victory at Carham on the Tweed. The northern English chronicle of the twelfth century names him there as ‘Eugenius Calvus’, Owain the Bald, king of the Clydesmen.[[cite:ho-owainfoel]]",
    "After him no king of Strathclyde is named, and in the eleventh century the kingdom was joined to Scotland. The British tongue of the North, Cumbric, was still spoken there until about the twelfth century.[[cite:ho-cumbric]] With Owain Foel the last kingdom of the Men of the North passed into history, after six centuries."],
   ["Owain Foel yw brenin olaf Brythoniaid y Gogledd y gwyddom ei enw. Teyrnasai ar Ystrad Clud, teyrnas y Clud a ymestynnai i’r de i Gumbria, fwy na chwe chan mlynedd wedi i’r llengoedd adael Prydain.",
    "Yn 1018 gorymdeithiodd gyda Malcolm, brenin yr Alban, yn erbyn Northumbria, ac enillasant fuddugoliaeth fawr yn Carham ar afon Tweed. Mae cronicl Seisnig o’r gogledd yn y ddeuddegfed ganrif yn ei enwi yno fel ‘Eugenius Calvus’, Owain Foel, brenin gwŷr y Clud.[[cite:ho-owainfoel]]",
    "Ar ei ôl ni enwir unrhyw frenin ar Ystrad Clud, ac yn yr unfed ganrif ar ddeg unwyd y deyrnas â’r Alban. Siaradwyd iaith Frythonig y Gogledd, y Gymbrieg, yno o hyd hyd tua’r ddeuddegfed ganrif.[[cite:ho-cumbric]] Gydag Owain Foel aeth teyrnas olaf Gwŷr y Gogledd yn rhan o hanes, wedi chwe chanrif."]),
 P("talhaearn", "saints", "fl. 6th century", "Talhaearn Tad Awen", "Talhaearn Tad Awen", "The father of the Muse", "Tad yr Awen", "Talhaearn_Tad_Awen", "words",
   "The first of the five poets of the sixth century named in the History of the Britons. His name, Tad Awen, means ‘father of the Muse’.",
   "Y cyntaf o’r pum bardd o’r chweched ganrif a enwir yn Hanes y Brythoniaid. Ystyr ei enw, Tad Awen, yw ‘tad yr awen’.",
   ["Talhaearn is the first name in the oldest list of Welsh poets. The History of the Britons, gathered in Gwynedd about 829, says that in the time of the wars against Ida of Bernicia, ‘Talhaiarn Cataguen was famed for poetry, and Neirin, and Taliesin and Bluchbard, and Cian’.[[cite:ho-hb]] Cataguen is the old spelling of Tad Awen, ‘father of the Muse’.",
    "No poem under his name has come down to us, but his fame lived on. A poem in the Book of Taliesin names him as the greatest of the wise men, and the poets who came after counted him the father of their art, the first of the Cynfeirdd, the earliest poets of the Welsh language."],
   ["Talhaearn yw’r enw cyntaf yn y rhestr hynaf o feirdd Cymraeg. Dywed Hanes y Brythoniaid, a gasglwyd yng Ngwynedd tua 829, fod Talhaearn Tad Awen yn enwog am farddoniaeth yn amser y rhyfeloedd yn erbyn Ida o Frynaich, a Neirin, a Thaliesin a Blwchfardd, a Chian.[[cite:ho-hb]]",
    "Ni ddaeth unrhyw gerdd dan ei enw i lawr atom, ond parhaodd ei fri. Mae cerdd yn Llyfr Taliesin yn ei enwi’n fwyaf o’r doethion, a chyfrifai’r beirdd a ddaeth ar ei ôl ef yn dad eu celfyddyd, y cyntaf o’r Cynfeirdd, beirdd cynharaf yr iaith Gymraeg."]),
]

# ---------------------------------------------------------------- the "Men of the North" block on each of their pages
GROUPS = [
 ("The forefathers", "Y cyndadau", ["coel-hen", "dyfnwal-hen", "cunedda", "cynfarch-oer", "pabo-post-prydain", "caw-o-brydyn"]),
 ("Rheged", "Rheged", ["urien-rheged", "owain-ab-urien", "rhun-ab-urien", "rhiainfellt", "llywarch-hen"]),
 ("Gododdin and Eidyn", "Gododdin ac Eidyn", ["mynyddog-mwynfawr", "clydno-eidyn", "cynon-ap-clydno"]),
 ("Ystrad Clud, the kingdom of the Clyde", "Ystrad Clud, teyrnas y Clud", ["rhydderch-hael", "mordaf-hael", "nudd-hael", "owain-ap-beli", "arthgal", "owain-foel"]),
 ("Elfed, Efrog and the Pennines", "Elfed, Efrog a’r Pennines", ["gwallog", "ceredig-ap-gwallog", "eliffer-gosgorddfawr", "dunod-fawr", "gwenddolau", "elidir-mwynfawr"]),
 ("Poets, prophets and saints", "Beirdd, proffwydi a saint", ["talhaearn", "aneirin", "taliesin", "myrddin", "cyndeyrn", "deiniol"]),
]
LINKS = [
 ("story-hen-ogledd.html", "Long read: Yr Hen Ogledd, the Old North", "Erthygl: Yr Hen Ogledd"),
 ("kings-rheged.html", "The kings of Rheged", "Brenhinoedd Rheged"),
 ("kings-ystrad-clud.html", "The kings of Strathclyde", "Brenhinoedd Ystrad Clud"),
 ("family-trees.html#tree-coeling", "The family tree of the Men of the North", "Coeden deulu Gwŷr y Gogledd"),
]
ALL_IDS = list(dict.fromkeys(s for _, _, ids in GROUPS for s in ids))

# ---------------------------------------------------------------- the map of the Old North
# (English, Cymraeg, lat, lon, note EN, note CY, link)
MAP = [
 ("Alt Clut, the Rock of the Clyde", "Alclud, Craig y Clud", 55.936, -4.563, "Dumbarton Rock, seat of the kings of Ystrad Clud for four hundred years, until the Viking siege of 870.", "Craig Dumbarton, sedd brenhinoedd Ystrad Clud am bedwar can mlynedd, hyd at warchae’r Llychlynwyr yn 870.", "kings-ystrad-clud.html"),
 ("Govan and Glasgow", "Govan a Glasgow", 55.864, -4.300, "Cyndeyrn’s church, round which Glasgow grew, and Govan, where the later kings of Strathclyde were remembered in carved stone.", "Eglwys Cyndeyrn, y tyfodd Glasgow o’i chwmpas, a Govan, lle cofiwyd brenhinoedd diweddarach Ystrad Clud mewn carreg gerfiedig.", "person-cyndeyrn.html"),
 ("Manaw Gododdin", "Manaw Gododdin", 56.107, -3.753, "The land at the head of the Forth, from which Cunedda came south to found Gwynedd.", "Y wlad ym mhen Gwerydd, y daeth Cunedda ohoni i’r de i sefydlu Gwynedd.", "person-cunedda.html"),
 ("Strathcarron", "Srath Caruin", 56.02, -3.93, "Where Owain ap Beli, king of the Britons of the Clyde, won his great victory in 642.", "Lle’r enillodd Owain ap Beli, brenin Brythoniaid y Clud, ei fuddugoliaeth fawr yn 642.", "person-owain-ap-beli.html"),
 ("Din Eidyn", "Din Eidyn", 55.949, -3.200, "Edinburgh’s castle rock, the hall of Mynyddog Mwynfawr, from which the Gododdin rode to Catraeth.", "Craig castell Caeredin, neuadd Mynyddog Mwynfawr, y marchogodd y Gododdin ohoni i Gatraeth.", "person-mynyddog-mwynfawr.html"),
 ("Traprain Law", "Traprain Law", 55.963, -2.672, "The great hill fort of the Votadini, the Gododdin of Roman times, where a hoard of Roman silver was found in 1919.", "Bryngaer fawr y Votadini, Gododdin oes Rhufain, lle cafwyd celc o arian Rhufeinig yn 1919.", "kings-gododdin.html"),
 ("Aeron", "Aeron", 55.46, -4.63, "Probably the land of the river Ayr. Cynon son of Clydno and the ‘spears of Aeron’ are praised in Y Gododdin.", "Gwlad afon Ayr, yn ôl pob tebyg. Mae Cynon fab Clydno a ‘gwaywawr Aeron’ yn cael eu canmol yn Y Gododdin.", "person-cynon-ap-clydno.html"),
 ("The Yarrow Stone", "Carreg Yarrow", 55.535, -3.06, "A memorial of the early sixth century to ‘the most famous princes Nudus and Dumnogenus’, sons of Liberalis.", "Carreg goffa o ddechrau’r chweched ganrif i ‘y tywysogion enwocaf Nudus a Dumnogenus’, meibion Liberalis.", "person-nudd-hael.html"),
 ("Carham", "Carham", 55.637, -2.322, "Where Owain Foel, the last king of Strathclyde, won the battle of 1018.", "Lle’r enillodd Owain Foel, brenin olaf Ystrad Clud, frwydr 1018.", "person-owain-foel.html"),
 ("Ynys Metcaud, Lindisfarne", "Ynys Fedcawd, Lindisfarne", 55.669, -1.801, "Where Urien and the kings of the Britons held the Angles under siege for three days and three nights.", "Lle gwarchaeodd Urien a brenhinoedd y Brythoniaid ar yr Eingl am dri diwrnod a thair noson.", "battles.html#b-metcaut"),
 ("Arfderydd", "Arfderydd", 55.03, -2.955, "Arthuret, by the Esk, where Gwenddolau fell in 573 and his war band fought on for six weeks.", "Arthuret, ger afon Esk, lle syrthiodd Gwenddolau yn 573 ac yr ymladdodd ei osgordd ymlaen am chwe wythnos.", "person-gwenddolau.html"),
 ("Caer Liwelydd", "Caer Liwelydd", 54.892, -2.932, "Carlisle, at the heart of Urien’s kingdom of Rheged.", "Carlisle, yng nghanol teyrnas Rheged Urien.", "kings-rheged.html"),
 ("Catraeth", "Catraeth", 54.376, -1.637, "Catterick, where the war band of Mynyddog rode against the Angles about 600, and where Taliesin calls Urien lord.", "Catterick, lle marchogodd gosgordd Mynyddog yn erbyn yr Eingl tua 600, a lle mae Taliesin yn galw Urien yn arglwydd.", "battles.html#b-catraeth"),
 ("Caer Efrog", "Caer Efrog", 53.96, -1.08, "York, linked by tradition with Gwrgi and Peredur, sons of Eliffer.", "Efrog, a gysylltir gan draddodiad â Gwrgi a Pheredur, meibion Eliffer.", "person-eliffer-gosgorddfawr.html"),
 ("Elfed", "Elfed", 53.80, -1.55, "Elmet, the British kingdom around Leeds, free until about 617.", "Y deyrnas Frythonig o gwmpas Leeds, yn rhydd hyd tua 617.", "kings-elfed.html"),
 ("Ynys Manaw", "Ynys Manaw", 54.23, -4.55, "The Isle of Man, from which Merfyn Frych came to Gwynedd in 825, of the line of Llywarch Hen.", "Ynys Manaw, y daeth Merfyn Frych ohoni i Wynedd yn 825, o linach Llywarch Hen.", "person-merfyn-frych.html"),
 ("Llanbabo", "Llanbabo", 53.36, -4.44, "Where Pabo Post Prydain, a king of the North, ended his days; his crowned stone figure is in the church.", "Lle diweddodd Pabo Post Prydain, brenin o’r Gogledd, ei ddyddiau; mae ei ddelw garreg goronog yn yr eglwys.", "person-pabo-post-prydain.html"),
 ("Bangor", "Bangor", 53.228, -4.128, "Founded by Saint Deiniol, son of Dunod Fawr, a king of the North.", "Sefydlwyd gan Sant Deiniol, mab Dunod Fawr, brenin o’r Gogledd.", "person-deiniol.html"),
 ("Llanelwy", "Llanelwy", 53.257, -3.442, "St Asaph, where Cyndeyrn of the Clyde founded his monastery in Wales.", "Lle sefydlodd Cyndeyrn o’r Clud ei fynachlog yng Nghymru.", "person-cyndeyrn.html"),
 ("Llanfor", "Llanfor", 52.92, -3.57, "Near Bala, where Welsh tradition holds that Llywarch Hen, cousin of Urien, ended his days.", "Ger y Bala, lle diweddodd Llywarch Hen, cefnder Urien, ei ddyddiau yn ôl traddodiad Cymru.", "person-llywarch-hen.html"),
]
# the kingdoms named on the map: (English, Cymraeg, lat, lon, class)   class "foe" for the kingdoms of the Angles
REGIONS = [
 ("Ystrad Clud", "Ystrad Clud", 55.62, -4.05, ""), ("Gododdin", "Gododdin", 55.80, -2.55, ""), ("Rheged", "Rheged", 54.55, -2.95, ""),
 ("Elfed", "Elfed", 53.62, -2.05, ""), ("Efrog", "Efrog", 54.20, -1.45, ""), ("Manaw", "Manaw", 56.30, -3.55, ""),
 ("Gwynedd", "Gwynedd", 52.72, -4.02, ""), ("Powys", "Powys", 52.45, -3.32, ""),
 ("Brynaich", "Brynaich", 55.25, -1.75, "foe"), ("Deifr", "Deifr", 53.95, -0.45, "foe"),
]
# journeys south: (English, Cymraeg, [(lat, lon), ...])  drawn as dashed curves through the points
ROUTES = [
 ("Cunedda", "Cunedda", [(56.07, -3.80), (55.2, -5.05), (53.95, -4.95), (53.15, -4.30)]),
 ("Llywarch Hen", "Llywarch Hen", [(54.80, -2.85), (53.95, -2.95), (53.02, -3.52)]),
 ("Cyndeyrn", "Cyndeyrn", [(55.84, -4.22), (54.95, -3.75), (54.0, -3.55), (53.40, -3.47)]),
]

# ---------------------------------------------------------------- the long read
STORY = dict(id="hen-ogledd", era="saints", art="sword", mins=22,
  people=["coel-hen", "dyfnwal-hen", "cunedda", "cynfarch-oer", "urien-rheged", "owain-ab-urien", "rhun-ab-urien", "rhiainfellt", "llywarch-hen",
          "mynyddog-mwynfawr", "clydno-eidyn", "cynon-ap-clydno", "rhydderch-hael", "mordaf-hael", "nudd-hael", "owain-ap-beli", "arthgal", "owain-foel",
          "gwallog", "ceredig-ap-gwallog", "eliffer-gosgorddfawr", "dunod-fawr", "pabo-post-prydain", "gwenddolau", "elidir-mwynfawr",
          "talhaearn", "aneirin", "taliesin", "myrddin", "cyndeyrn", "deiniol", "caw-o-brydyn", "merfyn-frych", "rhun-ap-maelgwn"],
  events=["Cunedda comes to Gwynedd", "Taliesin sings for Urien", "The battle of Arfderydd", "Urien besieges Lindisfarne", "Y Gododdin"],
  links=[("kings-rheged.html", "The kings of Rheged", "Brenhinoedd Rheged"),
         ("kings-gododdin.html", "The kings of Gododdin", "Brenhinoedd Gododdin"),
         ("kings-ystrad-clud.html", "The kings of Strathclyde", "Brenhinoedd Ystrad Clud"),
         ("kings-elfed.html", "The kings of Elfed", "Brenhinoedd Elfed"),
         ("family-trees.html#tree-coeling", "The family tree of the Men of the North", "Coeden deulu Gwŷr y Gogledd"),
         ("book-aneirin.html", "The Book of Aneirin", "Llyfr Aneirin"),
         ("book-taliesin.html", "The Book of Taliesin", "Llyfr Taliesin"),
         ("triads.html", "The Welsh Triads", "Trioedd Ynys Prydain"),
         ("person-arthur.html", "Arthur, King of the Britons", "Arthur, Brenin y Brythoniaid")],
  en="Yr Hen Ogledd: the Old North, where Welsh poetry was born",
  cy="Yr Hen Ogledd: y wlad lle ganed barddoniaeth Gymraeg",
  sumEn="From the Clyde and the Forth to the Pennines, the Britons of the North spoke the language that became Welsh. Their kingdoms, Gododdin, Rheged, Strathclyde and Elfed; their kings, Urien, Owain and Rhydderch Hael; the poets Aneirin and Taliesin; Catraeth and Arfderydd; and the Men of the North whom Wales has never forgotten.",
  sumCy="O’r Clud a Gwerydd hyd y Pennines, siaradai Brythoniaid y Gogledd yr iaith a drodd yn Gymraeg. Eu teyrnasoedd, Gododdin, Rheged, Ystrad Clud ac Elfed; eu brenhinoedd, Urien, Owain a Rhydderch Hael; y beirdd Aneirin a Thaliesin; Catraeth ac Arfderydd; a Gwŷr y Gogledd nad anghofiodd Cymru erioed.",
  pEn=[
   "Fourteen hundred years ago, a traveller could ride from the shore of the Severn to the head of the Firth of Forth and hear the same language all the way. In the hall of the king of Gwynedd at Aberffraw, in the fortress of Din Eidyn on Edinburgh’s rock, and on the Rock of the Clyde at Dumbarton, the people spoke the British tongue that became Welsh. The kingdoms of the North, between the Clyde and the Pennines, were as much the land of the Cymry as Gwynedd and Powys. Welsh writers call them Yr Hen Ogledd, the Old North, and the old poets called their people Gwŷr y Gogledd, the Men of the North.",
   "It was there, in the North, that the first poems in Welsh were made. It was from there that the royal house of Gwynedd came. And it was there that the Britons stood longest against the Angles, until the last king of Strathclyde won his final battle in 1018. This is their story.",
   "|| Where | From the Clyde and the Forth in the north to the Pennines and the Mersey in the south",
   "|| When | From the end of Roman Britain, about 410, to the last king of Strathclyde, about 1018",
   "|| The people | Britons, who called themselves Cymry, ‘fellow countrymen’",
   "|| The kingdoms | Gododdin, Ystrad Clud (Strathclyde), Rheged, Elfed, Efrog, Aeron and Manaw Gododdin",
   "|| The kings | Coel Hen, Cunedda, Urien, Owain, Rhydderch Hael, Gwallog, Mynyddog and many more",
   "|| The poets | Talhaearn, Aneirin and Taliesin; Myrddin and Llywarch Hen in the poems that bear their names",
   "|| Kept in Wales | The Book of Aneirin, the Book of Taliesin, the Black Book of Carmarthen, the Triads and the pedigree of the Men of the North",
   "## One people from the Clyde to the Severn",
   "When the legions left Britain about 410, the Britons ruled the whole island west and north of the lands the Saxons and Angles were taking. There was no border between Wales and the North. The kings of both married into each other’s houses, their poets sang in the same tongue, and their saints travelled freely between them. Cyndeyrn of the Clyde founded Llanelwy; Deiniol, son of a king of the North, founded Bangor; the family of Caw of Prydyn settled in Ynys Môn.",
   "They even shared a name. The Britons of Wales and of the North alike called themselves Cymry, ‘fellow countrymen’, and the same word lives on in Cumbria and Cumberland, the land of the Cymry of the North.[[cite:ho-cumbric]] Their language, which scholars call Cumbric, was still spoken in Strathclyde until about the twelfth century, and it has left its mark all over the map: Lanark is llannerch, a clearing; Penrith is pen rhyd, the chief ford; Ecclefechan is eglwys fechan, the little church; Blencathra begins with blaen, a summit.[[cite:ho-cumbric]] Even the old counting rhymes of the shepherds of the Dales, yan, tan, tethera, are close kin to the Welsh un, dau, tri.",
   "!! map",
   "## The kingdoms of the North",
   "Gododdin held the land around the Firth of Forth. In Roman times its people were the Votadini, and their great hill fort was Traprain Law in East Lothian, where a hoard of Roman silver was found in 1919. Its heart in the sixth century was Din Eidyn, the fortress on Edinburgh’s castle rock, and at the head of the Forth lay Manaw Gododdin, whose name survives in Clackmannan and Slamannan.",
   "Ystrad Clud, Strathclyde, was ruled from Alt Clut, the Rock of the Clyde, which the Gaels called Dùn Breatann, the fortress of the Britons: Dumbarton. It was the strongest and longest-lived of the northern kingdoms.",
   "Rheged was the kingdom of Urien, around the Solway Firth and Caer Liwelydd, Carlisle, and perhaps into Galloway and the Eden valley. Elfed, Elmet, held the valleys around Leeds, and Efrog was the land of York, Caer Efrog. Aeron, probably the land of the river Ayr, sent its warriors to Catraeth.[[cite:ho-aeron]] Further south and east lay the young kingdoms of the Angles, Bernicia and Deira, whose very names are British: in the poems they are Brynaich and Deifr.",
   "## The Men of the North",
   "Wales kept the memory of the northern kings in a short and precious text, Bonedd Gwŷr y Gogledd, the Descent of the Men of the North. It survives in a manuscript of the late thirteenth century, Peniarth 45, now in the National Library of Wales, and it traces the great families of the North back to two forefathers.[[cite:ho-bonedd]]",
   "The first was Coel Hen, Coel the Old, whose descendants were the Coeling. From him came Urien Rheged and his cousin Llywarch Hen; Clydno Eidyn; Dunod son of Pabo Post Prydain; Gwrgi and Peredur, sons of Eliffer of the Great Retinue; and Gwenddolau son of Ceidio. The second was Dyfnwal Hen, Dyfnwal the Old, from whom came Rhydderch Hael of the Clyde, Mordaf Hael, and Elffin son of Gwyddno.",
   "> Trychan cledyf Kynuerchyn, a thrychan ysgwyt Kynnwydyon, a thrychan wayw Coeling. | Bonedd Gwŷr y Gogledd",
   "‘The three hundred swords of the Cynferchyn, and the three hundred shields of the Cynwydion, and the three hundred spears of the Coeling: whatever errand they went on together, it never failed.’[[cite:ho-bonedd]] The Triads remember the Men of the North just as proudly. Three of them, Nudd, Mordaf and Rhydderch, are the Three Generous Men of the Island of Britain, and for a thousand years after, a Welsh poet could give a patron no higher praise than to call him as generous as Nudd. Dunod son of Pabo, Gwallog son of Lleënog and Cynfelyn Drwsgl are the Three Pillars of Battle.",
   "## Cunedda comes to Gwynedd",
   "The deepest bond between Wales and the Old North is the royal house of Gwynedd itself. The History of the Britons, gathered in Gwynedd about 829, tells that Cunedda came south from Manaw Gododdin with his sons a hundred and forty-six years before Maelgwn Gwynedd reigned, and drove the Irish settlers out of the land with great slaughter, so that they never came back.[[cite:ho-hb]] His sons gave their names to the lands of the north and west: Ceredigion, Meirionnydd, Edeirnion, Dunoding, Rhufoniog.",
   "From Cunedda came Maelgwn Gwynedd, the greatest king of his age, and every king and prince of Gwynedd after him. When Merfyn Frych took the throne in 825, the genealogies traced his father’s line to Llywarch Hen of the North, and his mother Esyllt was of the blood of Cunedda. So Rhodri Mawr, Hywel Dda, Owain Gwynedd and the two Llywelyns were Men of the North on both sides.",
   "## Urien of Rheged",
   "The greatest of the Men of the North was Urien son of Cynfarch, king of Rheged. We know him because his poet was Taliesin, and Taliesin’s poems to him are the oldest praise poems in the Welsh language. They call him lord of Rheged, of Erechwydd and of Catraeth, a giver of gold and horses and mead, a hawk over his enemies. ‘I saw the lord of Catraeth across the plains,’ Taliesin sings.[[cite:ho-urien-wiki]] In Gwaith Gwen Ystrad the men of Catraeth rise at dawn around their king and drive back an invading host; in Gwaith Argoed Llwyfain, when the enemy leader Fflamddwyn, the Flame-Bearer, demands hostages, Owain son of Urien answers with defiance and the men of Rheged ride out behind their king.",
   "> Ac yny vallwyf i hen, ym dygyn agheu aghen, ny bydif ym dirwen na molwyf i Vryen. | Taliesin, Book of Taliesin",
   "‘And until I grow old and fail, in death’s hard need, I shall never be glad unless I praise Urien.’ The same refrain ends poem after poem.",
   "The History of the Britons tells of Urien’s greatest campaign. Four kings of the Britons, Urien, Rhydderch, Gwallog and Morgant, fought against the sons of Ida of Bernicia, and Urien and his sons shut the Angles up on the island of Metcaut, Lindisfarne, for three days and three nights.[[cite:ho-hb]] It was the nearest the Britons of the North ever came to driving the newcomers into the sea. But Urien fell by treachery during the campaign, the History says, out of envy, because his skill in war was greater than any other king’s. In the englynion of the Urien cycle a warrior carries his lord’s head home from the field so that no enemy can shame it: ‘Penn a borthaf’, ‘I carry a head’.",
   "## Owain, Rhun and the line of Urien",
   "Urien’s son Owain ruled Rheged after him, and when he fell, Taliesin made his elegy: ‘The soul of Owain son of Urien, may the Lord look to its need.’ It tells how Owain cut down Fflamddwyn as easily as sleep. Welsh story never let him go. He is the hero of the romance of Owain, or the Lady of the Fountain, and the lord of the three hundred ravens in the Dream of Rhonabwy, and as Yvain he rode through the romances of all Europe.",
   "His brother Rhun did something just as remarkable. When Edwin, king of Northumbria, was baptised at Easter in 627, the History of the Britons says plainly: ‘If any one wishes to know who baptized them, it was Rum Map Urbgen’, Rhun son of Urien.[[cite:ho-hb]] And Rhun’s great-granddaughter Rhiainfellt became the wife of Oswiu, king of Northumbria, so that the blood of Urien Rheged ran in the royal house of the Angles.",
   "## Rhydderch Hael and the kingdom of the Clyde",
   "Beside Urien at Lindisfarne stood Rhydderch Hael, Rhydderch the Generous, king of the Clyde. He is one of the very few kings of his age written of by a stranger: Adomnán, abbot of Iona, remembered ‘Roderc son of Tothail, who reigned on the Rock of Clyde’ as a friend of Saint Columba. He was the patron of Saint Cyndeyrn, Kentigern, who came home from Llanelwy at his call and founded the church round which Glasgow grew. His sword Dyrnwyn is the first of the Thirteen Treasures of the Island of Britain: drawn by a worthy man, it blazed with fire from hilt to point.[[cite:ho-treasures]]",
   "His kingdom outlived all the others. In 642 Owain son of Beli, king of the Britons of the Clyde, beat Domnall Brecc of Dál Riata at Strathcarron, and the Annals of Ulster record that Domnall was slain ‘by Hoan, king of the Britons’.[[cite:ho-au642]] In 870 the Viking kings of Dublin, Olaf and Ivar, besieged the Rock of the Clyde for four months before they took it.[[cite:ho-au870]] Even then the kingdom lived on, ruled from Govan, where the carved stones of its kings, among them a great stone coffin and five Viking-style hogbacks, can still be seen in Govan Old Church.[[cite:ho-govan]] Its kings fought at Brunanburh in 937, and in 1018 Owain Foel, the last king of Strathclyde, marched beside the king of Scots and won the battle of Carham on the Tweed.[[cite:ho-owainfoel]]",
   "## Arfderydd and Myrddin",
   "Not every battle of the North was against the Angles. In 573, the Welsh Annals record, the battle of Arfderydd was fought, ‘in which battle Gwenddolau fell’.[[cite:ho-ac]] The place is Arthuret, on the Esk north of Carlisle, where Carwinley, Caer Wenddolau, still keeps the king’s name. The Triads honour his men as one of the Three Faithful War-Bands of the Island of Britain: after their lord was slain, they fought on for a fortnight and a month. His gwyddbwyll board of gold, whose silver pieces played by themselves, is one of the Thirteen Treasures.[[cite:ho-treasures]]",
   "Welsh tradition holds that Gwenddolau’s bard was Myrddin. After Arfderydd, the old poems of the Black Book of Carmarthen say, Myrddin went out into the forest of Celyddon, grieving for his lord, and there the gift of prophecy came upon him. In Yr Afallennau he speaks to the apple tree that shelters him and foretells the day when the Britons will rise again. Geoffrey of Monmouth carried him into the story of Arthur as Merlin, and Welsh tradition holds that Caerfyrddin, Carmarthen, is his fort.",
   "## Catraeth",
   "About the year 600, Mynyddog Mwynfawr, lord of Din Eidyn, gathered the finest young warriors of the Britons, from Gododdin and Aeron and as far as Gwynedd, and feasted them in his hall for a year on mead and wine. Then he sent them south against the Angles of Deira and Bernicia at Catraeth, Catterick, the old Roman fort on the road to York. They fought for a week, and of all who rode out, only a handful came home.",
   "> Gwŷr a aeth Gatraeth, oedd ffraeth eu llu; glasfedd eu hancwyn, a gwenwyn fu. | Aneirin, Y Gododdin",
   "‘Men went to Catraeth, swift was their host; fresh mead was their feast, and it was poison.’ Their poet was Aneirin, and his poem, Y Gododdin, honours each of them by name: Cynon son of Clydno; Tudfwlch; Cadwal; Gwawrddur, who fed black ravens on the rampart of the fortress, ‘though he was no Arthur’. It is the oldest poetry of Britain in a language still spoken. Among its verses, copied in the same old book, is a tender cradle song, Pais Dinogad, Dinogad’s speckled smock, in which a mother sings to her little son of his father who went hunting with his spear and his dogs. Din Eidyn itself was besieged in 638, the Annals of Ulster record, and passed to the Angles.[[cite:ho-au638]]",
   "## The first poets of Welsh",
   "The History of the Britons names five poets who were famous in British verse in the age of Ida of Bernicia: ‘Talhaiarn Cataguen’, Talhaearn Tad Awen, the father of the Muse; Neirin, who is Aneirin; Taliesin; Blwchfardd; and Cian, ‘who is called Guenith Guaut’.[[cite:ho-hb]] No verse of Talhaearn, Blwchfardd or Cian has come down to us, but the poems of Aneirin and Taliesin have, and with them the Welsh language has the oldest poetry of any living tongue in Britain.",
   "Sir Ifor Williams, the great scholar of Bangor, showed in Canu Aneirin (1938) and Canu Taliesin (1960) that these poems, though written down in Wales in the thirteenth and fourteenth centuries, keep words and forms far older than the books that hold them. They were carried south by bards, learned by heart and handed down for seven hundred years before a scribe wrote them on vellum.",
   "## How the North came to Wales",
   "As the kingdoms of the North fell one by one, their people, their poems and their stories came south. Welsh tradition holds that Llywarch Hen, cousin of Urien, lost his lands in the North and came to Powys, where the englynion of Canu Llywarch Hen mourn his sons, and that he lies at Llanfor near Bala. Pabo Post Prydain, the Pillar of Britain, ended his days in Ynys Môn, where his crowned stone figure still stands in the church at Llanbabo. His grandson Deiniol founded Bangor. Cyndeyrn of the Clyde founded Llanelwy before he went home to Glasgow.",
   "The road ran north as well as south. When Elidir Mwynfawr, a prince of the North, was killed at Aber Mewydus in Arfon, the kings of the North came south to avenge him, and Rhun son of Maelgwn led the men of Gwynedd through the lands of the Britons as far as the Forth. For that march, the Welsh law books say, the men of Arfon won the right to lead the van of the army of Gwynedd for ever.",
   "## How Wales remembers",
   "Wales never forgot the Men of the North. The bards kept their poems; the scribes copied them into the Book of Aneirin, the Book of Taliesin and the Black Book of Carmarthen; the Triads kept their names, their horses and their war bands. Of the Thirteen Treasures of the Island of Britain, the oldest lists say they were ‘in the North’: the sword of Rhydderch, the halter of Clydno Eidyn, the hamper of Gwyddno, the whetstone of Tudwal Tudglyd, the gwyddbwyll board of Gwenddolau.[[cite:ho-treasures]] For centuries the poets of the princes praised their lords by comparing them to Urien, to Rhydderch and to Nudd.",
   "In our own time the North is honoured again. Sir Ifor Williams gave its poems back to the Welsh-speaking world, and in 2021 Gillian Clarke, the former National Poet of Wales, made Y Gododdin new in English as The Gododdin: Lament for the Fallen.[[cite:ho-clarke]] Edinburgh, Glasgow, Dumbarton and Carlisle all have a Welsh past, and their oldest heroes speak to us in Welsh. When a Welsh child today learns the words ‘Gwŷr a aeth Gatraeth’, the Men of the North are still riding.",
  ],
  pCy=[
   "Bedwar can mlynedd ar ddeg yn ôl, gallai teithiwr farchogaeth o lan Hafren i ben Moryd Forth a chlywed yr un iaith yr holl ffordd. Yn neuadd brenin Gwynedd yn Aberffraw, yng nghaer Din Eidyn ar graig Caeredin, ac ar Graig y Clud yn Dumbarton, siaradai’r bobl yr iaith Frythoneg a drodd yn Gymraeg. Roedd teyrnasoedd y Gogledd, rhwng y Clud a’r Pennines, gymaint yn wlad y Cymry â Gwynedd a Phowys. Mae awduron Cymru’n eu galw’n Hen Ogledd, a galwai’r hen feirdd eu pobl yn Wŷr y Gogledd.",
   "Yno, yn y Gogledd, y lluniwyd y cerddi cyntaf yn Gymraeg. Oddi yno y daeth tŷ brenhinol Gwynedd. Ac yno y safodd y Brythoniaid hiraf yn erbyn yr Eingl, nes i frenin olaf Ystrad Clud ennill ei frwydr olaf yn 1018. Dyma eu hanes.",
   "|| Ble | O’r Clud a Gwerydd yn y gogledd hyd y Pennines a Merswy yn y de",
   "|| Pryd | O ddiwedd Prydain Rufeinig, tua 410, hyd frenin olaf Ystrad Clud, tua 1018",
   "|| Y bobl | Brythoniaid, a’u galwai eu hunain yn Gymry, ‘cyd-wladwyr’",
   "|| Y teyrnasoedd | Gododdin, Ystrad Clud, Rheged, Elfed, Efrog, Aeron a Manaw Gododdin",
   "|| Y brenhinoedd | Coel Hen, Cunedda, Urien, Owain, Rhydderch Hael, Gwallog, Mynyddog a llawer mwy",
   "|| Y beirdd | Talhaearn, Aneirin a Thaliesin; Myrddin a Llywarch Hen yn y cerddi sy’n dwyn eu henwau",
   "|| Wedi’u cadw yng Nghymru | Llyfr Aneirin, Llyfr Taliesin, Llyfr Du Caerfyrddin, y Trioedd ac ach Gwŷr y Gogledd",
   "## Un bobl o’r Clud i Hafren",
   "Pan adawodd y llengoedd Brydain tua 410, y Brythoniaid oedd yn rheoli’r ynys gyfan i’r gorllewin ac i’r gogledd o’r tiroedd yr oedd y Saeson a’r Eingl yn eu cymryd. Nid oedd ffin rhwng Cymru a’r Gogledd. Priodai brenhinoedd y ddwy wlad i mewn i dai ei gilydd, canai eu beirdd yn yr un iaith, a theithiai eu saint yn rhydd rhyngddynt. Sefydlodd Cyndeyrn o’r Clud Lanelwy; sefydlodd Deiniol, mab brenin o’r Gogledd, Fangor; ymsefydlodd teulu Caw o Brydyn ym Môn.",
   "Rhannent hyd yn oed enw. Galwai Brythoniaid Cymru a’r Gogledd fel ei gilydd eu hunain yn Gymry, ‘cyd-wladwyr’, ac mae’r un gair yn byw yn Cumbria a Cumberland, gwlad Cymry’r Gogledd.[[cite:ho-cumbric]] Siaradwyd eu hiaith, a eilw ysgolheigion yn Gymbrieg, yn Ystrad Clud o hyd hyd tua’r ddeuddegfed ganrif, ac mae wedi gadael ei hôl dros y map i gyd: llannerch yw Lanark; pen rhyd yw Penrith; eglwys fechan yw Ecclefechan; mae Blencathra’n dechrau â blaen.[[cite:ho-cumbric]] Mae hyd yn oed hen rigymau cyfrif bugeiliaid y Dales, yan, tan, tethera, yn perthyn yn agos i’r un, dau, tri Cymraeg.",
   "!! map",
   "## Teyrnasoedd y Gogledd",
   "Daliai Gododdin y tir o gwmpas Moryd Forth. Yn oes Rhufain y Votadini oedd ei phobl, a’u bryngaer fawr oedd Traprain Law yn Nwyrain Lothian, lle cafwyd celc o arian Rhufeinig yn 1919. Ei chalon yn y chweched ganrif oedd Din Eidyn, y gaer ar graig castell Caeredin, ac ym mhen Gwerydd gorweddai Manaw Gododdin, y mae ei henw’n byw yn Clackmannan a Slamannan.",
   "Rheolid Ystrad Clud o Alclud, Craig y Clud, a alwai’r Gwyddelod yn Dùn Breatann, caer y Brythoniaid: Dumbarton. Hi oedd y gryfaf a’r hiraf ei hoes o deyrnasoedd y gogledd.",
   "Rheged oedd teyrnas Urien, o gwmpas Moryd Solway a Chaer Liwelydd, Carlisle, ac efallai i Galloway a dyffryn Eden. Daliai Elfed ddyffrynnoedd Leeds, ac Efrog oedd gwlad Caer Efrog. Anfonodd Aeron, gwlad afon Ayr yn ôl pob tebyg, ei rhyfelwyr i Gatraeth.[[cite:ho-aeron]] Ymhellach i’r de a’r dwyrain gorweddai teyrnasoedd ifanc yr Eingl, Bernicia a Deira, y mae eu henwau’n Frythoneg: yn y cerddi Brynaich a Deifr ydynt.",
   "## Gwŷr y Gogledd",
   "Cadwodd Cymru gof brenhinoedd y Gogledd mewn testun byr a gwerthfawr, Bonedd Gwŷr y Gogledd. Mae wedi goroesi mewn llawysgrif o ddiwedd y drydedd ganrif ar ddeg, Peniarth 45, sydd heddiw yn Llyfrgell Genedlaethol Cymru, ac mae’n olrhain teuluoedd mawr y Gogledd yn ôl at ddau gyndad.[[cite:ho-bonedd]]",
   "Y cyntaf oedd Coel Hen, a’i ddisgynyddion oedd y Coeling. Ohono ef y daeth Urien Rheged a’i gefnder Llywarch Hen; Clydno Eidyn; Dunod fab Pabo Post Prydain; Gwrgi a Pheredur, meibion Eliffer Gosgorddfawr; a Gwenddolau fab Ceidio. Yr ail oedd Dyfnwal Hen, a ohono ef y daeth Rhydderch Hael o’r Clud, Mordaf Hael, ac Elffin fab Gwyddno.",
   "> Trychan cledyf Kynuerchyn, a thrychan ysgwyt Kynnwydyon, a thrychan wayw Coeling. | Bonedd Gwŷr y Gogledd",
   "‘Trichant cleddyf Cynferchyn, a thrichant ysgwyd Cynwydion, a thrichant gwaew Coeling: pa neges bynnag yr elynt iddi yn gytûn, ni fethai honno.’[[cite:ho-bonedd]] Mae’r Trioedd yn cofio Gwŷr y Gogledd yr un mor falch. Tri ohonynt, Nudd, Mordaf a Rhydderch, yw Tri Hael Ynys Prydain, ac am fil o flynyddoedd wedyn ni allai bardd o Gymro roi uwch clod i noddwr na’i alw mor hael â Nudd. Dunod fab Pabo, Gwallog fab Lleënog a Chynfelyn Drwsgl yw Tri Phost Cad.",
   "## Cunedda’n dod i Wynedd",
   "Y cwlwm dyfnaf rhwng Cymru a’r Hen Ogledd yw tŷ brenhinol Gwynedd ei hun. Mae Hanes y Brythoniaid, a gasglwyd yng Ngwynedd tua 829, yn adrodd i Gunedda ddod i’r de o Fanaw Gododdin gyda’i feibion gant pedwar deg a chwech o flynyddoedd cyn teyrnasiad Maelgwn Gwynedd, a gyrru’r gwladfawyr Gwyddelig o’r wlad â lladdfa fawr, fel na ddaethant fyth yn ôl.[[cite:ho-hb]] Rhoddodd ei feibion eu henwau i diroedd y gogledd a’r gorllewin: Ceredigion, Meirionnydd, Edeirnion, Dunoding, Rhufoniog.",
   "O Gunedda y daeth Maelgwn Gwynedd, brenin mwyaf ei oes, a phob brenin a thywysog o Wynedd ar ei ôl. Pan gymerodd Merfyn Frych yr orsedd yn 825, olrheiniai’r achau linach ei dad at Lywarch Hen o’r Gogledd, ac roedd ei fam Esyllt o waed Cunedda. Felly roedd Rhodri Mawr, Hywel Dda, Owain Gwynedd a’r ddau Lywelyn yn Wŷr y Gogledd o’r ddwy ochr.",
   "## Urien Rheged",
   "Y mwyaf o Wŷr y Gogledd oedd Urien fab Cynfarch, brenin Rheged. Fe’i hadwaenwn am mai Taliesin oedd ei fardd, a cherddi Taliesin iddo yw’r cerddi mawl hynaf yn yr iaith Gymraeg. Maent yn ei alw’n arglwydd Rheged, Erechwydd a Chatraeth, yn rhoddwr aur a meirch a medd, yn hebog uwchben ei elynion. ‘Gwelais i lyw Catraeth tra maes,’ cân Taliesin.[[cite:ho-urien-wiki]] Yng Ngwaith Gwen Ystrad mae gwŷr Catraeth yn codi gyda’r wawr o gwmpas eu brenin ac yn gyrru llu goresgynnol yn ôl; yng Ngwaith Argoed Llwyfain, pan fo arweinydd y gelyn, Fflamddwyn, yn mynnu gwystlon, mae Owain fab Urien yn ateb yn herfeiddiol a gwŷr Rheged yn marchogaeth allan y tu ôl i’w brenin.",
   "> Ac yny vallwyf i hen, ym dygyn agheu aghen, ny bydif ym dirwen na molwyf i Vryen. | Taliesin, Llyfr Taliesin",
   "Hyd nes i mi heneiddio a phallu, yn angen caled angau, ni fyddaf fyth yn llawen oni folaf i Urien: mae’r un byrdwn yn cloi cerdd ar ôl cerdd.",
   "Mae Hanes y Brythoniaid yn adrodd am ymgyrch fwyaf Urien. Ymladdodd pedwar o frenhinoedd y Brythoniaid, Urien, Rhydderch, Gwallog a Morgant, yn erbyn meibion Ida o Frynaich, a chaeodd Urien a’i feibion yr Eingl ar ynys Metcaut, Lindisfarne, am dri diwrnod a thair noson.[[cite:ho-hb]] Dyna’r agosaf y daeth Brythoniaid y Gogledd erioed at yrru’r dyfodiaid i’r môr. Ond syrthiodd Urien drwy frad yn ystod yr ymgyrch, medd yr Hanes, o genfigen, am fod ei ddawn mewn rhyfel yn fwy na dawn unrhyw frenin arall. Yn englynion cylch Urien mae rhyfelwr yn cario pen ei arglwydd adref o’r maes fel na all unrhyw elyn ei gywilyddio: ‘Pen a borthaf’.",
   "## Owain, Rhun a llinach Urien",
   "Teyrnasodd Owain fab Urien ar Reged ar ei ôl, a phan syrthiodd, lluniodd Taliesin ei farwnad: ‘Enaid Owain ab Urien, gobwyllid Rheen o’i raid.’ Mae’n adrodd sut y lladdodd Owain Fflamddwyn mor hawdd â chysgu. Ni ollyngodd chwedlau Cymru ef fyth. Ef yw arwr rhamant Owain, neu Iarlles y Ffynnon, ac arglwydd y trichant o frain yn Breuddwyd Rhonabwy, ac fel Yvain marchogodd drwy ramantau Ewrop gyfan.",
   "Gwnaeth ei frawd Rhun rywbeth yr un mor rhyfeddol. Pan fedyddiwyd Edwin, brenin Northumbria, adeg y Pasg yn 627, dywed Hanes y Brythoniaid yn blaen mai Rhun fab Urien a’u bedyddiodd.[[cite:ho-hb]] A daeth gor-wyres Rhun, Rhiainfellt, yn wraig i Oswiu, brenin Northumbria, fel bod gwaed Urien Rheged yn rhedeg yn nhŷ brenhinol yr Eingl.",
   "## Rhydderch Hael a theyrnas y Clud",
   "Wrth ochr Urien yn Lindisfarne safai Rhydderch Hael, brenin y Clud. Mae’n un o’r ychydig iawn o frenhinoedd ei oes yr ysgrifennodd dieithryn amdanynt: cofiai Adomnán, abad Iona, am ‘Roderc fab Tothail, a deyrnasai ar Graig y Clud’ fel cyfaill i Golwmba Sant. Ef oedd noddwr Sant Cyndeyrn, a ddaeth adref o Lanelwy ar ei alwad a sefydlu’r eglwys y tyfodd Glasgow o’i chwmpas. Ei gleddyf Dyrnwyn yw’r cyntaf o Dri Thlws ar Ddeg Ynys Prydain: o’i dynnu gan ŵr teilwng, fflamiai â thân o’r carn i’r blaen.[[cite:ho-treasures]]",
   "Goroesodd ei deyrnas bob un arall. Yn 642 trechodd Owain fab Beli, brenin Brythoniaid y Clud, Domnall Brecc o Dál Riata yn Srath Caruin, ac mae Annalau Ulster yn cofnodi i Domnall gael ei ladd gan Hoan, brenin y Brythoniaid.[[cite:ho-au642]] Yn 870 gwarchaeodd brenhinoedd Llychlynnaidd Dulyn, Olaf ac Ivar, ar Graig y Clud am bedwar mis cyn ei chipio.[[cite:ho-au870]] Hyd yn oed wedyn parhaodd y deyrnas, wedi’i rheoli o Govan, lle gellir gweld meini cerfiedig ei brenhinoedd o hyd yn Hen Eglwys Govan, yn eu plith arch garreg fawr a phum carreg gefngrwm yn null y Llychlynwyr.[[cite:ho-govan]] Ymladdodd ei brenhinoedd yn Brunanburh yn 937, ac yn 1018 gorymdeithiodd Owain Foel, brenin olaf Ystrad Clud, ochr yn ochr â brenin yr Alban ac ennill brwydr Carham ar afon Tweed.[[cite:ho-owainfoel]]",
   "## Arfderydd a Myrddin",
   "Nid yn erbyn yr Eingl yr ymladdwyd pob brwydr yn y Gogledd. Yn 573, medd yr Annales Cambriae, ymladdwyd brwydr Arfderydd, ‘lle syrthiodd Gwenddolau’.[[cite:ho-ac]] Arthuret yw’r lle, ar lan afon Esk i’r gogledd o Carlisle, lle mae Carwinley, Caer Wenddolau, yn cadw enw’r brenin o hyd. Mae’r Trioedd yn anrhydeddu ei wŷr yn un o Dri Diwair Deulu Ynys Prydain: wedi lladd eu harglwydd, ymladdasant ymlaen am bythefnos a mis. Mae ei wyddbwyll aur, y chwaraeai ei darnau arian ohonynt eu hunain, yn un o’r Tri Thlws ar Ddeg.[[cite:ho-treasures]]",
   "Yn ôl traddodiad Cymru, Myrddin oedd bardd Gwenddolau. Wedi Arfderydd, medd hen gerddi Llyfr Du Caerfyrddin, aeth Myrddin allan i goedwig Celyddon yn galaru am ei arglwydd, a daeth dawn proffwydoliaeth arno yno. Yn Yr Afallennau mae’n siarad â’r pren afalau sy’n ei gysgodi ac yn rhagweld y dydd pan gyfyd y Brythoniaid eto. Cariodd Sieffre o Fynwy ef i hanes Arthur fel Merlin, ac yn ôl traddodiad Cymru Caerfyrddin yw ei gaer.",
   "## Catraeth",
   "Tua’r flwyddyn 600, casglodd Mynyddog Mwynfawr, arglwydd Din Eidyn, ryfelwyr ifanc gorau’r Brythoniaid, o Ododdin ac Aeron a chyn belled â Gwynedd, a’u gwledda yn ei neuadd am flwyddyn ar fedd a gwin. Yna anfonodd hwy i’r de yn erbyn Eingl Deifr a Brynaich yng Nghatraeth, Catterick, yr hen gaer Rufeinig ar y ffordd i Efrog. Ymladdasant am wythnos, ac o’r holl rai a farchogodd allan, dim ond dyrnaid a ddaeth adref.",
   "> Gwŷr a aeth Gatraeth, oedd ffraeth eu llu; glasfedd eu hancwyn, a gwenwyn fu. | Aneirin, Y Gododdin",
   "Aneirin oedd eu bardd, ac mae ei gerdd, Y Gododdin, yn anrhydeddu pob un ohonynt wrth ei enw: Cynon fab Clydno; Tudfwlch; Cadwal; Gwawrddur, a borthai frain duon ar fur y gaer, ‘ceni bei ef Arthur’. Dyma’r farddoniaeth hynaf ym Mhrydain mewn iaith a siaredir o hyd. Ymhlith ei phenillion, wedi’i chopïo yn yr un hen lyfr, mae hwiangerdd dyner, Pais Dinogad, lle mae mam yn canu i’w mab bach am ei dad a âi i hela â’i waywffon a’i gŵn. Gwarchaewyd Din Eidyn ei hun yn 638, medd Annalau Ulster, ac aeth i’r Eingl.[[cite:ho-au638]]",
   "## Beirdd cyntaf y Gymraeg",
   "Mae Hanes y Brythoniaid yn enwi pum bardd a oedd yn enwog mewn barddoniaeth Frythoneg yn oes Ida o Frynaich: Talhaearn Tad Awen; Neirin, sef Aneirin; Taliesin; Blwchfardd; a Chian, ‘a elwir Gwenith Gwawd’.[[cite:ho-hb]] Ni ddaeth unrhyw bennill gan Dalhaearn, Blwchfardd na Chian i lawr atom, ond daeth cerddi Aneirin a Thaliesin, a chyda hwy mae gan yr iaith Gymraeg y farddoniaeth hynaf o unrhyw iaith fyw ym Mhrydain.",
   "Dangosodd Syr Ifor Williams, ysgolhaig mawr Bangor, yn Canu Aneirin (1938) a Canu Taliesin (1960) fod y cerddi hyn, er mai yng Nghymru yn y drydedd a’r bedwaredd ganrif ar ddeg yr ysgrifennwyd hwy, yn cadw geiriau a ffurfiau llawer hŷn na’r llyfrau sy’n eu dal. Cariwyd hwy i’r de gan feirdd, eu dysgu ar y cof a’u trosglwyddo am saith can mlynedd cyn i gopïydd eu hysgrifennu ar femrwn.",
   "## Sut y daeth y Gogledd i Gymru",
   "Wrth i deyrnasoedd y Gogledd syrthio fesul un, daeth eu pobl, eu cerddi a’u straeon i’r de. Yn ôl traddodiad Cymru collodd Llywarch Hen, cefnder Urien, ei diroedd yn y Gogledd a dod i Bowys, lle mae englynion Canu Llywarch Hen yn galaru am ei feibion, ac mae’n gorwedd yn Llanfor ger y Bala. Diweddodd Pabo Post Prydain ei ddyddiau ym Môn, lle saif ei ddelw garreg goronog o hyd yn eglwys Llanbabo. Sefydlodd ei ŵyr Deiniol Fangor. Sefydlodd Cyndeyrn o’r Clud Lanelwy cyn mynd adref i Glasgow.",
   "Rhedai’r ffordd tua’r gogledd yn ogystal â’r de. Pan laddwyd Elidir Mwynfawr, tywysog o’r Gogledd, yn Aber Mewydus yn Arfon, daeth brenhinoedd y Gogledd i’r de i ddial amdano, ac arweiniodd Rhun fab Maelgwn wŷr Gwynedd drwy diroedd y Brythoniaid hyd at Werydd. Am y daith honno, medd llyfrau cyfraith Cymru, enillodd gwŷr Arfon yr hawl i arwain blaen byddin Gwynedd am byth.",
   "## Sut y mae Cymru’n cofio",
   "Nid anghofiodd Cymru Wŷr y Gogledd erioed. Cadwodd y beirdd eu cerddi; copïodd yr ysgrifwyr hwy i Lyfr Aneirin, Llyfr Taliesin a Llyfr Du Caerfyrddin; cadwodd y Trioedd eu henwau, eu meirch a’u gosgorddion. Am Dri Thlws ar Ddeg Ynys Prydain, dywed yr hen restrau eu bod ‘yn y Gogledd’: cleddyf Rhydderch, cebystr Clydno Eidyn, mwys Gwyddno, hogalen Tudwal Tudglyd, gwyddbwyll Gwenddolau.[[cite:ho-treasures]] Am ganrifoedd canmolai Beirdd y Tywysogion eu harglwyddi drwy eu cymharu ag Urien, â Rhydderch ac â Nudd.",
   "Yn ein hoes ni mae’r Gogledd yn cael ei anrhydeddu eto. Rhoddodd Syr Ifor Williams ei gerddi yn ôl i’r byd Cymraeg, ac yn 2021 gwnaeth Gillian Clarke, cyn-Fardd Cenedlaethol Cymru, Y Gododdin yn newydd yn Saesneg fel The Gododdin: Lament for the Fallen.[[cite:ho-clarke]] Mae gan Gaeredin, Glasgow, Dumbarton a Carlisle orffennol Cymraeg, ac mae eu harwyr hynaf yn siarad â ni yn Gymraeg. Pan fo plentyn yng Nghymru heddiw’n dysgu’r geiriau ‘Gwŷr a aeth Gatraeth’, mae Gwŷr y Gogledd yn dal i farchogaeth.",
  ],
)
# the map of the Old North goes where the paragraph "!! map" is (build.py fills it in, north_map())
_BYSA = "https://creativecommons.org/licenses/by-sa/"
FIGS = {  # Commons file, author, licence, licence link, caption EN, caption CY, width, height (see lit_fig in build.py)
    "traprain": ("Traprain Law from the north.JPG", "Kim Traynor", "CC BY-SA 3.0", _BYSA + "3.0",
                 "Traprain Law in East Lothian, the great hill fort of the Votadini, the Gododdin of Roman times",
                 "Traprain Law yn Nwyrain Lothian, bryngaer fawr y Votadini, Gododdin oes Rhufain", 3975, 2219),
    "alclud": ("Dumbarton Castle from the south.JPG", "Rosser1954", "CC BY-SA 4.0", _BYSA + "4.0",
               "Dumbarton Rock, Alt Clut, the Rock of the Clyde: the seat of the kings of Ystrad Clud for four hundred years",
               "Craig Dumbarton, Alclud, Craig y Clud: sedd brenhinoedd Ystrad Clud am bedwar can mlynedd", 4518, 3332),
    "lindisfarne": ("LindisfarneCastleHolyIsland.jpg", "Matthew Hunt", "CC BY 2.0", "https://creativecommons.org/licenses/by/2.0",
                    "Lindisfarne, Ynys Metcaud, where Urien and the kings of the Britons held the Angles under siege",
                    "Lindisfarne, Ynys Fedcawd, lle gwarchaeodd Urien a brenhinoedd y Brythoniaid ar yr Eingl", 2048, 1323),
    "govan": ("Carved sarcophagus in Govan Old Church.jpg", "Joedkins", "CC BY-SA 3.0", _BYSA + "3.0",
              "The carved sarcophagus in Govan Old Church, made in the age of the later kings of Strathclyde",
              "Yr arch gerfiedig yn Hen Eglwys Govan, a wnaed yn oes brenhinoedd diweddarach Ystrad Clud", 2048, 1536),
    "arthuret": ("Arthuret Church and tower, Longtown, Cumbria, England.jpg", "Rosser1954", "CC BY-SA 4.0", _BYSA + "4.0",
                 "Arthuret church by the river Esk, near the field of Arfderydd, where Gwenddolau fell in 573",
                 "Eglwys Arthuret ger afon Esk, ger maes Arfderydd, lle syrthiodd Gwenddolau yn 573", 4896, 2752),
}
STORY["figs"] = dict(FIGS)  # build.py adds the map at '!! map'
# the pictures go after these paragraphs (the English and Welsh run paragraph for paragraph); gallery ids come from src/gallery_photos.py
for _after, _key in sorted([(14, "traprain"), (15, "alclud"), (28, "trea-book-taliesin"), (29, "lindisfarne"), (35, "govan"),
                            (37, "arthuret"), (38, "trea-black-book"), (42, "trea-book-aneirin")], reverse=True):
    STORY["pEn"].insert(_after + 1, "!! " + _key)
    STORY["pCy"].insert(_after + 1, "!! " + _key)

# ---------------------------------------------------------------- reading list
_P, _B = "p", "b"
REFS = {
 "hen-ogledd": dict(dwb=["aneirin", "taliesin", "urien-rheged", "llywarch-hen", "cunedda", "rhydderch-hael"], items=[
   (_P, "Sir Ifor Williams (ed.)", "Canu Aneirin", "Gwasg Prifysgol Cymru, 1938",
    "The great edition of Y Gododdin, which set the poem in the world of the Old North.",
    "Yr argraffiad mawr o’r Gododdin, a osododd y gerdd ym myd yr Hen Ogledd."),
   (_P, "Sir Ifor Williams (ed.), English version by J. E. Caerwyn Williams", "The Poems of Taliesin", "Dublin Institute for Advanced Studies, 1968",
    "Taliesin’s poems to Urien, Owain and Gwallog, with notes; first published in Welsh as Canu Taliesin, 1960.",
    "Cerddi Taliesin i Urien, Owain a Gwallog, gyda nodiadau; cyhoeddwyd gyntaf yn Gymraeg fel Canu Taliesin, 1960."),
   (_P, "A. O. H. Jarman (ed. and trans.)", "Aneirin: Y Gododdin, Britain’s Oldest Heroic Poem", "Gomer Press, 1988",
    "The whole poem in Welsh with an English translation and an introduction.",
    "Y gerdd gyfan yn Gymraeg gyda chyfieithiad Saesneg a rhagymadrodd."),
   (_P, "Gillian Clarke", "The Gododdin: Lament for the Fallen", "Faber & Faber, 2021",
    "Y Gododdin made new in English by the former National Poet of Wales.",
    "Y Gododdin wedi’i gwneud yn newydd yn Saesneg gan gyn-Fardd Cenedlaethol Cymru."),
   (_P, "Rachel Bromwich (ed. and trans.)", "Trioedd Ynys Prydein: The Triads of the Island of Britain", "University of Wales Press, 4th edition, 2014",
    "The Triads with notes on every name in them, among them the Men of the North and the Thirteen Treasures.",
    "Y Trioedd gyda nodiadau ar bob enw ynddynt, yn eu plith Gwŷr y Gogledd a’r Tri Thlws ar Ddeg."),
   (_P, "P. C. Bartrum (ed.)", "Early Welsh Genealogical Tracts", "University of Wales Press, 1966",
    "The old Welsh pedigrees, among them Bonedd Gwŷr y Gogledd, the Descent of the Men of the North.",
    "Yr hen achau Cymreig, yn eu plith Bonedd Gwŷr y Gogledd."),
   (_P, "Jenny Rowland", "Early Welsh Saga Poetry: A Study and Edition of the Englynion", "D. S. Brewer, 1990",
    "The englynion of Llywarch Hen and of the Urien cycle, in Welsh and English.",
    "Englynion Llywarch Hen a chylch Urien, yn Gymraeg ac yn Saesneg."),
   (_B, "Tim Clarkson", "The Men of the North: The Britons of Southern Scotland", "John Donald, 2010",
    "The history of the kingdoms of the Old North, from Rome to the end of Strathclyde.",
    "Hanes teyrnasoedd yr Hen Ogledd, o Rufain hyd ddiwedd Ystrad Clud."),
   (_B, "John T. Koch", "The Gododdin of Aneirin: Text and Context from Dark-Age North Britain", "University of Wales Press, 1997",
    "A modern edition of the poem with a full study of its world.",
    "Argraffiad modern o’r gerdd gydag astudiaeth lawn o’i byd."),
 ]),
}

# ---------------------------------------------------------------- sources beside the claims
# Each one opened and read (November 2026).
CITES = {
    "ho-hb": dict(
        short=("History of the Britons", "Hanes y Brythoniaid"),
        t="History of the Britons (Historia Brittonum), chapters 57, 62 and 63", by=("gathered in Gwynedd about 829; translated by J. A. Giles, Project Gutenberg", "a gasglwyd yng Ngwynedd tua 829; cyfieithiad Saesneg J. A. Giles, Project Gutenberg"),
        note=("Chapter 62: “Talhaiarn Cataguen was famed for poetry, and Neirin, and Taliesin and Bluchbard, and Cian, who is called Guenith Guaut”; Cunedda came from Manau Guotodin 146 years before Mailcun reigned and drove out the Scots. Chapter 63: “Against him fought four kings, Urien, and Ryderthen, and Guallauc, and Morcant”; Theodric shut up “three days and three nights in the island of Metcaut”; Edwin “seized on Elmete, and expelled Cerdic, its king”; “it was Rum Map Urbgen” who baptised them. Chapter 57: Oswy’s wife “Riemmelth, the daughter of Royth, son of Rum”.",
              "Pennod 62: Talhaearn Tad Awen, Neirin, Taliesin, Blwchfardd a Chian Gwenith Gwawd yn enwog am farddoniaeth; daeth Cunedda o Fanaw Gododdin 146 o flynyddoedd cyn teyrnasiad Maelgwn a gyrru’r Gwyddelod allan. Pennod 63: pedwar brenin, Urien, Rhydderch, Gwallog a Morgant; gwarchae tri diwrnod a thair noson ar ynys Metcaut; Edwin yn cipio Elfed ac yn gyrru Ceredig ei brenin allan; Rhun fab Urien a’u bedyddiodd. Pennod 57: gwraig Oswiu, Rhiainfellt ferch Rhoth fab Rhun."),
        url="https://www.gutenberg.org/ebooks/1972", lang="en"),
    "ho-ac": dict(
        short=("Welsh Annals", "Annales Cambriae"),
        t="Annales Cambriae, the Welsh Annals", by=("Fordham University, Internet Medieval Sourcebook", "Prifysgol Fordham, Internet Medieval Sourcebook"),
        note=("573: the battle of Arfderydd, “in which battle Gwenddolau fell”. 580: “Gwrgi and Peredur sons of Elifert died.” 595: “The death of king Dunod son of Pabo.” 616: “Ceredig died.” 870: “The fortress of Alt Clud was broken by the gentiles.”",
              "573: brwydr Arfderydd, lle syrthiodd Gwenddolau. 580: bu farw Gwrgi a Pheredur, meibion Eliffer. 595: marw’r brenin Dunod fab Pabo. 616: bu farw Ceredig. 870: torrwyd caer Alclud gan y paganiaid."),
        url="https://sourcebooks.web.fordham.edu/source/annalescambriae.asp", lang="en"),
    "ho-bonedd": dict(
        short=("Bonedd Gwŷr y Gogledd", "Bonedd Gwŷr y Gogledd"),
        t="Bonedd Gwŷr y Gogledd, the Descent of the Men of the North", by=("Peniarth MS 45, late 13th century, National Library of Wales; text and translation on maryjones.us", "Llawysgrif Peniarth 45, diwedd y 13eg ganrif, Llyfrgell Genedlaethol Cymru; testun a chyfieithiad ar maryjones.us"),
        note=("Urien son of Cynfarch son of Meirchion son of Gwrwst Ledlwm son of Ceneu son of Coel; Llywarch Hen son of Elidir Lydanwyn; Clydno Eidyn, Dunawd son of Pabo, Gwrgi and Peredur sons of Eliffer, and Gwenddolau, Nudd and Cof sons of Ceidio, all of the line of Arthwys son of Mar son of Ceneu son of Coel; Rhydderch Hael son of Tudwal Tudglyd son of Cedig son of Dyfnwal Hen; Mordaf son of Serwan son of Cedig; Elffin son of Gwyddno son of Cawrdaf son of Garmonion son of Dyfnwal Hen. “The 300 swords of the Cynferchyn, and the 300 shields of the Cynwydion, and the 300 spears of the Coeling.”",
              "Urien fab Cynfarch fab Meirchion fab Gwrwst Ledlwm fab Ceneu fab Coel; Llywarch Hen fab Elidir Lydanwyn; Clydno Eidyn, Dunawd fab Pabo, Gwrgi a Pheredur meibion Eliffer, a Gwenddolau, Nudd a Chof meibion Ceidio, o linach Arthwys fab Mar fab Ceneu fab Coel; Rhydderch Hael fab Tudwal Tudglyd fab Cedig fab Dyfnwal Hen; Mordaf fab Serwan fab Cedig; Elffin fab Gwyddno fab Cawrdaf fab Garmonion fab Dyfnwal Hen. Trichant cleddyf Cynferchyn, trichant ysgwyd Cynwydion a thrichant gwaew Coeling."),
        url="https://www.maryjones.us/ctexts/bonedd.html", lang="en"),
    "ho-au638": dict(
        short=("Annals of Ulster, 638", "Annalau Ulster, 638"),
        t="The Annals of Ulster, the year 638", by=("Corpus of Electronic Texts, University College Cork", "Corpus Testunau Electronig, Coleg Prifysgol Corc"),
        note=("U638.1: “The battle of Glenn Muiresan and the besieging of Eten”, Din Eidyn, Edinburgh.", "U638.1: brwydr Glenn Muiresan a’r gwarchae ar Eten, Din Eidyn."),
        url="https://celt.ucc.ie/published/T100001A/text208.html", lang="en"),
    "ho-au642": dict(
        short=("Annals of Ulster, 642", "Annalau Ulster, 642"),
        t="The Annals of Ulster, the year 642", by=("Corpus of Electronic Texts, University College Cork", "Corpus Testunau Electronig, Coleg Prifysgol Corc"),
        note=("U642.1: “Domnall Brec was slain at the end of the year, in December, in the battle of Srath Caruin, by Hoan, king of the Britons.”", "U642.1: lladdwyd Domnall Brecc ar ddiwedd y flwyddyn, ym mis Rhagfyr, ym mrwydr Srath Caruin, gan Hoan, brenin y Brythoniaid."),
        url="https://celt.ucc.ie/published/T100001A/text212.html", lang="en"),
    "ho-au870": dict(
        short=("Annals of Ulster, 870", "Annalau Ulster, 870"),
        t="The Annals of Ulster, the year 870", by=("Corpus of Electronic Texts, University College Cork", "Corpus Testunau Electronig, Coleg Prifysgol Corc"),
        note=("“The siege of Ail Cluaithe by the Norsemen: Amlaíb and Ímar, two kings of the Norsemen, laid siege to the fortress”, and took it at the end of four months.", "Gwarchae Ail Cluaithe, Alclud, gan y Llychlynwyr: gwarchaeodd Amlaíb ac Ímar, dau frenin y Llychlynwyr, ar y gaer, a’i chipio ymhen pedwar mis."),
        url="https://celt.ucc.ie/published/T100001A/text440.html", lang="en"),
    "ho-urien-wiki": dict(
        short=("Wikipedia, Urien", "Wicipedia, Urien"),
        t="Urien", by=("Wikipedia", "Wikipedia"),
        note=("Eight poems in the Book of Taliesin address Urien, seven of them ending with the same refrain. In Yspeil Taliesin: “gweleis i lyw katraeth tra maeu”, “I saw the lord of Catraeth across the plains”. In the Urien cycle of englynion: “penn a borthaf”, “I carry a head”. Urien slain while besieging Theodric on Medcaut, by envy.",
              "Mae wyth cerdd yn Llyfr Taliesin yn cyfarch Urien, a saith ohonynt yn gorffen â’r un byrdwn. Yn Yspeil Taliesin: ‘gweleis i lyw katraeth tra maeu’. Yng nghylch englynion Urien: ‘penn a borthaf’. Lladdwyd Urien tra’n gwarchae ar Theodric ar Fedcawd, o genfigen."),
        url="https://en.wikipedia.org/wiki/Urien", lang="en"),
    "ho-cumbric": dict(
        short=("Wikipedia, Cumbric", "Wicipedia, Cumbric"),
        t="Cumbric", by=("Wikipedia", "Wikipedia"),
        note=("The British language of the Old North; probably gone by the 12th century. Cumbria from the Cumbri, “fellow countrymen”. Place names: Lanark from llannerch, Penrith pen + rhyd “chief ford”, Ecclefechan with eglwys, Blencathra with blaen. The counting scores of northern England come from a British language close to Welsh.",
              "Iaith Frythonig yr Hen Ogledd; wedi mynd erbyn y 12fed ganrif yn ôl pob tebyg. Cumbria o’r Cumbri, ‘cyd-wladwyr’. Enwau lleoedd: Lanark o llannerch, Penrith pen + rhyd, Ecclefechan ag eglwys, Blencathra â blaen. Daw hen rifau cyfrif gogledd Lloegr o iaith Frythonig agos at y Gymraeg."),
        url="https://en.wikipedia.org/wiki/Cumbric", lang="en"),
    "ho-aeron": dict(
        short=("Wikipedia, Aeron", "Wicipedia, Aeron"),
        t="Aeron (kingdom)", by=("Wikipedia", "Wikipedia"),
        note=("Most often placed in Ayrshire, by the river Ayr; Ifor Williams and John Koch favour it. Named in the Book of Taliesin with Urien, and in Y Gododdin, where Cynon son of Clydno comes with “the desolating spears of Aeron”.",
              "Fe’i gosodir amlaf yn Swydd Ayr, ger afon Ayr; dyna farn Ifor Williams a John Koch. Fe’i henwir yn Llyfr Taliesin gydag Urien, ac yn Y Gododdin, lle daw Cynon fab Clydno gyda gwaywawr Aeron."),
        url="https://en.wikipedia.org/wiki/Aeron_(kingdom)", lang="en"),
    "ho-treasures": dict(
        short=("Wikipedia, Thirteen Treasures", "Wicipedia, y Tri Thlws ar Ddeg"),
        t="Thirteen Treasures of the Island of Britain", by=("Wikipedia, after Rachel Bromwich’s edition", "Wikipedia, ar sail argraffiad Rachel Bromwich"),
        note=("Dyrnwyn, the sword of Rhydderch Hael, which bursts into flame from hilt to tip in a well-born man’s hand; the hamper of Gwyddno Garanhir; the halter of Clydno Eidyn; the whetstone of Tudwal Tudglyd; the gold gwyddbwyll board of Gwenddolau son of Ceidio, whose silver pieces play by themselves. Most are placed in the Old North, and some early manuscripts describe the whole list as treasures “that were in the North”.",
              "Dyrnwyn, cleddyf Rhydderch Hael, sy’n fflamio o’r carn i’r blaen yn llaw gŵr bonheddig; mwys Gwyddno Garanhir; cebystr Clydno Eidyn; hogalen Tudwal Tudglyd; gwyddbwyll aur Gwenddolau fab Ceidio, y chwaraeai ei darnau arian ohonynt eu hunain. Gosodir y rhan fwyaf yn yr Hen Ogledd, ac mae rhai llawysgrifau cynnar yn disgrifio’r rhestr gyfan fel tlysau ‘a oedd yn y Gogledd’."),
        url="https://en.wikipedia.org/wiki/Thirteen_Treasures_of_the_Island_of_Britain", lang="en"),
    "ho-govan": dict(
        short=("The Govan Stones", "Meini Govan"),
        t="Govan Stones", by=("Wikipedia; the stones are kept in Govan Old Parish Church, Glasgow (thegovanstones.org.uk)", "Wikipedia; cedwir y meini yn Hen Eglwys Plwyf Govan, Glasgow (thegovanstones.org.uk)"),
        note=("A sarcophagus, five hogbacks, four standing crosses and many cross-slabs of the 9th to 11th centuries, thought to remember the rulers of the British kingdom of Strathclyde, which moved its centre up the Clyde to Govan after Dumbarton Rock fell in 870.",
              "Arch garreg, pum carreg gefngrwm, pedair croes sefyll a llawer o slabiau croes o’r 9fed i’r 11eg ganrif, y credir eu bod yn cofio rheolwyr teyrnas Frythonig Ystrad Clud, a symudodd ei chanolfan i fyny’r Clud i Govan wedi cwymp Craig Dumbarton yn 870."),
        url="https://en.wikipedia.org/wiki/Govan_Stones", lang="en"),
    "ho-owainfoel": dict(
        short=("Wikipedia, Owain Foel", "Wicipedia, Owain Foel"),
        t="Owain Foel", by=("Wikipedia", "Wikipedia"),
        note=("The last known king of Strathclyde. The twelfth-century Historia regum Anglorum names him Eugenius Calvus, “rex Clutinensium”, king of the Clydesmen, fighting with Malcolm, king of Scots, when they beat the English at Carham in 1018.",
              "Brenin olaf hysbys Ystrad Clud. Mae’r Historia regum Anglorum o’r ddeuddegfed ganrif yn ei enwi’n Eugenius Calvus, brenin gwŷr y Clud, yn ymladd gyda Malcolm, brenin yr Alban, pan drechasant y Saeson yn Carham yn 1018."),
        url="https://en.wikipedia.org/wiki/Owain_Foel", lang="en"),
    "ho-yarrow": dict(
        short=("Canmore, the Yarrow Stone", "Canmore, Carreg Yarrow"),
        t="Yarrow Stone, Selkirkshire", by=("Canmore, Historic Environment Scotland", "Canmore, Amgylchedd Hanesyddol yr Alban"),
        note=("An inscribed memorial stone of the early sixth century: the most famous princes Nudus and Dumnogenus lie here; in the tomb lie the two sons of Liberalis.",
              "Carreg goffa ag arysgrif o ddechrau’r chweched ganrif: yma y gorwedd y tywysogion enwocaf Nudus a Dumnogenus; yn y bedd gorwedd dau fab Liberalis."),
        url="https://canmore.org.uk/site/53078", lang="en"),
    "ho-clarke": dict(
        short=("Faber, 2021", "Faber, 2021"),
        t="The Gododdin: Lament for the Fallen", by=("Gillian Clarke, Faber & Faber, 2021 (ISBN 9780571352111)", "Gillian Clarke, Faber & Faber, 2021 (ISBN 9780571352111)"),
        note=("A new English version of Aneirin’s Y Gododdin by the former National Poet of Wales.", "Fersiwn Saesneg newydd o’r Gododdin gan Aneirin, gan gyn-Fardd Cenedlaethol Cymru."),
        url="https://www.faber.co.uk/product/9780571352111-the-gododdin/", lang="en"),
}
