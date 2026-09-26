"""Apply the shared quantitative-widget policy to source-linked Sketch regions.

Names only nominate regions for review. They never prove that a chart is an
icon, that an SVG is numerical, or that a bound value reached a native widget.
Explicit semantic_role annotations also cover charts with anonymous layer names.
"""
import copy,hashlib,json,re,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from core.policy import POLICY,POLICY_PATH,sha,data_issues
from core.source_identity import stable_tree_hash


def walk(node):
    yield node
    for child in node.get('children',[]):yield from walk(child)


def source_tree_hash(spec):
    fields=('source_path','object_id','cls','name','symbol_name','x','y','w','h','text')
    rows=[{k:n.get(k) for k in fields} for n in walk(spec)]
    return hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def candidates(spec):
    result=[]
    def visit(n):
        name=n.get('symbol_name') or n.get('name','')
        explicit=n.get('semantic_role') or n.get('semantic',{}).get('role')
        eligible=(bool(n.get('native_widget_id')) and n.get('cls')!='artboard'
                  and not n.get('text') and not n.get('control_part_of'))
        signal=bool(re.search(r'chart|graph|waveform|sparkline|progressbar|\bstatistic\b',name,re.I))
        icon=bool(re.search(r'(^|/)icons?(/|$)',name,re.I))
        background=bool(re.search(r'\((?:Background|Background/Mask)\)$',name,re.I))
        if eligible and (explicit or (signal and not icon and not background)):
            result.append(n)
        # Reviewing a containing card must not hide a quantitative child.
        for c in n.get('children',[]):visit(c)
    visit(spec)
    return result


def source_content_hash(spec):
    """Source review excludes native baseline calculations checked by Studio."""
    spec=copy.deepcopy(spec)
    for node in walk(spec):
        text=node.get('text')
        if isinstance(text,dict):
            for key in ('native_baseline','paragraph_leading_offset'):text.pop(key,None)
            # Original paragraph attributes remain in runs. This convenience
            # value is recomputed by the font/layout importer (including the
            # default leading for blank labels), then gated in native layout.
            if text.get('runs'):text.pop('line_height',None)
            # Row counting can include blank paragraph rows after re-import.
            # Exact exported spans (including their text, positions and styles)
            # remain in this hash; this derived count is checked by layout.
            if text.get('runs') and text.get('native_spans'):
                text.pop('source_rows',None)
    return stable_tree_hash(spec)


def compare(spec,portable,directory,manifest=None,snapshot=None,state=None,request=None,source_baseline=None):
    manifest=manifest or {};entries=manifest.get('elements',[]);errors=[];rows=[]
    review=manifest.get('source_review',{})
    source_match=(review.get('source_tree_sha256')==source_tree_hash(spec) or
                  review.get('stable_source_tree_sha256')==stable_tree_hash(spec))
    reused=False
    if not source_match and source_baseline is not None:
        reused=(review.get('source_tree_sha256')==source_tree_hash(source_baseline) and
                source_baseline.get('reference_sha256')==spec.get('reference_sha256') and
                source_content_hash(source_baseline)==source_content_hash(spec))
        source_match=reused
    if (manifest.get('reference_sha256')!=spec.get('reference_sha256') or
        manifest.get('policy_version')!=POLICY['version'] or
        review.get('verdict')!='complete' or not review.get('reviewer') or not review.get('basis') or
        review.get('method')!='source_image_and_hierarchy' or
        not source_match):
        errors.append('missing or stale whole-source semantic review; inspect anonymous data regions as well as named candidates')
    sources={n.get('native_widget_id'):n for n in walk(spec) if n.get('native_widget_id')}
    decisions={e['id']:e for e in entries}
    if len(decisions)!=len(entries):errors.append('duplicate Sketch semantic decisions')
    required={n['native_widget_id']:n for n in candidates(spec)}
    for ident in decisions:
        if ident not in sources:errors.append(ident+': semantic source is absent')
        else:required[ident]=sources[ident]
    if required and (manifest.get('reference_sha256')!=spec.get('reference_sha256') or
                     manifest.get('policy_version')!=POLICY['version']):
        errors.append('missing or stale Sketch semantic review; classify source data regions before acceptance')
    native={n.get('original_id'):n for n in portable.get('elements',[])}
    widgets={n['id']:n for n in (snapshot or {}).get('widgets',[])}
    for ident,source in required.items():
        entry=decisions.get(ident,{});role=entry.get('role');rule=POLICY['roles'].get(role);issues=[]
        if not rule or role=='unknown' or entry.get('decision')!='reviewed' or not entry.get('basis'):
            issues.append('source region needs an explicit reviewed semantic role')
        if entry.get('source_geometry'):
            geometry=entry['source_geometry']
            path=directory.parent/geometry.get('path','')
            if not path.is_file() or sha(path)!=geometry.get('sha256'):
                issues.append('resolved source curve evidence is missing or changed')
        explicit=source.get('semantic_role') or source.get('semantic',{}).get('role')
        if explicit and role!=explicit:issues.append('mapping contradicts declared source role')
        widget_id=entry.get('widget_id',source.get('native_data_widget_id',ident))
        mapped=native.get(widget_id,{})
        excluded=entry.get('excluded')=='outside_artboard'
        if excluded:
            outside=(source['x']>=spec['w'] or source['y']>=spec['h'] or source['x']+source['w']<=0 or source['y']+source['h']<=0)
            if not outside or mapped:issues.append('outside-artboard exclusion contradicts source geometry or generated widget')
        if not excluded and rule and (rule.get('data') or role=='progress'):
            kind={'StockPlot':'stockplot','Progress':'progress'}.get(mapped.get('kind'),mapped.get('kind','').lower())
            if kind not in rule['kinds']:issues.append('data graphic requires a native numerical widget; SVG/Image/View paint is insufficient')
            if rule.get('data'):issues.extend(data_issues(directory,entry))
            if snapshot is not None:
                actual=widgets.get(mapped.get('id'),{})
                if actual.get('widget_type') not in rule['native_types']:issues.append('Studio did not inspect the declared numerical widget')
                observed=(state or {}).get('elements',{}).get(widget_id,{})
                if (not request or (state or {}).get('nonce')!=request.get('nonce') or
                    (state or {}).get('build_id')!=(snapshot or {}).get('build_id') or observed.get('native_id')!=mapped.get('id')):
                    issues.append('missing current Studio-bound numerical state')
                elif rule.get('data'):
                    from core.policy import runtime_data_issues
                    issues.extend(runtime_data_issues(directory,entry,observed))
                elif role=='progress':
                    expected=entry.get('progress',{}).get('value')
                    if type(expected) not in (int,float) or not 0<=expected<=1:
                        issues.append('missing normalized source progress value')
                    elif any(type(observed.get(key)) not in (int,float) or abs(observed[key]-expected)>1e-6 for key in ('value','painted_value')):
                        issues.append('native progress value or painted fill differs from source')
        row={'source_id':source.get('object_id'),'widget_id':ident,'name':source.get('name'),
             'role':role,'issues':issues,'repair':(rule or {}).get('repair','Classify this source region, then map a native widget and bind its data.')}
        rows.append(row);errors.extend(ident+': '+s for s in issues)
    return {'pass':not errors,'errors':errors,'elements':rows,'policy_version':POLICY['version'],
            'source_review_reuse':'hash-verified original review; source content unchanged, native baseline metadata excluded' if reused else None,
            'policy_sha256':sha(POLICY_PATH),'scope':'Whole-source review plus named candidates and explicit quantitative annotations.'}


def evaluate(kit,name,portable,snapshot=None):
    root=kit['specs_dir'].parent;path=root/'semantics'/f'{name}.json'
    spec=json.loads((kit['specs_dir']/f'{name}.json').read_text())
    manifest=json.loads(path.read_text()) if path.exists() else None
    out=kit['splash_makepad_dir']
    def read(suffix):
        p=out/f'{name}.{suffix}.json';return json.loads(p.read_text()) if p.exists() else {}
    baseline=root/'semantic-source'/f'{name}.json'
    report=compare(spec,portable,path.parent,manifest,snapshot,read('semantic-baseline'),read('capture').get('request'),
                   json.loads(baseline.read_text()) if baseline.exists() else None)
    if snapshot is not None and any(e.get('role')=='progress' for e in (manifest or {}).get('elements',[])):
        probes=read('progress-interactions')
        by_id={p['id']:p for p in probes.get('checks',[])}
        for entry in manifest['elements']:
            if entry.get('role')!='progress':continue
            ident=entry.get('widget_id',entry['id']);probe=by_id.get(ident,{})
            before=probe.get('before',{});after=probe.get('after',{})
            if (probes.get('pass') is not True or probes.get('build_id')!=snapshot.get('build_id') or
                probe.get('status')!='pass' or before.get('value')==after.get('value') or
                type(after.get('value')) not in (float,int) or abs(after.get('painted_value',-1)-after['value'])>1e-6):
                report['errors'].append(ident+': missing current value-and-paint progress probe');report['pass']=False
    if kit.get('targets_dir'):
        target=kit['targets_dir']/f'{name}.png'
        if not target.is_file() or sha(target)!=spec.get('reference_sha256'):
            report['errors'].append('source reference pixels changed since import; reimport and review the source')
            report['pass']=False
    return report
