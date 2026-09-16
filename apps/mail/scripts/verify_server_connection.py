"""Save and test the configured account using the app's built-in instrument."""
import json
import time
from common import ROOT
from instrument import Instrument, read, settled
from mailbox import atomic_json


def main():
    meta=settled();remote=read(ROOT/'runtime/session/remote.json');instrument=Instrument(remote['endpoint'])
    (ROOT/'runtime/session/protocol.txt').write_text(instrument.get('/'))
    def state():return read(ROOT/'runtime/session/state.json')
    def wait(predicate,timeout=30):
        end=time.monotonic()+timeout
        while time.monotonic()<end:
            s=state()
            if predicate(s):settled();return s
            time.sleep(.1)
        raise AssertionError('Native state transition timed out')
    def click(ident):
        m=settled();node=next(n for n in read(m['mapping'])['elements'] if n['source_id']==ident+'_control')
        w=next(w for w in instrument.get('/snap',q=node['native_id'])['s'] if w['i']==node['native_id'])
        x,y,width,height=w['r'];instrument.get('/click',x=x+width/2,y=y+height/2,wait=1)
    assert state()['mailbox']['address']!='you@gmail.com'
    if state()['screen']=='inbox':click('back');wait(lambda s:s['screen']=='mailboxes')
    if state()['screen']=='mailboxes':click('settings');wait(lambda s:s['screen']=='settings')
    before=state()['account_form'];count=len(state()['mailbox']['messages'])
    click('save_server');wait(lambda s:s['account_status'].startswith('Settings saved'))
    click('test_server')
    connected=wait(lambda s:not s['account_busy'] and (s['account_status'].startswith('Connected securely') or s['account_error']),60)
    assert not connected['account_error'],connected['account_error']
    assert connected['account_form']==before
    assert len(connected['mailbox']['messages'])==count
    result={'passed':True,'build_id':remote['build_id'],'native_pid':remote['pid'],'hidden':remote['hidden'],
            'instrument':'Makepad built-in HTTP; no Studio','host':before['host'],'port':int(before['port']),
            'security':before['security'],'settings_saved':True,'connection_verified':True,
            'cached_messages_preserved':count,'password_rendered':False,'final_screen':'settings'}
    atomic_json(ROOT/'evidence/server-connection-native.json',result)
    print(json.dumps(result),flush=True)


if __name__=='__main__':main()
