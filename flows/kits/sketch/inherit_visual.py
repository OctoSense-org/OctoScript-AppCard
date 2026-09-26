#!/usr/bin/env python3
"""Reuse a screenshot review only for an identical, hash-bound screenshot pair.

This does not reuse structural evidence, assign scores, or accept changed pixels.
The current capture and inspection must still pass the regular freshness gate.
"""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # lab/, for `core`
import argparse
import hashlib
import json
import shutil

from core import gate_visual
from core import kitconf
from core import visual_evidence
from core.judge_shots import PROMPT


def inherit(kit):
    previous=kitconf.load(kit['source_native_kit'])
    old_path=kitconf.HERE/previous['verdicts']['splash_makepad']
    old_rows={r['screen']:r for r in map(json.loads,old_path.read_text().splitlines())} if old_path.exists() else {}
    destination=kitconf.HERE/kit['verdicts']['splash_makepad']
    rows={r['screen']:r for r in map(json.loads,destination.read_text().splitlines())} if destination.exists() else {}
    receipts=[]
    for name in kit['screens']:
        source=kit['targets_dir']/f'{name}.png';capture=kit['splash_makepad_dir']/f'{name}.png'
        if not source.exists() or not capture.exists():continue
        target,actual=source.read_bytes(),capture.read_bytes()
        row=old_rows.get(name,{})
        inputs=hashlib.sha256(target+actual+PROMPT.encode()).hexdigest()
        if row.get('inputs')!=inputs:continue
        result=gate_visual.review_result(target,actual,row,kit.get('visual_min_score',9))
        followup=previous['splash_makepad_dir']/f'{name}.visual-followup.json'
        inherited_followup=False
        if followup.exists():
            extra=json.loads(followup.read_text())
            if not visual_evidence.validate_followup(extra,row,inputs):
                result=gate_visual.review_result(target,actual,extra,kit.get('visual_min_score',9))
                if result['pass']:
                    shutil.copyfile(followup,kit['splash_makepad_dir']/followup.name)
                    inherited_followup=True
        if not result['pass']:continue
        rows[name]=row
        receipts.append({'screen':name,'inputs':inputs,'original_verdicts':str(old_path),
                         'original_row_sha256':visual_evidence.row_digest(row),
                         'followup':inherited_followup,'reason':'identical reviewed screenshot pair'})
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(''.join(json.dumps(rows[k],ensure_ascii=False)+'\n' for k in sorted(rows)))
    (kit['splash_makepad_dir']/'inherited-visual-reviews.json').write_text(json.dumps(receipts,indent=2)+'\n')
    print(f'{kit["name"]}: {len(receipts)} identical screenshot reviews reused; changed/unreviewed pairs require review')
    return receipts


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--kit',required=True)
    inherit(kitconf.load(parser.parse_args().kit))
