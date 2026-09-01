#!/usr/bin/env python3
"""Step 0: re-run the measurements that a disconnected knob invalidated.

Three results said theme axes do nothing — `accent_hue` costs +0.15 over 100
specimens, axes-vs-no-axes 52/48 blind-paired, mockup fidelity 2.67 -> 2.67 with
axes restored. All three were correct readings of a control with NO CONSUMER:
`card_theme_axes()` parsed the card's axes and nothing in the host ever called
it, so "with axes" and "without axes" rendered the same pixels.

That is now wired, and `axis_proof.py` shows the accent moving 20 of 21 text
nodes. So the question those three results tried to answer is open again, and
has to be asked before any further axis is built: **does a connected palette
knob move a judge?**

Same instrument as before — blind paired, order swapped per specimen, judged for
fidelity to the mockup rather than on an absolute scale, because absolute scores
drift more than the effect does. What differs is only that the treatment arm now
reaches the screen.

A tie is a real answer here and is reported as one. If axes and no-axes come out
level on a wired build, the idea is dead on evidence rather than on a miswiring,
and steps 1-5 are the wrong work.

Usage:  axis_ab.py [--n 12] [--out axis_ab]
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "style-factory"))
import shoot  # noqa: E402

OUT = HERE / "axis_ab"
RESULTS = OUT / "verdicts.jsonl"

# One axis set per design school, so the treatment arm is a real design choice
# rather than a random tint. These are the coordinates a designer would pick for
# that school, which is what the axes are FOR — a random draw would test whether
# noise helps, and the answer to that is already known.
ARMS = {
    # `ref_mockup` is cream type on terracotta and `r021` is Swiss achromatic:
    # for both, the design-correct accent is the IDENTITY. The first run gave
    # them amber and blue and lost 4 of 4 for one reason — "target pairs neutral
    # cream type with a saturated field; B tints all text amber" — which is a
    # correct verdict about a wrong arm and says nothing about the axis.
    #
    # A specimen whose right answer is `.neutral` cannot inform this comparison
    # at all, because `.neutral` renders identically to no axes. Those are
    # excluded rather than assigned a hue, and the two targets left are the ones
    # with genuinely chromatic ink: art deco's gold and the punk zine's acid.
    "r012-weather-art_deco": "accent: .amber type: .display emphasis: .poster",
    "r004-weather-punk_zine": "accent: .green emphasis: .poster texture: .noise",
}


def themed(src, line):
    return "\n".join(line if ln.strip().startswith("theme ") else ln
                     for ln in src.splitlines()) + "\n"


def mood_of(src):
    for ln in src.splitlines():
        if ln.strip().startswith("theme "):
            return ln.split()[1]
    return "dark"


def render(card_src, tag, data):
    card = OUT / f"{tag}.card"
    png = OUT / f"{tag}.png"
    card.write_text(card_src)
    if not png.exists():
        shoot.shoot(card, png, None, data=data)
    return png if png.exists() else None


def main():
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 12
    OUT.mkdir(exist_ok=True)
    import batch_styles as B  # noqa: E402  (needs the key path it owns)

    done = set()
    if RESULTS.exists():
        done = {json.loads(l)["id"] for l in RESULTS.open()}

    # Every card the E2E batch produced, paired with the mockup it came from —
    # so "closer to the target" is a question about a real target.
    jobs = []
    # The two batch directories reuse names (`01-weather-ref_mockup` exists in
    # both), so the id carries its batch. Without that the resume set collides
    # and one specimen is judged twice while another is never judged at all.
    # The id is also a FILENAME, so the batch tag carries no separator that a
    # path would eat. The first attempt used `batch[5:]` and a slash, which
    # sliced to "atch" and then tried to write into a directory that does not
    # exist.
    for tag, batch in (("now", "e2e_batch"), ("prev", "e2e_batch_before")):
        root = HERE / batch
        if not root.is_dir():
            continue
        for d in sorted(root.iterdir()):
            card = d / "card.card"
            if d.is_dir() and card.exists():
                # `e2e_batch.py` names its directories with the mockup
                # TRUNCATED to 12 characters, so a full-name match finds
                # nothing: "r012-weather-art_deco" is not a substring of
                # "06-weather-r012-weather".
                mock = next((m for m in ARMS if m[:12] in d.name), None)
                if mock:
                    jobs.append((f"{tag}-{d.name}", card, mock))
    jobs = jobs[:n]
    print(f"{len(jobs)} specimens · axes off vs on, blind paired\n", flush=True)

    for name, card, mock in jobs:
        if name in done:
            continue
        src = card.read_text()
        mood = mood_of(src)
        data = card.parent / "data.json"
        off = render(themed(src, f"theme {mood}"), f"{name}-off", data)
        on = render(themed(src, f"theme {mood} {ARMS[mock]}"), f"{name}-on", data)
        if not (off and on):
            print(f"[{name}] render failed", flush=True)
            continue
        target = next((p for p in (HERE / "e0").glob(f"{mock}*.png")), None)
        if target is None:
            print(f"[{name}] no target for {mock}", flush=True)
            continue
        # Order swapped per specimen, so position bias cannot become the result.
        swap = sum(ord(c) for c in name) % 2 == 0
        try:
            verdict, why = B.judge_pair(target, off, on, swap)
        except Exception as exc:  # noqa: BLE001
            print(f"[{name}] ERR {str(exc)[:70]}", flush=True)
            continue
        with RESULTS.open("a") as f:
            f.write(json.dumps({"id": name, "mock": mock, "arm": ARMS[mock],
                                "axes_win": verdict, "why": why}) + "\n")
        tag = "AXES" if verdict > 0 else ("NO-AXES" if verdict < 0 else "tie")
        print(f"[{name}] {tag}: {why[:64]}", flush=True)

    rows = [json.loads(l) for l in RESULTS.open()] if RESULTS.exists() else []
    if not rows:
        return
    w = sum(1 for r in rows if r["axes_win"] > 0)
    lose = sum(1 for r in rows if r["axes_win"] < 0)
    tie = len(rows) - w - lose
    print(f"\n{'=' * 56}\n{len(rows)} judged · axes {w} · no-axes {lose} · tie {tie}")
    # The pre-fix result was 52/48 on a disconnected knob, i.e. noise. Anything
    # that does not clear noise here says the same thing about a wired one.
    if w + lose:
        print(f"win rate among decided: {100 * w / (w + lose):.0f}%  "
              f"(pre-fix, disconnected: 52%)")
    print(f"-> {RESULTS}")


if __name__ == "__main__":
    main()
