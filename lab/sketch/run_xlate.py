#!/usr/bin/env python3
"""Mode-2 rail: every translated card, rendered under its own screen's theme.

Two deterministic numbers fall out per screen before any judge is paid:

  text recall     what fraction of the spec's visible strings made it into the
                  emitted DSL. The translator counts what it dropped; this
                  verifies what it kept actually reached the renderer.

  theme carry     same wire gate as mode-1 (ground + ink + face in the DSL).

Usage: run_xlate.py [--limit N] [--only substr]
"""
import json
import os
import pathlib
import re
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "gates"))
os.environ["GATE_WINDOW"] = "375x812"
import shoot  # noqa: E402

shoot.SIZE = "375x812"
OUT = HERE / "xrail"
RESULTS = OUT / "results.jsonl"
DATA = OUT / "data.json"


def spec_strings(spec):
    out = []

    def walk(n):
        t = n.get("text")
        if t and (t.get("string") or "").strip():
            s = " ".join(t["string"].split())
            if len(s) <= 220:
                out.append(s)
        for c in n.get("children", []):
            walk(c)
    walk(spec)
    return out


def main():
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 10 ** 9
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else ""
    OUT.mkdir(exist_ok=True)
    DATA.write_text(json.dumps({"env": {"locale": {}}}))
    done = set()
    if RESULTS.exists():
        done = {json.loads(l)["screen"] for l in RESULTS.open()}
    cards = [c for c in sorted((HERE / "cards").glob("*.card"))
             if only in c.stem and c.stem not in done][:limit]
    print(f"{len(cards)} translations to render", flush=True)
    t0 = time.time()
    for i, card in enumerate(cards, 1):
        theme = HERE / "out" / "themes" / f"{card.stem}.splash"
        spec = json.loads((HERE / "specs" / f"{card.stem}.json").read_text())
        png = OUT / f"{card.stem}.png"
        dsl = OUT / f"{card.stem}.dsl.txt"
        os.environ["MAKEPAD_DUMP_DSL"] = str(dsl)
        ok = shoot.shoot(card, png, theme if theme.exists() else None, data=DATA)
        got = dsl.read_text() if dsl.exists() else ""
        strings = spec_strings(spec)
        hit = sum(1 for s in strings if s[:40] in got)
        recall = hit / max(1, len(strings))
        with RESULTS.open("a") as f:
            f.write(json.dumps({"screen": card.stem, "render": bool(ok),
                                "strings": len(strings), "hit": hit,
                                "recall": round(recall, 3),
                                "face": "Montserrat" in got}) + "\n")
        el = time.time() - t0
        print(f"[{i}/{len(cards)}] {card.stem[:32]:<32} recall {recall:4.0%} "
              f"({hit}/{len(strings)})  [{el/60:.0f}m, ~{el/i*(len(cards)-i)/60:.0f}m left]",
              flush=True)
        dsl.unlink(missing_ok=True)

    rows = [json.loads(l) for l in RESULTS.open()]
    import statistics
    rec = [r["recall"] for r in rows]
    print(f"\n{'=' * 56}\n{len(rows)} rendered · text recall median "
          f"{statistics.median(rec):.0%} · mean {statistics.mean(rec):.0%} · "
          f"min {min(rec):.0%}")
    print(f"renders ok: {sum(1 for r in rows if r['render'])}/{len(rows)} · "
          f"face carried: {sum(1 for r in rows if r['face'])}/{len(rows)}")


if __name__ == "__main__":
    main()
