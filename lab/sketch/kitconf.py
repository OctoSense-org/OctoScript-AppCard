"""Kit configuration: one JSON per design kit, one loop for all of them."""
import json
import os
import pathlib

HERE = pathlib.Path(__file__).resolve().parent


def load(kit: str) -> dict:
    c = json.loads((HERE / "kits" / f"{kit}.json").read_text())
    c["name"] = kit
    for key in ("specs_dir", "targets_dir", "cards_dir", "desktop_dir",
                "android_dir", "ohos_dir"):
        c[key] = HERE / c.get(key, f"{key.split('_')[0]}_{kit}")
    # sketch/img_dir may be written repo-relative (kits ship in work/);
    # resolve against this directory so callers can run from anywhere.
    for key in ("sketch", "img_dir"):
        if key in c and not str(c[key]).startswith("/"):
            c[key] = str(HERE / c[key])
    # Device wiring: env override, then the kit's own value, then this bench.
    #
    # The README documented `ANDROID_SERIAL` and `OHOS_SERIAL` and nothing read
    # them, so someone could set the documented variable and still have every
    # stage talk to the wrong phone — the worst shape of a configuration bug,
    # because it looks configured.
    c.setdefault("android_serial", "bf0a4730")
    c.setdefault("ohos_serial", "5ZGYD25B13020968")
    c.setdefault("img_port", 8787)
    for key, var in (("android_serial", "ANDROID_SERIAL"),
                     ("ohos_serial", "OHOS_SERIAL"),
                     ("img_port", "IMG_PORT")):
        if os.environ.get(var):
            c[key] = os.environ[var]
    c.setdefault("verdicts", {})
    for rail in ("desktop", "android", "ohos"):
        c["verdicts"].setdefault(rail, f"xrail/strict_{kit}_{rail}.jsonl")
    return c
