import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from mailbox import decode_message, fetch_gmail, fixture, save_live
from model import initial, reduce, visible
from account import defaults


class MessageTests(unittest.TestCase):
    def test_long_message_keeps_final_content(self):
        from email.message import EmailMessage
        message=EmailMessage()
        body=('Complete message content.\n'*1200)+'FINAL MESSAGE LINE'
        message.set_content(body)
        self.assertEqual(decode_message(message.as_bytes(),'long')['body'],body)

    def test_mime_unicode_html_attachments(self):
        raw=b'From: =?utf-8?b?Sm9zw6k=?= <jose@example.com>\r\nSubject: =?utf-8?q?Hello_=E2=9C=93?=\r\nMIME-Version: 1.0\r\nContent-Type: text/html; charset=utf-8\r\n\r\n<head><style>secret</style></head><p>Hi &amp; welcome</p><script>evil()</script><img src="https://example.com/track">'
        m=decode_message(raw,'uid-1')
        self.assertEqual(m['sender'],'José')
        self.assertEqual(m['subject'],'Hello ✓')
        self.assertEqual(m['body'],'Hi & welcome')
        self.assertEqual(m['id'],decode_message(raw,'uid-1')['id'])

    def test_multipart_prefers_plain_and_counts_attachment(self):
        from email.message import EmailMessage
        m=EmailMessage();m['From']='a@example.com';m['Subject']='Report'
        m.set_content('Plain body');m.add_alternative('<b>HTML body</b>',subtype='html')
        m.add_attachment(b'file',maintype='application',subtype='pdf',filename='report.pdf')
        result=decode_message(m.as_bytes(),'abc')
        self.assertEqual(result['body'],'Plain body')
        self.assertIn('<b>HTML body</b>',result['html'])
        self.assertEqual(result['attachments'],1)

    def test_html_preserves_format_and_embedded_images_without_active_content(self):
        from email.message import EmailMessage
        from html_mail import document
        m=EmailMessage();m['Subject']='HTML <reader>'
        m.set_content('Plain fallback')
        m.add_alternative('<style>p{color:blue}</style><p><b>Rich content</b></p><img src="cid:badge" onerror="alert(1)"><script>window.emailScriptExecuted=true</script><form action="https://example.com"><input name="secret"></form>',subtype='html')
        m.get_payload()[1].add_related(b'inline image',maintype='image',subtype='png',cid='<badge>')
        decoded=decode_message(m.as_bytes(),'html')
        page=document(decoded,'you@gmail.com')
        self.assertIn('<b>Rich content</b>',page)
        self.assertIn('<style>p{color:blue}</style>',page)
        self.assertIn('src="data:image/png;base64,',page)
        self.assertIn('HTML &lt;reader&gt;',page)
        self.assertIn('Content-Security-Policy',page)
        self.assertNotIn('<script',page)
        self.assertNotIn('onerror',page)
        self.assertNotIn('<form',page)
        self.assertIn("img-src data:;",page)
        decoded['load_remote_images']=True
        self.assertIn("img-src data: https: http:;",document(decoded,'you@gmail.com'))

    def test_pop_uses_tls_recent_uidl_bounded_download_and_quit(self):
        calls=[]
        class Fake:
            def __init__(self,host,port,timeout,context):
                calls.append(('connect',host,port));assert context.check_hostname
            def user(self,value):calls.append(('user',value))
            def pass_(self,value):calls.append(('auth',))
            def stat(self):return 3,300
            def uidl(self):return b'+OK',[b'1 one',b'2 two',b'3 three'],0
            def list(self):return b'+OK',[b'1 20',b'2 3000000',b'3 20'],0
            def retr(self,n):calls.append(('retr',n));return b'+OK',[b'From: a@example.com',b'Subject: Hello',b'',b'Body'],0
            def quit(self):calls.append(('quit',))
        with patch('mailbox.load_account',return_value={**defaults('you@gmail.com'),'password':'local'}),patch('mailbox.poplib.POP3_SSL',Fake):
            result=fetch_gmail(2)
        self.assertIn(('user','recent:you@gmail.com'),calls)
        self.assertEqual([c for c in calls if c[0]=='retr'],[('retr',3)])
        self.assertEqual(result['skipped_large'],1)
        self.assertEqual(calls[-1],('quit',))
        calls.clear()
        with patch('mailbox.load_account',return_value={**defaults('you@gmail.com'),'password':'local'}),patch('mailbox.poplib.POP3_SSL',Fake):
            fetch_gmail(100,uids={'one'})
        self.assertEqual([c for c in calls if c[0]=='retr'],[('retr',1)])
        calls.clear()
        with patch('mailbox.load_account',return_value={**defaults('you@gmail.com'),'password':'local'}),patch('mailbox.poplib.POP3_SSL',Fake):
            batch=fetch_gmail(1,exclude_uids={'three'})
            self.assertTrue(batch['has_more'])
            self.assertEqual(batch['skipped_uids'],['two'])
            last=fetch_gmail(1,exclude_uids={'three',*batch['skipped_uids']})
            self.assertFalse(last['has_more'])
            self.assertEqual([m['uid'] for m in last['messages']],['one'])
            empty=fetch_gmail(25,exclude_uids={'one','two','three'})
            self.assertFalse(empty['has_more'])
            self.assertEqual(empty['messages'],[])
        self.assertEqual([c for c in calls if c[0]=='retr'],[('retr',1)])

    def test_sync_deduplicates_and_preserves_local_state(self):
        with tempfile.TemporaryDirectory() as d,patch('mailbox.PRIVATE',Path(d)):
            first=fixture();first['messages'][0]['archived']=True
            save_live(first)
            again=save_live(fixture())
            self.assertEqual(len(again['messages']),5)
            self.assertTrue(next(m for m in again['messages'] if m['id']=='demo-0')['archived'])


class StateTests(unittest.TestCase):
    def test_read_unread_filter_and_idempotent_action(self):
        s=initial();original=copy.deepcopy(s)
        s=reduce(s,'open',{'id':'demo-0'},'click-1')
        self.assertEqual(original,initial())
        self.assertFalse(s['mailbox']['messages'][0]['unread'])
        self.assertEqual(reduce(s,'open',{'id':'demo-0'},'click-1'),s)
        s=reduce(s,'folder',{'folder':'unread'})
        self.assertEqual([m['id'] for m in visible(s)],['demo-1'])

    def test_subject_search_in_inbox_and_clear(self):
        s=initial()
        s=reduce(s,'search',{'value':'DESIGN'})
        self.assertEqual([m['id'] for m in visible(s)],['demo-1'])
        s=reduce(s,'search',{'value':'boats'})
        self.assertEqual(visible(s),[])
        s=reduce(s,'search',{'value':'Alex'})
        self.assertEqual(visible(s),[])
        s=reduce(s,'clear_search')
        self.assertEqual(len(visible(s)),5)
        s=reduce(s,'search',{'value':'DESIGN'})
        s=reduce(s,'folder',{'folder':'flagged'})
        self.assertEqual(visible(s),[])

    def test_archive_selection_is_local_and_reversible(self):
        s=reduce(initial(),'edit')
        s=reduce(s,'open',{'id':'demo-0'})
        s=reduce(s,'archive')
        self.assertEqual(len(visible(s)),4)
        s=reduce(s,'folder',{'folder':'archive'})
        self.assertEqual(visible(s)[0]['id'],'demo-0')
        s=reduce(s,'open',{'id':'demo-0'});s=reduce(s,'archive')
        self.assertFalse(s['mailbox']['messages'][0]['archived'])

    def test_draft_save_reply_and_no_send_action(self):
        s=reduce(initial(),'open',{'id':'demo-0'});s=reduce(s,'reply')
        self.assertEqual(s['draft']['to'],'person0@example.com')
        self.assertEqual(s['draft']['subject'],'Re: Weekend plans')
        s=reduce(s,'draft_field',{'field':'body','value':'Thanks!'});s=reduce(s,'save_draft')
        self.assertEqual(s['drafts'][0]['body'],'Thanks!')
        s=reduce(s,'save_draft')
        self.assertEqual(len(s['drafts']),1)
        with self.assertRaises(ValueError):reduce(s,'send')

    def test_dismiss_service_card_does_not_change_mail(self):
        s=initial();after=reduce(s,'dismiss')
        self.assertTrue(after['card_dismissed'])
        self.assertEqual(s['mailbox'],after['mailbox'])

if __name__=='__main__':unittest.main()
