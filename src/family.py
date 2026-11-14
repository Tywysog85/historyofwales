"""Family history: family-history.html, "Finding your Welsh family" / "Dod o hyd i'ch teulu Cymreig".

Asked for by Ifan, 14 November 2026: Welsh surnames and where they come from, how ap / ab / ferch worked and when fixed
surnames came, and step-by-step guides to finding Welsh ancestors in the records (parish and chapel registers, the
census, the National Library of Wales, Welsh Newspapers Online, tithe maps).

build.py calls setup(globals()) once and page() for the HTML. The words are here; the Welsh names game (names.html,
src/static/play.js) stays the place to look up one surname or make your own name in the old way, and this page sends
people there.

SOURCES (each opened and read, 14 November 2026; see CITES below):
  - Gerald of Wales, Description of Wales I.17 (Hoare translation, read on buildinghistory.org): the common people
    recite their line to the sixth or seventh generation; his example is Rhys ap Gruffudd back to Rhodri Mawr.
  - John and Sheila Rowlands, "The Distribution of Surnames in Wales", Nomina 29: marriages 1813-37, the ten
    commonest names 55.85% of Wales against 5.15% of England, Jones 30.71% in Penllyn, the Registrar General in 1856.
  - Museum Wales, "Welsh Surnames: why are there so many Joneses in Wales?" (from Prys Morgan): land rights rested on
    proving descent; fixed surnames about 500 years ago.
  - Wikipedia, "Welsh surnames": fixed surnames from the 15th century, gentry under Henry VIII, the old way lasting in
    some rural areas to the early 19th century; Powell, Price, Bowen, Pritchard, Pugh.
  - National Library of Wales family-history pages: parish registers from 1538, bishop's transcripts 1598 to about
    1860 (few Welsh ones before 1660), marriage bonds indexed to 1837, chapel marriages in church 1754-1837, pre-1837
    chapel registers at The National Archives, tithe maps (more than 1,200 on Places of Wales), wills before 1858.
  - The National Archives census guide (1841-1921 online, 1931 burnt in 1942, none in 1941); A Vision of Britain
    (the language question first asked in Wales in 1891); FamilySearch (about 75% chapel-goers by 1851);
    FreeBMD (civil registration from July 1837); Welsh Newspapers Online (1804-1919, 120 papers, free).
  - Top surnames: one-name.org, from Michael A. Williams's count of the six Welsh telephone directories of 1986.
  - Dictionary of Welsh Biography, Lewys Dwnn: deputy herald for Wales from 1585; Meyrick's edition, 1846.
  - Aberystwyth University, the Bartrum Genealogical Project: Welsh Genealogies AD 300-1400 (UWP, 1974) and
    AD 1400-1500 (NLW, 1983), scanned and free online.
"""

g = {}


def setup(build_globals):
    g.update(build_globals)


# ---------- sources beside the claims (merged into src/cites.py) ----------
CITES = {
    "fam-gerald": dict(
        short=("Gerald of Wales", "Gerallt Gymro"),
        t="The Description of Wales, Book I, chapter 17: Their love of high birth and ancient genealogy",
        by=("Gerald of Wales, about 1194; translated by Sir Richard Colt Hoare", "Gerallt Gymro, tua 1194; cyfieithiad Syr Richard Colt Hoare"),
        note=("“Even the common people retain their genealogy”, back “to the sixth or seventh generation, or beyond”: his example is Rhys, son of Gruffudd, son of Rhys, son of Tewdwr, back to Rhodri Mawr.",
              "“Mae hyd yn oed y werin yn cadw eu hachau”, yn ôl “i’r chweched neu’r seithfed genhedlaeth, neu tu hwnt”: ei esiampl yw Rhys ap Gruffudd ap Rhys ap Tewdwr, yn ôl hyd at Rodri Mawr."),
        url="https://www.buildinghistory.org/primary/gerald.shtml", lang="en"),
    "fam-museum": dict(
        short=("Museum Wales", "Amgueddfa Cymru"),
        t="Welsh Surnames: Why are there so many Joneses in Wales?", by=("Amgueddfa Cymru – Museum Wales, from the work of Prys Morgan", "Amgueddfa Cymru, o waith Prys Morgan"),
        note=("Explains that a man’s long string of ap names had a legal purpose, because his right to land depended on proving descent from the forefather who held it, and that fixed surnames came about 500 years ago.",
              "Yn esbonio bod pwrpas cyfreithiol i’r rhes hir o enwau ap, gan fod hawl dyn i dir yn dibynnu ar brofi ei fod yn disgyn o’r hynafiad a’i daliai, ac mai tua 500 mlynedd yn ôl y daeth cyfenwau sefydlog."),
        url="https://museum.wales/articles/1220/Welsh-Surnames-Why-are-there-so-many-Joneses-in-Wales", lang="en"),
    "fam-wiki-names": dict(
        short=("Welsh surnames", "Cyfenwau Cymreig"),
        t="Welsh surnames", by=("Wikipedia, citing the Welsh Academy Encyclopaedia of Wales", "Wikipedia, gan ddyfynnu Gwyddoniadur Cymru"),
        note=("Fixed surnames from the 15th century onwards; hereditary among the gentry under Henry VIII, spreading slowly among other families; patronymics in some rural areas until the early 19th century. Lists Powell (ap Hywel), Price (ap Rhys), Bowen (ab Owen), Pritchard (ap Richard) and Pugh (ap Hugh).",
              "Cyfenwau sefydlog o’r 15fed ganrif ymlaen; yn etifeddol ymhlith y bonedd dan Harri VIII, ac yn lledu’n araf ymhlith teuluoedd eraill; enwau tadol mewn rhai ardaloedd gwledig hyd ddechrau’r 19eg ganrif. Mae’n rhestru Powell (ap Hywel), Price (ap Rhys), Bowen (ab Owen), Pritchard (ap Rhisiart) a Pugh (ap Huw)."),
        url="https://en.wikipedia.org/wiki/Welsh_surnames", lang="en"),
    "fam-rowlands": dict(
        short=("Nomina 29", "Nomina 29"),
        t="The Distribution of Surnames in Wales", by=("John and Sheila Rowlands, Nomina 29, Society for Name Studies in Britain and Ireland", "John a Sheila Rowlands, Nomina 29, Cymdeithas Astudiaethau Enwau Prydain ac Iwerddon"),
        note=("From the marriage registers of 1813 to 1837: the ten commonest surnames cover 55.85% of Wales against 5.15% of England, and Jones alone 30.71% in Penllyn. Quotes the Registrar General in 1856 on “less than 100 different surnames”.",
              "O gofrestri priodasau 1813 i 1837: mae’r deg cyfenw mwyaf cyffredin yn cyfrif am 55.85% o Gymru o’i gymharu â 5.15% o Loegr, a Jones ar ei ben ei hun am 30.71% ym Mhenllyn. Mae’n dyfynnu’r Cofrestrydd Cyffredinol yn 1856 am “lai na 100 o gyfenwau gwahanol”."),
        url="https://www.snsbi.org.uk/Nomina_articles/Nomina_29_Rowlands.pdf", lang="en"),
    "fam-onename": dict(
        short=("Guild of One-Name Studies", "Guild of One-Name Studies"),
        t="Top surnames in Wales", by=("Guild of One-Name Studies, from Michael A. Williams, Researching Local History (1996)", "Guild of One-Name Studies, o Michael A. Williams, Researching Local History (1996)"),
        note=("The commonest surnames in the six Welsh telephone directories of 1986, in thousands: Jones 60.57, Williams 37.81, Davies 36.76, Evans 24.66, Thomas 22.97 and on down to Lloyd 5.64.",
              "Y cyfenwau mwyaf cyffredin yn chwe chyfeirlyfr ffôn Cymru yn 1986, mewn miloedd: Jones 60.57, Williams 37.81, Davies 36.76, Evans 24.66, Thomas 22.97 ac i lawr at Lloyd 5.64."),
        url="https://one-name.org/modern-british-surnames/statistics/top-surnames/wales", lang="en"),
    "fam-nlw-church": dict(
        short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"),
        t="Church in Wales records", by=("National Library of Wales, information for family historians", "Llyfrgell Genedlaethol Cymru, gwybodaeth i haneswyr teulu"),
        note=("Parish registers were ordered in 1538 and the originals are now in the county archives; bishop’s transcripts run from 1598 to about 1860, though few Welsh ones survive from before 1660; marriage bonds are indexed to 1837.",
              "Gorchmynnwyd cofrestri plwyf yn 1538 ac mae’r rhai gwreiddiol yn yr archifdai sirol heddiw; mae trawsgrifiadau’r esgob yn rhedeg o 1598 hyd tua 1860, er mai ychydig o rai Cymru sydd wedi goroesi o cyn 1660; mae’r bondiau priodas wedi’u mynegeio hyd 1837."),
        url="https://library.wales/information-for/family-historians/records/church-in-wales-records", lang="en"),
    "fam-nlw-chapel": dict(
        short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"),
        t="Nonconformist records", by=("National Library of Wales, information for family historians", "Llyfrgell Genedlaethol Cymru, gwybodaeth i haneswyr teulu"),
        note=("From 1754 to 1837 everyone except Quakers and Jews had to marry in the parish church, chapel families too; chapel registers from before 1837 are at The National Archives in Kew.",
              "O 1754 hyd 1837 roedd yn rhaid i bawb ond y Crynwyr a’r Iddewon briodi yn eglwys y plwyf, teuluoedd y capel hefyd; mae cofrestri capeli o cyn 1837 yn yr Archifau Gwladol yn Kew."),
        url="https://www.library.wales/information-for/family-historians/records/nonconformist-records", lang="en"),
    "fam-familysearch": dict(
        short=("FamilySearch", "FamilySearch"),
        t="Discover Your Welsh Ancestry in These 3 Key Sources", by=("FamilySearch blog", "Blog FamilySearch"),
        note=("“By 1851, about 75 percent of Welsh people attended a nonconformist church”; the Welsh censuses of 1841 to 1911 and the 1939 Register can be searched free.",
              "Erbyn 1851 roedd tua 75 y cant o’r Cymry yn mynychu capel anghydffurfiol; gellir chwilio cyfrifiadau Cymru 1841 i 1911 a Chofrestr 1939 am ddim."),
        url="https://www.familysearch.org/en/blog/welsh-ancestry", lang="en"),
    "fam-tna-census": dict(
        short=("The National Archives", "Yr Archifau Gwladol"),
        t="Census records", by=("The National Archives, research guide", "Yr Archifau Gwladol, canllaw ymchwil"),
        note=("The censuses of England and Wales from 1841 to 1921 are online; the 1931 census was destroyed by fire in 1942 and none was taken in 1941; later censuses stay closed for 100 years.",
              "Mae cyfrifiadau Cymru a Lloegr o 1841 hyd 1921 ar-lein; dinistriwyd cyfrifiad 1931 gan dân yn 1942 ac ni chymerwyd un yn 1941; mae cyfrifiadau diweddarach ar gau am 100 mlynedd."),
        url="https://www.nationalarchives.gov.uk/help-with-your-research/research-guides/census-records", lang="en"),
    "fam-1891": dict(
        short=("A Vision of Britain", "A Vision of Britain"),
        t="Selected subjects: language spoken in Wales and Monmouthshire", by=("A Vision of Britain through Time, University of Portsmouth", "A Vision of Britain through Time, Prifysgol Portsmouth"),
        note=("The census of 1891 asked, “for the first time”, which language each person in Wales spoke, in a new column headed “Language Spoken”.",
              "Gofynnodd cyfrifiad 1891, “am y tro cyntaf”, pa iaith a siaradai pob person yng Nghymru, mewn colofn newydd dan y pennawd “Language Spoken”."),
        url="https://visionofbritain.org.uk/census/Cen_Guide/13", lang="en"),
    "fam-freebmd": dict(
        short=("FreeBMD", "FreeBMD"),
        t="About FreeBMD", by=("FreeBMD, a charity of volunteers", "FreeBMD, elusen o wirfoddolwyr"),
        note=("Civil registration of births, marriages and deaths in England and Wales began in July 1837; FreeBMD puts the index free online.",
              "Dechreuodd cofrestru sifil genedigaethau, priodasau a marwolaethau yng Nghymru a Lloegr ym mis Gorffennaf 1837; mae FreeBMD yn rhoi’r mynegai ar-lein am ddim."),
        url="https://www.freebmd.org.uk/", lang="en"),
    "fam-wno": dict(
        short=("Welsh Newspapers Online", "Papurau Newydd Cymru"),
        t="Welsh Newspapers Online", by=("National Library of Wales; summarised on Wikipedia", "Llyfrgell Genedlaethol Cymru; crynodeb ar Wikipedia"),
        note=("More than 1,100,000 pages from 120 newspapers, in Welsh and English, from 1804 to 1919, free online.",
              "Mwy na 1,100,000 o dudalennau o 120 o bapurau newydd, yn Gymraeg ac yn Saesneg, o 1804 hyd 1919, am ddim ar-lein."),
        url="https://newspapers.library.wales/", lang="en"),
    "fam-tithe": dict(
        short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"),
        t="Tithe maps", by=("National Library of Wales, family history help", "Llyfrgell Genedlaethol Cymru, help hanes teulu"),
        note=("Drawn for every parish after the Tithe Commutation Act of 1836; the apportionments give landowner, tenant, field names, use and acreage. More than 1,200 maps for Wales can be searched on Places of Wales.",
              "Fe’u lluniwyd ar gyfer pob plwyf ar ôl Deddf Cymudo’r Degwm 1836; mae’r rhanniadau’n rhoi’r tirfeddiannwr, y tenant, enwau’r caeau, eu defnydd a’u maint. Gellir chwilio mwy na 1,200 o fapiau Cymru ar wefan Lleoedd Cymru."),
        url="https://www.library.wales/catalogues-searching/help-to-search/family-history-help/tithe-maps", lang="en"),
    "fam-wills": dict(
        short=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"),
        t="Wills", by=("National Library of Wales", "Llyfrgell Genedlaethol Cymru"),
        note=("Wills proved in the church courts of Wales before 1858, from Bangor, Llandaff, St Asaph, St Davids, Brecon and Hawarden, the earliest from about 1521; about 190,000 wills and 800,000 pages were put online in 2009.",
              "Ewyllysiau a brofwyd yn llysoedd eglwysig Cymru cyn 1858, o Fangor, Llandaf, Llanelwy, Tyddewi, Aberhonddu a Phenarlâg, y cynharaf o tua 1521; rhoddwyd tua 190,000 o ewyllysiau ac 800,000 o dudalennau ar-lein yn 2009."),
        url="https://www.library.wales/discover/nlw-resources/wills/", lang="en"),
    "fam-dwnn": dict(
        short=("Dictionary of Welsh Biography", "Y Bywgraffiadur"),
        t="Dwnn, Lewys (c. 1550 – c. 1616), genealogist", by=("Dictionary of Welsh Biography, National Library of Wales", "Y Bywgraffiadur Cymreig, Llyfrgell Genedlaethol Cymru"),
        note=("Made deputy herald “for the three provinces of Kymry” in 1585, he gathered the pedigrees of the families of Wales until 1614; edited by S. R. Meyrick as Heraldic Visitations of Wales (Llandovery, 1846).",
              "Fe’i gwnaed yn ddirprwy herodr “for the three provinces of Kymry” yn 1585, a chasglodd achau teuluoedd Cymru hyd 1614; golygwyd gan S. R. Meyrick fel Heraldic Visitations of Wales (Llanymddyfri, 1846)."),
        url="https://biography.wales/article/s-DWNN-LEW-1550", url_cy="https://bywgraffiadur.cymru/article/c-DWNN-LEW-1550"),
    "fam-bartrum": dict(
        short=("Aberystwyth University", "Prifysgol Aberystwyth"),
        t="Bartrum Genealogical Project", by=("Aberystwyth University research data, 2020", "Data ymchwil Prifysgol Aberystwyth, 2020"),
        note=("Colour scans of Peter Bartrum’s Welsh Genealogies AD 300–1400 (University of Wales Press, 1974) and AD 1400–1500 (National Library of Wales, 1983), with their indexes, free to download.",
              "Sganiau lliw o Welsh Genealogies AD 300–1400 Peter Bartrum (Gwasg Prifysgol Cymru, 1974) ac AD 1400–1500 (Llyfrgell Genedlaethol Cymru, 1983), gyda’u mynegeion, i’w lawrlwytho am ddim."),
        url="https://research.aber.ac.uk/en/datasets/bartrum-genealogical-project/", lang="en"),
}


# ---------- Gerald's example: the line of the Lord Rhys, as he gave it (Description of Wales I.17) ----------
# (name EN, name CY, person page id or None)
PEDIGREE = [
    ("Rhys ap Gruffudd, the Lord Rhys", "Rhys ap Gruffudd, yr Arglwydd Rhys", "yr-arglwydd-rhys"),
    ("Gruffudd ap Rhys", "Gruffudd ap Rhys", "gruffudd-ap-rhys"),
    ("Rhys ap Tewdwr", "Rhys ap Tewdwr", "rhys-ap-tewdwr"),
    ("Tewdwr ab Einion", "Tewdwr ab Einion", None),
    ("Einion ab Owain", "Einion ab Owain", None),
    ("Owain ap Hywel", "Owain ap Hywel", "owain-ap-hywel"),
    ("Hywel Dda", "Hywel Dda", "hywel-dda"),
    ("Cadell ap Rhodri", "Cadell ap Rhodri", "cadell-ap-rhodri"),
    ("Rhodri Mawr", "Rhodri Mawr", "rhodri-mawr"),
]

INTRO_EN = [
    "Few peoples have cared about their family lines as much as the Welsh. Under the old Welsh law a man’s right to his share of the family land came through his descent, so he had to be able to name the forefathers it came down through. Knowing your people was part of who you were.[[cite:fam-museum]]",
    "> Even the common people retain their genealogy, and can not only readily recount the names of their grandfathers and great-grandfathers, but even refer back to the sixth or seventh generation, or beyond them. | Gerald of Wales, The Description of Wales, about 1194",
    "Gerald gave an example from his own family: his kinsman Rhys ap Gruffudd, the Lord Rhys of Deheubarth, whose line ran back nine generations to Rhodri Mawr. You can follow it below, name by name, the way a Welshman of the twelfth century would have said it.[[cite:fam-gerald]]",
]
INTRO_CY = [
    "Ychydig o bobloedd sydd wedi gofalu cymaint am eu llinach â’r Cymry. Dan yr hen gyfraith Gymreig deuai hawl dyn i’w gyfran o dir y teulu drwy ei dras, felly roedd yn rhaid iddo allu enwi’r hynafiaid y daeth y tir i lawr drwyddynt. Roedd adnabod eich pobl yn rhan o bwy oeddech chi.[[cite:fam-museum]]",
    "> Mae hyd yn oed y werin yn cadw eu hachau, a gallant nid yn unig enwi eu teidiau a’u hendeidiau yn rhwydd, ond mynd yn ôl i’r chweched neu’r seithfed genhedlaeth, neu tu hwnt. | Gerallt Gymro, Disgrifiad o Gymru, tua 1194",
    "Rhoddodd Gerallt esiampl o’i deulu ei hun: ei berthynas Rhys ap Gruffudd, yr Arglwydd Rhys o Ddeheubarth, yr âi ei linach yn ôl naw cenhedlaeth at Rodri Mawr. Gallwch ei dilyn isod, enw wrth enw, fel y byddai Cymro o’r ddeuddegfed ganrif wedi’i dweud.[[cite:fam-gerald]]",
]

NAMING_EN = [
    "For most of Welsh history nobody had a surname. You had your own name and your father’s: Llywelyn ap Gruffudd, Llywelyn son of Gruffudd; Gwenllian ferch Llywelyn, Gwenllian daughter of Llywelyn. Ap comes from the old word mab, son, and becomes ab before a vowel, as in Rhys ab Owain. Ferch, often written verch, comes from merch, daughter.",
    "A name could carry a whole line: Dafydd ap Ieuan ap Rhys ap Gruffudd is Dafydd, son of Ieuan, son of Rhys, son of Gruffudd. Each generation had a new name, and the family’s memory was kept in the chain.",
    "A woman kept her own name all her life. When Gwenllian, daughter of Gruffudd ap Cynan, married Gruffudd ap Rhys, she stayed Gwenllian ferch Gruffudd: her father’s daughter, in her own right.",
    "Some people were known by a word that described them, instead of or as well as their father’s name: Dafydd Llwyd (grey), Ieuan Fychan (the younger), Gwilym Ddu (dark), Morgan Goch (red). Those words later became surnames too.",
]
NAMING_CY = [
    "Am y rhan fwyaf o hanes Cymru nid oedd gan neb gyfenw. Roedd gennych eich enw eich hun ac enw eich tad: Llywelyn ap Gruffudd, Llywelyn fab Gruffudd; Gwenllian ferch Llywelyn. Daw ap o’r hen air mab, ac mae’n troi’n ab o flaen llafariad, fel yn Rhys ab Owain. Daw ferch, a ysgrifennid yn aml yn verch, o merch.",
    "Gallai enw gario llinach gyfan: ystyr Dafydd ap Ieuan ap Rhys ap Gruffudd yw Dafydd, mab Ieuan, mab Rhys, mab Gruffudd. Roedd gan bob cenhedlaeth enw newydd, a chedwid cof y teulu yn y gadwyn.",
    "Cadwai menyw ei henw ei hun ar hyd ei hoes. Pan briododd Gwenllian, merch Gruffudd ap Cynan, â Gruffudd ap Rhys, arhosodd yn Gwenllian ferch Gruffudd: merch ei thad, yn ei hawl ei hun.",
    "Câi rhai pobl eu hadnabod wrth air a’u disgrifiai, yn lle enw eu tad neu yn ogystal ag ef: Dafydd Llwyd, Ieuan Fychan (yr ieuengaf), Gwilym Ddu, Morgan Goch. Daeth y geiriau hynny’n gyfenwau hefyd yn nes ymlaen.",
]

SURNAMES_EN = [
    "Fixed family names, handed down unchanged from parent to child, came into Wales on the English pattern from the fifteenth century onwards. Under the Tudors the gentry took them first; the custom spread slowly through other families, and in some country districts the old way of ap and ferch lasted into the early nineteenth century.[[cite:fam-wiki-names,fam-museum]]",
    "When a family settled on a surname, it was usually the father’s name, frozen where it stood. Sometimes the ap or ab stuck to the front of it: ap Hywel became Powell, ap Rhys Price, ab Owain Bowen, ap Rhisiart Pritchard and ap Huw Pugh. Far more often the father’s name simply took an English -s: the children of John became Jones, of Dafydd Davies, of Gwilym Williams, of Ifan Evans.[[cite:fam-wiki-names]]",
    "That is why so few surnames cover so many Welsh families. Studying the marriage registers of 1813 to 1837, John and Sheila Rowlands found that the ten commonest surnames covered 55.85 per cent of Wales, against 5.15 per cent of England. In Penllyn, around Bala, nearly one person in three was a Jones.[[cite:fam-rowlands]]",
    "> Perhaps nine tenths of our countrymen in the principality could be mustered under less than 100 different surnames. | The Registrar General, 1856",
    "It is a mark of how long Wales kept its own way of naming. A Jones, a Davies or a Price today carries in one word the memory of a father whose name was spoken in Welsh.",
]
SURNAMES_CY = [
    "Daeth enwau teuluol sefydlog, a âi i lawr heb newid o riant i blentyn, i Gymru ar batrwm Lloegr o’r bymthegfed ganrif ymlaen. Dan y Tuduriaid y bonedd a’u cymerodd gyntaf; lledodd yr arfer yn araf drwy deuluoedd eraill, ac mewn rhai ardaloedd gwledig parhaodd yr hen ffordd o ap a ferch hyd ddechrau’r bedwaredd ganrif ar bymtheg.[[cite:fam-wiki-names,fam-museum]]",
    "Pan setlai teulu ar gyfenw, enw’r tad oedd hwnnw fel arfer, wedi’i rewi yn ei unfan. Weithiau glynai’r ap neu’r ab wrth ei flaen: aeth ap Hywel yn Powell, ap Rhys yn Price, ab Owain yn Bowen, ap Rhisiart yn Pritchard ac ap Huw yn Pugh. Yn llawer amlach cymerodd enw’r tad -s Saesneg: aeth plant John yn Jones, plant Dafydd yn Davies, plant Gwilym yn Williams, plant Ifan yn Evans.[[cite:fam-wiki-names]]",
    "Dyna pam mae cyn lleied o gyfenwau gan gynifer o deuluoedd Cymru. Wrth astudio cofrestri priodasau 1813 i 1837, canfu John a Sheila Rowlands fod y deg cyfenw mwyaf cyffredin yn cyfrif am 55.85 y cant o Gymru, o’i gymharu â 5.15 y cant o Loegr. Ym Mhenllyn, o gwmpas y Bala, roedd bron un person o bob tri yn Jones.[[cite:fam-rowlands]]",
    "> Efallai y gellid casglu naw rhan o ddeg o’n cydwladwyr yn y dywysogaeth dan lai na 100 o gyfenwau gwahanol. | Y Cofrestrydd Cyffredinol, 1856",
    "Mae’n arwydd o ba mor hir y cadwodd Cymru ei ffordd ei hun o enwi. Mae Jones, Davies neu Price heddiw yn cario mewn un gair gof am dad y dywedid ei enw yn Gymraeg.",
]

# ap names and describing names: (surname, from EN, from CY)
AP_NAMES = [
    ("Powell", "ap Hywel", "ap Hywel"), ("Price, Pryce, Prys", "ap Rhys", "ap Rhys"), ("Bowen", "ab Owain", "ab Owain"),
    ("Bevan", "ab Ifan", "ab Ifan"), ("Pritchard", "ap Rhisiart (Richard)", "ap Rhisiart"), ("Parry", "ap Harri (Harry)", "ap Harri"),
    ("Pugh", "ap Huw", "ap Huw"), ("Probert", "ap Robert", "ap Robert"), ("Prosser", "ap Rosser (Roger)", "ap Rosser"),
    ("Prothero", "ap Rhydderch", "ap Rhydderch"), ("Beynon", "ab Einion", "ab Einion"), ("Bellis", "ab Elis", "ab Elis"),
]
WORD_NAMES = [
    ("Lloyd, Floyd", "llwyd: grey, or grey-haired", "llwyd"), ("Vaughan", "fychan: the younger, the smaller", "fychan: yr ieuengaf, y lleiaf"),
    ("Wyn, Wynne, Gwyn", "gwyn: white, fair, blessed", "gwyn: gwyn, golau, bendigaid"), ("Gough, Goch", "coch: red-haired", "coch: pengoch"),
    ("Dee", "du: black, dark-haired", "du: gwallt tywyll"), ("Voyle, Moyle", "moel: bald", "moel"),
    ("Gethin", "cethin: swarthy, fierce", "cethin: tywyll, ffyrnig"), ("Annwyl, Anwyl", "annwyl: dear, beloved", "annwyl"),
]

# The twenty commonest surnames in Wales: the six Welsh telephone directories of 1986, in thousands (fam-onename)
TOP = [
    ("Jones", 60.57, "From John: in Welsh Siôn or Ioan.", "O John: Siôn neu Ioan yn Gymraeg."),
    ("Williams", 37.81, "From William: Gwilym.", "O William: Gwilym."),
    ("Davies", 36.76, "From Dafydd, the name of the patron saint.", "O Dafydd, enw’r nawddsant."),
    ("Evans", 24.66, "From Ifan or Ieuan, the Welsh forms of John.", "O Ifan neu Ieuan, ffurfiau Cymraeg ar John."),
    ("Thomas", 22.97, "From Tomos.", "O Tomos."),
    ("Roberts", 17.14, "From Robert, a favourite in the north.", "O Robert, ffefryn yn y gogledd."),
    ("Hughes", 13.38, "From Huw.", "O Huw."),
    ("Lewis", 12.96, "Often for Llywelyn, the name of the two great princes.", "Yn aml am Llywelyn, enw’r ddau dywysog mawr."),
    ("Morgan", 11.70, "An old Welsh name, borne by the kings who gave Morgannwg its name.", "Hen enw Cymraeg, enw’r brenhinoedd a roddodd ei enw i Forgannwg."),
    ("Griffiths", 10.90, "From Gruffudd, a name of kings and princes.", "O Gruffudd, enw brenhinoedd a thywysogion."),
    ("Edwards", 10.33, "From Edward, often standing for Iorwerth.", "O Edward, yn aml yn lle Iorwerth."),
    ("Owen", 8.85, "From Owain, the name of Owain Gwynedd and Owain Glyndŵr.", "O Owain, enw Owain Gwynedd ac Owain Glyndŵr."),
    ("James", 7.66, "From James: Iago.", "O James: Iago."),
    ("Morris", 7.50, "From Morys.", "O Morys."),
    ("Price", 7.50, "From ap Rhys, son of Rhys.", "O ap Rhys."),
    ("Rees", 7.30, "From Rhys, the name of the kings and princes of Deheubarth.", "O Rhys, enw brenhinoedd a thywysogion Deheubarth."),
    ("Phillips", 6.34, "From Phylip.", "O Phylip."),
    ("Jenkins", 6.23, "From Siencyn, a pet form of John.", "O Siencyn, ffurf anwes ar John."),
    ("Harris", 5.79, "From Harri.", "O Harri."),
    ("Lloyd", 5.64, "From llwyd, grey.", "O llwyd."),
]

# Step by step: (title EN, title CY, text EN, text CY, [(url, label EN, label CY)])
STEPS = [
    ("Start at home", "Dechrau gartref",
     "Write down what your family already knows: names, dates, farms, chapels and towns. Ask the oldest relatives first. Look for the family Bible, where births and deaths were often written inside the cover, and for memorial cards, chapel membership cards, letters and photographs. Every name and place you have now saves hours later.",
     "Ysgrifennwch yr hyn y mae eich teulu’n ei wybod yn barod: enwau, dyddiadau, ffermydd, capeli a threfi. Holwch yr hynaf yn gyntaf. Chwiliwch am Feibl y teulu, lle byddai genedigaethau a marwolaethau’n aml wedi’u hysgrifennu y tu mewn i’r clawr, ac am gardiau coffa, cardiau aelodaeth capel, llythyrau a lluniau. Mae pob enw a lle sydd gennych nawr yn arbed oriau wedyn.",
     []),
    ("Birth, marriage and death certificates, from 1837", "Tystysgrifau geni, priodi a marw, o 1837",
     "Civil registration began in England and Wales in July 1837. Search the free index on FreeBMD, then order the certificate from the General Register Office. A birth certificate names both parents, a marriage certificate both fathers, so each one takes you a generation further back.[[cite:fam-freebmd]]",
     "Dechreuodd cofrestru sifil yng Nghymru a Lloegr ym mis Gorffennaf 1837. Chwiliwch y mynegai am ddim ar FreeBMD, yna archebwch y dystysgrif gan y Swyddfa Gofrestru Gyffredinol. Mae tystysgrif geni’n enwi’r ddau riant, a thystysgrif priodas y ddau dad, felly mae pob un yn mynd â chi genhedlaeth ymhellach yn ôl.[[cite:fam-freebmd]]",
     [("https://www.freebmd.org.uk/", "FreeBMD", "FreeBMD"), ("https://www.gov.uk/order-copy-birth-death-marriage-certificate", "Order a certificate", "Archebu tystysgrif")]),
    ("The census, every ten years from 1841", "Y cyfrifiad, bob deng mlynedd o 1841",
     "The census lists every household on one night: names, ages, jobs, where each person was born and, from 1851, how they were related. The returns from 1841 to 1921 are online; the 1931 census was lost to fire in 1942, and none was taken in 1941. From 1891 the census in Wales asked which language each person spoke, so you may find your family written down as Welsh speakers.[[cite:fam-tna-census,fam-1891]]",
     "Mae’r cyfrifiad yn rhestru pob aelwyd ar un noson: enwau, oed, gwaith, ble y ganed pob person ac, o 1851, sut roedden nhw’n perthyn. Mae’r ffurflenni o 1841 hyd 1921 ar-lein; collwyd cyfrifiad 1931 mewn tân yn 1942, ac ni chymerwyd un yn 1941. O 1891 ymlaen gofynnai’r cyfrifiad yng Nghymru pa iaith a siaradai pob person, felly efallai y gwelwch eich teulu wedi’u cofnodi’n siaradwyr Cymraeg.[[cite:fam-tna-census,fam-1891]]",
     [("https://www.nationalarchives.gov.uk/help-with-your-research/research-guides/census-records", "Census guide", "Canllaw’r cyfrifiad"), ("https://www.familysearch.org/", "FamilySearch (free)", "FamilySearch (am ddim)")]),
    ("Parish registers and the bishop’s copies", "Cofrestri plwyf a chopïau’r esgob",
     "Before 1837, baptisms, marriages and burials were written in the parish register, kept by order from 1538. The originals are now in the county archives, and many are indexed online. Each year a copy went to the bishop, and these bishop’s transcripts, at the National Library of Wales, run from 1598 to about 1860; they can fill a gap where a register is lost.[[cite:fam-nlw-church]]",
     "Cyn 1837 ysgrifennid bedyddiadau, priodasau a chladdedigaethau yng nghofrestr y plwyf, a gedwid drwy orchymyn o 1538. Mae’r rhai gwreiddiol yn yr archifdai sirol heddiw, a llawer wedi’u mynegeio ar-lein. Bob blwyddyn âi copi at yr esgob, ac mae trawsgrifiadau’r esgob, yn Llyfrgell Genedlaethol Cymru, yn rhedeg o 1598 hyd tua 1860; gallant lenwi bwlch lle collwyd cofrestr.[[cite:fam-nlw-church]]",
     [("https://archives.wales/", "Archives Wales", "Archifau Cymru"), ("https://library.wales/information-for/family-historians/records/church-in-wales-records", "Church records at the Library", "Cofnodion yr eglwys yn y Llyfrgell")]),
    ("Chapel records", "Cofnodion y capeli",
     "Wales was a land of chapels: by 1851 about three in every four worshippers went to chapel. Chapel registers from before 1837 are at The National Archives in Kew and can be searched online; later ones are in the county archives or still with the chapel. Remember that from 1754 to 1837 chapel families had to marry in the parish church, so look for their weddings there. Chapel histories, anniversary books and the denominational magazines often name members, deacons and ministers.[[cite:fam-familysearch,fam-nlw-chapel]]",
     "Gwlad y capeli oedd Cymru: erbyn 1851 âi tua thri o bob pedwar addolwr i’r capel. Mae cofrestri capeli o cyn 1837 yn yr Archifau Gwladol yn Kew a gellir eu chwilio ar-lein; mae rhai diweddarach yn yr archifdai sirol neu gyda’r capel o hyd. Cofiwch fod yn rhaid i deuluoedd y capel briodi yn eglwys y plwyf rhwng 1754 ac 1837, felly chwiliwch am eu priodasau yno. Mae hanesion capeli, llyfrau dathlu a chylchgronau’r enwadau’n aml yn enwi aelodau, diaconiaid a gweinidogion.[[cite:fam-familysearch,fam-nlw-chapel]]",
     [("https://www.library.wales/information-for/family-historians/records/nonconformist-records", "Chapel records at the Library", "Cofnodion capeli yn y Llyfrgell")]),
    ("Wills", "Ewyllysiau",
     "Before 1858, wills in Wales were proved in the church courts, and the National Library of Wales holds them all: about 190,000 wills, from about 1521 to 1858, put online for anyone to read. A will names children, grandchildren, farms and even the family’s best bed. Wills from 1858 onwards are found through the government’s probate search.[[cite:fam-wills]]",
     "Cyn 1858 profid ewyllysiau yng Nghymru yn y llysoedd eglwysig, ac mae Llyfrgell Genedlaethol Cymru yn eu cadw i gyd: tua 190,000 o ewyllysiau, o tua 1521 hyd 1858, wedi’u rhoi ar-lein i bawb eu darllen. Mae ewyllys yn enwi plant, wyrion, ffermydd a hyd yn oed gwely gorau’r teulu. Ceir ewyllysiau o 1858 ymlaen drwy chwiliad profiant y llywodraeth.[[cite:fam-wills]]",
     [("https://www.library.wales/discover/nlw-resources/wills/", "Welsh wills before 1858", "Ewyllysiau Cymru cyn 1858"), ("https://probatesearch.service.gov.uk/", "Wills after 1858", "Ewyllysiau ar ôl 1858")]),
    ("Tithe maps: find the farm", "Mapiau’r degwm: dod o hyd i’r fferm",
     "In the years after 1836 a map was drawn of every parish, with a book naming the owner and the tenant of each field, its name, its use and its size. On the National Library’s Places of Wales site you can find your family’s farm, walk its fields by name and lay the old map over today’s.[[cite:fam-tithe]]",
     "Yn y blynyddoedd ar ôl 1836 lluniwyd map o bob plwyf, gyda llyfr yn enwi perchennog a thenant pob cae, ei enw, ei ddefnydd a’i faint. Ar wefan Lleoedd Cymru y Llyfrgell Genedlaethol gallwch ddod o hyd i fferm eich teulu, cerdded ei chaeau wrth eu henwau a gosod yr hen fap dros fap heddiw.[[cite:fam-tithe]]",
     [("https://places.library.wales/", "Places of Wales", "Lleoedd Cymru")]),
    ("Newspapers, in Welsh and English", "Papurau newydd, yn Gymraeg ac yn Saesneg",
     "Welsh Newspapers Online holds more than a million pages from 120 papers, from 1804 to 1919, free to search. Look for obituaries, chapel news, eisteddfod prizes, emigrants’ letters home, accidents at the pit and quarry, and the columns of local news where your people may appear by name and farm.[[cite:fam-wno]]",
     "Mae gan Bapurau Newydd Cymru Ar-lein fwy na miliwn o dudalennau o 120 o bapurau, o 1804 hyd 1919, i’w chwilio am ddim. Chwiliwch am ysgrifau coffa, newyddion y capel, gwobrau eisteddfod, llythyrau ymfudwyr adref, damweiniau yn y pwll a’r chwarel, a’r colofnau newyddion lleol lle gall eich pobl ymddangos wrth eu henw a’u fferm.[[cite:fam-wno]]",
     [("https://newspapers.library.wales/", "Welsh Newspapers Online", "Papurau Newydd Cymru Ar-lein")]),
    ("Visit, or ask for help", "Ymweld, neu ofyn am help",
     "The National Library of Wales in Aberystwyth and the county archives of Wales welcome family historians, and many records that are not online can be seen there. Local family history societies know their own parishes, chapels and graveyards better than anyone.",
     "Mae Llyfrgell Genedlaethol Cymru yn Aberystwyth ac archifdai sirol Cymru yn croesawu haneswyr teulu, a gellir gweld yno lawer o gofnodion nad ydynt ar-lein. Mae cymdeithasau hanes teulu lleol yn adnabod eu plwyfi, eu capeli a’u mynwentydd eu hunain yn well na neb.",
     [("https://www.library.wales/information-for/family-historians", "The Library for family historians", "Y Llyfrgell i haneswyr teulu"), ("https://archives.wales/", "Archives Wales", "Archifau Cymru")]),
]

# Which records cover a year: (from, to, title EN, title CY, note EN, note CY, url)
RECORDS = [
    (300, 1613, "Pedigrees of the kings, princes and gentry", "Achau’r brenhinoedd, y tywysogion a’r bonedd",
     "Bartrum’s Welsh Genealogies (AD 300–1500) and the herald Lewys Dwnn’s visitations of 1586 to 1613.", "Welsh Genealogies Bartrum (300–1500 OC) ac ymweliadau’r herodr Lewys Dwnn rhwng 1586 a 1613.",
     "https://research.aber.ac.uk/en/datasets/bartrum-genealogical-project/"),
    (1521, 1858, "Wills proved in the church courts of Wales", "Ewyllysiau a brofwyd yn llysoedd eglwysig Cymru",
     "About 190,000 wills, free online at the National Library of Wales.", "Tua 190,000 o ewyllysiau, am ddim ar-lein yn Llyfrgell Genedlaethol Cymru.",
     "https://www.library.wales/discover/nlw-resources/wills/"),
    (1538, 1950, "Parish registers", "Cofrestri plwyf",
     "Baptisms, marriages and burials, in the county archives; few early Welsh ones survive.", "Bedyddiadau, priodasau a chladdedigaethau, yn yr archifdai sirol; ychydig o rai cynnar Cymru sydd wedi goroesi.",
     "https://archives.wales/"),
    (1598, 1860, "Bishop’s transcripts", "Trawsgrifiadau’r esgob",
     "Yearly copies of the parish registers, at the National Library; few before 1660.", "Copïau blynyddol o gofrestri’r plwyf, yn y Llyfrgell Genedlaethol; ychydig cyn 1660.",
     "https://library.wales/information-for/family-historians/records/church-in-wales-records"),
    (1616, 1837, "Marriage bonds and allegations", "Bondiau a datganiadau priodas",
     "For marriages by licence instead of banns, indexed at the National Library.", "Ar gyfer priodasau drwy drwydded yn lle gostegion, wedi’u mynegeio yn y Llyfrgell Genedlaethol.",
     "https://library.wales/information-for/family-historians/records/church-in-wales-records"),
    (1700, 1950, "Chapel registers", "Cofrestri capeli",
     "Before 1837 at The National Archives in Kew; later ones in the county archives or the chapel.", "Cyn 1837 yn yr Archifau Gwladol yn Kew; rhai diweddarach yn yr archifdai sirol neu’r capel.",
     "https://www.library.wales/information-for/family-historians/records/nonconformist-records"),
    (1754, 1837, "Chapel families married in church", "Teuluoedd y capel yn priodi yn yr eglwys",
     "Everyone but Quakers and Jews married in the parish church: look in its register.", "Priodai pawb ond y Crynwyr a’r Iddewon yn eglwys y plwyf: chwiliwch ei chofrestr.",
     "https://www.library.wales/information-for/family-historians/records/nonconformist-records"),
    (1804, 1919, "Welsh Newspapers Online", "Papurau Newydd Cymru Ar-lein",
     "More than a million pages, in Welsh and English, free.", "Mwy na miliwn o dudalennau, yn Gymraeg ac yn Saesneg, am ddim.",
     "https://newspapers.library.wales/"),
    (1836, 1860, "Tithe maps", "Mapiau’r degwm",
     "Every field, its owner and its tenant, on Places of Wales.", "Pob cae, ei berchennog a’i denant, ar wefan Lleoedd Cymru.",
     "https://places.library.wales/"),
    (1837, 1950, "Birth, marriage and death certificates", "Tystysgrifau geni, priodi a marw",
     "The free index on FreeBMD; certificates from the General Register Office.", "Y mynegai am ddim ar FreeBMD; tystysgrifau gan y Swyddfa Gofrestru Gyffredinol.",
     "https://www.freebmd.org.uk/"),
    (1841, 1921, "The census", "Y cyfrifiad",
     "Every ten years; in Wales the language each person spoke is given from 1891. Lost: 1931. Not taken: 1941.", "Bob deng mlynedd; yng Nghymru rhoddir iaith pob person o 1891. Collwyd: 1931. Ni chymerwyd: 1941.",
     "https://www.nationalarchives.gov.uk/help-with-your-research/research-guides/census-records"),
    (1858, 1950, "Wills after 1858", "Ewyllysiau ar ôl 1858",
     "Through the government’s probate search.", "Drwy chwiliad profiant y llywodraeth.",
     "https://probatesearch.service.gov.uk/"),
    (1939, 1939, "The 1939 Register", "Cofrestr 1939",
     "Taken on the eve of war in place of a census, free to search on FamilySearch.", "Fe’i cymerwyd ar drothwy’r rhyfel yn lle cyfrifiad, i’w chwilio am ddim ar FamilySearch.",
     "https://www.familysearch.org/"),
]

TIPS = [
    ("Look for the farm name", "Chwiliwch am enw’r fferm",
     "With so many people called John Jones, the country knew them by their home: John Jones, Tŷ Coch, or Jac Penlan. The census, the chapel books and the tithe map all give the farm, and it is often the surest way to tell one family from another.",
     "Gyda chynifer o bobl o’r enw John Jones, roedd y wlad yn eu hadnabod wrth eu cartref: John Jones, Tŷ Coch, neu Jac Penlan. Mae’r cyfrifiad, llyfrau’r capel a map y degwm i gyd yn rhoi’r fferm, ac yn aml dyna’r ffordd sicraf o wahaniaethu rhwng un teulu ac un arall."),
    ("Expect a name in two languages", "Disgwyliwch enw mewn dwy iaith",
     "The same person can be Dafydd in the chapel book and David on the census, Gwilym and William, Siân and Jane, Ieuan and Evan or John. The oldest registers are often in Latin, too: Johannes, Davidus, Gulielmus.",
     "Gall yr un person fod yn Dafydd yn llyfr y capel ac yn David ar y cyfrifiad, Gwilym a William, Siân a Jane, Ieuan ac Evan neu John. Mae’r cofrestri hynaf yn aml yn Lladin hefyd: Johannes, Davidus, Gulielmus."),
    ("Watch the surname change", "Gwyliwch y cyfenw’n newid",
     "Where the old way lasted, a surname can change in a single generation: the son of Thomas Evans may be William Thomas, and his son Evan Williams. Follow the first names, not only the surnames.",
     "Lle parhaodd yr hen ffordd, gall cyfenw newid mewn un genhedlaeth: gall mab Thomas Evans fod yn William Thomas, a’i fab yntau yn Evan Williams. Dilynwch yr enwau cyntaf, nid y cyfenwau’n unig."),
    ("Find the chapel family’s wedding in church", "Chwiliwch am briodas teulu’r capel yn yr eglwys",
     "Between 1754 and 1837 even the most faithful chapel families married in the parish church, so their weddings are in the parish register while their children’s baptisms are in the chapel’s.",
     "Rhwng 1754 ac 1837 priodai hyd yn oed y teuluoedd capel ffyddlonaf yn eglwys y plwyf, felly mae eu priodasau yng nghofrestr y plwyf a bedyddiadau eu plant yng nghofrestr y capel."),
    ("Know the bardic names", "Adnabod yr enwau barddol",
     "Poets, ministers and musicians often went by a bardic name. Hedd Wyn was Ellis Humphrey Evans of Yr Ysgwrn, and Islwyn was the poet William Thomas. A bardic name in a newspaper or on a gravestone can lead you to a whole life.",
     "Âi beirdd, gweinidogion a cherddorion yn aml wrth enw barddol. Ellis Humphrey Evans o’r Ysgwrn oedd Hedd Wyn, ac Islwyn oedd y bardd William Thomas. Gall enw barddol mewn papur newydd neu ar garreg fedd eich arwain at fywyd cyfan."),
    ("Follow the family overseas", "Dilynwch y teulu dros y môr",
     "Welsh families settled in Pennsylvania from the 1680s, in the mining towns of America, in Patagonia from 1865 and across the world. Welsh newspapers printed their letters home, and the chapels they built kept their own registers.",
     "Ymsefydlodd teuluoedd o Gymru ym Mhennsylvania o’r 1680au, yn nhrefi glofaol America, ym Mhatagonia o 1865 a ledled y byd. Argraffai papurau Cymru eu llythyrau adref, a chadwai’r capeli a godwyd ganddynt eu cofrestri eu hunain."),
]

# Words you will meet on a Welsh gravestone or in a chapel book: (Welsh, English)
WORDS = [
    ("Er cof am", "In memory of"), ("Er serchus gof am", "In loving memory of"), ("annwyl briod", "dear husband or wife"),
    ("gwraig", "wife"), ("gŵr", "husband"), ("mab", "son"), ("merch", "daughter"), ("plentyn, plant", "child, children"),
    ("a fu farw", "who died"), ("hunodd", "fell asleep (died)"), ("yn … mlwydd oed", "aged …"), ("o’r plwyf hwn", "of this parish"),
    ("bedyddiwyd", "was baptised"), ("priodwyd", "were married"), ("claddwyd", "was buried"), ("aelod", "member (of the chapel)"),
]

BACK_EN = [
    "If your line reaches one of the old gentry families, the pedigrees of Wales may carry it much further. The poets kept the descents of the families they sang to, and in 1585 Lewys Dwnn of Betws Cedewain was made deputy herald for the whole of Wales. Until 1614 he rode from house to house writing down each family’s line, and his books were printed in 1846 as the Heraldic Visitations of Wales.[[cite:fam-dwnn]]",
    "In the twentieth century the scholar Peter Bartrum gathered every Welsh pedigree he could find into Welsh Genealogies AD 300–1400 and AD 1400–1500, tracing families back to the Fifteen Noble Tribes of Gwynedd, to the saints and to the kings and princes. His volumes are now free to read online.[[cite:fam-bartrum]]",
    "Many families of Wales can trace a line, through a daughter or a younger son, to the royal houses of Gwynedd, Deheubarth or Powys. Our royal family trees show the main lines of each.",
]
BACK_CY = [
    "Os yw eich llinach yn cyrraedd un o hen deuluoedd y bonedd, gall achau Cymru fynd â hi lawer ymhellach. Cadwai’r beirdd achau’r teuluoedd y canent iddynt, ac yn 1585 gwnaed Lewys Dwnn o Fetws Cedewain yn ddirprwy herodr dros Gymru gyfan. Hyd 1614 marchogodd o dŷ i dŷ yn ysgrifennu llinach pob teulu, ac argraffwyd ei lyfrau yn 1846 fel Heraldic Visitations of Wales.[[cite:fam-dwnn]]",
    "Yn yr ugeinfed ganrif casglodd yr ysgolhaig Peter Bartrum bob ach Gymreig y gallai ddod o hyd iddi yn Welsh Genealogies AD 300–1400 ac AD 1400–1500, gan olrhain teuluoedd yn ôl at Bymtheg Llwyth Bonheddig Gwynedd, at y seintiau ac at y brenhinoedd a’r tywysogion. Mae ei gyfrolau ar gael i’w darllen am ddim ar-lein bellach.[[cite:fam-bartrum]]",
    "Gall llawer o deuluoedd Cymru olrhain llinach, drwy ferch neu fab iau, at dai brenhinol Gwynedd, Deheubarth neu Bowys. Mae ein coed teulu brenhinol yn dangos prif linachau pob un.",
]


def _span(a, b):
    bi = g["bi"]
    if a == b:
        return str(a)
    if b >= 1950:
        return bi(f"{a} on", f"{a} ymlaen")
    return f"{a}–{b}"


def _ext(url, en, cy):
    bi = g["bi"]
    return f'<a class="btn" href="{url}" rel="noopener" target="_blank">{bi(en, cy)} <span aria-hidden="true">↗</span></a>'


def page():
    bi, e, section, hero, prose_bi, SITE, PERSON = g["bi"], g["e"], g["section"], g["hero"], g["prose_bi"], g["SITE"], g["PERSON"]

    jump = ('<nav class="chips l-jump" aria-label="Sections / Adrannau">' + "".join(
        f'<a class="chip" href="#{h}">{bi(a, b)}</a>' for h, a, b in (
            ("fh-names", "Ap and ferch", "Ap a ferch"), ("fh-surnames", "Surnames", "Cyfenwau"), ("fh-steps", "Step by step", "Gam wrth gam"),
            ("fh-records", "Which records?", "Pa gofnodion?"), ("fh-tips", "Tips", "Cynghorion"), ("fh-back", "Further back", "Ymhellach yn ôl"))) + "</nav>")

    # Gerald's pedigree, newest first, each name joined by "ap"
    links = []
    for k, (en, cy, pid) in enumerate(PEDIGREE):
        d = PERSON[pid][2] if pid and pid in PERSON else ""
        inner = f'<b>{bi(en, cy)}</b>' + (f'<small>{e(d)}</small>' if d else "")
        box = f'<a href="person-{pid}.html">{inner}</a>' if pid and pid in PERSON else f"<span>{inner}</span>"
        links.append(f'<li><span class="fh-n">{k + 1}</span>{box}</li>')
    chain = (f'<figure class="fh-chain"><figcaption>{bi("Rhys ap Gruffudd ap Rhys ap Tewdwr ab Einion ab Owain ap Hywel ap Cadell ap Rhodri", "Rhys ap Gruffudd ap Rhys ap Tewdwr ab Einion ab Owain ap Hywel ap Cadell ap Rhodri")}</figcaption>'
             f'<ol>{"".join(links)}</ol><p class="fh-cap">{bi("Each name is the son of the one below it: nine generations, from the Lord Rhys (died 1197) to Rhodri Mawr (died 878).", "Mae pob enw’n fab i’r un oddi tano: naw cenhedlaeth, o’r Arglwydd Rhys (bu farw 1197) hyd Rodri Mawr (bu farw 878).")}</p></figure>')

    names_btn = (f'<p class="l-links"><a class="btn solid" href="names.html">{bi("Make your own name the old Welsh way", "Gwnewch eich enw eich hun yn yr hen ffordd Gymreig")} →</a>'
                 f'<a class="btn" href="family-trees.html">{bi("Royal family trees", "Coed teulu brenhinol")} →</a></p>')

    def pairs(rows, cls):
        return f'<ul class="fh-pairs {cls}">' + "".join(
            f'<li><b>{e(a)}</b><span>{bi(b, c)}</span></li>' for a, b, c in rows) + "</ul>"

    top = TOP[0][1]
    bars = ('<ol class="fh-top">' + "".join(
        f'<li><span class="fh-r">{i + 1}</span><b>{e(n)}</b><span class="fh-bar" style="--w:{v / top * 100:.1f}%"><i></i><em>{v:.1f}k</em></span>'
        f'<span class="fh-o">{bi(a, b)}</span></li>' for i, (n, v, a, b) in enumerate(TOP)) + "</ol>"
            f'<p class="fh-cap">{bi("Entries in the six Welsh telephone directories of 1986, in thousands.", "Cofnodion yn chwe chyfeirlyfr ffôn Cymru yn 1986, mewn miloedd.")}[[cite:fam-onename]]</p>')

    steps = '<ol class="fh-steps">' + "".join(
        f'<li><h3>{bi(t, tc)}</h3><p>{bi(x, xc)}</p>' + (f'<p class="fh-go">{"".join(_ext(u, a, b) for u, a, b in ls)}</p>' if ls else "") + "</li>"
        for t, tc, x, xc, ls in STEPS) + "</ol>"
    # bi() escapes its text, which would show a [[cite:...]] marker's brackets as they are: they survive escaping, so the
    # chips are still made at the end of the build (CITE.render works on the finished page).

    recs = "".join(
        f'<li data-from="{a}" data-to="{b}"><span class="fh-yrs">{_span(a, b)}</span>'
        f'<a href="{u}" rel="noopener" target="_blank"><b>{bi(t, tc)}</b><span>{bi(x, xc)}</span></a></li>'
        for a, b, t, tc, x, xc, u in RECORDS)
    finder = (f'<div class="fh-find" id="fh-find"><label for="fh-year" class="fh-q">{bi("When did your ancestor live?", "Pryd roedd eich hynafiad yn byw?")}</label>'
              f'<div class="fh-slide"><input type="range" id="fh-year" min="1100" max="1950" step="10" value="1850" aria-describedby="fh-count">'
              f'<output for="fh-year" id="fh-out">1850</output></div>'
              f'<p class="fh-count" id="fh-count" aria-live="polite">{bi("Every kind of record is listed below. Move the slider to see which cover your year.", "Mae pob math o gofnod wedi’i restru isod. Symudwch y llithrydd i weld pa rai sy’n cwmpasu eich blwyddyn.")}</p>'
              f'<ul class="fh-recs" id="fh-recs">{recs}</ul></div>')

    tips = '<div class="fh-tips">' + "".join(f'<div><h3>{bi(t, tc)}</h3><p>{bi(x, xc)}</p></div>' for t, tc, x, xc in TIPS) + "</div>"
    words = ('<dl class="fh-words">' + "".join(f'<div><dt lang="cy">{e(w)}</dt><dd>{e(m)}</dd></div>' for w, m in WORDS) + "</dl>")

    more = (f'<p class="l-links"><a class="btn" href="names.html">{bi("Welsh names game", "Gêm enwau Cymraeg")} →</a>'
            f'<a class="btn" href="family-trees.html">{bi("Royal family trees", "Coed teulu brenhinol")} →</a>'
            f'<a class="btn" href="place-library.html">{bi("The National Library of Wales", "Llyfrgell Genedlaethol Cymru")} →</a>'
            f'<a class="btn" href="topic-abroad.html">{bi("The Welsh abroad", "Y Cymry ar wasgar")} →</a>'
            f'<a class="btn" href="towns.html">{bi("What your town’s name means", "Ystyr enw eich tref")} →</a></p>')

    main = (hero("revival", f'<a href="index.html">{SITE}</a>', "book", "Family history", "Hanes teulu",
                 "Finding your Welsh family", "Dod o hyd i’ch teulu Cymreig",
                 "The Welsh have always known who their people were. How the old names worked, where the great surnames came from, and how to find your own family in the records of Wales, step by step.",
                 "Mae’r Cymry wedi gwybod erioed pwy oedd eu pobl. Sut roedd yr hen enwau’n gweithio, o ble daeth y cyfenwau mawr, a sut i ddod o hyd i’ch teulu eich hun yng nghofnodion Cymru, gam wrth gam.",
                 art="book", extra=jump)
            + f'<section class="article"><div class="wrap narrow">{prose_bi(INTRO_EN, INTRO_CY)}{chain}</div></section>'
            + f'<section class="tight" id="fh-names"><div class="wrap narrow"><h2 class="sub-h">{bi("Ap and ferch: the Welsh way of naming", "Ap a ferch: ffordd y Cymry o enwi")}</h2>{prose_bi(NAMING_EN, NAMING_CY)}{names_btn}</div></section>'
            + f'<section class="tight" id="fh-surnames"><div class="wrap narrow"><h2 class="sub-h">{bi("From ap Hywel to Powell: how the surnames came", "O ap Hywel i Powell: sut y daeth y cyfenwau")}</h2>{prose_bi(SURNAMES_EN, SURNAMES_CY)}'
              f'<div class="fh-two"><div><h3>{bi("Where the ap stuck", "Lle glynodd yr ap")}</h3>{pairs(AP_NAMES, "ap")}</div>'
              f'<div><h3>{bi("Names from a Welsh word", "Enwau o air Cymraeg")}</h3>{pairs(WORD_NAMES, "word")}</div></div></div></section>'
            + f'<section class="tight" id="fh-top"><div class="wrap narrow"><h2 class="sub-h">{bi("The twenty commonest surnames in Wales", "Yr ugain cyfenw mwyaf cyffredin yng Nghymru")}</h2>{bars}</div></section>'
            + f'<section class="tight" id="fh-steps"><div class="wrap narrow"><h2 class="sub-h">{bi("Finding your Welsh ancestors, step by step", "Dod o hyd i’ch hynafiaid Cymreig, gam wrth gam")}</h2>{steps}</div></section>'
            + f'<section class="tight" id="fh-records"><div class="wrap narrow"><h2 class="sub-h">{bi("Which records cover your ancestor?", "Pa gofnodion sy’n cwmpasu eich hynafiad?")}</h2>{finder}</div></section>'
            + f'<section class="tight" id="fh-tips"><div class="wrap"><h2 class="sub-h">{bi("Tips for Welsh records", "Cynghorion ar gyfer cofnodion Cymru")}</h2>{tips}'
              f'<h3 class="fh-wh">{bi("Words you will meet on a Welsh gravestone", "Geiriau a welwch ar garreg fedd Gymraeg")}</h3>{words}</div></section>'
            + f'<section class="tight" id="fh-back"><div class="wrap narrow"><h2 class="sub-h">{bi("Further back: the pedigrees of Wales", "Ymhellach yn ôl: achau Cymru")}</h2>{prose_bi(BACK_EN, BACK_CY)}{more}</div></section>')
    return g["page"]("family-history.html", "Finding your Welsh family: surnames, ap and ferch, and tracing your ancestors · History of Wales",
                     "Welsh family history: how ap and ferch worked, where Jones, Davies, Powell and Price come from, and a step-by-step guide to finding Welsh ancestors in the census, parish and chapel registers, wills, tithe maps and newspapers.",
                     main, era="revival", og_type="article", active="family-history.html", track="page:family", extra=JS)


JS = r"""<script>(function(){
var r=document.getElementById("fh-year");if(!r)return;var o=document.getElementById("fh-out"),c=document.getElementById("fh-count"),li=document.querySelectorAll("#fh-recs li");
function cy(){return document.documentElement.lang==="cy"||document.documentElement.classList.contains("cy")}
function show(){var y=+r.value,n=0;o.textContent=y;[].forEach.call(li,function(x){var a=+x.dataset.from,b=+x.dataset.to;var on=y>=a-10&&y<=b+10;x.hidden=!on;if(on)n++});
c.textContent=n?(cy()?n+" math o gofnod ar gyfer "+y+":":n+(n===1?" kind of record":" kinds of record")+" for "+y+":"):(cy()?"Ychydig iawn o gofnodion sydd wedi goroesi o "+y+". Rhowch gynnig ar flwyddyn ddiweddarach.":"Very few records survive from "+y+". Try a later year.")}
r.addEventListener("input",show);show()})()</script>
"""


CSS = """
.fh-chain{margin:2rem 0 0;padding:1.3rem 1.3rem 1rem;background:var(--slate);border:1px solid var(--line);border-radius:14px}
.fh-chain figcaption{font-family:var(--f-display);font-size:1.15rem;line-height:1.45;margin:0 0 1rem;font-style:italic}
.fh-chain ol{list-style:none;margin:0;padding:0;display:grid;gap:.95rem}
.fh-chain li{display:grid;grid-template-columns:2rem 1fr;align-items:center;gap:.6rem;position:relative}
.fh-chain li + li::before{content:"ap";position:absolute;left:0;width:2rem;text-align:center;top:-.95rem;font-family:var(--f-mono);font-size:.7rem;line-height:.95rem;color:var(--muted)}
.fh-chain .fh-n{width:2rem;height:2rem;border-radius:50%;display:grid;place-items:center;background:var(--c,var(--gold));color:#111;font-weight:700;font-size:.85rem}
.fh-chain a,.fh-chain li>span:last-child{display:flex;flex-wrap:wrap;align-items:baseline;gap:.2rem .7rem;padding:.55rem .9rem;border:1px solid var(--line);border-radius:10px;color:inherit;text-decoration:none;background:var(--card,transparent)}
.fh-chain a:hover{border-color:var(--c,var(--gold))}
.fh-chain small{font-family:var(--f-mono);font-size:.75rem;color:var(--muted)}
.fh-cap{color:var(--muted);font-size:.9rem;margin:.8rem 0 0}
.fh-two{display:grid;gap:1.4rem;margin-top:1.6rem}
@media (min-width:44rem){.fh-two{grid-template-columns:1fr 1fr}}
.fh-two h3{font-family:var(--f-display);font-weight:400;font-size:1.3rem;margin:0 0 .7rem}
.fh-pairs{list-style:none;margin:0;padding:0;display:grid;gap:.4rem}
.fh-pairs li{display:grid;grid-template-columns:minmax(7rem,40%) 1fr;gap:.8rem;padding:.5rem .8rem;border-left:3px solid var(--c,var(--gold));background:var(--slate);border-radius:0 8px 8px 0}
.fh-pairs b{font-weight:700}
.fh-pairs span{color:var(--muted)}
.fh-top{list-style:none;margin:0;padding:0;display:grid;gap:.5rem}
.fh-top li{display:grid;grid-template-columns:1.8rem 6.5rem 1fr;grid-template-areas:"r n b" ". o o";gap:.15rem .7rem;align-items:center}
.fh-r{grid-area:r;font-family:var(--f-mono);font-size:.8rem;color:var(--muted);text-align:right}
.fh-top b{grid-area:n;font-family:var(--f-display);font-weight:400;font-size:1.2rem}
.fh-bar{grid-area:b;display:flex;align-items:center;gap:.5rem;min-width:0}
.fh-bar i{display:block;height:.75rem;width:var(--w);background:var(--c,var(--gold));border-radius:0 4px 4px 0;flex:none;max-width:calc(100% - 3.5rem)}
.fh-bar em{font-style:normal;font-family:var(--f-mono);font-size:.75rem;color:var(--muted)}
.fh-o{grid-area:o;color:var(--muted);font-size:.9rem}
.fh-steps{list-style:none;counter-reset:fh;margin:0;padding:0;display:grid;gap:1rem}
.fh-steps li{counter-increment:fh;position:relative;padding:1.1rem 1.2rem 1.1rem 3.6rem;background:var(--slate);border:1px solid var(--line);border-radius:14px}
.fh-steps li::before{content:counter(fh);position:absolute;left:1rem;top:1rem;width:1.9rem;height:1.9rem;border-radius:50%;display:grid;place-items:center;background:var(--c,var(--gold));color:#111;font-weight:700}
.fh-steps h3{font-family:var(--f-display);font-weight:400;font-size:1.35rem;margin:0 0 .4rem}
.fh-steps p{margin:0;line-height:1.6}
.fh-go{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem!important}
.fh-go .btn{font-size:.9rem}
.fh-find{background:var(--slate);border:1px solid var(--line);border-radius:14px;padding:1.2rem 1.2rem 1rem}
.fh-q{display:block;font-family:var(--f-display);font-size:1.3rem;margin-bottom:.6rem}
.fh-slide{display:flex;align-items:center;gap:1rem}
.fh-slide input{flex:1;min-width:0;accent-color:var(--c,var(--gold));height:2.75rem}
.fh-slide output{font-family:var(--f-mono);font-size:1.4rem;min-width:3.5rem;text-align:right;color:var(--c,var(--gold))}
.fh-count{color:var(--muted);margin:.4rem 0 .8rem}
.fh-recs{list-style:none;margin:0;padding:0;display:grid;gap:.45rem}
.fh-recs li{display:grid;grid-template-columns:6.5rem 1fr;gap:.8rem;align-items:start}
.fh-yrs{font-family:var(--f-mono);font-size:.8rem;color:var(--c,var(--gold));padding-top:.7rem}
.fh-recs a{display:grid;gap:.15rem;padding:.6rem .85rem;border:1px solid var(--line);border-radius:10px;color:inherit;text-decoration:none;background:var(--card,transparent)}
.fh-recs a:hover{border-color:var(--c,var(--gold))}
.fh-recs a b{color:var(--ink)}
.fh-recs a span{color:var(--muted);font-size:.92rem}
.fh-tips{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,19rem),1fr));gap:1rem}
.fh-tips>div{background:var(--slate);border:1px solid var(--line);border-top:3px solid var(--c,var(--gold));border-radius:14px;padding:1rem 1.2rem}
.fh-tips h3{font-family:var(--f-display);font-weight:400;font-size:1.3rem;margin:0 0 .4rem}
.fh-tips p{margin:0;line-height:1.55}
.fh-wh{font-family:var(--f-display);font-weight:400;font-size:1.45rem;margin:2.2rem 0 .8rem}
.fh-words{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,14rem),1fr));gap:.5rem;margin:0}
.fh-words div{border-left:3px solid var(--c,var(--gold));padding:.3rem 0 .3rem .8rem}
.fh-words dt{font-weight:700}
.fh-words dd{margin:.1rem 0 0;color:var(--muted)}
@media (max-width:30rem){.fh-top li{grid-template-columns:1.5rem 5.5rem 1fr}.fh-recs li{grid-template-columns:1fr}.fh-yrs{padding-top:0}.fh-pairs li{grid-template-columns:1fr;gap:.1rem}}
"""
