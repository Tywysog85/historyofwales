# Hanes Cymru

An interactive, bilingual (English / Cymraeg) history of Wales: a scroll-driven timeline, a map of historic sites and changing kingdoms, the people who shaped Wales, the Welsh language, a quiz, and a page for each age.

## How it is built

Everything is plain HTML, CSS and JavaScript. There is no framework and nothing to install.

- `src/data.py` holds all the content: eras, events, places, people, sources and translations. **Edit this file to change the history.**
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

## Adding photos

The site does not use photos yet; every illustration is an original line drawing in `src/head.html`. When photos are added, use only ones you own or that carry a free licence (for example from Wikimedia Commons), and credit the photographer and licence on the page.

## Accuracy

Dates and figures were written with care but should be checked against the linked sources. Welsh text should be proofread by a fluent speaker.
