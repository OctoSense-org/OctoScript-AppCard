#!/usr/bin/env python3
"""The measured stretch loop: close red gaps without an LLM.

For every screen the dead-space gate flags, compute the fill ratio between
design and render, inject `media_stretch` through the palette-override hook
(the env slot the kit assembly already splices), and re-render. Media heights
and card paddings grow by the measured ratio; the page fills with CONTENT,
not blank space. One extra render per flagged screen, deterministic.

Usage: fill_fix.py --kit <name> [--max 1.9]
"""
import json
import os
import pathlib
import sys

import numpy as np
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "gates"))
import kitconf  # noqa: E402
from gate_fill import profile  # noqa: E402  (dead-space mask)


def main():
    kit = kitconf.load(sys.argv[sys.argv.index("--kit") + 1]
                       if "--kit" in sys.argv else "atro")
    cap = float(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 2.7
    os.environ["GATE_WINDOW"] = "375x906"
    os.environ["MAKEPAD_SEED_L0_FILL_HEIGHT"] = "812"
    import shoot
    shoot.SIZE = "375x906"
    gate = HERE / "xrail" / f"fill_{kit['name']}_desktop.jsonl"
    rows = [json.loads(l) for l in gate.open()]
    data = kit["desktop_dir"] / "data.json"
    fixed = 0
    for r in rows:
        if not r.get("flag"):
            continue
        name = r["screen"]
        _, _, tm = profile(kit["targets_dir"] / f"{name}.png")
        tf = r["target_fill"]
        rf = max(r["render_fill"], 0.08)
        png = kit["desktop_dir"] / f"{name}.png"
        stretch, missing2 = 1.0, r["missing"]
        # Two measured passes: the second compounds on the first's residual.
        for _round in range(2):
            stretch = min(cap, max(1.15, stretch * tf / rf))
            ov = pathlib.Path(f"/tmp/stretch_{name}.splash")
            # Type carries list screens: grow the ramp at just over half the
            # stretch rate (full-rate text wraps everything); font_base rebinds
            # against the pack value and derive recomputes the whole ramp.
            fscale = 1 + (stretch - 1) * 0.55
            ov.write_text(f"let media_stretch = {stretch:.2f}\n"
                          f"let font_base = font_base * {fscale:.2f}\n")
            ok = shoot.shoot(kit["cards_dir"] / f"{name}.card", png, ov,
                             data=data, keep_pt=818)
            if not ok:
                print(f"{name}: render failed", flush=True)
                break
            f2, _, rm = profile(png)
            missing2 = float((tm & ~rm).mean())
            rf = max(f2, 0.08)
            if missing2 <= 0.18 or stretch >= cap - 0.01:
                break
        verdict = "CLOSED" if missing2 <= 0.18 else "still short"
        if missing2 <= 0.18:
            fixed += 1
        print(f"{name:<34} stretch x{stretch:.2f}  missing {r['missing']:.0%} -> "
              f"{missing2:.0%}  {verdict}", flush=True)
    print(f"\nfill-fix: {fixed} closed of {sum(1 for r in rows if r.get('flag'))} flagged")


if __name__ == "__main__":
    main()
