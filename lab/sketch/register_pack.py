#!/usr/bin/env python3
"""Register a NEW theme pack across the stack, with loud anchored edits.

spec2theme writes `_palette_<theme>.splash` (+ `_light`); this wires them in:
  - splash-makepad: palette files must already exist (spec2theme output)
  - catalog THEMES list, both lib.rs mirrors
  - app PALETTES include table (l0_card.rs)
  - accent axis fragments for the new moods (gen_accent_axes.py MOODS)
Then `cargo test -p splash-ui-l0 --test profile` must pass and the app/APK
rebuild picks it up. Idempotent: already-registered names are skipped.

Usage: register_pack.py --kit <name>
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import kitconf  # noqa: E402

HOME = pathlib.Path.home()
MK = HOME / "home/octos-one/splash-makepad/components/l0"
LIBS = [HOME / "home/Splash/crates/splash-ui-l0/src/lib.rs",
        HOME / "home/octos-one/splash/crates/splash-ui-l0/src/lib.rs"]
CARD = HOME / "home/octos-one/app/app/src/app/l0_card.rs"
ACCENTS = HOME / "home/octos-one/lab/sketch/../..//lab/sketch"  # gen script dir


def edit(path, old, new, tag):
    s = path.read_text()
    if new in s:
        print(f"{tag}: already registered")
        return
    if s.count(old) != 1:
        sys.exit(f"{tag}: anchor matches {s.count(old)}x in {path} — register by hand")
    path.write_text(s.replace(old, new))
    print(f"{tag}: registered")


def main():
    kit = kitconf.load(sys.argv[sys.argv.index("--kit") + 1])
    th, tl = kit["theme"], kit["theme_light"]
    for t in (th, tl):
        if not (MK / f"_palette_{t}.splash").exists():
            sys.exit(f"missing {MK / f'_palette_{t}.splash'} — run spec2theme first")

    for lib in LIBS:
        edit(lib, '"atro", "atro_light",',
             f'"atro", "atro_light", "{th}", "{tl}",', f"THEMES {lib.parent.parent.parent.name}")

    edit(CARD,
         '("atro_light", include_str!("../../../../splash-makepad/components/l0/_palette_atro_light.splash")),',
         '("atro_light", include_str!("../../../../splash-makepad/components/l0/_palette_atro_light.splash")),\n'
         f'    ("{th}", include_str!("../../../../splash-makepad/components/l0/_palette_{th}.splash")),\n'
         f'    ("{tl}", include_str!("../../../../splash-makepad/components/l0/_palette_{tl}.splash")),',
         "PALETTES")

    gen = HERE / "gen_accent_axes.py"
    if gen.exists():
        s = gen.read_text()
        if f'"{th}"' not in s:
            if '"atro", "atro_light"' not in s:
                sys.exit("gen_accent_axes MOODS anchor missing — add moods by hand")
            gen.write_text(s.replace('"atro", "atro_light"',
                                     f'"atro", "atro_light", "{th}", "{tl}"'))
            print("accent MOODS: registered")
        subprocess.run(["python3", str(gen)], check=True, cwd=HERE)
        print("accent fragments regenerated")

    r = subprocess.run(["cargo", "test", "-q", "-p", "splash-ui-l0", "--test", "profile"],
                       cwd=HOME / "home/Splash", capture_output=True, text=True)
    ok = "test result: ok" in r.stdout + r.stderr
    print("profile tests:", "ok" if ok else "FAILED — fix before rendering")
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
