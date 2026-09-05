#!/usr/bin/env python3
"""Re-render a kit's cards and report which screens MOVED.

The kit, the L0 lowering and the palettes are shared by every screen, and a
change to one of them is normally validated on the handful of screens that
motivated it. This renders the whole corpus again and says which screens
changed and by how much, so a fix proven on four cards cannot quietly rewrite a
hundred others. Pixel difference is a signal, not a verdict: a screen that moved
may have moved for the better. The point is that the list is short enough to
look at, and this found two real regressions in changes that had passed on the
screens they were written for.

    # 1. revert the change, render the baseline THROUGH THIS SCRIPT
    python3 regress_desktop.py --kit camo --out shots_camo_desktop_base
    # 2. restore the change, render again
    python3 regress_desktop.py --kit camo --out shots_camo_desktop_regress
    # 3. compare the two
    python3 regress_desktop.py --kit camo --against shots_camo_desktop_base \\
                               --out shots_camo_desktop_regress

**The kit's own `desktop_dir` is NOT a baseline.** `fill_fix.py` writes its
measured-stretch re-renders back into that same directory, so most of what sits
there came out of a different pipeline than a plain render. Diffed against it,
94 of 107 CaMo screens "moved" — identical content at a different scale — and
the real signal (one screen) was buried. A baseline has to be rendered the same
way as the thing it is compared against, which means rendering it here, with the
change reverted.
"""
import json
import os
import pathlib
import socket
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "gates"))
sys.path.insert(0, str(HERE))

os.environ["GATE_WINDOW"] = "375x906"
os.environ["MAKEPAD_SEED_L0_FILL_HEIGHT"] = "812"
import shoot  # noqa: E402
import kitconf  # noqa: E402

shoot.SIZE = "375x906"


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def serve_kit_images(img_dir: pathlib.Path, port: int = 8787):
    """Serve THIS kit's images on the port the cards name — and prove it.

    The cards carry `http://127.0.0.1:8787/...` as state initials, so the port
    is fixed and shared between kits. Checking only that something is listening
    is not a check: a server left over from another kit answers the connection
    and 404s every image, and the screens render with empty photo tiles. That
    read as a 50% regression in a shared-code change that had nothing to do with
    images. So probe a file this kit actually has, and take the port if the
    answer is wrong.
    """
    import urllib.request

    probe = next((p.name for p in sorted(img_dir.iterdir()) if p.is_file()), None)
    if probe is None:
        raise SystemExit(f"no images in {img_dir}")

    def serves_us():
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/{probe}", timeout=2) as r:
                return r.status == 200
        except Exception:
            return False

    if serves_us():
        return
    s = socket.socket()
    listening = s.connect_ex(("127.0.0.1", port)) == 0
    s.close()
    if listening:
        subprocess.run(["bash", "-c", f"lsof -ti :{port} -sTCP:LISTEN | xargs -r kill"],
                       capture_output=True)
        time.sleep(0.5)
    subprocess.Popen(["python3", "-m", "http.server", str(port)], cwd=img_dir,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(20):
        time.sleep(0.3)
        if serves_us():
            return
    raise SystemExit(f"image server on {port} is not serving {img_dir}")


def compare_dirs(cards, base, out):
    """(moved, missing) for one card list across two render directories.

    Split out so a test can drive it with directories it built itself. The test
    that used to stand for this one searched the source for a string.
    """
    import numpy as np
    from PIL import Image

    moved, missing = [], []
    for card in cards:
        a_p, b_p = base / f"{card.stem}.png", out / f"{card.stem}.png"
        if not (a_p.exists() and b_p.exists()):
            missing.append(card.stem)
            continue
        a = Image.open(a_p).convert("L").resize((188, 409))
        b = Image.open(b_p).convert("L").resize((188, 409))
        d = float((np.abs(np.asarray(a, float) - np.asarray(b, float)) > 24).mean())
        if d > 0.005:
            moved.append((d, card.stem))
    moved.sort(reverse=True)
    return moved, missing


def main():
    kit = kitconf.load(arg("--kit", "camo"))
    base = kit["desktop_dir"]
    out = pathlib.Path(arg("--out", str(base.parent / f"{base.name}_regress")))
    out.mkdir(parents=True, exist_ok=True)

    serve_kit_images(pathlib.Path(kit["img_dir"]))

    data = out / "data.json"
    data.write_text(json.dumps({"env": {"locale": {}}}))
    cards = sorted(kit["cards_dir"].glob("*.card"))
    for i, card in enumerate(cards, 1):
        png = out / f"{card.stem}.png"
        if png.exists():
            continue
        ok = shoot.shoot(card, png, None, data=data, keep_pt=818)
        print(f"[{i}/{len(cards)}] {card.stem} {'ok' if ok else 'FAILED'}", flush=True)

    # ---- diff -------------------------------------------------------------
    import numpy as np
    from PIL import Image

    against = arg("--against")
    if against:
        base = pathlib.Path(against)
        if not base.is_absolute():
            base = HERE / base
    else:
        print(f"WARNING: comparing against {base.name}, which fill_fix.py also "
              f"writes into — pass --against a baseline rendered by this script")

    moved, missing = compare_dirs(cards, base, out)
    print(f"\n{len(moved)} of {len(cards)} screens moved")
    for d, name in moved:
        print(f"  {d:6.1%}  {name}")
    # A render that never happened is not a screen that did not move. Printing
    # it and returning success meant a run that failed to render half the corpus
    # reported the same clean answer as one that rendered all of it.
    if missing:
        print(f"\n{len(missing)} screen(s) NOT COMPARED — a render is missing:")
        for name in missing[:12]:
            print(f"  {name}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
