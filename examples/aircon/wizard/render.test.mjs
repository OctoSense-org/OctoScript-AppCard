import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {buildNativePayload} from './render.mjs';
import {createSession, getView, activateControl, nextUpdate, dispatch} from './service.mjs';
const bundle=JSON.parse(readFileSync(new URL('./card-bundle/cards.bundle.json',import.meta.url)));
const render=view=>buildNativePayload(bundle,view,{assetBase:'https://example.test/wasm/service-cards/card-assets/',id:view.renderId||'test'});
const texts=payload=>payload.mapping.elements.filter(n=>n.text).map(n=>n.text);
const act=(s,id)=>activateControl(s,id);
function picker(){let s=createSession();s=act(s,'buy');s=act(s,'back');s=nextUpdate(s);s=nextUpdate(s);return act(s,'choose_time');}
function book(){return act(act(picker(),'afternoon'),'confirm_booking');}

test('twelve native scenes bind both languages without mutating the source atlas mapping',()=>{
  const before=JSON.stringify(bundle);
  for(let frameId=1;frameId<=12;frameId++)for(const locale of ['cn','en']){
    const state=JSON.parse(readFileSync(new URL(`../service/fixtures/${String(frameId).padStart(2,'0')}.state.json`,import.meta.url)));
    const p=render({state,locale,frameId});
    assert.ok(p.card.includes('view root'));
    assert.ok(!JSON.stringify(p).includes('127.0.0.1'));
    assert.ok(!JSON.stringify(p).includes('__OCTOSENSE_ASSETS__'));
    for(const n of p.mapping.elements){assert.ok(p.data.$kit.placements[n.source_id]);assert.ok(p.kit.components[n.component]);}
    if(locale==='en'){
      assert.equal(texts(p).filter(t=>/\p{Script=Han}/u.test(t)).length,0,`untranslated frame ${frameId}`);
      for(const n of p.mapping.elements.filter(n=>n.text))assert.ok(Number.isFinite(p.kit.components[n.component].style.size),'native font size must resolve to a finite number');
    }
  }
  assert.equal(JSON.stringify(bundle),before);
});
test('native enabled states follow conflict resolution and clear on a day change',()=>{
  let s=picker();let p=render(getView(s));
  assert.match(p.card,/state conflict_slot_control_enabled \{ shape: bool, initial: false/);
  assert.match(p.card,/state confirm_booking_control_enabled \{ shape: bool, initial: false/);
  s=act(s,'afternoon');s=act(s,'sunday');p=render(getView(s));
  assert.match(p.card,/state conflict_slot_control_enabled \{ shape: bool, initial: true/);
  assert.match(p.card,/state confirm_booking_control_enabled \{ shape: bool, initial: false/);
  s=act(s,'conflict_slot');s=act(s,'confirm_booking');p=render(getView(s));
  assert.ok(texts(p).some(t=>t.includes('周日 9月20日')&&t.includes('09:00–11:00')));
  assert.ok(!texts(p).some(t=>t.includes('周六 9月19日')));
});
test('native calendar and payment labels track acknowledgement and cancellation',()=>{
  let s=book();s=act(s,'acknowledge_calendar');let p=render(getView(s));
  assert.ok(texts(p).includes('已确认'));
  assert.match(p.card,/state acknowledge_calendar_control_enabled \{ shape: bool, initial: false/);
  s=nextUpdate(s);s=nextUpdate(s);s=act(s,'withdraw_payment_request');p=render(getView(s));
  assert.ok(texts(p).includes('材料费尚未支付'));assert.ok(texts(p).includes('重新打开'));
  assert.match(p.card,/state withdraw_payment_request_control_enabled \{ shape: bool, initial: false/);
});
test('dismissed cards are removed as native trees, while deferred installation remains actionable',()=>{
  let s=createSession();s=act(s,'buy');s=act(s,'back');s=act(s,'collapse');let p=render(getView(s));
  assert.ok(!p.mapping.elements.some(n=>n.source_id==='order_card'||n.source_id==='view_order_control'));
  assert.ok(!p.card.includes('instance: "order_card"'));
  s=picker();s=act(s,'close');s=act(s,'defer');p=render(getView(s));
  assert.ok(texts(p).includes('预约安装'));
});
test('receipt app uses readable native headers and a working back action',()=>{
  let s=nextUpdate(nextUpdate(book()));s=act(s,'pay_materials');s=act(s,'view_payment_receipt');const p=render(getView(s));
  assert.ok(texts(p).includes('付款凭证'));assert.ok(texts(p).includes('返回桌面'));
  const headers=p.mapping.elements.filter(n=>['支付应用','付款凭证'].includes(n.text));
  assert.deepEqual(headers.map(n=>n.bounds[1]).sort((a,b)=>a-b),[24,64]);
});
