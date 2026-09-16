import copy
import unittest

from controller import ServiceError, available_slots, demo_states, initial_state, reduce, view_model


class ServiceFlowTests(unittest.TestCase):
    def setUp(self):
        self.states, _ = demo_states()
        self.serial = 0

    def apply(self, state, action, payload=None, actor="user", event_id=None):
        self.serial += 1
        return reduce(state, {"id": event_id or f"test-{self.serial}", "action": action,
                              "actor": actor, "payload": payload or {}})

    def effects(self, state, kind):
        return [effect for effect in state["effects"] if effect["kind"] == kind]

    def pay_payload(self, state):
        return {"invoice_id": state["payment"]["id"], "amount_minor": 13000, "currency": "CNY"}

    def test_all_twelve_frames_are_derived_by_events(self):
        self.assertEqual(set(self.states), set(range(1, 13)))
        for frame, state in self.states.items():
            self.assertEqual(view_model(state)["frame_id"], frame)

    def test_conflicting_slot_is_disabled_and_rejected(self):
        state = self.states[6]
        slots = available_slots(state)
        self.assertFalse(slots[0]["enabled"])
        self.assertEqual(slots[0]["reason"], "项目例会")
        self.assertTrue(slots[1]["enabled"])
        before = copy.deepcopy(state)
        with self.assertRaisesRegex(ServiceError, "冲突"):
            self.apply(state, "installation.choose_slot", {"slot_id": "morning"})
        self.assertEqual(state, before)

    def test_confirm_requires_selection_and_rechecks_live_conflicts(self):
        with self.assertRaisesRegex(ServiceError, "请选择"):
            self.apply(self.states[6], "installation.confirm")
        state = copy.deepcopy(self.states[7])
        state["calendar"]["events"]["new-meeting"] = {"id": "new-meeting", "title": "临时会议", "starts_at": "2026-09-19T15:00:00+08:00", "ends_at": "2026-09-19T17:00:00+08:00"}
        with self.assertRaisesRegex(ServiceError, "冲突"):
            self.apply(state, "installation.confirm")
        self.assertFalse(view_model(state)["bindings"]["can_confirm_booking"])

    def test_duplicate_confirmation_does_not_create_booking_or_calendar_twice(self):
        state = self.apply(self.states[8], "installation.confirm")
        self.assertEqual(len(self.effects(state, "installation.upsert")), 1)
        self.assertEqual(len(self.effects(state, "calendar.upsert")), 1)
        self.assertEqual(state["installation"]["version"], 1)

    def test_undo_only_removes_installation_calendar_event(self):
        before = self.states[8]
        after = self.apply(before, "calendar.undo")
        for owner in ("installation", "payment", "order", "delivery"):
            self.assertEqual(after[owner], before[owner])
        self.assertIn("calendar-project-meeting", after["calendar"]["events"])
        self.assertNotIn(before["fixture"]["calendar"]["installation_event_id"], after["calendar"]["events"])
        twice = self.apply(after, "calendar.undo")
        self.assertEqual(len(self.effects(twice, "calendar.remove")), 1)

    def test_calendar_acknowledgement_does_not_create_an_event(self):
        state = self.apply(self.states[8], "calendar.acknowledge")
        self.assertEqual(state["calendar"]["events"], self.states[8]["calendar"]["events"])
        self.assertEqual(state["effects"], self.states[8]["effects"])
        self.assertTrue(state["calendar"]["acknowledged"])

    def test_restore_is_idempotent_and_does_not_rebook(self):
        before = self.states[9]
        after = self.apply(before, "calendar.restore")
        twice = self.apply(after, "calendar.restore")
        self.assertEqual(before["installation"], after["installation"])
        self.assertEqual(twice["calendar"], after["calendar"])
        self.assertEqual(twice["effects"], after["effects"])

    def test_calendar_messages_keep_their_own_ids_and_calendar_entity_identity(self):
        before = self.states[8]
        calendar_id = before["fixture"]["calendar"]["installation_event_id"]
        calendar_event = copy.deepcopy(before["calendar"]["events"][calendar_id])
        undo_id = "service-native-undo:0"
        undone = self.apply(before, "calendar.undo", event_id=undo_id)
        self.assertEqual(set(undone["processed_events"]) - set(before["processed_events"]), {undo_id})
        self.assertNotIn(calendar_id, undone["processed_events"])
        self.assertNotIn(calendar_id, undone["calendar"]["events"])
        restore_id = "service-native-restore:0"
        restored = self.apply(undone, "calendar.restore", event_id=restore_id)
        self.assertEqual(set(restored["processed_events"]) - set(undone["processed_events"]), {restore_id})
        self.assertEqual(restored["calendar"]["events"][calendar_id], calendar_event)
        self.assertEqual(restored["installation"], before["installation"])

    def test_replayed_calendar_undo_and_restore_are_exact_state_noops(self):
        state = self.states[8]
        for action in ("calendar.undo", "calendar.restore"):
            event = {"id": "native-replay-" + action + ":0", "action": action, "actor": "user"}
            with self.subTest(action=action):
                state = reduce(state, event)
                self.assertEqual(reduce(state, event), state)

    def test_calendar_action_message_ids_cannot_be_reused_for_other_actions(self):
        event_id = "service-native-unique:0"
        undone = self.apply(self.states[8], "calendar.undo", event_id=event_id)
        with self.assertRaisesRegex(ServiceError, "复用"):
            self.apply(undone, "calendar.restore", event_id=event_id)
        restored = self.apply(undone, "calendar.restore", event_id="service-native-restore:0")
        with self.assertRaisesRegex(ServiceError, "复用"):
            self.apply(restored, "calendar.undo", event_id="service-native-restore:0")

    def test_installation_cancel_keeps_message_id_separate_from_removed_event(self):
        before = self.states[8]
        event = {"id": "service-native-cancel:0", "action": "installation.cancel", "actor": "user"}
        after = reduce(before, event)
        self.assertEqual(set(after["processed_events"]) - set(before["processed_events"]), {event["id"]})
        self.assertNotIn(before["fixture"]["calendar"]["installation_event_id"], after["processed_events"])
        self.assertEqual(reduce(after, event), after)
        with self.assertRaisesRegex(ServiceError, "复用"):
            self.apply(after, "navigation.desktop", event_id=event["id"])

    def test_replaying_confirmation_after_undo_does_not_readd_calendar(self):
        after = self.apply(self.states[9], "installation.confirm")
        self.assertEqual(after["calendar"]["installation_sync"], "undone")

    def test_rescheduling_updates_same_booking_and_calendar_identity(self):
        state = copy.deepcopy(self.states[8])
        state["calendar"]["events"].pop("calendar-project-meeting")
        state = self.apply(state, "installation.open_slots")
        state = self.apply(state, "installation.choose_slot", {"slot_id": "morning"})
        state = self.apply(state, "installation.confirm")
        self.assertEqual(state["installation"]["id"], self.states[8]["installation"]["id"])
        self.assertEqual(state["installation"]["version"], 2)
        self.assertEqual(len(state["calendar"]["events"]), 1)
        event = next(iter(state["calendar"]["events"].values()))
        self.assertEqual(event["id"], state["fixture"]["calendar"]["installation_event_id"])
        self.assertEqual(event["starts_at"], "2026-09-19T09:00:00+08:00")

    def test_cancelling_draft_keeps_prior_booking(self):
        state = self.apply(self.states[8], "installation.open_slots")
        state = self.apply(state, "installation.close_slots")
        self.assertEqual(state["installation"], self.states[8]["installation"])
        self.assertEqual(state["calendar"], self.states[8]["calendar"])

    def test_day_selection_recomputes_conflicts_and_changes_calendar_date(self):
        state = self.apply(self.states[7], "installation.choose_day", {"date": "2026-09-20"})
        self.assertIsNone(state["installation"]["selected_slot_id"])
        self.assertTrue(all(slot["enabled"] for slot in available_slots(state)))
        state = self.apply(state, "installation.choose_slot", {"slot_id": "morning"})
        state = self.apply(state, "installation.confirm")
        event = state["calendar"]["events"][state["fixture"]["calendar"]["installation_event_id"]]
        self.assertEqual(event["starts_at"], "2026-09-20T09:00:00+08:00")

    def test_explicit_installation_cancel_removes_linked_event_only(self):
        before = self.states[8]
        after = self.apply(before, "installation.cancel")
        self.assertEqual(after["installation"]["status"], "cancelled")
        self.assertEqual(set(after["calendar"]["events"]), {"calendar-project-meeting"})
        self.assertEqual(after["payment"], before["payment"])
        twice = self.apply(after, "installation.cancel")
        self.assertEqual(after["effects"], twice["effects"])
        with self.assertRaises(ServiceError):
            self.apply(after, "calendar.restore")
        with self.assertRaises(ServiceError):
            self.apply(self.states[10], "installation.cancel")

    def test_defer_and_card_dismiss_only_change_presentation(self):
        state = self.apply(self.states[5], "installation.defer")
        self.assertEqual(view_model(state)["frame_id"], 3)
        self.assertEqual(state["installation"]["status"], "available")
        before = self.states[3]
        card_id = view_model(before)["cards"][0]["id"]
        after = self.apply(before, "card.dismiss", {"card_id": card_id})
        self.assertEqual(view_model(after)["cards"], [])
        self.assertEqual(before["order"], after["order"])

    def test_payment_requires_user_and_exact_invoice_details(self):
        state = self.states[11]
        self.assertEqual(state["payment"]["status"], "pending")
        self.assertIsNone(state["payment"]["receipt"])
        self.assertEqual(self.effects(state, "payment.capture_demo"), [])
        with self.assertRaisesRegex(ServiceError, "来源"):
            self.apply(state, "payment.pay", self.pay_payload(state), actor="provider")
        for key, value in (("amount_minor", 1), ("invoice_id", "wrong-invoice"), ("currency", "USD")):
            payload = self.pay_payload(state)
            payload[key] = value
            with self.assertRaises(ServiceError):
                self.apply(state, "payment.pay", payload)

    def test_payment_repeated_clicks_create_one_receipt(self):
        before = self.states[11]
        after = self.apply(before, "payment.pay", self.pay_payload(before))
        twice = self.apply(after, "payment.pay", self.pay_payload(after))
        self.assertEqual(after["payment"], twice["payment"])
        self.assertEqual(len(self.effects(twice, "payment.capture_demo")), 1)
        self.assertEqual(twice["payment"]["receipt"]["amount_minor"], 13000)

    def test_pending_cancel_is_not_refund_or_service_cancellation(self):
        before = self.states[11]
        after = self.apply(before, "payment.cancel")
        self.assertEqual(after["payment"]["status"], "cancelled")
        self.assertIsNone(after["payment"]["receipt"])
        self.assertEqual(before["installation"], after["installation"])
        self.assertEqual(before["calendar"], after["calendar"])
        with self.assertRaises(ServiceError):
            self.apply(after, "payment.pay", self.pay_payload(after))
        reopened = self.apply(after, "payment.reopen")
        paid = self.apply(reopened, "payment.pay", self.pay_payload(reopened))
        with self.assertRaisesRegex(ServiceError, "退款"):
            self.apply(paid, "payment.cancel")
        self.assertEqual(len(self.effects(paid, "payment.capture_demo")), 1)

    def test_duplicate_provider_messages_do_not_regress_or_duplicate_invoice(self):
        state = self.apply(self.states[12], "logistics.out_for_delivery", actor="provider")
        state = self.apply(state, "logistics.delivered", actor="provider")
        state = self.apply(state, "installation.technician_departed", actor="provider")
        state = self.apply(state, "installation.completed", actor="provider")
        self.assertEqual(state["delivery"]["status"], "delivered")
        self.assertEqual(state["installation"]["status"], "completed")
        self.assertEqual(state["payment"]["status"], "paid")
        self.assertEqual(len(self.effects(state, "payment.invoice_created")), 1)

    def test_duplicate_event_is_exact_noop_and_reused_id_is_rejected(self):
        state = initial_state()
        event = {"id": "unique-event", "action": "order.purchase_demo", "actor": "user"}
        after = reduce(state, event)
        self.assertEqual(reduce(after, event), after)
        event["action"] = "navigation.desktop"
        with self.assertRaisesRegex(ServiceError, "复用"):
            reduce(after, event)

    def test_card_body_opens_owning_app_without_domain_mutation(self):
        state = self.states[8]
        for card in view_model(state)["cards"]:
            action = card["body_action"]
            after = self.apply(state, action["action"], action["payload"])
            self.assertEqual(after["ui"]["app"], card["owner_app"])
            for domain in ("order", "delivery", "installation", "calendar", "payment", "effects"):
                self.assertEqual(after[domain], state[domain])

    def test_cards_have_distinct_owners_and_no_cross_scope_confirmation(self):
        cards = view_model(self.states[8])["cards"]
        self.assertEqual([card["owner_app"] for card in cards], ["installation", "calendar"])
        self.assertEqual({action["action"] for action in cards[1]["actions"]}, {"calendar.acknowledge", "calendar.undo"})
        cards = view_model(self.states[12])["cards"]
        self.assertEqual([card["owner_app"] for card in cards], ["payment", "installation"])


if __name__ == "__main__":
    unittest.main()
