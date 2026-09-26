#!/usr/bin/env python3
"""Reproducible measured school atlas mapping. Never generates images or approves captures."""
from pathlib import Path
import copy, hashlib, json, sys, shutil
ROOT=Path(__file__).resolve().parents[1]
PIPE=ROOT.parents[1]/'flows'
sys.path[:0]=[str(PIPE/'image-to-card'),str(PIPE/'image-lib')]
from atlas import intake
from prepare import prepare
from catalogue import walk
from semantics import propose, write_brief, preflight
from observe import metrics
import compile as compiler
compiler.GALLERY=ROOT/'artwork'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):Path(p).parent.mkdir(parents=True,exist_ok=True);Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def col(v):return int('ff'+v.lstrip('#'),16)
INK='33413c';MUTED='768079';SAGE='477d64';PANEL='fcfdfc'
SVG={
'back':'<path d="m18 3-11 11 11 11"/>',
'chevron':'<path d="m10 5 8 9-8 9"/>',
'mail':'<rect x="3" y="6" width="22" height="17" rx="2"/><path d="m3 7 11 9L25 7"/>',
'calendar':'<rect x="4" y="5" width="20" height="21" rx="2"/><path d="M4 11h20M9 2v6m10-6v6M8 16h2m3 0h2m3 0h2m-12 5h2m3 0h2"/>',
'wallet':'<rect x="2" y="5" width="24" height="19" rx="3"/><path d="M2 11h24m-8 5h7m-4 4h1"/>',
'clock':'<circle cx="14" cy="14" r="11"/><path d="M14 7v7l5 3"/>',
'pin':'<path d="M14 26S4 17 4 11a10 10 0 0 1 20 0c0 6-10 15-10 15Z"/><circle cx="14" cy="11" r="3"/>',
'check':'<circle cx="14" cy="14" r="13" fill="#477d64" stroke="none"/><path d="m7 14 5 5 9-10" stroke="white" stroke-width="2"/>',
'close':'<circle cx="14" cy="14" r="12" fill="#cd655e" stroke="none"/><path d="m9 9 10 10m0-10L9 19" stroke="white" stroke-width="2"/>',
'search':'<circle cx="11" cy="11" r="8"/><path d="m17 17 8 8"/>',
'compose':'<path d="M20 13v12H3V8h11m0 7 11-12 2 3-11 12-5 2z"/>',
'receipt':'<path d="M6 2h12l5 5v19H6zM17 2v7h6M10 13h9m-9 5h9m-9 4h5"/>',
'status':'<path d="M2 17v4m4-8v8m4-12v12m4-16v16M19 10q6-6 12 0m-9 3q3-3 6 0m-4 3h2M36 8h15v11H36zm17 3v5"/>',
}
# Each record is a directly reviewed source-frame rectangle; widths are not guessed from the prompt grid.
SPECS={
1:dict(cards=[],buttons=[('open_mail',[9,148,186,79],False,[8,9,10]),('dock_mail',[12,476,45,50],False,[16]),('dock_calendar',[80,476,45,50],False,[17]),('dock_payment',[147,476,45,50],False,[18])],plain=['open_mail','dock_mail','dock_calendar','dock_payment'],icons=[('search',[20,112,12,12]),('mail',[24,483,20,17]),('calendar',[93,483,18,18]),('wallet',[162,483,19,17]),('chevron',[185,182,8,12]),('chevron',[185,267,8,12])],lines=[[12,311,180,1],[12,471,180,1]],skip=[4,14]),
2:dict(cards=[('calendar_card',[14,239,180,118]),('payment_card',[14,363,180,105])],buttons=[('back_inbox',[10,31,62,22],False,[60]),('view_calendar',[21,325,164,24],False,[73]),('view_payment',[21,437,164,23],False,[77]),('show_desktop',[13,480,181,32],False,[78])],plain=['back_inbox'],icons=[('back',[10,35,9,14]),('calendar',[24,248,23,23]),('wallet',[23,373,23,20]),('check',[23,151,12,12])],skip=[59],avatar=[14,94,32,33],badge=[14,147,104,20]),
3:dict(cards=[('calendar_card',[9,77,185,176]),('payment_card',[9,264,185,176])],buttons=[('ack_calendar',[21,210,75,32],True,[126]),('undo_calendar',[106,210,77,32],False,[127]),('view_payment',[21,395,162,31],False,[132])],icons=[('calendar',[23,89,23,23]),('wallet',[23,278,23,20])],dock=[2,465,199,66]),
4:dict(cards=[('calendar_card',[9,78,185,157]),('payment_card',[9,247,185,190])],buttons=[('restore_calendar',[21,189,161,32],False,[177]),('view_payment',[21,394,161,32],False,[182])],icons=[('calendar',[22,89,23,23]),('close',[53,95,14,14]),('wallet',[23,262,24,22])],dock=[2,465,199,66]),
5:dict(cards=[('calendar_card',[9,77,185,159]),('payment_card',[9,248,185,179])],buttons=[('view_calendar',[20,192,80,31],False,[26]),('undo_calendar',[109,192,75,31],False,[27]),('view_payment',[21,385,162,32],False,[32])],icons=[('calendar',[23,89,22,23]),('check',[52,93,14,14]),('wallet',[22,263,24,21])],dock=[2,450,199,65],skip=[34]),
6:dict(cards=[('calendar_detail',[14,100,180,277])],buttons=[('show_desktop',[9,31,49,23],False,[]),('undo_calendar',[15,387,80,32],False,[93]),('return_mail',[104,387,88,32],False,[94])],plain=['show_desktop'],icons=[('back',[11,36,9,14]),('clock',[26,237,14,14]),('pin',[26,260,14,14]),('calendar',[25,287,15,15]),('mail',[25,314,15,13]),('check',[64,345,16,16])],badge=[52,340,106,25],date_tile=[66,111,75,80],dock=[2,453,199,62],skip=[87,89,96,98]),
7:dict(cards=[('payment_detail',[10,100,184,333])],buttons=[('show_desktop',[9,31,49,23],False,[139]),('pay_fee',[21,347,162,34],True,[148]),('cancel_payment',[19,391,72,31],False,[149]),('return_mail',[99,391,86,31],False,[150])],plain=['show_desktop'],icons=[('back',[10,37,9,14]),('wallet',[24,114,32,28]),('calendar',[24,247,14,14]),('clock',[24,271,14,14]),('mail',[24,315,14,13])],lines=[[24,302,159,1]],dock=[2,453,199,62],skip=[138]),
8:dict(cards=[('calendar_card',[9,78,185,164]),('payment_card',[9,255,185,168])],buttons=[('view_calendar',[21,198,161,32],False,[194]),('reopen_payment',[21,376,161,34],False,[198])],icons=[('calendar',[23,91,23,23]),('wallet',[23,272,27,22]),('close',[61,276,14,14])],dock=[2,451,199,64]),
9:dict(cards=[('payment_detail',[10,98,184,329])],buttons=[('show_desktop',[9,31,49,23],False,[40]),('pay_fee',[20,336,163,35],True,[51]),('cancel_payment',[20,382,163,33],False,[52])],plain=['show_desktop'],icons=[('back',[11,35,9,14]),('wallet',[23,112,31,27]),('calendar',[24,239,14,14]),('clock',[24,263,14,14]),('mail',[24,304,14,13])],lines=[[23,292,160,1]],dock=[2,468,199,62],skip=[41,48,54,56]),
10:dict(cards=[('calendar_card',[9,78,185,151]),('payment_card',[9,243,185,178])],buttons=[('view_calendar',[21,190,161,29],False,[107]),('view_receipt',[21,377,161,32],False,[113])],icons=[('calendar',[23,90,23,23]),('check',[22,255,26,26])],dock=[2,465,199,65],skip=[108,115]),
11:dict(cards=[('payment_receipt',[9,99,185,349])],buttons=[('show_desktop',[9,31,49,23],False,[]),('view_calendar',[19,366,168,29],False,[163]),('return_mail',[19,405,168,33],False,[164])],plain=['show_desktop'],icons=[('back',[10,35,9,14]),('check',[80,112,45,44]),('clock',[23,297,14,14]),('receipt',[23,325,14,14])],dock=[2,466,199,64],skip=[166,168]),
12:dict(cards=[('calendar_card',[14,207,180,109]),('payment_card',[14,322,180,90])],buttons=[('back_inbox',[10,31,62,22],False,[205]),('view_calendar',[22,285,162,23],False,[216]),('view_receipt',[22,380,162,24],False,[219]),('show_desktop',[14,458,180,33],False,[221])],plain=['back_inbox'],icons=[('back',[10,35,9,14]),('calendar',[22,214,23,23]),('check',[22,330,22,22]),('check',[49,426,14,14])],avatar=[14,92,32,32],badge=[33,421,141,25],skip=[204]),
}
# Explicit UX correction requested after source review: desktop payment cards
# offer direct Pay/Cancel and a separate invoice link. Original atlas is retained.
for frame,card_bottom,row_y,link_y,obs in [(3,462,391,432,132),(4,456,394,434,182),(5,449,385,425,32)]:
 spec=SPECS[frame]
 for id,b in spec['cards']:
  if id=='payment_card':b[3]=card_bottom-b[1]
 spec['buttons']=[v for v in spec['buttons']if v[0]!='view_payment']
 spec['buttons'] += [('pay_fee',[21,row_y,108,32],True,[]),('cancel_payment',[136,row_y,47,32],False,[]),('view_payment',[21,link_y-3,162,22],False,[obs])]
 spec.setdefault('plain',[]).append('view_payment')
 spec['ux_correction']={'reason':'Desktop payment card must expose explicit Pay and Cancel, independent of calendar; retain invoice link','reference_unchanged':True,'new_native_controls':['pay_fee','cancel_payment'],'label_bounds':{'pay_fee':[43,row_y+9,65,15],'cancel_payment':[146,row_y+9,27,15]},'invoice_label':[77,link_y,51,15]}
# Corrected source copy and compact English preserve the known fixture, not OCR artifacts.
COPY={}
def entries(s):
 for line in s.strip().splitlines():
  index,cn,en=line.split('|');COPY[int(index)]={'cn':cn,'en':en}
entries('''
2|9月24日 周四|Thu, Sep 24
3|09:41|09:41
5|邮箱|Mail
6|收件箱|Inbox
7|搜索邮件|Search mail
8|林老师|Teacher Lin
9|秋季科学日安排|Science Day
10|明天下午，一起探索科学|Explore science tomorrow
11|校务处|School office
12|九月校园简报|September news
13|新学期 · 共建美好校园|A new term together
15|昨天|Yesterday
16|邮件|Mail
17|日历|Calendar
18|支付|Pay
20|9月24日 周四|Thu, Sep 24
21|09:45|09:45
22|日历 · 已重新加入|Calendar · Restored
23|秋季科学日|Science Day
24|9月25日 14:00–16:00|Sep 25, 14:00–16:00
25|北辰小学 · 科学教室|Beichen · Science room
26|查看日程|View event
27|撤销日程|Undo event
28|支付 · 待确认|Payment · Pending
29|学校活动材料费|School materials
30|¥120|¥120
31|收款方：北辰小学|To: Beichen Primary
32|查看费用|View fee
33|邮件|Mail
35|日历|Calendar
36|支付|Pay
39|9月24日 周四 09:48|Thu, Sep 24 · 09:48
40|桌面|Desktop
42|支付|Payment
43|待付款 · 已重新打开|Unpaid · Reopened
44|¥120|¥120
45|学校活动材料费|School materials
46|收款方：北辰小学|To: Beichen Primary
47|活动：秋季科学日|Event: Science Day
49|9月25日 14:00–16:00|Sep 25, 14:00–16:00
50|来自林老师邮件|From Teacher Lin
51|支付 ¥120|Pay ¥120
52|撤销|Cancel
53|邮件|Mail
55|日历|Calendar
57|支付|Pay
60|收件箱|Inbox
61|秋季科学日安排|Science Day plans
62|林老师|Teacher Lin
63|9月24日 09:41|Sep 24, 09:41
64|收件人：Alex|To: Alex
65|已授权同步日历|Calendar access allowed
66|家长您好，秋季科学日将于9月25日|Dear parent, Science Day is Sep 25
67|14:00–16:00 在科学教室举行|14:00–16:00 in the Science Room
68|活动材料费为 ¥120，请确认缴费|Materials cost ¥120; please pay
69|日历 · 已更新|Calendar · Updated
70|秋季科学日|Science Day
71|9月25日 14:00–16:00|Sep 25, 14:00–16:00
72|北辰小学 · 科学教室|Beichen · Science room
73|查看日程|View event
74|支付 · 待确认|Payment · Pending
75|活动材料费|Materials fee
76|¥120|¥120
77|查看费用|View fee
78|返回桌面|Desktop
80|9月24日 周四 09:46|Thu, Sep 24 · 09:46
81|日历|Calendar
82|9月|Sep
83|25|25
84|周五|Fri
85|秋季科学日|Science Day
86|14:00–16:00|14:00–16:00
88|北辰小学 · 科学教室|Beichen · Science room
90|家庭日历|Family calendar
91|来自林老师邮件|From Teacher Lin
92|已加入日历|Added to calendar
93|撤销日程|Undo event
94|查看原邮件|Source mail
95|邮件|Mail
97|日历|Calendar
99|支付|Pay
101|9月24日 周四|Thu, Sep 24
102|09:50|09:50
103|日历 · 已更新|Calendar · Updated
104|秋季科学日|Science Day
105|9月25日 14:00–16:00|Sep 25, 14:00–16:00
106|北辰小学 · 科学教室|Beichen · Science room
107|查看日程|View event
109|支付 · 已完成|Payment · Paid
110|学校活动材料费|School materials
111|¥120 已支付|¥120 Paid
112|收款方：北辰小学|To: Beichen Primary
113|查看凭证|Receipt
114|邮件|Mail
116|日历|Calendar
117|支付|Pay
119|9月24日 周四|Thu, Sep 24
120|09:43|09:43
121|日历 · 已更新|Calendar · Updated
122|秋季科学日|Science Day
123|9月25日 14:00–16:00|Sep 25, 14:00–16:00
124|北辰小学 · 科学教室|Beichen · Science room
125|来自林老师邮件|From Teacher Lin
126|确认|Confirm
127|撤销日程|Undo event
128|支付 · 待确认|Payment · Pending
129|学校活动材料费|School materials
130|¥120|¥120
131|收款方：北辰小学|To: Beichen Primary
132|查看费用|View fee
133|邮件|Mail
134|日历|Calendar
135|支付|Pay
137|9月24日 周四 09:46|Thu, Sep 24 · 09:46
139|桌面|Desktop
140|支付|Payment
141|待付款|Unpaid
142|¥120|¥120
143|学校活动材料费|School materials
144|收款方：北辰小学|To: Beichen Primary
145|活动：秋季科学日|Event: Science Day
146|9月25日 14:00–16:00|Sep 25, 14:00–16:00
147|来自林老师邮件|From Teacher Lin
148|支付 ¥120|Pay ¥120
149|撤销|Cancel
150|查看原邮件|Source mail
151|邮件|Mail
152|日历|Calendar
153|支付|Pay
155|9月24日 周四 09:50|Thu, Sep 24 · 09:50
156|支付凭证|Receipt
157|已支付|Paid
158|¥120|¥120
159|学校活动材料费|School materials
160|收款方：北辰小学|To: Beichen Primary
161|支付时间：9月24日 09:50|Paid: Sep 24, 09:50
162|凭证号：SC-120-0924|Receipt: SC-120-0924
163|查看日程|View event
164|返回邮件|Back to mail
165|邮件|Mail
167|日历|Calendar
169|支付|Pay
171|9月24日|Sep 24
172|周四|Thu
173|09:44|09:44
174|日历 · 已撤销|Calendar · Undone
175|仅移除家庭日历记录|Family event removed
176|学校活动仍然有效|School event unchanged
177|重新加入|Restore
178|支付 · 待确认|Payment · Pending
179|学校活动材料费|School materials
180|¥120|¥120
181|收款方：北辰小学|To: Beichen Primary
182|查看费用|View fee
183|邮件|Mail
184|日历|Calendar
185|支付|Pay
187|9月24日|Sep 24
188|周四|Thu
189|09:47|09:47
190|日历 · 已更新|Calendar · Updated
191|秋季科学日|Science Day
192|9月25日 14:00–16:00|Sep 25, 14:00–16:00
193|北辰小学 · 科学教室|Beichen · Science room
194|查看日程|View event
195|支付 · 请求已撤销|Payment · Cancelled
196|尚未扣款|No charge made
197|日历安排不受影响|Calendar unchanged
198|重新打开|Reopen
199|邮件|Mail
200|日历|Calendar
201|支付|Pay
203|9月24日 周四 09:52|Thu, Sep 24 · 09:52
205|收件箱|Inbox
206|秋季科学日安排|Science Day plans
207|林老师|Teacher Lin
208|收件人：Alex|To: Alex
209|家长您好，秋季科学日将于9月25日|Dear parent, Science Day is Sep 25
210|14:00–16:00 在科学教室举行|14:00–16:00 in the Science Room
211|活动材料费为 ¥120，请确认缴费|Materials cost ¥120; please pay
212|日历 · 已更新|Calendar · Updated
213|秋季科学日|Science Day
214|9月25日 14:00–16:00|Sep 25, 14:00–16:00
215|北辰小学 · 科学教室|Beichen · Science room
216|查看日程|View event
217|支付 · 已完成|Payment · Paid
218|¥120 已支付|¥120 Paid
219|查看凭证|Receipt
220|日程与缴费已安排|Event and fee arranged
221|返回桌面|Desktop
''')
# Bounds corrections remove OCR's mistaken icon-prefix and recover source labels.
BOUNDS={7:[39,111,69,13],8:[28,158,61,17],11:[28,241,50,17],22:[72,95,110,13],40:[25,35,35,13],47:[48,240,119,14],60:[27,35,41,13],65:[41,151,81,12],66:[14,178,178,13],67:[14,196,177,13],68:[14,215,177,13],86:[49,237,99,14],92:[89,345,61,14],145:[48,247,128,14],146:[48,271,136,14],161:[47,297,138,14],162:[47,325,132,14],174:[74,97,111,13],195:[83,276,104,15],203:[11,9,94,11],205:[27,34,43,13],209:[14,149,178,13],210:[14,168,177,13],211:[14,186,177,13],220:[72,427,109,13]}
for frame,obs in [(3,132),(4,182),(5,32)]:BOUNDS[obs]=SPECS[frame]['ux_correction']['invoice_label']
DOCK_OBS={3:[133,134,135],4:[183,184,185],5:[33,35,36],6:[95,97,99],7:[151,152,153],8:[199,200,201],9:[53,55,57],10:[114,116,117],11:[165,167,169]}
TITLES=['收件箱','邮件里的可行动卡片','日历已更新','撤销日历','重新加入日历','日历应用','缴费详情','撤销缴费请求','重新打开缴费','支付完成','支付凭证','已处理的邮件']

def manifest():
 crops=json.loads((ROOT/'source/measured-crops.json').read_text())['crops']
 scenes=[dict(id=str(n),design_id=f'school-{n:02d}',directory=f'cards/school-{n:02d}',crop=crops[n-1],surface='desktop' if n in (3,4,5,8,10) else 'app',title=TITLES[n-1])for n in range(1,13)]
 cards=[dict(id=f'school-{owner}-{n:02d}',scene=str(n),root=owner+'_card',owner=owner)for n in (2,3,4,5,8,10,12)for owner in ('calendar','payment')]
 return dict(schema_version=1,id='school',artboard=[406,776],locales=['en','cn'],generation=dict(atlas='source/atlas.png',prompt='source/prompt.txt',provider='OpenAI built-in image_gen',requested_size=[2400,3456],quality='high'),scenes=scenes,cards=cards,artwork=dict(source_prefix='http://127.0.0.1:8170/ux-images/',root='artwork'),outputs=dict(intake='pipeline-output/intake',cards='pipeline-output/service-cards',bundle='wizard/card-bundle',runs='pipeline-output/runs'),browser_modules=['wizard/service.mjs','wizard/copy.mjs'],checks={'service-test':[{'argv':['{node}','--test','wizard/service.test.mjs'],'cwd':'.'}]})

def author(n,scene):
 d=ROOT/scene['directory']
 if (d/'latest.json').exists() or (d/'rounds').exists():raise ValueError('Retain captured native mappings; authoring cannot overwrite Studio history')
 (d/'assets').mkdir(exist_ok=True)
 spec=copy.deepcopy(SPECS[n]);cx,cy,cw,ch=scene['crop'];refhash=sha(d/'reference.png')
 tr=json.loads((d/'atlas-provenance.json').read_text())['transform'];scale=tr['uniform_scale']/2;ox,oy=[x/2 for x in tr['offset_pixels']]
 def rect(b):return [ox+b[0]*scale,oy+b[1]*scale,b[2]*scale,b[3]*scale]
 root=dict(t='stack',id='page',x=0,y=0,w=406,h=776,variant='surface',bg=col('f0f5f2'),c=[])
 nodes={'page':root};assets={};controls={};textcopy={};measure=[]
 def add(v,parent='screen'):nodes[parent].setdefault('c',[]).append(v);nodes[v['id']]=v;return v
 def stack(id,b,parent='screen',bg=None,radius=0):
  v=dict(t='stack',id=id,**dict(zip('xywh',rect(b))),c=[])
  if bg:v.update(variant='surface',bg=col(bg),radius=radius*scale)
  return add(v,parent)
 def owner(b):
  x,y,w,h=b;possible=[(a[2]*a[3],id)for id,a in spec.get('cards',[])if a[0]<=x+w/2<=a[0]+a[2]and a[1]<=y+h/2<=a[1]+a[3]]
  return min(possible)[1]if possible else 'screen'
 stack('screen',[0,0,cw,ch],'page','eef5f2' if scene['surface']=='desktop'else'fcfdfc')
 if scene['surface']=='desktop':
  # Native low-contrast wallpaper planes approximate the source tint; no raster wallpaper.
  stack('wallpaper_lower',[0,ch*.55,cw,ch*.45],bg='e8f3f5')
 for id,b in spec.get('cards',[]):
  node=stack(id,b,bg=PANEL,radius=10);node.update(border=.4,bordercolor=col('e2e8e3'))
 if spec.get('badge'):stack('status_badge',spec['badge'],owner(spec['badge']),'e5f1e9',5)
 if spec.get('date_tile'):stack('date_tile',spec['date_tile'],'calendar_detail','eef7ff',7)
 if spec.get('avatar'):stack('teacher_avatar',spec['avatar'],bg='8da9cf',radius=16)
 for i,b in enumerate(spec.get('lines',[])):stack(f'divider_{i}',b,owner(b),'e3e7e4')
 if n==1:
  stack('search_field',[12,103,182,30],bg='eff2f3',radius=10)
  stack('unread_dot',[12,165,7,7],bg=SAGE,radius=4)
  stack('newsletter_dot',[12,249,7,7],bg='c6ccca',radius=4)
 if spec.get('dock'):
  db=spec['dock'];stack('dock',db,bg='f5faf8',radius=16)
  for i,(action,obs)in enumerate(zip(('dock_mail','dock_calendar','dock_payment'),DOCK_OBS[n])):
   b=[14+i*67,db[1]+4,42,db[3]-6];spec['buttons'].append((action,b,False,[obs]));spec.setdefault('plain',[]).append(action)
   stack(action+'_tile',[16+i*67,db[1]+6,37,34],'dock','fcfdfc',8)
   spec.setdefault('icons',[]).append((['mail','calendar','wallet'][i],[25+i*67,db[1]+14,18,18]))
 for id,b,filled,obs in spec['buttons']:
  parent=owner(b);stack(id,b,parent)
  surface=stack(id+'_surface',b,id,None if id in spec.get('plain',[])else SAGE if filled else 'f9fcf9',4)
  if id not in spec.get('plain',[]) and not filled:surface.update(border=.7,bordercolor=col('a8bfb1'))
  add(dict(t='button',id=id+'_control',**dict(zip('xywh',rect(b))),enabled=1),id)
  controls[id]=dict(event=id,text_ids=[f'copy_{i}'for i in obs],ocr_ids=obs,source_bounds=b,enabled=True)
 def icon(kind,b,i,parent=None):
  id=f'{kind}_icon_{i}';path=d/'assets'/f'{id}.svg';viewbox='0 0 56 28'if kind=='status'else'0 0 28 28'
  color='34403b'if kind=='status'else'747d79'if(kind,b)in spec.get('icons',[])[-3:]and spec.get('dock')else SAGE
  path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" fill="none" stroke="#{color}" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round">{SVG[kind]}</svg>')
  add(dict(t='svg',id=id,**dict(zip('xywh',rect(b))),src=''),parent or owner(b))
  assets[id]=dict(path=f'assets/{path.name}',sha256=sha(path),method='reference_svg',reference_sha256=refhash,fit='stretch',clip=True,notes='Visually measured source icon reconstructed as vector paths; no text or embedded raster')
 for i,(kind,b)in enumerate(spec.get('icons',[])):icon(kind,b,i)
 if scene['surface']=='app':icon('status',[145,6,49,13],99)
 atlas=json.loads((ROOT/'source/atlas.ocr.json').read_text());font=str(ROOT/'fonts/NotoSansSC-Regular.ttf')
 def label(id,pair,b,parent=None,observation=None):
  x,y,w,h=rect(b);parent=parent or owner(b);cn=pair['cn'];textcopy[id]=pair
  ink,adv,asc,desc=metrics(font,cn);x0,y0,x1,y1=ink
  size=min(h/max(.1,y1-y0),w/max(.1,x1-x0));size*=.91;inkh=(y1-y0)*size
  tint=MUTED if cn.startswith(('来自','收款方','9月24'))else INK
  matched=next((k for k,v in controls.items()if id in v['text_ids']),None)
  if matched:
   parent=matched;filled=next(v[2]for v in spec['buttons']if v[0]==matched)
   tint='ffffff'if filled else SAGE
  if '待确认'in cn or cn.startswith('待付款'):tint='c38b52'
  if '已撤销'in cn or'请求已撤销'in cn:tint='c6655d'
  if'已更新'in cn or'已完成'in cn or'已重新'in cn:tint=SAGE
  # Preserve measured ink position. Available width follows source slot for translated copy.
  logical_w=max(adv*size+4,w+3)
  node=dict(t='text',id=id,text=cn,x=x-x0*size,y=y+(h-inkh)/2-2,w=logical_w,h=inkh+4,size=size,weight=400,tracking=0,line_height=inkh+4,alignx=0,variant='single_line',font_src='self:resources/service/NotoSansSC-Regular.ttf',color=col(tint),font_asc=y1+2/size-asc,font_desc=(y1*size+2-(inkh+4))/size-desc)
  add(node,parent);measure.append(dict(id=id,atlas_observation=observation,source_bounds=b,logical_ink_bounds=[x,y,w,h],copy=pair,method='Apple Vision observation and visual correction of generation/OCR artifacts; fitted bundled Noto glyph metrics'))
 for i,o in enumerate(atlas['observations']):
  a,b,w,h=o['bounds']
  if not(cx<=a+w/2<cx+cw and cy<=b+h/2<cy+ch)or i in spec.get('skip',[]):continue
  if i not in COPY:raise ValueError(f'Unreviewed source copy {n}:{i}:{o["text"]}')
  label(f'copy_{i}',COPY[i],BOUNDS.get(i,[a-cx,b-cy,w,h]),observation=i)
 if spec.get('ux_correction'):
  for action,pair in [('pay_fee',dict(cn='支付 ¥120',en='Pay ¥120')),('cancel_payment',dict(cn='撤销',en='Cancel'))]:
   tid=action+'_label';controls[action]['text_ids']=[tid];label(tid,pair,spec['ux_correction']['label_bounds'][action],action)
 if spec.get('avatar'):label('teacher_initial',dict(cn='林',en='L'),[spec['avatar'][0]+9,spec['avatar'][1]+7,15,20],'screen')
 if n in(6,11):
  label('desktop_label',dict(cn='桌面',en='Desktop'),[27,36,31,13],'show_desktop');controls['show_desktop']['text_ids']=['desktop_label']
 if n==12:label('mail_date',dict(cn='9月24日 09:41',en='Sep 24, 09:41'),[54,110,80,12])
 # Raise all native label layers above surfaces, then bind actual child indexes.
 for node in walk(root):
  if'c'in node:node['c'].sort(key=lambda v:v['t']=='text')
 for id in controls:
  children=nodes[id]['c'];bindings={'control':[next(i for i,v in enumerate(children)if v['t']=='button')]};labels=[i for i,v in enumerate(children)if v['t']=='text']
  if labels:bindings['label']=[labels[0]]
  nodes[id]['kit']=json.dumps(dict(widget='KitButton',bindings=bindings),separators=(',',':'))
 contract=dict(schema_version=1,id=scene['design_id'],app='service',number=n,title=scene['title'],artboard=[406,776],font_family='Noto Sans SC',structure='Measured native school service flow',content_source='Fictional teacher email fixture; calendar-only authorization and explicit payment',palette=dict(name='Fresh',page='#f0f5f2',panel='#fcfdfc',ink='#33413c',accent='#477d64'),graphics={},tree=root)
 save(d/'contract.json',contract);save(d/'mapped.json',dict(schema_version=1,reference_sha256=refhash,tree=copy.deepcopy(root),changes=[dict(source='Measured immutable 907×1733 atlas, reviewed OCR and source-pixel controls')],limits=['Draft original resolution 907×1733, requested 2400×3456; model not exposed','Uniform contain; native card tint/vector approximations','No Studio capture or visual approval yet']))
 if (d/'semantic-map.json').exists():(d/'semantic-map.json').unlink()
 semantic=propose(d);semantic.update(contract_sha256=sha(d/'contract.json'),reference_sha256=refhash)
 for entry in semantic['elements']:
  if entry['id']in assets:entry.update(role='icon',decision='reviewed',confidence=1,basis='Source icon inspected; native SVG paths without raster or text',asset=assets[entry['id']])
  elif entry['id']in dict(spec.get('cards',[])):entry.update(role='card',decision='reviewed',basis='Explicit independently owned service surface, native Label/Button children')
 save(d/'semantic-map.json',semantic);write_brief(d,semantic)
 save(d/'service-actions.json',dict(frame_id=n,source=scene['design_id'],controls=controls))
 save(d/'source-measurements.json',dict(atlas_sha256=sha(ROOT/'source/atlas.png'),reference_sha256=refhash,source_crop=scene['crop'],transform=tr,reviewed_source=True,text=measure,spec=spec,limits=['Source generation and OCR artifacts corrected against exact fixture','Review is source-region measurement, not native visual acceptance']))
 report=preflight(d)
 if report.get('errors')or report.get('status')=='fail':raise ValueError(report)
 result=compiler.compile_page(d)
 print(json.dumps(dict(scene=n,labels=len(textcopy),controls=len(controls),compiled=result),ensure_ascii=False),flush=True)
 return dict(text=textcopy,controls=controls,surface=scene['surface'])

if __name__=='__main__':
 doc=manifest();path=ROOT/'image-to-appcard-flow.json'
 if path.exists()and json.loads(path.read_text())!=doc:raise ValueError('Manifest changed; preserve old intake and choose new run')
 save(path,doc)
 intake(path,ROOT,ROOT/'pipeline-output/intake')
 if not(ROOT/'cards/school-01').exists():prepare(path,ROOT,ROOT/'pipeline-output/intake')
 bundle={str(i):author(i,s)for i,s in enumerate(doc['scenes'],1)}
 (ROOT/'wizard/copy.mjs').write_text('export const frames = '+json.dumps(bundle,ensure_ascii=False,separators=(',',':'))+';\n')
 save(ROOT/'source/native-measurement-summary.json',dict(frames=12,atlas_dimensions=[907,1733],requested_size=[2400,3456],native_only=True,labels=sum(len(v['text'])for v in bundle.values()),controls=sum(len(v['controls'])for v in bundle.values()),capture='pending parent serial Studio capture',visual_gate='not run'))
