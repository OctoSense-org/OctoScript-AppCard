"""Describe what a native capture contains, separately from design acceptance."""
import collections
import hashlib
import json


def describe(kit):
    measured = kit.get('input_format') in ('design','l0-kit')
    promoted = kit.get('input_format') == 'l0-kit'
    out = kit['splash_makepad_dir']
    totals = collections.Counter()
    semantic_totals = collections.Counter()
    backends = collections.Counter()
    fallbacks = []
    screens = []
    for name in kit['screens']:
        path = out / f'{name}.portable.json'
        row = {'screen': name, 'manifest': path.name}
        try:
            raw = path.read_bytes()
            elements = json.loads(raw)['elements']
            if not elements:
                raise ValueError('empty generated tree')
            counts = collections.Counter(n['kind'] for n in elements)
            semantic = collections.Counter(json.loads(n['kit'])['widget'] for n in elements if n.get('kit'))
            row['semantic_widget_counts']=dict(semantic)
            semantic_totals.update(semantic)
            row.update(node_counts=dict(counts), manifest_sha256=hashlib.sha256(raw).hexdigest())
            totals.update(counts)
        except (OSError, ValueError, KeyError, TypeError) as error:
            row['error'] = str(error)
        screens.append(row)
        spec_path = kit['specs_dir']/f'{name}.json' if kit.get('specs_dir') else None
        if spec_path and spec_path.exists():
            def visit(node):
                rendering=node.get('rendering')
                if rendering:
                    backends[rendering['backend']]+=1
                    if rendering['backend']=='bitmap':
                        fallbacks.append({'screen':name,'source_id':node['object_id'],
                            'widget_id':node.get('native_widget_id'),'name':node['name'],
                            'reason':rendering.get('reason'),'asset':node.get('graphic_asset')})
                for child in node.get('children',[]): visit(child)
            try:
                visit(json.loads(spec_path.read_text()))
            except (OSError, ValueError, KeyError, TypeError) as error:
                row['error'] = f'unreadable source mapping: {error}'
        elif measured:
            row['error'] = 'missing source mapping'
    return {
        'kit': kit['name'],
        'input_format': kit.get('input_format', 'l0'),
        'native_widgets_first':kit.get('native_widgets_first',False),
        'composition_path': 'L0 components → registered theme tokens → splash-widgets native components' if promoted else 'splash_makepad::design' if measured else 'L0 component lowering',
        'layout': 'fixed Sketch coordinates / absolute positions' if measured else 'component-defined layout',
        'graphics': ('Native surfaces and tessellated SVG first; bitmap fallbacks listed per source element'
                     if kit.get('native_widgets_first') else
                     'Individual exported layers in Image widgets, including shapes and backgrounds'
                     if measured else 'See generated image nodes and component implementation'),
        'acceptance_scope': 'Configured artboard sizes, inspected structure, and reviewed screenshots',
        'acceptance_scope_id': 'fixed_artboard_parity',
        'layout_mode': 'absolute' if measured else 'component_defined',
        'not_established': ['responsive layout', 'complete application workflows'] +
                            ([] if promoted else ['reusable L0–L3 composition quality']),
        'count_basis': 'Generated portable node instances; containers include composed controls; images are not unique assets',
        'evidence_note': 'Counts describe saved manifests. See composition-gate.json for native policy and '
                         'acceptance.json for current acceptance scope and remaining composition work.',
        'complete': all('error' not in r for r in screens) and bool(screens),
        'node_counts': dict(totals),
        'semantic_widget_counts': dict(semantic_totals),
        'graphic_backends':dict(backends),
        'bitmap_fallbacks':fallbacks,
        'screens': screens,
    }


def write(kit):
    out = kit['splash_makepad_dir']
    out.mkdir(parents=True, exist_ok=True)
    path = out / 'composition.json'
    report = describe(kit)
    path.write_text(json.dumps(report, indent=2) + '\n')
    return report
