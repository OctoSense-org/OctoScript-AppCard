#!/usr/bin/env python3
"""Promote source-linked native designs to token-backed, reusable L0 kits.

The importer owns source geometry. This stage owns reusable style/compound
definitions; cards own their hierarchy, copy and control state. No artwork is
generated here, and no screen screenshot becomes a component asset.
"""
import argparse
import collections
import hashlib
import json
import pathlib
import re

from core.native_paths import repository
from core import kitconf
from core import semantic_widgets

HERE = pathlib.Path(__file__).resolve().parent
PACKS = repository('splash-makepad') / 'components/l0/native'
LAYOUT = {'x', 'y', 'w', 'h', 'src', 'image_width', 'image_height'}
PROPS = {'kit_index':'index','text': 'text', 'placeholder': 'placeholder', 'enabled': 'enabled',
         'on': 'checked', 'selected': 'selected', 'value': 'value', 'value2': 'value2',
         'focused': 'focused', 'password': 'password'}
BOOL = {'enabled', 'checked', 'selected', 'focused', 'password'}
NUMBER = {'value', 'value2', 'index'}
LEX = re.compile(r'\s*("(?:[^"\\]|\\.)*"|-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|[A-Za-z_][A-Za-z_0-9]*|[{}\[\]:,])')


def sha(value):
    return hashlib.sha256(value if isinstance(value, bytes) else
                          json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def parse_design(source):
    """Parse only the importer's data-literal subset, never evaluate code."""
    tokens, pos = [], 0
    while source[pos:].strip():
        match = LEX.match(source, pos)
        if not match:
            raise ValueError(f'non-literal native source at {pos}')
        tokens.append(match[1]); pos = match.end()
    at = 0
    def read():
        nonlocal at
        tok = tokens[at]; at += 1
        if tok == '{':
            out = {}
            while tokens[at] != '}':
                if tokens[at] == ',': at += 1; continue
                key = tokens[at]; at += 1
                if tokens[at] != ':': raise ValueError('expected property colon')
                at += 1
                if key in out: raise ValueError('duplicate native property')
                out[key] = read()
            at += 1
            return out
        if tok == '[':
            out = []
            while tokens[at] != ']':
                if tokens[at] == ',': at += 1; continue
                out.append(read())
            at += 1
            return out
        if tok in ('nil', 'null'): return None
        return json.loads(tok)
    value = read()
    if at != len(tokens) or not isinstance(value, dict):
        raise ValueError('native design must be exactly one object')
    return value


def walk(node):
    yield node
    for child in node.get('c', []): yield from walk(child)


def role(node):
    kind = node['t']
    if kind == 'text':
        return 'TextTitle' if node.get('size', 0) >= 22 else 'TextCaption' if node.get('size', 0) < 13 else 'TextBody'
    if kind == 'stack':
        return {'surface':'Surface', 'ellipse':'Surface', 'button':'Button', 'pill':'Chip',
                'radio':'Radio', 'clip':'Clip', 'glass_group':'GlassGroup',
                'glass_surface':'GlassSurface', 'glass_overlay':'GlassSurface',
                'text_runs':'RichText', 'text_shadow':'TextShadow',
                'text_shadow_label':'RichText'}.get(node.get('variant'), 'Panel' if 'bg' in node else 'Group')
    return {'input':'Field', 'svg':'Vector', 'image':'Image', 'rangeslider':'RangeSlider'}.get(kind, kind.title())


def token_group(prop):
    if prop in ('bg', 'color', 'bordercolor', 'bg2', 'bg3'): return 'color'
    if prop in ('font_src', 'size', 'weight', 'line_height', 'font_asc', 'font_desc',
                'font_line', 'font_top', 'font_baseline', 'tracking'): return 'typography'
    if prop in ('radius', 'radius2', 'border'): return 'shape'
    if prop.startswith('pad') or prop in ('gap', 'spacing'): return 'spacing'
    return 'effect'


def theme_for(kit, name, tree):
    if kit['theme'] == 'taskplan': return 'taskplan_light'
    if name.startswith('Light_'): return kit['theme_light']
    if name.startswith('Dark_'): return kit['theme']
    colors = collections.Counter(n.get('color') for n in walk(tree) if n['t'] == 'text')
    primary = colors.most_common(1)[0][0] if colors else tree.get('bg', 0xffffffff)
    rgb = [(primary >> shift) & 255 for shift in (16, 8, 0)]
    return kit['theme'] if sum(rgb) / 3 > 150 else kit['theme_light']


def source_index(spec):
    out = {}
    def visit(n, parent=None):
        for key in ('native_widget_id', 'native_text_id', 'native_paint_id', 'control_widget_id'):
            if n.get(key): out[n[key]] = n
        for c in n.get('children', []): visit(c, n)
    visit(spec)
    return out


def shape_type(prop):
    return 'bool' if prop in BOOL else 'number' if prop in NUMBER else 'text'


def definition(name, component):
    params = ['instance: text'] + [f'{p}: {shape_type(p)}' for p in component['props']]
    args = [f'component: {json.dumps(name)}', 'instance: instance'] + [f'{p}: {p}' for p in component['props']]
    children = ' { slot }' if component['slot'] else ''
    return f'component {name}({", ".join(params)}) {{\n  view Kit({", ".join(args)}){children}\n}}\n'


def semantic_tokens(pack, screens):
    """Name measured recurring values, with exact source values underneath."""
    aliases = {}
    def common(alias, prop, roles, predicate=lambda v: True):
        counts = collections.Counter()
        for component in pack['components'].values():
            ref = component['style'].get(prop, {})
            if component['role'] in roles and isinstance(ref, dict) and '$token' in ref:
                key = ref['$token']
                if predicate(pack['tokens'][key]['value']): counts[key] += component['uses']
        if counts:
            key = counts.most_common(1)[0][0]
            pack['tokens'][alias] = dict(pack['tokens'][key])
            aliases[(tuple(roles),prop,key)] = alias
    text_roles = ('TextBody','TextTitle','TextCaption','RichText','Field')
    common('color.content.primary','color',text_roles)
    common('color.surface.panel','bg',('Panel','Surface','GlassSurface'))
    common('color.action.primary','color',('Checkbox','Toggle','Radio','Slider','RangeSlider'),
           lambda v: max((v>>s)&255 for s in (16,8,0))-min((v>>s)&255 for s in (16,8,0))>40)
    for role_name, semantic in [('TextBody','body'),('TextTitle','title'),('TextCaption','caption')]:
        candidates=[c for c in pack['components'].values() if c['role']==role_name and 'font_src' in c['style']]
        if semantic in ('body','caption'):
            regular=[c for c in candidates if pack['tokens'].get(c['style'].get('weight',{}).get('$token'),{}).get('value',400)<=400]
            candidates=regular or candidates
        families=collections.Counter()
        for c in candidates:families[c['style']['font_src']['$token']]+=c['uses']
        if families:
            family=families.most_common(1)[0][0]
            candidates=[c for c in candidates if c['style']['font_src']['$token']==family]
        chosen=max(candidates,key=lambda c:c['uses']) if candidates else None
        for prop in ('font_src','size','weight','line_height'):
            ref=chosen['style'].get(prop,{}) if chosen else {}
            if '$token' in ref:
                key=ref['$token'];alias=f'typography.{semantic}.{prop}'
                pack['tokens'][alias]=dict(pack['tokens'][key])
                aliases[((role_name,),prop,key)]=alias
    common('shape.surface.radius','radius',('Surface','Panel'))
    common('effect.glass.blur','blur',('GlassSurface','GlassGroup'))
    for prop in ('pad','padleft','padright','padtop','padbottom'):
        common(f'spacing.field.{prop}',prop,('Field',))
    for component in pack['components'].values():
        for prop,ref in component['style'].items():
            if not isinstance(ref,dict) or '$token' not in ref: continue
            for (roles,expected,key),alias in aliases.items():
                if component['role'] in roles and prop==expected and ref['$token']==key:
                    ref['$token']=alias; break
    backgrounds = collections.Counter()
    spaces=collections.Counter()
    for screen in screens:
        if screen['theme']!=pack['theme']:continue
        root=screen['tree']
        full=[n['bg'] for n in walk(root) if 'bg' in n and n.get('x',0)<=0 and n.get('y',0)<=0
              and n.get('w',0)>=root['w'] and n.get('h',0)>=root['h'] and (n['bg']>>24)==255]
        if full:backgrounds[full[-1]]+=1
        for parent in walk(root):
            children=parent.get('c',[])
            for child in children:
                for axis in ('x','y'):
                    gap=round(child.get(axis,0)-parent.get(axis,0),4)
                    if 0<gap<=48:spaces[gap]+=1
    for gap,count in spaces.most_common(16):
        pack['tokens']['spacing.inset_'+str(gap).replace('.','_')]={
            'value':gap,'property':'inset','measured_uses':count,
            'source':'positive child/parent frame inset in logical points'}
    backgrounds.pop(None,None)
    if backgrounds:
        pack['tokens']['color.surface.page']={'value':backgrounds.most_common(1)[0][0],
            'property':'bg','source_instances':[{'screen':s['name'],'id':s['tree']['id']} for s in screens if s['theme']==pack['theme']][:4]}
    # Public role aliases select the most-used measured component. Variants
    # remain available by stable IDs; all aliases carry the same typed contract.
    pack['roles']={}
    by_role=collections.defaultdict(list)
    for name,c in pack['components'].items(): by_role[c['role']].append((name,c))
    for role_name,items in by_role.items():
        name,component=max(items,key=lambda pair:pair[1]['uses'])
        pack['roles'][role_name]={'component':name,'props':component['props'], 'slot':component['slot']}


def promote(key):
    kit = kitconf.load(key)
    if not kit.get('native_widgets_first'):
        raise ValueError('promote only after native-widget-first import')
    brand = kit['theme'].title()
    output = kit['cards_dir'].parent / 'l0'
    output.mkdir(parents=True, exist_ok=True)
    packs, screens = {}, []
    for name in kit['screens']:
        source = kit['cards_dir'] / f'{name}.splash'
        raw = source.read_bytes()
        tree = parse_design(raw.decode())
        spec = json.loads((kit['specs_dir'] / f'{name}.json').read_text())
        if not spec.get('native_widgets_first'): raise ValueError(f'{name}: stale non-native import')
        index = source_index(spec)
        owners = {}
        def link(n, owner=None):
            owner=index.get(n['id'],owner)
            if owner is None: raise ValueError('native component has no Sketch owner: '+n['id'])
            owners[n['id']]=owner
            for c in n.get('c',[]):link(c,owner)
        link(tree)
        semantic, added_controls = semantic_widgets.annotate(tree, owners, kit['theme'])
        theme = theme_for(kit, name, tree)
        pack = packs.setdefault(theme, {'schema_version':1, 'theme':theme, 'family':kit['theme'],
            'source_archive_sha256':spec['source_sha256'], 'tokens':{}, 'components':{}, 'compounds':{}})
        mapping, placements = {}, {}
        for node in walk(tree):
            style = {k:v for k,v in node.items() if k not in LAYOUT | set(PROPS) | {'c', 'id'}}
            props = {PROPS[k]:k for k in node if k in PROPS}
            owner=owners[node['id']]
            semantic_role=(json.loads(node['kit'])['widget'] if node.get('kit') else
                      'Tab' if owner.get('control',{}).get('semantic_role')=='tab'
                      and owner.get('native_widget_id')==node['id'] else role(node))
            component = {'role':semantic_role, 'style':style, 'props':props, 'slot':'c' in node}
            cname = brand + semantic_role + sha(component)[:10]
            if cname not in pack['components']:
                tokens = {}
                for prop, val in style.items():
                    if prop in ('t', 'variant', 'kit') or isinstance(val, (list, dict)):
                        tokens[prop] = val; continue
                    tid = f'{token_group(prop)}.{prop}_{sha(val)[:10]}'
                    pack['tokens'].setdefault(tid, {'value':val, 'property':prop, 'source_instances':[]})
                    tokens[prop] = {'$token':tid}
                pack['components'][cname] = component | {'style':tokens, 'uses':0, 'screens':[]}
            entry = pack['components'][cname]
            entry['uses'] += 1
            if name not in entry['screens']: entry['screens'].append(name)
            for val in entry['style'].values():
                if isinstance(val, dict) and '$token' in val:
                    receipt = pack['tokens'][val['$token']]['source_instances']
                    if len(receipt) < 4: receipt.append({'screen':name, 'id':node['id']})
            placements[node['id']] = {'component':cname, 'layout':{k:v for k,v in node.items() if k in LAYOUT}}
            owner = owners[node['id']]
            mapping[node['id']] = {'component':cname, 'role':component['role'], 'source_id':owner.get('object_id'),
                'source_name':owner.get('symbol_name') or owner.get('name'), 'native_id':node['id'],
                'source_design_sha256':sha(raw)}
        screens.append({'name':name, 'theme':theme, 'tree':tree, 'mapping':mapping, 'placements':placements,
                        'semantic':semantic,'added_controls':added_controls,'instances':{}})

    # Repeated small subtrees become typed compound components. Each instance
    # identity and content/state field is a prop, never a copied screen fragment.
    candidates = collections.defaultdict(list)
    def pattern(n, mapping):
        base=[mapping[n['id']]['component'], [pattern(c,mapping) for c in n.get('c',[])]]
        if n.get('kit'):
            public=semantic_widgets.parameters(n,json.loads(n['kit']))
            # Literal internal state is part of the template identity; it may
            # never be silently inherited from another source instance.
            base.append([[i,k,v] for i,c in enumerate(walk(n)) for k,v in c.items()
                         if k in PROPS and (c['id'],k) not in public])
        return base
    for screen in screens:
        for node in walk(screen['tree']):
            nodes = list(walk(node))
            fields = sum(1 + len([k for k in n if k in PROPS]) for n in nodes)
            if node.get('kit') or (2 <= len(nodes) <= 9 and fields <= 28):
                signature = sha(pattern(node,screen['mapping']))
                candidates[(screen['theme'],signature)].append((screen,node))
    compounds = {}
    for (theme,signature), uses in candidates.items():
        screen, node = uses[0]
        is_semantic=bool(node.get('kit'))
        if not is_semantic and len({s['name'] for s,n in uses}) < 2: continue
        label = screen['mapping'][node['id']].get('source_name') or role(node)
        label = ''.join(x.title() for x in re.findall('[A-Za-z0-9]+',label))[:36] or 'Composition'
        name = brand + label + signature[:8]
        if is_semantic:
            widget=json.loads(node['kit'])['widget']
            name=(widget if widget.startswith(brand) else brand+widget.removeprefix('Kit'))+signature[:8]
        params, args_by_id, internal = [], {}, []
        public=semantic_widgets.parameters(node,json.loads(node['kit'])) if is_semantic else {}
        if is_semantic:params.append('instance: text')
        for i,n in enumerate(walk(node)):
            if is_semantic:
                args = [f'component: {json.dumps(screen["mapping"][n["id"]]["component"])}',
                        'instance: instance',f'part: "p{i}"']
            else:
                params.append(f'p{i}: text')
                args = [f'instance: p{i}']
            for k in n:
                if k in PROPS:
                    if is_semantic and (n['id'],k) not in public:
                        value=bool(n[k]) if PROPS[k] in BOOL else n[k]
                        local=f'internal_{i}_{PROPS[k]}'
                        internal.append(f'  state {local} {{ shape: {shape_type(PROPS[k])}, initial: {json.dumps(value)} }}\n')
                        args.append(f'{PROPS[k]}: {local}');continue
                    prop = PROPS[k]; pname = public[(n['id'],k)] if is_semantic else f'p{i}_{prop}'
                    params.append(f'{pname}: {shape_type(prop)}'); args.append(f'{prop}: {pname}')
            args_by_id[n['id']] = args
        def body(n, depth=0):
            result = '  '*depth + ('Kit' if is_semantic else screen['mapping'][n['id']]['component']) + '(' + ', '.join(args_by_id[n['id']]) + ')'
            if 'c' in n: result += ' {\n' + '\n'.join(body(c,depth+1) for c in n['c']) + '\n' + '  '*depth + '}'
            return result
        definition_text = f'component {name}({", ".join(params)}) {{\n'+''.join(internal)+f'  view {body(node)}\n}}\n'
        packs[theme]['compounds'][name] = {'definition':definition_text, 'pattern':pattern(node,screen['mapping']),
            'uses':len(uses), 'screens':sorted({s['name'] for s,n in uses}),'semantic':is_semantic}
        compounds[(theme,signature)] = name

    for pack in packs.values(): semantic_tokens(pack,screens)
    # Both theme modes answer the same component identifiers. Shared semantic
    # tokens follow the selected mode; uncommon source effects remain explicit.
    all_components={n:c for p in packs.values() for n,c in p['components'].items()}
    all_tokens={n:t for p in packs.values() for n,t in p['tokens'].items()}
    for pack in packs.values():
        for n,c in all_components.items(): pack['components'].setdefault(n,c)
        for n,t in all_tokens.items(): pack['tokens'].setdefault(n,t)
    for theme, pack in packs.items():
        directory = PACKS/theme; directory.mkdir(parents=True,exist_ok=True)
        defaults={}
        for cname,c in pack['compounds'].items():
            if not c.get('semantic'):continue
            root=pack['components'][c['pattern'][0]]
            widget=json.loads(root['style']['kit'])['widget']
            public_name=widget if widget.startswith(brand) else brand+widget.removeprefix('Kit')
            if public_name not in defaults or c['uses']>pack['compounds'][defaults[public_name]]['uses']:
                defaults[public_name]=cname
        pack['semantic_roles']={n:{'composition':c,'definition':pack['compounds'][c]['definition'].replace(
            'component '+c+'(','component '+n+'(',1)} for n,c in defaults.items()}
        for c in pack['components'].values(): c['screens'].sort()
        (directory/'kit.json').write_text(json.dumps(pack,indent=2)+'\n')
        (directory/'tokens.json').write_text(json.dumps(pack['tokens'],indent=2)+'\n')
        library = ''.join(definition(n,c) for n,c in sorted(pack['components'].items()))
        library += ''.join(c['definition'] for n,c in sorted(pack['compounds'].items()))
        (directory/'components.l0').write_text(library)
        public=[]
        for role_name,contract in sorted(pack['roles'].items()):
            cname=contract['component'];entry=pack['components'][cname]
            public_name=brand+role_name
            if public_name in defaults:public_name+='Control'
            public.append(definition(cname,entry).replace('component '+cname+'(', 'component '+public_name+'(',1))
        public.extend(c['definition'] for _,c in sorted(pack['semantic_roles'].items()))
        (directory/'roles.l0').write_text(''.join(public))
    for screen in screens:
        theme = screen['theme']; pack = packs[theme]
        copies, states, used, used_compounds = [], [], set(), set()
        def binding(node, key):
            prop = PROPS[key]; v = node[key]
            ident = node['id'] + '_' + prop
            if prop in BOOL or prop in NUMBER or (key=='text' and node['t']=='input'):
                v = bool(v) if prop in BOOL else v
                states.append(f'state {ident} {{ shape: {shape_type(prop)}, initial: {json.dumps(v)} }}')
                return ident
            copies.append(f'copy {ident} {{ class: user-copy, en: {json.dumps(v,ensure_ascii=False)} }}')
            return 'copy.'+ident
        def call(node, depth=0):
            cname = compounds.get((theme,sha(pattern(node,screen['mapping']))))
            if cname:
                used_compounds.add(cname)
                is_semantic=pack['compounds'][cname].get('semantic',False)
                public=semantic_widgets.parameters(node,json.loads(node['kit'])) if is_semantic else {}
                args = ['instance: '+json.dumps(node['id'])] if is_semantic else []
                if is_semantic:
                    screen['instances'][node['id']]={'component':cname,'parts':{
                        f'p{i}':n['id'] for i,n in enumerate(walk(node))}}
                for i,n in enumerate(walk(node)):
                    used.add(screen['mapping'][n['id']]['component'])
                    if not is_semantic:args.append(f'p{i}: {json.dumps(n["id"])}')
                    args.extend(f'{public[(n["id"],k)] if is_semantic else f"p{i}_{PROPS[k]}"}: {binding(n,k)}'
                        for k in n if k in PROPS and (not is_semantic or (n['id'],k) in public))
                return '  '*depth + cname + '(' + ', '.join(args) + ')'
            cname = screen['mapping'][node['id']]['component']; used.add(cname)
            args = ['instance: '+json.dumps(node['id'])] + [f'{PROPS[k]}: {binding(node,k)}' for k in node if k in PROPS]
            result = '  '*depth + cname + '(' + ', '.join(args) + ')'
            if 'c' in node: result += ' {\n' + '\n'.join(call(c,depth+1) for c in node['c']) + '\n'+'  '*depth+'}'
            return result
        body = call(screen['tree'])
        library = ''.join(definition(n,pack['components'][n]) for n in sorted(used))
        library += ''.join(pack['compounds'][n]['definition'] for n in sorted(used_compounds))
        source = f'# ledger {screen["name"]}@1.0.0\n# level: L0\n# profile: ui/l0\n# Source-linked native kit. Shared definitions: components/l0/native/{theme}/components.l0\ntheme {theme}\n'
        source += '\n'.join(dict.fromkeys(copies+states))+'\n'+library+'\nview root '+body+'\n'
        (output/f'{screen["name"]}.card').write_text(source)
        native_data=json.loads((kit['cards_dir']/f'{screen["name"]}.data.json').read_text())
        (output/f'{screen["name"]}.data.json').write_text(json.dumps({'$kit':{'theme':theme,'placements':screen['placements'],
            'instances':screen['instances'],'bindings':native_data.get('$kit',{}).get('bindings',[])}},indent=2)+'\n')
        (output/f'{screen["name"]}.l0map.json').write_text(json.dumps({'theme':theme,'elements':screen['mapping'],
            'components':sorted(used), 'compounds':sorted(used_compounds),
            'semantic_widgets':{i:b['config'] for i,b in screen['semantic'].items()},
            'added_controls':screen['added_controls']},indent=2)+'\n')
    config = json.loads((HERE/'kits'/f'{key}.json').read_text())
    config.update(input_format='l0-kit', cards_dir=str(output.relative_to(HERE)),
                  splash_makepad_dir=str((output.parent/'l0-captures').relative_to(HERE)),
                  source_native_kit=key, source_designs_dir=str(kit['cards_dir'].relative_to(HERE)))
    newkey = kit['theme']+'-l0-all'
    config.pop('verdicts',None)
    (HERE/'kits'/f'{newkey}.json').write_text(json.dumps(config,indent=2)+'\n')
    summary = {'kit':newkey,'screens':len(screens),'themes':{name:{'tokens':len(p['tokens']),
        'components':len(p['components']),'compounds':len(p['compounds']),
        'reused_components':sum(len(c['screens'])>1 for c in p['components'].values())} for name,p in packs.items()},
        'layout':'source-artboard placements; responsive behavior requires separate evidence',
        'status':'generated; Studio structure and visual validation required'}
    (output/'promotion.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    return summary


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--kit',required=True)
    promote(parser.parse_args().kit)
