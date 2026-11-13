# Editorial rules

How History of Wales is written. These are the owner's rules. Anyone adding or changing text on the site, person or AI, follows them.

## The aim

A Welsh person anywhere in the world, or anyone with a link to Wales, should finish a page feeling proud. The site is written mainly for adults, with quizzes and games that children enjoy too.

## Voice

- **Proud.** Proud of the history, the heroes, the kings, princes, saints and poets, and proud that the language is still here despite the Welsh Not, the Blue Books and the Acts of Union.
- **Nothing negative about the people of Welsh history.** Write what they did for Wales. Leave out insults and gossip.
- **Proud and true.** Never invent evidence. Where a point is argued over, give it in the tradition's own words ("Welsh tradition holds", "Owain wrote", "it is told") and leave it there.
- **Plain words.** Short sentences. No jargon.
- **Both languages.** Every line of text has an English and a Welsh version.

## Standing decisions

| Subject | Rule |
| --- | --- |
| King Arthur | A king, never a "myth" or a "legend". Welsh tradition holds that he was Athrwys ap Meurig, king of Gwent and Glywysing. This is the site's position. Each Arthur page may add one line, and only one: "Other historians may see it differently." (Welsh: "Gall haneswyr eraill weld pethau’n wahanol.") |
| Iolo Morganwg | Never called a forger or a drug addict. Write what he gave Wales: the Gorsedd, the manuscripts he saved, the hymns, his stand against slavery. |
| The Coelbren | Iolo had it from the old bards of Glamorgan, in his own account. Never "forged". Do not print the word "proof" without a source to show. |
| Brutus | Owain Glyndŵr wrote to the King of Scotland that both were descended from Brutus. State it as Owain's words. Do not label it a myth. |
| Britons, not Celts | The site never calls the Welsh "Celts" or "Celtic" (Ifan, 12 November 2026). Caesar called the people of this island Britons, and they called themselves Brythoniaid and Cymry. Use "Britons" / "Brythoniaid" for the people before and under Rome, and "the Welsh" / "the Cymry" after. The name "Celtic" was put on the languages of Wales, Cornwall, Brittany, Ireland and Scotland by Edward Lhuyd of Oxford in his Archaeologia Britannica of 1707; nobody here called themselves Celts before then. Say "carved cross" or "stone cross", not "Celtic cross". The word may appear only when telling how Lhuyd's label came about, and in real names such as the Celtic Manor. |
| Cymraeg and Latin | Present the case that they are sister languages, with the evidence, and say that some scholars explain the likeness another way. |
| The Druids | Britain was the home of Druid learning, in Caesar's own words. Students crossed the sea to study here. |
| Kings are kings | Anyone who ruled as a king is called a king (brenin), in English and Welsh: Cassivellaunus, Cunobelinus, Caratacus, Cunedda, Maelgwn, Urien, Brochwel, Rhodri Mawr, Hywel Dda, Gruffudd ap Llywelyn and every ruler of a Welsh or Old North kingdom before the 12th century. Never "chieftain", "war leader", "tribal leader" or "prince" for them. Queens are queens (Boudica, Cartimandua). "Prince" (tywysog) is kept for those who took that title from the 12th century on (Owain Gwynedd, the two Llywelyns, Dafydd, Owain Glyndŵr, the princes of Deheubarth and Powys after 1100), for kings' sons who did not reign (Cadog, Madog ab Owain Gwynedd), and for old titles such as Pwyll Pendefig Dyfed. |
| Llanilltud Fawr | The oldest centre of learning in Britain. |
| Vikings and Normans | No Viking kingdom took root in Wales. The Normans took England in five years and needed 216 for Wales (1067 to 1283). |
| The front page tagline | "A land of kings, princes, castles, poets, and saints. Built on coal, slate, iron, copper, and wool." Lower case, as written. |
| The nine ages | Wherever visitors choose between the ages (home page, Menu, footer, filters, next/previous buttons), each name goes with its dates, e.g. "The Age of Kings 800 – 1100", "The Age of Princes 1100 – 1485" (Ifan, 12 November 2026). Each age has one short question on the home page, in both languages (`ERA_Q` in `build.py`). |
| Where to begin | The home page opens with three ways in beside the introduction: "Explore the nine ages", "Find a place on the map" and "Follow a themed trail". The Today section (On this day, daily challenge, Did you know, New on the site) comes after the nine ages (Ifan, 12 November 2026). |

## Newest first

Ifan asked on 12 November 2026 that new material goes at the top of a page, not the bottom, so visitors see it first. This happens by itself (see `SKILLS.md`, "Newest first on listing pages"): you only add the new item to its list as usual.

- **Lists that simply grow** show the newest first: long reads (and the long reads on the home page), topic guides, games, and new pictures within each gallery group.
- **Lists whose order carries meaning keep it**: the timeline, battles and key documents by date, people and places by age, the A–Z, the questions by subject, the legends in their sections (the Four Branches stay in their order), family trees, and the chapters inside a long read. These get a **Just added** strip at the top with the newest few instead, linking down to each one.
- The newest few things added in the last two weeks wear a small red **New** badge.
- A big addition still gets a line at the top of What's new (`src/whatsnew.py`). Only history goes there: no notes about how the site works (Ifan, 12 November 2026).

## References

Every long read ends with a short list of further reading and references (`src/refs.py`), and so does every other content page: subject pages, legends, ages, kingdoms, saints, topic guides, trails, and each person and place page (the list for their age) (`src/refs2.py`): the old texts it rests on and the historians' books that tell the story in full, plus the Dictionary of Welsh Biography. Wikipedia alone is not enough for a teaching resource.

- Cite only works that really exist, with the right author, title, publisher and year. Never invent one; if a detail can't be checked, leave it out.
- Give the title as published, even when it uses a word the site avoids (for example "The Atlantic Celts"). The note in our own words follows the site's rules.

## Sources beside the claims

Ifan asked on 12 November 2026 for the source to sit right beside the claim it supports, not only in the list at the bottom. A small chip with a § (for example "§ Antiquity, 2019 +2") follows the sentence; tap it and a card shows each source, who wrote it, what it shows, and a link. How to add one is at the top of `src/cites.py`.

- Start with what the site features and what readers will question: the facts on the home page, superlatives ("largest", "first", "oldest") and traditional stories.
- Give the claim's own evidence where there is any: the archaeological paper, the museum or archive that holds the find, the old text itself. Open and read each source before it goes in.
- The source must say what the sentence says. If it says less, change the sentence to match the source (Marconi's 1897 message is now "between" Lavernock and Flat Holm, as the sources have it).
- Traditions (Arthur as Athrwys, Madog, Brutus) are cited to their own sources: the Book of Llandaff, The Historie of Cambria (1584), the Historia Brittonum, Geoffrey, Adam of Usk, and the books that make the tradition's case. No debunking sources and no debunking words.
- Put the marker in the English and the Welsh sentence alike.

## Author, dates and corrections

Ifan asked on 12 November 2026 that readers can see who writes the site and how fresh each page is.

- Every page ends with who wrote it, when it was first published (long reads, legends, people and places added since 11 November 2026) and when it was last updated. Long reads also say "By ..." and "Updated ..." at the top. The name and the way to report a mistake are set at the top of `src/about.py`.
- "Last updated" is never typed in: it moves on by itself when the words or pictures on a page change.
- Readers report mistakes, or get in touch about anything, by emailing hello@historyofwales.cymru (set in `src/about.py`). Do not put Google Forms or GitHub links on the site for this.
- When a reader reports a mistake: check it against the sources, fix it, and if it was more than a typo, add a line to `CORRECTIONS` in `src/about.py` so it is listed on the About page.

## Before publishing

- New Welsh text is run through Cysill and read line by line before it goes live (see SKILLS.md, "Checking the Welsh with Cysill").
- Big changes are shown to the owner as pictures first, and published when they say "go live".

## Where this lives in the code

The same rules are noted at the top of `src/pride.py`. To reword an existing line, add a pair to `REWORD` in that file. See `SKILLS.md`.
