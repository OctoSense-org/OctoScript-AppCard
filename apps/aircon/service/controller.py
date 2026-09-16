#!/usr/bin/env python3
"""Local deterministic service state for native App Cards; no network or payment API."""

import argparse
import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
PROVIDER_ACTIONS = {
    "logistics.out_for_delivery", "logistics.delivered",
    "installation.technician_departed", "installation.completed",
}
USER_ACTIONS = {
    "order.purchase_demo", "navigation.open_app", "navigation.desktop", "card.dismiss",
    "installation.open_slots", "installation.choose_slot", "installation.close_slots",
    "installation.defer", "installation.confirm", "installation.choose_day",
    "installation.reschedule", "installation.cancel", "calendar.acknowledge",
    "calendar.undo", "calendar.restore", "payment.pay", "payment.cancel", "payment.reopen",
}


class ServiceError(ValueError):
    """Rejected action: caller keeps the existing state and displays this reason."""


def initial_state(fixture=None):
    fixture = copy.deepcopy(fixture or json.loads((ROOT / "fixture.json").read_text()))
    return {
        "schema_version": 1, "scenario": fixture["scenario"], "simulation": True,
        "revision": 0, "fixture": fixture, "processed_events": {}, "effects": [],
        "ui": {"surface": "app", "app": "shopping", "page": "product", "slot_picker": False, "installation_deferred": False, "dismissed_cards": []},
        "order": {"id": fixture["order"]["id"], "status": "not_placed"},
        "delivery": {"id": fixture["delivery"]["id"], "status": "not_dispatched"},
        "installation": {"id": fixture["installation"]["id"], "status": "not_available", "selected_slot_id": None, "booked_slot_id": None, "selected_day": fixture["installation"]["days"][0]["date"], "booked_day": None, "version": 0},
        "calendar": {"events": {item["id"]: item for item in fixture["calendar"]["existing_events"]}, "installation_sync": "not_added", "acknowledged": False},
        "payment": {"id": fixture["payment"]["id"], "status": "not_due", "receipt": None},
    }


def require(condition, reason):
    if not condition:
        raise ServiceError(reason)


def _slot(state, slot_id, day=None):
    slot = next((s for s in state["fixture"]["installation"]["slots"] if s["id"] == slot_id), None)
    if slot is None:
        return None
    day = day or state["installation"]["selected_day"]
    return {**slot, "starts_at": day + slot["starts_at"][10:], "ends_at": day + slot["ends_at"][10:]}


def available_slots(state):
    """Derive conflicts from shared calendar data, not a hard-coded disabled index."""
    own_event = state["fixture"]["calendar"]["installation_event_id"]
    result = []
    for base_slot in state["fixture"]["installation"]["slots"]:
        slot = _slot(state, base_slot["id"])
        a, b = datetime.fromisoformat(slot["starts_at"]), datetime.fromisoformat(slot["ends_at"])
        conflicts = [event for event in state["calendar"]["events"].values()
                     if event["id"] != own_event
                     and a < datetime.fromisoformat(event["ends_at"])
                     and datetime.fromisoformat(event["starts_at"]) < b]
        result.append({**slot, "enabled": not conflicts,
                       "conflict_event_ids": [event["id"] for event in conflicts],
                       "reason": "、".join(event["title"] for event in conflicts),
                       "selected": slot["id"] == state["installation"]["selected_slot_id"]})
    return result


def _effect(state, kind, entity_id, **detail):
    state["effects"].append({"kind": kind, "entity_id": entity_id, "simulation": True, **detail})


def _calendar_upsert(state):
    booking = state["installation"]
    slot = _slot(state, booking["booked_slot_id"], booking["booked_day"])
    event_id = state["fixture"]["calendar"]["installation_event_id"]
    event = {"id": event_id, "title": "空调上门安装", "starts_at": slot["starts_at"],
             "ends_at": slot["ends_at"], "source_app": "installation",
             "source_entity_id": booking["id"], "booking_version": booking["version"]}
    if state["calendar"]["events"].get(event_id) != event:
        state["calendar"]["events"][event_id] = event
        _effect(state, "calendar.upsert", event_id)
    state["calendar"]["installation_sync"] = "added"


def reduce(state, event):
    """Apply one {id, action, actor, payload?} event without mutating the input.

    actor is a local validation boundary, not authentication. A production adapter
    must authenticate provider messages and user actions before calling this API.
    """
    require(isinstance(event, dict), "事件必须是 JSON 对象")
    message_id, action, actor = event.get("id"), event.get("action"), event.get("actor")
    payload = event.get("payload", {})
    require(isinstance(message_id, str) and bool(message_id), "事件需要唯一 id")
    require(isinstance(action, str) and action in USER_ACTIONS | PROVIDER_ACTIONS, "未知操作")
    require(isinstance(payload, dict), "payload 必须是 JSON 对象")
    required_actor = "provider" if action in PROVIDER_ACTIONS else "user"
    require(actor == required_actor, "操作来源不匹配")
    canonical = json.dumps(event, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode()).hexdigest()
    seen = state["processed_events"].get(message_id)
    if seen:
        require(seen == digest, "同一事件 id 不得复用于不同内容")
        return copy.deepcopy(state)
    out = copy.deepcopy(state)
    order, delivery, booking = out["order"], out["delivery"], out["installation"]
    calendar, payment, ui = out["calendar"], out["payment"], out["ui"]
    fixture = out["fixture"]

    if action == "order.purchase_demo":
        if order["status"] == "not_placed":
            order["status"] = "paid_demo"
            _effect(out, "order.create_demo", order["id"], amount_minor=fixture["order"]["amount_minor"])
        ui.update(surface="app", app="shopping", page="order", slot_picker=False)
    elif action == "navigation.open_app":
        app = payload.get("app")
        require(app in {"shopping", "logistics", "installation", "calendar", "payment"}, "未知应用")
        page = payload.get("page", "product" if app == "shopping" and order["status"] == "not_placed" else "detail")
        if app == "shopping" and page != "product":
            require(order["status"] != "not_placed", "订单尚未创建")
            if page == "detail":
                page = "order"
        ui.update(surface="app", app=app, page=page, slot_picker=False)
    elif action == "navigation.desktop":
        require(order["status"] != "not_placed", "请先创建演示订单")
        ui.update(surface="desktop", app=None, page=None, slot_picker=False)
    elif action == "card.dismiss":
        card_id = payload.get("card_id")
        require(card_id in {card["id"] for card in view_model(out)["cards"]} or card_id in ui["dismissed_cards"], "该卡片当前不可见")
        if card_id not in ui["dismissed_cards"]:
            ui["dismissed_cards"].append(card_id)
    elif action == "logistics.out_for_delivery":
        require(order["status"] != "not_placed", "订单尚未创建")
        if delivery["status"] == "not_dispatched":
            delivery["status"] = "out_for_delivery"
            _effect(out, "logistics.update", delivery["id"], status=delivery["status"])
    elif action == "logistics.delivered":
        require(order["status"] != "not_placed", "订单尚未创建")
        if delivery["status"] != "delivered":
            delivery.update(status="delivered", delivered_at=fixture["delivery"]["delivered_at"])
            booking["status"] = "available"
            _effect(out, "logistics.update", delivery["id"], status="delivered")
    elif action in {"installation.open_slots", "installation.reschedule"}:
        require(booking["status"] in {"available", "booked", "cancelled"}, "当前不可选择安装时段")
        ui["slot_picker"] = True
        ui["installation_deferred"] = False
        booking["selected_slot_id"] = booking["booked_slot_id"]
        booking["selected_day"] = booking["booked_day"] or fixture["installation"]["days"][0]["date"]
    elif action == "installation.choose_day":
        require(ui["slot_picker"], "请先展开安装时段")
        day = payload.get("date")
        require(day in {item["date"] for item in fixture["installation"]["days"]}, "该日期暂无服务时段")
        if day != booking["selected_day"]:
            booking["selected_day"] = day
            booking["selected_slot_id"] = None
    elif action == "installation.choose_slot":
        require(ui["slot_picker"], "请先展开安装时段")
        candidate = next((s for s in available_slots(out) if s["id"] == payload.get("slot_id")), None)
        require(candidate is not None, "未知安装时段")
        require(candidate["enabled"], "该时段与日历中的" + candidate["reason"] + "冲突")
        booking["selected_slot_id"] = candidate["id"]
    elif action in {"installation.close_slots", "installation.defer"}:
        ui["slot_picker"] = False
        booking["selected_slot_id"] = booking["booked_slot_id"]
        booking["selected_day"] = booking["booked_day"] or fixture["installation"]["days"][0]["date"]
        if action == "installation.defer":
            ui["installation_deferred"] = True
    elif action == "installation.confirm":
        require(booking["status"] in {"available", "booked", "cancelled"}, "当前不可确认安装预约")
        selected = booking["selected_slot_id"]
        candidate = next((s for s in available_slots(out) if s["id"] == selected), None)
        require(candidate is not None, "请选择安装时段")
        require(candidate["enabled"], "所选时段已产生冲突，请重新选择")
        changed = booking["status"] != "booked" or booking["booked_slot_id"] != selected or booking["booked_day"] != booking["selected_day"]
        if changed:
            booking.update(status="booked", booked_slot_id=selected, booked_day=booking["selected_day"], version=booking["version"] + 1)
            _effect(out, "installation.upsert", booking["id"], slot_id=selected, version=booking["version"])
            if fixture["authorizations"]["calendar_sync_from_confirmed_installation"]:
                _calendar_upsert(out)
                calendar["acknowledged"] = False
        ui["slot_picker"] = False
    elif action == "installation.cancel":
        require(booking["status"] in {"booked", "cancelled"}, "当前阶段不可直接取消安装预约")
        if booking["status"] == "booked":
            booking.update(status="cancelled", selected_slot_id=None, booked_slot_id=None, booked_day=None)
            _effect(out, "installation.cancel", booking["id"])
            calendar_event_id = fixture["calendar"]["installation_event_id"]
            if calendar["events"].pop(calendar_event_id, None) is not None:
                _effect(out, "calendar.remove", calendar_event_id)
            calendar.update(installation_sync="cancelled_with_booking", acknowledged=False)
        ui["slot_picker"] = False
    elif action == "calendar.acknowledge":
        require(calendar["installation_sync"] == "added", "没有可确认的日历更新")
        calendar["acknowledged"] = True
    elif action == "calendar.undo":
        require(calendar["installation_sync"] in {"added", "undone"}, "尚无可撤销的安装日程")
        calendar_event_id = fixture["calendar"]["installation_event_id"]
        if calendar["events"].pop(calendar_event_id, None) is not None:
            _effect(out, "calendar.remove", calendar_event_id)
        calendar.update(installation_sync="undone", acknowledged=False)
    elif action == "calendar.restore":
        require(booking["booked_slot_id"] is not None, "尚无安装预约可关联")
        _calendar_upsert(out)
    elif action == "installation.technician_departed":
        require(booking["status"] in {"booked", "en_route", "completed"}, "师傅出发前需要有效预约")
        if booking["status"] == "booked":
            booking["status"] = "en_route"
            _effect(out, "installation.progress", booking["id"], status="en_route")
    elif action == "installation.completed":
        require(booking["status"] in {"booked", "en_route", "completed"}, "安装尚未预约")
        if booking["status"] != "completed":
            booking["status"] = "completed"
            payment["status"] = "pending"
            _effect(out, "installation.progress", booking["id"], status="completed")
            _effect(out, "payment.invoice_created", payment["id"], amount_minor=fixture["payment"]["amount_minor"])
    elif action == "payment.pay":
        require(payment["status"] in {"pending", "paid"}, "当前没有待支付请求")
        require(payload.get("invoice_id") == payment["id"], "支付单号不匹配")
        require(payload.get("amount_minor") == fixture["payment"]["amount_minor"], "支付金额已变化，请重新确认")
        require(payload.get("currency") == fixture["payment"]["currency"], "支付币种不匹配")
        if payment["status"] == "pending":
            receipt = {"id": "receipt-" + payment["id"], "amount_minor": payload["amount_minor"], "currency": payload["currency"], "payee": fixture["payment"]["payee"], "simulation": True}
            payment.update(status="paid", receipt=receipt)
            _effect(out, "payment.capture_demo", payment["id"], receipt_id=receipt["id"], amount_minor=receipt["amount_minor"])
    elif action == "payment.cancel":
        require(payment["status"] in {"pending", "cancelled"}, "只能撤销待支付请求；已付款不在此操作中退款")
        if payment["status"] == "pending":
            payment["status"] = "cancelled"
            _effect(out, "payment.request_cancelled", payment["id"])
    elif action == "payment.reopen":
        require(payment["status"] in {"cancelled", "pending"}, "该支付请求不可重新打开")
        payment["status"] = "pending"

    out["revision"] += 1
    out["processed_events"][message_id] = digest
    return out


def _action(action, label, payload=None, enabled=True):
    return {"action": action, "label": label, "actor": "user", "enabled": enabled, "payload": payload or {}}


def frame_id(state):
    ui, booking, payment = state["ui"], state["installation"], state["payment"]
    if ui["surface"] == "app" and ui["app"] == "shopping":
        return 1 if ui["page"] == "product" else 2
    if ui["slot_picker"]:
        return 7 if booking["selected_slot_id"] else 6
    if payment["status"] == "paid":
        return 12
    if payment["status"] in {"pending", "cancelled"}:
        return 11
    if booking["status"] == "en_route":
        return 10
    if booking["status"] == "booked":
        return 9 if state["calendar"]["installation_sync"] == "undone" else 8
    if state["delivery"]["status"] == "delivered" and not ui.get("installation_deferred"):
        return 5
    return 4 if state["delivery"]["status"] == "out_for_delivery" else 3


def view_model(state):
    """Semantic data for native controls; no image hotspots or screenshot rendering."""
    fixture, booking, calendar, payment = state["fixture"], state["installation"], state["calendar"], state["payment"]
    frame = frame_id(state)
    cards = []
    def card(owner, entity_id, title, data, actions):
        cards.append({"id": owner + ":" + entity_id, "owner_app": owner, "entity_id": entity_id,
                      "title": title, "body_action": _action("navigation.open_app", "打开应用", {"app": owner}),
                      "data": data, "actions": actions})
    if frame == 3:
        actions = [_action("navigation.open_app", "查看订单", {"app": "shopping"})]
        if booking["status"] in {"available", "cancelled"}:
            actions.append(_action("installation.open_slots", "预约安装"))
        card("shopping", state["order"]["id"], "空调已下单", {**fixture["order"], **state["order"]}, actions)
    elif frame == 4:
        card("logistics", state["delivery"]["id"], "空调今天送达", {**fixture["delivery"], **state["delivery"]}, [])
    elif frame in {5, 6, 7}:
        actions = [_action("installation.open_slots", "选择时间"), _action("installation.defer", "暂不预约")]
        if frame in {6, 7}:
            actions = [_action("installation.choose_day", day["label"], {"date": day["date"]}) for day in fixture["installation"]["days"]]
            actions += [_action("installation.choose_slot", slot["label"], {"slot_id": slot["id"]}, slot["enabled"]) for slot in available_slots(state)]
            actions += [_action("installation.close_slots", "取消"), _action("installation.confirm", "确认预约", enabled=any(s["selected"] and s["enabled"] for s in available_slots(state)))]
        title = "选择安装时间" if frame in {6, 7} else "安装预约已取消" if booking["status"] == "cancelled" else "空调已送达，预约安装吧"
        card("installation", booking["id"], title, {**fixture["installation"], **booking, "slots": available_slots(state)}, actions)
    elif frame in {8, 9, 10}:
        card("installation", booking["id"], "师傅即将到达" if frame == 10 else "安装预约已确认", {**fixture["installation"], **booking, "slot": _slot(state, booking["booked_slot_id"], booking["booked_day"])}, [_action("installation.reschedule", "改约"), _action("installation.cancel", "取消预约")] if frame != 10 else [])
        if frame != 10:
            actions = [_action("calendar.restore", "重新加入日历")] if calendar["installation_sync"] == "undone" else [_action("calendar.acknowledge", "已确认" if calendar["acknowledged"] else "确认", enabled=not calendar["acknowledged"]), _action("calendar.undo", "撤销日程")]
            card("calendar", fixture["calendar"]["installation_event_id"], "日程已撤销，安装预约仍有效" if frame == 9 else "日历已经更新", {"status": calendar["installation_sync"], "event": calendar["events"].get(fixture["calendar"]["installation_event_id"]), "booking_still_valid": True}, actions)
    elif frame in {11, 12}:
        actions = []
        if payment["status"] == "pending":
            actions = [_action("payment.pay", "支付 ¥130", {"invoice_id": payment["id"], "amount_minor": fixture["payment"]["amount_minor"], "currency": "CNY"}), _action("payment.cancel", "撤销支付")]
        elif payment["status"] == "cancelled":
            actions = [_action("payment.reopen", "重新打开支付请求")]
        title = {"paid": "付款完成", "pending": "安装材料费待支付", "cancelled": "待支付请求已撤销"}[payment["status"]]
        card("payment", payment["id"], title, {**fixture["payment"], **payment}, actions)
        if frame == 12:
            card("installation", booking["id"], "安装服务已完成", {**fixture["installation"], **booking}, [])
    return {"schema_version": 1, "simulation": True, "revision": state["revision"], "frame_id": frame,
            "surface": state["ui"]["surface"], "app_route": {"app": state["ui"]["app"], "page": state["ui"]["page"]} if state["ui"]["surface"] == "app" else None,
            "cards": [card for card in cards if card["id"] not in state["ui"].get("dismissed_cards", [])], "slots": available_slots(state), "order": {**fixture["order"], **state["order"]},
            "bindings": {"selected_slot_id": booking["selected_slot_id"], "booking_status": booking["status"], "calendar_status": calendar["installation_sync"], "payment_status": payment["status"], "can_confirm_booking": bool(booking["selected_slot_id"]) and any(s["selected"] and s["enabled"] for s in available_slots(state)), "can_pay": payment["status"] == "pending"}}


def demo_states():
    state = initial_state()
    states = {1: copy.deepcopy(state)}
    steps = [
        (2, "order.purchase_demo", {}), (3, "navigation.desktop", {}),
        (4, "logistics.out_for_delivery", {}), (5, "logistics.delivered", {}),
        (6, "installation.open_slots", {}), (7, "installation.choose_slot", {"slot_id": "afternoon"}),
        (8, "installation.confirm", {}), (9, "calendar.undo", {}),
        (8, "calendar.restore", {}), (10, "installation.technician_departed", {}),
        (11, "installation.completed", {}),
        (12, "payment.pay", {"invoice_id": state["payment"]["id"], "amount_minor": 13000, "currency": "CNY"}),
    ]
    events = []
    for index, (frame, action, payload) in enumerate(steps, 1):
        event = {"id": "demo-" + str(index), "action": action, "actor": "provider" if action in PROVIDER_ACTIONS else "user", "payload": payload}
        state = reduce(state, event)
        events.append(event)
        states.setdefault(frame, copy.deepcopy(state))
    return states, events


def write_json(path, value):
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    if not path or path == "-":
        print(text, end="")
        return
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=target.parent, delete=False) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    temporary.replace(target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init")
    init.add_argument("--output")
    for name in ("view", "dispatch"):
        command = commands.add_parser(name)
        command.add_argument("--state", required=True)
        command.add_argument("--output")
        if name == "dispatch":
            command.add_argument("--event", required=True, help="JSON string, JSON file, or - for stdin")
    demo = commands.add_parser("demo")
    demo.add_argument("--output-dir", default=str(ROOT / "fixtures"))
    args = parser.parse_args()
    try:
        if args.command == "init":
            write_json(args.output, initial_state())
        elif args.command == "demo":
            states, events = demo_states()
            directory = Path(args.output_dir)
            for frame, state in sorted(states.items()):
                write_json(directory / f"{frame:02d}.state.json", state)
                write_json(directory / f"{frame:02d}.view.json", view_model(state))
            write_json(directory / "events.json", events)
        else:
            state = json.loads(Path(args.state).read_text())
            if args.command == "view":
                write_json(args.output, view_model(state))
            else:
                event_text = sys.stdin.read() if args.event == "-" else args.event if args.event.lstrip().startswith("{") else Path(args.event).read_text()
                write_json(args.output, reduce(state, json.loads(event_text)))
    except (ServiceError, ValueError, OSError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
