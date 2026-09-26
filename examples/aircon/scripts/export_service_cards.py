#!/usr/bin/env python3
"""Export each service surface as a standalone native L0/kit card."""
from pathlib import Path
import copy, hashlib, json, shutil, sys
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parents[1] / 'lab/image-to-appcard'))
from catalogue import walk
import compile as compiler
compiler.GALLERY = ROOT / "artwork"
from compile import compile_page

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

def export():
    catalogue=[]
    for frame in range(3,13):
        src=ROOT/'cards'/f'aircon-{frame:02d}'
        model=json.loads((src/'mapped.json').read_text())
        contract=json.loads((src/'contract.json').read_text())
        semantics=json.loads((src/'semantic-map.json').read_text())
        lookup={n['id']:n for n in walk(model['tree'])}
        declared=json.loads((src/'source-measurements.json').read_text())['spec']['cards']
        for id,_ in declared:
            owner='calendar' if id.startswith('calendar') else 'payment' if id.startswith('payment') else 'logistics' if id.startswith('logistics') else 'shopping' if id.startswith('order') else 'installation'
            name=f'{id}-{frame:02d}';d=ROOT/'service-cards'/owner/name
            d.mkdir(parents=True,exist_ok=True)
            tree=copy.deepcopy(lookup[id]);x,y,w,h=[tree[k] for k in 'xywh']
            px,py,pw,ph=[round(v*2) for v in (x,y,w,h)]
            Image.open(src/'reference.png').crop((px,py,px+pw,py+ph)).save(d/'reference.png')
            for n in walk(tree):n['x']-=x;n['y']-=y
            ids={n['id'] for n in walk(tree)}
            doc={**contract,'id':name,'title':contract['title']+' · '+owner,'artboard':[w,h],'tree':tree,'standalone_service_card':True}
            write(d/'contract.json',doc)
            write(d/'mapped.json',{'schema_version':1,'reference_sha256':sha(d/'reference.png'),'tree':tree,'changes':[{'source':f'cards/{src.name}/mapped.json','source_sha256':sha(src/'mapped.json'),'operation':'Extract service-owned native subtree and translate origin','source_root':id,'translation':[-x,-y]}]})
            manifest={**semantics,'contract_sha256':sha(d/'contract.json'),'reference_sha256':sha(d/'reference.png'),'elements':[copy.deepcopy(e) for e in semantics['elements'] if e['id'] in ids]}
            for entry in manifest['elements']:
                a=entry.get('asset')
                if not a:continue
                target=d/a['path'];target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src/a['path'],target)
                a['reference_sha256']=manifest['reference_sha256']
                if a['method']=='source_crop':a['crop_pixels'][0]-=px;a['crop_pixels'][1]-=py
            write(d/'semantic-map.json',manifest)
            shutil.copy2(src/'image-prompt.md',d/'image-prompt.md')
            write(d/'generation.json',{'provider':'OpenAI Image API','model':'gpt-image-2','derived_from':f'cards/{src.name}/reference.png','derived_from_sha256':sha(src/'reference.png'),'source_region_pixels':[px,py,pw,ph],'image_sha256':sha(d/'reference.png'),'original_prompt_sha256':sha(d/'image-prompt.md'),'note':'Crop of one atlas-generated service surface; no new image generation'})
            actions=json.loads((src/'service-actions.json').read_text())
            actions['controls']={key:value for key,value in actions['controls'].items() if key in ids}
            write(d/'service-actions.json',actions)
            result=compile_page(d)
            catalogue.append({'id':name,'owner_app':owner,'source_frame':frame,'source_surface':id,'folder':str(d.relative_to(ROOT)),'artboard':[w,h],**result})
    write(ROOT/'service-cards/catalogue.json',{'schema_version':1,'kind':'native-service-appcards','cards':catalogue,'validation':'Native subtrees also present in complete scene captures; standalone runtime geometry is declared, not a claim of responsive reflow'})
    print(json.dumps({'standalone_service_cards':len(catalogue),'owners':sorted({e['owner_app'] for e in catalogue})}),flush=True)

if __name__=='__main__':export()
