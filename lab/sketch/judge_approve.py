#!/usr/bin/env python3
"""Absolute approval: is each translation a faithful rendering of ITS screen?

The paired judge only ever says which of two candidates is closer; an approval
gate has to stand alone. Absolute scores drift, so the verdict is anchored on a
binary — "is this recognizably the SAME screen?" — with the score and the top
missing element as diagnostics, not the decision.
"""
import json, pathlib, random, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "style-factory"))
import batch_styles as B

RES = HERE / "xrail" / "approval.jsonl"
n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 24
done = {json.loads(l)["screen"] for l in RES.open()} if RES.exists() else set()
shots = sorted(p for p in (HERE / "xrail").glob("*.png"))
random.seed(7)
for i, png in enumerate(random.sample(shots, min(n, len(shots))), 1):
    if png.stem in done: continue
    target = HERE / "targets" / f"{png.stem}.png"
    if not target.exists(): continue
    out = B.claude_text(
        f"Read {target} — a mobile UI kit screen (TARGET). Read {png} — a "
        f"translation of that screen into a deliberately constrained card "
        f"language (no icons, no photos, flow layout only). Judge the "
        f"translation ON ITS OWN: is it recognizably the SAME screen — same "
        f"purpose, same content, same reading order — such that a user of the "
        f"target app would know where they are? Return ONLY JSON: "
        f'{{"same_screen": true|false, "fidelity": 1-10, "missing": "<=12 words"}}')
    m = re.search(r"\{.*\}", out, re.S)
    v = json.loads(m.group(0))
    with RES.open("a") as f:
        f.write(json.dumps({"screen": png.stem, **v}) + "\n")
    print(f"[{i}] {png.stem[:30]:<30} {'SAME' if v.get('same_screen') else 'NO  '} "
          f"{v.get('fidelity')}/10  missing: {str(v.get('missing'))[:44]}", flush=True)

rows = [json.loads(l) for l in RES.open()]
import statistics
ok = sum(1 for r in rows if r.get("same_screen"))
fid = [r["fidelity"] for r in rows if isinstance(r.get("fidelity"), (int, float))]
print(f"\n{'='*56}\napproved as same-screen: {ok}/{len(rows)} "
      f"({100*ok/len(rows):.0f}%) · fidelity median {statistics.median(fid)} mean {statistics.mean(fid):.1f}")
import collections
words = collections.Counter()
for r in rows:
    for w in str(r.get("missing","")).lower().replace(",", " ").split():
        if len(w) > 3: words[w] += 1
print("most-named missing:", dict(words.most_common(6)))
