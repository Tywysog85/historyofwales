"""A web page for every book in the reading lists that has no link of its own.

The home page Further reading list (READING in data.py) and every page's reading list
(refs.py, refs2.py, and so the Books and authors page too) look a book up here when it
has no url. Each entry: (author as written in the lists, title, url). A list item matches
when its author starts with the author here and its title is the same.

Prefer the publisher's own page for the book. A book long out of print gets its
Open Library record (openlibrary.org, the Internet Archive's free catalogue), which says
which libraries hold it and lets readers borrow a scan where there is one.
Every address was opened and checked on 2026-11-13.
"""

BOOKS = [
    ("John Davies", "A History of Wales",
     "https://www.penguin.co.uk/books/25362/a-history-of-wales-by-john-davies/9780140284751"),
    ("Gwyn A. Williams", "When Was Wales?",
     "https://openlibrary.org/books/OL14949719M/When_was_Wales"),
    ("Gwyn A. Williams", "When Was Wales? A History of the Welsh",
     "https://openlibrary.org/books/OL14949719M/When_was_Wales"),
    ("Geraint H. Jenkins", "A Concise History of Wales",
     "https://www.cambridge.org/core/books/concise-history-of-wales/353F60F13D445595973DDB9430EBCB70"),
    ("Wendy Davies", "Wales in the Early Middle Ages",
     "https://openlibrary.org/books/OL3279132M/Wales_in_the_Early_Middle_Ages"),
    ("Roger Turvey", "The Welsh Princes, 1063–1283",
     "https://www.routledge.com/The-Welsh-Princes-The-Native-Rulers-of-Wales-1063-1283/Turvey/p/book/9780582308114"),
    ("J. Beverley Smith", "Llywelyn ap Gruffudd, Prince of Wales",
     "https://uwp.co.uk/book/llywelyn-ap-gruffudd"),
    ("R. R. Davies", "The Age of Conquest: Wales 1063–1415",
     "https://academic.oup.com/book/26898"),
    ("R. R. Davies", "The Revolt of Owain Glyn Dŵr",
     "https://openlibrary.org/books/OL1279044M/The_revolt_of_Owain_Glyn_Dw%CC%82r"),
    ("Kenneth O. Morgan", "Rebirth of a Nation: Wales 1880–1980",
     "https://openlibrary.org/books/OL7397667M/Rebirth_of_a_Nation"),
    ("Martin Johnes", "Wales since 1939",
     "https://manchesteruniversitypress.co.uk/9780719086670"),
    ("Jan Morris", "Wales: Epic Views of a Small Country",
     "https://www.penguin.co.uk/books/24439/wales-by-morris-jan/9780241970249"),
    ("Jan Morris", "The Matter of Wales: Epic Views of a Small Country",
     "https://www.penguin.co.uk/books/24439/wales-by-morris-jan/9780241970249"),
    # old books: a free scan to read online (Internet Archive, Project Gutenberg)
    ("J. Gwenogvryn Evans and John Rhys", "The Text of the Book of Llan Dâv",
     "https://archive.org/details/cu31924028051559"),
    ("J. E. Lloyd", "A History of Wales from the Earliest Times to the Edwardian Conquest",
     "https://archive.org/details/historyofwalesfr01lloyuoft"),
    ("Theophilus Evans", "Drych y Prif Oesoedd",
     "https://archive.org/details/drychyprifoesoed00evan"),
    ("Lady Charlotte Guest", "The Mabinogion",
     "https://www.gutenberg.org/ebooks/5160"),
    ("Lady Charlotte Guest", "The Mabinogion, from the Llyfr Coch o Hergest, and other ancient Welsh manuscripts",
     "https://www.gutenberg.org/ebooks/5160"),
    ("Edward Maunde Thompson", "Chronicon Adae de Usk, A.D. 1377–1421",
     "https://archive.org/details/chroniconadaedeu00adamuoft"),
    ("John Rhys", "Celtic Folklore: Welsh and Manx",
     "https://www.gutenberg.org/ebooks/55025"),
    ("Wirt Sikes", "British Goblins: Welsh Folk-lore, Fairy Mythology, Legends and Traditions",
     "https://www.gutenberg.org/ebooks/34704"),
    ("Elias Owen", "Welsh Folk-Lore",
     "https://gutenberg.org/cache/epub/20096/pg20096-images.html"),
    ("David Powel", "The Historie of Cambria, now called Wales",
     "https://archive.org/download/historieofcambri00cara/historieofcambri00cara.pdf"),
    ("J. A. Giles", "Six Old English Chronicles",
     "https://archive.org/details/sixoldenglishch01gilegoog"),
    ("Matthew Arnold", "On the Study of Celtic Literature",
     "https://www.gutenberg.org/ebooks/5159"),
    ("Taliesin Williams", "Iolo Manuscripts",
     "https://archive.org/details/iolomanuscriptss00will/iolomanuscriptss00will"),
    ("Thomas Stephens", "Madoc: An Essay on the Discovery of America by Madoc ap Owen Gwynedd in the Twelfth Century",
     "https://archive.org/download/cu31924028727489/cu31924028727489.pdf"),
    ("Robert Southey", "Madoc",
     "https://openlibrary.org/books/OL23340695M"),
    ("Sebastian Evans", "Histories of the Kings of Britain, by Geoffrey of Monmouth",
     "https://openlibrary.org/works/OL2479707W"),
    ("Edward Lhuyd", "Archaeologia Britannica, volume I: Glossography",
     "https://leme.library.utoronto.ca/lexicons/1369"),
    ("Commissioners of Inquiry", "Reports of the Commissioners of Inquiry into the State of Education in Wales",
     "https://artsandculture.google.com/asset/the-blue-books-of-1847-reports-of-the-commissioners-of-inquiry-into-the-state-of-education-in-wales/cQE-QgCOrjTOPg"),
    ("R. R. W. Lingen", "Reports of the Commissioners of Inquiry into the State of Education in Wales",
     "https://artsandculture.google.com/asset/the-blue-books-of-1847-reports-of-the-commissioners-of-inquiry-into-the-state-of-education-in-wales/cQE-QgCOrjTOPg"),
    ("Daniel Owen", "Rhys Lewis",
     "https://www.library.wales/discover-learn/digital-exhibitions/books/prose-and-novels/hunangofiant-rhys-lewis-gweinidog-bethel"),
    ("J. Gwenogvryn Evans", "The White Book Mabinogion",
     "https://archive.org/details/whitebookofmabin00evan"),
    ("D. E. Jenkins", "Bedd Gelert: Its Facts, Fairies, and Folk-lore",
     "https://openlibrary.org/works/OL231169W"),
    ("Thomas Taylor", "The Life of St. Samson of Dol",
     "https://llanerchpress.com/book/category/lives-of-saints/6/the-life-of-saint-samson-of-dol/thomas-taylor/0947992774"),
    ("John Williams ab Ithel", "The Physicians of Myddvai: Meddygon Myddfai",
     "https://wellcomecollection.org/works/mebvns2s"),
    ("Owen Jones", "The Myvyrian Archaiology of Wales",
     "https://catalog.hathitrust.org/Record/102969426"),
]


def link(author, title):
    """The checked web page for this book, or "" if there is none here."""
    for a, t, u in BOOKS:
        if t == title and author.startswith(a):
            return u
    return ""


# ---------- where to buy (Ifan, 2026-11-13: "link the books to where to buy them from, amazon etc") ----------
# Every book on the Books and authors page and in the home Further reading list gets two shop links:
# Amazon UK (new copies) and AbeBooks (new and second-hand, so out-of-print and old books are covered too).
# They are search links built from the title and author, so they never go stale. No affiliate tags.
from urllib.parse import quote_plus as _q
import re as _re

NO_BUY = {"The Bible", "Trysorfa y Plant", "The South Wales Coal Annual"}   # not books you can buy as such


def _who(author):
    a = _re.sub(r"\([^)]*\)", "", author)                 # "(ed.)", "(trans.)", "(Alan Wilson and Baram Blackett)"
    a = _re.split(r",| and | trans\. | translated by ", a)[0]
    return a.strip()


def buy(author, title, details=""):
    """(Amazon UK, AbeBooks) search links for this book, or None for things that are not books on sale."""
    if author in NO_BUY or author == title or details == "booklet":
        return None
    t = title.split(":")[0].split(" / ")[0].strip()
    k = f"{t} {_who(author)}".strip()
    return (f"https://www.amazon.co.uk/s?k={_q(k)}&i=stripbooks",
            f"https://www.abebooks.co.uk/servlet/SearchResults?kn={_q(k)}&sts=t")
