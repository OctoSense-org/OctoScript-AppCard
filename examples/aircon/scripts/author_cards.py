#!/usr/bin/env python3
"""Measured storyboard intake; native labels/controls, artwork-only crops.

Source atlas and original crops are immutable. The parity reference is a
uniformly fitted frame on the pipeline's 406x776 artboard, never distorted.
"""
from pathlib import Path
import copy, hashlib, json, re, sys
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PIPE = ROOT.parents[1] / 'lab/image-to-appcard'
sys.path.insert(0, str(PIPE))
from catalogue import walk
from semantics import propose, write_brief

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, v): Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2)+'\n')
def col(v): return int('ff'+v.removeprefix('#'),16)

INK='31413c'; MUTED='75837c'; SAGE='608570'; PANEL='fcfdfb'
SVG = {
 'back':'<path d="M17 4 7 14l10 10"/>',
 'close':'<path d="m5 5 18 18M23 5 5 23"/>',
 'share':'<path d="M8 12H4v14h20V12h-4M14 20V2m-6 6 6-6 6 6"/>',
 'mail':'<rect x="2" y="5" width="24" height="18" rx="3"/><path d="m3 7 11 9L25 7"/>',
 'calendar':'<rect x="3" y="5" width="22" height="21" rx="3"/><path d="M3 11h22M8 2v6m12-6v6m-12 7h1m4 0h1m4 0h1m-11 5h1m4 0h1m4 0h1"/>',
 'wallet':'<rect x="2" y="5" width="24" height="19" rx="3"/><path d="M2 10h24m-9 5h9m-5 4h1"/>',
 'bag':'<path d="M5 10h18l2 16H3zm5-3c0-8 8-8 8 0"/>',
 'home':'<path d="m2 13 12-11 12 11h-4v13h-6v-8h-4v8H6V13z"/>',
 'order':'<path d="M4 2h19v25H4zM8 8h11M8 13h7M8 18h5"/><path d="M19 15v8m-3-4h6"/>',
 'truck':'<path d="M2 5h15v16H2zm15 6h5l4 6v4h-9"/><circle cx="7" cy="22" r="3"/><circle cx="22" cy="22" r="3"/>',
 'wrench':'<path d="M24 2c-8-3-12 4-9 9L3 23c-2 3 1 5 3 3l12-12c7 2 12-3 9-10l-6 6-3-3z"/>',
 'person':'<circle cx="14" cy="8" r="5"/><path d="M3 27v-3c0-12 22-12 22 0v3z"/>',
 'check':'<circle cx="14" cy="14" r="12"/><path d="m7 14 5 5 9-10" stroke="#ffffff"/>',
}

# Source-pixel measurements, reviewed against each original frame.
SPECS = {
 1: dict(cards=[], photos=[('product_photo',[0,127,512,423])],
   buttons=[('buy',[24,979,463,71],True,[9],'shopping.buy')],
   icons=[('back',[23,70,32,40]),('share',[449,71,36,35]),('truck',[25,834,39,34]),('calendar',[25,902,38,37])],
   lines=[[18,796,472,1]],skip=[3]),
 2: dict(cards=[('order_product',[20,213,475,190]),('order_details',[20,404,475,295])],
   photos=[('product_photo',[41,251,125,122])],
   buttons=[('back',[20,67,40,52],False,[],'navigation.desktop'),('view_logistics',[26,969,212,73],False,[61],'navigation.logistics'),('support',[279,969,209,72],False,[62],'navigation.support')],
   icons=[('back',[23,70,32,40]),('check',[30,152,40,40]),('person',[49,431,32,33]),('calendar',[49,552,35,34]),('wrench',[48,635,35,34])],
   lines=[[44,527,425,1],[44,609,425,1],[45,743,2,139]],
   dots=[[38,730,18,18,True],[38,800,18,18,True],[38,873,18,18,False]],skip=[45,52]),
 3: dict(cards=[('order_card',[28,235,455,528])],photos=[('product_photo',[55,345,138,138])],
   buttons=[('view_order',[57,658,187,68],True,[110],'navigation.order'),('collapse',[287,658,160,68],False,[111],'card.dismiss')],
   icons=[('order',[62,268,45,45])],dock=[0,927,523,160]),
 4: dict(cards=[('logistics_card',[28,228,572,603])],
   buttons=[('courier',[61,724,218,68],False,[169],'navigation.courier'),('delivery_time',[331,724,205,68],False,[170],'navigation.delivery_time')],
   icons=[('truck',[58,267,58,42]),('home',[59,607,31,31])],
   lines=[[106,496,395,3]],dots=[[94,486,23,23,False],[287,484,29,29,True],[490,486,23,23,False]],dock=[0,928,637,158]),
 5: dict(cards=[('installation_card',[17,153,466,678])],photos=[('product_photo',[37,442,161,146])],
   buttons=[('choose_time',[38,734,203,68],True,[19],'installation.open_slots'),('defer',[267,735,177,67],False,[20],'installation.defer')],
   icons=[('wrench',[41,184,44,45]),('check',[40,675,26,26])],dock=[12,867,488,154]),
 6: dict(cards=[('installation_card',[18,145,480,740])],
   buttons=[('close',[427,165,54,54],False,[],'installation.close_slots'),('saturday',[43,287,206,61],True,[69],'installation.choose_day'),('sunday',[274,287,197,61],False,[70],'installation.choose_day'),('conflict_slot',[43,374,430,120],False,[71,72],'installation.choose_slot'),('afternoon',[43,509,430,121],False,[73,74],'installation.choose_slot'),('confirm_booking',[42,789,429,71],True,[77],'installation.confirm')],
   icons=[('close',[442,181,24,24]),('home',[46,665,28,27])],lines=[[45,717,418,1]],
   dots=[[412,413,35,35,False],[412,548,35,35,False]],disabled=['conflict_slot','confirm_booking'],dock=[18,892,482,131],skip=[68]),
 7: dict(cards=[('installation_card',[18,145,483,740])],
   buttons=[('close',[431,165,54,54],False,[],'installation.close_slots'),('saturday',[43,287,208,61],True,[123],'installation.choose_day'),('sunday',[274,287,200,61],False,[124],'installation.choose_day'),('conflict_slot',[43,374,432,120],False,[125,126],'installation.choose_slot'),('afternoon',[43,509,432,120],False,[127,128],'installation.choose_slot'),('cancel_selection',[43,788,183,67],False,[131],'installation.close_slots'),('confirm_booking',[251,788,223,67],True,[132],'installation.confirm')],
   icons=[('close',[446,181,24,24]),('home',[46,665,28,27])],lines=[[46,716,419,1]],
   dots=[[414,413,35,35,False],[405,537,51,54,True]],disabled=['conflict_slot'],dock=[18,892,485,131],skip=[122]),
}

CORRECTIONS={7:('送货上门 · 专业安装',[81,832,245,30]),54:('到货后预约安装',[105,636,172,30]),
 13:('安装服务 · 待预约',[106,187,204,40]),18:('已送达 · 周五 15:20',[81,674,224,30]),
 74:('日历空闲',None),128:('日历空闲',None),75:('家 · 海棠路18号',[83,666,173,30]),
 129:('家 · 海棠路18号',[83,666,173,30]),167:('家 · 海棠路18号',[107,606,196,30]),
 172:('18',None)}

try:
 from late_specs import SPECS as LATE_SPECS, CORRECTIONS as LATE_CORRECTIONS
 SPECS.update(LATE_SPECS);CORRECTIONS.update(LATE_CORRECTIONS)
except ImportError:
 pass

def author(number):
 flow=json.loads((ROOT/'source/flow.json').read_text())
 state=flow['states'][number-1]; spec=copy.deepcopy(SPECS[number]); d=ROOT/'cards'/f'aircon-{number:02d}'
 d.mkdir(parents=True,exist_ok=True); (d/'assets').mkdir(exist_ok=True)
 original=ROOT/'source'/state['image']; src=Image.open(original).convert('RGB')
 scale=min(812/src.width,1552/src.height); fitted=(round(src.width*scale),round(src.height*scale))
 ox=(812-fitted[0])//2; oy=(1552-fitted[1])//2
 ref=Image.new('RGB',(812,1552),'#f0f5f2');ref.paste(src.resize(fitted,Image.Resampling.LANCZOS),(ox,oy));ref.save(d/'reference.png')
 # Tiny independent rounding errors of <=0.5 source pixel are recorded.
 sx=fitted[0]/src.width; sy=fitted[1]/src.height
 def rect(b): return [(b[0]*sx+ox)/2,(b[1]*sy+oy)/2,b[2]*sx/2,b[3]*sy/2]
 root=dict(t='stack',id='page',x=0,y=0,w=406,h=776,variant='surface',bg=col('f0f5f2'),c=[])
 nodes={'page':root}; assets={}; controls={}; annotations=[]
 def add(n,parent='page'):
  nodes[parent].setdefault('c',[]).append(n);nodes[n['id']]=n;return n
 def stack(id,b,parent='page',bg=None,radius=0):
  n=dict(t='stack',id=id,**dict(zip('xywh',rect(b))),c=[])
  if bg:n.update(variant='surface',bg=col(bg),radius=min(radius,min(b[2],b[3])/2)*sx/2)
  return add(n,parent)
 canvas=stack('screen',[0,0,src.width,src.height],bg='f1f6f3' if number>2 else 'fafbf9')
 def owner(b):
  x,y,w,h=b; candidates=[]
  for id,bb in spec.get('cards',[]):
   a,c,d,e=bb
   if a<=x+w/2<=a+d and c<=y+h/2<=c+e:candidates.append((d*e,id))
  return min(candidates)[1] if candidates else 'screen'
 for id,b in spec.get('cards',[]):stack(id,b,'screen',PANEL,32)
 if spec.get('dock'):
  stack('dock',spec['dock'],'screen','f7faf7',48)
 for id,b in spec.get('photos',[]):
  x,y,w,h=rect(b); px,py,pw,ph=round(x*2),round(y*2),round(w*2),round(h*2)
  path=d/'assets'/f'{id}.png'; ref.crop((px,py,px+pw,py+ph)).save(path)
  add(dict(t='image',id=id,x=px/2,y=py/2,w=pw/2,h=ph/2,src='',image_width=pw,image_height=ph),owner(b))
  assets[id]=dict(path=f'assets/{path.name}',sha256=sha(path),method='source_crop',reference_sha256=sha(d/'reference.png'),crop_pixels=[px,py,pw,ph],contains_ui=False,fit='contain',clip=True,notes='Artwork-only source region; product photography or technician portrait, visually reviewed')
 for i,b in enumerate(spec.get('lines',[])):stack(f'divider_{i}',b,owner(b),'d5ddd7',0)
 for id,b,filled,obs,action in spec.get('buttons',[]):
  parent=owner(b);g=stack(id,b,parent)
  g['kit']=json.dumps({'widget':'KitButton','bindings':{'control':[1],'label':[2]}},separators=(',',':'))
  surface=stack(id+'_surface',b,id,SAGE if filled else PANEL,20 if b[3]<100 else 26)
  if not filled:surface.update(border=.65,bordercolor=col('cbd6ce'))
  if id in spec.get('plain_buttons',[]):
   for key in ('bg','radius','border','bordercolor','variant'):surface.pop(key,None)
  if id in spec.get('disabled',[]) and filled:surface['bg']=col('e0e9e3')
  if id=='afternoon' and number==7:surface.update(bg=col('f0f5ef'),border=.7,bordercolor=col(SAGE))
  add(dict(t='button',id=id+'_control',**dict(zip('xywh',rect(b))),enabled=0 if id in spec.get('disabled',[]) else 1),id)
  controls[id]={'event':action,'ocr_ids':obs,'source_bounds':b,'enabled':id not in spec.get('disabled',[])}
 # All text remains native. Atlas observations are immutable measurement evidence.
 atlas=json.loads((ROOT/'source/atlas.ocr.json').read_text());cx,cy,cw,ch=state['crop'];ocr=[];ignored=[]
 for extra in spec.get('extra_text',[]):
  a,b,c,e=extra['bounds'];atlas['observations'].append({'text':extra['text'],'bounds':[a+cx,b+cy,c,e],'confidence':1,'manual_basis':extra['basis']})
 for i,o in enumerate(atlas['observations']):
  a,b,c,e=o['bounds']
  if not(cx<=a+c/2<cx+cw and cy<=b+e/2<cy+ch):continue
  bounds=[a-cx,b-cy,c,e]
  if i in spec.get('skip',[]):ignored.append({'index':i,'text':o['text'],'reason':'icon recognized as a text glyph; separately native SVG'});continue
  text=o['text'];corrected=CORRECTIONS.get(i)
  if corrected:text=corrected[0];bounds=corrected[1] or bounds
  text=re.sub(r'\s*[•·⋅]\s*',' · ',text)
  text=re.sub(r'(周[一二三四五六日])(?=[0-9])',r'\1 ',text)
  parent=owner(bounds)
  matched=next((id for id,v in controls.items() if i in v['ocr_ids']),None)
  if matched:parent=matched
  x,y,w,h=rect(bounds);size=h*.93
  color=INK
  if matched:
   filled=next(v[2] for v in spec['buttons'] if v[0]==matched)
   color='ffffff' if filled else (SAGE if matched not in ('conflict_slot','close') else INK)
  if i in (72,126):color='be873f'
  if i in (74,128):color='58816b'
  if text.startswith('来自') or text=='待发货':color=MUTED
  node=dict(t='text',id=f'text_{i}',text=text,x=x,y=y,w=w+3,h=h+4,size=size,weight=400,line_height=h+4,alignx=0,variant='single_line',font_src='self:resources/service/NotoSansSC-Regular.ttf',color=col(color))
  add(node,parent)
  ocr.append(dict(atlas_observation=i,source_text=o['text'],text=text,source_bounds=bounds,logical_ink_bounds=[x,y,w,h],correction=bool(corrected)))
 # Ensure KitButton bindings always refer to the true native label child.
 for id in controls:
  children=nodes[id]['c']; label=next((j for j,n in enumerate(children) if n['t']=='text'),None)
  binding={'control':[1]}
  if label is not None:binding['label']=[label]
  nodes[id]['kit']=json.dumps({'widget':'KitButton','bindings':binding},separators=(',',':'))
 def icon(kind,b,id=None,parent=None):
  id=id or kind+'_icon';x,y,w,h=rect(b);path=d/'assets'/f'{id}.svg'
  path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28" fill="none" stroke="#{SAGE}" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round">{SVG[kind]}</svg>')
  add(dict(t='svg',id=id,x=x,y=y,w=w,h=h,src=''),parent or owner(b))
  assets[id]=dict(path=f'assets/{path.name}',sha256=sha(path),method='reference_svg',reference_sha256=sha(d/'reference.png'),fit='stretch',clip=True,notes='Native vector reconstruction of the reviewed source symbol; no embedded text or raster UI')
 for i,(kind,b) in enumerate(spec.get('icons',[])):icon(kind,b,f'{kind}_icon_{i}')
 if spec.get('dock'):
  # Measure icon squares against the actual cropped frame; dock labels stay OCR Labels.
  db=spec['dock'];left,top,width,height=db
  for i,kind in enumerate(['mail','calendar','bag','wallet']):
   size=width*.156;xx=left+width*(.075+i*.235); yy=top+height*.12
   stack(f'dock_tile_{i}',[xx-7,yy-7,size+14,size+14],'dock','fcfdfb',24)
   if kind!='calendar':icon(kind,[xx+8,yy+12,size-16,size-19],f'dock_{kind}','dock')
 for i,(x,y,w,h,selected) in enumerate(spec.get('dots',[])):
  n=stack(f'step_{i}',[x,y,w,h],owner([x,y,w,h]),SAGE if selected else PANEL,80)
  n.update(ellipse=1,border=.8,bordercolor=col(SAGE if selected else 'b8c5be'))
 # Native labels paint above dock tile surfaces and decorative markers.
 for n in walk(root):
  if 'c' in n:n['c'].sort(key=lambda child: child['t']=='text')
 for id in controls:
  children=nodes[id]['c'];binding={'control':[next(j for j,n in enumerate(children) if n['t']=='button')]}
  label=next((j for j,n in enumerate(children) if n['t']=='text'),None)
  if label is not None:binding['label']=[label]
  nodes[id]['kit']=json.dumps({'widget':'KitButton','bindings':binding},separators=(',',':'))
 contract=dict(schema_version=1,id=d.name,app='service',number=number,title=state['title'],structure='Native service-owned cards reconstructed from reviewed storyboard',artboard=[406,776],font_family='Noto Sans SC',palette={'name':'Fresh','page':'#f0f5f2','panel':'#fcfdfb','ink':'#31413c','accent':'#608570'},content_source='Fictional service scenario from source/flow.json',graphics={},tree=root)
 save(d/'contract.json',contract)
 (d/'image-prompt.md').write_text((ROOT/'source/prompt.txt').read_text())
 save(d/'generation.json',dict(provider='OpenAI Image API',model='gpt-image-2',image_sha256=sha(d/'reference.png'),original_image_sha256=sha(original),atlas_sha256=sha(ROOT/'source/atlas.png'),prompt_sha256=sha(d/'image-prompt.md'),actual_dimensions=[812,1552],source_crop=state['crop'],normalization={'method':'uniform contain on 812x1552 matte','fitted_pixels':fitted,'offset_pixels':[ox,oy],'scale_xy':[sx,sy]},note='Single atlas generation; normalized parity reference is derived, not a separate generated image'))
 for n in walk(root):
  if n['t']=='text':continue
  annotations.append(dict(id=n['id'],bounds=[n[k] for k in 'xywh'],reviewed=True,**{k:n[k] for k in ('bg','radius','border','bordercolor') if k in n}))
 save(d/'annotations.json',dict(schema_version=1,reference_sha256=sha(d/'reference.png'),method='Explicit source-pixel bounds, uniformly fitted to fixed native artboard; surface tone/soft texture are declared approximations',elements=annotations))
 # Initial font placement uses true bundled glyph metrics over measured source ink.
 from observe import metrics
 mapped=copy.deepcopy(root)
 rows={f"text_{r['atlas_observation']}":r for r in ocr}
 font=ROOT/'fonts/NotoSansSC-Regular.ttf'
 for n in walk(mapped):
  if n['t']!='text':continue
  x,y,w,h=rows[n['id']]['logical_ink_bounds'];(x0,y0,x1,y1),adv,asc,desc=metrics(str(font),n['text'])
  # A generated reference may use condensed glyphs. Fit the native font in
  # both dimensions instead of forcing negative tracking and overlapping ink.
  size=min(h/(y1-y0),w/(x1-x0));ink_h=(y1-y0)*size
  n.update(x=x-x0*size,y=y+(h-ink_h)/2-2,w=adv*size+4,h=ink_h+4,size=size,tracking=0,line_height=ink_h+4,font_asc=y1+2/size-asc,font_desc=(y1*size+2-(ink_h+4))/size-desc)
 save(d/'mapped.json',dict(schema_version=1,reference_sha256=sha(d/'reference.png'),tree=mapped,changes=[{'source':'Apple Vision source atlas observations plus bundled Noto glyph metrics'}],limits=['Fixed 406x776 artboard','Native surface texture and line icon approximations recorded','Corrected OCR noise is documented separately']))
 save(d/'source-measurements.json',dict(source_sha256=sha(original),reference_sha256=sha(d/'reference.png'),text=ocr,ignored=ignored,spec=spec))
 manifest=propose(d)
 manifest.update(contract_sha256=sha(d/'contract.json'),reference_sha256=sha(d/'reference.png'))
 for e in manifest['elements']:
  if e['id'] in assets:e.update(role='photo' if nodes[e['id']]['t']=='image' else 'icon',decision='reviewed',confidence=1,basis='Visual source-region review and explicit native renderer ownership',asset=assets[e['id']])
  elif e['id'] in dict(spec.get('cards',[])):e.update(role='card',decision='reviewed',basis='Service-owned card surface with native child widgets')
 save(d/'semantic-map.json',manifest);write_brief(d,manifest)
 save(d/'service-actions.json',dict(frame_id=number,controls=controls,source=state['slug']))
 link=PIPE/d.name
 if not link.exists():link.symlink_to(d,target_is_directory=True)
 print(json.dumps({'id':d.name,'nodes':len(nodes),'controls':len(controls),'source_texts':len(ocr)},ensure_ascii=False),flush=True)

if __name__=='__main__':
 for n in [int(v) for v in sys.argv[1:]] or list(SPECS):author(n)
