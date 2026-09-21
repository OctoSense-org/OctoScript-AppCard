#!/usr/bin/env python3
"""The sibling checkouts the ArkUI camera host compiles against.

apps/camera/oh takes octoscript-oh-arkui, the Octoscript VM and makepad's script
crate by relative path, so without this the build silently follows whatever those
working copies happen to be on. oh-runtime.lock.json records the revisions known
to build, the way native-runtime.lock.json does for the Makepad host.

    python3 pins.py check     compare the siblings with the lock
    python3 pins.py update    rewrite the lock from the siblings
    python3 pins.py show      print what the siblings are on
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
# apps/camera/oh -> camera -> apps -> the repository -> the siblings live beside it,
# which is what the ../../../../ paths in Cargo.toml reach.
ROOT = HERE.parents[3]
LOCK = HERE / "oh-runtime.lock.json"


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args],
                          capture_output=True, text=True).stdout.strip()


def state(name):
    repo = ROOT / name
    if not (repo / ".git").exists():
        return None
    return {
        "revision": git(repo, "rev-parse", "HEAD"),
        "branch": git(repo, "rev-parse", "--abbrev-ref", "HEAD"),
        "dirty": bool(git(repo, "status", "--porcelain")),
        "path": repo,
    }


def same_subtree(repo, revision, paths):
    """True when `paths` are byte-identical between `revision` and the checkout."""
    if subprocess.run(["git", "-C", str(repo), "cat-file", "-e", revision + "^{commit}"],
                      capture_output=True).returncode != 0:
        return False
    done = subprocess.run(["git", "-C", str(repo), "diff", "--quiet", revision, "HEAD",
                           "--", *paths], capture_output=True)
    return done.returncode == 0


def load():
    return json.loads(LOCK.read_text())


def main(argv):
    command = argv[1] if len(argv) > 1 else "check"
    lock = load()
    repositories = lock["repositories"]

    if command == "update":
        for name, entry in repositories.items():
            now = state(name)
            if now is None:
                print(f"{name}: no checkout at {ROOT / name}, left alone")
                continue
            if now["revision"] != entry["revision"]:
                print(f"{name}: {entry['revision'][:8]} -> {now['revision'][:8]}")
            entry["revision"] = now["revision"]
            entry["branch"] = now["branch"]
        LOCK.write_text(json.dumps(lock, indent=2) + "\n")
        print(f"wrote {LOCK.name}")
        return 0

    problems = []
    for name, entry in repositories.items():
        now = state(name)
        if now is None:
            problems.append(f"{name}: no checkout at {ROOT / name}")
            continue
        if command == "show":
            mark = " dirty" if now["dirty"] else ""
            print(f"{name:16} {now['branch']:30} {now['revision'][:8]}{mark}")
            continue
        if now["revision"] != entry["revision"]:
            # Only part of a repository may be used here. makepad contributes its
            # script crate alone, so a different revision is fine as long as that
            # subtree is identical; a feature branch and its merge commit differ
            # in hash and not in anything this build compiles.
            paths = entry.get("paths")
            if paths and same_subtree(now["path"], entry["revision"], paths):
                print(f"note: {name} is on {now['revision'][:8]} rather than "
                      f"{entry['revision'][:8]}, but {', '.join(paths)} is identical")
                continue
            problems.append(
                f"{name}: on {now['revision'][:8]} ({now['branch']}), "
                f"the lock says {entry['revision'][:8]} ({entry.get('branch', '?')})")
        elif now["dirty"]:
            print(f"note: {name} is on the pinned revision but has uncommitted changes")

    if command == "show":
        return 0
    if problems:
        print("the ArkUI camera's sibling checkouts do not match oh-runtime.lock.json:")
        for p in problems:
            print("  " + p)
        print()
        print("Check them out at the pinned revisions, or accept the current ones with")
        print("  python3 apps/camera/oh/pins.py update")
        print("Set PINS=skip to build anyway.")
        return 1
    print("pins ok")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
