#!/usr/bin/env python3
"""Run the loop many times, and report a rate rather than an anecdote.

It closed once. That is not the same as working — the whole session's lesson is
that a single observation supports almost nothing, and 0 failures in 1 attempt
bounds the failure rate at 95%.

Twenty runs: five subjects across four source mockups, so neither the domain nor
the design direction is held constant. What comes out is a convergence rate, a
round count, and — more useful than either — a tally of what actually goes wrong.

Usage:  e2e_batch.py [--runs N] [--rounds N] [--model opus|glm]
"""
import collections
import json
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import e2e  # noqa: E402

OUT = HERE / "e2e_batch"

# Deliberately varied: a hero-and-list, a dense feed, a single big number, a
# route, a grid. If the loop only handles one shape, the rate should say so.
SUBJECTS = [
    ("weather", "a weather card for Florence, Italy — the current temperature "
                "prominently, the condition, and a short forecast list."),
    ("news", "a news card — one lead story with a headline and standfirst, then "
             "four more headlines beneath it."),
    ("stock", "a stock card for one ticker — the price as the hero, the day's "
              "change, and a few key figures as a small grid."),
    ("transit", "a transit card — the next departure as the hero, then the "
                "following three departures as rows."),
    ("activity", "a things-to-do card for a city — three suggestions, each with "
                 "a name and a short line of detail."),
]

# The four highest-ranked mockups from the blind comparison, so the design
# direction varies without dragging in the ones that lost every pair.
MOCKUPS = ["ref_mockup", "r012-weather-art_deco",
           "r004-weather-punk_zine", "r021-weather-swiss"]


def main():
    runs = int(sys.argv[sys.argv.index("--runs") + 1]) if "--runs" in sys.argv else 20
    rounds = int(sys.argv[sys.argv.index("--rounds") + 1]) if "--rounds" in sys.argv else 4
    model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "opus"
    ask = e2e.ask_opus if model == "opus" else e2e.ask_glm
    OUT.mkdir(exist_ok=True)

    plan = [(SUBJECTS[i % len(SUBJECTS)], MOCKUPS[(i // len(SUBJECTS)) % len(MOCKUPS)])
            for i in range(runs)]
    results, t0 = [], time.time()
    store = OUT / "results.json"
    if store.exists():
        results = json.loads(store.read_text())

    for i, ((name, subject), mockup) in enumerate(plan, 1):
        if i <= len(results):
            continue
        print(f"[{i}/{runs}] {name} × {mockup}", flush=True)
        try:
            r = e2e.run_once(subject, mockup, rounds, ask,
                             OUT / f"{i:02d}-{name}-{mockup[:12]}")
        except Exception as exc:
            r = {"subject": name, "mockup": mockup, "outcome": "error",
                 "trail": [str(exc)[:120]]}
            print(f"    error: {str(exc)[:80]}", flush=True)
        r["name"] = name
        results.append(r)
        store.write_text(json.dumps(results, indent=1))
        el = time.time() - t0
        print(f"    -> {r['outcome']}   [{el/60:.0f}m elapsed, "
              f"~{el/i*(runs-i)/60:.0f}m left]\n", flush=True)

    conv = [r for r in results if r["outcome"] == "converged"]
    print("=" * 64)
    print(f"{len(results)} runs · {len(conv)} converged "
          f"({100*len(conv)/max(1,len(results)):.0f}%)")
    if conv:
        rs = sorted(r["rounds"] for r in conv)
        print(f"rounds to clean: min {rs[0]} median {rs[len(rs)//2]} max {rs[-1]}")
        up = [r.get("upstream", 0) for r in conv]
        print(f"palette-owned failures left standing: {sum(up)} across {len(conv)} cards")
    print("\nby subject:")
    for n in {r["name"] for r in results}:
        rows = [r for r in results if r["name"] == n]
        ok = sum(1 for r in rows if r["outcome"] == "converged")
        print(f"  {n:<10} {ok}/{len(rows)}")
    print("\nwhat went wrong:")
    why = collections.Counter()
    for r in results:
        for line in r.get("trail", []):
            if "invalid:" in line:
                why["did not validate"] += 1
            elif "failing:" in line:
                for g in line.split("failing: ")[-1].split(","):
                    why[f"gate {g.strip()}"] += 1
    for k, v in why.most_common():
        print(f"  {v:4}  {k}")
    print(f"\n-> {store}")


if __name__ == "__main__":
    main()
