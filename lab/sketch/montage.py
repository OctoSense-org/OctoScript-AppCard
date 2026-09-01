#!/usr/bin/env python3
"""Contact sheet: target | themed card, N sampled screens. Evidence, not vibes."""
import pathlib
import random
import sys

from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent


def main():
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 8
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "/tmp/atro_montage.png"
    shots = sorted(p for p in (HERE / "rail").glob("*.png") if p.stem != "baseline")
    random.seed(11)
    sample = random.sample(shots, min(n, len(shots)))
    H, pad, lab = 400, 6, 14
    cols = 4  # pairs per row
    pairs = []
    for png in sample:
        t = HERE / "targets" / f"{png.stem}.png"
        if not t.exists():
            continue
        a = Image.open(t).convert("RGB")
        b = Image.open(png).convert("RGB")
        wa, wb = int(a.width * H / a.height), int(b.width * H / b.height)
        pairs.append((png.stem, a.resize((wa, H)), b.resize((wb, H))))
    pw = max(a.width + b.width + pad for _, a, b in pairs)
    rows = (len(pairs) + cols - 1) // cols
    W = cols * (pw + pad) + pad
    HH = rows * (H + pad + lab) + pad
    s = Image.new("RGB", (W, HH), (16, 16, 18))
    d = ImageDraw.Draw(s)
    for i, (name, a, b) in enumerate(pairs):
        r, c = divmod(i, cols)
        x = pad + c * (pw + pad)
        y = pad + r * (H + pad + lab)
        d.text((x, y), name[:38], fill=(235, 200, 130))
        s.paste(a, (x, y + lab))
        s.paste(b, (x + a.width + pad, y + lab))
    s.save(out)
    print(out, s.size)


if __name__ == "__main__":
    main()
