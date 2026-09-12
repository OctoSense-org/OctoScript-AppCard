#!/usr/bin/env python3
"""Fit real font faces to reference glyph silhouettes, then let Studio verify.

Raster masks here are analysis artifacts only. All output text remains Label.
The selected face is an approximation of the image, not asserted font identity.
"""
import functools,json,math
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw,ImageFont
from catalogue import HERE,walk
from observe import metrics
from compile import ROOT

FONT_ROOT=ROOT/'splash-makepad/apps/kit-host/resources'

def candidates():
    result=[]
    for family,folder,weights in [('Roboto','ux',{'Thin':100,'Light':300,'Regular':400,'Medium':500,'Bold':700}),
                                  ('RobotoCondensed','ux',{str(w):w for w in (200,300,400,500,600,700)}),
                                  ('Inter','ux',{str(w):w for w in (200,300,400,500,600,700)}),
                                  ('DMSans','camo',{'Regular':400,'Medium':500,'Bold':700})]:
        for suffix,weight in weights.items():
            path=FONT_ROOT/folder/f'{family}-{suffix}.ttf'
            if path.exists():result.append((family,weight,path))
    return result

@functools.lru_cache(maxsize=256)
def face(path,size):return ImageFont.truetype(str(path),size)

def score(text,path,target):
    # Simulate native spacing without horizontally stretching the glyphs.
    (x0,y0,x1,y1),advance,asc,desc=metrics(str(path),text)
    desired_height=target.shape[0]
    size=max(8,round(desired_height/(y1-y0)))
    font=face(path,size)
    tracking=(target.shape[1]-(x1-x0)*size)/max(1,len(text)-1)
    canvas=Image.new('L',(target.shape[1]+16,target.shape[0]+16))
    draw=ImageDraw.Draw(canvas);cursor=8-x0*size
    for ch in text:
        draw.text((cursor,8+y1*size),ch,font=font,fill=255,anchor='ls')
        cursor+=font.getlength(ch)+tracking
    a=np.asarray(canvas.crop((8,8,target.shape[1]+8,target.shape[0]+8)))>100
    overlap=np.logical_and(a,target).sum()/max(1,np.logical_or(a,target).sum())
    density=abs(math.log(max(1,a.sum())/max(1,target.sum())))
    return 1-overlap+.65*density+.1*abs(tracking/size)

def fit(directory, only_ids=None):
    directory=Path(directory);doc=json.loads((directory/'mapped.json').read_text())
    nodes={n['id']:n for n in walk(doc['tree'])};observed=json.loads((directory/'observations.json').read_text())
    source=np.asarray(Image.open(directory/'reference.png').convert('RGB'));sy,sx=source.shape[0]/776,source.shape[1]/406
    options=candidates();scores={};valid={}
    decision_path=directory/'font-decisions.json'
    decisions=json.loads(decision_path.read_text()).get('elements',{}) if decision_path.exists() else {}
    for row in observed['text']:
        if row['status']!='observed' or row['id'] not in nodes:continue
        node=nodes[row['id']];x,y,w,h=row['ink_bounds']
        box=source[round(y*sy):round((y+h)*sy),round(x*sx):round((x+w)*sx)].astype(float)
        if not box.size or not row.get('ink_color'):continue
        ink=np.array(row['ink_color']);mask=np.max(abs(box-ink),axis=2)<55
        # A fixed analysis height makes font selection independent of screenshot DPI.
        height=min(120,mask.shape[0]);width=max(1,round(mask.shape[1]*height/mask.shape[0]))
        mask=np.asarray(Image.fromarray((mask*255).astype('uint8')).resize((width,height)))>127
        scores[row['id']]=[(score(node['text'],path,mask),family,weight,str(path)) for family,weight,path in options]
        valid[row['id']]=row
    families={f for f,_,_ in options};aggregate={}
    for family in families:
        aggregate[family]=sum(min(s[0] for s in rows if s[1]==family) for id,rows in scores.items() if len(nodes[id]['text'])>=5)/max(1,sum(len(nodes[id]['text'])>=5 for id in scores))
    family=min(aggregate,key=aggregate.get);records=[]
    for id,rows in scores.items():
        if only_ids is not None and id not in only_ids:continue
        best=min((s for s in rows if s[1]==family or len(nodes[id]['text'])<5),key=lambda s:s[0]);
        if id in decisions:
            choice=decisions[id];best=min(s for s in rows if s[1]==choice['family'] and s[2]==choice['weight'])
        loss,_,weight,path=best
        n=nodes[id];row=valid[id];x,y,w,h=row['ink_bounds']
        if row.get('ink_color'):
            red,green,blue=row['ink_color'];n['color']=(255<<24)+(red<<16)+(green<<8)+blue
        (x0,y0,x1,y1),advance,asc,desc=metrics(path,n['text']);size=h/(y1-y0)
        tracking=(w-(x1-x0)*size)/max(1,len(n['text'])-1)
        n.update(font_src='self:resources/'+str(Path(path).relative_to(FONT_ROOT)),weight=weight,
                 size=size,tracking=tracking,line_height=h+4,alignx=0,
                 x=x-x0*size,y=y-2,w=max(w+4,advance*size+tracking*len(n['text'])+2),h=h+4,
                 font_asc=y1+2/size-asc,font_desc=(y1*size+2-(h+4))/size-desc)
        records.append({'id':id,'font':n['font_src'],'weight':weight,'silhouette_error':round(loss,4),
                        'reference_font_identity_verified':False,'tracking_px':round(tracking,4)})
    doc['font_repair']={'method':'reference glyph silhouette fit; native verification required','family':family,'family_errors':aggregate}
    (directory/'mapped.json').write_text(json.dumps(doc,indent=2)+'\n')
    previous=directory/'font-fit.json'
    if only_ids is not None and previous.exists():
        records=[r for r in json.loads(previous.read_text())['elements'] if r['id'] not in only_ids]+records
    previous.write_text(json.dumps({'family':family,'family_errors':aggregate,'elements':records},indent=2)+'\n')
    return {'id':directory.name,'family':family,'elements':len(records)}

if __name__=='__main__':
    import sys
    for id in sys.argv[1:]:print(json.dumps(fit(HERE/id)),flush=True)
