#!/usr/bin/env python3
"""Publish reference/native comparisons and preserve review choices locally."""
import json,shutil
from catalogue import HERE
from compile import GALLERY
from semantics import audit

def publish():
    entries=json.loads((HERE/'catalogue.json').read_text())
    for name in ('MAPPING-RULES.md','mapping-rules.json'):
        shutil.copy2(HERE/name,GALLERY/name)
    for row in entries:
        d=HERE/row['id'];out=GALLERY/row['id'];out.mkdir(parents=True,exist_ok=True)
        for name in ['reference.png','image-prompt.md','original-image-prompt.md','generation.json','contract.json','page.card','page.data.json','mapping.json','observations.json','annotations.json','text-annotations.json','ocr-classifications.json','font-fit.json','visual-review.json']:
            if (d/name).exists():shutil.copy2(d/name,out/name)
        shutil.copytree(d/'kit',out/'kit',dirs_exist_ok=True)
        row['reference']=(d/'reference.png').exists();row['native']=False
        if (d/'latest.json').exists():
            latest=json.loads((d/'latest.json').read_text());r=d/'rounds'/latest['round']
            row.update(round=latest['round'],build_id=latest['build_id'])
            for name in ['native.png','gate.json','repair.json','tree.json','snapshot.json','queries.json','layout.json','interactions.json','semantic-baseline.json','semantic-state.json','semantic-interactions.json','provenance.json']:
                if (r/name).exists():shutil.copy2(r/name,out/name)
            for path in r.glob('*-changed.*'):shutil.copy2(path,out/path.name)
            row['native']=(r/'native.png').exists()
            if (r/'gate.json').exists():
                g=json.loads((r/'gate.json').read_text());row['native_pass']=g['native_structure_pass'];row['image_pass']=g['image_structure_pass']
                row['native_issues']=g['native_errors'];row['image_issues']=g['image_errors'];row['nodes']=len(g['elements'])
                row['runtime_semantic_pass']=g['semantic_mapping_pass'];row['runtime_semantic_issues']=g['semantic_errors']
                row['visual']=g['visual_review'];row['accepted']=g['accepted']
        semantic=audit(d)
        row['semantic_pass']=semantic['pass'] and row.get('runtime_semantic_pass',False)
        row['semantic_issues']=semantic['errors']+row.get('runtime_semantic_issues',[])
        row['accepted']=row.get('accepted',False) and semantic['pass']
        run_path=d/'pipeline-run.json'
        if run_path.exists():
            run=json.loads(run_path.read_text());row['pipeline_status']=run['status']
            if run['status'] in ('running','failed','interrupted'):row['accepted']=False
            shutil.copy2(run_path,out/run_path.name)
        for name in ('semantic-map.json','semantic-audit.json','semantic-repair.json','conversion-brief.md'):
            if (d/name).exists():shutil.copy2(d/name,out/name)
        for entry in json.loads((d/'semantic-map.json').read_text())['elements']:
            for key in ('asset','data'):
                relative=entry.get(key,{}).get('path')
                if relative:
                    target=out/relative;target.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copy2(d/relative,target)
        doc=json.loads((d/'contract.json').read_text());row['palette']=doc['palette']
        generation=json.loads((d/'generation.json').read_text()) if (d/'generation.json').exists() else {}
        row['prompt_file']=generation.get('prompt','image-prompt.md')
    (GALLERY/'catalogue.json').write_text(json.dumps(entries,indent=2)+'\n')
    template=(HERE/'gallery.html').read_text()
    (GALLERY/'index.html').write_text(template.replace('/*CATALOGUE*/[]',json.dumps(entries).replace('</','<\\/')))
    summary={'designs':len(entries),'references':sum(r['reference'] for r in entries),'native_captures':sum(r['native'] for r in entries),
             'native_pass':sum(r.get('native_pass',False) for r in entries),'image_structure_pass':sum(r.get('image_pass',False) for r in entries),
             'semantic_mapping_pass':sum(r.get('semantic_pass',False) for r in entries),
             'visual_qa_pass':sum(r.get('visual',{}).get('status')=='pass' and r.get('visual',{}).get('receipt_current',False) for r in entries),
             'accepted':sum(r.get('accepted',False) for r in entries),'url':'http://127.0.0.1:8170/ux-images/'}
    (HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    for name in ('VISUAL-QA.md','validation.json','summary.json','qa-work/final-build-comparison.json','qa-work/gallery-qa.json'):
        if (HERE/name).exists():
            target=GALLERY/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(HERE/name,target)
    print(json.dumps(summary));return summary

if __name__=='__main__':publish()
