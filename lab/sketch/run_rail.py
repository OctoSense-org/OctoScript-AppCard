#!/usr/bin/env python3
"""Mode-1 rail: one functional card, 150 kit skins, a wire gate per screen.

The claim under test is the reframed pipeline's: the FUNCTION is fixed (a plain
weather card), and the theme carries all the taste. Each Atro screen's projected
palette is spliced through the override slot and rendered; the gate then reads
the emitted DSL and verifies the theme actually LANDED — ground on the page, ink
on the text, the kit's face on the runs. That check is exact and free, which is
what makes running all 150 tractable; the paired judge only ever sees a sample.

Sequential on purpose: the capture harness photographs by PID now, but two
octos-app windows still fight for the same screen space and dock focus.

Usage: run_rail.py [--limit N] [--only substr]
"""
import json
import os
import pathlib
import re
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
GATES = HERE.parent / "gates"
sys.path.insert(0, str(GATES))
os.environ["GATE_WINDOW"] = "375x812"
import shoot  # noqa: E402

shoot.SIZE = "375x812"
CARD = GATES / "e2e_batch" / "01-weather-ref_mockup" / "card.card"
DATA = GATES / "e2e_batch" / "01-weather-ref_mockup" / "data.json"
OUT = HERE / "rail"
RESULTS = OUT / "results.jsonl"

ARGB = re.compile(r"let\s+(l0_base|l0_text|l0_accent)\s*=\s*argb\(\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+)\s*\)")


def theme_colors(theme_path):
    out = {}
    for m in ARGB.finditer(theme_path.read_text()):
        _, r, g, b = (int(x) for x in m.groups()[1:])
        out[m.group(1)] = f"#{r:02x}{g:02x}{b:02x}"
    return out


def main():
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 10 ** 9
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else ""
    OUT.mkdir(exist_ok=True)
    done = set()
    if RESULTS.exists():
        done = {json.loads(l)["screen"] for l in RESULTS.open()}
    themes = sorted((HERE / "out" / "themes").glob("*.splash"))
    todo = [t for t in themes if only in t.stem and t.stem not in done][:limit]
    print(f"{len(todo)} screens to render (of {len(themes)})", flush=True)
    t0 = time.time()
    for i, theme in enumerate(todo, 1):
        png = OUT / f"{theme.stem}.png"
        dsl = OUT / f"{theme.stem}.dsl.txt"
        os.environ["MAKEPAD_DUMP_DSL"] = str(dsl)
        ok = shoot.shoot(CARD, png, theme, data=DATA)
        want = theme_colors(theme)
        got = dsl.read_text().lower() if dsl.exists() else ""
        gate = {
            "render": bool(ok),
            "ground": want.get("l0_base", "?")[1:] in got,
            "ink": want.get("l0_text", "?")[1:] in got,
            "face": "montserrat" in got,
        }
        gate["pass"] = all(gate.values())
        with RESULTS.open("a") as f:
            f.write(json.dumps({"screen": theme.stem, **gate, **want}) + "\n")
        el = time.time() - t0
        print(f"[{i}/{len(todo)}] {theme.stem[:34]:<34} "
              f"{'PASS' if gate['pass'] else 'FAIL ' + str([k for k, v in gate.items() if not v])}"
              f"   [{el / 60:.0f}m, ~{el / i * (len(todo) - i) / 60:.0f}m left]", flush=True)
        dsl.unlink(missing_ok=True)

    rows = [json.loads(l) for l in RESULTS.open()]
    ok = sum(1 for r in rows if r["pass"])
    print(f"\n{'=' * 56}\nwire gate: {ok}/{len(rows)} screens carry their theme "
          f"(ground+ink+face verified in the emitted DSL)")
    for k in ("render", "ground", "ink", "face"):
        bad = sum(1 for r in rows if not r[k])
        if bad:
            print(f"  failing {k}: {bad}")


if __name__ == "__main__":
    main()
