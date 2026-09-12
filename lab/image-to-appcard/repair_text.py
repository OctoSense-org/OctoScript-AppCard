#!/usr/bin/env python3
"""Apply bounded, recorded residual corrections from a real Studio capture."""
import argparse,json,copy,sys
from catalogue import HERE,walk
sys.path.insert(0,str(HERE.parent))
from core.repair import apply,sha

def repair(directory):
    latest=json.loads((directory/'latest.json').read_text());r=directory/'rounds'/latest['round']
    plan_path=directory/f'text-repair-{latest["round"]}.json'
    if plan_path.exists():
        result=apply(directory,plan_path)
        return result['changes']
    gate=json.loads((r/'gate.json').read_text());path=directory/'mapped.json';doc=json.loads(path.read_text())
    if not (r/'mapped.json').exists() or sha(path.read_bytes())!=sha((r/'mapped.json').read_bytes()):
        raise ValueError('text repair requires a capture of the current mapped design')
    before=copy.deepcopy(doc['tree'])
    nodes={n['id']:n for n in walk(doc['tree'])};changes=[]
    for row in gate['text_differences']:
        if not row['issues'] or not row['delta']:continue
        dx,dy,dw,dh=row['delta'];n=nodes[row['id']];change={'id':n['id'],'from_round':latest['round']}
        if 'text ink dimensions' in row['issues'] and abs(dy)<=2 and abs(dh)<=1.5 and abs(dw)<=10 and len(n['text'])>=2:
            adjustment=-dw/(len(n['text'])-1)
            n['tracking']=n.get('tracking',0)+adjustment
            n['w']+=max(0,-dw)*len(n['text'])/(len(n['text'])-1)+1
            change.update(ink_width_delta=dw,tracking_adjustment=adjustment)
        if 'text ink position' in row['issues'] and max(abs(dx),abs(dy))<=6:
            n['x']-=dx;n['y']-=dy;change['position_adjustment']=[-dx,-dy]
        if 'text color' in row['issues'] and row.get('reference_color') and row.get('native_color'):
            old=[(n['color']>>shift)&255 for shift in (16,8,0)]
            adjustment=[round(max(-32,min(32,(wanted-actual)*1.2))) for wanted,actual in zip(row['reference_color'],row['native_color'])]
            rgb=[max(0,min(255,v+delta)) for v,delta in zip(old,adjustment)]
            n['color']=(255<<24)+(rgb[0]<<16)+(rgb[1]<<8)+rgb[2]
            change.update(color_before=old,color_after=rgb,reference_ink=row['reference_color'],captured_ink=row['native_color'])
        if len(change)>2:changes.append(change)
    if changes:
        plan={'schema_version':1,'findings':changes,
              'evidence':{str((r/'gate.json').relative_to(directory)):sha((r/'gate.json').read_bytes()),
                          'reference.png':sha((directory/'reference.png').read_bytes())},
              'inputs':{'mapped.json':sha(path.read_bytes())},
              'operations':[{'op':'set','file':'mapped.json','pointer':'/tree','before':before,'after':doc['tree'],
                             'category':'typography','element':','.join(c['id'] for c in changes),
                             'reason':'Measured bounded residual corrections from round '+latest['round']}]}
        plan_path.write_text(json.dumps(plan,indent=2)+'\n');apply(directory,plan_path)
    return changes

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('design',nargs='+');a=p.parse_args()
    for id in a.design:print(json.dumps({'id':id,'repairs':repair(HERE/id)}))
