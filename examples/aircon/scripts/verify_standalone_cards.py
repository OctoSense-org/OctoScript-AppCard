#!/usr/bin/env python3
"""Verify exported fixed-fixture service cards using an existing Studio build.

No compilation, scene wrapper, service reducer, or image-parity gate is run.
The caller must own the Studio transport and pause live service watchers.
All host writes target _runtime; cards/ contains copies sealed by SHA-256.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / "flows"))
from core.native_paths import repository


def source_path(relative):
    """Resolve paths recorded before apps/ became examples/ and lab/ became flows/."""
    if relative.startswith("pipeline/"):
        name, _, tail = relative[9:].partition("/")
        if name in ("makepad", "splash", "splash-makepad"):
            return repository(name) / tail
        relative = relative[9:]
        for old, new in LEGACY_PREFIXES:
            if relative.startswith(old):
                relative = new + relative[len(old):]
                break
        return ROOT.parents[1] / relative
    return ROOT / relative


# Recorded infrastructure receipts name the pre-restructure directories.
LEGACY_PREFIXES = (("lab/image-to-appcard-flow/", "flows/image-to-card/"),
                   ("lab/image-to-appcard/", "flows/image-lib/"),
                   ("lab/sketch-to-appcard/", "flows/kits/sketch/"),
                   ("lab/", "flows/"),
                   ("apps/", "examples/"))

PIPELINE = ROOT.parents[1] / "flows/image-lib"
CATALOGUE = ROOT / "service-cards/catalogue.json"
CURRENT = PIPELINE / "current-request.json"
TOLERANCE = 1.0  # Native Studio integer inspection rounds logical points.
SCOPE = ("Standalone native fixed-fixture mounting at each exported artboard size; "
         "WidgetTreeDump, WidgetSnapshot, WidgetQuery, measured layout and real "
         "Button/KitAction probes. No service effects or full-image parity claim.")


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".new")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def sha(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def manifest(directory):
    directory = Path(directory)
    return {str(p.relative_to(directory)): sha(p)
            for p in sorted(directory.rglob("*")) if p.is_file()}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def delta(a, b):
    if not isinstance(a, (list, tuple)) or len(a) != 4 or len(b) != 4:
        return math.inf
    if not all(isinstance(v, (int, float)) and math.isfinite(v) for v in (*a, *b)):
        return math.inf
    return max(abs(x - y) for x, y in zip(a, b))


def inside(inner, outer, tolerance=TOLERANCE):
    x, y, w, h = inner
    ox, oy, ow, oh = outer
    return (w >= 0 and h >= 0 and x >= ox - tolerance and y >= oy - tolerance
            and x + w <= ox + ow + tolerance and y + h <= oy + oh + tolerance)


def check_inputs(catalogue):
    cards = catalogue["cards"]
    require(len(cards) == 14, "Expected all 14 exported service-card fixtures")
    require(len({c["id"] for c in cards}) == len(cards), "Duplicate catalogue card ID")
    for card in cards:
        folder = (ROOT / card["folder"]).resolve()
        require(folder.is_relative_to(ROOT / "service-cards"), "Card folder escapes service-cards")
        require(card["id"] == folder.name, "Catalogue ID/folder mismatch")
        for name in ("page.card", "page.data.json", "mapping.json", "mapped.json",
                     "contract.json", "semantic-map.json", "service-actions.json",
                     "kit/native/light/kit.json", "kit/native/light/components.l0"):
            require((folder / name).is_file(), f"{card['id']}: missing {name}")
        width, height = card["artboard"]
        require(all(isinstance(v, (int, float)) and math.isfinite(v) and v > 0
                    for v in (width, height)), "Invalid standalone artboard")
        contract, mapping = read(folder / "contract.json"), read(folder / "mapping.json")
        require(contract.get("standalone_service_card") is True, "Export is not a standalone card")
        require(contract["id"] == card["id"] and contract["artboard"] == card["artboard"],
                "Catalogue/contract artboard mismatch")
        require(mapping["contract_sha256"] == sha(folder / "contract.json"), "Stale compiled contract")
        rows = mapping["elements"]
        require(len(rows) == card["nodes"], "Catalogue/native mapping node count mismatch")
        require(len({r["native_id"] for r in rows}) == len(rows), "Duplicate native mapping ID")
        require(len({r["source_id"] for r in rows}) == len(rows), "Duplicate source mapping ID")
        roots = [r for r in rows if r["parent"] is None]
        require(len(roots) == 1 and roots[0]["source_id"] == card["source_surface"],
                "Export must contain exactly the standalone service surface root")
        require(delta(roots[0]["bounds"], [0, 0, width, height]) < 1e-5,
                "Standalone root must be at origin and match its artboard")
        controls = [r for r in rows if r["kind"] == "button"]
        require(len(controls) == card["native_controls"], "Catalogue/button count mismatch")
        actions = read(folder / "service-actions.json")["controls"]
        require({r["parent"] for r in controls} == set(actions), "Service action/button binding mismatch")
        for control in controls:
            require(bool(control["enabled"]) == bool(actions[control["parent"]]["enabled"]),
                    "Service action/native enabled-state mismatch")
        for entry in read(folder / "semantic-map.json")["elements"]:
            require(not entry.get("behavior") and not entry.get("data"),
                    "Standalone verifier expects a static fixture without mutable semantic bindings")
        for font, expected in mapping.get("fonts", {}).items():
            require(font.startswith("self:"), "Unexpected font resource scheme")
            font_path = repository("splash-makepad") / "apps/kit-host" / font.removeprefix("self:")
            require(sha(font_path) == expected, "Compiled font/runtime resource hash mismatch")
    return cards


def runtime_manifest():
    """Hash actual runtime inputs/binaries, independently of historical receipts."""
    paths = {ROOT / "runtime/infrastructure.json", Path(__file__).resolve(),
             PIPELINE / "studio.py", PIPELINE / "compile.py",
             ROOT.parents[1] / "flows/core/gate_structure.py"}
    infra = read(ROOT / "runtime/infrastructure.json")
    paths.update(source_path(value["path"]) for value in infra["binaries"].values())
    for base in ("runtime", "pipeline/splash-makepad/apps/kit-host/src",
                 "pipeline/splash-makepad/apps/kit-host/resources/service",
                 "pipeline/splash-makepad/crates/splash-makepad/src",
                 "pipeline/splash-makepad/crates/splash-widgets/src",
                 "pipeline/splash-makepad/crates/makepad-plot/src",
                 "pipeline/makepad/widgets/src", "pipeline/makepad/draw/src",
                 "pipeline/makepad/platform/studio/src", "pipeline/makepad/platform/script/src"):
        for path in (source_path(base)).rglob("*"):
            if path.is_file() and path.suffix in (".rs", ".py", ".sh", ".patch", ".ttf"):
                paths.add(path)
    return {os.path.relpath(p, ROOT): sha(p) for p in sorted(paths)}


def snapshot_rect(node, snapshot):
    windows = [w for w in snapshot["widgets"] if w["widget_type"] == "Window"
               and w.get("window_id") == node.get("window_id")]
    require(len(windows) == 1, "Snapshot widget has no unique native Window origin")
    origin = windows[0]
    return [node["x"] - origin["x"], node["y"] - origin["y"], node["width"], node["height"]]


def evaluate_geometry(card, mapping, native, layout, tree, snapshot, queries, build, nonce):
    """Compare independent native inspection sources with the compiled mapping."""
    errors, differences = [], []
    require(native.get("ok") is True, "Native host rejected this card")
    require(native.get("request", {}).get("nonce") == nonce, "Stale native manifest nonce")
    require(native["request"].get("build_id") == build, "Stale native manifest build")
    require(layout.get("nonce") == nonce, "Stale native layout nonce")
    require(snapshot.get("build_id") == build, "Stale native snapshot build")
    expected_ids = {r["native_id"] for r in mapping}
    require({n["id"] for n in native["elements"]} == expected_ids,
            "Mounted subtree differs from standalone mapping (or contains scene siblings)")
    require(native["nodes"] == len(mapping), "Native manifest node count mismatch")
    trees = {n["id"]: n for n in tree}
    snaps = {n["id"]: n for n in snapshot["widgets"]}
    layouts = {n["id"]: n for n in layout["elements"]}
    sources = {n["source_id"]: n for n in mapping}
    width, height = card["artboard"]
    windows = [n for n in snapshot["widgets"] if n["widget_type"] == "Window"]
    if len(windows) != 1 or delta([0, 0, windows[0]["width"], windows[0]["height"]],
                                  [0, 0, width, height]) > TOLERANCE:
        errors.append("Native Window is not the standalone artboard size")
    for row in mapping:
        wid = row["native_id"]
        t, s, l, q = trees.get(wid), snaps.get(wid), layouts.get(wid), queries.get(wid, {})
        issues = []
        actual = l.get("bounds") if l else None
        if not t or not s or not l:
            issues.append("Missing native tree/snapshot/layout element")
        else:
            if delta(actual, row["bounds"]) > TOLERANCE:
                issues.append("Measured layout differs from mapping")
            if delta(actual, t["bounds"]) > TOLERANCE:
                issues.append("Native tree/layout geometry disagrees")
            if delta(actual, snapshot_rect(s, snapshot)) > TOLERANCE:
                issues.append("Native snapshot/layout geometry disagrees")
            if delta(actual, l.get("clipped_bounds", [])) > TOLERANCE:
                issues.append("Native bounds are clipped")
            if not inside(actual, [0, 0, width, height]):
                issues.append("Native element falls outside standalone artboard")
            if s.get("visible") is not True:
                issues.append("Native element is hidden")
            if row["parent"] and t.get("parent") != sources[row["parent"]]["native_id"]:
                issues.append("Wrong native parent")
            if t["type"] != s["widget_type"]:
                issues.append("Tree/snapshot widget type disagrees")
            expected_type = {"text": "Label", "button": "Button", "svg": "Svg"}.get(row["kind"])
            if expected_type and s["widget_type"] != expected_type:
                issues.append("Wrong native widget type")
            if row.get("text") is not None and s.get("text") != row["text"]:
                issues.append("Native text mismatch")
            if row.get("enabled") is not None and s.get("enabled") != bool(row["enabled"]):
                issues.append("Native enabled state mismatch")
            if row["kind"] == "text" and (not l.get("text_layout") or not inside(l["text_layout"], actual)):
                issues.append("Missing or overflowing native text layout")
            if row["kind"] == "svg" and l.get("vector_ready") is not True:
                issues.append("Native SVG is not ready")
            if row["kind"] == "image" and not l.get("image_pixels"):
                issues.append("Native image pixels are unavailable")
            if l.get("glass_ready") is False:
                issues.append("Native backdrop is unavailable")
            rects = q.get("rects", [])
            if q.get("build_id") != build or q.get("query") != "id:" + wid or len(rects) != 1:
                issues.append("Missing, stale or ambiguous WidgetQuery")
            else:
                parts = rects[0].split()
                if (len(parts) != 7 or parts[1] != wid or parts[2] != t["type"]
                        or delta(list(map(float, parts[3:])), actual) > TOLERANCE):
                    issues.append("WidgetQuery/layout geometry or type disagrees")
        differences.append({"source_id": row["source_id"], "native_id": wid,
                            "expected_bounds": row["bounds"], "actual_bounds": actual, "issues": issues})
        errors.extend(row["source_id"] + ": " + issue for issue in issues)
    return {"passed": not errors, "errors": errors, "elements": differences,
            "tolerance_logical_points": TOLERANCE, "viewport_logical": [width, height]}


class Verifier:
    def __init__(self, output, build, studio, parse_dump, timeout):
        self.output, self.build, self.studio = output, build, studio
        self.parse_dump, self.timeout = parse_dump, timeout
        self.active = None

    def guard(self):
        if self.active:
            require(read(CURRENT).get("nonce") == self.active["nonce"],
                    "Native request ownership lost; another session mounted the host")

    def ask(self, kind, body=None, response=True):
        self.guard()
        reply = self.studio.request(kind, body or {"build_id": self.build}, kind if response else None)
        self.guard()
        if response:
            require(reply.get("build_id") == self.build, "Stale Studio build in " + kind)
        return reply

    def mount(self, card, inputs, work):
        self.guard()
        work.mkdir(parents=True, exist_ok=False)
        width, height = card["artboard"]
        spec = {"card": str(inputs / "page.card"), "data": str(inputs / "page.data.json"),
                "format": "l0-kit", "kit_dir": str(inputs / "kit"), "width": width, "height": height,
                "nonce": "standalone-" + uuid.uuid4().hex, "build_id": self.build,
                "semantic": str(inputs / "semantic-map.json")}
        for key, name in (("result", "native.json"), ("layout", "layout.json"),
                          ("actions", "actions.json"), ("semantic_result", "semantic-state.json"),
                          ("semantic_probe", "semantic-probe.json")):
            spec[key] = str(work / name)
        write(work / "request.json", spec)
        # Always redirect startup/parking writes into this run's mutable work.
        write(CURRENT, spec)
        self.active = spec
        return spec

    def settled(self, card, work):
        deadline, resize_at = time.monotonic() + self.timeout, 0
        while time.monotonic() < deadline:
            self.guard()
            if time.monotonic() >= resize_at:
                self.ask("RunViewResize", {"build_id": self.build, "window_id": 0,
                         "width": card["artboard"][0], "height": card["artboard"][1], "dpi": 2.0}, False)
                resize_at = time.monotonic() + 2
            try:
                native, layout = read(work / "native.json"), read(work / "layout.json")
                require(native.get("ok") is True, "Native host rejected standalone card")
                if (native.get("request", {}).get("nonce") == self.active["nonce"]
                        and layout.get("nonce") == self.active["nonce"]):
                    require(native["request"].get("build_id") == self.build, "Stale native build")
                    return native, layout
            except (OSError, ValueError):
                pass
            time.sleep(.1)
        pending = work / "layout.json.pending.json"
        detail = pending.read_text() if pending.exists() else "No native layout written"
        raise RuntimeError("Standalone layout did not settle: " + detail)

    def screenshot(self, work, card, name="native"):
        shot = self.ask("Screenshot", {"build_id": self.build, "kind_id": 0})
        receipt = self.studio.save_viewport_screenshot(
            shot, work / (name + ".png"), width=card["artboard"][0], height=card["artboard"][1], dpi=2.0)
        write(work / (name + "-screenshot.json"), shot)
        return receipt

    def probe_buttons(self, card, mapping, layout, work):
        sources = {r["source_id"]: r for r in mapping}
        measured = {n["id"]: n for n in layout["elements"]}
        controls, checks = [r for r in mapping if r["kind"] == "button"], []
        for index, row in enumerate(controls):
            self.guard()
            directory = work / "controls" / f"{index + 1:02d}-{row['source_id']}"
            directory.mkdir(parents=True)
            query = self.ask("WidgetQuery", {"build_id": self.build, "query": "id:" + row["native_id"]})
            write(directory / "query.json", query)
            require(len(query.get("rects", [])) == 1, "Ambiguous native button query")
            before_snapshot = self.ask("WidgetSnapshot")
            write(directory / "snapshot-before.json", before_snapshot)
            widgets = [w for w in before_snapshot["widgets"] if w["id"] == row["native_id"]]
            require(len(widgets) == 1 and widgets[0]["widget_type"] == "Button", "Button not native")
            enabled = bool(row["enabled"])
            require(widgets[0].get("enabled") == enabled, "Button enabled state differs from fixture")
            bounds = measured[row["native_id"]]["bounds"]
            require(delta(snapshot_rect(widgets[0], before_snapshot), bounds) <= TOLERANCE,
                    "Button geometry changed before click")
            before = read(work / "actions.json")
            require(isinstance(before, list), "Invalid native action log")
            write(directory / "actions-before.json", before)
            x, y, w, h = bounds
            point = [round(x + w / 2), round(y + h / 2)]
            write(directory / "click.json", {"build_id": self.build, "nonce": self.active["nonce"],
                  "source_id": row["source_id"], "native_id": row["native_id"], "bounds": bounds,
                  "point": point, "enabled": enabled, "method": "Actual Studio Click at measured native centre"})
            self.ask("Click", {"build_id": self.build, "x": point[0], "y": point[1]}, False)
            deadline = time.monotonic() + (3 if enabled else .8)
            after = before
            while time.monotonic() < deadline:
                self.guard()
                after = read(work / "actions.json")
                require(after[:len(before)] == before, "Native action log reset during fixture probe")
                activated = [a for a in after[len(before):] if a.get("action", {}).get("kind") == "activated"]
                if activated:
                    break
                time.sleep(.08)
            after_snapshot = self.ask("WidgetSnapshot")
            write(directory / "snapshot-after.json", after_snapshot)
            write(directory / "actions-after.json", after)
            expected_id = sources[row["parent"]]["native_id"]
            matching = [a for a in activated if a.get("id") == expected_id]
            wrong = [a for a in activated if a.get("id") != expected_id]
            after_node = next(w for w in after_snapshot["widgets"] if w["id"] == row["native_id"])
            passed = (len(matching) == 1 and not wrong) if enabled else not activated
            passed = passed and after_node.get("enabled") == enabled
            checks.append({"source_id": row["source_id"], "native_id": row["native_id"],
                           "kit_action_id": expected_id, "enabled": enabled, "passed": passed,
                           "activated_events": activated, "evidence": str(directory.relative_to(work))})
        result = {"passed": all(c["passed"] for c in checks), "buttons": checks,
                  "fixture_state": "unchanged; KitAction is observed without a reducer or external service"}
        write(work / "interactions.json", result)
        return result

    def capture(self, card, inputs, work):
        spec = self.mount(card, inputs, work)
        native, layout = self.settled(card, work)
        tree_reply, snapshot = self.ask("WidgetTreeDump"), self.ask("WidgetSnapshot")
        write(work / "tree.json", tree_reply)
        write(work / "snapshot.json", snapshot)
        mapping = read(inputs / "mapping.json")["elements"]
        queries = {}
        for row in mapping:
            queries[row["native_id"]] = self.ask("WidgetQuery", {
                "build_id": self.build, "query": "id:" + row["native_id"]})
        write(work / "queries.json", queries)
        geometry = evaluate_geometry(card, mapping, native, layout, self.parse_dump(tree_reply["dump"]),
                                     snapshot, queries, self.build, spec["nonce"])
        write(work / "geometry.json", geometry)
        self.screenshot(work, card)
        # A failed geometry comparison is retained; clicks require measured in-bounds Buttons.
        button_ids = {r["source_id"] for r in mapping if r["kind"] == "button"}
        safe = all(not r["issues"] for r in geometry["elements"] if r["source_id"] in button_ids)
        interactions = self.probe_buttons(card, mapping, layout, work) if safe else {
            "passed": False, "buttons": [], "error": "Button geometry failed; actual click probes skipped"}
        write(work / "interactions.json", interactions)
        after = self.ask("WidgetSnapshot")
        write(work / "snapshot-after-probes.json", after)
        before_nodes = {w["id"]: w for w in snapshot["widgets"]}
        after_nodes = {w["id"]: w for w in after["widgets"]}
        fields = ("text", "enabled", "selected", "checked", "value")
        fixture_unchanged = all(all(before_nodes[r["native_id"]].get(k) == after_nodes[r["native_id"]].get(k)
                                   for k in fields) for r in mapping)
        self.guard()
        require(read(work / "native.json")["request"] == spec, "Host request changed during probes")
        return {"id": card["id"], "passed": geometry["passed"] and interactions["passed"] and fixture_unchanged,
                "build_id": self.build, "nonce": spec["nonce"], "viewport_logical": card["artboard"],
                "viewport_px": [round(v * 2) for v in card["artboard"]], "geometry_passed": geometry["passed"],
                "actions_passed": interactions["passed"], "fixture_unchanged": fixture_unchanged,
                "native_nodes": native["nodes"], "controls_tested": len(interactions["buttons"]),
                "errors": geometry["errors"], "scope": SCOPE}


def run(args):
    catalogue = read(CATALOGUE)
    cards = check_inputs(catalogue)
    if args.check_inputs:
        print(json.dumps({"inputs_passed": True, "cards": len(cards), "studio_called": False}))
        return 0
    require(args.build_id is not None, "Supply --build-id '[N]' for the caller-owned Studio host")
    build = [args.build_id] if isinstance(args.build_id, int) else args.build_id
    require(isinstance(build, list) and len(build) == 1 and type(build[0]) is int, "Invalid Studio build ID")
    os.environ["BEAUTY_BRIDGE"] = args.bridge
    sys.path[:0] = [str(PIPELINE), str(PIPELINE.parent)]
    import studio
    from core.gate_structure import parse_dump
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ") + "-" + uuid.uuid4().hex[:8]
    output = ROOT / "evidence/standalone" / stamp
    output.mkdir(parents=True, exist_ok=False)
    write(output / "catalogue.json", catalogue)
    shutil.copy2(ROOT / "runtime/infrastructure.json", output / "infrastructure.json")
    verifier = Verifier(output, build, studio, parse_dump, args.timeout)
    report = {"schema_version": 1, "passed": False, "scope": SCOPE, "build_id": build,
              "bridge": args.bridge, "run_item": studio.RUN_ITEM, "cards": [],
              "full_image_gate": "not performed", "external_service_effects": False}
    source_hashes = {}
    runtime_before = None
    archive = output / "cards"
    archive.mkdir()
    try:
        builds = studio.request("ListBuilds", [], "Builds")
        write(output / "builds.json", builds)
        matching = [b for b in builds["builds"] if b["build_id"] == build]
        require(len(matching) == 1 and matching[0].get("package") == studio.RUN_ITEM
                and matching[0].get("mount") == studio.MOUNT, "Build is not the isolated service-card RunItem")
        for card in cards:
            source = ROOT / card["folder"]
            hashes = manifest(source)
            inputs = output / "inputs" / card["id"]
            shutil.copytree(source, inputs)
            require(manifest(inputs) == hashes == manifest(source), "Source changed while staging " + card["id"])
            source_hashes[card["id"]] = hashes
        runtime_before = runtime_manifest()
        write(output / "runtime-hashes.json", runtime_before)
        write(output / "source-hashes.json", source_hashes)
        # The first mount is a fresh throwaway request, never the previous capture's output paths.
        startup = output / "_runtime/startup"
        verifier.mount(cards[0], output / "inputs" / cards[0]["id"], startup)
        verifier.settled(cards[0], startup)
        for card in cards:
            work = output / "_runtime" / card["id"]
            try:
                result = verifier.capture(card, output / "inputs" / card["id"], work)
            except Exception as error:
                result = {"id": card["id"], "passed": False, "build_id": build,
                          "nonce": verifier.active["nonce"] if verifier.active else None, "error": str(error)}
            # Archive by copying, so even an old native poll cannot rewrite saved evidence.
            destination = archive / card["id"]
            if work.exists():
                shutil.copytree(work, destination)
            else:
                destination.mkdir()
            result["evidence"] = str(destination.relative_to(output))
            write(destination / "result.json", result)
            write(destination / "provenance.json", {"build_id": build, "nonce": result.get("nonce"),
                  "source_sha256": source_hashes[card["id"]], "runtime_hashes_sha256": sha(output / "runtime-hashes.json"),
                  "infrastructure_sha256": sha(output / "infrastructure.json"),
                  "catalogue_sha256": sha(output / "catalogue.json"), "files": manifest(destination), "scope": SCOPE})
            report["cards"].append(result)
            print(json.dumps({"id": card["id"], "passed": result["passed"], "evidence": str(destination)}), flush=True)
            verifier.guard()
        require(runtime_manifest() == runtime_before, "Runtime/binary/infrastructure changed during verification")
        for card in cards:
            require(manifest(ROOT / card["folder"]) == source_hashes[card["id"]], "Export changed during verification")
            require(manifest(output / "inputs" / card["id"]) == source_hashes[card["id"]], "Staged fixture changed")
        require(read(CATALOGUE) == catalogue, "Catalogue changed during verification")
        report["passed"] = len(report["cards"]) == len(cards) and all(r["passed"] for r in report["cards"])
    except Exception as error:
        report["error"] = str(error)
    finally:
        if verifier.active:
            try:
                parking = output / "_runtime/parking"
                verifier.mount(cards[0], output / "inputs" / cards[0]["id"], parking)
                verifier.settled(cards[0], parking)
                report["parking_nonce"] = verifier.active["nonce"]
            except Exception as error:
                report["passed"] = False
                report["parking_error"] = str(error)
        report["completed_at"] = datetime.now(timezone.utc).isoformat()
        write(output / "report.json", report)
        # _runtime remains explicitly mutable. Every other file is an archived, hashed artifact.
        files = {name: digest for name, digest in manifest(output).items()
                 if not name.startswith("_runtime/")}
        write(output / "seal.json", {"schema_version": 1, "files": files,
              "excluded_mutable_directory": "_runtime", "scope": SCOPE})
        write(ROOT / "evidence/standalone-latest.json", {
              "directory": str(output.relative_to(ROOT)), "report_sha256": sha(output / "report.json"),
              "seal_sha256": sha(output / "seal.json"), "passed": report["passed"], "build_id": build,
              "cards": [{**r, "evidence": str((output / r["evidence"]).relative_to(ROOT))}
                        for r in report["cards"]]})
    print(json.dumps({"passed": report["passed"], "report": str(output / "report.json")}), flush=True)
    return 0 if report["passed"] else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-id", type=json.loads, help="Existing isolated Studio build ID, e.g. '[8]'")
    parser.add_argument("--bridge", default=os.environ.get("BEAUTY_BRIDGE", "http://127.0.0.1:8182"))
    parser.add_argument("--timeout", type=float, default=45, help="Seconds to await each native mount")
    parser.add_argument("--check-inputs", action="store_true", help="Only validate exported files; never contact Studio")
    args = parser.parse_args()
    require(args.timeout > 0, "Timeout must be positive")
    if args.check_inputs:
        return run(args)
    lock_path = ROOT / "runtime/standalone-verifier.lock"
    with lock_path.open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError("Another standalone verifier owns the transport")
        return run(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, OSError, ValueError, KeyError) as error:
        print(json.dumps({"passed": False, "error": str(error)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)
