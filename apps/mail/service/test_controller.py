"""Durability and async races that cannot be reliably forced with UI timing."""
from contextlib import ExitStack
from copy import deepcopy
from pathlib import Path
import os
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import run as app_run
import mailbox
import sending
from mailbox import atomic_json,fixture
from account import defaults,save_account,account_id
from model import visible


class ControllerTests(unittest.TestCase):
    def setUp(self):
        self.stack=ExitStack();self.addCleanup(self.stack.close)
        self.temp=self.stack.enter_context(tempfile.TemporaryDirectory());self.private=Path(self.temp)/'private'
        self.stack.enter_context(patch.dict(os.environ,{'OCTOS_MAIL_CREDENTIALS':str(Path(self.temp)/'credentials.json')}))
        for module in (app_run,mailbox,sending):self.stack.enter_context(patch.object(module,'PRIVATE',self.private))
        self.config={**defaults('fixture@example.com'),'password':'test'};save_account(self.config)
        box=fixture();box.update(address=self.config['address'],account_id=account_id(self.config))
        for m in box['messages']:m.update(source='gmail',message_id='<'+m['id']+'@example.com>',labels=['\\Inbox'])
        atomic_json(self.private/'mailbox.json',box)
        self.stack.enter_context(patch.object(app_run.MailSession,'mount',lambda self:self.persist()))
        self.app=app_run.MailSession()

    def test_pending_version_ack_cannot_erase_newer_intent(self):
        app=self.app;app.queue_values('demo-0',{'flagged':True});old=deepcopy(app.state['pending_sync']['demo-0'])
        app.queue_values('demo-0',{'flagged':False})
        with patch.object(app,'start_remote') as worker:
            app.mail_update('remote_done',{'done':[('demo-0',old['version'])],'error':''},app.mailbox_epoch)
            worker.assert_called_once()
        self.assertFalse(app.state['pending_sync']['demo-0']['values']['flagged'])
        restarted=app_run.MailSession();self.assertEqual(restarted.state['pending_sync'],app.state['pending_sync'])
        epoch=app.mailbox_epoch;app.mailbox_epoch+=1
        app.mail_update('remote_done',{'done':[('demo-0',app.state['pending_sync']['demo-0']['version'])]},epoch)
        self.assertTrue(app.state['pending_sync'])

    def test_pull_overlays_pending_and_serializes_against_folder_download(self):
        app=self.app;app.queue_values('demo-0',{'unread':False,'archived':True,'label:Projects':True})
        app.overlay_pending();m=app.state['mailbox']['messages'][0]
        self.assertFalse(m['unread']);self.assertNotIn('\\Inbox',m['labels']);self.assertIn('Projects',m['labels'])
        app.state['loading_more']=True
        with patch.object(app,'worker') as worker:app.start_remote();worker.assert_not_called()
        app.state['loading_more']=False
        with patch.object(app,'worker') as worker:app.start_remote();worker.assert_called_once()

    def test_delivery_journal_recovers_unconfirmed_and_confirmed_drafts(self):
        app=self.app;draft={'id':'persisted','to':'receiver@example.com','subject':'Fixture','body':'Body'}
        app.state['draft']=draft;app.state['drafts']=[draft];app.persist()
        record={'draft_id':'persisted','message_id':'<delivery@example.com>','to':draft['to'],'subject':draft['subject'],'body':draft['body'],'status':'sending','account_id':account_id(self.config)}
        path=sending.record_path(self.config,'persisted');atomic_json(path,record)
        restarted=app_run.MailSession();self.assertTrue(restarted.state['send_uncertain'])
        with patch.object(sending,'submit') as submit:restarted.start_send();submit.assert_not_called()
        record['status']='sent';atomic_json(path,record)
        restarted=app_run.MailSession();self.assertFalse(restarted.state['drafts'])
        self.assertEqual(len([m for m in restarted.state['mailbox']['messages'] if m.get('message_id')==record['message_id']]),1)

    def test_folder_membership_refresh_pagination_and_pending_labels(self):
        app=self.app;app.state['folder']='remote:Projects';app.state['folders']=[{'wire':'Projects','label':'Projects','name':'Projects'}]
        first=deepcopy(app.state['mailbox']['messages'][0]);first.update(labels=['Projects'],archived=True,server_state=True)
        second=deepcopy(app.state['mailbox']['messages'][1]);second.update(labels=['Projects'],archived=True,server_state=True)
        app.mail_update('folder_done',{'folder':'Projects','append':False,'messages':[first],'cursor':100,'more':True,'skipped':0},0)
        self.assertEqual([m['id'] for m in visible(app.state)],['demo-0'])
        app.mail_update('folder_done',{'folder':'Projects','append':True,'messages':[second],'cursor':70,'more':False,'skipped':0},0)
        self.assertEqual(len(visible(app.state)),2)
        app.mail_update('folder_done',{'folder':'Projects','append':False,'messages':[second],'cursor':70,'more':False,'skipped':0},0)
        self.assertEqual([m['id'] for m in visible(app.state)],['demo-1'])

if __name__=='__main__':unittest.main()
