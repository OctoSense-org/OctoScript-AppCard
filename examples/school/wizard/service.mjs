/** Pure, local school-service demonstration. No network, timers, or payment operations. */
import {frames} from './copy.mjs';

const freeze = value => { if(value && typeof value==='object' && !Object.isFrozen(value)){Object.freeze(value);for(const child of Object.values(value))freeze(child);}return value; };
const clone = value => structuredClone(value);
const t = (locale,cn,en) => locale==='en'?en:cn;
export const scenario = freeze({id:'school',title:{cn:'林老师的一封邮件',en:'One email from Teacher Lin'},description:{cn:'日程已经更新，缴费由你决定；在邮件、桌面和应用间自然衔接',en:'The calendar is updated; payment stays your choice, across mail, desktop and apps'},phases:{cn:['读一封邮件','确认日程','处理缴费','回到邮件'],en:['Read the mail','Review the event','Handle the fee','Return to mail']}});
export const FIXTURE = freeze({teacher:{id:'teacher-lin',name:{cn:'林老师',en:'Teacher Lin'},authorized:['calendar.update']},event:{id:'school-science-day-2026-09-25',start:'2026-09-25T14:00:00+08:00',end:'2026-09-25T16:00:00+08:00',title:{cn:'秋季科学日',en:'Science Day'},calendar:'family'},invoice:{id:'school-materials-120',amount_minor:12000,currency:'CNY',payee:{cn:'北辰小学',en:'Beichen Primary'}},receiptId:'SC-120-0924'});
const appFrames=new Set([1,2,6,7,9,11,12]);
const guides={
1:['一封熟悉的来信','林老师有日历同步授权。打开邮件，看看活动安排和独立的缴费请求','A familiar email','Teacher Lin can update your calendar. Open the email to review the event and its separate fee'],
2:['邮件里就能行动','日历已根据授权更新；¥120 仍待你确认。两张卡片都可以直接打开对应应用','Act inside the email','Calendar access has added the event. The ¥120 fee still needs your choice. Each card opens its own app'],
3:['日历已经更新','确认只表示你已知晓。撤销只移除家庭日历记录，不会取消学校活动或替你付款','The calendar is updated','Confirm acknowledges the update. Undo removes your family event; it does not cancel the school event or pay the fee'],
4:['只撤销这条日程','学校活动和缴费请求继续保留。重新加入可恢复同一个日历事件','Undo just the calendar entry','The school event and fee remain. Restore brings back the same calendar event'],
5:['同一条日程已恢复','可以查看日历详情，也可以继续处理独立的缴费请求','The same event is restored','Review it inside Calendar, or continue with the separate payment request'],
6:['打开日历核对','时间、地点、家庭日历和来源邮件都在一起。撤销或恢复会同步到桌面卡片','Check the Calendar app','Time, place, family calendar and source mail stay connected. Undo or restore updates the desktop card too'],
7:['付款由你确认','核对学校、活动和 ¥120 金额。点击支付才记录这次本地演示付款；撤销不会扣款','Payment needs your choice','Check the school, event and ¥120 amount. Pay records this local demo payment; Cancel creates no charge'],
8:['请求已撤销，没有扣款','日历保持原状态。需要时重新打开同一张缴费单，金额不会重复累加','Cancelled, with no charge','Your calendar keeps its state. Reopen the same invoice whenever you are ready'],
9:['重新打开同一张缴费单','仍是学校活动材料费 ¥120；重新打开不等于支付，也不会创建第二张账单','The same invoice, reopened','The materials fee is still ¥120. Reopening neither pays nor creates another invoice'],
10:['桌面上的两件事','日历和支付各自展示服务状态。打开凭证核对这一笔付款','Two services on the desktop','Calendar and payment show their own state. Open the receipt to review this payment'],
11:['一笔付款，一张凭证','金额、收款学校和凭证号可直接查看，再回到原邮件检查结果','One payment, one receipt','Review the amount, school and receipt number, then return to the original email'],
12:['回到邮件，一切有迹可循','邮件里的日程和缴费卡片读取相同的服务记录，你随时可以打开详情','Back to mail, with a clear trail','The embedded calendar and fee cards use the same service records. Their details remain one tap away'],
};
function initialState(){return {fixture:clone(FIXTURE),ui:{frame:1,surface:'app'},mail:{id:'lin-science-day-mail',read:false,processedViewed:false},authorization:{calendarUpdate:true,autoPay:false},calendar:{id:FIXTURE.event.id,status:'added',present:true,acknowledged:false,restored:false,start:FIXTURE.event.start,end:FIXTURE.event.end,sourceMailId:'lin-science-day-mail'},payment:{id:FIXTURE.invoice.id,status:'pending',amount_minor:12000,currency:'CNY',reopened:false,charges:0,receipt:null,sourceMailId:'lin-science-day-mail'},desktopDelivered:false,receiptViewed:false};}
export function createSession({locale='cn'}={}){if(!['en','cn'].includes(locale))throw new TypeError('Unsupported locale');return freeze({schemaVersion:1,locale,epoch:0,revision:0,state:initialState(),history:[],events:[]});}
function renderId(s){return `school:${s.epoch}:${s.revision}:${s.state.ui.frame}`;}
function failure(code){const error=new Error(code);error.code=code;return error;}
function commit(s,state,eventId){return freeze({...s,revision:s.revision+1,state,history:[...s.history,clone(s.state)],events:eventId?[...s.events,eventId]:s.events});}
function setFrame(state,frame){state.ui={frame,surface:appFrames.has(frame)?'app':'desktop'};}
function desktopFrame(state){return state.payment.status==='paid'?10:state.payment.status==='cancelled'?8:!state.calendar.present?4:state.calendar.restored?5:3;}
function desktop(state){state.desktopDelivered=true;setFrame(state,desktopFrame(state));}
function mail(state){state.mail.read=true;if(state.payment.status==='paid'){state.mail.processedViewed=true;setFrame(state,12);}else setFrame(state,2);}
function payment(state){
 if(state.payment.status==='paid'){state.receiptViewed=true;setFrame(state,11);return;}
 // Explicitly opening a dismissed fee reopens the same invoice, without payment.
 if(state.payment.status==='cancelled'){state.payment.status='pending';state.payment.reopened=true;}
 setFrame(state,state.payment.reopened?9:7);
}
function enabled(state,id){
 if(id==='ack_calendar')return state.calendar.present&&!state.calendar.acknowledged;
 if(id==='restore_calendar')return !state.calendar.present;
 if(id==='pay_fee'||id==='cancel_payment')return state.payment.status==='pending';
 if(id==='reopen_payment')return state.payment.status==='cancelled';
 if(id==='view_receipt')return state.payment.status==='paid';
 return true;
}
function nativeCopy(state,locale){
 const frame=state.ui.frame;const out=Object.fromEntries(Object.entries(frames[frame].text).map(([id,pair])=>[id,pair[locale]]));
 const set=(index,cn,en)=>{const id=typeof index==='number'?`copy_${index}`:index;if(Object.hasOwn(out,id))out[id]=t(locale,cn,en);};
 const calIndex={2:69,3:121,4:174,5:22,6:92,8:190,10:103,12:212}[frame];
 if(calIndex){
  if(!state.calendar.present)set(calIndex,frame===6?'已移出家庭日历':'日历 · 已撤销',frame===6?'Removed':'Calendar · Undone');
  else if(frame===6)set(calIndex,'已加入日历','Added to calendar');
  else set(calIndex,state.calendar.restored?'日历 · 已重新加入':'日历 · 已更新',state.calendar.restored?'Calendar · Restored':'Calendar · Updated');
 }
 if(frame===3&&state.calendar.acknowledged)set(126,'已确认','Confirmed');
 if(frame===6&&!state.calendar.present)set(93,'重新加入','Restore');
 const paymentIndex={2:74,3:128,4:178,5:28,7:141,8:195,9:43,10:109,11:157,12:217}[frame];
 if(paymentIndex){
  if(state.payment.status==='paid')set(paymentIndex,frame===11?'已支付':'支付 · 已完成',frame===11?'Paid':'Payment · Paid');
  else if(state.payment.status==='cancelled')set(paymentIndex,'支付 · 请求已撤销','Payment · Cancelled');
  else if(frame===7)set(paymentIndex,'待付款','Unpaid');
  else if(frame===9)set(paymentIndex,'待付款 · 已重新打开','Unpaid · Reopened');
  else set(paymentIndex,'支付 · 待确认','Payment · Pending');
 }
 if(frame===2&&state.payment.status==='cancelled')set(77,'重新打开','Reopen');
 if(frame===8&&!state.calendar.present)set(197,'日历撤销状态保持不变','Calendar remains undone');
 if(frame===12&&!state.calendar.present)set(220,'已缴费 · 日程已撤销','Paid · Event undone');
 if(frame===1&&state.mail.read)set(10,'已读 · 查看活动安排','Read · View event plans');
 return out;
}
function primaryFor(state){const frame=state.ui.frame;
 return ({1:'open_mail',2:'show_desktop',3:state.calendar.acknowledged?'view_payment':'ack_calendar',4:'restore_calendar',5:'view_calendar',6:'show_desktop',7:'pay_fee',8:'reopen_payment',9:'pay_fee',10:'view_receipt',11:'return_mail',12:null})[frame];
}
export function getView(session){
 const state=clone(session.state),frameId=state.ui.frame,locale=session.locale,nativeText=nativeCopy(state,locale);
 const nativeControls=Object.entries(frames[frameId].controls).map(([sourceId,control])=>({sourceId,textIds:[...control.text_ids],enabled:enabled(state,sourceId),label:control.text_ids.length?control.text_ids.map(id=>nativeText[id]).join(' · '):sourceId}));
 const nativeEnabled=Object.fromEntries(nativeControls.map(control=>[control.sourceId,control.enabled]));
 const nativeStyles={};
 // Runtime-only spacing correction for the expanded desktop payment card.
 // Keep >=12 px above and below it; compress the generous pre-button gap,
 // preserving every Button's height and all text as native widgets.
 const nativeLayout=frameId===5?{
  payment_card:{y:367.6854368932039,h:296.86601941747574},
  pay_fee:{y:568.1165048543689},
  cancel_payment:{y:568.1165048543689},
  view_payment:{y:623.8679611650485},
 }:{};
 if(frameId===3&&state.calendar.acknowledged){nativeStyles.ack_calendar_surface={bg:0xffdfe9e2};nativeStyles.copy_126={color:0xff477d64};}
 if(frameId===1&&state.mail.read)nativeStyles.unread_dot={bg:0xffc6ccca};
 const guide=guides[frameId],primaryId=primaryFor(state),control=nativeControls.find(c=>c.sourceId===primaryId);
 const completed=state.payment.status==='paid'&&state.calendar.present&&state.mail.processedViewed;
 return freeze({schemaVersion:1,renderId:renderId(session),frameId,locale,phase:frameId<=2?0:frameId<=6?1:frameId<=9?2:3,state,nativeControls,nativeText,nativeEnabled,nativeStyles,nativeLayout,guidance:{title:guide[locale==='en'?2:0],description:guide[locale==='en'?3:1],primary:control?{kind:'native',sourceId:control.sourceId,label:control.label}:null},nextUpdate:frameId===2&&!state.desktopDelivered?{label:t(locale,'查看桌面服务卡片','Show desktop service cards')}:null,canGoBack:session.history.length>0,completed});
}
function checkEvent(session,eventId){if(typeof eventId!=='string'||!eventId.trim())throw failure('invalid_event');return session.events.includes(eventId);}
export function activateControl(session,sourceId,eventId,expectedRenderId){
 if(checkEvent(session,eventId))return session;
 if(expectedRenderId!==renderId(session))throw failure('stale_render');
 const control=getView(session).nativeControls.find(c=>c.sourceId===sourceId);
 if(!control)throw failure('unknown_control');if(!control.enabled)throw failure('disabled_control');
 const state=clone(session.state);
 switch(sourceId){
  case'open_mail':case'dock_mail':case'return_mail':mail(state);break;
  case'back_inbox':setFrame(state,1);break;
  case'show_desktop':desktop(state);break;
  case'dock_calendar':case'view_calendar':setFrame(state,6);break;
  case'dock_payment':case'view_payment':payment(state);break;
  case'ack_calendar':state.calendar.acknowledged=true;break;
  case'undo_calendar':
   if(state.calendar.present){state.calendar.present=false;state.calendar.status='removed';state.calendar.acknowledged=false;if(state.ui.frame!==6)desktop(state);}
   else{state.calendar.present=true;state.calendar.status='added';state.calendar.restored=true;state.calendar.acknowledged=false;}
   break;
  case'restore_calendar':state.calendar.present=true;state.calendar.status='added';state.calendar.restored=true;state.calendar.acknowledged=false;desktop(state);break;
  case'cancel_payment':state.payment.status='cancelled';desktop(state);break;
  case'reopen_payment':state.payment.status='pending';state.payment.reopened=true;setFrame(state,9);break;
  case'pay_fee':
   state.payment.status='paid';state.payment.charges=1;state.payment.receipt={id:FIXTURE.receiptId,invoiceId:state.payment.id,amount_minor:state.payment.amount_minor,currency:state.payment.currency,paidAt:'2026-09-24T09:50:00+08:00'};desktop(state);break;
  case'view_receipt':state.receiptViewed=true;setFrame(state,11);break;
  default:throw failure('unknown_control');
 }
 return commit(session,state,eventId);
}
export function nextUpdate(session,eventId){if(checkEvent(session,eventId))return session;if(!getView(session).nextUpdate)throw failure('no_update');const state=clone(session.state);desktop(state);return commit(session,state,eventId);}
export function goBack(session){if(!session.history.length)throw failure('no_history');return freeze({...session,revision:session.revision+1,state:clone(session.history.at(-1)),history:session.history.slice(0,-1)});}
export function restart(session){const clean=createSession({locale:session.locale});return freeze({...clean,epoch:session.epoch+1});}
export function errorMessage(error,locale='cn'){const messages={invalid_event:['操作标识无效，请重试','Invalid action identifier. Please retry'],stale_render:['卡片已更新，请使用当前操作','This card changed. Use the current action'],unknown_control:['当前界面没有这个操作','This action is not on the current screen'],disabled_control:['这个操作当前不可用','This action is currently unavailable'],no_update:['目前没有新的服务更新','There is no new service update'],no_history:['已经是第一步','You are at the first step']};const pair=messages[error?.code]||['操作未完成，请重试','The action could not finish. Please retry'];return pair[locale==='en'?1:0];}
