#!/usr/bin/env python3
"""Rasterize a spec tree into a target PNG.

Honesty first: this is a SPEC-faithful render, not a Sketch-faithful one. What
it reproduces exactly are the attributes the fidelity gate scores — boxes,
fills, gradients, radii, text content/face/size/colour. What it approximates is
logged per file: vector icon paths draw as their silhouette bounds, masks clip
to rects, blurs are skipped. Judging L0 against these therefore measures the
mappable style surface, which is the claim under test — not Sketch's rendering
quality.

Usage: spec2png.py <specs-dir> <out-dir> [--scale 0.5] [--only name-substr]
"""
import json
import pathlib
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).resolve().parent
FONT = HERE / "fonts" / "Montserrat-var.ttf"
WEIGHTS = {"Thin": 250, "Light": 300, "Regular": 400, "Medium": 500,
           "SemiBold": 600, "Bold": 700, "ExtraBold": 800, "Black": 900}

_fonts = {}


def font_for(name, size):
    w = 400
    for suffix, wt in WEIGHTS.items():
        if name and name.endswith(suffix):
            w = wt
            break
    key = (w, round(size))
    if key not in _fonts:
        f = ImageFont.truetype(str(FONT), round(size))
        try:
            f.set_variation_by_axes([w])
        except Exception:
            pass
        _fonts[key] = f
    return _fonts[key]


def rgba(c, default=(0, 0, 0, 255)):
    if not c:
        return default
    h = c["hex"].lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16),
            round(255 * c.get("a", 1)))


def lin_gradient(w, h, g):
    """A linear gradient by projecting each pixel onto the from->to axis."""
    (fx, fy), (tx, ty) = g["from"], g["to"]
    fx, fy, tx, ty = fx * w, fy * h, tx * w, ty * h
    dx, dy = tx - fx, ty - fy
    denom = dx * dx + dy * dy or 1.0
    ys, xs = np.mgrid[0:h, 0:w]
    t = np.clip(((xs - fx) * dx + (ys - fy) * dy) / denom, 0, 1)
    stops = sorted(g["stops"], key=lambda s: s["p"])
    ps = [s["p"] for s in stops]
    cols = np.array([rgba(s["c"]) for s in stops], dtype=float)
    out = np.zeros((h, w, 4), dtype=float)
    for ch in range(4):
        out[..., ch] = np.interp(t, ps, cols[:, ch])
    return Image.fromarray(out.astype(np.uint8), "RGBA")


class Raster:
    def __init__(self, spec, scale):
        self.s = scale
        self.W, self.H = round(spec["w"] * scale), round(spec["h"] * scale)
        self.im = Image.new("RGBA", (self.W, self.H), (255, 255, 255, 255))
        self.approx = {"shapes": 0, "masks": 0, "missing_img": 0}
        self.images_dir = None

    def box(self, n):
        s = self.s
        return (round(n["x"] * s), round(n["y"] * s),
                round((n["x"] + n["w"]) * s), round((n["y"] + n["h"]) * s))

    def paint_fill(self, n, alpha_mul=1.0):
        alpha_mul *= n.get("opacity", 1.0)
        x0, y0, x1, y1 = self.box(n)
        w, h = max(1, x1 - x0), max(1, y1 - y0)
        r = round(n.get("radius", 0) * self.s)
        layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        shape_kwargs = dict(radius=min(r, w // 2, h // 2)) if r else {}
        draw_fn = d.rounded_rectangle if r else d.rectangle
        if n.get("gradient"):
            grad = lin_gradient(w, h, n["gradient"])
            mask = Image.new("L", (w, h), 0)
            md = ImageDraw.Draw(mask)
            (md.rounded_rectangle if r else md.rectangle)(
                (0, 0, w - 1, h - 1), fill=255, **shape_kwargs)
            layer = Image.composite(grad, layer, mask)
        elif n.get("fill"):
            col = rgba(n["fill"])
            col = col[:3] + (round(col[3] * alpha_mul),)
            if n["cls"] == "oval":
                d.ellipse((0, 0, w - 1, h - 1), fill=col)
            else:
                draw_fn((0, 0, w - 1, h - 1), fill=col, **shape_kwargs)
        if n.get("stroke") and n["stroke"].get("c"):
            sw = max(1, round(n["stroke"]["w"] * self.s))
            (d.rounded_rectangle if r else d.rectangle)(
                (0, 0, w - 1, h - 1), outline=rgba(n["stroke"]["c"]),
                width=sw, **shape_kwargs)
        self.im.alpha_composite(layer, (x0, y0))

    def paint_text(self, n):
        t = n["text"]
        s = (t.get("string") or "").strip()
        run = t.get("run") or {}
        if not s or not run.get("size"):
            return
        f = font_for(run.get("font") or "", run["size"] * self.s)
        col = rgba(run.get("c"))
        x0, y0, x1, y1 = self.box(n)
        d = ImageDraw.Draw(self.im)
        # Multi-line wrap to the node's width, coarse but shaped like the design.
        words, lines, cur = s.split(), [], ""
        for wd in words:
            trial = (cur + " " + wd).strip()
            if d.textlength(trial, font=f) <= (x1 - x0) or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = wd
        lines.append(cur)
        lh = round(run["size"] * self.s * 1.25)
        total = lh * len(lines)
        y = y0 + max(0, ((y1 - y0) - total) // 2)
        align = run.get("align", 0)
        for ln in lines[:6]:
            wpx = d.textlength(ln, font=f)
            x = x0
            if align == 2:
                x = x0 + ((x1 - x0) - wpx) // 2
            elif align == 1:
                x = x1 - wpx
            d.text((x, y), ln, font=f, fill=col)
            y += lh

    def paint_rings(self, n):
        """The actual vector: filled even-odd, or stroked polylines for the
        line-icon style where the path has a stroke and no fill."""
        import paths as P
        x0, y0, x1, y1 = self.box(n)
        w, h = max(1, x1 - x0), max(1, y1 - y0)
        fill = n.get("fill")
        st = n.get("stroke")
        op = n.get("opacity", 1.0)
        if n.get("gradient"):
            paint = lin_gradient(w, h, n["gradient"])
            if op < 0.999:
                paint.putalpha(paint.getchannel("A").point(lambda v: int(v * op)))
            tile = P.render_rings(n["rings"], w, h, paint,
                                  ops=n.get("ring_ops"))
            self.im.alpha_composite(tile, (x0, y0))
        elif fill:
            hx = fill["hex"].lstrip("#")
            rgba = (int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16),
                    round(255 * fill.get("a", 1) * op))
            tile = P.render_rings(n["rings"], w, h, rgba, ops=n.get("ring_ops"))
            self.im.alpha_composite(tile, (x0, y0))
        elif st and st.get("c"):
            hx = st["c"]["hex"].lstrip("#")
            col = (int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16),
                   round(255 * st["c"].get("a", 1)))
            layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
            d = ImageDraw.Draw(layer)
            lw = max(1, round(st.get("w", 1) * self.s))
            for ring in n["rings"]:
                d.line([(px * (w - 1), py * (h - 1)) for px, py in ring],
                       fill=col, width=lw, joint="curve")
            self.im.alpha_composite(layer, (x0, y0))

    def paint_image(self, n):
        ref = n.get("image")
        # refs may be bare filenames or "images/<hash>.png" — the dir is
        # already the images dir, so resolve by basename.
        p = (self.images_dir / pathlib.Path(ref).name
             if (ref and self.images_dir) else None)
        if not (p and p.exists()):
            self.approx["missing_img"] += 1
            return
        try:
            img = Image.open(p).convert("RGBA")
        except Exception:
            self.approx["missing_img"] += 1
            return
        x0, y0, x1, y1 = self.box(n)
        img = img.resize((max(1, x1 - x0), max(1, y1 - y0)))
        self.im.alpha_composite(img, (x0, y0))

    def walk(self, n):
        cls = n.get("cls")
        if n.get("mask"):
            self.approx["masks"] += 1
        if cls in ("rectangle", "oval"):
            self.paint_fill(n)
        elif cls in ("shapePath", "shapeGroup", "triangle", "polygon"):
            if n.get("rings"):
                self.paint_rings(n)
            elif n.get("fill") or n.get("gradient"):
                # No path data survived — silhouette bounds, logged.
                self.approx["shapes"] += 1
                self.paint_fill(n, alpha_mul=0.9)
        elif cls == "bitmap":
            self.paint_image(n)
        elif cls == "text":
            self.paint_text(n)
        elif n.get("fill") or n.get("gradient"):
            # A group or instance that carries its own background.
            self.paint_fill(n)
        for ch in n.get("children", []):
            self.walk(ch)


def render(spec_path, out_path, images_dir, scale):
    spec = json.loads(spec_path.read_text())
    r = Raster(spec, scale)
    r.images_dir = images_dir
    if spec.get("fill"):
        ImageDraw.Draw(r.im).rectangle((0, 0, r.W, r.H), fill=rgba(spec["fill"]))
    for ch in spec.get("children", []):
        r.walk(ch)
    r.im.convert("RGB").save(out_path)
    return r.approx


def main():
    specs = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    scale = float(sys.argv[sys.argv.index("--scale") + 1]) if "--scale" in sys.argv else 0.5
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else ""
    if "--images" in sys.argv:
        images = pathlib.Path(sys.argv[sys.argv.index("--images") + 1])
    else:
        images = specs.parent / "images"
        if not images.exists():
            images = pathlib.Path(
                "/private/tmp/claude-501/-Users-user-home-Splash/"
                "df6c4ec5-2002-4e8f-84de-7d846576918e/scratchpad/atro/src/images")
    total = {"shapes": 0, "masks": 0, "missing_img": 0}
    n = 0
    for p in sorted(specs.glob("*.json")):
        if only and only not in p.stem:
            continue
        a = render(p, out / f"{p.stem}.png", images, scale)
        for k in total:
            total[k] += a[k]
        n += 1
    print(f"{n} targets -> {out} · approximations: {total}")


if __name__ == "__main__":
    main()
