#!/usr/bin/env python3
"""Frozen-fidelity compiler: Sketch spec -> the L3 widget dialect, directly.

This is the CSS-equivalence experiment, built as an instrument. Every node maps
1:1 — absolute position via Overlay+margin, exact colours, exact sizes, the
kit's own fonts and photos — with NO roles, NO theme, NO data. The output is a
poster: pixel-faithful and dead. Its value is attribution: whatever still
differs from the target after this compile is a RENDERER gap (stroke, masks,
angled gradients), with the card language fully out of the equation.

Usage: spec2dsl.py <specs-dir> <out-dir> [--only substr]
"""
import json
import pathlib
import sys

S = 0.5  # spec @2x -> logical
# makepad's font_size is NOT points: measured empirically, a size-20 label
# advances ~18px per character (near-square glyphs), ~1.6x a 20pt font. Both
# rails' "type 2-3x oversized" verdicts were this one unit mismatch. 0.62
# brings cap-height to parity with the design's point sizes.
FONT_SCALE = 0.62

FONTS = {"Thin": "Roboto-Thin", "Light": "Roboto-Light"}
def face_of(name):
    name = name or ""
    for w in ("SemiBold", "Bold", "Medium", "Regular"):
        if name.endswith(w):
            # Bold face isn't bundled for Montserrat; SemiBold is the kit's bold.
            m = {"Bold": "Montserrat-SemiBold", "SemiBold": "Montserrat-SemiBold",
                 "Medium": "Montserrat-Medium", "Regular": "Montserrat-Regular"}[w]
            return m
    return "Montserrat-Regular"


def hexa(c, default="00000000"):
    if not c:
        return default
    a = round(255 * c.get("a", 1))
    return f"{c['hex'][1:]}{a:02x}"


def style_label(run, w, line_spacing=None):
    face = face_of(run.get("font"))
    size = (run.get("size") or 24) * S * FONT_SCALE
    col = hexa(run.get("c"), "000000ff")
    ls = f' line_spacing: {line_spacing:.1f}' if line_spacing else ""
    return (f'draw_text.color: #{col} draw_text.text_style: TextStyle{{ '
            f'font_family: FontFamily{{ latin := FontMember{{ res: '
            f'crate_resource("makepad_widgets:resources/{face}.ttf") '
            f'asc: 0.0 desc: 0.0 }} }} font_size: {size:.1f}{ls} }}')


class Comp:
    def __init__(self):
        self.out = []
        self.stats = {"nodes": 0, "text": 0, "img": 0, "shape": 0,
                      "masked_skipped": 0, "gradient": 0}

    def emit(self, line):
        self.out.append("    " + line)
        self.stats["nodes"] += 1

    def box(self, n):
        return (n["x"] * S, n["y"] * S, max(1.0, n["w"] * S), max(1.0, n["h"] * S))

    def pos(self, x, y, w, h):
        return (f'width: {w:.1f} height: {h:.1f} '
                f'margin: Inset{{left: {x:.1f} right: 0 top: {y:.1f} bottom: 0}}')

    def fill_view(self, n, radius=None, alpha_mul=1.0):
        # Layer opacity — extracted since day one, applied by nobody. Scrims
        # and washes are MADE of this.
        alpha_mul *= n.get("opacity", 1.0)
        x, y, w, h = self.box(n)
        r = radius if radius is not None else (n.get("radius", 0) * S)
        bits = [self.pos(x, y, w, h)]
        widget = "RoundedView"
        sh = n.get("shadow")
        if sh and sh.get("c"):
            widget = "RoundedShadowView"
            bits.append(f'draw_bg.shadow_color: #{hexa(sh["c"])} '
                        f'draw_bg.shadow_radius: {sh.get("blur", 0) * S:.1f} '
                        f'draw_bg.shadow_offset: vec2({sh.get("dx", 0) * S:.1f}, '
                        f'{sh.get("dy", 0) * S:.1f})')
        g = n.get("gradient")
        if g and g.get("stops"):
            self.stats["gradient"] += 1
            stops = sorted(g["stops"], key=lambda s: s["p"])
            bits.append(f'draw_bg.color: #{hexa(stops[0]["c"])}')
            bits.append(f'draw_bg.color_2: #{hexa(stops[-1]["c"])}')
            (fx, fy), (tx, ty) = g.get("from", (0, 0)), g.get("to", (0, 1))
            import math
            ang = math.degrees(math.atan2(tx - fx, ty - fy))
            if abs(ang) < 8 or abs(abs(ang) - 180) < 8:
                pass                                    # vertical: the default
            elif abs(abs(ang) - 90) < 8:
                bits.append("draw_bg.gradient_fill_horizontal: 1.0")
            else:
                # the new renderer uniform — Atro's signature diagonals
                bits.append(f"draw_bg.gradient_angle: {ang:.1f}")
        elif n.get("fill"):
            c = dict(n["fill"])
            c["a"] = c.get("a", 1) * alpha_mul
            bits.append(f'draw_bg.color: #{hexa(c)}')
        else:
            return
        if r:
            bits.append(f'draw_bg.border_radius: {min(r, w / 2, h / 2):.1f}')
        st = n.get("stroke")
        if st and st.get("c"):
            # Known not to draw (the stroke bug) — emitted anyway so the
            # residue shows it honestly.
            bits.append(f'draw_bg.border_size: {st.get("w", 1) * S:.1f} '
                        f'draw_bg.border_color: #{hexa(st["c"])}')
        self.emit(f'{widget}{{ {" ".join(bits)} }}')

    ICON_DIR = pathlib.Path(
        "/private/tmp/claude-501/-Users-user-home-Splash/"
        "df6c4ec5-2002-4e8f-84de-7d846576918e/scratchpad/atro/src/images/_icons")

    def icon_tile(self, n):
        """Rasterize the node's rings once, cache by content, serve over 8787.

        The renderer never learns about beziers — it loads a PNG like any
        photo, which is why this lands with zero renderer risk. Stroked paths
        (the line-icon library) draw as polylines; filled ones as even-odd."""
        import hashlib, json as _json
        import paths as P
        from PIL import Image as I, ImageDraw as D
        w = max(2, int(n["w"] * S * 2))   # @2x so the stretch stays crisp
        h = max(2, int(n["h"] * S * 2))
        fill, st = n.get("fill"), n.get("stroke")
        grad = n.get("gradient")
        op = n.get("opacity", 1.0)
        key = hashlib.md5(_json.dumps(
            [n["rings"], n.get("ring_ops"), fill, st, grad, op, w, h]).encode()).hexdigest()[:16]
        self.ICON_DIR.mkdir(exist_ok=True)
        out = self.ICON_DIR / f"{key}.png"
        if not out.exists():
            if grad and grad.get("stops"):
                sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
                from spec2png import lin_gradient
                paint = lin_gradient(w, h, grad)
                if op < 0.999:
                    paint.putalpha(paint.getchannel("A").point(lambda v: int(v * op)))
                tile = P.render_rings(n["rings"], w, h, paint,
                                      ops=n.get("ring_ops"))
            elif fill:
                hx = fill["hex"].lstrip("#")
                rgba = (int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16),
                        round(255 * fill.get("a", 1) * op))
                tile = P.render_rings(n["rings"], w, h, rgba, ops=n.get("ring_ops"))
            elif st and st.get("c"):
                hx = st["c"]["hex"].lstrip("#")
                col = (int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16),
                       round(255 * st["c"].get("a", 1)))
                tile = I.new("RGBA", (w, h), (0, 0, 0, 0))
                d = D.Draw(tile)
                lw = max(1, round(st.get("w", 1) * S * 2))
                for ring in n["rings"]:
                    d.line([(px * (w - 1), py * (h - 1)) for px, py in ring],
                           fill=col, width=lw, joint="curve")
            else:
                return None
            tile.save(out)
        return f"_icons/{key}.png"

    def walk(self, n):
        cls = n.get("cls")
        if n.get("mask"):
            self.stats["masked_skipped"] += 1
        x, y, w, h = self.box(n)
        if cls in ("rectangle",):
            self.fill_view(n)
        elif cls == "oval":
            self.fill_view(n, radius=min(w, h) / 2)
        elif cls in ("shapePath", "shapeGroup", "triangle", "polygon"):
            if n.get("rings"):
                ref = self.icon_tile(n)
                if ref:
                    self.stats["icons_svg"] = self.stats.get("icons_svg", 0) + 1
                    # Never below 2px: a 1px-high Stretch image poisoned the
                    # draw pass and every LATER sibling vanished (the missing
                    # country names). Hairline vector strips render as fills
                    # instead — same pixels, no degenerate texture math.
                    if w < 2.5 or h < 2.5:
                        self.fill_view(n, radius=0)
                        return
                    self.emit(f'Image{{ {self.pos(x, y, max(w, 2.5), max(h, 2.5))} '
                              f'fit: ImageFit.Stretch '
                              f'src: http_resource("http://127.0.0.1:8787/{ref}") }}')
                    return
            if n.get("fill") or n.get("gradient"):
                self.stats["shape"] += 1
                self.fill_view(n, radius=min(w, h) * 0.2, alpha_mul=0.92)
        elif cls == "bitmap" and n.get("image"):
            ref = n["image"].split("/")[-1]
            self.stats["img"] += 1
            self.emit(f'Image{{ {self.pos(x, y, w, h)} fit: ImageFit.CropToFill '
                      f'src: http_resource("http://127.0.0.1:8787/{ref}") }}')
        elif cls == "text":
            t = n.get("text") or {}
            s = " ".join((t.get("string") or "").split())
            if s:
                self.stats["text"] += 1
                run = t.get("run") or {}
                esc = s.replace("\\", "\\\\").replace('"', '\\"')
                align = run.get("align", 0)
                size = (run.get("size") or 24) * S * FONT_SCALE
                # Sketch text boxes hug the design font's own metrics; ours
                # differ slightly, so a pinned width wraps "card balance" into
                # "card". A run whose box is one line tall gets a natural-width
                # Label; only genuinely multi-line runs keep the box width.
                one_line = h <= size * 2.0 / FONT_SCALE * 0.62 * 2.0 or h <= (run.get("size") or 24) * S * 1.9
                ax = {0: 0.0, 2: 0.5, 1: 1.0}.get(align, 0.0)
                if one_line:
                    # Width clamp ESTIMATED FROM THE RENDERER'S OWN METRICS:
                    # makepad advances ~0.9 x font_size per character (probe-
                    # measured), so this container can hold the whole run and
                    # clipping is impossible without floating the label free.
                    # (A bare margin-positioned Label collapsed to the origin —
                    # iter2's vanished-country-names regression, which the px
                    # gate barely registered because thin glyphs are few
                    # pixels. Hence the ink column.)
                    est = size * 0.92 * len(s) + 8
                    cw = max(w * 1.1, min(est, 372 - x))
                    lab = (f'Label{{ width: Fit height: Fit text: "{esc}" '
                           f'{style_label(run, w)} }}')
                    self.emit(f'View{{ {self.pos(x, y, cw, h + 6)} '
                              f'flow: Down align: Align{{x: {ax}}} {lab} }}')
                else:
                    # Multi-line: makepad's line box equals font_size (measured),
                    # so after the 0.62 calibration the pitch lands at ~0.62pt
                    # against the design's ~1.25pt — paragraphs compress into
                    # each other. line_spacing 2.0 restores the design pitch.
                    lab = (f'Label{{ width: Fill height: Fit text: "{esc}" '
                           f'{style_label(run, w, line_spacing=2.0)} }}')
                    self.emit(f'View{{ {self.pos(x, y, w + 10, h + 8)} flow: Down '
                              f'align: Align{{x: {ax}}} {lab} }}')
        # gradients/fills on groups/instances that carry their own background
        elif (n.get("fill") or n.get("gradient")) and cls in ("group", "symbolInstance"):
            self.fill_view(n)
        for c in n.get("children", []):
            self.walk(c)

    def compile(self, spec):
        bg = hexa(spec.get("fill"), "ffffffff") if spec.get("fill") else "ffffffff"
        # Explicit page size: the seed path hosts the body in a fit-height
        # column, where a Fill-height root collapses to zero and paints nothing.
        pw, ph = spec["w"] * S, spec["h"] * S
        head = (f'// FROZEN compile of {spec.get("name", "?")} — spec2dsl.py.\n'
                f'// A poster, not an app: no roles, no data, no theme.\n'
                f'View{{ flow: Overlay width: {pw:.0f} height: {ph:.0f} '
                f'draw_bg.color: #{bg}\n')
        for c in spec.get("children", []):
            self.walk(c)
        return head + "\n".join(self.out) + "\n}\n"


def main():
    specs = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[2])
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else ""
    out.mkdir(parents=True, exist_ok=True)
    for p in sorted(specs.glob("*.json")):
        if only and only not in p.stem:
            continue
        c = Comp()
        dsl = c.compile(json.loads(p.read_text()))
        (out / f"{p.stem}.dsl").write_text(dsl)
        print(f"{p.stem:<32} {c.stats}")


if __name__ == "__main__":
    main()
