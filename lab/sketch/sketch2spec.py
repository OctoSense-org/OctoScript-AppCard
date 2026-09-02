#!/usr/bin/env python3
"""Sketch file -> per-artboard spec JSON. The ground-truth half of the rail.

A .sketch is a ZIP of JSON, so this is a *reader*, not an inferrer — the whole
reason design files beat image mockups as ground truth. The one real job here is
SYMBOL RESOLUTION: kit screens are ~60% `symbolInstance` nodes (Atro: 3,272
instances over 241 masters), so an unresolved tree is mostly holes. Masters are
inlined at each use, instance-frame scaled, with text overrides applied — the
three mechanisms that carry virtually all per-use variation in real kits.

Approximations, all logged rather than silent:
  - instance resize uses naive proportional scaling, not Sketch's pin/resize
    constraints (kits mostly place instances at native size; `scaled` counts
    the exceptions)
  - masks clip to the mask's rect, not its path
  - rotation/flips are recorded on the node and not applied

Output: specs/<artboard>.json — a nested tree of
  {cls,name,x,y,w,h,fill,gradient,radius,stroke,shadow,text,image,children}
with absolute artboard coordinates, plus tokens.json for the document styles.

Usage: sketch2spec.py <unzipped-sketch-dir> <out-dir> [--pages "UI Part"]
"""
import json
import pathlib
import re
import sys

def hexa(c):
    if not c:
        return None
    return {"hex": "#%02x%02x%02x" % (round(c["red"] * 255), round(c["green"] * 255),
                                      round(c["blue"] * 255)),
            "a": round(c.get("alpha", 1), 3)}


def pt(s):
    m = re.findall(r"[-\d.]+", s or "")
    return (float(m[0]), float(m[1])) if len(m) >= 2 else (0.0, 0.0)


class Extractor:
    def __init__(self, src):
        self.src = pathlib.Path(src)
        self.doc = json.loads((self.src / "document.json").read_text())
        meta = json.loads((self.src / "meta.json").read_text())
        self.pages = {}
        for pid, p in meta["pagesAndArtboards"].items():
            self.pages[p["name"]] = json.loads(
                (self.src / "pages" / f"{pid}.json").read_text())
        # Masters may live on any page; index them all.
        self.masters = {}
        for page in self.pages.values():
            for ab in page.get("layers", []):
                if ab.get("_class") == "symbolMaster":
                    self.masters[ab["symbolID"]] = ab
        # ...and in LIBRARIES. A kit's icons and illustrations usually come from
        # separate library files, and Sketch embeds those masters in the
        # document as `foreignSymbols` — 271 of them here, which is where 30%
        # of instances resolved to nothing before this.
        for f in self.doc.get("foreignSymbols", []):
            sm = f.get("symbolMaster")
            if sm and sm.get("symbolID"):
                self.masters.setdefault(sm["symbolID"], sm)
        self.shared = {}
        for kind in ("layerStyles", "layerTextStyles"):
            for s in self.doc.get(kind, {}).get("objects", []):
                self.shared[s["do_objectID"]] = s["value"]
        self.stats = {"instances": 0, "unresolved": 0, "scaled": 0,
                      "text_overrides": 0, "symbol_swaps": 0, "masked": 0,
                      "rotated": 0}

    # ---- style ------------------------------------------------------------
    def style_of(self, layer):
        st = layer.get("style") or {}
        sid = st.get("do_objectID")
        # A shared-style reference with no local fills takes the shared one.
        ref = layer.get("sharedStyleID")
        if ref and ref in self.shared and not st.get("fills"):
            st = self.shared[ref]
        out = {}
        fills = [f for f in (st.get("fills") or []) if f.get("isEnabled")]
        for f in fills:
            if f.get("fillType") == 1 and f.get("gradient", {}).get("stops"):
                g = f["gradient"]
                out["gradient"] = {
                    "type": g.get("gradientType", 0),
                    "from": pt(g.get("from")), "to": pt(g.get("to")),
                    "stops": [{"c": hexa(s["color"]), "p": round(s.get("position", 0), 3)}
                              for s in g["stops"]]}
            elif f.get("fillType") == 4 and (f.get("image") or {}).get("_ref"):
                # An IMAGE FILL on a shape — how photo-heavy kits place their
                # pictures (Atro used bitmap layers; CaMo fills rectangles).
                out["imagefill"] = f["image"]["_ref"]
            elif f.get("color") and f["color"].get("alpha", 1) > 0.02:
                out["fill"] = hexa(f["color"])
        borders = [b for b in (st.get("borders") or []) if b.get("isEnabled")]
        if borders:
            b = borders[0]
            out["stroke"] = {"c": hexa(b.get("color")), "w": b.get("thickness", 1)}
        shadows = [s for s in (st.get("shadows") or []) if s.get("isEnabled")]
        if shadows:
            s = shadows[0]
            out["shadow"] = {"c": hexa(s.get("color")), "blur": s.get("blurRadius", 0),
                             "dx": s.get("offsetX", 0), "dy": s.get("offsetY", 0)}
        op = (st.get("contextSettings") or {}).get("opacity", 1)
        if op < 0.999:
            out["opacity"] = round(op, 3)
        return out

    def text_of(self, layer, overrides, path):
        # An override replaces the WHOLE string; attributes stay the master's.
        astr = layer.get("attributedString", {})
        s = astr.get("string", "")
        for key in ("/".join(path + [layer["do_objectID"]]) + "_stringValue",
                    layer["do_objectID"] + "_stringValue"):
            if key in overrides:
                s = overrides[key]
                self.stats["text_overrides"] += 1
                break
        runs = []
        for a in astr.get("attributes", [])[:1]:
            at = a.get("attributes", {})
            fo = at.get("MSAttributedStringFontAttribute", {}).get("attributes", {})
            runs.append({"font": fo.get("name"), "size": fo.get("size"),
                         "c": hexa(at.get("MSAttributedStringColorAttribute")),
                         "align": (at.get("paragraphStyle") or {}).get("alignment", 0)})
        return {"string": s, "run": runs[0] if runs else {}}

    # ---- tree -------------------------------------------------------------
    def node(self, layer, ox, oy, sx, sy, overrides, path):
        f = layer.get("frame", {})
        x, y = ox + f.get("x", 0) * sx, oy + f.get("y", 0) * sy
        w, h = f.get("width", 0) * sx, f.get("height", 0) * sy
        cls = layer.get("_class")
        if not layer.get("isVisible", True):
            return None
        n = {"cls": cls, "name": layer.get("name", ""),
             "x": round(x, 1), "y": round(y, 1), "w": round(w, 1), "h": round(h, 1)}
        n.update(self.style_of(layer))
        if layer.get("rotation"):
            n["rot"] = layer["rotation"]
            self.stats["rotated"] += 1
        r = layer.get("fixedRadius") or 0
        pts = layer.get("points") or []
        prs = [p.get("cornerRadius", 0) for p in pts]
        if prs and max(prs) > r:
            r = max(prs)
        if r:
            n["radius"] = round(r * min(sx, sy), 1)
        if layer.get("hasClippingMask"):
            n["mask"] = True
            self.stats["masked"] += 1
        if cls == "text":
            n["text"] = self.text_of(layer, overrides, path)
        if cls in ("shapePath", "shapeGroup", "triangle", "polygon"):
            # The actual beziers, kept — the difference between an icon and a
            # silhouette box downstream. Stored as flattened normalized rings
            # (cheap, backend-neutral) plus the SVG `d` for the CSS control.
            import paths as _paths
            raw, _ = _paths.collect_rings(layer)
            if raw:
                flat = [(_paths.ring_points(pts, closed), op)
                        for pts, closed, op in raw]
                flat = [(r, op) for r, op in flat if len(r) >= 3]
                if flat:
                    n["rings"] = [[(round(x, 4), round(y, 4)) for x, y in r]
                                  for r, _ in flat]
                    n["ring_ops"] = [op for _, op in flat]
                    n["svg_d"] = _paths.svg_d(raw)
                    # evenodd only when a subtract ring exists; nonzero keeps
                    # union overlaps solid in the CSS control.
                    n["svg_rule"] = ("evenodd" if any(op == 1 for _, op in flat)
                                     else "nonzero")
        if cls == "bitmap":
            n["image"] = (layer.get("image") or {}).get("_ref")
        elif n.get("imagefill"):
            n["image"] = n.pop("imagefill")
            n["cls"] = "bitmap"
        if cls == "symbolInstance":
            self.stats["instances"] += 1
            sid = layer.get("symbolID")
            for key in ("/".join(path + [layer["do_objectID"]]) + "_symbolID",
                        layer["do_objectID"] + "_symbolID"):
                if key in overrides:
                    sid = overrides[key]
                    self.stats["symbol_swaps"] += 1
                    break
            # An override swap to "" is Sketch's "remove this symbol" — a real
            # design decision (hide the badge, drop the icon), not a failure.
            if not sid:
                self.stats["swap_hidden"] = self.stats.get("swap_hidden", 0) + 1
                return None
            master = self.masters.get(sid)
            if master is None:
                self.stats["unresolved"] += 1
                return n
            mf = master.get("frame", {})
            msx = w / mf["width"] if mf.get("width") else 1
            msy = h / mf["height"] if mf.get("height") else 1
            if abs(msx - 1) > 0.01 or abs(msy - 1) > 0.01:
                self.stats["scaled"] += 1
            # Merge override maps: the instance's own, prefixed under its id.
            sub = dict(overrides)
            for ov in layer.get("overrideValues", []):
                sub[ov.get("overrideName", "")] = ov.get("value")
            kids = [self.node(ch, x, y, msx, msy, sub, path + [layer["do_objectID"]])
                    for ch in master.get("layers", [])]
            # The master's own background, when it draws one.
            if master.get("hasBackgroundColor") and master.get("includeBackgroundColorInInstance"):
                n["fill"] = hexa(master.get("backgroundColor"))
            n["children"] = [k for k in kids if k]
            return n
        kids = [self.node(ch, x, y, sx, sy, overrides, path)
                for ch in layer.get("layers", [])]
        kids = [k for k in kids if k]
        if kids:
            n["children"] = kids
        return n

    def artboards(self, page_filter):
        for pname, page in self.pages.items():
            if page_filter and page_filter not in pname:
                continue
            for ab in page.get("layers", []):
                if ab.get("_class") != "artboard":
                    continue
                f = ab.get("frame", {})
                root = {"cls": "artboard", "name": ab.get("name", ""),
                        "x": 0, "y": 0, "w": f.get("width"), "h": f.get("height"),
                        "page": pname,
                        "fill": hexa(ab.get("backgroundColor"))
                        if ab.get("hasBackgroundColor") else None}
                kids = [self.node(ch, 0, 0, 1, 1, {}, [])
                        for ch in ab.get("layers", [])]
                root["children"] = [k for k in kids if k]
                yield root


def main():
    src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    pf = sys.argv[sys.argv.index("--pages") + 1] if "--pages" in sys.argv else ""
    out.mkdir(parents=True, exist_ok=True)
    ex = Extractor(src)
    count = 0
    seen = {}
    for ab in ex.artboards(pf):
        safe = re.sub(r"[^\w\-]+", "_", ab["name"]).strip("_")[:60]
        # Kits that ship Light and Dark page sets repeat artboard names; a
        # silent overwrite kept whichever mode came last. Number the repeats.
        seen[safe] = seen.get(safe, 0) + 1
        if seen[safe] > 1:
            safe = f"{safe}_{seen[safe]}"
        (out / f"{safe}.json").write_text(json.dumps(ab))
        count += 1
    print(f"{count} artboards -> {out}")
    print("stats:", ex.stats)


if __name__ == "__main__":
    main()
