"""Recover a reviewed single-series line region as approximate numeric data.

The source region, color and domains are explicit review inputs. OCR ink is
excluded so labels cannot turn into spikes. Ambiguous/missing columns fail.
Output is consumed by LinePlot; no source pixels become chart paint.
"""
import argparse,json
from pathlib import Path
import numpy as np
from PIL import Image
from observe import ocr
from compile import digest


def measure(directory,ident,bounds,color,x_domain,y_domain,stride=2,smooth=0):
    directory=Path(directory);source=directory/'reference.png';pixels=np.asarray(Image.open(source).convert('RGB')).astype(float)
    x,y,w,h=map(int,bounds)
    if x<0 or y<0 or w<2 or h<2 or x+w>pixels.shape[1] or y+h>pixels.shape[0]:raise ValueError('invalid source chart region')
    ink=np.array([int(color.lstrip('#')[i:i+2],16) for i in (0,2,4)])
    mask=np.max(abs(pixels[y:y+h,x:x+w]-ink),axis=2)<42
    for row in ocr(source)['observations']:
        a,b,c,d=row['bounds'];left=max(x,int(a)-2);top=max(y,int(b)-2)
        right=min(x+w,int(a+c)+3);bottom=min(y+h,int(b+d)+3)
        if right>left and bottom>top:mask[top-y:bottom-y,left-x:right-x]=False
    points=[];columns=[]
    for column in range(0,w,stride):
        hits=np.where(mask[:,column])[0]
        if not len(hits):continue
        if hits[-1]-hits[0]>18:raise ValueError(f'ambiguous chart column {x+column}; narrow the region or separate series')
        columns.append(column);points.append({'x':x_domain[0]+column/(w-1)*(x_domain[1]-x_domain[0]),
            'y':y_domain[1]-float(np.median(hits))/(h-1)*(y_domain[1]-y_domain[0])})
    if len(points)<8 or max(np.diff(columns),default=0)>max(8,stride*4):raise ValueError('insufficient continuous chart evidence')
    if smooth:
        if smooth<3 or smooth%2!=1 or smooth>len(points):raise ValueError('smooth must be an odd sample window of at least 3')
        values=np.array([p['y'] for p in points]);half=smooth//2
        filtered=np.convolve(np.pad(values,half,mode='edge'),np.ones(smooth)/smooth,mode='valid')
        for point,value in zip(points,filtered):point['y']=float(value)
    out=directory/'data'/f'{ident}.json';out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(points,indent=2)+'\n')
    report={'reference_sha256':digest(source.read_bytes()),'crop_pixels':bounds,'color':color,'samples':len(points),
            'method':'reviewed chart ROI, color separation, OCR exclusion, median centerline; approximate source values',
            'data_sha256':digest(out.read_bytes()),'domain':{'x':x_domain,'y':y_domain},'smoothing_window_samples':smooth}
    (out.with_suffix('.measurement.json')).write_text(json.dumps(report,indent=2)+'\n')
    return report


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--directory',required=True);p.add_argument('--id',required=True)
    p.add_argument('--bounds',nargs=4,type=int,required=True);p.add_argument('--color',required=True)
    p.add_argument('--x-domain',nargs=2,type=float,required=True);p.add_argument('--y-domain',nargs=2,type=float,required=True)
    p.add_argument('--smooth',type=int,default=0)
    a=p.parse_args();print(json.dumps(measure(a.directory,a.id,a.bounds,a.color,a.x_domain,a.y_domain,smooth=a.smooth)))
