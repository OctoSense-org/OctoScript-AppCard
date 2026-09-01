#!/usr/bin/env python3
"""The comparison score: blind paired judging of the skin transfer.

Per sampled screen the judge sees the TARGET (the kit screen, spec-rendered)
and two card renders — the plain functional card and the themed one — order
swapped per specimen, and picks which carries the target's STYLE. Content and
layout differ by construction (a weather card is not a chat screen), so the
prompt scopes the question to the style system: palette, type feel, shape
language, surface treatment.

Win-rate is the score. The wire gate already proved the theme *landed*; this
asks whether landing it actually reads as the kit's look.

Usage: judge_rail.py [--n 20]
"""
import json
import pathlib
import random
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "style-factory"))
import batch_styles as B  # noqa: E402

OUT = HERE / "rail"
RESULTS = OUT / "verdicts.jsonl"


def judge(target, base, themed, swap):
    first, second = (themed, base) if swap else (base, themed)
    out = B.claude_text(
        f"Read {target} — a screen from a commercial mobile UI kit (the TARGET "
        f"style). Then Read {first} (call it A) and {second} (call it B): two "
        f"renders of the SAME simple weather card. The card's layout and content "
        f"are fixed and are NOT the question — judge ONLY which render adopts "
        f"the target's STYLE SYSTEM: its palette (ground, ink, accent), its type "
        f"feel, its corner language, its surface treatment. Return ONLY JSON: "
        f'{{"winner": "A"|"B"|"tie", "why": "<=18 words"}}')
    m = re.search(r"\{.*\}", out, re.S)
    v = json.loads(m.group(0))
    if v.get("winner") == "tie":
        return 0, v.get("why", "")
    themed_first = swap
    themed_won = (v["winner"] == "A") == themed_first
    return (1 if themed_won else -1), v.get("why", "")


def main():
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 20
    base = OUT / "baseline.png"
    assert base.exists(), "render the baseline first (run_rail renders it last)"
    done = set()
    if RESULTS.exists():
        done = {json.loads(l)["screen"] for l in RESULTS.open()}
    shots = sorted(p for p in OUT.glob("*.png") if p.stem != "baseline")
    random.seed(7)
    sample = random.sample(shots, min(n, len(shots)))
    for i, png in enumerate(sample, 1):
        if png.stem in done:
            continue
        target = HERE / "targets" / f"{png.stem}.png"
        if not target.exists():
            continue
        swap = sum(ord(c) for c in png.stem) % 2 == 0
        try:
            v, why = judge(target, base, png, swap)
        except Exception as exc:  # noqa: BLE001
            print(f"[{png.stem}] ERR {str(exc)[:60]}", flush=True)
            continue
        with RESULTS.open("a") as f:
            f.write(json.dumps({"screen": png.stem, "themed_win": v, "why": why}) + "\n")
        tag = "THEMED" if v > 0 else ("BASELINE" if v < 0 else "tie")
        print(f"[{i}/{len(sample)}] {png.stem[:32]:<32} {tag}: {why[:52]}", flush=True)

    rows = [json.loads(l) for l in RESULTS.open()]
    w = sum(1 for r in rows if r["themed_win"] > 0)
    l = sum(1 for r in rows if r["themed_win"] < 0)
    t = len(rows) - w - l
    print(f"\n{'=' * 56}\n{len(rows)} judged · themed {w} · baseline {l} · tie {t}")
    if w + l:
        print(f"skin-transfer win rate: {100 * w / (w + l):.0f}%")


if __name__ == "__main__":
    main()
