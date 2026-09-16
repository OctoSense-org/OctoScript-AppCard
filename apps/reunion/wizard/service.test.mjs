import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createSession,getView,activateControl,nextUpdate,goBack,restart,errorMessage,scenario} from './service.mjs';

function driver(locale='en') {
 let session=createSession({locale}),count=0;
 return {
  get session(){return session;},get view(){return getView(session);},
  click(id){session=activateControl(session,id,`click-${++count}`,getView(session).renderId);return this;},
  update(){session=nextUpdate(session,`update-${++count}`);return this;},
  back(){session=goBack(session);return this;},
  reset(){session=restart(session);return this;},
  frame(n){assert.equal(getView(session).frameId,n);return this;},
  rsvp(slot='saturday'){return this.click('open_invite').click('open_poll').click('choose_time').click(slot).click('confirm_attendance');},
 };
}
const code=(fn,value)=>assert.throws(fn,error=>error.code===value);

for(const locale of ['cn','en'])test(`${locale}: all 12 states, independently owned calendar and payment`,()=>{
 const d=driver(locale).frame(1),seen=new Set([1]);
 const record=frame=>{d.frame(frame);seen.add(frame);};
 d.click('open_invite_control');record(2);
 d.click('open_poll');record(3);
 d.click('choose_time');record(4);
 for(const id of ['friday','confirm_attendance'])code(()=>activateControl(d.session,id,'disabled-'+id,d.view.renderId),'DISABLED');
 d.click('saturday');record(5);
 assert.equal(d.view.state.reunion.rsvp,'invited');
 d.click('confirm_attendance');record(6);
 assert.equal(d.view.state.reunion.rsvp,'confirmed');
 assert.equal(d.view.state.calendar.status,'absent');
 assert.equal(d.view.state.payment.status,'unrequested');
 assert.match(d.view.nextUpdate.label,locale==='cn'?/确认/:/confirmation/);
 d.update();record(7);
 const originalEvent=d.view.state.calendar.event;
 assert.equal(originalEvent.id,'calendar-reunion-2016');
 assert.equal(originalEvent.startsAt,'2026-10-24T18:30:00+08:00');
 d.click('ack_calendar');
 assert.equal(d.view.state.calendar.acknowledged,true);
 code(()=>activateControl(d.session,'ack_calendar','repeat-ack',d.view.renderId),'DISABLED');
 d.click('undo_calendar');record(8);
 assert.equal(d.view.state.calendar.status,'removed');
 assert.equal(d.view.state.reunion.rsvp,'confirmed');
 d.click('restore_calendar').frame(7);
 assert.deepEqual(d.view.state.calendar.event,originalEvent);
 assert.equal(d.view.state.calendar.revision,3);
 d.update();record(9);
 assert.equal(d.view.state.payment.status,'due');
 assert.equal(d.view.state.payment.amountMinor,18000);
 assert.equal(d.view.state.payment.payee,'王宁');
 assert.equal(d.view.state.payment.receipt,null);
 d.click('cancel_payment');record(10);
 assert.equal(d.view.state.reunion.rsvp,'confirmed');
 assert.equal(d.view.state.calendar.status,'added');
 assert.equal(d.view.state.payment.status,'cancelled');
 d.click('reopen_payment').frame(9);
 assert.equal(d.view.state.payment.receipt,null);
 d.click('pay_contribution');record(11);
 assert.deepEqual(d.view.state.payment.receipt,{id:'REU-20261024-001',paymentId:'contribution-reunion-2016',eventId:'reunion-2016',amountMinor:18000,currency:'CNY',payee:'王宁',purpose:'2016届同学聚会餐费',paidAt:'2026-10-21T10:18:00+08:00'});
 assert.ok(Object.isFrozen(d.session.state.payment.receipt));
 const receipt=JSON.stringify(d.view.state.payment.receipt);
 d.click('view_reunion');record(12);
 assert.equal(d.view.completed,true);
 assert.equal(d.view.state.ui.surface,'app');
 d.click('back_desktop').frame(11).back();
 assert.equal(JSON.stringify(d.view.state.payment.receipt),receipt);
 assert.deepEqual([...seen].sort((a,b)=>a-b),Array.from({length:12},(_,i)=>i+1));
});

test('Sunday is a preference; explicit organizer confirmation updates the same event',()=>{
 const d=driver('cn').rsvp('sunday').frame(6);
 assert.equal(d.view.state.reunion.preferredSlot,'sunday');
 assert.match(d.view.nativeText.text_73,/周日/);
 assert.equal(d.view.state.calendar.event,null);
 d.update().frame(7);
 assert.equal(d.view.state.reunion.preferredSlot,'sunday');
 assert.equal(d.view.state.reunion.confirmedSlot,'saturday');
 assert.match(d.view.nativeText.text_117,/改定周六/);
 assert.equal(d.view.state.calendar.event.startsAt,'2026-10-24T18:30:00+08:00');
});

test('native delivery is idempotent, rejects stale actions and conflicting event IDs',()=>{
 const initial=createSession(),id=getView(initial).renderId;
 const opened=activateControl(initial,'open_invite','event-1',id);
 assert.strictEqual(activateControl(opened,'open_invite_control','event-1',id),opened);
 code(()=>activateControl(opened,'open_poll','event-1',getView(opened).renderId),'ID_CONFLICT');
 code(()=>activateControl(opened,'open_poll','event-2',id),'STALE');
 code(()=>activateControl(opened,'pay_contribution','event-3',getView(opened).renderId),'UNKNOWN_CONTROL');
 code(()=>activateControl(opened,'open_poll','',getView(opened).renderId),'EVENT_ID');
 assert.equal(initial.state.ui.frame,1);
 assert.equal(opened.events.length,1);
 const d=driver().rsvp();
 const updated=nextUpdate(d.session,'organizer-1');
 assert.strictEqual(nextUpdate(updated,'organizer-1'),updated);
 assert.equal(updated.state.calendar.revision,1);
 assert.equal(updated.state.payment.status,'unrequested');
});

test('before RSVP and payment, app details never invent confirmation or a receipt',()=>{
 const d=driver('en').click('open_invite').click('group_info').frame(12);
 assert.equal(d.view.nativeText.text_193,'Not joined');
 assert.equal(d.view.nativeText.text_194,'Not requested');
 assert.equal(d.view.nativeText.text_197,'No receipt yet');
 assert.match(d.view.nativeText.text_188,/awaiting/);
 assert.equal(d.view.completed,false);
 assert.equal(d.view.nextUpdate,null);
 code(()=>nextUpdate(d.session,'premature'),'NO_UPDATE');
 d.click('back_desktop').click('choose_time').click('saturday').click('confirm_attendance').click('view_registration').frame(12);
 assert.equal(d.view.nativeText.text_193,'RSVP sent');
 assert.equal(d.view.nativeText.text_197,'No receipt yet');
});

test('payment request remains separate when a calendar entry was removed',()=>{
 const d=driver().rsvp().update().click('undo_calendar').update().frame(9);
 d.click('cancel_payment').click('view_reunion').frame(12);
 assert.equal(d.view.state.calendar.status,'removed');
 assert.equal(d.view.state.reunion.rsvp,'confirmed');
 assert.equal(d.view.nativeText.text_194,'Payment cancelled');
 assert.equal(d.view.nativeText.text_197,'No receipt yet');
});

test('back keeps service facts and restart creates a new rendering epoch',()=>{
 const d=driver('cn').rsvp().update().update().click('pay_contribution').frame(11);
 const paid=JSON.stringify(d.view.state.payment),oldId=d.view.renderId;
 d.back().frame(11);
 assert.equal(JSON.stringify(d.view.state.payment),paid);
 d.reset().frame(1);
 assert.equal(d.view.locale,'cn');
 assert.equal(d.view.state.payment.status,'unrequested');
 assert.equal(d.view.canGoBack,false);
 assert.notEqual(d.view.renderId,oldId);
 code(()=>activateControl(d.session,'open_invite','old-action',oldId),'STALE');
 assert.match(errorMessage({code:'STALE'},'cn'),/更新/);
 assert.match(errorMessage({code:'STALE'},'en'),/changed/);
 assert.equal(scenario.phases.cn.length,4);
});

test('every scene translates every native label and only updates existing native nodes',()=>{
 const catalogue=JSON.parse(readFileSync(new URL('../source/native-catalogue.json',import.meta.url)));
 const walk=node=>[node,...(node.children??node.c??[]).flatMap(walk)];
 for(const locale of ['cn','en'])for(let frame=1;frame<=12;frame++){
  const fixture=JSON.parse(JSON.stringify(createSession({locale})));fixture.state.ui.frame=frame;
  const v=getView(fixture),c=catalogue[frame-1];
  assert.deepEqual(Object.keys(v.nativeText).sort(),Object.keys(c.texts).sort());
  const mapped=JSON.parse(readFileSync(new URL(`../cards/reunion-${String(frame).padStart(2,'0')}/mapped.json`,import.meta.url)));
  const ids=new Set(walk(mapped.tree).map(n=>n.id));
  for(const id of [...Object.keys(v.nativeText),...Object.keys(v.nativeStyles),...Object.keys(v.nativeEnabled),...Object.keys(v.nativeLayout)])assert.ok(ids.has(id),`frame ${frame}: missing ${id}`);
  for(const value of Object.values(v.nativeText)){
   assert.equal(typeof value,'string');assert.ok(value.length>0);
   if(locale==='en')assert.doesNotMatch(value,/\p{Script=Han}/u);
  }
  for(const c of v.nativeControls){assert.ok(ids.has(c.sourceId+'_control'));assert.ok(c.textIds.every(id=>id in v.nativeText));}
 }
});

test('dock label widths support readable English and center on their real native icons',()=>{
 for(let frame=3;frame<=11;frame++){
  const fixture=JSON.parse(JSON.stringify(createSession({locale:'en'})));fixture.state.ui.frame=frame;
  const v=getView(fixture),mapping=JSON.parse(readFileSync(new URL(`../cards/reunion-${String(frame).padStart(2,'0')}/mapping.json`,import.meta.url)));
  for(const [id,layout]of Object.entries(v.nativeLayout)){
   const name={Messages:'dock_message',Calendar:'dock_calendar',Reunion:'dock_group',Payment:'dock_wallet'}[v.nativeText[id]];
   const icon=mapping.elements.find(n=>n.source_id===name);assert.ok(icon);
   assert.equal(layout.w,64);assert.equal(layout.x+layout.w/2,icon.bounds[0]+icon.bounds[2]/2);
   assert.ok(v.nativeStyles[id].size>=10);assert.equal(v.nativeStyles[id].alignx,.5);
  }
 }
});
