#!/usr/bin/env python3
"""Role-first mapping policy. Inspection of an SVG is not proof of a chart.

Classification suggestions come from the authored contract, not image recognition.
Audits of existing captures are written beside them, without changing old rounds.
"""
import argparse
import hashlib
import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path
from catalogue import HERE, walk

import sys
sys.path.insert(0,str(HERE.parent))
from core.policy import POLICY_PATH,POLICY,numeric,local_asset,data_issues,asset_issues,runtime_data_issues
# This compiler's implemented adapters. A policy candidate is not automatically
# a working runtime adapter; new native chart lowering must be added explicitly.
IMPLEMENTED_KINDS = {'stack', 'text', 'button', 'input', 'svg', 'image', 'stockplot', 'progress', 'web'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2) + '\n')


def classify(node, contract):
    """Use declared intent first. Name heuristics only produce review candidates."""
    graphic = contract.get('graphics', {}).get(node['id'], {}).get('kind')
    if graphic in ('line', 'compare', 'donut', 'wave'):
        role = {'line': 'chart.line', 'compare': 'chart.line',
                'donut': 'chart.donut', 'wave': 'waveform'}[graphic]
        if node['id'] == 'portfolio_chart':
            role = 'chart.area'  # The authored portfolio brief explicitly asks for an area chart.
        return role, 'authored graphic intent: ' + graphic, 1.0
    if graphic == 'radar':
        return 'unknown', 'radar could mean a weather map or a radial data plot', 0.5
    if graphic == 'landscape':
        return 'illustration', 'authored landscape illustration', 1.0
    if graphic in ('sun', 'cloud', 'moon'):
        return 'icon', 'authored weather icon', 1.0
    if node['id'].startswith('period_'):
        return 'range_option', 'range-selector candidate; confirm chart binding', 0.8
    if 'progress' in node['id'] and node['t'] == 'stack':
        return 'progress', 'progress-value candidate; identify its value owner', 0.8
    if node.get('kit'):
        widget = json.loads(node['kit']).get('widget')
        if widget == 'KitButton':
            return 'button', 'authored KitButton composition', 1.0
        if widget == 'KitFormField':
            return 'input', 'authored KitFormField with native TextInput binding', 1.0
        return 'unknown', 'unclassified kit component: ' + str(widget), 0.0
    roles = {'stack': 'layout', 'text': 'text', 'button': 'button',
             'input': 'input', 'radio': 'toggle', 'checkbox': 'toggle', 'web': 'webview'}
    role = roles.get(node['t'], 'unknown')
    return role, 'authored ' + node['t'] + ' node', 1.0 if role != 'unknown' else 0.0


def propose(directory):
    directory = Path(directory)
    path = directory / 'semantic-map.json'
    if path.exists():
        return read(path)  # Never overwrite subsequent decisions or asset provenance.
    contract = read(directory / 'contract.json')
    entries = []
    for node in walk(contract['tree']):
        role, basis, confidence = classify(node, contract)
        entry = {'id': node['id'], 'role': role, 'basis': basis,
                 'confidence': confidence, 'decision': 'declared' if confidence == 1 else 'needs_review'}
        if POLICY['roles'][role].get('asset'):
            entry['asset'] = {'method': 'unrecorded', 'note': 'Record the exact reference-derived artwork or source crop; generic artwork is not fidelity evidence.'}
        entries.append(entry)
    result = {'schema_version': 1, 'policy_version': POLICY['version'],
              'contract_sha256': sha(directory / 'contract.json'),
              'reference_sha256': sha(directory / 'reference.png'),
              'classification_scope': 'Authored intent and explicit review candidates; no claim of automatic visual recognition.',
              'elements': entries}
    write(path, result)
    write_brief(directory, result)
    return result


def write_brief(directory, manifest):
    contract = read(directory / 'contract.json')
    rows = []
    roles = {e['id']: e for e in manifest['elements']}
    for node in walk(contract['tree']):
        entry = roles[node['id']]
        rows.append({**{k: node[k] for k in ('id', 'x', 'y', 'w', 'h', 'text', 'font_src', 'size', 'weight') if k in node},
                     'role': entry['role'], 'native_candidates': POLICY['roles'][entry['role']]['native_types'],
                     **{k: entry[k] for k in ('data', 'behavior', 'asset') if k in entry}})
    text = '''# Conversion brief

This is an implementation brief, not a claim that these instructions were used
to generate the existing reference. Keep the submitted image prompt unchanged.

Apply MAPPING-RULES.md and mapping-rules.json. Resolve every needs_review/unknown
region. Prefer a matching native kit component, then built-in Makepad widgets,
then a reusable custom widget for missing behavior. Use SVG or cropped Image
assets only for artwork. Never substitute a chart or control with an asset.

For new image generation, include the exact text, font files/family/weights,
layout hierarchy, dimensions, spacing, colors, chart samples/units/domains and
selected control states. Preserve a separate machine-readable manifest. Request
complex illustrations as separate assets, or clearly bounded artwork-only regions
with no overlaid UI text. Do not invent missing numerical values from a mockup.

After generation, measure the actual reference. Requested layout is not measured
evidence. Inspect through Makepad's built-in HTTP instrument with a standalone
release binary; hidden windows support automated tests. See
`lab/core/NATIVE-INSTRUMENT.md`. Run semantic, geometry and visual checks;
legacy Studio capture/gate adapters require their own evidence schema.

```json
''' + json.dumps(rows, indent=2) + '\n```\n'
    (directory / 'conversion-brief.md').write_text(text)



def evaluate(directory, round_dir=None):
    directory = Path(directory)
    source = Path(round_dir) if round_dir else directory
    errors = []
    results = []
    manifest_path = source / 'semantic-map.json'
    # Retrospective audits explicitly apply today's rules to an immutable capture.
    if not manifest_path.exists():
        manifest_path = directory / 'semantic-map.json'
    if not manifest_path.exists():
        return {'pass': False, 'errors': ['missing semantic-map.json; run the classify stage'], 'elements': []}
    manifest = read(manifest_path)
    contract = read(source / 'contract.json')
    tree_path = source / 'mapped.json'
    nodes = {n['id']: n for n in walk(read(tree_path)['tree'] if tree_path.exists() else contract['tree'])}
    if manifest.get('policy_version') != POLICY['version']:
        errors.append('mapping policy version mismatch')
    if manifest.get('contract_sha256') != sha(source / 'contract.json'):
        errors.append('semantic mapping belongs to a different contract')
    if manifest.get('reference_sha256') != sha(directory / 'reference.png'):
        errors.append('semantic mapping belongs to a different reference image')
    entries = manifest.get('elements', [])
    ids = [e['id'] for e in entries]
    if len(ids) != len(set(ids)):
        errors.append('duplicate semantic element IDs')
    for id in sorted(nodes.keys() - set(ids)):
        errors.append(id + ': unclassified source element')
    for id in sorted(set(ids) - nodes.keys()):
        errors.append(id + ': semantic element is absent from the composition')
    mapping = {n['source_id']: n for n in read(source / 'mapping.json')['elements']} if round_dir else {}
    snapshots = {n['id']: n for n in read(source / 'snapshot.json')['widgets']} if round_dir else {}
    proof = read(source / 'provenance.json') if round_dir else {}
    if round_dir:
        for name in ('snapshot.json','tree.json','queries.json','mapping.json','page.data.json','contract.json','native.png'):
            if name not in proof.get('files', {}):
                errors.append('missing capture provenance: ' + name)
        for name, checksum in proof.get('files', {}).items():
            path = local_asset(source, name)
            if not path or sha(path) != checksum:
                errors.append('stale capture evidence: ' + name)
        if proof.get('reference_sha256') != manifest.get('reference_sha256'):
            errors.append('capture belongs to a different reference image')
        if read(source / 'snapshot.json').get('build_id') != proof.get('build_id'):
            errors.append('snapshot belongs to a different Studio build')
        current_manifest = directory / 'semantic-map.json'
        if manifest_path != current_manifest and current_manifest.exists() and sha(current_manifest) != sha(manifest_path):
            errors.append('mapping decisions changed since capture; recapture the current composition')
    state_path = source / 'semantic-state.json'
    state = read(state_path) if state_path.exists() else {}
    state_current = bool(round_dir and state_path.exists() and
                         proof.get('files', {}).get('semantic-state.json') == sha(state_path) and
                         state.get('nonce') == proof.get('nonce') and state.get('build_id') == proof.get('build_id'))
    for entry in entries:
        id = entry['id']
        node = nodes.get(id)
        if node is None:
            continue
        role = entry.get('role')
        rule = POLICY['roles'].get(role)
        issues = []
        # Value domains the renderer will not check for us. Each of these
        # compiled cleanly in the calendar evaluation and failed on screen:
        # alignx 2 (200 %) drew the label outside its box, a 44 pt title in
        # a 30 pt box clipped every line, and a 0-height box drew nothing.
        issues.extend(value_domain_issues(node))
        actual = snapshots.get(mapping.get(id, {}).get('native_id'), {})
        if not rule or role == 'unknown':
            issues.append('unresolved semantic role')
            rule = POLICY['roles']['unknown']
        confidence = entry.get('confidence')
        if not numeric(confidence) or not POLICY['minimum_confidence'] <= confidence <= 1:
            issues.append('classification requires review with recorded evidence')
        if entry.get('decision') not in ('declared', 'reviewed') or not entry.get('basis'):
            issues.append('missing supported mapping decision')
        # Do not hide a declared chart behind a convenient icon/illustration role.
        original = next((n for n in walk(contract['tree']) if n['id'] == id), node)
        expected, _, certainty = classify(original, contract)
        if certainty == 1 and (expected.startswith('chart.') or expected == 'waveform') and role != expected:
            issues.append('mapping contradicts the authored data-visualization role')
        if node['t'] not in rule['kinds']:
            issues.append('wrong renderer kind: ' + node['t'] + '; expected ' + ', '.join(rule['kinds']))
        if not round_dir and node['t'] not in IMPLEMENTED_KINDS:
            issues.append('native adapter is not implemented in the UX-image compiler: ' + node['t'])
        if round_dir and actual.get('widget_type') not in rule['native_types']:
            issues.append('wrong inspected widget: ' + str(actual.get('widget_type')) + '; expected ' + ', '.join(rule['native_types']))
        if rule.get('data'):
            issues.extend(data_issues(source, entry))
        if rule.get('asset'):
            issues.extend(asset_issues(source, entry, manifest, reference_dir=directory))
            asset_path = local_asset(source, entry.get('asset', {}).get('path'))
            if asset_path and ((node['t'] == 'svg') != (asset_path.suffix.lower() == '.svg')):
                issues.append('asset file format does not match its native renderer')
            if asset_path and entry.get('asset', {}).get('fit') in ('contain', 'cover'):
                # The current design emitter uses Stretch. At equal aspect it
                # is equivalent; otherwise this needs native fitting support or
                # an explicitly fitted child rectangle and clipping container.
                try:
                    if asset_path.suffix.lower() == '.svg':
                        box = [float(v) for v in ET.parse(asset_path).getroot().get('viewBox', '').replace(',', ' ').split()]
                        aw, ah = box[2:4]
                    else:
                        from PIL import Image
                        with Image.open(asset_path) as asset_image:
                            aw, ah = asset_image.size
                    equivalent = all(numeric(v) and v > 0 for v in (aw, ah, node.get('w'), node.get('h'))) and abs(aw/ah-node['w']/node['h']) < 1e-6
                except (ValueError, OSError, ET.ParseError):
                    equivalent = False
                if not equivalent:
                    issues.append('requested asset fit needs a native fitting adapter or correctly fitted child bounds; current emitter stretches')
            if round_dir and asset_path:
                native_doc = read(source / 'native.json')
                # The compiled tree records the content-addressed URL bound to
                # the widget. A valid unrelated asset is not rendering evidence.
                compiled = next((n for n in walk(native_doc.get('tree', {})) if n.get('original_id') == id), None)
                # Hosts that do not expose their emitted tree must supply this
                # binding through the captured placements file instead.
                placements = read(source / 'page.data.json').get('$kit', {}).get('placements', {})
                url = (compiled or {}).get('src') or placements.get(id, {}).get('layout', {}).get('src', '')
                suffix = '-' + sha(asset_path)[:12] + asset_path.suffix.lower()
                if not url.endswith(suffix):
                    issues.append('inspected composition is not bound to the declared artwork asset')
        if rule.get('behavior'):
            behavior = entry.get('behavior', {})
            if not behavior.get('event') or behavior.get('target') not in nodes or not behavior.get('property'):
                issues.append('missing event, target and state/data binding')
            if behavior.get('label') and nodes.get(behavior['label'],{}).get('t')!='text':
                issues.append('selection label must reference a native text element')
        if round_dir and (rule.get('data') or rule.get('behavior')):
            runtime = state.get('elements', {}).get(id, {})
            if not state_current or runtime.get('native_id') != mapping.get(id, {}).get('native_id'):
                issues.append('missing current Studio-bound semantic state evidence')
            if rule.get('data') and state_current:
                issues.extend(runtime_data_issues(source,entry,runtime))
            if rule.get('behavior') and not (runtime.get('event') == entry.get('behavior', {}).get('event') and
                                           runtime.get('target') == entry.get('behavior', {}).get('target') and
                                           runtime.get('property') == entry.get('behavior', {}).get('property') and
                                           'before' in runtime and 'after' in runtime and runtime['before'] != runtime['after']):
                issues.append('missing observed state change for the declared interaction')
            behavior=entry.get('behavior',{})
            if behavior.get('label'):
                ink=behavior.get('active_color' if runtime.get('selected') else 'inactive_color','').lstrip('#')
                if len(ink)!=6 or any(c not in '0123456789abcdefABCDEF' for c in ink):
                    issues.append('missing valid selected/unselected label colors')
                else:
                    expected=[int(ink[i:i+2],16)/255 for i in (0,2,4)]+[1.0]
                    actual_ink=runtime.get('label_color',[])
                    if len(actual_ink)!=4 or max(abs(a-b) for a,b in zip(actual_ink,expected))>1e-6:
                        issues.append('native label color does not follow the current selection')
        results.append({'id': id, 'role': role, 'basis': entry.get('basis'),
                        'expected_widgets': rule['native_types'], 'actual_widget': actual.get('widget_type'),
                        'issues': issues, 'repair': rule['repair']})
        errors.extend(id + ': ' + issue for issue in issues)
    return {'schema_version': 1, 'policy_version': POLICY['version'], 'policy_sha256': sha(POLICY_PATH),
            'evaluator_sha256': sha(Path(__file__)),
            'manifest_sha256': sha(manifest_path), 'reference_sha256': manifest.get('reference_sha256'),
            'id': directory.name, 'round': source.name if round_dir else None,
            'phase': 'inspection' if round_dir else 'preflight', 'pass': not errors,
            'errors': errors, 'elements': results,
            'scope': 'Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate.'}



# The natural line box of the shipped fonts is about 1.45 x the size; a
# text box shorter than that clips the glyphs at the bottom.
LINE_BOX_FACTOR = 1.45


def value_domain_issues(node):
    """Cheap, deterministic checks on a composition node's values.

    Structure and semantics are checked elsewhere; this is the layer that was
    missing: a value that parses but cannot render as intended.
    """
    issues = []
    kind = node.get('t')
    for axis in ('alignx', 'aligny'):
        value = node.get(axis)
        if value is not None and not (numeric(value) and 0 <= value <= 1):
            issues.append(f'{axis} {value!r} is outside 0..1 (0 = start, 0.5 = centre, 1 = end)')
    for dim in ('w', 'h'):
        value = node.get(dim)
        if value is not None and not (numeric(value) and value >= 0):
            issues.append(f'{dim} {value!r} is not a non-negative number')
    for colour in ('color', 'bg'):
        value = node.get(colour)
        if value is None:
            continue
        ok = (numeric(value) and 0 <= value <= 0xFFFFFFFF) or (
            isinstance(value, str) and value.startswith('#') and len(value) in (7, 9)
            and all(c in '0123456789abcdefABCDEF' for c in value[1:]))
        if not ok:
            issues.append(f'{colour} {value!r} is neither a packed ARGB integer nor #RRGGBB / #AARRGGBB')
    if kind == 'text':
        size = node.get('size')
        if size is not None and not (numeric(size) and size > 0):
            issues.append(f'text size {size!r} must be a positive number')
        # The box must hold the line: an authored line_height when there is
        # one, else the font's natural line box. A 44 pt title in a 30 pt box
        # clipped every line of the calendar's first build.
        if numeric(size) and size > 0 and numeric(node.get('h')):
            line = node.get('line_height')
            needed = line if numeric(line) and line > 0 else size * LINE_BOX_FACTOR
            if node['h'] < needed - 0.5:
                issues.append(f"text box height {node['h']} is under its line box ({round(needed, 1)}); "
                              "the glyphs will clip at the bottom")
        if numeric(node.get('w')) and node['w'] == 0 and node.get('text'):
            issues.append('text box width 0 draws nothing')
    return issues

def preflight(directory):
    report = evaluate(directory)
    write(Path(directory) / 'semantic-preflight.json', report)
    if not report['pass']:
        raise ValueError('Semantic mapping blocked: ' + '; '.join(report['errors'][:4]) +
                         '. See semantic-preflight.json and MAPPING-RULES.md.')
    return report


def audit(directory):
    directory = Path(directory)
    latest = read(directory / 'latest.json') if (directory / 'latest.json').exists() else None
    report = evaluate(directory, directory / 'rounds' / latest['round'] if latest else None)
    write(directory / 'semantic-audit.json', report)
    write(directory / 'semantic-repair.json', {
        'policy_version': POLICY['version'], 'round': report.get('round'), 'pass': report['pass'],
        'errors': report['errors'], 'repairs': [e for e in report['elements'] if e['issues']]})
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('design', nargs='+')
    parser.add_argument('--propose', action='store_true')
    args = parser.parse_args()
    failed = False
    for id in args.design:
        directory = HERE / id
        if args.propose:
            propose(directory)
        report = audit(directory)
        print(json.dumps({'id': id, 'semantic_pass': report['pass'], 'findings': len(report['errors'])}))
        failed |= not report['pass']
    raise SystemExit(1 if failed else 0)
