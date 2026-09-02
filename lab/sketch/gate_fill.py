#!/usr/bin/env python3
"""The frame-fill gate: catches squeezed / letterboxed renders deterministically.

A row is CONTENT if its pixels vary horizontally (a flat page row — solid or
vertical-gradient — is near-uniform across x). Per screen, measure the
fraction of content rows and where content ends, in the target and in the
render; a render whose content stops well short of the target's is squeezed,
no judge required.

    gate_fill.py --kit <name> --rail desktop|android|ohos

Writes xrail/fill_<kit>_<rail>.jsonl:
    {screen, target_fill, render_fill, target_bottom, render_bottom,
     flag: "squeezed"|"overflow"|null, note}
"""
import json
import pathlib
import sys

import numpy as np
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import kitconf  # noqa: E402

ROW_STD = 6.0      # horizontal stddev above this = a content row
SHORTFALL = 0.12   # render content ends this much earlier than target = squeezed
FILL_RATIO = 0.70  # or render has under 70% of the target's content rows


def profile(path):
    im = Image.open(path).convert("L").resize((150, 300), Image.BILINEAR)
    a = np.asarray(im, dtype=np.float32)
    # ignore a thin frame border on each side
    a = a[:, 6:-6]
    act = a.std(axis=1) > ROW_STD
    rows = np.where(act)[0]
    if len(rows) == 0:
        return 0.0, 0.0
    return float(act.mean()), float(rows.max() / a.shape[0])


def main():
    kit = kitconf.load(sys.argv[sys.argv.index("--kit") + 1]
                       if "--kit" in sys.argv else "atro")
    rail = sys.argv[sys.argv.index("--rail") + 1] if "--rail" in sys.argv else "desktop"
    shots = kit[f"{rail}_dir"]
    out = HERE / "xrail" / f"fill_{kit['name']}_{rail}.jsonl"
    out.parent.mkdir(exist_ok=True)
    rows, flags = [], 0
    for name in kit["screens"]:
        t, x = kit["targets_dir"] / f"{name}.png", shots / f"{name}.png"
        if not (t.exists() and x.exists()):
            continue
        tf, tb = profile(t)
        rf, rb = profile(x)
        flag = note = None
        if tb - rb > SHORTFALL or rf < tf * FILL_RATIO:
            flag = "squeezed"
            note = (f"content fills {rf:.0%} of the frame and ends at "
                    f"{rb:.0%} height; the design fills {tf:.0%} and ends at "
                    f"{tb:.0%} — stretch sections, size media taller, and "
                    f"include the design's remaining rows")
            flags += 1
        elif rb - tb > SHORTFALL and tb < 0.85:
            flag = "overflow"
            note = "content runs past where the design stops"
        rows.append({"screen": name, "target_fill": round(tf, 3),
                     "render_fill": round(rf, 3), "target_bottom": round(tb, 3),
                     "render_bottom": round(rb, 3), "flag": flag, "note": note})
        mark = f"  << {flag.upper()}" if flag else ""
        print(f"{name:<34} target {tf:4.0%}/{tb:4.0%}  render {rf:4.0%}/{rb:4.0%}{mark}")
    out.write_text("".join(json.dumps(r) + "\n" for r in rows))
    print(f"\n{rail}: {flags}/{len(rows)} flagged -> {out.name}")


if __name__ == "__main__":
    main()
