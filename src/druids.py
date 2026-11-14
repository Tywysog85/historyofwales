# The Druids: the teachers of the Britons, to whose island Europe came to learn (story-druids.html).
# Asked for by Ifan, 13 November 2026: "Make sure there is a page on druids and about how they were teachers etc and how
# people from all over Europe came here to learn from them. Also mention how Caesar said they use Greek letters. I don't
# want it said that they sacrificed people or anything else negative." Then: "Write everything positive."
#
# House rules (EDITORIAL.md): proud; the people are Britons and Cymry, never "Celts" in our own words; Britain was the
# home of Druid learning, in Caesar's own words. This page tells only what the druids taught, judged and kept: the old
# writers' lines on sacrifice and the like are left out on purpose. Do not add them.
#
# features.py adds STORY to the long reads; build.py merges REFS into the reading lists; cites.py adds CITES.
#
# Sources opened and read (November 2026), with the translations quoted:
#   Caesar, Gallic War VI.13-14, VI.18, I.29, tr. W. A. McDevitte and W. S. Bohn (Harper, 1869), at Perseus/Perseids:
#     "This institution is supposed to have been devised in Britain, and to have been brought over from it into Gaul";
#     "those who desire to gain a more accurate knowledge of that system generally proceed thither";
#     "many embrace this profession of their own accord, and [many] are sent to it by their parents and relations";
#     "They are said there to learn by heart a great number of verses"; "some remain in the course of training twenty years";
#     "in almost all other matters, in their public and private transactions, they use Greek characters";
#     the second reason for not writing: so the students do not "devote themselves the less to the efforts of memory, relying
#     on writing"; "that souls do not become extinct, but pass after death from one body to another"; "respecting the stars
#     and their motion, respecting the extent of the world and of our earth"; "Over all these Druids one presides, who
#     possesses supreme authority among them"; assembly "at a fixed period of the year in a consecrated place in the
#     territories of the Carnutes"; disputes "about an inheritance, if any about boundaries"; "The Druids do not go to war,
#     nor pay tribute together with the rest"; VI.18 "they compute the divisions of every season, not by the number of days,
#     but of nights"; I.29 "In the camp of the Helvetii, lists were found, drawn up in Greek characters" (368,000 people).
#   Strabo, Geography IV.4.4 and IV.1.5 (Loeb, tr. H. L. Jones, 1923), LacusCurtius: "the Bards, the Vates and the Druids";
#     "the Druids, in addition to natural philosophy, study also moral philosophy"; "The Druids are considered the most just
#     of men"; "they even arbitrated cases of war and made the opponents stop when they were about to line up for battle";
#     "men's souls, and also the universe, are indestructible"; Massilia "schooling the Galatae to be fond enough of the
#     Greeks to write even their contracts in Greek".
#   Diodorus Siculus V.28, V.31 (Loeb, tr. C. H. Oldfather, 1939), LacusCurtius: bards "sing to the accompaniment of
#     instruments which are like lyres"; philosophers and theologians "unusually honoured among them and are called by them
#     Druids"; "these men step forth between them and cause them to cease"; "passion give place before wisdom"; "the belief
#     of Pythagoras prevails among them, that the souls of men are immortal".
#   Pomponius Mela III.2, as given in Barddas, ed. J. Williams ab Ithel (1862): "masters of wisdom"; "the magnitude and form
#     of the earth and the world"; "the motions of the heaven and the stars"; "teach the most noble of the nation many things
#     privately"; "even for twenty years"; "in a cave, or in inaccessible woods"; "that souls are immortal".
#   Pliny, Natural History XVI.95, tr. J. Bostock and H. T. Riley (1855): "Clad in a white robe the priest ascends the tree,
#     and cuts the mistletoe with a golden sickle"; "a name which signifies, in their language, the all-healing".
#   Lucan, Pharsalia I, tr. Sir Edward Ridley (1896): "To you alone 'tis given the gods and stars / To know"; "the breath of
#     life / Still rules these bodies in another age"; "Happy the peoples 'neath the Northern Star".
#   Cicero, On Divination I.90 (Loeb, tr. W. A. Falconer, 1923), LacusCurtius: "Divitiacus, the Aeduan, your guest and
#     eulogist" (Quintus speaking to his brother Marcus), who knew the science of nature the Greeks call physiologia.
#   Diogenes Laertius, Lives of the Philosophers, prologue (Loeb, R. D. Hicks, 1925), Perseids: "There are some who say that
#     the study of philosophy had its beginning among the barbarians"; Druids "uttered their philosophy in riddles, bidding men
#     to reverence the gods ... to abstain from wrongdoing, and to practise courage".
#   Ammianus Marcellinus XV.9.8 (Loeb, tr. J. C. Rolfe), Perseids: bards "sang to the sweet strains of the lyre the valorous
#     deeds of famous men"; Euhages "attempted to explain the secret laws of nature"; Druids "loftier than the rest in
#     intellect", "pronounced the soul immortal".
#   Tacitus, Annals XIV.29-30 (Loeb, tr. J. Jackson, 1937; and Church and Brodribb, 1876): Môn "a haven for refugees", the
#     flat-bottomed boats, the women in black with torches, the Druids "lifting their hands to heaven", the soldiers frozen.
#   Armes Prydein (Book of Taliesin, about 930), Welsh text at ancienttexts.org: "Dysgogan derwydon meint a deruyd."
#   Dictionary of Welsh Biography, ROWLANDS, HENRY (1655-1723): Mona Antiqua Restaurata, Dublin 1723, tries to prove
#     Anglesey "the chief seat of the druids".
#   Coligny calendar (Wikipedia): found 1897 at Coligny, Ain; bronze, second century AD; five years of lunar months, 62 in all,
#     set to the sun; Gaulish in Latin letters; Gallo-Roman Museum, Lyon.

STORY = dict(id="druids", era="ancient", art="dolmen", mins=12,
  people=["buddug", "iolo-morganwg", "cynan"],
  places=["cerrigbach"],
  events=["The druids of Môn", "Rome attacks Ynys Môn", "Caesar writes of the Druids of Britain"],
  links=[("place-cerrigbach.html", "Llyn Cerrig Bach", "Llyn Cerrig Bach"),
         ("documents.html#doc-caesar", "Caesar on the Druids, in his own words", "Cesar ar y Derwyddon, yn ei eiriau ei hun"),
         ("battles.html#b-mon60", "The stand on the shore of Môn, AD 60", "Y safiad ar lan Môn, 60 OC"),
         ("story-learning.html", "The oldest schools in Britain", "Ysgolion hynaf Prydain"),
         ("story-iolo.html", "Iolo Morganwg and the Gorsedd of the Bards", "Iolo Morganwg a Gorsedd y Beirdd"),
         ("story-celts.html", "Britons, not Celts", "Brythoniaid, nid Celtiaid"),
         ("laws.html", "The Laws of Hywel Dda", "Cyfraith Hywel Dda")],
  en="The Druids: when Europe came to Britain to learn",
  cy="Y Derwyddon: pan ddaeth Ewrop i Brydain i ddysgu",
  sumEn="Julius Caesar wrote that the learning of the Druids began in Britain, and that students crossed the sea to master it here. They were the teachers, judges, philosophers and keepers of memory of the Britons; they trained for up to twenty years, and they wrote their business in Greek letters.",
  sumCy="Ysgrifennodd Iŵl Cesar mai ym Mhrydain y dechreuodd dysg y Derwyddon, a bod myfyrwyr yn croesi’r môr i’w meistroli yma. Hwy oedd athrawon, barnwyr, athronwyr a cheidwaid cof y Brythoniaid; buont yn hyfforddi am hyd at ugain mlynedd, ac ysgrifennent eu busnes mewn llythrennau Groeg.",
  pEn=[
   "Two thousand years ago, long before Oxford or Paris, there was a place in Europe where the young went to finish their learning. It was this island. The man who tells us so was no friend of the Britons: he was Julius Caesar, who came here with his legions in 55 and 54 BC. In his book on the war in Gaul he wrote that the teaching of the Druids was believed to have begun in Britain, and that those who wished to know it best still crossed the sea to learn it here.[[cite:dr-caesar]]",
   "The Druids, the derwyddon, were the learned men of the Britons and of their cousins across the Channel in Gaul. They were the teachers, the judges, the philosophers, the astronomers and the keepers of memory. This is what the old writers of Greece and Rome said of them, in their own words.",
   "|| In Welsh | Derwydd, plural derwyddon",
   "|| What they were | Teachers, judges, philosophers, healers and keepers of memory",
   "|| Where their learning began | In Britain, in Caesar’s own words",
   "|| Who came to learn | Students from Gaul, a land that stretched from the Rhine to the Pyrenees",
   "|| How long they studied | Up to twenty years, all of it by heart",
   "|| How they wrote | In Greek letters, Caesar says, for public and private business",
   "|| What they taught | The stars and their motion, the size of the earth, the nature of things, and that the soul does not die",
   "|| Their great centre in Wales | Ynys Môn",
   "|| Their heirs | The bards of Wales, and the Gorsedd of the Bards today",
   "!! druid-teaching",
   "## The school of Europe",
   "Caesar wrote about the Druids in about 52 BC, in the sixth book of his Gallic War. He had spent years among the peoples of Gaul, the great land that is now France, Belgium, Switzerland and the Rhineland, and he had twice crossed to Britain. What he heard about the Druids, he wrote down plainly:",
   "> This institution is supposed to have been devised in Britain, and to have been brought over from it into Gaul; and now those who desire to gain a more accurate knowledge of that system generally proceed thither for the purpose of studying it. | Julius Caesar, The Gallic War, VI.13, translated by W. A. McDevitte and W. S. Bohn",
   "So the learning that guided all of Gaul had its home here. When a young man of Gaul wanted to go deeper than his own teachers could take him, he took ship for Britain. Caesar adds that the young came to the Druids gladly: ‘many embrace this profession of their own accord, and many are sent to it by their parents and relations’.[[cite:dr-caesar]]",
   "It is the oldest written witness to a truth that runs right through the story of Wales. In the age of the saints, students from Ireland and Brittany came to Illtud at Llanilltud Fawr and to Cadog at Llancarfan. Two thousand years ago they were already coming to the Druids.",
   "## Twenty years of learning",
   "A Druid’s training was long. Caesar says some stayed at it for twenty years, and that they ‘learn by heart a great number of verses’. The Roman geographer Pomponius Mela, writing about AD 43, says the same: the Druids taught ‘the most noble of the nation many things privately’, ‘even for twenty years’, in a cave or deep in the woods.[[cite:dr-caesar,dr-mela]]",
   "Why learn it all by heart? Caesar gives two reasons. The first was to keep their teaching for those who had earned it. The second shows real wisdom about how people learn: they did not want their students to rely on writing, and so ‘devote themselves the less to the efforts of memory’. A Druid carried a whole library in his head.[[cite:dr-caesar]]",
   "Wales kept that gift. The poets of the princes learned their craft from a master over many years, by word of mouth, and could carry long poems and the pedigrees of every great family in their heads. To this day the strict metres of cynghanedd are learned by ear as much as from the page.",
   "## They wrote in Greek letters",
   "None of this means the Druids could not write. Caesar is clear that they could. They would not commit their sacred teaching to writing, he says, ‘though in almost all other matters, in their public and private transactions, they use Greek characters’.[[cite:dr-caesar]]",
   "> In almost all other matters, in their public and private transactions, they use Greek characters. | Julius Caesar, The Gallic War, VI.14, translated by W. A. McDevitte and W. S. Bohn",
   "In other words, the learned men of Gaul and Britain kept their accounts and their records in the alphabet of Homer and Plato, the alphabet of the most learned people of the ancient world. Caesar saw the proof himself. After his first great battle in Gaul, lists were found in the camp of the Helvetii, ‘drawn up in Greek characters’, counting every man, woman and child of the people: 368,000 in all.[[cite:dr-caesar-1]]",
   "The Greek geographer Strabo explains where the letters came from. The Greek city of Massalia, now Marseille, had become a school for the peoples of Gaul, who grew so fond of the Greeks that they wrote ‘even their contracts in Greek’. Stones carved with Gaulish words in Greek letters are still found in the south of France.[[cite:dr-strabo-massalia]]",
   "Britain’s kings wrote too. Before the Romans came, Cunobelinus, the Cynfelyn of Welsh tradition, and other kings of the Britons struck gold coins with their names spelled out in letters. The Britons were a lettered people, and the Druids were the most lettered of all.",
   "## Teachers of the stars and of the soul",
   "What did they teach in those twenty years? Caesar gives the list: ‘the stars and their motion’, ‘the extent of the world and of our earth’, ‘the nature of things’, and the power of the gods. Mela calls them ‘masters of wisdom’, who claimed to know ‘the magnitude and form of the earth and the world’ and ‘the motions of the heaven and the stars’.[[cite:dr-caesar,dr-mela]]",
   "They kept time by the moon and the stars. Caesar noticed that they counted time ‘not by the number of days, but of nights’. Welsh still does. A week is wythnos, ‘eight nights’, and a fortnight is pythefnos, ‘fifteen nights’, and English kept the same habit in its own word fortnight, ‘fourteen nights’.[[cite:dr-caesar-18]]",
   "A great bronze calendar found at Coligny in France in 1897, made in the second century AD, shows the kind of reckoning the learned men of Gaul could keep: five years of months set by the moon, sixty-two months in all, fitted to the year of the sun, with the lucky and unlucky days marked. It is written in the Gaulish language.[[cite:dr-coligny]]",
   "Above all, they taught that the soul does not die. Caesar wrote that the Druids taught ‘that souls do not become extinct, but pass after death from one body to another’, and that this was the greatest spur to courage, since it took away the fear of death. Diodorus of Sicily, Strabo, Mela and Ammianus all say the same. The Roman poet Lucan, writing in the time of Nero, addressed the Druids directly:[[cite:dr-caesar,dr-diodorus,dr-strabo]]",
   "> To you alone ’tis given the gods and stars / To know or not to know … the breath of life / Still rules these bodies in another age. … Happy the peoples ’neath the Northern Star. | Lucan, Pharsalia, book I, translated by Sir Edward Ridley",
   "## Philosophers the Greeks admired",
   "The Greeks, who thought of themselves as the inventors of philosophy, counted the Druids among the first philosophers of the world. Diogenes Laertius, who wrote the lives of the Greek thinkers, begins his book by noting that some held philosophy to have begun among the peoples beyond Greece, with the Magi of Persia, the wise men of India, and the Druids. He gives their teaching in three short rules, like a Welsh triad:[[cite:dr-diogenes]]",
   "> To reverence the gods, to abstain from wrongdoing, and to practise courage. | The teaching of the Druids, from Diogenes Laertius, Lives of the Philosophers, prologue, translated by R. D. Hicks",
   "Diodorus of Sicily calls them ‘philosophers and theologians’ who were ‘unusually honoured’, and says the teaching of Pythagoras, that the souls of men are immortal, held among them. Strabo says that ‘in addition to natural philosophy’, the study of the world, they ‘study also moral philosophy’, the study of right and wrong. Ammianus Marcellinus wrote that the Druids were ‘loftier than the rest in intellect’ and lived in close fellowship, as Pythagoras had taught.[[cite:dr-diodorus,dr-strabo,dr-ammianus]]",
   "One Druid was a friend of Rome’s greatest orator. Diviciacus of the Aedui, a people of Gaul, came to Rome to speak before the Senate for his people, and stayed as the guest of Marcus Tullius Cicero. In Cicero’s book On Divination, his brother Quintus remembers ‘Divitiacus, the Aeduan, your guest and eulogist’, who knew the science of nature that the Greeks call physiologia and could read what was to come.[[cite:dr-cicero]]",
   "!! druid-caesar",
   "## Judges and peacemakers",
   "The Druids were the judges of their people. Caesar says they decided nearly every dispute, public and private: a wrong done, a quarrel ‘about an inheritance’ or ‘about boundaries’. Each year they met at a holy place in the land of the Carnutes, at the very centre of Gaul, and people came from every part to have their cases heard. Strabo says simply: ‘The Druids are considered the most just of men.’[[cite:dr-caesar,dr-strabo]]",
   "They were bound together in one order, with one head. ‘Over all these Druids one presides, who possesses supreme authority among them,’ Caesar writes; when he died, the most worthy took his place. The Druids were free of war service and of taxes, so that they could give their lives to learning.[[cite:dr-caesar]]",
   "Most remarkable of all, they were peacemakers. Strabo says they ‘made the opponents stop when they were about to line up for battle’. Diodorus paints the scene: two armies drawn up, swords out, spears levelled, and the Druids stepping out between them, so that the fighting stopped. ‘In this way,’ he writes, ‘does passion give place before wisdom.’[[cite:dr-strabo,dr-diodorus]]",
   "!! druid-arch-judge",
   "Wales kept its learned judges too. A thousand years later the Laws of Hywel Dda were kept by trained judges, the ynaid, who had to prove their knowledge of the law before they could judge, and Welsh law was famous for setting a wrong right by payment and agreement.",
   "## The three orders",
   "The old writers knew that the learned men of the Britons and Gauls came in three orders. Strabo names them: ‘the Bards, the Vates and the Druids’. Diodorus says the bards sang ‘to the accompaniment of instruments which are like lyres’. Ammianus, drawing on the Greek writer Timagenes, describes all three: the bards ‘sang to the sweet strains of the lyre the valorous deeds of famous men’, the vates ‘attempted to explain the secret laws of nature’, and the Druids, highest of all, taught that the soul is immortal.[[cite:dr-strabo,dr-diodorus,dr-ammianus]]",
   "The poet who sang the praise of heroes to the harp; the seer who studied nature; the Druid who taught and judged. Anyone who knows Wales knows those three. They are the beirdd, the ofyddion and the derwyddon of the Gorsedd of the Bards of the Island of Britain.",
   "!! druid-mistletoe",
   "Pliny the Elder, the great Roman naturalist, describes the Druids as healers who knew the plants of the woods. Nothing was more sacred to them, he says, than the oak and the mistletoe that grows on it. On the appointed day of the moon a Druid ‘clad in a white robe’ climbed the oak and cut the mistletoe ‘with a golden sickle’. They called it by a name that meant ‘the all-healing’. Pliny thought the name of the Druids itself came from the oak, and the Welsh word agrees: derwydd, from derw, oak, and the old root of gwybod, to know.[[cite:dr-pliny]]",
   "## Môn, the island of the Druids",
   "In Britain, the heart of it all was Ynys Môn. The Roman historian Tacitus calls Môn an island with ‘a considerable population of its own’ and a haven for all who would not bow to Rome. In AD 60 the governor Suetonius Paulinus decided that while Môn stood, Britain would never be his. He built flat-bottomed boats for his foot soldiers, and sent his cavalry to swim the Menai Strait beside their horses.[[cite:dr-tacitus]]",
   "The Britons of Môn were waiting for them on the shore. Tacitus tells what the Romans saw: the warriors drawn up in their ranks, the women running between them in black robes with torches blazing, and all around them the Druids, ‘lifting their hands to heaven’ and calling on the gods to defend their island. The sight was so strange and so terrible that the legions stood still, as if their limbs were frozen.[[cite:dr-tacitus,dr-tacitus-cb]]",
   "Rome crossed in the end, and cut down the sacred groves. But Môn had held up the whole Roman army at the very moment that mattered. While Paulinus was on the island, Boudica, queen of the Iceni, rose in the east, and he had to march away at once to face her. Môn was not taken for good until about AD 78.[[cite:dr-tacitus]]",
   "!! druid-cerrigbach-lake",
   "Môn’s fame reached far. In 1942, while peat was being cleared to lengthen a runway at RAF Valley, the bed of a small lake called Llyn Cerrig Bach gave up more than 150 pieces of Iron Age metalwork: swords, spears, shields, a bronze trumpet, chariot fittings, cauldrons and fine bronze plaques, laid in the water as offerings over some four hundred years, from about 300 BC to AD 100. Some came from far across Britain and from Ireland. The archaeologist Sir Cyril Fox saw in them the gifts of the island of the Druids. They are in National Museum Cardiff today.[[cite:pl-wiki-cerrigbach]]",
   "## The Druids in Welsh memory",
   "Rome could cut down the groves, but it could not cut the memory. The Welsh word derwydd lived on in the poetry of Wales for a thousand years, meaning a sage and a seer. The great poem Armes Prydein, the Prophecy of Britain, made in about 930 and kept in the Book of Taliesin, opens its vision of the Cymry rising again with the line Dysgogan derwydon meint a deruyd: ‘The Druids foretell all that will come to pass.’[[cite:dr-armes]]",
   "> Dysgogan derwydon meint a deruyd. | Armes Prydein, the Book of Taliesin, about 930",
   "!! druid-chief-mona",
   "In 1723 Henry Rowlands, vicar of Llanidan in Môn, published Mona Antiqua Restaurata, Ancient Môn Restored, a book on the antiquities of his island that set out to show that Môn had been the chief seat of the Druids of Britain. Its picture of ‘The Chief Druid’, with his staff and his oak branch, was copied all over Europe.[[cite:dr-rowlands]]",
   "Seventy years later Iolo Morganwg gathered the poets of Wales on Primrose Hill in London, on 21 June 1792, and founded the Gorsedd of the Bards of the Island of Britain, with its three orders of Druids, Bards and Ovates: the same three orders Strabo had named eighteen hundred years before. Since 1819 the Gorsedd has been part of the Eisteddfod, and at its head stands the Archdruid, as Caesar said one Druid presided over all.",
   "!! druid-cynan-1952",
   "Every August, at the National Eisteddfod, the Archdruid stands at the maen llog in the circle of stones and asks three times, A oes heddwch? Is there peace? Two thousand years ago the Druids walked out between two armies and made peace. Students crossed the sea to learn from them, and the soul, they taught, does not die. In Wales, their memory has not died either.",
  ],
  pCy=[
   "Ddwy fil o flynyddoedd yn ôl, ymhell cyn bod Rhydychen na Pharis, roedd lle yn Ewrop lle’r âi’r ifanc i gwblhau eu dysg. Yr ynys hon oedd y lle hwnnw. Nid cyfaill i’r Brythoniaid yw’r gŵr sy’n dweud hynny wrthym: Iŵl Cesar ydoedd, a ddaeth yma gyda’i lengoedd yn 55 a 54 CC. Yn ei lyfr ar y rhyfel yng Ngâl ysgrifennodd y credid mai ym Mhrydain y dechreuodd dysgeidiaeth y Derwyddon, a bod y rhai a fynnai ei hadnabod orau yn dal i groesi’r môr i’w dysgu yma.[[cite:dr-caesar]]",
   "Y Derwyddon oedd gwŷr dysgedig y Brythoniaid a’u cefndryd dros y môr yng Ngâl. Hwy oedd yr athrawon, y barnwyr, yr athronwyr, y seryddwyr a cheidwaid y cof. Dyma a ddywedodd hen awduron Groeg a Rhufain amdanynt, yn eu geiriau eu hunain.",
   "|| Yn Gymraeg | Derwydd, lluosog derwyddon",
   "|| Beth oeddynt | Athrawon, barnwyr, athronwyr, iachawyr a cheidwaid y cof",
   "|| Ble dechreuodd eu dysg | Ym Mhrydain, yng ngeiriau Cesar ei hun",
   "|| Pwy a ddaeth i ddysgu | Myfyrwyr o Âl, gwlad a ymestynnai o afon Rhein i’r Pyreneau",
   "|| Am faint y buont yn astudio | Hyd at ugain mlynedd, y cyfan ar gof",
   "|| Sut yr ysgrifennent | Mewn llythrennau Groeg, medd Cesar, ar gyfer busnes cyhoeddus a phreifat",
   "|| Beth a ddysgent | Y sêr a’u symudiad, maint y ddaear, natur pethau, ac nad yw’r enaid yn marw",
   "|| Eu canolfan fawr yng Nghymru | Ynys Môn",
   "|| Eu hetifeddion | Beirdd Cymru, a Gorsedd y Beirdd heddiw",
   "!! druid-teaching",
   "## Ysgol Ewrop",
   "Ysgrifennodd Cesar am y Derwyddon tua 52 CC, yn chweched llyfr ei Ryfel Gâl. Roedd wedi treulio blynyddoedd ymhlith pobloedd Gâl, y wlad fawr sydd heddiw’n Ffrainc, Gwlad Belg, y Swistir a’r Rheinland, ac roedd wedi croesi i Brydain ddwywaith. Yr hyn a glywodd am y Derwyddon, fe’i hysgrifennodd yn blaen:",
   "> Credir i’r drefn hon gael ei dyfeisio ym Mhrydain, a’i dwyn oddi yno i Âl; a heddiw mae’r rhai sy’n dymuno gwybodaeth fanylach o’r drefn honno fel arfer yn mynd yno i’w hastudio. | Iŵl Cesar, Rhyfel Gâl, VI.13, o gyfieithiad Saesneg W. A. McDevitte a W. S. Bohn",
   "Felly yma yr oedd cartref y ddysg a dywysai Âl gyfan. Pan fynnai gŵr ifanc o Âl fynd yn ddyfnach nag y gallai ei athrawon ei hun ei arwain, âi ar long i Brydain. Ychwanega Cesar fod yr ifanc yn dod at y Derwyddon yn llawen: ‘mae llawer yn cofleidio’r alwedigaeth hon o’u gwirfodd, a llawer yn cael eu hanfon ati gan eu rhieni a’u perthnasau’.[[cite:dr-caesar]]",
   "Dyma’r tyst ysgrifenedig hynaf i wirionedd sy’n rhedeg drwy holl stori Cymru. Yn oes y saint, daeth myfyrwyr o Iwerddon a Llydaw at Illtud yn Llanilltud Fawr ac at Gadog yn Llancarfan. Ddwy fil o flynyddoedd yn ôl roeddynt eisoes yn dod at y Derwyddon.",
   "## Ugain mlynedd o ddysg",
   "Roedd hyfforddiant Derwydd yn hir. Medd Cesar fod rhai wrthi am ugain mlynedd, a’u bod yn ‘dysgu ar gof nifer fawr o benillion’. Mae’r daearyddwr Rhufeinig Pomponius Mela, yn ysgrifennu tua 43 OC, yn dweud yr un peth: dysgai’r Derwyddon ‘lawer o bethau’n breifat i bendefigion y genedl’, ‘hyd yn oed am ugain mlynedd’, mewn ogof neu ym mherfeddion y coed.[[cite:dr-caesar,dr-mela]]",
   "Pam dysgu’r cyfan ar gof? Mae Cesar yn rhoi dau reswm. Y cyntaf oedd cadw eu dysgeidiaeth i’r rhai a’i haeddai. Mae’r ail yn dangos gwir ddoethineb am y ffordd y mae pobl yn dysgu: nid oeddynt am i’w disgyblion bwyso ar ysgrifen, ac felly ‘ymroi’n llai i ymdrechion y cof’. Cariai Derwydd lyfrgell gyfan yn ei ben.[[cite:dr-caesar]]",
   "Cadwodd Cymru’r ddawn honno. Dysgai beirdd y tywysogion eu crefft gan athro dros flynyddoedd lawer, ar lafar, a gallent gario cerddi hir ac achau pob teulu mawr yn eu pennau. Hyd heddiw dysgir mesurau caeth y gynghanedd drwy’r glust gymaint â thrwy’r dudalen.",
   "## Ysgrifennent mewn llythrennau Groeg",
   "Nid yw hyn oll yn golygu na allai’r Derwyddon ysgrifennu. Mae Cesar yn eglur y gallent. Ni fynnent roi eu dysgeidiaeth gysegredig ar glawr, meddai, ‘er eu bod ym mron pob mater arall, yn eu trafodion cyhoeddus a phreifat, yn defnyddio llythrennau Groeg’.[[cite:dr-caesar]]",
   "> Ym mron pob mater arall, yn eu trafodion cyhoeddus a phreifat, defnyddiant lythrennau Groeg. | Iŵl Cesar, Rhyfel Gâl, VI.14, o gyfieithiad Saesneg W. A. McDevitte a W. S. Bohn",
   "Hynny yw, cadwai gwŷr dysgedig Gâl a Phrydain eu cyfrifon a’u cofnodion yng ngwyddor Homer a Phlaton, gwyddor pobl fwyaf dysgedig yr hen fyd. Gwelodd Cesar y prawf ei hun. Ar ôl ei frwydr fawr gyntaf yng Ngâl, cafwyd rhestrau yng ngwersyll yr Helvetii, ‘wedi’u llunio mewn llythrennau Groeg’, yn cyfrif pob gŵr, gwraig a phlentyn o’r bobl: 368,000 i gyd.[[cite:dr-caesar-1]]",
   "Mae’r daearyddwr Groeg Strabo yn egluro o ble y daeth y llythrennau. Roedd dinas Roeg Massalia, Marseille heddiw, wedi dod yn ysgol i bobloedd Gâl, a aeth mor hoff o’r Groegiaid nes ysgrifennu ‘hyd yn oed eu cytundebau mewn Groeg’. Mae cerrig â geiriau Galeg wedi’u cerfio mewn llythrennau Groeg i’w cael o hyd yn ne Ffrainc.[[cite:dr-strabo-massalia]]",
   "Ysgrifennai brenhinoedd Prydain hefyd. Cyn i’r Rhufeiniaid ddod, trawodd Cunobelinus, Cynfelyn traddodiad Cymru, a brenhinoedd eraill y Brythoniaid ddarnau arian aur â’u henwau wedi’u sillafu mewn llythrennau. Pobl lythrennog oedd y Brythoniaid, a’r Derwyddon oedd y mwyaf llythrennog oll.",
   "## Athrawon y sêr a’r enaid",
   "Beth a ddysgent yn yr ugain mlynedd hynny? Mae Cesar yn rhoi’r rhestr: ‘y sêr a’u symudiad’, ‘maint y byd a’n daear ni’, ‘natur pethau’, a nerth y duwiau. Geilw Mela hwy yn ‘feistri doethineb’, a honnent wybod ‘maint a ffurf y ddaear a’r byd’ a ‘symudiadau’r nef a’r sêr’.[[cite:dr-caesar,dr-mela]]",
   "Cadwent amser wrth y lleuad a’r sêr. Sylwodd Cesar eu bod yn cyfrif amser ‘nid wrth nifer y dyddiau, ond y nosweithiau’. Felly y mae’r Gymraeg o hyd. Wyth nos yw wythnos, a phymtheg nos yw pythefnos, a chadwodd y Saesneg yr un arfer yn ei gair fortnight, ‘pedair noson ar ddeg’.[[cite:dr-caesar-18]]",
   "Mae calendr efydd mawr a gafwyd yn Coligny yn Ffrainc yn 1897, a wnaed yn yr ail ganrif OC, yn dangos y math o gyfrif y gallai gwŷr dysgedig Gâl ei gadw: pum mlynedd o fisoedd wedi’u gosod wrth y lleuad, dau fis a thrigain i gyd, wedi’u cysoni â blwyddyn yr haul, a’r dyddiau lwcus ac anlwcus wedi’u nodi. Mae wedi’i ysgrifennu mewn Galeg, iaith Gâl.[[cite:dr-coligny]]",
   "Yn anad dim, dysgent nad yw’r enaid yn marw. Ysgrifennodd Cesar fod y Derwyddon yn dysgu ‘nad yw eneidiau’n darfod, ond yn mynd ar ôl marwolaeth o un corff i’r llall’, ac mai dyma’r symbyliad mwyaf i ddewrder, gan ei fod yn dileu ofn angau. Mae Diodorus o Sisili, Strabo, Mela ac Ammianus i gyd yn dweud yr un peth. Cyfarchodd y bardd Rhufeinig Lucan, yn ysgrifennu yn amser Nero, y Derwyddon yn uniongyrchol:[[cite:dr-caesar,dr-diodorus,dr-strabo]]",
   "> I chwi yn unig y rhoddwyd adnabod y duwiau a’r sêr … mae anadl einioes yn dal i lywodraethu’r cyrff hyn mewn oes arall. … Gwyn eu byd y pobloedd dan Seren y Gogledd. | Lucan, Pharsalia, llyfr I, o gyfieithiad Saesneg Syr Edward Ridley",
   "## Athronwyr a edmygai’r Groegiaid",
   "Cyfrifai’r Groegiaid, a ystyriai eu hunain yn ddyfeiswyr athroniaeth, y Derwyddon ymhlith athronwyr cyntaf y byd. Mae Diogenes Laertius, a ysgrifennodd fucheddau meddylwyr Groeg, yn agor ei lyfr drwy nodi bod rhai’n credu i athroniaeth ddechrau ymhlith y pobloedd y tu hwnt i Roeg, gyda Magi Persia, doethion India, a’r Derwyddon. Mae’n rhoi eu dysgeidiaeth mewn tair rheol fer, fel triawd Cymraeg:[[cite:dr-diogenes]]",
   "> Parchu’r duwiau, ymgadw rhag gwneud drwg, ac arfer dewrder. | Dysgeidiaeth y Derwyddon, o Diogenes Laertius, Bucheddau’r Athronwyr, y rhagair, o gyfieithiad Saesneg R. D. Hicks",
   "Geilw Diodorus o Sisili hwy’n ‘athronwyr a diwinyddion’ a gâi ‘barch anghyffredin’, a dywed fod dysgeidiaeth Pythagoras, fod eneidiau dynion yn anfarwol, yn ffynnu yn eu plith. Medd Strabo eu bod ‘yn ogystal ag athroniaeth natur’, astudio’r byd, ‘yn astudio hefyd athroniaeth foesol’, astudio da a drwg. Ysgrifennodd Ammianus Marcellinus fod y Derwyddon ‘yn uwch na’r lleill o ran deall’ a’u bod yn byw mewn cymdeithas glos, fel y dysgasai Pythagoras.[[cite:dr-diodorus,dr-strabo,dr-ammianus]]",
   "Roedd un Derwydd yn gyfaill i areithiwr mwyaf Rhufain. Daeth Diviciacus o’r Aedui, un o bobloedd Gâl, i Rufain i siarad gerbron y Senedd dros ei bobl, ac arhosodd yn westai i Farcus Tullius Cicero. Yn llyfr Cicero Ar Ddewiniaeth, mae ei frawd Quintus yn cofio ‘Divitiacus, yr Aeduad, dy westai a’th folwr’, a adwaenai wyddor natur a eilw’r Groegiaid yn physiologia ac a allai ddarllen yr hyn oedd i ddod.[[cite:dr-cicero]]",
   "!! druid-caesar",
   "## Barnwyr a thangnefeddwyr",
   "Y Derwyddon oedd barnwyr eu pobl. Medd Cesar eu bod yn penderfynu bron pob anghydfod, cyhoeddus a phreifat: cam a wnaed, cweryl ‘am etifeddiaeth’ neu ‘am derfynau’. Bob blwyddyn cyfarfyddent mewn lle sanctaidd yng ngwlad y Carnutes, yng nghanol Gâl, a deuai pobl o bob parth i gael gwrando eu hachosion. Medd Strabo yn syml: ‘Ystyrir y Derwyddon y cyfiawnaf o ddynion.’[[cite:dr-caesar,dr-strabo]]",
   "Roeddynt wedi’u rhwymo ynghyd mewn un urdd, ag un pen. ‘Dros yr holl Dderwyddon hyn mae un yn llywyddu, a chanddo’r awdurdod goruchaf yn eu plith,’ medd Cesar; pan fu farw, cymerai’r teilyngaf ei le. Roedd y Derwyddon yn rhydd o wasanaeth rhyfel a threthi, er mwyn iddynt roi eu bywyd i ddysg.[[cite:dr-caesar]]",
   "Yn fwy rhyfeddol na’r cyfan, tangnefeddwyr oeddynt. Medd Strabo iddynt ‘atal y gwrthwynebwyr pan oeddynt ar fin ymffurfio i frwydr’. Mae Diodorus yn peintio’r olygfa: dwy fyddin yn eu rhengoedd, cleddyfau wedi’u tynnu, gwaywffyn yn barod, a’r Derwyddon yn camu allan rhyngddynt, nes i’r ymladd beidio. ‘Fel hyn,’ meddai, ‘mae nwyd yn ildio i ddoethineb.’[[cite:dr-strabo,dr-diodorus]]",
   "!! druid-arch-judge",
   "Cadwodd Cymru ei barnwyr dysgedig hefyd. Fil o flynyddoedd yn ddiweddarach cedwid Cyfraith Hywel Dda gan farnwyr hyfforddedig, yr ynaid, a oedd yn gorfod profi eu gwybodaeth o’r gyfraith cyn cael barnu, ac roedd cyfraith Cymru yn enwog am unioni cam drwy dâl a chytundeb.",
   "## Y tair urdd",
   "Gwyddai’r hen awduron fod gwŷr dysgedig y Brythoniaid a’r Galiaid mewn tair urdd. Mae Strabo yn eu henwi: ‘y Beirdd, y Vates a’r Derwyddon’. Medd Diodorus fod y beirdd yn canu ‘i gyfeiliant offerynnau tebyg i delynau’. Mae Ammianus, gan dynnu ar yr awdur Groeg Timagenes, yn disgrifio’r tair: canai’r beirdd ‘i seiniau melys y delyn gampau dewr gwŷr enwog’, ceisiai’r vates ‘egluro deddfau cudd natur’, a dysgai’r Derwyddon, yr uchaf oll, fod yr enaid yn anfarwol.[[cite:dr-strabo,dr-diodorus,dr-ammianus]]",
   "Y bardd a ganai glod arwyr i’r delyn; y gweledydd a astudiai natur; y Derwydd a ddysgai ac a farnai. Mae pawb sy’n adnabod Cymru yn adnabod y tri hynny. Hwy yw beirdd, ofyddion a derwyddon Gorsedd Beirdd Ynys Prydain.",
   "!! druid-mistletoe",
   "Mae Pliny yr Hynaf, naturiaethwr mawr Rhufain, yn disgrifio’r Derwyddon fel iachawyr a adwaenai blanhigion y coed. Nid oedd dim yn fwy cysegredig iddynt, meddai, na’r dderwen a’r uchelwydd sy’n tyfu arni. Ar ddydd penodedig y lleuad dringai Derwydd ‘mewn gwisg wen’ y dderwen a thorri’r uchelwydd ‘â chryman aur’. Galwent hi wrth enw a olygai ‘yr holliachâd’. Credai Pliny fod enw’r Derwyddon ei hun yn dod o’r dderwen, ac mae’r gair Cymraeg yn cytuno: derwydd, o’r gair derw a hen wreiddyn y gair gwybod.[[cite:dr-pliny]]",
   "## Môn, ynys y Derwyddon",
   "Ym Mhrydain, Ynys Môn oedd calon y cyfan. Geilw’r hanesydd Rhufeinig Tacitus Fôn yn ynys ‘â phoblogaeth sylweddol ei hun’ ac yn hafan i bawb na phlygai i Rufain. Yn 60 OC penderfynodd y llywodraethwr Suetonius Paulinus na fyddai Prydain byth yn eiddo iddo tra safai Môn. Adeiladodd gychod gwaelod gwastad i’w filwyr traed, ac anfonodd ei farchogion i nofio’r Fenai wrth ochr eu meirch.[[cite:dr-tacitus]]",
   "Roedd Brythoniaid Môn yn eu disgwyl ar y lan. Mae Tacitus yn adrodd yr hyn a welodd y Rhufeiniaid: y rhyfelwyr yn eu rhengoedd, y gwragedd yn rhedeg rhyngddynt mewn gwisgoedd duon â ffaglau ynghyn, ac o’u cwmpas y Derwyddon, ‘yn codi eu dwylo i’r nef’ ac yn galw ar y duwiau i amddiffyn eu hynys. Roedd yr olygfa mor ddieithr ac mor ofnadwy nes i’r llengoedd sefyll yn stond, fel petai eu haelodau wedi rhewi.[[cite:dr-tacitus,dr-tacitus-cb]]",
   "Croesodd Rhufain yn y diwedd, a thorri’r llwyni sanctaidd. Ond roedd Môn wedi dal holl fyddin Rhufain yn ôl ar yr union adeg a oedd yn cyfrif. Tra oedd Paulinus ar yr ynys, cododd Buddug, brenhines yr Iceni, yn y dwyrain, a bu raid iddo orymdeithio ymaith ar unwaith i’w hwynebu. Ni chymerwyd Môn am byth tan tua 78 OC.[[cite:dr-tacitus]]",
   "!! druid-cerrigbach-lake",
   "Cyrhaeddodd enw Môn ymhell. Yn 1942, wrth glirio mawn i estyn rhedfa yn RAF y Fali, rhoddodd gwely llyn bach o’r enw Llyn Cerrig Bach dros 150 o ddarnau o waith metel Oes yr Haearn: cleddyfau, gwaywffyn, tarianau, utgorn efydd, offer cerbydau rhyfel, crochanau a phlaciau efydd cain, a osodwyd yn y dŵr yn offrymau dros ryw bedwar can mlynedd, o tua 300 CC i 100 OC. Daeth rhai o bell ar draws Prydain ac o Iwerddon. Gwelodd yr archaeolegydd Syr Cyril Fox ynddynt roddion ynys y Derwyddon. Maent yn Amgueddfa Genedlaethol Caerdydd heddiw.[[cite:pl-wiki-cerrigbach]]",
   "## Y Derwyddon yng nghof Cymru",
   "Gallai Rhufain dorri’r llwyni, ond ni allai dorri’r cof. Bu’r gair derwydd fyw ym marddoniaeth Cymru am fil o flynyddoedd, yn golygu doeth a gweledydd. Mae’r gerdd fawr Armes Prydein, a luniwyd tua 930 ac a gadwyd yn Llyfr Taliesin, yn agor ei gweledigaeth o’r Cymry’n codi eto â’r llinell Dysgogan derwydon meint a deruyd: ‘Mae’r derwyddon yn darogan y cyfan a ddaw.’[[cite:dr-armes]]",
   "> Dysgogan derwydon meint a deruyd. | Armes Prydein, Llyfr Taliesin, tua 930",
   "!! druid-chief-mona",
   "Yn 1723 cyhoeddodd Henry Rowlands, ficer Llanidan ym Môn, Mona Antiqua Restaurata, Môn Hynafol wedi’i Hadfer, llyfr ar hynafiaethau ei ynys a geisiai ddangos mai Môn oedd prif sedd Derwyddon Prydain. Copïwyd ei lun o ‘The Chief Druid’, y Prif Dderwydd, gyda’i ffon a’i gangen dderw, ar draws Ewrop.[[cite:dr-rowlands]]",
   "Saith deg mlynedd yn ddiweddarach casglodd Iolo Morganwg feirdd Cymru ar Fryn y Briallu yn Llundain, ar 21 Mehefin 1792, a sefydlu Gorsedd Beirdd Ynys Prydain, gyda’i thair urdd o Dderwyddon, Beirdd ac Ofyddion: yr un tair urdd ag a enwodd Strabo ddeunaw can mlynedd ynghynt. Er 1819 bu’r Orsedd yn rhan o’r Eisteddfod, ac ar ei phen saif yr Archdderwydd, fel y dywedodd Cesar fod un Derwydd yn llywyddu dros y cyfan.",
   "!! druid-cynan-1952",
   "Bob mis Awst, yn yr Eisteddfod Genedlaethol, saif yr Archdderwydd wrth y maen llog yng nghylch y cerrig a gofyn deirgwaith, A oes heddwch? Ddwy fil o flynyddoedd yn ôl cerddai’r Derwyddon allan rhwng dwy fyddin a gwneud heddwch. Croesai myfyrwyr y môr i ddysgu ganddynt, ac nid yw’r enaid, meddent, yn marw. Yng Nghymru, nid yw eu cof wedi marw chwaith.",
  ],
)

# A timeline event for the Caesar witness (data.py adds EVENTS; the title matches events=[...] above).
EVENTS = [
 ("ancient", -52, 1, 0, "", "Caesar writes of the Druids of Britain", "Cesar yn ysgrifennu am Dderwyddon Prydain",
  "In his Gallic War, Julius Caesar writes that the learning of the Druids began in Britain, and that those who want to know it best cross the sea to study it here.",
  "Yn ei Ryfel Gâl, mae Iŵl Cesar yn ysgrifennu mai ym Mhrydain y dechreuodd dysg y Derwyddon, a bod y rhai sydd am ei hadnabod orau yn croesi’r môr i’w hastudio yma.", 0, "", "Druid"),
]

# ---------------------------------------------------------------- reading list
_O, _B, _W = "p", "b", "w"
REFS = {
 "druids": dict(dwb=["iolo-morganwg"], items=[
   (_O, "Julius Caesar, translated by W. A. McDevitte and W. S. Bohn", "The Gallic War", "Harper & Brothers, 1869",
    "Book VI, chapters 13 to 18: the Druids, their schools in Britain, their twenty years of learning and their Greek letters.",
    "Llyfr VI, penodau 13 i 18: y Derwyddon, eu hysgolion ym Mhrydain, eu hugain mlynedd o ddysg a’u llythrennau Groeg."),
   (_O, "Strabo, translated by H. L. Jones", "The Geography of Strabo, volume II", "Loeb Classical Library, 1923",
    "Book IV: the Bards, the Vates and the Druids, ‘the most just of men’, who stopped armies before battle.",
    "Llyfr IV: y Beirdd, y Vates a’r Derwyddon, ‘y cyfiawnaf o ddynion’, a ataliai fyddinoedd cyn brwydr."),
   (_O, "Diodorus Siculus, translated by C. H. Oldfather", "The Library of History, volume III", "Loeb Classical Library, 1939",
    "Book V, chapters 28 and 31: the bards with their lyres, and the Druids as philosophers and peacemakers.",
    "Llyfr V, penodau 28 a 31: y beirdd a’u telynau, a’r Derwyddon fel athronwyr a thangnefeddwyr."),
   (_O, "Tacitus, translated by A. J. Church and W. J. Brodribb", "The Annals", "Macmillan, 1876",
    "Book XIV, chapters 29 and 30: Môn and its Druids in AD 60.",
    "Llyfr XIV, penodau 29 a 30: Môn a’i Derwyddon yn 60 OC."),
   (_O, "Henry Rowlands", "Mona Antiqua Restaurata", "Dublin, 1723",
    "The Anglesey vicar’s book that made Môn the chief seat of the Druids.",
    "Llyfr ficer Llanidan a wnaeth Fôn yn brif sedd y Derwyddon."),
   (_B, "Miranda Aldhouse-Green", "Caesar’s Druids: Story of an Ancient Priesthood", "Yale University Press, 2010",
    "What the ancient writers and archaeology tell us of the Druids.",
    "Yr hyn y mae’r hen awduron ac archaeoleg yn ei ddweud wrthym am y Derwyddon."),
   (_B, "Peter Berresford Ellis", "The Druids", "Constable, 1994",
    "The Druids as the learned class: teachers, judges, philosophers and keepers of the calendar.",
    "Y Derwyddon fel y dosbarth dysgedig: athrawon, barnwyr, athronwyr a cheidwaid y calendr."),
   (_B, "Anne Ross", "Druids: Preachers of Immortality", "Tempus, 1999",
    "The Druids as teachers, poets and keepers of the belief that the soul does not die.",
    "Y Derwyddon fel athrawon, beirdd a cheidwaid y gred nad yw’r enaid yn marw."),
 ]),
}

# ---------------------------------------------------------------- sources beside the claims
_PERSEUS_BG = "https://fgh.perseids.org/read/latinLit/phi0448/phi001/perseus-eng2/"
CITES = {
    "dr-caesar": dict(
        short=("Caesar, Gallic War VI", "Cesar, Rhyfel Gâl VI"),
        t="The Gallic War, book VI, chapters 13 and 14", by=("Julius Caesar, about 52 BC; translated by W. A. McDevitte and W. S. Bohn, 1869", "Iŵl Cesar, tua 52 CC; cyfieithiad Saesneg W. A. McDevitte a W. S. Bohn, 1869"),
        note=("“This institution is supposed to have been devised in Britain, and to have been brought over from it into Gaul; and now those who desire to gain a more accurate knowledge of that system generally proceed thither.” Some stay twenty years and learn a great number of verses by heart; “in almost all other matters, in their public and private transactions, they use Greek characters”; they teach that souls do not perish, and about the stars, the size of the world and the nature of things; they judge disputes; one Druid presides over all.",
              "Credir i’r drefn hon gael ei dyfeisio ym Mhrydain a’i dwyn oddi yno i Âl, ac mae’r rhai sydd am ei hadnabod yn well yn mynd yno i’w hastudio. Mae rhai’n aros ugain mlynedd ac yn dysgu llawer o benillion ar gof; yn eu trafodion cyhoeddus a phreifat defnyddiant lythrennau Groeg; dysgant nad yw eneidiau’n darfod, ac am y sêr, maint y byd a natur pethau; barnant anghydfodau; mae un Derwydd yn llywyddu dros bawb."),
        url=_PERSEUS_BG + "6.13-6.16", lang="en"),
    "dr-caesar-1": dict(
        short=("Caesar, Gallic War I.29", "Cesar, Rhyfel Gâl I.29"),
        t="The Gallic War, book I, chapter 29", by=("Julius Caesar; translated by W. A. McDevitte and W. S. Bohn, 1869", "Iŵl Cesar; cyfieithiad Saesneg W. A. McDevitte a W. S. Bohn, 1869"),
        note=("“In the camp of the Helvetii, lists were found, drawn up in Greek characters, and were brought to Caesar”, counting those able to bear arms, the boys, old men and women: 368,000 in all.",
              "Cafwyd rhestrau yng ngwersyll yr Helvetii, wedi’u llunio mewn llythrennau Groeg, a’u dwyn at Gesar, yn cyfrif y rhai a allai ddwyn arfau, y bechgyn, yr hen wŷr a’r gwragedd: 368,000 i gyd."),
        url=_PERSEUS_BG + "1.29", lang="en"),
    "dr-caesar-18": dict(
        short=("Caesar, Gallic War VI.18", "Cesar, Rhyfel Gâl VI.18"),
        t="The Gallic War, book VI, chapter 18", by=("Julius Caesar; translated by W. A. McDevitte and W. S. Bohn, 1869", "Iŵl Cesar; cyfieithiad Saesneg W. A. McDevitte a W. S. Bohn, 1869"),
        note=("“They compute the divisions of every season, not by the number of days, but of nights.” Welsh wythnos (wyth nos, eight nights) and pythefnos (pymtheg nos, fifteen nights) keep the old way of counting.",
              "“Cyfrifant raniadau pob tymor, nid wrth nifer y dyddiau, ond y nosweithiau.” Mae’r geiriau Cymraeg wythnos (wyth nos) a phythefnos (pymtheg nos) yn cadw’r hen ffordd o gyfrif."),
        url=_PERSEUS_BG + "6.13-6.21", lang="en"),
    "dr-strabo": dict(
        short=("Strabo IV.4.4", "Strabo IV.4.4"),
        t="The Geography of Strabo, book IV, chapter 4, section 4", by=("Strabo, about AD 20; Loeb Classical Library, translated by H. L. Jones, 1923; LacusCurtius", "Strabo, tua 20 OC; Loeb Classical Library, cyfieithiad Saesneg H. L. Jones, 1923; LacusCurtius"),
        note=("Three orders held in exceptional honour, “the Bards, the Vates and the Druids”; the Druids study “in addition to natural philosophy ... also moral philosophy”; “The Druids are considered the most just of men”; they “made the opponents stop when they were about to line up for battle”; souls and the universe are indestructible.",
              "Tair urdd mewn parch eithriadol, y Beirdd, y Vates a’r Derwyddon; mae’r Derwyddon yn astudio athroniaeth foesol yn ogystal ag athroniaeth natur; ystyrir y Derwyddon y cyfiawnaf o ddynion; ataliant wrthwynebwyr ar fin ymffurfio i frwydr; mae eneidiau a’r bydysawd yn anninistriadwy."),
        url="https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Strabo/4D*.html", lang="en"),
    "dr-strabo-massalia": dict(
        short=("Strabo IV.1.5", "Strabo IV.1.5"),
        t="The Geography of Strabo, book IV, chapter 1, section 5", by=("Strabo; Loeb Classical Library, translated by H. L. Jones, 1923; LacusCurtius", "Strabo; Loeb Classical Library, cyfieithiad Saesneg H. L. Jones, 1923; LacusCurtius"),
        note=("Massalia (Marseille) as “a training-school for the barbarians”, “schooling the Galatae to be fond enough of the Greeks to write even their contracts in Greek”.",
              "Massalia (Marseille) yn ysgol i bobloedd Gâl, a aeth mor hoff o’r Groegiaid nes ysgrifennu hyd yn oed eu cytundebau mewn Groeg."),
        url="https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Strabo/4A*.html", lang="en"),
    "dr-diodorus": dict(
        short=("Diodorus V.31", "Diodorus V.31"),
        t="The Library of History, book V, chapters 28 and 31", by=("Diodorus of Sicily, about 30 BC; Loeb Classical Library, volume III, translated by C. H. Oldfather, 1939; LacusCurtius", "Diodorus o Sisili, tua 30 CC; Loeb Classical Library, cyfrol III, cyfieithiad Saesneg C. H. Oldfather, 1939; LacusCurtius"),
        note=("Bards who “sing to the accompaniment of instruments which are like lyres”; philosophers and theologians “unusually honoured among them and are called by them Druids”; when armies are drawn up “these men step forth between them and cause them to cease”, so that “passion give[s] place before wisdom”. V.28: “the belief of Pythagoras prevails among them, that the souls of men are immortal”.",
              "Beirdd sy’n canu i gyfeiliant offerynnau tebyg i delynau; athronwyr a diwinyddion mewn parch anghyffredin a elwir yn Dderwyddon; pan fo byddinoedd yn eu rhengoedd, camant allan rhyngddynt a pheri iddynt beidio, fel bod nwyd yn ildio i ddoethineb. V.28: cred Pythagoras, fod eneidiau dynion yn anfarwol, sy’n ffynnu yn eu plith."),
        url="https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Diodorus_Siculus/5B*.html", lang="en"),
    "dr-mela": dict(
        short=("Pomponius Mela III.2", "Pomponius Mela III.2"),
        t="De Chorographia, book III, chapter 2", by=("Pomponius Mela, about AD 43; English as given in Barddas, ed. J. Williams ab Ithel, 1862", "Pomponius Mela, tua 43 OC; Saesneg fel yn Barddas, gol. J. Williams ab Ithel, 1862"),
        note=("The Druids are “masters of wisdom”, who profess to know “the magnitude and form of the earth and the world” and “the motions of the heaven and the stars”; they “teach the most noble of the nation many things privately ... even for twenty years, in a cave, or in inaccessible woods”; they teach “that souls are immortal”.",
              "Mae’r Derwyddon yn feistri doethineb, sy’n honni gwybod maint a ffurf y ddaear a’r byd a symudiadau’r nef a’r sêr; dysgant lawer o bethau’n breifat i bendefigion y genedl, hyd yn oed am ugain mlynedd, mewn ogof neu mewn coedwigoedd anhygyrch; dysgant fod eneidiau’n anfarwol."),
        url="https://sacred-texts.com/neu/celt/bim1/bim1009.htm", lang="en"),
    "dr-pliny": dict(
        short=("Pliny XVI.95", "Pliny XVI.95"),
        t="The Natural History, book XVI, chapter 95", by=("Pliny the Elder, AD 77; translated by John Bostock and H. T. Riley, 1855; Perseus", "Pliny yr Hynaf, 77 OC; cyfieithiad Saesneg John Bostock a H. T. Riley, 1855; Perseus"),
        note=("The Druids hold “nothing more sacred than the mistletoe and the tree that bears it”; “Clad in a white robe the priest ascends the tree, and cuts the mistletoe with a golden sickle”; they call it by “a name which signifies, in their language, the all-healing”; Pliny thinks their name may come from the Greek word for the oak.",
              "Nid oes dim yn fwy cysegredig i’r Derwyddon na’r uchelwydd a’r goeden sy’n ei dwyn; mewn gwisg wen dringa’r offeiriad y goeden a thorri’r uchelwydd â chryman aur; galwant hi wrth enw sy’n golygu’r holliachâd; tybia Pliny y gall eu henw ddod o’r gair Groeg am y dderwen."),
        url="https://www.perseus.tufts.edu/hopper/text?doc=Plin.+Nat.+16.95", lang="en"),
    "dr-diogenes": dict(
        short=("Diogenes Laertius", "Diogenes Laertius"),
        t="Lives of the Eminent Philosophers, prologue", by=("Diogenes Laertius, third century AD; Loeb Classical Library, R. D. Hicks, 1925; Perseus", "Diogenes Laertius, y drydedd ganrif OC; Loeb Classical Library, R. D. Hicks, 1925; Perseus"),
        note=("“There are some who say that the study of philosophy had its beginning among the barbarians”, among them the Druids; the Druids “uttered their philosophy in riddles, bidding men to reverence the gods ... to abstain from wrongdoing, and to practise courage”.",
              "Mae rhai’n dweud i astudio athroniaeth ddechrau ymhlith y pobloedd y tu hwnt i Roeg, yn eu plith y Derwyddon; traethai’r Derwyddon eu hathroniaeth mewn posau, gan annog dynion i barchu’r duwiau, ymgadw rhag drwg ac arfer dewrder."),
        url="https://fgh.perseids.org/read/greekLit/tlg0004/tlg001/perseus-eng2/1.prol.1-1.prol.20", lang="en"),
    "dr-ammianus": dict(
        short=("Ammianus XV.9", "Ammianus XV.9"),
        t="The History (Res Gestae), book XV, chapter 9, section 8", by=("Ammianus Marcellinus, about 390, after Timagenes; Loeb Classical Library, translated by J. C. Rolfe; Perseus", "Ammianus Marcellinus, tua 390, ar ôl Timagenes; Loeb Classical Library, cyfieithiad Saesneg J. C. Rolfe; Perseus"),
        note=("The bards “sang to the sweet strains of the lyre the valorous deeds of famous men”; the Euhages “attempted to explain the secret laws of nature”; the Druids, “loftier than the rest in intellect”, bound together in fellowship as Pythagoras taught, “pronounced the soul immortal”.",
              "Canai’r beirdd i seiniau melys y delyn gampau dewr gwŷr enwog; ceisiai’r Euhages egluro deddfau cudd natur; a’r Derwyddon, yn uwch na’r lleill o ran deall ac mewn cymdeithas fel y dysgodd Pythagoras, a gyhoeddodd fod yr enaid yn anfarwol."),
        url="https://cts.perseids.org/read/latinLit/stoa0023/stoa001/perseus-eng2/15.9.7-15.9.8", lang="en"),
    "dr-cicero": dict(
        short=("Cicero, On Divination", "Cicero, Ar Ddewiniaeth"),
        t="On Divination (De Divinatione), book I, section 90", by=("Marcus Tullius Cicero, 44 BC; Loeb Classical Library, translated by W. A. Falconer, 1923; LacusCurtius", "Marcus Tullius Cicero, 44 CC; Loeb Classical Library, cyfieithiad Saesneg W. A. Falconer, 1923; LacusCurtius"),
        note=("Quintus Cicero to his brother: there are Druids in Gaul, “I knew one of them myself, Divitiacus, the Aeduan, your guest and eulogist”, who claimed the knowledge of nature that the Greeks call physiologia and foretold what was to come.",
              "Quintus Cicero wrth ei frawd: mae Derwyddon yng Ngâl, ac adwaenai un ei hun, Divitiacus yr Aeduad, gwestai a molwr ei frawd, a honnai’r wybodaeth am natur a eilw’r Groegiaid yn physiologia ac a ragfynegai’r hyn oedd i ddod."),
        url="https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cicero/de_Divinatione/1*.html", lang="en"),
    "dr-tacitus": dict(
        short=("Tacitus, Annals XIV", "Tacitus, Annales XIV"),
        t="The Annals, book XIV, chapters 29 and 30", by=("Tacitus, about AD 116; Loeb Classical Library, translated by J. Jackson, 1937; LacusCurtius", "Tacitus, tua 116 OC; Loeb Classical Library, cyfieithiad Saesneg J. Jackson, 1937; LacusCurtius"),
        note=("Paulinus attacks Mona, “which had a considerable population of its own, while serving as a haven for refugees”: flat-bottomed boats for the foot, the cavalry fording or swimming beside their horses; on the shore the warriors, the women in black with torches, “a circle of Druids, lifting their hands to heaven”; the soldiers stood “as though their limbs were paralysed”. News of the rising in the east then called Paulinus away.",
              "Ymosoda Paulinus ar Fôn, ynys â phoblogaeth sylweddol ac yn hafan i ffoaduriaid: cychod gwaelod gwastad i’r gwŷr traed, y marchogion yn rhydio neu’n nofio wrth ochr eu meirch; ar y lan y rhyfelwyr, y gwragedd mewn du â ffaglau, a chylch o Dderwyddon yn codi eu dwylo i’r nef; safai’r milwyr fel petai eu haelodau wedi’u parlysu. Yna galwodd y gwrthryfel yn y dwyrain Paulinus ymaith."),
        url="https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Tacitus/Annals/14B*.html", lang="en"),
    "dr-tacitus-cb": dict(
        short=("Tacitus, tr. Church and Brodribb", "Tacitus, cyf. Church a Brodribb"),
        t="The Annals, book XIV, chapter 30", by=("translated by A. J. Church and W. J. Brodribb, 1876; MIT Internet Classics Archive", "cyfieithiad Saesneg A. J. Church a W. J. Brodribb, 1876"),
        note=("“All around, the Druids, lifting up their hands to heaven ... scared our soldiers by the unfamiliar sight, so that, as if their limbs were paralysed, they stood motionless.”",
              "O amgylch, y Derwyddon yn codi eu dwylo i’r nef, gan ddychryn y milwyr â’r olwg ddieithr, nes iddynt sefyll yn llonydd fel petai eu haelodau wedi’u parlysu."),
        url="https://classics.mit.edu/Tacitus/annals.mb.txt", lang="en"),
    "dr-armes": dict(
        short=("Armes Prydein", "Armes Prydein"),
        t="Armes Prydein Vawr, the Great Prophecy of Britain", by=("Book of Taliesin (National Library of Wales, Peniarth MS 2), poem of about 930; Welsh text at ancienttexts.org", "Llyfr Taliesin (Llyfrgell Genedlaethol Cymru, Peniarth 2), cerdd o tua 930; testun Cymraeg yn ancienttexts.org"),
        note=("The poem foretells the Cymry and their allies driving the English out of Britain; one of its lines is “Dysgogan derwydon meint a deruyd”, the druids foretell all that will come to pass.",
              "Mae’r gerdd yn darogan y Cymry a’u cynghreiriaid yn gyrru’r Saeson o Brydain; un o’i llinellau yw “Dysgogan derwydon meint a deruyd”."),
        url="https://www.ancienttexts.org/library/celtic/ctexts/t06w.html", lang="cy"),
    "dr-rowlands": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur Cymreig"),
        t="ROWLANDS, HENRY (1655 - 1723), antiquary", by=("Dictionary of Welsh Biography, National Library of Wales", "Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
        note=("Henry Rowlands of Plas Gwyn, Llanedwen, vicar of Llanidan; his Mona Antiqua Restaurata (Dublin, 1723) sets out the antiquities of Anglesey and tries to prove that the island was the chief seat of the druids.",
              "Henry Rowlands o Blas Gwyn, Llanedwen, ficer Llanidan; mae ei Mona Antiqua Restaurata (Dulyn, 1723) yn disgrifio hynafiaethau Môn ac yn ceisio profi mai’r ynys oedd prif sedd y derwyddon."),
        url="https://biography.wales/article/s-ROWL-HEN-1655", url_cy="https://bywgraffiadur.cymru/article/s-ROWL-HEN-1655"),
    "dr-coligny": dict(
        short=("Coligny calendar", "Calendr Coligny"),
        t="Coligny calendar", by=("Wikipedia, from the bronze tablets in the Gallo-Roman Museum of Lyon-Fourvière", "Wikipedia, o’r tabledi efydd yn Amgueddfa Galo-Rufeinig Lyon-Fourvière"),
        note=("Found in 1897 at Coligny, near Lyon; bronze, second century AD; a five-year cycle of lunar months with two extra months, 62 in all, fitted to the solar year; in the Gaulish language, in Latin letters.",
              "Fe’i cafwyd yn 1897 yn Coligny, ger Lyon; efydd, yr ail ganrif OC; cylch pum mlynedd o fisoedd lleuad gyda dau fis ychwanegol, 62 i gyd, wedi’u cysoni â blwyddyn yr haul; yn yr iaith Aleg, mewn llythrennau Lladin."),
        url="https://en.wikipedia.org/wiki/Coligny_calendar", lang="en"),
}
