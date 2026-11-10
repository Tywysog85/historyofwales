# Original scene illustrations, drawn in code as SVG. Each scene is a night landscape in the
# site's own style (sky, moon, rolling ridges) with one paper-cut motif in the foreground.
# scene(kind, colour) returns an <svg> string that fills its container.
import math
import random

W, H = 800, 500
DRAGON_BODY = "M186 34C190 33 196 35 200 38L193 40C196 42 199 44 200 46C194 47 188 46 184 45C178 47 172 52 168 58C163 66 156 72 146 74C132 77 116 78 102 77C88 76 76 74 66 76C52 79 40 88 28 96C20 101 12 102 6 98C10 98 16 95 22 90C34 80 46 70 60 66C74 62 90 64 104 63C118 62 132 62 142 58C152 54 158 46 164 38C168 32 174 28 180 28L176 20L184 27L186 18L189 29C189 31 188 32 186 34ZM8 99L-6 92L0 104L-4 112L12 102ZM138 72C142 80 144 86 150 90L156 90L152 94L158 96L146 96C138 92 134 84 130 76ZM76 74C76 84 72 92 66 98L72 100L64 102L68 106L58 104C62 96 64 86 64 76Z"
DRAGON_FAR = "M128 62C130 40 140 18 160 2C150 18 150 26 152 32C144 30 140 36 142 42C134 42 132 50 134 58Z"
DRAGON_NEAR = "M92 64C86 40 74 18 48 0C62 4 80 10 96 20L104 10C112 22 118 36 120 52C114 48 108 50 108 56C102 52 96 56 98 62Z"

INK = "#0b0e16"
FRONT = "#10141d"


def _ridge(rng, base, amp, step=10):
    ws = [(rng.random() * 6.28, 0.5 + rng.random() * (k + 1) * 1.5, (1 / (k + 1.2)) * (0.6 + rng.random() * 0.6)) for k in range(5)]
    pts = []
    for x in range(0, W + step, step):
        u = x / W * 3
        v = sum(math.sin(u * f + p) * a for p, f, a in ws)
        v = abs(v) * 0.6 + v * 0.4
        pts.append(f"{x},{base - v * amp:.0f}")
    return f"M0,{H} L" + " L".join(pts) + f" L{W},{H}Z"


def dragon(x, y, s, fill, flip=False, rot=0):
    f = f"translate({x} {y}) scale({-s if flip else s} {s}) rotate({rot})"
    return (f'<g transform="{f}" fill="{fill}"><path d="{DRAGON_FAR}" opacity=".8"/><path d="{DRAGON_BODY}"/><path d="{DRAGON_NEAR}"/></g>')


def _castle(c):
    def tower(x, w, top, cap=True):
        s = f'<rect x="{x}" y="{top}" width="{w}" height="{440 - top}"/>'
        n = max(2, w // 14)
        cw = w / (n * 2 - 1)
        for i in range(n):
            s += f'<rect x="{x + i * 2 * cw:.1f}" y="{top - 10}" width="{cw:.1f}" height="11"/>'
        return s
    s = f'<g fill="{FRONT}">' + tower(230, 60, 250) + tower(330, 84, 190) + tower(470, 56, 262) + tower(560, 70, 230)
    s += '<rect x="250" y="320" width="360" height="120"/>'
    for i in range(12):
        s += f'<rect x="{292 + i * 22}" y="310" width="12" height="11"/>' if not (2 <= i <= 4 or 8 <= i <= 11) else ""
    s += '<path d="M150 440 L230 372 L630 372 L700 440Z"/></g>'
    s += f'<path d="M358 440v-46a18 18 0 0 1 36 0v46z" fill="{INK}"/>'
    s += f'<g fill="{c}"><rect x="348" y="232" width="5" height="16" rx="2"/><rect x="390" y="232" width="5" height="16" rx="2"/><rect x="590" y="270" width="5" height="14" rx="2"/><rect x="256" y="290" width="5" height="14" rx="2"/><rect x="494" y="300" width="5" height="14" rx="2"/></g>'
    s += f'<path d="M372 180V128" stroke="{FRONT}" stroke-width="3"/><path d="M373 130c12-6 20 6 34 0v20c-14 6-22-6-34 0z" fill="{c}"/>'
    return s


def _dolmen(c):
    return (f'<g fill="{FRONT}"><path d="M250 300 L560 262 L610 292 L300 338Z"/><path d="M296 332 L330 328 L338 440 L284 440Z"/>'
            '<path d="M420 316 L452 312 L462 440 L414 440Z"/><path d="M540 300 L574 296 L590 440 L536 440Z"/>'
            '<path d="M130 440 L142 372 L162 362 L176 440Z"/><path d="M668 440 L676 392 L694 384 L704 440Z"/></g>'
            f'<path d="M250 300 L560 262 L610 292" fill="none" stroke="{c}" stroke-width="2.5" stroke-linejoin="round" opacity=".8"/>')


def _cross(c):
    return (f'<g fill="{FRONT}"><path d="M382 440 L388 150 L412 150 L418 440Z"/><rect x="336" y="196" width="128" height="26"/>'
            '<path d="M360 440h80l10 20h-100z"/><path d="M560 440V350l40-34 40 34v90z"/><path d="M596 316v-22M588 302h16" stroke="#10141d" stroke-width="5"/>'
            '<path d="M150 440 L160 380 L176 374 L186 440Z"/></g>'
            f'<circle cx="400" cy="209" r="44" fill="none" stroke="{FRONT}" stroke-width="13"/>'
            f'<circle cx="400" cy="209" r="44" fill="none" stroke="{c}" stroke-width="2" opacity=".8"/>'
            f'<circle cx="400" cy="209" r="7" fill="{c}"/><path d="M588 440v-34a12 12 0 0 1 24 0v34z" fill="{c}" opacity=".85"/>')


def _ship(c, x=0, y=0):
    return (f'<g transform="translate({x} {y})"><path d="M400 180V390" stroke="{FRONT}" stroke-width="7"/>'
            f'<path d="M300 210 C340 222 460 222 500 210 L494 340 C450 352 350 352 306 340Z" fill="{c}" opacity=".9"/>'
            f'<path d="M332 216L326 346M366 219L362 350M400 220V352M434 219L438 350M468 216L474 346" stroke="{INK}" stroke-width="9" opacity=".45"/>'
            f'<path d="M190 372 C200 420 260 432 400 432 C540 432 600 420 612 372 L636 322 C640 312 652 312 650 326 L640 372 C640 430 580 462 400 462 C220 462 162 430 162 376 L150 330 C150 316 164 318 166 328Z" fill="{FRONT}"/>'
            f'<g fill="{c}"><circle cx="250" cy="418" r="11"/><circle cx="300" cy="426" r="11"/><circle cx="350" cy="430" r="11"/><circle cx="400" cy="431" r="11"/><circle cx="450" cy="430" r="11"/><circle cx="500" cy="426" r="11"/><circle cx="550" cy="418" r="11"/></g></g>')


def _sea(c, y=440, n=3):
    s = ""
    for i in range(n):
        yy = y + i * 18
        d = f"M0,{yy} " + " ".join(f"q25,-14 50,0 t50,0" for _ in range(9)) + f" V{H} H0Z"
        s += f'<path d="{d}" fill="{["#161c2a", "#111622", "#0b0e16"][i % 3]}"/>'
    s += f'<path d="M0,{y} ' + " ".join("q25,-14 50,0 t50,0" for _ in range(9)) + f'" fill="none" stroke="{c}" stroke-width="1.5" opacity=".5"/>'
    return s


def _pit(c):
    s = (f'<g stroke="{FRONT}" stroke-width="9" fill="none" stroke-linecap="round"><path d="M330 440L392 196M470 440L408 196M350 360h100M366 296h68M408 200L560 300V440"/></g>'
         f'<circle cx="400" cy="190" r="46" fill="none" stroke="{FRONT}" stroke-width="9"/>'
         f'<g stroke="{c}" stroke-width="2.5" opacity=".9"><circle cx="400" cy="190" r="46" fill="none"/><path d="M354 190h92M400 144v92M367 157l66 66M433 157l-66 66"/></g>'
         f'<g fill="{FRONT}"><rect x="520" y="372" width="120" height="68"/><path d="M510 372l70-34 70 34z"/><path d="M196 440L206 250h26l10 190z"/><path d="M130 440L138 300h22l8 140z"/></g>'
         f'<g fill="{c}" opacity=".85"><rect x="540" y="392" width="16" height="20"/><rect x="572" y="392" width="16" height="20"/><rect x="604" y="392" width="16" height="20"/></g>'
         '<g fill="#8a90a3" opacity=".22"><circle cx="222" cy="226" r="22"/><circle cx="248" cy="196" r="30"/><circle cx="290" cy="170" r="36"/><circle cx="152" cy="280" r="16"/><circle cx="170" cy="256" r="22"/></g>')
    return s


def _senedd(c):
    return (f'<g fill="{FRONT}"><path d="M120 250 C260 214 540 214 700 250 L700 266 L120 266Z"/>'
            '<path d="M372 266 C376 310 388 340 388 372 L412 372 C412 340 424 310 428 266Z"/>'
            '<rect x="170" y="372" width="480" height="68"/><path d="M110 440h600l30 20H80z"/></g>'
            f'<g stroke="{FRONT}" stroke-width="6"><path d="M176 266V372M250 266V372M324 266V372M476 266V372M550 266V372M644 266V372"/></g>'
            f'<path d="M120 250 C260 214 540 214 700 250" fill="none" stroke="{c}" stroke-width="2.5" opacity=".85"/>'
            f'<g fill="{c}" opacity=".5"><rect x="182" y="300" width="62" height="70"/><rect x="256" y="300" width="62" height="70"/><rect x="482" y="300" width="62" height="70"/><rect x="556" y="300" width="82" height="70"/></g>'
            f'<path d="M400 214V150" stroke="{FRONT}" stroke-width="3"/><path d="M401 152c12-6 20 6 34 0v20c-14 6-22-6-34 0z" fill="{c}"/>')


def _dragons(c):
    return dragon(90, 150, 1.45, "#e2453d") + dragon(710, 170, 1.45, "#e9e4d8", flip=True) + \
        f'<g fill="{FRONT}"><path d="M300 440 L360 330 L392 352 L420 318 L452 356 L500 440Z"/><rect x="386" y="300" width="30" height="50"/><rect x="382" y="292" width="8" height="10"/><rect x="397" y="292" width="8" height="10"/><rect x="412" y="292" width="8" height="10"/></g>'


def _hound(c):
    return (f'<g fill="{FRONT}"><path d="M330 440 L330 372 C326 330 338 292 366 270 C380 258 388 240 386 220 L376 176 L400 204 L420 160 L428 212 C446 216 468 226 490 226 L486 240 L452 250 C444 276 446 300 456 324 C470 356 476 400 476 440 L440 440 L434 384 L412 440Z"/>'
            '<path d="M330 420 C300 420 280 400 284 372 C286 390 304 400 330 398Z"/>'
            '<path d="M560 440 L572 350 C576 330 604 330 608 350 L620 440Z"/></g>'
            f'<circle cx="436" cy="222" r="3.5" fill="{c}"/><path d="M582 372h18M582 386h18M582 400h18" stroke="{c}" stroke-width="2" opacity=".7"/>')


def _sunken(c):
    s = _sea(c, 150, 1).replace(f"V{H} H0Z", "V500 H0Z")
    s = f'<rect x="0" y="150" width="800" height="350" fill="#0c1422" opacity=".72"/>' + \
        f'<path d="M0,150 ' + " ".join("q25,-14 50,0 t50,0" for _ in range(9)) + f'" fill="none" stroke="{c}" stroke-width="2" opacity=".7"/>'
    s += (f'<g fill="{FRONT}"><rect x="350" y="250" width="100" height="250"/><rect x="342" y="236" width="20" height="16"/><rect x="372" y="236" width="20" height="16"/><rect x="406" y="236" width="20" height="16"/><rect x="438" y="236" width="20" height="16"/>'
          '<path d="M180 500V380l40-30 40 30v120zM540 500V400l50-36 50 36v100z"/><path d="M90 500 L110 440 L130 500Z"/></g>'
          f'<path d="M374 330a26 26 0 0 1 52 0v50h-52z" fill="#0b0e16"/>'
          f'<path d="M400 336c-12 0-16 14-16 28l-6 8h44l-6-8c0-14-4-28-16-28z" fill="{c}"/><circle cx="400" cy="377" r="4" fill="{c}"/>'
          f'<g fill="none" stroke="{c}" opacity=".5"><circle cx="470" cy="216" r="5"/><circle cx="486" cy="186" r="3"/><circle cx="320" cy="206" r="4"/><circle cx="306" cy="176" r="2.5"/></g>')
    return s


def _lady(c):
    return (_sea(c, 400, 3) +
            f'<path d="M560 400 L580 500 L660 500 L640 400Z" fill="#e9d9c6" opacity=".12"/>'
            f'<g fill="{FRONT}"><circle cx="400" cy="232" r="17"/><path d="M384 228 C372 262 372 300 362 330 L384 320 C388 290 392 262 398 246Z"/>'
            '<path d="M386 250 C380 300 356 372 340 420 L460 420 C444 372 420 300 414 250Z"/></g>'
            f'<path d="M386 250 C380 300 356 372 340 420" fill="none" stroke="{c}" stroke-width="2" opacity=".8"/>'
            f'<path d="M414 250 C420 300 444 372 460 420" fill="none" stroke="{c}" stroke-width="2" opacity=".35"/>'
            f'<g fill="none" stroke="{c}" stroke-width="1.5" opacity=".5"><ellipse cx="400" cy="424" rx="80" ry="9"/><ellipse cx="400" cy="424" rx="130" ry="15"/></g>')


def _bird(c):
    b = ('<path d="M0 0 C-30 -8 -52 -4 -70 12 C-50 6 -36 8 -24 14 C-40 30 -44 50 -40 70 C-28 46 -10 30 12 22 C24 30 40 32 56 26 L80 30 L60 16 C50 4 34 -2 18 0 C10 -22 -6 -40 -30 -52 C-18 -36 -8 -18 0 0Z"/>')
    return (_sea(c, 430, 3) + f'<g transform="translate(420 210) scale(1.7)" fill="{FRONT}">{b}</g>'
            f'<g transform="translate(420 210) scale(1.7)" fill="none" stroke="{c}" stroke-width="1.2" opacity=".8">{b}</g>'
            f'<rect x="512" y="258" width="26" height="18" rx="2" fill="{c}" transform="rotate(14 525 267)"/>'
            f'<g fill="{FRONT}"><path d="M80 430V380l14-10 14 10v50zM108 430v-30h40v30z"/></g>')


def _owl(c):
    fl = ""
    for x, y, r in [(170, 400, 16), (230, 372, 12), (600, 396, 16), (650, 360, 11), (540, 420, 10), (120, 350, 9)]:
        fl += "".join(f'<circle cx="{x + math.cos(a) * r:.0f}" cy="{y + math.sin(a) * r:.0f}" r="{r * .62:.0f}" fill="{c}" opacity=".55"/>' for a in [i * 1.2566 for i in range(5)])
        fl += f'<circle cx="{x}" cy="{y}" r="{r * .45:.0f}" fill="#e9d9c6"/>'
    return (f'<path d="M0 372 C200 352 520 372 800 340" fill="none" stroke="{FRONT}" stroke-width="16" stroke-linecap="round"/>' + fl +
            f'<g fill="{FRONT}"><path d="M340 372 C320 300 330 220 360 196 L352 160 L384 186 C394 182 406 182 416 186 L448 160 L440 196 C470 220 480 300 460 372Z"/></g>'
            f'<g fill="none" stroke="{c}" stroke-width="2"><circle cx="378" cy="224" r="17"/><circle cx="422" cy="224" r="17"/></g>'
            f'<circle cx="378" cy="224" r="6" fill="{c}"/><circle cx="422" cy="224" r="6" fill="{c}"/><path d="M394 240l6 14 6-14z" fill="{c}"/>'
            f'<g stroke="{c}" stroke-width="1.5" opacity=".45" fill="none"><path d="M372 286q10 10 20 0q10 10 20 0q10 10 20 0M366 312q10 10 20 0q10 10 20 0q10 10 20 0q10 10 12 0M372 338q10 10 20 0q10 10 20 0q10 10 20 0"/></g>')


def _sword(c):
    return (_sea(c, 400, 3) +
            f'<g fill="{FRONT}"><path d="M384 420 C380 380 384 350 392 330 L412 330 C420 350 422 380 418 420Z"/><circle cx="402" cy="322" r="15"/></g>'
            f'<path d="M397 300 L399 120 L402 104 L405 120 L407 300Z" fill="#e9e4d8"/><rect x="376" y="298" width="52" height="8" rx="3" fill="{c}"/>'
            f'<circle cx="402" cy="322" r="5" fill="{c}"/>'
            f'<g fill="none" stroke="{c}" stroke-width="1.5" opacity=".5"><ellipse cx="402" cy="424" rx="70" ry="8"/><ellipse cx="402" cy="424" rx="120" ry="14"/></g>')


def _cauldron(c):
    return (f'<g fill="{FRONT}"><path d="M290 300 C280 380 330 430 400 430 C470 430 520 380 510 300Z"/><rect x="276" y="286" width="248" height="20" rx="10"/>'
            '<path d="M330 420l-14 30h16l10-24zM470 420l14 30h-16l-10-24z"/></g>'
            f'<path d="M290 300 C280 380 330 430 400 430" fill="none" stroke="{c}" stroke-width="2" opacity=".7"/>'
            f'<g fill="{c}"><path d="M340 470c-10-18 6-22 2-40c16 12 18 26 10 40zM392 472c-14-22 8-30 2-52c22 16 24 34 12 52zM452 470c-10-18 6-22 2-40c16 12 18 26 10 40z" opacity=".9"/></g>'
            f'<g fill="#e9e4d8"><path d="M400 150c10 14 14 20 14 28a14 14 0 0 1-28 0c0-8 4-14 14-28zM350 196c7 10 10 14 10 20a10 10 0 0 1-20 0c0-6 3-10 10-20zM450 196c7 10 10 14 10 20a10 10 0 0 1-20 0c0-6 3-10 10-20z"/></g>'
            '<g fill="#8a90a3" opacity=".16"><circle cx="360" cy="262" r="20"/><circle cx="410" cy="250" r="26"/><circle cx="450" cy="266" r="18"/></g>')


def _book(c):
    return (f'<g fill="{FRONT}"><path d="M400 250 C330 214 250 212 170 236 V420 C250 396 330 398 400 434 C470 398 550 396 630 420 V236 C550 212 470 214 400 250Z"/></g>'
            f'<path d="M400 250 C330 214 250 212 170 236 V420 C250 396 330 398 400 434 C470 398 550 396 630 420 V236 C550 212 470 214 400 250ZM400 250V434" fill="none" stroke="{c}" stroke-width="2.5" stroke-linejoin="round" opacity=".85"/>'
            f'<g stroke="{c}" stroke-width="2" opacity=".45" fill="none"><path d="M204 272c56-14 110-10 164 12M204 304c56-14 110-10 164 12M204 336c56-14 110-10 164 12M204 368c56-14 110-10 164 12M432 284c54-22 108-26 164-12M432 316c54-22 108-26 164-12M432 348c54-22 108-26 164-12M432 380c54-22 108-26 164-12"/></g>'
            f'<text x="214" y="262" font-family="Gloock,Georgia,serif" font-size="54" fill="{c}">C</text>')


def _arches(c):
    s = f'<g fill="{FRONT}"><rect x="0" y="250" width="800" height="26"/>'
    for i in range(7):
        x = 40 + i * 120
        s += f'<path d="M{x - 12} 276h24l6 224h-36z"/>'
    s += "</g>"
    for i in range(6):
        x = 52 + i * 120
        s += f'<path d="M{x} 276 a48 60 0 0 1 96 0" fill="none" stroke="{FRONT}" stroke-width="14"/>'
    s += f'<path d="M0 250h800" stroke="{c}" stroke-width="2.5" opacity=".8"/>'
    s += f'<g fill="{FRONT}"><rect x="300" y="226" width="150" height="24" rx="4"/><rect x="456" y="232" width="60" height="18" rx="3"/></g><rect x="312" y="232" width="126" height="6" fill="{c}" opacity=".7"/>'
    return s


def _torch(c):
    s = ""
    for i, x in enumerate([130, 235, 335, 440, 545, 660]):
        h = [70, 96, 80, 104, 76, 92][i]
        s += f'<g fill="{FRONT}"><circle cx="{x}" cy="{416 - h}" r="18"/><path d="M{x - 30} 500V{466 - h}a30 30 0 0 1 60 0V500z"/></g>'
        if i % 2 == 1:
            s += f'<path d="M{x + 24} {474 - h} L{x + 46} {396 - h}" stroke="{FRONT}" stroke-width="7" stroke-linecap="round"/>'
            s += f'<circle cx="{x + 48}" cy="{372 - h}" r="46" fill="{c}" opacity=".13"/><path d="M{x + 46} {396 - h}c-14-20 9-27 2-50c23 16 25 34 12 50z" fill="{c}"/>'
    return s


def _amph(c):
    return (f'<g fill="none" stroke="{FRONT}" stroke-width="20"><ellipse cx="400" cy="400" rx="300" ry="74"/><ellipse cx="400" cy="400" rx="210" ry="44"/></g>'
            f'<ellipse cx="400" cy="400" rx="300" ry="74" fill="none" stroke="{c}" stroke-width="2" opacity=".7"/>'
            f'<g fill="{FRONT}"><path d="M372 250l28-150 28 150z"/><rect x="386" y="246" width="28" height="90"/><path d="M362 100h76l-8 14h-60z"/></g>'
            f'<circle cx="400" cy="86" r="16" fill="{c}"/><path d="M370 108h60" stroke="{c}" stroke-width="3"/>')


MOTIF = dict(castle=_castle, dolmen=_dolmen, cross=_cross, ship=lambda c: _sea(c, 446, 2) + _ship(c, 0, -10), pit=_pit, senedd=_senedd,
             dragons=_dragons, hound=_hound, sunken=_sunken, lady=_lady, bird=_bird, owl=_owl, sword=_sword, cauldron=_cauldron,
             book=_book, arches=_arches, torch=_torch, amph=_amph)
MOON = dict(castle=(640, 110, 34), dolmen=(400, 190, 60), cross=(620, 120, 30), ship=(170, 120, 36), pit=(650, 110, 30), senedd=(650, 100, 30),
            dragons=(400, 120, 44), hound=(560, 120, 46), sunken=(640, 70, 26), lady=(600, 120, 40), bird=(180, 110, 34), owl=(620, 110, 50),
            sword=(600, 110, 36), cauldron=(640, 100, 30), book=(650, 96, 28), arches=(140, 110, 32), torch=(660, 100, 30), amph=(160, 110, 30))


def scene(kind, colour, seed=None):
    rng = random.Random(seed if seed is not None else sum(map(ord, kind)) * 7 + 3)
    uid = f"{kind}{abs(hash(colour)) % 9973}"
    mx, my, mr = MOON.get(kind, (640, 110, 32))
    stars = "".join(f'<circle cx="{rng.random() * W:.0f}" cy="{rng.random() * H * .6:.0f}" r="{rng.random() * 1.1 + .4:.1f}" opacity="{rng.random() * .6 + .2:.2f}"/>' for _ in range(60))
    ridges = ""
    for i, (base, amp, col) in enumerate([(330, 70, "#232a3d"), (390, 60, "#1b2231"), (440, 40, "#141926")]):
        ridges += f'<path d="{_ridge(rng, base, amp)}" fill="{col}"/>'
    ground = f'<path d="M0 440h800v60H0z" fill="{INK}"/>' if kind not in ("ship", "lady", "bird", "sword", "sunken") else ""
    return (f'<svg class="scene" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
            f'<defs><linearGradient id="sk{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#090c14"/><stop offset=".62" stop-color="#1a2032"/>'
            f'<stop offset="1" stop-color="{colour}" stop-opacity=".55"/></linearGradient>'
            f'<radialGradient id="gl{uid}" cx="{mx / W:.2f}" cy="{my / H:.2f}" r=".6"><stop offset="0" stop-color="{colour}" stop-opacity=".34"/><stop offset="1" stop-color="{colour}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="{W}" height="{H}" fill="#0b0e16"/><rect width="{W}" height="{H}" fill="url(#sk{uid})"/><rect width="{W}" height="{H}" fill="url(#gl{uid})"/>'
            f'<g fill="#ece9e1">{stars}</g><circle cx="{mx}" cy="{my}" r="{mr}" fill="#e9d9c6"/>'
            f'{ridges}{ground}{MOTIF[kind](colour)}</svg>')
