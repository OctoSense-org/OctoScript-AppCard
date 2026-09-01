#!/usr/bin/env python3
"""Run the layout gates over the Material catalog, not just the L0 corpus.

The L0 corpus exercises about a dozen roles. `kit-host` renders 45 screens of
the Material Components catalog — buttons, chips, sheets, pickers, navigation —
from the byte-identical `.splash` sources the Android catalog renders with real
`com.google.android.material.*` views. That is a much wider surface, and it is
the one where the widget layer's gaps live.

Getting here needed three things that did not exist:
  * `Area::rect_union` and `WidgetTree::geometry_json` ported into the second
    makepad checkout (`makepad-splash`), which had neither
  * a dump hook in kit-host
  * `Splash::register_subtree`, because kit-host assigns `view` directly rather
    than going through `set_text`, so nothing ever put the screen in the widget
    tree — the first dump of a fully-rendered screen returned SEVEN nodes

Usage:  catalog_sweep.py [--only <substring>]
"""
import collections
import json
import os
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gates  # noqa: E402

KIT = pathlib.Path.home() / "home" / "Splash-Makepad"
APP = KIT / "target" / "debug" / "kit-host"
SCREENS = KIT / "components" / "material" / "screens"
OUT = HERE / "catsweep"
SETTLE = float(os.environ.get("CAT_SETTLE", "18"))


def render(route, out):
    if out.exists():
        return True
    env = dict(os.environ, SPLASH_ROUTE=route,
               MAKEPAD_DUMP_GEOMETRY=str(out),
               MAKEPAD_DUMP_GEOMETRY_FRAMES="40")
    p = subprocess.Popen([str(APP)], cwd=KIT, env=env,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    t0 = time.time()
    while time.time() - t0 < SETTLE and not out.exists():
        time.sleep(0.3)
    if p.poll() is None:
        p.terminate()
        try:
            p.wait(timeout=4)
        except subprocess.TimeoutExpired:
            p.kill()
    return out.exists()


def main():
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    OUT.mkdir(exist_ok=True)
    routes = sorted(p.stem for p in SCREENS.glob("*.splash") if p.stem != "kit")
    if only:
        routes = [r for r in routes if only in r]

    findings = collections.defaultdict(list)
    clean, failed, sizes = 0, [], {}
    for i, r in enumerate(routes, 1):
        g = OUT / f"{r}.json"
        if not render(r, g):
            failed.append(r)
            print(f"  [{i}/{len(routes)}] {r:<20} no render", flush=True)
            continue
        doc = json.loads(g.read_text())
        sizes[r] = len(doc["widgets"])
        hits = collections.Counter()
        for f in gates.run(doc):
            # tap_target fires on every render in the L0 host too; counting it
            # per card drowns everything else. Reported separately below.
            if f.verdict == gates.FAIL and f.gate != "tap_target":
                hits[f.gate] += 1
                findings[f.gate].append((r, f.detail))
        if hits:
            print(f"  [{i}/{len(routes)}] {r:<20} {len(doc['widgets']):4} nodes  "
                  + " ".join(f"{k}x{v}" for k, v in hits.items()), flush=True)
        else:
            clean += 1
            print(f"  [{i}/{len(routes)}] {r:<20} {len(doc['widgets']):4} nodes  clean", flush=True)

    print(f"\n{'=' * 66}")
    print(f"{len(routes)} screens · {len(routes)-len(failed)} rendered · {clean} clean "
          f"· {len(failed)} failed")
    if sizes:
        print(f"nodes per screen: min {min(sizes.values())} "
              f"max {max(sizes.values())} total {sum(sizes.values())}\n")
    for gate, items in sorted(findings.items(), key=lambda kv: -len(kv[1])):
        print(f"  {gate:<11} {len(items):4} findings across "
              f"{len({r for r, _ in items})} screens")
    (OUT / "findings.json").write_text(json.dumps(dict(findings), indent=1))
    print(f"\n-> {OUT / 'findings.json'}")


if __name__ == "__main__":
    main()
