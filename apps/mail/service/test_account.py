import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from account import defaults, load_account, public_account, candidate, save_account, validate, account_id
from mailbox import test_connection, fetch_gmail, merge_mailbox


class AccountTests(unittest.TestCase):
    def test_saved_configuration_survives_reload_and_preserves_legacy_keys(self):
        with tempfile.TemporaryDirectory() as d,patch.dict(os.environ,{'OCTOS_MAIL_CREDENTIALS':str(Path(d)/'credentials.json')},clear=True):
            path=Path(d)/'credentials.json'
            path.write_text(json.dumps({'GMAIL_ADDRESS':'you@gmail.com','GMAIL_APP_PASSWORD':'abcd efgh ijkl mnop','OTHER_KEY':'unrelated'}))
            config=load_account()
            self.assertEqual(config['password'],'abcdefghijklmnop')
            form={**public_account(config),'port':'1995','recent':False}
            updated=candidate(form);save_account(updated)
            self.assertEqual(load_account(),updated)
            self.assertEqual(json.loads(path.read_text())['OTHER_KEY'],'unrelated')
            self.assertEqual(path.stat().st_mode&0o777,0o600)
            self.assertNotIn('password',public_account(updated))
            self.assertNotIn('abcdefghijklmnop',json.dumps(public_account(updated)))

    def test_validation_and_credentials_bound_to_server_and_login(self):
        config={**defaults('you@gmail.com'),'password':'saved-secret'}
        with patch('account.load_account',return_value=config):
            self.assertEqual(candidate(defaults('you@gmail.com'))['password'],'saved-secret')
            for key,value in [('host','pop.other.example'),('username','another')]:
                with self.assertRaisesRegex(ValueError,'Set a password'):candidate({**defaults('you@gmail.com'),key:value})
            custom=candidate({**defaults('you@gmail.com'),'host':'POP.EXAMPLE.COM','security':'starttls','port':'110'},'new secret')
            self.assertFalse(custom['recent']);self.assertEqual(custom['password'],'new secret')
        for key,value in [('port','0'),('port','65536'),('port','abc'),('address','not-email'),('username','a\r\nb'),('host','https://mail.example.com'),('host','mail.example.com/path'),('security','none')]:
            with self.assertRaises(ValueError,msg=key):validate({**defaults('you@gmail.com'),key:value})

    def test_starttls_precedes_auth_and_connection_test_does_not_retrieve(self):
        calls=[]
        class Fake:
            def __init__(self,host,port,timeout):calls.append(('connect',host,port))
            def stls(self,context):
                self.secure=True;assert context.check_hostname;calls.append(('tls',))
            def user(self,value):assert self.secure;calls.append(('user',value))
            def pass_(self,value):assert self.secure;calls.append(('auth',))
            def stat(self):return 42,400
            def quit(self):calls.append(('quit',))
        config={**defaults('me@example.com'),'host':'pop.example.com','port':'110','security':'starttls','recent':False,'password':'local'}
        with patch('mailbox.poplib.POP3',Fake):self.assertEqual(test_connection(config),42)
        self.assertEqual(calls,[('connect','pop.example.com',110),('tls',),('user','me@example.com'),('auth',),('quit',)])

    def test_failed_tls_does_not_send_credentials(self):
        calls=[]
        class Fake:
            def __init__(self,*a,**kw):pass
            def stls(self,context):raise OSError('certificate failure')
            def user(self,value):calls.append('credentials')
            def close(self):calls.append('closed')
        config={**defaults('you@gmail.com'),'security':'starttls','password':'local'}
        with patch('mailbox.poplib.POP3',Fake),self.assertRaises(OSError):test_connection(config)
        self.assertEqual(calls,['closed'])

    def test_mailbox_identity_prevents_cross_account_uid_collisions(self):
        old={'account_id':account_id(defaults('first@gmail.com')),'messages':[{'id':'same-uid','subject':'Old account','date':'2026'}]}
        result={'account_id':account_id(defaults('second@gmail.com')),'messages':[{'id':'same-uid','subject':'New account','date':'2026'}],'available':1}
        self.assertEqual(merge_mailbox(old,result)['messages'][0]['subject'],'New account')


if __name__=='__main__':unittest.main()
