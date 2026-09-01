#!/usr/bin/env python3
"""The STRICT question: same DESIGN, not same screen.

No forgiveness clause. The judge is told nothing about constraints — it judges
as a designer reviewing whether the right image is a faithful implementation of
the left's visual design: geometry, scale, controls, imagery, rhythm.
"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "style-factory"))
import batch_styles as B

NAMES = ["Stats_Cards","Settings_Choose_Country","Shop_View_12","Social_Feed_1",
         "Social_Contacts_2","Shop_View_18","Email_Mail_View_1","Chat_Doodle_Pad",
         "Alerts_View_2","Navigation_View_9","Onboarding_View_2","Calendar_View_3",
         "Profile_View_6","Calendar_View_4","Photo_Gallery_Selection"]
res = HERE / "xrail" / ("strict2.jsonl" if "--v2" in sys.argv else "strict.jsonl")
xdir = HERE / ("xrail2" if "--v2" in sys.argv else "xrail")
done = {json.loads(l)["screen"] for l in res.open()} if res.exists() else set()
for name in NAMES:
    if name in done: continue
    t = HERE/"targets"/f"{name}.png"; x = xdir/f"{name}.png"
    if not (t.exists() and x.exists()): continue
    out = B.claude_text(
        f"Read {t} (the DESIGN) and {x} (an IMPLEMENTATION). You are a strict "
        f"design reviewer. Judge whether the implementation reproduces the "
        f"design's VISUAL DESIGN: layout geometry, element scale and position, "
        f"button/control styling, imagery, spacing rhythm. Content matching is "
        f"NOT sufficient. Return ONLY JSON: "
        f'{{"design_match": 1-10, "verdict": "accept"|"rework"|"reject", '
        f'"worst": "<=12 words"}}')
    m = re.search(r"\{.*\}", out, re.S)
    v = json.loads(m.group(0))
    with res.open("a") as f:
        f.write(json.dumps({"screen": name, **v}) + "\n")
    print(f"{name:<28} {v.get('design_match'):>2}/10 {v.get('verdict'):<7} {str(v.get('worst'))[:46]}", flush=True)

rows = [json.loads(l) for l in res.open()]
import statistics, collections
print(f"\nstrict design-match: median {statistics.median(r['design_match'] for r in rows)}"
      f" · verdicts {dict(collections.Counter(r['verdict'] for r in rows))}")
