# The Laws of Hywel Dda: the big page (laws.html). build.py's laws_page() turns this into the page.
# The shorter story of Hywel himself is the long read in src/hywel.py (story-hywel.html).
# Paragraph codes are the same as for long reads (prose() in build.py):
#   "## Heading"   a sub-heading      "> Quote | Source"   a pull quote      "|| Left | Right"   a table row
# Text uses curly quotes ‘ ’ so it never clashes with code quotes.
#
# Main sources: the lawbooks themselves in translation (Aneurin Owen, Ancient Laws and Institutes of Wales, 1841;
# Dafydd Jenkins, The Law of Hywel Dda, 1986), the Dictionary of Welsh Biography (Blegywryd), the National Library
# of Wales (the manuscripts) and the Hywel Dda Centre, Whitland.

# ---------- pictures: Commons file, who made it, licence, licence link, caption EN, caption CY ----------
PD = ("Public domain", "https://en.wikipedia.org/wiki/Public_domain")
CC0 = ("CC0", "https://creativecommons.org/publicdomain/zero/1.0/")
BYSA2 = ("CC BY-SA 2.0", "https://creativecommons.org/licenses/by-sa/2.0/")
BYSA3 = ("CC BY-SA 3.0", "https://creativecommons.org/licenses/by-sa/3.0/")

NLW = "National Library of Wales"
FIGS = {
 "king": ("Laws of Hywel Dda (f.1.v) King Hywel.jpg", "Unknown scribe, " + NLW + " (Peniarth MS 28)", *CC0,
          "King Hywel on his throne, the first picture in Peniarth 28, the Latin lawbook of the thirteenth century",
          "Y Brenin Hywel ar ei orsedd, y llun cyntaf yn Peniarth 28, llyfr cyfraith Lladin y drydedd ganrif ar ddeg"),
 "kingc": ("Laws of Hywel Dda (f.1.v) King Hywel cropped.jpg", "Unknown scribe, " + NLW + " (Peniarth MS 28)", *CC0,
           "Hywel Dda, crowned and holding his sceptre: the picture of the king in Peniarth 28, drawn some three hundred years after his death",
           "Hywel Dda, â’i goron a’i deyrnwialen: llun y brenin yn Peniarth 28, wedi’i dynnu tua thri chan mlynedd wedi ei farw"),
 "codifying": ("William Edward Jones (1825-1877) - Hywel Dda Codifying the Laws of Wales - OP4 - Aberystwyth University, School of Art Museum and Galleries.jpg",
               "William Edward Jones, 1876 (Aberystwyth University School of Art)", *PD,
               "Hywel Dda codifying the laws of Wales, painted by William Edward Jones in 1876",
               "Hywel Dda yn trefnu cyfreithiau Cymru, paentiad gan William Edward Jones yn 1876"),
 "proclaim": ("Proclaiming the Laws of Howel Dda.jpg", "From Flame Bearers of Welsh History (1905), " + NLW, *PD,
              "Proclaiming the laws of Hywel Dda, as a book for Welsh schoolchildren pictured it in 1905",
              "Cyhoeddi cyfreithiau Hywel Dda, fel y’i darluniwyd mewn llyfr i blant ysgol Cymru yn 1905"),
 "judge": ("Laws of Hywel Dda (f.4.r) Judge & Hawker.jpg", "Unknown scribe, " + NLW + " (Peniarth MS 28)", *CC0,
           "The court judge and the falconer with his hawk, drawn in the margins of Peniarth 28",
           "Ynad y llys a’r hebogydd â’i hebog, wedi’u tynnu ar ymylon Peniarth 28"),
 "distain": ("Distain, Peniarth MS 28 f. 3v.png", "Unknown scribe, " + NLW + " (Peniarth MS 28)", *PD,
             "The distain, the steward of the king’s court, in Peniarth 28",
             "Y distain, stiward llys y brenin, yn Peniarth 28"),
 "hair": ("The Laws of Hywel Dda (f.15.v) hair pulling (cropped).png", "Unknown scribe, " + NLW + " (Peniarth MS 28)", *CC0,
          "One man pulls another’s hair, drawn beside the law of insults and injuries in Peniarth 28: even that had its price",
          "Un gŵr yn tynnu gwallt un arall, wedi’i dynnu ger cyfraith sarhad ac anafiadau yn Peniarth 28: roedd pris ar hynny hyd yn oed"),
 "couple": ("Laws of Hywel Dda (f.5.r) Kissing couple cropped.jpg", "Unknown scribe, " + NLW + " (Peniarth MS 28)", *CC0,
            "A man and a woman kiss beside the law of marriage in Peniarth 28",
            "Gŵr a gwraig yn cusanu ger cyfraith priodas yn Peniarth 28"),
 "chirk": ("ChirkCodex.png", "Unknown scribe, " + NLW + " (Peniarth MS 29)", *PD,
           "A page of the Black Book of Chirk, about 1250, the oldest copy of the law in Welsh",
           "Tudalen o Lyfr Du’r Waun, tua 1250, y copi hynaf o’r gyfraith yn Gymraeg"),
 "boston": ("Boston Welsh Law Ms (f.6.v).jpg", "Unknown scribe, " + NLW + " (the Boston manuscript)", *CC0,
            "The Boston manuscript: a small pocket lawbook of the fourteenth century with the law of Dyfed, the Book of Blegywryd",
            "Llawysgrif Boston: llyfr cyfraith bach i’w gario o’r bedwaredd ganrif ar ddeg, â chyfraith Dyfed, Llyfr Blegywryd"),
 "pen38": ("Cyfraith Hywel Dda, folio 7r (4780062).jpg", "Unknown scribe, " + NLW + " (Peniarth MS 38)", *CC0,
           "Red and black: a page of Cyfraith Hywel in Peniarth 38",
           "Coch a du: tudalen o Gyfraith Hywel yn Peniarth 38"),
 "pen36": ("Cyfraith Hywel Dda, folio 1v (4783982).jpg", "Unknown scribe, " + NLW + " (Peniarth MS 36)", *CC0,
           "A lawyer’s copy, worn by use: Peniarth 36",
           "Copi cyfreithiwr, wedi’i dreulio gan ei ddefnyddio: Peniarth 36"),
 "welsh29": ("F. 29r. Welsh text of Laws of Hywel Dda.jpg", "Unknown scribe, " + NLW, *CC0,
             "A Welsh lawbook of the fourteenth century, with its own little pictures in the margin",
             "Llyfr cyfraith Cymraeg o’r bedwaredd ganrif ar ddeg, â’i luniau bach ei hun ar yr ymyl"),
 "plaque": ("Plaque, Hywel Dda Centre, Whitland - geograph.org.uk - 1162210.jpg", "welshbabe, geograph.org.uk", *BYSA2,
            "The memorial stone at Whitland: ‘In honour of Hywel Dda, king of all Wales in the tenth century, the head and glory of all the Britons. By his name the Welsh law of the Middle Ages was called. He is linked especially with this district.’",
            "Y garreg goffa yn Hendy-gwyn: ‘Er anrhydedd i Hywel Dda, brenin Cymru oll yn y ddegfed ganrif, pen a moliant yr holl Frytaniaid. Ar ei enw ef y galwyd Cyfraith Gymreig yr Oesau Canol. Cysylltir ef yn arbennig â’r fro hon.’"),
 "cat": ("The value of a cat, according to the Law of Hywel Dda - geograph.org.uk - 1985829.jpg", "ceridwen, geograph.org.uk", *BYSA2,
         "The value of a cat, set in the paving of the Hywel Dda garden at Whitland",
         "Gwerth cath, wedi’i osod yn llawr gardd Hywel Dda yn Hendy-gwyn"),
 "garden": ("The Oak garden, Hywel Dda Centre - geograph.org.uk - 1987810.jpg", "ceridwen, geograph.org.uk", *BYSA2,
            "The oak garden at the Hywel Dda Centre, Whitland, one of six gardens that each tell of one part of the law",
            "Gardd y dderwen yng Nghanolfan Hywel Dda, Hendy-gwyn, un o chwe gardd sydd bob un yn adrodd am un rhan o’r gyfraith"),
}

# ---------- at a glance ----------
FACTS_EN = [
 "|| Its name | Cyfraith Hywel, the Law of Hywel",
 "|| Named after | Hywel Dda, king of almost all Wales, died 950",
 "|| Set in order | at Tŷ Gwyn ar Daf, Whitland, in Lent, about 945, the lawbooks say",
 "|| Written down by | Master Blegywryd, with twelve wise laymen",
 "|| The books | Llyfr Cyfnerth, Llyfr Blegywryd, Llyfr Iorwerth, and Latin versions",
 "|| Copies that survive | about forty, the oldest from the thirteenth century",
 "|| Its great idea | put a wrong right with payment, instead of revenge",
 "|| In use until | 1536 to 1543; the last known case was heard in 1540",
]
FACTS_CY = [
 "|| Ei henw | Cyfraith Hywel",
 "|| Wedi’i henwi ar ôl | Hywel Dda, brenin bron y cyfan o Gymru, bu farw 950",
 "|| Ei threfnu | yn y Tŷ Gwyn ar Daf, Hendy-gwyn, yn y Grawys, tua 945, medd y llyfrau",
 "|| Ei hysgrifennu gan | Meistr Blegywryd, gyda deuddeg lleygwr doeth",
 "|| Y llyfrau | Llyfr Cyfnerth, Llyfr Blegywryd, Llyfr Iorwerth, a fersiynau Lladin",
 "|| Copïau sydd wedi goroesi | tua deugain, y rhai hynaf o’r drydedd ganrif ar ddeg",
 "|| Ei syniad mawr | unioni cam drwy dalu, yn lle dial",
 "|| Mewn grym hyd | 1536 i 1543; clywyd yr achos olaf y gwyddys amdano yn 1540",
]

INTRO_EN = [
 "For six hundred years the people of Wales lived under a law of their own. It did not come from Rome, or from England, or from any foreign king. It grew out of the customs of the Britons, it was written in Welsh, it was argued by Welsh lawyers in Welsh courts, and it carried the name of one Welsh king: Hywel Dda, Hywel the Good. It was called Cyfraith Hywel, the Law of Hywel.",
 "It is one of the great achievements of medieval Europe. At a time when much of the continent settled a killing with another killing, the law of Wales asked for payment and peace. It set a fair price on every loss, from a king’s honour to a kitten. It gave a wife a share of everything after seven years of marriage. It divided a father’s land among all his sons. And it would not punish a hungry person for taking food to stay alive.",
 "This page tells the whole story: how the law was made, the books that carried it, what it said about crime, honour, marriage, children, land and animals, the pictures its scribes drew, and how it lasted until the Acts of Union. At the bottom there is a quiz: see how well you would have done as a judge in Hywel’s Wales.",
]
INTRO_CY = [
 "Am chwe chan mlynedd bu pobl Cymru’n byw dan eu cyfraith eu hunain. Nid o Rufain y daeth hi, nac o Loegr, nac oddi wrth unrhyw frenin estron. Tyfodd o arferion y Brythoniaid, fe’i hysgrifennwyd yn Gymraeg, fe’i dadleuwyd gan gyfreithwyr Cymreig mewn llysoedd Cymreig, a dygai enw un brenin o Gymro: Hywel Dda. Ei henw oedd Cyfraith Hywel.",
 "Mae’n un o gampau mawr Ewrop yr Oesoedd Canol. Mewn oes pan setlai llawer o’r cyfandir un lladdiad ag un arall, gofynnai cyfraith Cymru am dâl a heddwch. Rhoddai bris teg ar bob colled, o anrhydedd brenin i gath fach. Rhoddai i wraig ran o bopeth wedi saith mlynedd o briodas. Rhannai dir tad rhwng ei feibion i gyd. Ac ni chosbai’r newynog am gymryd bwyd i aros yn fyw.",
 "Mae’r dudalen hon yn adrodd yr hanes cyfan: sut y lluniwyd y gyfraith, y llyfrau a’i cariodd, yr hyn a ddywedai am drosedd, anrhydedd, priodas, plant, tir ac anifeiliaid, y lluniau a dynnodd ei hysgrifwyr, a sut y parhaodd hyd y Deddfau Uno. Ar y gwaelod mae cwis: gwelwch pa mor dda y byddech wedi gwneud fel ynad yng Nghymru Hywel.",
]

# ---------- the story in dates: year, EN, CY ----------
DATES = [
 ("about 880", "Hywel ap Cadell is born, a grandson of Rhodri Mawr.", "Ganwyd Hywel ap Cadell, ŵyr i Rodri Mawr."),
 ("920", "Hywel joins Dyfed and Seisyllwg into one kingdom, Deheubarth.", "Hywel yn uno Dyfed a Seisyllwg yn un deyrnas, Deheubarth."),
 ("928", "Hywel makes the pilgrimage to Rome.", "Hywel yn mynd ar bererindod i Rufain."),
 ("942", "Hywel becomes king of Gwynedd and Powys too, ruling almost all Wales.", "Hywel yn frenin Gwynedd a Phowys hefyd, gan reoli bron y cyfan o Gymru."),
 ("about 945", "The gathering at the White House on the Taf, as the lawbooks tell it.", "Y cynulliad yn y Tŷ Gwyn ar Daf, fel yr adrodda’r llyfrau cyfraith."),
 ("950", "Hywel dies. The chronicle calls him king of the Britons.", "Marw Hywel. Geilw’r cronicl ef yn frenin y Brythoniaid."),
 ("late 1100s", "Llyfr Cyfnerth takes shape in the lands between the Wye and the Severn.", "Llyfr Cyfnerth yn cymryd ffurf yn y tiroedd rhwng Gwy a Hafren."),
 ("early 1200s", "Iorwerth ap Madog revises the law of Gwynedd in the time of Llywelyn Fawr.", "Iorwerth ap Madog yn adolygu cyfraith Gwynedd yn oes Llywelyn Fawr."),
 ("about 1250", "The Black Book of Chirk and Peniarth 28 are written, the oldest copies we have.", "Ysgrifennu Llyfr Du’r Waun a Peniarth 28, y copïau hynaf sydd gennym."),
 ("1278 to 1282", "Llywelyn ap Gruffudd demands that Welsh land be judged by Welsh law.", "Llywelyn ap Gruffudd yn mynnu barnu tir Cymru dan gyfraith Cymru."),
 ("1284", "The Statute of Rhuddlan replaces Welsh criminal law. Welsh law of land, family and contracts lives on.", "Statud Rhuddlan yn disodli cyfraith droseddol Cymru. Mae cyfraith Cymru am dir, teulu a chytundebau’n parhau."),
 ("1300s and 1400s", "Lawyers keep copying the books. Many of the forty surviving manuscripts are from these years.", "Cyfreithwyr yn dal i gopïo’r llyfrau. Daw llawer o’r deugain llawysgrif o’r blynyddoedd hyn."),
 ("1536 and 1543", "The Acts of Union bring Wales under English law.", "Y Deddfau Uno yn dod â Chymru dan gyfraith Lloegr."),
 ("1540", "The last known case under Welsh law is heard, over land in Carmarthenshire.", "Clywed yr achos olaf y gwyddys amdano dan gyfraith Cymru, am dir yn Sir Gaerfyrddin."),
 ("1841", "Aneurin Owen prints the lawbooks in full: Ancient Laws and Institutes of Wales.", "Aneurin Owen yn argraffu’r llyfrau cyfraith yn llawn: Ancient Laws and Institutes of Wales."),
 ("1986", "Dafydd Jenkins publishes The Law of Hywel Dda, a modern translation.", "Dafydd Jenkins yn cyhoeddi The Law of Hywel Dda, cyfieithiad modern."),
 ("2011", "The people of Wales vote for the Senedd to make its own laws.", "Pobl Cymru’n pleidleisio i’r Senedd wneud ei chyfreithiau ei hun."),
 ("2012", "The first Act made in Wales, in Welsh and English, becomes law.", "Y Ddeddf gyntaf a wnaed yng Nghymru, yn Gymraeg a Saesneg, yn dod yn gyfraith."),
]

# ---------- the chapters: id, title EN, title CY, short label EN/CY for the jump links, paragraphs, pictures ----------
CHAPTERS = [
 dict(id="whitland", en="The gathering at the White House", cy="Y cynulliad yn y Tŷ Gwyn", figs=["codifying"],
  pEn=[
   "Every lawbook begins with the same story. Hywel, son of Cadell, king of all Wales, saw that the laws and customs of the land had grown tangled, and were often broken. So he called to him, at the White House on the Taf, six men from every part of his kingdom. Some books say six from every cantref; others say six from every commote. With them came the bishops, the abbots and the learned clergy of Wales.",
   "They came in Lent, and the books say they spent the whole forty days in fasting and prayer, asking God to guide them to good law. One book explains the name: Tŷ Gwyn, the White House, was a hunting lodge of the king, built of white peeled rods. It stood near the river Taf, where the town of Whitland, Hendy-gwyn ar Daf, stands today.",
   "They went through the old laws one by one. Some they let stand, some they amended, some they set aside altogether, and some new laws they made.",
   "From the whole gathering Hywel chose twelve of the wisest laymen, and one scholar, Master Blegywryd, to set the law in order and write it down. When the work was done it was read aloud before them all. The bishops laid the curse of the church on anyone who would break it.",
   "Three copies were made, says the book of Gwynedd: one to go with the court wherever the king went, one for Aberffraw, the chief court of the north, and one for Dinefwr, the chief court of the south. Then Hywel went to Rome with his bishops, so the books say, and the law was read before the Pope, and found good, and came home with his blessing.",
   "The copies we have were all written down two or three centuries after Hywel, and the law kept growing as lawyers used it, so scholars still weigh which parts go back to his own day. But that is how the law told its own beginning, and every lawyer in Wales, north and south, held it to be the law of Hywel.",
  ],
  pCy=[
   "Mae pob llyfr cyfraith yn dechrau â’r un stori. Gwelodd Hywel ap Cadell, brenin Cymru oll, fod cyfreithiau ac arferion y wlad wedi mynd yn ddryslyd, ac yn cael eu torri’n aml. Felly galwodd ato, i’r Tŷ Gwyn ar Daf, chwe gŵr o bob rhan o’i deyrnas. Dywed rhai llyfrau chwech o bob cantref; dywed eraill chwech o bob cwmwd. Gyda hwy daeth esgobion, abadau a chlerigwyr dysgedig Cymru.",
   "Daethant yn y Grawys, a dywed y llyfrau iddynt dreulio’r deugain niwrnod cyfan yn ymprydio a gweddïo, gan ofyn i Dduw eu harwain at gyfraith dda. Mae un llyfr yn egluro’r enw: hela-dy i’r brenin oedd y Tŷ Gwyn, wedi’i godi o wiail gwynion wedi’u pilio. Safai ger afon Taf, lle saif tref Hendy-gwyn ar Daf heddiw.",
   "Aethant drwy’r hen gyfreithiau fesul un. Rhai a adawsant i sefyll, rhai a ddiwygiasant, rhai a roesant o’r neilltu’n llwyr, a rhai cyfreithiau newydd a wnaethant.",
   "O’r cynulliad cyfan dewisodd Hywel ddeuddeg o’r lleygwyr doethaf, ac un ysgolhaig, Meistr Blegywryd, i roi trefn ar y gyfraith a’i hysgrifennu. Pan oedd y gwaith ar ben fe’i darllenwyd yn uchel ger eu bron i gyd. Gosododd yr esgobion felltith yr eglwys ar unrhyw un a’i torrai.",
   "Gwnaed tri chopi, medd llyfr Gwynedd: un i fynd gyda’r llys i ble bynnag yr âi’r brenin, un i Aberffraw, prif lys y gogledd, ac un i Ddinefwr, prif lys y de. Yna aeth Hywel i Rufain gyda’i esgobion, medd y llyfrau, a darllenwyd y gyfraith gerbron y Pab, a’i chael yn dda, a daeth adref gyda’i fendith.",
   "Ysgrifennwyd y copïau sydd gennym i gyd ddwy neu dair canrif wedi Hywel, a pharhaodd y gyfraith i dyfu wrth i gyfreithwyr ei defnyddio, felly mae ysgolheigion yn dal i bwyso a mesur pa rannau sy’n mynd yn ôl i’w ddydd ef. Ond dyna sut yr adroddai’r gyfraith ei dechreuad ei hun, a daliai pob cyfreithiwr yng Nghymru, yn y gogledd a’r de, mai cyfraith Hywel ydoedd.",
  ]),

 dict(id="blegywryd", en="Master Blegywryd", cy="Meistr Blegywryd", figs=["proclaim"],
  pEn=[
   "Of all the wise men at the White House, only one is named in the books: Blegywryd, son of Einion. The Welsh books call him athro, master, and yr un ysgolhaig doethaf, the one wisest scholar. The Latin books call him clericus doctissimus, a most learned clerk, and doctor of law to Hywel’s company. He was the one who took the law the gathering agreed and wrote it out.",
   "The Book of Llandaf, written in the twelfth century, names a Blegywryd son of Einion in Gwent in the 950s, which may be the same man. His name lives on in Llyfr Blegywryd, the lawbook of Dyfed and Deheubarth, which some scholars have thought stands closest of all the books to the law of Hywel’s own kingdom.",
  ],
  pCy=[
   "O’r holl wŷr doeth yn y Tŷ Gwyn, dim ond un a enwir yn y llyfrau: Blegywryd ab Einion. Geilw’r llyfrau Cymraeg ef yn athro, ac yn ‘yr un ysgolhaig doethaf’. Geilw’r llyfrau Lladin ef yn clericus doctissimus, clerigwr dysgedig iawn, ac yn ddoctor y gyfraith i osgordd Hywel. Ef a gymerodd y gyfraith y cytunodd y cynulliad arni a’i hysgrifennu.",
   "Mae Llyfr Llandaf, a ysgrifennwyd yn y ddeuddegfed ganrif, yn enwi Blegywryd ab Einion yng Ngwent yn y 950au, a gall mai’r un gŵr ydyw. Mae ei enw’n fyw o hyd yn Llyfr Blegywryd, llyfr cyfraith Dyfed a Deheubarth, y tybiodd rhai ysgolheigion mai ef sydd agosaf o’r holl lyfrau at gyfraith teyrnas Hywel ei hun.",
  ]),

 dict(id="books", en="The three lawbooks", cy="Y tri llyfr cyfraith", figs=[], books=True,
  pEn=[
   "The law was not kept in one book but in many, copied by hand by lawyers who used them in court and added to them as cases came up. Scholars sort the Welsh books into three families, each named after a lawyer and each belonging to a part of Wales. Beside them stand the Latin books, made for churchmen and for courts that wrote in Latin.",
  ],
  pCy=[
   "Ni chadwyd y gyfraith mewn un llyfr ond mewn llawer, wedi’u copïo â llaw gan gyfreithwyr a’u defnyddiai yn y llys ac a ychwanegai atynt wrth i achosion godi. Mae ysgolheigion yn rhannu’r llyfrau Cymraeg yn dri theulu, pob un wedi’i enwi ar ôl cyfreithiwr a phob un yn perthyn i ran o Gymru. Wrth eu hochr saif y llyfrau Lladin, a wnaed i wŷr eglwysig ac i lysoedd a ysgrifennai yn Lladin.",
  ]),

 dict(id="inside", en="Inside a lawbook", cy="Y tu mewn i lyfr cyfraith", figs=[],
  pEn=[
   "A Welsh lawbook has two great parts. The first is the Laws of the Court: the king, the queen and the heir, the twenty-four officers of the royal household, their duties, their rights and their gifts. The second is the Laws of the Country: everything else, from killing and theft to marriage, land, contracts, ploughing together, and the worth of animals and trees.",
   "## The Three Columns of Law",
   "The northern books add a third part, the Judges’ Test Book, Llyfr Prawf Ynad, which a man had to know before he could sit as a judge. At its heart are the Three Columns of Law: the nine accessories of killing, the nine accessories of fire and the nine accessories of theft. An accessory was anyone who helped a wrong along without doing it himself: the one who pointed out the victim, the one who held the horse, the one who stood by and did nothing. The law of Wales held each of them to account, and set a price for each.",
   "## Law that could be remembered",
   "Welsh lawyers liked to put the law in threes, the same way the poets kept the history of the Britons in the triads. The books are full of them: three things that cannot be sold, three kinds of witnesses, three ways to prove a claim. A lawyer could carry the law in his memory as well as in his book.",
   "## The judges",
   "In Gwynedd the judge, the ynad, was a trained lawyer. According to Llyfr Iorwerth he had to be at least twenty-five years old and be examined by the court judge before he could judge, and he paid twenty-four pence for the privilege. In parts of the south the free landowners of the district sat together to judge, with the professional judges beside them. A judge whose judgement was proved false had to pay the worth of his tongue, as the law called it.",
  ],
  pCy=[
   "Mae dwy ran fawr i lyfr cyfraith Cymraeg. Y gyntaf yw Cyfraith y Llys: y brenin, y frenhines a’r edling, pedwar swyddog ar hugain y llys brenhinol, eu dyletswyddau, eu hawliau a’u rhoddion. Yr ail yw Cyfraith y Wlad: popeth arall, o ladd a lladrata i briodas, tir, cytundebau, cyd-aredig, a gwerth anifeiliaid a choed.",
   "## Tair Colofn Cyfraith",
   "Mae llyfrau’r gogledd yn ychwanegu trydedd ran, Llyfr Prawf Ynad, y bu’n rhaid i ŵr ei wybod cyn y gallai eistedd yn ynad. Wrth ei galon y mae Tair Colofn Cyfraith: naw affaith galanas, naw affaith tân a naw affaith lladrad. Affaith oedd unrhyw un a helpai gam ymlaen heb ei wneud ei hun: yr un a ddangosai’r ffordd at y dioddefwr, yr un a ddaliai’r march, yr un a safai heb wneud dim. Daliai cyfraith Cymru bob un ohonynt yn gyfrifol, a gosod pris ar bob un.",
   "## Cyfraith y gellid ei chofio",
   "Hoffai cyfreithwyr Cymru osod y gyfraith yn drioedd, yn yr un modd ag y cadwai’r beirdd hanes y Brythoniaid yn y trioedd. Mae’r llyfrau’n llawn ohonynt: tri pheth na ellir eu gwerthu, tri math o dystion, tair ffordd o brofi hawl. Gallai cyfreithiwr gario’r gyfraith yn ei gof yn ogystal ag yn ei lyfr.",
   "## Yr ynadon",
   "Yng Ngwynedd roedd yr ynad yn gyfreithiwr wedi’i hyfforddi. Yn ôl Llyfr Iorwerth rhaid oedd iddo fod yn bump ar hugain oed o leiaf a chael ei holi gan ynad y llys cyn y câi farnu, a thalai bedair ceiniog ar hugain am y fraint. Mewn rhannau o’r de eisteddai tirfeddianwyr rhydd y fro gyda’i gilydd i farnu, a’r ynadon proffesiynol wrth eu hochr. Rhaid oedd i ynad y profwyd ei farn yn gam dalu gwerth ei dafod, fel y dywedai’r gyfraith.",
  ]),

 dict(id="court", en="The king’s court", cy="Llys y brenin", figs=["judge", "distain"], officers=True,
  pEn=[
   "The Laws of the Court open a door into a Welsh royal hall a thousand years ago. The king sat at the head of the hall, his heir, the edling, near him. The edling’s title came from the English word ætheling, a prince of the blood; the queen and the edling each had a sarhaed one third of the king’s. Around them sat the twenty-four officers, each in his own place, each with his own share of the meat, the mead, the horses and the clothes the king gave at the three great feasts of the year: Christmas, Easter and Whitsun.",
   "The law tells us the smallest things about them. The household priest received the garment in which the king had done penance in Lent. The court judge received a gaming board from the king and a gold ring from the queen when he took office. The bard of the household received a harp from the king and a gold ring from the queen, and when the warband went into battle he sang to them Unbennaeth Prydain, The Sovereignty of Britain. The falconer was allowed only three drinks in the hall, so that the king’s hawks would never be neglected for the mead.",
  ],
  pCy=[
   "Mae Cyfraith y Llys yn agor drws i neuadd frenhinol Gymreig fil o flynyddoedd yn ôl. Eisteddai’r brenin ym mhen y neuadd, a’i etifedd, yr edling, yn ei ymyl. Daeth teitl yr edling o’r gair Saesneg ætheling, tywysog o waed brenhinol; roedd sarhaed y frenhines a’r edling ill dau’n draean un y brenin. O’u cwmpas eisteddai’r pedwar swyddog ar hugain, pob un yn ei le ei hun, pob un â’i gyfran ei hun o’r cig, y medd, y meirch a’r dillad a roddai’r brenin ar dair gŵyl fawr y flwyddyn: y Nadolig, y Pasg a’r Sulgwyn.",
   "Mae’r gyfraith yn dweud wrthym y pethau lleiaf amdanynt. Câi offeiriad y teulu’r wisg y gwnaethai’r brenin ei benyd ynddi yn y Grawys. Câi ynad y llys fwrdd chwarae gan y brenin a modrwy aur gan y frenhines pan dderbyniai ei swydd. Câi bardd teulu delyn gan y brenin a modrwy aur gan y frenhines, a phan âi’r osgordd i frwydr canai iddynt Unbennaeth Prydain. Dim ond tair diod a gâi’r hebogydd yn y neuadd, rhag i hebogau’r brenin gael eu hesgeuluso er mwyn y medd.",
  ]),

 dict(id="galanas", en="Galanas: payment instead of revenge", cy="Galanas: tâl yn lle dial", figs=[],
  pEn=[
   "At the heart of the law was a simple and powerful idea. When one person killed another, the dead person’s family was not left to take revenge, and a feud was not left to run on for generations. Instead the killer and his kindred paid galanas, a blood-price, to the kindred of the dead. Once it was paid, the dead person’s family gave up the right to vengeance. A killing became a debt that two families settled together.",
   "The kindred shared the cost, out to distant cousins, and each cousin paid his part and each cousin of the dead received his. The father’s side of the family paid two shares and the mother’s side one. The killer paid his own share too. A killing from ambush cost double. Only the worst crime of all, killing by poison, was punished with death.",
   "The price depended on the standing of the person killed, and it was reckoned in cattle, the wealth of Wales:",
   "|| A free-born Welshman | 63 cows, with three augmentations",
   "|| A nobleman without office | 126 cows, with three augmentations",
   "|| The king | three times his sarhaed, with three augmentations",
   "A man who denied a killing could clear himself on oath, but he needed three hundred men to swear with him. The law made it very hard to lie one’s way out of a killing.",
  ],
  pCy=[
   "Wrth galon y gyfraith roedd syniad syml a grymus. Pan laddai un person un arall, ni adewid teulu’r marw i ddial, ac ni adewid i alanastra redeg ymlaen am genedlaethau. Yn hytrach talai’r lladdwr a’i dylwyth alanas, pris gwaed, i dylwyth y marw. Unwaith y’i talwyd, ildiai teulu’r marw yr hawl i ddial. Daeth lladdiad yn ddyled a setlai dau deulu gyda’i gilydd.",
   "Rhannai’r tylwyth y gost, hyd at gefndryd pell, a thalai pob cefnder ei ran a derbyniai pob cefnder i’r marw ei ran yntau. Talai ochr y tad ddwy ran ac ochr y fam un. Talai’r lladdwr ei ran ei hun hefyd. Costiai lladd o gynllwyn ddwbl. Dim ond y drosedd waethaf oll, lladd drwy wenwyn, a gosbid â marwolaeth.",
   "Dibynnai’r pris ar statws y sawl a laddwyd, ac fe’i cyfrifid mewn gwartheg, cyfoeth Cymru:",
   "|| Bonheddig canhwynol, Cymro rhydd o’i enedigaeth | 63 o wartheg, gyda thri dyrchafiad",
   "|| Uchelwr heb swydd | 126 o wartheg, gyda thri dyrchafiad",
   "|| Y brenin | tair gwaith ei sarhaed, gyda thri dyrchafiad",
   "Gallai gŵr a wadai ladd glirio’i hun ar ei lw, ond roedd arno angen tri chant o wŷr i dyngu gydag ef. Gwnâi’r gyfraith hi’n anodd iawn i neb gelwyddu ei ffordd allan o ladd.",
  ]),

 dict(id="sarhaed", en="Sarhaed: the price of honour", cy="Sarhaed: pris anrhydedd", figs=["hair"],
  pEn=[
   "Sarhaed means both an insult and the payment owed for it. In the law of Wales a blow, a wound, a shove, a pulled beard or a word of shame were all wrongs against a person’s honour, and every one of them had to be paid for, according to the standing of the one who was wronged.",
   "The king’s sarhaed was the greatest of all: a hundred cows for every cantref he ruled, a rod of silver reaching from the ground to the top of his head as he sat in his chair, and a cup of gold holding a full draught for the king. Another book says a plate of gold as broad as the king’s face. The queen’s sarhaed was a third of the king’s, without the gold and silver.",
   "## Every wound had its price",
   "The books set out the worth of the body part by part, so that an injury could be paid for without a quarrel:",
   "|| A hand, a foot, an eye, a lip, a nose, or an ear that has lost its hearing | 6 cows and 120 pence each",
   "|| A finger | a cow and 20 pence",
   "|| A front tooth | 24 pence, with three augmentations",
   "|| An eyelid | a penny for every hair",
   "|| A scar on the face | more than a scar where clothes hid it",
   "A wound that showed on the face was worth more, because the shame of it was seen every day. Even the physician’s fees were set down in the law.",
  ],
  pCy=[
   "Ystyr sarhaed yw sarhad a’r tâl sy’n ddyledus amdano. Yng nghyfraith Cymru roedd ergyd, clwyf, gwthiad, tynnu barf neu air o gywilydd i gyd yn gamau yn erbyn anrhydedd person, a rhaid oedd talu am bob un ohonynt, yn ôl statws y sawl a gafodd gam.",
   "Sarhaed y brenin oedd y fwyaf oll: can buwch am bob cantref a reolai, gwialen arian yn cyrraedd o’r llawr i gorun ei ben wrth iddo eistedd yn ei gadair, a ffiol aur yn dal llond llwnc i’r brenin. Dywed llyfr arall glawr aur cyn lleted ag wyneb y brenin. Traean sarhaed y brenin oedd sarhaed y frenhines, heb yr aur a’r arian.",
   "## Roedd pris ar bob clwyf",
   "Gosodai’r llyfrau werth y corff fesul rhan, fel y gellid talu am anaf heb ffraeo:",
   "|| Llaw, troed, llygad, gwefus, trwyn, neu glust a gollodd ei chlyw | 6 buwch a 120 ceiniog yr un",
   "|| Bys | buwch ac 20 ceiniog",
   "|| Dant blaen | 24 ceiniog, gyda thri dyrchafiad",
   "|| Amrant | ceiniog am bob blewyn",
   "|| Craith ar yr wyneb | mwy na chraith lle cuddiai dillad hi",
   "Roedd clwyf a ddangosai ar yr wyneb yn werth mwy, am fod ei gywilydd i’w weld bob dydd. Roedd hyd yn oed ffioedd y meddyg wedi’u gosod yn y gyfraith.",
  ]),

 dict(id="proof", en="Oaths, sureties and witnesses", cy="Llwon, meichiau a thystion", figs=[],
  pEn=[
   "Medieval Wales had no police and no prisons. The law worked because people gave their word, and because their neighbours stood behind it.",
   "A person accused of a wrong could deny it on oath, and bring a rhaith, a group of oath-helpers, to swear that they believed him. The worse the charge, the more oath-helpers he needed: a few for a small theft, three hundred to deny a killing. A false oath was a sin before God as well as a crime before men, sworn on the relics of the saints in the church.",
   "A bargain was made safe by a mach, a surety, who promised before witnesses that the debt would be paid, and who had to make the debtor pay if he would not. Land could be pledged for four years at a time, and the pledge renewed up to three times; after sixteen years the land passed for good to the one who held it. Witnesses, gwybyddiaid, who had seen a bargain made could be called to say so before the judge.",
  ],
  pCy=[
   "Nid oedd heddlu na charchardai yng Nghymru’r Oesoedd Canol. Gweithiai’r gyfraith am fod pobl yn rhoi eu gair, ac am fod eu cymdogion yn sefyll y tu ôl iddo.",
   "Gallai person a gyhuddwyd o gam ei wadu ar ei lw, a dod â rhaith, criw o gynorthwywyr llw, i dyngu eu bod yn ei gredu. Po waethaf y cyhuddiad, mwyaf o wŷr rhaith yr oedd eu hangen: ychydig am fân ladrad, tri chant i wadu lladd. Roedd llw anudon yn bechod gerbron Duw yn ogystal â throsedd gerbron dynion, wedi’i dyngu ar greiriau’r saint yn yr eglwys.",
   "Diogelid bargen gan fach, sef mechnïydd, a addawai o flaen tystion y telid y ddyled, ac y bu’n rhaid iddo wneud i’r dyledwr dalu os gwrthodai. Gellid gwystlo tir am bedair blynedd ar y tro, ac adnewyddu’r gwystl hyd at dair gwaith; wedi un mlynedd ar bymtheg âi’r tir am byth i’r sawl a’i daliai. Gellid galw gwybyddiaid, tystion a welodd fargen yn cael ei gwneud, i ddweud hynny gerbron yr ynad.",
  ]),

 dict(id="women", en="Women and marriage", cy="Menywod a phriodas", figs=["couple"], split=True,
  pEn=[
   "The law of Hywel gave women rights that women in much of Europe would wait centuries for. A married woman of free birth could give away her own shirt, her mantle, her headcloth, her shoes and her flour and food without asking her husband. And the law said plainly that every woman was to go her own way freely.",
   "## Three gifts",
   "A bride brought three kinds of property into a marriage. Her gwaddol was her portion from her own family. The cowyll was her husband’s gift to her on the morning after the wedding, and it was hers alone. Her agweddi was the sum that was hers by right if the marriage ended in its first seven years, set according to her family’s rank.",
   "## Seven years",
   "After seven years a marriage became a partnership of equals. If the couple then parted, everything they owned was divided into two halves. The wife made the division and the husband chose, so the wife had every reason to divide fairly, and the husband could not complain. Then the law went through the household, item by item:",
   "## A wronged wife",
   "If a husband was unfaithful, the law paid his wife for the shame: six score pence the first time, a pound the second time, and the third time she could leave him and take all that was hers. She could even strike the other woman without paying for it.",
  ],
  pCy=[
   "Rhoddai cyfraith Hywel hawliau i fenywod y byddai menywod mewn llawer o Ewrop yn aros canrifoedd amdanynt. Gallai gwraig briod o waed rhydd roi ei chrys, ei mantell, ei phenlliain, ei hesgidiau a’i blawd a’i bwyd ei hun heb ofyn i’w gŵr. A dywedai’r gyfraith yn blaen fod pob gwraig i fynd ei ffordd ei hun yn rhydd.",
   "## Tair rhodd",
   "Dôi priodferch â thri math o eiddo i briodas. Ei gwaddol oedd ei chyfran gan ei theulu ei hun. Y cowyll oedd rhodd ei gŵr iddi ar y bore wedi’r briodas, a’i heiddo hi yn unig ydoedd. Ei hagweddi oedd y swm a oedd yn eiddo iddi o hawl pe deuai’r briodas i ben yn ei saith mlynedd cyntaf, wedi’i osod yn ôl tras ei theulu.",
   "## Saith mlynedd",
   "Wedi saith mlynedd daeth priodas yn bartneriaeth gyfartal. Pe gwahanai’r pâr wedyn, rhennid popeth a feddent yn ddau hanner. Y wraig a rannai a’r gŵr a ddewisai, felly roedd gan y wraig bob rheswm i rannu’n deg, ac ni allai’r gŵr gwyno. Yna âi’r gyfraith drwy’r aelwyd, fesul eitem:",
   "## Gwraig a gafodd gam",
   "Pe bai gŵr yn anffyddlon, talai’r gyfraith i’w wraig am y cywilydd: chweugain y tro cyntaf, punt yr ail dro, a’r trydydd tro gallai ei adael a chymryd y cyfan a oedd yn eiddo iddi. Gallai hyd yn oed daro’r wraig arall heb dalu amdano.",
  ]),

 dict(id="land", en="Children, family and land", cy="Plant, teulu a thir", figs=[],
  pEn=[
   "In Hywel’s Wales the family, the kindred, stood behind every person. It paid for their wrongs and was paid for the wrongs done to them, and it held the land together.",
   "## Every son a share",
   "When a free man died, his land was not handed whole to his eldest son, as in England. It went to all his sons, in equal shares. This was cyfran. The youngest son made the division and his brothers chose in turn, so the youngest had every reason to divide fairly. The youngest also kept the family home, the chief homestead with eight erwau, Welsh acres, and the buildings with it.",
   "A son born outside marriage had the same right to a share as his brothers, once his father acknowledged him. In the law of Wales a child did not pay for the way he came into the world. A son could claim the land his father had held by dadannudd, a claim to his father’s hearth and holding, and a family that had held its land through four generations became its rightful owners, priodorion, with a claim that could not be taken away.",
   "Cyfran outlived the princes, and in places even the Acts of Union. Gentry families in the north were still sharing out land by the old Welsh rules in the fifteen hundreds.",
  ],
  pCy=[
   "Yng Nghymru Hywel safai’r teulu, y tylwyth, y tu ôl i bob person. Talai am eu camweddau a chael ei dalu am y camau a wnaed iddynt, a daliai’r tir ynghyd.",
   "## Cyfran i bob mab",
   "Pan fu farw gŵr rhydd, nid i’w fab hynaf yn gyfan y rhoddid ei dir, fel yn Lloegr. Âi i’w feibion i gyd, yn gyfrannau cyfartal. Hon oedd y gyfran. Y mab ieuengaf a wnâi’r rhaniad a dewisai ei frodyr yn eu tro, felly roedd gan yr ieuengaf bob rheswm i rannu’n deg. Yr ieuengaf hefyd a gadwai gartref y teulu, y prif dyddyn â’i wyth erw, a’r adeiladau gydag ef.",
   "Roedd gan fab a anwyd y tu allan i briodas yr un hawl i gyfran â’i frodyr, unwaith y’i harddelai ei dad. Yng nghyfraith Cymru ni thalai plentyn am y modd y daeth i’r byd. Gallai mab hawlio’r tir a ddaliai ei dad drwy ddadannudd, hawl i aelwyd a daliad ei dad, a deuai teulu a ddaliodd ei dir am bedair cenhedlaeth yn berchnogion cyfreithlon arno, yn briodorion, â hawl na ellid ei dwyn oddi arnynt.",
   "Goroesodd y gyfran y tywysogion, ac mewn mannau hyd yn oed y Deddfau Uno. Roedd teuluoedd bonedd yn y gogledd yn dal i rannu tir yn ôl yr hen reolau Cymreig yn yr unfed ganrif ar bymtheg.",
  ]),

 dict(id="mercy", en="Bread for the hungry", cy="Bara i’r newynog", figs=[],
  pEn=[
   "One rule of the law is remembered above all the others. A person in need who had walked through three townships in a day, and called at nine houses in every township, and been given neither food nor shelter, and who then took food to keep alive, was not to be hanged or punished as a thief.",
   "A thousand years ago the law of Wales would not make hunger a crime. The shame of it fell on the twenty-seven houses that had turned a hungry person from the door.",
  ],
  pCy=[
   "Cofir un rheol o’r gyfraith yn anad yr un arall. Ni chrogid ac ni chosbid fel lleidr y sawl mewn angen a gerddodd drwy dair tref mewn diwrnod, a galw mewn naw tŷ ym mhob tref, heb gael na bwyd na lloches, ac a gymerodd fwyd wedyn i aros yn fyw.",
   "Fil o flynyddoedd yn ôl ni wnâi cyfraith Cymru drosedd o newyn. Syrthiai’r cywilydd ar y saith tŷ ar hugain a drodd y newynog o’r drws.",
  ]),

 dict(id="worth", en="The worth of everything", cy="Gwerth pob peth", figs=["cat"], worth=True,
  pEn=[
   "So that any loss could be paid for fairly, the law set a value on almost everything a household might own: animals, tools, trees, houses, and every part of a beast. A buyer was protected too. Each animal had its teithi, the qualities it was meant to have, and if it lacked one the seller paid part of the price back. A cat, for example, had to be perfect of ear, eye, tail, teeth and claw, catch mice, and not eat its kittens.",
   "And the cat that guarded the king’s barn was worth more again. If anyone killed it, the cat was held by its tail with its nose to the floor, and the killer poured wheat over it until the tip of its tail was hidden. That heap of grain was the price.",
   "> The origin of bees is from paradise; and because of the sin of man they came thence, and God conferred his grace on them; and therefore the mass cannot be sung without the wax. | The Laws of Hywel Dda, on the worth of bees",
  ],
  pCy=[
   "Fel y gellid talu’n deg am unrhyw golled, rhoddai’r gyfraith werth ar bron bopeth a allai fod gan aelwyd: anifeiliaid, offer, coed, tai, a phob rhan o anifail. Diogelid y prynwr hefyd. Roedd gan bob anifail ei deithi, y rhinweddau y dylai eu bod ganddo, ac os oedd un yn eisiau talai’r gwerthwr ran o’r pris yn ôl. Rhaid oedd i gath, er enghraifft, fod yn berffaith ei chlust, ei llygad, ei chynffon, ei dannedd a’i hewinedd, lladd llygod, a pheidio â bwyta’i chathod bach.",
   "Ac roedd y gath a warchodai ysgubor y brenin yn werth mwy eto. Pe lladdai rhywun hi, delid y gath gerfydd ei chynffon â’i thrwyn at y llawr, a thywalltai’r lladdwr wenith drosti nes cuddio blaen ei chynffon. Y twr hwnnw o ŷd oedd y pris.",
   "> O baradwys y mae bonedd gwenyn; ac oherwydd pechod dyn y daethant oddi yno, a rhoddodd Duw ei ras arnynt; ac am hynny ni ellir canu’r offeren heb y cwyr. | Cyfraith Hywel Dda, am werth gwenyn",
  ]),

 dict(id="manuscripts", en="The books that survive", cy="Y llyfrau sydd wedi goroesi", figs=[], gallery=True,
  pEn=[
   "About forty manuscripts of the law have come down to us, most of them small, plain books made to be carried to court and used, not to sit on a shelf. Many are worn from use, with notes squeezed into the margins by lawyers adding the cases of their own day. Most are kept in the National Library of Wales at Aberystwyth, where the Peniarth manuscripts were added to UNESCO’s UK Memory of the World register in 2010.",
   "The oldest are from the middle of the thirteenth century. The Black Book of Chirk, Peniarth 29, is the oldest copy of the law in Welsh and one of the oldest books of Welsh prose in the world. Peniarth 28, a Latin copy of about the same age, is famous for its little pen drawings of the people of the law: the king on his throne, the judge, the falconer, the steward, a married couple, and men quarrelling. In 2012 the National Library brought home the Boston manuscript, a pocket lawbook of Dyfed from the fourteenth century that had spent more than 150 years in the care of the Massachusetts Historical Society in America.",
  ],
  pCy=[
   "Mae tua deugain llawysgrif o’r gyfraith wedi dod i lawr atom, y rhan fwyaf yn llyfrau bach plaen a wnaed i’w cario i’r llys a’u defnyddio, nid i eistedd ar silff. Mae llawer wedi’u treulio gan ddefnydd, â nodiadau wedi’u gwasgu i’r ymylon gan gyfreithwyr yn ychwanegu achosion eu dydd eu hunain. Cedwir y rhan fwyaf yn Llyfrgell Genedlaethol Cymru yn Aberystwyth, lle ychwanegwyd llawysgrifau Peniarth at gofrestr Cof y Byd UNESCO yn y DU yn 2010.",
   "Daw’r rhai hynaf o ganol y drydedd ganrif ar ddeg. Llyfr Du’r Waun, Peniarth 29, yw’r copi hynaf o’r gyfraith yn Gymraeg ac un o’r llyfrau rhyddiaith Gymraeg hynaf yn y byd. Mae Peniarth 28, copi Lladin o tua’r un oed, yn enwog am ei luniau pin bach o bobl y gyfraith: y brenin ar ei orsedd, yr ynad, yr hebogydd, y distain, gŵr a gwraig, a dynion yn ffraeo. Yn 2012 daeth y Llyfrgell Genedlaethol â llawysgrif Boston adref, llyfr cyfraith poced o Ddyfed o’r bedwaredd ganrif ar ddeg a fu yng ngofal Cymdeithas Hanes Massachusetts yn America am fwy na 150 o flynyddoedd.",
  ]),

 dict(id="princes", en="Defended by the princes", cy="Wedi’i hamddiffyn gan y tywysogion", figs=[],
  pEn=[
   "The law was part of what made the Welsh a nation, and the princes of Wales defended it to the end. When Edward I tried to have a quarrel over the land of Arwystli tried under English law, Llywelyn ap Gruffudd, Prince of Wales, answered that every land under the king’s rule, Gascony, Scotland, Ireland and England, kept its own laws and customs, and that Wales should keep hers. The right of the Welsh to be judged by Welsh law was one of the causes he took up in his last war, in 1282.",
   "Even after the fall of the princes the law lived on. The Statute of Rhuddlan of 1284 brought English law for killing, theft and arson, but Welsh law for land, family, contracts and sureties carried on across the country, and in the March, Welsh courts sat into the sixteenth century. Only the Acts of Union, in 1536 and 1543, brought it to an end. The last case known to have been heard under the law of Hywel was a quarrel over land in Carmarthenshire in 1540, some six hundred years after the gathering on the Taf.",
  ],
  pCy=[
   "Roedd y gyfraith yn rhan o’r hyn a wnâi’r Cymry’n genedl, ac amddiffynnodd tywysogion Cymru hi hyd y diwedd. Pan geisiodd Edward I gael profi ffrae am dir Arwystli dan gyfraith Lloegr, atebodd Llywelyn ap Gruffudd, Tywysog Cymru, fod pob gwlad dan reolaeth y brenin, Gasgwyn, yr Alban, Iwerddon a Lloegr, yn cadw’i chyfreithiau a’i harferion ei hun, ac y dylai Cymru gadw’i rhai hithau. Roedd hawl y Cymry i’w barnu dan gyfraith Cymru yn un o’r achosion a gododd yn ei ryfel olaf, yn 1282.",
   "Hyd yn oed wedi cwymp y tywysogion parhaodd y gyfraith yn fyw. Daeth Statud Rhuddlan yn 1284 â chyfraith Lloegr i ladd, lladrata a llosgi, ond parhaodd cyfraith Cymru am dir, teulu, cytundebau a meichiau ledled y wlad, ac yn y Mers eisteddai llysoedd Cymreig hyd yr unfed ganrif ar bymtheg. Dim ond y Deddfau Uno, yn 1536 a 1543, a ddaeth â hi i ben. Yr achos olaf y gwyddys iddo gael ei glywed dan gyfraith Hywel oedd ffrae am dir yn Sir Gaerfyrddin yn 1540, tua chwe chan mlynedd wedi’r cynulliad ar y Taf.",
  ]),

 dict(id="today", en="Hywel’s law today", cy="Cyfraith Hywel heddiw", figs=["plaque", "garden"],
  pEn=[
   "The law of Hywel never left the memory of Wales. Lawyers and scholars kept copying and studying the books long after the courts stopped using them. In 1841 Aneurin Owen printed them all in Ancient Laws and Institutes of Wales, and in 1986 Dafydd Jenkins gave the world a modern translation, The Law of Hywel Dda. Today the Cyfraith Hywel project puts the words of the manuscripts online for anyone to search.",
   "At Whitland the Hywel Dda Centre and its memorial garden, designed by the artist Peter Lord, stand where tradition places the gathering. The garden has six parts, each planted with its own tree and each telling of one side of the law: society and kindred, crime and wrongs, women, contracts, property, and the king and his court. Slate plaques set with enamels show the laws in pictures. The health board of west Wales carries his name too: Hywel Dda University Health Board.",
   "And Wales makes its own laws again. In 2011 the people of Wales voted for their Senedd to make laws, and in 2012 the first Act made in Wales, in Welsh and English with equal standing, became law. More than a thousand years after the gathering on the Taf, the laws of Wales are once again made in Wales.",
  ],
  pCy=[
   "Ni adawodd cyfraith Hywel gof Cymru erioed. Daliodd cyfreithwyr ac ysgolheigion i gopïo ac astudio’r llyfrau ymhell wedi i’r llysoedd beidio â’u defnyddio. Yn 1841 argraffodd Aneurin Owen hwy i gyd yn Ancient Laws and Institutes of Wales, ac yn 1986 rhoddodd Dafydd Jenkins gyfieithiad modern i’r byd, The Law of Hywel Dda. Heddiw mae prosiect Cyfraith Hywel yn rhoi geiriau’r llawysgrifau ar-lein i unrhyw un chwilio drwyddynt.",
   "Yn Hendy-gwyn saif Canolfan Hywel Dda a’i gardd goffa, a gynlluniwyd gan yr artist Peter Lord, lle mae’r traddodiad yn gosod y cynulliad. Mae chwe rhan i’r ardd, pob un wedi’i phlannu â’i choeden ei hun a phob un yn adrodd am un wedd ar y gyfraith: cymdeithas a thylwyth, trosedd a chamweddau, menywod, cytundebau, eiddo, a’r brenin a’i lys. Mae placiau llechen ag enamel ynddynt yn dangos y cyfreithiau mewn lluniau. Mae bwrdd iechyd gorllewin Cymru’n dwyn ei enw hefyd: Bwrdd Iechyd Prifysgol Hywel Dda.",
   "Ac mae Cymru’n gwneud ei chyfreithiau ei hun unwaith eto. Yn 2011 pleidleisiodd pobl Cymru i’w Senedd wneud cyfreithiau, ac yn 2012 daeth y Ddeddf gyntaf a wnaed yng Nghymru, yn Gymraeg a Saesneg â statws cyfartal, yn gyfraith. Fwy na mil o flynyddoedd wedi’r cynulliad ar y Taf, gwneir cyfreithiau Cymru yng Nghymru unwaith eto.",
  ]),
]

# ---------- the three lawbooks (cards) ----------
BOOKS = [
 dict(cy="Llyfr Cyfnerth", en="The Book of Cyfnerth", whereEn="The border lands between the Wye and the Severn", whereCy="Y gororau rhwng Gwy a Hafren",
  tEn="The shortest of the three and, scholars think, the oldest in shape, taking form in the late twelfth century. Aneurin Owen called it the Gwentian Code. It keeps some of the simplest and most ancient law of all.",
  tCy="Y byrraf o’r tri ac, yn ôl ysgolheigion, yr hynaf ei ffurf, yn cymryd siâp yn niwedd y ddeuddegfed ganrif. Galwodd Aneurin Owen ef yn Gwentian Code. Mae’n cadw peth o’r gyfraith symlaf a hynaf oll."),
 dict(cy="Llyfr Blegywryd", en="The Book of Blegywryd", whereEn="Dyfed and Deheubarth, Hywel’s own kingdom", whereCy="Dyfed a Deheubarth, teyrnas Hywel ei hun",
  tEn="Named after Hywel’s master of law. It is the law of the south-west, shaped by learned churchmen, and Aneurin Owen called it the Dimetian Code, the code of Dyfed. The Boston manuscript is a copy of it.",
  tCy="Wedi’i enwi ar ôl athro cyfraith Hywel. Cyfraith y de-orllewin ydyw, wedi’i llunio gan wŷr eglwysig dysgedig, a galwodd Aneurin Owen ef yn Dimetian Code, cod Dyfed. Copi ohono yw llawysgrif Boston."),
 dict(cy="Llyfr Iorwerth", en="The Book of Iorwerth", whereEn="Gwynedd, in the days of Llywelyn Fawr", whereCy="Gwynedd, yn nyddiau Llywelyn Fawr",
  tEn="The fullest and most developed of the books, revised by the lawyer Iorwerth ap Madog in the first half of the thirteenth century. It contains the Judges’ Test Book. Aneurin Owen called it the Venedotian Code, the code of Gwynedd.",
  tCy="Y llawnaf a’r mwyaf datblygedig o’r llyfrau, wedi’i adolygu gan y cyfreithiwr Iorwerth ap Madog yn hanner cyntaf y drydedd ganrif ar ddeg. Ynddo y mae Llyfr Prawf Ynad. Galwodd Aneurin Owen ef yn Venedotian Code, cod Gwynedd."),
 dict(cy="Y llyfrau Lladin", en="The Latin books", whereEn="Made for churchmen and Latin-writing courts", whereCy="I wŷr eglwysig a llysoedd a ysgrifennai yn Lladin",
  tEn="Five Latin versions survive. They are not a foreign law but the law of Hywel turned into the language of the church. Peniarth 28, with its famous drawings, is the oldest of them.",
  tCy="Mae pum fersiwn Ladin wedi goroesi. Nid cyfraith estron mohonynt ond cyfraith Hywel wedi’i throi i iaith yr eglwys. Peniarth 28, â’i luniau enwog, yw’r hynaf ohonynt."),
]

# ---------- officers of the court: Welsh title, EN, CY ----------
OFFICERS = [
 ("Penteulu", "Captain of the household warband, often the king’s son or nephew.", "Capten osgordd y llys, yn aml mab neu nai’r brenin."),
 ("Offeiriad teulu", "The household priest, who received the king’s Lent garment.", "Offeiriad y llys, a gâi wisg Grawys y brenin."),
 ("Distain", "The steward, in charge of the food and drink of the court.", "Y stiward, yng ngofal bwyd a diod y llys."),
 ("Ynad llys", "The court judge, keeper of the law in the king’s presence.", "Barnwr y llys, ceidwad y gyfraith yng ngŵydd y brenin."),
 ("Hebogydd", "The falconer. Three drinks only in the hall, for the hawks’ sake.", "Yr hebogydd. Tair diod yn unig yn y neuadd, er mwyn yr hebogau."),
 ("Pengwastrawd", "The chief groom, master of the king’s horses.", "Y pen-gwastrawd, meistr meirch y brenin."),
 ("Gwas ystafell", "The chamberlain, who kept the king’s chamber.", "Gwas yr ystafell, a gadwai ystafell y brenin."),
 ("Bardd teulu", "The household bard, who sang The Sovereignty of Britain before battle.", "Bardd y llys, a ganai Unbennaeth Prydain cyn brwydr."),
 ("Gostegwr", "The silentiary, who called the hall to silence and fined the noisy.", "Y gostegwr, a alwai’r neuadd i dawelwch a dirwyo’r swnllyd."),
 ("Pencynydd", "The chief huntsman, master of the hounds.", "Y pencynydd, meistr y cŵn hela."),
 ("Meddydd", "The mead-brewer.", "Y meddydd, a fragai’r medd."),
 ("Meddyg", "The physician, who healed the household.", "Y meddyg, a iachâi bobl y llys."),
 ("Trulliad", "The butler, keeper of the drink.", "Y trulliad, ceidwad y ddiod."),
 ("Drysor", "The doorkeeper of the hall.", "Porthor drws y neuadd."),
 ("Cog", "The cook.", "Y cogydd."),
 ("Canhwyllydd", "The candle-bearer, who lit the king’s table.", "Y canhwyllydd, a oleuai fwrdd y brenin."),
 ("Troediog", "The footholder, who sat under the king’s feet at the feast and ate from the same dish.", "Y troediog, a eisteddai dan draed y brenin yn y wledd a bwyta o’r un ddysgl."),
]

# ---------- after seven years: who took what (EN left, EN right, CY left, CY right) ----------
SPLIT = [
 ("The husband", "The wife", "Y gŵr", "Y wraig"),
 ("The pigs", "The sheep", "Y moch", "Y defaid"),
 ("If only sheep and goats: the sheep", "If only sheep and goats: the goats", "Os defaid a geifr yn unig: y defaid", "Os defaid a geifr yn unig: y geifr"),
 ("One pail", "All the other milk vessels", "Un stên", "Y llestri llaeth eraill i gyd"),
 ("The drinking vessels", "The fine sieve", "Y llestri yfed", "Y gogr mân"),
 ("The upper stone of the quern", "The lower stone of the quern", "Maen uchaf y felin law", "Maen isaf y felin law"),
 ("The bedclothes underneath", "The bedclothes on top", "Y dillad gwely isaf", "Y dillad gwely uchaf"),
]

# ---------- the worth table: group EN, group CY, rows of (EN, CY, value EN, value CY) ----------
WORTH = [
 ("Animals", "Anifeiliaid", [
  ("A kitten, from birth until its eyes open", "Cath fach, o’i geni hyd nes yr agoro’i llygaid", "1 penny", "1 geiniog"),
  ("A kitten, until it has caught a mouse", "Cath fach, hyd nes y dalio lygoden", "2 pence", "2 geiniog"),
  ("A cat that catches mice", "Cath sy’n dal llygod", "4 pence", "4 ceiniog"),
  ("The cat that guards the king’s barn", "Y gath sy’n gwarchod ysgubor y brenin", "a heap of wheat to cover it", "twr o wenith i’w chuddio"),
  ("A cub of the king’s covert hound, eyes still shut", "Cenau gellgi’r brenin, a’i lygaid ynghau", "24 pence", "24 ceiniog"),
  ("A sucking lamb", "Oen sugno", "1 penny", "1 geiniog"),
  ("A piglet in its litter", "Porchell yn ei dorllwyth", "1 penny", "1 geiniog"),
  ("A hen, or a cock", "Iâr, neu geiliog", "1 small penny", "1 geiniog cwta"),
  ("The horn, eye, ear or tail of a cow", "Corn, llygad, clust neu gynffon buwch", "4 pence each", "4 ceiniog yr un"),
  ("A stud mare", "Caseg fridio", "120 pence", "120 ceiniog"),
  ("A palfrey, a riding horse", "Palffrai, march marchogaeth", "a mark, 160 pence", "marc, 160 ceiniog"),
  ("A hawk before its moult", "Hebog cyn ei folltio", "120 pence", "120 ceiniog"),
  ("A mother hive of bees", "Mam-haid o wenyn", "24 pence", "24 ceiniog"),
  ("A first swarm", "Haid gyntaf", "16 pence", "16 ceiniog"),
 ]),
 ("Honour and the body", "Anrhydedd a’r corff", [
  ("The king’s sarhaed", "Sarhaed y brenin", "100 cows for every cantref, a silver rod and a gold cup", "100 buwch am bob cantref, gwialen arian a ffiol aur"),
  ("The queen’s sarhaed", "Sarhaed y frenhines", "a third of the king’s", "traean un y brenin"),
  ("Galanas of a free-born Welshman", "Galanas bonheddig canhwynol", "63 cows", "63 o wartheg"),
  ("A hand, foot, eye, lip or nose", "Llaw, troed, llygad, gwefus neu drwyn", "6 cows and 120 pence", "6 buwch a 120 ceiniog"),
  ("A finger", "Bys", "a cow and 20 pence", "buwch ac 20 ceiniog"),
  ("A front tooth", "Dant blaen", "24 pence", "24 ceiniog"),
  ("An eyelid", "Amrant", "a penny a hair", "ceiniog y blewyn"),
 ]),
 ("Fine things", "Pethau gwych", [
  ("The king’s harp", "Telyn y brenin", "120 pence", "120 ceiniog"),
  ("The fee to become a judge in Gwynedd", "Y tâl i ddod yn ynad yng Ngwynedd", "24 pence", "24 ceiniog"),
  ("A wronged wife, the first time", "Gwraig a gafodd gam, y tro cyntaf", "120 pence", "chweugain"),
  ("A wronged wife, the second time", "Gwraig a gafodd gam, yr ail dro", "a pound, 240 pence", "punt, 240 ceiniog"),
 ]),
]

# ---------- the quiz: question EN, CY, answers [(EN, CY)], the right one (0-based), why EN, why CY ----------
QUIZ = [
 ("A man is killed in a quarrel. What does the law of Hywel ask for?", "Lleddir gŵr mewn ffrae. Beth mae cyfraith Hywel yn ei ofyn?",
  [("His family takes revenge", "Ei deulu’n dial"), ("The killer’s kindred pay galanas to his kindred", "Tylwyth y lladdwr yn talu galanas i’w dylwyth"), ("The killer is sent out of Wales", "Anfon y lladdwr allan o Gymru")], 1,
  "Galanas, the blood-price, ended the matter. Once it was paid, the dead man’s family gave up revenge.", "Galanas, y pris gwaed, a ddôi â’r mater i ben. Unwaith y’i talwyd, ildiai teulu’r marw ddial."),
 ("A starving traveller has called at nine houses in each of three townships and been given nothing. Then she takes food. What happens?", "Mae teithiwr llwglyd wedi galw mewn naw tŷ ym mhob un o dair tref heb gael dim. Yna mae hi’n cymryd bwyd. Beth sy’n digwydd?",
  [("She is hanged as a thief", "Fe’i crogir fel lleidr"), ("She pays a fine to the king", "Mae hi’n talu dirwy i’r brenin"), ("She is not punished", "Ni chosbir hi")], 2,
  "The law would not make hunger a crime. The shame fell on the houses that turned her away.", "Ni wnâi’r gyfraith drosedd o newyn. Syrthiai’r cywilydd ar y tai a’i trodd ymaith."),
 ("You buy a cat, and it will not catch mice. What can you do?", "Rydych yn prynu cath, ac nid yw’n dal llygod. Beth allwch chi ei wneud?",
  [("Nothing: a cat is a cat", "Dim: cath yw cath"), ("Claim part of your money back", "Hawlio rhan o’ch arian yn ôl"), ("Take the seller to the king", "Mynd â’r gwerthwr at y brenin")], 1,
  "Every animal had its teithi, the qualities it should have. A cat that would not catch mice was not a whole cat in law.", "Roedd gan bob anifail ei deithi, y rhinweddau y dylai eu bod ganddo. Nid oedd cath na ddaliai lygod yn gath gyfan yn y gyfraith."),
 ("Someone kills the cat that guards the king’s barn. What is the price?", "Mae rhywun yn lladd y gath sy’n gwarchod ysgubor y brenin. Beth yw’r pris?",
  [("Four pence", "Pedair ceiniog"), ("Enough wheat to bury the cat to the tip of its tail", "Digon o wenith i gladdu’r gath hyd flaen ei chynffon"), ("A new cat", "Cath newydd")], 1,
  "The cat was held up by its tail, nose to the floor, and wheat poured over it until the tail was hidden.", "Delid y gath gerfydd ei chynffon, â’i thrwyn at y llawr, a thywallt gwenith drosti nes cuddio’r gynffon."),
 ("A couple married for ten years decide to part. How is their property shared?", "Mae pâr a fu’n briod am ddeng mlynedd yn penderfynu gwahanu. Sut y rhennir eu heiddo?",
  [("The husband keeps it all", "Y gŵr sy’n cadw’r cyfan"), ("In two halves: the wife divides and the husband chooses", "Yn ddau hanner: y wraig sy’n rhannu a’r gŵr sy’n dewis"), ("The king decides", "Y brenin sy’n penderfynu")], 1,
  "After seven years a marriage was a partnership of equals. Because the wife divided, she made the halves fair.", "Wedi saith mlynedd roedd priodas yn bartneriaeth gyfartal. Am mai’r wraig a rannai, gwnâi’r haneri’n deg."),
 ("When that couple part, who takes the pigs?", "Pan wahana’r pâr hwnnw, pwy sy’n cael y moch?",
  [("The husband", "Y gŵr"), ("The wife", "Y wraig"), ("They are sold and the money shared", "Fe’u gwerthir a rhannu’r arian")], 0,
  "The pigs went to the husband and the sheep to the wife.", "Âi’r moch i’r gŵr a’r defaid i’r wraig."),
 ("A farmer dies leaving three sons. What happens to his land?", "Mae ffermwr yn marw gan adael tri mab. Beth sy’n digwydd i’w dir?",
  [("The eldest son gets it all", "Y mab hynaf sy’n cael y cyfan"), ("It is shared equally, and the youngest keeps the home", "Fe’i rhennir yn gyfartal, a’r ieuengaf sy’n cadw’r cartref"), ("It goes to the king", "Mae’n mynd i’r brenin")], 1,
  "This was cyfran. The youngest son made the division, the others chose, and the youngest kept the family homestead.", "Dyma’r gyfran. Y mab ieuengaf a wnâi’r rhaniad, dewisai’r lleill, a chadwai’r ieuengaf dyddyn y teulu."),
 ("How many drinks was the king’s falconer allowed in the hall?", "Sawl diod a ganiateid i hebogydd y brenin yn y neuadd?",
  [("Three", "Tair"), ("As many as he liked", "Cymaint ag a fynnai"), ("None at all", "Dim un")], 0,
  "Three only, so that the king’s hawks would never be neglected.", "Tair yn unig, rhag i hebogau’r brenin gael eu hesgeuluso."),
 ("Where, says the law, do bees come from?", "O ble, medd y gyfraith, y daw gwenyn?",
  [("From paradise", "O baradwys"), ("From Ireland", "O Iwerddon"), ("From the king’s garden", "O ardd y brenin")], 0,
  "Bees came from paradise, the law says, and God blessed them, so mass cannot be sung without their wax.", "O baradwys y daeth gwenyn, medd y gyfraith, a bendithiodd Duw hwy, felly ni ellir canu’r offeren heb eu cwyr."),
 ("Someone insults the queen. What is her sarhaed?", "Mae rhywun yn sarhau’r frenhines. Beth yw ei sarhaed?",
  [("The same as the king’s", "Yr un fath ag un y brenin"), ("A third of the king’s", "Traean un y brenin"), ("Nothing: only the king’s honour counts", "Dim: anrhydedd y brenin yn unig sy’n cyfrif")], 1,
  "The queen’s sarhaed was a third of the king’s, without the gold and silver.", "Traean sarhaed y brenin oedd sarhaed y frenhines, heb yr aur a’r arian."),
 ("A father acknowledges a son born outside marriage. Does that son get a share of the land?", "Mae tad yn arddel mab a anwyd y tu allan i briodas. A gaiff y mab hwnnw gyfran o’r tir?",
  [("No, never", "Na, byth"), ("Yes, the same share as his brothers", "Caiff, yr un gyfran â’i frodyr"), ("Only if the king agrees", "Dim ond os cytuna’r brenin")], 1,
  "In the law of Wales a child did not pay for the way he came into the world.", "Yng nghyfraith Cymru ni thalai plentyn am y modd y daeth i’r byd."),
 ("A galanas is due. Which side of the killer’s family pays the bigger part?", "Mae galanas yn ddyledus. Pa ochr i deulu’r lladdwr sy’n talu’r rhan fwyaf?",
  [("The father’s side: two shares to one", "Ochr y tad: dwy ran i un"), ("The mother’s side: two shares to one", "Ochr y fam: dwy ran i un"), ("The killer alone pays it all", "Y lladdwr yn unig sy’n talu’r cyfan")], 0,
  "The father’s kindred paid two shares and the mother’s kindred one, and the killer paid his own part.", "Talai tylwyth y tad ddwy ran a thylwyth y fam un, a thalai’r lladdwr ei ran ei hun."),
]

# ---------- words of the law: Welsh word, meaning EN, meaning CY, how to say it ----------
WORDS = [
 ("Cyfraith", "law", "y drefn a’r rheolau a gadwai’r wlad", "KUV-ryth"),
 ("Ynad", "a judge", "barnwr", "UN-ad"),
 ("Galanas", "the blood-price paid for a killing", "y pris gwaed a delid am ladd", "ga-LAN-ass"),
 ("Sarhaed", "an insult or injury, and the payment owed for it", "sarhad neu anaf, a’r tâl sy’n ddyledus amdano", "SAR-hyed"),
 ("Dirwy", "a heavy fine paid to the king or lord", "dirwy drom a delid i’r brenin neu’r arglwydd", "DEER-wee"),
 ("Camlwrw", "a lighter fine paid to the king or lord", "dirwy ysgafnach a delid i’r brenin neu’r arglwydd", "kam-LOO-roo"),
 ("Tylwyth", "the kindred, the wider family", "y teulu estynedig", "TUL-with"),
 ("Cyfran", "the sharing of land among all the sons", "rhannu tir rhwng y meibion i gyd", "KUV-ran"),
 ("Gwaddol", "a bride’s portion from her family", "cyfran priodferch gan ei theulu", "GWA-thol (th as in ‘this’)"),
 ("Cowyll", "the husband’s gift to his wife the morning after the wedding", "rhodd y gŵr i’w wraig fore trannoeth y briodas", "KOW-ihl"),
 ("Agweddi", "a wife’s due if the marriage ended within seven years", "hawl gwraig pe deuai’r briodas i ben o fewn saith mlynedd", "ag-WETH-ee (th as in ‘this’)"),
 ("Mach", "a surety, who guaranteed a debt", "mechnïydd, a warantai ddyled", "MAHKH (ch as in ‘loch’)"),
 ("Rhaith", "a group of oath-helpers", "criw o gynorthwywyr llw", "HRYTH"),
 ("Teithi", "the qualities an animal ought to have", "y rhinweddau y dylai anifail eu bod ganddo", "TAY-thee"),
 ("Edling", "the heir to the throne", "etifedd yr orsedd", "ED-ling"),
 ("Penteulu", "captain of the king’s household warband", "capten osgordd y brenin", "pen-TAY-lee"),
 ("Cantref", "a hundred townships, a district of Wales", "can tref, un o ardaloedd Cymru", "KAN-trev"),
 ("Cwmwd", "a commote, half a cantref", "hanner cantref", "KOO-mood"),
]

SOURCES_EN = "Sources: the lawbooks in translation (Aneurin Owen, Ancient Laws and Institutes of Wales, 1841; Dafydd Jenkins, The Law of Hywel Dda, 1986); the Dictionary of Welsh Biography (Blegywryd); the National Library of Wales; the Hywel Dda Centre, Whitland. Values differ a little from one lawbook to another; we give one version."
SOURCES_CY = "Ffynonellau: y llyfrau cyfraith mewn cyfieithiad (Aneurin Owen, Ancient Laws and Institutes of Wales, 1841; Dafydd Jenkins, The Law of Hywel Dda, 1986); y Bywgraffiadur Cymreig (Blegywryd); Llyfrgell Genedlaethol Cymru; Canolfan Hywel Dda, Hendy-gwyn. Mae’r gwerthoedd yn amrywio ychydig o un llyfr cyfraith i’r llall; rhoddwn un fersiwn."
