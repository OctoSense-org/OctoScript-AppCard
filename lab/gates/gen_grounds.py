#!/usr/bin/env python3
"""Generate the `ground` axis — SEEDS, not palettes.

The difference from `gen_accent_axes.py` is the whole architecture lesson: that
generator wrote 48 complete solved palettes because the kit could not compute a
colour; this one writes NINE NUMBERS per ground and lets `_derive_color.splash`
compute the palette in-kit. A new ground is three seed triplets, not a file of
literals — the Ant seed model, running in the kit's own language.

What stays offline is exactly one thing: the AA clamp on the ink. That is an
iterative search, and the honest place for a search is the generator; the seed
it emits is already legal, and the derivation that consumes it preserves
legality by construction (secondary inks step back from a solved primary).

Every ground here is one the 150-screen Atro ledger or the mockup corpus asked
for and the mood set could not say — the deco teal included.

Usage: gen_grounds.py [--check]
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from e4_roundtrip import clamp_ink, contrast, rgb  # noqa: E402

L0 = HERE.parent.parent / "splash-makepad" / "components" / "l0"

# name -> (ground hex, natural ink hex, accent hex). The ink states the
# DESIGN'S polarity and gets clamped to AA; the accent is the hue that suits
# the ground when the card names none (a card's `accent:` still overrides).
GROUNDS = {
    # the two the review called unreachable, first
    "teal":       ("#0d3b34", "#e8c76a", "#d4a83c"),   # the Art Deco page
    "violet":     ("#140f26", "#ffffff", "#645aff"),   # Atro's dark screens
    "navy":       ("#17212d", "#ffffff", "#4c5fef"),   # Atro's slate screens
    "ivory":      ("#f6f1e7", "#2a2420", "#9a7817"),
    "sand":       ("#e8dcc8", "#3a3226", "#b05f2c"),
    "terracotta": ("#b4552d", "#ffe9d8", "#ffd9a0"),   # the Florence mockup
    "wine":       ("#4a1526", "#f2dfe0", "#e08273"),
    "forest":     ("#15291d", "#dcefe2", "#67c795"),
    "slate":      ("#232a33", "#e6ebf1", "#79b7dd"),
    "paper":      ("#fafafa", "#1c1c1e", "#3d48b8"),
    "cream":      ("#f4ead8", "#4a3a24", "#9a6c10"),
    "midnight":   ("#0a1030", "#dfe6ff", "#6d79f0"),
    "blush":      ("#f6e3e1", "#4a2830", "#b03a5e"),
    "olive":      ("#3a3d26", "#eef0d8", "#c9c26a"),
}


def seeds(name, g_hex, i_hex, a_hex):
    g, i0, a = rgb(g_hex), rgb(i_hex), rgb(a_hex)
    i = clamp_ink(g, i0)
    c = contrast(g, i)
    moved = "" if i == i0 else f" (clamped {contrast(g, i0):.1f} -> {c:.1f}:1)"
    return "\n".join([
        f"// Axis delta: ground .{name} — nine seeds; `_derive_color.splash`",
        "// computes the palette from them in-kit. Compare `gen_accent_axes.py`,",
        "// which had to ship 48 solved files because nothing could compute.",
        f"// Ink {c:.2f}:1 on this ground{moved}.",
        "let seed_on       = 1",
        f"let seed_ground_r = {g[0]}",
        f"let seed_ground_g = {g[1]}",
        f"let seed_ground_b = {g[2]}",
        f"let seed_ink_r    = {i[0]}",
        f"let seed_ink_g    = {i[1]}",
        f"let seed_ink_b    = {i[2]}",
        f"let seed_accent_r = {a[0]}",
        f"let seed_accent_g = {a[1]}",
        f"let seed_accent_b = {a[2]}",
        "",
    ])


def main():
    check = "--check" in sys.argv
    print(f"{'ground':<12} {'ink':>9}")
    for name, (g, i, a) in GROUNDS.items():
        src = seeds(name, g, i, a)
        if not check:
            (L0 / f"_axis_ground_{name}.splash").write_text(src)
        gi = clamp_ink(rgb(g), rgb(i))
        print(f"{name:<12} {contrast(rgb(g), gi):>6.2f}:1")
    print(f"\n{len(GROUNDS)} ground fragments -> {L0}  "
          f"({'check only' if check else '9 seeds each'})")


if __name__ == "__main__":
    main()
