"""When each thing was added to the site, so that pages can show the newest first.

src/added.json records the time each long read, legend, document, battle, question, topic guide, game, person, place,
gallery picture and card set first appeared. You never need to edit it by hand: when build.py meets an item that is not
in the file yet, it gives it the time of that build and saves the file. Commit src/added.json with your change (the
deploy on GitHub also saves it back if a change forgot to).

The rule (see EDITORIAL.md, "Newest first"):
  * Collections that simply grow (long reads, topic guides, games) list the newest first: newest(kind, items).
  * Lists whose order means something (by date, by age, A to Z, the branches of the Mabinogi) keep their order, and get a
    "Just added" strip at the top instead: recent(kind, items) gives the items for it.
  * is_new(kind, id) is True for the few newest items added in the last two weeks: they wear a small "New" badge.
"""
import datetime
import json
import os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "added.json")
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
NEW_DAYS = 14   # how long the "New" badge stays on
NEW_MAX = 3     # at most this many items in one list wear it at once

with open(PATH, encoding="utf-8") as _f:
    DATA = json.load(_f)
_changed = []


def when(kind, i):
    """The time (UTC, ISO) item i of this kind was first added. An item never seen before is stamped with now."""
    d = DATA.setdefault(kind, {})
    if i not in d:
        d[i] = NOW
        _changed.append(f"{kind}:{i}")
    return d[i]


def track(kind, ids):
    for i in ids:
        when(kind, i)


def _id(x):
    return x["id"] if isinstance(x, dict) else x[0]


def newest(kind, items, key=_id, ties="reverse"):
    """items, newest added first. Items added in the same change keep their order (ties="keep") or are turned round
    (ties="reverse", for lists that were always added to at the bottom, so lower down meant newer)."""
    items = list(items)
    if ties == "reverse":
        return [x for _, x in sorted(enumerate(items), key=lambda p: (when(kind, key(p[1])), p[0]), reverse=True)]
    return sorted(items, key=lambda x: when(kind, key(x)), reverse=True)  # sorted() keeps ties in order


def _first(kind):
    return min(DATA.get(kind, {}).values(), default=NOW)


def recent(kind, items, key=_id, n=4):
    """Up to n items added after the list first went up, newest first: for a "Just added" strip. Empty if none."""
    base = _first(kind)
    return [x for x in newest(kind, items, key) if when(kind, key(x)) > base][:n]


def _age_days(t):
    then = datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
    return (datetime.datetime.now(datetime.timezone.utc) - then).total_seconds() / 86400


def is_new(kind, i, ids=None):
    """True for one of the newest NEW_MAX items of this kind (among ids, if given), added in the last NEW_DAYS days
    and after the list first went up."""
    pool = list(ids) if ids is not None else list(DATA.get(kind, {}))
    top = [x for x in newest(kind, pool, key=lambda s: s) if when(kind, x) > _first(kind) and _age_days(when(kind, x)) <= NEW_DAYS][:NEW_MAX]
    return i in top


def save():
    """Write added.json if this build met new items. Returns the new items, for the build to report."""
    if _changed:
        with open(PATH, "w", encoding="utf-8") as f:
            json.dump(DATA, f, ensure_ascii=False, indent=1, sort_keys=True)
            f.write("\n")
    return list(_changed)
