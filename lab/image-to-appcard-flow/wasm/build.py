#!/usr/bin/env python3
"""Build a source-traceable Makepad/WASM host without modifying submodules."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import uuid

from manifest import PACKAGE, cargo_manifest
from package import package_runtime
from publish import publish_package

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from core.native_paths import repository, WORKSPACE as NATIVE_WORKSPACE
from core.native_runtime import runtime_tool, verify as verify_runtime


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), *args])


def prepare_dependencies(workspace: Path, scratch: Path, mode: str) -> tuple[dict, dict]:
    from core.native_runtime import prepare, verify, dependencies
    root = workspace if mode == "existing" else scratch / "dependencies"
    receipt = verify(root) if mode == "existing" else prepare(root, cache=workspace)
    return dependencies(root), receipt


def checked_inputs(project: Path) -> tuple[dict[str, Path], dict[str, str]]:
    fonts = {f"NotoSansSC-{weight}.ttf": project / "fonts" / f"NotoSansSC-{weight}.ttf"
             for weight in ("Regular", "Medium", "Bold")}
    fonts["OFL.txt"] = project / "fonts/OFL.txt"
    for name, path in fonts.items():
        if not path.is_file() or not path.stat().st_size:
            raise RuntimeError(f"Missing required project font/license: fonts/{name}")
    return fonts, {f"fonts/{name}": sha(path) for name, path in fonts.items()}


def capture_sources() -> dict[str, str]:
    return {str(path.relative_to(HERE)): sha(path) for path in sorted(HERE.rglob("*"))
            if path.is_file() and not any(part.startswith(".") or part == "__pycache__"
                                          for part in path.relative_to(HERE).parts)
            and path.suffix != ".pyc"}


def run(args: argparse.Namespace) -> dict:
    workspace, project, output = (p.resolve() for p in (args.workspace, args.project, args.output))
    if output.exists() and not args.replace:
        raise RuntimeError("Output already exists; use a new output directory to retain previous package evidence")
    if output == project or output in project.parents or output == HERE or output in HERE.parents:
        raise RuntimeError("Package output must not replace project or pipeline source directories")
    scratch = (args.build_dir or NATIVE_WORKSPACE / '.appcard-native/wasm' / project.name).resolve()
    if scratch == output or output in scratch.parents or scratch in output.parents:
        raise RuntimeError("Build directory and package output must be separate directory trees")
    for protected in (repository(name, workspace) for name in ('makepad', 'splash', 'splash-makepad')):
        if scratch == protected or protected in scratch.parents:
            raise RuntimeError("Build directory must not be inside a source submodule")
        if output == protected or protected in output.parents:
            raise RuntimeError("Package output must not be inside a source submodule")
    scratch.mkdir(parents=True, exist_ok=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    build_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    run_dir = scratch / "runs" / build_id
    run_dir.mkdir(parents=True)
    receipt = {"schema": 1, "build_id": build_id, "status": "preparing", "renderer": "Makepad/WASM",
               "workspace": str(workspace), "project": str(project), "output": str(output),
               "dependency_mode": args.dependency_mode, "pipeline_sources": capture_sources()}
    (run_dir / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    try:
        fonts, receipt["project_inputs"] = checked_inputs(project)
        dependencies, receipt["runtime"] = prepare_dependencies(workspace, scratch, args.dependency_mode)
        receipt["dependencies"] = {**receipt["runtime"]["repositories"], "octoscript-makepad": receipt["runtime"]["runtime"]}
        host = scratch / "host"
        host.mkdir(exist_ok=True)
        shutil.copytree(HERE / "template", host, dirs_exist_ok=True)
        (host / "Cargo.toml").write_text(cargo_manifest(dependencies))
        runtime_root = dependencies["octoscript-makepad"].parent
        (host / ".cargo").mkdir(exist_ok=True)
        (host / ".cargo/config.toml").write_text(runtime_tool(runtime_root).cargo_config(runtime_root))
        resources = host / "resources/service"
        resources.mkdir(parents=True, exist_ok=True)
        for name, path in fonts.items():
            shutil.copy2(path, resources / name)
        if args.target_dir:
            target = args.target_dir.resolve()
            target.mkdir(parents=True, exist_ok=True)
            host_target = host / "target"
            if host_target.exists() and host_target.resolve() != target:
                raise RuntimeError("Generated host already uses a different target cache")
            if not host_target.exists():
                host_target.symlink_to(target, target_is_directory=True)
        receipt["generated_sources"] = {
            name: sha(host / name) for name in ("Cargo.toml", "Cargo.lock", "src/main.rs", "bridge.mjs", "index.html")}
        receipt["toolchain"] = {}
        for name, command in (("rustc_nightly", ["rustup", "run", "nightly", "rustc", "--version"]),
                              ("cargo_nightly", ["rustup", "run", "nightly", "cargo", "--version"])):
            receipt["toolchain"][name] = subprocess.check_output(command, text=True).strip()
        if args.prepare_only:
            receipt["status"] = "prepared"
            receipt["host"] = str(host)
            return receipt
        tool = args.cargo_makepad.resolve() if args.cargo_makepad else dependencies["makepad"] / "target/release/cargo-makepad"
        if not tool.is_file():
            if args.dependency_mode == "existing":
                raise RuntimeError("Existing mode requires an existing cargo-makepad executable; use isolated mode to build it")
            # Tool output stays in scratch; the source checkout is not changed.
            tool_target = scratch / "tool-target"
            compiler_lock = HERE / "toolchain/cargo-makepad.lock"
            shutil.copy2(compiler_lock, dependencies["makepad"] / "Cargo.lock")
            shutil.copy2(compiler_lock, run_dir / "cargo-makepad.lock")
            receipt["compiler_lock_sha256"] = sha(compiler_lock)
            with (run_dir / "compiler-build.log").open("w") as log:
                subprocess.run(["cargo", "build", "--manifest-path", str(dependencies["makepad"] / "Cargo.toml"),
                                "-p", "cargo-makepad", "--release", "--locked", "--target-dir", str(tool_target)],
                               cwd=dependencies["makepad"], stdout=log, stderr=subprocess.STDOUT, check=True)
            tool = tool_target / "release/cargo-makepad"
        receipt["cargo_makepad_sha256"] = sha(tool)
        command = [str(tool), "wasm", "--no-threads", "build", "-p", PACKAGE, "--release", "--locked"]
        receipt["command"] = command
        env = os.environ.copy()
        # Pinned cargo-makepad packages from cwd/target, so a symlink is used for caching.
        env.pop("CARGO_TARGET_DIR", None)
        with (run_dir / "build.log").open("w") as log:
            subprocess.run(command, cwd=host, env=env, stdout=log, stderr=subprocess.STDOUT, check=True)
        if sha(host / "Cargo.lock") != receipt["generated_sources"]["Cargo.lock"]:
            raise RuntimeError("Cargo.lock changed despite locked compilation")
        receipt["cargo_sources"] = runtime_tool(runtime_root).verify_cargo(runtime_root, host / "Cargo.toml")
        if verify_runtime(runtime_root) != receipt["runtime"]:
            raise RuntimeError("Unified runtime source changed while building")
        if capture_sources() != receipt["pipeline_sources"]:
            raise RuntimeError("Pipeline sources changed while building; retry from a stable source snapshot")
        receipt["status"] = "compiled"
        receipt["threads"] = False
        receipt["font_backend"] = "SDF/SLUG; no-atomics build does not launch an MSDF worker"
        receipt["asset_policy"] = "Same-origin iframe card-assets plus locked Octosense HTTPS bases; native remains loopback-only"
        receipt["known_limits"] = ["Explicit HTTPS hosting bases only", "Complete Noto Sans SC Regular embedded",
                                    "Chromium 1243 occasionally stalls on direct appointment-card cold mount; this build is not a browser compatibility claim"]
        temp = Path(tempfile.mkdtemp(prefix=f".{output.name}-package-", dir=output.parent))
        receipt["staging_package"] = str(temp)
        try:
            package_runtime(host, temp, project, dependencies, receipt)
            receipt["status"] = "packaged"
            previous = output.parent / f".{output.name}.previous-{build_id}" if output.exists() else None
            if previous:
                if not args.replace:
                    raise RuntimeError("Output appeared during build; refusing to overwrite")
                receipt["previous_package"] = str(previous)
            # Full provenance is copied into every package; file hashes exclude this self-referential record.
            (temp / "build.json").write_text(json.dumps(receipt, indent=2) + "\n")
            receipt["package_receipt_sha256"] = sha(temp / "build.json")
            # Stage and hash everything before the OS atomic directory exchange.
            for name, expected in receipt["files"].items():
                if sha(temp / name) != expected:
                    raise RuntimeError(f"Staged package hash mismatch: {name}")
            (run_dir / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
            publish_package(temp, output, previous)
        except Exception:
            receipt["incomplete_package"] = str(temp)
            raise
        return receipt
    except Exception as error:
        receipt["status"] = "failed"
        receipt["error"] = str(error)
        raise
    finally:
        receipt["run_evidence"] = str(run_dir)
        (run_dir / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("workspace", "project", "output"):
        p.add_argument(f"--{name}", type=Path, required=True)
    p.add_argument("--dependency-mode", choices=("isolated", "existing"), default="isolated")
    p.add_argument("--build-dir", type=Path)
    p.add_argument("--target-dir", type=Path, help="Reuse Cargo artifacts via generated host/target symlink")
    p.add_argument("--cargo-makepad", type=Path, help="Existing compiler executable; SHA is recorded")
    p.add_argument("--prepare-only", action="store_true", help="Verify/stage dependencies and generate the host without compiling")
    p.add_argument("--replace", action="store_true", help="Publish only after verification; retain the previous package beside output")
    return p


if __name__ == "__main__":
    try:
        result = run(parser().parse_args())
        print(json.dumps({key: result.get(key) for key in ("status", "build_id", "output", "wasm_sha256", "run_evidence")}))
    except Exception as error:
        print(f"WASM pipeline failed: {error}", file=sys.stderr)
        sys.exit(1)
