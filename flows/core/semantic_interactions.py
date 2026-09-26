"""Studio proofs for the behavior owned by composed native widgets."""
import json
import pathlib
import time


def check_progress(bridge,build,name,portable,out,remount,save_screenshot,sha):
    """Change each value and inspect both the model and the actual paint input."""
    nodes=[n for n in portable['elements'] if n.get('kind')=='Progress']
    if not nodes:return []
    from PIL import Image,ImageChops
    request,result=remount(name,bootstrap=True)
    state_path=pathlib.Path(request['semantic_result'])
    def current():
        state=json.loads(state_path.read_text())
        if state.get('nonce')!=request['nonce'] or state.get('build_id')!=build:
            raise RuntimeError('stale progress probe state')
        return state
    deadline=time.monotonic()+15
    while time.monotonic()<deadline:
        try:
            state=current()
            if result.exists():break
        except (OSError,ValueError,RuntimeError):pass
        time.sleep(.1)
    else:raise RuntimeError('progress probe did not mount')
    time.sleep(.5)
    files=[];checks=[];path=out/f'{name}.progress-interactions.json'
    layout={n['id']:n for n in json.loads((out/f'{name}.layout.json').read_text())['elements']}
    def shot(suffix):
        bridge.send('Screenshot',{'build_id':build,'kind_id':0})
        image=out/f'{name}.{suffix}.png';save_screenshot(bridge.wait('Screenshot'),image);files.append(image)
        return image
    for node in nodes:
        ident=node['original_id'];before=current()['elements'][ident]
        value=.25 if before['value']>.5 else .75
        baseline=shot('progress-'+node['id']+'-before')
        pathlib.Path(request['semantic_probe']).write_text(json.dumps({'id':ident,'value':value}))
        deadline=time.monotonic()+5
        while time.monotonic()<deadline:
            after=current()['elements'][ident]
            if after.get('value')==value and abs(after.get('painted_value',-1)-value)<1e-6:break
            time.sleep(.1)
        else:raise RuntimeError(ident+': progress changed value without repainting the fill')
        changed=shot('progress-'+node['id']+'-after')
        with Image.open(baseline).convert('RGB') as a,Image.open(changed).convert('RGB') as b:
            x,y,w,h=layout[node['id']]['clipped_bounds'];scale=a.width/request['width']
            box=(round(x*scale),round(y*scale),round((x+w)*scale),round((y+h)*scale))
            visible_change=bool(w>0 and h>0 and ImageChops.difference(a.crop(box),b.crop(box)).getbbox())
        checks.append({'id':ident,'native_id':node['id'],'status':'pass','before':before,'after':after,
            'fill_pixels_changed':visible_change,'clipped_bounds':layout[node['id']]['clipped_bounds'],
            'paint_verification':'current native draw input; screenshot visibility recorded separately'})
    path.write_text(json.dumps({'pass':True,'build_id':build,'nonce':request['nonce'],'checks':checks},indent=2)+'\n')
    return [path,*files]


def child_id(root,path):
    return root['id']+'_'+ '_'.join(map(str,path))


def exposed_point(target,elements,layout):
    """Choose a measured hit area outside later native controls."""
    rect=layout[target]['clipped_bounds']
    regions=[rect] if rect[2]>=2 and rect[3]>=2 else []
    blockers=[];after=False
    for node in elements:
        if node['id']==target:after=True;continue
        if not after or node['kind'] not in ('Button','Input','Radio','Checkbox','Toggle','Slider','RangeSlider') or node.get('enabled')==0:continue
        bx,by,bw,bh=layout[node['id']]['clipped_bounds'];remaining=[];covered=False
        for x,y,w,h in regions:
            left,top=max(x,bx),max(y,by);right,bottom=min(x+w,bx+bw),min(y+h,by+bh)
            if left>=right or top>=bottom:remaining.append([x,y,w,h]);continue
            covered=True
            remaining.extend([[x,y,left-x,h],[right,y,x+w-right,h],
                [left,y,right-left,top-y],[left,bottom,right-left,y+h-bottom]])
        if covered:blockers.append({'id':node['id'],'bounds':[bx,by,bw,bh]})
        regions=[r for r in remaining if r[2]>=2 and r[3]>=2]
    if not regions:return None,blockers
    x,y,w,h=max(regions,key=lambda r:r[2]*r[3])
    return (x+w/2,y+h/2),blockers


def surface_palette(config,node,layout,pixels,scale,parts='surfaces',color_key='surface_color'):
    """Read source-state paint through the same composited overlays.

    The initial screenshot has its own visual gate. Matching another declared
    source state proves the highlight moves even when a modal scrim dims it.
    Reject inconsistent samples instead of assuming a uniform overlay.
    """
    palette={}
    for item in config['items']:
        color=item.get(color_key)
        if not isinstance(color,int):continue
        for path in item.get(parts,[]):
            sid=child_id(node,path);x,y,w,h=layout[sid]['bounds']
            px,py=round((x+w*.5)*scale),round((y+min(4,h*.5))*scale)
            if not(0<=px<pixels.width and 0<=py<pixels.height):continue
            sample=list(pixels.getpixel((px,py)))
            if color in palette and max(abs(a-b) for a,b in zip(sample,palette[color]))>3:
                raise RuntimeError(f'{node["id"]}: source surface palette varies across sample points')
            palette[color]=sample
    return palette


def check(bridge,build,name,portable,out,remount,save_screenshot,sha):
    nodes=[n for n in portable['elements'] if n.get('kit')]
    if not nodes:return []
    checks=[];files=[];click_points={}
    path=out/f'{name}.semantic-interactions.json'
    layout={n['id']:n for n in json.loads((out/f'{name}.layout.json').read_text())['elements']}
    actions_path=out/f'{name}.semantic-actions.json'
    by_id={n['id']:n for n in nodes}
    def actions():return json.loads(actions_path.read_text())
    def snapshot():
        bridge.send('WidgetSnapshot',{'build_id':build})
        return {w['id']:w for w in bridge.wait('WidgetSnapshot')['widgets']}
    def shot(suffix):
        bridge.send('Screenshot',{'build_id':build,'kind_id':0})
        image=out/f'{name}.{suffix}.png';save_screenshot(bridge.wait('Screenshot'),image);files.append(image)
        return image
    def restore(updates=None):
        request,result=remount(name,bootstrap=True,updates=updates)
        dest=pathlib.Path(request['layout']);deadline=time.monotonic()+15
        while (not result.exists() or not dest.exists()) and time.monotonic()<deadline:time.sleep(.1)
        if not dest.exists() or json.loads(dest.read_text()).get('nonce')!=request['nonce']:
            raise RuntimeError('semantic probe remount was stale')
        time.sleep(.15)
    def click(wid):
        point,blockers=exposed_point(wid,portable['elements'],layout)
        if blockers:checks.append({'id':wid,'status':'hit_area_inspected','click_point':point,'covering_controls':blockers})
        if point is None:return False
        px,py=map(round,point);click_points[wid]=(px,py)
        bridge.send('Click',{'build_id':build,'x':px,'y':py})
        time.sleep(.15)
        return True
    def occluding_action(target,observed):
        px,py=click_points[target]
        for action in observed:
            recipient=by_id.get(action['id'])
            if recipient is None:continue
            config=json.loads(recipient['kit']);event=action['action'];kind=event['kind']
            binding=(config['items'][event['index']]['control'] if kind=='selected' else
                config.get('action_bindings',{}).get(event.get('name')) if kind=='action' else
                config['bindings'].get('control') if kind=='activated' else None)
            if binding is None:continue
            control=child_id(recipient,binding)
            if control==target:continue
            rx,ry,rw,rh=layout[control]['clipped_bounds']
            if rx<=px<rx+rw and ry<=py<ry+rh:
                return {'action':action,'control':control,'bounds':[rx,ry,rw,rh]}
        return None
    try:
        restore()
        mounted=snapshot()
        for node in nodes:
            config=json.loads(node['kit'])
            if mounted[node['id']]['widget_type']!=config['widget']:
                raise RuntimeError(f'{node["id"]}: semantic widget became a generic container')
            primary=config['bindings'].get('input',config['bindings'].get('control'))
            initial={'id':node['id'],'status':'pass','initial':mounted[node['id']]}
            if primary is not None:
                control=mounted[child_id(node,primary)]
                enabled=node.get('enabled')!=0 and control.get('enabled',True)
                if mounted[node['id']].get('enabled')!=enabled:
                    raise RuntimeError(f'{node["id"]}: component enabled state disagrees with its native control')
                initial['primary_control']=control
            if config['widget'] in ('KitTabBar','KitBottomNavigation'):
                selected=node.get('kit_index',config['selected_index'])
                if mounted[node['id']].get('selected')!=str(selected):
                    raise RuntimeError(f'{node["id"]}: initial navigation index is incorrect')
                initial['controls']=[mounted[child_id(node,it['control'])] for it in config['items']]
                for i,control in enumerate(initial['controls']):
                    if control['widget_type']=='RadioButton' and control.get('checked')!=(i==selected):
                        raise RuntimeError(f'{node["id"]}: initial native radio state disagrees with the selected index')
            checks.append(initial)
            if config['widget'] not in ('KitTabBar','KitBottomNavigation'):continue
            channels=[]
            from PIL import Image
            with Image.open(out/f'{name}.png').convert('RGB') as source_pixels:
                for parts,key in [('surfaces','surface'),('indicators','indicator')]:
                    colors=[config.get(k+'_'+key) for k in ('active','inactive')]
                    if all(isinstance(c,int) for c in colors) and colors[0]!=colors[1]:
                        palette=surface_palette(config,node,layout,source_pixels,
                            source_pixels.width/mounted['main_window']['width'],parts,key+'_color')
                        channels.append((parts,key,colors,palette))
            for i,item in enumerate(config['items']):
                control=child_id(node,item['control'])
                before=snapshot()[node['id']].get('selected')
                if mounted[control].get('enabled') is False or not click(control):
                    checks.append({'id':node['id'],'item':i,'status':'not_interactable_at_this_viewport'});continue
                current=snapshot();observed=actions()
                if current[node['id']].get('selected')!=str(i):
                    raise RuntimeError(f'{node["id"]}: navigation did not select item {i}')
                if before!=str(i) and not any(a['id']==node['id'] and a['action']=={'kind':'selected','index':i} for a in observed):
                    raise RuntimeError(f'{node["id"]}: missing navigation action')
                for j,sibling in enumerate(config['items']):
                    state=current[child_id(node,sibling['control'])]
                    if state['widget_type']=='RadioButton' and state.get('checked')!=(i==j):
                        raise RuntimeError(f'{node["id"]}: navigation selection is not exclusive')
                checks.append({'id':node['id'],'item':i,'status':'pass','snapshot':current[node['id']],
                    'controls':[current[child_id(node,it['control'])] for it in config['items']], 'actions':observed})
                # A changed state flag with the old pill background is still a
                # broken component. Sample opaque native surfaces away from
                # text and rounded edges, using the measured logical frames.
                if channels:
                    image=shot(f'navigation-{node["id"]}-{i}')
                    from PIL import Image
                    with Image.open(image).convert('RGB') as pixels:
                        scale=pixels.width/mounted['main_window']['width'];differences=[]
                        for parts,key,colors,palette in channels:
                          for j,sibling in enumerate(config['items']):
                            if not sibling.get(parts):continue
                            color=sibling[key+'_color'] if current[child_id(node,sibling['control'])].get('enabled') is False else colors[0 if i==j else 1]
                            expected=palette.get(color,[(color>>shift)&255 for shift in (16,8,0)])
                            for surface in sibling[parts]:
                                sid=child_id(node,surface);x,y,w,h=layout[sid]['bounds']
                                px,py=round((x+w*.5)*scale),round((y+min(4,h*.5))*scale)
                                if not(0<=px<pixels.width and 0<=py<pixels.height):continue
                                actual=list(pixels.getpixel((px,py)))
                                differences.append({'id':sid,'part':key,'expected':expected,'actual':actual,'tolerance':3,
                                    'reference':'initial source-state screenshot' if color in palette else 'source color',
                                    'pass':max(abs(a-b) for a,b in zip(actual,expected))<=3})
                        checks[-1]['surface_colors']=differences
                        if any(not d['pass'] for d in differences):
                            checks[-1]['status']='failed'
                            raise RuntimeError(f'{node["id"]}: selected surface styling did not update')
            shot(f'navigation-{node["id"]}-selected')
        # Native inputs are exhaustively typed by check_inputs. Here prove that
        # the enclosing field owns the same value and emits its public action.
        for node in nodes:
            config=json.loads(node['kit'])
            if config['widget']!='KitFormField':continue
            control=child_id(node,config['bindings']['input'])
            if not click(control):continue
            before=snapshot()[control].get('value','')
            bridge.send('TypeText',{'build_id':build,'text':'7'});time.sleep(.15)
            current=snapshot();observed=actions();value=current[control].get('value')
            if value==before or current[node['id']].get('text')!=value:
                raise RuntimeError(f'{node["id"]}: composed field does not own its input value')
            if not any(a['id']==node['id'] and a['action']=={'kind':'changed','value':value} for a in observed):
                raise RuntimeError(f'{node["id"]}: missing field change action')
            checks.append({'id':node['id'],'status':'pass','field':current[node['id']],
                'input':current[control],'actions':observed});break
        # Choose the last mounted visible button to exercise the topmost source
        # control, avoiding unrelated buttons behind source modal overlays.
        for node in reversed(nodes):
            config=json.loads(node['kit'])
            if config['widget']!='KitButton' or 'control' not in config['bindings']:continue
            control=child_id(node,config['bindings']['control'])
            enabled=mounted[node['id']].get('enabled',True)
            previous=len(actions())
            if not click(control):continue
            observed=actions()[previous:]
            fired=any(a['id']==node['id'] and a['action']['kind']=='activated' for a in observed)
            occluder=occluding_action(control,observed) if not fired else None
            if occluder:
                checks.append({'id':node['id'],'status':'occluded_by_native_control','occluder':occluder});continue
            if fired!=enabled:raise RuntimeError(f'{node["id"]}: composed button activation/disabled contract failed')
            checks.append({'id':node['id'],'status':'pass','enabled':enabled,'actions':observed});break
        # Exercise the real Widget::set_text API on one card/row per screen.
        for kind in ('TaskplanProjectCard','CamoTrackRow'):
            node=next((n for n in nodes if json.loads(n['kit'])['widget']==kind),None)
            if node is None:continue
            restore();config=json.loads(node['kit'])
            for role,binding in {'control':config['bindings']['control'],**config.get('action_bindings',{})}.items():
                if not click(child_id(node,binding)):continue
                wanted={'kind':'activated'} if role=='control' else {'kind':'action','name':role}
                observed=actions()
                if not any(a['id']==node['id'] and a['action']==wanted for a in observed):
                    raise RuntimeError(f'{node["id"]}: missing {role} action')
                checks.append({'id':node['id'],'status':'pass','role':role,'actions':observed})
            restore(updates=[{'id':node['id'],'text':'Component title probe'}])
            current=snapshot();config=json.loads(node['kit']);label=child_id(node,config['bindings']['title'])
            if current[node['id']].get('text')!='Component title probe' or current[label].get('text')!='Component title probe':
                raise RuntimeError(f'{node["id"]}: public title update did not reach native Label')
            checks.append({'id':node['id'],'status':'pass','component':current[node['id']],'label':current[label]})
            shot('component-title')
        restore();current=snapshot()
        for node in nodes:
            if current[node['id']].get('text')!=mounted[node['id']].get('text') or current[node['id']].get('selected')!=mounted[node['id']].get('selected'):
                raise RuntimeError(f'{node["id"]}: source component state was not restored')
        shot('semantic-restored')
        report={'pass':True,'build_id':build,'checks':checks,'restored':True,
                'scope':'all navigation items; one visible button/field and one card/row setter per screen'}
    except Exception as error:
        report={'pass':False,'build_id':build,'checks':checks,'error':str(error)}
        path.write_text(json.dumps(report,indent=2)+'\n')
        raise
    report['screenshots']={p.name:sha(p) for p in files}
    path.write_text(json.dumps(report,indent=2)+'\n')
    return [path,*files]
