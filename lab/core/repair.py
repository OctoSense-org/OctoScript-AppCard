"""Declarative, hash-bound repairs with restartable multi-file commits.

The plan is data, never executable Python. Gate findings and reviewed source
images remain immutable. Applying a plan never grants acceptance; each branch
must compile, recapture, inspect and visually review the resulting page.
"""
import argparse
import base64
import hashlib
import json
from pathlib import Path

CATEGORIES={'layout','typography','color','asset','semantic','data','hierarchy','state'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value,indent=2,ensure_ascii=False)+'\n').encode()


def target(root,relative):
    path=(root/relative).resolve()
    if not path.is_relative_to(root) or path==root:
        raise ValueError('repair path escapes the design workspace: '+relative)
    return path


def write(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.repair-pending')
    tmp.write_bytes(data);tmp.replace(path)


def pointer(doc,path):
    if not path.startswith('/') or path=='/':raise ValueError('expected a non-root JSON pointer')
    keys=[s.replace('~1','/').replace('~0','~') for s in path[1:].split('/')]
    value=doc
    for key in keys[:-1]:value=value[int(key)] if isinstance(value,list) else value[key]
    key=int(keys[-1]) if isinstance(value,list) else keys[-1]
    return value,key


def prepare(root,plan):
    if plan.get('schema_version')!=1 or not plan.get('findings') or not plan.get('operations'):
        raise ValueError('repair requires schema_version 1, findings and concrete operations')
    if not plan.get('evidence') or not plan.get('inputs'):
        raise ValueError('repair must bind both gate evidence and edited source hashes')
    for relative,expected in {**plan['evidence'],**plan['inputs']}.items():
        path=target(root,relative)
        actual=sha(path.read_bytes()) if path.exists() else None
        if actual!=expected:raise ValueError('stale repair input: '+relative)
    staged={};changes=[]
    for op in plan['operations']:
        if op.get('category') not in CATEGORIES or not op.get('element') or not op.get('reason'):
            raise ValueError('every repair needs a category, source element and reason')
        relative=op['file'];path=target(root,relative)
        if relative not in plan['inputs']:raise ValueError('unbound repair output: '+relative)
        if relative in plan['evidence']:raise ValueError('repair cannot rewrite gate/reference evidence')
        if op['op'] in ('set','document') and path.suffix!='.json':raise ValueError('structured repairs require a JSON file')
        if op['op']=='document':
            if not isinstance(op['after'],(dict,list)):raise ValueError('replacement document must be structured JSON')
            staged[relative]=encode(op['after'])
        elif op['op']=='set':
            doc=json.loads(staged.get(relative,path.read_bytes()))
            parent,key=pointer(doc,op['pointer'])
            exists=key in parent if isinstance(parent,dict) else 0<=key<len(parent)
            if exists!=op.get('exists',True) or (exists and parent[key]!=op['before']):
                raise ValueError('repair precondition changed: '+relative+op['pointer'])
            parent[key]=op['after'];staged[relative]=encode(doc)
        elif op['op']=='asset':
            # This supports reviewed SVG and an exact source asset/crop prepared
            # by the branch's provenance-aware intake. No executable payloads.
            source=op['source'];source_path=target(root,source)
            if source not in plan['evidence']:raise ValueError('replacement asset lacks a source receipt')
            if source_path.suffix.lower() not in ('.svg','.png','.jpg','.jpeg','.webp','.ttf','.otf'):
                raise ValueError('unsupported asset type')
            staged[relative]=source_path.read_bytes()
        else:raise ValueError('unsupported repair operation: '+str(op['op']))
        changes.append({k:op[k] for k in ('category','element','file','reason')})
    return staged,changes


def apply(root,plan_path,preview=False,after_write=None):
    root=Path(root).resolve();plan_path=Path(plan_path).resolve()
    raw=plan_path.read_bytes();plan=json.loads(raw);ident=sha(raw)
    journal_path=root/'.repairs'/f'{ident}.json'
    if journal_path.exists():
        journal=json.loads(journal_path.read_text())
        # Evidence remains mandatory during recovery. A source edit which is
        # neither our before nor our after state is a conflict, never overwritten.
        for relative,expected in plan['evidence'].items():
            if sha(target(root,relative).read_bytes())!=expected:
                raise ValueError('repair evidence changed during recovery: '+relative)
        for relative,expected in plan['inputs'].items():
            if relative in journal['outputs']:continue
            path=target(root,relative)
            actual=sha(path.read_bytes()) if path.exists() else None
            if actual!=expected:raise ValueError('repair dependency changed during recovery: '+relative)
        for relative,item in journal['outputs'].items():
            p=target(root,relative);actual=sha(p.read_bytes()) if p.exists() else None
            allowed=(item['after'],) if journal['status']=='applied' else (item['before'],item['after'])
            if actual not in allowed:raise ValueError('repair recovery conflict: '+relative)
        if journal['status']=='applied':return {k:v for k,v in journal.items() if k!='outputs'}|{'replayed':True}
    else:
        staged,changes=prepare(root,plan)
        journal={'schema_version':1,'id':ident,'status':'prepared','changes':changes,
                 'acceptance':'requires compile, fresh Studio capture and all design gates',
                 'outputs':{relative:{'before':plan['inputs'][relative],'after':sha(data),
                            'bytes':base64.b64encode(data).decode()} for relative,data in staged.items()}}
        if preview:return {k:v for k,v in journal.items() if k!='outputs'}|{'outputs':{
            k:{p:v[p] for p in ('before','after')} for k,v in journal['outputs'].items()}}
        write(journal_path,encode(journal))
    for index,(relative,item) in enumerate(journal['outputs'].items()):
        path=target(root,relative);data=base64.b64decode(item['bytes'])
        actual=sha(path.read_bytes()) if path.exists() else None
        if actual not in (item['before'],item['after']):raise ValueError('repair commit conflict: '+relative)
        if sha(data)!=item['after']:raise ValueError('corrupt repair journal')
        if not path.exists() or sha(path.read_bytes())!=item['after']:write(path,data)
        if after_write:after_write(index)  # Failure injection used by recovery tests.
    journal['status']='applied';write(journal_path,encode(journal))
    write(root/'pending-repair.json',encode({k:v for k,v in journal.items() if k!='outputs'}))
    return {k:v for k,v in journal.items() if k!='outputs'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',required=True);p.add_argument('--plan',required=True)
    p.add_argument('--preview',action='store_true');a=p.parse_args()
    try:print(json.dumps(apply(a.root,a.plan,a.preview),indent=2))
    except (OSError,ValueError,KeyError,TypeError) as error:p.exit(1,str(error)+'\n')


if __name__=='__main__':main()
