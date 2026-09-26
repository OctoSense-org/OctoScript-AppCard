#!/usr/bin/env python3
"""Propose source-image surface bounds; never infer them from native captures.

Rounded rectangles are found from reference edges, then associated using OCR
descendants. Transparent groups and hit targets have inferred semantic extents.
Graphic proposals remain explicitly unreviewed, even when their bounds match.
"""
import argparse,json,sys
import numpy as np
from PIL import Image
from catalogue import HERE,walk
from compile import digest
from observe import observe
sys.path.insert(0,str(HERE/'.deps'))
import cv2

def measure(directory):
    directory=HERE/directory if isinstance(directory,str) else directory
    observations=observe(directory);doc=json.loads((directory/'contract.json').read_text())
    tree=doc['tree'];nodes=list(walk(tree));byid={n['id']:n for n in nodes}
    image=np.asarray(Image.open(directory/'reference.png').convert('RGB').resize((406,776)))
    gray=cv2.cvtColor(cv2.GaussianBlur(image,(5,5),1),cv2.COLOR_RGB2GRAY)
    candidates=[]
    for thresholds in [(2,6),(4,12),(10,30)]:
        contours,_=cv2.findContours(cv2.Canny(gray,*thresholds),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            x,y,w,h=cv2.boundingRect(c);area=cv2.contourArea(c)
            if w<40 or h<25 or area/(w*h)<.82:continue
            box=[float(x),float(y),float(w),float(h)]
            if any(max(abs(a-b) for a,b in zip(box,k))<3 for k in candidates):continue
            candidates.append(box)
    obs={n['id']:n for n in observations['text'] if n['status']=='observed'}
    found={};used=set();rows=[];parents={c['id']:n['id'] for n in nodes for c in n.get('c',[])}
    def inside(box,point,tol=2):
        x,y,w,h=box;px,py=point;return x-tol<=px<=x+w+tol and y-tol<=py<=y+h+tol
    for n in sorted([n for n in nodes if 'bg' in n and n['id']!='page'],key=lambda n:n['w']*n['h'],reverse=True):
        # Semantic button text is a sibling of its paint surface.
        group=byid[parents[n['id']]] if n['id'].endswith('_surface') else n
        anchors=[obs[c['id']]['ink_bounds'] for c in walk(group) if c['id'] in obs]
        best=None
        for i,b in enumerate(candidates):
            if i in used:continue
            if not .45<b[2]/n['w']<2.1 or not .4<b[3]/n['h']<3:continue
            if anchors and not all(inside(b,(a[0]+a[2]/2,a[1]+a[3]/2)) for a in anchors):continue
            distance=abs(b[0]-n['x'])+abs(b[1]-n['y'])+.4*abs(b[2]-n['w'])+.3*abs(b[3]-n['h'])
            # Prefer a tight enclosing panel, not another large enclosing card.
            if anchors:distance+=.001*b[2]*b[3]
            if best is None or distance<best[0]:best=(distance,i,b)
        if best:
            _,i,b=best;used.add(i);found[n['id']]=b
            if n['id'].endswith('_surface'):found[parents[n['id']]]=b
    def transformed(n):
        if n['id'] in found:return found[n['id']]
        parent=parents.get(n['id'])
        if not parent:return [n['x'],n['y'],n['w'],n['h']]
        p=byid[parent];b=transformed(p)
        return [b[0]+(n['x']-p['x'])*b[2]/p['w'],b[1]+(n['y']-p['y'])*b[3]/p['h'],n['w']*b[2]/p['w'],n['h']*b[3]/p['h']]
    for n in nodes:
        if n['t']=='text':continue
        b=transformed(n);method='inferred semantic extent from observed parent'
        if n['id']=='page':method='image canvas';b=[0,0,406,776]
        elif n['id'] in found:method='reference edge contour with contained OCR text anchors'
        elif n['t']=='svg':method='graphic extent projected from observed parent; visual annotation needed'
        elif 'bg' in n:method='surface contour unresolved; requested geometry retained'
        row={'id':n['id'],'bounds':[round(v,3) for v in b],'method':method,'reviewed':False}
        if 'bg' in n:
            # Sample the panel interior, excluding text; record a flat-color
            # approximation rather than claiming generated gradients are flat.
            x,y,w,h=b;x0=max(0,int(x+4));x1=min(406,int(x+w-4));y0=max(0,int(y+4));y1=min(776,int(y+h-4))
            crop=image[y0:y1,x0:x1]
            if n['id']=='page':crop=image[:,2:10]
            if crop.size:
                rgb=np.median(crop.reshape(-1,3),axis=0).round().astype(int)
                row['bg']=int(0xff000000+int(rgb[0])*65536+int(rgb[1])*256+int(rgb[2]))
            if n.get('radius'):row['radius']=round(min(b[2],b[3])*min(.5,n['radius']/min(n['w'],n['h'])),2)
        rows.append(row)
    report={'schema_version':1,'reference_sha256':observations['reference_sha256'],'method':'automatic proposals; unreviewed source-image measurements',
            'candidate_rectangles':candidates,'elements':rows}
    path=directory/'annotations.json'
    if path.exists():
        prior=json.loads(path.read_text())
        if prior.get('method')!=report['method']:raise ValueError('Refusing to overwrite manually reviewed annotations: '+str(path))
    path.write_text(json.dumps(report,indent=2)+'\n')
    return {'id':directory.name,'surfaces_found':len(found),'nontext':len(rows),'candidates':len(candidates)}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('design',nargs='+');a=p.parse_args()
    for id in a.design:print(json.dumps(measure(id)))
