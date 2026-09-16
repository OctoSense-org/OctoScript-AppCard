"""Local mail actions shared by the mobile app and the new-mail App Card."""
from copy import deepcopy
import uuid
from mailbox import fixture
from account import defaults


def initial(mailbox=None):
    return {'mailbox': mailbox or fixture(), 'screen': 'inbox', 'folder': 'inbox',
            'query': '', 'search_focused': False, 'list_scroll': 0, 'list_start': 0,
            'loading_more': False, 'load_error': '', 'selected': None, 'editing': False, 'selection': [],
            'draft': {'to': '', 'subject': '', 'body': ''}, 'drafts': [], 'notice': '',
            'account_form':defaults('you@gmail.com'),'password_saved':False,'password_pending':False,
            'account_busy':False,'account_status':'Changes apply when you tap Save.','account_error':'','settings_focus':None,
            'pending_sync':{},'remote_busy':False,'remote_error':'','folders':[],'folder_pages':{},'move_mode':False,
            'send_busy':False,'send_error':'','send_uncertain':False,'attachment_busy':False,'attachment_status':'',
            'syncing': False, 'error': '', 'revision': 0, 'card_dismissed': False, 'events': []}


def visible(state):
    messages = state['mailbox']['messages']
    folder = state['folder']
    if folder.startswith('remote:'):
        selected=next((f for f in state.get('folders',[]) if f['wire']==folder[7:]),None)
        if selected:
            label=selected['label']
            page=state.get('folder_pages',{}).get(folder)
            if page is not None and 'ids' in page:messages=[m for m in messages if m['id'] in page['ids']]
            messages=[m for m in messages if (label in m.get('labels',[]) if label else not any(x in m.get('labels',[]) for x in ('\\Trash','\\Spam')))]
        else:messages=[]
    elif folder=='sent':messages=[m for m in messages if '\\Sent' in m.get('labels',[])]
    else:messages = [m for m in messages if bool(m.get('archived')) == (folder == 'archive')]
    if folder == 'unread':
        messages = [m for m in messages if m['unread']]
    if folder == 'flagged':
        messages = [m for m in messages if m['flagged']]
    query = state['query'].strip().casefold() if state['screen'] in ('inbox','search') else ''
    if query:
        messages = [m for m in messages if query in m.get('subject','').casefold()]
    return messages


def has_more(state):
    if state['folder'].startswith('remote:'):return state.get('folder_pages',{}).get(state['folder'],{}).get('more',True)
    if state['folder']!='inbox':return False
    box=state['mailbox']
    return box.get('has_more',box.get('available',0)>len(box['messages'])+len(box.get('skipped_uids',[])))


def reduce(state, event, payload=None, event_id=None):
    if event_id and event_id in state['events']:
        return state
    s = deepcopy(state)
    payload = payload or {}
    s['revision'] += 1
    if event_id:
        s['events'] = (s['events'] + [event_id])[-200:]
    s['notice'] = ''
    if event == 'navigate':
        s.update(screen=payload['screen'], editing=False, selection=[], search_focused=payload['screen']=='search')
        if payload['screen']=='mailboxes':s.update(query='',list_scroll=0,list_start=0)
        if 'folder' in payload:
            s['folder'] = payload['folder']
    elif event == 'open':
        selected = next((m for m in s['mailbox']['messages'] if m['id'] == payload['id']), None)
        if selected is None:
            raise ValueError('Message is no longer available')
        if s['editing']:
            if selected['id'] in s['selection']:
                s['selection'].remove(selected['id'])
            else:
                s['selection'].append(selected['id'])
        else:
            selected['unread'] = False
            s.update(selected=selected['id'], screen='read',search_focused=False)
    elif event == 'folder':
        s.update(screen='inbox', folder=payload['folder'], list_scroll=0, list_start=0, editing=False, selection=[],search_focused=False)
    elif event == 'search':
        s.update(query=payload['value'], list_scroll=0,list_start=0,search_focused=True)
    elif event == 'clear_search':
        s.update(query='',list_scroll=0,list_start=0,search_focused=False)
    elif event == 'load_images':
        message=next(m for m in s['mailbox']['messages'] if m['id']==s['selected'])
        message['load_remote_images']=True
    elif event == 'edit':
        s.update(editing=not s['editing'], selection=[])
    elif event in ('archive', 'flag', 'unread'):
        ids = s['selection'] if s['editing'] else [s['selected']]
        for m in s['mailbox']['messages']:
            if m['id'] in ids:
                key = {'archive': 'archived', 'flag': 'flagged', 'unread': 'unread'}[event]
                m[key] = not m.get(key, False)
        if event != 'flag':
            s.update(screen='inbox', editing=False, selection=[])
        s['notice'] = {'archive': 'Updated on this device', 'flag': 'Flag updated', 'unread': 'Marked unread'}[event]
    elif event in ('compose', 'reply'):
        s['draft'] = {'id':uuid.uuid4().hex,'to': '', 'subject': '', 'body': ''}
        s.update(send_error='',send_uncertain=False)
        if event == 'reply':
            m = next(m for m in s['mailbox']['messages'] if m['id'] == s['selected'])
            s['draft'].update(to=m.get('reply_to') or m['address'], in_reply_to=m.get('message_id',''), references=' '.join(filter(None,[m.get('references',''),m.get('message_id','')])), subject=m['subject'] if m['subject'].lower().startswith('re:') else 'Re: ' + m['subject'])
        s['screen'] = 'compose'
    elif event == 'draft_field':
        if payload['field'] not in ('to', 'subject', 'body'):
            raise ValueError('Unknown draft field')
        s['draft'][payload['field']] = payload['value'][:24000]
    elif event == 'account_field':
        key=payload['field']
        if key not in ('address','username','host','port','smtp_host','smtp_port'):raise ValueError('Unknown account field')
        s['account_form'][key]=payload['value'][:254]
        s.update(account_error='',account_status='Unsaved changes',settings_focus='server_'+key)
    elif event == 'account_security':
        security=payload['security']
        if security not in ('tls','starttls'):raise ValueError('Unknown security mode')
        old=s['account_form']['security'];port=s['account_form']['port']
        if (old,port) in (('tls','995'),('starttls','110')):s['account_form']['port']='995' if security=='tls' else '110'
        s['account_form']['security']=security
        s.update(account_error='',account_status='Unsaved changes',settings_focus=None)
    elif event == 'smtp_security':
        mode=payload['security']
        if mode not in ('tls','starttls'):raise ValueError('Unknown security mode')
        if (s['account_form']['smtp_security'],s['account_form']['smtp_port']) in (('tls','465'),('starttls','587')):s['account_form']['smtp_port']='465' if mode=='tls' else '587'
        s['account_form']['smtp_security']=mode
        s.update(account_error='',account_status='Unsaved changes',settings_focus=None)
    elif event == 'account_sync':
        s['account_form']['sync_enabled']=not s['account_form']['sync_enabled']
        s.update(account_error='',account_status='Unsaved changes',settings_focus=None)
    elif event == 'account_recent':
        s['account_form']['recent']=not s['account_form']['recent']
        s.update(account_error='',account_status='Unsaved changes',settings_focus=None)
    elif event == 'save_draft':
        if not any(s['draft'].get(k) for k in ('to','subject','body')):
            return state
        s['draft'].setdefault('id',uuid.uuid4().hex)
        s['drafts']=[d for d in s['drafts'] if d.get('id')!=s['draft']['id']]+[deepcopy(s['draft'])]
        s.update(screen='inbox', notice='Draft saved on this Mac')
    elif event == 'open_draft':
        s.update(draft=deepcopy(s['drafts'][payload['index']]), screen='compose',send_error='',send_uncertain=False)
        s['draft'].setdefault('id',uuid.uuid4().hex)
    elif event == 'dismiss':
        s['card_dismissed'] = True
    else:
        raise ValueError('Unknown mail action: ' + event)
    return s
