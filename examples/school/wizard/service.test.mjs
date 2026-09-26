import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createSession,getView,activateControl,nextUpdate,goBack,restart,errorMessage,FIXTURE,scenario} from './service.mjs';
import {frames} from './copy.mjs';
import {buildNativePayload} from '../../shared/render.mjs';
const routes=JSON.parse(fs.readFileSync(new URL('../route_test.json',import.meta.url))).routes;
const bundle=JSON.parse(fs.readFileSync(new URL('./card-bundle/cards.bundle.json',import.meta.url)));
const path=(obj,name)=>name.split('.').reduce((v,k)=>v?.[k],obj);
let event=0;
const click=(s,id)=>activateControl(s,id,`test-${++event}`,getView(s).renderId);
function verify(s){
 const view=getView(s),state=view.state;
 assert.equal(state.calendar.id,FIXTURE.event.id);assert.equal(state.payment.id,FIXTURE.invoice.id);
 assert.equal(state.payment.amount_minor,12000);assert.equal(state.payment.currency,'CNY');
 assert.equal(state.authorization.autoPay,false);assert.equal(state.authorization.calendarUpdate,true);
 assert.equal(state.calendar.status,state.calendar.present?'added':'removed');
 assert.equal(state.payment.charges,state.payment.status==='paid'?1:0);
 if(state.payment.receipt){assert.equal(state.payment.status,'paid');assert.equal(state.payment.receipt.amount_minor,12000);}
 const textIds=Object.keys(frames[view.frameId].text).sort();assert.deepEqual(Object.keys(view.nativeText).sort(),textIds);
 for(const control of view.nativeControls){assert.ok(Object.hasOwn(frames[view.frameId].controls,control.sourceId));assert.ok(control.textIds.length);assert.ok(control.label);for(const id of control.textIds)assert.ok(view.nativeText[id]);}
 const rendered=buildNativePayload(bundle,view,{assetBase:'http://127.0.0.1:8170/ux-images/',id:view.renderId});
 assert.equal(rendered.frameId,view.frameId);
 return view;
}
for(const locale of ['cn','en'])for(const route of routes)test(`${locale}: ${route.name}`,()=>{
 let s=createSession({locale});verify(s);
 for(const step of route.steps){
  if(step.disabled){const control=getView(s).nativeControls.find(v=>v.sourceId===step.control);assert.equal(control?.enabled,false);assert.throws(()=>click(s,step.control),{code:'disabled_control'});}
  else if(step.control)s=click(s,step.control);
  else if(step.update)s=nextUpdate(s,`test-${++event}`);
  else if(step.back)s=goBack(s);
  else if(step.restart)s=restart(s);
  const v=verify(s);assert.equal(v.frameId,step.frame,`${route.name}: ${JSON.stringify(step)}`);
  for(const [key,value]of Object.entries(step.assert||{}))assert.deepEqual(path(v.state,key),value,key);
 }
});
test('calendar authorization never authorizes payment, even after delivery and acknowledgement',()=>{
 let s=createSession();assert.equal(s.state.calendar.present,true);s=click(s,'open_mail');s=nextUpdate(s,'delivery');s=click(s,'ack_calendar');
 assert.equal(s.state.payment.charges,0);assert.equal(s.state.payment.status,'pending');assert.throws(()=>nextUpdate(s,'unrequested'),{code:'no_update'});
});
test('events are immutable, idempotent, and reject stale/unknown/disabled controls',()=>{
 const start=createSession();const before=JSON.stringify(start);const s=activateControl(start,'open_mail','same',getView(start).renderId);
 assert.equal(JSON.stringify(start),before);assert.ok(Object.isFrozen(start.state.payment));
 assert.equal(activateControl(s,'open_mail','same',getView(start).renderId),s);
 assert.throws(()=>activateControl(s,'show_desktop','new',getView(start).renderId),{code:'stale_render'});
 assert.throws(()=>activateControl(s,'pay_fee','new',getView(s).renderId),{code:'unknown_control'});
 assert.throws(()=>activateControl(s,'show_desktop','',getView(s).renderId),{code:'invalid_event'});
 const delivered=nextUpdate(s,'delivery');assert.equal(nextUpdate(delivered,'delivery'),delivered);
});
test('explicit payment is single and independently undoing calendar preserves receipt',()=>{
 let s=click(click(createSession(),'open_mail'),'show_desktop');const pending=s;
 s=activateControl(s,'pay_fee','one-payment',getView(s).renderId);assert.equal(s.state.payment.charges,1);
 assert.equal(activateControl(s,'pay_fee','one-payment',getView(pending).renderId),s);
 s=click(s,'view_calendar');s=click(s,'undo_calendar');assert.equal(s.state.calendar.present,false);assert.equal(s.state.payment.status,'paid');
 s=click(s,'return_mail');assert.equal(getView(s).frameId,12);assert.equal(getView(s).completed,false);assert.match(getView(s).nativeText.copy_220,/日程已撤销/);
 s=click(s,'view_calendar');s=click(s,'undo_calendar');s=click(s,'return_mail');assert.equal(getView(s).completed,true);assert.equal(s.state.payment.charges,1);
});
test('history restores a whole service snapshot and restart invalidates old renders',()=>{
 let s=click(click(createSession({locale:'en'}),'open_mail'),'show_desktop');const before=s.state;
 s=click(s,'pay_fee');const paidRender=getView(s).renderId;s=goBack(s);assert.deepEqual(s.state,before);assert.notEqual(getView(s).renderId,paidRender);
 const clean=restart(s);assert.equal(clean.locale,'en');assert.equal(clean.state.payment.charges,0);assert.equal(clean.history.length,0);assert.notEqual(getView(clean).renderId,getView(createSession({locale:'en'})).renderId);
 assert.throws(()=>goBack(clean),{code:'no_history'});
});
test('all twelve scenes, native labels and service controls are exported for both locales',()=>{
 assert.equal(Object.keys(bundle.scenes).length,12);assert.equal(Object.keys(frames).length,12);assert.equal(scenario.phases.en.length,4);
 for(const [frame,spec]of Object.entries(frames)){
  const exported=bundle.scenes[frame];const actual=new Set(exported.mapping.elements.map(n=>n.source_id));
  for(const [id,pair]of Object.entries(spec.text)){assert.ok(actual.has(id));assert.ok(pair.cn);assert.ok(pair.en);assert.doesNotMatch(pair.en,/[\u3400-\u9fff]/);}
  for(const [id,control]of Object.entries(spec.controls)){assert.ok(actual.has(id));assert.ok(actual.has(id+'_control'));for(const tid of control.text_ids)assert.ok(actual.has(tid));}
 }
 for(const code of ['stale_render','disabled_control','unknown_control']){assert.ok(errorMessage({code},'cn'));assert.ok(errorMessage({code},'en'));}
});
test('each reachable native action preserves invariants and binds only current-frame targets',()=>{
 let queue=[createSession({locale:'en'})],seen=new Set(),visited=new Set(),executed=new Set();
 const key=s=>JSON.stringify(s.state);
 while(queue.length&&seen.size<180){const s=queue.shift(),k=key(s);if(seen.has(k))continue;seen.add(k);const view=verify(s);visited.add(view.frameId);
  for(const control of view.nativeControls){if(!control.enabled)continue;const next=click(s,control.sourceId);verify(next);executed.add(`${view.frameId}:${control.sourceId}`);if(!seen.has(key(next)))queue.push(next);}
  if(view.nextUpdate)queue.push(nextUpdate(s,`test-${++event}`));
 }
 assert.deepEqual([...visited].sort((a,b)=>a-b),Array.from({length:12},(_,i)=>i+1));
 for(const [frame,spec]of Object.entries(frames))for(const id of Object.keys(spec.controls))assert.ok(executed.has(`${frame}:${id}`),`${frame}:${id} never exercised`);
});

test('runtime frame05 keeps twelve pixels between cards and dock without shrinking native buttons',()=>{
 let s=click(click(createSession(),'open_mail'),'show_desktop');s=click(s,'undo_calendar');s=click(s,'restore_calendar');
 const view=getView(s);assert.equal(view.frameId,5);
 const payload=buildNativePayload(bundle,view,{assetBase:'http://127.0.0.1:8170/ux-images/',id:view.renderId});
 const nodes=Object.fromEntries(payload.mapping.elements.map(n=>[n.source_id,n]));
 const bounds=id=>nodes[id].bounds;const bottom=id=>bounds(id)[1]+bounds(id)[3];
 assert.ok(bounds('payment_card')[1]-bottom('calendar_card')>=12);
 assert.ok(bounds('dock')[1]-bottom('payment_card')>=12);
 for(const id of ['pay_fee','cancel_payment','view_payment']){
  assert.equal(bounds(id)[1],bounds(id+'_control')[1],id+' retains native hit target');
  assert.ok(bounds(id)[1]>=bounds('payment_card')[1]);assert.ok(bottom(id)<=bottom('payment_card'));
  const original=bundle.scenes['5'].mapping.elements.find(n=>n.source_id===id).bounds;
  assert.equal(bounds(id)[3],original[3],id+' keeps full button height');
  const label=getView(s).nativeControls.find(c=>c.sourceId===id).textIds[0];
  assert.ok(bounds(label)[1]>=bounds(id)[1]);assert.ok(bottom(label)<=bottom(id));
 }
 assert.ok(bounds('pay_fee')[1]-bottom('copy_31')>=12,'payee remains separated from payment actions');
});
