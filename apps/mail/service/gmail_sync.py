"""Gmail IMAP metadata and folders; POP3 remains the incoming transport.

Uses Gmail's documented X-GM-MSGID / X-GM-LABELS extension. No delete,
expunge, or implicit Seen writes: message downloads always use BODY.PEEK.
"""
from __future__ import annotations
import base64
import imaplib
import re
import ssl
from email import policy
from email.parser import BytesParser
from mailbox import connect as pop_connect, disconnect, decode_message
from account import account_id

MAX_MESSAGE=40_000_000


def quote(value):
    if any(c in str(value) for c in '\r\n\x00'):raise ValueError('Invalid IMAP value')
    return '"'+str(value).replace('\\','\\\\').replace('"','\\"')+'"'


def encode_name(value):
    out=[];non_ascii=[]
    def flush():
        if non_ascii:
            out.append('&'+base64.b64encode(''.join(non_ascii).encode('utf-16-be')).decode().rstrip('=').replace('/',',')+'-');non_ascii.clear()
    for c in value:
        if 32<=ord(c)<=126:flush();out.append('&-' if c=='&' else c)
        else:non_ascii.append(c)
    flush();return ''.join(out)


def decode_name(value):
    def part(m):
        data=m.group(1)
        if not data:return '&'
        return base64.b64decode(data.replace(',','/')+'='*((-len(data))%4)).decode('utf-16-be')
    return re.sub(r'&([^-]*)-',part,value)


def tokens(value):
    """Parse IMAP atoms/quoted strings/lists, including escaped system labels."""
    source=value.decode('ascii',errors='replace') if isinstance(value,bytes) else value
    parts=re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+',source);index=0
    def sequence(nested=False):
        nonlocal index
        result=[]
        while index<len(parts):
            token=parts[index];index+=1
            if token==')':break
            if token=='(':result.append(sequence(True))
            elif token.startswith('"'):result.append(re.sub(r'\\(.)',r'\1',token[1:-1]))
            else:result.append(token)
        return result
    return sequence()


def checked(result):
    status,data=result
    if status!='OK':raise RuntimeError('Gmail did not accept the request')
    return data


def connect(account):
    client=imaplib.IMAP4_SSL('imap.gmail.com',993,ssl_context=ssl.create_default_context(),timeout=25)
    try:
        checked(client.login(account['username'].removeprefix('recent:'),account['password']))
        if b'X-GM-EXT-1' not in client.capabilities and 'X-GM-EXT-1' not in client.capabilities:
            caps=checked(client.capability())
            if b'X-GM-EXT-1' not in b' '.join(caps):raise RuntimeError('Gmail extensions are unavailable')
        return client
    except Exception:client.shutdown();raise


def close(client):
    try:client.logout()
    except Exception:
        try:client.shutdown()
        except Exception:pass


def folders(client):
    result=[]
    for row in checked(client.list()):
        if not isinstance(row,bytes):continue
        parts=tokens(row)
        if len(parts)<3 or not isinstance(parts[0],list):continue
        flags=parts[0];wire=parts[2]
        if '\\Noselect' in flags:continue
        name=decode_name(wire)
        special=next((flag for flag in flags if flag in ('\\All','\\Sent','\\Drafts','\\Trash','\\Junk','\\Flagged','\\Important')),None)
        label={'\\All':None,'\\Flagged':'\\Starred','\\Junk':'\\Spam'}.get(special,special) if special else ('\\Inbox' if wire.upper()=='INBOX' else name)
        result.append({'name':name,'wire':wire,'label':label,'special':special,
                       'movable':special not in ('\\All','\\Sent','\\Drafts','\\Trash','\\Junk','\\Flagged','\\Important')})
    return result


def select_all(client,listing,readonly=True):
    folder=next((f for f in listing if f['special']=='\\All'),None)
    if not folder:raise RuntimeError('Enable All Mail in Gmail IMAP settings')
    checked(client.select(quote(folder['wire']),readonly=readonly))


def headers(account,messages):
    """Backfill RFC Message-ID for the pre-IMAP POP cache, without guessing UIDs."""
    missing={m.get('uid'):m for m in messages if m.get('uid') and not m.get('message_id') and m.get('source')=='gmail'}
    if not missing:return messages
    client=pop_connect(account)
    try:
        for row in client.uidl()[1]:
            number,uid=row.decode('ascii').split(maxsplit=1)
            if uid not in missing:continue
            try:raw=b'\r\n'.join(client.top(int(number),0)[1])
            except Exception:continue
            parsed=BytesParser(policy=policy.default).parsebytes(raw)
            missing[uid]['message_id']=str(parsed.get('Message-ID','')).strip()
            missing[uid]['references']=str(parsed.get('References','')).replace('\r','').replace('\n',' ')
        return messages
    finally:disconnect(client)


def metadata(meta):
    parsed=tokens(meta);attrs=next((x for x in parsed if isinstance(x,list)),[])
    fields={}
    for i,item in enumerate(attrs[:-1]):
        if isinstance(item,str) and item in ('UID','FLAGS','X-GM-MSGID','X-GM-LABELS','RFC822.SIZE'):fields[item]=attrs[i+1]
    labels=[decode_name(x) for x in fields.get('X-GM-LABELS',[])]
    flags=fields.get('FLAGS',[])
    return {'imap_uid':fields.get('UID'),'gmail_id':fields.get('X-GM-MSGID'),'labels':labels,
            'unread':'\\Seen' not in flags,'flagged':'\\Flagged' in flags,'archived':'\\Inbox' not in labels,
            'server_state':True,'size':int(fields.get('RFC822.SIZE',0))}


def search_one(client,message):
    if message.get('gmail_id'):
        result=checked(client.uid('SEARCH',None,'X-GM-MSGID',str(int(message['gmail_id']))))
    elif message.get('message_id'):
        result=checked(client.uid('SEARCH',None,'HEADER','Message-ID',quote(message['message_id'])))
    else:raise RuntimeError('Message identity is not available; refresh Mail first')
    ids=result[0].split() if result and result[0] else []
    if len(ids)!=1:raise RuntimeError('Message could not be uniquely matched in Gmail')
    return ids[0].decode('ascii')


def pull(account,messages):
    client=connect(account)
    try:
        listing=folders(client);select_all(client,listing)
        by_rfc={}
        for m in messages:
            if m.get('message_id'):by_rfc.setdefault(m['message_id'],[]).append(m)
        ids=list(by_rfc)
        for start in range(0,len(ids),20):
            batch=ids[start:start+20]
            criteria=' '.join(['OR']*(len(batch)-1)+['HEADER Message-ID '+quote(mid) for mid in batch])
            found=checked(client.uid('SEARCH',None,criteria))
            if not found or not found[0]:continue
            rows=checked(client.uid('FETCH',b','.join(found[0].split()),'(UID FLAGS X-GM-MSGID X-GM-LABELS BODY.PEEK[HEADER.FIELDS (MESSAGE-ID)])'))
            grouped={}
            for row in rows:
                if not isinstance(row,tuple):continue
                mid=str(BytesParser(policy=policy.default).parsebytes(row[1]).get('Message-ID','')).strip()
                grouped.setdefault(mid,[]).append(metadata(row[0]))
            for mid,states in grouped.items():
                if len(states)==1 and len(by_rfc.get(mid,[]))==1:by_rfc[mid][0].update(states[0])
        return messages,listing
    finally:close(client)


def locate(client,listing,message,readonly=True):
    select_all(client,listing,readonly)
    try:return search_one(client,message)
    except RuntimeError:
        wire=message.get('imap_folder')
        if not wire:raise
        checked(client.select(quote(wire),readonly=readonly))
        return search_one(client,message)


def apply(account,messages,pending):
    client=connect(account);done=[]
    try:
        listing=folders(client)
        for ident,operation in pending.items():
            message=next(m for m in messages if m['id']==ident)
            uid=locate(client,listing,message,readonly=False)
            for field,value in operation['values'].items():
                if field in ('unread','flagged'):
                    flag='\\Seen' if field=='unread' else '\\Flagged'
                    add=not value if field=='unread' else value
                    checked(client.uid('STORE',uid,'+FLAGS.SILENT' if add else '-FLAGS.SILENT','('+flag+')'))
                elif field=='archived':
                    checked(client.uid('STORE',uid,'-X-GM-LABELS' if value else '+X-GM-LABELS','('+quote('\\Inbox')+')'))
                elif field.startswith('label:'):
                    label=field[6:]
                    if label.startswith('\\'):raise ValueError('System folder cannot be changed this way')
                    checked(client.uid('STORE',uid,'+X-GM-LABELS' if value else '-X-GM-LABELS','('+quote(encode_name(label))+')'))
            done.append((ident,operation['version']))
        return {'done':done,'error':''}
    except Exception:return {'done':done,'error':'Gmail changes are pending. Tap Retry sync when connected.'}
    finally:close(client)


def fetch_folder(account,folder,before=None,limit=25):
    client=connect(account)
    try:
        checked(client.select(quote(folder['wire']),readonly=True))
        criteria='ALL' if before is None else 'UID 1:'+str(max(0,int(before)-1))
        if before is not None and int(before)<=1:ids=[]
        else:
            data=checked(client.uid('SEARCH',None,criteria));ids=[int(x) for x in data[0].split()] if data and data[0] else []
        chosen=sorted(ids,reverse=True)[:limit];messages=[];skipped=0
        for uid in chosen:
            sizes=checked(client.uid('FETCH',str(uid),'(UID RFC822.SIZE)'))
            size=metadata(next(x for x in sizes if isinstance(x,bytes)))['size']
            if size>MAX_MESSAGE:skipped+=1;continue
            rows=checked(client.uid('FETCH',str(uid),'(UID FLAGS X-GM-MSGID X-GM-LABELS BODY.PEEK[])'))
            pair=next(x for x in rows if isinstance(x,tuple));state=metadata(pair[0])
            if len(pair[1])>MAX_MESSAGE:skipped+=1;continue
            m=decode_message(pair[1],'imap:'+str(state['gmail_id'] or folder['wire']+':'+str(uid)))
            m.update(state,imap_folder=folder['wire']);messages.append(m)
        return {'account_id':account_id(account),'messages':messages,'cursor':min(chosen) if chosen else before,
                'more':len(ids)>len(chosen),'skipped':skipped}
    finally:close(client)


def hydrate(account,message):
    client=connect(account)
    try:
        listing=folders(client)
        uid=locate(client,listing,message)
        sizes=checked(client.uid('FETCH',uid,'(UID RFC822.SIZE)'))
        if metadata(next(x for x in sizes if isinstance(x,bytes)))['size']>MAX_MESSAGE:raise ValueError('Message exceeds the 40 MB download limit.')
        rows=checked(client.uid('FETCH',uid,'(UID FLAGS X-GM-MSGID X-GM-LABELS BODY.PEEK[])'))
        pair=next(x for x in rows if isinstance(x,tuple))
        if len(pair[1])>MAX_MESSAGE:raise ValueError('Message exceeds the 40 MB download limit.')
        m=decode_message(pair[1],message.get('uid') or 'imap:'+uid);m.update(metadata(pair[0]));m['id']=message['id']
        return m
    finally:close(client)


def confirm_sent(account,message_id):
    client=connect(account)
    try:
        listing=folders(client);sent=next(f for f in listing if f['special']=='\\Sent')
        checked(client.select(quote(sent['wire']),readonly=True))
        data=checked(client.uid('SEARCH',None,'HEADER','Message-ID',quote(message_id)))
        return bool(data and data[0])
    finally:close(client)
