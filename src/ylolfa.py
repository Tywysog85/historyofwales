"""Books from Y Lolfa, the Talybont press (ylolfa.com), Ifan's recommendation.

Each book is a normal reading-list item (same format as src/refs.py) whose last field is its page on ylolfa.com.
They sit in the reading lists of the pages they belong to (refs.py, refs2.py), or in SHELF_EXTRA for the
Books and authors page only. build.py's bookshelf_page() gathers every item with a ylolfa.com link into the
"Y Lolfa" section of that page, so a new Y Lolfa book only needs adding to a list.

Checked 2026-11-12: every title and ISBN is from the book's own page on ylolfa.com (the ISBN is in the link),
and every author from booksellers' listings of that same ISBN. A year is given only when it was confirmed.
Pages being written on Tryweryn, the Welsh Not and MAC/FWA can import these names.
"""
B = "b"   # a book by a historian (same as refs.B)

YL = "https://www.ylolfa.com/products/"

# ---------- the whole story ----------
CHRONOLOGY = (B, "Glyn German (compiler)", "Welsh History: A Chronological Outline", "Y Lolfa",
              "Every great date of the story of Wales in order, from the first people to today.",
              "Holl ddyddiadau mawr stori Cymru yn eu trefn, o’r bobl gyntaf hyd heddiw.",
              YL + "9781847718228/welsh-history-a-chronological-outline")
BRIEF_HISTORY = (B, "Gerald Morgan", "A Brief History of Wales", "Y Lolfa, 2008",
                 "The whole story of Wales in one short, clear book.",
                 "Stori gyfan Cymru mewn un llyfr byr a chlir.",
                 YL + "9781847710185/a-brief-history-of-wales")
HIGHLIGHTS = (B, "Emrys Roberts", "Highlights from Welsh History: Opening Some Windows on Our Past", "Y Lolfa",
              "Great moments of the Welsh past, one window at a time.",
              "Eiliadau mawr o orffennol Cymru, fesul ffenestr.",
              YL + "9781784613891")
FIGHT_FREEDOM = (B, "Gwynfor Evans", "The Fight for Welsh Freedom", "Y Lolfa",
                 "Gwynfor’s story of the long struggle of the Welsh to stay a free nation.",
                 "Stori Gwynfor am frwydr hir y Cymry i aros yn genedl rydd.",
                 YL + "9780862435158/the-fight-for-welsh-freedom")
WALES_SEA = (B, "Mark Redknap, Siân Rees and Alun Aberg (eds)", "Wales and the Sea: 10,000 Years of Welsh Maritime History",
             "Y Lolfa with the Royal Commission on the Ancient and Historical Monuments of Wales, 2019",
             "Ten thousand years of Wales and the sea: boats, ports, sailors and shipwrecks.",
             "Deng mil o flynyddoedd o Gymru a’r môr: cychod, porthladdoedd, morwyr a llongddrylliadau.",
             YL + "9781784615277/wales-and-the-sea")

# ---------- saints ----------
PURSUIT_DAVID = (B, "Gerald Morgan", "In Pursuit of Saint David: Patron Saint of Wales", "Y Lolfa, 2017",
                 "Dewi Sant followed through the old Lives and the places that remember him.",
                 "Dilyn Dewi Sant drwy’r hen Fucheddau a’r lleoedd sy’n ei gofio.",
                 YL + "9781784613723/in-pursuit-of-saint-david-patron-saint-of-wales")
DEPICTING_DAVID = (B, "Martin Crampin", "Depicting St David", "Y Lolfa, 2020",
                   "Dewi Sant in the stained glass, statues and pictures of the churches of Wales.",
                   "Dewi Sant yng ngwydr lliw, cerfluniau a lluniau eglwysi Cymru.",
                   YL + "9781912631230/depicting-st-david")
SAINTS_CAME = (B, "Anne Hayward", "Where the Saints Came From: On Pilgrimage in Wales and Beyond", "Y Lolfa, 2024",
               "A pilgrim’s journey to the homes of the saints, in Wales and across the sea.",
               "Taith pererin i gartrefi’r saint, yng Nghymru a thros y môr.",
               YL + "9781800994867/where-the-saints-came-from-on-pilgrimage-in-wales-and-beyond")

# ---------- princes and Glyndŵr ----------
LORD_RHYS = (B, "Roger Turvey", "The Lord Rhys: Prince of Deheubarth", "Y Lolfa, 2023",
             "The prince who made Deheubarth great and held the first eisteddfod.",
             "Y tywysog a wnaeth Ddeheubarth yn fawr ac a gynhaliodd yr eisteddfod gyntaf.",
             YL + "9781800993143/the-lord-rhys-prince-of-deheubarth")
LLYWELYN_GREAT = (B, "Roger Turvey", "Llywelyn the Great", "Y Lolfa, 2023",
                  "The life of Llywelyn ab Iorwerth, the prince who ruled almost all of Wales.",
                  "Bywyd Llywelyn ab Iorwerth, y tywysog a reolodd bron y cyfan o Gymru.",
                  YL + "9781800993150/llywelyn-the-great")
GLYNDWR_PRINCE = (B, "R. R. Davies", "Owain Glyn Dŵr: Prince of Wales", "Y Lolfa",
                  "The great historian of Owain’s war tells his story in a short book for everyone.",
                  "Hanesydd mawr rhyfel Owain yn adrodd ei hanes mewn llyfr byr i bawb.",
                  YL + "9781847711274/owain-glyndwr-prince-of-wales")

# ---------- risings and protest ----------
DIC_PENDERYN = (B, "Sally Roberts Jones", "Dic Penderyn: The Man and the Martyr", "Y Lolfa, 2022",
                "The first full life of the young Merthyr man hanged after the Rising of 1831.",
                "Y cofiant llawn cyntaf i’r gŵr ifanc o Ferthyr a grogwyd ar ôl Gwrthryfel 1831.",
                YL + "9781800991842/dic-penderyn-the-man-and-the-martyr")
TWM_CARNABWTH = (B, "Hefin Wyn", "In Pursuit of Twm Carnabwth: The Original Leader of the Rebecca Rioters", "Y Lolfa; also in Welsh as Ar Drywydd Twm Carnabwth",
                 "Thomas Rees of Mynachlog-ddu, the first ‘Rebecca’, who led the attack on the Efail-wen gate in 1839.",
                 "Thomas Rees o Fynachlog-ddu, y ‘Beca’ cyntaf, a arweiniodd yr ymosodiad ar glwyd Efail-wen yn 1839.",
                 YL + "9781800992719/in-pursuit-of-twm-carnabwth")

# ---------- Tryweryn, MAC and the Free Wales Army ----------
TRYWERYN_DAWN = (B, "Wyn Thomas", "Tryweryn: A New Dawn? The Legacy of the Drowning of Capel Celyn", "Y Lolfa",
                 "The drowning of Capel Celyn and how it woke a nation.",
                 "Boddi Capel Celyn a sut y deffrodd genedl.",
                 YL + "9781912631483/tryweryn-a-new-dawn")
TRYWERYN_AWAKES = (B, "Owain Williams", "Tryweryn: A Nation Awakes – The Story of a Welsh Freedom Fighter", "Y Lolfa",
                   "Owain Williams’s own story of the stand against the drowning of Capel Celyn.",
                   "Stori Owain Williams ei hun am y safiad yn erbyn boddi Capel Celyn.",
                   YL + "9781784612467/tryweryn-a-nation-awakes-the-story-of-a-welsh-freedom-fighter")
JOHN_JENKINS = (B, "Wyn Thomas", "John Jenkins: The Reluctant Revolutionary?", "Y Lolfa",
                "The authorised life of John Jenkins, who led Mudiad Amddiffyn Cymru (MAC) in the 1960s.",
                "Cofiant awdurdodedig John Jenkins, a arweiniodd Fudiad Amddiffyn Cymru (MAC) yn y 1960au.",
                YL + "9781912631148/john-jenkins-the-reluctant-revolutionary")
DREAM_FREEDOM = (B, "Roy Clews", "To Dream of Freedom: The Story of MAC and the Free Wales Army", "Y Lolfa; first published 1980",
                 "The men of MAC and the Free Wales Army and the years of the Investiture.",
                 "Gwŷr MAC a Byddin Rhyddid Cymru a blynyddoedd yr Arwisgo.",
                 YL + "9780862435868/to-dream-of-freedom")
DIM_CROESO = (B, "Arwel Vittle", "Dim Croeso ’69: Gwrthsefyll yr Arwisgo", "Y Lolfa",
              "In Welsh: the people who stood against the Investiture of 1969.",
              "Y bobl a safodd yn erbyn Arwisgo 1969.",
              YL + "9781784617103/dim-croeso-69")
GWYNFOR_PORTRAIT = (B, "Rhys Evans", "Gwynfor Evans: A Portrait of a Patriot", "Y Lolfa, 2008; first published in Welsh as Rhag Pob Brad, 2005",
                    "The full life of Gwynfor Evans, from Barry to the fast for S4C.",
                    "Cofiant llawn Gwynfor Evans, o’r Barri i’r ympryd dros S4C.",
                    YL + "9780862439187/gwynfor-evans-a-portrait-of-a-patriot")

# ---------- the language ----------
BRWYDR_IAITH = (B, "Geraint Jones", "Brwydr yr Iaith, 1962–67", "Y Lolfa",
                "In Welsh: the fight for the language in the first years of Cymdeithas yr Iaith.",
                "Y frwydr dros yr iaith ym mlynyddoedd cyntaf Cymdeithas yr Iaith.",
                YL + "9781800997004/brwydr-yr-iaith")
CARDIFF_WELSH = (B, "Owen John Thomas", "The Welsh Language in Cardiff: A History of Survival", "Y Lolfa, 2020",
                 "How Welsh lived on in the capital through the centuries.",
                 "Sut y bu’r Gymraeg fyw yn y brifddinas ar hyd y canrifoedd.",
                 YL + "9781784618827/the-welsh-language-in-cardiff")

# ---------- abroad ----------
DREAMING_CITY = (B, "Colin Thomas", "Dreaming a City: From Wales to Ukraine", "Y Lolfa, 2009",
                 "John Hughes of Merthyr and the city he founded in Ukraine, Hughesovka, now Donetsk.",
                 "John Hughes o Ferthyr a’r ddinas a sefydlodd yn Wcráin, Hughesovka, Donetsk heddiw.",
                 YL + "9781847711243")
MADOG_CHILDREN = (B, "Gwyn Thomas, pictures by Margaret D. Jones", "Madog, the First White American", "Y Lolfa",
                  "Prince Madog’s voyage told for children.",
                  "Mordaith y Tywysog Madog i blant.",
                  YL + "9780862437664/madog-the-first-white-american-(english)")

LAND_OF_MY_FATHERS_URL = YL + "9780862432652/land-of-my-fathers"

# ---------- the section on the Books and authors page ----------
SECTION = ("Y Lolfa: books from Talybont", "Y Lolfa: llyfrau o Dal-y-bont")
INTRO = ("Y Lolfa was founded in 1967 by Robat Gruffudd at Talybont in Ceredigion, and for more than half a century this "
         "Welsh press has published the history of Wales, in Welsh and in English: the princes, Glyndŵr, Tryweryn, the "
         "language and the fight for freedom. Every book below links to its page on ylolfa.com, where you can buy it "
         "from the publisher. Each one also sits in its period further down this page, with the pages of this site that use it.",
         "Sefydlwyd Y Lolfa yn 1967 gan Robat Gruffudd yn Nhal-y-bont, Ceredigion, ac ers dros hanner canrif mae’r wasg "
         "Gymreig hon wedi cyhoeddi hanes Cymru, yn Gymraeg ac yn Saesneg: y tywysogion, Glyndŵr, Tryweryn, yr iaith a’r "
         "frwydr dros ryddid. Mae pob llyfr isod yn mynd â chi i’w dudalen ar ylolfa.com, lle gallwch ei brynu gan y "
         "cyhoeddwr. Mae pob un hefyd yn ei gyfnod yn is i lawr y dudalen hon, gyda’r tudalennau o’r wefan hon sy’n ei ddefnyddio.")
