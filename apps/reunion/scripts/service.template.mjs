export const scenario={id:'reunion',title:{en:'A reunion, all arranged',cn:'老同学，慢慢聚'},description:{en:'Choose a time, keep the calendar in sync, and settle your share',cn:'选好时间，同步日历，安心凑份子'},phases:{en:['The invitation','Your RSVP','The calendar','Your contribution'],cn:['收到邀请','选择时间','日历安排','聚会凑份子']}};
const clone=value=>JSON.parse(JSON.stringify(value));
const freeze=value=>{if(value&&typeof value==='object'){Object.values(value).forEach(freeze);Object.freeze(value);}return value;};
const choose=(locale,cn,en)=>locale==='cn'?cn:en;
const fail=code=>{throw Object.assign(new Error(code),{code});};
const fingerprint=value=>JSON.stringify(value);
const normalized=id=>String(id).replace(/_control$/,'');
const isRegistered=s=>s.reunion.rsvp==='confirmed';
export function createSession({locale='en'}={}){
 if(!['cn','en'].includes(locale))fail('LOCALE');
 return freeze({locale,epoch:0,sequence:0,history:[],seen:{},events:[],state:{ui:{surface:'app',frame:1},reunion:{id:'reunion-2016',organizer:'王宁',rsvp:'invited',preferredSlot:null,confirmed:false,confirmedSlot:null,venue:null},poll:{selected:null},calendar:{eventId:'calendar-reunion-2016',status:'absent',acknowledged:false,revision:0,event:null},payment:{id:'contribution-reunion-2016',eventId:'reunion-2016',status:'unrequested',amountMinor:18000,currency:'CNY',payee:'王宁',receipt:null}}});
}
function renderId(s){return `reunion-${s.epoch}-${s.sequence}`;}
function desktopFrame(state){return state.payment.status==='paid'?11:state.payment.status==='cancelled'?10:state.payment.status==='due'?9:state.reunion.confirmed?(state.calendar.status==='removed'?8:7):isRegistered(state)?6:3;}
function enabled(state,id){
 if(id==='friday')return false;
 if(['saturday','sunday'].includes(id))return !state.reunion.confirmed;
 if(id==='confirm_attendance')return !!state.poll.selected&&!state.reunion.confirmed;
 if(id==='ack_calendar')return state.calendar.status==='added'&&!state.calendar.acknowledged;
 if(id==='undo_calendar')return state.calendar.status==='added';
 if(id==='restore_calendar')return state.calendar.status==='removed';
 if(['pay_contribution','cancel_payment'].includes(id))return state.payment.status==='due';
 if(id==='reopen_payment')return state.payment.status==='cancelled';
 return true;
}
function navigate(session,frame){
 if(session.state.ui.frame!==frame)session.history.push(session.state.ui.frame);
 session.state.ui={surface:[1,2,12].includes(frame)?'app':'desktop',frame};
}
function finish(session,eventId,kind,payload,operation){
 if(typeof eventId!=='string'||!eventId.trim())fail('EVENT_ID');
 const fp=fingerprint({kind,payload});
 if(session.seen[eventId]){if(session.seen[eventId]!==fp)fail('ID_CONFLICT');return session;}
 const next=clone(session);operation(next);next.sequence+=1;next.seen[eventId]=fp;next.events.push({id:eventId,kind,payload:clone(payload),sequence:next.sequence});return freeze(next);
}
export function activateControl(session,sourceId,eventId,expectedRenderId){
 const id=normalized(sourceId),payload={sourceId:id,renderId:expectedRenderId};
 if(session.seen[eventId])return finish(session,eventId,'native',payload,()=>{});
 if(expectedRenderId!==renderId(session))fail('STALE');
 if(!FRAMES[session.state.ui.frame].controls[id])fail('UNKNOWN_CONTROL');
 if(!enabled(session.state,id))fail('DISABLED');
 return finish(session,eventId,'native',payload,next=>{
  const s=next.state;
  if(['open_invite','view_invite'].includes(id))navigate(next,2);
  else if(id==='back_messages')navigate(next,1);
  else if(id==='open_poll')navigate(next,desktopFrame(s));
  else if(id==='choose_time'){s.poll.selected=null;navigate(next,4);}
  else if(['saturday','sunday'].includes(id)){s.poll.selected=id;navigate(next,5);}
  else if(id==='reset_selection'){s.poll.selected=null;navigate(next,4);}
  else if(id==='back_poll')navigate(next,3);
  else if(id==='confirm_attendance'){s.reunion.rsvp='confirmed';s.reunion.preferredSlot=s.poll.selected;navigate(next,6);}
  else if(['group_info','view_registration','view_reunion'].includes(id))navigate(next,12);
  else if(['back_desktop','detail_back'].includes(id))navigate(next,desktopFrame(s));
  else if(id==='ack_calendar'){s.calendar.acknowledged=true;}
  else if(id==='undo_calendar'){s.calendar.status='removed';s.calendar.acknowledged=false;s.calendar.revision+=1;navigate(next,8);}
  else if(id==='restore_calendar'){s.calendar.status='added';s.calendar.acknowledged=false;s.calendar.revision+=1;navigate(next,7);}
  else if(id==='cancel_payment'){s.payment.status='cancelled';navigate(next,10);}
  else if(id==='reopen_payment'){s.payment.status='due';navigate(next,9);}
  else if(id==='pay_contribution'){
   s.payment.status='paid';s.payment.receipt={id:'REU-20261024-001',paymentId:s.payment.id,eventId:s.reunion.id,amountMinor:s.payment.amountMinor,currency:s.payment.currency,payee:s.payment.payee,purpose:'2016届同学聚会餐费',paidAt:'2026-10-21T10:18:00+08:00'};navigate(next,11);
  }else fail('UNKNOWN_CONTROL');
 });
}
function pendingUpdate(state){
 if(isRegistered(state)&&!state.reunion.confirmed)return 'organizer';
 if(state.reunion.confirmed&&state.payment.status==='unrequested')return 'contribution';
 return null;
}
export function nextUpdate(session,eventId){
 return finish(session,eventId,'external',{},next=>{
  const s=next.state,kind=pendingUpdate(s);if(!kind)fail('NO_UPDATE');
  if(kind==='organizer'){
   s.reunion.confirmed=true;s.reunion.confirmedSlot='saturday';s.reunion.venue={name:'木光餐厅',address:'桂花路8号'};
   s.calendar.status='added';s.calendar.acknowledged=false;s.calendar.revision+=1;
   s.calendar.event={id:s.calendar.eventId,sourceEventId:s.reunion.id,title:'2016届同学聚会',startsAt:'2026-10-24T18:30:00+08:00',endsAt:'2026-10-24T21:00:00+08:00',venue:'木光餐厅 · 桂花路8号',source:'王宁明确确认的场地与时间'};navigate(next,7);
  }else{s.payment.status='due';navigate(next,9);}
 });
}
export function goBack(session){
 if(!session.history.length)return session;
 const next=clone(session);let frame=next.history.pop();
 if(next.state.payment.status==='paid'&&[9,10].includes(frame))frame=11;
 if(next.state.reunion.confirmed&&[4,5,6].includes(frame))frame=desktopFrame(next.state);
 next.state.ui={frame,surface:[1,2,12].includes(frame)?'app':'desktop'};next.sequence+=1;return freeze(next);
}
export function restart(session){const next=clone(createSession({locale:session.locale}));next.epoch=session.epoch+1;return freeze(next);}
export function errorMessage(error,locale='en'){
 const messages={STALE:['这张卡片已更新，请使用当前操作','This card has changed. Use its current controls.'],DISABLED:['当前状态不能执行这个操作','This action is unavailable in the current state.'],ID_CONFLICT:['这个操作编号已用于另一个事件','This event ID already belongs to another action.'],EVENT_ID:['操作需要独立编号','Each action needs an event ID.'],UNKNOWN_CONTROL:['当前页面没有这个操作','This control is not on the current page.'],NO_UPDATE:['暂无新的组织者消息','No organizer update is pending.'],LOCALE:['请选择中文或英文','Choose Chinese or English.']};
 const value=messages[error?.code]||['操作未完成，请重试','The action could not be completed. Try again.'];return value[locale==='cn'?0:1];
}
const GUIDE={
1:['先打开同学群邀请','熟悉的消息列表，仍然是这次聚会的起点','Open the invitation','Begin in the familiar Messages inbox','open_invite'],
2:['从邀请进入投票','邀请内容保留在应用内，时间选择交给聚会卡片','Take the invitation to a poll','The original invitation stays in Messages; the reunion card handles time choices','open_poll'],
3:['在桌面选择时间','聚会服务把待决定的事项带到桌面','Choose from your desktop','The reunion service brings the decision to your desktop','choose_time'],
4:['避开已有安排','周五与工作例会冲突，选择空闲的周六或周日','Avoid the calendar conflict','Friday overlaps a work meeting; choose the free Saturday or Sunday slot','saturday'],
5:['确认你的参加意愿','当前选择只是偏好，确认后才提交报名','Confirm your RSVP','The selection is a preference; confirm to submit your RSVP','confirm_attendance'],
6:['等待组织者明确确认','报名已记录，场地确定前不会预填日历','Wait for the organizer','Your RSVP is recorded. The calendar waits for a confirmed venue and time',null],
7:['确认或撤销日历记录','组织者已确定场地与时间，日历操作独立于聚会报名','Review the calendar update','The organizer confirmed the time and venue; calendar controls are separate from your RSVP','ack_calendar'],
8:['撤销的只是日历记录','报名仍然有效，可以把同一个日程重新加入','Only the calendar entry was removed','Your RSVP remains active. Restore the same calendar event whenever you want','restore_calendar'],
9:['确认收款人与金额','聚会餐费 ¥180，收款人王宁，只有点击支付才会确认','Check the recipient and amount','Your ¥180 contribution goes to Wang Ning; payment needs your explicit action','pay_contribution'],
10:['支付已取消，报名保留','需要付款时，重新打开这张支付卡','Payment cancelled; RSVP retained','Reopen this payment card when you are ready to contribute','reopen_payment'],
11:['支付凭证已经保存','收款人、金额和活动记录固定保留，可打开聚会详情','Your receipt is saved','The recipient, amount and event remain fixed in the receipt','view_reunion'],
12:['回到应用看完整详情','消息、报名、日历与支付各自保留清楚的记录','See the complete event in the app','Messages, RSVP, calendar and payment keep their own clear records','back_desktop'],
};
export function getView(session){
 const {state:s,locale}=session,frameId=s.ui.frame,frame=FRAMES[frameId],cn=locale==='cn';
 const nativeText=Object.fromEntries(Object.entries(frame.texts).map(([id,t])=>[id,t[locale]]));
 const set=(id,zh,en)=>{if(id in nativeText)nativeText[id]=choose(locale,zh,en);};
 if(frameId===5&&s.poll.selected==='sunday')set('text_25','已选择 周日午餐','Selected: Sunday lunch');
 if(frameId===6&&s.reunion.preferredSlot==='sunday')set('text_73','周日 10月25日 12:00','Sun 25 Oct · 12:00');
 if([7,8].includes(frameId)&&s.reunion.preferredSlot==='sunday')set(frameId===7?'text_117':'text_174','王宁已改定周六','Organizer chose Saturday');
 if(frameId===7&&s.calendar.acknowledged){set('ack_label','已确认','Confirmed');set('text_119','日历 · 已确认','Calendar · confirmed');}
 if(frameId===12){
  set('text_193',s.reunion.confirmed?'已确认':isRegistered(s)?'已报名':'未报名',s.reunion.confirmed?'Confirmed':isRegistered(s)?'RSVP sent':'Not joined');
  if(!s.reunion.confirmed){set('text_188','场地待组织者确认','Venue awaiting confirmation');set('text_187',s.reunion.preferredSlot==='sunday'?'偏好 周日10月25日12:00':'暂定 周六10月24日18:30',s.reunion.preferredSlot==='sunday'?'Preferred: Sun 25 Oct, 12:00':'Proposed: Sat 24 Oct, 18:30');}
  if(s.payment.status!=='paid'){set('text_194',s.payment.status==='due'?'¥180 待支付':s.payment.status==='cancelled'?'支付已取消':'尚未发起',s.payment.status==='due'?'¥180 due':s.payment.status==='cancelled'?'Payment cancelled':'Not requested');set('text_197','暂无支付凭证','No receipt yet');}
 }
 const nativeEnabled={},nativeStyles={},nativeLayout={};
 const nativeControls=Object.entries(frame.controls).map(([sourceId,c])=>{
  const active=enabled(s,sourceId);nativeEnabled[sourceId+'_control']=active;
  const textIds=c.textIds;const label=textIds.length?nativeText[textIds[0]]:choose(locale,'返回','Back');
  if(sourceId==='confirm_attendance'||sourceId==='ack_calendar')nativeStyles[sourceId+'_surface']={bg:active?0xff608570:0xffdce4de};
  return {sourceId,label,enabled:active,textIds};
 });
 if([4,5].includes(frameId))for(const id of ['saturday','sunday']){
  nativeStyles[id+'_surface']={bg:s.poll.selected===id?0xffe8f0ea:0xfffcfdfb,bordercolor:0xff608570};
  nativeStyles[id+'_dot']={bg:s.poll.selected===id?0xff608570:0xfffcfdfb};
 }
 for(const [id,t]of Object.entries(frame.texts)){
  const dock=frame.dock[id];
  const text=nativeText[id],width=dock?64:t.bounds[2];let units=0;
  for(const c of text)units+=c.charCodeAt(0)>255?1:.55;
  nativeStyles[id]={...(nativeStyles[id]||{}),size:Math.min(t.size,dock?Math.max(10,(width-3)/Math.max(units,.5)):width/Math.max(units,.5))};
  if(dock){nativeLayout[id]={x:dock.center-width/2,w:width};nativeStyles[id].alignx=.5;}
 }
 const g=GUIDE[frameId],primary=nativeControls.find(c=>c.sourceId===g[4]&&c.enabled),update=pendingUpdate(s);
 return {renderId:renderId(session),frameId,locale,phase:s.payment.status!=='unrequested'?3:s.reunion.confirmed?2:isRegistered(s)||[4,5].includes(frameId)?1:0,state:clone(s),nativeControls,guidance:{title:g[cn?0:2],description:g[cn?1:3],primary:primary?{kind:'native',sourceId:primary.sourceId,label:primary.label}:null},nextUpdate:update?{label:update==='organizer'?choose(locale,'王宁确认场地与时间','Receive venue confirmation'):choose(locale,'王宁发来 ¥180 聚会餐费','Receive the ¥180 contribution request')}:null,canGoBack:session.history.length>0,completed:s.payment.status==='paid'&&frameId===12,nativeText,nativeEnabled,nativeStyles,nativeLayout};
}
