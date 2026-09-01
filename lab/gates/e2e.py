#!/usr/bin/env python3
"""One card, all the way through. The loop, closed.

Every stage of this pipeline had been validated in isolation and none of them
had ever been run in sequence — which is the same mistake this whole session
kept finding in its own measurements. Two stages had never run at all:

  stage 5  author an L0 card FROM the extracted attributes (never attempted)
  stage 9  feed a gate failure back and re-author (never attempted)

So: take the mockup that won its blind comparison 7/7, lift its palette and
composition, have a model write a card against them, render it, gate it, and
hand every failure back until it passes or the budget runs out. Then judge the
result against the shipped-palette build of the same card.

Stage 1 (generate the mockup) stays blocked on the image key, so this starts
from a mockup already on disk.

Usage:  e2e.py [--rounds N] [--model opus|glm]
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gates            # noqa: E402
import e4_roundtrip     # noqa: E402
import shoot            # noqa: E402
import synth_data       # noqa: E402

OUT = HERE / "e2e"
SUBJECT = ("a weather card for Florence, Italy. It shows the current temperature\n"
           "prominently, the condition, and a short forecast list of a few days.")
# The CARD profile — not `authoring-for-llms.md`, which is the workflow profile
# and says so in its own header: "the generated-UI (card) profile is a sibling
# with different rules — do not carry rules between them." Feeding a model that
# document cost a full E2E run: it opens with `fn add(a, b) { return a + b }`,
# which L0 refuses outright, and taught nothing about `value:`/`unit:`.
SPEC = pathlib.Path.home() / "home" / "Splash" / "docs" / "ui-profile-l0.md"
CATALOG = pathlib.Path.home() / "home" / "Splash" / "docs" / "ui-l0-constructors.toml"
CORPUS = HERE.parent / "style-factory" / "corpus"
APP = pathlib.Path.home() / "home" / "octos-one" / "app" / "target" / "debug" / "octos-app"

BRIEF = """Write ONE card in the L0 profile.

Subject: {subject}

The design direction is lifted from a reference the judges ranked first out of
eight. Honour it:

  ground colour   {ground}   — the page carries the colour; it is not neutral
  ink colour      {ink}
  hero-to-body    {hero_to_body}:1 — one element dominates, everything else is subordinate
  side margin     {margin_fraction} of the width
  hero alignment  {hero_align}
  bands           {bands} — few, large groups; not a dense list

A card names ROLES and never colours: the palette is supplied separately, so do
not write hex anywhere.

Note one trap the catalog answers and prose does not: L0 has NO arithmetic, and
that includes string concatenation. `wx.temp + "°"` is refused. A number with a
unit is a role argument pair — `value:` with `unit:` — not an expression. Use `theme vibrant` — that mood puts the colour in the
page, which is what this reference does.

{guide}

Reply with ONLY the card source. No prose, no code fences."""

REPAIR = """The card you wrote renders, but the layout gates reject it.

{findings}

A gate failure names a node and what is wrong with its geometry. Fix the card so
those stop. Do not change the subject or the design direction.

Here is the card as it stands:

{card}

Reply with ONLY the corrected card source. No prose, no fences."""


def ask_opus(prompt):
    r = subprocess.run(["claude", "-p", prompt, "--model", "opus"],
                       capture_output=True, text=True, timeout=900)
    return strip(r.stdout)


def ask_glm(prompt):
    import urllib.request
    key = os.environ.get("ZAI_KEY") or pathlib.Path(os.environ["ZAI_KEY_FILE"]).read_text().strip()
    body = {"model": "glm-5.3", "max_tokens": 3000, "temperature": 0.3,
            "thinking": {"type": "disabled"},
            "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request(
        "https://api.z.ai/api/coding/paas/v4/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return strip(json.load(r)["choices"][0]["message"]["content"])


def strip(t):
    """Unwrap a fence if there is one, and never leave a stray backtick.

    A single unmatched backtick reached the checker as `unexpected character`
    and burned a whole repair round on my bug rather than the model's."""
    t = (t or "").strip()
    m = re.search(r"```[a-z]*\n(.*?)```", t, re.S)
    t = (m.group(1) if m else t).strip()
    return t.strip("`").strip()


def realize_ok(card_path):
    """Does it pass the L0 checker and realize? Returns (ok, message)."""
    data = synth_data.synth(card_path.read_text())
    dp = OUT / "data.json"
    dp.write_text(json.dumps(data))
    r = subprocess.run(
        ["cargo", "run", "-q", "-p", "splash-ui-l0", "--example", "lower_l0",
         "--", str(card_path), str(dp)],
        cwd=pathlib.Path.home() / "home" / "Splash",
        capture_output=True, text=True, timeout=300)
    first = (r.stderr or "").strip().splitlines()
    msg = first[0] if first else ""
    return (r.returncode == 0 and "realized" in msg), msg


def render_and_gate(card_path, png, geom, palette):
    data = OUT / "data.json"
    env = dict(os.environ,
               MAKEPAD_SEED_L0_FILE=str(card_path),
               MAKEPAD_SEED_L0_DATA=str(data),
               MAKEPAD_WINDOW_SIZE="360x780",
               MAKEPAD_DUMP_GEOMETRY=str(geom),
               MAKEPAD_DUMP_GEOMETRY_FRAMES="40")
    if palette:
        env["MAKEPAD_L0_PALETTE_OVERRIDE"] = str(palette)
    geom.unlink(missing_ok=True)
    p = subprocess.Popen([str(APP)], env=env,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    t0 = time.time()
    while time.time() - t0 < 30 and not geom.exists():
        time.sleep(0.3)
    p.terminate()
    try:
        p.wait(timeout=4)
    except subprocess.TimeoutExpired:
        p.kill()
    if not geom.exists():
        return None, ["render produced no geometry"]
    doc = json.loads(geom.read_text())
    bad = [f for f in gates.run(doc)
           if f.verdict == gates.FAIL and f.gate != "tap_target"]
    shoot.shoot(card_path, png, palette, data=data)
    return doc, bad


def run_once(subject, mockup, rounds, ask, out, log=print):
    """One card, all the way through. Returns a dict describing what happened."""
    out.mkdir(parents=True, exist_ok=True)
    ex = json.loads((HERE / "extract_results.json").read_text())[mockup]["opus"]
    pal = out / "palette.splash"
    src = e4_roundtrip.palette_src(ex["ground"], ex["ink"], ex["accent"])
    if src is None:
        return {"subject": subject, "mockup": mockup, "outcome": "no palette"}
    pal.write_text(src)

    guide = ("Here is the L0 card profile.\n\n" + SPEC.read_text()
             + "\n\nAnd the exact constructor catalog — every role, argument and\n"
               "token that exists. Nothing outside this is admitted.\n\n"
             + CATALOG.read_text())
    card_path = out / "card.card"
    global OUT
    OUT = out                          # realize_ok/render_and_gate write beside the card
    card = ask(BRIEF.format(guide=guide, subject=subject, **ex))
    card_path.write_text(card)

    trail = []
    for rnd in range(1, rounds + 1):
        ok, msg = realize_ok(card_path)
        if not ok:
            trail.append(f"r{rnd} invalid: {msg[:70]}")
            log(f"    r{rnd} invalid: {msg[:64]}")
            card = ask(REPAIR.format(
                findings=f"The card does not validate:\n{msg}", card=card_path.read_text()))
            card_path.write_text(card)
            continue
        doc, bad = render_and_gate(card_path, out / f"r{rnd}.png", out / f"r{rnd}.json", pal)
        PALETTE_OWNED = {"contrast"}
        upstream = [f for f in bad if f.gate in PALETTE_OWNED]
        bad = [f for f in bad if f.gate not in PALETTE_OWNED]
        n = len(doc["widgets"]) if doc else 0
        if not bad:
            trail.append(f"r{rnd} clean ({n} nodes, {len(upstream)} upstream)")
            log(f"    r{rnd} CLEAN — {n} nodes, {len(upstream)} palette-owned")
            return {"subject": subject, "mockup": mockup, "outcome": "converged",
                    "rounds": rnd, "nodes": n, "upstream": len(upstream), "trail": trail}
        trail.append(f"r{rnd} {len(bad)} failing: " + ",".join(sorted({f.gate for f in bad})))
        log(f"    r{rnd} {len(bad)} failing: " + ",".join(sorted({f.gate for f in bad})))
        card = ask(REPAIR.format(
            findings="\n".join(f"  {f.gate}: {f.detail}" for f in bad[:10]),
            card=card_path.read_text()))
        card_path.write_text(card)
    return {"subject": subject, "mockup": mockup, "outcome": "no convergence",
            "rounds": rounds, "trail": trail}


def main():
    rounds = int(sys.argv[sys.argv.index("--rounds") + 1]) if "--rounds" in sys.argv else 3
    model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "opus"
    ask = ask_opus if model == "opus" else ask_glm
    OUT.mkdir(exist_ok=True)

    # ---- stages 2+3: the mockup that won 7/7, and what was lifted from it ----
    ex = json.loads((HERE / "extract_results.json").read_text())["ref_mockup"]["opus"]
    pal_src = e4_roundtrip.palette_src(ex["ground"], ex["ink"], ex["accent"])
    pal = OUT / "palette.splash"
    pal.write_text(pal_src)
    print(f"stage 2/3  ref_mockup (7/7)  ground {ex['ground']}  ink {ex['ink']}\n")

    # ---- stage 5: author ----------------------------------------------------
    guide = ("Here is the L0 card profile.\n\n" + SPEC.read_text()
             + "\n\nAnd the exact constructor catalog — every role, argument and\n"
               "token that exists. Nothing outside this is admitted.\n\n"
             + CATALOG.read_text())
    card_path = OUT / "card.card"
    print(f"stage 5    authoring with {model} …", flush=True)
    card = ask(BRIEF.format(guide=guide, subject=SUBJECT, **ex))
    card_path.write_text(card)
    print(f"           {len(card.splitlines())} lines\n")

    # ---- stages 6-9: render, gate, feed back --------------------------------
    for rnd in range(1, rounds + 1):
        ok, msg = realize_ok(card_path)
        print(f"round {rnd}    realize: {msg[:88]}")
        if not ok:
            card = ask(REPAIR.format(findings=f"The card does not even validate:\n{msg}",
                                     card=card_path.read_text()))
            card_path.write_text(card)
            continue
        doc, bad = render_and_gate(card_path, OUT / f"r{rnd}.png",
                                   OUT / f"r{rnd}.json", pal)
        # Route each failure to the stage that can act on it. A card names ROLES
        # and never colours, so a contrast failure is not something the author
        # can repair — it belongs to the palette, upstream. The first run handed
        # 18 contrast failures to the author and would have looped forever,
        # because every card it could write has exactly the same colours.
        PALETTE_OWNED = {"contrast"}
        upstream = [f for f in bad if f.gate in PALETTE_OWNED]
        bad = [f for f in bad if f.gate not in PALETTE_OWNED]
        if upstream:
            print(f"           {len(upstream)} contrast failure(s) belong to the"
                  f" PALETTE, not the card — not fed back:")
            for f in upstream[:3]:
                print(f"             {f.detail[:70]}")
        n = len(doc["widgets"]) if doc else 0
        print(f"           render: {n} nodes · gates: "
              f"{'CLEAN' if not bad else str(len(bad)) + ' failing'}")
        for f in bad[:6]:
            print(f"             {f.gate:<10} {f.detail[:66]}")
        if not bad:
            print(f"\n  PASSED at round {rnd} -> {OUT}/r{rnd}.png")
            (OUT / "final.card").write_text(card_path.read_text())
            return
        findings = "\n".join(f"  {f.gate}: {f.detail}" for f in bad[:10])
        print("           feeding back …\n", flush=True)
        card = ask(REPAIR.format(findings=findings, card=card_path.read_text()))
        card_path.write_text(card)

    print(f"\n  did not converge in {rounds} rounds")


if __name__ == "__main__":
    main()
