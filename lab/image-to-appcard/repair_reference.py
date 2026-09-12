#!/usr/bin/env python3
"""Reviewed reference repairs, preserved separately from the image authoring brief.

UI text/controls stay native. Charts consume approximate numeric measurements.
Only isolated artwork is vectorized or cropped. Original inputs remain immutable.
"""
import copy,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'.deps'))
import cv2
import numpy as np
from PIL import Image
from catalogue import HERE,walk
from semantics import POLICY,sha,write,classify,write_brief,preflight
from observe import observe,ink_box
from fit_reference_fonts import fit

ART={
'weather-01':{'weather_symbol':[249,186,111,103]},
'weather-02':{'weather_symbol':[277,143,103,114]},
'weather-04':{'weather_symbol':[65,286,132,108]},
'weather-05':{'weather_symbol':[279,240,107,79]},
'weather-06':{'weather_symbol':[268,240,88,76]},
'weather-07':{'rain_radar':[47,165,312,314]},
'weather-08':{'weather_symbol':[39,160,77,53]},
'weather-10':{'weather_symbol':[256,216,106,111]},
'news-01':{'lead_art':[39,128,328,188]},
'news-03':{'lead_art':[38,126,330,208]},
'news-08':{'lead_art':[41,138,324,186]},
'news-04':{'topic_art_0':[129,146,55,57],'topic_art_1':[313,147,50,56],
           'topic_art_2':[129,347,54,56],'topic_art_3':[310,347,59,58],
           'latest_art':[260,587,111,112]},
}
PLOTS={
 'weather-03':{'temperature_chart':([31,341,344,175],['#1e63ee'],['#6ea0ef70'])},
 'stock-01':{'portfolio_chart':([41,270,321,167],['#3d7d58'],['#98b99380'])},
 'stock-03':{f'chart_{i}':(b,['#527fac'],[]) for i,b in enumerate([[39,230,139,90],[224,228,141,88],[39,506,139,77],[222,514,143,70]])},
 'stock-04':{'price_chart':([35,307,337,200],['#c84410'],['#f0b67c65'])},
 'stock-05':{'market_chart':([66,336,300,204],['#657849'],[])},
 'stock-08':{'comparison_chart':([66,379,301,179],['#a55b32','#d5a777'],[])},
}

def argb(c):return 0xff000000|sum(int(v)<<(16-i*8) for i,v in enumerate(c))
def hexcolor(c):return '#'+''.join(f'{int(v):02x}' for v in c)
def rect(n):return [n[k] for k in ('x','y','w','h')]

def crop_rect(im,b):
 sx,sy=im.width/406,im.height/776
 x,y,w,h=b;left,top,right,bottom=round(x*sx),round(y*sy),round((x+w)*sx),round((y+h)*sy)
 return im.crop((left,top,right,bottom)),[left,top,right-left,bottom-top],[left/sx,top/sy,(right-left)/sx,(bottom-top)/sx]

def vectorize(im,monochrome=False):
 """Trace a bounded flat illustration; never emits text or embedded images."""
 a=np.asarray(im.convert('RGB'));h,w=a.shape[:2]
 border=np.concatenate([a[0],a[-1],a[:,0],a[:,-1]])
 bg=np.median(border,axis=0)
 mask=np.max(abs(a.astype(float)-bg),axis=2)>10
 # Quantize only foreground; antialiasing remains the vector renderer's job.
 samples=a[mask].astype('float32');count=min(5,max(1,len(samples)//80))
 if len(samples)<5:raise ValueError('empty artwork trace')
 # Monochrome line art shares one continuous mask. Splitting antialias
 # shades into independent paths breaks thin strokes at their joins.
 chroma=samples-samples.mean(axis=1,keepdims=True)
 mono=monochrome
 if mono:
  count=1
 cv2.setRNGSeed(24)
 _,labels,colors=cv2.kmeans(samples,count,None,(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,50,.2),4,cv2.KMEANS_PP_CENTERS)
 groups=np.full(mask.shape,-1,dtype=int);groups[mask]=labels.ravel()
 if mono:colors=np.array([np.percentile(samples,15,axis=0)])
 paths=[]
 for i,c in enumerate(colors):
  # Discard antialias colors close to the local background.
  if max(abs(c-bg))<8:continue
  contours,hierarchy=cv2.findContours((groups==i).astype('uint8'),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  parts=[]
  for contour in contours:
   if abs(cv2.contourArea(contour))<2:continue
   points=cv2.approxPolyDP(contour,.35,True).reshape(-1,2)
   if len(points)<3:continue
   parts.append('M'+' L'.join(f'{x+.5:g},{y+.5:g}' for x,y in points)+' Z')
  if parts:paths.append('<path fill="'+hexcolor(np.round(c))+'" stroke="'+hexcolor(np.round(c))+'" stroke-width="0.9" stroke-linejoin="round" fill-rule="evenodd" d="'+' '.join(parts)+'"/>')
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">'+''.join(paths)+'</svg>\n'

def line_samples(im,b,target):
 crop,_,_=crop_rect(im,b);a=np.asarray(crop.convert('RGB')).astype(float)
 color=np.array([int(target[i:i+2],16) for i in (1,3,5)])
 distance=np.linalg.norm(a-color,axis=2)
 mask=(distance<85).astype('uint8')
 # Keep the connected line, excluding labels and grid strokes.
 num,labels,stats,_=cv2.connectedComponentsWithStats(mask)
 candidates=[i for i in range(1,num) if stats[i,cv2.CC_STAT_WIDTH]>a.shape[1]*.025]
 if candidates:
  mask=np.isin(labels,candidates)
 xs=[];ys=[]
 for x in range(a.shape[1]):
  eligible=np.where(mask[:,x])[0]
  if len(eligible):
   best=eligible[np.argmin(distance[eligible,x])];xs.append(x);ys.append(best)
 if len(xs)<a.shape[1]*.4:raise ValueError(f'line not recovered: {target} {len(xs)}/{a.shape[1]}')
 xx=np.linspace(xs[0],xs[-1],181);yy=np.interp(xx,xs,ys)
 # Small analysis smoothing removes single-pixel threshold chatter.
 yy=np.convolve(np.pad(yy,(1,1),mode='edge'),np.array([.2,.6,.2]),'valid')
 return xx/(a.shape[1]-1),1-yy/(a.shape[0]-1)

def repair(id):
 directory=HERE/id;baseline=HERE/'qa-work/baseline'/id
 doc=json.load(open(baseline/'mapped.json'));contract=json.load(open(baseline/'contract.json'))
 ann=json.load(open(baseline/'annotations.json'));obs=json.load(open(baseline/'observations.json'))
 original=directory/'authoring-contract.json'
 if not original.exists():write(original,contract)
 im=Image.open(directory/'reference.png').convert('RGB');pixels=np.asarray(im)
 nodes={n['id']:n for n in walk(doc['tree'])};entries={}
 anns={r['id']:r for r in ann['elements']}
 assets=directory/'repaired-assets';assets.mkdir(exist_ok=True)
 data_dir=directory/'data';data_dir.mkdir(exist_ok=True)
 def annotate(n,why):
  anns[n['id']]={'id':n['id'],'bounds':rect(n),'method':why,'reviewed':True}
 def entry(n,role,basis):
  e={'id':n['id'],'role':role,'basis':basis,'confidence':1.0,'decision':'reviewed'};entries[n['id']]=e;return e
 def bounds(n,b):n.update(dict(zip(('x','y','w','h'),b)))
 def add(n,parent=None):
  (parent or doc['tree'])['c'].append(n);nodes[n['id']]=n
 def remove(id):
  for p in list(nodes.values()):
   if 'c' in p:p['c']=[c for c in p['c'] if c['id']!=id]
  nodes.pop(id,None);anns.pop(id,None)
 # Preserve authoring evidence and declare the observed composition revision.
 contract['source_revision']={'basis':'reviewed original reference image','authoring_contract':'authoring-contract.json','changes':'Repair native charts, artwork extents, missing labels, typography and value controls.'}
 if id=='stock-04':
  bounds(nodes['chart_panel'],[23,279,359,274]);annotate(nodes['chart_panel'],'reviewed white chart card including range selectors')
 # Apply measured local surface gradients, not an image backdrop.
 for n in nodes.values():
  if n['t']!='stack' or 'bg' not in n:continue
  b=rect(n);x,y,w,h=b;sx,sy=im.width/406,im.height/776
  old=np.array([(n['bg']>>s)&255 for s in (16,8,0)])
  occupied=[rect(c) for c in walk(n) if c is not n and (c['t']!='stack' or 'bg' in c)]
  samples=[]
  for fy in np.linspace(.08,.92,13):
   for fx in np.linspace(.06,.94,13):
    px,py=x+w*fx,y+h*fy
    if any(xx<=px<=xx+ww and yy<=py<=yy+hh for xx,yy,ww,hh in occupied):continue
    ix,iy=round(px*sx),round(py*sy)
    if 0<=iy<pixels.shape[0] and 0<=ix<pixels.shape[1]:
     c=pixels[iy,ix].astype(float)
     if max(abs(c-old))<22:samples.append((fy,c))
  if len(samples)>25:
   mat=np.array([[1,fy] for fy,c in samples]);rgb=np.array([c for fy,c in samples]);coef=np.linalg.lstsq(mat,rgb,rcond=None)[0]
   n['bg']=argb(np.clip(np.round(coef[0]),0,255));n['bg2']=argb(np.clip(np.round(coef[0]+coef[1]),0,255))
 # Missing source artwork has its own native Image/Svg widget.
 if id=='news-04':
  add({'t':'svg','id':'latest_art','x':260,'y':587,'w':111,'h':112})
  contract['graphics']['latest_art']={'kind':'landscape'}
 artwork=copy.deepcopy(ART.get(id,{}));textrows={r['id']:r for r in obs['text']}
 for n in nodes.values():
  if not n['id'].startswith('day_icon_'):continue
  i=n['id'].split('_')[-1]
  label=textrows.get('day_label_'+i);temp=textrows.get('day_temp_'+i)
  if id in ('weather-02','weather-09'):
   center_y=(label['ink_bounds'][1]+label['ink_bounds'][3]/2) if label else n['y']+n['h']/2
   center_x=204 if id=='weather-02' else 213
   artwork[n['id']]=[center_x-31,center_y-30,62,60]
  elif label and temp:
   l,t=label['ink_bounds'],temp['ink_bounds'];cx=(l[0]+l[2]/2+t[0]+t[2]/2)/2
   top=l[1]+l[3]+3;bottom=t[1]-4
   artwork[n['id']]=[cx-31,top,62,bottom-top]
  else:raise ValueError('missing icon anchors '+id+' '+n['id'])
 for name,b in artwork.items():
  n=nodes[name];crop,box,logical=crop_rect(im,b);bounds(n,logical)
  raster=name in ('lead_art','rain_radar')
  path=assets/(name+('.png' if raster else '.svg'))
  if raster:crop.save(path);n.update(t='image',image_width=crop.width,image_height=crop.height)
  else:path.write_text(vectorize(crop));n['t']='svg'
  role='illustration' if name in ('lead_art','rain_radar','latest_art') else 'icon'
  e=entry(n,role,'Reviewed isolated source artwork; no UI text, controls or quantitative chart are included.'+(' Static rain-pattern illustration; the source provides no coordinates, time frames or radar measurements.' if name=='rain_radar' else ''))
  e['asset']={'path':str(path.relative_to(directory)),'sha256':sha(path),'reference_sha256':sha(directory/'reference.png'),
    'method':'source_crop' if raster else 'reference_svg','crop_pixels':box,'contains_ui':False,'fit':'contain','clip':True,
    'notes':'Original complex illustration pixels' if raster else 'Reference-colored vector contours; native SVG paths, no embedded bitmap/text.'}
  annotate(n,'reviewed source artwork region, measured in original pixels')
 # Numeric native plots.
 for name,(b,colors,fills) in PLOTS.get(id,{}).items():
  n=nodes[name];bounds(n,b);n.update(t='stockplot');n.pop('src',None)
  allsamples=[line_samples(im,b,c) for c in colors];x=allsamples[0][0]
  rows=[{'x':round(float(xx),6),**{f'y{j}':round(float(np.interp(xx,xxj,yyj)),6) for j,(xxj,yyj) in enumerate(allsamples)}} for xx in x]
  path=data_dir/(name+'.json');write(path,rows)
  role='chart.area' if name=='portfolio_chart' else 'chart.line'
  e=entry(n,role,'Numeric series digitized from the original trend; approximate design measurements, not market data.')
  e['data']={'path':str(path.relative_to(directory)),'sha256':sha(path),'origin':'measured_image','approximate':True,
    'x_key':'x','y_keys':[f'y{j}' for j in range(len(colors))],'units':{'x':'normalized image plot position','y':'normalized image plot height'},'domain':{'x':[0,1],'y':[0,1]}}
  e['plot']={'colors':colors,'fills':fills,'line_width':1.4,'gradient_fill':bool(fills)}
  if id=='stock-04':e['plot']['horizontal']=[{'value':1-(418-b[1])/b[3],'color':'#bba088','width':.6,'dotted':True}]
  if id in ('stock-05','stock-08'):
   yy=[336,377,418,458,499,539] if id=='stock-05' else [379,423,469,513,557]
   e['plot']['horizontal']=[{'value':1-(y-b[1])/b[3],'color':'#c8c5bd','width':.45} for y in yy]
   if id=='stock-05':e['plot']['vertical']=[{'value':0,'color':'#6c7063','width':.6}]
  if id=='weather-03':
   e['plot']['markers']=[]
   for mx in [64,157,254,346]:
    xx=(mx-b[0])/b[2];yy=float(np.interp(xx,x,allsamples[0][1]))
    e['plot']['markers'] += [{'x':xx,'y':yy,'color':'#ffffff','radius':4.2},{'x':xx,'y':yy,'color':colors[0],'radius':2.2}]
   e['plot']['vertical']=[{'value':(mx-b[0])/b[2],'color':'#9bb4d7','width':.6,'dotted':True} for mx in [64,157,254,346]]
  annotate(n,'reviewed quantitative plot domain in the reference; numeric samples retain their own bounds')
 if id=='stock-06':
  n=nodes['donut'];n.update(t='stockplot',variant='donut');bounds(n,[71,235,263,263])
  path=data_dir/'donut.json';write(path,[{'x':i,'value':v,'label':s} for i,(v,s) in enumerate([(64,'Stocks'),(28,'Funds'),(8,'Cash')])])
  e=entry(n,'chart.donut','Native category chart from the visible 64%, 28%, 8% allocation legend.')
  e['data']={'path':'data/donut.json','sha256':sha(path),'origin':'fixture','x_key':'x','y_keys':['value'],'units':{'x':'category-index','y':'percent'},'domain':{'x':[0,3],'y':[0,100]}}
  e['plot']={'colors':['#325c77','#7e94a6','#c3d8e4'],'inner_radius':.448};annotate(n,'reviewed circle center and radii; 0.95 native radius accounted for')
 if id=='news-07':
  n=nodes['waveform'];bounds(n,[44,175,316,96]);n['t']='stockplot'
  crop,_,_=crop_rect(im,rect(n));a=np.asarray(crop);mask=(a[:,:,2].astype(float)-a[:,:,0]>17)&(a[:,:,0]<170)
  counts=mask.sum(axis=0);active=counts>4;groups=[]
  for x in range(len(active)):
   if active[x] and (not x or not active[x-1]):groups.append([x,x])
   elif active[x]:groups[-1][1]=x
  rows=[]
  for lo,hi in groups:
   ys=np.where(mask[:,lo:hi+1])[0]
   rows.append({'x':((lo+hi)/2)/(crop.width-1),'amplitude':(ys.max()-ys.min()+1)/crop.height})
  path=data_dir/'waveform.json';write(path,rows)
  e=entry(n,'waveform','Measured amplitude envelope from the artwork waveform; no original audio was supplied.')
  e['data']={'path':'data/waveform.json','sha256':sha(path),'origin':'measured_image','approximate':True,'x_key':'x','y_keys':['amplitude'],'units':{'x':'normalized sample position','y':'normalized amplitude'},'domain':{'x':[0,1],'y':[-1,1]}}
  e['plot']={'colors':['#8056b2'],'line_width':2.1,'mode':'waveform'};annotate(n,'reviewed waveform envelope bounds including its tallest bars')
 if id=='news-09':
  for i in range(3):
   n=nodes[f'progress_{i}'];track=nodes[f'progress_track_{i}'];value=n['w']/track['w'];fillcolor=n['bg']
   bounds(n,rect(track));n.update(t='progress',value=value,color=fillcolor,bg=track['bg']);n.pop('variant',None)
   remove(track['id']);e=entry(n,'progress','Reading progress is one reusable value-driven native widget; track and fill are owned by the component.')
   e['behavior']={'event':'value_change','target':n['id'],'property':'value','value':value,'probe_value':.45 if value>.5 else .75}
   annotate(n,'reviewed full progress-track extent; normalized value controls its fill')
 if id=='stock-04':
  for i in range(4):
   label=nodes[f'period_{i}'];entry(label,'text','Native label owned by the adjacent chart-range control.')
   # A native Button owns each hit region; the Label remains independently inspectable.
   b=[label['x']-12,label['y']-6,label['w']+24,label['h']+15]
   control={'t':'button','id':f'range_control_{i}','enabled':True};bounds(control,b);add(control)
   e=entry(control,'range_option','Reviewed 1D/1W/1M/1Y native selector; changes the plot viewport over the measured fixture.')
   e['behavior']={'event':'click','target':'price_chart','property':'viewport','value':[[0,1],[.15,.9],[.3,.85],[.5,.8]][i]}
   annotate(control,'reviewed chart-range label with native hit padding')
 # Add missing source text as native Labels, using the original OCR bounds.
 if id in ('weather-03','stock-05','stock-08'):
  base=copy.deepcopy(next(n for n in nodes.values() if n['t']=='text' and n['id']=='subtitle'))
  for i,o in enumerate(obs['unmapped_ocr']):
   n=copy.deepcopy(base);n.update(id=f'chart_annotation_{i}',text=o['text'])
   sx,sy=im.width/406,im.height/776;bounds(n,[v/(sx if j%2==0 else sy) for j,v in enumerate(o['bounds'])]);add(n)
 # Record the reviewed composition, retaining original prompt/contract separately.
 contract['tree']=copy.deepcopy(doc['tree']);write(directory/'contract.json',contract)
 ann['elements']=list(anns.values());write(directory/'annotations.json',ann);write(directory/'mapped.json',doc)
 observed=observe(directory)
 if id=='news-07':
  # Vision's "1'1/1." is the waveform bars, verified against the isolated source region.
  observed['non_text_ocr']=[dict(o,classification='waveform strokes misread as characters',source_id='waveform',reviewed=True) for o in observed['unmapped_ocr']]
  observed['unmapped_ocr']=[];write(directory/'observations.json',observed)
 fit(directory)
 repaired=json.load(open(directory/'mapped.json'))
 for n in walk(repaired['tree']):
  if n['id'] in entries:continue
  role,basis,confidence=classify(n,contract)
  entries[n['id']]={'id':n['id'],'role':role,'basis':basis,'confidence':confidence,'decision':'declared' if confidence==1 else 'needs_review'}
 manifest={'schema_version':1,'policy_version':POLICY['version'],'reference_sha256':sha(directory/'reference.png'),'contract_sha256':sha(directory/'contract.json'),
  'classification_scope':'Reviewed original reference regions and authored intent; approximate plot measurements are explicitly marked.','elements':list(entries.values())}
 write(directory/'semantic-map.json',manifest);write_brief(directory,manifest)
 report=preflight(directory)
 return {'id':id,'nodes':len(entries),'semantic_preflight':report['pass']}

if __name__=='__main__':
 for id in sys.argv[1:]:print(json.dumps(repair(id)),flush=True)
