/** Bind the same compiled native L0/kit scenes to browser service state. */
const clone = value => structuredClone(value);
const escape = value => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const palette = {sage:0xff608570, panel:0xfffcfdfb, ink:0xff31413c, selected:0xfff0f5ef};

const english = {
  '1.5匹变频空调':'Inverter air conditioner', '一级能效 · 冷暖两用 · 安静睡眠':'Efficient · Heating & cooling · Quiet',
  '好物':'Good Things','送货上门 · 专业安装':'Home delivery · Expert installation','立即购买':'Buy now',
  '订单详情':'Order details','已付款':'Paid','到货后预约安装':'Book installation after delivery',
  '下单':'Ordered','待发货':'Awaiting dispatch','查看物流':'Track delivery','联系客服':'Contact support',
  '订单 · 已付款':'Order · Paid','预计周五送达':'Arriving Friday','来自购物订单':'From your shopping order',
  '查看订单':'View order','收起':'Dismiss','邮件':'Mail','日历':'Calendar','购物':'Shop','支付':'Pay',
  '物流 · 配送中':'Delivery · On the way','空调正在送往你家':'Your air conditioner is on its way',
  '已发货':'Dispatched','配送中':'In transit','已送达':'Delivered','联系配送员':'Contact courier','修改时间':'Change time',
  '安装服务 · 待预约':'Installation · Ready to book','空调已送达':'Your delivery is here',
  '请选择上门安装时间':'Choose an installation time','王师傅':'Mr Wang','王师傅 · 安装服务团队':'Mr Wang · Installation team',
  '选择时间':'Choose a time','暂不预约':'Not now','选择安装时间':'Choose installation time',
  '与项目例会冲突':'Conflicts with team meeting','日历空闲':'Your calendar is free','请选择安装时段':'Select an available time',
  '确认预约':'Confirm booking','取消':'Cancel','安装服务 · 预约成功':'Installation · Booked',
  '改约':'Reschedule','取消预约':'Cancel booking','日历 · 已更新':'Calendar · Updated','空调安装':'AC installation',
  '已加入家庭日历':'Added to your family calendar','确认':'Confirm','已确认':'Confirmed','撤销日程':'Undo calendar',
  '日历记录已撤销':'Calendar entry removed','安装预约仍然有效':'Your installation is still booked',
  '重新加入':'Restore event','安装服务 · 师傅在路上':'Installation · On the way','约20分钟后到达':'Arriving in about 20 minutes',
  '预约成功':'Booked','正在前往':'On the way','安装完成':'Completed','联系师傅':'Contact installer','查看预约':'View booking',
  '支付 · 待付款':'Payment · Awaiting approval','空调安装材料费':'Installation materials','加长铜管 2米':'Extra copper pipe · 2 m',
  '收款方：安装服务团队':'Payee: Installation team','安装服务单':'Installation invoice','支付 ¥130':'Pay ¥130','撤销':'Cancel',
  '安装服务 · 安装已完成':'Installation · Completed','反馈问题':'Report an issue','支付 · 已完成':'Payment · Completed',
  '已支付':'Paid','查看凭证':'View receipt','查看服务单':'View service record',
  '支付 · 请求已撤销':'Payment · Request cancelled','材料费尚未支付':'Materials remain unpaid','重新打开':'Reopen request',
  '已撤销':'Cancelled','安装服务 · 预约已取消':'Installation · Cancelled','安装预约已取消':'Booking cancelled',
  '日历中的关联日程已移除':'Linked calendar event removed','重新预约':'Book again','返回桌面':'Back to desktop',
  '购物应用':'Shopping','物流应用':'Delivery','安装服务':'Installation','日历应用':'Calendar','支付应用':'Payment',
  '详情预览':'Details','联系服务':'Contact service','配送安排':'Delivery time','安装预约':'Your booking',
  '服务单':'Service record','服务反馈':'Service feedback','付款凭证':'Payment receipt',
};

export function translate(text) {
  if (english[text]) return english[text];
  return text.replace(/家[\s·．.]*海棠路\s*18\s*号/g,'Home · 18 Haitang Road')
    .replace(/已送达/g,'Delivered').replace(/周([一二三四五六日])/g,(_,d)=>({一:'Mon',二:'Tue',三:'Wed',四:'Thu',五:'Fri',六:'Sat',日:'Sun'})[d])
    .replace(/9月(\d+)日/g, 'Sep $1').replace(/送达/g,' delivery').replace(/今天/g,'Today');
}

export function buildNativePayload(bundle, view, {assetBase, id}) {
  const state = view.state || view.renderProps.state;
  const frame = view.frameId || view.renderProps.frameId;
  const locale = view.locale || view.renderProps.locale;
  const raw = JSON.stringify(bundle.scenes[String(frame)]).replaceAll('__OCTOSENSE_ASSETS__/', assetBase);
  const scene = JSON.parse(raw);
  let card = scene.card;
  const {data, kit, mapping} = scene;
  const controls = scene.actions.controls;
  const placements = data.$kit.placements;
  let nodes = Object.fromEntries(mapping.elements.map(n => [n.source_id,n]));
  const style = (key, values) => {
    const placement=placements[key]; if(!placement)return;
    const old=placement.component, name=`${old}_live_${key}`;
    kit.components[name]=clone(kit.components[old]);Object.assign(kit.components[name].style,values);
    const definition=card.match(new RegExp(`component ${escape(old)}\\([^\\n]*\\) \\{\\n[^\\n]*\\n\\}\\n`));
    if(!definition)throw new Error(`Missing native component ${old}`);
    const newDefinition=definition[0].replace(`component ${old}(`,`component ${name}(`).replace(`component: "${old}"`,`component: "${name}"`);
    card=card.replace('\nview root ',`\n${newDefinition}\nview root `);
    card=card.replace(`${old}(instance: ${JSON.stringify(key)}`,`${name}(instance: ${JSON.stringify(key)}`);
    placement.component=name;
  };
  const text=(key,value,center) => {
    if(!placements[key])return;
    const pattern=new RegExp(`(copy ${escape(key)}_text \\{ class: user-copy, en: )"(?:[^"\\\\]|\\\\.)*"( \\})`);
    if(!pattern.test(card))throw new Error(`Missing native copy ${key}`);
    card=card.replace(pattern,(_,a,b)=>a+JSON.stringify(value)+b);nodes[key].text=value;
    if(center){
      const r=placements[center].layout;
      Object.assign(placements[key].layout,{x:r.x+5,w:r.w-10});style(key,{alignx:.5,tracking:0});
    }
  };
  const enabled=(key,value)=>{
    if(!controls[key])return;
    const control=`${key}_control`;
    card=card.replace(new RegExp(`(state ${escape(control)}_enabled \\{ shape: bool, initial: )(true|false)( \\})`),(_,a,_previous,c)=>a+String(Boolean(value))+c);
    nodes[control].enabled=Number(Boolean(value));controls[key].enabled=Boolean(value);
  };
  const button=(key,label,value)=>{
    if(!controls[key])return;
    if(label && controls[key].ocr_ids.length)text(`text_${controls[key].ocr_ids[0]}`,label,key);
    if(value!==undefined)enabled(key,value);
  };
  const remove=(key)=>{
    if(!placements[key])return;
    const pattern=new RegExp(`^([ \\t]*)[A-Za-z0-9_]+\\(instance: ${escape(JSON.stringify(key))}[^\\n]*\\n`,'m');
    const match=pattern.exec(card);if(!match)throw new Error(`Missing native instance ${key}`);
    let end=match.index+match[0].length;
    if(match[0].trimEnd().endsWith('{')){
      const closing=new RegExp(`^${escape(match[1])}\\}\\n`,'m').exec(card.slice(end));
      if(!closing)throw new Error('Unbalanced native instance');end+=closing.index+closing[0].length;
    }
    card=card.slice(0,match.index)+card.slice(end);
    const removed=new Set([key]);
    for(let changed=true;changed;){changed=false;for(const n of mapping.elements)if(removed.has(n.parent)&&!removed.has(n.source_id)){removed.add(n.source_id);changed=true;}}
    mapping.elements=mapping.elements.filter(n=>!removed.has(n.source_id));
    for(const k of removed){delete placements[k];delete controls[k];}
    nodes=Object.fromEntries(mapping.elements.map(n=>[n.source_id,n]));const counts={};
    for(const n of mapping.elements){const index=counts[n.parent]||0;counts[n.parent]=index+1;n.native_id=n.parent?`${nodes[n.parent].native_id}_${index}`:`beauty_${index}`;}
  };
  const booking=state.installation, calendar=state.calendar, payment=state.payment;
  if(frame===6||frame===7){
    const sunday=booking.selected_day==='2026-09-20', selected=booking.selected_slot_id;
    enabled('conflict_slot',sunday);enabled('afternoon',true);enabled('confirm_booking',Boolean(selected));
    for(const [key,active] of [['saturday',!sunday],['sunday',sunday]]){
      style(`${key}_surface`,{bg:active?palette.sage:palette.panel});
      for(const t of controls[key].ocr_ids)style(`text_${t}`,{color:active?0xffffffff:palette.ink});
    }
    const conflict=`text_${frame===6?72:126}`;
    text(conflict,sunday?'日历空闲':'与项目例会冲突');style(conflict,{color:sunday?0xff58816b:0xffbe873f});
    text(`text_${frame===6?76:130}`,selected?`${sunday?'周日 9月20日':'周六 9月19日'} · ${selected==='morning'?'09:00–11:00':'14:00–16:00'}`:'请选择安装时段');
    for(const [index,slot] of [[0,'morning'],[1,'afternoon']])style(`step_${index}`,{bg:selected===slot?palette.sage:palette.panel});
    style('afternoon_surface',{bg:selected==='afternoon'?palette.selected:palette.panel});
    style('conflict_slot_surface',{bg:selected==='morning'?palette.selected:palette.panel});
  }
  if(frame===8&&calendar.acknowledged)button('acknowledge_calendar','已确认',false);
  if([8,9,10].includes(frame)&&booking.booked_day==='2026-09-20')for(const n of mapping.elements)if(n.text?.includes('9月19日'))text(n.source_id,n.text.replaceAll('周六','周日').replaceAll('9月19日','9月20日'));
  if([8,9,10].includes(frame)&&booking.booked_slot_id){
    const slot=state.fixture.installation.slots.find(s=>s.id===booking.booked_slot_id);
    for(const n of mapping.elements)if(n.text&&(n.text.includes('月')||n.text.startsWith('今天')))text(n.source_id,n.text.replace(/\d\d:\d\d[-–]\d\d:\d\d/g,slot.label));
  }
  if([10,11,12].includes(frame)&&booking.booked_day==='2026-09-20'){
    const [date,dock]=({10:[84,98],11:[139,153],12:[195,208]})[frame];text(`text_${date}`,'9月20日 周日');text(`text_${dock}`,'20');
  }
  if(frame===5&&booking.status==='cancelled'){
    text('text_13','安装服务 · 预约已取消');text('text_14','安装预约已取消');text('text_15','日历中的关联日程已移除');button('choose_time','重新预约');
  }
  if(frame===11&&payment.status==='cancelled'){
    text('text_141','支付 · 请求已撤销');text('text_142','材料费尚未支付');button('pay_materials','重新打开',true);button('withdraw_payment_request','已撤销',false);
  }
  if(frame===3&&state.ui.dismissed_cards?.includes(`shopping:${state.order.id}`))remove('order_card');
  if(state.ui.surface==='app'&&!(state.ui.app==='shopping'&&['product','order'].includes(state.ui.page))){
    const app={shopping:'购物应用',logistics:'物流应用',installation:'安装服务',calendar:'日历应用',payment:'支付应用'}[state.ui.app];
    const page={detail:'详情预览',support:'联系服务',contact:'联系服务','delivery-time':'配送安排',booking:'安装预约','service-order':'服务单',feedback:'服务反馈',receipt:'付款凭证'}[state.ui.page]||'详情预览';
    const headers=mapping.elements.filter(n=>n.text&&n.parent==='screen').sort((a,b)=>a.bounds[1]-b.bounds[1]).slice(0,2);
    headers.forEach((n,i)=>{text(n.source_id,[app,page][i]);Object.assign(placements[n.source_id].layout,{x:24,y:24+i*40,w:350,h:30});style(n.source_id,{size:22,line_height:28,tracking:0});});
    const back=Object.keys(controls)[0];if(back)button(back,'返回桌面',true);
  }
  // The service view is authoritative for actions, labels, and availability.
  for(const control of view.nativeControls || []) {
    enabled(control.sourceId,control.enabled);
    if(control.textIds?.length===1 && placements[control.textIds[0]])
      text(control.textIds[0],control.label,control.sourceId);
  }
  // Latin copy is fitted into the same native component boxes. No raster text.
  if(locale==='en' && (frame===1||frame===2)){
    const key=frame===1?'text_2':'text_46';
    Object.assign(placements[key].layout,{x:100,w:206});style(key,{alignx:.5});
    if(frame===1)placements.text_4.layout.w=310;
    if(frame===2)placements.text_48.layout.w=210;
  }
  if(locale==='en')for(const n of mapping.elements){
    if(!n.text)continue;
    const translated=translate(n.text);
    const component=kit.components[placements[n.source_id].component];
    const resolve=v=>typeof v==='object'&&v?.$token?kit.tokens[v.$token]?.value:v;
    const size=resolve(component.style.size)||14;
    const width=placements[n.source_id].layout.w;
    const em=[...translated].reduce((sum,c)=>sum+(c===' '?.28:/[iljtfrI.,:·]/.test(c)?.3:/[WM]/.test(c)?.85:.56),0);
    const fitted=Math.min(size,Math.max(9,(width-3)/Math.max(1,em)));
    text(n.source_id,translated);style(n.source_id,{size:fitted,tracking:0});
  }
  for(const n of mapping.elements){const p=placements[n.source_id];n.bounds=['x','y','w','h'].map(k=>p.layout[k]||0);n.component=p.component;}
  return {id,frameId:frame,card,data,kit,mapping,width:406,height:776};
}
