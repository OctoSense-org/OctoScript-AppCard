#!/usr/bin/env python3
import json,sys
from pathlib import Path
import numpy as np
from PIL import Image
from catalogue import HERE,walk
from semantics import write,sha,write_brief
from repair_reference import crop_rect

def repair(id):
 p=HERE/id;s=json.load(open(p/'semantic-map.json'));m=json.load(open(p/'mapped.json'));nodes={n['id']:n for n in walk(m['tree'])};im=Image.open(p/'reference.png')
 for e in s['elements']:
  if e['role'] not in ('chart.line','chart.area'):continue
  n=nodes[e['id']];b=[n[k] for k in ('x','y','w','h')];crop,_,_=crop_rect(im,b);a=np.asarray(crop).astype(float);R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
  if id=='stock-08':masks=[(R>100)&(R<195)&(R-G>40)&(G-B>15),(R>215)&(R-G>24)&(G-B>17)&(G<225)];colors=['#a24723','#efbe9e']
  elif id=='stock-05':masks=[(G-R>7)&(G-B>20)&(R<155)];colors=['#506333']
  elif id=='stock-01':masks=[(G-R>6)&(G-B>4)&(R<145)];colors=['#35664e']
  elif id=='stock-04':masks=[(R-G>75)&(G-B>25)&(G<150)&(R>135)];colors=['#c74714']
  else:masks=[(B-R>80)&(B-G>40)&(R<160)];colors=['#155fee']
  # Exclude all measured native text regions before digitizing a curve.
  for row in json.load(open(p/'observations.json'))['text']:
   if row.get('status')!='observed':continue
   tx,ty,tw,th=row['ink_bounds'];sx,sy=im.width/406,im.height/776
   left=max(0,round((tx-b[0]-1)*sx));right=min(crop.width,round((tx+tw-b[0]+1)*sx))
   top=max(0,round((ty-b[1]-1)*sy));bottom=min(crop.height,round((ty+th-b[1]+1)*sy))
   if right>left and bottom>top:
    for mask in masks:mask[top:bottom,left:right]=False
  series=[]
  for mask in masks:
   xs=[];ys=[]
   for x in range(crop.width):
    hits=np.where(mask[:,x])[0]
    if len(hits):xs.append(x);ys.append(np.median(hits))
   if len(xs)<crop.width*.65:raise ValueError(f'{id}: incomplete measured line ({len(xs)}/{crop.width})')
   series.append((np.array(xs)/(crop.width-1),1-np.array(ys)/(crop.height-1)))
  lo=max(x[0] for x,y in series);hi=min(x[-1] for x,y in series);xs=np.linspace(lo,hi,round((hi-lo)*crop.width))
  rows=[{'x':round(float(x),6),**{f'y{i}':round(float(np.interp(x,xx,yy)),6) for i,(xx,yy) in enumerate(series)}} for x in xs]
  path=p/e['data']['path'];write(path,rows);e['data']['sha256']=sha(path)
  e['plot']['colors']=colors;e['plot']['line_width']=1.05 if id=='stock-03' else 1.3
  if id in ('stock-05','stock-08'):
   for line in e['plot']['horizontal']:line.update(dotted=True,color='#cbbcaf',width=.5)
  if id=='weather-03':
   e['plot']['line_width']=2.25;e['plot'].pop('vertical',None);e['plot']['guides']=[]
   for marker in e['plot']['markers']:
    marker['y']=float(np.interp(marker['x'],series[0][0],series[0][1]))
    if marker['color']!='#ffffff':marker.update(color=colors[0],radius=3.25)
   for mx in [64,157,254,346]:
    xx=(mx-b[0])/b[2];yy=float(np.interp(xx,series[0][0],series[0][1]));e['plot']['guides'].append({'x':xx,'y0':0,'y1':yy,'color':'#c6d4e8','width':.7})
  if id=='stock-01':e['plot']['markers']=[{'x':rows[-1]['x'],'y':rows[-1]['y0'],'color':colors[0],'radius':2.8}]
 for e in s['elements']:
  if e['role']=='chart.donut':e['plot'].update(slice_gap=2.0,show_center_label=False)
 write(p/'semantic-map.json',s);write_brief(p,s);print(id,flush=True)
if __name__=='__main__':
 for id in sys.argv[1:]:repair(id)
