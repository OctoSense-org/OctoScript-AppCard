#!/usr/bin/env python3
"""Does the render carry the same INK as its reference?

`gate_fill.py` asks whether pixels differ from the page background. That
question has a blind spot big enough to ship through: a card whose panels draw
but whose bound VALUES resolve to nothing is a page of large flat rectangles,
and every one of them differs from the background. The ArkUI weather card
scored 98% "filled" while showing seven forecast rows with no temperatures, no
condition, and no hero — a screen with almost nothing on it.

So this measures ink instead: local edge energy, which text and icons have and
a flat panel does not. And it measures it DIFFERENTIALLY, against the same card
on a rail known good, because an absolute ink number has no meaning across
themes — a light card on white and a dark card on black are both correct.

    python3 gate_ink.py --ref desktop.png --shot device.png [--json]

`missing` is the fraction of reference cells carrying ink where the candidate
has none. Above MISSING_MAX the render is dropping content, whatever its fill
score says.
"""
import argparse
import json
import sys

import numpy as np
from PIL import Image

# The comparison grid. Fine enough that a row with a day name but no
# temperature reads as three empty cells out of four, coarse enough to absorb
# the aspect-ratio difference between a phone and a desktop window.
ROWS, COLS = 48, 12
# An edge is worth counting at 6% of the frame's own dynamic range; below that
# is JPEG mush and panel borders.
EDGE = 0.06
# A cell is inked if this fraction of its pixels sit on an edge. One glyph in a
# cell clears it; a panel corner radius does not.
CELL_INK = 0.012
# Above this a candidate is dropping reference content outright: bands the
# reference inks that the candidate leaves entirely bare. Calibrated against
# the desktop and Android renders of one card, which differ only in layout.
BAND_MISSING_MAX = 0.12
# Coarse backstop for content lost sideways rather than in whole bands.
CELL_MISSING_MAX = 0.75


def ink_grid(path):
    """Per-cell ink presence, plus the raw fraction of inked cells."""
    im = Image.open(path).convert("L")
    # Trim a phone's status and gesture bars: they carry ink no card asked for.
    w, h = im.size
    im = im.crop((0, int(h * 0.02), w, int(h * 0.985)))
    a = np.asarray(im.resize((COLS * 24, ROWS * 24), Image.LANCZOS), dtype=np.float32)
    rng = a.max() - a.min()
    if rng < 1e-6:
        return np.zeros((ROWS, COLS), bool), 0.0
    a = (a - a.min()) / rng
    edge = np.zeros_like(a)
    edge[:, 1:] += np.abs(np.diff(a, axis=1))
    edge[1:, :] += np.abs(np.diff(a, axis=0))
    on = edge > EDGE
    cells = on.reshape(ROWS, 24, COLS, 24).mean(axis=(1, 3))
    grid = cells > CELL_INK
    return grid, float(grid.mean())


def compare(ref_path, shot_path):
    ref, ref_ink = ink_grid(ref_path)
    shot, shot_ink = ink_grid(shot_path)
    # Two correct rails put the same content at slightly different heights —
    # different aspect ratios, a status bar on one, a window chrome on the
    # other. Measured between the desktop and Android renders of one card that
    # drift alone accounted for 26% of cells, which is most of the way to a
    # failing score on a page with nothing wrong. So a reference cell counts as
    # covered when the candidate has ink in the SAME COLUMN within one row.
    # Columns stay strict: a row that keeps its label and loses its value is
    # exactly what this exists to catch.
    reach = shot.copy()
    reach[1:] |= shot[:-1]
    reach[:-1] |= shot[1:]
    n = int(ref.sum())
    missing = float((ref & ~reach).sum() / n) if n else 0.0
    lost_rows = [i for i in range(ROWS) if (ref[i] & ~reach[i]).sum() >= 2]
    # `missing` counts a cell that moved sideways the same as one that is gone,
    # and two correct rails do move things sideways: a flexible blank pushes a
    # forecast row's temperatures to the far edge on one and centres them on
    # the other. `bands` asks the weaker question — does this band carry ink at
    # all — which separates content that RELOCATED from content that vanished.
    ref_bands = ref.any(1)
    band_missing = float((ref_bands & ~reach.any(1)).sum() / max(1, ref_bands.sum()))
    return {
        "ref_ink": round(ref_ink, 3),
        "shot_ink": round(shot_ink, 3),
        "missing": round(missing, 3),
        "band_missing": round(band_missing, 3),
        # Two ways to fail. A band the reference inks and the candidate leaves
        # entirely bare is content that is GONE. And a candidate that keeps one
        # column per row while losing the rest scores 92% missing cells with
        # every band still "inked" — it passed on band_missing alone, which made
        # this a report rather than a gate. The cell ceiling is deliberately
        # loose: two correct rails measured 0.008-0.696 apart on layout drift,
        # the ArkUI card that had lost its values measured 0.829.
        "ok": band_missing <= BAND_MISSING_MAX and missing <= CELL_MISSING_MAX,
        "lost_bands": [round(i / ROWS, 2) for i in lost_rows],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ref", required=True, help="render on a rail known good")
    p.add_argument("--shot", required=True, help="render under test")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    r = compare(a.ref, a.shot)
    if a.json:
        print(json.dumps(r))
    else:
        print(f"ref ink {r['ref_ink']:.1%}  shot ink {r['shot_ink']:.1%}  "
              f"cells missing {r['missing']:.1%}  bands bare {r['band_missing']:.1%}  "
              f"{'OK' if r['ok'] else 'DROPPING CONTENT'}")
        if r["lost_bands"]:
            print("lost bands (fraction down the page): "
                  + ", ".join(f"{b:.2f}" for b in r["lost_bands"][:20]))
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
