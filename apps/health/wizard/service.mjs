// Deterministic local simulation. No network, real appointments, or medical recommendations.
const FRAMES = {"1":{"labels":{"title":{"cn":"健康","en":"Health"},"heading":{"cn":"年度体检邀请","en":"Annual health check"},"provider_name":{"cn":"安心体检中心","en":"Willow Health Centre"},"tagline":{"cn":"为自己留一点时间","en":"Make time for yourself"},"open_details_text":{"cn":"查看详情","en":"View details"},"dock_health":{"cn":"健康","en":"Health"},"dock_calendar":{"cn":"日历","en":"Calendar"},"dock_mail":{"cn":"邮件","en":"Mail"},"dock_profile":{"cn":"我的","en":"Profile"},"status_time":{"cn":"9:41","en":"9:41"}},"controls":{"open_details":{"event":"health.open_details","source_bounds":[16,407,201,43],"enabled":true,"text_ids":["open_details_text"],"ocr_ids":[5]}},"surface":"app","nodeIds":["page","screen","open_details","open_details_surface","open_details_control","clinic_photo","dock","dock_icon_heart","dock_icon_calendar","dock_icon_mail","dock_icon_person","title","heading","provider_name","tagline","open_details_text","dock_health","dock_calendar","dock_mail","dock_profile","status_time"]},"2":{"labels":{"status_time":{"cn":"9:41","en":"9:41"},"title":{"cn":"体检详情","en":"Checkup details"},"provider_name":{"cn":"安心体检中心","en":"Willow Health Centre"},"basic_name":{"cn":"基础体检套餐","en":"Basic checkup package"},"optional_note":{"cn":"可自选牙科与视力项目","en":"Dental and vision options"},"edit_note":{"cn":"预约前可随时修改","en":"Review before booking"},"arrange_desktop_text":{"cn":"在桌面安排","en":"Arrange on desktop"}},"controls":{"arrange_desktop":{"event":"health.arrange_desktop","source_bounds":[18,402,199,47],"enabled":true,"text_ids":["arrange_desktop_text"],"ocr_ids":[56]}},"surface":"app","nodeIds":["page","screen","details_provider","details_package","details_options","details_edit","arrange_desktop","arrange_desktop_surface","arrange_desktop_control","back_icon_0","clinic_icon_1","package_icon_2","tooth_icon_3","sliders_icon_4","status_time","title","provider_name","basic_name","optional_note","edit_note","arrange_desktop_text"]},"3":{"labels":{"status_time":{"cn":"09:41","en":"09:41"},"status_date":{"cn":"10月22日 周四","en":"Thu, 22 Oct"},"card_status":{"cn":"健康 · 待预约","en":"Health · Invitation"},"appointment_title":{"cn":"年度体检","en":"Annual health check"},"appointment_note":{"cn":"选择项目和适合你的时间","en":"Choose items and a time"},"provider_name":{"cn":"安心体检中心","en":"Willow Health Centre"},"choose_items_text":{"cn":"选择项目","en":"Choose items"},"defer_text":{"cn":"稍后安排","en":"Later"},"dock_health":{"cn":"健康","en":"Health"},"dock_calendar":{"cn":"日历","en":"Calendar"},"dock_mail":{"cn":"邮件","en":"Mail"}},"controls":{"choose_items":{"event":"health.choose_items","source_bounds":[28,268,179,41],"enabled":true,"text_ids":["choose_items_text"],"ocr_ids":[96]},"defer":{"event":"health.defer","source_bounds":[28,316,179,39],"enabled":true,"text_ids":["defer_text"],"ocr_ids":[97]}},"surface":"desktop","nodeIds":["page","screen","wallpaper_upper","wallpaper_lower","appointment_card","choose_items","choose_items_surface","choose_items_control","defer","defer_surface","defer_control","heart_icon_0","dock","dock_icon_heart","dock_icon_calendar","dock_icon_mail","status_time","status_date","card_status","appointment_title","appointment_note","provider_name","choose_items_text","defer_text","dock_health","dock_calendar","dock_mail"]},"4":{"labels":{"status_time":{"cn":"09:41","en":"09:41"},"status_date":{"cn":"10月22日 周四","en":"Thu, 22 Oct"},"title":{"cn":"选择体检项目","en":"Choose checkup items"},"basic_name":{"cn":"基础套餐","en":"Basic package"},"basic_note":{"cn":"已包含","en":"Included"},"dental_name":{"cn":"牙科检查","en":"Dental check"},"dental_note":{"cn":"可选","en":"Optional"},"vision_name":{"cn":"视力检查","en":"Vision check"},"vision_note":{"cn":"可选","en":"Optional"},"choice_note":{"cn":"用户自主选择","en":"Your choice"},"cancel_items_text":{"cn":"取消","en":"Cancel"},"choose_time_text":{"cn":"选择时间","en":"Choose time"},"dock_health":{"cn":"健康","en":"Health"},"dock_calendar":{"cn":"日历","en":"Calendar"},"dock_mail":{"cn":"邮件","en":"Mail"}},"controls":{"basic_package":{"event":"health.basic_package","source_bounds":[20,146,193,50],"enabled":false,"text_ids":["basic_name","basic_note"],"ocr_ids":[139,140]},"toggle_dental":{"event":"health.toggle_dental","source_bounds":[20,202,193,50],"enabled":true,"text_ids":["dental_name","dental_note"],"ocr_ids":[141,142]},"toggle_vision":{"event":"health.toggle_vision","source_bounds":[20,258,193,50],"enabled":true,"text_ids":["vision_name","vision_note"],"ocr_ids":[143,144]},"cancel_items":{"event":"health.cancel_items","source_bounds":[20,351,88,38],"enabled":true,"text_ids":["cancel_items_text"],"ocr_ids":[146]},"choose_time":{"event":"health.choose_time","source_bounds":[115,351,100,38],"enabled":true,"text_ids":["choose_time_text"],"ocr_ids":[147]}},"surface":"desktop","nodeIds":["page","screen","wallpaper_upper","wallpaper_lower","package_card","basic_package","basic_package_surface","basic_package_control","toggle_dental","toggle_dental_surface","toggle_dental_control","toggle_vision","toggle_vision_surface","toggle_vision_control","cancel_items","cancel_items_surface","cancel_items_control","choose_time","choose_time_surface","choose_time_control","clinic_icon_0","tooth_icon_1","eye_icon_2","dock","dock_icon_heart","dock_icon_calendar","dock_icon_mail","status_time","status_date","title","basic_name","basic_note","dental_name","dental_note","vision_name","vision_note","choice_note","cancel_items_text","choose_time_text","dock_health","dock_calendar","dock_mail","basic_checkbox","dental_checkbox","vision_checkbox"]},"5":{"labels":{"status_time":{"cn":"09:41","en":"09:41"},"status_date":{"cn":"10月22日 周四","en":"Thu, 22 Oct"},"title":{"cn":"选择预约时间","en":"Choose a time"},"saturday_name":{"cn":"周六","en":"Sat"},"saturday_date":{"cn":"10月24日","en":"24 Oct"},"sunday_name":{"cn":"周日","en":"Sun"},"sunday_date":{"cn":"10月25日","en":"25 Oct"},"morning_time":{"cn":"09:00–10:00","en":"09:00–10:00"},"morning_note":{"cn":"与已有日程冲突","en":"Calendar conflict"},"afternoon_time":{"cn":"14:00–15:00","en":"14:00–15:00"},"afternoon_note":{"cn":"日历空闲","en":"Calendar free"},"confirm_booking_text":{"cn":"确认预约","en":"Confirm booking"},"return_items_text":{"cn":"返回项目","en":"Back to items"},"dock_health":{"cn":"健康","en":"Health"},"dock_calendar":{"cn":"日历","en":"Calendar"},"dock_mail":{"cn":"邮件","en":"Mail"}},"controls":{"saturday":{"event":"health.saturday","source_bounds":[24,118,92,54],"enabled":true,"text_ids":["saturday_name","saturday_date"],"ocr_ids":[16,17]},"sunday":{"event":"health.sunday","source_bounds":[123,118,92,54],"enabled":true,"text_ids":["sunday_name","sunday_date"],"ocr_ids":[18,19]},"conflict_slot":{"event":"health.conflict_slot","source_bounds":[23,187,192,57],"enabled":false,"text_ids":["morning_time","morning_note"],"ocr_ids":[20,21]},"afternoon":{"event":"health.afternoon","source_bounds":[23,250,192,56],"enabled":true,"text_ids":["afternoon_time","afternoon_note"],"ocr_ids":[22,23]},"confirm_booking":{"event":"health.confirm_booking","source_bounds":[22,321,193,38],"enabled":false,"text_ids":["confirm_booking_text"],"ocr_ids":[24]},"return_items":{"event":"health.return_items","source_bounds":[22,368,193,38],"enabled":true,"text_ids":["return_items_text"],"ocr_ids":[25]}},"surface":"desktop","nodeIds":["page","screen","wallpaper_upper","wallpaper_lower","picker_card","saturday","saturday_surface","saturday_control","sunday","sunday_surface","sunday_control","conflict_slot","conflict_slot_surface","conflict_slot_control","afternoon","afternoon_surface","afternoon_control","confirm_booking","confirm_booking_surface","confirm_booking_control","return_items","return_items_surface","return_items_control","dock","dock_icon_heart","dock_icon_calendar","dock_icon_mail","status_time","status_date","title","saturday_name","saturday_date","sunday_name","sunday_date","morning_time","morning_note","afternoon_time","afternoon_note","confirm_booking_text","return_items_text","dock_health","dock_calendar","dock_mail","morning_radio","afternoon_radio"]},"6":{"labels":{"status_time":{"cn":"09:41","en":"09:41"},"status_date":{"cn":"10月22日 周四","en":"Thu, 22 Oct"},"title":{"cn":"确认预约时间","en":"Confirm your time"},"selected_day":{"cn":"周六 10月24日","en":"Sat, 24 Oct"},"selected_time":{"cn":"14:00–15:00","en":"14:00–15:00"},"morning_time":{"cn":"09:00–10:00","en":"09:00–10:00"},"morning_note":{"cn":"与已有日程冲突","en":"Calendar conflict"},"afternoon_time":{"cn":"14:00–15:00","en":"14:00–15:00"},"afternoon_note":{"cn":"日历空闲","en":"Calendar free"},"confirm_booking_text":{"cn":"确认预约","en":"Confirm booking"},"cancel_selection_text":{"cn":"返回","en":"Back"},"dock_health":{"cn":"健康","en":"Health"},"dock_calendar":{"cn":"日历","en":"Calendar"},"dock_mail":{"cn":"邮件","en":"Mail"}},"controls":{"conflict_slot":{"event":"health.conflict_slot","source_bounds":[22,187,192,57],"enabled":false,"text_ids":["morning_time","morning_note"],"ocr_ids":[63,64]},"afternoon":{"event":"health.afternoon","source_bounds":[22,250,192,56],"enabled":true,"text_ids":["afternoon_time","afternoon_note"],"ocr_ids":[65,66]},"confirm_booking":{"event":"health.confirm_booking","source_bounds":[22,321,192,38],"enabled":true,"text_ids":["confirm_booking_text"],"ocr_ids":[67]},"cancel_selection":{"event":"health.cancel_selection","source_bounds":[22,368,192,38],"enabled":true,"text_ids":["cancel_selection_text"],"ocr_ids":[68]}},"surface":"desktop","nodeIds":["page","screen","wallpaper_upper","wallpaper_lower","picker_card","selected_summary","conflict_slot","conflict_slot_surface","conflict_slot_control","afternoon","afternoon_surface","afternoon_control","confirm_booking","confirm_booking_surface","confirm_booking_control","cancel_selection","cancel_selection_surface","cancel_selection_control","dock","dock_icon_heart","dock_icon_calendar","dock_icon_mail","status_time","status_date","title","selected_day","selected_time","morning_time","morning_note","afternoon_time","afternoon_note","confirm_booking_text","cancel_selection_text","dock_health","dock_calendar","dock_mail","morning_radio","afternoon_radio"]},"7":{"labels":{"status_time":{"cn":"09:41","en":"09:41"},"status_date":{"cn":"10月22日 周四","en":"Thu, 22 Oct"},"booking_title":{"cn":"健康 · 预约成功","en":"Health · Booked"},"appointment_title":{"cn":"年度体检","en":"Annual health check"},"package_summary":{"cn":"基础套餐","en":"Basic package"},"appointment_time":{"cn":"周六 10月24日 14:00–15:00","en":"Sat, 24 Oct · 14:00–15:00"},"provider_name":{"cn":"安心体检中心","en":"Willow Health Centre"},"edit_booking_text":{"cn":"修改预约","en":"Edit booking"},"view_booking_text":{"cn":"查看预约","en":"View booking"},"calendar_title":{"cn":"日历 · 已更新","en":"Calendar · Updated"},"calendar_event_title":{"cn":"年度体检","en":"Annual health check"},"calendar_note":{"cn":"同一预约已加入日历","en":"Appointment added to calendar"},"calendar_confirm_text":{"cn":"确认","en":"Confirm"},"calendar_undo_text":{"cn":"撤销日程","en":"Undo event"},"dock_health":{"cn":"健康","en":"Health"},"dock_calendar":{"cn":"日历","en":"Calendar"},"dock_mail":{"cn":"邮件","en":"Mail"}},"controls":{"edit_booking":{"event":"health.edit_booking","source_bounds":[23,216,92,37],"enabled":true,"text_ids":["edit_booking_text"],"ocr_ids":[109]},"view_booking":{"event":"health.view_booking","source_bounds":[121,216,92,37],"enabled":true,"text_ids":["view_booking_text"],"ocr_ids":[110]},"calendar_confirm":{"event":"health.calendar_confirm","source_bounds":[24,384,91,37],"enabled":true,"text_ids":["calendar_confirm_text"],"ocr_ids":[114]},"calendar_undo":{"event":"health.calendar_undo","source_bounds":[121,384,91,37],"enabled":true,"text_ids":["calendar_undo_text"],"ocr_ids":[115]}},"surface":"desktop","nodeIds":["page","screen","wallpaper_upper","wallpaper_lower","booking_card","calendar_card","edit_booking","edit_booking_surface","edit_booking_control","view_booking","view_booking_surface","view_booking_control","calendar_confirm","calendar_confirm_surface","calendar_confirm_control","calendar_undo","calendar_undo_surface","calendar_undo_control","heart_icon_0","calendar_icon_1","location_icon_2","calendar_icon_3","dock","dock_icon_heart","dock_icon_calendar","dock_icon_mail","status_time","status_date","booking_title","appointment_title","package_summary","appointment_time","provider_name","edit_booking_text","view_booking_text","calendar_title","calendar_event_title","calendar_note","calendar_confirm_text","calendar_undo_text","dock_health","dock_calendar","dock_mail"]},"8":{"labels":{"status_time":{"cn":"09:41","en":"09:41"},"status_date":{"cn":"10月22日 周四","en":"Thu, 22 Oct"},"booking_title":{"cn":"健康 · 预约有效","en":"Health · Booking active"},"appointment_title":{"cn":"年度体检","en":"Annual health check"},"package_summary":{"cn":"基础套餐","en":"Basic package"},"appointment_time":{"cn":"周六 10月24日 14:00–15:00","en":"Sat, 24 Oct · 14:00–15:00"},"provider_name":{"cn":"安心体检中心","en":"Willow Health Centre"},"view_booking_text":{"cn":"查看预约","en":"View booking"},"calendar_title":{"cn":"日历记录已撤销","en":"Calendar event removed"},"calendar_note":{"cn":"仅移除日历提醒","en":"Only the calendar event was removed"},"booking_note":{"cn":"体检预约仍然有效","en":"Your appointment is still booked"},"calendar_restore_text":{"cn":"重新加入","en":"Restore event"},"dock_health":{"cn":"健康","en":"Health"},"dock_calendar":{"cn":"日历","en":"Calendar"},"dock_mail":{"cn":"邮件","en":"Mail"}},"controls":{"view_booking":{"event":"health.view_booking","source_bounds":[22,216,193,38],"enabled":true,"text_ids":["view_booking_text"],"ocr_ids":[162]},"calendar_restore":{"event":"health.calendar_restore","source_bounds":[22,384,193,36],"enabled":true,"text_ids":["calendar_restore_text"],"ocr_ids":[166]}},"surface":"desktop","nodeIds":["page","screen","wallpaper_upper","wallpaper_lower","booking_card","calendar_card","view_booking","view_booking_surface","view_booking_control","calendar_restore","calendar_restore_surface","calendar_restore_control","heart_icon_0","calendar_icon_1","location_icon_2","calendar_icon_3","dock","dock_icon_heart","dock_icon_calendar","dock_icon_mail","status_time","status_date","booking_title","appointment_title","package_summary","appointment_time","provider_name","view_booking_text","calendar_title","calendar_note","booking_note","calendar_restore_text","dock_health","dock_calendar","dock_mail"]},"9":{"labels":{"status_time":{"cn":"09:41","en":"09:41"},"status_date":{"cn":"10月22日 周四","en":"Thu, 22 Oct"},"title":{"cn":"修改预约","en":"Edit booking"},"current_label":{"cn":"当前预约","en":"Current booking"},"current_day":{"cn":"周六 10月24日","en":"Sat, 24 Oct"},"current_time":{"cn":"14:00–15:00","en":"14:00–15:00"},"draft_label":{"cn":"新时间","en":"New time"},"draft_weekday":{"cn":"周日","en":"Sun"},"draft_date":{"cn":"10月25日","en":"25 Oct"},"draft_time":{"cn":"10:00–11:00","en":"10:00–11:00"},"draft_availability":{"cn":"日历空闲","en":"Calendar free"},"draft_note":{"cn":"确认修改前保留原预约","en":"Your booking stays until you confirm"},"keep_booking_text":{"cn":"保留原预约","en":"Keep booking"},"select_new_time_text":{"cn":"选择新时间","en":"Choose new time"},"dock_health":{"cn":"健康","en":"Health"},"dock_calendar":{"cn":"日历","en":"Calendar"},"dock_mail":{"cn":"邮件","en":"Mail"}},"controls":{"keep_booking":{"event":"health.keep_booking","source_bounds":[21,373,92,39],"enabled":true,"text_ids":["keep_booking_text"],"ocr_ids":[44]},"select_new_time":{"event":"health.select_new_time","source_bounds":[120,373,93,39],"enabled":true,"text_ids":["select_new_time_text"],"ocr_ids":[45]}},"surface":"desktop","nodeIds":["page","screen","wallpaper_upper","wallpaper_lower","edit_card","current_summary","draft_day_surface","new_slot_surface","keep_booking","keep_booking_surface","keep_booking_control","select_new_time","select_new_time_surface","select_new_time_control","dock","dock_icon_heart","dock_icon_calendar","dock_icon_mail","status_time","status_date","title","current_label","current_day","current_time","draft_label","draft_weekday","draft_date","draft_time","draft_availability","draft_note","keep_booking_text","select_new_time_text","dock_health","dock_calendar","dock_mail","draft_radio"]},"10":{"labels":{"status_time":{"cn":"09:41","en":"09:41"},"status_date":{"cn":"10月22日 周四","en":"Thu, 22 Oct"},"title":{"cn":"确认修改","en":"Review changes"},"old_label":{"cn":"原时间","en":"Current"},"current_day":{"cn":"周六 10月24日","en":"Sat, 24 Oct"},"current_time":{"cn":"14:00–15:00","en":"14:00–15:00"},"new_label":{"cn":"新时间","en":"New"},"draft_day":{"cn":"周日 10月25日","en":"Sun, 25 Oct"},"draft_time":{"cn":"10:00–11:00","en":"10:00–11:00"},"change_note":{"cn":"同一预约与日历将同步更新","en":"Booking and calendar will update"},"discard_changes_text":{"cn":"放弃修改","en":"Discard"},"confirm_changes_text":{"cn":"确认修改","en":"Confirm change"},"dock_health":{"cn":"健康","en":"Health"},"dock_calendar":{"cn":"日历","en":"Calendar"},"dock_mail":{"cn":"邮件","en":"Mail"}},"controls":{"discard_changes":{"event":"health.discard_changes","source_bounds":[21,352,92,39],"enabled":true,"text_ids":["discard_changes_text"],"ocr_ids":[85]},"confirm_changes":{"event":"health.confirm_changes","source_bounds":[120,352,93,39],"enabled":true,"text_ids":["confirm_changes_text"],"ocr_ids":[86]}},"surface":"desktop","nodeIds":["page","screen","wallpaper_upper","wallpaper_lower","review_card","old_time_surface","new_time_surface","discard_changes","discard_changes_surface","discard_changes_control","confirm_changes","confirm_changes_surface","confirm_changes_control","arrow_down_icon_0","dock","dock_icon_heart","dock_icon_calendar","dock_icon_mail","status_time","status_date","title","old_label","current_day","current_time","new_label","draft_day","draft_time","change_note","discard_changes_text","confirm_changes_text","dock_health","dock_calendar","dock_mail"]},"11":{"labels":{"status_time":{"cn":"09:41","en":"09:41"},"status_date":{"cn":"10月22日 周四","en":"Thu, 22 Oct"},"title":{"cn":"取消体检预约","en":"Cancel appointment"},"cancel_note":{"cn":"这会取消预约并移除关联日历","en":"Cancels booking and linked event"},"scope_note":{"cn":"仅撤销日历不会取消预约","en":"Undoing a calendar event keeps booking"},"provider_name":{"cn":"安心体检中心","en":"Willow Health Centre"},"appointment_time":{"cn":"周日 10月25日 10:00–11:00","en":"Sun, 25 Oct · 10:00–11:00"},"keep_booking_text":{"cn":"保留预约","en":"Keep booking"},"confirm_cancel_text":{"cn":"确认取消","en":"Confirm cancel"},"dock_health":{"cn":"健康","en":"Health"},"dock_calendar":{"cn":"日历","en":"Calendar"},"dock_mail":{"cn":"邮件","en":"Mail"}},"controls":{"keep_booking":{"event":"health.keep_booking","source_bounds":[22,346,92,38],"enabled":true,"text_ids":["keep_booking_text"],"ocr_ids":[129]},"confirm_cancel":{"event":"health.confirm_cancel","source_bounds":[121,346,91,38],"enabled":true,"text_ids":["confirm_cancel_text"],"ocr_ids":[130]}},"surface":"desktop","nodeIds":["page","screen","wallpaper_upper","wallpaper_lower","cancel_card","cancel_summary","keep_booking","keep_booking_surface","keep_booking_control","confirm_cancel","confirm_cancel_surface","confirm_cancel_control","clinic_icon_0","calendar_icon_1","dock","dock_icon_heart","dock_icon_calendar","dock_icon_mail","status_time","status_date","title","cancel_note","scope_note","provider_name","appointment_time","keep_booking_text","confirm_cancel_text","dock_health","dock_calendar","dock_mail"]},"12":{"labels":{"status_time":{"cn":"09:41","en":"09:41"},"status_date":{"cn":"10月22日 周四","en":"Thu, 22 Oct"},"title":{"cn":"预约已就绪","en":"Your booking is ready"},"appointment_title":{"cn":"年度体检","en":"Annual health check"},"package_summary":{"cn":"基础套餐","en":"Basic package"},"appointment_time":{"cn":"周日 10月25日 10:00–11:00","en":"Sun, 25 Oct · 10:00–11:00"},"provider_name":{"cn":"安心体检中心","en":"Willow Health Centre"},"booking_label":{"cn":"预约","en":"Booking"},"booking_status":{"cn":"已确认","en":"Confirmed"},"calendar_label":{"cn":"日历","en":"Calendar"},"calendar_status":{"cn":"已同步","en":"Synced"},"return_booking_text":{"cn":"返回预约","en":"Back to booking"},"cancel_booking_text":{"cn":"取消预约","en":"Cancel booking"},"dock_health":{"cn":"健康","en":"Health"},"dock_calendar":{"cn":"日历","en":"Calendar"},"dock_mail":{"cn":"邮件","en":"Mail"}},"controls":{"return_booking":{"event":"health.return_booking","source_bounds":[21,358,92,39],"enabled":true,"text_ids":["return_booking_text"],"ocr_ids":[185]},"cancel_booking":{"event":"health.cancel_booking","source_bounds":[120,358,93,39],"enabled":true,"text_ids":["cancel_booking_text"],"ocr_ids":[186]}},"surface":"desktop","nodeIds":["page","screen","wallpaper_upper","wallpaper_lower","summary_card","booking_status_surface","calendar_status_surface","return_booking","return_booking_surface","return_booking_control","cancel_booking","cancel_booking_surface","cancel_booking_control","check_icon_0","clinic_icon_1","package_icon_2","calendar_icon_3","location_icon_4","calendar_icon_5","calendar_icon_6","check_icon_7","check_icon_8","dock","dock_icon_heart","dock_icon_calendar","dock_icon_mail","status_time","status_date","title","appointment_title","package_summary","appointment_time","provider_name","booking_label","booking_status","calendar_label","calendar_status","return_booking_text","cancel_booking_text","dock_health","dock_calendar","dock_mail"]}}; // populated from measured source labels by scripts/author.py

export const scenario = {
  id: 'health',
  title: {en: 'An appointment that fits your day', cn: '把体检安排进生活'},
  description: {en: 'Choose your checkup items, book a time, and manage the same appointment across health and calendar cards', cn: '自主选择体检项目，预约合适时间，在健康与日历卡片中管理同一预约'},
  phases: {en: ['Invitation', 'Your choices', 'Booking and calendar', 'Review and changes'], cn: ['收到邀请', '自主选择', '预约与日历', '查看与修改']},
};
export const metadata = scenario;
const BOOKING_ID = 'health-booking-annual-2026';
const EVENT_ID = 'calendar-health-annual-2026';
const CONFLICT_ID = 'calendar-personal-20261024';
const SATURDAY = '2026-10-24';
const SUNDAY = '2026-10-25';
const copy = value => structuredClone(value);
const text = (locale, cn, en) => locale === 'cn' ? cn : en;
const initialState = () => ({
  ui: {frameId: 1, surface: 'app'},
  invitation: {id: 'health-invitation-annual-2026', deferred: false},
  provider: {id: 'health-provider-willow', packageId: 'basic', optionalItems: ['dental', 'vision']},
  selection: {packageId: 'basic', dental: false, vision: false, day: SATURDAY, slot: null},
  booking: null,
  draft: null,
  calendar: {linkedEventId: EVENT_ID, acknowledged: false, events: {
    [CONFLICT_ID]: {id: CONFLICT_ID, owner: 'personal', day: SATURDAY, start: '09:00', end: '10:00', title: '已有日程'},
  }},
});

class FlowError extends Error {
  constructor(code) {super(code); this.name = 'HealthFlowError'; this.code = code;}
}
const requireThat = (condition, code) => {if (!condition) throw new FlowError(code);};
const normalize = sourceId => String(sourceId).replace(/_control$/, '');
const renderId = session => `health-${session.revision}`;
const setFrame = (state, frameId) => {state.ui = {frameId, surface: frameId <= 2 ? 'app' : 'desktop'};};
const hasEvent = state => Object.hasOwn(state.calendar.events, EVENT_ID);
const dayParts = (day, locale) => day === SATURDAY
  ? {weekday: text(locale, '周六', 'Sat'), date: text(locale, '10月24日', '24 Oct'), full: text(locale, '周六 10月24日', 'Sat, 24 Oct')}
  : {weekday: text(locale, '周日', 'Sun'), date: text(locale, '10月25日', '25 Oct'), full: text(locale, '周日 10月25日', 'Sun, 25 Oct')};
const slotTime = slot => slot ? `${slot.start}–${slot.end}` : '';
const bookingTime = (booking, locale) => booking ? `${dayParts(booking.day, locale).full} · ${slotTime(booking)}` : '';
const itemSummary = (selection, locale) => [text(locale, '基础套餐', 'Basic'), ...(selection.dental ? [text(locale, '牙科', 'Dental')] : []), ...(selection.vision ? [text(locale, '视力', 'Vision')] : [])].join(' · ');

export function createSession({locale = 'en'} = {}) {
  requireThat(['cn', 'en'].includes(locale), 'LOCALE');
  return {schemaVersion: 1, scenarioId: 'health', locale, revision: 0, state: initialState(), history: [], processedEvents: {}, notice: null};
}

function eventReplay(session, kind, payload, eventId) {
  const id = eventId || `health-event-${session.revision + 1}`;
  requireThat(typeof id === 'string' && id.length > 0, 'EVENT_ID');
  const signature = JSON.stringify({kind, payload});
  const previous = session.processedEvents[id];
  if (Object.hasOwn(session.processedEvents, id)) {requireThat(previous === signature, 'EVENT_ID_REUSED'); return {replay: true};}
  return {id, signature, replay: false};
}

function commit(session, state, event, {notice = null, history = null} = {}) {
  return {...session, revision: session.revision + 1, state, notice,
    history: history || [...session.history, {state: copy(session.state), notice: session.notice}],
    processedEvents: {...session.processedEvents, [event.id]: event.signature}};
}

function enabledFor(state, id) {
  if (id === 'basic_package') return false;
  if (id === 'conflict_slot') return state.selection.day !== SATURDAY;
  if (id === 'confirm_booking') return !!state.selection.slot;
  if (id === 'calendar_confirm') return state.booking?.status === 'booked' && (!hasEvent(state) || !state.calendar.acknowledged);
  if (id === 'calendar_undo') return hasEvent(state);
  if (id === 'calendar_restore') return state.booking?.status === 'booked' && !hasEvent(state);
  if (id === 'confirm_changes') return !!state.draft?.slot && state.booking?.status === 'booked';
  if (id === 'confirm_cancel' || id === 'cancel_booking') return state.booking?.status === 'booked';
  return true;
}

function syncCalendar(state) {
  const booking = state.booking;
  state.calendar.events[EVENT_ID] = {id: EVENT_ID, owner: 'health', bookingId: BOOKING_ID,
    title: '年度体检', day: booking.day, start: booking.start, end: booking.end, bookingVersion: booking.version};
  state.calendar.acknowledged = false;
}

export function activateControl(session, sourceId, eventId, expectedRenderId) {
  const id = normalize(sourceId);
  const event = eventReplay(session, 'control', {sourceId: id}, eventId);
  if (event.replay) return session;
  requireThat(expectedRenderId === undefined || expectedRenderId === renderId(session), 'STALE_RENDER');
  const frame = FRAMES[session.state.ui.frameId];
  requireThat(frame && Object.hasOwn(frame.controls, id), 'UNKNOWN_CONTROL');
  requireThat(enabledFor(session.state, id), 'DISABLED_CONTROL');
  const state = copy(session.state);
  let notice = null;
  switch (id) {
    case 'open_details': setFrame(state, 2); break;
    case 'arrange_desktop': setFrame(state, 3); break;
    case 'choose_items': state.invitation.deferred = false; setFrame(state, 4); break;
    case 'defer': state.invitation.deferred = true; notice = 'DEFERRED'; break;
    case 'toggle_dental': state.selection.dental = !state.selection.dental; break;
    case 'toggle_vision': state.selection.vision = !state.selection.vision; break;
    case 'cancel_items': setFrame(state, 3); break;
    case 'choose_time': setFrame(state, state.selection.slot ? 6 : 5); break;
    case 'saturday': case 'sunday': state.selection.day = id === 'saturday' ? SATURDAY : SUNDAY; state.selection.slot = null; setFrame(state, 5); break;
    case 'conflict_slot': state.selection.slot = {start: '09:00', end: '10:00'}; setFrame(state, 6); break;
    case 'afternoon': state.selection.slot = {start: '14:00', end: '15:00'}; setFrame(state, 6); break;
    case 'return_items': setFrame(state, 4); break;
    case 'cancel_selection': state.selection.slot = null; setFrame(state, 5); break;
    case 'confirm_booking':
      requireThat(state.booking === null, 'ALREADY_BOOKED');
      state.booking = {id: BOOKING_ID, providerId: state.provider.id, status: 'booked', version: 1,
        packageId: 'basic', dental: state.selection.dental, vision: state.selection.vision,
        day: state.selection.day, ...state.selection.slot};
      syncCalendar(state); setFrame(state, 7); break;
    case 'calendar_confirm':
      if (!hasEvent(state)) syncCalendar(state);
      else {state.calendar.acknowledged = true; notice = 'CALENDAR_CONFIRMED';}
      break;
    case 'calendar_undo': delete state.calendar.events[EVENT_ID]; state.calendar.acknowledged = false; setFrame(state, 8); break;
    case 'calendar_restore': syncCalendar(state); setFrame(state, 7); break;
    case 'edit_booking':
      requireThat(state.booking?.status === 'booked', 'NO_BOOKING');
      state.draft = {day: state.booking.day === SATURDAY ? SUNDAY : SATURDAY, slot: null}; setFrame(state, 9); break;
    case 'select_new_time': state.draft.slot = {start: state.draft.day === SUNDAY ? '10:00' : '14:00', end: state.draft.day === SUNDAY ? '11:00' : '15:00'}; setFrame(state, 10); break;
    case 'keep_booking': case 'discard_changes': state.draft = null; setFrame(state, hasEvent(state) ? 7 : 8); break;
    case 'confirm_changes': {
      const calendarPresent = hasEvent(state);
      state.booking = {...state.booking, day: state.draft.day, ...state.draft.slot, version: state.booking.version + 1};
      state.selection.day = state.booking.day; state.selection.slot = {start: state.booking.start, end: state.booking.end};
      state.draft = null;
      if (calendarPresent) syncCalendar(state);
      setFrame(state, calendarPresent ? 7 : 8); break;
    }
    case 'view_booking': setFrame(state, 12); break;
    case 'cancel_booking': state.draft = null; setFrame(state, 11); break;
    case 'confirm_cancel': state.booking.status = 'canceled'; state.draft = null; delete state.calendar.events[EVENT_ID]; state.calendar.acknowledged = false; setFrame(state, 12); break;
    case 'return_booking':
      if (state.booking?.status === 'canceled') return commit(session, initialState(), event, {history: []});
      setFrame(state, 7); break;
    default: throw new FlowError('UNKNOWN_CONTROL');
  }
  return commit(session, state, event, {notice});
}

export function nextUpdate(session, eventId) {
  const event = eventReplay(session, 'provider_update', {}, eventId);
  if (event.replay) return session;
  throw new FlowError('NO_UPDATE');
}

export function goBack(session, eventId) {
  const event = eventReplay(session, 'back', {}, eventId);
  if (event.replay) return session;
  if (!session.history.length) return session;
  const prior = session.history.at(-1);
  return commit(session, copy(prior.state), event, {notice: prior.notice, history: session.history.slice(0, -1)});
}

export function restart(session, eventId) {
  const event = eventReplay(session, 'restart', {}, eventId);
  if (event.replay) return session;
  return commit(session, initialState(), event, {history: []});
}

const GUIDANCE = {
1: ['一封体检邀请', '从熟悉的健康应用进入，先查看机构提供的预约信息', 'An invitation in Health', 'Open the familiar Health app to review the provider’s invitation', 'open_details'],
2: ['先了解，再安排', '基础套餐与可选项目由机构提供，点击按钮把预约卡放到桌面', 'Review the details', 'See the provider’s basic package and optional items, then bring the appointment card to your desktop', 'arrange_desktop'],
3: ['在桌面继续安排', '卡片保留预约上下文，可以现在选择项目，也可以稍后再来', 'Continue on your desktop', 'The appointment card keeps the details together, ready whenever you are', 'choose_items'],
4: ['项目由你选择', '基础套餐已包含，牙科和视力项目可以分别选择或取消', 'Choose your items', 'The basic package is included; dental and vision checks are optional choices', 'choose_time'],
5: ['找到合适的时间', '周六上午与已有日程冲突，选择空闲时段，或切换到周日查看', 'Find a time that fits', 'Saturday morning overlaps an existing event; choose a free slot or check Sunday', 'afternoon'],
6: ['确认后才会预约', '检查日期与时间，确认后会生成预约，并在日历中加入同一事件', 'Confirm your appointment', 'Review the date and time before creating the booking and its linked calendar event', 'confirm_booking'],
7: ['同一预约，两张卡片', '健康卡管理预约，日历卡管理提醒；可以确认日历，也可以单独撤销它', 'One booking, two cards', 'The health card manages your appointment; the calendar card lets you acknowledge or remove its event', 'view_booking'],
8: ['只撤销日历提醒', '预约仍然有效，重新加入会恢复同一个日历事件', 'Your booking is still active', 'Only the calendar event was removed; restoring it keeps the same event identity', 'calendar_restore'],
9: ['先修改草稿', '新时间确认前，原预约与原日历保持有效', 'Edit a draft first', 'Your current booking and calendar event stay in place until you confirm a new time', 'select_new_time'],
10: ['核对预约变更', '确认会更新同一预约；如果日历已撤销，会继续尊重这个选择', 'Review the change', 'Confirm to update this booking; a calendar event you removed will remain removed', 'confirm_changes'],
11: ['明确取消预约', '确认取消会取消这次预约并移除关联日历，其他日程保持不变', 'Cancel this appointment', 'Confirming cancels this booking and removes its linked calendar event, while keeping your other events', 'keep_booking'],
12: ['安排已整理好', '在摘要中查看预约与日历状态，也可以返回继续修改', 'Everything in one place', 'Review the booking and calendar status, or return to make a change', null],
};

export function getView(session) {
  const state = copy(session.state), locale = session.locale, frameId = state.ui.frameId, frame = FRAMES[frameId];
  const nativeText = Object.fromEntries(Object.entries(frame.labels).map(([id, labels]) => [id, labels[locale]]));
  const nativeEnabled = {}, nativeStyles = {}, nativeLayout = {}, nativeHidden = [];
  const put = (id, value) => {if (Object.hasOwn(nativeText, id)) nativeText[id] = value;};
  put('dental_note', text(locale, state.selection.dental ? '已选择' : '可选', state.selection.dental ? 'Selected' : 'Optional'));
  put('vision_note', text(locale, state.selection.vision ? '已选择' : '可选', state.selection.vision ? 'Selected' : 'Optional'));
  for (const item of ['dental', 'vision']) nativeStyles[`${item}_checkbox`] = {bg: state.selection[item] ? 0xff5c8069 : 0xfffcfdfb};
  for (const day of ['saturday', 'sunday']) nativeStyles[`${day}_surface`] = {bg: state.selection.day === (day === 'saturday' ? SATURDAY : SUNDAY) ? 0xff5c8069 : 0xffeff2ef};
  for (const day of ['saturday', 'sunday']) for (const suffix of ['name', 'date']) nativeStyles[`${day}_${suffix}`] = {color: state.selection.day === (day === 'saturday' ? SATURDAY : SUNDAY) ? 0xffffffff : 0xff26342e};
  const conflict = state.selection.day === SATURDAY;
  put('morning_note', text(locale, conflict ? '与已有日程冲突' : '日历空闲', conflict ? 'Calendar conflict' : 'Calendar free'));
  nativeStyles.morning_note = {color: conflict ? 0xffbf914a : 0xff5c8069};
  put('selected_day', dayParts(state.selection.day, locale).full);
  put('selected_time', slotTime(state.selection.slot));
  for (const [key, start] of [['morning', '09:00'], ['afternoon', '14:00']]) nativeStyles[`${key}_radio`] = {bg: state.selection.slot?.start === start ? 0xff5c8069 : 0xfffcfdfb};
  if (state.booking) {
    put('appointment_time', bookingTime(state.booking, locale));
    put('package_summary', itemSummary(state.booking, locale));
    put('current_day', dayParts(state.booking.day, locale).full);
    put('current_time', slotTime(state.booking));
    if (frameId === 7) {
      put('calendar_note', `${dayParts(state.booking.day, locale).date} · ${slotTime(state.booking)}`);
      nativeStyles.calendar_note = {size: locale === 'cn' ? 14 : 13};
    }
  }
  if (state.draft) {
    const day = dayParts(state.draft.day, locale);
    put('draft_weekday', day.weekday); put('draft_date', day.date); put('draft_day', day.full);
    put('draft_time', state.draft.day === SUNDAY ? '10:00–11:00' : '14:00–15:00');
  }
  if (state.calendar.acknowledged) {
    put('calendar_title', text(locale, '日历 · 已确认', 'Calendar · Confirmed'));
    put('calendar_confirm_text', text(locale, '已确认', 'Confirmed'));
  }
  if (frameId === 7 && !hasEvent(state)) {
    put('calendar_title', text(locale, '日历 · 未加入', 'Calendar · Not added'));
    put('calendar_confirm_text', text(locale, '重新加入', 'Restore event'));
    put('calendar_undo_text', text(locale, '未加入', 'Not added'));
  }
  if (frameId === 8 && locale === 'en') put('calendar_note', 'Calendar entry removed');
  if (frameId === 12) {
    const canceled = state.booking?.status === 'canceled';
    put('title', text(locale, canceled ? '预约已取消' : '预约已就绪', canceled ? 'Appointment canceled' : 'Your booking is ready'));
    put('booking_status', text(locale, canceled ? '已取消' : '已确认', canceled ? 'Canceled' : 'Confirmed'));
    put('calendar_status', text(locale, hasEvent(state) ? '已同步' : '已移除', hasEvent(state) ? 'Synced' : 'Removed'));
    if (canceled) nativeHidden.push('check_icon_0', 'check_icon_7');
    if (!hasEvent(state)) nativeHidden.push('check_icon_8');
    if (canceled) {put('return_booking_text', text(locale, '重新开始', 'Start again')); put('cancel_booking_text', text(locale, '已取消', 'Canceled'));}
  }
  const nativeControls = Object.entries(frame.controls).map(([sourceId, control]) => {
    const enabled = enabledFor(state, sourceId);nativeEnabled[sourceId] = enabled;nativeEnabled[`${sourceId}_control`] = enabled;
    return {sourceId, label: nativeText[control.text_ids[0]], enabled, textIds: [...control.text_ids], action: `health.${sourceId}`};
  });
  const guide = GUIDANCE[frameId];
  const primary = nativeControls.find(control => control.sourceId === guide[4] && control.enabled);
  const guidance = {title: locale === 'cn' ? guide[0] : guide[2], description: locale === 'cn' ? guide[1] : guide[3],
    primary: primary ? {kind: 'native', sourceId: primary.sourceId, label: primary.label} : null};
  if (session.notice === 'DEFERRED') guidance.description = text(locale, '预约卡会保留在桌面，准备好后继续选择项目', 'The invitation stays on your desktop, ready when you want to continue');
  if (frameId === 12 && state.booking?.status === 'canceled') {guidance.title = text(locale, '预约已取消', 'Appointment canceled'); guidance.description = text(locale, '关联日历已移除，其他个人日程保留', 'The linked event is removed and your other calendar events are kept');}
  // Measured source labels had tight ink bounds. Runtime data and translations get
  // the available card width while preserving the frozen original geometry.
  if (frameId === 1) {
    Object.assign(nativeLayout, {title: {x:155,w:98}, heading: {x:60,w:286}, provider_name: {x:92,w:222}, tagline: {x:78,w:252}});
    for (const id of ['title','heading','provider_name','tagline']) nativeStyles[id] = {...nativeStyles[id], alignx:.5};
    for (const [id,x] of [['dock_health',43],['dock_calendar',129],['dock_mail',213],['dock_profile',300]]) {
      nativeLayout[id] = {x,w:68}; nativeStyles[id] = {...nativeStyles[id],alignx:.5};
    }
  } else if (frameId === 2) {
    nativeLayout.title = {x:76,w:254}; nativeStyles.title = {alignx:.5};
    nativeLayout.provider_name = {w:224}; nativeLayout.basic_name = {w:224};
    nativeLayout.optional_note = {w:224}; nativeLayout.edit_note = {w:224};
  } else {
    for (const [id,x] of [['dock_health',76],['dock_calendar',164],['dock_mail',256]]) {
      nativeLayout[id] = {x,w:76}; nativeStyles[id] = {...nativeStyles[id],alignx:.5};
    }
    if (Object.hasOwn(nativeText,'title')) nativeLayout.title = {w:286};
    if (Object.hasOwn(nativeText,'provider_name')) nativeLayout.provider_name = {w:frameId===3?275:246};
    if (Object.hasOwn(nativeText,'appointment_title')) nativeLayout.appointment_title = {w:270};
  }
  if (Object.hasOwn(nativeText,'appointment_time')) {
    nativeLayout.appointment_time = {x:92,w:266};
    nativeStyles.appointment_time = {size:18};
  }
  if (Object.hasOwn(nativeText,'package_summary')) {
    nativeLayout.package_summary = {w:frameId===12?260:282};
    nativeStyles.package_summary = {size:18};
  }
  if (frameId===9) {
    nativeLayout.current_day = {x:72,w:132}; nativeStyles.current_day = {size:18};
    nativeLayout.current_time = {x:215,w:130}; nativeStyles.current_time = {size:18};
  }
  if (frameId===12) {
    nativeLayout.title={x:64,w:278};nativeStyles.title={alignx:.5};
    for (const id of ['appointment_title','package_summary','appointment_time','provider_name']) nativeLayout[id]={x:99,w:256};
  }
  for (const id of Object.keys(nativeStyles)) if (!frame.nodeIds.includes(id)) delete nativeStyles[id];
  return {renderId: renderId(session), frameId, locale, phase: frameId <= 3 ? 0 : frameId <= 6 ? 1 : frameId <= 8 ? 2 : 3,
    state, nativeControls, guidance, nextUpdate: null, canGoBack: session.history.length > 0,
    completed: frameId === 12, nativeText, nativeEnabled, nativeStyles, nativeLayout, nativeHidden};
}

const ERRORS = {
  STALE_RENDER: ['画面已更新，请在当前卡片继续操作', 'This card has changed; use the current controls'],
  DISABLED_CONTROL: ['这个选项目前不可用', 'This option is currently unavailable'],
  UNKNOWN_CONTROL: ['当前卡片没有这个操作', 'This action is not on the current card'],
  EVENT_ID_REUSED: ['同一操作编号不能用于不同操作', 'An event ID cannot be reused for another action'],
  ALREADY_BOOKED: ['这次体检已经预约', 'This appointment is already booked'],
  NO_BOOKING: ['当前没有有效预约', 'There is no active appointment'],
  NO_UPDATE: ['请直接使用卡片上的操作', 'Continue using the controls on the card'],
  EVENT_ID: ['操作编号无效', 'Invalid event ID'], LOCALE: ['语言不可用', 'Unsupported language'],
};
export function errorMessage(error, locale = 'en') {
  const values = ERRORS[error?.code || error?.message] || ['暂时无法完成操作，请重试', 'This action could not be completed; please try again'];
  return values[locale === 'cn' ? 0 : 1];
}
