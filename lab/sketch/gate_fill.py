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
MISSING_MAX = 0.18  # design fills this fraction the render leaves empty = squeezed


def _mask(path):
    """A per-row 'has content' mask + the page background colour.

    Content = rows that are NOT the flat page background. A flat card counts
    (its fill differs from the page), a photo counts, text counts; only the
    uniform page gutter is 'dead'. This is what pixel-variance got wrong —
    a flat-but-correct card read as empty because it lacked texture."""
    im = Image.open(path).convert("RGB").resize((120, 300), Image.BILINEAR)
    a = np.asarray(im, dtype=np.float32)[:, 8:-8, :]
    # background = the median of the four corners (page colour, light or dark)
    corners = np.concatenate([a[:6, :6], a[:6, -6:], a[-6:, :6], a[-6:, -6:]]
                             ).reshape(-1, 3)
    bg = np.median(corners, axis=0)
    near_bg = (np.abs(a - bg).sum(2) < 36)          # pixel ~= page colour
    row_content = near_bg.mean(1) < 0.90            # <90% background = content row
    return row_content


def profile(path):
    """fill fraction and content-bottom, from the dead-space mask."""
    m = _mask(path)
    rows = np.where(m)[0]
    if len(rows) == 0:
        return 0.0, 0.0, m
    return float(m.mean()), float(rows.max() / len(m)), m


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
        tf, tb, tm = profile(t)
        rf, rb, rm = profile(x)
        # The real signal: rows the DESIGN fills but the RENDER leaves empty.
        # Symmetric flatness (a flat card in both) cancels; only genuine
        # missing content survives. Design-only chrome (a keyboard) still
        # shows here — a small, known residual.
        missing = float((tm & ~rm).mean())
        flag = note = None
        if missing > MISSING_MAX:
            flag = "squeezed"
            note = (f"the design fills {tf:.0%} of the frame; the render leaves "
                    f"{missing:.0%} of it empty where the design has content — "
                    f"add the missing sections, size media taller, keep lists complete")
            flags += 1
        rows.append({"screen": name, "target_fill": round(tf, 3),
                     "render_fill": round(rf, 3), "target_bottom": round(tb, 3),
                     "render_bottom": round(rb, 3), "missing": round(missing, 3),
                     "flag": flag, "note": note})
        mark = f"  << SQUEEZED (missing {missing:.0%})" if flag else ""
        print(f"{name:<34} design {tf:4.0%}  render {rf:4.0%}  missing {missing:4.0%}{mark}")
    out.write_text("".join(json.dumps(r) + "\n" for r in rows))
    print(f"\n{rail}: {flags}/{len(rows)} flagged -> {out.name}")


if __name__ == "__main__":
    main()
