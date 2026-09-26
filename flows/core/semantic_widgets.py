"""Source-backed semantic boundaries for the native L0 kits.

Only complete, recognized compositions are promoted. Child paths are local to
the shared template, so neither the runtime widget nor its public API depends
on a particular Sketch instance ID.
"""
import collections
import json
import re


def walk(node, path=()):
    yield path, node
    for i, child in enumerate(node.get('c', [])):
        yield from walk(child, path+(i,))


def annotate(tree, owners, family):
    boundaries, added = {}, {}
    nodes = list(walk(tree))
    names = {n['id']: owners[n['id']].get('symbol_name') or owners[n['id']].get('name', '')
             for _, n in nodes}
    def source_root(n):
        return owners[n['id']].get('native_widget_id') == n['id']
    def tab(n):
        name=names[n['id']]
        return source_root(n) and (name.startswith(('Bar/Bottom/navTab', 'Navigation/Tab/',
                'Navigation/Tabs/Items/', 'Navigation/Appbar/Item'))
                or owners[n['id']].get('name') == 'Tab Field')
    # Source symbols sometimes wrap another instance of the same symbol.
    tab_paths=[]
    for path,n in nodes:
        if tab(n) and not any(path[:len(p)]==p for p in tab_paths): tab_paths.append(path)
    tabs={p:next(n for q,n in nodes if p==q) for p in tab_paths}
    for path,n in nodes:
        if n['t']!='stack' or not n.get('c'): continue
        own=owners[n['id']];name=names[n['id']]
        descendants=list(walk(n))
        inputs=[(p,c) for p,c in descendants if c['t']=='input']
        controls=[(p,c) for p,c in descendants if c['t'] in ('button','radio')]
        kind=None
        if source_root(n) and own.get('control',{}).get('kind')=='button' and controls:
            kind='KitButton'
        if source_root(n) and len(inputs)==1 and re.search(
                r'input with label|^input=|^Forms/Textfield/|^Inputs/Text-Field/',name,re.I):
            kind='KitFormField'
        if source_root(n) and family=='taskplan' and name=='Project Card': kind='TaskplanProjectCard'
        if source_root(n) and family=='camo' and name.startswith('UI Elements/Music/List'):
            kind='CamoTrackRow'
        # A clipped source symbol can leave only its background in the native
        # tree. That remnant is a layout/paint container, not a complete card.
        if kind in ('TaskplanProjectCard','CamoTrackRow') and not any(
                c['t']=='text' and c.get('text') for _,c in descendants):kind=None
        contained=[p for p in tab_paths if len(p)>len(path) and p[:len(path)]==path]
        # The smallest common parent owns the group, including intervening
        # source layout wrappers, never the enclosing screen.
        if 2<=len(contained)<=8 and len({p[len(path)] for p in contained})>=2 and (
                max(tabs[p].get('y',0) for p in contained)-min(tabs[p].get('y',0) for p in contained)
                < max(tabs[p].get('h',1) for p in contained)):
            kind='KitBottomNavigation' if family=='camo' and any(
                names[tabs[p]['id']].startswith('Navigation/Appbar/') for p in contained) else 'KitTabBar'
        if kind:
            boundaries[n['id']]={'widget':kind,'path':path,'node':n}
    # Prefer the outer complete field (label + input + error) over its pieces.
    for ident,b in list(boundaries.items()):
        if b['widget']=='KitFormField' and any(a['widget']=='KitFormField' and
                len(a['path'])<len(b['path']) and b['path'][:len(a['path'])]==a['path']
                for a in boundaries.values()): del boundaries[ident]
    for ident,b in boundaries.items():
        n=b['node'];kind=b['widget'];binding={};config={'widget':kind,'bindings':binding}
        def button(target):
            cid=target['id']+'_kit_button'
            child={k:target[k] for k in ('x','y','w','h')}
            child.update(t='button',id=cid,text='',enabled=1)
            target.setdefault('c',[]).insert(0,child)
            owners[cid]=owners[target['id']]
            added[cid]={'owner':target['id'],'kind':'button','reason':'native semantic component action'}
            return cid
        if kind in ('TaskplanProjectCard','CamoTrackRow'):
            button(n)
            if kind=='CamoTrackRow':
                for _,c in list(walk(n)):
                    if c['t']=='stack' and names.get(c['id'],'').startswith('Icons/') and source_root(c):
                        button(c)
        flat=list(walk(n))
        controls=[(p,c) for p,c in flat if c['t'] in ('button','radio')]
        inputs=[(p,c) for p,c in flat if c['t']=='input']
        texts=[(p,c) for p,c in flat if c['t']=='text' and c.get('text')]
        if texts:
            primary=max(texts,key=lambda pc:pc[1].get('size',0)) if kind in ('TaskplanProjectCard','CamoTrackRow') else texts[0]
            binding['title' if kind in ('TaskplanProjectCard','CamoTrackRow') else 'label']=list(primary[0])
            other=[pc for pc in texts if pc!=primary]
            pending=None
            for i,(p,c) in enumerate(other):
                role='artist' if kind=='CamoTrackRow' and i==0 else 'subtitle' if i==0 else f'detail_{i}'
                text=c.get('text','').strip()
                if kind=='TaskplanProjectCard':
                    if pending:role,pending=pending,None
                    elif text in ('Star Date','Start Date'):role,pending='start_label','start_date'
                    elif text=='Due Date':role,pending='due_label','due_date'
                    elif re.fullmatch(r'\d+(?:\.\d+)?%',text):role='progress_text'
                    elif re.fullmatch(r'\d+ Tasks?',text,re.I):role='task_count_text'
                    elif re.fullmatch(r'\+\d+',text):role='member_overflow'
                    elif text in ('Done','In Progress','To Do','Todo'):role='status'
                if role in binding:role=f'detail_{i}'
                binding[role]=list(p)
        if controls:binding['control']=list(controls[-1][0])
        if kind in ('TaskplanProjectCard','CamoTrackRow'):
            binding['control']=[0]
            config['action_bindings']={}
            for p,c in flat:
                if c['id'] in added and c['t']=='button' and p!=(0,):
                    role=re.sub(r'[^a-z0-9]+','_',names[added[c['id']]['owner']].removeprefix('Icons/').lower()).strip('_')
                    config['action_bindings'][role]=list(p)
        if inputs:binding['input']=list(inputs[0][0])
        if kind in ('KitTabBar','KitBottomNavigation'):
            config['items']=[]
            for path,t in sorted(tabs.items(),key=lambda pc:(pc[1].get('x',0),pc[1].get('y',0))):
                if path[:len(b['path'])]!=b['path']:continue
                relative=path[len(b['path']):]
                inner=list(walk(t));native=[(p,c) for p,c in inner if c['t'] in ('button','radio')]
                if not native:
                    cid=t['id']+'_kit_radio'
                    control={k:t[k] for k in ('x','y','w','h')}
                    control.update(t='radio',id=cid,variant='silent',on=0,enabled=1)
                    t.setdefault('c',[]).append(control)
                    owners[cid]=owners[t['id']]
                    added[cid]={'owner':t['id'],'kind':'radio','reason':'native control for source navigation item'}
                    native=[((len(t['c'])-1,),control)]
                labels=[(p,c) for p,c in inner if c['t']=='text']
                colors=[c.get('color',0) for p,c in labels]
                surfaces=[(p,c) for p,c in inner if c.get('variant')=='surface' and 'bg' in c
                    and not re.search(r'elevation|bounds',names[c['id']],re.I)
                    and c.get('w',0)>=t.get('w',1)*.7 and c.get('h',0)>=t.get('h',1)*.7]
                indicators=[(p,c) for p,c in inner if c.get('variant')=='surface' and 'bg' in c
                    and re.search(r'underline|indicator',names[c['id']],re.I)]
                config['items'].append({'root':list(relative),'control':list(relative+native[-1][0]),
                    'paint':[list(relative+p) for p,c in inner if c['t'] in ('text','svg')
                        and not(c['t']=='text' and c.get('text','').isdigit() and c.get('w',0)<t.get('w',1)*.4)],
                    'surfaces':[list(relative+p) for p,c in surfaces],
                    'surface_color':surfaces[0][1]['bg'] if surfaces else None,
                    'indicators':[list(relative+p) for p,c in indicators],
                    'indicator_color':indicators[0][1]['bg'] if indicators else None,
                    'source_enabled':native[-1][1].get('enabled',1)!=0,
                    'source_selected':bool(t.get('selected') or native[-1][1].get('on')),
                    'ink':max(colors,key=lambda c:c>>24) if colors else None})
            selected=[i for i,item in enumerate(config['items']) if item['source_selected']]
            inks=[item['ink'] for item in config['items']]
            if not selected and all(v is not None for v in inks):
                counts=collections.Counter(v for i,v in enumerate(inks) if config['items'][i]['source_enabled'])
                unique=[i for i,v in enumerate(inks) if config['items'][i]['source_enabled'] and counts[v]==1]
                if len(unique)==1:selected=unique
            config['selected_index']=selected[0] if len(selected)==1 else -1
            # Newly introduced native radios must express the source's selected
            # item immediately, before any click. Source controls keep their
            # existing state; only our declared additions are initialized here.
            for i,item in enumerate(config['items']):
                control=n
                for index in item['control']:control=control['c'][index]
                if control['id'] in added and control['t']=='radio':
                    control['on']=int(i==config['selected_index'])
            n['kit_index']=config['selected_index']
            config['active_color']=inks[selected[0]] if selected and inks[selected[0]] is not None else 0xff4c5fef
            config['inactive_color']=next((v for i,v in enumerate(inks)
                if i not in selected and config['items'][i]['source_enabled'] and v is not None),0xff8c8c96)
            if selected:
                config['active_surface']=config['items'][selected[0]]['surface_color']
                config['inactive_surface']=next((item['surface_color'] for i,item in enumerate(config['items'])
                    if i not in selected and item['source_enabled'] and item['surface_color'] is not None),None)
            if any(item['indicators'] for item in config['items']):
                config['active_indicator']=config['items'][selected[0]]['indicator_color'] if selected else config['active_color']
                config['inactive_indicator']=next((item['indicator_color'] for i,item in enumerate(config['items'])
                    if i not in selected and item['source_enabled'] and item['indicator_color'] is not None),None)
            binding.pop('control',None)
        n['kit']=json.dumps(config,sort_keys=True,separators=(',',':'))
        b['config']=config
    return boundaries,added


def parameters(node, config):
    """Names for public content/state inputs, independent of source IDs."""
    roles={tuple(path):role for role,path in config['bindings'].items()}
    used=collections.Counter();result={}
    for path,n in walk(node):
        for key in ('text','placeholder','enabled','on','selected','value','value2','focused','password','kit_index'):
            if key not in n:continue
            # Decoration and repeated per-item state are template details. A
            # navigation group exposes its selected index through the native
            # component API, rather than dozens of independent booleans.
            if n['t']=='button' and key=='text' and not n[key]:continue
            if config['widget'] in ('KitTabBar','KitBottomNavigation') and key in ('on','selected','enabled'):continue
            if key=='enabled' and any(k[1]=='enabled' for k in result):continue
            role=roles.get(path)
            if key=='text':
                name='value' if n['t']=='input' else role if role not in (None,'control') else 'detail'
            elif key=='on':name='checked'
            elif key=='kit_index':name='selected_index'
            else:name=key
            used[name]+=1
            result[(n['id'],key)]=name if used[name]==1 else f'{name}_{used[name]}'
    return result
