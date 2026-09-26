#!/usr/bin/env python3
"""Measured Studio/Sketch comparison. Unknown provenance is never a pass.

Studio W3/Query bounds are window-local logical points. Snapshot bounds are
desktop-global; subtract the Window snapshot origin, not a guessed DPI factor.
Sketch frames are divided by the kit's explicit design_scale.
"""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # flows/, for `core`
import argparse
import collections
import hashlib
import json
import math
import pathlib
import re

from core import kitconf

HERE = pathlib.Path(__file__).resolve().parent
TOLERANCES = {'position_pt': 4, 'dimension_pt': 6, 'alignment_pt': 4,
              'spacing_pt': 4, 'clipping_pt': 2, 'inspection_pt': 1}


def norm(text):
    return re.sub(r'\s+', ' ', text or '').strip().casefold()


def rect(node):
    return [node[k] for k in ('x', 'y', 'width', 'height')]


def graphic_paint_is_owned(spec, source, owner, paint, imported, actual):
    if paint.get('image') != owner.get('image'):
        return False
    if paint.get('parent') == owner['id']:
        return True
    # A rotated graphic's painted extent can overlap deferred glass even when
    # its thin source frame does not. The importer explicitly routes that paint
    # through one inspected overlay, retaining its exact source owner.
    paint_id=source['native_paint_id']
    wrappers=imported.get(paint_id+'_foreground',[])
    if paint_id not in spec.get('glass_foreground_routes',[]) or len(wrappers)!=1:
        return False
    wrapper=wrappers[0]
    return (wrapper.get('kind')=='Stack' and wrapper.get('parent')==owner['id']
            and paint.get('parent')==wrapper['id']
            and actual.get(wrapper['id'],{}).get('type')=='DesignOverlay')


def numerical_paint_is_owned(source, owner_id, plot, imported, actual, tolerance):
    if plot.get('parent')==owner_id:
        return True
    # The importer can preserve a source mask as one explicit clip View.
    # Its identity, immediate ancestry and inspected extent must all agree.
    wrappers=imported.get(source['native_data_widget_id']+'_clip',[])
    if len(wrappers)!=1:
        return False
    wrapper=wrappers[0];seen=actual.get(wrapper['id'],{})
    expected=source.get('native_data_bounds_logical') or []
    return (plot.get('parent')==wrapper['id'] and wrapper.get('parent')==owner_id
            and wrapper.get('kind')=='Stack' and seen.get('type')=='View'
            and len(expected)==4 and len(seen.get('bounds',[]))==4
            and all(abs(a-b)<=tolerance for a,b in zip(expected,seen['bounds'])))


def parse_dump(dump):
    lines = dump.strip().splitlines()
    if not lines or not lines[0].startswith('W3 '):
        raise ValueError('missing W3 widget hierarchy')
    rows = []
    for line in lines[1:]:
        parts = line.split()
        if len(parts) != 8:
            raise ValueError(f'invalid W3 row: {line}')
        i, parent, wid, kind, x, y, w, h = parts
        rows.append({'index': int(i), 'parent_index': int(parent), 'id': wid,
                     'type': kind, 'bounds': list(map(float, (x, y, w, h)))})
    if len(rows) != int(lines[0].split()[1]):
        raise ValueError('truncated W3 widget hierarchy')
    indices = {r['index']: r for r in rows}
    for r in rows:
        parent = indices.get(r['parent_index'])
        r['parent'] = parent['id'] if parent else None
        if r['parent_index'] != -1 and not parent:
            raise ValueError('broken W3 parent reference')
    return rows


def source_elements(spec, scale):
    """Retain the complete hierarchy and stable instance-qualified Sketch IDs.

    Every painted leaf, text and image intersecting the artboard is required.
    Vector subpaths remain auditable; unsupported mappings fail closed. Pure
    layout groups, masks, transparent and off-artboard nodes are documented
    separately, rather than counted as missing visible content.
    """
    rows = []
    fw, fh = spec['w'] / scale, spec['h'] / scale
    def visit(n, parent, path, opacity, hidden=False):
        sid = '/'.join(path + [n.get('object_id') or 'node'])
        box = [n.get(k, 0) / scale for k in ('x', 'y', 'w', 'h')]
        opacity *= n.get('opacity', 1)
        x, y, w, h = box
        stroke = n.get('stroke',{}).get('w',0)/scale
        if stroke > 0:
            if w == 0: x -= stroke/2; w = stroke
            if h == 0: y -= stroke/2; h = stroke
        hidden=hidden or n.get('fully_clipped',False)
        masks=n.get('graphic_masks',[])
        invalid_clipping_claim=n.get('fully_clipped',False) and not masks
        # Sketch frames precede rotation. Use the painted extent to decide
        # intersection, while retaining the original frame for layout checks.
        angle=math.radians(n.get('rot',0))
        vw=abs(w*math.cos(angle))+abs(h*math.sin(angle))
        vh=abs(w*math.sin(angle))+abs(h*math.cos(angle))
        vx,vy=x+(w-vw)/2,y+(h-vh)/2
        visible = (not hidden and n.get('visible', True) and opacity > .01 and w > 0 and h > 0
                   and vx < fw and vy < fh and vx+vw > 0 and vy+vh > 0)
        text = n.get('text', {}).get('string')
        image = n.get('image')
        painted = (n.get('fill', {}).get('a', 0) > .01 if n.get('fill') else False)
        painted |= bool(n.get('gradient') or n.get('border') or n.get('borders') or n.get('stroke'))
        required = visible and not n.get('mask') and not n.get('graphic_part_of') and not n.get('control_part_of') and bool(
            text or image or n.get('control') or n.get('graphic_asset') or (painted and not n.get('children')))
        row = {'id': sid, 'object_id': n.get('object_id'), 'parent': parent,
               'native_widget_id': n.get('native_widget_id'),
               'invalid_clipping_claim':invalid_clipping_claim,
               'graphic_part_of': n.get('graphic_part_of'), 'graphic_asset': n.get('graphic_asset'),
               'native_paint_id': n.get('native_paint_id'),
               'native_data_widget_id': n.get('native_data_widget_id'),
               'native_data_bounds_logical': n.get('native_data_bounds_logical'),
               'control': n.get('control'), 'control_part_of': n.get('control_part_of'),
               'control_widget_id': n.get('control_widget_id'),
               'native_text_id':n.get('native_text_id'),
               'source_clip_bounds':[v/scale for v in n['source_clip_bounds']] if n.get('source_clip_bounds') else None,
               'paint_bounds': [v/scale for v in n['paint_bounds']] if n.get('paint_bounds') else None,
               'name': n.get('name'), 'kind': n.get('cls'), 'bounds': box,
               'symbol_name': n.get('symbol_name'),
               'visibility_bounds':[vx,vy,vw,vh],
               'text': text, 'image': image, 'visible': visible, 'required': required,
               'source_text_rows':n.get('text',{}).get('source_rows',1),
               'source_line_height':n.get('text',{}).get('line_height',0)/scale,
               'source_baseline':n.get('text',{}).get('native_baseline',0)/scale,
               'mask': bool(n.get('mask')), 'rotation': n.get('rot', 0)}
        rows.append(row)
        for i, child in enumerate(n.get('children', [])):
            visit(child, sid, path + [n.get('object_id') or 'node', str(i)], opacity,hidden)
    visit(spec, None, [], 1)
    return rows


def compare(spec, portable, dump, snapshot, queries, scale=1, tolerances=None, layout=None):
    tol = TOLERANCES | (tolerances or {})
    errors, differences, relations = [], [], []
    try:
        tree = parse_dump(dump.get('dump', ''))
    except (ValueError, TypeError) as e:
        tree = []
        errors.append(str(e))
    nodes = portable.get('elements', [])
    ids = [n['id'] for n in nodes]
    if not ids or len(set(ids)) != len(ids):
        errors.append('missing or duplicate generated widget IDs')
    trees = {n['id']: n for n in tree}
    snaps = {n['id']: n for n in snapshot.get('widgets', [])}
    if not any(i in trees and i in snaps for i in ids):
        errors.append('host-only inspection: no generated widgets in tree and snapshot')
    sources = source_elements(spec, scale)
    for s in sources:
        if s.get('invalid_clipping_claim'):
            errors.append(f"{s['object_id']}: source visibility suppressed without a source mask")
    if spec.get('native_widgets_first'):
        def check_rendering(node):
            if node.get('graphic_asset'):
                rendering=node.get('rendering',{})
                if rendering.get('backend') not in ('native_surface','native_svg','bitmap'):
                    errors.append(f"{node['object_id']}: missing native-first graphic decision")
                elif rendering['backend']=='bitmap' and not rendering.get('reason'):
                    errors.append(f"{node['object_id']}: bitmap fallback lacks an explicit limitation")
            for child in node.get('children',[]):check_rendering(child)
        check_rendering(spec)
    src = {s['id']: s for s in sources}
    control_roles = {'Text Input':'text_input','Text Input/chevron':'text_input',
                     'Search':'text_input','Text Area':'text_input',
                     'Code Input':'text_input','Radio Button':'radio','Tab Field':'tab'}
    for source in sources:
        # An artboard titled Search or Tab is a canvas, not a control instance.
        if source['kind']=='artboard':continue
        role = control_roles.get(source.get('name'))
        name=source.get('name') or ''
        if name=='Search' and source['kind']=='text':role=None
        if name.startswith('Textfield/'): role='text_input'
        elif name.startswith('Component/Checkbox/'): role='checkbox'
        elif name.startswith('Component/Toggle/Switch-'): role='toggle'
        elif name=='Component/Toggle/Pill':role='checkbox'
        elif name=='slider':role='slider'
        variant=source.get('symbol_name') or name
        if variant.startswith(('Inputs/Text-Field/','Inputs/Code/')):role='text_input'
        elif variant.startswith('Inputs/Selector/Checkbox/'):role='checkbox'
        elif variant.startswith('Inputs/Selector/Radio-Button/'):role='radio'
        elif variant.startswith('Inputs/Switch-Toggle/'):role='toggle'
        elif variant.startswith(('Buttons/','Inputs/Dropdown','Navigation/Tabs/Items/','Navigation/Appbar/Item')):role='button'
        if role and source['visible']:
            # Sketch detachment can retain an inner styling group named after
            # its owning symbol. That group shares the symbol's control; it is
            # not another hit target. Require matching symbol provenance so an
            # unrelated outer control cannot conceal a missing inner control.
            owner=source
            if not source.get('symbol_name'):
                owners=[s for s in sources if s.get('symbol_name')==variant
                        and source['id'].startswith(s['id']+'/')]
                if owners:owner=max(owners,key=lambda s:len(s['id']))
                elif role=='button' and variant.startswith(('Buttons/','Inputs/Dropdown/')):
                    boundaries=[s for s in sources if s.get('symbol_name')
                                and source['id'].startswith(s['id']+'/')]
                    boundary=max(boundaries,key=lambda s:len(s['id'])) if boundaries else None
                    if boundary and boundary['symbol_name'].startswith('Inputs/Code/'):
                        # Camo reuses a button-shaped background inside a code
                        # cell. The owning symbol is an editable input, so its
                        # styling prototype must not create a second hit target.
                        owner,role=boundary,'text_input'
                    elif boundary and boundary['symbol_name']=='Inputs/Dropdown' and variant.startswith('Inputs/Dropdown/'):
                        owner=boundary
            descendants = [s for s in sources if s['id'] == owner['id'] or s['id'].startswith(owner['id']+'/')]
            def matches_role(s):
                control=s.get('control') or {}
                if control.get('kind') in (('slider','range_slider') if role=='slider' else (role,)):
                    return True
                # Makepad's Tab is not a standalone Widget. The importer can
                # explicitly adapt selection to RadioButton; the native type,
                # ownership and checked state are still verified below.
                return (role=='tab' and spec.get('native_widgets_first')
                        and control.get('kind')=='radio'
                        and control.get('semantic_role')=='tab'
                        and bool(control.get('adapter')))
            if not any(matches_role(s) for s in descendants):
                errors.append(f"{source['id']}: Sketch {role} lacks native control mapping")
    windows = {s['id']: s for s in snapshot.get('widgets', []) if s['widget_type'] == 'Window'}
    actual = {}
    clips = {e['id']:e for e in (layout or {}).get('elements',[])}
    for n in nodes:
        wid = n['id']
        t, s = trees.get(wid), snaps.get(wid)
        if not t or not s:
            errors.append(f'{wid}: missing from WidgetTreeDump or WidgetSnapshot')
            continue
        win = windows.get(s.get('window_id'))
        if not win:
            errors.append(f'{wid}: missing snapshot window origin')
            continue
        box = rect(s)
        box[0] -= win['x']
        box[1] -= win['y']
        if max(abs(a-b) for a, b in zip(box, t['bounds'])) > tol['inspection_pt']:
            errors.append(f'{wid}: tree/snapshot bounds disagree')
        # Exact ID queries avoid the broad-query 256-row truncation limit.
        q = queries.get(wid, {})
        parsed = []
        for line in q.get('rects', []):
            p = line.split()
            if len(p) == 7 and p[1] == wid:
                parsed.append(list(map(float, p[3:])))
        precise = clips.get(wid, {}).get('bounds', box)
        if precise[2] > 0 and precise[3] > 0 and (len(parsed) != 1 or
                max(abs(a-b) for a, b in zip(box, parsed[0])) > tol['inspection_pt']):
            errors.append(f'{wid}: WidgetQuery missing, ambiguous or inconsistent')
        actual[wid] = {'bounds': box, 'parent': t['parent'], 'type': s['widget_type'],
                       **{k: s.get(k) for k in ('visible', 'enabled', 'text', 'value', 'checked', 'selected')}}
        measured = clips.get(wid)
        if not measured:
            errors.append(f'{wid}: missing native clipping measurement')
        elif max(abs(a-b) for a,b in zip(box,measured['bounds'])) > tol['inspection_pt']:
            errors.append(f'{wid}: native layout/Studio bounds disagree')
        else:
            # Studio's compact protocol rounds coordinates to integers. After
            # cross-checking it, retain native subpixel dimensions for thin paths.
            actual[wid]['bounds'] = clips[wid]['bounds']
            actual[wid]['clipped_bounds'] = measured['clipped_bounds']
            actual[wid]['focused'] = measured.get('focused')
            actual[wid]['password'] = measured.get('password')
            actual[wid]['text_layout'] = measured.get('text_layout')
            actual[wid]['text_clip'] = measured.get('text_clip')
            actual[wid]['rotation_degrees']=measured.get('rotation_degrees')
        # Compare generated ancestry through any native helper wrappers.
        expected_parent = n.get('parent')
        parent = t['parent']
        seen = set()
        while parent and parent not in ids and parent not in seen:
            seen.add(parent)
            parent = trees.get(parent, {}).get('parent')
        if parent != expected_parent:
            errors.append(f'{wid}: generated hierarchy changed: {parent} != {expected_parent}')
        expected_text = n.get('text')
        if expected_text and norm(s.get('text') or s.get('value')) != norm(expected_text):
            errors.append(f'{wid}: native text/value differs from generated content')
        for expected, measured in (('enabled', 'enabled'), ('on', 'checked')):
            if n.get(expected) is not None and s.get(measured) != bool(n[expected]):
                errors.append(f'{wid}: native {measured} state missing or incorrect')
        if n.get('focused') is not None and actual[wid].get('focused') != bool(n['focused']):
            errors.append(f'{wid}: native focus state missing or incorrect')
        if n.get('kind') == 'Input':
            if actual[wid].get('password') != bool(n.get('password')):
                errors.append(f'{wid}: native password masking state missing or incorrect')
            if s.get('widget_type') != 'TextInput' or s.get('value') != (n.get('text') or ''):
                errors.append(f'{wid}: native editable input or value missing')
            if not n.get('text') and s.get('text') != (n.get('placeholder') or ''):
                errors.append(f'{wid}: native placeholder missing or incorrect')
        if spec.get('reference_renderer') == 'Sketch' and n.get('kind') == 'Image':
            pixels = clips.get(wid, {}).get('image_pixels')
            if not pixels or len(pixels) != 2 or min(pixels) <= 0:
                errors.append(f'{wid}: native image texture not ready')
        if spec.get('reference_renderer') == 'Sketch' and n.get('kind') == 'Svg':
            if not clips.get(wid,{}).get('vector_ready') or s.get('widget_type') not in ('Svg','DesignGlassSvg'):
                errors.append(f'{wid}: native SVG geometry not ready')
        if s.get('widget_type') in ('GaussRoundedView','DesignGlassSvg') and not clips.get(wid,{}).get('glass_ready'):
            errors.append(f'{wid}: native backdrop texture not ready')
        if spec.get('reference_renderer') == 'Sketch' and s.get('widget_type') == 'Label':
            if not clips.get(wid, {}).get('text_layout'):
                errors.append(f'{wid}: native text layout measurement missing')
        if n.get('selected') is not None and s.get('selected') != str(bool(n['selected'])).lower():
            errors.append(f'{wid}: native selected state missing or incorrect')

    # Content-based provenance first. Never choose the nearest widget by its
    # measured geometry: that would let a layout defect change the mapping.
    mappings, used = {}, set()
    # An imported design carries an exact, instance-qualified source ID through
    # the checked VM. Join those identities before legacy content heuristics.
    imported = collections.defaultdict(list)
    for n in nodes:
        if n.get('original_id'):
            imported[n['original_id']].append(n)
    for s in sources:
        if not s.get('native_widget_id'):
            continue
        candidates = imported[s['native_widget_id']]
        if len(candidates) == 1 and candidates[0]['id'] in actual:
            n = candidates[0]
            mappings[s['id']] = {'widget_id': n['id'], 'method': 'sketch_object_id'}
            used.add(n['id'])
            source_text = (s.get('control') or {}).get('display_text', s.get('text'))
            if source_text and norm(source_text) != norm(n.get('text') or n.get('placeholder')):
                errors.append(f"{n['id']}: generated text differs from Sketch")
            if s.get('control'):
                control_actual = actual[n['id']]
                if s.get('control_widget_id'):
                    controls = imported[s['control_widget_id']]
                    if len(controls) != 1 or controls[0]['id'] not in actual or controls[0].get('parent') != n['id']:
                        errors.append(f"{n['id']}: missing native control child")
                        control_actual = {}
                    else:
                        control_actual = actual[controls[0]['id']]
                        used.add(controls[0]['id'])
                if s['control'].get('kind') == 'text_input' and control_actual.get('type') != 'TextInput':
                    errors.append(f"{n['id']}: Sketch input mapped to a noneditable widget")
                if spec.get('native_widgets_first'):
                    expected_type={'button':'Button','checkbox':'CheckBox','toggle':'CheckBox','radio':'RadioButton','slider':'Slider','range_slider':'Slider'}.get(s['control'].get('kind'))
                    if expected_type and control_actual.get('type')!=expected_type:
                        errors.append(f"{n['id']}: source control must use native {expected_type}")
                for field in ('checked','enabled','selected','value','focused','password'):
                    if field=='value' and s['control']['kind'] in ('slider','range_slider'):
                        try:
                            values=json.loads(control_actual.get('value') or '')
                            expected=s['control']['value']
                            pairs=zip(values,expected) if isinstance(expected,list) and isinstance(values,list) and len(values)==len(expected) else [(values,expected)]
                            if any(abs(a-b)>1e-5 for a,b in pairs):raise ValueError('slider value differs')
                        except (TypeError,ValueError):
                            errors.append(f"{n['id']}: native slider value differs from source handle positions")
                        continue
                    if field in s['control'] and control_actual.get(field) != s['control'][field]:
                        errors.append(f"{n['id']}: native control {field} differs from Sketch variant")
            if s.get('graphic_asset') and pathlib.Path(n.get('image') or '').name != s['graphic_asset']:
                errors.append(f"{n['id']}: generated graphic differs from Sketch export")
            if s.get('native_paint_id'):
                paints = imported[s['native_paint_id']]
                if len(paints) != 1 or paints[0]['id'] not in actual:
                    errors.append(f"{n['id']}: missing inspected graphic paint widget")
                else:
                    paint = paints[0]
                    used.add(paint['id'])
                    if not graphic_paint_is_owned(spec,s,n,paint,imported,actual):
                        errors.append(f"{n['id']}: graphic paint provenance mismatch")
                    delta = [round(a-b,3) for a,b in zip(actual[paint['id']]['bounds'], s['paint_bounds'])]
                    differences.append({'sketch_id':s['id']+'/paint', 'name':s['name']+' paint',
                        'widget_id':paint['id'], 'expected_bounds':s['paint_bounds'],
                        'actual_bounds':actual[paint['id']]['bounds'], 'delta':delta,
                        'issues':['graphic_paint_bounds'] if any(abs(v)>tol['inspection_pt'] for v in delta) else []})
            if s.get('native_text_id'):
                texts=imported[s['native_text_id']]
                if len(texts)!=1 or texts[0]['id'] not in actual:
                    errors.append(f"{n['id']}: clipped source text lacks native inspection")
                elif s.get('source_clip_bounds'):
                    measured=actual[texts[0]['id']].get('clipped_bounds',[])
                    expected=s['source_clip_bounds']
                    if len(measured)!=4 or any(abs(a-b)>tol['clipping_pt'] for a,b in zip(measured,expected)):
                        errors.append(f"{n['id']}: native text clipping differs from source mask")
    for s in sources:
        owner = s.get('graphic_part_of') or s.get('control_part_of')
        if owner:
            ancestor = src.get(s['parent'])
            while ancestor and ancestor.get('native_widget_id') != owner:
                ancestor = src.get(ancestor.get('parent'))
            if not ancestor and s.get('control_part_of'):
                # Explicit sibling password circles may belong to a text input
                # in another source group. Require a source mask identity and
                # containment, never infer ownership from proximity alone.
                candidate=next((n for n in sources if n.get('native_widget_id')==owner),None)
                control=(candidate or {}).get('control') or {}
                mask_id=control.get('graphic_mask_source_id')
                chain=s
                while chain and chain.get('object_id')!=mask_id:chain=src.get(chain.get('parent'))
                if chain and control.get('kind')=='text_input' and control.get('password'):
                    x,y,w,h=s['bounds'];cx,cy,cw,ch=candidate['bounds']
                    if x>=cx and y>=cy and x+w<=cx+cw and y+h<=cy+ch:ancestor=candidate
            coverage = 'control' if s.get('control_part_of') else 'graphic_asset'
            quantitative=False
            if ancestor and ancestor.get('native_data_widget_id') and ancestor['id'] in mappings:
                plots=imported.get(ancestor['native_data_widget_id'],[])
                if len(plots)==1:
                    plot=plots[0];observed=actual.get(plot['id'],{})
                    expected=ancestor.get('native_data_bounds_logical') or []
                    quantitative=(plot.get('kind') in ('StockPlot','Progress')
                        and numerical_paint_is_owned(ancestor,mappings[ancestor['id']]['widget_id'],plot,imported,actual,tol['inspection_pt'])
                        and observed.get('type') in ('LinePlot','DonutChart','BarPlot','RadarChart','ScatterPlot','DesignProgressBar')
                        and len(expected)==4 and len(observed.get('bounds',[]))==4
                        and all(abs(a-b)<=tol['inspection_pt'] for a,b in zip(expected,observed['bounds'])))
            if (not ancestor or not (ancestor.get(coverage) or quantitative) or ancestor['id'] not in mappings
                    or s.get('text') or s.get('image')):
                errors.append(f"{s['id']}: invalid compound graphic coverage")
    for field, method in (('text', 'exact_text'), ('image', 'image_asset')):
        left, right = collections.defaultdict(list), collections.defaultdict(list)
        for s in sources:
            if s['required'] and s.get(field) and s['id'] not in mappings and not s.get('native_widget_id'):
                key = norm(s[field]) if field == 'text' else pathlib.Path(str(s[field])).stem
                left[key].append(s)
        for n in nodes:
            v = (n.get('text') or n.get('placeholder')) if field == 'text' else n.get('image')
            if v and n['id'] in actual and n['id'] not in used:
                key = norm(v) if field == 'text' else pathlib.Path(str(v)).stem
                right[key].append(n)
        for key, refs in left.items():
            candidates = right.get(key, [])
            # Repeated labels map by document/preorder when multiplicities
            # agree; a missing duplicate remains explicitly ambiguous.
            if len(refs) != len(candidates):
                continue
            for s, n in zip(refs, candidates):
                if n['id'] not in used:
                    mappings[s['id']] = {'widget_id': n['id'], 'method': method + ('_preorder' if len(refs)>1 else '')}
                    used.add(n['id'])

    # Containers map by the exact set of anchored descendants. This preserves
    # logical grouping without pretending every Sketch vector path is a widget.
    def ancestors(key, table):
        found = set()
        while key in table and key not in found:
            found.add(key)
            key = table[key].get('parent')
        return found
    node_table = {n['id']: n for n in nodes}
    anchor_widgets = set(used)
    for s in sources:
        if s['id'] in mappings or s.get('native_widget_id') or not s['visible'] or s.get('text') or s.get('image'):
            continue
        anchors = {m['widget_id'] for sid, m in mappings.items()
                   if m['method'].startswith(('exact_text','image_asset')) and s['id'] in ancestors(sid, src)}
        if len(anchors) < 2:
            continue
        candidates = []
        for n in nodes:
            if n['id'] in used or n['id'] not in actual:
                continue
            members = {wid for wid in anchor_widgets if n['id'] in ancestors(wid, node_table)}
            if members == anchors:
                candidates.append(n)
        if candidates:
            # Deepest common container, independent of measured coordinates.
            n = max(candidates, key=lambda n: len(ancestors(n['id'], node_table)))
            mappings[s['id']] = {'widget_id': n['id'], 'method': 'descendant_anchors'}
            used.add(n['id'])

    fw, fh = spec['w']/scale, spec['h']/scale
    for s in sources:
        mapping = mappings.get(s['id'])
        if not mapping:
            if s['required']:
                differences.append({'sketch_id': s['id'], 'name': s['name'], 'text': s['text'],
                    'expected_bounds': s['bounds'], 'issues': ['missing_or_unmapped_element']})
            continue
        wid = mapping['widget_id']
        a = actual[wid]
        delta = [round(v-e, 3) for v, e in zip(a['bounds'], s['bounds'])]
        issues = []
        if any(abs(v)>tol['position_pt'] for v in delta[:2]): issues.append('position')
        if any(abs(v)>tol['dimension_pt'] for v in delta[2:]): issues.append('dimensions')
        if not a['visible']: issues.append('invisible')
        x,y,w,h = a['bounds']
        sx,sy,sw,sh = s['bounds']
        # Compare to expected artboard overflow: intentional crop in Sketch
        # is allowed; new overflow of an otherwise visible element is not.
        overflow = [max(0,-x), max(0,-y), max(0,x+w-fw), max(0,y+h-fh)]
        expected = [max(0,-sx),max(0,-sy),max(0,sx+sw-fw),max(0,sy+sh-fh)]
        if any(v-e>tol['clipping_pt'] for v,e in zip(overflow,expected)) or w<=0 or h<=0:
            issues.append('clipping_or_empty_bounds')
        clipped = a.get('clipped_bounds',a['bounds'])
        if (w-clipped[2] > expected[0]+expected[2]+tol['clipping_pt'] or
                h-clipped[3] > expected[1]+expected[3]+tol['clipping_pt']):
            issues.append('native_ancestor_clipping')
        text_actual=a
        if s.get('native_text_id') and len(imported[s['native_text_id']])==1:
            text_actual=actual.get(imported[s['native_text_id']][0]['id'],a)
        text_layout = text_actual.get('text_layout')
        if s.get('text') and s.get('rotation') and abs((text_actual.get('rotation_degrees') or 0)+s['rotation'])>.01:
            issues.append('native_text_rotation_differs')
        if s['source_baseline'] > h + tol['clipping_pt'] and text_actual.get('text_clip',[False,False]) == [True,True]:
            issues.append('source_glyph_overflow_clipped')
        # Sketch can intentionally clip a text layer (e.g. a text area showing
        # part of its third line). Its native SVG export establishes row count.
        expected_text_height = s['source_text_rows']*s['source_line_height'] or h
        if text_layout and (text_layout[2] > w+tol['clipping_pt']
                            or text_layout[3] > expected_text_height+tol['clipping_pt']):
            issues.append('native_text_layout_overflow')
        differences.append({'sketch_id':s['id'], 'name':s['name'], 'text':s['text'], **mapping,
            'expected_bounds':s['bounds'], 'actual':a, 'delta_xywh_pt':delta, 'issues':issues})

    mapped = [d for d in differences if 'widget_id' in d]
    # Compare alignment and gap for consecutive mapped siblings in Sketch's
    # hierarchy. The position test already covers items in different groups.
    siblings = collections.defaultdict(list)
    for d in mapped:
        if d['sketch_id'] in src:
            siblings[src[d['sketch_id']]['parent']].append(d)
    for group in siblings.values():
        for axis, start, size in (('vertical',1,3),('horizontal',0,2)):
            ordered = sorted(group, key=lambda d:d['expected_bounds'][start])
            for a,b in zip(ordered,ordered[1:]):
                ea,eb = a['expected_bounds'],b['expected_bounds']
                aa,ab = a['actual']['bounds'],b['actual']['bounds']
                cross = 1-start
                # Only peers sharing an edge/center in the design form a row
                # or column; do not infer spacing between diagonal elements.
                expected_align = eb[cross]-ea[cross]
                if abs(expected_align)>tol['alignment_pt']: continue
                gap = eb[start]-ea[start]-ea[size]
                if gap < -tol['clipping_pt']: continue
                gap_delta = ab[start]-aa[start]-aa[size]-gap
                align_delta = ab[cross]-aa[cross]-expected_align
                issues = []
                if abs(gap_delta)>tol['spacing_pt']: issues.append('spacing')
                if abs(align_delta)>tol['alignment_pt']: issues.append('alignment')
                relations.append({'from':a['sketch_id'],'to':b['sketch_id'],'axis':axis,
                    'expected_gap_pt':round(gap,3),'gap_delta_pt':round(gap_delta,3),
                    'alignment_delta_pt':round(align_delta,3),'issues':issues})
    failures = sum(bool(d['issues']) for d in differences)+sum(bool(r['issues']) for r in relations)
    return {'schema':1, 'pass':not errors and not failures, 'inspection_pass':not errors,
            'tolerances':tol, 'units':'logical points; Sketch frame/design_scale',
            'inspection_errors':errors, 'generated_nodes':len(nodes), 'inspected_nodes':len(actual),
            'required_sketch_elements':sum(s['required'] for s in sources),
            'mapped_elements':len(mapped), 'failed_checks':failures, 'elements':differences,
            'relations':relations, 'sketch_hierarchy':sources, 'native_hierarchy':tree,
            'unmapped_widgets':[{'generated':n, 'actual':actual.get(n['id'])} for n in nodes if n['id'] not in used]}


def evaluate(kit, name, verify_capture=False):
    out = kit['splash_makepad_dir']
    def read(suffix):
        return json.loads((out/f'{name}.{suffix}.json').read_text())
    paths = [out/f'{name}.{s}.json' for s in ('portable','widgets','snapshot','queries','layout')]
    paths += [kit['specs_dir']/f'{name}.json', pathlib.Path(__file__)]
    try:
        report = compare(json.loads(paths[-2].read_text()), read('portable'), read('widgets'),
                         read('snapshot'), read('queries'), kit['design_scale'], kit.get('structure_tolerances'), read('layout'))
        report['inputs'] = hashlib.sha256(b''.join(p.read_bytes() for p in paths)).hexdigest()
        if verify_capture:
            from core import render_splash_makepad as native
            card,data,spec=native.selected_inputs(kit,name)
            inputs=native.fingerprint([*native.shared_inputs(kit),card,data,spec])
            meta=read('capture')
            if not native.fresh(meta,inputs,out/f'{name}.png'):
                report['inspection_errors'].append('stale or altered capture/inspection evidence; rerender')
            build=meta.get('build_id')
            runtime=read('runtime-errors')
            if runtime.get('requested_build_id')!=build or runtime.get('done') is not True or runtime.get('entries'):
                report['inspection_errors'].append('missing or failed current Studio runtime/shader error inspection')
            if any(read(s).get('build_id')!=build for s in ('widgets','snapshot')):
                report['inspection_errors'].append('inspection evidence came from another build')
            if read('layout').get('nonce')!=meta.get('request',{}).get('nonce'):
                report['inspection_errors'].append('clipping measurements came from another mount')
            if report['inspection_errors']:
                report.update(inspection_pass=False, **{'pass':False})
    except (OSError, ValueError, KeyError, TypeError) as e:
        report = {'pass':False,'inspection_pass':False,'inspection_errors':[str(e)],'elements':[]}
    report['screen'] = name
    (out/f'{name}.structure.json').write_text(json.dumps(report, indent=2)+'\n')
    return report


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--kit',required=True)
    args=p.parse_args()
    kit=kitconf.load(args.kit)
    rows=[evaluate(kit,n,verify_capture=True) for n in kit['screens']]
    for r in rows:
        print(f"{r['screen']}: structure {'PASS' if r['pass'] else 'FAIL'}; "
              f"inspection {'PASS' if r['inspection_pass'] else 'FAIL'}; "
              f"{r.get('mapped_elements',0)} mapped; {r.get('failed_checks',0)} differences")
    if not all(r['pass'] for r in rows):
        raise SystemExit(1)


if __name__=='__main__': main()
