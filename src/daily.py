"""Things on the home page that change every day, the same for everyone that day (Ifan, 2026-11-14).

The build picks them by today's date in Wales; the site is rebuilt every morning (the 04:15 UTC run in
.github/workflows/deploy.yml), so the long reads, people, legends and games move on each day. Parts drawn in the
browser (Did you know?, Words to know, the place-name decoder) pick by the visitor's own date with the same day number.

Every list is shuffled once with a fixed seed, then each day takes the next few in turn, so a visitor sees every item
before any comes round again, and neighbours in the source list (one age, one author) don't arrive together.
"""
import datetime

try:
    from zoneinfo import ZoneInfo
    _WALES = ZoneInfo("Europe/London")
except Exception:  # no time zone data: UTC is at most an hour out
    _WALES = datetime.timezone.utc


def day_no(now=None):
    """Days since 1 January 1970 by the date in Wales: the same number app.js gets from the visitor's date."""
    d = (now or datetime.datetime.now(_WALES)).date()
    return (d - datetime.date(1970, 1, 1)).days


def shuffled(items, seed):
    """A fixed shuffle (Park–Miller, as the Daily challenge uses), so the order only changes when items are added."""
    xs, s = list(items), seed
    for i in range(len(xs) - 1, 0, -1):
        s = (s * 16807) % 2147483647
        j = int((s - 1) / 2147483646 * (i + 1))
        xs[i], xs[j] = xs[j], xs[i]
    return xs


def window(order, n, k, skip=()):
    """Day n's k items from a shuffled list: the next k in turn, leaving out any in `skip`."""
    pool = [x for x in order if x not in skip]
    if not pool:
        return []
    k = min(k, len(pool))
    start = (n * k) % len(pool)
    return [pool[(start + j) % len(pool)] for j in range(k)]


def mixed_ages(people_by_age, ages, n, k):
    """Day n's k people, each from a different age, in the order of the ages. people_by_age maps age -> shuffled list."""
    ages = [a for a in ages if people_by_age.get(a)]
    k = min(k, len(ages))
    picks = []
    for j in range(k):
        turn = n * k + j  # the ages take turns, so each age is visited in order and its people in order
        a = ages[turn % len(ages)]
        ps = people_by_age[a]
        picks.append((ages.index(a), ps[(turn // len(ages)) % len(ps)]))
    return [p for _, p in sorted(picks, key=lambda t: t[0])]
