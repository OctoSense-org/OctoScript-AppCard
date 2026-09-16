#!/usr/bin/env python3
"""Compatibility entry point for the reusable image-to-appcard-flow bundle exporter."""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "wizard/card-bundle")
    args = parser.parse_args()
    return subprocess.run([
        sys.executable, str(ROOT.parents[1] / "lab/image-to-appcard-flow/bundle.py"),
        "--project", str(ROOT), "--manifest", str(ROOT / "image-to-appcard-flow.json"),
        "--output", str(args.output),
    ], check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
