#!/usr/bin/env python3
"""Reconstruct the single generated atlas from measured pixels, never UI crops."""
from pathlib import Path
import copy, hashlib, importlib.util, json, re, shutil, sys
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
MAIN=ROOT.parents[1]
PIPE=MAIN/'lab/image-to-appcard'
sys.path.insert(0,str(PIPE))
from catalogue import walk
from observe import metrics
from semantics import propose,write_brief,preflight
import compile as compiler
compiler.GALLERY=ROOT/'artwork'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def col(s):return int('ff'+s.lstrip('#'),16)
INK='31413c';MUTED='75837c';SAGE='608570';PANEL='fcfdfb'
SVG={
 'back':'<path d="m18 4-10 10 10 10"/>',
 'calendar':'<rect x="3" y="5" width="22" height="21" rx="3"/><path d="M3 11h22M8 2v6m12-6v6m-12 7h1m4 0h1m4 0h1m-11 5h1m4 0h1m4 0h1"/>',
 'message':'<path d="M4 21 3 27l7-3c18 5 21-22 5-22C1 2-2 16 4 21z"/>',
 'group':'<circle cx="14" cy="7" r="4"/><circle cx="5" cy="11" r="3"/><circle cx="23" cy="11" r="3"/><path d="M6 27c0-18 16-18 16 0M1 25c0-10 5-12 8-9m18 9c0-10-5-12-8-9"/>',
 'wallet':'<rect x="2" y="5" width="24" height="19" rx="3"/><path d="M2 10h24m-9 5h9m-5 4h1"/>',
 'person':'<circle cx="14" cy="8" r="5"/><path d="M3 27v-3c0-12 22-12 22 0v3z"/>',
 'pin':'<path d="M14 27C-6 9 7-5 18 3c10 7 3 17-4 24z"/><circle cx="14" cy="10" r="3"/>',
 'receipt':'<path d="M5 2h18v25l-3-2-3 2-3-2-3 2-3-2-3 2zM9 8h10M9 13h10M9 18h7"/>',
 'check':'<circle cx="14" cy="14" r="12"/><path d="m7 14 5 5 9-10"/>',
 'warning':'<circle cx="14" cy="14" r="12"/><path d="M14 6v10m0 5v1"/>',
 'search':'<circle cx="11" cy="11" r="8"/><path d="m17 17 8 8"/>',
}

# Every rectangle is measured in pixels of its original generated panel crop.
# Buttons carry wrapper ID, rect, filled, source OCR indices, and service event.
SPECS={
1:dict(cards=[('inbox_list',[6,93,226,200])],photos=[('group_avatar',[13,110,42,43]),('teacher_avatar',[13,173,42,44]),('family_avatar',[13,237,42,42])],
 buttons=[('open_invite',[12,394,217,37],True,[13],'messages.open_invite')],icons=[('search',[20,68,12,12])],surfaces=[('search_field',[13,60,216,29],'eeeeec'),('selected_chat',[6,99,228,63],'e4ede5')],skip=[3,4],extras=[('search_label','搜索',[40,66,120,16])]),
2:dict(cards=[('invitation',[9,244,226,142])],photos=[('organizer_avatar',[7,65,38,38]),('venue_photo',[44,118,188,121])],
 buttons=[('back_messages',[7,29,22,22],False,[],'messages.back'),('open_poll',[10,394,108,36],True,[66],'reunion.open_poll'),('group_info',[126,394,108,36],False,[67],'reunion.view_info')],plain=['back_messages'],
 icons=[('back',[9,32,14,14]),('calendar',[21,258,20,20]),('calendar',[23,302,13,14]),('calendar',[23,331,13,14]),('calendar',[23,362,13,14])],skip=[55,60],surfaces=[('invitation_message',[50,83,185,29],'f2f5f1')]),
3:dict(cards=[('poll_card',[14,113,216,235])],buttons=[('choose_time',[29,257,186,33],True,[106],'reunion.choose_time'),('view_invite',[29,298,186,34],False,[107],'messages.open_invite')],icons=[('calendar',[31,126,23,23])],dock=[0,394,244,62],skip=[101]),
4:dict(cards=[('poll_card',[14,108,216,261])],buttons=[('friday',[25,148,194,45],False,[155,156],'reunion.choose_friday'),('saturday',[25,201,194,47],False,[157,158],'reunion.choose_saturday'),('sunday',[25,257,194,47],False,[159,160],'reunion.choose_sunday'),('confirm_attendance',[25,322,95,34],True,[161],'reunion.confirm_attendance'),('back_poll',[126,322,93,34],False,[162],'reunion.back_poll')],disabled=['friday','confirm_attendance'],icons=[('calendar',[27,120,16,18]),('warning',[36,158,20,20]),('calendar',[37,214,18,19]),('calendar',[37,270,18,19])],dots=[('friday_dot',[197,164,14,14],False),('saturday_dot',[196,217,15,15],False),('sunday_dot',[196,273,15,15],False)],dock=[0,394,243,62],skip=[151]),
5:dict(cards=[('poll_card',[13,113,217,274])],buttons=[('friday',[25,149,192,44],False,[19,20],'reunion.choose_friday'),('saturday',[25,200,192,47],False,[21,22],'reunion.choose_saturday'),('sunday',[25,257,192,47],False,[23,24],'reunion.choose_sunday'),('confirm_attendance',[25,342,94,31],True,[26],'reunion.confirm_attendance'),('reset_selection',[127,342,90,31],False,[27],'reunion.reset_selection')],disabled=['friday'],icons=[('calendar',[28,120,16,18]),('warning',[34,158,20,20]),('calendar',[36,214,18,19]),('calendar',[36,270,18,19])],dots=[('friday_dot',[193,164,14,14],False),('saturday_dot',[192,216,15,15],True),('sunday_dot',[192,271,15,15],False)],dock=[0,397,240,68],skip=[29]),
6:dict(cards=[('rsvp_card',[15,125,215,247])],buttons=[('view_registration',[29,323,186,33],True,[78],'reunion.view_info')],icons=[('check',[32,143,32,32]),('warning',[32,285,16,17])],dock=[0,397,244,68],skip=[76]),
7:dict(cards=[('confirmed_card',[14,31,217,198]),('calendar_card',[14,236,217,151])],buttons=[('view_reunion',[30,184,185,32],True,[118],'reunion.view_info'),('ack_calendar',[28,350,85,29],True,[],'calendar.acknowledge'),('undo_calendar',[121,350,95,29],False,[123],'calendar.undo')],icons=[('calendar',[31,49,19,20]),('pin',[32,115,13,15]),('pin',[32,138,13,15]),('calendar',[31,253,19,20])],dock=[0,397,244,68],skip=[125],extras=[('ack_label','确认',[55,358,37,14])],corrections={118:('查看聚会',[67,194,116,14]),123:('撤销日程',[135,358,74,14]),121:('10月24日 18:30–21:00',[52,307,146,18]),116:('木光餐厅 · 桂花路8号',[54,137,150,17])},refinements=['Move calendar acknowledgement into its own service card, split footer into explicit confirm and undo actions; reunion card opens app details'] ),
8:dict(cards=[('confirmed_card',[14,32,217,204]),('calendar_card',[14,243,217,146])],buttons=[('view_reunion',[29,192,189,30],True,[175],'reunion.view_info'),('restore_calendar',[33,343,179,30],False,[179],'calendar.restore')],icons=[('calendar',[31,49,19,20]),('pin',[32,117,13,15]),('pin',[32,140,13,15]),('calendar',[31,253,22,23]),('calendar',[31,315,14,15])],dock=[0,397,243,68],skip=[169],corrections={175:('查看聚会',[65,201,114,15])}),
9:dict(cards=[('payment_card',[13,34,216,261]),('rsvp_summary',[13,304,216,64])],buttons=[('pay_contribution',[25,248,97,34],True,[46],'payment.pay'),('cancel_payment',[126,248,92,34],False,[47],'payment.cancel'),('view_reunion',[13,304,216,64],False,[],'reunion.view_info')],plain=['view_reunion'],icons=[('wallet',[29,47,25,25]),('group',[28,318,25,25])],dock=[0,390,240,66],skip=[35],extras=[('dock_calendar_label','日历',[79,429,22,14])]),
10:dict(cards=[('payment_card',[14,32,216,263]),('rsvp_summary',[14,304,216,64])],buttons=[('reopen_payment',[29,246,186,35],True,[91],'payment.reopen'),('view_reunion',[14,304,216,64],False,[],'reunion.view_info')],plain=['view_reunion'],icons=[('warning',[29,46,27,28]),('group',[28,318,25,25])],dock=[0,390,244,66]),
11:dict(cards=[('payment_receipt',[14,28,217,254]),('confirmed_summary',[14,289,217,87])],buttons=[('view_reunion',[29,239,186,33],True,[139],'reunion.view_info')],icons=[('check',[29,42,30,30]),('calendar',[28,299,18,18]),('pin',[30,327,12,13]),('pin',[30,350,12,13])],dock=[0,390,244,66]),
12:dict(cards=[('app_detail',[10,192,222,237])],photos=[('venue_photo',[1,55,240,131])],buttons=[('back_desktop',[10,386,219,32],True,[198],'navigation.desktop'),('detail_back',[6,25,23,26],False,[],'navigation.desktop')],plain=['detail_back'],icons=[('back',[8,31,14,15]),('calendar',[15,230,13,14]),('pin',[15,253,13,14]),('person',[15,281,13,14]),('person',[15,303,13,14]),('wallet',[15,327,13,14]),('receipt',[15,350,13,14])],skip=[189]),
}
CORRECT={6:'王宁：好久不见，一起聚聚吧',13:'查看邀请',18:'聚会 · 选择时间',20:'与工作例会冲突',21:'周六 10月24日 18:30',22:'日历空闲',24:'日历空闲',25:'已选择 周六晚餐',27:'重新选择',31:'聚会',36:'支付 · 待付款',39:'收款人',44:'周六 10月24日 18:30',49:'你已确认参加本次聚会',59:'好久不见，找个周末一起吃饭吧',62:'2016届同学聚会',78:'查看报名',90:'聚会报名不受影响',91:'重新打开支付',93:'你已确认参加本次聚会',106:'选择时间',156:'与工作例会冲突',157:'周六 10月24日 18:30',160:'日历空闲',166:'支付',176:'日历记录已撤销',177:'报名仍然有效',178:'周六 10月24日 18:30',181:'日历',185:'聚会详情',195:'凑份子'}

def author(number):
 states=json.loads((ROOT/'source/crops.json').read_text())['states'];state=states[number-1];spec=copy.deepcopy(SPECS[number])
 d=ROOT/state['directory'];d.mkdir(parents=True,exist_ok=True);(d/'assets').mkdir(exist_ok=True)
 src=Image.open(ROOT/'source'/f'frame-{number:02}.png').convert('RGB');scale=min(812/src.width,1552/src.height);fw,fh=round(src.width*scale),round(src.height*scale);ox,oy=(812-fw)//2,(1552-fh)//2
 ref=Image.new('RGB',(812,1552),'#f0f5f2');ref.paste(src.resize((fw,fh),Image.Resampling.LANCZOS),(ox,oy));ref.save(d/'reference.png');sx,sy=fw/src.width/2,fh/src.height/2
 def rect(b):return [b[0]*sx+ox/2,b[1]*sy+oy/2,b[2]*sx,b[3]*sy]
 tree={'t':'stack','id':'page','x':0,'y':0,'w':406,'h':776,'variant':'surface','bg':col('f0f5f2'),'c':[]};nodes={'page':tree};assets={};controls={};texts=[]
 def add(node,parent='page'):nodes[parent].setdefault('c',[]).append(node);nodes[node['id']]=node;return node
 def stack(id,b,parent='page',bg=PANEL,radius=12):return add(dict(t='stack',id=id,**dict(zip('xywh',rect(b))),variant='surface',bg=col(bg),radius=min(radius,min(b[2:])/2)*sx,c=[]),parent)
 stack('screen',[0,0,src.width,src.height],bg='fafbf9' if state['surface']=='app' else 'edf3ef',radius=0)
 def owner(b):
  x,y,w,h=b;candidates=[(bb[2]*bb[3],id) for id,bb in spec['cards'] if bb[0]<=x+w/2<=bb[0]+bb[2] and bb[1]<=y+h/2<=bb[1]+bb[3]]
  return min(candidates)[1] if candidates else 'screen'
 for id,b in spec['cards']:stack(id,b,'screen')
 for id,b,color in spec.get('surfaces',[]):stack(id,b,owner(b),color,7)
 if spec.get('dock'):stack('dock',spec['dock'],'screen','f8faf7',17)
 for id,b in spec.get('photos',[]):
  x,y,w,h=rect(b);px,py,pw,ph=round(x*2),round(y*2),round(w*2),round(h*2);p=d/'assets'/f'{id}.png';ref.crop((px,py,px+pw,py+ph)).save(p)
  add(dict(t='image',id=id,x=px/2,y=py/2,w=pw/2,h=ph/2,src='',image_width=pw,image_height=ph),owner(b));assets[id]={'path':f'assets/{p.name}','sha256':sha(p),'method':'source_crop','reference_sha256':sha(d/'reference.png'),'crop_pixels':[px,py,pw,ph],'contains_ui':False,'fit':'contain','clip':True,'notes':'Reviewed text-free venue photography or contact avatar only, cropped from original generated artwork'}
 for id,b,filled,obs,event in spec.get('buttons',[]):
  stack(id,b,owner(b),PANEL,0);surface=stack(id+'_surface',b,id,SAGE if filled else PANEL,7)
  if not filled:surface.update(border=.65,bordercolor=col('a9bdb0'))
  if id in spec.get('plain',[]):surface.update(bg=0,radius=0);surface.pop('border',None);surface.pop('bordercolor',None)
  if id=='friday':surface['bg']=col('faf4e7')
  if number==5 and id=='saturday':surface.update(bg=col('edf4ef'),border=.8,bordercolor=col(SAGE))
  enabled=id not in spec.get('disabled',[])
  if not enabled and filled:surface['bg']=col('dce4de')
  add(dict(t='button',id=id+'_control',**dict(zip('xywh',rect(b))),enabled=int(enabled)),id)
  controls[id]={'event':event,'enabled':enabled,'source_bounds':b,'ocr_ids':obs,'textIds':[]}
 def label(id,text,b,parent=None,obs=None):
  x,y,w,h=rect(b);parent=parent or owner(b);filled=next((v[2] for v in spec.get('buttons',[]) if v[0]==parent),False);color='ffffff' if filled else INK
  if '冲突' in text:color='bf883e'
  elif text=='日历空闲':color=SAGE
  elif text.startswith('来自') or text in ['消息','日历','聚会','支付']:color=MUTED
  n=add(dict(t='text',id=id,text=text,x=x,y=y,w=w+4,h=h+4,size=h*.9,weight=400,line_height=h+4,variant='single_line',alignx=0,font_src='self:resources/service/NotoSansSC-Regular.ttf',color=col(color)),parent)
  texts.append({'id':id,'text':text,'atlas_ocr_index':obs,'source_bounds':b,'logical_ink_bounds':[x,y,w,h]})
  if parent in controls:controls[parent]['textIds'].append(id)
 atlas=json.loads((ROOT/'source/atlas.ocr.json').read_text());cx,cy,cw,ch=state['crop'];ignored=[]
 for i,o in enumerate(atlas['observations']):
  a,b,c,e=o['bounds']
  if not(cx<=a+c/2<cx+cw and cy<=b+e/2<cy+ch):continue
  if i in spec.get('skip',[]):ignored.append({'index':i,'text':o['text'],'reason':'OCR icon/noise replaced by native vector or corrected native label'});continue
  bounds=[a-cx,b-cy,c,e];text=CORRECT.get(i,o['text']);correction=spec.get('corrections',{}).get(i)
  if correction:text,bounds=correction
  text=re.sub(r'\s*[•·]\s*',' · ',text)
  parent=next((id for id,data in controls.items() if i in data['ocr_ids']),None)
  label(f'text_{i}',text,bounds,parent,i)
 for id,text,b in spec.get('extras',[]):label(id,text,b,'ack_calendar' if id=='ack_label' else None)
 def icon(kind,b,id,parent=None):
  p=d/'assets'/f'{id}.svg';p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28" fill="none" stroke="#{SAGE}" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round">{SVG[kind]}</svg>')
  add(dict(t='svg',id=id,**dict(zip('xywh',rect(b))),src=''),parent or owner(b));assets[id]={'path':f'assets/{p.name}','sha256':sha(p),'method':'reference_svg','reference_sha256':sha(d/'reference.png'),'fit':'stretch','clip':True,'notes':'Native SVG reconstruction of a reviewed line symbol; no embedded raster or text'}
 for i,(kind,b) in enumerate(spec.get('icons',[])):icon(kind,b,f'{kind}_icon_{i}')
 if spec.get('dock'):
  x,y,w,h=spec['dock']
  for i,kind in enumerate(['message','calendar','group','wallet']):icon(kind,[x+20+i*(w-64)/3,y+9,22,23],f'dock_{kind}','dock')
 for id,b,selected in spec.get('dots',[]):
  n=stack(id,b,owner(b),SAGE if selected else PANEL,20);n.update(ellipse=1,border=.7,bordercolor=col(SAGE))
 # All labels remain above decorative native surfaces. Kit bindings reference actual children.
 for n in walk(tree):
  if 'c' in n:n['c'].sort(key=lambda child:child['t']=='text')
 for id in controls:
  children=nodes[id]['c'];binding={'control':[next(i for i,n in enumerate(children) if n['t']=='button')]};lab=next((i for i,n in enumerate(children) if n['t']=='text'),None)
  if lab is not None:binding['label']=[lab]
  nodes[id]['kit']=json.dumps({'widget':'KitButton','bindings':binding},separators=(',',':'))
 contract={'schema_version':1,'id':d.name,'app':'service','number':number,'title':state['title'],'artboard':[406,776],'font_family':'Noto Sans SC','graphics':{},'content_source':'Single generated reunion atlas; fictional fixtures','tree':tree}
 save(d/'contract.json',contract);shutil.copy2(ROOT/'source/prompt.txt',d/'image-prompt.md')
 generation=json.loads((ROOT/'source/generation.json').read_text());generation.update(image_sha256=sha(d/'reference.png'),original_image_sha256=sha(ROOT/'source'/f'frame-{number:02}.png'),actual_dimensions=[812,1552],source_crop=state['crop'],normalization={'method':'uniform contain; derived reference, not a new generation','fitted_pixels':[fw,fh],'offset_pixels':[ox,oy]});save(d/'generation.json',generation)
 save(d/'annotations.json',{'schema_version':1,'reference_sha256':sha(d/'reference.png'),'method':'Measured source pixel card/control rectangles; flat native surfaces approximate botanical background; text corrections and calendar UX refinements declared','elements':[dict(id=n['id'],bounds=[n[k] for k in 'xywh'],reviewed=True,**{k:n[k] for k in ['bg','radius','border','bordercolor'] if k in n}) for n in walk(tree) if n['t']!='text']})
 mapped=copy.deepcopy(tree);rows={r['id']:r for r in texts};font=MAIN/'fonts/NotoSansSC-Regular.ttf'
 for n in walk(mapped):
  if n['t']!='text':continue
  x,y,w,h=rows[n['id']]['logical_ink_bounds'];(x0,y0,x1,y1),adv,asc,desc=metrics(str(font),n['text']);size=min(h/max(y1-y0,.1),w/max(x1-x0,.1));ink_h=(y1-y0)*size
  n.update(x=x-x0*size,y=y+(h-ink_h)/2-2,w=adv*size+4,h=ink_h+4,size=size,tracking=0,line_height=ink_h+4,font_asc=y1+2/size-asc,font_desc=(y1*size+2-(ink_h+4))/size-desc)
 save(d/'mapped.json',{'schema_version':1,'reference_sha256':sha(d/'reference.png'),'tree':mapped,'changes':[{'source':'Actual atlas OCR and source-pixel measurements with exact Noto glyph metrics'}],'limits':['1045×1505 source atlas; normalized references do not add native source detail','Decorative leafy backdrop approximated by native flat surface',*spec.get('refinements',[])]})
 save(d/'source-measurements.json',{'atlas_sha256':sha(ROOT/'source/atlas.png'),'text':texts,'ignored_ocr':ignored,'spec':spec})
 if (d/'semantic-map.json').exists():(d/'semantic-map.json').unlink()
 semantics=propose(d)
 for row in semantics['elements']:
  if row['id'] in assets:row.update(role='photo' if nodes[row['id']]['t']=='image' else 'icon',decision='reviewed',confidence=1,basis='Reviewed artwork-only source region or native vector icon',asset=assets[row['id']])
  elif row['id'] in dict(spec['cards']):row.update(role='card',decision='reviewed',confidence=1,basis='Explicit event-specific service composition with native children')
 save(d/'semantic-map.json',semantics);write_brief(d,semantics)
 save(d/'service-actions.json',{'frame_id':number,'controls':controls,'source':'reunion','simulation':True})
 result=preflight(d);compiler.compile_page(d)
 return {'id':d.name,'nodes':len(nodes),'controls':controls,'texts':{n['id']:{'cn':n['text'],'bounds':[n[k] for k in 'xywh'],'size':n['size']} for n in walk(mapped) if n['t']=='text'},'pass':result['pass']}

if __name__=='__main__':
 result=[author(i) for i in range(1,13)];save(ROOT/'source/native-catalogue.json',result);print(json.dumps({'frames':len(result),'native_nodes':sum(r['nodes'] for r in result),'semantic_pass':all(r['pass'] for r in result)}))
