"""Sample a source SVG's single open cubic curve into numeric chart values.

This adapter deliberately rejects transforms, multiple paths and unsupported
commands. It does not render SVG or pretend source geometry is market data.
"""
import argparse,json,math,re
import xml.etree.ElementTree as ET
from pathlib import Path
from hashlib import sha256


def sample(source,output,steps=64):
    if steps<8:raise ValueError('at least eight subdivisions are required')
    source=Path(source);root=ET.fromstring(source.read_bytes())
    elements=list(root.iter());paths=[e for e in elements if e.tag.split('}')[-1]=='path']
    if len(paths)!=1 or any(e.get('transform') for e in elements):raise ValueError('requires one untransformed curve')
    x0,y0,w,h=map(float,root.attrib['viewBox'].replace(',',' ').split())
    if w<=0 or h<=0:raise ValueError('invalid SVG canvas')
    raw=paths[0].attrib['d'];pattern=r'[MLC]|[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?'
    if re.sub(pattern,'',raw).strip(' ,\n\t'):raise ValueError('only absolute M, L and C commands are supported')
    tokens=re.findall(pattern,raw);at=0;points=[];current=None
    def pair():
        nonlocal at
        value=tuple(map(float,tokens[at:at+2]));at+=2
        if len(value)!=2 or not all(map(math.isfinite,value)):raise ValueError('invalid curve point')
        return value
    while at<len(tokens):
        command=tokens[at];at+=1
        if command=='M':
            if current is not None:raise ValueError('multiple subpaths are not a single series')
            current=pair();points.append(current)
        elif command=='L' and current is not None:current=pair();points.append(current)
        elif command=='C' and current is not None:
            a,b,c=pair(),pair(),pair();start=current
            for index in range(1,steps+1):
                t=index/steps;u=1-t
                points.append(tuple(u**3*start[k]+3*u*u*t*a[k]+3*u*t*t*b[k]+t**3*c[k] for k in (0,1)))
            current=c
        else:raise ValueError('invalid curve command sequence')
    if len(points)<2 or any(b[0]<a[0] for a,b in zip(points,points[1:])):raise ValueError('source curve must be monotonic in x')
    rows=[{'x':(x-x0)/w,'y':1-(y-y0)/h} for x,y in points]
    output=Path(output);output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(rows,indent=2)+'\n')
    receipt={'source_svg_sha256':sha256(source.read_bytes()).hexdigest(),'data_sha256':sha256(output.read_bytes()).hexdigest(),
             'samples':len(rows),'viewbox':[x0,y0,w,h],'origin':'measured_sketch','approximate':True,
             'method':'Cubic source geometry sampled in normalized source-canvas units; not recovered business values'}
    output.with_suffix('.measurement.json').write_text(json.dumps(receipt,indent=2)+'\n')
    return receipt


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('output');a=p.parse_args()
    print(json.dumps(sample(a.source,a.output)))
