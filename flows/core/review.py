#!/usr/bin/env python3
"""Prepare frozen screenshot pairs and record an explicit external review.

This command never judges an image or calls a model. A human or a vision-capable
reviewer supplies the decision; the existing pipeline gates retain authority.
"""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # flows/, for `core`
import argparse
import fcntl
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys

HERE = Path(__file__).resolve().parent
SKETCH = HERE.parent / 'kits' / 'sketch'
IMAGES = HERE.parent / 'image-lib'
CRITERIA = ('typography', 'colors', 'imagery', 'effects')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def write(path, value):
    temporary = path.with_suffix(path.suffix + '.pending')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.replace(path)


def identifier(value):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*', value):
        raise ValueError('use a configured kit, screen or design ID')
    return value


def paths(origin):
    if origin['kind'] == 'image':
        directory = IMAGES / identifier(origin['design'])
        latest = read(directory / 'latest.json')
        if not re.fullmatch(r'\d+', latest['round']):
            raise ValueError('invalid capture round')
        return directory / 'reference.png', directory / 'rounds' / latest['round'] / 'native.png'
    if origin['kind'] != 'sketch':
        raise ValueError('unknown review source')
    from core import kitconf
    kit = kitconf.load(identifier(origin['kit']))
    screen = identifier(origin['screen'])
    if screen not in kit['screens']:
        raise ValueError('screen is not configured in this kit')
    return kit['targets_dir'] / (screen + '.png'), kit['splash_makepad_dir'] / (screen + '.png')


def prepare(origin, output):
    source, native = paths(origin)
    source_bytes, native_bytes = source.read_bytes(), native.read_bytes()
    pair = {'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
            'native_sha256': hashlib.sha256(native_bytes).hexdigest()}
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    (output / 'source.png').write_bytes(source_bytes)
    (output / 'native.png').write_bytes(native_bytes)
    if origin['kind'] == 'sketch':
        from core.judge_shots import comparison_reference
        comparison_reference(output / 'source.png', output / 'native.png', output / 'reference.png')
    else:
        (output / 'reference.png').write_bytes(source_bytes)
    write(output / 'packet.json', {'schema_version': 1, 'origin': origin, **pair,
          'files': {name: sha(output / name) for name in ('source.png', 'reference.png', 'native.png')}})
    write(output / 'decision.template.json', {**pair, 'reviewer': '', 'verdict': 'unreviewed',
          'design_match': None, 'criteria': {key: False for key in CRITERIA},
          'basis': '', 'remaining_differences': ''})
    (output / 'index.html').write_text('''<!doctype html><meta charset="utf-8">
<meta name="viewport" content="width=device-width"><title>Source and native review</title>
<style>body{font:16px system-ui;margin:24px;background:#eef1f4}.pair{display:flex;gap:24px}
figure{margin:0;flex:1;max-width:480px;min-width:0}img{width:100%}figcaption{margin:12px 0}</style>
<h1>Source and native review</h1><p>Inspect both images before completing decision.template.json.
Review typography, colors, imagery and effects. Record remaining differences.
Geometry, semantics and state have separate mandatory gates.</p><div class="pair">
<figure><figcaption>Source reference</figcaption><img src="reference.png" alt="Source"></figure>
<figure><figcaption>Native Makepad capture</figcaption><img src="native.png" alt="Native"></figure></div>''')
    return output / 'index.html'


def prepare_source(kit_name, screen, output):
    """Seed an unresolved Sketch semantic review, never a classification/pass."""
    from core import kitconf
    from core.semantic_policy import POLICY, candidates, source_tree_hash
    from core.source_identity import stable_tree_hash
    kit = kitconf.load(identifier(kit_name))
    if identifier(screen) not in kit['screens']:
        raise ValueError('screen is not configured in this kit')
    spec_path = kit['specs_dir'] / (screen + '.json')
    source = kit['targets_dir'] / (screen + '.png')
    spec_bytes, source_bytes = spec_path.read_bytes(), source.read_bytes()
    spec = json.loads(spec_bytes)
    source_hash = hashlib.sha256(source_bytes).hexdigest()
    if source_hash != spec.get('reference_sha256'):
        raise ValueError('source pixels changed since import')
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    (output / 'source.png').write_bytes(source_bytes)
    (output / 'source-tree.json').write_bytes(spec_bytes)
    write(output / 'semantic-manifest.template.json', {
        'policy_version': POLICY['version'], 'reference_sha256': source_hash,
        'source_review': {'reviewer': '', 'basis': '', 'verdict': 'needs_review',
            'method': 'source_image_and_hierarchy', 'source_tree_sha256': source_tree_hash(spec),
            'stable_source_tree_sha256': stable_tree_hash(spec)},
        'elements': [{'id': n['native_widget_id'], 'role': 'unknown', 'decision': 'needs_review',
                      'basis': ''} for n in candidates(spec)]})
    (output / 'README.md').write_text('''Inspect the entire source.png and source-tree.json, including anonymous data regions.
The candidate list is incomplete by design and is not a semantic classification.
Complete the source review and classify every required region using the shared
mapping policy. Add anonymous regions. Charts need numerical data, domains,
units, source paint owners and supported adapters. Preserve the reference and
original tree. Install only the explicitly reviewed manifest in the kit's
semantics directory, then re-import, promote, capture and audit.
''')
    return output / 'semantic-manifest.template.json'


def submit(packet_dir, decision_path):
    packet_dir = Path(packet_dir)
    packet = read(packet_dir / 'packet.json')
    for name in ('source.png', 'reference.png', 'native.png'):
        if sha(packet_dir / name) != packet['files'][name]:
            raise ValueError('review packet changed: ' + name)
    source, native = paths(packet['origin'])
    source_bytes, native_bytes = source.read_bytes(), native.read_bytes()
    pair = {'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
            'native_sha256': hashlib.sha256(native_bytes).hexdigest()}
    decision = read(Path(decision_path))
    if any(pair[key] != packet[key] or pair[key] != decision.get(key) for key in pair):
        raise ValueError('source/native pixels changed; prepare and inspect a new pair')
    if decision.get('verdict') not in ('pass', 'repair', 'reject'):
        raise ValueError('an explicit reviewed verdict is required')
    if not all(isinstance(decision.get(key), str) and decision[key].strip() for key in ('reviewer', 'basis')):
        raise ValueError('reviewer and written review basis are required')
    criteria = decision.get('criteria', {})
    if any(type(criteria.get(key)) is not bool for key in CRITERIA):
        raise ValueError('all four visual criteria must be boolean')
    if decision['verdict'] == 'pass' and not all(criteria[key] for key in CRITERIA):
        raise ValueError('a pass requires all four visual criteria')
    origin = packet['origin']
    if origin['kind'] == 'image':
        directory = source.parent
        target = directory / 'visual-review.json'
        receipt = {'reference_sha256': pair['source_sha256'], 'native_sha256': pair['native_sha256'],
                   'reviewer': decision['reviewer'], 'verdict': 'pass' if decision['verdict'] == 'pass' else 'repair',
                   'criteria': criteria, 'findings': [{'area': 'overall', 'status': decision['verdict'],
                    'detail': decision['basis'], 'remaining_differences': decision.get('remaining_differences', '')}]}
        archive = directory / 'visual-reviews'
        archive.mkdir(exist_ok=True)
        if target.exists():
            previous = archive / (sha(target) + '.json')
            if not previous.exists():
                shutil.copy2(target, previous)
        write(target, receipt)
    else:
        from core import kitconf
        from core.judge_shots import PROMPT
        score = decision.get('design_match')
        if type(score) is not int or not 1 <= score <= 10:
            raise ValueError('Sketch review requires an integer design_match from 1 to 10')
        kit = kitconf.load(origin['kit'])
        target = SKETCH / kit['verdicts']['splash_makepad']
        target.parent.mkdir(parents=True, exist_ok=True)
        receipt = {'screen': origin['screen'], 'inputs': hashlib.sha256(source_bytes + native_bytes + PROMPT.encode()).hexdigest(),
                   'design_match': score, 'verdict': {'pass': 'accept', 'repair': 'rework', 'reject': 'reject'}[decision['verdict']],
                   'reviewer': decision['reviewer'], 'method': 'external source/native visual inspection',
                   'basis': decision['basis'], 'worst': decision.get('remaining_differences', ''), 'criteria': criteria}
        with target.with_suffix('.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            with target.open('a') as output:
                output.write(json.dumps(receipt) + '\n')
    write(packet_dir / 'submitted-decision.json', decision)
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest='action', required=True)
    create = actions.add_parser('prepare')
    branch = create.add_mutually_exclusive_group(required=True)
    branch.add_argument('--kit')
    branch.add_argument('--design')
    create.add_argument('--screen')
    create.add_argument('--out', required=True, type=Path)
    record = actions.add_parser('submit')
    record.add_argument('--packet', required=True, type=Path)
    record.add_argument('--decision', required=True, type=Path)
    source = actions.add_parser('prepare-source')
    source.add_argument('--kit', required=True)
    source.add_argument('--screen', required=True)
    source.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    if args.action == 'submit':
        print(submit(args.packet, args.decision))
    elif args.action == 'prepare-source':
        print(prepare_source(args.kit, args.screen, args.out))
    else:
        if args.kit and not args.screen:
            parser.error('--kit requires --screen')
        origin = ({'kind': 'sketch', 'kit': args.kit, 'screen': args.screen} if args.kit else
                  {'kind': 'image', 'design': args.design})
        print(prepare(origin, args.out))


if __name__ == '__main__':
    main()
