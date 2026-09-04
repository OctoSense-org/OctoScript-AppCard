"""Kit configuration: one JSON per design kit, one loop for all of them."""
import json
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
    # Device wiring, overridable per kit or by env; defaults are this bench.
    c.setdefault("android_serial", "bf0a4730")
    c.setdefault("ohos_serial", "5ZGYD25B13020968")
    c.setdefault("img_port", 8787)
    c.setdefault("verdicts", {})
    for rail in ("desktop", "android", "ohos"):
        c["verdicts"].setdefault(rail, f"xrail/strict_{kit}_{rail}.jsonl")
    return c
