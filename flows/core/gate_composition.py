#!/usr/bin/env python3
"""Audit native-first source mappings; widget counts alone cannot pass this gate.

This gate covers generated composition policy. Studio inspection and visual
freshness remain separate required gates. It does not certify reusable layouts.
"""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # flows/, for `core`
import argparse
import collections
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlparse

from core import kitconf
from core.gate_structure import source_elements

CONTROL_KINDS = {'button': 'Button', 'text_input': 'Input', 'checkbox': 'Checkbox',
                 'toggle': 'Toggle', 'radio': 'Radio', 'tab': 'Tab',
                 'slider': 'Slider', 'range_slider': 'RangeSlider'}


def walk(node):
    yield node
    for child in node.get('children', []):
        yield from walk(child)


def compare(spec, portable, scale=1):
    errors, differences, assets = [], [], []
    nodes = portable.get('elements', [])
    if not nodes:
        errors.append('missing generated widgets')
    imported = collections.defaultdict(list)
    for node in nodes:
        imported[node.get('original_id')].append(node)
    sources = list(walk(spec))
    owners = collections.defaultdict(list)
    for source in sources:
        if source.get('graphic_asset'):
            owners[source.get('native_paint_id') or source.get('native_widget_id')].append(source)
    if spec.get('native_widgets_first') is not True:
        errors.append('source was not imported with native_widgets_first; reimport with the native policy')

    def issue(source, message, node=None):
        differences.append({'source_id': source.get('object_id'),
            'source_path': source.get('source_path'), 'name': source.get('name'),
            'widget_id': node.get('id') if node else source.get('native_widget_id'),
            'issue': message})

    # Every actual paint widget needs an individual source decision. Checking
    # only spec declarations lets unowned Image nodes bypass the fallback rules.
    for node in nodes:
        if node['kind'] not in ('Image', 'Svg'):
            continue
        matches = owners.get(node.get('original_id'), [])
        if len(matches) != 1:
            issue({}, 'paint widget lacks one unambiguous source owner', node)
            continue
        source = matches[0]
        rendering = source.get('rendering', {})
        backend = rendering.get('backend')
        expected = 'bitmap' if node['kind'] == 'Image' else 'native_svg'
        if backend != expected:
            issue(source, f'{node["kind"]} paint disagrees with declared backend {backend!r}', node)
        actual_asset = Path(unquote(urlparse(node.get('image') or '').path)).name
        if actual_asset != source['graphic_asset']:
            issue(source, 'paint asset disagrees with its source mapping', node)
        if source.get('cls') == 'artboard' or source is spec:
            issue(source, 'an artboard cannot be flattened into a paint widget', node)
        if any(n.get('text') or n.get('control') for n in walk(source)):
            issue(source, 'paint fallback contains source text or controls', node)
        if node['kind'] == 'Image':
            reason = rendering.get('reason')
            if not isinstance(reason, str) or not reason.strip():
                issue(source, 'bitmap fallback lacks an explicit native limitation or source-photo reason', node)
            if reason == 'source photograph/bitmap' and not source.get('image'):
                issue(source, 'source-photo reason has no source bitmap reference', node)
            context = source.get('backdrop_context', {})
            if context.get('text_in_paint_region'):
                issue(source, 'backdrop fallback includes source text', node)
        assets.append({'source_id': source.get('object_id'),
            'source_path': source.get('source_path'), 'widget_id': node['id'],
            'kind': node['kind'], 'asset': actual_asset, 'backend': backend,
            'category': ('source_bitmap' if source.get('image') else 'unsupported_effect')
                        if node['kind'] == 'Image' else 'native_vector',
            'reason': rendering.get('reason')})

    # Text and controls must remain semantic nodes even if their graphics are
    # painted separately. The structural gate verifies their runtime state.
    for source in source_elements(spec, scale):
        if not source['required']:
            continue
        control = source.get('control')
        if control:
            expected = CONTROL_KINDS.get(control['kind'])
            wid = source.get('control_widget_id') or source.get('native_widget_id')
            matches = imported.get(wid, [])
            if not expected or len(matches) != 1 or matches[0]['kind'] != expected:
                issue(source, f'source {control["kind"]} lacks its native control widget')
        elif source.get('text'):
            wid = source.get('native_text_id') or source.get('native_widget_id')
            matches = imported.get(wid, [])
            if len(matches) != 1:
                issue(source, 'source text lacks an unambiguous native widget')
            elif matches[0]['kind'] != 'Text':
                # Rich text is a container whose individual runs are Labels.
                root = matches[0]
                descendants = {root['id']}
                for _ in range(len(nodes)):
                    expanded = descendants | {n['id'] for n in nodes if n.get('parent') in descendants}
                    if expanded == descendants:
                        break
                    descendants = expanded
                if root['kind'] != 'Stack' or not any(
                        n['kind'] == 'Text' and n['id'] in descendants for n in nodes):
                    issue(source, 'source text was replaced by non-text paint')
    return {'pass': not errors and not differences, 'errors': errors,
            'element_differences': differences, 'assets': assets,
            'node_counts': dict(collections.Counter(n['kind'] for n in nodes)),
            'asset_counts': dict(collections.Counter(a['category'] for a in assets))}


def evaluate(kit):
    out = kit['splash_makepad_dir']
    out.mkdir(parents=True, exist_ok=True)
    results = []
    applicable = kit.get('input_format') in ('design', 'l0-kit')
    for name in kit['screens']:
        if not applicable:
            row = {'pass': None, 'status': 'not_applicable', 'errors': [],
                   'element_differences': [], 'reason': 'source-mapped design importer only; legacy L0 is not certified'}
        else:
            try:
                paths = [kit['specs_dir']/f'{name}.json', out/f'{name}.portable.json']
                raw = [p.read_bytes() for p in paths]
                row = compare(*map(json.loads, raw), scale=kit.get('design_scale', 1))
                from core import semantic_policy
                snapshot_path=out/f'{name}.snapshot.json'
                semantic=semantic_policy.evaluate(kit,name,json.loads(raw[1]),
                    json.loads(snapshot_path.read_text()) if snapshot_path.exists() else {})
                row['semantic_mapping']=semantic
                row['errors'].extend(semantic['errors'])
                row['pass']=row['pass'] and semantic['pass']
                row['evidence_sha256'] = {str(p): hashlib.sha256(b).hexdigest() for p, b in zip(paths, raw)}
                if kit.get('native_widgets_first') is not True:
                    row['errors'].append('kit must enable native_widgets_first for native design acceptance')
                    row['pass'] = False
                row['status'] = 'passed' if row['pass'] else 'failed'
            except (OSError, ValueError, KeyError, TypeError) as error:
                row = {'pass': False, 'status': 'failed', 'errors': [str(error)], 'element_differences': []}
        row['screen'] = name
        (out/f'{name}.composition.json').write_text(json.dumps(row, indent=2)+'\n')
        results.append(row)
    report = {'kit': kit['name'], 'scope': 'native_widget_policy',
              'pass': bool(results) and all(r['pass'] is True for r in results) if applicable else None,
              'required': applicable, 'screens': results}
    (out/'composition-gate.json').write_text(json.dumps(report, indent=2)+'\n')
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--kit', required=True)
    report = evaluate(kitconf.load(parser.parse_args().kit))
    print(f"Native widget policy: {sum(r['pass'] is True for r in report['screens'])}/{len(report['screens'])} passed")
    for row in report['screens']:
        if row['pass'] is False:
            print(f"{row['screen']}: {len(row['element_differences'])} differences; {'; '.join(row['errors'])}")
    if report['required'] and not report['pass']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
