import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {createSession, getView, activateControl, goBack, restart, nextUpdate, errorMessage} from './service.mjs';

const BOOKING = 'health-booking-annual-2026';
const CALENDAR = 'calendar-health-annual-2026';
const CONFLICT = 'calendar-personal-20261024';
let serial = 0;
const click = (session, control, id = `test-${++serial}`) => activateControl(session, control, id, getView(session).renderId);
const follow = (session, control) => click(session, control);
const enter = (locale = 'en') => ['open_details', 'arrange_desktop', 'choose_items', 'choose_time'].reduce(follow, createSession({locale}));
const book = (locale = 'en') => ['afternoon', 'confirm_booking'].reduce(follow, enter(locale));

test('primary route creates one booking and one linked event, then shows a summary', () => {
  let session = book('cn');
  assert.equal(getView(session).frameId, 7);
  assert.equal(session.state.booking.id, BOOKING);
  assert.equal(session.state.booking.status, 'booked');
  assert.equal(Object.keys(session.state.calendar.events).length, 2);
  assert.equal(session.state.calendar.events[CALENDAR].bookingId, BOOKING);
  session = click(session, 'view_booking');
  assert.equal(getView(session).frameId, 12);
  assert.equal(getView(session).completed, true);
  assert.match(getView(session).nativeText.appointment_time, /10月24日/);
});

test('optional dental and vision items require separate user selections', () => {
  let session = ['open_details', 'arrange_desktop', 'choose_items'].reduce(follow, createSession());
  assert.equal(session.state.selection.dental, false);
  assert.equal(session.state.selection.vision, false);
  const before = structuredClone(session);
  session = click(session, 'toggle_dental');
  assert.equal(before.state.selection.dental, false);
  assert.equal(session.state.selection.dental, true);
  assert.equal(getView(session).nativeText.dental_note, 'Selected');
  session = click(click(session, 'toggle_vision'), 'toggle_dental');
  session = ['choose_time', 'afternoon', 'confirm_booking'].reduce(follow, session);
  assert.equal(session.state.booking.dental, false);
  assert.equal(session.state.booking.vision, true);
});

test('Saturday conflict is disabled and changing day clears a selection', () => {
  let session = enter();
  assert.throws(() => click(session, 'conflict_slot'), error => error.code === 'DISABLED_CONTROL');
  assert.throws(() => click(session, 'confirm_booking'), error => error.code === 'DISABLED_CONTROL');
  session = click(session, 'sunday');
  assert.equal(getView(session).nativeEnabled.conflict_slot_control, true);
  assert.equal(getView(session).nativeText.morning_note, 'Calendar free');
  session = click(session, 'conflict_slot_control');
  assert.equal(getView(session).frameId, 6);
  assert.equal(session.state.selection.slot.start, '09:00');
  session = click(session, 'cancel_selection');
  session = click(session, 'saturday');
  assert.equal(session.state.selection.slot, null);
  assert.equal(getView(session).nativeEnabled.confirm_booking_control, false);
});

test('calendar acknowledgement, undo and restore keep booking identity and other events', () => {
  let session = book();
  const booking = structuredClone(session.state.booking);
  session = click(session, 'calendar_confirm', 'ack');
  assert.equal(getView(session).nativeEnabled.calendar_confirm_control, false);
  assert.equal(activateControl(session, 'calendar_confirm', 'ack', 'old-render'), session);
  session = click(session, 'calendar_undo', 'undo');
  assert.deepEqual(session.state.booking, booking);
  assert.equal(getView(session).frameId, 8);
  assert.equal(session.state.calendar.events[CALENDAR], undefined);
  assert.ok(session.state.calendar.events[CONFLICT]);
  assert.equal(activateControl(session, 'calendar_undo', 'undo', 'old-render'), session);
  session = click(session, 'calendar_restore', 'restore');
  assert.equal(session.state.calendar.events[CALENDAR].id, CALENDAR);
  assert.equal(Object.keys(session.state.calendar.events).length, 2);
  assert.equal(activateControl(session, 'calendar_restore', 'restore', 'old-render'), session);
});

test('editing remains a draft until confirmed, then updates the same entities once', () => {
  let session = book();
  const original = structuredClone(session.state);
  session = click(session, 'edit_booking');
  session = click(session, 'select_new_time');
  assert.equal(getView(session).frameId, 10);
  assert.deepEqual(session.state.booking, original.booking);
  assert.deepEqual(session.state.calendar, original.calendar);
  session = click(session, 'confirm_changes', 'change-once');
  assert.equal(session.state.booking.id, BOOKING);
  assert.equal(session.state.booking.day, '2026-10-25');
  assert.equal(session.state.booking.version, 2);
  assert.equal(session.state.calendar.events[CALENDAR].day, '2026-10-25');
  assert.equal(Object.keys(session.state.calendar.events).length, 2);
  assert.equal(activateControl(session, 'confirm_changes', 'change-once', 'old-render'), session);
});

test('discarding a draft preserves booking, while edits respect a removed calendar event', () => {
  let session = book();
  const booking = structuredClone(session.state.booking);
  session = ['edit_booking', 'select_new_time', 'discard_changes'].reduce(follow, session);
  assert.deepEqual(session.state.booking, booking);
  session = ['calendar_undo', 'view_booking', 'return_booking', 'edit_booking', 'select_new_time', 'confirm_changes'].reduce(follow, session);
  assert.equal(session.state.booking.day, '2026-10-25');
  assert.equal(session.state.calendar.events[CALENDAR], undefined);
  assert.equal(getView(session).frameId, 8);
  session = click(session, 'calendar_restore');
  assert.equal(session.state.calendar.events[CALENDAR].day, '2026-10-25');
});

test('cancel review has no effect until explicit confirmation and never removes unrelated events', () => {
  let session = ['view_booking', 'cancel_booking'].reduce(follow, book());
  assert.equal(getView(session).frameId, 11);
  assert.equal(session.state.booking.status, 'booked');
  assert.ok(session.state.calendar.events[CALENDAR]);
  session = click(session, 'keep_booking');
  assert.equal(session.state.booking.status, 'booked');
  session = ['view_booking', 'cancel_booking'].reduce(follow, session);
  session = click(session, 'confirm_cancel', 'cancel-once');
  assert.equal(session.state.booking.status, 'canceled');
  assert.equal(session.state.calendar.events[CALENDAR], undefined);
  assert.ok(session.state.calendar.events[CONFLICT]);
  assert.equal(getView(session).nativeText.title, 'Appointment canceled');
  assert.equal(getView(session).nativeEnabled.cancel_booking_control, false);
  assert.equal(activateControl(session, 'confirm_cancel', 'cancel-once', 'old-render'), session);
});

test('stale controls and reused event IDs cannot apply another action', () => {
  const initial = createSession();
  const session = click(initial, 'open_details', 'identity');
  assert.throws(() => activateControl(session, 'arrange_desktop', 'identity'), error => error.code === 'EVENT_ID_REUSED');
  assert.throws(() => activateControl(session, 'arrange_desktop', 'new', getView(initial).renderId), error => error.code === 'STALE_RENDER');
  assert.throws(() => click(session, 'confirm_cancel'), error => error.code === 'UNKNOWN_CONTROL');
  assert.equal(activateControl(initial, 'open_details', '__proto__').state.ui.frameId, 2);
});

test('summary imagery follows booking and calendar state instead of retaining stale success marks', () => {
  let session = click(book(), 'view_booking');
  assert.deepEqual(getView(session).nativeHidden, []);
  session = ['return_booking','calendar_undo','view_booking'].reduce(follow,session);
  assert.deepEqual(getView(session).nativeHidden, ['check_icon_8']);
  assert.equal(getView(session).nativeText.booking_status, 'Confirmed');
  assert.equal(getView(session).nativeText.calendar_status, 'Removed');
  session = ['cancel_booking','confirm_cancel'].reduce(follow,session);
  assert.deepEqual(getView(session).nativeHidden, ['check_icon_0','check_icon_7','check_icon_8']);
  assert.equal(getView(session).nativeText.booking_status, 'Canceled');
  assert.equal(getView({...session,locale:'cn'}).nativeText.calendar_status, '已移除');
});

test('edit date/time have a visible gap and summary labels have room after their icons', async () => {
  const draft = getView(click(book(),'edit_booking'));
  assert.ok(draft.nativeLayout.current_day.x + draft.nativeLayout.current_day.w + 8 <= draft.nativeLayout.current_time.x);
  const summary = getView(click(book(),'view_booking'));
  const bundle = JSON.parse(await readFile(new URL('./card-bundle/cards.bundle.json',import.meta.url),'utf8'));
  const nodes = Object.fromEntries(bundle.scenes['12'].mapping.elements.map(n=>[n.source_id,n]));
  for (const [label,icon] of [['appointment_title','clinic_icon_1'],['package_summary','package_icon_2'],['appointment_time','calendar_icon_3'],['provider_name','location_icon_4']]) {
    assert.ok(summary.nativeLayout[label].x >= nodes[icon].bounds[0]+nodes[icon].bounds[2]+8,label);
  }
});

test('Back restores local snapshots; Restart preserves stale-render protection', () => {
  let session = book();
  const previousRender = getView(session).renderId;
  session = goBack(session, 'back');
  assert.equal(session.state.booking, null);
  assert.equal(getView(session).frameId, 6);
  assert.equal(session.state.calendar.events[CALENDAR], undefined);
  session = restart(session, 'restart');
  assert.equal(getView(session).frameId, 1);
  assert.equal(getView(session).canGoBack, false);
  assert.notEqual(getView(session).renderId, previousRender);
  assert.equal(restart(session, 'restart'), session);
  assert.throws(() => nextUpdate(session), error => error.code === 'NO_UPDATE');
});

test('all current labels are bilingual and every override targets a real current-frame node', async () => {
  const frames = JSON.parse(await readFile(new URL('./frames.json', import.meta.url), 'utf8'));
  let session = createSession();
  const route = ['open_details','arrange_desktop','choose_items','choose_time','afternoon','confirm_booking','calendar_undo','calendar_restore','edit_booking','select_new_time','confirm_changes','view_booking','cancel_booking','confirm_cancel'];
  const visited = new Set();
  for (const control of [null, ...route]) {
    if (control) session = click(session, control);
    for (const locale of ['en', 'cn']) {
      const view = getView({...session, locale}), frame = frames[view.frameId]; visited.add(view.frameId);
      assert.deepEqual(Object.keys(view.nativeText).sort(), Object.keys(frame.labels).sort());
      for (const value of Object.values(view.nativeText)) {
        assert.equal(typeof value, 'string'); assert.ok(value.length > 0);
        if (locale === 'en') assert.doesNotMatch(value, /[\u3400-\u9fff]/);
      }
      for (const id of [...Object.keys(view.nativeText), ...Object.keys(view.nativeEnabled), ...Object.keys(view.nativeStyles), ...Object.keys(view.nativeLayout), ...view.nativeHidden]) assert.ok(frame.nodeIds.includes(id), `${view.frameId}: ${id}`);
      for (const button of view.nativeControls) for (const id of button.textIds) assert.ok(view.nativeText[id]);
    }
  }
  assert.equal(visited.size, 12);
  assert.equal(errorMessage({code:'DISABLED_CONTROL'},'en'), 'This option is currently unavailable');
});
