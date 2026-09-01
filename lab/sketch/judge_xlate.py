#!/usr/bin/env python3
"""Mode-1 vs mode-2, judged against the target screen.

The skin rail proved a theme transfers; this asks the question the full
translation exists for: with CONTENT AND STRUCTURE also translated, is the
render closer to the target screen than the best skin-only card was? Blind,
order-swapped, same sample seed as the montage so the two reports describe the
same screens.

Usage: judge_xlate.py [--n 24]
"""
import json
import pathlib
import random
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "style-factory"))
import batch_styles as B  # noqa: E402

RESULTS = HERE / "xrail" / "verdicts.jsonl"


def judge(target, mode1, mode2, swap):
    first, second = (mode2, mode1) if swap else (mode1, mode2)
    out = B.claude_text(
        f"Read {target} — a screen from a commercial mobile UI kit (the TARGET). "
        f"Then Read {first} (call it A) and {second} (call it B): two attempts to "
        f"reproduce that screen in a constrained card language. Judge which is "
        f"closer to the TARGET overall — its content, its structure, its layout "
        f"AND its visual style all count. Return ONLY JSON: "
        f'{{"winner": "A"|"B"|"tie", "why": "<=18 words"}}')
    m = re.search(r"\{.*\}", out, re.S)
    v = json.loads(m.group(0))
    if v.get("winner") == "tie":
        return 0, v.get("why", "")
    mode2_first = swap
    mode2_won = (v["winner"] == "A") == mode2_first
    return (1 if mode2_won else -1), v.get("why", "")


def main():
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 24
    done = set()
    if RESULTS.exists():
        done = {json.loads(l)["screen"] for l in RESULTS.open()}
    shots = sorted(p for p in (HERE / "xrail").glob("*.png"))
    random.seed(7)   # the same screens the mode-1 judge sampled
    sample = random.sample(shots, min(n, len(shots)))
    for i, png in enumerate(sample, 1):
        if png.stem in done:
            continue
        target = HERE / "targets" / f"{png.stem}.png"
        mode1 = HERE / "rail" / f"{png.stem}.png"
        if not (target.exists() and mode1.exists()):
            continue
        swap = sum(ord(c) for c in png.stem) % 2 == 0
        try:
            v, why = judge(target, mode1, png, swap)
        except Exception as exc:  # noqa: BLE001
            print(f"[{png.stem}] ERR {str(exc)[:60]}", flush=True)
            continue
        with RESULTS.open("a") as f:
            f.write(json.dumps({"screen": png.stem, "mode2_win": v, "why": why}) + "\n")
        tag = "TRANSLATION" if v > 0 else ("SKIN-ONLY" if v < 0 else "tie")
        print(f"[{i}/{len(sample)}] {png.stem[:30]:<30} {tag}: {why[:52]}", flush=True)

    rows = [json.loads(l) for l in RESULTS.open()]
    w = sum(1 for r in rows if r["mode2_win"] > 0)
    l = sum(1 for r in rows if r["mode2_win"] < 0)
    print(f"\n{'=' * 56}\n{len(rows)} judged · translation {w} · skin-only {l} · "
          f"tie {len(rows) - w - l}")
    if w + l:
        print(f"full-translation win rate vs skin-only: {100 * w / (w + l):.0f}%")


if __name__ == "__main__":
    main()
