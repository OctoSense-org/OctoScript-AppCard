#!/usr/bin/env python3
"""The whole loop, one kit config at a time: Sketch file in, three rails out.

    run_kit.py --kit <name> [--stages a,b,c] [--rounds 2]

Stages, in order (each resumable — existing outputs are kept):
  extract   .sketch -> specs (sketch2spec) and design targets (spec2png)
  theme     specs -> theme pack (spec2theme) + registration (register_pack)
            [new kits only; then REBUILD desktop app + APK before rendering]
  author    LLM writes one L0 card per screen (author_cards, validate loop)
  desktop   render on desktop makepad (render_v2) + strict judge
  android   render on the OnePlus 6T (render_device l0) + strict judge
            [assumes the installed APK carries the current kit code]
  ohos      assemble ArkUI sources (gen_ohos_atro), deploy fresh HAP
            (build-atro.sh), capture one cold launch per screen, judge
  status    print per-stage artifact freshness and rail medians

A NEW kit needs kits/<name>.json first — copy kits/atro.json and set: sketch
path, theme/theme_light/model names, screens (artboard names), img_dir
(extracted kit images). Prereqs the loop cannot do for you: phones plugged in
(adb: OnePlus, hdc: Mate 70 Air), a valid 14-day HarmonyOS debug signature,
and a rebuild of the desktop binary/APK after `theme` registers a new pack.
"""
import json
import pathlib
import statistics
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import kitconf  # noqa: E402

HOME = pathlib.Path.home()


def sh(*cmd, cwd=HERE, check=True):
    print(f"$ {' '.join(str(c) for c in cmd)}", flush=True)
    r = subprocess.run([str(c) for c in cmd], cwd=cwd)
    if check and r.returncode != 0:
        sys.exit(f"stage failed: {' '.join(str(c) for c in cmd)}")


def stage_extract(kit):
    sh("python3", "sketch2spec.py", kit["sketch"], kit["specs_dir"])
    sh("python3", "spec2png.py", kit["specs_dir"], kit["targets_dir"])


def stage_theme(kit):
    sh("python3", "spec2pack.py", "--kit", kit["name"])
    sh("python3", "register_pack.py", "--kit", kit["name"])
    print("REBUILD REQUIRED before desktop/android: "
          "cargo build -p octos-app && tools/build-android.sh")


def stage_author(kit, rounds=1):
    for r in range(rounds):
        args = ["python3", "author_cards.py", "--kit", kit["name"]]
        if r > 0:
            args.append("--round2")
        sh(*args)


def stage_desktop(kit):
    sh("python3", "render_v2.py", "--kit", kit["name"])
    sh("python3", "judge_shots.py", "--kit", kit["name"], "--rail", "desktop")


def stage_android(kit):
    sh("python3", "render_device.py", "l0", "--kit", kit["name"])
    sh("python3", "judge_shots.py", "--kit", kit["name"], "--rail", "android")


def stage_ohos(kit):
    sh("python3", "gen_ohos_atro.py", "--kit", kit["name"])
    hdc = HOME / "ohos-sdk/ohos-base-deveco/21/toolchains/hdc"
    subprocess.run([str(hdc), "-t", "5ZGYD25B13020968", "shell",
                    "bm", "uninstall", "-n", "com.example.myapplication"],
                   capture_output=True)
    sh("bash", "-c", "./build-atro.sh --no-launch", cwd=HOME / "home/Splash-OH")
    sh("python3", "capture_ohos.py", "--kit", kit["name"])
    sh("python3", "judge_shots.py", "--kit", kit["name"], "--rail", "ohos")


def stage_status(kit):
    def newest(d, pat="*.png"):
        files = list(pathlib.Path(d).glob(pat))
        if not files:
            return "—"
        age = (time.time() - max(f.stat().st_mtime for f in files)) / 3600
        return f"{len(files)} files, newest {age:.1f}h old"

    print(f"kit: {kit['name']}  screens: {len(kit['screens'])}")
    print(f"  specs    {newest(kit['specs_dir'], '*.json')}")
    print(f"  targets  {newest(kit['targets_dir'])}")
    print(f"  cards    {newest(kit['cards_dir'], '*.card')}")
    for rail in ("desktop", "android", "ohos"):
        line = f"  {rail:<8} {newest(kit[f'{rail}_dir'])}"
        v = HERE / kit["verdicts"][rail]
        if v.exists():
            scores = [json.loads(l)["design_match"] for l in v.open()]
            line += f"  · judged {len(scores)}, median {statistics.median(scores)}"
        print(line)


STAGES = {"extract": stage_extract, "theme": stage_theme, "author": stage_author,
          "desktop": stage_desktop, "android": stage_android, "ohos": stage_ohos,
          "status": stage_status}


def main():
    kit = kitconf.load(sys.argv[sys.argv.index("--kit") + 1]
                       if "--kit" in sys.argv else "atro")
    want = (sys.argv[sys.argv.index("--stages") + 1].split(",")
            if "--stages" in sys.argv else ["status"])
    rounds = (int(sys.argv[sys.argv.index("--rounds") + 1])
              if "--rounds" in sys.argv else 1)
    for name in want:
        fn = STAGES.get(name)
        if fn is None:
            sys.exit(f"unknown stage {name!r}; known: {', '.join(STAGES)}")
        print(f"\n=== {name} ===", flush=True)
        fn(kit, rounds) if name == "author" else fn(kit)


if __name__ == "__main__":
    main()
