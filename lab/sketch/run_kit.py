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


def stage_unpack(kit):
    """A purchased kit arrives as a .zip holding a .sketch (itself a zip).
    Land the unpacked sketch tree in work/<kit>_sketch and point the config
    at it, so every later stage reads durable paths."""
    import json
    import zipfile
    src = pathlib.Path(kit["sketch"])
    dest = HERE / "work" / f"{kit['name']}_sketch"
    if (dest / "document.json").exists():
        print(f"already unpacked: {dest}")
        return
    if src.is_dir() and (src / "document.json").exists():
        print(f"sketch already a directory: {src}")
        return
    if src.suffix == ".zip":
        with zipfile.ZipFile(src) as z:
            inner = [n for n in z.namelist()
                     if n.endswith(".sketch") and "__MACOSX" not in n]
            if not inner:
                sys.exit(f"no .sketch inside {src}")
            tmp = HERE / "work" / f"{kit['name']}_zip"
            z.extract(inner[0], tmp)
            src = tmp / inner[0]
    dest.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(src) as z:
        z.extractall(dest)
    conf = HERE / "kits" / f"{kit['name']}.json"
    c = json.loads(conf.read_text())
    c["sketch"] = f"work/{kit['name']}_sketch"
    c["img_dir"] = f"work/{kit['name']}_sketch/images"
    conf.write_text(json.dumps(c, indent=2))
    print(f"unpacked -> {dest}; config repointed")


def stage_doctor(kit):
    """Preflight: everything the loop needs, checked in one pass.

    RAISES when not ready. It used to print `NOT ready` and return normally, so
    `--stages doctor,desktop` sailed past a failed preflight and a caller
    reading the shell status was told everything was fine. A preflight that
    cannot stop anything is a paragraph, not a check.
    """
    import shutil
    import socket
    import subprocess as sp
    ok = True

    def check(name, cond, hint=""):
        nonlocal ok
        mark = "ok " if cond else "MISSING"
        print(f"  [{mark:>7}] {name}" + (f"  ({hint})" if hint and not cond else ""))
        ok = ok and bool(cond)

    # The validators, and the theme chain they check. A gate that cannot catch
    # its own defect is worse than no gate, and three of these shipped blind
    # today — so the preflight runs them against injected failures before the
    # loop trusts a single one of their answers.
    print("validators:")
    for name, argv in (
            ("gates catch what they exist for", ["test_gates.py"]),
            ("theme chain resolves in every mood", ["lint_theme.py"]),
            ("HarmonyOS theme copy is current", ["vendor_oh_themes.py", "--check"])):
        r = sp.run([sys.executable, str(HERE / argv[0]), *argv[1:]],
                   capture_output=True, text=True)
        check(name, r.returncode == 0, (r.stdout or r.stderr).strip()[-160:])

    print("tools:")
    check("python PIL+numpy", _try_import("PIL") and _try_import("numpy"),
          "pip install pillow numpy")
    # The desktop capture path imports Quartz (`lab/gates/shoot.py`). It was an
    # undocumented prerequisite: a newcomer discovered it by following an import
    # after the render stage failed.
    check("python Quartz (desktop capture)", _try_import("Quartz"),
          "pip install pyobjc-framework-Quartz")
    check("claude CLI (judge)", shutil.which("claude"), "npm i -g @anthropic-ai/claude-code")
    check("cargo", shutil.which("cargo"))
    check("adb", (pathlib.Path.home() / "Library/Android/sdk/platform-tools/adb").exists()
          or shutil.which("adb"), "Android platform-tools")
    print("repos:")
    for rel in ("home/Splash", "home/octos-one/splash-makepad", "home/Splash-OH"):
        check(rel, (HOME / rel).exists())
    check("desktop binary", (HOME / "home/octos-one/app/target/debug/octos-app").exists(),
          "cd app && cargo build -p octos-app")
    print("kit inputs:")
    check("sketch tree", pathlib.Path(kit["sketch"]).exists())
    check("images dir", pathlib.Path(kit["img_dir"]).is_dir())
    print("devices (optional per rail):")
    adb = str(pathlib.Path.home() / "Library/Android/sdk/platform-tools/adb")
    r = sp.run([adb, "devices"], capture_output=True, text=True) if pathlib.Path(adb).exists() else None
    check(f"android {kit['android_serial']}",
          r and kit["android_serial"] in r.stdout, "plug in + adb authorize")
    hdc = pathlib.Path.home() / "ohos-sdk/ohos-base-deveco/21/toolchains/hdc"
    r = sp.run([str(hdc), "list", "targets"], capture_output=True, text=True) if hdc.exists() else None
    check(f"ohos {kit['ohos_serial']}",
          r and kit["ohos_serial"] in r.stdout, "plug in + 14-day debug signature valid")
    s2 = socket.socket()
    free = s2.connect_ex(("127.0.0.1", kit["img_port"])) != 0
    s2.close()
    check(f"port {kit['img_port']}", True,
          "" if free else "in use (fine if it is this kit's image server)")
    print("doctor:", "ready" if ok else "NOT ready — fix MISSING lines above")
    if not ok:
        raise SystemExit("doctor: preflight failed; nothing after it will be run")


def _try_import(m):
    try:
        __import__(m)
        return True
    except ImportError:
        return False


def stage_extract(kit):
    sh("python3", "sketch2spec.py", kit["sketch"], kit["specs_dir"])
    sh("python3", "spec2png.py", kit["specs_dir"], kit["targets_dir"],
       "--images", kit["img_dir"])


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
    sh("python3", "gate_fill.py", "--kit", kit["name"], "--rail", "desktop")
    sh("python3", "judge_shots.py", "--kit", kit["name"], "--rail", "desktop")


def _ink_parity(kit, rail):
    """Every screen on a device rail, against the desktop render of the same card.

    `gate_ink` existed, passed its own tests, was documented — and no stage
    called it, so nothing it can catch was being caught on any rail. A tested
    gate that is not an applied gate protects nothing.
    """
    ref_dir, shot_dir = kit["desktop_dir"], kit[f"{rail}_dir"]
    bad = []
    for shot in sorted(shot_dir.glob("*.png")):
        ref = ref_dir / shot.name
        if not ref.exists():
            continue
        r = sp.run([sys.executable, str(HERE / "gate_ink.py"), "--ref", str(ref),
                    "--shot", str(shot), "--json"], capture_output=True, text=True)
        if r.returncode != 0:
            bad.append((shot.stem, r.stdout.strip()))
    print(f"ink parity vs desktop: {len(bad)} of {len(list(shot_dir.glob('*.png')))} "
          f"screen(s) dropping content")
    for name, detail in bad[:12]:
        print(f"  {name}: {detail[:120]}")


def stage_android(kit):
    sh("python3", "render_device.py", "l0", "--kit", kit["name"])
    sh("python3", "gate_fill.py", "--kit", kit["name"], "--rail", "android")
    _ink_parity(kit, "android")
    sh("python3", "judge_shots.py", "--kit", kit["name"], "--rail", "android")


def stage_ohos(kit):
    sh("python3", "gen_ohos_atro.py", "--kit", kit["name"])
    hdc = HOME / "ohos-sdk/ohos-base-deveco/21/toolchains/hdc"
    subprocess.run([str(hdc), "-t", "5ZGYD25B13020968", "shell",
                    "bm", "uninstall", "-n", "com.example.myapplication"],
                   capture_output=True)
    sh("bash", "-c", "./build-atro.sh --no-launch", cwd=HOME / "home/Splash-OH")
    sh("python3", "capture_ohos.py", "--kit", kit["name"])
    sh("python3", "gate_fill.py", "--kit", kit["name"], "--rail", "ohos")
    _ink_parity(kit, "ohos")
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
    # Freshness PER CARD, not "the newest file in the directory".
    #
    # The directory's newest file says nothing about the other hundred. Measured
    # here once: 106 of 106 Android captures and 68 of 68 OHOS captures predated
    # the cards they were rendered from, violating this loop's own "renders must
    # postdate their cards" rule, while status printed their medians without a
    # word. A median over stale screens is a number about a previous run.
    cards = {c.stem: c.stat().st_mtime for c in kit["cards_dir"].glob("*.card")}
    for rail in ("desktop", "android", "ohos"):
        d = kit[f"{rail}_dir"]
        shots = {f.stem: f.stat().st_mtime for f in pathlib.Path(d).glob("*.png")}
        missing = sorted(set(cards) - set(shots))
        stale = sorted(n for n, t in shots.items() if n in cards and t < cards[n])
        line = f"  {rail:<8} {newest(d)}"
        v = HERE / kit["verdicts"][rail]
        if v.exists():
            scores = [json.loads(l)["design_match"] for l in v.open()]
            line += f"  · judged {len(scores)}, median {statistics.median(scores)}"
        if missing or stale:
            line += f"  · {len(missing)} MISSING, {len(stale)} STALE"
        print(line)
        for label, names in (("missing", missing), ("stale", stale)):
            if names:
                shown = ", ".join(names[:4])
                more = f" +{len(names) - 4} more" if len(names) > 4 else ""
                print(f"             {label}: {shown}{more}")



def stage_verify(kit):
    """What proves a render kept the card's CONTENT, independent of pixels.

    The rest of this loop measures how a screen looks. Everything that went
    wrong on the data path this year looked fine: numbers that rendered blank,
    a shim whose arity fetched nothing, a field name the API does not have, a
    coordinate that defaulted to 0,0 and pulled a week of ocean weather under a
    card headed 上海. So this stage asks a different question — do two rails
    resolve the SAME strings, in the same order, for one card — and it answers
    it without looking at a single pixel.

    Needs the phone; `desktop` alone cannot answer it, which is the point.
    """
    cards = kit.get("parity_cards", [])
    if not cards:
        raise SystemExit(
            "verify: this kit lists no `parity_cards`, so there is nothing to "
            "compare. Silently doing zero comparisons and reporting success is "
            "the failure this stage exists to prevent — add the card stems to "
            f"kits/{kit['name']}.json.")
    for i, name in enumerate(cards):
        print(f"--- content parity: {name} (screen {i})")
        sh("python3", "content_parity.py", "--card", f"{name}.card", "--index", str(i))


def stage_regress(kit):
    """Did a change to a SHARED piece move screens it was not aimed at?

    The kit, the lowering and the palettes are shared by every screen, and a fix
    is normally proven on the handful that motivated it. Two real regressions
    this year were caught here and nowhere else. Render the corpus twice — once
    with the change reverted — and compare; see regress_desktop.py for why the
    kit's own shots directory is not a baseline.
    """
    sh("python3", "regress_desktop.py", "--kit", kit["name"],
       "--out", f"{kit['desktop_dir'].name}_regress")


STAGES = {"unpack": stage_unpack, "doctor": stage_doctor, "extract": stage_extract, "theme": stage_theme, "author": stage_author,
          "desktop": stage_desktop, "android": stage_android, "ohos": stage_ohos,
          "verify": stage_verify, "regress": stage_regress,
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
