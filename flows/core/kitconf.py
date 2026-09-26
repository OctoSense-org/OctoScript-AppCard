"""Kit configuration: one JSON per design kit, one loop for all of them."""
import json
import os
import pathlib

HERE = pathlib.Path(__file__).resolve().parent


def load(kit: str) -> dict:
    c = json.loads((HERE / "kits" / f"{kit}.json").read_text())
    c["name"] = kit
    for key in ("specs_dir", "targets_dir", "cards_dir", "desktop_dir",
                "android_dir", "ohos_dir", "splash_makepad_dir"):
        c[key] = HERE / c.get(key, f"{key.split('_')[0]}_{kit}")
    # sketch/img_dir may be written repo-relative (kits ship in work/);
    # resolve against this directory so callers can run from anywhere.
    for key in ("sketch", "img_dir", "source_archive"):
        if key in c and not str(c[key]).startswith("/"):
            c[key] = str(HERE / c[key])
    # Device wiring is local configuration, never a built-in personal device.
    #
    # The README documented `ANDROID_SERIAL` and `OHOS_SERIAL` and nothing read
    # them, so someone could set the documented variable and still have every
    # stage talk to the wrong phone — the worst shape of a configuration bug,
    # because it looks configured.
    c.setdefault("android_serial", "")
    c.setdefault("ohos_serial", "")
    c.setdefault("img_port", 8787)
    c.setdefault("rails", ["desktop", "android", "ohos"])
    c.setdefault("design_scale", 2)
    for key, var in (("android_serial", "ANDROID_SERIAL"),
                     ("ohos_serial", "OHOS_SERIAL"),
                     ("img_port", "IMG_PORT")):
        if os.environ.get(var):
            c[key] = os.environ[var]
    c["img_port"] = int(c["img_port"])
    c.setdefault("verdicts", {})
    for rail in ("desktop", "android", "ohos", "splash_makepad"):
        c["verdicts"].setdefault(rail, f"xrail/strict_{kit}_{rail}.jsonl")
    c.setdefault("feedback_rail", c["rails"][0].replace("-", "_"))
    c.setdefault("feedback", c["verdicts"][c["feedback_rail"]])
    return c
