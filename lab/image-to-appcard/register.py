"""Register an authored new input without regenerating the existing catalogue."""
import argparse,json,re
from catalogue import HERE


def register(ident):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',ident):raise ValueError('invalid design ID')
    root=HERE/ident;doc=json.loads((root/'contract.json').read_text())
    if doc.get('id')!=ident:raise ValueError('contract ID differs from the directory')
    if doc.get('artboard')!=[406,776]:raise ValueError('current image renderer is certified only for a 406 by 776 logical artboard')
    for name in ('reference.png','generation.json','image-prompt.md'):
        if not (root/name).is_file():raise ValueError('missing immutable reference intake: '+name)
    path=HERE/'catalogue.json';rows=json.loads(path.read_text())
    entry={k:doc[k] for k in ('id','app','number','title','structure')}
    old=next((r for r in rows if r['id']==ident),None)
    if old:
        if old!=entry:raise ValueError('design registration changed; use a new ID')
        return entry
    rows.append(entry);pending=path.with_suffix('.pending.json')
    pending.write_text(json.dumps(rows,indent=2)+'\n');pending.replace(path)
    return entry


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('id');print(json.dumps(register(p.parse_args().id)))
