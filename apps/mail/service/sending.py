"""TLS SMTP submission with a durable result and no automatic ambiguous retries."""
from datetime import datetime, timezone
from email import policy
from email.message import EmailMessage
from email.utils import getaddresses, make_msgid, format_datetime
from pathlib import Path
import hashlib
import json
import re
import smtplib
import ssl
import uuid
from account import account_id
from mailbox import atomic_json, PRIVATE


class SendFailure(Exception):
    def __init__(self,message,uncertain=False):
        super().__init__(message);self.uncertain=uncertain


def recipients(value):
    if any(c in value for c in '\r\n\x00'):raise ValueError('Enter valid recipient email addresses.')
    parsed=getaddresses([value]);addresses=[]
    for _,address in parsed:
        if not re.fullmatch(r'[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+',address):raise ValueError('Enter valid recipient email addresses.')
        if address not in addresses:addresses.append(address)
    if not addresses:raise ValueError('Add at least one recipient.')
    if len(addresses)>50:raise ValueError('Use at most 50 recipients per message.')
    return addresses


def prepare(account,draft,message_id=None):
    to=recipients(draft.get('to',''))
    subject=draft.get('subject','')
    if any(c in subject for c in '\r\n\x00'):raise ValueError('Subject must be one line.')
    if not account.get('smtp_host'):raise ValueError('Set an outgoing server in Mail Server settings.')
    msg=EmailMessage(policy=policy.SMTP)
    msg['From']=account['address'];msg['To']=draft['to'];msg['Subject']=subject
    msg['Date']=format_datetime(datetime.now(timezone.utc));msg['Message-ID']=message_id or make_msgid(domain=account['address'].split('@')[-1])
    for header,key in [('In-Reply-To','in_reply_to'),('References','references')]:
        value=draft.get(key,'')
        if value:
            if any(c in value for c in '\r\n\x00'):raise ValueError('Invalid reply header.')
            msg[header]=value
    msg.set_content(draft.get('body',''))
    return msg,to


def smtp_connect(account):
    context=ssl.create_default_context();client=None
    try:
        if account.get('smtp_security','tls')=='tls':client=smtplib.SMTP_SSL(account['smtp_host'],int(account['smtp_port']),timeout=25,context=context)
        else:
            client=smtplib.SMTP(account['smtp_host'],int(account['smtp_port']),timeout=25)
            client.ehlo();client.starttls(context=context)
        client.ehlo();client.login(account['username'].removeprefix('recent:'),account['password'])
        return client
    except Exception:
        if client:
            try:client.close()
            except Exception:pass
        raise


def smtp_test(account):
    client=smtp_connect(account)
    try:return client.noop()[0]==250
    finally:
        try:client.quit()
        except Exception:client.close()


def transmit(account,msg,to):
    client=None;data_started=False
    try:
        client=smtp_connect(account)
        code,_=client.mail(account['address'])
        if code!=250:raise SendFailure('The outgoing server rejected the sender. Message was not sent.')
        for address in to:
            code,_=client.rcpt(address)
            if code not in (250,251):
                client.rset()
                raise SendFailure('A recipient was rejected. Nothing was sent; check the addresses.')
        data_started=True
        code,_=client.data(msg.as_bytes())
        if code!=250:raise SendFailure('The outgoing server rejected the message. It was not sent.')
    except SendFailure:raise
    except smtplib.SMTPDataError:
        raise SendFailure('The outgoing server rejected the message. It was not sent.') from None
    except smtplib.SMTPAuthenticationError:
        raise SendFailure('Outgoing login failed. Check your mail password.') from None
    except Exception:
        raise SendFailure('Delivery is unconfirmed. Check Sent before sending again.' if data_started else 'Could not connect to the outgoing server. Message was not sent.',data_started) from None
    finally:
        if client:
            try:client.quit()
            except Exception:
                try:client.close()
                except Exception:pass


def record_path(account,draft_id):
    ident=hashlib.sha256(draft_id.encode()).hexdigest()
    return PRIVATE/'accounts'/account_id(account)/'outbox'/(ident+'.json')


def submit(account,draft):
    path=record_path(account,draft['id'])
    previous=json.loads(path.read_text()) if path.exists() else {}
    if previous.get('status')=='sent':return previous
    if previous.get('status') in ('sending','uncertain'):
        raise SendFailure('Delivery is unconfirmed. Check Sent before sending again.',True)
    msg,to=prepare(account,draft,previous.get('message_id'))
    record={'draft_id':draft['id'],'message_id':str(msg['Message-ID']),'to':draft['to'],'subject':draft['subject'],
            'date':str(msg['Date']),'body':draft['body'],'status':'sending','account_id':account_id(account)}
    atomic_json(path,record)
    try:transmit(account,msg,to)
    except SendFailure as e:
        record.update(status='uncertain' if e.uncertain else 'failed',error=str(e));atomic_json(path,record)
        raise
    record.update(status='sent',sent_at=datetime.now(timezone.utc).isoformat())
    atomic_json(path,record)
    return record


def find_record(account,draft_id):
    path=record_path(account,draft_id)
    return json.loads(path.read_text()) if path.exists() else None
