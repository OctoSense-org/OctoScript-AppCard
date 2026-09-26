import sys
from pathlib import Path
import unittest
import json
import tempfile
import uuid
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "runtime"))
from service_session import Session, native_event
from controller import ServiceError, demo_states, reduce, write_json


class NativeAdapterTests(unittest.TestCase):
    def setUp(self):
        self.states, _ = demo_states()
        self.mapping = {"elements": [
            {"source_id": "afternoon", "native_id": "beauty_0_1", "parent": "page"},
            {"source_id": "afternoon_control", "native_id": "beauty_0_1_1", "parent": "afternoon"},
        ]}
        self.controls = {"afternoon": {"event": "installation.choose_slot", "enabled": True}}

    def test_parent_and_native_child_resolve_to_same_action(self):
        for native_id in ("beauty_0_1", "beauty_0_1_1"):
            event = native_event(self.states[6], {"id": native_id, "action": {"kind": "activated"}}, self.mapping, self.controls, native_id)
            self.assertEqual(event["payload"], {"slot_id": "afternoon"})
            self.assertEqual(reduce(self.states[6], event)["installation"]["selected_slot_id"], "afternoon")

    def test_unmapped_native_id_is_rejected(self):
        with self.assertRaises(ServiceError):
            native_event(self.states[6], {"id": "old_frame_button", "action": {"kind": "activated"}}, self.mapping, self.controls, "event")

    def test_non_activation_does_not_submit_a_service_action(self):
        result = native_event(self.states[6], {"id": "beauty_0_1", "action": {"kind": "changed", "value": True}}, self.mapping, self.controls, "event")
        self.assertIsNone(result)

    def test_native_payment_uses_current_invoice_and_scope(self):
        mapping = {"elements": [{"source_id": "pay_materials", "native_id": "beauty_1", "parent": None}]}
        controls = {"pay_materials": {"event": "payment.pay"}}
        event = native_event(self.states[11], {"id": "beauty_1", "action": {"kind": "activated"}}, mapping, controls, "pay-native")
        self.assertEqual(event["actor"], "user")
        self.assertEqual(event["payload"]["amount_minor"], 13000)
        after = reduce(self.states[11], event)
        self.assertEqual(after["payment"]["status"], "paid")

    def fake_prepare(self, state):
        nonce = uuid.uuid4().hex
        path = self.temporary / nonce
        path.mkdir()
        request = {"nonce": nonce, "layout": str(path / "layout.json"), "result": str(path / "native.json"), "actions": str(path / "actions.json")}
        write_json(request["layout"], {"nonce": nonce})
        write_json(request["result"], {"request": request})
        write_json(request["actions"], [])
        write_json(path / "mapping.json", self.mapping)
        write_json(path / "service-actions.json", {"controls": self.controls})
        return {"request": request, "mapping": str(path / "mapping.json"), "service_actions": str(path / "service-actions.json"), "frame_id": 7 if state["installation"]["selected_slot_id"] else 6, "revision": state["revision"], "request_path": str(self.temporary / "current-request.json")}

    def test_watcher_ignores_stale_nonce_then_consumes_current_native_action(self):
        with tempfile.TemporaryDirectory() as temporary:
            self.temporary = Path(temporary)
            session = Session(self.temporary / "session", self.temporary / "current-request.json")
            with patch.object(session, "prepare", side_effect=self.fake_prepare):
                session.start(self.states[6])
                request = session.meta["request"]
                write_json(request["actions"], [{"id": "beauty_0_1", "action": {"kind": "activated"}}])
                write_json(request["layout"], {"nonce": "old-frame"})
                session.poll_native()
                self.assertIsNone(session.state["installation"]["selected_slot_id"])
                self.assertEqual(session.cursor, 0)
                write_json(request["layout"], {"nonce": request["nonce"]})
                session.poll_native()
                self.assertEqual(session.state["installation"]["selected_slot_id"], "afternoon")
                self.assertNotEqual(session.meta["request"]["nonce"], request["nonce"])

    def test_ownership_change_does_not_overwrite_capture_request_or_state(self):
        with tempfile.TemporaryDirectory() as temporary:
            self.temporary = Path(temporary)
            session = Session(self.temporary / "session", self.temporary / "current-request.json")
            with patch.object(session, "prepare", side_effect=self.fake_prepare):
                session.start(self.states[6])
                capture_request = {"nonce": "other-capture"}
                write_json(session.request_path, capture_request)
                with self.assertRaisesRegex(ServiceError, "归属"):
                    session.dispatch({"id": "event", "action": "installation.choose_slot", "actor": "user", "payload": {"slot_id": "afternoon"}})
                self.assertIsNone(session.state["installation"]["selected_slot_id"])
                self.assertEqual(json.loads(session.request_path.read_text()), capture_request)


if __name__ == "__main__":
    unittest.main()
