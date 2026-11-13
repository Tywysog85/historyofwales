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
]


def link(author, title):
    """The checked web page for this book, or "" if there is none here."""
    for a, t, u in BOOKS:
        if t == title and author.startswith(a):
            return u
    return ""
