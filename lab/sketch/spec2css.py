#!/usr/bin/env python3
"""The CSS control: the same spec, compiled to HTML/CSS, rendered by Chrome.

Same walk, same silhouette-icon approximation, same coordinates as spec2dsl —
the ONLY variable is the backend. What CSS adds natively is exactly the widget
layer's measured gap list: borders that draw, angled multi-stop gradients, real
text metrics. If the browser render judges high, that difference is the
renderer's bill, itemized; if it judges low, strict parity was never on the
table for anyone and the expectation recalibrates.

Usage: spec2css.py <specs-dir> <out-dir> [--only substr]
"""
import json
import pathlib
import sys

S = 0.5
IMG = ("/private/tmp/claude-501/-Users-yuechen-home-Splash/"
       "df6c4ec5-2002-4e8f-84de-7d846576918e/scratchpad/atro/src/images")
FONT = str(pathlib.Path(__file__).resolve().parent / "fonts" / "Montserrat-var.ttf")

WEIGHTS = {"Thin": 250, "Light": 300, "Regular": 400, "Medium": 500,
           "SemiBold": 600, "Bold": 700, "ExtraBold": 800}


def weight_of(name):
    for w, v in WEIGHTS.items():
        if (name or "").endswith(w):
            return v
    return 400


def rgba(c, default="transparent"):
    if not c:
        return default
    h = c["hex"].lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{c.get('a', 1):.3f})"


class Css:
    def __init__(self):
        self.out = []
        self.stats = {"nodes": 0, "borders": 0, "grad_angled": 0}

    def emit(self, style, inner=""):
        self.out.append(f'<div style="{style}">{inner}</div>')
        self.stats["nodes"] += 1

    def pos(self, n, dh=0.0):
        return (f"position:absolute;left:{n['x']*S:.1f}px;top:{n['y']*S:.1f}px;"
                f"width:{n['w']*S:.1f}px;height:{n['h']*S+dh:.1f}px;")

    def fill_div(self, n, radius=None, alpha_mul=1.0):
        alpha_mul *= n.get("opacity", 1.0)
        r = radius if radius is not None else n.get("radius", 0) * S
        bits = [self.pos(n)]
        g = n.get("gradient")
        if g and g.get("stops"):
            stops = sorted(g["stops"], key=lambda s: s["p"])
            (fx, fy), (tx, ty) = g.get("from", (0, 0)), g.get("to", (0, 1))
            import math
            ang = math.degrees(math.atan2(tx - fx, ty - fy))
            if abs(ang) > 8 and abs(abs(ang) - 90) > 8 and abs(abs(ang) - 180) > 8:
                self.stats["grad_angled"] += 1
            css_stops = ",".join(f'{rgba(s["c"])} {s["p"]*100:.0f}%' for s in stops)
            bits.append(f"background:linear-gradient({180-ang:.0f}deg,{css_stops});")
            if alpha_mul < 0.999:
                bits.append(f"opacity:{alpha_mul:.3f};")
        elif n.get("fill"):
            c = dict(n["fill"]); c["a"] = c.get("a", 1) * alpha_mul
            bits.append(f"background:{rgba(c)};")
        else:
            return
        if r:
            bits.append(f"border-radius:{r:.1f}px;")
        st = n.get("stroke")
        if st and st.get("c"):
            self.stats["borders"] += 1
            bits.append(f"border:{max(0.5, st.get('w',1)*S):.1f}px solid {rgba(st['c'])};"
                        f"box-sizing:border-box;")
        sh = n.get("shadow")
        if sh and sh.get("c"):
            bits.append(f"box-shadow:{sh.get('dx',0)*S:.0f}px {sh.get('dy',0)*S:.0f}px "
                        f"{sh.get('blur',0)*S:.0f}px {rgba(sh['c'])};")
        self.emit("".join(bits))

    def walk(self, n):
        cls = n.get("cls")
        if cls == "rectangle":
            self.fill_div(n)
        elif cls == "oval":
            self.fill_div(n, radius=min(n["w"], n["h"]) * S / 2)
        elif cls in ("shapePath", "shapeGroup", "triangle", "polygon"):
            if n.get("svg_d"):
                fill = n.get("fill")
                st = n.get("stroke")
                if fill:
                    attrs = f'fill="{rgba(fill)}" fill-rule="{n.get("svg_rule", "nonzero")}"'
                elif st and st.get("c"):
                    sw = st.get("w", 1) / max(n["w"], 1)
                    attrs = (f'fill="none" stroke="{rgba(st["c"])}" '
                             f'stroke-width="{sw:.4f}" stroke-linejoin="round"')
                else:
                    attrs = 'fill="#000"'
                self.out.append(
                    f'<svg style="{self.pos(n)}" viewBox="0 0 1 1" '
                    f'preserveAspectRatio="none"><path d="{n["svg_d"]}" {attrs}/></svg>')
                self.stats["nodes"] += 1
            elif n.get("fill") or n.get("gradient"):
                self.fill_div(n, radius=min(n["w"], n["h"]) * S * 0.2, alpha_mul=0.92)
        elif cls == "bitmap" and n.get("image"):
            ref = n["image"].split("/")[-1]
            self.emit(self.pos(n) + f"background:url('file://{IMG}/{ref}') center/cover;"
                      + (f"border-radius:{n.get('radius',0)*S:.0f}px;" if n.get("radius") else ""))
        elif cls == "text":
            t = n.get("text") or {}
            s = " ".join((t.get("string") or "").split())
            if s:
                run = t.get("run") or {}
                size = (run.get("size") or 24) * S
                al = {0: "left", 2: "center", 1: "right"}.get(run.get("align", 0), "left")
                esc = s.replace("&", "&amp;").replace("<", "&lt;")
                self.emit(self.pos(n, dh=6) +
                          f"font:{weight_of(run.get('font'))} {size:.1f}px Montserrat;"
                          f"color:{rgba(run.get('c'), '#000')};text-align:{al};"
                          f"line-height:1.25;overflow:visible;white-space:normal;", esc)
        elif (n.get("fill") or n.get("gradient")) and cls in ("group", "symbolInstance"):
            self.fill_div(n)
        for c in n.get("children", []):
            self.walk(c)

    def compile(self, spec):
        self.out = []
        for c in spec.get("children", []):
            self.walk(c)
        bg = rgba(spec.get("fill"), "#fff") if spec.get("fill") else "#fff"
        return f"""<!doctype html><meta charset="utf-8">
<style>
@font-face {{ font-family: Montserrat; src: url("file://{FONT}"); font-weight: 100 900; }}
* {{ margin:0; box-sizing:content-box; }}
body {{ width:375px; height:812px; overflow:hidden; background:{bg};
       font-family:Montserrat; position:relative; }}
</style>
<body>{"".join(self.out)}</body>"""


def main():
    specs = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[2])
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else ""
    out.mkdir(parents=True, exist_ok=True)
    for p in sorted(specs.glob("*.json")):
        if only and only not in p.stem:
            continue
        c = Css()
        html = c.compile(json.loads(p.read_text()))
        (out / f"{p.stem}.html").write_text(html)
        print(f"{p.stem:<32} {c.stats}")


if __name__ == "__main__":
    main()
