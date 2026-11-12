"""Further reading and references for every long read (story-*.html) and for Wales in 10 minutes.

Each list is a short, real reading list for teachers, students and anyone who wants to go further:
the old texts the story rests on, and the historians' books that tell it in full.

RULES (see EDITORIAL.md, "References"):
- Only cite works that really exist, with the right author, title, publisher and year. Never invent one.
  If unsure of a publisher or year, leave that part out rather than guess.
- Titles stay as published. The note under each one has an English and a Welsh version.
- A new long read needs an entry here: build.py prints a warning when one is missing.

Item: (kind, author, title, details, note_en, note_cy[, url])
  kind "p" = an old text or record (primary source), "b" = a book by a historian, "w" = online.
dwb: person ids whose Dictionary of Welsh Biography article is linked (from source_links.json).
"""

P, B, W = "p", "b", "w"

R_R_DAVIES_AGE = (B, "R. R. Davies", "The Age of Conquest: Wales 1063–1415", "Oxford University Press, 1991; first published 1987 as Conquest, Coexistence, and Change",
                  "The great history of the princes and of the long fight with the Normans and the English crown.",
                  "Yr hanes mawr am y tywysogion a’r frwydr hir yn erbyn y Normaniaid a choron Lloegr.")
JOHN_DAVIES = (B, "John Davies", "A History of Wales", "Penguin, revised edition 2007; first published in Welsh as Hanes Cymru, 1990",
               "The standard one-volume history of Wales, from the first people to the Senedd.",
               "Y safon mewn un gyfrol, o’r bobl gyntaf hyd at y Senedd. Ar gael yn Gymraeg fel Hanes Cymru.")
BRUT_Y_TYWYSOGYON = (P, "Thomas Jones (ed. and trans.)", "Brut y Tywysogyon, or The Chronicle of the Princes", "University of Wales Press: Peniarth MS. 20 version, 1952; Red Book of Hergest version, 1955",
                     "The Welsh chronicle of the princes, year by year, in Welsh with an English translation.",
                     "Cronicl Cymraeg y tywysogion, flwyddyn wrth flwyddyn, gyda chyfieithiad Saesneg.")
GERALD = (P, "Gerald of Wales", "The Journey through Wales and The Description of Wales", "translated by Lewis Thorpe, Penguin Classics, 1978",
          "Gerallt Gymro’s own account of his ride round Wales in 1188, and his portrait of the Welsh people.",
          "Hanes Gerallt Gymro ei hun am ei daith o amgylch Cymru yn 1188, a’i ddarlun o’r Cymry.")
NENNIUS = (P, "John Morris (ed. and trans.)", "Nennius: British History and the Welsh Annals", "Phillimore, 1980",
           "The Historia Brittonum of about 829 and the Annales Cambriae, in Latin and English.",
           "Historia Brittonum tua 829 ac Annales Cambriae, yn Lladin ac yn Saesneg.")
GEOFFREY = (P, "Geoffrey of Monmouth", "The History of the Kings of Britain", "edited by Michael D. Reeve, translated by Neil Wright, Boydell Press, 2007",
            "The best modern edition of Geoffrey’s Historia Regum Britanniae, Latin text with English translation.",
            "Yr argraffiad modern gorau o Historia Regum Britanniae Sieffre, y testun Lladin gyda chyfieithiad Saesneg.")
ADAM_USK = (P, "Edward Maunde Thompson (ed. and trans.)", "Chronicon Adae de Usk, A.D. 1377–1421", "London, second edition 1904",
            "Adam of Usk’s chronicle, which keeps the text of Owain Glyndŵr’s letters to Scotland and Ireland.",
            "Cronicl Adda o Frynbuga, sy’n cadw testun llythyrau Owain Glyndŵr at yr Alban ac Iwerddon.")
ADAM_USK_GW = (P, "Chris Given-Wilson (ed. and trans.)", "The Chronicle of Adam Usk, 1377–1421", "Clarendon Press, 1997",
               "The modern edition of the same chronicle, Latin with English on facing pages.",
               "Yr argraffiad modern o’r un cronicl, Lladin a Saesneg ochr yn ochr.")
CHARLES_EDWARDS = (B, "T. M. Charles-Edwards", "Wales and the Britons, 350–1064", "Oxford University Press, 2013",
                   "The fullest modern history of the Britons and the early Welsh kingdoms.",
                   "Yr hanes modern llawnaf am y Brythoniaid a theyrnasoedd cynnar Cymru.")
LLANDAFF = (P, "J. Gwenogvryn Evans and John Rhys (eds)", "The Text of the Book of Llan Dâv", "Oxford, 1893",
            "The Book of Llandaff, with the charters of the kings of Gwent and Glywysing.",
            "Llyfr Llandaf, gyda siarteri brenhinoedd Gwent a Glywysing.")
LLANDAFF_WD = (B, "Wendy Davies", "The Llandaff Charters", "National Library of Wales, 1979",
               "A study of every charter in the Book of Llandaff, with the kings and churches they name.",
               "Astudiaeth o bob siarter yn Llyfr Llandaf, gyda’r brenhinoedd a’r eglwysi a enwir ynddynt.")
CAESAR = (P, "Julius Caesar", "The Gallic War", "translated by Carolyn Hammond, Oxford World’s Classics, 1996",
          "Caesar’s own account of Gaul and Britain. Book 6 tells of the Druids and their schools in Britain.",
          "Hanes Cesar ei hun am Âl a Phrydain. Mae Llyfr 6 yn sôn am y derwyddon a’u hysgolion ym Mhrydain.")
SAMSON = (P, "Thomas Taylor (trans.)", "The Life of St. Samson of Dol", "SPCK, 1925",
          "The oldest Life of a Welsh saint, with its picture of Illtud and his school at Llanilltud Fawr.",
          "Y Fuchedd hynaf i un o seintiau Cymru, gyda’i darlun o Illtud a’i ysgol yn Llanilltud Fawr.")
MABINOGION = (P, "Sioned Davies (trans.)", "The Mabinogion", "Oxford World’s Classics, 2007",
              "The eleven tales, including The Dream of the Emperor Maxen, in a fine modern translation.",
              "Yr un chwedl ar ddeg, gan gynnwys Breuddwyd Macsen Wledig, mewn cyfieithiad modern gwych.")
TRIADS = (P, "Rachel Bromwich (ed. and trans.)", "Trioedd Ynys Prydein: The Triads of the Island of Britain", "University of Wales Press, fourth edition 2014; first edition 1961",
          "The Welsh Triads in Welsh and English, with notes on every name in them.",
          "Trioedd Ynys Prydain yn Gymraeg ac yn Saesneg, gyda nodiadau ar bob enw ynddynt.")
JOHNES = (B, "Martin Johnes", "Wales since 1939", "Manchester University Press, 2012",
          "Modern Wales, from the Second World War to devolution.",
          "Cymru fodern, o’r Ail Ryfel Byd hyd at ddatganoli.")
TYNGED = (P, "Saunders Lewis", "Tynged yr Iaith (The Fate of the Language)", "BBC radio lecture, 13 February 1962; printed by the BBC the same year",
          "The lecture that gave birth to Cymdeithas yr Iaith Gymraeg.",
          "Y ddarlith a esgorodd ar Gymdeithas yr Iaith Gymraeg.")
LHUYD = (P, "Edward Lhuyd", "Archaeologia Britannica, volume I: Glossography", "Oxford, 1707",
         "The book that proved Welsh, Cornish, Breton, Irish and Gaelic were one family of languages.",
         "Y llyfr a brofodd fod y Gymraeg, y Gernyweg, y Llydaweg, yr Wyddeleg a Gaeleg yr Alban yn un teulu o ieithoedd.")
CADW = (W, "Cadw", "Historic monuments in the care of Cadw", "cadw.gov.wales",
        "Opening times, guidebooks and histories for the castles and abbeys in state care.",
        "Oriau agor, arweinlyfrau a hanes y cestyll a’r abatai yng ngofal y wladwriaeth.", "https://cadw.gov.wales/")
COFLEIN = (W, "Royal Commission on the Ancient and Historical Monuments of Wales", "Coflein, the national record of the historic environment", "coflein.gov.uk",
           "The record of every known site in Wales, with plans, photographs and reports.",
           "Cofnod o bob safle hysbys yng Nghymru, gyda chynlluniau, ffotograffau ac adroddiadau.", "https://coflein.gov.uk/")


REFS = {
    "castles": dict(dwb=["llywelyn-ap-gruffudd", "owain-glyndwr"], items=[
        (B, "John R. Kenyon", "The Medieval Castles of Wales", "University of Wales Press, 2010",
         "A guide to the castles of Wales, both Welsh and Norman, by a leading castle historian.",
         "Arweiniad i gestyll Cymru, rhai Cymreig a Normanaidd, gan un o brif haneswyr y cestyll."),
        (B, "Richard Avent", "Cestyll Tywysogion Gwynedd / Castles of the Princes of Gwynedd", "HMSO for the Welsh Office, 1983",
         "The castles the princes built: Dolwyddelan, Dolbadarn, Castell y Bere, Cricieth and more. Bilingual.",
         "Y cestyll a gododd y tywysogion: Dolwyddelan, Dolbadarn, Castell y Bere, Cricieth a mwy. Dwyieithog."),
        (B, "Arnold Taylor", "The Welsh Castles of Edward I", "Hambledon Press, 1986",
         "Master James of St George and the building of Conwy, Caernarfon, Harlech and Beaumaris.",
         "Meistr James o St George a chodi Conwy, Caernarfon, Harlech a Biwmares."),
        R_R_DAVIES_AGE, CADW, COFLEIN]),

    "language": dict(dwb=["william-morgan", "saunders-lewis"], items=[
        (P, "William Morgan (trans.)", "Y Beibl Cyssegr-lan", "London, 1588",
         "The Welsh Bible that gave the language its standard written form.",
         "Y Beibl Cymraeg a roddodd i’r iaith ei ffurf ysgrifenedig safonol."),
        (P, "Commissioners of Inquiry", "Reports of the Commissioners of Inquiry into the State of Education in Wales", "London, 1847",
         "The ‘Blue Books’ themselves, which Wales named the Treachery of the Blue Books.",
         "Y Llyfrau Gleision eu hunain, a alwodd Cymru yn Frad y Llyfrau Gleision."),
        TYNGED,
        (B, "Janet Davies", "The Welsh Language: A History", "University of Wales Press, 2014",
         "A short, clear history of Welsh from Brittonic to today.",
         "Hanes byr a chlir y Gymraeg o’r Frythoneg hyd heddiw."),
        (B, "Geraint H. Jenkins (ed.)", "The Welsh Language before the Industrial Revolution", "University of Wales Press, 1997",
         "The first volume of the Social History of the Welsh Language series.",
         "Cyfrol gyntaf cyfres Hanes Cymdeithasol yr Iaith Gymraeg."),
        (B, "Gwyneth Tyson Roberts", "The Language of the Blue Books", "University of Wales Press, 1998",
         "How the 1847 reports were written, and what they said about the Welsh and their language.",
         "Sut yr ysgrifennwyd adroddiadau 1847, a’r hyn a ddywedent am y Cymry a’u hiaith.")]),

    "hywel": dict(dwb=["hywel-dda", "rhodri-mawr"], items=[
        (P, "Dafydd Jenkins (ed. and trans.)", "The Law of Hywel Dda: Law Texts from Medieval Wales", "Gomer, 1986",
         "The laws themselves in clear English: the court, compensation, women, land and the poor.",
         "Y cyfreithiau eu hunain mewn Saesneg clir: y llys, iawndal, merched, tir a’r tlodion."),
        (P, "Aneurin Owen (ed.)", "Ancient Laws and Institutes of Wales", "London, 1841",
         "The first full printed edition of the Welsh law books.",
         "Yr argraffiad printiedig llawn cyntaf o lyfrau cyfraith Cymru."),
        (B, "Dafydd Jenkins and Morfydd E. Owen (eds)", "The Welsh Law of Women", "University of Wales Press, 1980",
         "Studies of the rights the law gave to women.",
         "Astudiaethau o’r hawliau a roddai’r gyfraith i ferched."),
        (B, "T. M. Charles-Edwards, Morfydd E. Owen and Paul Russell (eds)", "The Welsh King and his Court", "University of Wales Press, 2000",
         "The king’s household and officers as the laws describe them.",
         "Llys y brenin a’i swyddogion fel y’u disgrifir yn y cyfreithiau."),
        CHARLES_EDWARDS]),

    "coal": dict(dwb=["aneurin-bevan"], items=[
        (B, "E. D. Lewis", "The Rhondda Valleys", "Phoenix House, 1959",
         "How two quiet valleys became the most famous coalfield in the world.",
         "Sut y daeth dau gwm tawel yn faes glo enwocaf y byd."),
        (B, "Hywel Francis and David Smith", "The Fed: A History of the South Wales Miners in the Twentieth Century", "Lawrence and Wishart, 1980",
         "The miners’ union and the communities it built.",
         "Undeb y glowyr a’r cymunedau a gododd."),
        (B, "Chris Williams", "Capitalism, Community and Conflict: The South Wales Coalfield, 1898–1947", "University of Wales Press, 1998",
         "The coalfield at its height and through the hard years between the wars.",
         "Maes glo’r de ar ei anterth a thrwy’r blynyddoedd caled rhwng y rhyfeloedd."),
        (B, "Iain McLean and Martin Johnes", "Aberfan: Government and Disasters", "Welsh Academic Press, 2000",
         "The Aberfan disaster of 1966 and how the families were treated.",
         "Trychineb Aberfan yn 1966 a’r modd y triniwyd y teuluoedd."),
        (W, "Amgueddfa Cymru", "Big Pit National Coal Museum", "museum.wales",
         "Go underground with former miners at Blaenavon.",
         "Ewch dan ddaear gyda chyn-lowyr ym Mlaenafon.", "https://museum.wales/bigpit/")]),

    "protest": dict(dwb=["dic-penderyn", "john-frost"], items=[
        (B, "Gwyn A. Williams", "The Merthyr Rising", "Croom Helm, 1978",
         "The rising of 1831, the red flag and Dic Penderyn.",
         "Gwrthryfel 1831, y faner goch a Dic Penderyn."),
        (B, "David J. V. Jones", "The Last Rising: The Newport Insurrection of 1839", "Clarendon Press, 1985",
         "The Chartist march on Newport, hour by hour.",
         "Gorymdaith y Siartwyr ar Gasnewydd, awr wrth awr."),
        (B, "David Williams", "The Rebecca Riots: A Study in Agrarian Discontent", "University of Wales Press, 1955",
         "The classic history of Rebecca and her daughters.",
         "Yr hanes clasurol am Beca a’i merched."),
        (B, "David J. V. Jones", "Rebecca’s Children: A Study of Rural Society, Crime, and Protest", "Clarendon Press, 1989",
         "The farmers behind the riots and the world they lived in.",
         "Y ffermwyr y tu ôl i’r helynt a’r byd yr oeddent yn byw ynddo."),
        (B, "R. Merfyn Jones", "The North Wales Quarrymen, 1874–1922", "University of Wales Press, 1981",
         "The slate quarrymen and the great Penrhyn lock-out of 1900–03.",
         "Chwarelwyr y llechi a Streic Fawr y Penrhyn, 1900–03.")]),

    "world": dict(dwb=["michael-d-jones"], items=[
        (B, "Glyn Williams", "The Desert and the Dream: A Study of Welsh Colonization in Chubut, 1865–1915", "University of Wales Press, 1975",
         "The Welsh settlement in Patagonia, from the Mimosa onwards.",
         "Y Wladfa ym Mhatagonia, o’r Mimosa ymlaen."),
        (P, "Alan Conway (ed.)", "The Welsh in America: Letters from the Immigrants", "University of Minnesota Press, 1961",
         "The emigrants in their own words, writing home from America.",
         "Yr ymfudwyr yn eu geiriau eu hunain, yn ysgrifennu adref o America."),
        (B, "Colin Thomas", "Dreaming a City", "Y Lolfa, 2009",
         "John Hughes of Merthyr and the city he founded in Ukraine, Hughesovka, now Donetsk.",
         "John Hughes o Ferthyr a’r ddinas a sefydlodd yn Wcráin, Hughesovka, Donetsk heddiw."),
        (B, "Theodore H. Friedgut", "Iuzovka and Revolution", "Princeton University Press, two volumes, 1989 and 1994",
         "The full scholarly history of Hughesovka.",
         "Hanes ysgolheigaidd llawn Hughesovka."),
        (B, "Charlotte Williams, Neil Evans and Paul O’Leary (eds)", "A Tolerant Nation? Exploring Ethnic Diversity in Wales", "University of Wales Press, 2003",
         "The Irish, Italian, Somali, Yemeni and other communities that made their home in Wales.",
         "Y cymunedau Gwyddelig, Eidalaidd, Somalïaidd, Yemenaidd ac eraill a wnaeth eu cartref yng Nghymru.")]),

    "arthur": dict(dwb=[], items=[
        LLANDAFF, NENNIUS,
        (P, "A. O. H. Jarman (ed. and trans.)", "Aneirin: Y Gododdin, Britain’s Oldest Heroic Poem", "Gomer, 1988",
         "The poem with the line ‘though he was no Arthur’, in Welsh and English.",
         "Y gerdd â’r llinell ‘ceni bei ef Arthur’, yn Gymraeg ac yn Saesneg."),
        LLANDAFF_WD,
        (B, "Rachel Bromwich, A. O. H. Jarman and Brynley F. Roberts (eds)", "The Arthur of the Welsh", "University of Wales Press, 1991",
         "Arthur in the early Welsh poems, tales, triads and Lives of the saints.",
         "Arthur yn yr hen gerddi, y chwedlau, y trioedd a bucheddau’r saint."),
        (B, "Adrian Gilbert, Alan Wilson and Baram Blackett", "The Holy Kingdom", "Bantam Press, 1998",
         "The case for Arthur as a king of Gwent and Glamorgan, set out at length.",
         "Yr achos dros Arthur fel brenin Gwent a Morgannwg, wedi’i osod allan yn llawn.")]),

    "glyndwr": dict(dwb=["owain-glyndwr"], items=[
        ADAM_USK, ADAM_USK_GW,
        (P, "Owain Glyndŵr", "The Pennal Letter, 31 March 1406", "the original is kept in the Archives nationales, Paris",
         "Owain’s letter to Charles VI of France, with his plan for the Church and universities of Wales.",
         "Llythyr Owain at Siarl VI o Ffrainc, gyda’i gynllun ar gyfer Eglwys a phrifysgolion Cymru."),
        (B, "R. R. Davies", "The Revolt of Owain Glyn Dŵr", "Oxford University Press, 1995",
         "The standard history of the war of independence and of Owain himself.",
         "Yr hanes safonol am y rhyfel annibyniaeth ac am Owain ei hun."),
        (B, "J. E. Lloyd", "Owen Glendower: Owen Glyn Dŵr", "Clarendon Press, 1931",
         "The first full modern life of Owain.",
         "Y cofiant modern llawn cyntaf i Owain."),
        (B, "Gideon Brough", "The Rise and Fall of Owain Glyn Dŵr: England, France and the Welsh Rebellion in the Late Middle Ages", "I. B. Tauris, 2017",
         "Owain’s alliance with France and the French army in Wales.",
         "Cynghrair Owain â Ffrainc a byddin Ffrainc yng Nghymru.")]),

    "longbow": dict(dwb=["gerallt-gymro", "gwenllian"], items=[
        GERALD, BRUT_Y_TYWYSOGYON,
        (B, "Robert Hardy", "Longbow: A Social and Military History", "Patrick Stephens, 1976",
         "The history of the bow from the Welsh hills to Agincourt.",
         "Hanes y bwa o fryniau Cymru i Agincourt."),
        (B, "Matthew Strickland and Robert Hardy", "The Great Warbow: From Hastings to the Mary Rose", "Sutton, 2005",
         "The fullest history of the longbow, with the evidence of the bows found on the Mary Rose.",
         "Hanes llawnaf y bwa hir, gyda thystiolaeth y bwâu a gafwyd ar y Mary Rose.")]),

    "learning": dict(dwb=["illtud", "samson", "cadog", "dewi-sant", "asser"], items=[
        CAESAR,
        (P, "Tacitus", "The Annals of Imperial Rome", "translated by Michael Grant, Penguin Classics",
         "Book 14 tells of the Roman attack on Môn and its Druids in AD 60.",
         "Mae Llyfr 14 yn sôn am ymosodiad Rhufain ar Fôn a’i derwyddon yn OC 60."),
        SAMSON,
        (P, "Bede", "Ecclesiastical History of the English People", "translated by Leo Sherley-Price, Penguin Classics",
         "Book 2, chapter 2, describes the great monastery of Bangor Is-coed.",
         "Mae Llyfr 2, pennod 2, yn disgrifio mynachlog fawr Bangor Is-coed."),
        (P, "Simon Keynes and Michael Lapidge (trans.)", "Alfred the Great: Asser’s Life of King Alfred and Other Contemporary Sources", "Penguin Classics, 1983",
         "Asser of St Davids in his own words, at the court of King Alfred.",
         "Asser o Dyddewi yn ei eiriau ei hun, yn llys y Brenin Alffred."),
        (B, "Miranda Aldhouse-Green", "Caesar’s Druids: Story of an Ancient Priesthood", "Yale University Press, 2010",
         "What the ancient writers and archaeology tell us of the Druids.",
         "Yr hyn a ddywed yr hen awduron a’r archaeoleg wrthym am y derwyddon."),
        (B, "E. L. Ellis", "The University College of Wales, Aberystwyth, 1872–1972", "University of Wales Press, 1972",
         "The college the people of Wales paid for in pennies.",
         "Y coleg a dalwyd amdano â cheiniogau pobl Cymru.")]),

    "unconquered": dict(dwb=["rhodri-mawr", "llywelyn-ap-gruffudd", "owain-glyndwr"], items=[
        BRUT_Y_TYWYSOGYON, GERALD,
        (B, "J. E. Lloyd", "A History of Wales from the Earliest Times to the Edwardian Conquest", "Longmans, two volumes, 1911",
         "The founding modern history of independent Wales.",
         "Sylfaen yr hanes modern am Gymru annibynnol."),
        R_R_DAVIES_AGE,
        (B, "K. L. Maund", "Ireland, Wales and England in the Eleventh Century", "Boydell Press, 1991",
         "The Welsh kings, the Norse of Dublin and the English in the century of the Conquest.",
         "Brenhinoedd Cymru, Llychlynwyr Dulyn a’r Saeson yng nghanrif y Goncwest."),
        (B, "Mark Redknap", "Vikings in Wales: An Archaeological Quest", "National Museums and Galleries of Wales, 2000",
         "What the ground tells us of the Northmen in Wales.",
         "Yr hyn a ddywed y tir wrthym am y Llychlynwyr yng Nghymru.")]),

    "firsts": dict(dwb=["robert-recorde", "william-jones", "william-grove", "alfred-russel-wallace", "pryce-pryce-jones", "robert-owen", "aneurin-bevan"], items=[
        (P, "Robert Recorde", "The Whetstone of Witte", "London, 1557",
         "The book in which the equals sign first appears.",
         "Y llyfr lle mae’r arwydd hafal yn ymddangos gyntaf."),
        (P, "William Jones", "Synopsis Palmariorum Matheseos", "London, 1706",
         "The book in which π is first used for the circle.",
         "Y llyfr lle defnyddir π am y cylch am y tro cyntaf."),
        (P, "Alfred Russel Wallace", "My Life: A Record of Events and Opinions", "Chapman and Hall, 1905",
         "Wallace’s own story, from Usk to the theory of natural selection.",
         "Stori Wallace ei hun, o Frynbuga i ddamcaniaeth detholiad naturiol."),
        (B, "Gareth Roberts and Fenny Smith (eds)", "Robert Recorde: The Life and Times of a Tudor Mathematician", "University of Wales Press, 2012",
         "The man from Tenby who gave the world the equals sign.",
         "Y gŵr o Ddinbych-y-pysgod a roddodd yr arwydd hafal i’r byd."),
        (P, "National Assembly for Wales", "Well-being of Future Generations (Wales) Act 2015", "legislation.gov.uk",
         "The law that made Wales the first country to protect future generations.",
         "Y gyfraith a wnaeth Gymru y wlad gyntaf i warchod cenedlaethau’r dyfodol.", "https://www.legislation.gov.uk/anaw/2015/2/contents")]),

    "brittany": dict(dwb=["samson", "illtud", "harri-tudur"], items=[
        MABINOGION,
        (P, "Brynley F. Roberts (ed.)", "Breudwyt Maxen Wledic", "Dublin Institute for Advanced Studies, 2005",
         "The Welsh text of the Dream of Macsen Wledig, with notes.",
         "Testun Cymraeg Breuddwyd Macsen Wledig, gyda nodiadau."),
        SAMSON,
        (B, "Nora K. Chadwick", "Early Brittany", "University of Wales Press, 1969",
         "The Britons who crossed the sea and the saints who went with them.",
         "Y Brythoniaid a groesodd y môr a’r seintiau a aeth gyda hwy."),
        (B, "Léon Fleuriot", "Les origines de la Bretagne", "Payot, 1980",
         "The great Breton scholar on how Brittany was founded from Britain.",
         "Yr ysgolhaig mawr o Lydaw ar sut y sefydlwyd Llydaw o Brydain.")]),

    "revival": dict(dwb=["gwynfor-evans", "saunders-lewis", "ifan-ab-owen-edwards"], items=[
        TYNGED,
        (P, "Gwynfor Evans", "Land of My Fathers: 2000 Years of Welsh History", "1974; first published in Welsh as Aros Mae, 1971",
         "The history of Wales as Gwynfor himself told it.",
         "Hanes Cymru fel yr adroddodd Gwynfor ef ei hun."),
        (B, "Rhys Evans", "Gwynfor: Portrait of a Patriot", "Y Lolfa, 2008; first published in Welsh as Rhag Pob Brad, 2005",
         "The full life of Gwynfor Evans, from Barry to the fast for S4C.",
         "Cofiant llawn Gwynfor Evans, o’r Barri i’r ympryd dros S4C."),
        (B, "D. Hywel Davies", "The Welsh Nationalist Party, 1925–1945: A Call to Nationhood", "University of Wales Press, 1983",
         "The early years of Plaid Cymru, from Pwllheli to Penyberth and beyond.",
         "Blynyddoedd cynnar Plaid Cymru, o Bwllheli i Benyberth a thu hwnt."),
        (B, "Laura McAllister", "Plaid Cymru: The Emergence of a Political Party", "Seren, 2001",
         "The story of the party from 1925 to devolution.",
         "Hanes y blaid o 1925 hyd at ddatganoli."),
        JOHNES]),

    "iolo": dict(dwb=["iolo-morganwg"], items=[
        (P, "Edward Williams (Iolo Morganwg)", "Poems, Lyric and Pastoral", "London, two volumes, 1794",
         "Iolo’s English poems, with his first account of the Gorsedd of the Bards.",
         "Cerddi Saesneg Iolo, gyda’i hanes cyntaf am Orsedd y Beirdd."),
        (P, "Owen Jones, Edward Williams and William Owen Pughe (eds)", "The Myvyrian Archaiology of Wales", "London, three volumes, 1801–07",
         "The great printed treasury of early Welsh poetry and prose that Iolo helped to make.",
         "Y drysorfa brintiedig fawr o hen farddoniaeth a rhyddiaith Gymraeg y bu Iolo’n helpu i’w llunio."),
        (P, "Taliesin Williams (ed.)", "Iolo Manuscripts", "Welsh Manuscripts Society, 1848",
         "A selection from Iolo’s papers, edited by his son.",
         "Detholiad o bapurau Iolo, wedi’i olygu gan ei fab."),
        (P, "Geraint H. Jenkins, Ffion Mair Jones and David Ceri Jones (eds)", "The Correspondence of Iolo Morganwg", "University of Wales Press, three volumes, 2007",
         "Iolo’s letters in full.",
         "Llythyrau Iolo yn llawn."),
        (B, "G. J. Williams", "Iolo Morganwg: y gyfrol gyntaf", "Gwasg Prifysgol Cymru, 1956",
         "The classic Welsh life of Iolo.",
         "Y cofiant Cymraeg clasurol i Iolo."),
        (B, "Geraint H. Jenkins (ed.)", "A Rattleskull Genius: The Many Faces of Iolo Morganwg", "University of Wales Press, 2005",
         "Iolo as poet, antiquary, radical, hymn writer and stonemason.",
         "Iolo fel bardd, hynafiaethydd, radical, emynydd a saer maen."),
        (B, "Geraint H. Jenkins", "Bard of Liberty: The Political Radicalism of Iolo Morganwg", "University of Wales Press, 2012",
         "Iolo the radical: liberty, the rights of man and his stand against slavery.",
         "Iolo’r radical: rhyddid, hawliau dyn a’i safiad yn erbyn caethwasiaeth."),
        (B, "Cathryn A. Charnell-White", "Bardic Circles: National, Regional and Personal Identity in the Bardic Vision of Iolo Morganwg", "University of Wales Press, 2007",
         "Iolo’s Gorsedd and the bardic tradition of Glamorgan.",
         "Gorsedd Iolo a thraddodiad barddol Morgannwg.")]),

    "wilson-blackett": dict(dwb=["iolo-morganwg"], items=[
        (B, "Alan Wilson and Baram Blackett", "Artorius Rex Discovered", "1986",
         "Their case for Athrwys ap Meurig as King Arthur.",
         "Eu hachos dros Athrwys ap Meurig fel y Brenin Arthur."),
        (B, "Adrian Gilbert, Alan Wilson and Baram Blackett", "The Holy Kingdom", "Bantam Press, 1998",
         "The whole case, from Brutus and Macsen to the two Arthurs.",
         "Yr achos cyfan, o Brutus a Macsen i’r ddau Arthur."),
        (B, "Alan Wilson and Baram Blackett", "Moses in the Hieroglyphs", "2006",
         "Their reading of ancient Egyptian writing through the old tongue of the Britons.",
         "Eu darlleniad o hen ysgrifen yr Aifft drwy hen iaith y Brythoniaid."),
        LLANDAFF,
        (P, "Peter Roberts (trans.)", "The Chronicle of the Kings of Britain", "London, 1811",
         "Brut Tysilio in English, one of the old histories the two men read.",
         "Brut Tysilio yn Saesneg, un o’r hen hanesion a ddarllenodd y ddau."),
        TRIADS]),

    "brutus": dict(dwb=["geoffrey-of-monmouth", "gerallt-gymro", "harri-tudur"], items=[
        NENNIUS, GEOFFREY,
        (P, "Sebastian Evans (trans.)", "Histories of the Kings of Britain, by Geoffrey of Monmouth", "J. M. Dent, 1904",
         "The translation quoted on this page.",
         "Y cyfieithiad a ddyfynnir ar y dudalen hon."),
        (P, "Brynley F. Roberts (ed.)", "Brut y Brenhinedd: Llanstephan MS. 1 Version", "Dublin Institute for Advanced Studies, 1971",
         "One of the oldest Welsh texts of the Brut, with an introduction on the Welsh versions.",
         "Un o destunau Cymraeg hynaf y Brut, gyda chyflwyniad i’r fersiynau Cymraeg."),
        ADAM_USK, TRIADS,
        (P, "Sir John Price", "Historiae Brytannicae Defensio", "London, 1573",
         "The Defence of the British History, Wales’s answer to Polydore Vergil.",
         "Amddiffyniad yr Hanes Brytanaidd, ateb Cymru i Polydore Vergil."),
        (P, "Theophilus Evans", "Drych y Prif Oesoedd", "Amwythig, 1716",
         "The Mirror of the First Ages, read in farmhouses across Wales for two hundred years.",
         "Y llyfr a ddarllenwyd mewn ffermdai ledled Cymru am ddau gan mlynedd."),
        (B, "T. D. Kendrick", "British Antiquity", "Methuen, 1950",
         "How the Tudors and the scholars of Wales defended the British history.",
         "Sut yr amddiffynnodd y Tuduriaid ac ysgolheigion Cymru yr hanes Brytanaidd.")]),

    "celts": dict(dwb=["edward-lhuyd", "lady-llanover"], items=[
        (P, "Julius Caesar", "The Gallic War", "translated by W. A. McDevitte and W. S. Bohn, 1869",
         "The translation quoted on this page: Celts in Gaul, Britons in Britain.",
         "Y cyfieithiad a ddyfynnir ar y dudalen hon: Celtiaid yng Ngâl, Brythoniaid ym Mhrydain."),
        (P, "George Buchanan", "Rerum Scoticarum Historia", "Edinburgh, 1582",
         "The Scottish history that first guessed at a link between the languages.",
         "Yr hanes Albanaidd a ddyfalodd gyntaf fod cysylltiad rhwng yr ieithoedd."),
        (P, "Paul-Yves Pezron", "Antiquité de la nation et de la langue des Celtes", "Paris, 1703",
         "The Breton monk’s book, four years before Lhuyd.",
         "Llyfr y mynach o Lydaw, bedair blynedd cyn Lhuyd."),
        LHUYD,
        (P, "Matthew Arnold", "On the Study of Celtic Literature", "London, 1867",
         "The lectures that spread the name from the languages to the peoples.",
         "Y darlithoedd a ledodd yr enw o’r ieithoedd i’r bobloedd."),
        (B, "Simon James", "The Atlantic Celts: Ancient People or Modern Invention?", "British Museum Press, 1999",
         "The archaeologist who showed that no ancient writer called the islanders Celts.",
         "Yr archaeolegydd a ddangosodd na alwodd unrhyw awdur hynafol bobl yr ynysoedd yn Geltiaid."),
        (B, "John Collis", "The Celts: Origins, Myths and Inventions", "Tempus, 2003",
         "How the name was made and spread, from the Greeks to the nineteenth century.",
         "Sut y crëwyd ac y lledodd yr enw, o’r Groegiaid i’r bedwaredd ganrif ar bymtheg.")]),

    "wales-in-10": dict(dwb=[], items=[
        JOHN_DAVIES,
        (B, "Gwyn A. Williams", "When Was Wales? A History of the Welsh", "Penguin, 1985",
         "A passionate, unforgettable history of the Welsh as a people.",
         "Hanes angerddol a bythgofiadwy o’r Cymry fel pobl."),
        (B, "Geraint H. Jenkins", "A Concise History of Wales", "Cambridge University Press, 2007",
         "The whole story in one short, well-illustrated book.",
         "Yr hanes cyfan mewn un llyfr byr, llawn lluniau."),
        R_R_DAVIES_AGE,
        (B, "Kenneth O. Morgan", "Rebirth of a Nation: Wales 1880–1980", "Oxford University Press and University of Wales Press, 1981",
         "Modern Wales, from the Liberal age to the eve of devolution.",
         "Cymru fodern, o oes y Rhyddfrydwyr hyd at drothwy datganoli."),
        JOHNES,
        (B, "John Davies, Nigel Jenkins, Menna Baines and Peredur I. Lynch (eds)", "The Welsh Academy Encyclopaedia of Wales", "University of Wales Press, 2008",
         "Everything Welsh from A to Z; also in Welsh as Gwyddoniadur Cymru.",
         "Popeth Cymreig o A i Y; hefyd yn Gymraeg fel Gwyddoniadur Cymru.")]),
}
