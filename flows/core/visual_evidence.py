"""Reconsider a disputed visual finding with hashed, measurable pixel evidence.

The first verdict remains unchanged. A follow-up still reviews the full pair,
uses the same acceptance threshold, and cannot bypass native structural checks.
"""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # flows/, for `core`
import argparse
import hashlib
import io
import json
import pathlib

import numpy as np
from PIL import Image, ImageDraw
from core import judge_shots
from core import kitconf
from core import llm


PROMPT = (
    'Review the complete DESIGN {target} and IMPLEMENTATION {capture}. '
    'The original review is {original}. An additional investigation supplied '
    'pixel measurements and paired region crops in {evidence}. Read that file '
    'and inspect its crops, then reconcile the disputed finding with the full '
    'screenshots. Measurements cover only their stated regions; they do not '
    'prove the whole screen passes. Retain any real typography, color, imagery '
    'or effect differences. Geometry has a separate strict structural gate. '
    'Use 9 for visual parity with only minor rendering differences, 10 for '
    'indistinguishable results, and 8 or lower for material style mismatches. '
    'Return ONLY JSON: {{"design_match":1-10,"verdict":"accept"|"rework"|"reject",'
    '"worst":"<=12 words","reason":"Explain whether the evidence resolves the original finding."}}'
)


def digest(value):
    return hashlib.sha256(value).hexdigest()


def row_digest(row):
    return digest(json.dumps(row,sort_keys=True).encode())


def validate_followup(review, original, inputs):
    """An old or edited evidence file cannot promote a current visual verdict."""
    errors=[]
    if original.get('inputs')!=inputs:errors.append('stale original screenshot review')
    if review.get('inputs')!=inputs:errors.append('stale follow-up screenshots')
    if review.get('original_review_sha256')!=row_digest(original):errors.append('different original review')
    if review.get('prompt_sha256')!=digest(PROMPT.encode()):errors.append('different follow-up criteria')
    try:
        evidence=pathlib.Path(review['evidence'])
        if digest(evidence.read_bytes())!=review['evidence_sha256']:errors.append('changed pixel evidence')
        data=json.loads(evidence.read_text())
        if data['inputs']!=inputs:errors.append('pixel evidence belongs to different screenshots')
        if not data.get('regions') or not data.get('files'):errors.append('missing measured regions')
        for path,expected in data['files'].items():
            if digest(pathlib.Path(path).read_bytes())!=expected:errors.append('changed evidence image')
    except (OSError,KeyError,ValueError) as e:errors.append(str(e))
    return errors


def build_evidence(kit,name,regions,context):
    out=kit['splash_makepad_dir'];target=(kit['targets_dir']/(name+'.png')).read_bytes()
    capture=(out/(name+'.png')).read_bytes()
    inputs=digest(target+capture+judge_shots.PROMPT.encode())
    structure=out/(name+'.structure.json')
    structure_bytes=structure.read_bytes() if structure.exists() else b'{}'
    recipe=digest(json.dumps({'regions':regions,'context':context},sort_keys=True).encode()+
        structure_bytes+pathlib.Path(__file__).read_bytes())[:16]
    folder=out/'.visual-evidence'/inputs/recipe;folder.mkdir(parents=True,exist_ok=True)
    native=folder/'native.png';native.write_bytes(capture)
    reference=judge_shots.comparison_reference(io.BytesIO(target),native,folder/'reference.png')
    a=Image.open(reference).convert('RGB');b=Image.open(native).convert('RGB')
    data={'screen':name,'inputs':inputs,'context':context,'units':'capture pixels; RGB channels 0–255',
        'regions':[],'files':{str(p.resolve()):digest(p.read_bytes()) for p in (native,reference)}}
    measured=json.loads(structure_bytes)
    if measured:
        frozen=folder/'structure.json';frozen.write_bytes(structure_bytes)
        data['files'][str(frozen.resolve())]=digest(structure_bytes)
        data['structural_gate']={k:measured.get(k) for k in ('pass','failed_checks','inspected_nodes')}
    for index,region in enumerate(regions):
        x,y,w,h=region['bounds'];box=(x,y,x+w,y+h)
        if min(x,y)<0 or min(w,h)<=0 or x+w>a.width or y+h>a.height:raise ValueError('region outside screenshot')
        ac,bc=a.crop(box),b.crop(box)
        av,bv=np.array(ac).astype(float),np.array(bc).astype(float)
        difference=np.abs(av-bv)
        mode=lambda v:max(v.getcolors(v.width*v.height),key=lambda item:item[0])
        am,bm=mode(ac),mode(bc)
        pair=Image.new('RGB',(w*2,h+24),'white');draw=ImageDraw.Draw(pair)
        draw.text((4,4),'Sketch',fill='black');draw.text((w+4,4),'Native',fill='black')
        pair.paste(ac,(0,24));pair.paste(bc,(w,24))
        path=folder/f'region-{index}.png';pair.save(path)
        data['files'][str(path.resolve())]=digest(path.read_bytes())
        data['regions'].append(region|{'comparison':str(path.resolve()),
            'measured_elements':[r for r in measured.get('elements',[]) if r.get('name')==region.get('source_element')],
            'mean_absolute_rgb_error':float(difference.mean()),
            'p95_absolute_rgb_error':float(np.percentile(difference,95)),
            'mean_channel_difference':(bv-av).mean((0,1)).tolist(),
            'reference_dominant_rgb':am[1],'reference_dominant_pixels':am[0],
            'native_dominant_rgb':bm[1],'native_dominant_pixels':bm[0],
            'reference_pixels_within_2_of_reference_mode':int((np.abs(av-np.array(am[1])).max(2)<=2).sum()),
            'native_pixels_within_2_of_reference_mode':int((np.abs(bv-np.array(am[1])).max(2)<=2).sum())})
    evidence=folder/'measurements.json';evidence.write_text(json.dumps(data,indent=2)+'\n')
    return inputs,reference,native,evidence


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--kit',required=True)
    p.add_argument('--screen',required=True);p.add_argument('--regions',type=pathlib.Path,required=True)
    args=p.parse_args();kit=kitconf.load(args.kit)
    if args.screen not in kit['screens']:raise ValueError('screen outside configured kit')
    rows={r['screen']:r for r in map(json.loads,(kitconf.HERE/kit['verdicts']['splash_makepad']).read_text().splitlines())}
    original=rows[args.screen];request=json.loads(args.regions.read_text())
    inputs,target,capture,evidence=build_evidence(kit,args.screen,request['regions'],request['context'])
    if original.get('inputs')!=inputs:raise ValueError('rerun primary screenshot review before reconsideration')
    response=llm.claude_text(PROMPT.format(target=target.resolve(),capture=capture.resolve(),
        original=json.dumps(original),evidence=evidence.resolve()))
    evidence.with_name('follow-up-response.txt').write_text(response)
    verdict=json.JSONDecoder().raw_decode(response[response.index('{'):])[0]
    if (type(verdict.get('design_match')) is not int or not 1<=verdict['design_match']<=10 or
        verdict.get('verdict') not in ('accept','rework','reject') or not verdict.get('reason')):
        raise ValueError('invalid follow-up verdict')
    review=verdict|{'inputs':inputs,'original_review_sha256':row_digest(original),
        'prompt_sha256':digest(PROMPT.encode()),'evidence':str(evidence.resolve()),
        'evidence_sha256':digest(evidence.read_bytes()),'method':'evidence-informed follow-up'}
    (kit['splash_makepad_dir']/(args.screen+'.visual-followup.json')).write_text(json.dumps(review,indent=2)+'\n')
    print(args.screen,json.dumps(verdict),flush=True)


if __name__=='__main__':main()
