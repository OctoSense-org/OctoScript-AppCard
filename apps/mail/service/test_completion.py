import base64
from copy import deepcopy
from email.message import EmailMessage
from email.parser import BytesParser
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import attachments
import gmail_sync as gmail
import sending
from account import defaults,validate
from mailbox import decode_message,merge_mailbox
from test_support import SMTPFixture


class SendingTests(unittest.TestCase):
    def test_tls_delivery_reply_headers_durable_duplicate_guard(self):
        with SMTPFixture() as server,tempfile.TemporaryDirectory() as d,patch.object(sending,'PRIVATE',Path(d)),patch.object(sending.ssl,'create_default_context',return_value=server.context):
            config={**defaults('sender@example.com'),'smtp_host':'localhost','smtp_port':str(server.port),'password':'test-password'}
            draft={'id':'one','to':'Reader <reader@example.com>','subject':'Hello ✓','body':'First line\n.dot\nLast line','in_reply_to':'<parent@example.com>','references':'<parent@example.com>'}
            self.assertTrue(sending.smtp_test(config));self.assertEqual(server.messages,[])
            first=sending.submit(config,draft);second=sending.submit(config,draft)
            self.assertEqual(first,second);self.assertEqual(len(server.messages),1)
            parsed=BytesParser().parsebytes(server.messages[0]);self.assertEqual(parsed['In-Reply-To'],'<parent@example.com>')
            self.assertIn(b'\r\n.dot\r\n',server.messages[0])
            self.assertEqual(sending.record_path(config,'one').stat().st_mode&0o777,0o600)

    def test_failures_and_ambiguous_delivery_do_not_resend(self):
        with SMTPFixture() as server,tempfile.TemporaryDirectory() as d,patch.object(sending,'PRIVATE',Path(d)),patch.object(sending.ssl,'create_default_context',return_value=server.context):
            config={**defaults('sender@example.com'),'smtp_host':'localhost','smtp_port':str(server.port),'password':'test'}
            for mode,uncertain in [('auth_fail',False),('reject_recipient',False),('reject_data',False),('disconnect_data',True)]:
                server.mode=mode;server.commands.clear();server.messages.clear()
                draft={'id':mode,'to':'reader@example.com','subject':'Fixture','body':'Test only'}
                with self.assertRaises(sending.SendFailure) as error:sending.submit(config,draft)
                self.assertEqual(error.exception.uncertain,uncertain)
                if mode=='reject_recipient':self.assertNotIn('DATA',server.commands)
                if uncertain:
                    count=len(server.commands)
                    with self.assertRaises(sending.SendFailure):sending.submit(config,draft)
                    self.assertEqual(len(server.commands),count)
                    self.assertEqual(sending.find_record(config,mode)['status'],'uncertain')
            server.mode='quit_error'
            self.assertEqual(sending.submit(config,{'id':'accepted','to':'reader@example.com','subject':'Accepted','body':'Test'})['status'],'sent')

    def test_injection_and_invalid_recipients_rejected_before_network(self):
        config={**defaults('sender@example.com'),'password':'test'}
        for to in ('','not-an-address','a@example.com\r\nBcc: x@example.com'):
            with self.assertRaises(ValueError):sending.prepare(config,{'to':to})
        with self.assertRaises(ValueError):sending.prepare(config,{'to':'a@example.com','subject':'Hello\nBcc: x@example.com'})
        self.assertEqual(sending.recipients('a@example.com, a@example.com'),['a@example.com'])


class AttachmentTests(unittest.TestCase):
    def test_mime_nested_attachments_safe_paths_and_integrity(self):
        msg=EmailMessage();msg['Message-ID']='<attachment@example.com>';msg['Reply-To']='reply@example.com';msg.set_content('Body')
        msg.add_alternative('<p>HTML</p>',subtype='html');msg.get_payload()[1].add_related(b'inline',maintype='image',subtype='png',cid='<image>')
        msg.add_attachment(b'%PDF-1.4 fixture',maintype='application',subtype='pdf',filename='../../report.pdf')
        decoded=decode_message(msg.as_bytes(),'attachment-uid')
        self.assertEqual(decoded['attachments'],1);self.assertEqual(decoded['reply_to'],'reply@example.com')
        with tempfile.TemporaryDirectory() as d,patch.object(attachments,'PRIVATE',Path(d)):
            path=attachments.materialize(defaults('sender@example.com'),decoded,0)
            self.assertEqual(path.name,'report.pdf');self.assertTrue(path.is_relative_to(Path(d)))
            self.assertEqual(path.read_bytes(),b'%PDF-1.4 fixture');self.assertEqual(path.stat().st_mode&0o777,0o600)
            decoded['attachment_items'][0]['data']=base64.b64encode(b'corrupt').decode()
            with self.assertRaises(ValueError):attachments.materialize(defaults(),decoded,0)
        self.assertEqual(attachments.filename('C:\\download\\script.sh'),'script.sh')
        with patch.object(attachments.subprocess,'run') as run,patch.object(attachments.subprocess,'Popen') as popen:
            attachments.open_attachment('/tmp/script.sh');run.assert_called_once();popen.assert_not_called()
            self.assertEqual(run.call_args.args[0][:2],['/usr/bin/open','-R'])


class FakeIMAP:
    def __init__(self,ambiguous=False,fail_store=False):self.calls=[];self.ambiguous=ambiguous;self.fail_store=fail_store;self.raw=None
    def list(self):return 'OK',[b'(\\HasNoChildren) "/" "INBOX"',b'(\\All) "/" "[Gmail]/All Mail"',b'(\\Sent) "/" "[Gmail]/Sent Mail"',b'() "/" "Projects"']
    def select(self,*args,**kwargs):self.calls.append(('SELECT',args,kwargs));return 'OK',[b'1']
    def uid(self,command,*args):
        self.calls.append((command,args))
        if command=='SEARCH':return 'OK',[b'7 8' if self.ambiguous else b'7']
        if command=='STORE':return ('NO',[b'failed']) if self.fail_store else ('OK',[b''])
        if command=='FETCH':
            if args[1]=='(UID RFC822.SIZE)':return 'OK',[b'1 (UID 7 RFC822.SIZE 200)']
            meta=b'1 (UID 7 FLAGS (\\Seen \\Flagged) X-GM-MSGID 123456 X-GM-LABELS ("\\\\Inbox" "Projects") BODY[] {200}'
            raw=b'Message-ID: <test@example.com>\r\nSubject: Fixture\r\nFrom: sender@example.com\r\n\r\nComplete body'
            return 'OK',[(meta,self.raw or raw),b')']
        raise AssertionError(command)
    def logout(self):return 'BYE',[]


class GmailTests(unittest.TestCase):
    def test_modified_utf7_and_metadata_parser(self):
        for name in ('Projects','收件箱 & Stuff','旅行/日本'):self.assertEqual(gmail.decode_name(gmail.encode_name(name)),name)
        meta=gmail.metadata(b'12 (UID 7 FLAGS (\\Seen) X-GM-MSGID 123 X-GM-LABELS ("\\\\Inbox" "Label with spaces") RFC822.SIZE 900)')
        self.assertFalse(meta['unread']);self.assertFalse(meta['archived']);self.assertEqual(meta['labels'],['\\Inbox','Label with spaces'])
        self.assertEqual(meta['size'],900)

    def test_pull_flags_and_folder_downloads_never_mark_read(self):
        fake=FakeIMAP();message={'id':'local','message_id':'<test@example.com>','unread':True}
        with patch.object(gmail,'connect',return_value=fake):
            rows,folders=gmail.pull(defaults(),[message])
            self.assertFalse(rows[0]['unread']);self.assertTrue(rows[0]['flagged']);self.assertFalse(rows[0]['archived'])
            folder=next(f for f in folders if f['name']=='Projects');result=gmail.fetch_folder(defaults(),folder)
            self.assertEqual(result['messages'][0]['gmail_id'],'123456');self.assertFalse(result['more'])
        fetches=[c for c in fake.calls if c[0]=='FETCH']
        self.assertTrue(all('BODY.PEEK' in c[1][1] or 'RFC822.SIZE' in c[1][1] for c in fetches))
        self.assertTrue(all(c[2]['readonly'] for c in fake.calls if c[0]=='SELECT'))
        self.assertFalse(any(c[0]=='STORE' for c in fake.calls))

    def test_remote_targets_reversible_without_deleting_and_failures_retained(self):
        fake=FakeIMAP();rows=[{'id':'one','message_id':'<test@example.com>'}]
        operations={'one':{'version':'v1','values':{'unread':False,'flagged':True,'archived':True,'label:Projects':True}}}
        with patch.object(gmail,'connect',return_value=fake):
            result=gmail.apply(defaults(),rows,operations);self.assertEqual(result['done'],[('one','v1')])
            commands=[c[1] for c in fake.calls if c[0]=='STORE']
            self.assertIn(('7','+FLAGS.SILENT','(\\Seen)'),commands)
            self.assertIn(('7','-X-GM-LABELS','("\\\\Inbox")'),commands)
            self.assertFalse(any('Deleted' in str(c) or 'EXPUNGE' in str(c) for c in fake.calls))
            fake.fail_store=True;result=gmail.apply(defaults(),rows,operations)
            self.assertEqual(result['done'],[]);self.assertTrue(result['error'])
            fake.fail_store=False;fake.ambiguous=True;fake.calls.clear()
            self.assertTrue(gmail.apply(defaults(),rows,operations)['error'])
            self.assertFalse(any(c[0]=='STORE' for c in fake.calls))

    def test_real_refresh_replaces_sample_mail(self):
        from mailbox import fixture
        sample=fixture();real={'address':'real@example.com','messages':[dict(sample['messages'][0],id='real-message')]}
        self.assertEqual([m['id'] for m in merge_mailbox(sample,real)['messages']],['real-message'])

    def test_reused_rfc_ids_do_not_collapse_distinct_pop_mail(self):
        msg=EmailMessage();msg['Message-ID']='<same@example.com>';msg.set_content('Content')
        a=decode_message(msg.as_bytes(),'pop-one');b=decode_message(msg.as_bytes(),'pop-two')
        self.assertEqual(len(merge_mailbox({'messages':[a]},{'messages':[b]})['messages']),2)
        sent=decode_message(msg.as_bytes(),'sent:<same@example.com>')
        merged=merge_mailbox({'messages':[sent]},{'messages':[a]})
        self.assertEqual(len(merged['messages']),1);self.assertEqual(merged['messages'][0]['uid'],'pop-one')

    def test_remote_merge_deduplicates_pop_and_sent_while_accepting_server_flags(self):
        msg=EmailMessage();msg['Message-ID']='<same@example.com>';msg.set_content('Content')
        pop=decode_message(msg.as_bytes(),'pop-uid');sent=decode_message(msg.as_bytes(),'sent:<same@example.com>')
        sent.update(unread=False,flagged=True,archived=True,server_state=True,labels=['\\Sent'])
        merged=merge_mailbox({'messages':[pop],'available':5},{'messages':[sent]})
        self.assertEqual(len(merged['messages']),1);self.assertEqual(merged['messages'][0]['uid'],'pop-uid')
        self.assertTrue(merged['messages'][0]['flagged']);self.assertTrue(merged['has_more'])

if __name__=='__main__':unittest.main()
