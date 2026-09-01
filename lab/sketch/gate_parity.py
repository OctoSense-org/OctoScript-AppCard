#!/usr/bin/env python3
"""The parity gate: Splash frozen render vs the CSS reference, deterministically.

The judge drifts and answers only what it is asked; this measures. The CSS
render (Chrome, same compiler logic) is the reference because it is
re-renderable and already ≈ the design. Per screen:

  px        mean absolute pixel difference over the common area (0-255 scale)
  clip      text-clipping proxy: strings from the spec that the CSS render's
            own compile emitted whole — a Splash render that clips mid-word
            diverges most where glyphs are, so px in TEXT ROWS is reported too
  worst     the 3 screens with the highest px, named — the next fix's targets

An iteration of the loop is: change one thing, re-render, re-run this. The
number moves or the change is reverted. LLM judging happens once per few
iterations as a gestalt check, never as the loop signal.

Usage: gate_parity.py [--tag iter0]
"""
import json
import pathlib
import sys

import numpy as np
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent


def norm(path, width=375):
    im = Image.open(path).convert("RGB")
    h = round(im.height * width / im.width)
    return np.asarray(im.resize((width, h), Image.LANCZOS), dtype=np.int16)


def main():
    tag = sys.argv[sys.argv.index("--tag") + 1] if "--tag" in sys.argv else "iter"
    ref_dir = HERE / (sys.argv[sys.argv.index("--ref") + 1] if "--ref" in sys.argv else "targets")
    spl_dir = HERE / (sys.argv[sys.argv.index("--splash") + 1] if "--splash" in sys.argv else "frozen")
    css_dir = HERE / (sys.argv[sys.argv.index("--css") + 1] if "--css" in sys.argv else "css")
    rows = []
    for r in sorted(ref_dir.glob("*.png")):
        f, c = spl_dir / r.name, css_dir / r.name
        if not (f.exists() and c.exists()):
            continue
        ref = norm(r)
        entry = {"screen": r.stem}
        for key, img in (("px", f), ("css_px", c)):
            a = norm(img)
            h = min(a.shape[0], ref.shape[0])
            entry[key] = round(float(np.abs(a[:h] - ref[:h]).mean()), 2)
            # High-frequency "ink" channel: text and hairlines live in the
            # residual after a small box blur. Missing glyphs barely move the
            # raw mean (thin, sparse); they crater this one. Added after a
            # vanished-text regression scored as an improvement.
            if key == "px":
                def hf(x):
                    k = 3
                    blur = np.cumsum(np.cumsum(x.astype(np.float32), 0), 1)
                    return x[k:-k, k:-k].astype(np.float32) - (
                        blur[2*k:, 2*k:] - blur[:-2*k, 2*k:]
                        - blur[2*k:, :-2*k] + blur[:-2*k, :-2*k]) / (2*k)**2
                ha, hr = hf(a[:h].mean(2)), hf(ref[:h].mean(2))
                entry["ink"] = round(float(np.abs(ha - hr).mean()), 2)
        rows.append(entry)
    out = HERE / f"parity-{tag}.json"
    out.write_text(json.dumps(rows))
    px = sorted(r["px"] for r in rows)
    cx = sorted(r["css_px"] for r in rows)
    n = len(px)
    print(f"{tag}: {n} screens vs DESIGN target")
    print(f"  splash px: median {px[n//2]:.1f} · p90 {px[int(n*.9)]:.1f}")
    print(f"  css    px: median {cx[n//2]:.1f} · p90 {cx[int(n*.9)]:.1f}   <- the control")
    ink = sorted(r.get("ink", 0) for r in rows)
    print(f"  splash INK (text/hairline channel): median {ink[n//2]:.1f} · p90 {ink[int(n*.9)]:.1f}")
    worst = sorted(rows, key=lambda r: -r["px"])[:3]
    for w in worst:
        print(f"  worst: {w['screen']:<34} {w['px']}")
    # Delta vs any previous tags on disk.
    for prev in sorted(HERE.glob("parity-*.json")):
        if prev == out:
            continue
        old = {r["screen"]: r["px"] for r in json.loads(prev.read_text())}
        deltas = [r["px"] - old[r["screen"]] for r in rows if r["screen"] in old]
        if deltas:
            import statistics
            print(f"  vs {prev.stem}: median Δpx {statistics.median(deltas):+.2f} "
                  f"({sum(1 for d in deltas if d < -0.5)} improved, "
                  f"{sum(1 for d in deltas if d > 0.5)} regressed)")


if __name__ == "__main__":
    main()
