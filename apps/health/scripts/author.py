#!/usr/bin/env python3
"""Measured reconstruction of one generated health atlas; no UI raster overlays."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]
PIPE = PROJECT / 'lab/image-to-appcard'
sys.path.insert(0, str(PIPE))
from catalogue import walk
from semantics import propose, write_brief
from observe import metrics

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def save(path, value): Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
def color(value): return int('ff' + value.lstrip('#'), 16)
INK='26342e';MUTED='69766f';SAGE='5c8069';PANEL='fcfdfb'

# These bounds address the actual 234x513 source crops, not the requested atlas size.
SPECS = {
1:dict(cards=[],photo=[5,73,224,216],buttons=[('open_details',[16,407,201,43],True,['open_details_text'])],dock=[0,464,234,49]),
2:dict(cards=[('details_provider',[15,88,205,53]),('details_package',[15,150,205,53]),('details_options',[15,212,205,53]),('details_edit',[15,274,205,53])],buttons=[('arrange_desktop',[18,402,199,47],True,['arrange_desktop_text'])],icons=[('back',[16,43,14,18]),('clinic',[28,105,22,21]),('package',[29,167,19,22]),('tooth',[28,227,24,24]),('sliders',[28,291,23,23])]),
3:dict(cards=[('appointment_card',[11,127,211,242])],buttons=[('choose_items',[28,268,179,41],True,['choose_items_text']),('defer',[28,316,179,39],False,['defer_text'])],icons=[('heart',[28,141,21,21])],dock=[7,450,221,59]),
4:dict(cards=[('package_card',[8,97,218,305])],buttons=[('basic_package',[20,146,193,50],False,['basic_name','basic_note']),('toggle_dental',[20,202,193,50],False,['dental_name','dental_note']),('toggle_vision',[20,258,193,50],False,['vision_name','vision_note']),('cancel_items',[20,351,88,38],False,['cancel_items_text']),('choose_time',[115,351,100,38],True,['choose_time_text'])],icons=[('clinic',[31,159,22,23]),('tooth',[31,215,24,25]),('eye',[31,273,24,20])],disabled=['basic_package'],dock=[7,450,221,59]),
5:dict(cards=[('picker_card',[8,70,219,349])],buttons=[('saturday',[24,118,92,54],True,['saturday_name','saturday_date']),('sunday',[123,118,92,54],False,['sunday_name','sunday_date']),('conflict_slot',[23,187,192,57],False,['morning_time','morning_note']),('afternoon',[23,250,192,56],False,['afternoon_time','afternoon_note']),('confirm_booking',[22,321,193,38],True,['confirm_booking_text']),('return_items',[22,368,193,38],False,['return_items_text'])],disabled=['conflict_slot','confirm_booking'],dock=[7,450,221,59]),
6:dict(cards=[('picker_card',[8,70,219,349]),('selected_summary',[22,118,193,60])],buttons=[('conflict_slot',[22,187,192,57],False,['morning_time','morning_note']),('afternoon',[22,250,192,56],False,['afternoon_time','afternoon_note']),('confirm_booking',[22,321,192,38],True,['confirm_booking_text']),('cancel_selection',[22,368,192,38],False,['cancel_selection_text'])],disabled=['conflict_slot'],dock=[7,450,221,59]),
7:dict(cards=[('booking_card',[8,59,219,207]),('calendar_card',[8,278,219,157])],buttons=[('edit_booking',[23,216,92,37],False,['edit_booking_text']),('view_booking',[121,216,92,37],True,['view_booking_text']),('calendar_confirm',[24,384,91,37],True,['calendar_confirm_text']),('calendar_undo',[121,384,91,37],False,['calendar_undo_text'])],icons=[('heart',[25,73,21,21]),('calendar',[26,160,14,14]),('location',[26,183,14,16]),('calendar',[24,293,18,18])],dock=[7,450,221,59]),
8:dict(cards=[('booking_card',[8,59,219,208]),('calendar_card',[8,279,219,154])],buttons=[('view_booking',[22,216,193,38],True,['view_booking_text']),('calendar_restore',[22,384,193,36],False,['calendar_restore_text'])],icons=[('heart',[25,73,21,21]),('calendar',[25,160,14,14]),('location',[26,183,14,16]),('calendar',[24,293,18,18])],dock=[7,450,221,59]),
9:dict(cards=[('edit_card',[8,60,219,364]),('current_summary',[21,106,193,64]),('draft_day_surface',[20,207,91,53]),('new_slot_surface',[21,269,193,57])],buttons=[('keep_booking',[21,373,92,39],False,['keep_booking_text']),('select_new_time',[120,373,93,39],True,['select_new_time_text'])],dock=[7,450,221,59]),
10:dict(cards=[('review_card',[8,87,219,320]),('old_time_surface',[20,140,194,65]),('new_time_surface',[20,236,194,65])],buttons=[('discard_changes',[21,352,92,39],False,['discard_changes_text']),('confirm_changes',[120,352,93,39],True,['confirm_changes_text'])],icons=[('arrow_down',[110,211,17,17])],dock=[7,450,221,59]),
11:dict(cards=[('cancel_card',[8,93,219,305]),('cancel_summary',[20,204,195,91])],buttons=[('keep_booking',[22,346,92,38],False,['keep_booking_text']),('confirm_cancel',[121,346,91,38],True,['confirm_cancel_text'])],icons=[('clinic',[29,219,20,22]),('calendar',[29,255,16,17])],dock=[7,450,221,59]),
12:dict(cards=[('summary_card',[8,57,219,354]),('booking_status_surface',[20,257,194,41]),('calendar_status_surface',[20,298,194,42])],buttons=[('return_booking',[21,358,92,39],False,['return_booking_text']),('cancel_booking',[120,358,93,39],False,['cancel_booking_text'])],icons=[('check',[100,72,34,34]),('clinic',[25,149,15,15]),('package',[25,175,15,15]),('calendar',[25,202,15,15]),('location',[27,225,13,15]),('calendar',[30,270,23,22]),('calendar',[30,307,23,22]),('check',[189,278,12,12]),('check',[189,314,12,12])],dock=[7,450,221,59]),
}

# OCR index, stable native text ID, reviewed Chinese, concise English.
TEXT = {
1:[(1,'title','健康','Health'),(2,'heading','年度体检邀请','Annual health check'),(3,'provider_name','安心体检中心','Willow Health Centre'),(4,'tagline','为自己留一点时间','Make time for yourself'),(5,'open_details_text','查看详情','View details'),(6,'dock_health','健康','Health'),(7,'dock_calendar','日历','Calendar'),(8,'dock_mail','邮件','Mail'),(10,'dock_profile','我的','Profile')],
2:[(50,'status_time','9:41','9:41'),(51,'title','体检详情','Checkup details'),(52,'provider_name','安心体检中心','Willow Health Centre'),(53,'basic_name','基础体检套餐','Basic checkup package'),(54,'optional_note','可自选牙科与视力项目','Dental and vision options'),(55,'edit_note','预约前可随时修改','Review before booking'),(56,'arrange_desktop_text','在桌面安排','Arrange on desktop')],
3:[(90,'status_time','09:41','09:41'),(91,'status_date','10月22日 周四','Thu, 22 Oct'),(92,'card_status','健康 · 待预约','Health · Invitation'),(93,'appointment_title','年度体检','Annual health check'),(94,'appointment_note','选择项目和适合你的时间','Choose items and a time'),(95,'provider_name','安心体检中心','Willow Health Centre'),(96,'choose_items_text','选择项目','Choose items'),(97,'defer_text','稍后安排','Later')],
4:[(136,'status_time','09:41','09:41'),(137,'status_date','10月22日 周四','Thu, 22 Oct'),(138,'title','选择体检项目','Choose checkup items'),(139,'basic_name','基础套餐','Basic package'),(140,'basic_note','已包含','Included'),(141,'dental_name','牙科检查','Dental check'),(142,'dental_note','可选','Optional'),(143,'vision_name','视力检查','Vision check'),(144,'vision_note','可选','Optional'),(145,'choice_note','用户自主选择','Your choice'),(146,'cancel_items_text','取消','Cancel'),(147,'choose_time_text','选择时间','Choose time')],
5:[(12,'status_time','09:41','09:41'),(13,'status_date','10月22日 周四','Thu, 22 Oct'),(15,'title','选择预约时间','Choose a time'),(16,'saturday_name','周六','Sat'),(17,'saturday_date','10月24日','24 Oct'),(18,'sunday_name','周日','Sun'),(19,'sunday_date','10月25日','25 Oct'),(20,'morning_time','09:00–10:00','09:00–10:00'),(21,'morning_note','与已有日程冲突','Calendar conflict'),(22,'afternoon_time','14:00–15:00','14:00–15:00'),(23,'afternoon_note','日历空闲','Calendar free'),(24,'confirm_booking_text','确认预约','Confirm booking'),(25,'return_items_text','返回项目','Back to items')],
6:[(58,'status_time','09:41','09:41'),(59,'status_date','10月22日 周四','Thu, 22 Oct'),(60,'title','确认预约时间','Confirm your time'),(61,'selected_day','周六 10月24日','Sat, 24 Oct'),(62,'selected_time','14:00–15:00','14:00–15:00'),(63,'morning_time','09:00–10:00','09:00–10:00'),(64,'morning_note','与已有日程冲突','Calendar conflict'),(65,'afternoon_time','14:00–15:00','14:00–15:00'),(66,'afternoon_note','日历空闲','Calendar free'),(67,'confirm_booking_text','确认预约','Confirm booking'),(68,'cancel_selection_text','返回','Back')],
7:[(102,'status_time','09:41','09:41'),(103,'status_date','10月22日 周四','Thu, 22 Oct'),(104,'booking_title','健康 · 预约成功','Health · Booked'),(105,'appointment_title','年度体检','Annual health check'),(106,'package_summary','基础套餐','Basic package'),(107,'appointment_time','周六 10月24日 14:00–15:00','Sat, 24 Oct · 14:00–15:00'),(108,'provider_name','安心体检中心','Willow Health Centre'),(109,'edit_booking_text','修改预约','Edit booking'),(110,'view_booking_text','查看预约','View booking'),(111,'calendar_title','日历 · 已更新','Calendar · Updated'),(112,'calendar_event_title','年度体检','Annual health check'),(113,'calendar_note','同一预约已加入日历','Appointment added to calendar'),(114,'calendar_confirm_text','确认','Confirm'),(115,'calendar_undo_text','撤销日程','Undo event')],
8:[(153,'status_time','09:41','09:41'),(154,'status_date','10月22日 周四','Thu, 22 Oct'),(156,'booking_title','健康 · 预约有效','Health · Booking active'),(157,'appointment_title','年度体检','Annual health check'),(158,'package_summary','基础套餐','Basic package'),(160,'appointment_time','周六 10月24日 14:00–15:00','Sat, 24 Oct · 14:00–15:00'),(161,'provider_name','安心体检中心','Willow Health Centre'),(162,'view_booking_text','查看预约','View booking'),(163,'calendar_title','日历记录已撤销','Calendar event removed'),(164,'calendar_note','仅移除日历提醒','Only the calendar event was removed'),(165,'booking_note','体检预约仍然有效','Your appointment is still booked'),(166,'calendar_restore_text','重新加入','Restore event')],
9:[(31,'status_time','09:41','09:41'),(32,'status_date','10月22日 周四','Thu, 22 Oct'),(34,'title','修改预约','Edit booking'),(35,'current_label','当前预约','Current booking'),(36,'current_day','周六 10月24日','Sat, 24 Oct'),(37,'current_time','14:00–15:00','14:00–15:00'),(38,'draft_label','新时间','New time'),(39,'draft_weekday','周日','Sun'),(40,'draft_date','10月25日','25 Oct'),(41,'draft_time','10:00–11:00','10:00–11:00'),(42,'draft_availability','日历空闲','Calendar free'),(43,'draft_note','确认修改前保留原预约','Your booking stays until you confirm'),(44,'keep_booking_text','保留原预约','Keep booking'),(45,'select_new_time_text','选择新时间','Choose new time')],
10:[(74,'status_time','09:41','09:41'),(75,'status_date','10月22日 周四','Thu, 22 Oct'),(77,'title','确认修改','Review changes'),(78,'old_label','原时间','Current'),(79,'current_day','周六 10月24日','Sat, 24 Oct'),(80,'current_time','14:00–15:00','14:00–15:00'),(81,'new_label','新时间','New'),(82,'draft_day','周日 10月25日','Sun, 25 Oct'),(83,'draft_time','10:00–11:00','10:00–11:00'),(84,'change_note','同一预约与日历将同步更新','Booking and calendar will update'),(85,'discard_changes_text','放弃修改','Discard'),(86,'confirm_changes_text','确认修改','Confirm change')],
11:[(120,'status_time','09:41','09:41'),(121,'status_date','10月22日 周四','Thu, 22 Oct'),(123,'title','取消体检预约','Cancel appointment'),(124,'cancel_note','这会取消预约并移除关联日历','Cancels booking and linked event'),(125,'scope_note','仅撤销日历不会取消预约','Undoing a calendar event keeps booking'),(126,'provider_name','安心体检中心','Willow Health Centre'),(128,'appointment_time','周日 10月25日 10:00–11:00','Sun, 25 Oct · 10:00–11:00'),(129,'keep_booking_text','保留预约','Keep booking'),(130,'confirm_cancel_text','确认取消','Confirm cancel')],
12:[(171,'status_time','09:41','09:41'),(172,'status_date','10月22日 周四','Thu, 22 Oct'),(174,'title','预约已就绪','Your booking is ready'),(175,'appointment_title','年度体检','Annual health check'),(176,'package_summary','基础套餐','Basic package'),(177,'appointment_time','周日 10月25日 10:00–11:00','Sun, 25 Oct · 10:00–11:00'),(178,'provider_name','安心体检中心','Willow Health Centre'),(179,'booking_label','预约','Booking'),(180,'booking_status','已确认','Confirmed'),(182,'calendar_label','日历','Calendar'),(183,'calendar_status','已同步','Synced'),(185,'return_booking_text','返回预约','Back to booking'),(186,'cancel_booking_text','取消预约','Cancel booking')],
}

SVG = {
'back':'<path d="m17 4-10 10 10 10"/>',
'clinic':'<path d="M4 27V3h20v24M1 27h26M9 7h2m6 0h2M9 12h2m6 0h2M9 17h2m6 0h2M11 27v-5h6v5"/>',
'package':'<rect x="4" y="2" width="20" height="24" rx="2"/><path d="M8 8h12M8 13h12M8 18h7"/>',
'heart':'<path d="M14 25 3 14C-5 1 9-4 14 5 19-4 33 1 25 14Z"/>',
'tooth':'<path d="M14 6C4-2 0 7 5 17c2 13 5 12 7 1 1-3 3-3 4 0 2 11 5 12 7-1C28 7 24-2 14 6Z"/>',
'eye':'<path d="M1 14Q14-4 27 14 14 32 1 14Z"/><circle cx="14" cy="14" r="5"/>',
'sliders':'<path d="M2 6h24M2 14h24M2 22h24"/><circle cx="9" cy="6" r="3"/><circle cx="20" cy="14" r="3"/><circle cx="11" cy="22" r="3"/>',
'calendar':'<rect x="3" y="5" width="22" height="21" rx="3"/><path d="M3 11h22M8 2v6m12-6v6M8 15h1m4 0h1m4 0h1M8 20h1m4 0h1m4 0h1"/>',
'mail':'<rect x="2" y="5" width="24" height="18" rx="3"/><path d="m3 7 11 9L25 7"/>',
'person':'<circle cx="14" cy="8" r="5"/><path d="M3 27v-3c0-12 22-12 22 0v3z"/>',
'check':'<circle cx="14" cy="14" r="12" fill="#5c8069"/><path d="m7 14 5 5 9-10" stroke="#ffffff"/>',
'location':'<path d="M14 27C-7 2 35-7 14 27Z"/><circle cx="14" cy="10" r="3"/>',
'arrow_down':'<path d="M14 2v23m-9-8 9 9 9-9"/>',
}

def author(number, manifest, atlas_ocr):
    scene=manifest['scenes'][number-1]; spec=SPECS[number]; directory=ROOT/scene['directory'];(directory/'assets').mkdir(exist_ok=True)
    generation=json.loads((directory/'generation.json').read_text());transform=generation['normalization'];scale=transform['uniform_scale']/2;ox,oy=[v/2 for v in transform['offset_pixels']]
    def rect(bounds):x,y,w,h=bounds;return [ox+x*scale,oy+y*scale,w*scale,h*scale]
    tree=dict(t='stack',id='page',x=0,y=0,w=406,h=776,bg=color('f0f5f2'),variant='surface',c=[]);nodes={'page':tree};assets={};controls={};measurements=[];labels={}
    def add(node,parent='page'):nodes[parent]['c'].append(node);nodes[node['id']]=node;return node
    def stack(id,bounds,parent='page',bg=None,radius=0):
        node=dict(t='stack',id=id,**dict(zip('xywh',rect(bounds))),c=[])
        if bg:node.update(bg=color(bg),variant='surface',radius=radius*scale)
        return add(node,parent)
    stack('screen',[0,0,234,513],bg='d9e9df' if number>2 else 'f8faf7',radius=12)
    def owner(bounds):
        x,y,w,h=bounds;candidates=[]
        for name,(a,b,c,d) in spec.get('cards',[]):
            if a<=x+w/2<=a+c and b<=y+h/2<=b+d:candidates.append((c*d,name))
        return min(candidates)[1] if candidates else 'screen'
    # Native surfaces replace the generated wallpaper texture. They are a declared visual approximation.
    if number>2:
        stack('wallpaper_upper',[0,0,234,105],'screen','d2e5df',12)
        stack('wallpaper_lower',[0,423,234,90],'screen','d5e6d6',12)
    for id,bounds in spec.get('cards',[]):
        x,y,w,h=bounds
        containers=[(c*d,name) for name,(a,b,c,d) in spec.get('cards',[]) if name in nodes and a<=x and b<=y and x+w<=a+c and y+h<=b+d]
        parent=min(containers)[1] if containers else 'screen'
        stack(id,bounds,parent,'eff3f0' if id.endswith('surface') or id in ('selected_summary','current_summary','cancel_summary') else PANEL,12)
    for id,bounds,filled,text_ids in spec['buttons']:
        stack(id,bounds,owner(bounds));surface=stack(id+'_surface',bounds,id,SAGE if filled else 'eff2ef',8)
        if id=='confirm_cancel':surface['bg']=color('c77969')
        if id in spec.get('disabled',[]) and filled:surface['bg']=color('cbd2cd')
        add(dict(t='button',id=id+'_control',**dict(zip('xywh',rect(bounds))),enabled=int(id not in spec.get('disabled',[]))),id)
        controls[id]={'event':'health.'+id,'source_bounds':bounds,'enabled':id not in spec.get('disabled',[]),'text_ids':text_ids,'ocr_ids':[r[0] for r in TEXT[number] if r[1] in text_ids]}
    reference=Image.open(directory/'reference.png').convert('RGB')
    if 'photo' in spec:
        x,y,w,h=rect(spec['photo']);box=[round(x*2),round(y*2),round(w*2),round(h*2)];a,b,c,d=box
        target=directory/'assets/clinic_photo.png';reference.crop((a,b,a+c,b+d)).save(target)
        add(dict(t='image',id='clinic_photo',x=a/2,y=b/2,w=c/2,h=d/2,src='',image_width=c,image_height=d),'screen')
        assets['clinic_photo']={'path':'assets/clinic_photo.png','sha256':sha(target),'method':'source_crop','reference_sha256':sha(directory/'reference.png'),'crop_pixels':box,'contains_ui':False,'fit':'contain','clip':True,'notes':'Visually inspected empty waiting-room photograph; no UI, text, diagnostics or people'}
    def icon(kind,bounds,id,parent=None):
        target=directory/'assets'/f'{id}.svg';target.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28" fill="none" stroke="#{SAGE}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{SVG[kind]}</svg>')
        add(dict(t='svg',id=id,**dict(zip('xywh',rect(bounds))),src=''),parent or owner(bounds))
        assets[id]={'path':f'assets/{id}.svg','sha256':sha(target),'method':'reference_svg','reference_sha256':sha(directory/'reference.png'),'fit':'stretch','clip':True,'notes':'Native vector tracing of visible source symbol; shape approximation, no raster or text'}
    for i,(kind,bounds) in enumerate(spec.get('icons',[])):icon(kind,bounds,f'{kind}_icon_{i}')
    if spec.get('dock'):
        stack('dock',spec['dock'],'screen','edf4eb',12)
        for i,kind in enumerate(['heart','calendar','mail'] if number>2 else ['heart','calendar','mail','person']):
            x=[42,102,162][i] if number>2 else [24,82,137,191][i]
            icon(kind,[x,459 if number>2 else 471,27 if number>2 else 18,27 if number>2 else 18],'dock_icon_'+kind,'dock')
    def native_text(id,cn,en,bounds,obs=None):
        control=next((key for key,value in controls.items() if id in value['text_ids']),None);parent=control or ('dock' if id.startswith('dock_') and 'dock' in nodes else owner(bounds));x,y,w,h=rect(bounds)
        fill=next((v[2] for v in spec['buttons'] if v[0]==control),False)
        ink='ffffff' if fill else INK
        if id=='morning_note':ink='bf914a'
        if id in ('afternoon_note','draft_availability'):ink=SAGE
        node=dict(t='text',id=id,text=cn,x=x,y=y,w=w+3,h=h+4,size=h*.93,weight=400,line_height=h+4,alignx=0,variant='single_line',font_src='self:resources/service/NotoSansSC-Regular.ttf',color=color(ink))
        add(node,parent);labels[id]={'cn':cn,'en':en};measurements.append({'id':id,'atlas_observation':obs,'source_bounds':bounds,'logical_ink_bounds':[x,y,w,h],'source_text':atlas_ocr['observations'][obs]['text'] if obs is not None else None,'text':cn,'basis':'Apple Vision OCR with visually reviewed corrections' if obs is not None else 'Visible source label manually measured where OCR missed it'})
    cx,cy,_,_=scene['crop']
    for obs,id,cn,en in TEXT[number]:
        a,b,w,h=atlas_ocr['observations'][obs]['bounds'];bounds=[a-cx,b-cy,w,h]
        # OCR included adjacent icon glyphs; keep text inside the actual label region.
        if number==2 and id=='optional_note':bounds=[64,232,134,15]
        if number==2 and id=='edit_note':bounds=[64,294,137,16]
        if number==11 and id=='provider_name':bounds=[54,222,108,16]
        if number==12 and id=='booking_label':bounds=[60,273,29,16]
        native_text(id,cn,en,bounds,obs)
    if number==1:native_text('status_time','9:41','9:41',[24,13,27,10])
    if number>2:
        for id,cn,en,x in [('dock_health','健康','Health',45),('dock_calendar','日历','Calendar',104),('dock_mail','邮件','Mail',164)]:native_text(id,cn,en,[x,491,24,12])
    if number==4:
        for key,y in [('basic',163),('dental',218),('vision',274)]:
            n=stack(key+'_checkbox',[188,y,17,17], 'basic_package' if key=='basic' else 'toggle_'+key, SAGE if key=='basic' else PANEL,3);n.update(border=.8,bordercolor=color(SAGE if key=='basic' else '9fa9a2'))
    if number in (5,6):
        for key,y in [('morning',207),('afternoon',270)]:
            n=stack(key+'_radio',[36,y,16,16],'conflict_slot' if key=='morning' else 'afternoon',SAGE if number==6 and key=='afternoon' else PANEL,8);n.update(ellipse=1,border=.8,bordercolor=color('9fa9a2'))
    if number==9:
        n=stack('draft_radio',[32,289,16,16],'new_slot_surface',PANEL,8);n.update(ellipse=1,border=.8,bordercolor=color(SAGE))
    for node in walk(tree):
        if 'c' in node:node['c'].sort(key=lambda child:child['t']=='text')
    for id in controls:
        children=nodes[id]['c'];binding={'control':[next(i for i,n in enumerate(children) if n['t']=='button')]};label=next((i for i,n in enumerate(children) if n['t']=='text'),None)
        if label is not None:binding['label']=[label]
        nodes[id]['kit']=json.dumps({'widget':'KitButton','bindings':binding},separators=(',',':'))
    contract={'schema_version':1,'id':scene['design_id'],'app':'health','number':number,'title':scene['title'],'structure':'Measured native application and health/calendar-owned service cards','artboard':[406,776],'font_family':'Noto Sans SC','content_source':'Fictional annual checkup booking; optional items are provider choices, not medical recommendations','palette':{'name':'Sage','page':'#d9e9df','panel':'#fcfdfb','ink':'#26342e','accent':'#5c8069'},'graphics':{},'tree':tree}
    save(directory/'contract.json',contract)
    annotations=[{'id':n['id'],'bounds':[n[k] for k in 'xywh'],'reviewed':True,**{k:n[k] for k in ('bg','radius','border','bordercolor') if k in n}} for n in walk(tree) if n['t']!='text']
    save(directory/'annotations.json',{'schema_version':1,'reference_sha256':sha(directory/'reference.png'),'method':'Measured source-pixel geometry; native flat wallpaper and traced icons are explicit approximations','elements':annotations})
    mapped=copy.deepcopy(tree);rows={row['id']:row for row in measurements}
    for node in walk(mapped):
        if node['t']!='text':continue
        x,y,w,h=rows[node['id']]['logical_ink_bounds'];(x0,y0,x1,y1),advance,asc,desc=metrics(str(ROOT/'fonts/NotoSansSC-Regular.ttf'),node['text']);size=min(h/(y1-y0),w/(x1-x0));ink_h=(y1-y0)*size
        node.update(x=x-x0*size,y=y+(h-ink_h)/2-2,w=advance*size+4,h=ink_h+4,size=size,tracking=0,line_height=ink_h+4,font_asc=y1+2/size-asc,font_desc=(y1*size+2-(ink_h+4))/size-desc)
    save(directory/'mapped.json',{'schema_version':1,'reference_sha256':sha(directory/'reference.png'),'tree':mapped,'changes':[{'source':'Actual source atlas OCR and explicit surface geometry, fitted with bundled Noto glyph metrics'}],'limits':['Generated atlas actual size 962x1635, requested 2400x3456','No native Studio capture or visual acceptance yet','Wallpaper is native flat tone approximation; source photo only in first app screen']})
    save(directory/'source-measurements.json',{'reference_sha256':sha(directory/'reference.png'),'atlas_sha256':sha(ROOT/'source/atlas.png'),'text':measurements,'spec':spec,'ignored_ocr':[{'index':i,'text':o['text'],'reason':'Decorative icon or dock duplication'} for i,o in enumerate(atlas_ocr['observations']) if cx<=o['bounds'][0]+o['bounds'][2]/2<cx+234 and cy<=o['bounds'][1]+o['bounds'][3]/2<cy+513 and i not in [r[0] for r in TEXT[number]]]})
    semantic=propose(directory);semantic.update(contract_sha256=sha(directory/'contract.json'),reference_sha256=sha(directory/'reference.png'))
    for element in semantic['elements']:
        if element['id'] in assets:element.update(role='photo' if element['id']=='clinic_photo' else 'icon',decision='reviewed',confidence=1,basis='Explicit inspected source region or traced vector symbol',asset=assets[element['id']])
        elif element['id'] in dict(spec.get('cards',[])):element.update(role='card',decision='reviewed',basis='Explicit measured service composition ownership')
    save(directory/'semantic-map.json',semantic);write_brief(directory,semantic)
    save(directory/'service-actions.json',{'frame_id':number,'controls':controls,'source':scene['design_id'],'simulation':True})
    save(directory/'labels.json',labels)
    return {'labels':labels,'controls':controls,'surface':scene['surface'],'nodeIds':list(nodes)}

if __name__=='__main__':
    manifest=json.loads((ROOT/'image-to-appcard-flow.json').read_text());atlas=json.loads((ROOT/'source/atlas.ocr.json').read_text());frames={}
    for number in range(1,13):
        frames[number]=author(number,manifest,atlas);print('authored health-'+str(number).zfill(2),flush=True)
    save(ROOT/'wizard/frames.json',frames)
    service=ROOT/'wizard/service.mjs'
    if service.exists():
        content=service.read_text();content=re.sub(r'^const FRAMES = .*?; // populated from measured source labels by scripts/author.py$', 'const FRAMES = '+json.dumps(frames,ensure_ascii=False,separators=(',',':'))+'; // populated from measured source labels by scripts/author.py', content, count=1, flags=re.M)
        service.write_text(content)
