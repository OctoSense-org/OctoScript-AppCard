#!/usr/bin/env python3
"""Beauty-card loop: source -> widgets -> Studio inspection -> review -> repair.

    run_kit.py --kit <name> [--stages a,b,c] [--rounds 2]

Stages, in order (each resumable — existing outputs are kept):
  beauty    one author/import + native validation cycle; rerun after repairs
  splash-makepad  release Studio capture, structure + visual gates, repair/gallery
  audit     rerun gates on saved captures; no Studio build or new visual review
  report    refresh composition, visual freshness, repair feedback and gallery
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
CORE = HERE.parent / "core"
sys.path.insert(0, str(HERE.parent))
from core import kitconf  # noqa: E402

HOME = pathlib.Path.home()


def sh(*cmd, cwd=HERE, check=True):
    if cmd[0] == "python3":
        cmd = (sys.executable, *cmd[1:])
    print(f"$ {' '.join(str(c) for c in cmd)}", flush=True)
    r = subprocess.run([str(c) for c in cmd], cwd=cwd)
    if check and r.returncode != 0:
        sys.exit(f"stage failed: {' '.join(str(c) for c in cmd)}")
    return r


def stage_unpack(kit):
    """A purchased kit arrives as a .zip holding a .sketch (itself a zip).
    Land the unpacked sketch tree in work/<kit>_sketch and point the config
    at it, so every later stage reads durable paths."""
    import json
    import zipfile
    src = pathlib.Path(kit["sketch"])
    if not src.exists() and kit.get("source_archive"):
        src = pathlib.Path(kit["source_archive"])
    archive = str(src) if src.is_file() else kit.get("source_archive")
    dest = HERE / "work" / f"{kit['name']}_sketch"
    already = (dest / "document.json").exists()
    if src.is_dir() and (src / "document.json").exists():
        print(f"sketch already a directory: {src}")
        return
    if not already and src.suffix == ".zip":
        with zipfile.ZipFile(src) as z:
            inner = [n for n in z.namelist()
                     if n.endswith(".sketch") and "__MACOSX" not in n]
            if not inner:
                sys.exit(f"no .sketch inside {src}")
            tmp = HERE / "work" / f"{kit['name']}_zip"
            z.extract(inner[0], tmp)
            src = tmp / inner[0]
    if not already:
        dest.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(src) as z:
            z.extractall(dest)
    conf = HERE / "kits" / f"{kit['name']}.json"
    c = json.loads(conf.read_text())
    if archive:
        c["source_archive"] = archive
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
            ("beauty failure handoff and composition evidence", [HERE / "test_beauty_loop.py"]),
            ("native widget policy and acceptance scope", [CORE / "test_composition.py"]),
            ("Camo duplicate pages, source fonts and control mappings", [HERE / "test_camo_native.py"]),
            ("Studio structural gate fault injection", [CORE / "test_structure.py"]),
            ("visual gate freshness and verdict checks", [CORE / "test_visual.py"]),
            ("native import and interaction checks", [HERE / "test_native.py"]),
            ("native graphic and text rendering checks", [HERE / "test_native_graphics.py"])):
        r = sp.run([sys.executable, str(argv[0]), *argv[1:]],
                   capture_output=True, text=True)
        check(name, r.returncode == 0, (r.stdout or r.stderr).strip()[-160:])

    rails = kit["rails"]
    print("tools:")
    check("python PIL+numpy", _try_import("PIL") and _try_import("numpy"),
          "python3 -m venv .venv && .venv/bin/pip install -r requirements.txt")
    check("cargo", shutil.which("cargo"))
    if (kit.get('input_format') not in ('design', 'l0-kit')
            or any(rail != 'splash-makepad' for rail in rails)
            or kit.get('visual_review', 'external') == 'claude_cli'):
        check("claude CLI (legacy author/reviewer)", shutil.which("claude"))
    root = HERE.parents[1]
    for rel in ("Octoscript", "Octoscript-Makepad", "makepad"):
        check(rel, (root / rel).is_dir())
    if "desktop" in rails:
        check("python Quartz", _try_import("Quartz"))
        check("desktop binary", (root / "app/target/release/octos-app").is_file())
    if "splash-makepad" in rails:
        import os
        # EXPLICIT, never PATH. A stale PATH client speaks a misaligned enum
        # protocol at the studio server and misroutes silently — tree dumps
        # answer, snapshots never do, and it reads as a renderer bug.
        if os.environ.get('BEAUTY_BRIDGE'):
            import urllib.request
            try:
                with urllib.request.urlopen(os.environ['BEAUTY_BRIDGE'],timeout=5) as response:
                    health=json.load(response)
                ready=health.get('running') is True
            except (OSError,ValueError):ready=False
            check('persistent Studio bridge is running',ready,'start lab/core/studio_bridge.py')
        else:
            binary = os.environ.get("CARGO_MAKEPAD")
            check("CARGO_MAKEPAD set to the studio's own bridge client",
                  binary and pathlib.Path(binary).is_file(),
                  "export CARGO_MAKEPAD=<studio checkout>/target/release/cargo-makepad")
    if kit.get('input_format') == 'design':
        import os
        binary = os.environ.get('SKETCHTOOL') or shutil.which('sketchtool')
        check('Sketch CLI for original exports and symbol resolution',
              binary and pathlib.Path(binary).is_file(), 'set SKETCHTOOL to Sketch.app/Contents/MacOS/sketchtool')
    if "android" in rails:
        adb = shutil.which("adb") or str(HOME / "Library/Android/sdk/platform-tools/adb")
        r = sp.run([adb, "devices"], capture_output=True, text=True) if pathlib.Path(adb).exists() else None
        check(f"android {kit['android_serial']}", r and bool(kit['android_serial']) and kit['android_serial'] in r.stdout)
    if "ohos" in rails:
        import os
        hdc = pathlib.Path(os.environ.get("HDC", str(HOME / "ohos-sdk/ohos-base-deveco/21/toolchains/hdc")))
        check("Splash-OH", (HOME / "home/Splash-OH").is_dir())
        r = sp.run([str(hdc), "list", "targets"], capture_output=True, text=True) if hdc.exists() else None
        check(f"ohos {kit['ohos_serial']}", r and bool(kit['ohos_serial']) and kit['ohos_serial'] in r.stdout)
    print("kit inputs:")
    check("sketch source", pathlib.Path(kit["sketch"]).exists())
    check("images dir", pathlib.Path(kit.get("img_dir", "")).is_dir())
    print("doctor:", "ready" if ok else "NOT ready")
    if not ok:
        raise SystemExit("doctor: preflight failed; nothing after it will be run")


def _try_import(m):
    try:
        __import__(m)
        return True
    except ImportError:
        return False


def stage_extract(kit):
    if kit.get('input_format') == 'l0-kit':
        sh('python3','sketch_native.py','--kit',kit['source_native_kit'])
        return
    if kit.get('input_format') == 'design':
        sh('python3','sketch_native.py','--kit',kit['name'])
        return
    sys.exit(f"unsupported input_format {kit.get('input_format')!r}: the current path imports "
             "'design' (Sketch) or 'l0-kit' sources; the spec/theme rail was retired")


def stage_promote(kit):
    sh("python3", CORE / "promote_l0.py",'--kit',kit.get('source_native_kit',kit['name']))
    sh('python3','export_app_recipes.py')


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
    suffix = 'splash' if kit.get('input_format') == 'design' else 'card'
    print(f"  cards    {newest(kit['cards_dir'], '*.'+suffix)}")
    # Freshness PER CARD, not "the newest file in the directory".
    #
    # The directory's newest file says nothing about the other hundred. Measured
    # here once: 106 of 106 Android captures and 68 of 68 OHOS captures predated
    # the cards they were rendered from, violating this loop's own "renders must
    # postdate their cards" rule, while status printed their medians without a
    # word. A median over stale screens is a number about a previous run.
    cards = {c.stem: c.stat().st_mtime for c in kit["cards_dir"].glob('*.'+suffix) if c.stem in kit['screens']}
    for rail in (r.replace("-", "_") for r in kit["rails"]):
        d = kit[f"{rail}_dir"]
        shots = {f.stem: f.stat().st_mtime for f in pathlib.Path(d).glob("*.png")}
        missing = sorted(set(cards) - set(shots))
        stale = sorted(n for n, t in shots.items() if n in cards and t < cards[n])
        if rail == "splash_makepad":
            from core import render_splash_makepad as native
            for name in sorted(set(cards) & set(shots)):
                try:
                    meta = json.loads((d / f"{name}.capture.json").read_text())
                    inputs = [kit["cards_dir"] / f"{name}.{suffix}",
                              kit["cards_dir"] / f"{name}.data.json",
                              kit["specs_dir"] / f"{name}.json"]
                    expected = native.fingerprint([*native.shared_inputs(kit), *inputs])
                    current = native.fresh(meta, expected, d / f"{name}.png")
                except (OSError, ValueError):
                    current = False
                if not current and name not in stale:
                    stale.append(name)
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



def stage_report(kit):
    """Refresh saved evidence without rebuilding or making a new visual judgment."""
    # Gallery refreshes feedback, composition and acceptance together, including
    # when invoked directly. Do not independently hash every capture twice.
    sh("python3", CORE / "gallery.py", "--kit", kit["name"], "--rail", "splash_makepad")
    print(f"Repair findings: {kit['splash_makepad_dir']/'repair-feedback.json'}")


def stage_splash_makepad(kit, audit_only=False):
    out = kit['splash_makepad_dir']
    out.mkdir(parents=True, exist_ok=True)
    run = {'kit':kit['name'], 'status':'running', 'scope':'fixed_artboard_parity',
           'operation':'audit_saved_evidence' if audit_only else 'capture_and_review',
           'stages':[], 'errors':[]}
    path = out/'pipeline-run.json'
    def save():
        path.write_text(json.dumps(run,indent=2)+'\n')
    def step(script, *args):
        result = sh('python3',script,'--kit',kit['name'],*args,check=False)
        run['stages'].append({'script':script,'returncode':result.returncode})
        if result.returncode:
            run['errors'].append(f'{script} exited {result.returncode}')
        save()
        return result.returncode == 0
    save()
    try:
        reviewer = kit.get('visual_review', 'external')
        if reviewer not in ('external', 'claude_cli'):
            raise ValueError('visual_review must be external or claude_cli')
        captured = False if audit_only else step('capture_loop.py')
        # Even a failed capture must leave missing/host-only inspection findings.
        step('gate_structure.py')
        step('gate_composition.py')
        if kit.get('input_format') == 'l0-kit':
            step('gate_kit.py')
        if captured:
            step('gate_fill.py','--rail','splash_makepad')
            if reviewer == 'claude_cli':
                step('judge_shots.py','--rail','splash_makepad')
            elif reviewer == 'external':
                print('Visual review: supply a current source/native receipt with lab/core/review.py, then audit.')
        step('gate_visual.py','--rail','splash_makepad')
    except (OSError, ValueError, KeyboardInterrupt) as error:
        run['errors'].append(f'{type(error).__name__}: {error}')
        raise
    finally:
        run['status'] = 'failed' if run['errors'] else 'passed'
        save()
        # Rendering/judging failures used to exit before this repair handoff.
        stage_report(kit)
    if run['errors']:
        raise SystemExit('design gates failed; see pipeline-run.json, repair-feedback.json and gallery.html')


def stage_audit(kit):
    stage_splash_makepad(kit, audit_only=True)


def stage_beauty(kit):
    """One concrete cycle. Importer/renderer repairs are code changes between runs."""
    try:
        stage_author(kit)
    except (subprocess.CalledProcessError, OSError, KeyboardInterrupt, SystemExit) as error:
        out=kit['splash_makepad_dir']
        out.mkdir(parents=True,exist_ok=True)
        (out/'pipeline-run.json').write_text(json.dumps({'kit':kit['name'],'status':'failed',
            'stages':[{'script':'author','returncode':getattr(error,'returncode',1)}],
            'errors':[f'author: {type(error).__name__}: {error}']},indent=2)+'\n')
        stage_report(kit)
        raise
    stage_splash_makepad(kit)


def stage_validate(kit):
    sh("python3", CORE / "render_splash_makepad.py", "--kit", kit["name"], "--check-only")


STAGES = {"beauty": stage_beauty, "audit": stage_audit, "report": stage_report, "validate": stage_validate,
          "splash-makepad": stage_splash_makepad, "unpack": stage_unpack, "doctor": stage_doctor,
          "extract": stage_extract, "status": stage_status, "promote": stage_promote}


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
        # unpack changes the sketch/image paths; chained stages must see them.
        kit = kitconf.load(kit["name"])


if __name__ == "__main__":
    main()
