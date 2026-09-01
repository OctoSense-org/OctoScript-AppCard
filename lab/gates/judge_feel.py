#!/usr/bin/env python3
"""Does each `feel:` (a) change pixels and (b) READ as its word?

Two gates, in the session's canonical order: deterministic first (px diff vs
the unfeeling baseline — a feel that changes nothing is disconnected), judge
second (blind paired, order-swapped: "which render feels more <word>?"). A
feel ships only if both pass; a failed word gets retuned or cut, never shipped
silent.
"""
import json, pathlib, re, sys
sys.path.insert(0, '.')
import shoot
sys.path.insert(0, str(pathlib.Path('../style-factory').resolve()))
import batch_styles as B

FEELS = ["bright", "calm", "bold", "premium", "playful", "warm", "cool",
         "minimal", "inspirational"]
OUT = pathlib.Path('feel_proof'); OUT.mkdir(exist_ok=True)
card = pathlib.Path('e2e_batch/01-weather-ref_mockup/card.card')
src = card.read_text(); data = card.parent / 'data.json'

def render(tag, line):
    s = "\n".join(line if l.strip().startswith("theme ") else l
                  for l in src.splitlines()) + "\n"
    p = OUT / f"{tag}.card"; p.write_text(s)
    png = OUT / f"{tag}.png"
    if not png.exists():
        shoot.shoot(p, png, None, data=data)
    return png

base = render("base", "theme dark")
from PIL import Image, ImageChops, ImageStat
rows = []
for f in FEELS:
    png = render(f, f"theme dark feel: .{f}")
    d = ImageStat.Stat(ImageChops.difference(
        Image.open(base).convert('RGB'), Image.open(png).convert('RGB'))).mean[0]
    rows.append((f, d))
    print(f"{f:<14} px diff vs base: {d:6.2f} {'  <- DISCONNECTED' if d < 0.5 else ''}",
          flush=True)

print("\nsemantic pass (blind, order-swapped):", flush=True)
res = pathlib.Path('feel_proof/verdicts.jsonl')
done = {json.loads(l)["feel"] for l in res.open()} if res.exists() else set()
for f, d in rows:
    if d < 0.5 or f in done:
        continue
    swap = len(f) % 2 == 0
    a, b = (OUT / f"{f}.png", base) if swap else (base, OUT / f"{f}.png")
    out = B.claude_text(
        f"Read {a.resolve()} (call it A) and {b.resolve()} (call it B) — two "
        f"renders of the same weather card in different themes. Which one "
        f"feels more \"{f}\"? Return ONLY JSON: "
        f'{{"winner": "A"|"B", "why": "<=12 words"}}')
    m = re.search(r"\{.*\}", out, re.S)
    v = json.loads(m.group(0))
    feel_won = (v["winner"] == "A") == swap
    with res.open("a") as fp:
        fp.write(json.dumps({"feel": f, "won": feel_won, "why": v.get("why", "")}) + "\n")
    print(f"  {f:<14} {'READS AS ITS WORD' if feel_won else 'FAILED'}: {v.get('why','')[:52]}",
          flush=True)

rows2 = [json.loads(l) for l in res.open()]
print(f"\n{sum(1 for r in rows2 if r['won'])}/{len(rows2)} feels read as their word")
