#!/usr/bin/env python3
"""Does `accent: .<hue>` reach the ink? Decide it on the wire, not by eye.

The old axis was reported inert three times and the reports were correct — it
tinted a bar, a chip and a button, so on a card without those it changed nothing
at all. The claim now is that it moves `l0_text`, which is a claim about pixels
the renderer emits, so read them: the geometry dump carries `fg` per node, and a
foreground colour that does not move is a knob that is still disconnected.

Reports the share of TEXT nodes whose colour changed against `.neutral`, and the
distinct colours drawn, per hue.

Usage:  accent_proof.py [--card PATH] [--hues amber,blue,...]
"""
import collections
import json
import os
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
APP = pathlib.Path.home() / "home" / "octos-one" / "app" / "target" / "debug" / "octos-app"
OUT = HERE / "accent_proof"
DEFAULT_CARD = HERE / "e2e_batch" / "01-weather-ref_mockup" / "card.card"


def themed(src, mood, accent):
    """The card with its theme line rewritten. The card owns its mood; this is a
    measurement rewriting one line, which is why it is here and not in the loop."""
    line = f"theme {mood}" + (f" accent: .{accent}" if accent else "")
    out = []
    for ln in src.splitlines():
        out.append(line if ln.strip().startswith("theme ") else ln)
    return "\n".join(out) + "\n"


def render(card_src, tag, data):
    card = OUT / f"{tag}.card"
    geom = OUT / f"{tag}.json"
    card.write_text(card_src)
    geom.unlink(missing_ok=True)
    env = dict(os.environ,
               MAKEPAD_SEED_L0_FILE=str(card),
               MAKEPAD_SEED_L0_DATA=str(data),
               MAKEPAD_WINDOW_SIZE="360x780",
               MAKEPAD_DUMP_GEOMETRY=str(geom),
               MAKEPAD_DUMP_GEOMETRY_FRAMES="40")
    env.pop("MAKEPAD_L0_PALETTE_OVERRIDE", None)   # the card's own theme, nothing spliced
    p = subprocess.Popen([str(APP)], env=env,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    t0 = time.time()
    while time.time() - t0 < 40 and not geom.exists():
        time.sleep(0.3)
    p.terminate()
    try:
        p.wait(timeout=4)
    except subprocess.TimeoutExpired:
        p.kill()
    if not geom.exists():
        return None
    return json.loads(geom.read_text())


def inks(doc):
    """Every text node's colour, keyed by node index so two runs line up."""
    nodes = doc["widgets"] if isinstance(doc, dict) else doc
    return {n["i"]: n.get("fg") for n in nodes
            if (n.get("text") or "").strip() and n.get("fg")}


def main():
    card_path = pathlib.Path(sys.argv[sys.argv.index("--card") + 1]) if "--card" in sys.argv \
        else DEFAULT_CARD
    hues = (sys.argv[sys.argv.index("--hues") + 1].split(",") if "--hues" in sys.argv
            else ["amber", "blue", "red", "green", "cyan", "magenta", "violet", "indigo"])
    OUT.mkdir(exist_ok=True)
    src = card_path.read_text()
    mood = next((ln.split()[1] for ln in src.splitlines()
                 if ln.strip().startswith("theme ")), "dark")
    data = card_path.parent / "data.json"

    base = render(themed(src, mood, None), "neutral", data)
    if base is None:
        print("baseline render produced no geometry — is the app built?")
        return 1
    b = inks(base)
    print(f"card {card_path.name} · mood {mood} · {len(b)} text nodes\n")
    print(f"{'hue':<9} {'moved':>12}  {'distinct colours':>16}")
    print(f"{'neutral':<9} {'—':>12}  {len(set(b.values())):>16}")

    for hue in hues:
        doc = render(themed(src, mood, hue), hue, data)
        if doc is None:
            print(f"{hue:<9} {'no geometry':>12}")
            continue
        a = inks(doc)
        shared = set(a) & set(b)
        moved = sum(1 for i in shared if a[i] != b[i])
        pct = 100 * moved / max(1, len(shared))
        print(f"{hue:<9} {moved:>4}/{len(shared):<3} {pct:3.0f}%  "
              f"{len(set(a.values())):>16}")

    # What the old axis could reach, for the contrast: a bar, a chip, a button.
    print("\nfor reference, the axis this replaces moved 0 text nodes on every "
          "card:\nit set l0_accent (no readers), l0_bar, l0_active, l0_go.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
