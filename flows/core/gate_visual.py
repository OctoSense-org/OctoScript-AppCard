#!/usr/bin/env python3
"""Require a current, accepted screenshot review at the kit's parity threshold."""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # flows/, for `core`
import argparse
import hashlib
import json

from core import kitconf
from core.judge_shots import PROMPT


def review_result(target, capture, row, minimum):
    inputs = hashlib.sha256(target + capture + PROMPT.encode()).hexdigest()
    errors = []
    if row.get('inputs') != inputs:
        errors.append('missing or stale screenshot review')
    if row.get('verdict') != 'accept':
        errors.append('visual reviewer did not accept this screen')
    score = row.get('design_match')
    if type(score) is not int or score < minimum:
        errors.append(f'visual score below {minimum}/10')
    return {'pass':not errors,'errors':errors,'minimum_score':minimum,'review':row}


def evaluate(kit, rail):
    if not kit['screens']:
        raise ValueError('visual gate requires at least one configured screen')
    verdicts = kitconf.HERE / kit['verdicts'][rail]
    rows = {r['screen']:r for r in map(json.loads,verdicts.read_text().splitlines())} if verdicts.exists() else {}
    results = []
    for name in kit['screens']:
        try:
            target=(kit['targets_dir']/f'{name}.png').read_bytes()
            capture=(kit[f'{rail}_dir']/f'{name}.png').read_bytes()
            original=rows.get(name,{})
            r = review_result(target,capture,original,kit.get('visual_min_score',9))
            followup=kit[f'{rail}_dir']/f'{name}.visual-followup.json'
            if followup.exists():
                from core import visual_evidence
                review=json.loads(followup.read_text())
                inputs=hashlib.sha256(target+capture+PROMPT.encode()).hexdigest()
                errors=visual_evidence.validate_followup(review,original,inputs)
                if not errors:
                    r=review_result(target,capture,review,kit.get('visual_min_score',9))
                    r.update(original_review=original,review_method=review['method'])
                else:r['follow_up_errors']=errors
            if rail == 'splash_makepad':
                from core import render_splash_makepad as native
                card,data,spec = native.selected_inputs(kit,name)
                expected = native.fingerprint([*native.shared_inputs(kit),card,data,spec])
                meta = json.loads((kit[f'{rail}_dir']/f'{name}.capture.json').read_text())
                r['capture_current']=native.fresh(meta,expected,kit[f'{rail}_dir']/f'{name}.png')
                if not r['capture_current']:
                    r['pass'] = False
                    r['errors'].append('native capture or inspection is stale; rerender before visual acceptance')
        except (OSError,ValueError,KeyError) as e:
            r = {'pass':False,'errors':[str(e)]}
        if rail=='splash_makepad':r.setdefault('capture_current',False)
        r['screen'] = name
        results.append(r)
    out = kit[f'{rail}_dir'] / 'visual-gate.json'
    out.write_text(json.dumps({'pass':all(r['pass'] for r in results),'screens':results},indent=2)+'\n')
    return results


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--kit',required=True)
    p.add_argument('--rail',default='splash_makepad')
    args=p.parse_args()
    results=evaluate(kitconf.load(args.kit),args.rail)
    for r in results:
        print(f"{r['screen']}: visual {'PASS' if r['pass'] else 'FAIL'} {'; '.join(r['errors'])}")
    if not all(r['pass'] for r in results): raise SystemExit(1)


if __name__=='__main__': main()
