#!/usr/bin/env python3
"""Apply one capture-bound typography and service-icon refinement pass.

Never edits original references, historical rounds, contracts, runtime or
service state. Plans are replayable through the pipeline's core.repair API.
Every modified source has a backup and SHA-256 precondition. Fresh Studio
capture and visual review remain required after this script completes.
"""

import argparse
import copy
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PIPE = ROOT.parents[1] / 'lab/image-to-appcard'
sys.path.insert(0, str(PIPE))
sys.path.insert(0, str(PIPE.parent))
from catalogue import walk
import compile as compiler
compiler.GALLERY = ROOT / "artwork"
from compile import compile_page
from semantics import preflight
from core.repair import apply, sha


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def read(path):
    return json.loads(path.read_text())


def create_plan(directory):
    latest = read(directory / 'latest.json')
    round_id = str(latest['round'])
    captured = directory / 'rounds' / round_id
    plan_path = directory / f'refine-measured-{round_id}.json'
    if plan_path.exists():
        return plan_path
    mapped_path = directory / 'mapped.json'
    semantic_path = directory / 'semantic-map.json'
    if sha(mapped_path.read_bytes()) != sha((captured / 'mapped.json').read_bytes()):
        raise ValueError(f'{directory.name}: current mapped design differs from captured input')
    document = read(mapped_path)
    original = copy.deepcopy(document)
    manifest = read(semantic_path)
    old_manifest = copy.deepcopy(manifest)
    nodes = {node['id']: node for node in walk(document['tree'])}
    evidence = {
        'reference.png': sha((directory / 'reference.png').read_bytes()),
        f'rounds/{round_id}/native.png': sha((captured / 'native.png').read_bytes()),
        f'rounds/{round_id}/gate.json': sha((captured / 'gate.json').read_bytes()),
        f'rounds/{round_id}/repair.json': sha((captured / 'repair.json').read_bytes()),
        f'rounds/{round_id}/mapped.json': sha((captured / 'mapped.json').read_bytes()),
    }
    inputs = {'mapped.json': sha(mapped_path.read_bytes())}
    gate = read(captured / 'gate.json')
    changes, skipped = [], []
    for measured in gate.get('text_differences', []):
        node = nodes.get(measured['id'])
        reason = None
        if not node or node.get('t') != 'text':
            reason = 'not a native text node'
        elif any('OCR' in issue or 'reference text missing' in issue for issue in measured.get('issues', [])):
            reason = 'reference OCR is unresolved or differs from approved text; preserve semantics and typography'
        elif not measured.get('reference') or not measured.get('native'):
            reason = 'no paired reference/native ink measurement'
        if reason:
            skipped.append({'id': measured['id'], 'reason': reason})
            continue
        rx, ry, rw, rh = measured['reference']
        nx, ny, nw, nh = measured['native']
        if min(rw, rh, nw, nh) <= 0:
            skipped.append({'id': node['id'], 'reason': 'invalid ink dimensions'})
            continue
        scale = min(rw / nw, rh / nh)
        if not .60 <= scale <= 1.12 or max(abs(rx - nx), abs(ry - ny)) > 15:
            skipped.append({'id': node['id'], 'reason': 'measurement exceeds bounded correction range', 'scale': scale})
            continue
        if node.get('tracking', 0) < 0:
            raise ValueError(f'{directory.name}/{node["id"]}: negative input tracking requires separate capture review')
        before = {key: node.get(key) for key in ('x', 'y', 'w', 'h', 'size', 'tracking', 'line_height')}
        new_size = node['size'] * scale
        gaps = max(1, len(node['text']) - 1)
        # Width first fits at non-negative tracking. Only add positive spacing
        # where the measured glyph height leaves real horizontal room.
        tracking = max(0, (rw - nw * scale) / gaps)
        tracking = min(tracking, 1.25, new_size * .10)
        target_width = nw * scale + tracking * gaps
        node.update(
            x=rx - (nx - node['x']) * scale,
            y=ry - (ny - node['y']) * scale,
            size=new_size,
            tracking=tracking,
            w=max(target_width + 5, node['w'] * scale + tracking * gaps + 2),
            h=max(rh + 4, node['h'] * scale),
        )
        node['line_height'] = node['h']
        changes.append({
            'id': node['id'], 'category': 'typography', 'text_unchanged': node['text'],
            'reference_ink': measured['reference'], 'captured_ink': measured['native'],
            'scale': scale, 'before': before,
            'after': {key: node[key] for key in before},
            'estimated_ink_after': [rx, ry, target_width, nh * scale],
            'reason': 'Uniform glyph-size fit to real paired ink bounds; non-negative capped tracking and measured-origin correction',
        })

    backup = directory / 'repairs' / f'measured-{round_id}'
    backup.mkdir(parents=True, exist_ok=True)
    (backup / 'mapped.before.json').write_bytes(mapped_path.read_bytes())
    (backup / 'semantic-map.before.json').write_bytes(semantic_path.read_bytes())
    operations = []
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    for element in manifest['elements']:
        asset = element.get('asset')
        if not asset or not asset.get('path', '').endswith('.svg'):
            continue
        ident = element['id']
        dock = ident in {'dock_mail', 'dock_bag', 'dock_wallet'}
        check = ident.startswith('check_icon_')
        if not (dock or check):
            continue
        relative = asset['path']
        path = directory / relative
        raw = path.read_bytes()
        if sha(raw) != asset['sha256']:
            raise ValueError(f'{directory.name}: stale semantic asset hash for {ident}')
        svg = ET.fromstring(raw)
        if dock:
            x, y, w, h = [float(value) for value in svg.attrib['viewBox'].split()]
            svg.set('viewBox', ' '.join(f'{value:g}' for value in (x - w / 4, y - h / 4, w * 1.5, h * 1.5)))
            reason = 'Reviewed Studio dock symbol is about 1.5 times the source size; expand internal viewBox 1.5 times while keeping the measured native component rectangle'
        else:
            circle = next((n for n in svg.iter() if n.tag.split('}')[-1] == 'circle'), None)
            if circle is None:
                raise ValueError(f'{directory.name}: expected check circle in {ident}')
            circle.set('fill', '#608570')
            circle.set('stroke', '#608570')
            for child in svg.iter():
                if child.tag.split('}')[-1] == 'path':
                    child.set('stroke', '#ffffff')
                    child.set('stroke-width', '2')
            reason = 'Reviewed white confirmation check had a transparent circle; fill the native SVG circle with sage so the white tick is legible'
        new_raw = ET.tostring(svg, encoding='utf-8') + b'\n'
        before_path = backup / 'assets.before' / path.name
        replacement = backup / 'assets.refined' / path.name
        before_path.parent.mkdir(exist_ok=True)
        replacement.parent.mkdir(exist_ok=True)
        before_path.write_bytes(raw)
        replacement.write_bytes(new_raw)
        replacement_relative = replacement.relative_to(directory).as_posix()
        evidence[replacement_relative] = sha(new_raw)
        inputs[relative] = sha(raw)
        operations.append({'op': 'asset', 'file': relative, 'source': replacement_relative,
                           'category': 'asset', 'element': ident, 'reason': reason})
        asset['sha256'] = sha(new_raw)
        asset['notes'] = asset.get('notes', '') + '; Measured native refinement: ' + reason
        changes.append({'id': ident, 'category': 'asset', 'before_sha256': sha(raw),
                        'after_sha256': sha(new_raw), 'bounds_unchanged': True, 'reason': reason})

    if document != original:
        document.setdefault('changes', []).append({
            'source': 'Paired actual/reference ink from Studio round ' + round_id,
            'repair_plan': plan_path.name, 'tracking_policy': 'non-negative and capped at min(1.25 logical pixels, 0.10 em)',
            'acceptance': 'Requires fresh Studio capture and full gate review',
        })
        operations.insert(0, {'op': 'document', 'file': 'mapped.json', 'after': document,
                              'category': 'typography', 'element': 'native-text-labels',
                              'reason': 'Measured uniform size and origin refinements; preserve all native labels/buttons and exact approved text'})
    if manifest != old_manifest:
        inputs['semantic-map.json'] = sha(semantic_path.read_bytes())
        operations.append({'op': 'document', 'file': 'semantic-map.json', 'after': manifest,
                           'category': 'semantic', 'element': 'reviewed-native-vector-assets',
                           'reason': 'Bind the reviewed SVG refinements to their exact new asset hashes'})
    if not operations:
        raise ValueError(f'{directory.name}: no eligible measured corrections')
    plan = {'schema_version': 1, 'findings': changes, 'skipped': skipped,
            'evidence': evidence, 'inputs': inputs, 'operations': operations,
            'source_round': round_id, 'backup_directory': backup.relative_to(directory).as_posix(),
            'scope': 'Native typography plus existing dock/check SVG artwork only; no raster UI, original image edits, service or runtime changes'}
    save(plan_path, plan)
    return plan_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Apply bound repairs and run native compile + semantic preflight')
    parser.add_argument('designs', nargs='*')
    args = parser.parse_args()
    directories = [ROOT / 'cards' / name for name in args.designs] if args.designs else sorted((ROOT / 'cards').glob('aircon-*'))
    prepared = [(directory, create_plan(directory)) for directory in directories]
    report = {'schema_version': 1, 'applied': args.apply, 'studio_capture_performed': False,
              'acceptance': 'pending fresh Studio capture, gate and visual review', 'cards': []}
    for directory, plan_path in prepared:
        plan = read(plan_path)
        result = apply(directory, plan_path, preview=not args.apply)
        row = {'id': directory.name, 'source_round': plan['source_round'],
               'plan': plan_path.relative_to(ROOT).as_posix(), 'plan_sha256': sha(plan_path.read_bytes()),
               'typography_changes': sum(c['category'] == 'typography' for c in plan['findings']),
               'asset_changes': sum(c['category'] == 'asset' for c in plan['findings']),
               'skipped': plan['skipped'], 'repair_status': result['status']}
        if args.apply:
            row['semantic_preflight_pass'] = preflight(directory)['pass']
            row['compile'] = compile_page(directory)
            row['mapped_sha256'] = sha((directory / 'mapped.json').read_bytes())
            assert all(n.get('tracking', 0) >= 0 for n in walk(read(directory / 'mapped.json')['tree']) if n['t'] == 'text')
        report['cards'].append(row)
        print(json.dumps({key: row[key] for key in ('id', 'source_round', 'typography_changes', 'asset_changes', 'repair_status')}, ensure_ascii=False), flush=True)
    save(ROOT / 'review/refine-measured.json', report)


if __name__ == '__main__':
    main()
