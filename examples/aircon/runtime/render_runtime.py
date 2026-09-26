"""Bind service data to compiled native L0 cards without rasterizing UI.

Each live request owns its L0 copy, placement JSON and kit tokens. The reviewed
source card stays immutable; action evidence can identify the exact live inputs.
"""
from pathlib import Path
import copy, json, re, shutil

ROOT = Path(__file__).resolve().parents[1]

def write(p, v):
    Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2)+'\n')

def render_runtime(state, view, output_dir):
    out = Path(output_dir).resolve(); out.mkdir(parents=True, exist_ok=True)
    frame = view['frame_id']; source = ROOT/'cards'/f'aircon-{frame:02d}'
    card = (source/'page.card').read_text()
    data = json.loads((source/'page.data.json').read_text())
    kit = json.loads((source/'kit/native/light/kit.json').read_text())
    mapping = json.loads((source/'mapping.json').read_text())
    actions = json.loads((source/'service-actions.json').read_text())
    by_id = {n['source_id']:n for n in mapping['elements']}
    placements = data['$kit']['placements']
    extra_components=[]

    def remove(id):
        nonlocal card
        if id not in placements:return
        # Generated L0 instances occupy a line or a balanced indented block.
        pattern=re.compile(r'(?m)^([ \t]*)[A-Za-z0-9_]+\(instance: '+re.escape(json.dumps(id))+r'[^\n]*\n')
        match=pattern.search(card)
        if not match:raise ValueError('Native instance missing: '+id)
        end=match.end()
        if match[0].rstrip().endswith('{'):
            closing=re.search(r'(?m)^'+re.escape(match[1])+r'\}\n',card[end:])
            if not closing:raise ValueError('Native instance block unbalanced: '+id)
            end+=closing.end()
        card=card[:match.start()]+card[end:]
        removed={id}
        while True:
            children={n['source_id'] for n in mapping['elements'] if n.get('parent') in removed}
            if children<=removed:break
            removed|=children
        mapping['elements']=[n for n in mapping['elements'] if n['source_id'] not in removed]
        for key in removed:
            placements.pop(key,None);by_id.pop(key,None);actions['controls'].pop(key,None)
        counts={}
        for node in mapping['elements']:
            parent=node.get('parent')
            index=counts.get(parent,0);counts[parent]=index+1
            node['native_id']=(by_id[parent]['native_id']+'_'+str(index)) if parent else 'beauty_'+str(index)

    def style(id, **values):
        nonlocal card
        if id not in placements:return
        placement=placements[id];name=placement['component']
        new=name+'_live_'+id
        kit['components'][new]=copy.deepcopy(kit['components'][name])
        kit['components'][new]['style'].update(values)
        placement['component']=new
        definition=re.search(r'component '+re.escape(name)+r'\([^\n]*\) \{\n[^\n]*\n\}\n',card)
        if not definition:raise ValueError('Native component definition missing: '+name)
        cloned=definition[0].replace('component '+name+'(', 'component '+new+'(').replace('component: "'+name+'"','component: "'+new+'"')
        card=card.replace('\nview root ', '\n'+cloned+'\nview root ',1)
        old_use=name+'(instance: '+json.dumps(id)
        if old_use not in card:raise ValueError('Native component instance missing: '+id)
        card=card.replace(old_use,new+'(instance: '+json.dumps(id),1)
        extra_components.append(cloned)

    def text(id, value, center_in=None):
        nonlocal card
        if id not in placements:return
        pattern=r'(copy '+re.escape(id)+r'_text \{ class: user-copy, en: )"(?:[^"\\]|\\.)*"( \})'
        card,n=re.subn(pattern,lambda m:m[1]+json.dumps(value,ensure_ascii=False)+m[2],card)
        if n!=1:raise ValueError('Native copy binding missing: '+id)
        by_id[id]['text']=value
        if center_in and center_in in placements:
            r=placements[center_in]['layout'];l=placements[id]['layout']
            l.update(x=r['x']+5,w=r['w']-10)
            style(id,alignx=.5,tracking=0)
        elif len(value)>len(next((n.get('text') or '' for n in json.loads((source/'mapping.json').read_text())['elements'] if n['source_id']==id),'')):
            p=by_id[id].get('parent');parent=placements.get(p,{}).get('layout',{})
            if parent:placements[id]['layout']['w']=max(placements[id]['layout']['w'],parent['x']+parent['w']-placements[id]['layout']['x']-12)

    def enabled(id, value):
        nonlocal card
        cid=id+'_control'
        if cid not in placements:return
        pattern=r'(state '+re.escape(cid)+r'_enabled \{ shape: bool, initial: )(true|false)( \})'
        card,n=re.subn(pattern,lambda m:m[1]+str(bool(value)).lower()+m[3],card)
        if n!=1:raise ValueError('Native enabled binding missing: '+id)
        by_id[cid]['enabled']=int(bool(value))
        actions['controls'][id]['enabled']=bool(value)

    def button(id, label=None, action=None, active=None):
        if id not in actions['controls']:return
        if label is not None:
            label_ids=actions['controls'][id]['ocr_ids']
            if label_ids:text('text_'+str(label_ids[0]),label,center_in=id)
        if action:actions['controls'][id]['event']=action
        if active is not None:enabled(id,active)

    fixture=state['fixture'];booking=state['installation'];calendar=state['calendar'];payment=state['payment']
    if frame in (6,7):
        slots={s['id']:s for s in view['slots']}
        for id,sid in [('conflict_slot','morning'),('afternoon','afternoon')]:
            slot=slots.get(sid)
            if slot:enabled(id,slot['enabled'])
        enabled('confirm_booking',view['bindings']['can_confirm_booking'])
        selected=booking.get('selected_slot_id')
        day=booking.get('selected_day','2026-09-19')
        sunday=day=='2026-09-20'
        for id,selected_day in [('saturday',not sunday),('sunday',sunday)]:
            style(id+'_surface',bg=0xff608570 if selected_day else 0xfffcfdfb)
            for i in actions['controls'][id]['ocr_ids']:style('text_'+str(i),color=0xffffffff if selected_day else 0xff31413c)
        conflict_text='text_'+str(72 if frame==6 else 126)
        text(conflict_text,'与项目例会冲突' if not slots['morning']['enabled'] else '日历空闲')
        style(conflict_text,color=0xffbe873f if not slots['morning']['enabled'] else 0xff58816b)
        summary='请选择安装时段' if not selected else ('周日 9月20日' if sunday else '周六 9月19日')+' · '+slots[selected]['label']
        text('text_'+str(76 if frame==6 else 130),summary)
        # Radio dots and outline paint follow the same service-selected slot.
        for index,sid in [(0,'morning'),(1,'afternoon')]:
            style('step_'+str(index),bg=0xff608570 if selected==sid else 0xfffcfdfb)
        style('afternoon_surface',bg=0xfff0f5ef if selected=='afternoon' else 0xfffcfdfb)
        style('conflict_slot_surface',bg=0xfff0f5ef if selected=='morning' else 0xfffcfdfb)
    if frame==8 and calendar['acknowledged']:
        button('acknowledge_calendar','已确认',active=False)
    if frame in (8,9,10) and booking.get('booked_day')=='2026-09-20':
        for node in list(by_id.values()):
            value=node.get('text')
            if value and '9月19日' in value:text(node['source_id'],value.replace('周六','周日').replace('9月19日','9月20日'))
    if frame in (8,9,10) and booking.get('booked_slot_id'):
        slot=next(s for s in fixture['installation']['slots'] if s['id']==booking['booked_slot_id'])
        for node in list(by_id.values()):
            value=node.get('text')
            if value and ('月' in value or value.startswith('今天')) and re.search(r'\d\d:\d\d[-–]\d\d:\d\d',value):
                text(node['source_id'],re.sub(r'\d\d:\d\d[-–]\d\d:\d\d',slot['label'],value))
    if frame in (10,11,12) and booking.get('booked_day')=='2026-09-20':
        date_id,dock_id={10:(84,98),11:(139,153),12:(195,208)}[frame]
        text('text_'+str(date_id),'9月20日 周日')
        text('text_'+str(dock_id),'20')
    if frame==5 and booking['status']=='cancelled':
        text('text_13','安装服务 · 预约已取消')
        text('text_14','安装预约已取消')
        text('text_15','日历中的关联日程已移除')
        button('choose_time','重新预约',action='installation.open_slots')
    if frame==11 and payment['status']=='cancelled':
        text('text_141','支付 · 请求已撤销')
        text('text_142','材料费尚未支付')
        button('pay_materials','重新打开',action='payment.reopen',active=True)
        button('withdraw_payment_request','已撤销',active=False)
    if frame==11:
        actions['controls']['pay_materials']['payload']={'invoice_id':payment['id'],'amount_minor':fixture['payment']['amount_minor'],'currency':fixture['payment']['currency']}

    if frame==3 and state['ui'].get('dismissed_cards'):
        if 'shopping:'+state['order']['id'] in state['ui']['dismissed_cards']:
            remove('order_card')

    # Route to an internal native preview of the current service data. These
    # headers make the route visible without claiming an external OS app launch.
    route=view.get('app_route')
    if route and not (route['app']=='shopping' and route.get('page') in ('product','order')):
        app_names={'shopping':'购物应用','logistics':'物流应用','installation':'安装服务','calendar':'日历应用','payment':'支付应用'}
        page_names={'detail':'详情预览','support':'联系服务','contact':'联系服务','delivery-time':'配送安排','booking':'安装预约','service-order':'服务单','feedback':'服务反馈','receipt':'付款凭证'}
        # The source atlas has different letterbox offsets. Select the first
        # two screen labels by order, rather than an absolute y cutoff that
        # omitted the clock/page heading in the payment receipt frame.
        headers=[n for n in mapping['elements'] if n.get('text') and n.get('parent')=='screen']
        headers.sort(key=lambda n:n['bounds'][1])
        for index,(node,label) in enumerate(zip(headers[:2],[app_names[route['app']],page_names.get(route.get('page'),'详情预览')])):
            text(node['source_id'],label)
            placements[node['source_id']]['layout'].update(x=24,y=24+index*40,w=350,h=30)
            style(node['source_id'],size=22,line_height=28,tracking=0)
        back=next(iter(actions['controls']),None)
        if back:
            button(back,'返回桌面',action='navigation.desktop',active=True)
            actions['controls'][back]['payload']={}
        write(out/'route-preview.json',{'route':route,'kind':'internal-native-data-preview','external_app_launched':False,'scope':'Current service data with an internal route header; complete detail-app layouts are not reconstructed'})

    for node in mapping['elements']:
        if node['source_id'] in placements:
            p=placements[node['source_id']];node['bounds']=[p['layout'].get(k,0) for k in ('x','y','w','h')];node['component']=p['component']
    native=out/'kit/native/light';native.mkdir(parents=True,exist_ok=True)
    (out/'page.card').write_text(card)
    write(out/'page.data.json',data);write(native/'kit.json',kit)
    (native/'components.l0').write_text((source/'kit/native/light/components.l0').read_text()+''.join(extra_components))
    write(out/'mapping.json',mapping);write(out/'service-actions.json',actions)
    write(out/'service-state.json',state);write(out/'service-view.json',view)
    return {'card':str(out/'page.card'),'data':str(out/'page.data.json'),'kit_dir':str(out/'kit'),
            'mapping':str(out/'mapping.json'),'service_actions':str(out/'service-actions.json'),
            'semantic':str(source/'semantic-map.json'),'source_design':source.name,'format':'l0-kit'}
