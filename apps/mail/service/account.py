"""Editable POP3 account configuration; secrets never enter rendered app state."""
from pathlib import Path
import hashlib
import json
import os
import re


def credential_path():
    return Path(os.environ.get('OCTOS_MAIL_CREDENTIALS',Path.home()/'.config/octos-mail/credentials.json'))


def defaults(address=''):
    return dict(address=address,username=address,host='pop.gmail.com',port='995',security='tls',recent=True,
                smtp_host='smtp.gmail.com',smtp_port='465',smtp_security='tls',sync_enabled=True)


def load_account():
    path=credential_path()
    data=json.loads(path.read_text()) if path.exists() else {}
    if 'MAIL_ACCOUNT' in data:
        saved=data['MAIL_ACCOUNT']
        base=defaults()
        if saved.get('host')!='pop.gmail.com':base.update(smtp_host='',sync_enabled=False)
        return {**base,**saved}
    address=os.environ.get('GMAIL_ADDRESS',data.get('GMAIL_ADDRESS',''))
    return {**defaults(address),'password':os.environ.get('GMAIL_APP_PASSWORD',data.get('GMAIL_APP_PASSWORD','')).replace(' ','')}


def public_account(account=None):
    account=load_account() if account is None else account
    return {key:str(account.get(key,'')) if key not in ('recent','sync_enabled') else bool(account.get(key)) for key in defaults()}


def identity(account):
    return (account.get('host','').strip().lower(),account.get('username','').strip())


def account_id(account):
    return hashlib.sha256(json.dumps(identity(account)).encode()).hexdigest()[:24]


def validate(form):
    clean={key:form.get(key,value) for key,value in defaults().items()}
    for key in ('address','username','host','port','security'):clean[key]=str(clean[key]).strip()
    if not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',clean['address']):raise ValueError('Enter a valid email address.')
    if not clean['username'] or any(c in clean['username'] for c in '\r\n\x00'):raise ValueError('Enter a valid login name.')
    host=clean['host'].lower().rstrip('.')
    if not host or len(host)>253 or not all(re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?',label) for label in host.split('.')):
        raise ValueError('Enter a server hostname, such as pop.gmail.com.')
    clean['host']=host
    if not clean['port'].isascii() or not clean['port'].isdigit() or not 1<=int(clean['port'])<=65535:raise ValueError('Port must be a number from 1 to 65535.')
    clean['port']=str(int(clean['port']))
    if clean['security'] not in ('tls','starttls'):raise ValueError('Choose SSL/TLS or STARTTLS.')
    clean['recent']=bool(clean['recent']) and host=='pop.gmail.com'
    clean['sync_enabled']=bool(clean['sync_enabled']) and host=='pop.gmail.com'
    smtp=str(clean['smtp_host']).strip().lower().rstrip('.')
    if host!='pop.gmail.com' and smtp=='smtp.gmail.com':smtp=''
    if smtp and (len(smtp)>253 or not all(re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?',label) for label in smtp.split('.'))):raise ValueError('Enter a valid outgoing server hostname.')
    clean['smtp_host']=smtp
    port=str(clean['smtp_port']).strip()
    if not port.isascii() or not port.isdigit() or not 1<=int(port)<=65535:raise ValueError('Outgoing port must be from 1 to 65535.')
    clean['smtp_port']=str(int(port))
    if clean['smtp_security'] not in ('tls','starttls'):raise ValueError('Choose outgoing SSL/TLS or STARTTLS.')
    return clean


def candidate(form,password=None):
    clean=validate(form)
    if password is None:
        old=load_account()
        password=old.get('password','') if identity(clean)==identity(old) else ''
    if clean['host']=='pop.gmail.com':password=password.replace(' ','')
    if not password or any(c in password for c in '\r\n\x00'):raise ValueError('Set a password for this account.')
    return {**clean,'password':password}


def save_account(account):
    from mailbox import atomic_json
    path=credential_path();path.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
    data=json.loads(path.read_text()) if path.exists() else {}
    data['MAIL_ACCOUNT']=dict(account)
    atomic_json(path,data)
