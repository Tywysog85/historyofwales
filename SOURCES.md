# Sources

How History of Wales checks and cites what it says. The editorial rules behind this are in `EDITORIAL.md` ("References", "Sources beside the claims"); how the code works is in `SKILLS.md`.

## Which sources to trust first

1. **The claim's own evidence**: the old text itself (the Laws, the Book of Llandaff, the Historia Brittonum, the poets), the archaeological report, or the museum, library or archive that holds the find.
2. **The national records of Wales**: the Dictionary of Welsh Biography (biography.wales / bywgraffiadur.cymru), Coflein, Cadw, the National Library of Wales, Welsh Journals (journals.library.wales).
3. **Books by historians** that tell the story in full, and peer-reviewed articles.
4. **Wikipedia** only to find the sources above. It is never enough on its own.

On traditions (Arthur as Athrwys ap Meurig, Madog, Brutus), cite the tradition's own sources: the old texts and the books that make its case. No debunking sources and no debunking words.

## Checking a source

- Open and read every source before it goes in. Never invent one.
- The source must say what the sentence says. If it says less, change the sentence to match.
- A book is real when a publisher's page, a library catalogue or a bookseller with the ISBN shows it. If the year or publisher cannot be confirmed, give only what can.
- Quote old books only from a named, published translation, and name the translator.
- When a site is blocked from the cloud, try WebFetch, a mirror found by WebSearch, or the GitHub research workflow (see `SKILLS.md`).

## How to cite

- **Beside the claim.** Put `[[cite:key]]` straight after the full stop, in the English and the Welsh sentence alike, and add the key to `S` in `src/cites.py` (short label, title, author, what it shows, link). The build turns it into a § chip. An unknown key stops the build.
- **At the foot of the page.** Long reads take their reading list from `src/refs.py`; every other content page from `src/refs2.py`. Each item is an old text, a historian's book or a website. A new long read without a list prints a warning.
- **People and places** get their Dictionary of Welsh Biography, Coflein and other record links from `src/source_links.json` (made by `tools/fetch_sources.py`).
- Give a title exactly as published, even when it uses a word the site avoids. Our own note beside it follows the site's rules.

## Corrections

When a reader reports a mistake (hello@historyofwales.cymru): check it against the sources, fix it, and if it was more than a typo add a line to `CORRECTIONS` in `src/about.py`.
