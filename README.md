# History of Wales (Hanes Cymru)

An interactive, bilingual (English / Cymraeg) history of Wales: a scroll-driven timeline, a map of historic sites and changing kingdoms, the people who shaped Wales, the Welsh language, a quiz, and a page for each age.

## How it is built

Everything is plain HTML, CSS and JavaScript. There is no framework and nothing to install.

- `src/data.py` holds the core content: eras, events, places, people, sources and translations. `src/long.py` holds the longer person and place histories, the themed trails and the teacher notes. **Edit these files to change the history.**
- `src/static/` holds the icons, share image, app manifest and offline support. `tools/make_images.js` regenerates the share image and icons.
- `src/head.html`, `src/body.html`, `src/app.js` and `src/extra.css` are the home page.
- `src/geo/` holds the outline of Wales and its 22 local authorities, drawn from public boundary data.
- `build.py` turns these into the finished site in `_site/`.

To build locally:

```
python3 build.py
python3 -m http.server -d _site 8000   # then open http://localhost:8000
```

## Publishing

Every push to `main` runs `.github/workflows/deploy.yml`, which builds the site and publishes it to GitHub Pages.

One-time setup: in the repository, go to **Settings → Pages** and set **Source** to **GitHub Actions**.

If you use your own domain, set `SITE_URL` in the workflow's build step (for example `SITE_URL=https://hanes.cymru/ python3 build.py`) so the sitemap and canonical links use it, and add the domain under **Settings → Pages → Custom domain**.

## Visitor statistics

The site can count visitors with [GoatCounter](https://www.goatcounter.com), which is free for non-commercial sites, uses no cookies and needs no cookie banner. Sign up, choose a code (for example `hanescymru`), then add `GOATCOUNTER: hanescymru` under `env:` in the build step of `.github/workflows/deploy.yml`.

## Adding photos

Photos are linked from Wikimedia Commons in `src/photos.py`, and scene illustrations are drawn in `src/art.py`. When adding photos, use only ones you own or that carry a free licence (for example from Wikimedia Commons), and credit the photographer and licence on the page.

## Accuracy

Dates and figures were written with care but should be checked against the linked sources. Welsh text should be proofread by a fluent speaker.

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
