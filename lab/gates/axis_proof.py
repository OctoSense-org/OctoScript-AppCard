#!/usr/bin/env python3
"""Every theme axis, and what it actually changes on screen.

`accent_proof.py` answered one axis. This answers all five, and it exists
because "wired" is a claim about the render and not about the code: four of
these fragments have been on disk and correct since the grammar landed, and were
reachable by nothing. A table that shows a column of zeroes is the same finding
in a different costume, so the useful output is per-axis and per-effect.

Two effects are measured separately, because an axis that moves neither is
disconnected and an axis that moves the wrong one is miswired:

  ink        the share of text nodes whose `fg` changed
  geometry   the share of nodes whose box moved or resized

`accent` should move ink and not geometry. `density`, `emphasis` and `radius`
should move geometry and not ink. `icons` moves neither on a card with no icons,
which is why the card under test needs some.

Usage:  axis_proof.py [--card PATH]
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from accent_proof import OUT, render, themed  # noqa: E402
import shoot  # noqa: E402

AXES = [
    ("accent", ["amber", "blue", "violet"]),
    ("radius", ["none", "large", "full"]),
    ("density", ["compact", "airy"]),
    ("emphasis", ["quiet", "poster"]),
    ("icons", ["filled", "mono"]),
    ("texture", ["paper", "deco", "halftone"]),
    ("depth", ["hard", "glow"]),
    ("type", ["serif", "display"]),
]


def nodes(doc):
    return {n["i"]: n for n in doc["widgets"]}


def deltas(base, other):
    a, b = nodes(base), nodes(other)
    shared = set(a) & set(b)
    ink_nodes = [i for i in shared
                 if (a[i].get("text") or "").strip() and a[i].get("fg")]
    ink = sum(1 for i in ink_nodes if a[i].get("fg") != b[i].get("fg"))
    geo = sum(1 for i in shared
              if (a[i].get("x"), a[i].get("y"), a[i].get("w"), a[i].get("h"))
              != (b[i].get("x"), b[i].get("y"), b[i].get("w"), b[i].get("h")))
    # A count of nodes understates a uniform shift; the page height says whether
    # the CARD changed size, which is what density and emphasis are for.
    def page_h(d):
        return max((n.get("y", 0) + n.get("h", 0)) for n in d["widgets"])
    return (ink, len(ink_nodes), geo, len(shared),
            page_h(other) - page_h(base))


def pixels(card_path, tag, data):
    """Mean per-pixel difference against the baseline render.

    The geometry dump is blind to anything that is a DRAW property rather than a
    box: a corner radius, a shadow, a typeface. Those axes read 0/0 here and are
    not therefore disconnected — `radius`, `depth` and `type` all measure as
    working when the screen is compared instead. So the proof needs both columns,
    or it reports a working axis as dead and the next person deletes it.
    """
    png = OUT / f"{tag}.png"
    if not png.exists():
        shoot.shoot(card_path, png, None, data=data)
    return png if png.exists() else None


def mean_diff(a, b):
    from PIL import Image, ImageChops, ImageStat
    ia = Image.open(a).convert("RGB")
    ib = Image.open(b).convert("RGB")
    if ia.size != ib.size:
        return float("nan")
    return ImageStat.Stat(ImageChops.difference(ia, ib)).mean[0]


def themed_axis(src, mood, axis, value):
    line = f"theme {mood} {axis}: .{value}"
    return "\n".join(line if ln.strip().startswith("theme ") else ln
                     for ln in src.splitlines()) + "\n"


def main():
    card_path = (pathlib.Path(sys.argv[sys.argv.index("--card") + 1])
                 if "--card" in sys.argv
                 else HERE / "e2e_batch" / "01-weather-ref_mockup" / "card.card")
    OUT.mkdir(exist_ok=True)
    src = card_path.read_text()
    mood = next((ln.split()[1] for ln in src.splitlines()
                 if ln.strip().startswith("theme ")), "dark")
    data = card_path.parent / "data.json"

    base = render(themed(src, mood, None), "ax-base", data)
    if base is None:
        print("baseline render produced no geometry")
        return 1
    print(f"card {card_path.name} · mood {mood} · "
          f"{len(base['widgets'])} nodes\n")
    base_png = pixels(OUT / "ax-base.card", "ax-base", data)
    print(f"{'axis':<10} {'value':<9} {'ink moved':>12} {'boxes moved':>13} "
          f"{'px diff':>8}")
    for axis, values in AXES:
        for v in values:
            doc = render(themed_axis(src, mood, axis, v), f"ax-{axis}-{v}", data)
            if doc is None:
                print(f"{axis:<10} {v:<9} {'no geometry':>12}")
                continue
            ink, ninks, geo, nall, _ = deltas(base, doc)
            png = pixels(OUT / f"ax-{axis}-{v}.card", f"ax-{axis}-{v}", data)
            px = mean_diff(base_png, png) if (base_png and png) else float("nan")
            flag = "" if (ink or geo or px > 0.3) else "   <- DISCONNECTED"
            print(f"{axis:<10} {v:<9} {ink:>4}/{ninks:<3} {100*ink/max(1,ninks):3.0f}% "
                  f"{geo:>5}/{nall:<3} {100*geo/max(1,nall):3.0f}% {px:>8.2f}{flag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
