#!/usr/bin/env python3
"""The shared vector-path stage: Sketch beziers -> rings -> pixels or SVG.

One module feeds all three backends so the comparison stays honest: the target
rasterizer and the Splash icon cache both fill through `render_rings` (XOR
even-odd — a counter ring cancels its outer ring, which is what makes a bell's
clapper hole a hole); the CSS control gets the identical geometry as an inline
<svg> path. Icons stop being silhouette boxes everywhere at once, or nowhere.

Sketch stores each point normalized 0..1 in the layer's own frame, with
curveFrom (outgoing control) and curveTo (incoming control); a straight segment
just has both flags false, which the cubic form degrades to gracefully.
"""
import re

from PIL import Image, ImageChops, ImageDraw


def _pt(s):
    m = re.findall(r"[-\d.eE]+", s or "")
    return (float(m[0]), float(m[1])) if len(m) >= 2 else (0.0, 0.0)


def ring_points(points, closed, steps=14):
    """One Sketch point list -> a flattened polyline ring (normalized coords)."""
    n = len(points)
    if n < 2:
        return []
    segs = n if closed else n - 1
    out = []
    for i in range(segs):
        a, b = points[i], points[(i + 1) % n]
        p0 = _pt(a.get("point"))
        p3 = _pt(b.get("point"))
        p1 = _pt(a.get("curveFrom")) if a.get("hasCurveFrom") else p0
        p2 = _pt(b.get("curveTo")) if b.get("hasCurveTo") else p3
        for k in range(steps):
            t = k / steps
            mt = 1 - t
            x = (mt**3 * p0[0] + 3 * mt**2 * t * p1[0]
                 + 3 * mt * t**2 * p2[0] + t**3 * p3[0])
            y = (mt**3 * p0[1] + 3 * mt**2 * t * p1[1]
                 + 3 * mt * t**2 * p2[1] + t**3 * p3[1])
            out.append((x, y))
    out.append(out[0] if closed else _pt(points[-1].get("point")))
    return out


def render_rings(rings, w, h, rgba, ss=3, ops=None):
    """Fill normalized rings honouring Sketch boolean ops: union rings OR into
    the mask, subtract rings XOR holes out. Pure even-odd was wrong both ways —
    it made a bell's clapper a hole (good) and a phone body's overlapping
    parts a hole too (very bad; measured as the iter1 regression spike)."""
    W, H = max(2, int(w * ss)), max(2, int(h * ss))
    acc = Image.new("1", (W, H), 0)
    ops = ops or [0] * len(rings)
    for ring, op in zip(rings, ops):
        if len(ring) < 3:
            continue
        m = Image.new("1", (W, H), 0)
        ImageDraw.Draw(m).polygon(
            [(x * (W - 1), y * (H - 1)) for x, y in ring], fill=1)
        if op == 1:                      # subtract -> punch a hole
            acc = ImageChops.logical_xor(acc, m)
        else:                            # union / none -> accumulate
            acc = ImageChops.logical_or(acc, m)
    alpha = acc.convert("L").resize((max(1, int(w)), max(1, int(h))),
                                    Image.LANCZOS)
    if isinstance(rgba, Image.Image):
        # a PAINT image (e.g. a gradient) masked by the rings — the case that
        # broke three backends three different ways on the phone-mock body
        paint = rgba.convert("RGBA").resize(alpha.size)
        pa = paint.getchannel("A").point(lambda v: v)
        combined = Image.composite(alpha, Image.new("L", alpha.size, 0),
                                   pa.point(lambda v: 255 if v > 8 else 0))
        out = paint.copy()
        out.putalpha(Image.eval(alpha, lambda v: v))
        return out
    r, g, b, a = rgba
    tile = Image.new("RGBA", alpha.size, (r, g, b, 0))
    tile.putalpha(alpha.point(lambda v: v * a // 255))
    return tile


def svg_d(rings_raw):
    """Sketch point lists -> an SVG path `d` in normalized 0..1 units."""
    parts = []
    for points, closed, _op in rings_raw:
        n = len(points)
        if n < 2:
            continue
        p0 = _pt(points[0].get("point"))
        parts.append(f"M{p0[0]:.4f},{p0[1]:.4f}")
        segs = n if closed else n - 1
        for i in range(segs):
            a, b = points[i], points[(i + 1) % n]
            c1 = _pt(a.get("curveFrom")) if a.get("hasCurveFrom") else _pt(a.get("point"))
            c2 = _pt(b.get("curveTo")) if b.get("hasCurveTo") else _pt(b.get("point"))
            p = _pt(b.get("point"))
            parts.append(f"C{c1[0]:.4f},{c1[1]:.4f} {c2[0]:.4f},{c2[1]:.4f} "
                         f"{p[0]:.4f},{p[1]:.4f}")
        if closed:
            parts.append("Z")
    return "".join(parts)


def collect_rings(layer):
    """A shapePath's own ring, or a shapeGroup's children merged into one
    even-odd set — each child's points mapped through its frame within the
    group, which is what turns a bell outline + clapper into one glyph."""
    cls = layer.get("_class")
    if cls == "shapePath" and layer.get("points"):
        return [(layer["points"], layer.get("isClosed", True), -1)], None
    if cls in ("rectangle", "oval", "triangle", "polygon") and layer.get("points"):
        return [(layer["points"], True, -1)], None
    if cls == "shapeGroup":
        gw = layer.get("frame", {}).get("width") or 1
        gh = layer.get("frame", {}).get("height") or 1
        raw = []
        for ch in layer.get("layers", []):
            if not ch.get("points"):
                continue
            f = ch.get("frame", {})
            op = ch.get("booleanOperation", -1)
            ox, oy = f.get("x", 0) / gw, f.get("y", 0) / gh
            sx, sy = (f.get("width", 0) or 0) / gw, (f.get("height", 0) or 0) / gh
            mapped = []
            for p in ch["points"]:
                q = dict(p)
                for key in ("point", "curveFrom", "curveTo"):
                    x, y = _pt(p.get(key))
                    q[key] = f"{{{ox + x * sx}, {oy + y * sy}}}"
                mapped.append(q)
            raw.append((mapped, ch.get("isClosed", True), op))
        return raw, None
    return None, None
