"""Further reading and references for the site's other pages: the big subject pages, the legends, the ages
(also used on every person and place page of that age), the kingdoms, the saints, the topic guides and trails.

Same rules and item format as src/refs.py (read its docstring): real works only, titles as published,
leave out any detail that could not be checked. build.py's page_refs() picks the list for each page.
"""
from refs import (P, B, W, R_R_DAVIES_AGE, JOHN_DAVIES, BRUT_Y_TYWYSOGYON, GERALD, NENNIUS, GEOFFREY, ADAM_USK,
                  CHARLES_EDWARDS, LLANDAFF, LLANDAFF_WD, CAESAR, SAMSON, MABINOGION, TRIADS, JOHNES, TYNGED, LHUYD, CADW,
                  COFLEIN, REFS, LAND_OF_MY_FATHERS)
import ylolfa as YLF   # books from Y Lolfa (ylolfa.com)

# ---------- shared items ----------
DWB = (W, "National Library of Wales", "Dictionary of Welsh Biography", "biography.wales",
       "Free lives of thousands of Welsh men and women, in English and Welsh.",
       "Bywgraffiadau rhad ac am ddim o filoedd o Gymry, yn Saesneg ac yn Gymraeg.", "https://biography.wales/")
ENCYC = (B, "John Davies, Nigel Jenkins, Menna Baines and Peredur I. Lynch (eds)", "The Welsh Academy Encyclopaedia of Wales", "University of Wales Press, 2008",
         "Everything Welsh from A to Z; also in Welsh as Gwyddoniadur Cymru.", "Popeth Cymreig o A i Y; hefyd yn Gymraeg fel Gwyddoniadur Cymru.")
GWYN_WILLIAMS = (B, "Gwyn A. Williams", "When Was Wales? A History of the Welsh", "Penguin, 1985",
                 "A passionate history of the Welsh as a people.", "Hanes angerddol o’r Cymry fel pobl.")
CONCISE = (B, "Geraint H. Jenkins", "A Concise History of Wales", "Cambridge University Press, 2007",
           "The whole story in one short, well-illustrated book.", "Yr hanes cyfan mewn un llyfr byr, llawn lluniau.")
LLOYD = (B, "J. E. Lloyd", "A History of Wales from the Earliest Times to the Edwardian Conquest", "Longmans, two volumes, 1911",
         "The founding modern history of independent Wales.", "Sylfaen yr hanes modern am Gymru annibynnol.")
WD_EMW = (B, "Wendy Davies", "Wales in the Early Middle Ages", "Leicester University Press, 1982",
          "Land, kings, church and people from Rome to the Normans.", "Tir, brenhinoedd, eglwys a phobl o Rufain hyd y Normaniaid.")
WD_POWER = (B, "Wendy Davies", "Patterns of Power in Early Wales", "Clarendon Press, 1990",
            "How the early Welsh kings ruled.", "Sut y rheolai brenhinoedd cynnar Cymru.")
MAUND = (B, "Kari Maund", "The Welsh Kings: Warriors, Warlords and Princes", "Tempus",
         "The kings of Wales from the fifth century to 1283, one by one.", "Brenhinoedd Cymru o’r bumed ganrif hyd 1283, fesul un.")
TURVEY = (B, "Roger Turvey", "The Welsh Princes, 1063–1283", "Longman, 2002",
          "The princes of Gwynedd, Powys and Deheubarth and how they ruled.", "Tywysogion Gwynedd, Powys a Deheubarth a’u dull o reoli.")
JBS = (B, "J. Beverley Smith", "Llywelyn ap Gruffudd, Prince of Wales", "University of Wales Press, 1998",
       "The great life of the last native Prince of Wales.", "Y cofiant mawr i dywysog brodorol olaf Cymru.")
REVOLT = (B, "R. R. Davies", "The Revolt of Owain Glyn Dŵr", "Oxford University Press, 1995",
          "The standard history of Owain’s war of independence.", "Yr hanes safonol am ryfel annibyniaeth Owain.")
BARTRUM_EWGT = (P, "P. C. Bartrum (ed.)", "Early Welsh Genealogical Tracts", "University of Wales Press, 1966",
                "The old pedigrees of the kings and saints of Wales, from the manuscripts.", "Hen achau brenhinoedd a seintiau Cymru, o’r llawysgrifau.")
GLANMOR = (B, "Glanmor Williams", "Recovery, Reorientation and Reformation: Wales c.1415–1642", "Clarendon Press, 1987",
           "Wales from Glyndŵr to the Civil War: the Tudors, the Acts of Union and the Welsh Bible.", "Cymru o Glyndŵr i’r Rhyfel Cartref: y Tuduriaid, y Deddfau Uno a’r Beibl Cymraeg.")
GHJ_FOUND = (B, "Geraint H. Jenkins", "The Foundations of Modern Wales: Wales 1642–1780", "Clarendon Press, 1987",
             "The age of the circulating schools, the Methodist revival and the first Welsh books for the people.", "Oes yr ysgolion cylchynol, y diwygiad Methodistaidd a’r llyfrau Cymraeg cyntaf i’r werin.")
KOM = (B, "Kenneth O. Morgan", "Rebirth of a Nation: Wales 1880–1980", "Oxford University Press and University of Wales Press, 1981",
       "Modern Wales, from the Liberal age to the eve of devolution.", "Cymru fodern, o oes y Rhyddfrydwyr hyd at drothwy datganoli.")
MERTHYR = (B, "Gwyn A. Williams", "The Merthyr Rising", "Croom Helm, 1978",
           "The rising of 1831 and the iron town that made it.", "Gwrthryfel 1831 a’r dref haearn a’i creodd.")
RHONDDA = (B, "E. D. Lewis", "The Rhondda Valleys", "Phoenix House, 1959",
           "How two quiet valleys became the most famous coalfield in the world.", "Sut y daeth dau gwm tawel yn faes glo enwocaf y byd.")
AH_JOHN = (B, "A. H. John", "The Industrial Development of South Wales, 1750–1850", "University of Wales Press, 1950",
           "Iron, copper and coal in the first industrial century.", "Haearn, copr a glo yn y ganrif ddiwydiannol gyntaf.")
IGJ = (B, "Ieuan Gwynedd Jones", "Explorations and Explanations: Essays in the Social History of Victorian Wales", "Gomer, 1981",
       "Chapel, politics and community in Victorian Wales.", "Capel, gwleidyddiaeth a chymdeithas yng Nghymru oes Victoria.")
QUARRY = (B, "R. Merfyn Jones", "The North Wales Quarrymen, 1874–1922", "University of Wales Press, 1981",
          "The slate quarrymen and the great Penrhyn lock-out.", "Chwarelwyr y llechi a Streic Fawr y Penrhyn.")
FED = (B, "Hywel Francis and David Smith", "The Fed: A History of the South Wales Miners in the Twentieth Century", "Lawrence and Wishart, 1980",
       "The miners’ union and the communities it built.", "Undeb y glowyr a’r cymunedau a gododd.")
PREHIST = (B, "Frances Lynch, Stephen Aldhouse-Green and Jeffrey L. Davies", "Prehistoric Wales", "Sutton, 2000",
           "Wales from the first hunters to the coming of Rome.", "Cymru o’r helwyr cyntaf hyd at ddyfodiad Rhufain.")
ROMAN_FR = (B, "Barry C. Burnham and Jeffrey L. Davies (eds)", "Roman Frontiers in Wales and the Marches", "Royal Commission on the Ancient and Historical Monuments of Wales, 2010",
            "Every Roman fort, road and camp in Wales, with plans and photographs.", "Pob caer, ffordd a gwersyll Rhufeinig yng Nghymru, gyda chynlluniau a ffotograffau.")
TACITUS_ANN = (P, "Tacitus", "The Annals of Imperial Rome", "translated by Michael Grant, Penguin Classics",
               "Caratacus before Claudius (Book 12) and the attack on Môn (Book 14).", "Caradog gerbron Clawdiws (Llyfr 12) a’r ymosodiad ar Fôn (Llyfr 14).")
TACITUS_AGR = (P, "Tacitus", "Agricola", "translated by H. Mattingly, Penguin Classics",
               "The Roman governor who conquered the Ordovices and took Môn in AD 77.", "Y llywodraethwr Rhufeinig a orchfygodd yr Ordofigiaid ac a gipiodd Fôn yn OC 77.")
GILDAS = (P, "Michael Winterbottom (ed. and trans.)", "Gildas: The Ruin of Britain and Other Works", "Phillimore, 1978",
          "The oldest book by a Briton, written in the sixth century.", "Y llyfr hynaf gan Frython, a ysgrifennwyd yn y chweched ganrif.")
HENKEN = (B, "Elissa R. Henken", "Traditions of the Welsh Saints", "D. S. Brewer, 1987",
          "The saints of Wales as the Lives, poems and local traditions remember them.", "Seintiau Cymru fel y’u cofir yn y bucheddau, y cerddi a’r traddodiadau lleol.")
BARING = (B, "S. Baring-Gould and John Fisher", "The Lives of the British Saints", "Honourable Society of Cymmrodorion, four volumes, 1907–13",
          "Hundreds of saints of Wales, Cornwall and Brittany, with their churches and wells.", "Cannoedd o seintiau Cymru, Cernyw a Llydaw, gyda’u heglwysi a’u ffynhonnau.")
WADE_EVANS = (P, "A. W. Wade-Evans (ed. and trans.)", "Vitae Sanctorum Britanniae et Genealogiae", "University of Wales Press, 1944",
              "The Latin Lives of Cadog, Illtud, Padarn, Gwynllyw and other saints, with English.", "Bucheddau Lladin Cadog, Illtud, Padarn, Gwynllyw a seintiau eraill, gyda Saesneg.")
ST_DAVID = (B, "J. Wyn Evans and Jonathan M. Wooding (eds)", "St David of Wales: Cult, Church and Nation", "Boydell Press, 2007",
            "Dewi Sant, with Rhygyfarch’s Life of St David in Latin and English.", "Dewi Sant, gyda Buchedd Dewi gan Rhygyfarch yn Lladin ac yn Saesneg.")
LAW_JENKINS = (P, "Dafydd Jenkins (ed. and trans.)", "The Law of Hywel Dda: Law Texts from Medieval Wales", "Gomer, 1986",
               "The laws themselves in clear English.", "Y cyfreithiau eu hunain mewn Saesneg clir.")
LAW_WOMEN = (B, "Dafydd Jenkins and Morfydd E. Owen (eds)", "The Welsh Law of Women", "University of Wales Press, 1980",
             "The rights the law gave to women.", "Yr hawliau a roddai’r gyfraith i ferched.")
SDAVIES_4B = (B, "Sioned Davies", "The Four Branches of the Mabinogi", "Gomer, 1993",
              "A guide to how the Four Branches were told and what they mean.", "Arweiniad i sut yr adroddwyd y Pedair Cainc a’u hystyr.")
PEDEIR = (P, "Ifor Williams (ed.)", "Pedeir Keinc y Mabinogi", "Gwasg Prifysgol Cymru, 1930",
          "The Welsh text of the Four Branches, with notes.", "Testun Cymraeg y Pedair Cainc, gyda nodiadau.")
GANTZ = (P, "Jeffrey Gantz (trans.)", "The Mabinogion", "Penguin Classics, 1976",
         "A widely read English translation.", "Cyfieithiad Saesneg poblogaidd.")
FORD = (P, "Patrick K. Ford (trans.)", "The Mabinogi and Other Medieval Welsh Tales", "University of California Press, 1977",
        "The Four Branches with the Tale of Taliesin and other stories.", "Y Pedair Cainc gyda Hanes Taliesin a chwedlau eraill.")
GUEST = (P, "Lady Charlotte Guest (trans.)", "The Mabinogion", "London and Llandovery, 1838–49",
         "The first English translation, which gave the tales their name in English.", "Y cyfieithiad Saesneg cyntaf, a roddodd i’r chwedlau eu henw Saesneg.")
RHYS_FOLK = (P, "John Rhys", "Celtic Folklore: Welsh and Manx", "Clarendon Press, two volumes, 1901",
             "Welsh folk tales gathered from the people who told them.", "Chwedlau gwerin Cymru wedi’u casglu gan y bobl a’u hadroddai.")
SIKES = (P, "Wirt Sikes", "British Goblins: Welsh Folk-lore, Fairy Mythology, Legends and Traditions", "Sampson Low, 1880",
         "A Victorian collection of the fairy lore of Wales.", "Casgliad o oes Victoria o draddodiadau’r tylwyth teg yng Nghymru.")
TREVELYAN = (P, "Marie Trevelyan", "Folk-Lore and Folk-Stories of Wales", "Elliot Stock, 1909",
             "Legends of lakes, mountains and saints from across Wales.", "Chwedlau llynnoedd, mynyddoedd a seintiau o bob rhan o Gymru.")
ELIAS_OWEN = (P, "Elias Owen", "Welsh Folk-Lore", "Woodall, Minshall and Co., 1896",
              "The folk beliefs of north Wales, collected by a country vicar.", "Coelion gwerin y gogledd, wedi’u casglu gan ficer gwlad.")
TREFOR_OWEN = (B, "Trefor M. Owen", "Welsh Folk Customs", "National Museum of Wales, 1959",
               "The customs of the Welsh year, from the Mari Lwyd to the harvest.", "Arferion blwyddyn y Cymry, o’r Fari Lwyd i’r cynhaeaf.")
LOFMARK = (B, "Carl Lofmark", "A History of the Red Dragon", "Gwasg Carreg Gwalch, 1995",
           "The red dragon from the Britons to the flag of Wales.", "Y ddraig goch o’r Brythoniaid i faner Cymru.")
BROMWICH_ARTHUR = (B, "Rachel Bromwich, A. O. H. Jarman and Brynley F. Roberts (eds)", "The Arthur of the Welsh", "University of Wales Press, 1991",
                   "Arthur in the early Welsh poems, tales, triads and Lives of the saints.", "Arthur yn yr hen gerddi, y chwedlau, y trioedd a bucheddau’r saint.")
PARRY = (B, "Thomas Parry", "A History of Welsh Literature", "translated by H. Idris Bell, Clarendon Press, 1955",
         "The classic history of Welsh writing, from the first poets to the twentieth century.", "Hanes clasurol llên Cymru, o’r beirdd cyntaf i’r ugeinfed ganrif.")
GUIDE = (B, "A. O. H. Jarman and Gwilym Rees Hughes (eds)", "A Guide to Welsh Literature", "Christopher Davies, volumes 1 and 2, 1976–79",
         "Scholars on each age of Welsh poetry and prose.", "Ysgolheigion ar bob oes o farddoniaeth a rhyddiaith Gymraeg.")
JOHNSTON = (B, "Dafydd Johnston", "The Literature of Wales", "University of Wales Press, 1994",
            "A short guide to fifteen centuries of Welsh writing.", "Arweiniad byr i bymtheg canrif o ysgrifennu Cymraeg.")
CLANCY = (P, "Joseph P. Clancy (trans.)", "Medieval Welsh Poems", "Four Courts Press, 2003",
          "The poets from Taliesin to the fifteenth century in English verse.", "Y beirdd o Daliesin i’r bymthegfed ganrif mewn barddoniaeth Saesneg.")
OXF_VERSE = (P, "Thomas Parry (ed.)", "The Oxford Book of Welsh Verse", "Clarendon Press, 1962",
             "Welsh poetry from the beginning, in Welsh.", "Barddoniaeth Gymraeg o’r dechrau, yn Gymraeg.")
GODODDIN = (P, "A. O. H. Jarman (ed. and trans.)", "Aneirin: Y Gododdin, Britain’s Oldest Heroic Poem", "Gomer, 1988",
            "The great poem of the men of Din Eidyn, in Welsh and English.", "Cerdd fawr gwŷr Din Eidyn, yn Gymraeg ac yn Saesneg.")
TALIESIN_POEMS = (P, "Ifor Williams (ed.), English version by J. E. Caerwyn Williams", "The Poems of Taliesin", "Dublin Institute for Advanced Studies, 1968",
                  "Taliesin’s poems to Urien of Rheged and his son Owain.", "Cerddi Taliesin i Urien Rheged a’i fab Owain.")
HUWS = (B, "Daniel Huws", "Medieval Welsh Manuscripts", "University of Wales Press and the National Library of Wales, 2000",
        "The great manuscripts of Wales, who wrote them and where they are now.", "Llawysgrifau mawr Cymru, pwy a’u hysgrifennodd a ble y maent heddiw.")
NLW = (W, "National Library of Wales", "Digital collections", "library.wales",
       "Many of the great manuscripts and old books can be read free online.", "Gellir darllen llawer o’r llawysgrifau mawr a’r hen lyfrau ar-lein am ddim.", "https://www.library.wales/")
BOWEN = (P, "Ivor Bowen (ed.)", "The Statutes of Wales", "T. Fisher Unwin, 1908",
         "The laws made for Wales from the Statute of Rhuddlan to the Acts of Union and after.", "Y cyfreithiau a wnaed i Gymru o Statud Rhuddlan i’r Deddfau Uno a wedyn.")
PRYCE_ACTS = (P, "Huw Pryce (ed.)", "The Acts of Welsh Rulers, 1120–1283", "University of Wales Press, 2005",
              "Every surviving charter and letter of the princes of Wales.", "Pob siarter a llythyr sydd wedi goroesi gan dywysogion Cymru.")
LITTERE = (P, "J. Goronwy Edwards (ed.)", "Littere Wallie", "University of Wales Press, 1940",
           "The treaties and letters between the princes and the English crown, including Montgomery 1267.", "Y cytundebau a’r llythyrau rhwng y tywysogion a choron Lloegr, gan gynnwys Trefaldwyn 1267.")
PLACENAMES = (B, "Hywel Wyn Owen and Richard Morgan", "Dictionary of the Place-Names of Wales", "Gomer, 2007",
              "The meaning and history of the names of towns, villages and rivers across Wales.", "Ystyr a hanes enwau trefi, pentrefi ac afonydd ledled Cymru.")
RA = REFS["firsts"]["items"]


def L(*items, dwb=()):
    return dict(dwb=list(dwb), items=list(items))


PAGES = {
    # ---------- the big subject pages ----------
    "laws": L(LAW_JENKINS,
              (P, "Aneurin Owen (ed.)", "Ancient Laws and Institutes of Wales", "London, 1841",
               "The first full printed edition of the Welsh law books.", "Yr argraffiad printiedig llawn cyntaf o lyfrau cyfraith Cymru."),
              (P, "Aled Rhys Wiliam (ed.)", "Llyfr Iorwerth", "Gwasg Prifysgol Cymru, 1960",
               "The law book of Gwynedd in Welsh.", "Llyfr cyfraith Gwynedd yn Gymraeg."),
              (P, "Stephen J. Williams and J. Enoch Powell (eds)", "Cyfreithiau Hywel Dda yn ôl Llyfr Blegywryd", "Gwasg Prifysgol Cymru, 1942",
               "The law book of the south in Welsh.", "Llyfr cyfraith y de yn Gymraeg."),
              (B, "T. M. Charles-Edwards", "The Welsh Laws", "University of Wales Press, 1989",
               "A short guide to the law books and how they grew.", "Arweiniad byr i lyfrau’r gyfraith a sut y tyfasant."),
              LAW_WOMEN,
              (B, "T. M. Charles-Edwards, Morfydd E. Owen and Paul Russell (eds)", "The Welsh King and his Court", "University of Wales Press, 2000",
               "The king’s household and officers as the laws describe them.", "Llys y brenin a’i swyddogion fel y’u disgrifir yn y cyfreithiau."),
              (B, "Huw Pryce", "Native Law and the Church in Medieval Wales", "Clarendon Press, 1993",
               "How Welsh law and the Church lived side by side.", "Sut y bu cyfraith Cymru a’r Eglwys yn cyd-fyw."),
              dwb=["hywel-dda"]),
    "mabinogion": L(MABINOGION, GANTZ, FORD, GUEST, PEDEIR,
                    (P, "Rachel Bromwich and D. Simon Evans (eds)", "Culhwch and Olwen: An Edition and Study of the Oldest Arthurian Tale", "University of Wales Press, 1992",
                     "The Welsh text of Culhwch and Olwen with a full study.", "Testun Cymraeg Culhwch ac Olwen gydag astudiaeth lawn."),
                    SDAVIES_4B, dwb=["lady-llanover"]),
    "kings": L(BARTRUM_EWGT, BRUT_Y_TYWYSOGYON, LLOYD, CHARLES_EDWARDS, MAUND, TURVEY, R_R_DAVIES_AGE, JBS,
               dwb=["rhodri-mawr", "hywel-dda", "gruffudd-ap-llywelyn", "llywelyn-fawr", "llywelyn-ap-gruffudd"]),
    "saints": L(WADE_EVANS, SAMSON, GILDAS, ST_DAVID, HENKEN, BARING, WD_EMW, YLF.PURSUIT_DAVID, YLF.DEPICTING_DAVID, YLF.SAINTS_CAME, dwb=["dewi-sant", "illtud", "cadog", "samson"]),
    "literature": L(OXF_VERSE, CLANCY, PARRY, GUIDE, JOHNSTON,
                    (P, "Gwyn Jones (ed.)", "The Oxford Book of Welsh Verse in English", "Oxford University Press, 1977",
                     "Welsh poetry in English, from the earliest poets to the twentieth century.", "Barddoniaeth Gymreig yn Saesneg, o’r beirdd cynharaf i’r ugeinfed ganrif."),
                    dwb=["taliesin", "aneirin", "dafydd-ap-gwilym", "kate-roberts", "dylan-thomas"]),
    "books": L(GODODDIN, TALIESIN_POEMS, TRIADS,
               (P, "Ifor Williams (ed.)", "Canu Aneirin", "Gwasg Prifysgol Cymru, 1938",
                "The Welsh text of Y Gododdin from the Book of Aneirin.", "Testun Cymraeg Y Gododdin o Lyfr Aneirin."),
               (P, "A. O. H. Jarman (ed.)", "Llyfr Du Caerfyrddin", "Gwasg Prifysgol Cymru, 1982",
                "The Black Book of Carmarthen in print.", "Llyfr Du Caerfyrddin mewn print."),
               HUWS, PARRY, NLW),
    "triads": L(TRIADS,
                (P, "Owen Jones, Edward Williams and William Owen Pughe (eds)", "The Myvyrian Archaiology of Wales", "London, three volumes, 1801–07",
                 "The great printed treasury of early Welsh writing, with the triads.", "Y drysorfa brintiedig fawr o hen ysgrifennu Cymraeg, gyda’r trioedd."),
                BROMWICH_ARTHUR, PARRY),
    "symbols": L(NENNIUS, MABINOGION, LOFMARK, TREFOR_OWEN,
                 (B, "Iorwerth C. Peate", "Tradition and Folk Life: A Welsh View", "Faber and Faber, 1972",
                  "The founder of St Fagans on the life and customs of Wales.", "Sylfaenydd Sain Ffagan ar fywyd ac arferion Cymru."),
                 (W, "Amgueddfa Cymru", "St Fagans National Museum of History", "museum.wales",
                  "The open-air museum of Welsh life near Cardiff.", "Amgueddfa awyr agored bywyd Cymru ger Caerdydd.", "https://museum.wales/stfagans/")),
    "firsts": REFS["firsts"],
    "castles": REFS["castles"],
    "family-trees": L(BARTRUM_EWGT,
                      (P, "P. C. Bartrum (ed.)", "Welsh Genealogies, AD 300–1400", "University of Wales Press, eight volumes, 1974",
                       "The family trees of Wales from the manuscripts, the work of a lifetime.", "Achau Cymru o’r llawysgrifau, gwaith oes."),
                      BRUT_Y_TYWYSOGYON, MAUND, TURVEY,
                      (B, "Ralph A. Griffiths and Roger S. Thomas", "The Making of the Tudor Dynasty", "Alan Sutton, 1985",
                       "The family of Penmynydd, from Ednyfed Fychan to Bosworth.", "Teulu Penmynydd, o Ednyfed Fychan i Bosworth."),
                      dwb=["rhodri-mawr", "harri-tudur"]),
    "battles": L(NENNIUS, BRUT_Y_TYWYSOGYON, GERALD, ADAM_USK, CHARLES_EDWARDS, R_R_DAVIES_AGE, REVOLT,
                 (B, "Matthew Strickland and Robert Hardy", "The Great Warbow: From Hastings to the Mary Rose", "Sutton, 2005",
                  "The longbow and the Welsh archers who made its name.", "Y bwa hir a’r saethwyr o Gymru a wnaeth ei enw.")),
    "documents": L(PRYCE_ACTS, LITTERE, BOWEN, ADAM_USK, LAW_JENKINS, R_R_DAVIES_AGE, GLANMOR, NLW),
    "towns": L(PLACENAMES,
               (B, "Ian Soulsby", "The Towns of Medieval Wales", "Phillimore, 1983",
                "How the towns of Wales began, with plans of each.", "Sut y dechreuodd trefi Cymru, gyda chynllun o bob un."),
               ENCYC, COFLEIN),
    "sites": L(CADW, COFLEIN, PREHIST, ROMAN_FR,
               (B, "John R. Kenyon", "The Medieval Castles of Wales", "University of Wales Press, 2010",
                "A guide to the castles of Wales, both Welsh and Norman.", "Arweiniad i gestyll Cymru, rhai Cymreig a Normanaidd.")),
    "maps": L((P, "John Speed", "The Theatre of the Empire of Great Britaine", "London, 1611–12",
               "Speed’s county maps of Wales, the first set to show every Welsh county.", "Mapiau sirol Speed o Gymru, y set gyntaf i ddangos pob sir yng Nghymru."),
              (B, "William Rees", "An Historical Atlas of Wales from Early to Modern Times", "Faber and Faber, 1951",
               "The history of Wales told in maps.", "Hanes Cymru wedi’i adrodd mewn mapiau."),
              (B, "Harold Carter (ed.)", "National Atlas of Wales", "University of Wales Press, 1980–89",
               "The land, people and language of Wales mapped.", "Tir, pobl ac iaith Cymru ar fapiau."),
              PLACENAMES, LLOYD),
    "welsh": L((B, "Janet Davies", "The Welsh Language: A History", "University of Wales Press, 2014",
                "A short, clear history of Welsh from Brittonic to today.", "Hanes byr a chlir y Gymraeg o’r Frythoneg hyd heddiw."),
               (B, "Gareth King", "Modern Welsh: A Comprehensive Grammar", "Routledge, third edition 2016",
                "The grammar of the Welsh people speak today.", "Gramadeg y Gymraeg a siaredir heddiw."),
               (W, "University of Wales", "Geiriadur Prifysgol Cymru", "geiriadur.ac.uk",
                "The historical dictionary of the Welsh language, free online.", "Geiriadur hanesyddol yr iaith Gymraeg, am ddim ar-lein.", "https://geiriadur.ac.uk/"),
               (W, "National Centre for Learning Welsh", "Learn Welsh", "learnwelsh.cymru",
                "Courses for adults everywhere in Wales and online.", "Cyrsiau i oedolion ym mhob rhan o Gymru ac ar-lein.", "https://learnwelsh.cymru/"),
               TYNGED),
    "names": L((B, "T. J. Morgan and Prys Morgan", "Welsh Surnames", "University of Wales Press, 1985",
                "Where Welsh surnames come from, from ap and ab to Jones and Pritchard.", "O ble y daw cyfenwau Cymreig, o ap ac ab i Jones a Pritchard."),
               PLACENAMES, BARTRUM_EWGT),
    "legends": L(MABINOGION, GUEST, RHYS_FOLK, TREVELYAN, SIKES, TRIADS),
    "general": L(JOHN_DAVIES, LAND_OF_MY_FATHERS, GWYN_WILLIAMS, CONCISE,
                 (B, "Jan Morris", "The Matter of Wales: Epic Views of a Small Country", "Oxford University Press, 1984",
                  "Wales, its history and its people, by a writer who loved them.", "Cymru, ei hanes a’i phobl, gan awdur a’u carai."),
                 ENCYC, DWB),

    # ---------- the ages; also used on every person and place page of that age ----------
    "era-ancient": L(PREHIST, CAESAR,
                     (B, "Simon James", "The Atlantic Celts: Ancient People or Modern Invention?", "British Museum Press, 1999",
                      "The Britons as the ancient writers knew them.", "Y Brythoniaid fel yr adwaenai’r hen awduron hwy."),
                     (W, "Amgueddfa Cymru", "Collections Online", "museum.wales",
                      "The treasures of the Britons, such as the Llyn Cerrig Bach hoard, in the national collection.", "Trysorau’r Brythoniaid, megis celc Llyn Cerrig Bach, yn y casgliad cenedlaethol.", "https://museum.wales/collections/online/"),
                     CADW),
    "era-roman": L(TACITUS_ANN, TACITUS_AGR, ROMAN_FR, PREHIST, CADW),
    "era-saints": L(GILDAS, NENNIUS, SAMSON, GODODDIN, CHARLES_EDWARDS, WD_EMW, HENKEN),
    "era-kings": L(NENNIUS, BRUT_Y_TYWYSOGYON, LAW_JENKINS, CHARLES_EDWARDS, WD_POWER, MAUND, LLOYD),
    "era-medieval": L(BRUT_Y_TYWYSOGYON, GERALD, PRYCE_ACTS, ADAM_USK, R_R_DAVIES_AGE, TURVEY, JBS, REVOLT, YLF.LLYWELYN_GREAT, YLF.GLYNDWR_PRINCE),
    "era-tudor": L((P, "William Morgan (trans.)", "Y Beibl Cyssegr-lan", "London, 1588",
                    "The Welsh Bible that gave the language its standard written form.", "Y Beibl Cymraeg a roddodd i’r iaith ei ffurf ysgrifenedig safonol."),
                   BOWEN, GLANMOR,
                   (B, "Ralph A. Griffiths and Roger S. Thomas", "The Making of the Tudor Dynasty", "Alan Sutton, 1985",
                    "The Welsh family that won the crown at Bosworth.", "Y teulu Cymreig a enillodd y goron yn Bosworth."),
                   GHJ_FOUND),
    "era-industrial": L(AH_JOHN, MERTHYR, RHONDDA, IGJ, QUARRY, KOM),
    "era-modern": L(KOM, JOHNES, FED,
                    (B, "John Davies", "Broadcasting and the BBC in Wales", "University of Wales Press, 1994",
                     "How Wales won a voice on radio and television.", "Sut yr enillodd Cymru lais ar y radio a’r teledu."),
                    TYNGED, YLF.TRYWERYN_DAWN, YLF.TRYWERYN_AWAKES),
    "era-today": L(JOHNES,
                   (B, "Richard Wyn Jones and Roger Scully", "Wales Says Yes: Devolution and the 2011 Welsh Referendum", "University of Wales Press, 2012",
                    "How Wales voted for law-making powers for its parliament.", "Sut y pleidleisiodd Cymru dros bwerau deddfu i’w senedd."),
                   (W, "Senedd Cymru", "The Welsh Parliament", "senedd.wales",
                    "The work and history of the Senedd.", "Gwaith a hanes y Senedd.", "https://senedd.wales/"),
                   JOHN_DAVIES),

    # ---------- kingdoms (kings-*.html); see KINGS_GROUP ----------
    "kings-north": L(GODODDIN, TALIESIN_POEMS, NENNIUS, TRIADS, BARTRUM_EWGT,
                     (B, "Tim Clarkson", "The Men of the North: The Britons of Southern Scotland", "John Donald, 2010",
                      "The British kingdoms of the Old North, from Rheged to Ystrad Clud.", "Teyrnasoedd Brythonig yr Hen Ogledd, o Reged i Ystrad Clud."),
                     CHARLES_EDWARDS),
    "kings-southeast": L(LLANDAFF, LLANDAFF_WD,
                         (B, "Wendy Davies", "An Early Welsh Microcosm: Studies in the Llandaff Charters", "Royal Historical Society, 1978",
                          "The kings, land and churches of the south-east in the Llandaff charters.", "Brenhinoedd, tir ac eglwysi’r de-ddwyrain yn siarteri Llandaf."),
                         BARTRUM_EWGT, CHARLES_EDWARDS, LLOYD),
    "kings-gwynedd": L(BRUT_Y_TYWYSOGYON, BARTRUM_EWGT, LLOYD, MAUND, TURVEY, YLF.LLYWELYN_GREAT, JBS, R_R_DAVIES_AGE),
    "kings-powys": L(BRUT_Y_TYWYSOGYON, BARTRUM_EWGT, LLOYD,
                     (B, "David Stephenson", "Medieval Powys: Kingdom, Principality and Lordships, 1132–1293", "Boydell Press, 2016",
                      "The kingdom and princes of Powys in their great age.", "Teyrnas a thywysogion Powys yn eu hoes fawr."),
                     MAUND, R_R_DAVIES_AGE),
    "kings-southwest": L(BRUT_Y_TYWYSOGYON, GERALD, BARTRUM_EWGT, LLOYD,
                         YLF.LORD_RHYS,
                         MAUND, R_R_DAVIES_AGE),
    # ---------- saints by region ----------
    "saints-llydaw": L(SAMSON, WADE_EVANS, HENKEN, BARING,
                       (B, "Nora K. Chadwick", "Early Brittany", "University of Wales Press, 1969",
                        "The Britons who crossed the sea and the saints who went with them.", "Y Brythoniaid a groesodd y môr a’r seintiau a aeth gyda hwy."),
                       dwb=["samson"]),

    # ---------- legends ----------
    "legend-arthur": L(NENNIUS, LLANDAFF, RHYS_FOLK, BROMWICH_ARTHUR, TRIADS),
    "legend-owain": L(ADAM_USK, REVOLT,
                      (B, "Elissa R. Henken", "National Redeemer: Owain Glyndŵr in Welsh Tradition", "University of Wales Press, 1996",
                       "How Wales has remembered Owain, the prince who never died.", "Sut y cofiodd Cymru Owain, y tywysog na fu farw."),
                      dwb=["owain-glyndwr"]),
    "legend-gelert": L((P, "D. E. Jenkins", "Bedd Gelert: Its Facts, Fairies, and Folk-lore", "Porthmadog, 1899",
                        "The village’s history and tales, told by a local minister.", "Hanes a chwedlau’r pentref, gan weinidog lleol."),
                       (P, "William Robert Spencer", "Beth Gêlert, or The Grave of the Greyhound", "1800",
                        "The ballad that carried the story across Britain.", "Y faled a gariodd y stori ar draws Prydain."),
                       TREVELYAN),
    "legend-twm": L((P, "T. J. Llewelyn Prichard", "The Adventures and Vagaries of Twm Shon Catti", "1828",
                     "The novel that made Twm the Welsh Robin Hood.", "Y nofel a wnaeth Twm yn Robin Hood Cymru."),
                    TREVELYAN, DWB),
    "legend-pwyll": L(MABINOGION, PEDEIR, SDAVIES_4B, GANTZ),
    "legend-branwen": L(MABINOGION, PEDEIR, SDAVIES_4B, GANTZ, TRIADS),
    "legend-manawydan": L(MABINOGION, PEDEIR, SDAVIES_4B, GANTZ),
    "legend-blodeuwedd": L(MABINOGION, PEDEIR, SDAVIES_4B, GANTZ),
    "legend-dragons": L(NENNIUS, GEOFFREY, MABINOGION, LOFMARK),
    "legend-lludd": L(MABINOGION,
                      (P, "Brynley F. Roberts (ed.)", "Cyfranc Lludd a Llefelys", "Dublin Institute for Advanced Studies",
                       "The Welsh text of the tale, with notes.", "Testun Cymraeg y chwedl, gyda nodiadau."),
                      GEOFFREY, LOFMARK),
    "legend-macsen": L(MABINOGION,
                       (P, "Brynley F. Roberts (ed.)", "Breudwyt Maxen Wledic", "Dublin Institute for Advanced Studies, 2005",
                        "The Welsh text of the Dream of Macsen Wledig, with notes.", "Testun Cymraeg Breuddwyd Macsen Wledig, gyda nodiadau."),
                       GANTZ, ROMAN_FR),
    "legend-culhwch": L(MABINOGION,
                        (P, "Rachel Bromwich and D. Simon Evans (eds)", "Culhwch and Olwen: An Edition and Study of the Oldest Arthurian Tale", "University of Wales Press, 1992",
                         "The Welsh text of Culhwch and Olwen with a full study.", "Testun Cymraeg Culhwch ac Olwen gydag astudiaeth lawn."),
                        BROMWICH_ARTHUR, GANTZ),
    "legend-dwynwen": L(HENKEN, BARING,
                        (W, "Swansea University", "Dafydd ap Gwilym: the poems", "dafyddapgwilym.net",
                         "The online edition of Dafydd’s poems, including his prayer to Dwynwen.", "Argraffiad ar-lein o gerddi Dafydd, gan gynnwys ei weddi i Ddwynwen.", "https://dafyddapgwilym.net/"),
                        TREFOR_OWEN),
    "legend-melangell": L(HENKEN, BARING, WADE_EVANS),
    "legend-gwenffrewi": L(HENKEN, BARING, TREVELYAN),
    "legend-taliesin": L((P, "Patrick K. Ford (ed.)", "Ystoria Taliesin", "University of Wales Press, 1992",
                          "The Welsh text of the Tale of Taliesin.", "Testun Cymraeg Hanes Taliesin."),
                         FORD, GUEST,
                         (P, "Marged Haycock (ed. and trans.)", "Legendary Poems from the Book of Taliesin", "CMCS Publications, 2007",
                          "The poems in Taliesin’s own voice, in Welsh and English.", "Y cerddi yn llais Taliesin ei hun, yn Gymraeg ac yn Saesneg."),
                         dwb=["taliesin"]),
    "legend-cantre": L((P, "A. O. H. Jarman (ed.)", "Llyfr Du Caerfyrddin", "Gwasg Prifysgol Cymru, 1982",
                        "The Black Book of Carmarthen, with the oldest poem on the drowned land.", "Llyfr Du Caerfyrddin, gyda’r gerdd hynaf am y tir a foddwyd."),
                       (B, "F. J. North", "Sunken Cities: Some Legends of the Coast and Lakes of Wales", "University of Wales Press, 1957",
                        "The drowned lands of Wales, legend and landscape together.", "Tiroedd boddedig Cymru, y chwedl a’r tirwedd ynghyd."),
                       RHYS_FOLK),
    "legend-llynyfan": L(RHYS_FOLK,
                         (P, "John Williams ab Ithel (ed.), translated by John Pughe", "The Physicians of Myddvai: Meddygon Myddfai", "Welsh Manuscripts Society, 1861",
                          "The remedies of the physicians descended from the Lady of the Lake.", "Meddyginiaethau’r meddygon a ddisgynnai o Arglwyddes y Llyn."),
                         SIKES),
    "legend-tylwyth": L(GERALD, RHYS_FOLK, SIKES, ELIAS_OWEN),
    "legend-afanc": L(TREVELYAN, RHYS_FOLK, SIKES),
    "legend-cadair": L(TREVELYAN, RHYS_FOLK, ELIAS_OWEN),

    # ---------- topic guides and trails ----------
    "topic-abroad": REFS["world"],
    "topic-language": REFS["language"],
    "topic-law": None,  # filled below from "laws"
    "topic-science": REFS["firsts"],
    "topic-countryside": L(
        (B, "David Jenkins", "The Agricultural Community in South-West Wales at the Turn of the Twentieth Century", "University of Wales Press, 1971",
         "Farm life in Ceredigion, from a lifetime of listening to the people.", "Bywyd fferm yng Ngheredigion, o oes o wrando ar y bobl."),
        (B, "Iorwerth C. Peate", "Tradition and Folk Life: A Welsh View", "Faber and Faber, 1972",
         "The founder of St Fagans on the life and customs of Wales.", "Sylfaenydd Sain Ffagan ar fywyd ac arferion Cymru."),
        TREFOR_OWEN, REFS["protest"]["items"][2]),
    "topic-faith": L(HENKEN,
                     (B, "Glanmor Williams", "The Welsh Church from Conquest to Reformation", "University of Wales Press, 1962",
                      "The Church in Wales in the later Middle Ages.", "Yr Eglwys yng Nghymru yn yr Oesoedd Canol diweddar."),
                     (B, "Derec Llwyd Morgan", "The Great Awakening in Wales", "Epworth Press, 1988",
                      "The Methodist revival of the eighteenth century.", "Diwygiad Methodistaidd y ddeunawfed ganrif."),
                     (B, "R. Tudur Jones", "Faith and the Crisis of a Nation: Wales 1890–1914", "University of Wales Press, 2004",
                      "Chapel Wales at its height, and the revival of 1904–05.", "Cymru’r capeli ar ei hanterth, a diwygiad 1904–05."),
                     dwb=["dewi-sant", "william-morgan", "evan-roberts"]),
    "topic-industry": L(AH_JOHN, MERTHYR,
                        (B, "Chris Evans", "‘The Labyrinth of Flames’: Work and Social Conflict in Early Industrial Merthyr Tydfil", "University of Wales Press, 1993",
                         "Merthyr in the age of iron.", "Merthyr yn oes yr haearn."),
                        RHONDDA, FED, QUARRY,
                        (B, "Jean Lindsay", "A History of the North Wales Slate Industry", "David and Charles, 1974",
                         "The quarries that roofed the world.", "Y chwareli a doodd y byd."),
                        (W, "Amgueddfa Cymru", "National Slate Museum", "museum.wales",
                         "The quarry workshops at Llanberis.", "Gweithdai’r chwarel yn Llanberis.", "https://museum.wales/slate/")),
    "topic-music": L((B, "Sally Harper", "Music in Welsh Culture before 1650: A Study of the Principal Sources", "Ashgate, 2007",
                      "The harp, the crwth and the music of the old courts.", "Y delyn, y crwth a cherddoriaeth yr hen lysoedd."),
                     (B, "Gareth Williams", "Valleys of Song: Music and Society in Wales, 1840–1914", "University of Wales Press, 1998",
                      "The choirs, chapels and eisteddfodau of industrial Wales.", "Corau, capeli ac eisteddfodau’r Gymru ddiwydiannol."),
                     (B, "Hywel Teifi Edwards", "The Eisteddfod", "University of Wales Press, 1990",
                      "A short history of the eisteddfod.", "Hanes byr yr eisteddfod."),
                     dwb=["joseph-parry"]),
    "topic-sport": L((B, "David Smith and Gareth Williams", "Fields of Praise: The Official History of the Welsh Rugby Union, 1881–1981", "University of Wales Press, 1980",
                      "A hundred years of Welsh rugby.", "Can mlynedd o rygbi yng Nghymru."),
                     (B, "Gareth Williams", "1905 and All That: Essays on Rugby Football, Sport and Welsh Society", "Gomer, 1991",
                      "The day Wales beat the All Blacks, and what sport has meant to Wales.", "Y diwrnod y curodd Cymru’r Crysau Duon, a’r hyn a olygodd chwaraeon i Gymru."),
                     (B, "Martin Johnes", "Soccer and Society: South Wales, 1900–1939", "University of Wales Press, 2002",
                      "Football in the valleys and the cities.", "Pêl-droed yn y cymoedd a’r dinasoedd.")),
    "topic-war": L(NENNIUS, BRUT_Y_TYWYSOGYON, GERALD, R_R_DAVIES_AGE, REVOLT,
                   (B, "Matthew Strickland and Robert Hardy", "The Great Warbow: From Hastings to the Mary Rose", "Sutton, 2005",
                    "The longbow and the Welsh archers who made its name.", "Y bwa hir a’r saethwyr o Gymru a wnaeth ei enw."),
                   (B, "Robin Barlow", "Wales and World War One", "Gomer, 2014",
                    "Wales at home and at the front, 1914–18.", "Cymru gartref ac yn y ffosydd, 1914–18."),
                   dwb=["hedd-wyn"]),
    "topic-women": L(LAW_WOMEN,
                     (B, "Angela V. John (ed.)", "Our Mothers’ Land: Chapters in Welsh Women’s History, 1830–1939", "University of Wales Press, 1991",
                      "Welsh women at work, at home and in politics.", "Menywod Cymru yn y gwaith, yn y cartref ac mewn gwleidyddiaeth."),
                     (B, "Deirdre Beddoe", "Out of the Shadows: A History of Women in Twentieth-Century Wales", "University of Wales Press, 2000",
                      "A century of Welsh women’s lives.", "Canrif o fywydau menywod Cymru."),
                     dwb=["gwenllian", "ann-griffiths", "cranogwen", "megan-lloyd-george"]),
    "trail-coal": REFS["coal"],
    "trail-song": None,   # same as topic-music, below
    "trail-women": None,  # same as topic-women, below
    "trail-sea": L((B, "J. Geraint Jenkins", "Maritime Heritage: The Ships and Seamen of Southern Ceredigion", "Gomer, 1982",
                    "The little ports of Cardigan Bay and the ships they built.", "Porthladdoedd bach Bae Ceredigion a’r llongau a adeiladwyd ynddynt."),
                   (B, "David Jenkins", "Shipowners of Cardiff: A Class by Themselves", "University of Wales Press, 1997",
                    "The men who made Cardiff the coal port of the world.", "Y dynion a wnaeth Gaerdydd yn borthladd glo’r byd."),
                   REFS["world"]["items"][0], YLF.WALES_SEA, ENCYC),
}
PAGES["topic-law"] = PAGES["laws"]
PAGES["trail-song"] = PAGES["topic-music"]
PAGES["trail-women"] = PAGES["topic-women"]

# kings-<realm>.html -> which list
KINGS_GROUP = {
    "efrog": "kings-north", "elfed": "kings-north", "gododdin": "kings-north", "rheged": "kings-north", "ystrad-clud": "kings-north",
    "gwent": "kings-southeast", "glywysing": "kings-southeast", "ergyng": "kings-southeast", "brycheiniog": "kings-southeast",
    "gwynedd": "kings-gwynedd", "meirionnydd": "kings-gwynedd", "rhos": "kings-gwynedd",
    "powys": "kings-powys", "gwy-a-hafren": "kings-powys",
    "deheubarth": "kings-southwest", "dyfed": "kings-southwest", "ceredigion": "kings-southwest",
}

# pages that simply get the general list
# ---------- Arthur's circle: every person page of src/arthur_circle.py except Arthur's own ----------
PAGES["arthur-circle"] = L(
    TRIADS, MABINOGION, NENNIUS, LLANDAFF, WADE_EVANS,
    (P, "A. O. H. Jarman (ed.)", "Llyfr Du Caerfyrddin", "Gwasg Prifysgol Cymru, 1982",
     "The Black Book of Carmarthen: Pa Gŵr, the Stanzas of the Graves, the elegy for Geraint and the poems of Myrddin.",
     "Llyfr Du Caerfyrddin: Pa Gŵr, Englynion y Beddau, marwnad Geraint a cherddi Myrddin."),
    (P, "Marged Haycock (ed. and trans.)", "Legendary Poems from the Book of Taliesin", "CMCS Publications, 2007",
     "The poems of the Book of Taliesin about Arthur, Uthr and the Spoils of Annwfn, in Welsh and English.",
     "Cerddi Llyfr Taliesin am Arthur, Uthr a Phreiddeu Annwfn, yn Gymraeg ac yn Saesneg."),
    (B, "Rachel Bromwich and D. Simon Evans (eds)", "Culhwch and Olwen: An Edition and Study of the Oldest Arthurian Tale", "University of Wales Press, 1992",
     "The tale with full notes on every one of Arthur’s warriors.", "Y chwedl gyda nodiadau llawn ar bob un o ryfelwyr Arthur."),
    (B, "P. C. Bartrum", "A Welsh Classical Dictionary: People in History and Legend up to about A.D. 1000", "National Library of Wales, 1993",
     "Every person of early Welsh history and story, from the pedigrees, Lives, poems and tales.", "Pob person o hanes a chwedlau cynnar Cymru, o’r achau, y bucheddau, y cerddi a’r chwedlau."),
    BROMWICH_ARTHUR, GEOFFREY,
    (B, "Adrian Gilbert, Alan Wilson and Baram Blackett", "The Holy Kingdom", "Bantam Press, 1998",
     "The case for Arthur as a king of Gwent and Glamorgan, set out at length.", "Yr achos dros Arthur fel brenin Gwent a Morgannwg, wedi’i osod allan yn llawn."))

GENERAL = {"timeline", "a-z", "questions", "onthisday", "people", "reference", "topics", "trails", "teachers", "stories", "journey"}


# ---------- more books for the Books and authors page only (not tied to one page) ----------
# keyed by the page's section ids (SHELF in build.py). Same rules: real works, details checked.
SHELF_EXTRA = {
    "start": [
        YLF.CHRONOLOGY, YLF.BRIEF_HISTORY, YLF.HIGHLIGHTS,
        (B, "Prys Morgan and David Thomas", "Wales: The Shaping of a Nation", "David and Charles, 1984",
         "How Wales became a nation, told in pictures and plain words.", "Sut y daeth Cymru’n genedl, mewn lluniau a geiriau plaen."),
        (B, "Prys Morgan (ed.)", "The Tempus History of Wales, 25,000 BC – AD 2000", "Tempus, 2001",
         "The whole story by leading historians, one age each.", "Yr hanes cyfan gan haneswyr blaenllaw, un oes yr un."),
        (B, "Wynford Vaughan-Thomas", "Wales: A History", "Michael Joseph, 1985",
         "The broadcaster’s warm and lively history of his country.", "Hanes cynnes a bywiog y darlledwr am ei wlad."),
        (B, "Norman Davies", "The Isles: A History", "Macmillan, 1999",
         "The history of these islands told so that Wales stands in its own right beside England.", "Hanes yr ynysoedd hyn wedi’i adrodd fel bod Cymru’n sefyll yn ei hawl ei hun wrth ochr Lloegr."),
    ],
    "britons": [
        (B, "Stephen Aldhouse-Green", "Paviland Cave and the ‘Red Lady’: A Definitive Report", "Western Academic and Specialist Press, 2000",
         "The oldest ceremonial burial in western Europe, on the Gower coast.", "Y gladdedigaeth seremonïol hynaf yng ngorllewin Ewrop, ar arfordir Gŵyr."),
        (B, "Miranda Aldhouse-Green and Ray Howell (eds)", "The Gwent County History, volume 1: Gwent in Prehistory and Early History", "University of Wales Press, 2004",
         "The Silures and the Britons of the south-east, to the age of the kings.", "Y Silwriaid a Brythoniaid y de-ddwyrain, hyd at oes y brenhinoedd."),
        (B, "Ray Howell", "Searching for the Silures: An Iron Age Tribe in South-East Wales", "Tempus, 2006",
         "The people of Gwent who held Rome at bay for a generation.", "Pobl Gwent a gadwodd Rufain draw am genhedlaeth."),
        (B, "Graham Webster", "Rome Against Caratacus: The Roman Campaigns in Britain, AD 48–58", "Batsford, 1981",
         "Caradog’s war against the legions in the hills of Wales.", "Rhyfel Caradog yn erbyn y llengoedd ym mryniau Cymru."),
        (B, "Barry Cunliffe", "Iron Age Communities in Britain", "Routledge, fourth edition 2005",
         "The standard work on Britain before Rome.", "Y gwaith safonol ar Brydain cyn Rhufain."),
    ],
    "kings": [
        (B, "Norman Davies", "Vanished Kingdoms: The History of Half-Forgotten Europe", "Allen Lane, 2011",
         "Opens with Alt Clud, the kingdom of the Britons on the Clyde.", "Mae’n agor ag Alt Clud, teyrnas y Brythoniaid ar afon Clud."),
        (B, "Leslie Alcock", "Arthur’s Britain: History and Archaeology, AD 367–634", "Allen Lane, 1971",
         "An archaeologist’s case for the age of Arthur, from the sources and the ground.", "Achos archaeolegydd dros oes Arthur, o’r ffynonellau a’r tir."),
        (P, "Ifor Williams (ed.), English version by Rachel Bromwich", "Armes Prydein: The Prophecy of Britain, from the Book of Taliesin", "Dublin Institute for Advanced Studies, 1972",
         "The great poem of about 930 that calls the Cymry and their allies to drive out the English.", "Y gerdd fawr tua 930 sy’n galw ar y Cymry a’u cynghreiriaid i yrru’r Saeson allan."),
        (P, "John T. Koch (ed. and trans.)", "The Gododdin of Aneirin: Text and Context from Dark-Age North Britain", "University of Wales Press, 1997",
         "Y Gododdin and the world of the Old North.", "Y Gododdin a byd yr Hen Ogledd."),
        (P, "Kenneth Hurlstone Jackson (trans.)", "The Gododdin: The Oldest Scottish Poem", "Edinburgh University Press, 1969",
         "The men of Din Eidyn in English, with a study of the poem.", "Gwŷr Din Eidyn yn Saesneg, gydag astudiaeth o’r gerdd."),
        (B, "Ken Dark", "Britain and the End of the Roman Empire", "Tempus, 2000",
         "How the Britons kept Roman ways alive in the west after 410.", "Sut y cadwodd y Brythoniaid ffordd Rhufain yn fyw yn y gorllewin wedi 410."),
    ],
    "saints": [
        (P, "J. W. James (ed. and trans.)", "Rhigyfarch’s Life of St David", "University of Wales Press, 1967",
         "The Life of Dewi Sant written at St Davids about 1090.", "Buchedd Dewi Sant a ysgrifennwyd yn Nhyddewi tua 1090."),
        (B, "Nora K. Chadwick (ed.)", "Studies in the Early British Church", "Cambridge University Press, 1958",
         "The church of the Britons in the age of the saints.", "Eglwys y Brythoniaid yn oes y saint."),
        (B, "John Reuben Davies", "The Book of Llandaf and the Norman Church in Wales", "Boydell Press, 2003",
         "How the Book of Llandaff was made, and why.", "Sut y lluniwyd Llyfr Llandaf, a pham."),
    ],
    "law": [
        (B, "T. M. Charles-Edwards", "Early Irish and Welsh Kinship", "Clarendon Press, 1993",
         "Family, land and inheritance in the Welsh laws.", "Teulu, tir ac etifeddiaeth yng nghyfreithiau Cymru."),
        (B, "Robin Chapman Stacey", "The Road to Judgment: From Custom to Court in Medieval Ireland and Wales", "University of Pennsylvania Press, 1994",
         "How disputes were settled under Welsh law.", "Sut y setlwyd anghydfodau dan gyfraith Cymru."),
    ],
    "princes": [
        (P, "D. Simon Evans (ed. and trans.)", "A Mediaeval Prince of Wales: The Life of Gruffudd ap Cynan", "Llanerch, 1990",
         "The life of the king of Gwynedd who fought his way home from Ireland.", "Buchedd brenin Gwynedd a ymladdodd ei ffordd adref o Iwerddon."),
        (P, "Paul Russell (ed. and trans.)", "Vita Griffini Filii Conani: The Medieval Latin Life of Gruffudd ap Cynan", "University of Wales Press, 2005",
         "The Latin Life of Gruffudd ap Cynan, with English.", "Buchedd Ladin Gruffudd ap Cynan, gyda Saesneg."),
        (B, "David Moore", "The Welsh Wars of Independence, c.410–c.1415", "Tempus, 2005",
         "A thousand years of Welsh resistance, from the Britons to Glyndŵr.", "Mil o flynyddoedd o wrthsafiad Cymreig, o’r Brythoniaid i Glyndŵr."),
        (B, "Sean Davies", "Welsh Military Institutions, 633–1283", "University of Wales Press, 2004",
         "How the Welsh kings and princes made war.", "Sut yr âi brenhinoedd a thywysogion Cymru i ryfel."),
        (B, "A. D. Carr", "Medieval Wales", "Macmillan, 1995",
         "A clear short history of Wales from 1063 to 1536.", "Hanes byr a chlir o Gymru o 1063 i 1536."),
        (B, "A. D. Carr", "Owen of Wales: The End of the House of Gwynedd", "University of Wales Press, 1991",
         "Owain Lawgoch, heir of the princes, who fought for France.", "Owain Lawgoch, etifedd y tywysogion, a ymladdodd dros Ffrainc."),
        (B, "David Walker", "Medieval Wales", "Cambridge University Press, 1990",
         "Wales from the Normans to the Tudors.", "Cymru o’r Normaniaid i’r Tuduriaid."),
        (B, "Glanmor Williams", "Owain Glyndŵr", "University of Wales Press, 1993",
         "A short life of Owain by the master historian.", "Cofiant byr i Owain gan y meistr hanesydd."),
    ],
    "tudor": [
        (B, "Ralph A. Griffiths", "Sir Rhys ap Thomas and his Family", "University of Wales Press, 1993",
         "The Welsh knight who stood with Harri Tudur at Bosworth.", "Y marchog o Gymro a safodd gyda Harri Tudur yn Bosworth."),
        (B, "J. Gwynfor Jones", "Early Modern Wales, c.1525–1640", "Macmillan, 1994",
         "The Wales of the Acts of Union, the gentry and the Welsh Bible.", "Cymru’r Deddfau Uno, yr uchelwyr a’r Beibl Cymraeg."),
        (B, "Philip Jenkins", "A History of Modern Wales, 1536–1990", "Longman, 1992",
         "Four and a half centuries in one volume.", "Pedair canrif a hanner mewn un gyfrol."),
        (B, "Prys Morgan", "The Eighteenth Century Renaissance", "Christopher Davies, 1981",
         "The great revival of Welsh learning, poetry and pride in the 1700s.", "Adfywiad mawr dysg, barddoniaeth a balchder Cymreig yn y 1700au."),
        (B, "Geraint H. Jenkins", "Literature, Religion and Society in Wales, 1660–1730", "University of Wales Press, 1978",
         "The Welsh books that taught a nation to read.", "Y llyfrau Cymraeg a ddysgodd genedl i ddarllen."),
        (B, "Eifion Evans", "Daniel Rowland and the Great Evangelical Awakening in Wales", "Banner of Truth Trust, 1985",
         "The preacher of Llangeitho and the Methodist revival.", "Pregethwr Llangeitho a’r diwygiad Methodistaidd."),
    ],
    "industry": [
        (B, "Russell Davies", "Hope and Heartbreak: A Social History of Wales and the Welsh, 1776–1871", "University of Wales Press, 2005",
         "The lives of ordinary Welsh people in the age of iron and chapel.", "Bywydau Cymry cyffredin yn oes yr haearn a’r capel."),
        (B, "D. Gareth Evans", "A History of Wales, 1815–1906", "University of Wales Press, 1989",
         "Wales in the century of industry.", "Cymru yng nghanrif diwydiant."),
        (B, "David Egan", "Coal Society: A History of the South Wales Mining Valleys, 1840–1980", "Gomer, 1987",
         "The valleys and their people from the first pits to the last.", "Y cymoedd a’u pobl o’r pyllau cyntaf i’r olaf."),
        (B, "Ivor Wilks", "South Wales and the Rising of 1839", "Croom Helm, 1984",
         "The Chartist rising at Newport and the valleys behind it.", "Gwrthryfel y Siartwyr yng Nghasnewydd a’r cymoedd y tu ôl iddo."),
    ],
    "modern": [
        (B, "Kenneth O. Morgan", "Wales in British Politics, 1868–1922", "University of Wales Press, 1963",
         "How Wales found its voice at Westminster.", "Sut y cafodd Cymru ei llais yn San Steffan."),
        (B, "Dai Smith", "Wales! Wales?", "George Allen and Unwin, 1984",
         "The history of modern Wales, written for the television series of the same name.", "Hanes Cymru fodern, a ysgrifennwyd ar gyfer y gyfres deledu o’r un enw."),
        (B, "Gareth Elwyn Jones", "Modern Wales: A Concise History", "Cambridge University Press, 1984",
         "Wales from about 1485 to the present.", "Cymru o tua 1485 hyd heddiw."),
        (B, "Gwyn A. Williams", "The Search for Beulah Land: The Welsh and the Atlantic Revolution", "Croom Helm, 1980",
         "The Welsh radicals and emigrants of the age of the American and French revolutions.", "Radicaliaid ac ymfudwyr Cymreig oes chwyldroadau America a Ffrainc."),
        (B, "Bill Jones", "Wales in America: Scranton and the Welsh, 1860–1920", "University of Wales Press, 1993",
         "The greatest Welsh community in the United States.", "Y gymuned Gymreig fwyaf yn yr Unol Daleithiau."),
    ],
    "lit": [
        (B, "Saunders Lewis", "Braslun o Hanes Llenyddiaeth Gymraeg", "Gwasg Prifysgol Cymru, 1932",
         "A sketch of Welsh literature to 1535, by Wales’s great critic.", "Braslun o lenyddiaeth Gymraeg hyd 1535, gan feirniad mawr Cymru."),
        (P, "Ifor Williams", "Lectures on Early Welsh Poetry", "Dublin Institute for Advanced Studies, 1944",
         "How the poems of Aneirin and Taliesin were rediscovered.", "Sut yr ailddarganfuwyd cerddi Aneirin a Thaliesin."),
        (P, "Gwyn Jones and Thomas Jones (trans.)", "The Mabinogion", "Golden Cockerel Press, 1948; Everyman’s Library, 1949",
         "The classic English translation of the twentieth century.", "Cyfieithiad Saesneg clasurol yr ugeinfed ganrif."),
        (P, "Rachel Bromwich (trans.)", "Dafydd ap Gwilym: A Selection of Poems", "Gomer, 1982",
         "Wales’s greatest poet in Welsh and English.", "Bardd mwyaf Cymru yn Gymraeg ac yn Saesneg."),
        (B, "Dafydd Johnston", "Llên yr Uchelwyr: Hanes Beirniadol Llenyddiaeth Gymraeg 1300–1525", "Gwasg Prifysgol Cymru, 2005",
         "The poets of the gentry, from Dafydd ap Gwilym to Guto’r Glyn.", "Beirdd yr uchelwyr, o Ddafydd ap Gwilym i Guto’r Glyn."),
        (B, "R. Geraint Gruffydd (ed.)", "A Guide to Welsh Literature, c.1530–1700", "University of Wales Press, 1997",
         "The writers of the age of the Welsh Bible.", "Awduron oes y Beibl Cymraeg."),
        (B, "Hywel Teifi Edwards", "Gŵyl Gwalia: Yr Eisteddfod Genedlaethol yn Oes Aur Victoria, 1858–1868", "Gomer, 1980",
         "The National Eisteddfod in its first great years.", "Yr Eisteddfod Genedlaethol yn ei blynyddoedd mawr cyntaf."),
        (B, "Glyn Jones", "The Dragon Has Two Tongues: Essays on Anglo-Welsh Writers and Writing", "J. M. Dent, 1968",
         "A poet on the Welsh writers who wrote in English.", "Bardd ar yr awduron o Gymry a ysgrifennai yn Saesneg."),
        (B, "M. Wynn Thomas", "Corresponding Cultures: The Two Literatures of Wales", "University of Wales Press, 1999",
         "How Welsh and English writing in Wales speak to each other.", "Sut y mae llên Gymraeg a llên Saesneg Cymru’n siarad â’i gilydd."),
        (B, "Peter Lord", "The Visual Culture of Wales: Imaging the Nation", "University of Wales Press, 2000",
         "How Wales has pictured itself, in paintings, prints and carvings.", "Sut y mae Cymru wedi’i darlunio ei hun, mewn paentiadau, printiau a cherfiadau."),
        (P, "Daniel Owen", "Rhys Lewis", "Wrexham, 1885",
         "The great Welsh novel of chapel life in Mold.", "Y nofel Gymraeg fawr am fywyd capel yr Wyddgrug."),
        (P, "Hedd Wyn", "Cerddi’r Bugail", "1918",
         "The shepherd poet’s poems, published after he fell at Passchendaele.", "Cerddi’r bardd-fugail, a gyhoeddwyd wedi iddo syrthio yn Passchendaele."),
        (P, "Kate Roberts", "Traed mewn Cyffion", "Gwasg Aberystwyth, 1936",
         "The quarrying families of Arfon, by the Queen of Welsh prose.", "Teuluoedd chwarel Arfon, gan Frenhines ein rhyddiaith."),
        (P, "Dylan Thomas", "Under Milk Wood", "J. M. Dent, 1954",
         "A day in the life of a Welsh seaside town, the most famous play for voices.", "Diwrnod ym mywyd tref glan môr Gymreig, y ddrama i leisiau enwocaf."),
        (P, "Waldo Williams", "Dail Pren", "Gwasg Aberystwyth, 1956",
         "The one collection of the poet of Preseli.", "Unig gasgliad bardd y Preseli."),
        (P, "R. S. Thomas", "Collected Poems, 1945–1990", "J. M. Dent, 1993",
         "The poet of the hill farms and the Welsh soul.", "Bardd y ffermydd mynydd ac enaid Cymru."),
    ],
    "lang": [
        (B, "Geraint H. Jenkins (ed.)", "Language and Community in the Nineteenth Century", "University of Wales Press, 1998",
         "Welsh at its height as the language of a working nation.", "Y Gymraeg ar ei hanterth fel iaith cenedl o weithwyr."),
        (B, "Geraint H. Jenkins and Mari A. Williams (eds)", "‘Let’s Do Our Best for the Ancient Tongue’: The Welsh Language in the Twentieth Century", "University of Wales Press, 2000",
         "The century of the fight for Welsh.", "Canrif y frwydr dros y Gymraeg."),
    ],
    "life": [
        (B, "Angela V. John", "By the Sweat of Their Brow: Women Workers at Victorian Coal Mines", "Croom Helm, 1980",
         "The women who worked at the pits, in Wales and beyond.", "Y menywod a weithiai yn y pyllau, yng Nghymru a thu hwnt."),
        (B, "Jane Aaron", "Nineteenth-Century Women’s Writing in Wales: Nation, Gender and Identity", "University of Wales Press, 2007",
         "The Welsh women writers of the 1800s.", "Llenorion benywaidd Cymru’r 1800au."),
    ],
}

# The Mabinogi section (src/mabinogi_tales.py, src/mabinogi_people.py): the tale guides and the people of the tales.
import refs as _R  # noqa: E402
PAGES["mabinogi-tales"] = L(_R.MABINOGION, _R.PEDEIR_KEINC, _R.GUEST_MABINOGION, _R.IFANS_MABINOGION, _R.TRIADS, _R.DAVIES_FOUR_BRANCHES,
    (B, "Hywel Wyn Owen and Richard Morgan", "Dictionary of the Place-Names of Wales", "Gomer, 2007",
     "The meaning of the place names the tales explain, from Nantlle to Mochdre.", "Ystyr yr enwau lleoedd a eglurir yn y chwedlau, o Nantlle i Fochdre."))
PAGES["mabinogi-people"] = PAGES["mabinogi-tales"]
_MBT = PAGES["mabinogi-tales"]["items"][:4]  # the editions and translations of the whole Mabinogion
PAGES["mabinogi-culhwch"] = L(*_MBT,
    (B, "Rachel Bromwich and D. Simon Evans", "Culhwch and Olwen: An Edition and Study of the Oldest Arthurian Tale", "University of Wales Press, 1992",
     "The standard edition, with the tasks, the list of Arthur’s men and the route of the boar.", "Yr argraffiad safonol, gyda’r anoethau, rhestr gwŷr Arthur a llwybr y twrch."),
    (B, "Rachel Bromwich and D. Simon Evans", "Culhwch ac Olwen: Testun Syr Idris Foster", "Gwasg Prifysgol Cymru, 1988",
     "The Welsh text begun by Idris Foster and finished by Rachel Bromwich and D. Simon Evans, with notes.", "Y testun Cymraeg a ddechreuwyd gan Idris Foster ac a orffennwyd gan Rachel Bromwich a D. Simon Evans, gyda nodiadau."),
    _R.TRIADS)
PAGES["mabinogi-macsen"] = L(*_MBT,
    (B, "Ifor Williams", "Breuddwyd Maxen", "Jarvis a Foster, Bangor, 1908",
     "The Welsh text of the Dream, edited by Ifor Williams.", "Testun Cymraeg y Breuddwyd, wedi’i olygu gan Ifor Williams."),
    (B, "Brynley F. Roberts", "Breuddwyd Maxen Wledig", "Dublin Institute for Advanced Studies, 2005",
     "A modern edition with a study of the tale and its history.", "Argraffiad diweddar gydag astudiaeth o’r chwedl a’i hanes."))
PAGES["mabinogi-lludd"] = L(*_MBT,
    (B, "Brynley F. Roberts", "Cyfranc Lludd a Llefelys", "Dublin Institute for Advanced Studies, 1975",
     "The standard edition of the tale, with its place in the Welsh Brut.", "Argraffiad safonol y chwedl, a’i lle yn y Brut Cymraeg."))
PAGES["mabinogi-rhonabwy"] = L(*_MBT,
    (B, "Melville Richards", "Breudwyt Ronabwy", "Gwasg Prifysgol Cymru, 1948",
     "The Welsh text of the Dream from the Red Book of Hergest, with notes on its places in Powys.", "Testun Cymraeg y Breuddwyd o Lyfr Coch Hergest, gyda nodiadau ar ei leoedd ym Mhowys."))
PAGES["mabinogi-owain"] = L(*_MBT,
    (B, "R. L. Thomson", "Owein, or Chwedyl Iarlles y Ffynnawn", "Dublin Institute for Advanced Studies, 1968",
     "The standard edition of the romance.", "Argraffiad safonol y rhamant."))
PAGES["mabinogi-peredur"] = L(*_MBT,
    (B, "Glenys Witchard Goetinck", "Historia Peredur vab Efrawc", "Gwasg Prifysgol Cymru, 1976",
     "The Welsh text of Peredur.", "Testun Cymraeg Peredur."))
PAGES["mabinogi-geraint"] = L(*_MBT,
    (B, "R. L. Thomson", "Ystorya Gereint uab Erbin", "Dublin Institute for Advanced Studies, 1997",
     "The standard edition of the romance.", "Argraffiad safonol y rhamant."))
PAGES["mabinogi-taliesin"] = L(*_MBT,
    (B, "Patrick K. Ford", "Ystoria Taliesin", "University of Wales Press, 1992",
     "The tale as Elis Gruffydd wrote it, edited with a study of its poems.", "Y chwedl fel yr ysgrifennodd Elis Gruffydd hi, wedi’i golygu gydag astudiaeth o’i cherddi."),
    _R.BOOK_TALIESIN if hasattr(_R, "BOOK_TALIESIN") else _R.TRIADS)
