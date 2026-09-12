#!/usr/bin/env python3
"""Recorded repairs from source/native screenshot review, preserving prior fits."""
import copy,json,sys
import numpy as np
from PIL import Image
from catalogue import HERE,walk
from semantics import write,sha,write_brief
from fit_reference_fonts import fit
from observe import observe

FONTS={
 'weather-03':{'heading':('DMSans',700),'humidity_value':('Roboto',700),'primary_label':('Roboto',500)},
 'weather-08':{'metric_0_value':('Roboto',700)},
 'weather-10':{'heading':('Roboto',700),'comfort_score':('RobotoCondensed',300),'comfort_label':('Roboto',700),'activity':('Roboto',700),'sunrise_value':('RobotoCondensed',600),'sunset_value':('RobotoCondensed',600)},
 'news-04':{'topic_title_0':('DMSans',700)},
 'news-08':{'lead_title':('RobotoCondensed',600),'lead_title2':('Roboto',700)},
 'news-09':{f'story_{i}_title{s}':('Roboto',500) for i in range(3) for s in ('','2')},
 'news-10':{'lead_title':('RobotoCondensed',600),'lead_title2':('RobotoCondensed',600)},
 'stock-05':{'index_value_0':('Roboto',700),'index_value_2':('Roboto',700),'trend_title':('Roboto',700),'quote_price':('Roboto',500),**{f'index_gain_{i}':('Roboto',500) for i in range(3)}},
 'stock-08':{'heading':('DMSans',700),'performance_title':('Roboto',700)},
 'stock-09':{'heading':('Roboto',700)},
}
BORDERS={
 'weather-01':(['forecast','humidity','wind'],0xffedf0ec),
 'weather-03':(['timeline','humidity','wind'],0xffe9edf5),
 'weather-06':(['city_0','city_1','city_2'],0xffdee8f0),
 'news-04':(['topic_1','topic_2','topic_3','latest'],0xffeee5d8),
 'stock-01':(['quote_0','quote_1'],0xffeef0e9),
 'stock-02':([f'quote_{i}' for i in range(4)],0xff1d354b),
 'stock-03':(['tile_1','tile_2','tile_3'],0xffe9edf5),
 'stock-05':(['index_1','index_2','trend','quote'],0xffe8e2d9),
 'stock-08':(['compare_1','comparison','apple_return','nvidia_return'],0xffe9ddd2),
}

def split_wind(p,key):
    m=json.load(open(p/'mapped.json'));c=json.load(open(p/'contract.json'));o=json.load(open(p/'observations.json'))
    nodes={n['id']:n for n in walk(m['tree'])};n=nodes[key]
    if n['t']!='text':return []
    row=next(r for r in o['text'] if r['id']==key);x,y,w,h=row['ink_bounds']
    im=Image.open(p/'reference.png').convert('RGB');a=np.asarray(im).astype(float);sx,sy=im.width/406,im.height/776
    ix,iy=round(x*sx),round(y*sy);box=a[iy:round((y+h)*sy),ix:round((x+w)*sx)]
    mask=np.max(abs(box-np.array(row['ink_color'])),axis=2)<45
    # The reviewed reference uses large numerals and a smaller unit. Locate the
    # intervening empty column; keep both measurements tied to the source OCR.
    cols=mask.any(axis=0);candidates=np.where(~cols)[0]
    cut=min((v for v in candidates if .25*len(cols)<v<.5*len(cols)),key=lambda v:abs(v-.38*len(cols)))
    original=copy.deepcopy(n);parts=[];children=[]
    manifest=json.load(open(p/'semantic-map.json'));entries={e['id']:e for e in manifest['elements']}
    for suffix,text,lo,hi in [('number','12',0,cut),('unit','km/h',cut,len(cols))]:
        yy,xx=np.where(mask[:,lo:hi]);b=[(ix+lo+xx.min())/sx,(iy+yy.min())/sy,(xx.max()-xx.min()+1)/sx,(yy.max()-yy.min()+1)/sy]
        child=copy.deepcopy(original);child.update(id=key+'_'+suffix,text=text,x=b[0]-1,y=b[1]-2,w=b[2]+3,h=b[3]+4)
        children.append(child);parts.append({'id':child['id'],'ink_bounds':b,'ink_color':row['ink_color'],'light_foreground':False})
        entries[child['id']]={'id':child['id'],'role':'text','basis':'Reviewed numeric value and smaller unit composed with independent native Labels.','confidence':1.0,'decision':'reviewed'}
    n.clear();n.update(t='stack',id=key,x=x-2,y=y-2,w=w+4,h=h+4,c=children)
    annotations=json.load(open(p/'annotations.json'));annotations['elements'].append({'id':key,'bounds':[n[k] for k in ('x','y','w','h')],'method':'reviewed source mixed-size text group','reviewed':True})
    groups=json.load(open(p/'text-annotations.json'));groups['groups'].append({'id':key,'text':original['text'],'bounds':[x,y,w,h],'parts':parts})
    entries[key].update(role='layout',basis='Native value and independently sized unit Labels.')
    c['tree']=copy.deepcopy(m['tree']);write(p/'contract.json',c);write(p/'mapped.json',m);write(p/'annotations.json',annotations);write(p/'text-annotations.json',groups)
    observe(p);manifest.update(contract_sha256=sha(p/'contract.json'),elements=list(entries.values()));write(p/'semantic-map.json',manifest);write_brief(p,manifest)
    return [child['id'] for child in children]

def repair(id):
    p=HERE/id;choices=dict(FONTS.get(id,{}))
    if id in ('weather-03','weather-04','weather-08'):
        for key in split_wind(p,'metric_1_value' if id=='weather-08' else 'wind_value'):choices[key]=('Roboto',700)
    if choices:
        path=p/'font-decisions.json';decisions=json.load(open(path)) if path.exists() else {'elements':{}}
        for key,(family,weight) in choices.items():decisions['elements'][key]={'family':family,'weight':weight,'basis':'Source/native visual QA: preserve readable word spaces and value/unit proportions.'}
        write(path,decisions);fit(p,set(choices))
    m=json.load(open(p/'mapped.json'));nodes={n['id']:n for n in walk(m['tree'])}
    changed=[]
    if id in BORDERS:
        keys,color=BORDERS[id]
        for key in keys:
            if key in nodes:nodes[key].update(border=.65,bordercolor=color,value=1.);changed.append(key)
    if id=='weather-05':
        for key,n in nodes.items():
            if key.startswith('forecast_separator_'):n.update(w=.8,bg=0xffe6e1d9,radius=0)
    write(p/'mapped.json',m)
    s=json.load(open(p/'semantic-map.json'))
    if id in ('stock-05','stock-08'):
        e=next(e for e in s['elements'] if 'plot' in e);lines=e['plot']['horizontal']
        lines[-1].update(dotted=False,color='#8b8c81' if id=='stock-05' else '#ad9282',width=.7)
        if id=='stock-08':lines[2].update(dotted=False,color='#ad9282',width=.7)
    if id=='stock-06':
        next(e for e in s['elements'] if 'plot' in e)['plot']['slice_gap']=3.0
    write(p/'semantic-map.json',s);write_brief(p,s)
    print(id,'fonts',list(choices),'borders',changed,flush=True)

if __name__=='__main__':
    for id in sys.argv[1:]:repair(id)
