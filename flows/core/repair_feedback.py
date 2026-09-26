"""Carry measured differences and screenshot findings into the next repair run."""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # flows/, for `core`
import hashlib
import json
import pathlib

from core import gate_visual
from core import composition
from core import gate_composition
from core import acceptance
from core import gate_kit


def collect(kit):
    out = kit['splash_makepad_dir']
    out.mkdir(parents=True, exist_ok=True)
    implementation = composition.write(kit)
    run_path = out/'pipeline-run.json'
    run = json.loads(run_path.read_text()) if run_path.exists() else {}
    run_errors = run.get('errors', [])
    if run.get('status') in ('running', 'failed', 'interrupted') and not run_errors:
        run_errors = [f"latest pipeline run is {run['status']}; rerun the validation stages"]
        run = {**run, 'errors': run_errors}
    visual = {r['screen']:r for r in gate_visual.evaluate(kit,'splash_makepad')}
    policy = gate_composition.evaluate(kit)
    compositions = {r['screen']: r for r in policy['screens']}
    kits = {r['screen']:r for r in gate_kit.evaluate(kit)['screens']}
    screens = []
    for name in kit['screens']:
        path = out/f'{name}.structure.json'
        try:
            structure = json.loads(path.read_text()) if path.exists() else {}
        except (OSError, ValueError):
            structure = {'pass': False, 'inspection_errors': ['unreadable structural review']}
        failures = [r for r in structure.get('elements',[]) if r.get('issues')]
        relations = [r for r in structure.get('relations',[]) if r.get('issues')]
        evidence = [out/f'{name}.{suffix}' for suffix in
                    ('png','capture.json','widgets.json','snapshot.json','queries.json',
                     'layout.json','structure.json','composition.json')]
        screens.append({'screen':name,
            'needs_repair':bool(run_errors) or not (structure.get('pass') and visual[name]['pass'])
                           or compositions[name]['pass'] is False or kits.get(name,{}).get('pass') is False,
            'pipeline_errors':run_errors,
            'source_spec':str(kit['specs_dir']/f'{name}.json'),
            'design_screenshot':str(kit['targets_dir']/f'{name}.png'),
            'implementation_screenshot':str(out/f'{name}.png'),
            'tolerances':structure.get('tolerances'),
            'inspection_errors':structure.get('inspection_errors', ['missing structural review']),
            'element_differences':failures,'relation_differences':relations,
            'composition': compositions[name],
            'kit': kits.get(name,{}),
            'semantic_interactions': json.loads((out/f'{name}.semantic-interactions.json').read_text())
                if (out/f'{name}.semantic-interactions.json').exists() else None,
            'visual':visual[name],
            'evidence_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in evidence if p.exists()}})
    scope = acceptance.write(kit, screens, run)
    recovery={}
    for filename in ('capture-recovery.json','capture-preflight.json'):
        evidence=out/filename
        if evidence.exists():
            try:recovery[filename]={'report':json.loads(evidence.read_text()),'sha256':hashlib.sha256(evidence.read_bytes()).hexdigest()}
            except (OSError,ValueError):recovery[filename]={'error':'unreadable capture recovery evidence'}
    path = out/'repair-feedback.json'
    path.write_text(json.dumps({'kit':kit['name'],'composition':implementation,
                               'acceptance':scope, 'pipeline_run':run,'capture_recovery':recovery,'screens':screens},indent=2)+'\n')
    return path
