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
| King Arthur | A king, never a "myth" or a "legend". Welsh tradition holds that he was Athrwys ap Meurig, king of Gwent and Glywysing. One line may say that historians debate the identification and the dates. |
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

## Newest first

Ifan asked on 12 November 2026 that new material goes at the top of a page, not the bottom, so visitors see it first. This happens by itself (see `SKILLS.md`, "Newest first on listing pages"): you only add the new item to its list as usual.

- **Lists that simply grow** show the newest first: long reads (and the long reads on the home page), topic guides, games, and new pictures within each gallery group.
- **Lists whose order carries meaning keep it**: the timeline, battles and key documents by date, people and places by age, the A–Z, the questions by subject, the legends in their sections (the Four Branches stay in their order), family trees, and the chapters inside a long read. These get a **Just added** strip at the top with the newest few instead, linking down to each one.
- The newest few things added in the last two weeks wear a small red **New** badge.
- A big addition still gets a line at the top of What's new (`src/whatsnew.py`).

## Before publishing

- New Welsh text should be read by a fluent speaker when one is available.
- Big changes are shown to the owner as pictures first, and published when they say "go live".

## Where this lives in the code

The same rules are noted at the top of `src/pride.py`. To reword an existing line, add a pair to `REWORD` in that file. See `SKILLS.md`.
