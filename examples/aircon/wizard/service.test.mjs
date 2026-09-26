/** Browser model tests only: these do not claim native Makepad input evidence. */
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {DEFAULT_FIXTURE,ServiceError,eventFingerprint,initialState,reduce,availableSlots,frameId,createSession,dispatch,activateControl,nextUpdate,goBack,restart,setLocale,getView,errorMessage} from './service.mjs';

const root=fileURLToPath(new URL('../',import.meta.url));
const read=path=>JSON.parse(readFileSync(new URL('../'+path,import.meta.url),'utf8'));
const stable=value=>Array.isArray(value)?value.map(stable):value&&typeof value==='object'?Object.fromEntries(Object.keys(value).sort().map(key=>[key,stable(value[key])])):value;
const failCode=code=>error=>error instanceof ServiceError&&error.code===code;
const act=(session,source,id)=>activateControl(session,source,id);
function picker(locale='cn') {
  let session=createSession({locale});
  session=act(session,'buy'); session=act(session,'back'); session=nextUpdate(session); session=nextUpdate(session);
  return act(session,'choose_time');
}
function booked() { return act(act(picker(),'afternoon'),'confirm_booking'); }
function pending() { return nextUpdate(nextUpdate(booked())); }
function event(action,id,payload={}) { return {id,action,actor:action.startsWith('logistics.')||['installation.technician_departed','installation.completed'].includes(action)?'provider':'user',payload}; }
function pythonStates(events) {
  const code='import json,sys\nfrom controller import initial_state,reduce\ns=initial_state();out=[]\nfor e in json.load(sys.stdin):\n s=reduce(s,e);out.append(s)\nprint(json.dumps(out,ensure_ascii=False))';
  return JSON.parse(execFileSync('python3',['-c',code],{cwd:root+'service',input:JSON.stringify(events),encoding:'utf8'}));
}

test('embedded fixture exactly matches the validated Python fixture',()=>{
  assert.deepEqual(DEFAULT_FIXTURE,read('service/fixture.json'));
});

test('UTF-8 fingerprints match standard SHA-256 for exact canonical event JSON',()=>{
  for(const value of [{id:'a',action:'calendar.undo',actor:'user'},event('payment.pay','native:0',{invoice_id:'账单🙂',amount_minor:13000,currency:'CNY'}),{id:'padding',payload:{text:'测'.repeat(500)}}]) {
    assert.equal(eventFingerprint(value),createHash('sha256').update(JSON.stringify(stable(value))).digest('hex'));
  }
});

test('all twelve complete states match Python fixtures, including processed-event hashes',()=>{
  let state=initialState();const compared=new Set([1]);
  assert.deepEqual(state,read('service/fixtures/01.state.json'));
  for(const input of read('service/fixtures/events.json')) {
    state=reduce(state,input);const frame=frameId(state);
    if(!compared.has(frame)) { assert.deepEqual(state,read(`service/fixtures/${String(frame).padStart(2,'0')}.state.json`),`frame ${frame}`); compared.add(frame); }
  }
  assert.deepEqual([...compared].sort((a,b)=>a-b),Array.from({length:12},(_,i)=>i+1));
});

test('Sunday, reschedule, undo, restore, and explicit cancellation match Python after every event',()=>{
  const events=read('service/fixtures/events.json').slice(0,7);
  events.push(event('installation.reschedule','branch-1'),event('installation.choose_day','branch-2',{date:'2026-09-20'}),event('installation.choose_slot','branch-3',{slot_id:'morning'}),event('installation.confirm','branch-4'),event('calendar.undo','native-undo:0'),event('calendar.restore','native-restore:0'),event('installation.cancel','native-cancel:0'));
  const expected=pythonStates(events);let state=initialState();
  for(let index=0;index<events.length;index++) { state=reduce(state,events[index]);assert.deepEqual(state,expected[index],events[index].action); }
});

test('cancel, reopen, repeated payment, and receipt route match Python',()=>{
  const events=read('service/fixtures/events.json').slice(0,-1);
  events.push(event('payment.cancel','cancel'),event('payment.reopen','reopen'),event('payment.pay','pay',{invoice_id:DEFAULT_FIXTURE.payment.id,amount_minor:13000,currency:'CNY'}),event('payment.pay','pay-again',{invoice_id:DEFAULT_FIXTURE.payment.id,amount_minor:13000,currency:'CNY'}),event('navigation.open_app','receipt',{app:'payment',page:'receipt'}));
  const expected=pythonStates(events);let state=initialState();
  for(let index=0;index<events.length;index++) { state=reduce(state,events[index]); assert.deepEqual(state,expected[index],events[index].action); }
});

test('guided workflow is driven by native source controls and explicit provider updates',()=>{
  let session=createSession();const frames=new Set([getView(session).frameId]);
  assert.equal(getView(session).nextUpdate,null);
  assert.throws(()=>nextUpdate(session),failCode('no_update'));
  const native=source=>{session=act(session,source);frames.add(getView(session).frameId);};
  const update=()=>{session=nextUpdate(session);frames.add(getView(session).frameId);};
  native('buy_control'); assert.equal(getView(session).frameId,2);assert.equal(getView(session).nextUpdate,null);
  native('back');assert.equal(getView(session).nextUpdate.action,'logistics.out_for_delivery');
  update();update();native('choose_time');
  assert.throws(()=>act(session,'conflict_slot'),failCode('disabled_control'));
  assert.throws(()=>act(session,'confirm_booking'),failCode('disabled_control'));
  native('afternoon');native('confirm_booking');native('acknowledge_calendar');native('undo_calendar');native('restore_calendar');
  update();update();native('withdraw_payment_request');native('pay_materials');native('pay_materials');native('view_payment_receipt');
  assert.deepEqual([...frames].sort((a,b)=>a-b),Array.from({length:12},(_,i)=>i+1));
  assert.equal(getView(session).completed,true);assert.equal(session.state.payment.receipt.amount_minor,13000);
  assert.equal(getView(session).nextUpdate,null);
});

test('Saturday conflicts, Sunday availability and submit-time conflict checks use shared dates',()=>{
  let session=picker();assert.equal(getView(session).nativeControls.find(n=>n.sourceId==='conflict_slot').enabled,false);
  session=act(session,'afternoon');session=act(session,'sunday');
  assert.equal(session.state.installation.selected_slot_id,null);
  assert.equal(getView(session).nativeControls.find(n=>n.sourceId==='conflict_slot').enabled,true);
  assert.equal(getView(session).nativeControls.find(n=>n.sourceId==='confirm_booking').enabled,false);
  session=act(session,'conflict_slot');
  const raced=structuredClone(session.state);
  raced.calendar.events.new={id:'new',title:'临时会议',starts_at:'2026-09-20T10:00:00+08:00',ends_at:'2026-09-20T12:00:00+08:00'};
  assert.throws(()=>reduce(raced,event('installation.confirm','race')),failCode('calendar_conflict'));
  session=act(session,'confirm_booking');
  assert.equal(session.state.calendar.events[DEFAULT_FIXTURE.calendar.installation_event_id].starts_at,'2026-09-20T09:00:00+08:00');
});

test('calendar undo and restore keep message IDs distinct from stable calendar entity IDs',()=>{
  let state=booked().state;const before=structuredClone(state),calendarId=DEFAULT_FIXTURE.calendar.installation_event_id;
  const undo=event('calendar.undo','service-undo:0');state=reduce(state,undo);
  assert.deepEqual(state.installation,before.installation);assert.equal(state.calendar.events[calendarId],undefined);
  assert.ok(state.processed_events[undo.id]);assert.equal(state.processed_events[calendarId],undefined);
  assert.deepEqual(reduce(state,undo),state);
  assert.throws(()=>reduce(state,event('calendar.restore',undo.id)),failCode('reused_id'));
  const restore=event('calendar.restore','service-restore:0');state=reduce(state,restore);
  assert.deepEqual(state.calendar.events[calendarId],before.calendar.events[calendarId]);assert.deepEqual(reduce(state,restore),state);
  assert.equal(state.effects.filter(n=>n.kind==='installation.upsert').length,1);
});

test('explicit booking cancellation is separate from calendar-only undo and draft cancellation',()=>{
  const session=booked(),before=session.state;
  let changed=act(act(session,'reschedule'),'cancel_selection');
  assert.deepEqual(changed.state.installation,before.installation);assert.deepEqual(changed.state.calendar,before.calendar);
  changed=act(session,'cancel_booking','native-booking-cancel:0');
  assert.equal(changed.state.installation.status,'cancelled');assert.deepEqual(changed.state.payment,before.payment);
  assert.deepEqual(Object.keys(changed.state.calendar.events),['calendar-project-meeting']);
  assert.ok(changed.state.processed_events['native-booking-cancel:0']);
});

test('pending payment cancellation is not payment, refund, or service cancellation',()=>{
  const before=pending();let session=act(before,'withdraw_payment_request');
  assert.equal(session.state.payment.status,'cancelled');assert.equal(session.state.payment.receipt,null);
  assert.deepEqual(session.state.installation,before.state.installation);assert.deepEqual(session.state.calendar,before.state.calendar);
  assert.equal(getView(session).nativeControls.find(n=>n.sourceId==='pay_materials').action,'payment.reopen');
  assert.equal(getView(session).nativeControls.find(n=>n.sourceId==='withdraw_payment_request').enabled,false);
  session=act(session,'pay_materials');assert.equal(session.state.payment.status,'pending');assert.equal(session.state.payment.receipt,null);
  const payload={invoice_id:session.state.payment.id,amount_minor:13000,currency:'CNY'};
  assert.throws(()=>reduce(session.state,{...event('payment.pay','wrong-owner',payload),actor:'provider'}),failCode('wrong_actor'));
  assert.throws(()=>reduce(session.state,event('payment.pay','wrong-amount',{...payload,amount_minor:1})),failCode('amount_changed'));
  session=act(session,'pay_materials','same-payment-click');
  assert.deepEqual(act(session,'pay_materials_control','same-payment-click'),session);
  assert.equal(session.state.effects.filter(n=>n.kind==='payment.capture_demo').length,1);
  assert.throws(()=>reduce(session.state,event('payment.cancel','after-payment')),failCode('not_pending'));
});

test('provider updates are monotonic, cannot auto-pay, and duplicate inputs are idempotent',()=>{
  let session=act(act(createSession(),'buy'),'back');
  session=nextUpdate(session,'same-provider-event');assert.deepEqual(nextUpdate(session,'same-provider-event'),session);
  const paid=act(pending(),'pay_materials').state;
  let state=reduce(paid,event('logistics.out_for_delivery','late-1'));
  state=reduce(state,event('logistics.delivered','late-2'));state=reduce(state,event('installation.completed','late-3'));
  assert.equal(state.delivery.status,'delivered');assert.equal(state.installation.status,'completed');assert.equal(state.payment.status,'paid');
  assert.equal(state.effects.filter(n=>n.kind==='payment.invoice_created').length,1);
});

test('Back restores a prior snapshot without pretending to send compensating service requests',()=>{
  const pendingSession=pending(),paid=act(pendingSession,'pay_materials','pay-before-back');
  const back=goBack(paid);
  assert.deepEqual(back.state,pendingSession.state);assert.notEqual(getView(back).renderId,getView(pendingSession).renderId);
  assert.equal(back.inputEvents['pay-before-back'],undefined);
  const paidAgain=act(back,'pay_materials','pay-after-back');
  assert.equal(paidAgain.state.effects.filter(n=>n.kind==='payment.capture_demo').length,1);
  assert.deepEqual(paid.state.payment.receipt,paidAgain.state.payment.receipt);
});

test('Back skips semantic no-op taps, restart clears history, and stale render actions are rejected',()=>{
  let session=picker(),length=session.history.length;
  session=act(session,'saturday');assert.equal(session.history.length,length);
  const oldRender=getView(session).renderId;
  session=act(session,'afternoon');
  assert.throws(()=>activateControl(session,'confirm_booking','stale-submit',oldRender),failCode('stale_control'));
  session=setLocale(session,'en');const restarted=restart(session);
  assert.equal(restarted.locale,'en');assert.equal(getView(restarted).frameId,1);assert.equal(restarted.history.length,0);
  assert.equal(getView(restarted).canGoBack,false);assert.deepEqual(restarted.state,initialState());
  assert.notEqual(getView(restarted).renderId,getView(session).renderId);
});

test('locale changes presentation only and native controls retain the same owned action',()=>{
  const cn=booked(),en=setLocale(cn,'en');assert.deepEqual(en.state,cn.state);
  for(const frame of Array.from({length:12},(_,i)=>i+1)) {
    const session={...createSession(),state:read(`service/fixtures/${String(frame).padStart(2,'0')}.state.json`)};
    for(const locale of ['cn','en']) {
      const view=getView(setLocale(session,locale));assert.ok(view.guidance.title);assert.ok(view.guidance.description);
      assert.deepEqual(view.nativeControls.map(n=>n.sourceId),read(`cards/aircon-${String(frame).padStart(2,'0')}/service-actions.json`).controls?Object.keys(read(`cards/aircon-${String(frame).padStart(2,'0')}/service-actions.json`).controls):[]);
      for(const control of view.nativeControls) { assert.ok(control.label);assert.equal(control.actor,'user');assert.equal(typeof control.enabled,'boolean'); }
    }
  }
  const error=new ServiceError('test','中文提示','English message');assert.equal(errorMessage(error,'en'),'English message');
});

test('guided defer, dismiss, and route branches have an explicit way to continue',()=>{
  let session=goBack(picker());session=act(session,'defer');assert.equal(getView(session).frameId,3);
  assert.equal(getView(session).nativeControls.find(n=>n.sourceId==='view_order').action,'installation.open_slots');
  session=act(session,'view_order');assert.equal(getView(session).frameId,6);
  session=act(act(createSession(),'buy'),'back');session=act(session,'collapse');
  assert.deepEqual(getView(session).nativeControls,[]);assert.equal(getView(session).nextUpdate.action,'logistics.out_for_delivery');
  session=nextUpdate(session);assert.equal(getView(session).frameId,4);
  session=act(session,'courier');assert.equal(session.state.ui.app,'logistics');
  const back=getView(session).nativeControls[0];assert.equal(back.action,'navigation.desktop');
  session=act(session,back.sourceId);assert.equal(session.state.ui.surface,'desktop');
});

test('reducers and views are immutable and reject malformed event payloads',()=>{
  const state=initialState(),before=structuredClone(state);const result=reduce(state,event('order.purchase_demo','first'));
  assert.deepEqual(state,before);assert.notEqual(result,state);
  const session=createSession(),view=getView(session);view.state.order.status='tampered';assert.equal(session.state.order.status,'not_placed');
  assert.throws(()=>reduce(state,{id:'null-payload',action:'order.purchase_demo',actor:'user',payload:null}),failCode('invalid_payload'));
  const special=reduce(state,event('order.purchase_demo','__proto__'));
  assert.equal(Object.hasOwn(special.processed_events,'__proto__'),true);assert.deepEqual(reduce(special,event('order.purchase_demo','__proto__')),special);
});
