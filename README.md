# History of Wales (Hanes Cymru)

A proud, bilingual (English and Cymraeg) history of Wales, live at [historyofwales.cymru](https://historyofwales.cymru).

## What is on it

- **Nine ages**, from the first people in the caves to Wales today, each with its own page.
- **A timeline** of about 160 events.
- **A map** of 68 historic sites, and a Kingdoms view showing Wales at 13 moments in time.
- **322 people**, from the Red Lady of Paviland to today, each with a field (kings, poets, scientists, sport and more), and a **Welsh world firsts** page (`firsts.html`).
- **Kings and princes**: every royal line, kingdom by kingdom (12 kingdoms of Wales and 5 of the Old North), and the kings and princes of all Wales.
- **Saints of Wales**: 68 saints in ten regions, with the 130 llannau and holy places named after them on a map, a llan name decoder and a saints’ calendar.
- **15 long reads**, 21 legends in five sections, a Mabinogion page with all eleven tales, symbols and traditions.
- **On this day in Welsh history**: about 350 dates across 233 days of the year, on the home page and on `onthisday.html`.
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
| Events, people, places | `src/data.py`, `src/more.py`, `src/places2.py` (extra items are merged in and sorted by year) |
| The 251 people added in November 2026, every person’s field, and the Welsh firsts | `src/people2a.py` to `src/people2f.py`, gathered by `src/people2.py` |
| The reference pages: Look it up, the A–Z and quick answers (and the pages still being added) | `src/refpages.py` lays them out; the words are in `src/ref_az.py` and `src/ref_faq.py` |
| Longer histories of people and places, trails, teacher notes | `src/long.py` |
| The nine ages | `src/ages.py`, `src/ages9.py` |
| Long reads, legends, symbols, facts | `src/features.py`, `src/legends2.py`, `src/mabinogion.py`, `src/pride.py`, `src/pride2.py`, `src/pride3.py`, `src/hywel.py`, `src/iolo.py` |
| The Kingdoms map | `src/kingdoms.py` |
| On this day (`onthisday.html` and the home page panel) | `src/onthisday.py`, `src/onthisday.css` |
| Kings and princes of each kingdom (`kings.html`, `kings-*.html`) | `src/royal.py` |
| Saints of Wales (`saints.html`, `saints-*.html`) | `src/saints.py`; map and decoder in `src/static/saints.js` |
| Photos and their credits | `src/photos.py`, `src/photos2.py` |
| Photo gallery: categories, and its 258 pictures with credits | `src/gallery.py`, `src/gallery_photos.py`, `src/static/gallery/` |
| Drawn pictures | `src/art.py` |
| The home page and opening screen | `src/head.html`, `src/body.html`, `src/app.js`, `src/extra.css`, `src/v6.css`; the 3D dragon, mountains and castle in `tools/*.src.js`, built into `src/static/hero3d.js` |
| Games, menu, badges, search | `src/static/play.js`, `src/static/site.js`, `src/static/search.js` |
| Menu and footer shared by every page | `nav()` and `footer()` in `build.py` |
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

Photos are linked from Wikimedia Commons in `src/photos.py`. The gallery's pictures are stored on the site itself (`src/static/gallery/`), with the photographer and licence of each in `src/gallery_photos.py`; when a place or person has a gallery picture, their page uses it. Pages without a photo show a picture drawn in code by `src/art.py`. Use only photos you own or that carry a free licence, and credit the photographer and licence on the page.

## Credits for artwork

- **Dragon of the flag** (castle flag, and the stand-in sky dragon): vector artwork from the [flag-icons](https://github.com/lipis/flag-icons) project, MIT licence, copyright (c) 2013 Panayiotis Lipiridis.
- **Lifelike dragon** (`src/static/dragon.glb`): 3D model and animation from the Ethereal Engine "Open Asset Kit, Basic" (github.com/ir-engine/ir-engine-assets-basic, `assets/fantasy/Dragon.glb`), described there as Creative Commons. The author is not named there; see TODO.md.
- **three.js** (inside `src/static/hero3d.js`): MIT licence, copyright three.js authors.
- **Castle walls and crag** (`stone.webp`, `rock.webp`, `detail.webp` and their `-n` relief maps in `src/static/`): photographs "Castle Wall Slates" and "Aerial Rocks 02" from [Poly Haven](https://polyhaven.com), CC0 (free for any use, no credit required).
- **The mountains** (`eryri-h.png`, `eryri-c.webp`, `eryri-n.webp`): made from Mapzen Terrain Tiles on AWS (terrarium format), whose height data for Wales comes from open survey sources such as SRTM and EU-DEM. Attribution asked for: "Mapzen, and the terrain data sources".

## Other things worth knowing

- **Search**: `build.py` writes `search.json`; `src/static/search.js` runs the magnifier button and the `/` shortcut.
- **History near you**: the town list is in `src/towns.py`.
- **Learn Welsh** (`welsh.html`) and the word of the day on the home page: words and phrases are in `src/cymraeg.py`.
- **Pronunciation**: MP3s go in `src/static/audio/` (see the README there). Without them, the play buttons use the device's own voice.
- **Your journey** (`journey.html`) shows what a visitor has read and the badges they have earned. It is stored only in their browser.
- **The nine ages**: see "Adding or splitting an age" in `SKILLS.md`.
- **Accuracy**: checking facts against sources and proofreading the Welsh are open jobs in `TODO.md`.
