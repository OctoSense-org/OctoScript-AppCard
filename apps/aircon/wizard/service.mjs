/** Pure browser service state for native Makepad cards. No timers or service IO.
 * Domain JSON intentionally matches service/controller.py, including SHA-256
 * event fingerprints. Session history belongs to the guided local demonstration.
 */
export const DEFAULT_FIXTURE = {
  "schema_version": 1,
  "scenario": "aircon-fresh",
  "locale": "zh-CN",
  "timezone": "Asia/Shanghai",
  "simulation": true,
  "customer": {
    "name": "Alex",
    "address": "家 · 海棠路 18 号"
  },
  "order": {
    "id": "order-aircon-001",
    "product": "1.5匹变频空调",
    "amount_minor": 279900,
    "currency": "CNY"
  },
  "delivery": {
    "id": "delivery-aircon-001",
    "starts_at": "2026-09-18T14:00:00+08:00",
    "ends_at": "2026-09-18T16:00:00+08:00",
    "delivered_at": "2026-09-18T15:20:00+08:00"
  },
  "installation": {
    "id": "booking-aircon-001",
    "technician": "王师傅",
    "provider": "安装服务团队",
    "days": [
      {
        "date": "2026-09-19",
        "label": "周六 9月19日"
      },
      {
        "date": "2026-09-20",
        "label": "周日 9月20日"
      }
    ],
    "slots": [
      {
        "id": "morning",
        "label": "09:00–11:00",
        "starts_at": "2026-09-19T09:00:00+08:00",
        "ends_at": "2026-09-19T11:00:00+08:00"
      },
      {
        "id": "afternoon",
        "label": "14:00–16:00",
        "starts_at": "2026-09-19T14:00:00+08:00",
        "ends_at": "2026-09-19T16:00:00+08:00"
      }
    ]
  },
  "calendar": {
    "installation_event_id": "calendar-installation-aircon-001",
    "existing_events": [
      {
        "id": "calendar-project-meeting",
        "title": "项目例会",
        "starts_at": "2026-09-19T09:00:00+08:00",
        "ends_at": "2026-09-19T11:00:00+08:00"
      }
    ]
  },
  "payment": {
    "id": "invoice-materials-aircon-001",
    "description": "加长铜管 2米",
    "amount_minor": 13000,
    "currency": "CNY",
    "payee": "安装服务团队"
  },
  "authorizations": {
    "calendar_sync_from_confirmed_installation": true,
    "automatic_payment": false
  },
  "source": {
    "flow_id": "aircon-fresh-v2",
    "atlas_sha256": "168eb235aefdd446b1f9941b15107d7b6ca2a1ff88ec5d437801d2ea2ee0abf5",
    "source_frame_count": 12
  }
};
const FRAME_CONTROLS = {
  "1": [
    {
      "sourceId": "buy",
      "action": "shopping.buy",
      "enabled": true,
      "cn": "立即购买",
      "en": "Buy now",
      "textIds": [
        "text_9"
      ]
    }
  ],
  "2": [
    {
      "sourceId": "back",
      "action": "navigation.desktop",
      "enabled": true,
      "cn": "返回",
      "en": "Back",
      "textIds": []
    },
    {
      "sourceId": "view_logistics",
      "action": "navigation.logistics",
      "enabled": true,
      "cn": "查看物流",
      "en": "Track order",
      "textIds": [
        "text_61"
      ]
    },
    {
      "sourceId": "support",
      "action": "navigation.support",
      "enabled": true,
      "cn": "联系客服",
      "en": "Contact service",
      "textIds": [
        "text_62"
      ]
    }
  ],
  "3": [
    {
      "sourceId": "view_order",
      "action": "navigation.order",
      "enabled": true,
      "cn": "查看订单",
      "en": "View order",
      "textIds": [
        "text_110"
      ]
    },
    {
      "sourceId": "collapse",
      "action": "card.dismiss",
      "enabled": true,
      "cn": "收起",
      "en": "Dismiss",
      "textIds": [
        "text_111"
      ]
    }
  ],
  "4": [
    {
      "sourceId": "courier",
      "action": "navigation.courier",
      "enabled": true,
      "cn": "联系配送员",
      "en": "Contact courier",
      "textIds": [
        "text_169"
      ]
    },
    {
      "sourceId": "delivery_time",
      "action": "navigation.delivery_time",
      "enabled": true,
      "cn": "修改时间",
      "en": "Delivery time",
      "textIds": [
        "text_170"
      ]
    }
  ],
  "5": [
    {
      "sourceId": "choose_time",
      "action": "installation.open_slots",
      "enabled": true,
      "cn": "选择时间",
      "en": "Choose time",
      "textIds": [
        "text_19"
      ]
    },
    {
      "sourceId": "defer",
      "action": "installation.defer",
      "enabled": true,
      "cn": "暂不预约",
      "en": "Not now",
      "textIds": [
        "text_20"
      ]
    }
  ],
  "6": [
    {
      "sourceId": "close",
      "action": "installation.close_slots",
      "enabled": true,
      "cn": "关闭",
      "en": "Close",
      "textIds": []
    },
    {
      "sourceId": "saturday",
      "action": "installation.choose_day",
      "enabled": true,
      "cn": "周六 9月19日",
      "en": "Sat · Sep 19",
      "textIds": [
        "text_69"
      ]
    },
    {
      "sourceId": "sunday",
      "action": "installation.choose_day",
      "enabled": true,
      "cn": "周日 9月20日",
      "en": "Sun · Sep 20",
      "textIds": [
        "text_70"
      ]
    },
    {
      "sourceId": "conflict_slot",
      "action": "installation.choose_slot",
      "enabled": false,
      "cn": "09:00-11:00",
      "en": "09:00–11:00",
      "textIds": [
        "text_71",
        "text_72"
      ]
    },
    {
      "sourceId": "afternoon",
      "action": "installation.choose_slot",
      "enabled": true,
      "cn": "14:00-16:00",
      "en": "14:00–16:00",
      "textIds": [
        "text_73",
        "text_74"
      ]
    },
    {
      "sourceId": "confirm_booking",
      "action": "installation.confirm",
      "enabled": false,
      "cn": "确认预约",
      "en": "Confirm booking",
      "textIds": [
        "text_77"
      ]
    }
  ],
  "7": [
    {
      "sourceId": "close",
      "action": "installation.close_slots",
      "enabled": true,
      "cn": "关闭",
      "en": "Close",
      "textIds": []
    },
    {
      "sourceId": "saturday",
      "action": "installation.choose_day",
      "enabled": true,
      "cn": "周六 9月19日",
      "en": "Sat · Sep 19",
      "textIds": [
        "text_123"
      ]
    },
    {
      "sourceId": "sunday",
      "action": "installation.choose_day",
      "enabled": true,
      "cn": "周日 9月20日",
      "en": "Sun · Sep 20",
      "textIds": [
        "text_124"
      ]
    },
    {
      "sourceId": "conflict_slot",
      "action": "installation.choose_slot",
      "enabled": false,
      "cn": "09:00-11:00",
      "en": "09:00–11:00",
      "textIds": [
        "text_125",
        "text_126"
      ]
    },
    {
      "sourceId": "afternoon",
      "action": "installation.choose_slot",
      "enabled": true,
      "cn": "14:00-16:00",
      "en": "14:00–16:00",
      "textIds": [
        "text_127",
        "text_128"
      ]
    },
    {
      "sourceId": "cancel_selection",
      "action": "installation.close_slots",
      "enabled": true,
      "cn": "取消",
      "en": "Cancel",
      "textIds": [
        "text_131"
      ]
    },
    {
      "sourceId": "confirm_booking",
      "action": "installation.confirm",
      "enabled": true,
      "cn": "确认预约",
      "en": "Confirm booking",
      "textIds": [
        "text_132"
      ]
    }
  ],
  "8": [
    {
      "sourceId": "reschedule",
      "action": "installation.open_slots",
      "enabled": true,
      "cn": "改约",
      "en": "Reschedule",
      "textIds": [
        "text_182"
      ]
    },
    {
      "sourceId": "cancel_booking",
      "action": "installation.cancel",
      "enabled": true,
      "cn": "取消预约",
      "en": "Cancel booking",
      "textIds": [
        "text_183"
      ]
    },
    {
      "sourceId": "acknowledge_calendar",
      "action": "calendar.acknowledge",
      "enabled": true,
      "cn": "确认",
      "en": "Confirm",
      "textIds": [
        "text_188"
      ]
    },
    {
      "sourceId": "undo_calendar",
      "action": "calendar.undo",
      "enabled": true,
      "cn": "撤销日程",
      "en": "Undo event",
      "textIds": [
        "text_189"
      ]
    }
  ],
  "9": [
    {
      "sourceId": "reschedule",
      "action": "installation.open_slots",
      "enabled": true,
      "cn": "改约",
      "en": "Reschedule",
      "textIds": [
        "text_32"
      ]
    },
    {
      "sourceId": "cancel_booking",
      "action": "installation.cancel",
      "enabled": true,
      "cn": "取消预约",
      "en": "Cancel booking",
      "textIds": [
        "text_33"
      ]
    },
    {
      "sourceId": "restore_calendar",
      "action": "calendar.restore",
      "enabled": true,
      "cn": "重新加入",
      "en": "Restore event",
      "textIds": [
        "text_36"
      ]
    }
  ],
  "10": [
    {
      "sourceId": "contact_technician",
      "action": "navigation.technician",
      "enabled": true,
      "cn": "联系师傅",
      "en": "Contact installer",
      "textIds": [
        "text_95"
      ]
    },
    {
      "sourceId": "view_booking",
      "action": "navigation.booking",
      "enabled": true,
      "cn": "查看预约",
      "en": "View booking",
      "textIds": [
        "text_96"
      ]
    }
  ],
  "11": [
    {
      "sourceId": "source_service_order",
      "action": "navigation.service_order",
      "enabled": true,
      "cn": "安装服务单",
      "en": "Service order",
      "textIds": [
        "text_146"
      ]
    },
    {
      "sourceId": "pay_materials",
      "action": "payment.pay",
      "enabled": true,
      "cn": "支付 ¥130",
      "en": "Pay ¥130",
      "textIds": [
        "text_148"
      ]
    },
    {
      "sourceId": "withdraw_payment_request",
      "action": "payment.cancel",
      "enabled": true,
      "cn": "撤销",
      "en": "Cancel",
      "textIds": [
        "text_149"
      ]
    },
    {
      "sourceId": "report_installation_issue",
      "action": "navigation.service_feedback",
      "enabled": true,
      "cn": "反馈问题",
      "en": "Report an issue",
      "textIds": [
        "text_152"
      ]
    }
  ],
  "12": [
    {
      "sourceId": "source_service_order",
      "action": "navigation.service_order",
      "enabled": true,
      "cn": "安装服务单",
      "en": "Service order",
      "textIds": [
        "text_203"
      ]
    },
    {
      "sourceId": "view_payment_receipt",
      "action": "navigation.payment_receipt",
      "enabled": true,
      "cn": "查看凭证",
      "en": "View receipt",
      "textIds": [
        "text_204"
      ]
    },
    {
      "sourceId": "view_service_order",
      "action": "navigation.service_order",
      "enabled": true,
      "cn": "查看服务单",
      "en": "View service",
      "textIds": [
        "text_207"
      ]
    }
  ]
};
const clone = value => structuredClone(value);
const same = (a, b) => canonical(a) === canonical(b);
const own = (object, key) => Object.hasOwn(object, key);
const PROVIDER = new Set(['logistics.out_for_delivery', 'logistics.delivered', 'installation.technician_departed', 'installation.completed']);
const USER = new Set(['order.purchase_demo', 'navigation.open_app', 'navigation.desktop', 'card.dismiss', 'installation.open_slots', 'installation.choose_slot', 'installation.close_slots', 'installation.defer', 'installation.confirm', 'installation.choose_day', 'installation.reschedule', 'installation.cancel', 'calendar.acknowledge', 'calendar.undo', 'calendar.restore', 'payment.pay', 'payment.cancel', 'payment.reopen']);
const ROUTES = {
  'navigation.order': ['shopping', 'order'], 'navigation.logistics': ['logistics', 'detail'],
  'navigation.support': ['shopping', 'support'], 'navigation.courier': ['logistics', 'contact'],
  'navigation.delivery_time': ['logistics', 'delivery-time'], 'navigation.technician': ['installation', 'contact'],
  'navigation.booking': ['installation', 'booking'], 'navigation.service_order': ['installation', 'service-order'],
  'navigation.service_feedback': ['installation', 'feedback'], 'navigation.payment_receipt': ['payment', 'receipt'],
};
export class ServiceError extends Error {
  constructor(code, cn, en = 'This action is not available in the current state') {
    super(cn); this.name = 'ServiceError'; this.code = code; this.messages = {cn, en};
  }
}
function require(condition, code, cn, en) { if (!condition) throw new ServiceError(code, cn, en); }
export const errorMessage = (error, locale = 'cn') => error.messages?.[locale === 'en' ? 'en' : 'cn'] ?? error.message;
const object = value => value !== null && typeof value === 'object' && !Array.isArray(value);
function canonical(value) {
  if (Array.isArray(value)) return '[' + value.map(canonical).join(',') + ']';
  if (object(value)) return '{' + Object.keys(value).sort().map(key => JSON.stringify(key) + ':' + canonical(value[key])).join(',') + '}';
  return JSON.stringify(value);
}

/** Synchronous SHA-256 for short UTF-8 event JSON, also available in the browser.
 * This is a deduplication fingerprint, not an authentication mechanism.
 */
export function eventFingerprint(event) {
  const bytes = new TextEncoder().encode(canonical(event));
  const length = Math.ceil((bytes.length + 9) / 64) * 64;
  const data = new Uint8Array(length); data.set(bytes); data[bytes.length] = 0x80;
  const memory = new DataView(data.buffer);
  memory.setUint32(length - 8, Math.floor(bytes.length / 0x20000000));
  memory.setUint32(length - 4, (bytes.length * 8) >>> 0);
  const hash = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
  const constants = [0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
  const rotate = (x, n) => (x >>> n) | (x << (32 - n));
  for (let offset = 0; offset < length; offset += 64) {
    const words = new Uint32Array(64);
    for (let i = 0; i < 16; i++) words[i] = memory.getUint32(offset + i * 4);
    for (let i = 16; i < 64; i++) {
      const a = words[i - 15], b = words[i - 2];
      words[i] = (words[i - 16] + (rotate(a, 7) ^ rotate(a, 18) ^ (a >>> 3)) + words[i - 7] + (rotate(b, 17) ^ rotate(b, 19) ^ (b >>> 10))) >>> 0;
    }
    let [a,b,c,d,e,f,g,h] = hash;
    for (let i = 0; i < 64; i++) {
      const first = (h + (rotate(e,6) ^ rotate(e,11) ^ rotate(e,25)) + ((e & f) ^ (~e & g)) + constants[i] + words[i]) >>> 0;
      const second = ((rotate(a,2) ^ rotate(a,13) ^ rotate(a,22)) + ((a & b) ^ (a & c) ^ (b & c))) >>> 0;
      h=g; g=f; f=e; e=(d+first)>>>0; d=c; c=b; b=a; a=(first+second)>>>0;
    }
    [a,b,c,d,e,f,g,h].forEach((word,i) => { hash[i] = (hash[i] + word) >>> 0; });
  }
  return hash.map(word => word.toString(16).padStart(8, '0')).join('');
}

export function initialState(fixture = DEFAULT_FIXTURE) {
  fixture = clone(fixture);
  return {schema_version:1, scenario:fixture.scenario, simulation:true, revision:0, fixture, processed_events:{}, effects:[],
    ui:{surface:'app',app:'shopping',page:'product',slot_picker:false,installation_deferred:false,dismissed_cards:[]},
    order:{id:fixture.order.id,status:'not_placed'}, delivery:{id:fixture.delivery.id,status:'not_dispatched'},
    installation:{id:fixture.installation.id,status:'not_available',selected_slot_id:null,booked_slot_id:null,selected_day:fixture.installation.days[0].date,booked_day:null,version:0},
    calendar:{events:Object.fromEntries(fixture.calendar.existing_events.map(event => [event.id,event])),installation_sync:'not_added',acknowledged:false},
    payment:{id:fixture.payment.id,status:'not_due',receipt:null}};
}
function slot(state, id, day = state.installation.selected_day) {
  const item = state.fixture.installation.slots.find(value => value.id === id);
  return item ? {...item,starts_at:day+item.starts_at.slice(10),ends_at:day+item.ends_at.slice(10)} : null;
}
export function availableSlots(state) {
  return state.fixture.installation.slots.map(base => {
    const item = slot(state,base.id);
    const conflicts = Object.values(state.calendar.events).filter(event => event.id !== state.fixture.calendar.installation_event_id && Date.parse(item.starts_at) < Date.parse(event.ends_at) && Date.parse(event.starts_at) < Date.parse(item.ends_at));
    return {...item,enabled:conflicts.length===0,conflict_event_ids:conflicts.map(event=>event.id),reason:conflicts.map(event=>event.title).join('、'),selected:item.id===state.installation.selected_slot_id};
  });
}
function effect(state, kind, entity_id, detail = {}) { state.effects.push({kind,entity_id,simulation:true,...detail}); }
function calendarUpsert(state) {
  const booking=state.installation, selected=slot(state,booking.booked_slot_id,booking.booked_day);
  const calendarId=state.fixture.calendar.installation_event_id;
  const event={id:calendarId,title:'空调上门安装',starts_at:selected.starts_at,ends_at:selected.ends_at,source_app:'installation',source_entity_id:booking.id,booking_version:booking.version};
  if (!same(state.calendar.events[calendarId],event)) { state.calendar.events[calendarId]=event; effect(state,'calendar.upsert',calendarId); }
  state.calendar.installation_sync='added';
}

/** Apply an owned user/provider event without mutating state. */
export function reduce(state, event) {
  require(object(event),'invalid_event','事件必须是 JSON 对象');
  const {id:messageId,action,actor}=event, payload=own(event,'payload')?event.payload:{};
  require(typeof messageId==='string' && messageId.length>0,'missing_id','事件需要唯一 id');
  require(USER.has(action)||PROVIDER.has(action),'unknown_action','未知操作');
  require(object(payload),'invalid_payload','payload 必须是 JSON 对象');
  require(actor===(PROVIDER.has(action)?'provider':'user'),'wrong_actor','操作来源不匹配','Only the owner of this action may perform it');
  const digest=eventFingerprint(event);
  if (own(state.processed_events,messageId)) {
    require(state.processed_events[messageId]===digest,'reused_id','同一事件 id 不得复用于不同内容','This event ID was already used for a different action');
    return clone(state);
  }
  const out=clone(state), {order,delivery,installation:booking,calendar,payment,ui,fixture}=out;
  if (action==='order.purchase_demo') {
    if (order.status==='not_placed') { order.status='paid_demo'; effect(out,'order.create_demo',order.id,{amount_minor:fixture.order.amount_minor}); }
    Object.assign(ui,{surface:'app',app:'shopping',page:'order',slot_picker:false});
  } else if (action==='navigation.open_app') {
    const app=payload.app;
    require(['shopping','logistics','installation','calendar','payment'].includes(app),'unknown_app','未知应用');
    let page=payload.page ?? (app==='shopping'&&order.status==='not_placed'?'product':'detail');
    if (app==='shopping'&&page!=='product') { require(order.status!=='not_placed','no_order','订单尚未创建'); if(page==='detail')page='order'; }
    Object.assign(ui,{surface:'app',app,page,slot_picker:false});
  } else if (action==='navigation.desktop') {
    require(order.status!=='not_placed','no_order','请先创建演示订单'); Object.assign(ui,{surface:'desktop',app:null,page:null,slot_picker:false});
  } else if (action==='card.dismiss') {
    const visible=serviceCards(out).some(card=>card.id===payload.card_id);
    require(visible||ui.dismissed_cards.includes(payload.card_id),'missing_card','该卡片当前不可见');
    if (!ui.dismissed_cards.includes(payload.card_id)) ui.dismissed_cards.push(payload.card_id);
  } else if (action==='logistics.out_for_delivery') {
    require(order.status!=='not_placed','no_order','订单尚未创建');
    if(delivery.status==='not_dispatched') { delivery.status='out_for_delivery'; effect(out,'logistics.update',delivery.id,{status:delivery.status}); }
  } else if (action==='logistics.delivered') {
    require(order.status!=='not_placed','no_order','订单尚未创建');
    if(delivery.status!=='delivered') { Object.assign(delivery,{status:'delivered',delivered_at:fixture.delivery.delivered_at}); booking.status='available'; effect(out,'logistics.update',delivery.id,{status:'delivered'}); }
  } else if (['installation.open_slots','installation.reschedule'].includes(action)) {
    require(['available','booked','cancelled'].includes(booking.status),'unavailable_booking','当前不可选择安装时段');
    ui.slot_picker=true; ui.installation_deferred=false; booking.selected_slot_id=booking.booked_slot_id; booking.selected_day=booking.booked_day||fixture.installation.days[0].date;
  } else if(action==='installation.choose_day') {
    require(ui.slot_picker,'closed_picker','请先展开安装时段');
    require(fixture.installation.days.some(day=>day.date===payload.date),'unknown_day','该日期暂无服务时段');
    if(payload.date!==booking.selected_day) { booking.selected_day=payload.date; booking.selected_slot_id=null; }
  } else if(action==='installation.choose_slot') {
    require(ui.slot_picker,'closed_picker','请先展开安装时段');
    const candidate=availableSlots(out).find(item=>item.id===payload.slot_id);
    require(candidate,'unknown_slot','未知安装时段'); require(candidate.enabled,'calendar_conflict','该时段与日历中的'+candidate.reason+'冲突','This time conflicts with your calendar'); booking.selected_slot_id=candidate.id;
  } else if(['installation.close_slots','installation.defer'].includes(action)) {
    ui.slot_picker=false; booking.selected_slot_id=booking.booked_slot_id; booking.selected_day=booking.booked_day||fixture.installation.days[0].date;
    if(action==='installation.defer')ui.installation_deferred=true;
  } else if(action==='installation.confirm') {
    require(['available','booked','cancelled'].includes(booking.status),'unavailable_booking','当前不可确认安装预约');
    const candidate=availableSlots(out).find(item=>item.id===booking.selected_slot_id);
    require(candidate,'no_selection','请选择安装时段','Choose an installation time first'); require(candidate.enabled,'calendar_conflict','所选时段已产生冲突，请重新选择','Your calendar changed; choose a free time');
    if(booking.status!=='booked'||booking.booked_slot_id!==booking.selected_slot_id||booking.booked_day!==booking.selected_day) {
      Object.assign(booking,{status:'booked',booked_slot_id:booking.selected_slot_id,booked_day:booking.selected_day,version:booking.version+1});
      effect(out,'installation.upsert',booking.id,{slot_id:booking.selected_slot_id,version:booking.version});
      if(fixture.authorizations.calendar_sync_from_confirmed_installation) { calendarUpsert(out); calendar.acknowledged=false; }
    }
    ui.slot_picker=false;
  } else if(action==='installation.cancel') {
    require(['booked','cancelled'].includes(booking.status),'cannot_cancel_booking','当前阶段不可直接取消安装预约');
    if(booking.status==='booked') {
      Object.assign(booking,{status:'cancelled',selected_slot_id:null,booked_slot_id:null,booked_day:null}); effect(out,'installation.cancel',booking.id);
      const calendarId=fixture.calendar.installation_event_id;
      if(own(calendar.events,calendarId)) { delete calendar.events[calendarId]; effect(out,'calendar.remove',calendarId); }
      Object.assign(calendar,{installation_sync:'cancelled_with_booking',acknowledged:false});
    }
    ui.slot_picker=false;
  } else if(action==='calendar.acknowledge') {
    require(calendar.installation_sync==='added','missing_calendar','没有可确认的日历更新'); calendar.acknowledged=true;
  } else if(action==='calendar.undo') {
    require(['added','undone'].includes(calendar.installation_sync),'missing_calendar','尚无可撤销的安装日程');
    const calendarId=fixture.calendar.installation_event_id;
    if(own(calendar.events,calendarId)) { delete calendar.events[calendarId]; effect(out,'calendar.remove',calendarId); }
    Object.assign(calendar,{installation_sync:'undone',acknowledged:false});
  } else if(action==='calendar.restore') {
    require(booking.booked_slot_id!==null,'missing_booking','尚无安装预约可关联'); calendarUpsert(out);
  } else if(action==='installation.technician_departed') {
    require(['booked','en_route','completed'].includes(booking.status),'missing_booking','师傅出发前需要有效预约');
    if(booking.status==='booked') { booking.status='en_route'; effect(out,'installation.progress',booking.id,{status:'en_route'}); }
  } else if(action==='installation.completed') {
    require(['booked','en_route','completed'].includes(booking.status),'missing_booking','安装尚未预约');
    if(booking.status!=='completed') { booking.status='completed'; payment.status='pending'; effect(out,'installation.progress',booking.id,{status:'completed'}); effect(out,'payment.invoice_created',payment.id,{amount_minor:fixture.payment.amount_minor}); }
  } else if(action==='payment.pay') {
    require(['pending','paid'].includes(payment.status),'not_payable','当前没有待支付请求');
    require(payload.invoice_id===payment.id,'invoice_changed','支付单号不匹配');
    require(Number.isSafeInteger(payload.amount_minor)&&payload.amount_minor===fixture.payment.amount_minor,'amount_changed','支付金额已变化，请重新确认','The amount changed; review the current invoice');
    require(payload.currency===fixture.payment.currency,'currency_changed','支付币种不匹配');
    if(payment.status==='pending') {
      const receipt={id:'receipt-'+payment.id,amount_minor:payload.amount_minor,currency:payload.currency,payee:fixture.payment.payee,simulation:true};
      Object.assign(payment,{status:'paid',receipt}); effect(out,'payment.capture_demo',payment.id,{receipt_id:receipt.id,amount_minor:receipt.amount_minor});
    }
  } else if(action==='payment.cancel') {
    require(['pending','cancelled'].includes(payment.status),'not_pending','只能撤销待支付请求；已付款不在此操作中退款','Only a pending request can be cancelled; this action does not issue a refund');
    if(payment.status==='pending') { payment.status='cancelled'; effect(out,'payment.request_cancelled',payment.id); }
  } else if(action==='payment.reopen') {
    require(['cancelled','pending'].includes(payment.status),'not_reopenable','该支付请求不可重新打开'); payment.status='pending';
  }
  out.revision++; Object.defineProperty(out.processed_events,messageId,{value:digest,enumerable:true,writable:true,configurable:true});
  return out;
}

export function frameId(state) {
  const {ui,installation:booking,payment}=state;
  if(ui.surface==='app'&&ui.app==='shopping')return ui.page==='product'?1:2;
  if(ui.slot_picker)return booking.selected_slot_id?7:6;
  if(payment.status==='paid')return 12;
  if(['pending','cancelled'].includes(payment.status))return 11;
  if(booking.status==='en_route')return 10;
  if(booking.status==='booked')return state.calendar.installation_sync==='undone'?9:8;
  if(state.delivery.status==='delivered'&&!ui.installation_deferred)return 5;
  return state.delivery.status==='out_for_delivery'?4:3;
}
function serviceCards(state) {
  const frame=frameId(state), {fixture,installation:booking,calendar,payment}=state;
  const card=(owner,entity,title,data)=>({id:owner+':'+entity,ownerApp:owner,entityId:entity,title,data,bodyAction:{action:'navigation.open_app',actor:'user',payload:{app:owner}}});
  let cards=[];
  if(frame===3)cards=[card('shopping',state.order.id,'订单', {...fixture.order,...state.order})];
  if(frame===4)cards=[card('logistics',state.delivery.id,'物流', {...fixture.delivery,...state.delivery})];
  if([5,6,7,8,9,10].includes(frame))cards=[card('installation',booking.id,'安装服务',{...fixture.installation,...booking,slots:availableSlots(state),slot:slot(state,booking.booked_slot_id,booking.booked_day)})];
  if([8,9].includes(frame))cards.push(card('calendar',fixture.calendar.installation_event_id,'日历',{status:calendar.installation_sync,acknowledged:calendar.acknowledged,event:calendar.events[fixture.calendar.installation_event_id]??null,bookingStillValid:true}));
  if([11,12].includes(frame))cards=[card('payment',payment.id,'支付',{...fixture.payment,...payment})];
  if(frame===12)cards.push(card('installation',booking.id,'安装服务',{...fixture.installation,...booking}));
  return cards.filter(item=>!state.ui.dismissed_cards.includes(item.id));
}

function controlEvent(state, definition) {
  let action=definition.action,payload={};
  if(action==='shopping.buy')action='order.purchase_demo';
  else if(ROUTES[action]) { payload={app:ROUTES[action][0],page:ROUTES[action][1]}; action='navigation.open_app'; }
  else if(action==='installation.choose_day')payload={date:definition.sourceId==='sunday'?'2026-09-20':'2026-09-19'};
  else if(action==='installation.choose_slot')payload={slot_id:definition.sourceId==='conflict_slot'?'morning':'afternoon'};
  else if(action==='payment.pay')payload={invoice_id:state.payment.id,amount_minor:state.fixture.payment.amount_minor,currency:state.fixture.payment.currency};
  else if(action==='card.dismiss')payload={card_id:serviceCards(state)[0]?.id};
  return {action,actor:'user',payload};
}
function isDetailRoute(state) { return state.ui.surface==='app'&&!(state.ui.app==='shopping'&&['product','order'].includes(state.ui.page)); }
export function nativeControls(state, locale='cn') {
  const frame=frameId(state), slots=availableSlots(state), isEn=locale==='en';
  let definitions=FRAME_CONTROLS[frame];
  if(frame===3&&serviceCards(state).length===0)definitions=[];
  return definitions.map((definition,index)=>{
    const result={sourceId:definition.sourceId,enabled:definition.enabled,label:isEn?definition.en:definition.cn,textIds:definition.textIds,event:controlEvent(state,definition)};
    if(result.sourceId==='conflict_slot')result.enabled=slots[0].enabled;
    if(result.sourceId==='afternoon')result.enabled=slots[1].enabled;
    if(result.sourceId==='confirm_booking')result.enabled=slots.some(item=>item.selected&&item.enabled);
    if(result.sourceId==='acknowledge_calendar'&&state.calendar.acknowledged) { result.enabled=false; result.label=isEn?'Confirmed':'已确认'; }
    if(frame===5&&state.installation.status==='cancelled'&&result.sourceId==='choose_time')result.label=isEn?'Book again':'重新预约';
    if(frame===3&&state.ui.installation_deferred&&result.sourceId==='view_order') { result.label=isEn?'Book installation':'预约安装'; result.event={action:'installation.open_slots',actor:'user',payload:{}}; }
    if(frame===11&&state.payment.status==='cancelled') {
      if(result.sourceId==='pay_materials') { result.label=isEn?'Reopen':'重新打开'; result.event={action:'payment.reopen',actor:'user',payload:{}}; }
      if(result.sourceId==='withdraw_payment_request') { result.label=isEn?'Cancelled':'已撤销'; result.enabled=false; }
    }
    if(isDetailRoute(state)&&index===0) { result.label=isEn?'Back to desktop':'返回桌面'; result.enabled=true; result.event={action:'navigation.desktop',actor:'user',payload:{}}; }
    return result;
  });
}

/** Session mutations are pure. Keep the returned session as the single source of truth. */
export function createSession({locale='cn',fixture=DEFAULT_FIXTURE}={}) {
  return {schemaVersion:1,locale:locale==='en'?'en':'cn',state:initialState(fixture),history:[],sequence:0,epoch:0,lastEvent:null,inputEvents:{},providerEvents:{}};
}
const renderId = session => `wizard-${session.epoch}-${session.sequence}`;
function semanticState(state) { const {revision,processed_events,...domain}=state; return domain; }
export function dispatch(session, event) {
  event={...event,id:event.id??`${renderId(session)}:${event.action}`};
  const state=reduce(session.state,event);
  if(same(state,session.state))return clone(session);
  const next=clone(session);
  if(!same(semanticState(state),semanticState(session.state)))next.history.push({state:clone(session.state),lastEvent:clone(session.lastEvent)});
  next.state=state; next.sequence++; next.lastEvent=clone(event); return next;
}
export function activateControl(session, sourceId, eventId, expectedRenderId) {
  require(typeof sourceId==='string','unknown_control','未知控件');
  sourceId=sourceId.replace(/_control$/,'');
  const id=eventId??`${renderId(session)}:native:${sourceId}`;
  if(own(session.inputEvents,id)) {
    require(session.inputEvents[id].sourceId===sourceId,'reused_id','同一事件 id 不得复用于不同控件','This input ID was already used by another control');
    return dispatch(session,session.inputEvents[id].event);
  }
  require(expectedRenderId===undefined||expectedRenderId===renderId(session),'stale_control','页面已经更新，请使用当前卡片','The card changed; use its current controls');
  const control=nativeControls(session.state,session.locale).find(item=>item.sourceId===sourceId);
  require(control,'unknown_control','当前页面没有这个控件','This control is not on the current card');
  require(control.enabled,'disabled_control','该操作当前不可用','This control is currently unavailable');
  const event={id,...control.event},next=dispatch(session,event);
  Object.defineProperty(next.inputEvents,id,{value:{sourceId,event},enumerable:true,writable:true,configurable:true});
  return next;
}
function nextProvider(state,locale) {
  if(state.ui.surface!=='desktop'||state.ui.slot_picker)return null;
  let action=null,cn='',en='';
  if(state.delivery.status==='not_dispatched'&&state.order.status!=='not_placed') { action='logistics.out_for_delivery'; cn='查看配送更新'; en='Show delivery update'; }
  else if(state.delivery.status==='out_for_delivery') { action='logistics.delivered'; cn='空调已送达'; en='Mark as delivered'; }
  else if(state.installation.status==='booked') { action='installation.technician_departed'; cn='师傅已出发'; en='Technician is on the way'; }
  else if(state.installation.status==='en_route') { action='installation.completed'; cn='安装已完成'; en='Mark installation complete'; }
  return action?{action,actor:'provider',payload:{},label:locale==='en'?en:cn}:null;
}
export function nextUpdate(session,eventId) {
  if(eventId!==undefined&&own(session.providerEvents,eventId))return dispatch(session,session.providerEvents[eventId]);
  const update=nextProvider(session.state,session.locale);
  require(update,'no_update','当前没有待展示的服务更新，请先操作卡片','Use the card controls before showing another service update');
  const event={id:eventId??`${renderId(session)}:provider:${update.action}`,action:update.action,actor:update.actor,payload:update.payload};
  const next=dispatch(session,event);
  Object.defineProperty(next.providerEvents,event.id,{value:event,enumerable:true,writable:true,configurable:true});
  return next;
}
export function goBack(session) {
  if(!session.history.length)return clone(session);
  const next=clone(session), previous=next.history.pop(); next.state=previous.state; next.lastEvent=previous.lastEvent; next.sequence++;
  next.inputEvents=Object.fromEntries(Object.entries(next.inputEvents).filter(([id])=>own(next.state.processed_events,id)));
  next.providerEvents=Object.fromEntries(Object.entries(next.providerEvents).filter(([id])=>own(next.state.processed_events,id)));
  return next;
}
export function restart(session) {
  const next=createSession({locale:session.locale,fixture:session.state.fixture}); next.epoch=session.epoch+1; next.sequence=session.sequence+1; return next;
}
export function setLocale(session,locale) { const next=clone(session); next.locale=locale==='en'?'en':'cn'; next.sequence++; return next; }

const GUIDANCE = {
  1:[['从熟悉的购物应用开始','查看空调详情，然后点击「立即购买」'],['Start with a familiar shopping app','Review the air conditioner, then choose Buy now']],
  2:[['订单已准备好','点击左上角的返回按钮，在桌面继续查看服务进度'],['Your order is ready','Use the back button to follow your order on the desktop']],
  3:[['订单来到桌面','不用打开购物应用，也能查看订单；点击下一条更新，查看配送进度'],['Your order, on the desktop','Check your order at a glance, then show the next delivery update']],
  4:[['配送进度及时更新','卡片显示预计送达时间，准备好后点击「空调已送达」'],['Follow your delivery','The card shows when to expect your order; mark it as delivered when ready']],
  5:[['接下来，预约安装','点击卡片中的「选择时间」，查看可预约的日期和时段'],['Book your installation','Choose a time on the installation card to see the available dates and times']],
  6:[['先看日历，再选时段','周六上午与项目例会冲突，下午可选；也可以切换到周日'],['Find a time that works','Saturday morning conflicts with a meeting; choose the afternoon or switch to Sunday']],
  7:[['选好了，再确认','检查所选时段，点击「确认预约」后才会完成预约'],['Review your chosen time','Check the time, then choose Confirm booking to reserve it']],
  8:[['预约已确认，日历已更新','日程已经加入日历，点击「确认」表示已知晓；撤销日程不会取消安装'],['Booked and added to your calendar','Your calendar is already updated; acknowledge it with Confirm, or remove just the calendar entry']],
  9:[['撤销日程，预约仍然有效','可以重新加入日历，也可以保留这个选择，继续查看师傅的进度'],['Calendar entry removed, booking kept','Restore the calendar entry or leave it removed and follow the installer’s progress']],
  10:[['师傅正在前往','查看预约或联系师傅，安装结束后再点击「安装已完成」'],['Your installer is on the way','Review the booking or contact the installer, then mark installation complete when ready']],
  11:[['材料费，由你确认支付','核对材料费后，可以点击支付，也可以撤销这次待支付请求'],['Review the materials charge','Check the invoice, then choose Pay or cancel the payment request']],
  12:[['安装与付款，都有记录','点击「查看凭证」，查看这次付款的详细记录'],['Your receipt is ready','Choose View receipt to see the payment details']],
};

function textUpdates(state,locale,controls) {
  const updates=[],frame=frameId(state),en=locale==='en',booking=state.installation;
  const text=(id,value)=>updates.push({id:`text_${id}`,text:value});
  for(const control of controls)if(control.textIds.length)updates.push({id:control.textIds[0],text:control.label});
  if([6,7].includes(frame)) {
    const slots=availableSlots(state),morning=slots[0],selected=slots.find(item=>item.selected),sunday=booking.selected_day==='2026-09-20';
    text(frame===6?72:126,morning.enabled?(en?'Calendar free':'日历空闲'):(en?'Conflicts with a meeting':'与项目例会冲突'));
    text(frame===6?74:128,en?'Calendar free':'日历空闲');
    text(frame===6?76:130,selected?`${en?(sunday?'Sun · Sep 20':'Sat · Sep 19'):(sunday?'周日 9月20日':'周六 9月19日')} · ${selected.label}`:(en?'Choose an installation time':'请选择安装时段'));
  }
  if([8,9,10].includes(frame)&&booking.booked_slot_id) {
    const selected=slot(state,booking.booked_slot_id,booking.booked_day),sunday=booking.booked_day==='2026-09-20';
    const date=en?(sunday?'Sun · Sep 20':'Sat · Sep 19'):(sunday?'周日 9月20日':'周六 9月19日');
    for(const id of ({8:[180,186],9:[30],10:[89]}[frame]))text(id,`${date} · ${selected.label}`);
  }
  if(frame===5&&booking.status==='cancelled') { text(13,en?'Installation · Cancelled':'安装服务 · 预约已取消'); text(14,en?'Booking cancelled':'安装预约已取消'); text(15,en?'The linked calendar event was removed':'日历中的关联日程已移除'); }
  if(frame===11&&state.payment.status==='cancelled') { text(141,en?'Payment · Request cancelled':'支付 · 请求已撤销'); text(142,en?'Materials are not paid yet':'材料费尚未支付'); }
  if([10,11,12].includes(frame)&&booking.booked_day==='2026-09-20') {
    const [date,dock]={10:[84,98],11:[139,153],12:[195,208]}[frame]; text(date,en?'Sun · Sep 20':'9月20日 周日'); text(dock,'20');
  }
  if(isDetailRoute(state)) {
    const app={shopping:['购物应用','Shopping'],logistics:['物流应用','Delivery'],installation:['安装服务','Installation'],calendar:['日历应用','Calendar'],payment:['支付应用','Payment']}[state.ui.app];
    const page={receipt:['付款凭证','Payment receipt'],contact:['联系服务','Contact service'],support:['联系服务','Contact service'],booking:['安装预约','Installation booking'],'service-order':['服务单','Service order'],feedback:['服务反馈','Service feedback'],'delivery-time':['配送安排','Delivery window'],detail:['详情预览','Details']}[state.ui.page]??['详情预览','Details'];
    const ids={2:[44,46],3:[103,104],4:[160,161],5:[11,12],6:[64,65],7:[118,119],8:[176,177],9:[217,27],10:[84,85],11:[139,140],12:[195,196]}[frame];
    if(ids) { text(ids[0],app[en?1:0]); text(ids[1],page[en?1:0]); }
  }
  return updates;
}

/** Stable contract for Astro + the Makepad WASM bridge. Native control events
 * call activateControl; the outer Next update button calls nextUpdate.
 */
export function getView(session) {
  const state=clone(session.state),frame=frameId(state),locale=session.locale,controls=nativeControls(state,locale),en=locale==='en';
  let [title,body]=GUIDANCE[frame][en?1:0];
  const next=nextProvider(state,locale),detail=isDetailRoute(state),complete=detail&&state.ui.app==='payment'&&state.ui.page==='receipt';
  let primarySource={1:'buy',2:'back',3:state.ui.installation_deferred?'view_order':null,4:null,5:'choose_time',6:'afternoon',7:'confirm_booking',8:state.calendar.acknowledged?null:'acknowledge_calendar',9:'restore_calendar',10:null,11:'pay_materials',12:'view_payment_receipt'}[frame];
  if(frame===11&&state.payment.status==='cancelled') { title=en?'Payment request cancelled':'请求已撤销，材料费尚未支付'; body=en?'Reopen the request to review the charge again; your installation is still complete':'重新打开请求后可以再次确认支付，已经完成的安装保持不变'; }
  if(frame===5&&state.installation.status==='cancelled') { title=en?'Installation booking cancelled':'安装预约已取消'; body=en?'The booking and its calendar entry were removed; book again when you are ready':'这次预约和关联日程已移除，准备好后可以重新预约'; }
  if(frame===3&&state.ui.installation_deferred) { title=en?'Book installation when you are ready':'准备好了，再预约安装'; body=en?'Use Book installation on the order card to return to the available times':'点击订单卡上的「预约安装」，重新展开可选时段'; }
  if(detail) { primarySource=complete?null:controls[0]?.sourceId; title=complete?(en?'You’re all set':'这次体验已完成'):(en?'Service details':'查看服务详情'); body=complete?(en?'Installation is complete and your payment is recorded':'安装已完成，付款也有了记录'):(en?'Review the details here, then return to the desktop to continue':'在这里查看详情，返回桌面可继续查看进度'); }
  const primary=controls.find(item=>item.sourceId===primarySource&&item.enabled);
  const guidance={title,body,description:body,primary:primary?{kind:'native',sourceId:primary.sourceId,label:primary.label}:next?{kind:'provider',label:next.label}:null};
  const updates=textUpdates(state,locale,controls),id=renderId(session),cards=serviceCards(state);
  return {schemaVersion:1,renderId:id,frameId:frame,locale,state,controls,nativeControls:controls.map(control=>({...control,action:control.event.action,actor:control.event.actor,payload:control.event.payload})),cards,slots:availableSlots(state),guidance,nextUpdate:next,canGoBack:session.history.length>0,complete,completed:complete,
    labels:{back:en?'Previous step':'上一步',restart:en?'Restart':'重新开始',update:en?'Next service update':'下一条服务更新',clickCard:en?'Choose the action on the card':'直接点击卡片中的操作'},
    renderProps:{id,frameId:frame,locale,state,controls,textUpdates:updates,enabledUpdates:controls.map(control=>({id:control.sourceId+'_control',enabled:control.enabled})),selection:{day:state.installation.selected_day,slotId:state.installation.selected_slot_id},hiddenCardIds:state.ui.dismissed_cards,appRoute:detail?{app:state.ui.app,page:state.ui.page}:null}};
}
