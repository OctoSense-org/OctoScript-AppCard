#!/usr/bin/env python3
"""Do two rails resolve the SAME content for one card?

The check a screenshot cannot be. A rendered card is correct when it carries the
content the card asked for; pixels only ever show that it carries something. So
both rails record the strings they resolved, in tree order, and this compares
the two lists.

Everything this session got wrong about data is a difference in that list and in
nothing any pixel gate was measuring: numbers rendering blank on ArkUI while
makepad coerced them, a shim whose arity left every headline index nil, a field
name the API does not have, a label the lowering discarded. Each one produced a
screen that looked composed.

    python3 content_parity.py --card glm_weather.card

Renders the card on the desktop rail with `SPLASH_CONTENT_DUMP` set, launches it
on the phone, reads the phone's list out of hilog, and diffs. Exit non-zero when
they disagree.

Absent values are compared too: a node whose text resolved to nothing is an
empty entry, not a missing one, so a rail that dropped a value shows a hole at a
POSITION rather than a shorter list.
"""
import argparse
import difflib
import json
import os
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
OH = pathlib.Path.home() / "home/Splash-OH"
TOOLCHAIN = pathlib.Path.home() / "ohos-sdk/ohos-base-deveco/21/toolchains"


def hdc(*args, dev):
    env = dict(os.environ, PATH=f"{TOOLCHAIN}:{os.environ['PATH']}")
    # errors="replace": hilog carries other apps' output and it is not all
    # valid UTF-8. A decode error there would fail the whole comparison over
    # bytes that have nothing to do with this card.
    out = subprocess.run(["hdc", "-t", dev, *args], capture_output=True,
                         env=env).stdout
    return out.decode("utf-8", errors="replace")


def desktop_content(card: pathlib.Path, out_dir: pathlib.Path) -> list:
    """Render on the makepad rail and read back what it resolved."""
    sys.path.insert(0, str(HERE.parent / "gates"))
    dump = out_dir / "content.txt"
    os.environ["GATE_WINDOW"] = "375x906"
    os.environ["MAKEPAD_SEED_L0_FILL_HEIGHT"] = "812"
    os.environ["SPLASH_CONTENT_DUMP"] = str(dump)
    import shoot

    shoot.SIZE = "375x906"
    data = out_dir / "data.json"
    data.write_text(json.dumps({"env": {"locale": {}}}))
    if not shoot.shoot(card, out_dir / f"{card.stem}.png", None,
                       data=data, keep_pt=818):
        raise SystemExit(f"desktop render failed for {card.name}")
    if not dump.exists():
        raise SystemExit("no content dump — is SPLASH_CONTENT_DUMP wired in "
                         "app/app/src/app/l0_widgets.rs?")
    return parse(dump.read_text())


def phone_content(dev: str, index: int) -> list:
    """Launch the card on the phone and read its list out of hilog."""
    pkg = "com.example.myapplication"
    hdc("shell", "aa", "force-stop", pkg, dev=dev)
    hdc("shell", "bm", "clean", "-n", pkg, "-d", dev=dev)
    for i in range(index + 1):
        hdc("shell", "aa", "force-stop", pkg, dev=dev)
        hdc("shell", "hilog", "-r", dev=dev)
        hdc("shell", "power-shell", "wakeup", dev=dev)
        hdc("shell", "aa", "start", "-a", "EntryAbility", "-b", pkg, dev=dev)
        time.sleep(14)
    return parse(hdc("shell", "hilog", "-x", dev=dev))


def parse(text: str) -> list:
    """`content[i]: <string>` lines, in index order, holes preserved."""
    found = {}
    for line in text.splitlines():
        marker = line.find("content[")
        if marker < 0:
            continue
        rest = line[marker + len("content["):]
        idx, _, body = rest.partition("]: ")
        if idx.isdigit():
            found[int(idx)] = body.rstrip()
    return [found.get(i, "\x00MISSING") for i in range(max(found) + 1)] if found else []


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--card", required=True)
    p.add_argument("--index", type=int, default=0,
                   help="which themed screen the phone shows this card at")
    p.add_argument("--device", default=os.environ.get("DEVICE", "5ZGYD25B13020968"))
    p.add_argument("--out", default=str(HERE / "content_parity"))
    a = p.parse_args()

    card = pathlib.Path(a.card)
    if not card.is_absolute():
        card = HERE / card
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    desk = desktop_content(card, out)
    phone = phone_content(a.device, a.index)
    print(f"desktop resolved {len(desk)} text nodes, phone {len(phone)}")

    # Two empty lists are not a match. A capture that produced nothing — a
    # render that failed, a log that was cleared, a card that never mounted —
    # compares equal to another one, and the tool said "content matches".
    # Agreement between two absences is the emptiest possible pass.
    if not desk or not phone:
        print("NO CONTENT: "
              + ", ".join(r for r, l in (("desktop", desk), ("phone", phone)) if not l)
              + " resolved nothing — this is a failed capture, not a match")
        return 1
    if "\x00MISSING" in desk or "\x00MISSING" in phone:
        print("GAP: a capture is missing an index another one has — the two "
              "logs did not come from one render each")
        return 1

    holes = [(r, i) for r, lst in (("desktop", desk), ("phone", phone))
             for i, s in enumerate(lst) if s == ""]
    for rail, i in holes:
        print(f"  EMPTY  {rail}[{i}] resolved to nothing")

    if desk == phone:
        print("content matches" + (" (but see the empties above)" if holes else ""))
        return 1 if holes else 0

    # Two rails fetching LIVE data seconds apart legitimately disagree about a
    # comment count. That is not a content defect, and reporting it the same way
    # as a dropped label makes the tool noise. A position where both sides parse
    # as a number and the lists are the same length is drift; anything else is
    # structural, and structural is what this exists to catch. For a clean run,
    # render both against a frozen fixture.
    def numeric(x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    drift, structural = [], []
    if len(desk) == len(phone):
        for i, (d, p_) in enumerate(zip(desk, phone)):
            if d == p_:
                continue
            (drift if numeric(d) and numeric(p_) else structural).append((i, d, p_))
    else:
        structural = [(None, None, None)]

    # Live data moves by a little. A temperature that reads 30 on one rail and
    # -273 on the other is not drift, and an unconditional numeric exemption
    # passed exactly that. Bound it: same sign, and within a quarter of the
    # larger magnitude.
    def plausible(d, p_):
        x, y = float(d), float(p_)
        if (x < 0) != (y < 0):
            return False
        return abs(x - y) <= max(abs(x), abs(y), 1.0) * 0.25

    wild = [(i, d, p_) for i, d, p_ in drift if not plausible(d, p_)]
    if wild:
        print("\nnumeric values differ by more than live data explains:")
        for i, d, p_ in wild[:8]:
            print(f"  [{i}] desktop {d}  phone {p_}")
        return 1
    if holes:
        print("\nboth rails resolved a text node to nothing at the same "
              "position — agreeing about an absence is not a pass")
        return 1
    if drift and not structural:
        print(f"\ncontent matches structurally; {len(drift)} numeric value(s) "
              f"differ — live data moved between the two renders:")
        for i, d, p_ in drift[:8]:
            print(f"  [{i}] desktop {d}  phone {p_}")
        return 0

    print("\ncontent DIFFERS structurally:")
    for line in difflib.unified_diff(desk, phone, "desktop", "phone",
                                     lineterm="", n=1):
        print("  " + line[:110])
    return 1


if __name__ == "__main__":
    sys.exit(main())
