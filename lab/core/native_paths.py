"""Shared native repositories live outside AppCards, in the organization workspace."""
from pathlib import Path
import os

APPCARDS = Path(__file__).resolve().parents[2]
WORKSPACE = Path(os.environ.get(
    "OCTOSENSE_WORKSPACE",
    APPCARDS.parent if APPCARDS.parent.name == "octosense-org" else APPCARDS.parent / "octosense-org",
)).resolve()
DIRECTORIES = {"makepad": "makepad", "splash": "octoscript", "splash-makepad": "octoscript-makepad"}


def repository(name, workspace=None):
    return Path(workspace or os.environ.get("OCTOS_APPCARD_NATIVE_ROOT", WORKSPACE)) / DIRECTORIES.get(name, name)


def adapt_cargo_paths(repo):
    """Adapt the pinned upstream sibling directory name; leave Rust crate names intact."""
    import subprocess
    names = subprocess.check_output(["git", "-C", str(repo), "ls-files", "--", "*Cargo.toml"], text=True).splitlines()
    for name in names:
        path = Path(repo) / name
        source = path.read_text()
        updated = cargo_paths(source)
        if updated != source:
            path.write_text(updated)


def cargo_paths(source):
    return source.replace("../../../splash/crates/", "../../../octoscript/crates/")
