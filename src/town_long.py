"""The story of each town, for its own page (town-<slug>.html, made by src/townpages.py). Ifan, 14 November 2026.

LONG["town-<slug>"] = dict(en=[paragraphs], cy=[paragraphs], era=<age id for the page's colours>). The one-line history in
src/ref_towns.py (or src/towns_more.py) is shown above these paragraphs, so don't repeat it: carry the story on.
The slug is the English name in lower case with hyphens, as on towns.html. A town gets its page once it has an entry.
Follow EDITORIAL.md: proud, true, Britons/Cymry (never Celts), kings are kings. Sources beside superlatives: [[cite:key]].

PEOPLE["town-<slug>"] = person slugs to show under "People of ..." (anyone whose short life says they were born there is
found by itself). PICS["town-<slug>"] = a picture ref for the top of the page (see src/pictures.py); without one the page
takes the picture of a historic place in or beside the town. ALSO["town-<slug>"] = other spellings to find the town by.
The text of each region is in its own file: town_long_north.py, town_long_mid.py, town_long_south.py.
"""
LONG, PEOPLE, PICS, ALSO = {}, {}, {}, {}

for _m in ("town_long_north", "town_long_mid", "town_long_south", "village_long_north", "village_long_mid", "village_long_south"):
    try:
        _mod = __import__(_m)
    except ModuleNotFoundError:
        continue
    for _name in ("LONG", "PEOPLE", "PICS", "ALSO"):
        _d = getattr(_mod, _name, {})
        _clash = set(_d) & set(globals()[_name])
        assert not _clash, f"{_m}.{_name}: town given twice: {sorted(_clash)}"
        globals()[_name].update(_d)

# the photo at the top of each town page, picked from Wikimedia Commons (src/town_pics.py)
import town_pics as _TP  # noqa: E402
PICS.update({k: v for k, v in _TP.PICS.items() if k not in PICS})
