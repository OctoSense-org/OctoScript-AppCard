#!/usr/bin/env python3
"""Strict design-match over one rail's captures, resumable per screen.

Usage: judge_shots.py --kit atro --rail desktop|android|ohos [--redo name]
"""
import collections
import json
import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "style-factory"))
import batch_styles as B  # noqa: E402
import kitconf  # noqa: E402

PROMPT = (
    "Read {t} (the DESIGN) and {x} (an IMPLEMENTATION screenshot). You are a "
    "strict design reviewer. Judge whether the implementation reproduces the "
    "design's VISUAL DESIGN: layout geometry, element scale and position, "
    "button/control styling, imagery, spacing rhythm. Content matching is NOT "
    "sufficient. Return ONLY JSON: "
    '{{"design_match": 1-10, "verdict": "accept"|"rework"|"reject", '
    '"worst": "<=12 words"}}')


def main():
    kit = kitconf.load(sys.argv[sys.argv.index("--kit") + 1]
                       if "--kit" in sys.argv else "atro")
    rail = sys.argv[sys.argv.index("--rail") + 1] if "--rail" in sys.argv else "desktop"
    shots = kit[f"{rail}_dir"]
    res = HERE / kit["verdicts"][rail]
    res.parent.mkdir(exist_ok=True)
    rows = [json.loads(l) for l in res.open()] if res.exists() else []
    if "--redo" in sys.argv:
        redo = sys.argv[sys.argv.index("--redo") + 1]
        rows = [r for r in rows if redo not in r["screen"]]
    done = {r["screen"] for r in rows}
    dec = json.JSONDecoder()
    for name in kit["screens"]:
        if name in done:
            continue
        t = (kit["targets_dir"] / f"{name}.png").resolve()
        x = (shots / f"{name}.png").resolve()
        if not x.exists():
            print(f"{name}: no capture, skipped", flush=True)
            continue
        out = B.claude_text(PROMPT.format(t=t, x=x))
        v = dec.raw_decode(out[out.index("{"):])[0]
        rows.append({"screen": name, **v})
        print(f"{name:<28} {v['design_match']:>2}/10 {v['verdict']:<7} "
              f"{str(v['worst'])[:46]}", flush=True)
    res.write_text("".join(json.dumps(r) + "\n" for r in rows))
    if rows:
        print(f"\n{rail}: median "
              f"{statistics.median(r['design_match'] for r in rows)} · "
              f"{dict(collections.Counter(r['verdict'] for r in rows))}")


if __name__ == "__main__":
    main()
