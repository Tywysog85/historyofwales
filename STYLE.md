# Style

How History of Wales looks. Follow this when adding or changing a page, so the site stays one piece. How each part is built is in `SKILLS.md`; what the words say is in `EDITORIAL.md`.

## Colours

Set once in `:root` at the top of `src/head.html`. Use the names, never a new hex value.

| Name | Colour | Used for |
| --- | --- | --- |
| `--night` | #0e1118 | Page background (the site is dark) |
| `--slate`, `--slate-2` | #171c27, #202736 | Cards and panels |
| `--line` | #2e3647 | Borders and rules |
| `--ink` | #ece9e1 | Main text |
| `--muted` | #9ba2b0 | Small print, labels |
| `--dragon`, `--dragon-deep` | #f26a62, #c02c25 | The red of the dragon: highlights, New badges |

Each of the nine ages has its own colour, `--e-<age>` (ancient red ochre, roman pink, saints violet, kings gold, medieval dragon red, tudor teal, industrial slate blue, modern hill green, today orange). An age's pages, cards and timeline dots use its colour and nothing else.

## Fonts

Three fonts, kept on the site in `src/static/fonts/`:

- **Gloock** (`--f-display`) for headings, the logo and big numbers, with `word-spacing: .1em` so short phrases read clearly.
- **Figtree** (`--f-body`) for all running text and buttons.
- **JetBrains Mono** (`--f-mono`) only for small upper-case labels (`.eyebrow`).

Headings in sibling cards or list rows must all have the same size and font: no bigger style for "key" items. A drop cap only catches a page's first paragraph (`.story > p:first-child`).

## Cards and links

- **Whole cards are links.** Every card and list row is one big link (`wl-card` with an `a.wl` inside). Never add "Read more", "Read →", "The full story" or "Source ↗" to a card. Other buttons inside a card stay clickable on their own.
- Tap areas on phones are at least 44 × 44 px, without changing the look (see "Touch targets" in `SKILLS.md`).
- Every `<img>` has a width and height, so the page does not jump while pictures load.

## Spacing

The gap between home page sections is one setting, `--home-gap` near the end of `src/v6.css` (about 56 px on a phone, 112 px on a wide screen). Ifan wants the gaps tight and even: change that value, not single sections.

## Pictures

- **Real pictures on every page**: a photograph or old artwork at the top, with its credit under the title (`src/pictures.py`). Only freely licensed pictures (CC0, public domain, CC BY, CC BY-SA), each credited.
- **Never draw dragons by hand.** The flag dragon is the real flag artwork (`DSVG` in `src/app.js`), and the red and white dragons elsewhere are pictures of the 3D dragon. Hand-drawn dragons were rejected as fake.
- Drawn scenes from `src/art.py` are only a stand-in where no picture exists yet.
- **A picture on every card** (Ifan, 13 November 2026). A card shows the picture of the page it opens (`card_pic()` in `build.py`), never the stand-in picture of an age. People cards: the picture across the top (down the left side on phones); with no likeness, the age's picture dimmed behind their initials. Tiles: the photo where the drawing was. List rows: a small square at the side. Use the small copies (`src/thumbs.py`), `loading="lazy"` and `alt=""`. See SKILLS.md, "A picture on every card".
- **Picture backgrounds on plain panels** (Ifan, 13 November 2026): a fitting real picture under a dark veil (`src/panels.py`), never so light that the words get hard to read. Side-by-side panels take turns from a set of pictures, never the same one repeated.

## Movement

- The opening screen is a moving 3D scene: sky, mountains, castle and dragon (see "The opening screen" in `SKILLS.md`).
- **No Pause button** (Ifan, 13 November 2026). Old phones and slow connections get a still picture instead, and visitors who ask their device for reduced motion get no animation.
- Content must never depend on a script or an animation: anything that fades in is shown anyway if the script has not started.

## Both languages

Every page exists in English and in Welsh (`cy/`), with the same layout. Welsh dates use CC and OC.
