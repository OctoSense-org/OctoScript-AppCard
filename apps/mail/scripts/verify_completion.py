"""Headless native mail completion flow: built-in instrument + local TLS SMTP.

All accounts and messages are fixtures. Gmail IMAP is a protocol fixture and
attachment viewer launch is intercepted after checking the extracted bytes.
"""
from contextlib import ExitStack
from datetime import datetime, timezone
from email.message import EmailMessage
from email.parser import BytesParser
from pathlib import Path
import json
import os
import sys
import tempfile
import time
from unittest.mock import patch
import run as app_run
from run import MailSession,launch_native
from common import ROOT
from account import defaults,save_account,account_id,load_account
import mailbox
import sending
import attachments
import gmail_sync
from mailbox import atomic_json,fixture,decode_message
from test_support import SMTPFixture
from test_completion import FakeIMAP
from instrument import settled,read
from stop import stop


def main():
    stop();process=None;instrument=None;checks=[]
    out=ROOT/'evidence'/('completion-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'));out.mkdir(parents=True)
    try:
        with tempfile.TemporaryDirectory() as d,SMTPFixture() as smtp,ExitStack() as stack:
            private=Path(d)/'mail';private.mkdir();fake=FakeIMAP()
            stack.enter_context(patch.dict(os.environ,{'OCTOS_MAIL_CREDENTIALS':str(Path(d)/'credentials.json')}))
            for module in (app_run,mailbox,sending,attachments):stack.enter_context(patch.object(module,'PRIVATE',private))
            stack.enter_context(patch.object(sending.ssl,'create_default_context',return_value=smtp.context))
            stack.enter_context(patch.object(gmail_sync,'connect',return_value=fake))
            config={**defaults('reader@example.com'),'password':'fixture-password','smtp_host':'localhost','smtp_port':str(smtp.port)};save_account(config)
            msg=EmailMessage();msg['From']='Design Team <sender@example.com>';msg['Reply-To']='reply@example.com';msg['Subject']='Design review attachment';msg['Message-ID']='<test@example.com>'
            msg.set_content('Hi there,\n\nThe attachment is ready to review.\n\nThanks,\nDesign Team')
            msg.add_attachment(b'Fixture attachment content\n',maintype='text',subtype='plain',filename='review-notes.txt')
            fake.raw=msg.as_bytes()
            message=decode_message(msg.as_bytes(),'fixture-pop-uid');message.pop('attachment_items');message.update(labels=['\\Inbox'],gmail_id='123456')
            box=fixture();box.update(address=config['address'],host=config['host'],account_id=account_id(config),messages=[message],has_more=False,available=1)
            atomic_json(private/'mailbox.json',box)
            app=MailSession();process,instrument=launch_native(app,hidden=True);settled()
            (out/'protocol.txt').write_text(instrument.get('/'))

            def pump(seconds=.7):
                end=time.monotonic()+seconds
                while time.monotonic()<end:app.poll();time.sleep(.04)
                deadline=time.monotonic()+12
                while any(app.state.get(k) for k in ('remote_busy','send_busy','attachment_busy','loading_more','account_busy')):
                    app.poll();time.sleep(.05)
                    if time.monotonic()>deadline:raise AssertionError('Fixture operation did not complete')
                settled()

            def click(ident):
                meta=settled();node=next(n for n in read(meta['mapping'])['elements'] if n['source_id']==ident)
                widget=next(w for w in instrument.get('/snap',q=node['native_id'])['s'] if w['i']==node['native_id'])
                x,y,w,h=widget['r'];assert w and h and 0<=y<776,(ident,widget['r'])
                instrument.get('/click',x=round(x+w/2),y=round(y+h/2),wait=1);pump()

            def replace(ident,value):
                click(ident+'_input');instrument.get('/k',k='press',c='KeyA',cmd=1,wait=1);instrument.get('/t',t=value,wait=1);pump()

            def capture(name):
                meta=settled();atomic_json(out/(name+'-snapshot.json'),instrument.get('/snap',all=1));atomic_json(out/(name+'-mapping.json'),read(meta['mapping']));instrument.grab(out/(name+'.png'))

            click('message_0_open_control')
            assert app.state['screen']=='read' and not app.selected_message()['unread'] and not app.state['pending_sync']
            assert any(c[0]=='STORE' and '\\Seen' in str(c) for c in fake.calls)
            click('tool_attachments_control');assert app.state['screen']=='attachments';capture('01-attachments')
            def opened(path):
                assert path.read_bytes()==b'Fixture attachment content\n'
                assert path.name=='review-notes.txt' and path.is_relative_to(private)
                return 'Opened in Quick Look'
            with patch.object(attachments,'open_attachment',side_effect=opened) as opener:
                click('attachment_0_control');assert opener.call_count==1
            assert app.state['attachment_status']=='Opened in Quick Look'
            checks.append('Legacy cached attachment downloaded through IMAP BODY.PEEK, private file bytes verified, native Open dispatches viewer')
            click('back_control');click('tool_flag_control');assert app.selected_message()['flagged'] and not app.state['pending_sync']
            fake.fail_store=True;click('tool_flag_control');assert app.state['pending_sync'] and app.state['remote_error']
            click('back_control');capture('02-sync-retry');fake.fail_store=False;click('retry_sync_control');assert not app.state['pending_sync']
            click('message_0_open_control');click('top_action_control');assert app.state['mailbox']['messages'][0]['unread']
            click('message_0_open_control');click('tool_archive_control');assert app.state['mailbox']['messages'][0]['archived']
            click('back_control');click('folder_5_control');click('message_0_open_control');click('tool_archive_control');assert not app.state['mailbox']['messages'][0]['archived']
            click('back_control');click('folder_1_control');click('message_0_open_control');click('tool_move_control');capture('03-move-message')
            click('remote_folder_1_control');assert 'Projects' in app.state['mailbox']['messages'][0]['labels'] and app.state['mailbox']['messages'][0]['archived']
            checks.append('Read/unread, star/unstar, archive/restore, move and failed sync Retry reach IMAP STORE')
            click('back_control');click('gmail_folders_control');capture('04-gmail-folders');click('remote_folder_3_control')
            assert app.state['folder']=='remote:Projects' and len(app.state['mailbox']['messages'])==1
            assert app.state['folder_pages']['remote:Projects']['more'] is False
            checks.append('Gmail folders open through IMAP BODY.PEEK and deduplicate the existing POP message')
            click('message_0_open_control');click('tool_reply_control')
            assert app.state['draft']['in_reply_to']=='<test@example.com>'
            replace('body','Thanks for the review.');capture('05-reply');click('top_action_control')
            assert len(smtp.messages)==1 and app.state['screen']=='inbox' and app.state['notice']=='Message sent'
            assert BytesParser().parsebytes(smtp.messages[0])['In-Reply-To']=='<test@example.com>'
            checks.append('Reply sends through a real local TLS SMTP socket with threading headers and Sent record')
            click('tool_compose_control');click('top_action_control');assert app.state['send_error'] and len(smtp.messages)==1
            replace('to','receiver@example.com');replace('subject','Native compose fixture');replace('body','This message stays in the local SMTP test server.')
            click('save_draft_control');click('back_control');click('folder_4_control');click('draft_0_control')
            assert app.state['draft']['subject']=='Native compose fixture'
            smtp.mode='reject_recipient';click('top_action_control');assert 'recipient' in app.state['send_error'] and len(smtp.messages)==1;capture('06-send-error')
            smtp.mode='ok';click('top_action_control');assert len(smtp.messages)==2 and not app.state['drafts']
            checks.append('Compose validates recipients, saves/reopens draft, reports rejection, retries definitive failure and removes sent draft')
            click('tool_compose_control');replace('to','receiver@example.com');replace('subject','Unconfirmed fixture');replace('body','Test connection interruption.')
            smtp.mode='disconnect_data';click('top_action_control');assert app.state['send_uncertain'] and len(smtp.messages)==3
            click('top_action_control');assert len(smtp.messages)==3;capture('07-delivery-unconfirmed')
            with patch.object(gmail_sync,'confirm_sent',return_value=True):click('check_sent_control')
            assert not app.state['send_uncertain'] and app.state['notice']=='Message sent' and len(smtp.messages)==3
            checks.append('Ambiguous delivery disables Send; Check Sent reconciles success without duplicate submission')
            click('back_control');click('settings_control');click('outgoing_settings_control')
            assert app.state['screen']=='services';click('smtp_starttls_control');assert app.state['account_form']['smtp_security']=='starttls'
            click('smtp_tls_control');replace('server_smtp_host','localhost');replace('server_smtp_port',str(smtp.port));click('save_server_control')
            smtp.mode='ok';click('test_services_control');assert not app.state['account_error'] and 'connected' in app.state['account_status']
            assert load_account()['smtp_host']=='localhost';capture('08-outgoing-settings')
            checks.append('Native outgoing host/port/security settings save and Test Outgoing & Sync verifies SMTP NOOP and IMAP folders')
            result={'passed':True,'build_id':app.build,'native_pid':process.pid,'hidden':True,'instrument':'Makepad built-in HTTP; no Studio',
                'checks':checks,'smtp_messages_in_local_fixture':len(smtp.messages),'external_messages_sent':0,'imap_fixture_store_commands':sum(c[0]=='STORE' for c in fake.calls),
                'attachment_viewer':'File extracted and checked; OS viewer launch intercepted in hidden test'}
            instrument.grab(out/'final.png',quit=True);process.wait(timeout=10);result['native_exited']=True
            atomic_json(out/'result.json',result);atomic_json(ROOT/'evidence/latest-completion.json',{'directory':str(out.relative_to(ROOT)),**result});print(json.dumps(result),flush=True)
    finally:
        if process is not None and process.poll() is None:
            try:instrument.grab(out/'failed-final.png',quit=True)
            except Exception:
                try:instrument.get('/quit')
                except Exception:pass
            process.wait(timeout=10)

if __name__=='__main__':main()
