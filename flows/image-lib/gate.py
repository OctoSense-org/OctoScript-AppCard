#!/usr/bin/env python3
"""Fail closed on host-only, stale or incomplete image-to-widget evidence."""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # flows/, for `core`
import argparse,json,sys
from pathlib import Path
import numpy as np
from PIL import Image
from catalogue import HERE,walk
from compile import digest,ROOT
from observe import ocr,ocr_label,match_text,ink_box,norm
from semantics import evaluate as evaluate_semantics
sys.path.insert(0,str(HERE.parent))
from core.gate_structure import parse_dump
sys.path.pop(0)

TOL={'native_geometry_px':1.0,'image_position_px':3.0,'image_dimension_px':3.0,
     'text_ink_position_px':3.0,'text_ink_dimension_px':3.0,'clipping_px':1.0,'color_channel':16}

def evaluate(directory,round_dir):
    directory=Path(directory);round_dir=Path(round_dir)
    def read(name):return json.loads((round_dir/name).read_text())
    mapping=read('mapping.json')['elements'];proof=read('provenance.json');errors=[];differences=[]
    required=('native.png','native.json','tree.json','snapshot.json','queries.json','layout.json',
              'screenshot.json','mapping.json','page.card','page.data.json','contract.json','interactions.json')
    errors.extend('missing evidence receipt: '+name for name in required if name not in proof.get('files',{}))
    runtime=proof.get('runtime_sources',{})
    if not runtime:errors.append('missing native runtime source receipt; recapture')
    for name,expected in runtime.items():
        path=ROOT/name
        if not path.is_file() or digest(path.read_bytes())!=expected:
            errors.append('native runtime changed since capture: '+name)
    current_model=directory/'mapped.json';captured_model=round_dir/'mapped.json'
    if current_model.exists() and captured_model.exists() and digest(current_model.read_bytes())!=digest(captured_model.read_bytes()):
        errors.append('mapped model changed since capture; recapture the current composition')
    for name in ('page.card','page.data.json','mapping.json','contract.json','kit/native/light/kit.json'):
        current=directory/name;captured=round_dir/name
        if current.exists() and (not captured.exists() or digest(current.read_bytes())!=digest(captured.read_bytes())):
            errors.append('compiled input changed since capture: '+name)
    for name,sha in proof['files'].items():
        path=round_dir/name
        if not path.is_file() or digest(path.read_bytes())!=sha:errors.append('stale evidence: '+name)
    for name in ('tree.json','snapshot.json','screenshot.json'):
        if read(name).get('build_id')!=proof['build_id']:errors.append('mismatched build: '+name)
    if read('layout.json').get('nonce')!=proof['nonce']:errors.append('stale native layout nonce')
    tree=parse_dump(read('tree.json').get('dump',''));trees={n['id']:n for n in tree}
    snaps={n['id']:n for n in read('snapshot.json').get('widgets',[])}
    layouts={n['id']:n for n in read('layout.json').get('elements',[])};queries=read('queries.json')
    native_ids={n['native_id'] for n in mapping}
    if len(native_ids & trees.keys())<2 or len(native_ids & snaps.keys())<2:
        errors.append('host-only inspection: inner generated widgets are missing')
    ids={n['source_id']:n for n in mapping}
    for n in mapping:
        id=n['native_id'];t=trees.get(id);s=snaps.get(id);l=layouts.get(id);fails=[]
        if not t or not s or not l:fails.append('missing native element')
        else:
            actual=l['bounds'];delta=[round(a-b,3) for a,b in zip(actual,n['bounds'])]
            if max(map(abs,delta))>TOL['native_geometry_px']:fails.append('native bounds differ from compiled mapping')
            if not s.get('visible'):fails.append('native widget is hidden')
            if max(abs(a-b) for a,b in zip(actual,l['clipped_bounds']))>TOL['clipping_px']:fails.append('native bounds clipped')
            expected_parent=ids[n['parent']]['native_id'] if n['parent'] else None
            if expected_parent and t['parent']!=expected_parent:fails.append('wrong hierarchy parent')
            if n['text'] is not None and s.get('text')!=n['text']:fails.append('native text mismatch')
            if n['enabled'] is not None and bool(s.get('enabled'))!=bool(n['enabled']):fails.append('native enabled-state mismatch')
            types={'text':['Label'],'button':['Button'],'svg':['Svg']}
            if n['kind'] in types and t['type'] not in types[n['kind']]:fails.append('wrong native widget type')
            q=queries.get(id,{})
            if q.get('build_id')!=proof['build_id'] or q.get('query')!='id:'+id or len(q.get('rects',[]))!=1:fails.append('missing or ambiguous WidgetQuery')
            if l.get('vector_ready') is False:fails.append('SVG not loaded')
            text=l.get('text_layout')
            if text and n['kind']=='text':
                x,y,w,h=actual;tx,ty,tw,th=text
                if tx<x-1 or ty<y-1 or tx+tw>x+w+1 or ty+th>y+h+1:fails.append('text layout overflows its Label')
        differences.append({'id':n['source_id'],'native_id':id,'expected_bounds':n['bounds'],
            'actual_bounds':l['bounds'] if l else None,'parent':t.get('parent') if t else None,
            'widget_type':t.get('type') if t else None,'visible':s.get('visible') if s else None,
            'text':s.get('text') if s else None,'enabled':s.get('enabled') if s else None,'issues':fails})
        errors.extend(n['source_id']+': '+f for f in fails)
    interactions=read('interactions.json')
    if not interactions['pass']:errors.append('native control activation failed')
    native_pass=not errors
    semantic=evaluate_semantics(directory,round_dir)
    image_errors=[];text_diffs=[];geometry_diffs=[];relations=[];observations_path=directory/'observations.json'
    if (round_dir/'observations.json').exists():observations_path=round_dir/'observations.json'
    visual={'status':'awaiting reference image'}
    if observations_path.exists() and (directory/'reference.png').exists():
        observed=json.loads(observations_path.read_text());sha=digest((directory/'reference.png').read_bytes())
        if observed['reference_sha256']!=sha or proof['reference_sha256']!=sha:image_errors.append('stale reference image')
        if not observed['opaque']:image_errors.append('reference contains unintended transparency')
        if observed['aspect_error']>.005:image_errors.append('reference artboard aspect differs by more than 0.5%')
        contract=read('contract.json');nodes=list(walk(contract['tree']))
        shot_ocr=ocr(round_dir/'native.png');pixels=np.asarray(Image.open(round_dir/'native.png').convert('RGB'))
        matched,used=match_text(nodes,shot_ocr['observations'],shot_ocr['width']/406,shot_ocr['height']/776)
        src_nodes={n['id']:n for n in nodes}
        for row in observed['text']:
            id=row['id'];match=matched.get(id);issues=[];actual=None;delta=None;ink=None
            actual_ocr=shot_ocr['observations'][match[0]] if match else None
            expected_copy=norm(row['expected_text']).replace(' ','')
            if id in ids and row.get('measurement')!='reviewed glyph region' and (
                    actual_ocr is None or norm(actual_ocr['text']).replace(' ','')!=expected_copy):
                bounds=layouts.get(ids[id]['native_id'],{}).get('bounds')
                local=[o for o in ocr_label(round_dir/'native.png',bounds) if
                       norm(o['text']).replace(' ','')==expected_copy] if bounds else []
                if len(local)==1:actual_ocr=local[0]
            if id not in ids:issues.append('reference text element missing from captured composition')
            elif row['status']!='observed':issues.append('reference text missing or OCR unresolved')
            elif row.get('measurement')=='reviewed glyph region':
                label_bounds=layouts.get(ids[id]['native_id'],{}).get('bounds')
                if label_bounds:
                    scale=[pixels.shape[1]/406,pixels.shape[0]/776]
                    roi=[v*scale[j%2] for j,v in enumerate(label_bounds)]
                    actual,ink=ink_box(pixels,roi,[406,776],row.get('light_foreground',False),clip=label_bounds,
                                        min_component_height=label_bounds[3]*.5 if row['id'].endswith('_number') else None)
                    delta=[round(a-b,3) for a,b in zip(actual,row['ink_bounds'])]
                    if max(map(abs,delta[:2]))>TOL['text_ink_position_px']:issues.append('text ink position')
                    if max(map(abs,delta[2:]))>TOL['text_ink_dimension_px']:issues.append('text ink dimensions')
                    if ink and row['ink_color'] and max(abs(a-b) for a,b in zip(ink,row['ink_color']))>TOL['color_channel']:issues.append('text color')
                else:issues.append('missing native glyph group Label')
            elif actual_ocr is None:issues.append('native screenshot text missing or OCR unresolved')
            else:
                # Vision may concatenate adjacent words. Exact native strings
                # are checked independently through WidgetSnapshot above.
                if norm(actual_ocr['text']).replace(' ','')!=norm(row['expected_text']).replace(' ',''):issues.append('native OCR text differs')
                if norm(row['ocr_text']).replace(' ','')!=norm(row['expected_text']).replace(' ',''):issues.append('reference OCR text differs')
                light=row.get('light_foreground',False)
                # Tight leading can put a previous line's descender in the OCR
                # region. The inspected Label bounds identify this text's ROI.
                label_bounds=layouts.get(ids[id]['native_id'],{}).get('bounds')
                actual,ink=ink_box(pixels,actual_ocr['bounds'],[406,776],light,clip=label_bounds)
                delta=[round(a-b,3) for a,b in zip(actual,row['ink_bounds'])]
                if max(map(abs,delta[:2]))>TOL['text_ink_position_px']:issues.append('text ink position')
                if max(map(abs,delta[2:]))>TOL['text_ink_dimension_px']:issues.append('text ink dimensions')
                if ink and row['ink_color'] and max(abs(a-b) for a,b in zip(ink,row['ink_color']))>TOL['color_channel']:issues.append('text color')
            text_diffs.append({'id':id,'reference':row.get('ink_bounds'),'native':actual,'delta':delta,'reference_color':row.get('ink_color'),'native_color':ink,'issues':issues})
            image_errors.extend(id+': '+issue for issue in issues)
        annotated={a['id'] for a in observed['non_text']}
        required_nontext={n['source_id'] for n in mapping if n['kind']!='text'}
        missing=sorted(required_nontext-annotated)
        if missing:image_errors.append('unmeasured non-text elements: '+', '.join(missing))
        for a in observed['non_text']:
            if 'unresolved' in a.get('method','') or 'visual annotation needed' in a.get('method',''):
                image_errors.append(a['id']+': source geometry still needs measurement')
            n=ids.get(a['id']);l=layouts.get(n['native_id']) if n else None
            delta=[round(v-e,3) for v,e in zip(l['bounds'],a['bounds'])] if l else None
            issues=[]
            if not delta or max(map(abs,delta))>TOL['image_position_px']:issues.append('observed image bounds differ')
            geometry_diffs.append({'id':a['id'],'reference':a['bounds'],'native':l['bounds'] if l else None,'delta':delta,'issues':issues})
            image_errors.extend(a['id']+': '+v for v in issues)
        # Compare spacing and left alignment of consecutive semantic siblings.
        by_parent={}
        for a in observed['non_text']:
            n=ids.get(a['id'])
            if n:by_parent.setdefault(n['parent'],[]).append(a)
        for parent,rows in by_parent.items():
            rows=sorted(rows,key=lambda a:(a['bounds'][1],a['bounds'][0]))
            for a,b in zip(rows,rows[1:]):
                aa=layouts.get(ids[a['id']]['native_id']);bb=layouts.get(ids[b['id']]['native_id'])
                if not aa or not bb:continue
                def gap(r,s):return s[1]-r[1]-r[3]
                expected=gap(a['bounds'],b['bounds']);actual=gap(aa['bounds'],bb['bounds'])
                relations.append({'first':a['id'],'second':b['id'],'vertical_gap_reference':expected,'vertical_gap_native':actual,
                                  'left_alignment_delta':(bb['bounds'][0]-aa['bounds'][0])-(b['bounds'][0]-a['bounds'][0])})
        # Runtime state alone cannot prove the fill was painted. Verify value
        # graphics in the actual baseline and changed Studio screenshots.
        current_nodes={n['id']:n for n in walk(read('mapped.json')['tree'])}
        baseline=read('semantic-baseline.json') if (round_dir/'semantic-baseline.json').exists() else {}
        semantic_entries=read('semantic-map.json')['elements'] if (round_dir/'semantic-map.json').exists() else []
        for entry in semantic_entries:
            if entry['role']!='progress':continue
            n=current_nodes[entry['id']];fill=np.array([(n['color']>>shift)&255 for shift in (16,8,0)])
            def painted_width(path):
                im=np.asarray(Image.open(path).convert('RGB')).astype(float);sx,sy=im.shape[1]/406,im.shape[0]/776
                x,y,w,h=[n[k] for k in ('x','y','w','h')]
                row=im[round((y+h/2)*sy),round(x*sx):round((x+w)*sx)]
                hit=np.where(np.max(abs(row-fill),axis=1)<30)[0]
                return (hit[-1]+1)/sx if len(hit) else 0
            expected=baseline.get('elements',{}).get(n['id'],{}).get('value',n['value'])*n['w']
            actual=painted_width(round_dir/'native.png')
            if abs(actual-expected)>TOL['image_dimension_px']:image_errors.append(n['id']+': painted fill differs from native value')
            changed=round_dir/(n['id']+'-changed.png')
            if not changed.exists():image_errors.append(n['id']+': missing changed-value screenshot')
            elif abs(painted_width(changed)-entry['behavior']['probe_value']*n['w'])>TOL['image_dimension_px']:
                image_errors.append(n['id']+': changed value did not repaint the progress fill')
        if observed['unmapped_ocr']:image_errors.append(f'{len(observed["unmapped_ocr"])} extra reference text observations need classification')
        a=np.asarray(Image.open(directory/'reference.png').convert('RGB').resize((406,776)),dtype=float)
        b=np.asarray(Image.open(round_dir/'native.png').convert('RGB').resize((406,776)),dtype=float)
        visual={'status':'human review required','rgb_mae':round(float(abs(a-b).mean()),3),
                'note':'Diagnostic only. Typography, graphics, color and effects still need side-by-side review.'}
    else:image_errors.append('missing observed reference measurements')
    visual_receipt=directory/'visual-review.json'
    visual_pass=False;review={};current=False
    if visual_receipt.exists():
        review=json.loads(visual_receipt.read_text())
        current=(review.get('reference_sha256')==proof['reference_sha256'] and
                 review.get('native_sha256')==digest((round_dir/'native.png').read_bytes()))
        complete=bool(review.get('reviewer')) and all(k in review.get('criteria',{}) for k in ('typography','colors','imagery','effects'))
        visual_pass=current and complete and review.get('verdict')=='pass' and all(review['criteria'][k] is True for k in ('typography','colors','imagery','effects'))
        visual.update(status=review.get('verdict') if current and complete else 'stale or incomplete visual review',
                      review=review,receipt_current=current)
    report={'schema_version':1,'id':directory.name,'round':round_dir.name,'build_id':proof['build_id'],
        'tolerances':TOL,'native_structure_pass':native_pass,'image_structure_pass':not image_errors,
        'semantic_mapping_pass':semantic['pass'],'semantic_errors':semantic['errors'],'semantic_mapping':semantic,
        'accepted':native_pass and semantic['pass'] and not image_errors and visual_pass,'visual_review':visual,'native_errors':errors,'image_errors':image_errors,
        'elements':differences,'text_differences':text_diffs,'geometry_differences':geometry_diffs,'relations':relations,
        'interaction_scope':'native activation and declared fixture state/data probes; no live feeds or complete app navigation'}
    (round_dir/'gate.json').write_text(json.dumps(report,indent=2)+'\n')
    repair={'id':directory.name,'reference_sha256':proof['reference_sha256'],'round':round_dir.name,
            'native_findings':errors,'image_findings':image_errors,'text_differences':text_diffs,
            'visual_findings':review.get('findings',[]) if current else [],
            'visual_review_current':current,'visual_verdict':review.get('verdict') if current else None,
            'semantic_findings':semantic['errors'],'semantic_repairs':[e for e in semantic['elements'] if e['issues']],
            'rules':['Preserve real native Labels and controls.','Never replace a page with its screenshot.',
                     'Follow MAPPING-RULES.md: data graphics require native data-bound widgets; artwork requires asset provenance.',
                     'Repair mapped.json or native vector assets; recapture through Studio.','Do not widen tolerances to manufacture a pass.']}
    (round_dir/'repair.json').write_text(json.dumps(repair,indent=2)+'\n')
    pending=directory/'pending-repair.json'
    if report['accepted'] and pending.exists():
        handoff=json.loads(pending.read_text())
        handoff.update(status='verified',verification={'round':round_dir.name,'accepted':True,
            'reference_sha256':proof['reference_sha256'],'native_sha256':digest((round_dir/'native.png').read_bytes())})
        pending.write_text(json.dumps(handoff,indent=2)+'\n')
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('design',nargs='+');a=p.parse_args()
    failed=False
    for id in a.design:
        directory=HERE/id;latest=json.loads((directory/'latest.json').read_text());r=evaluate(directory,directory/'rounds'/latest['round'])
        print(json.dumps({k:r[k] for k in ('id','round','native_structure_pass','image_structure_pass','visual_review')}))
        failed |= not r['accepted']
    raise SystemExit(1 if failed else 0)
