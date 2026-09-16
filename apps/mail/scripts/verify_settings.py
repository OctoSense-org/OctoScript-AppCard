"""Native server-settings controls with isolated credentials and mailbox caches."""
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import struct
import subprocess
import sys
import tempfile
import time
from unittest.mock import patch
import argparse
import run as app_run
from run import MailSession, launch_native
from common import ROOT
import mailbox
from mailbox import atomic_json, fixture
from account import defaults, account_id, save_account, load_account
from stop import stop
from instrument import settled, read


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--keep-closed',action='store_true');options=parser.parse_args()
    stop();process=None;instrument=None
    out=ROOT/'evidence'/('settings-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'));out.mkdir(parents=True)
    checks=[]
    try:
        with tempfile.TemporaryDirectory() as d:
            private=Path(d)/'mail';private.mkdir()
            with patch.dict(os.environ,{'OCTOS_MAIL_CREDENTIALS':str(Path(d)/'credentials.json')}),patch.object(app_run,'PRIVATE',private),patch.object(mailbox,'PRIVATE',private):
                config={**defaults('reader@example.com'),'password':'fixture-original-secret'};save_account(config)
                box=fixture();box.update(address=config['address'],host=config['host'],account_id=account_id(config))
                atomic_json(private/'mailbox.json',box)
                atomic_json(private/'local-state.json',{'drafts':[{'to':'draft@example.com','subject':'Saved draft','body':'Local content'}],'draft':{'to':'','subject':'','body':''}})
                app=MailSession();app.state['screen']='mailboxes'
                process,instrument=launch_native(app,hidden=True);build=app.build;settled()
                (out/'protocol.txt').write_text(instrument.get('/'))

                def pump(seconds=.9):
                    end=time.monotonic()+seconds
                    while time.monotonic()<end:app.poll();time.sleep(.06)
                    settled()

                def click(ident):
                    meta=settled();n=next(n for n in read(meta['mapping'])['elements'] if n['source_id']==ident)
                    widget=next(w for w in instrument.get('/snap',q=n['native_id'])['s'] if w['i']==n['native_id'])
                    x,y,w,h=widget['r']
                    instrument.get('/click',x=round(x+w/2),y=round(y+h/2),wait=1);pump()

                def replace(key,value):
                    click('server_'+key+'_input')
                    instrument.get('/k',k='press',c='KeyA',cmd=1,wait=1)
                    instrument.get('/t',t=value,wait=1);pump()
                    assert app.state['account_form'][key]==value,(key,app.state['account_form'][key])

                def capture(name):
                    meta=settled();snap=instrument.get('/snap',all=1)
                    mapping=read(meta['mapping'])['elements'];widgets={w['i']:w for w in snap['s']}
                    for n in mapping:
                        if n['kind']=='input':assert widgets[n['native_id']]['ty']=='TextInput'
                    atomic_json(out/(name+'-snapshot.json'),snap);atomic_json(out/(name+'-mapping.json'),read(meta['mapping']))
                    instrument.grab(out/(name+'.png'))

                subprocess.run(['swiftc',str(ROOT/'service/password_prompt.swift'),'-o',str(ROOT/'runtime/mail-password-prompt')],check=True,capture_output=True)

                def password(value):
                    completed=subprocess.CompletedProcess([],0,json.dumps({'password':value}),'')
                    with patch.object(app_run.subprocess,'run',return_value=completed) as prompt:
                        click('server_password_control');pump()
                        assert prompt.call_count==1
                        assert prompt.call_args.args[0]==[str(ROOT/'runtime/mail-password-prompt')]
                    assert app.state['password_pending']
                    for path in Path(app.meta['mapping']).parent.glob('*'):
                        if path.is_file() and path.suffix in ('.json','.card','.splash'):
                            assert value not in path.read_text(),path.name
                    assert value not in (ROOT/'runtime/session/state.json').read_text()

                click('settings_control')
                assert app.state['screen']=='settings'
                capture('01-settings')
                replace('port','70000');click('save_server_control')
                assert 'Port must' in app.state['account_error'] and load_account()['port']=='995'
                capture('02-validation')
                replace('port','1995');click('save_server_control')
                assert load_account()['port']=='1995' and load_account()['password']==config['password']
                checks.append('Native editable fields validate port, save configuration and preserve the existing password')
                with patch.object(app_run,'test_connection',return_value=42) as connection:
                    click('test_server_control');pump()
                    assert connection.call_args.args[0]['port']=='1995'
                    assert '42 messages' in app.state['account_status'] and not app.state['account_error']
                with patch.object(app_run,'test_connection',side_effect=OSError('private diagnostic')):
                    click('test_server_control');pump()
                    assert app.state['account_error'].startswith('Connection failed')
                click('security_starttls_control');assert app.state['account_form']['port']=='1995'
                replace('port','110');click('security_tls_control');assert app.state['account_form']['port']=='995'
                click('recent_toggle_control');assert not app.state['account_form']['recent']
                password('fixture-new-secret');click('save_server_control')
                assert load_account()['password']=='fixture-new-secret' and not load_account()['recent']
                assert not app.state['password_pending']
                checks.append('Test Connection uses edited values, reports success/failure; TLS mode and Gmail recent-mode controls work')
                checks.append('Secure-dialog result stays out of state, cards and native action logs; Save commits the password')

                replace('host','pop.other.example');replace('username','other-login');replace('address','other@example.com')
                click('save_server_control');assert 'Set a password' in app.state['account_error']
                password('fixture-other-secret');click('save_server_control')
                assert not app.state['mailbox']['messages'] and not app.state['drafts']
                assert (private/'accounts'/account_id(config)/'mailbox.json').exists()
                capture('03-custom-server')
                replace('host',config['host']);replace('username',config['username']);replace('address',config['address'])
                password(config['password']);click('save_server_control')
                assert len(app.state['mailbox']['messages'])==5 and app.state['drafts'][0]['subject']=='Saved draft'
                checks.append('Changing server requires its own password, isolates mail/drafts and restores the previous account cache')
                replace('host','unsaved.example');click('back_control');assert app.state['screen']=='mailboxes'
                click('settings_control');assert app.state['account_form']['host']==config['host']
                with patch.object(app_run,'test_connection',return_value=42):click('test_server_control');pump()
                capture('04-connected')
                checks.append('Leaving settings discards unsaved edits; saved settings reload on reopening')
                result={'passed':True,'build_id':build,'native_pid':process.pid,'hidden':True,'nonce':app.meta['request']['nonce'],'checks':checks,
                    'instrument':'Makepad built-in HTTP /snap, /click, /k, /t, /g; standalone release, hidden window; no Studio',
                    'password_dialog':'Compiled AppKit NSSecureTextField; controller result tested using an isolated subprocess fixture'}
                atomic_json(out/'result.json',result);atomic_json(ROOT/'evidence/latest-settings.json',{'directory':str(out.relative_to(ROOT)),**result})
                print(json.dumps(result),flush=True)
    finally:
        if process is not None and process.poll() is None:
            try:instrument.grab(out/'final.png',quit=True)
            except Exception:
                if process.poll() is None:
                    try:instrument.get('/quit')
                    except Exception:pass
            process.wait(timeout=10)
        if not options.keep_closed:subprocess.run([sys.executable,str(ROOT/'scripts/run.py'),'--background'],cwd=ROOT,check=True)


if __name__=='__main__':main()
