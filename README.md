# History of Wales (Hanes Cymru)

A proud, bilingual (English and Cymraeg) history of Wales, live at [historyofwales.cymru](https://historyofwales.cymru).

## What is on it

- **Nine ages**, from the first people in the caves to Wales today, each with its own page.
- **A timeline** of about 160 events.
- **A map** of 67 historic sites, and a Kingdoms view showing Wales at 13 moments in time.
- **71 people**, from Caratacus to today.
- **14 long reads**, 7 legends, symbols and traditions.
- **Games**: a daily challenge, a quiz, a map game, Welsh names, word pairs and more.
- Every page in **English and Cymraeg**.

## The other notes in this folder

- `EDITORIAL.md`: the rules for how the site is written. Read this before changing any text.
- `TODO.md`: the open jobs.
- `SKILLS.md`: how things are done, step by step, added to each time something new is learnt.

## How it is built

Everything is plain HTML, CSS and JavaScript. There is no framework and nothing to install. `build.py` reads the files in `src/` and writes the finished site to `_site/`.

| To change | Edit |
| --- | --- |
| Events, people, places | `src/data.py`, `src/more.py`, `src/places2.py` |
| Longer histories of people and places, trails, teacher notes | `src/long.py` |
| The nine ages | `src/ages.py`, `src/ages9.py` |
| Long reads, legends, symbols, facts | `src/features.py`, `src/pride.py`, `src/pride2.py`, `src/pride3.py` |
| The Kingdoms map | `src/kingdoms.py` |
| Photos and their credits | `src/photos.py` |
| Drawn pictures | `src/art.py` |
| The home page and opening screen | `src/head.html`, `src/body.html`, `src/app.js`, `src/extra.css`, `src/v6.css` |
| Games, menu, badges, search | `src/static/play.js`, `src/static/site.js`, `src/static/search.js` |
| Icons and the share picture | `src/static/`, made by `tools/make_images.js` |

To build and look at it on your own computer:

```
python3 build.py
python3 -m http.server -d _site 8000   # then open http://localhost:8000
```

## Publishing

Every push to `main` runs `.github/workflows/deploy.yml`, which builds the site and publishes it to GitHub Pages.

The site's address is set by `SITE_URL` in the workflow and by `src/static/CNAME`. Changes are made on a branch and published by merging a pull request into `main`.

## Visitor statistics

Visitors are counted with [GoatCounter](https://www.goatcounter.com), which uses no cookies and needs no cookie banner. The dashboard is at [historyofwales.goatcounter.com](https://historyofwales.goatcounter.com).

## Adding photos

Photos are linked from Wikimedia Commons in `src/photos.py`, and scene illustrations are drawn in `src/art.py`. When adding photos, use only ones you own or that carry a free licence (for example from Wikimedia Commons), and credit the photographer and licence on the page.

## Accuracy

Dates and figures were written with care but should be checked against sources, and the Welsh should be proofread by a fluent speaker. Both jobs are listed in `TODO.md`.

## Round 3 additions

- **Extra content** lives in `src/more.py` (events, people and places) and is merged into `src/data.py` automatically. Events are sorted by year.
- **Search**: `build.py` writes `search.json`; `src/static/search.js` powers the magnifier button and the `/` shortcut on every page.
- **History near you**: town list in `src/towns.py`.
- **Pronunciation recordings**: put MP3s in `src/static/audio/` (see the README there). Without them, the play buttons use the device's speech voice.

## The redesign (round 4)

- **Long reads, legends, symbols and facts** live in `src/features.py`. Each has its own page.
- **Illustrations** are drawn in code by `src/art.py`.
- **Games** (daily challenge, map game, Welsh names, word pairs and more) are in `src/static/play.js`; the quiz and timeline challenge now have their own page, `quiz.html`.
- **Your journey** (`journey.html`) shows what a visitor has read and the badges they have earned. It is stored only in their browser.
- The menu, footer and page effects shared by every page are in `build.py` (`nav()`, `footer()`), `src/v6.css` and `src/static/site.js`.

## Nine ages

The site is organised into nine ages: Ancient Wales, Roman Wales, the Age of Saints, the Age of Kings, the Age of Princes, Tudor and Stuart Wales, Industrial Wales, Twentieth-Century Wales and Wales Today. See "Adding or splitting an age" in SKILLS.md.
