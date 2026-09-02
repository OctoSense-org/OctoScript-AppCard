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
    c.setdefault("verdicts", {})
    for rail in ("desktop", "android", "ohos"):
        c["verdicts"].setdefault(rail, f"xrail/strict_{kit}_{rail}.jsonl")
    return c
