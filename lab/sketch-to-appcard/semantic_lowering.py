"""Lower reviewed Sketch data regions through the same native chart adapters.

Each replacement lists exact source paint owners. Text, controls and layout
groups remain separate widgets; original source paths stay in the specification.
"""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # lab/, for `core`
import copy
import json
from core.semantic_policy import POLICY,walk
from core.policy import data_issues


def lower(spec,tree,manifest,directory):
    if manifest.get('reference_sha256')!=spec.get('reference_sha256') or manifest.get('policy_version')!=POLICY['version']:
        raise ValueError('stale semantic lowering decisions')
    def nodes(n):
        yield n
        for c in n.get('c',[]):yield from nodes(c)
    source={n.get('native_widget_id'):n for n in walk(spec) if n.get('native_widget_id')}
    generated={n['id']:n for n in nodes(tree)};bindings=[]
    for entry in manifest.get('elements',[]):
        replacement=entry.get('replacement')
        if not replacement:continue
        owner=source.get(entry['id']);parent=generated.get(entry['id'])
        if not owner or not parent or parent['t']!='stack':raise ValueError(f'semantic replacement requires a source layout owner: {entry["id"]} ({(parent or {}).get("t")})')
        if entry.get('decision')!='reviewed' or not entry.get('basis'):raise ValueError('semantic replacement requires reviewed evidence')
        role=entry['role'];rule=POLICY['roles'].get(role,{})
        if role not in ('chart.line','chart.area','chart.donut','chart.bar','chart.radar','chart.scatter','waveform','progress'):
            raise ValueError('native adapter is not implemented for '+role)
        problems=data_issues(directory,entry) if rule.get('data') else []
        if problems:raise ValueError('; '.join(problems))
        paint=replacement.get('paint_sources',[])
        if not paint or len(paint)!=len(set(paint)):raise ValueError('declare distinct source paint owners')
        owned={n.get('native_widget_id') for n in walk(owner)};boxes=[];removed=set()
        for ident in paint:
            if ident==entry['id'] or ident not in owned or ident not in generated:
                raise ValueError(f'paint replacement escapes its source region: owner={entry["id"]}, paint={ident}, owned={ident in owned}, generated={ident in generated}')
            branch=source[ident]
            if any(n.get('text') or n.get('control') for n in walk(branch)):
                raise ValueError('a chart cannot flatten source text or controls')
            paints=[n for n in nodes(generated[ident]) if n['t'] in ('svg','image')]
            boxes.extend([n[k] for k in ('x','y','w','h')] for n in paints or [generated[ident]])
            removed.update(n['id'] for n in nodes(generated[ident]))
            for n in walk(branch):
                for key in ('native_widget_id','native_paint_id','graphic_asset'):n.pop(key,None)
                n['graphic_part_of']=entry['id'];n['rendering']={'backend':'native_data','reason':'source paint represented by explicit numeric samples'}
        def prune(n):
            if 'c' in n:n['c']=[c for c in n['c'] if c['id'] not in removed]
            for c in n.get('c',[]):prune(c)
        # Preserve the source paint's position among backgrounds and labels.
        # Always inserting first can hide a radar inside its opaque card.
        insertion=next((i for i,c in enumerate(parent.get('c',[]))
                        if any(n['id'] in removed for n in nodes(c))),len(parent.get('c',[])))
        insertion=sum(c['id'] not in removed for c in parent.get('c',[])[:insertion])
        prune(parent)
        x=min(b[0] for b in boxes);y=min(b[1] for b in boxes)
        w=max(b[0]+b[2] for b in boxes)-x;h=max(b[1]+b[3] for b in boxes)-y
        wid=entry.get('widget_id',entry['id']+'_data')
        if wid in generated:raise ValueError('duplicate semantic widget ID')
        if replacement.get('bounds_source'):
            box=generated.get(replacement['bounds_source'])
            if not box or replacement['bounds_source'] not in owned:raise ValueError('bounds source escapes chart region')
            x,y,w,h=[box[k] for k in ('x','y','w','h')]
        chart={'id':wid,'t':'stockplot','variant':{'chart.donut':'donut','chart.bar':'bar','chart.radar':'radar','chart.scatter':'scatter'}.get(role,'line'),
               'x':x,'y':y,'w':w,'h':h}
        if role=='waveform' and entry.get('plot',{}).get('mode')=='intervals':chart['variant']='bar'
        if role=='progress':
            progress=entry.get('progress',{})
            if type(progress.get('value')) not in (float,int) or not 0<=progress['value']<=1:
                raise ValueError('progress needs a normalized source value')
            chart.update(t='progress',value=progress['value'],bg=progress['track'],color=progress['fill'])
            chart.pop('variant')
        placed=chart
        if replacement.get('clip_to_bounds'):
            # A source mask may clip data paint while allowing independent
            # markers or tooltips to extend outside the same plot region.
            for ident in paint:
                masks=source[ident].get('graphic_masks',[])
                scale=owner['w']/parent['w']
                if not any(all(abs(mask[k]/scale-v)<.01 for k,v in zip(('x','y','w','h'),(x,y,w,h))) for mask in masks):
                    raise ValueError('native data clip lacks matching source-mask evidence')
            placed={'t':'stack','variant':'clip','id':wid+'_clip','x':x,'y':y,'w':w,'h':h,'c':[chart]}
        parent.setdefault('c',[]).insert(insertion,placed)
        owner['semantic_role']=role;owner['native_data_widget_id']=wid
        owner['native_data_bounds_logical']=[x,y,w,h]
        bindings.append({**copy.deepcopy(entry),'id':wid})
    return bindings
