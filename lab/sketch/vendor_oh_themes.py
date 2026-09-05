#!/usr/bin/env python3
"""Copy the L0 theme chain into Splash-OH so the phone can assemble it itself.

The ArkUI app carries the palettes, axis fragments, derivations and kit as
`include_str!` assets and splices them on the device (see
Splash-OH/crates/splash-oh-native/src/theme.rs). Those files are a COPY of
octos-one/splash-makepad/components/l0, with one transform: the kit goes
through `gen_ohos_atro.adapt()`, which retags what the ArkUI walk has no node
type for and rewrites the handful of constructs that mean something different
there.

Without this, a change to a palette or the kit lands on the desktop and Android
rails and silently does not reach the phone. It was an inline script through the
first device-theme round, which is exactly how the OH copy came to be a version
behind.

    python3 vendor_oh_themes.py [--check]

`--check` reports what would change and exits non-zero, for a pre-flight.
"""
import argparse
import pathlib
import re
import sys

import gen_ohos_atro as G

L0 = G.L0
DEST = G.OH / "assets" / "themes"
# Everything the device-side splice reads, in the order theme.rs splices it.
PATTERNS = ["_palette_*.splash", "_axis_*.splash",
            "_derive_color.splash", "_derive.splash"]

# The type scale, matched to the desktop rail by measurement.
#
# It must be applied where `_derive.splash` COMPUTES the sizes, not restated
# after the kit. This VM binds a function's free names when the function is
# DEFINED, so `let font_caption = 14` appended behind the kit creates a fresh
# binding that `l0_caption` — defined earlier, closed over the old one — never
# sees. A block of five such lets sat in the vendored kit doing nothing at all,
# which is why the phone's body type never moved while its hero did (the hero's
# function is redefined in the tail, and the TREE calls that one).
#
# 1.30 is measured, not chosen: against the desktop render of the same card in
# the same frame, a 6pt forecast label and a 60pt hero were both short by that
# factor. Small type in a frame sized for larger type is also where the page's
# empty lower third came from — nothing was missing, everything was short.
OH_TYPE_SCALE = 1.3


def scale_type(derive: str) -> str:
    """Multiply the five derived type sizes by the OH factor."""
    out, hit = [], 0
    for line in derive.splitlines(True):
        m = re.match(r"(let font_(?:caption|row|body|value|title)\s*=\s*)(.+?)(\s*//.*)?$",
                     line.rstrip("\n"))
        if m:
            hit += 1
            tail = m.group(3) or ""
            out.append(f"{m.group(1)}({m.group(2).strip()}) * {OH_TYPE_SCALE}{tail}\n")
        else:
            out.append(line)
    if hit != 5:
        raise SystemExit(f"_derive.splash: scaled {hit} of 5 type sizes — check the names")
    return "".join(out)


RESCALE = """

// A hero's size does NOT come from the scale above: the lowering computes it
// per card and passes it in as an absolute, so it needs the factor applied
// here or the headline alone stays small while everything around it grows.
// The branch still tests the ORIGINAL value, so a card lands in the same arm
// on both rails.
fn l0_hero(s, pt) {
    if pt >= 43 { return l0_display(l0_txt(s, pt * 1.3 * hero_factor, weight_hero, l0_text)) }
    return l0_display(l0_txt(s, pt * 1.3, weight_hero, l0_text))
}
"""


def write_tables(want: dict) -> tuple:
    """Write the generated mood/axis table, and report what it registered.

    `theme.rs` used to carry these as hand-written macro lists, and they were
    SHORTER than the desktop's without anything saying so: six moods against
    ten, and grounds plus a subset of accents against the whole axis library —
    `type`, `texture`, `density`, `depth` and `emphasis` had no entry at all on
    that backend. A card naming one passed the catalog, reached the phone, and
    rendered as though it had asked for nothing. Generated from the vendored
    files, the device supports exactly what was shipped to it and a gap is a
    missing FILE rather than a line somebody forgot.
    """
    text = render_tables(want)
    (G.OH / "src" / "theme_tables.rs").write_text(text)
    rows = [l for l in text.splitlines() if l.startswith('    ("')]
    axes = [l for l in rows if l.split('"')[1].count(":") == 1 and "include_str" in l
            and not l.split('"')[1].startswith(("dark", "light", "glass", "minimal",
                                                "vibrant", "photo", "atro", "camo"))]
    return len(rows) - len(axes), len(axes)


def render_tables(want: dict) -> str:
    """The generated table, as text, so `--check` can compare it too."""
    moods, axes = [], []
    for n in sorted(want):
        if n.startswith("_palette_"):
            mood = n[len("_palette_"):-len(".splash")]
            src = '""' if mood == "dark" else f'include_str!("../assets/themes/{n}")'
            moods.append(f'    ("{mood}", {src}),')
        elif n.startswith("_axis_"):
            rest = n[len("_axis_"):-len(".splash")]
            kind, _, tail = rest.partition("_")
            key = f"accent:{tail.split('_', 1)[0]}@{tail.split('_', 1)[1]}" \
                if kind == "accent" and "_" in tail else f"{kind}:{tail}"
            axes.append(f'    ("{key}", include_str!("../assets/themes/{n}")),')
    return ("// GENERATED by octos-one/lab/sketch/vendor_oh_themes.py — do not edit.\n"
            "/// Mood deltas, one per vendored palette.\n"
            "pub const PALETTES: &[(&str, &str)] = &[\n" + "\n".join(moods) + "\n];\n\n"
            "/// Axis fragments, keyed `axis:value` or `accent:hue@mood`.\n"
            "pub const AXES: &[(&str, &str)] = &[\n" + "\n".join(axes) + "\n];\n")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true")
    a = p.parse_args()
    DEST.mkdir(parents=True, exist_ok=True)

    want = {}
    for pat in PATTERNS:
        for f in sorted(L0.glob(pat)):
            src = f.read_text()
            want[f.name] = scale_type(src) if f.name == "_derive.splash" else src
    want["_kit.splash"] = G.adapt((L0 / "_kit.splash").read_text()) + RESCALE

    # The generated table counts too. `--check` compared only the copied theme
    # FILES, so a stale `theme_tables.rs` — the very thing that decides which
    # moods and axes the device supports at all — passed a "copy is current"
    # verdict. The file that explains why silence there is dangerous was not
    # itself checked.
    tables = G.OH / "src" / "theme_tables.rs"
    want_tables = render_tables(want)
    changed = [n for n, s in want.items()
               if not (DEST / n).exists() or (DEST / n).read_text() != s]
    if not tables.exists() or tables.read_text() != want_tables:
        changed.append("src/theme_tables.rs")
    if a.check:
        for n in changed:
            print(f"stale: {n}")
        print(f"{len(changed)} of {len(want)} files differ")
        return 1 if changed else 0

    for n, s in want.items():
        (DEST / n).write_text(s)
    gen = write_tables(want)
    print(f"vendored {len(want)} theme files, {len(changed)} changed; "
          f"registered {gen[0]} moods and {gen[1]} axes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
