"""Makepad's built-in HTTP instrument, connected directly to the owned app."""
import json
from pathlib import Path
import time
from urllib.parse import urlencode
from urllib.request import urlopen


class Instrument:
    def __init__(self,endpoint):self.endpoint=endpoint.rstrip('/')

    def get(self,path,**params):
        url=self.endpoint+path+('?' + urlencode(params) if params else '')
        with urlopen(url,timeout=30) as response:
            body=response.read()
            if response.headers.get_content_type()=='image/png':return body
        text=body.decode()
        try:data=json.loads(text)
        except ValueError:return text
        if isinstance(data,dict) and data.get('err'):raise RuntimeError(data['err'])
        return data

    def grab(self,path,quit=False):
        data=self.get('/gq' if quit else '/g')
        def pngs(value):
            if isinstance(value,dict):
                if isinstance(value.get('png'),str):yield value['png']
                elif isinstance(value.get('png'),list):yield from value['png']
                for key,item in value.items():
                    if key!='png':yield from pngs(item)
            elif isinstance(value,list):
                for item in value:yield from pngs(item)
        source=next(pngs(data),None)
        if not source:raise RuntimeError('Native instrument did not return a drawable capture')
        Path(path).write_bytes(Path(source).read_bytes())
        return data


def read(path):return json.loads(Path(path).read_text())


def settled(timeout=25,poll=None):
    from common import ROOT
    end=time.monotonic()+timeout
    status={}
    while time.monotonic()<end:
        if poll is not None:poll()
        try:
            meta=read(ROOT/'runtime/session/session.json');r=meta['request']
            native,layout=read(r['result']),read(r['layout'])
            state=read(ROOT/'runtime/session/state.json')
            status={'native_ok':native.get('ok'),'layout_matches':layout.get('nonce')==r['nonce'],
                    'build_matches':native.get('request',{}).get('build_id')==r['build_id'],
                    'screen':state.get('screen'),'mount_revision':meta.get('revision'),'state_revision':state.get('revision')}
            if native.get('ok') and layout.get('nonce')==r['nonce'] and native['request'].get('build_id')==r['build_id'] and (state['screen']=='compose' or meta['revision']==state['revision']):return meta
        except (OSError,ValueError):pass
        time.sleep(.1)
    raise RuntimeError('Native scene did not settle: '+json.dumps(status))
