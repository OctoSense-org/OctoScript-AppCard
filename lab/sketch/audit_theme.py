#!/usr/bin/env python3
"""Can the ink a pack states be READ on the surfaces that pack states?

The ground x accent audit answered 112/112 and missed this entirely, because it
only ever checked ink against the PAGE. A card carries its own fill — CaMo's
black slab, Atro's indigo gradient — stated once in the pack's base palette and
inherited unchanged by that pack's light variant, which also flips the ink dark.
CaMo light therefore drew near-black text on a pure black card: unreadable, on
the desktop and the phone alike, and invisible to a fill gate because the slab
is opaque.

So: every surface a pack states, against the ink that pack states, at AA.

    python3 audit_theme.py [--dir <components/l0>]

Static by design — it reads the literal `argb(...)` a palette states. Grounds
and accents rebind the ink at derive time and are out of scope here; this is
the base pair, which is where the bug lived.
"""
import argparse
import pathlib
import re
import sys

DEFAULT_DIR = pathlib.Path.home() / "home/octos-one/splash-makepad/components/l0"
AA = 4.5
# WCAG's large-text floor. Between this and AA a surface carries headings but
# not body copy, which is a real state and not the same as unreadable.
AA_LARGE = 3.0
# Surfaces text sits on, the ink that sits on them, and what to call it.
# A card states its own ink because the pack's card colour does not flip when
# the pack's light variant flips `l0_text`.
# Checking only the PRIMARY ink was a hole the size of the roles that use the
# others: `l0_caption` draws in `l0_dim` and `l0_row_text` in `l0_soft`, and
# neither was ever measured. The base light mood's `l0_dim` sits at 2.92
# against its page — below AA, below even the large-text floor — while the
# auditor reported "0 unreadable".
SURFACES = [("l0_card_1", "l0_card_ink", "card"),
            ("l0_card_2", "l0_card_ink", "card, far end"),
            ("l0_fill", "l0_text", "panel"),
            ("l0_fill", "l0_soft", "panel, row text"),
            ("l0_fill", "l0_dim", "panel, caption"),
            ("l0_base", "l0_text", "page"),
            ("l0_base", "l0_soft", "page, row text"),
            ("l0_base", "l0_dim", "page, caption")]


def literals(path):
    """Every `let <name> = argb(a, r, g, b)` a palette states."""
    out = {}
    for m in re.finditer(r"let\s+(\w+)\s*=\s*argb\(\s*(\d+)\s*,\s*(\d+)\s*,"
                         r"\s*(\d+)\s*,\s*(\d+)\s*\)", path.read_text()):
        name, a, r, g, b = m.group(1), *(int(x) for x in m.groups()[1:])
        out[name] = (a, r, g, b)
    return out


def _lin(c):
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def rlum(rgb):
    r, g, b = (_lin(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(c1, c2):
    a, b = rlum(c1), rlum(c2)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def over(top, ground):
    """A translucent surface is the colour you SEE, not the colour stated.

    Panel fills are commonly a low-alpha white lift over the page (`argb(18,
    255, 255, 255)`), and read literally that is white-on-white — a failure
    the eye never sees.
    """
    a = top[0] / 255
    return tuple(round(top[i + 1] * a + ground[i] * (1 - a)) for i in (0, 1, 2))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dir", type=pathlib.Path, default=DEFAULT_DIR)
    a = p.parse_args()

    packs = sorted(a.dir.glob("_palette_*.splash"))
    base = literals(a.dir / "_palette_dark.splash")
    bad = warn = 0
    for pack in packs:
        v = dict(base)
        v.update(literals(pack))
        name = pack.stem.replace("_palette_", "")
        # A pack with no card of its own states `let l0_card_1 = 0` — a plain
        # zero, which `literals()` does not match, so the name is ABSENT here.
        # A pack with a BLACK card states `argb(255, 0, 0, 0)`, which is present
        # and whose rgb is also (0,0,0). Testing the colour could not tell those
        # apart, so this skipped exactly the pack it was written for: CaMo's
        # opaque black card went unchecked, and restoring the near-black ink
        # that made it unreadable at 1.14 would still have passed. Presence, not
        # colour.
        flat_card = "l0_card_1" not in v and "l0_card_2" not in v
        for key, ink_key, what in SURFACES:
            fill, ink = v.get(key), v.get(ink_key)
            if not fill or not ink:
                continue
            if key.startswith("l0_card") and flat_card:
                continue
            page = v.get("l0_base", (255, 0, 0, 0))
            seen = over(fill, page[1:])
            c = contrast(over(ink, seen), seen)
            if c >= AA:
                continue
            level, note = ("FAIL", "unreadable") if c < AA_LARGE else \
                ("WARN", "large text only")
            bad += level == "FAIL"
            warn += level == "WARN"
            print(f"{level} {name:<12} {what:<14} {c:5.2f}  {note:<16}"
                  f"#{ink[1]:02x}{ink[2]:02x}{ink[3]:02x} on "
                  f"#{fill[1]:02x}{fill[2]:02x}{fill[3]:02x}")
    print(f"{bad} unreadable, {warn} large-text-only" if bad or warn
          else "every stated surface carries its ink at AA")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
