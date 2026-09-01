#!/usr/bin/env python3
"""Translate a spec tree into an L0 card — content and structure, not just skin.

Deterministic on purpose. An LLM translator would be judged twice (once for
reading the design, once for writing the card); this one is a fixed function of
the spec, so every fidelity number downstream measures the LANGUAGE — what L0's
role vocabulary can and cannot carry — rather than a model's mood. Same input,
same card, forever; and every drop is counted into a ledger instead of vanishing.

Mapping, tree-first: the kit's own nesting (already symbol-resolved by
sketch2spec) supplies the structure. A group whose first child is a covering
rounded fill becomes a Panel; a pill-radius rect with one centred text becomes a
Chip; children that overlap in y become a Row; text takes its role from its size
rank. Bitmaps and vector icons have no L0 constructor a card may feed (a literal
in a data position is a §4 refusal) — they are DROPPED AND COUNTED, which is the
honest translation of "this language cannot say that".

Usage: spec2card.py <specs-dir> <cards-dir> [--only substr]
"""
import json
import pathlib
import re
import sys

CHROME = re.compile(r"status|iphone|home-indicator|keyboard|bar/bottom|bar/top",
                    re.I)


def esc(s):
    # Kit strings carry real newlines; the card grammar has no escape for one,
    # and a wrapped TextTitle rewraps to its own width anyway — the break was
    # presentation, not content.
    s = " ".join(s.split())
    return s.replace("\\", "\\\\").replace('"', '\\"')


class Xlate:
    def __init__(self, spec):
        self.spec = spec
        self.W = spec["w"]
        self.led = {"texts": 0, "texts_out": 0, "bitmaps": 0, "icons": 0,
                    "chips": 0, "panels": 0, "rows": 0, "deep": 0}
        sizes = []

        def sz(n):
            t = n.get("text")
            if t and t.get("run", {}).get("size") and (t.get("string") or "").strip():
                sizes.append(t["run"]["size"])
            for c in n.get("children", []):
                sz(c)
        sz(spec)
        sizes.sort(reverse=True)
        self.hero_floor = sizes[0] * 0.85 if sizes else 99
        self.title_floor = 30  # @2x

    # ---- classification ---------------------------------------------------
    def text_role(self, n):
        t = n["text"]
        s = (t.get("string") or "").strip()
        run = t.get("run") or {}
        size = run.get("size") or 20
        caps = s.isupper() and 2 < len(s) < 28 and size <= 26
        if size >= self.hero_floor and size >= 40 and len(s) <= 14:
            return "TextHero"
        if caps:
            return "TextEyebrow"
        if size >= self.title_floor:
            return "TextTitle"
        if size >= 24:
            return "TextBody"
        return "TextCaption"

    def covering_fill(self, n, kids):
        """The child that is this group's own background."""
        for k in kids[:2]:
            if k.get("cls") in ("rectangle", "oval") and not k.get("text"):
                if (k["w"] * k["h"] >= 0.72 * max(1, n["w"] * n["h"])
                        and (k.get("fill") or k.get("gradient"))):
                    return k
        return None

    def is_chip(self, n, kids):
        bg = self.covering_fill(n, kids)
        if not bg or not bg.get("radius"):
            return None
        if bg["radius"] < 0.32 * bg["h"] or n["h"] > 130:
            return None
        texts = [k for k in kids if k.get("text")
                 and (k["text"].get("string") or "").strip()]
        rest = [k for k in kids if k is not bg and not k.get("text")
                and min(k["w"], k["h"]) > 30]
        if len(texts) == 1 and not rest:
            return texts[0]
        return None

    # ---- structure --------------------------------------------------------
    def lines(self, kids):
        """Group siblings into visual lines by vertical overlap."""
        ks = sorted(kids, key=lambda k: (k["y"], k["x"]))
        out = []
        for k in ks:
            placed = False
            for line in out:
                ref = line[0]
                if (k["y"] < ref["y"] + ref["h"] * 0.6
                        and ref["y"] < k["y"] + k["h"] * 0.6):
                    line.append(k)
                    placed = True
                    break
            if not placed:
                out.append([k])
        for line in out:
            line.sort(key=lambda k: k["x"])
        return out

    def emit(self, n, out, depth):
        if depth > 10:
            self.led["deep"] += 1
            return
        pad = "  " * depth
        cls = n.get("cls")
        name = (n.get("name") or "")
        if CHROME.search(name):
            return
        if n.get("text") is not None:
            s = (n["text"].get("string") or "").strip()
            self.led["texts"] += 1
            if not s or len(s) > 220:
                return
            # The emitted string is the SPEC's demo content, verbatim — that is
            # what makes text recall a measurable number afterwards.
            role = self.text_role(n)
            self.led["texts_out"] += 1
            width = ", width: .fill" if n["w"] > 0.5 * self.W and role in (
                "TextTitle", "TextBody", "TextCaption") else ""
            out.append(f'{pad}{role}(text: "{esc(s)}"{width})')
            return
        if cls == "bitmap":
            self.led["bitmaps"] += 1
            return
        if cls in ("shapePath", "shapeGroup", "triangle", "polygon", "oval"):
            if max(n["w"], n["h"]) <= 64:
                self.led["icons"] += 1
                return
            return
        kids = n.get("children") or []
        if cls == "rectangle" or not kids:
            return

        chip_text = self.is_chip(n, kids)
        if chip_text is not None:
            s = (chip_text["text"].get("string") or "").strip()
            if s:
                self.led["chips"] += 1
                self.led["texts"] += 1
                self.led["texts_out"] += 1
                out.append(f'{pad}Chip(text: "{esc(s)}")')
                return

        bg = self.covering_fill(n, kids)
        inner = [k for k in kids if k is not bg]
        opener = None
        if bg is not None and bg.get("radius") and n["w"] > 0.35 * self.W \
                and n["h"] > 60:
            self.led["panels"] += 1
            opener = f"{pad}Panel {{"
        body = []
        for line in self.lines(inner):
            if 1 < len(line) <= 5:
                # Wrap in a Row only if MORE THAN ONE member survives
                # translation — kit lines are full of icon pairs that drop to
                # nothing, and an empty Row is noise, not structure.
                probe = []
                for k in line:
                    self.emit(k, probe, depth + 2)
                tops = sum(1 for b in probe if b.strip() and not b.startswith((" " * (2 * depth + 6))))
                if sum(1 for b in probe if b.strip()) == 0:
                    continue
                if tops > 1:
                    self.led["rows"] += 1
                    body.append(f'{pad}  Row(gap: 8, align: .center) {{')
                    body.extend(probe)
                    body.append(f"{pad}  }}")
                else:
                    body.extend(b[2:] if b.startswith("  ") else b for b in probe)
            else:
                for k in line:
                    self.emit(k, body, depth + (1 if opener else 0))
        if opener and any("Text" in b or "Chip" in b for b in body):
            out.append(opener)
            out.extend(body)
            out.append(f"{pad}}}")
        else:
            out.extend(b[2:] if opener and b.startswith(pad + "  ") else b
                       for b in body)

    def card(self):
        out = []
        for line in self.lines(self.spec.get("children") or []):
            for k in line:
                self.emit(k, out, 1)
        # Strip runs of identical consecutive lines (kit screens repeat demo
        # rows verbatim; three identical captions in a row read as a defect).
        dedup, prev = [], None
        for l in out:
            if l != prev or l.strip().endswith(("{", "}")):
                dedup.append(l)
            prev = l
        # Row wrappers that ended up with a single child collapse away.
        src = "\n".join(dedup[:170])
        head = (f"# level: L0\n# model: atro-translation\n"
                f"# source-artboard: {self.spec.get('name', '?')}\n\n"
                "theme dark\n\n"
                "view root Surface(pad: .page) {\n")
        return head + src + "\n}\n"


def main():
    specs = pathlib.Path(sys.argv[1])
    cards = pathlib.Path(sys.argv[2])
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else ""
    cards.mkdir(parents=True, exist_ok=True)
    ledger = (cards / "_ledger.jsonl").open("w")
    n = 0
    for p in sorted(specs.glob("*.json")):
        if only and only not in p.stem:
            continue
        x = Xlate(json.loads(p.read_text()))
        (cards / f"{p.stem}.card").write_text(x.card())
        ledger.write(json.dumps({"screen": p.stem, **x.led}) + "\n")
        n += 1
    ledger.close()
    print(f"{n} cards -> {cards}")


if __name__ == "__main__":
    main()
