#!/usr/bin/env python3
"""Validate cards, then capture the dedicated release host through Studio.

Requires a Studio mount named splashref pointing to this checkout's
splash-makepad directory. Set CARGO_MAKEPAD to the release bridge binary.
"""
import argparse
import hashlib
import http.server
import json
import os
import pathlib
import queue
import shutil
import subprocess
import struct
import tempfile
import threading
import time
import uuid
import urllib.request
from urllib.parse import urlparse

from core.native_paths import repository
from core import kitconf
from core import gate_structure
from core import semantic_interactions

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MOUNT = repository('splash-makepad')
_file_digests = {}


def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def fingerprint(paths):
    h = hashlib.sha256(b'beauty-file-digests-v2\0')
    for p in sorted(set(paths)):
        stat=p.stat()
        version=(stat.st_dev,stat.st_ino,stat.st_size,stat.st_mtime_ns,stat.st_ctime_ns)
        cached=_file_digests.get(p)
        if cached is None or cached[0]!=version:
            cached=(version,hashlib.sha256(p.read_bytes()).digest())
            _file_digests[p]=cached
        h.update(str(p).encode())
        h.update(b'\0')
        h.update(cached[1])
    return h.hexdigest()


def fresh(meta, expected, png):
    return (png.is_file() and meta.get('inputs') == expected
            and meta.get('png_sha256') == sha(png)
            and meta.get('inspection_pass') is True
            and bool(meta.get('inspection_sha256'))
            and all((png.parent/name).is_file() and sha(png.parent/name) == value
                    for name, value in meta['inspection_sha256'].items()))


def shared_inputs(kit):
    packs = [MOUNT/'components/l0/native'/name/'kit.json'
             for name in (kit.get('theme'),kit.get('theme_light'))
             if name and (MOUNT/'components/l0/native'/name/'kit.json').is_file()]
    return [MOUNT/'target/release/beauty-host', MOUNT/'makepad.splash',
            *sorted(p for p in (MOUNT/'apps/kit-host/resources').rglob('*') if p.is_file()),
            *sorted((MOUNT/'components/l0').glob('*.splash')),
            *(packs if kit.get('input_format')=='l0-kit' else []),
            *sorted(p for p in pathlib.Path(kit['img_dir']).rglob('*') if p.is_file()),
            *sorted(pathlib.Path(p).expanduser() for p in kit.get('font_files',{}).values()),
            *sorted(p for p in (kit['specs_dir'].parent/'semantics').rglob('*') if p.is_file()),
            pathlib.Path(__file__), pathlib.Path(gate_structure.__file__), pathlib.Path(semantic_interactions.__file__)]


class SharedBridge:
    """Reuse an existing HTTP wrapper around one persistent Studio client."""
    def __init__(self, url):
        self.url=url; self.replies=[]; self.queries=[]
        with urllib.request.urlopen(url,timeout=5) as handle:
            self.batch_queries=json.load(handle).get('batch_widget_queries',False)

    def post(self, payload):
        raw=json.dumps(payload).encode()
        with urllib.request.urlopen(urllib.request.Request(self.url,data=raw,
                headers={'Content-Type':'application/json'}),timeout=65) as handle:
            reply=json.load(handle)
        if reply.get('error'):raise RuntimeError(reply['error'])
        return reply

    def flush_queries(self):
        while self.queries:
            batch=self.queries[:128]
            reply=self.post({'requests':batch,'timeout':60})
            rows=reply.get('responses',[])
            expected={(json.dumps(r['WidgetQuery']['build_id']),r['WidgetQuery']['query']) for r in batch}
            actual=[(json.dumps(r['build_id']),r['query']) for r in rows]
            if len(actual)!=len(expected) or set(actual)!=expected:
                raise RuntimeError('Incomplete or mismatched Studio query batch')
            self.replies.extend(('WidgetQuery',row) for row in rows)
            del self.queries[:len(batch)]

    def send(self, kind, value):
        if kind=='WidgetQuery' and self.batch_queries:
            self.queries.append({kind:value});return
        self.flush_queries()
        response={'ListBuilds':'Builds','RunItem':'BuildStarted','QueryLogs':'QueryLogResults'}.get(kind,kind)
        if kind in ('ClearBuild','Click','TypeText','Return','RunViewResize','ForwardToApp'):
            response=None
        reply=self.post({'request':{kind:value},'response':response,'timeout':30})
        if response:self.replies.append((response,reply))

    def wait(self, kind, timeout=120):
        self.flush_queries()
        for index,(response,reply) in enumerate(self.replies):
            if response==kind:
                self.replies.pop(index);return reply
        raise RuntimeError(f'No pending Studio response: {kind}')

    def close(self):
        pass  # This run does not own the persistent bridge.


class Bridge:
    def __init__(self, address, log):
        binary = os.environ.get('CARGO_MAKEPAD') or shutil.which('cargo-makepad')
        if not binary:
            raise RuntimeError('set CARGO_MAKEPAD to a release cargo-makepad binary')
        if not os.environ.get('CARGO_MAKEPAD'):
            # The bridge client and the studio server speak a binary enum
            # protocol, and a PATH client from another era misroutes SILENTLY:
            # an Aug 8 client against a Sep 4 server answered WidgetTreeDump
            # and WidgetQuery correctly and dropped every WidgetSnapshot into
            # the void, which read as a child-side visibility bug and cost a
            # day. A capture run does not get to guess which client it used.
            raise RuntimeError(
                'CARGO_MAKEPAD is not set. This run would fall back to '
                f'{binary!r} from PATH, and a client that does not match the '
                'running studio server misroutes requests silently (tree dumps '
                'answer, snapshots never do). Point CARGO_MAKEPAD at the '
                'cargo-makepad built alongside the studio server.')
        self.log = log.open('w')
        self.q = queue.Queue()
        self.p = subprocess.Popen([binary, 'studio', f'--studio={address}'],
                                  cwd=MOUNT, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT, text=True, bufsize=1)
        threading.Thread(target=self._read, daemon=True).start()
        self.wait('Hello', timeout=20)

    def _read(self):
        for line in self.p.stdout:
            self.log.write(line)
            self.log.flush()
            try:
                self.q.put(json.loads(line))
            except json.JSONDecodeError:
                if line.startswith('studio remote: invalid request'):
                    self.q.put({'Error': {'message': line.strip()}})
        self.q.put({'BridgeClosed': True})

    def send(self, kind, value):
        self.p.stdin.write(json.dumps({kind: value}) + '\n')
        self.p.stdin.flush()

    def wait(self, kind, timeout=120):
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            try:
                row = self.q.get(timeout=min(10, max(.01, deadline-time.monotonic())))
            except queue.Empty:
                continue
            if kind in row:
                if kind=='QueryLogResults' and not row[kind].get('done'):continue
                return row[kind]
            if 'Error' in row and 'unknown build:' not in row['Error']['message']:
                raise RuntimeError(row['Error']['message'])
            if 'BridgeClosed' in row or 'BuildStopped' in row:
                raise RuntimeError(f'Studio stopped before {kind}: {row}')
            for _, entry in row.get('QueryLogResults', {}).get('entries', []):
                msg = entry.get('message', '')
                if kind == 'NativeMounted' and 'BEAUTY_MOUNT ' in msg:
                    return json.loads(msg.split('BEAUTY_MOUNT ', 1)[1])
                if 'BEAUTY_ERROR' in msg:
                    raise RuntimeError(msg)
                if 'Error' in entry.get('level', {}) or msg.startswith('[E]'):
                    raise RuntimeError(f'Studio build/runtime error: {msg}')
        raise TimeoutError(f'Studio did not return {kind} in {timeout}s')

    def close(self):
        self.p.stdin.close()
        try:
            self.p.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.p.terminate()
            self.p.wait(timeout=5)
        self.log.close()


def selected_inputs(kit, name):
    suffix = 'splash' if kit.get('input_format') == 'design' else 'card'
    card = kit['cards_dir'] / f'{name}.{suffix}'
    data = card.with_suffix('.data.json')
    if not data.exists():
        data.write_text('{}\n')
    spec = kit['specs_dir'] / f'{name}.json'
    return card, data, spec


def evidence_paths(out, name, bootstrap=False):
    # Startup must not overwrite a cached screen's nonce-bound inspection.
    stem = f'.bootstrap-{name}' if bootstrap else name
    return out/f'{stem}.native.json', out/f'{stem}.layout.json'


def release_screenshot(shot):
    """Consume only the exact temporary file returned for our own request."""
    if not shot.get('path'):
        return
    path=pathlib.Path(shot['path'])
    hub=pathlib.Path(tempfile.gettempdir())/'makepad_studio_hub'
    if (path.parent.resolve()==hub.resolve() and path.suffix=='.png'
            and path.name.startswith('build-')):
        path.unlink(missing_ok=True)


def save_screenshot(shot, destination):
    # A failed copy leaves Studio's source intact for recovery.
    shutil.copyfile(shot['path'], destination)
    release_screenshot(shot)


def ensure_embedded_frame(bridge, build, width, height):
    """Studio's initial tab layout can overwrite an early RunViewResize."""
    expected=(round(width*2),round(height*2))
    for attempt in range(4):
        bridge.send('Screenshot',{'build_id':build,'kind_id':0})
        shot=bridge.wait('Screenshot')
        release_screenshot(shot)
        if (shot['width'],shot['height'])==expected:
            return
        if attempt<3:
            bridge.send('RunViewResize',{'build_id':build,'window_id':0,
                        'width':width,'height':height,'dpi':2.0})
            time.sleep(.35)
    raise RuntimeError(f'Studio frame did not settle at {expected}: {shot}')


def frame_has_content(reference, capture):
    """Reject empty GPU readbacks without rejecting an intentionally flat design."""
    from PIL import Image, ImageStat
    def stats(path):
        with Image.open(path) as source:
            rgba = source.convert('RGBA')
        visible = rgba.getchannel('A').getextrema()[1] > 0
        rgb = Image.alpha_composite(Image.new('RGBA',rgba.size,'white'),rgba).convert('RGB')
        return visible, max(ImageStat.Stat(rgb.resize((128,128))).stddev)
    expected_visible, expected_variance = stats(reference)
    visible, variance = stats(capture)
    return ((not expected_visible or visible)
            and (expected_variance <= 3 or variance > 1))


def check_toggles(bridge, build, name, portable, snapshot, out):
    # The standalone websocket dispatch uses window-local coordinates (zero
    # origin). W3 dump and query frames use that same coordinate system.
    layout = json.loads((out/f'{name}.layout.json').read_text())
    boxes = {n['id']:n['bounds'] for n in layout['elements']}
    evidence = []
    for node in portable['elements']:
        if node['kind'] not in ('Toggle','Checkbox'):
            continue
        wid = node['id']
        x,y,w,h = boxes[wid]
        states = []
        changed = bool(node['on']) if node.get('enabled') == 0 else not bool(node['on'])
        for stage, expected in [('toggled', changed), ('restored', bool(node['on']))]:
            bridge.send('Click', {'build_id':build, 'x':round(x+w/2), 'y':round(y+h/2)})
            time.sleep(.4)
            bridge.send('WidgetSnapshot', {'build_id':build})
            snapshot = bridge.wait('WidgetSnapshot')
            actual = next(n for n in snapshot['widgets'] if n['id']==wid)
            if actual.get('checked') != expected:
                raise RuntimeError(f'{name}: {wid} did not {stage}: {actual}')
            bridge.send('Screenshot', {'build_id':build,'kind_id':0})
            shot = bridge.wait('Screenshot')
            image = out/f'{name}.{wid}.{stage}.png'
            save_screenshot(shot,image)
            states.append({'stage':stage,'widget':actual,'screenshot':image.name,'sha256':sha(image)})
        evidence.append({'id':wid,'source_id':node['original_id'],'states':states})
    path=out/f'{name}.interactions.json'
    path.write_text(json.dumps({'build_id':build,'checks':evidence},indent=2))
    return [path,*(out/s['screenshot'] for e in evidence for s in e['states'])]


def check_inputs(bridge, build, name, portable, out, remount):
    inputs = [n for n in portable['elements'] if n['kind'] == 'Input']
    if not inputs:
        return []
    layout = json.loads((out/f'{name}.layout.json').read_text())
    boxes = {n['id']:n['bounds'] for n in layout['elements']}
    checks = []
    for node in inputs:
        x,y,w,h = boxes[node['id']]
        bridge.send('Click', {'build_id':build,'x':round(x+w/2),'y':round(y+h/2)})
        bridge.send('TypeText', {'build_id':build,'text':'7'})
        time.sleep(.15)
        bridge.send('WidgetSnapshot', {'build_id':build})
        snapshot = bridge.wait('WidgetSnapshot')
        actual = next(n for n in snapshot['widgets'] if n['id']==node['id'])
        before, after = node.get('text') or '', actual.get('value')
        if (not isinstance(after,str) or len(after) != len(before)+1
                or not any(after[i]=='7' and after[:i]+after[i+1:]==before for i in range(len(after)))):
            raise RuntimeError(f"{name}: native input {node['id']} did not accept typing")
        checks.append({'id':node['id'],'source_id':node['original_id'],'before':before,'typed':actual})
    bridge.send('Screenshot', {'build_id':build,'kind_id':0})
    typed = out/f'{name}.inputs-typed.png'
    save_screenshot(bridge.wait('Screenshot'),typed)
    request, result = remount(name, bootstrap=True)
    restored_layout = pathlib.Path(request['layout'])
    deadline = time.monotonic()+15
    while (not result.exists() or not restored_layout.exists()) and time.monotonic()<deadline:
        time.sleep(.1)
    if not result.exists() or not restored_layout.exists():
        raise RuntimeError(f'{name}: native input restoration did not finish')
    restored = json.loads(restored_layout.read_text())
    if restored.get('nonce') != request['nonce']:
        raise RuntimeError(f'{name}: stale input restoration')
    bridge.send('WidgetSnapshot', {'build_id':build})
    snapshot = bridge.wait('WidgetSnapshot')
    widgets = {w['id']:w for w in snapshot['widgets']}
    focused = {w['id']:w.get('focused') for w in restored['elements']}
    for node in inputs:
        if (widgets[node['id']].get('value') != (node.get('text') or '')
                or focused[node['id']] != bool(node.get('focused'))):
            raise RuntimeError(f"{name}: native input {node['id']} was not restored")
    bridge.send('Screenshot', {'build_id':build,'kind_id':0})
    image = out/f'{name}.inputs-restored.png'
    save_screenshot(bridge.wait('Screenshot'),image)
    path = out/f'{name}.input-interactions.json'
    path.write_text(json.dumps({'build_id':build,'checks':checks,'restored_request':request,
        'restored_widgets':snapshot,'restored_layout':restored,
        'screenshots':{p.name:sha(p) for p in (typed,image)}},indent=2))
    return [path,typed,image]


def interaction_point(element):
    x,y,w,h=element['clipped_bounds']
    return (x+w/2,y+h/2) if w>0 and h>0 else None


def check_radios(bridge, build, name, portable, out, remount):
    radios=[n for n in portable['elements'] if n['kind']=='Radio']
    if not radios:return []
    boxes={n['id']:n for n in json.loads((out/f'{name}.layout.json').read_text())['elements']}
    checks=[]
    for node in radios:
        element=boxes[node['id']]
        point,blockers=semantic_interactions.exposed_point(node['id'],portable['elements'],boxes)
        if point is None:
            checks.append({'id':node['id'],'source_id':node['original_id'],
                'status':'not_interactable_at_this_viewport','reason':'fully clipped or covered by measured native controls',
                'covering_controls':blockers,
                'bounds':element['bounds'],'clipped_bounds':element['clipped_bounds'],'states':[]})
            continue
        x,y=point
        states=[]
        expected=bool(node.get('on')) if node.get('enabled')==0 else True
        for stage in ('selected','selected_again'):
            bridge.send('Click',{'build_id':build,'x':round(x),'y':round(y)})
            time.sleep(.3)
            bridge.send('WidgetSnapshot',{'build_id':build})
            widget=next(n for n in bridge.wait('WidgetSnapshot')['widgets'] if n['id']==node['id'])
            if widget.get('checked')!=expected:
                raise RuntimeError(f'{name}: native radio {node["id"]} failed {stage}')
            states.append({'stage':stage,'widget':widget})
        checks.append({'id':node['id'],'source_id':node['original_id'],
                       'click_point':list(point),'covering_controls':blockers,'clipped_bounds':element['clipped_bounds'],'states':states})
    bridge.send('Screenshot',{'build_id':build,'kind_id':0})
    changed=out/f'{name}.radios-selected.png'
    save_screenshot(bridge.wait('Screenshot'),changed)
    request,result=remount(name,bootstrap=True)
    layout=pathlib.Path(request['layout'])
    deadline=time.monotonic()+15
    while (not result.exists() or not layout.exists()) and time.monotonic()<deadline:time.sleep(.1)
    if not result.exists() or not layout.exists() or json.loads(layout.read_text()).get('nonce')!=request['nonce']:
        raise RuntimeError(f'{name}: radio restoration did not finish with current layout')
    bridge.send('WidgetSnapshot',{'build_id':build})
    snapshot=bridge.wait('WidgetSnapshot'); widgets={n['id']:n for n in snapshot['widgets']}
    if any(widgets[n['id']].get('checked')!=bool(n.get('on')) for n in radios):
        raise RuntimeError(f'{name}: native radio source state was not restored')
    bridge.send('Screenshot',{'build_id':build,'kind_id':0})
    restored=out/f'{name}.radios-restored.png'
    save_screenshot(bridge.wait('Screenshot'),restored)
    path=out/f'{name}.radio-interactions.json'
    path.write_text(json.dumps({'build_id':build,'checks':checks,'restored_request':request,
        'restored_widgets':snapshot,'screenshots':{p.name:sha(p) for p in (changed,restored)}},indent=2))
    return [path,changed,restored]


def mouse_packet(kind, x, y, timestamp):
    """StudioToApp SerBin: u16 variant, packed fields, four modifier bools.

    Field order is defined in makepad/platform/studio/src/studio.rs. Keep this
    narrow adapter covered by a native deserialization regression test.
    """
    # ForwardToApp carries StudioToAppVec, including its u64 item count.
    if kind=='down':return list(struct.pack('<QHIddd4?',1,10,1,x,y,timestamp,False,False,False,False))
    if kind=='move':return list(struct.pack('<QHddd4?',1,12,timestamp,x,y,False,False,False,False))
    if kind=='up':return list(struct.pack('<QHdIdd4?',1,11,timestamp,1,x,y,False,False,False,False))
    raise ValueError('unknown pointer event')


def check_sliders(bridge, build, name, portable, out):
    nodes=[n for n in portable['elements'] if n['kind'] in ('Slider','RangeSlider')]
    if not nodes:return []
    boxes={n['id']:n['bounds'] for n in json.loads((out/f'{name}.layout.json').read_text())['elements']}
    evidence=[];checks=[]
    for node in nodes:
        x,y,w,h=boxes[node['id']]
        initial=[node['value']]+([node['value2']] if node['kind']=='RangeSlider' else [])
        for handle,position in enumerate(initial):
            delta=.04 if handle==0 and (len(initial)==1 or initial[1]-position>.09) else -.04
            if position+delta<0 or position+delta>1:delta=-delta
            stages=[]
            for stage,start,end in [('dragged',position,position+delta),('restored',position+delta,position)]:
                for kind,fraction in [('down',start),('move',end),('up',end)]:
                    bridge.send('ForwardToApp',{'build_id':build,'msg_bin':mouse_packet(kind,x+w*fraction,y+h/2,time.time())})
                    time.sleep(.08)
                bridge.send('WidgetSnapshot',{'build_id':build})
                snap=bridge.wait('WidgetSnapshot')
                actual=next(n for n in snap['widgets'] if n['id']==node['id'])
                value=json.loads(actual.get('value') or 'null')
                values=value if isinstance(value,list) else [value]
                expected=initial.copy();expected[handle]=end
                if len(values)!=len(expected) or any(not isinstance(a,(float,int)) or abs(a-b)>1e-4 for a,b in zip(values,expected)):
                    raise RuntimeError(f"{name}: native slider {node['id']} handle {handle} did not {stage}: {actual}")
                bridge.send('Screenshot',{'build_id':build,'kind_id':0})
                image=out/f'{name}.{node["id"]}.handle-{handle}.{stage}.png'
                save_screenshot(bridge.wait('Screenshot'),image)
                evidence.append(image);stages.append({'stage':stage,'widget':actual,'screenshot':image.name})
            checks.append({'id':node['id'],'source_id':node['original_id'],'handle':handle,'states':stages})
    path=out/f'{name}.slider-interactions.json'
    path.write_text(json.dumps({'build_id':build,'checks':checks},indent=2)+'\n')
    return [path,*evidence]


def validate(kit, name):
    card, data, spec = selected_inputs(kit, name)
    r = subprocess.run(['cargo', 'run', '--release', '-q', '-p', 'splash-makepad',
                        '--example', 'beauty_check', '--', str(card), str(data),
                        str(MOUNT / 'components/l0')], cwd=MOUNT,
                       capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f'{name}: portable validation failed\n{r.stderr[-4000:]}\n{r.stdout[-1000:]}')
    result = json.loads(r.stdout)
    if not result.get('ok') or not result.get('nodes') or not result.get('elements'):
        raise RuntimeError(f'{name}: empty or rejected tree')
    (kit['splash_makepad_dir'] / f'{name}.portable.json').write_text(json.dumps(result, indent=2))
    return result


def run(kit, address, check_only=False):
    out = kit['splash_makepad_dir']
    out.mkdir(parents=True, exist_ok=True)
    if not kit['screens']:
        raise RuntimeError('no screens selected')
    portable = {name: validate(kit, name) for name in kit['screens']}
    print(f"portable: {len(portable)} complete cards through splash-makepad", flush=True)
    if check_only:
        return
    # Binding the configured port is mandatory: never accept another kit's server.
    served = set()
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(kit['img_dir']), **kwargs)
        def log_request(self, code='-', size='-'):
            if str(code) == '200':
                served.add(urlparse(self.path).path)
            super().log_request(code, size)
    handler = Handler
    server = http.server.ThreadingHTTPServer(('127.0.0.1', kit['img_port']), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    bridge = None
    build = None
    try:
        bridge = (SharedBridge(os.environ['BEAUTY_BRIDGE']) if os.environ.get('BEAUTY_BRIDGE')
                  else Bridge(address, out / 'studio.jsonl'))
        bridge.send('ListBuilds', [])
        for old in bridge.wait('Builds')['builds']:
            if old.get('mount') == 'splashref' and old.get('package') in ('splash-beauty-host','splash-beauty-studio-host'):
                bridge.send('ClearBuild', {'build_id': old['build_id']})
        # Configure Startup, then use the native resize operation for tall
        # artboards. Every capture still checks its own requested frame.
        sizes = {n: tuple(json.loads((kit['specs_dir']/f'{n}.json').read_text())[k]
                         / kit['design_scale'] for k in ('w', 'h')) for n in kit['screens']}
        request_path = HERE / 'work/beauty-request.json'
        embedded = kit.get('studio_embedded',False)
        def request(name, bootstrap=False, updates=None):
            card, data, spec = selected_inputs(kit, name)
            width, height = sizes[name]
            if embedded and build:
                bridge.send('RunViewResize', {'build_id':build,'window_id':0,
                            'width':width,'height':height,'dpi':2.0})
                time.sleep(.25)
            result, layout = evidence_paths(out, name, bootstrap)
            result.unlink(missing_ok=True)
            layout.unlink(missing_ok=True)
            pathlib.Path(str(layout)+'.pending.json').unlink(missing_ok=True)
            r = {'card':str(card), 'data':str(data), 'format':kit.get('input_format', 'l0'), 'kit_dir':str(MOUNT/'components/l0'),
                 'width':width, 'height':height, 'result':str(result), 'layout':str(layout),
                 'nonce':uuid.uuid4().hex,'actions':str(out/f'{name}.semantic-actions.json')}
            semantic=kit['specs_dir'].parent/'semantics'/f'{name}.json'
            if semantic.exists() and json.loads(data.read_text()).get('$kit',{}).get('bindings'):
                stem=name+('.bootstrap' if bootstrap else '')
                r.update(semantic=str(semantic),semantic_result=str(out/f'{stem}.semantic-state.json'),
                         semantic_probe=str(out/f'{stem}.semantic-probe.json'),build_id=build)
            if updates:r['updates']=updates
            temp = request_path.with_suffix('.tmp')
            temp.write_text(json.dumps(r))
            temp.replace(request_path)
            return r, result
        startup_request,startup_result=request(kit['screens'][0], bootstrap=True)
        bridge.send('RunItem', {'mount':'splashref', 'name':
                               'splash-beauty-studio-host' if embedded else 'splash-beauty-host'})
        build = bridge.wait('BuildStarted')['build_id']
        print(f'Studio release build {build}: waiting for native host', flush=True)
        # Standalone Studio RunItems do not emit the embedded AppStarted
        # event. The host's successful mount acknowledgment is stronger.
        if isinstance(bridge,SharedBridge):
            deadline=time.monotonic()+600
            while not startup_result.exists() and time.monotonic()<deadline:
                bridge.send('QueryLogs', {'build_id':build,'level':'error','live':False})
                errors=bridge.wait('QueryLogResults')
                if errors.get('entries'):
                    raise RuntimeError('Studio failed to start: '+json.dumps(errors['entries']))
                time.sleep(1)
            if not startup_result.exists():raise RuntimeError('Studio host did not acknowledge startup')
            if json.loads(startup_result.read_text()).get('request')!=startup_request:
                raise RuntimeError('Studio startup acknowledged a stale request')
        else:
            bridge.wait('NativeMounted', timeout=600)
        shared = shared_inputs(kit)
        semantic_failures=[]
        for name in kit['screens']:
            card, data, spec = selected_inputs(kit, name)
            inputs = fingerprint([*shared, card, data, spec])
            png = out/f'{name}.png'
            meta_path = out/f'{name}.capture.json'
            meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
            if fresh(meta, inputs, png):
                print(f'{name}: current capture (content hashes match)', flush=True)
                continue
            # Invalidate the prior commit before replacing any of its evidence.
            # An interrupted capture may leave files, but never a valid receipt.
            meta_path.unlink(missing_ok=True)
            r, result = request(name)
            deadline = time.monotonic()+30
            while not result.exists() and time.monotonic() < deadline:
                time.sleep(.1)
            if not result.exists():
                raise RuntimeError(f'{name}: no successful native mount acknowledgment; see studio.jsonl')
            native = json.loads(result.read_text())
            if (native.get('request') != r or native['texts'] != portable[name]['texts']
                    or native['elements'] != portable[name]['elements']):
                raise RuntimeError(f'{name}: stale mount or portable/native text mismatch')
            local_images = {urlparse(url).path for url in portable[name].get('images', [])
                            if url.startswith(f"http://127.0.0.1:{kit['img_port']}/")}
            deadline = time.monotonic()+10
            while not local_images.issubset(served) and time.monotonic() < deadline:
                time.sleep(.1)
            if not local_images.issubset(served):
                raise RuntimeError(f'{name}: native host did not load images {local_images-served}')
            time.sleep(.5)
            if embedded:
                ensure_embedded_frame(bridge,build,r['width'],r['height'])
            layout = pathlib.Path(r['layout'])
            deadline = time.monotonic()+10
            while not layout.exists() and time.monotonic()<deadline:
                time.sleep(.1)
            if not layout.exists() or json.loads(layout.read_text()).get('nonce') != r['nonce']:
                pending = pathlib.Path(str(layout)+'.pending.json')
                detail = pending.read_text() if pending.exists() else 'no native layout status'
                raise RuntimeError(f'{name}: missing current native clipping measurements: {detail}')
            if r.get('semantic_result'):
                state=json.loads(pathlib.Path(r['semantic_result']).read_text())
                if state.get('nonce')!=r['nonce'] or state.get('build_id')!=build:
                    raise RuntimeError('stale numerical binding evidence')
                (out/f'{name}.semantic-baseline.json').write_text(json.dumps(state,indent=2)+'\n')
            bridge.send('WidgetTreeDump', {'build_id':build})
            dump = bridge.wait('WidgetTreeDump')
            (out/f'{name}.widgets.json').write_text(json.dumps(dump, indent=2))
            bridge.send('WidgetSnapshot', {'build_id':build})
            snapshot = bridge.wait('WidgetSnapshot')
            (out/f'{name}.snapshot.json').write_text(json.dumps(snapshot, indent=2))
            queries = {}
            pending = {f'id:{element["id"]}':element['id'] for element in portable[name]['elements']}
            # Every query is independent. Pipeline requests through the one
            # persistent bridge, then bind each response to its exact query.
            for query in pending:
                bridge.send('WidgetQuery', {'build_id':build, 'query':query})
            while pending:
                reply = bridge.wait('WidgetQuery')
                if reply.get('build_id') != build or reply.get('query') not in pending:
                    raise RuntimeError(f'{name}: stale or mismatched widget query response')
                wid = pending.pop(reply['query'])
                queries[wid] = reply
            (out/f'{name}.queries.json').write_text(json.dumps(queries, indent=2))
            for attempt in range(3):
                bridge.send('Screenshot', {'build_id':build, 'kind_id':0})
                shot = bridge.wait('Screenshot')
                save_screenshot(shot, png)
                if frame_has_content(kit['targets_dir']/f'{name}.png',png):
                    break
                shutil.copyfile(png,out/f'{name}.blank-attempt-{attempt+1}.png')
                if embedded:
                    # A same-size resize can retain a cleared Studio backing
                    # texture. Force a real reallocation, then restore the
                    # exact requested viewport before taking new evidence.
                    bridge.send('RunViewResize',{'build_id':build,'window_id':0,
                                'width':r['width']+1,'height':r['height'],'dpi':2.0})
                    time.sleep(.2)
                    ensure_embedded_frame(bridge,build,r['width'],r['height'])
                time.sleep(.35)
            else:
                raise RuntimeError(f'{name}: empty native frame after three readbacks; check Studio backing allocation')
            from PIL import Image
            with Image.open(png) as im:
                if (abs(im.width/im.height-r['width']/r['height']) > .01
                        or (embedded and im.size != (round(r['width']*2),round(r['height']*2)))):
                    raise RuntimeError(f'{name}: wrong screenshot frame {im.size}')
            report = gate_structure.evaluate(kit, name)
            # Gate reports are derived and rewritten by audits. Only immutable
            # native observations belong in the capture receipt.
            evidence = [out/f'{name}.{suffix}.json' for suffix in
                        ('widgets','snapshot','queries','layout')]
            if r.get('semantic_result'):evidence.append(out/f'{name}.semantic-baseline.json')
            evidence += check_toggles(bridge,build,name,portable[name],snapshot,out)
            evidence += check_sliders(bridge,build,name,portable[name],out)
            evidence += check_inputs(bridge,build,name,portable[name],out,request)
            evidence += check_radios(bridge,build,name,portable[name],out,request)
            try:
                evidence += semantic_interactions.check(bridge,build,name,portable[name],out,request,save_screenshot,sha)
                evidence += semantic_interactions.check_progress(bridge,build,name,portable[name],out,request,save_screenshot,sha)
            except RuntimeError as error:
                # Keep collecting independent screens for the repair round.
                # The failed report is saved by the probe; no stale successful
                # capture may survive this attempt, and the run still fails.
                meta_path.unlink(missing_ok=True)
                semantic_failures.append((name,str(error)))
                print(f'{name}: semantic interaction FAILED: {error}',flush=True)
                continue
            bridge.send('QueryLogs',{'build_id':build,'level':'error','live':False})
            runtime=bridge.wait('QueryLogResults')
            runtime['requested_build_id']=build
            runtime_path=out/f'{name}.runtime-errors.json'
            runtime_path.write_text(json.dumps(runtime,indent=2)+'\n');evidence.append(runtime_path)
            if runtime.get('entries'):
                meta_path.unlink(missing_ok=True)
                raise RuntimeError(f'{name}: Studio runtime/shader errors: '+str(runtime['entries']))
            pending_meta = meta_path.with_suffix('.pending.json')
            pending_meta.write_text(json.dumps({'inputs':inputs, 'png_sha256':sha(png),
                'inspection_pass':report['inspection_pass'],
                'inspection_sha256':{p.name:sha(p) for p in evidence},
                'build_id':build, 'request':r, 'captured_at':time.time()}, indent=2))
            pending_meta.replace(meta_path)
            print(f'{name}: native capture, {native["nodes"]} nodes, '
                  f'inspection={report["inspection_pass"]}, structure={report["pass"]}, '
                  f'{report.get("failed_checks",0)} differences', flush=True)
            if not report['inspection_pass']:
                raise RuntimeError(f'{name}: incomplete/inconsistent Studio inspection; see {name}.structure.json')
        if semantic_failures:
            raise RuntimeError(f'{len(semantic_failures)} screens failed semantic interactions; see per-screen reports: {semantic_failures}')
    finally:
        if bridge:
            if build:
                bridge.send('ClearBuild', {'build_id':build})
            bridge.close()
        server.shutdown()
        server.server_close()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--kit', required=True)
    p.add_argument('--studio', default=os.environ.get('BEAUTY_STUDIO', '127.0.0.1:8001'))
    p.add_argument('--check-only', action='store_true')
    p.add_argument('--only',action='append',help='screen-name substring; repeat for a focused repair set')
    args = p.parse_args()
    kit = kitconf.load(args.kit)
    if args.only:
        kit['screens'] = [n for n in kit['screens'] if any(part in n for part in args.only)]
    run(kit, args.studio, args.check_only)


if __name__ == '__main__':
    main()
