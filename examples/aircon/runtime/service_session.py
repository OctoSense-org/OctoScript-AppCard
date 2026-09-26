#!/usr/bin/env python3
"""Bridge native Makepad KitAction events to the local service reducer.

Starting a session explicitly mounts a request in the isolated Studio host.
Per-frame capture and this watcher must never own that host simultaneously.
"""

import argparse
import fcntl
import importlib.util
import json
from pathlib import Path
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "service"))
from controller import ServiceError, demo_states, initial_state, reduce, view_model, write_json

DEFAULT_REQUEST = ROOT.parents[1] / "lab/image-to-appcard/current-request.json"
ROUTE_ALIASES = {
    "navigation.order": ("shopping", "order"),
    "navigation.logistics": ("logistics", "detail"),
    "navigation.support": ("shopping", "support"),
    "navigation.courier": ("logistics", "contact"),
    "navigation.delivery_time": ("logistics", "delivery-time"),
    "navigation.technician": ("installation", "contact"),
    "navigation.booking": ("installation", "booking"),
    "navigation.service_order": ("installation", "service-order"),
    "navigation.service_feedback": ("installation", "feedback"),
    "navigation.payment_receipt": ("payment", "receipt"),
}


def read(path):
    return json.loads(Path(path).read_text())


def native_event(state, native_action, mapping, controls, event_id):
    """Resolve an observed native component id to its owned service action."""
    if native_action.get("action", {}).get("kind") != "activated":
        return None
    entries = mapping["elements"]
    entry = next((item for item in entries if item["native_id"] == native_action.get("id")), None)
    if entry is None:
        raise ServiceError("原生动作 id 不属于当前组件映射")
    by_source = {item["source_id"]: item for item in entries}
    source = entry["source_id"]
    while source not in controls:
        parent = by_source.get(source, {}).get("parent")
        if not parent:
            raise ServiceError("该原生组件没有服务动作绑定: " + source)
        source = parent
    control = controls[source]
    action = control["event"]
    payload = dict(control.get("payload", {}))
    if action == "shopping.buy":
        action = "order.purchase_demo"
    elif action in ROUTE_ALIASES:
        app, page = ROUTE_ALIASES[action]
        action, payload = "navigation.open_app", {"app": app, "page": page}
    elif action == "installation.choose_day" and not payload:
        payload = {"date": "2026-09-20" if source == "sunday" else "2026-09-19"}
    elif action == "installation.choose_slot" and not payload:
        payload = {"slot_id": "morning" if source == "conflict_slot" else "afternoon"}
    elif action == "payment.pay" and not payload:
        payload = {"invoice_id": state["payment"]["id"], "amount_minor": state["fixture"]["payment"]["amount_minor"], "currency": state["fixture"]["payment"]["currency"]}
    elif action == "card.dismiss" and not payload:
        visible = view_model(state)["cards"]
        if not visible:
            raise ServiceError("当前没有可收起卡片")
        payload = {"card_id": visible[0]["id"]}
    return {"id": event_id, "action": action, "actor": "user", "payload": payload}


class Session:
    def __init__(self, directory, request_path=DEFAULT_REQUEST, build_id=None):
        self.directory = Path(directory).resolve()
        self.request_path = Path(request_path).resolve()
        self.build_id = build_id
        self.state = None
        self.meta = None
        self.cursor = 0

    def log(self, kind, **details):
        self.directory.mkdir(parents=True, exist_ok=True)
        with (self.directory / "events.jsonl").open("a") as handle:
            handle.write(json.dumps({"time": time.time(), "kind": kind, **details}, ensure_ascii=False) + "\n")

    def prepare(self, state):
        view = view_model(state)
        nonce = "service-" + uuid.uuid4().hex
        output = self.directory / "mounts" / nonce
        output.mkdir(parents=True)
        hook = ROOT / "runtime/render_runtime.py"
        if hook.exists():
            spec = importlib.util.spec_from_file_location("service_render_runtime", hook)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            rendered = module.render_runtime(state, view, output)
        else:
            frame = ROOT / "cards" / f"aircon-{view['frame_id']:02d}"
            rendered = {"card": str(frame / "page.card"), "data": str(frame / "page.data.json"),
                        "kit_dir": str(frame / "kit"), "mapping": str(frame / "mapping.json"),
                        "service_actions": str(frame / "service-actions.json"), "semantic": str(frame / "semantic-map.json")}
        required = ("card", "data", "kit_dir", "mapping", "service_actions")
        for key in required:
            if key not in rendered or not Path(rendered[key]).exists():
                raise ServiceError("原生渲染产物缺失: " + key)
        request = {key: str(rendered[key]) for key in ("card", "data", "kit_dir")}
        request.update(format="l0-kit", width=406, height=776, nonce=nonce,
                       result=str(output / "native.json"), layout=str(output / "layout.json"),
                       actions=str(output / "actions.json"), semantic_result=str(output / "semantic-state.json"),
                       semantic_probe=str(output / "semantic-probe.json"))
        if rendered.get("semantic"):
            request["semantic"] = str(rendered["semantic"])
        if self.build_id is not None:
            request["build_id"] = self.build_id
        meta = {"schema_version": 1, "request": request, "mapping": str(rendered["mapping"]),
                "service_actions": str(rendered["service_actions"]), "revision": state["revision"],
                "frame_id": view["frame_id"], "request_path": str(self.request_path), "native_action_cursor": 0}
        write_json(output / "request.json", request)
        write_json(output / "state.json", state)
        write_json(output / "view.json", view)
        return meta

    def publish(self, state, meta):
        if self.meta is not None and not self.owns_request():
            raise ServiceError("原生请求归属已变化，未覆盖其他任务的请求")
        write_json(self.directory / "state.json", state)
        write_json(self.directory / "view.json", view_model(state))
        write_json(self.directory / "session.json", meta)
        write_json(self.request_path, meta["request"])
        self.state, self.meta, self.cursor = state, meta, 0
        self.log("mounted", frame_id=meta["frame_id"], revision=state["revision"], nonce=meta["request"]["nonce"])

    def start(self, state):
        self.publish(state, self.prepare(state))

    def resume(self):
        self.state = read(self.directory / "state.json")
        self.meta = read(self.directory / "session.json")
        self.request_path = Path(self.meta["request_path"])
        self.build_id = self.meta["request"].get("build_id")
        self.cursor = self.meta.get("native_action_cursor", 0)

    def owns_request(self):
        try:
            return read(self.request_path).get("nonce") == self.meta["request"]["nonce"]
        except (OSError, ValueError):
            return False

    def dispatch(self, event, source="inbox"):
        candidate = reduce(self.state, event)
        if candidate == self.state:
            self.log("duplicate_event", event_id=event["id"], source=source)
            return False
        meta = self.prepare(candidate)
        self.publish(candidate, meta)
        self.log("applied", event=event, source=source, frame_id=meta["frame_id"], revision=candidate["revision"])
        return True

    def poll_native(self):
        request = self.meta["request"]
        try:
            layout, native = read(request["layout"]), read(request["result"])
            if layout.get("nonce") != request["nonce"] or native.get("request", {}).get("nonce") != request["nonce"]:
                return
            if self.build_id is not None and native.get("request", {}).get("build_id") != self.build_id:
                return
            actions = read(request["actions"])
        except (OSError, ValueError):
            return
        if not isinstance(actions, list):
            self.log("invalid_native_log", nonce=request["nonce"])
            return
        mapping = read(self.meta["mapping"])
        controls = read(self.meta["service_actions"])["controls"]
        while self.cursor < len(actions):
            index = self.cursor
            self.cursor += 1
            self.meta["native_action_cursor"] = self.cursor
            write_json(self.directory / "session.json", self.meta)
            try:
                event = native_event(self.state, actions[index], mapping, controls, request["nonce"] + ":" + str(index))
                if event and self.dispatch(event, source="native"):
                    return  # Ignore remaining events from the replaced mount.
            except (ServiceError, OSError, ValueError) as error:
                self.log("rejected_native", native_action=actions[index], error=str(error), nonce=request["nonce"])

    def poll_inbox(self):
        inbox = self.directory / "inbox"
        inbox.mkdir(parents=True, exist_ok=True)
        processed = self.directory / "processed"
        processed.mkdir(exist_ok=True)
        for path in sorted(inbox.glob("*.json")):
            try:
                event = read(path)
                self.dispatch(event)
                result = {"ok": True, "event_id": event["id"], "revision": self.state["revision"]}
            except (ServiceError, OSError, ValueError, KeyError) as error:
                result = {"ok": False, "error": str(error)}
                self.log("rejected_inbox", file=path.name, error=str(error))
            write_json(processed / (path.stem + ".result.json"), result)
            path.replace(processed / path.name)

    def watch(self):
        self.log("watching")
        while True:
            if not self.owns_request():
                self.log("ownership_lost", message="Another native capture/session mounted a new request; watcher stopped")
                raise ServiceError("当前原生请求已被其他任务替换，服务 watcher 已停止")
            self.poll_inbox()
            self.poll_native()
            time.sleep(0.1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session-dir", default=str(ROOT / "runtime/session"))
    commands = parser.add_subparsers(dest="command", required=True)
    start = commands.add_parser("start")
    start.add_argument("--frame", type=int, choices=range(1, 13), default=1)
    start.add_argument("--state")
    start.add_argument("--request", default=str(DEFAULT_REQUEST))
    start.add_argument("--build-id", type=json.loads, help='Studio build ID as JSON, for example [8]')
    start.add_argument("--once", action="store_true", help="Mount only; resume with watch")
    commands.add_parser("watch")
    commands.add_parser("status")
    dispatch = commands.add_parser("dispatch")
    dispatch.add_argument("--event", required=True, help="JSON string, file, or - for stdin; queues to watcher")
    args = parser.parse_args()
    directory = Path(args.session_dir).resolve()
    directory.mkdir(parents=True, exist_ok=True)
    try:
        if args.command == "dispatch":
            text = sys.stdin.read() if args.event == "-" else args.event if args.event.lstrip().startswith("{") else Path(args.event).read_text()
            event = json.loads(text)
            destination = directory / "inbox" / (str(time.time_ns()) + "-" + uuid.uuid4().hex + ".json")
            write_json(destination, event)
            print(json.dumps({"queued": str(destination)}, ensure_ascii=False))
            return 0
        if args.command == "status":
            write_json(None, {"session": read(directory / "session.json"), "view": read(directory / "view.json")})
            return 0
        with (directory / "watcher.lock").open("w") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise ServiceError("该 session 已有运行中的 watcher")
            session = Session(directory)
            if args.command == "start":
                session.request_path = Path(args.request).resolve()
                session.build_id = [args.build_id] if isinstance(args.build_id, int) else args.build_id
                state = read(args.state) if args.state else demo_states()[0][args.frame]
                session.start(state)
                print(json.dumps({"mounted": session.meta["request"]["nonce"], "frame_id": session.meta["frame_id"]}), flush=True)
                if args.once:
                    return 0
            else:
                session.resume()
            session.watch()
    except KeyboardInterrupt:
        return 0
    except (ServiceError, ValueError, OSError, KeyError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
