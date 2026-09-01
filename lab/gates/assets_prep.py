#!/usr/bin/env python3
"""Gate and prepare the generated elements. An asset is not usable because it
looks right in a contact sheet.

Two checks and one conversion, all cheap and all deterministic:

  tiles      A texture prompted "seamless" is not seamless because it was asked
             to be. Wrapping it means column 0 sits against column -1, so if
             that join is far worse than an ordinary interior join, the seam is
             visible and the asset is a picture rather than a texture.

  neutral    A texture prompted "greyscale" often is not — a warm paper comes
             back warm. Any residual chroma survives into the render and fights
             whatever accent the card names, which is precisely the disconnected
             knob this week was spent removing. Measured as max channel spread,
             and stripped rather than reported, because stripping is correct.

  slice      Icon sheets become twelve transparent PNGs. Black-on-white is a
             picture of an icon; alpha is an icon, because only alpha can take
             `l0_text` and follow the palette.

Usage:  assets_prep.py [--dir assets]
"""
import pathlib
import sys

from PIL import Image, ImageChops

HERE = pathlib.Path(__file__).resolve().parent
GLYPHS = ["sun", "cloud", "rain", "snow", "wind", "moon",
          "thermometer", "umbrella", "arrow-up", "arrow-down", "clock", "pin"]
COLS, ROWS = 4, 3
# A seam that is more than this many times worse than an ordinary interior join
# is visible. Chosen from the measured spread rather than from taste: a genuinely
# seamless tile lands near 1.0 because the wrap join IS an ordinary join.
SEAM_MAX = 2.0
# Residual chroma worth stripping. 8/255 is roughly where a tint stops being
# noise and starts being a colour.
CHROMA_MAX = 8


def seam_ratio(im):
    """How much worse the wrap join is than an average interior join."""
    g = im.convert("L")
    w, h = g.size
    px = g.load()

    def col_diff(a, b):
        return sum(abs(px[a, y] - px[b, y]) for y in range(0, h, 2)) / (h / 2)

    def row_diff(a, b):
        return sum(abs(px[x, a] - px[x, b]) for x in range(0, w, 2)) / (w / 2)

    interior_c = sum(col_diff(x, x + 1) for x in range(w // 4, 3 * w // 4, 37))
    interior_c /= len(range(w // 4, 3 * w // 4, 37))
    interior_r = sum(row_diff(y, y + 1) for y in range(h // 4, 3 * h // 4, 37))
    interior_r /= len(range(h // 4, 3 * h // 4, 37))
    return (col_diff(0, w - 1) / max(0.5, interior_c),
            row_diff(0, h - 1) / max(0.5, interior_r))


def chroma(im):
    """Largest per-pixel channel spread — 0 for a true greyscale."""
    r, g, b = im.convert("RGB").split()
    hi = ImageChops.lighter(ImageChops.lighter(r, g), b)
    lo = ImageChops.darker(ImageChops.darker(r, g), b)
    return ImageChops.difference(hi, lo).getextrema()[1]


def slice_icons(path, out_dir):
    """A 4x3 sheet into twelve transparent PNGs, cropped to their own ink."""
    im = Image.open(path).convert("L")
    w, h = im.size
    cw, ch = w // COLS, h // ROWS
    out_dir.mkdir(parents=True, exist_ok=True)
    made = []
    for i, name in enumerate(GLYPHS):
        r, c = divmod(i, COLS)
        cell = im.crop((c * cw, r * ch, (c + 1) * cw, (r + 1) * ch))
        # Ink is dark on white, so alpha is the INVERSE of luminance. This is
        # what makes the icon tintable: the renderer multiplies a colour through
        # the alpha, and a black-on-white RGB would paint the white too.
        alpha = ImageChops.invert(cell)
        box = alpha.point(lambda v: 255 if v > 40 else 0).getbbox()
        if box is None:
            made.append((name, "EMPTY"))
            continue
        alpha = alpha.crop(box)
        rgba = Image.new("RGBA", alpha.size, (255, 255, 255, 0))
        rgba.putalpha(alpha)
        rgba.save(out_dir / f"{name}.png")
        made.append((name, f"{alpha.size[0]}x{alpha.size[1]}"))
    return made


def main():
    root = HERE / (sys.argv[sys.argv.index("--dir") + 1] if "--dir" in sys.argv else "assets")

    print("textures\n" + "-" * 58)
    print(f"{'name':<14} {'seam x/y':>13} {'chroma':>7}  verdict")
    for p in sorted((root / "texture").glob("*.png")):
        sx, sy = seam_ratio(Image.open(p))
        ch = chroma(Image.open(p))
        tiles = max(sx, sy) <= SEAM_MAX
        if ch > CHROMA_MAX:
            g = Image.open(p).convert("L").convert("RGB")
            g.save(p.with_name(p.stem + "-grey.png"))
        verdict = ("tiles" if tiles else "SEAM VISIBLE")
        if ch > CHROMA_MAX:
            verdict += f" · stripped to grey ({p.stem}-grey.png)"
        print(f"{p.stem:<14} {sx:5.2f} / {sy:5.2f} {ch:>7}  {verdict}")

    print("\nicon sheets\n" + "-" * 58)
    for p in sorted((root / "icons").glob("*.png")):
        if p.stem.endswith("-grey"):
            continue
        made = slice_icons(p, root / "icons" / p.stem)
        empty = [n for n, s in made if s == "EMPTY"]
        print(f"{p.stem:<8} {len(made) - len(empty):>2}/12 sliced"
              + (f"  · empty: {', '.join(empty)}" if empty else ""))

    print("\nheroes\n" + "-" * 58)
    for p in sorted((root / "hero").glob("*.png")):
        im = Image.open(p)
        # The top third carries the title, so its BUSYNESS is what decides
        # whether a scrim can save it. Reported, not gated: the scrim solves for
        # the worst case already, and a busy sky is a legitimate photograph.
        top = im.convert("L").crop((0, 0, im.width, im.height // 3))
        lo, hi = top.getextrema()
        print(f"{p.stem:<16} {im.size[0]}x{im.size[1]}  top-third range {lo}-{hi}")


if __name__ == "__main__":
    main()
