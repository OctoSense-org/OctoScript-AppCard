import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))
from render_runtime import render_runtime
from controller import demo_states, reduce, view_model


class RuntimeBindingTests(unittest.TestCase):
    def setUp(self):
        self.states, _ = demo_states()
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)

    def render(self, state, name="fixture"):
        output = Path(self.temporary.name) / name
        result = render_runtime(state, view_model(state), output)
        files = {key: json.loads(Path(result[key]).read_text()) for key in ("mapping", "service_actions", "data")}
        files["kit"] = json.loads((Path(result["kit_dir"]) / "native/light/kit.json").read_text())
        files["card"] = Path(result["card"]).read_text()
        files["output"] = output
        return files

    def event(self, state, action, payload=None):
        return reduce(state, {"id": "render-" + action + "-" + str(state["revision"]), "action": action, "actor": "user", "payload": payload or {}})

    def text(self, files, source_id):
        return next(n["text"] for n in files["mapping"]["elements"] if n["source_id"] == source_id)

    def assert_component_integrity(self, files):
        placements = files["data"]["$kit"]["placements"]
        definitions = set(re.findall(r"^component ([A-Za-z0-9_]+)\(", files["card"], re.M))
        for node in files["mapping"]["elements"]:
            source = node["source_id"]
            component = placements[source]["component"]
            self.assertEqual(node["component"], component, source)
            self.assertIn(component, definitions, source)
            self.assertIn(component, files["kit"]["components"], source)
            self.assertIn(component + '(instance: "' + source + '"', files["card"], source)

    def test_all_twelve_frames_render_with_matching_native_bindings(self):
        for frame, state in self.states.items():
            source = ROOT / "cards" / f"aircon-{frame:02d}" / "page.card"
            before = hashlib.sha256(source.read_bytes()).hexdigest()
            files = self.render(state, f"frame-{frame:02d}")
            self.assert_component_integrity(files)
            self.assertEqual(before, hashlib.sha256(source.read_bytes()).hexdigest())

    def test_sunday_clears_selection_and_enables_native_morning_control(self):
        state = self.event(self.states[7], "installation.choose_day", {"date": "2026-09-20"})
        files = self.render(state)
        self.assertIn("state conflict_slot_control_enabled { shape: bool, initial: true }", files["card"])
        self.assertIn("state confirm_booking_control_enabled { shape: bool, initial: false }", files["card"])
        self.assertEqual(self.text(files, "text_72"), "日历空闲")
        self.assertEqual(self.text(files, "text_76"), "请选择安装时段")
        self.assert_component_integrity(files)

    def test_sunday_morning_booking_updates_date_and_time_in_both_cards(self):
        state = self.event(self.states[7], "installation.choose_day", {"date": "2026-09-20"})
        state = self.event(state, "installation.choose_slot", {"slot_id": "morning"})
        state = self.event(state, "installation.confirm")
        files = self.render(state)
        self.assertIn("9月20日", self.text(files, "text_180"))
        self.assertIn("09:00–11:00", self.text(files, "text_180"))
        self.assertIn("09:00–11:00", self.text(files, "text_186"))

    def test_cancelled_payment_updates_native_copy_and_action_not_service_status(self):
        state = self.event(self.states[11], "payment.cancel")
        files = self.render(state)
        self.assertEqual(self.text(files, "text_141"), "支付 · 请求已撤销")
        self.assertEqual(self.text(files, "text_142"), "材料费尚未支付")
        self.assertEqual(files["service_actions"]["controls"]["pay_materials"]["event"], "payment.reopen")
        self.assertIn("state withdraw_payment_request_control_enabled { shape: bool, initial: false }", files["card"])
        self.assertEqual(self.text(files, "text_150"), "安装服务 · 安装已完成")
        self.assert_component_integrity(files)

    def test_calendar_acknowledgement_only_changes_its_native_control(self):
        state = self.event(self.states[8], "calendar.acknowledge")
        files = self.render(state)
        self.assertEqual(self.text(files, "text_188"), "已确认")
        self.assertIn("state acknowledge_calendar_control_enabled { shape: bool, initial: false }", files["card"])
        self.assertTrue(files["service_actions"]["controls"]["undo_calendar"]["enabled"])
        self.assertEqual(state["installation"], self.states[8]["installation"])
        self.assert_component_integrity(files)

    def test_dismissed_order_card_is_removed_from_native_tree(self):
        state = self.event(self.states[3], "card.dismiss", {"card_id": "shopping:order-aircon-001"})
        files = self.render(state)
        self.assertNotIn('instance: "order_card"', files["card"])
        self.assertNotIn("order_card", files["data"]["$kit"]["placements"])
        self.assertEqual(files["service_actions"]["controls"], {})
        self.assert_component_integrity(files)

    def test_internal_route_preview_is_visible_and_has_native_back_action(self):
        state = self.event(self.states[10], "navigation.open_app", {"app": "installation", "page": "contact"})
        files = self.render(state)
        self.assertEqual(self.text(files, "text_84"), "安装服务")
        self.assertEqual(self.text(files, "text_85"), "联系服务")
        self.assertEqual(files["service_actions"]["controls"]["contact_technician"]["event"], "navigation.desktop")
        route = json.loads((files["output"] / "route-preview.json").read_text())
        self.assertFalse(route["external_app_launched"])
        self.assert_component_integrity(files)

    def test_letterboxed_payment_receipt_has_two_separate_native_headings(self):
        state = self.event(self.states[12], "navigation.open_app", {"app": "payment", "page": "receipt"})
        files = self.render(state)
        self.assertEqual(self.text(files, "text_195"), "支付应用")
        self.assertEqual(self.text(files, "text_196"), "付款凭证")
        placements = files["data"]["$kit"]["placements"]
        title = placements["text_195"]["layout"]
        subtitle = placements["text_196"]["layout"]
        self.assertLessEqual(title["y"] + title["h"], subtitle["y"])
        self.assert_component_integrity(files)


if __name__ == "__main__":
    unittest.main()
