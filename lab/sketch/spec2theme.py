#!/usr/bin/env python3
"""Project each spec's style system onto L0 — with a quantization ledger.

Two outputs per screen, kept deliberately separate:

  themes/<name>.splash   the palette L0 RENDERS — built by the E4 solver
                         (`palette_src`) from the screen's ground+ink+accent, so
                         contrast holds by construction. Spliced in through the
                         override slot, because that is the slot that exists.

  ledger.jsonl           what the CARD LANGUAGE could have said — every screen
                         value projected to its nearest axis token with the
                         delta logged. This is the honest gap price: the render
                         path can show the skin today; the syntax cannot yet
                         name most of it.

Extraction is by structure, not by average: the ground is the largest opaque
covering fill (the `bg` rect every kit screen carries), the ink is the modal
text colour ON that ground, the accent is the most saturated gradient stop —
the mistakes the naive hue-picker made on the deco target, made unmakeable by
reading the tree instead of the pixels.

Usage: spec2theme.py <specs-dir> <out-dir>
"""
import collections
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "gates"))
from e4_roundtrip import contrast, palette_src  # noqa: E402
from gen_accent_axes import HUES, MOODS, mood_surfaces  # noqa: E402

RADII = {"none": 0, "small": 6, "large": 20, "full": 100}


def rgb(c):
    h = c["hex"].lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def sat(c):
    r, g, b = rgb(c)
    return (max(r, g, b) - min(r, g, b)) / max(1, max(r, g, b))


def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5


def collect(spec):
    fills = collections.Counter()
    inks = collections.Counter()
    grads = collections.Counter()
    radii = collections.Counter()
    fonts = collections.Counter()
    shadows = []

    def walk(n, depth):
        a = n.get("fill")
        area = n["w"] * n["h"]
        if a and a["a"] > 0.85 and area > 40000:
            fills[(a["hex"], depth)] += area
        g = n.get("gradient")
        if g:
            for s in g["stops"]:
                if s["c"] and sat(s["c"]) > 0.25:
                    grads[s["c"]["hex"]] += n["w"] * n["h"]
        # Saturated FLAT fills are accents too — the sign-in button is one
        # indigo rectangle, and only collecting gradient stops missed it, so
        # that screen's "accent" fell back to white ink.
        if a and sat(a) > 0.3 and a["a"] > 0.5:
            grads[a["hex"]] += n["w"] * n["h"] * 0.6
        if n.get("radius") and n["w"] > 40:
            radii[round(n["radius"])] += 1
        if n.get("shadow"):
            shadows.append(n["shadow"])
        t = n.get("text")
        if t and t.get("run"):
            r = t["run"]
            if r.get("c"):
                inks[r["c"]["hex"]] += len(t.get("string") or "")
            if r.get("font"):
                fonts[r["font"]] += 1
        for ch in n.get("children", []):
            walk(ch, depth + 1)

    walk(spec, 0)
    return fills, inks, grads, radii, fonts, shadows


def project(spec):
    fills, inks, grads, radii, fonts, shadows = collect(spec)
    # Ground: the largest SHALLOW covering fill — depth breaks the tie between
    # the page and a big panel sitting on it.
    ground = None
    if fills:
        (ground, _), _ = min(fills.items(),
                             key=lambda kv: (kv[0][1], -kv[1]))
    if not ground and spec.get("fill"):
        ground = spec["fill"]["hex"]
    ground = ground or "#ffffff"
    g = rgb({"hex": ground})
    # Ink: modal text colour that actually reads on that ground.
    ink = None
    for h, _ in inks.most_common(6):
        if contrast(rgb({"hex": h}), g) >= 2.2:
            ink = h
            break
    ink = ink or ("#ffffff" if sum(g) < 380 else "#131315")
    # An accent has to be SEEN AGAINST the ground and must not BE the ground:
    # scrim violets (huge, ground-adjacent) and white highlight stops both
    # passed a bare saturation test and became "accents" on the first run.
    def plausible(h):
        c = rgb({"hex": h})
        return (dist(c, g) > 70 and max(c) > 60 and min(c) < 235)
    cand = {h: wt for h, wt in grads.items() if plausible(h)}
    accent = max(cand.items(), key=lambda kv: kv[1])[0] if cand else None
    if not accent:
        ic = [(h, n) for h, n in inks.items()
              if sat({"hex": h}) > 0.35 and plausible(h)]
        accent = max(ic, key=lambda kv: kv[1])[0] if ic else ink
    radius = radii.most_common(1)[0][0] if radii else 0
    font = fonts.most_common(1)[0][0] if fonts else ""
    shadow = max(shadows, key=lambda s: s.get("blur", 0)) if shadows else None
    return dict(ground=ground, ink=ink, accent=accent, radius=radius,
                font=font, shadow=shadow)


def quantize(want):
    """The nearest thing the CARD SYNTAX can say, with deltas."""
    led = {}
    g = rgb({"hex": want["ground"]})
    best = min(MOODS, key=lambda m: dist(mood_surfaces(m)[0], g))
    led["ground"] = {"want": want["ground"],
                     "got": f"theme {best}",
                     "delta": round(dist(mood_surfaces(best)[0], g), 1)}
    a = rgb({"hex": want["accent"]})
    hue = min(HUES, key=lambda h: dist(HUES[h], a))
    led["accent"] = {"want": want["accent"], "got": f"accent: .{hue}",
                     "delta": round(dist(HUES[hue], a), 1)}
    # Radii in the spec are @2x; L0 speaks logical px.
    r = want["radius"] / 2
    tok = min(RADII, key=lambda k: abs(RADII[k] - r))
    led["radius"] = {"want": r, "got": f"radius: .{tok}",
                     "delta": round(abs(RADII[tok] - r), 1)}
    led["type"] = {"want": want["font"],
                   "got": "family: geometric" if want["font"].startswith("Montserrat")
                   else "family: sans",
                   "delta": 0 if want["font"].startswith("Montserrat") else None}
    if want["shadow"]:
        s = want["shadow"]
        which = ".glow" if s.get("dy", 0) <= 2 and s.get("blur", 0) > 30 else ".soft"
        led["depth"] = {"want": f'{s["c"]["hex"]}@{s["c"]["a"]} b{s["blur"]} dy{s["dy"]}',
                        "got": f"depth: {which}", "delta": None}
    return led, best, hue


def main():
    specs = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[2])
    (out / "themes").mkdir(parents=True, exist_ok=True)
    ledger = (out / "ledger.jsonl").open("w")
    n = 0
    for p in sorted(specs.glob("*.json")):
        spec = json.loads(p.read_text())
        want = project(spec)
        led, mood, hue = quantize(want)
        src = palette_src(want["ground"], want["ink"], want["accent"])
        if src is None:
            continue
        # The kit's type, carried through the same override slot: the family
        # the emitter maps and the tracking the spec measured.
        src += ('\n// type, from the kit\'s own text runs\n'
                'let l0_family         = "geometric"\n'
                'let l0_display_family = "geometric"\n')
        (out / "themes" / f"{p.stem}.splash").write_text(src)
        ledger.write(json.dumps({"screen": p.stem, "want": {
            k: v for k, v in want.items() if k != "shadow"},
            "ledger": led, "nearest_mood": mood, "nearest_hue": hue}) + "\n")
        n += 1
    ledger.close()
    print(f"{n} themes -> {out}/themes · ledger -> {out}/ledger.jsonl")


if __name__ == "__main__":
    main()
