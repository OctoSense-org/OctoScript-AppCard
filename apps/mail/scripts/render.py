"""Reusable native mail components lowered by the AppCard L0 compiler."""
from __future__ import annotations
from copy import deepcopy
from pathlib import Path
import hashlib
import json
import shutil
import re
from functools import lru_cache
from bisect import bisect_right
from itertools import accumulate
from fontTools.ttLib import TTFont
from common import ROOT, PIPELINE, NATIVE_ROOT
from mailbox import atomic_json
from model import visible, has_more
from html_mail import document_url
from catalogue import walk
from compile import compile_page
from semantics import propose

INK = '1C1C1E'
GRAY = '8E8E93'
BLUE = '007AFF'
LIGHT = 'F2F2F7'
WHITE = 'FFFFFF'

ICONS = {
    'attachment':'<path d="m9 16 8-8a3 3 0 0 0-4-4L4 13a5 5 0 0 0 7 7L22 9M7 14l8-8"/>',
    'folder':'<path d="M2 6h8l3 3h11v13H2zM2 6V3h8l3 3h9v3"/>',
    'back': '<path d="m16 4-8 8 8 8"/>',
    'next': '<path d="m8 4 8 8-8 8"/>',
    'mail': '<rect x="2" y="4" width="20" height="16" rx="3"/><path d="m3 6 9 7 9-7"/>',
    'inbox': '<path d="M5 4h14l3 10v6H2v-6zm-3 10h6l2 3h4l2-3h6"/>',
    'archive': '<rect x="4" y="7" width="16" height="15" rx="2"/><path d="M2 3h20v4H2zm7 9h6"/>',
    'flag': '<path d="M5 22V3c5-5 9 5 15 0v10c-6 5-10-5-15 0"/>',
    'draft': '<path d="M6 2h8l5 5v15H6zm8 0v6h5"/>',
    'compose': '<path d="M12 4H4v17h17v-9M10 15l2-5L21 1l3 3-9 9z"/>',
    'search': '<circle cx="10" cy="10" r="7"/><path d="m15 15 7 7"/>',
    'filter': '<circle cx="12" cy="12" r="10"/><path d="M6 8h12M8 12h8m-6 4h4"/>',
    'reply': '<path d="m10 4-8 8 8 8v-6c6-1 9 1 12 6 0-10-5-12-12-12z"/>',
    'refresh': '<path d="M20 8a9 9 0 1 0 0 9M20 2v7h-7"/>',
    'check': '<path d="m4 12 5 5L21 5"/>',
    'settings': '<circle cx="12" cy="12" r="4"/><path d="m10 2 4 0 1 3 3 1 3-1 2 4-2 2v3l2 2-2 4-3-1-3 1-1 3h-4l-1-3-3-1-3 1-2-4 2-2v-3L1 9l2-4 3 1 3-1z"/>',
}


def col(value):
    return int('ff' + value, 16)


def short(value, length):
    value = ' '.join(str(value).split())
    return value if len(value) <= length else value[:length-1] + '…'


@lru_cache(maxsize=4)
def mail_advances(size, weight):
    # Native Makepad uses unhinted font advances. Pillow's basic layout rounds
    # small glyphs to whole pixels and can underestimate a long line's width.
    with TTFont(NATIVE_ROOT/'octoscript-makepad/apps/kit-host/resources/ux'/f'Inter-{weight}.ttf') as font:
        scale=size/font['head'].unitsPerEm
        return {chr(c):font['hmtx'][glyph][0]*scale for c,glyph in font.getBestCmap().items()}


def mail_lines(text, width=360, size=15, weight=400):
    """Wrap all message text by font advance, including long unbroken URLs."""
    advances=mail_advances(size,weight)
    lines=[]
    for paragraph in text.expandtabs(4).splitlines() or ['']:
        positions=[0,*accumulate(advances.get(c,size*1.5) for c in paragraph)]
        start=0
        while positions[-1]-positions[start]>width:
            end=max(start+1,bisect_right(positions,positions[start]+width,lo=start+1)-1)
            split=paragraph.rfind(' ',start,end+1)
            cut=split if split>start else end
            lines.append(paragraph[start:cut])
            start=cut+1 if split>start else cut
        lines.append(paragraph[start:])
    return lines


class Scene:
    def __init__(self, background=WHITE):
        self.nodes, self.controls, self.assets = [], {}, {}
        self.background = background

    def stack(self, ident, x, y, w, h, bg=None, radius=0, children=None, **extra):
        return {'t': 'stack', 'id': ident, 'x': x, 'y': y, 'w': w, 'h': h,
                'c': children or [], **({'bg': col(bg), 'variant': 'surface', 'radius': radius} if bg else {}), **extra}

    def text(self, ident, text, x, y, w, h=24, size=17, weight=400, color=INK, align=0):
        line_height=round(size*1.32,2)
        if h>line_height:
            y+=(h-line_height)/2
            h=line_height
        return {'t': 'text', 'id': ident, 'text': str(text), 'x': x, 'y': y, 'w': w, 'h': h,
                'size': size, 'line_height': line_height, 'weight': weight,
                'color': col(color), 'font_src': f'self:resources/ux/Inter-{weight}.ttf',
                'variant': 'single_line', 'alignx': align}

    def icon(self, ident, name, x, y, size=24, color=BLUE):
        content = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 26 26" fill="none" stroke="#{color}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'
        self.assets[ident] = content
        return {'t': 'svg', 'id': ident, 'x': x, 'y': y, 'w': size*.45 if name in ('back','next') else size, 'h': size}

    def line(self, ident, y, x=20, w=366):
        return self.stack(ident, x, y, w, .65, 'E2E2E7')

    def button(self, ident, label, x, y, w, h, event, payload=None, bg=None, icon=None, enabled=True, color=BLUE, size=17, label_align=None):
        children = [{'t':'button', 'id':ident+'_control', 'x':x,'y':y,'w':w,'h':h,'enabled':enabled}]
        if bg:
            children.append(self.stack(ident+'_surface',x,y,w,h,bg,12))
        if icon:
            children.append(self.icon(ident+'_icon',icon,x+(w-24)/2 if not label else x+10,y+(h-24)/2,color=BLUE if color==INK else color))
        if label:
            inset=27 if icon=='back' else 40 if icon else 3
            alignment=label_align if label_align is not None else 0 if icon else .5
            children.append(self.text(ident+'_label',label,x+inset,y,w-inset-4,h,size,400,color if enabled else GRAY,alignment))
        self.controls[ident] = {'event':event,'payload':payload or {},'enabled':enabled}
        return self.stack(ident,x,y,w,h,children=children,kit=json.dumps({'widget':'KitButton','bindings':{'control':[0]}}))

    def field(self, ident, value, placeholder, x,y,w,h,event,payload=None,multiline=False,focus=False,size=17):
        control = self.text(ident+'_input',value,x,y,w,h)
        control.update(t='input',x=x,y=y,w=w,h=h,size=size,placeholder=placeholder, variant='multiline' if multiline else 'single_line', focused=int(focus))
        self.controls[ident] = {'event':event, 'payload':payload or {},'enabled':True, 'input':True}
        return self.stack(ident,x,y,w,h,children=[control],kit=json.dumps({'widget':'KitFormField','bindings':{'input':[0]}}))

    def chrome(self, title=None, back=None, right=None):
        self.nodes += [self.text('clock','9:41',28,12,60,20,14,600),
            self.text('signal','•••',310,11,30,20,12,600),
            self.stack('battery',354,17,23,10,INK,2),self.stack('battery_tip',378,20,2,4,GRAY,1),
            self.stack('home_indicator',137,762,132,5,INK,3)]
        if back:
            self.nodes.append(self.button('back',back[0],12,40,140 if back[0]!='Cancel' else 84,42,'navigate',{'screen':back[1]},icon='back' if back[0]!='Cancel' else None))
        if title:
            self.nodes.append(self.text('heading',title,22,91,364,46,34,700))
        if right:
            self.nodes.append(self.button('top_action',right[0],324,40,68,42,right[1],right[2] if len(right)>2 else {}))

    def toolbar(self, state, read=False):
        self.nodes += [self.stack('toolbar_surface',0,704,406,49,WHITE),self.line('toolbar_separator',704,0,406)]
        if read:
            for i,(ident,icon,event) in enumerate([('archive','archive','archive'),('flag','flag','flag'),('attachments','attachment','attachments'),('move','folder','move'),('reply','reply','reply'),('compose','compose','compose')]):
                message=next(m for m in state['mailbox']['messages'] if m['id']==state['selected'])
                if ident=='archive' and message.get('archived'):icon='inbox'
                self.nodes.append(self.button('tool_'+ident,'',8+i*66,708,54,44,event,icon=icon,color='FF9500' if ident=='flag' and message.get('flagged') else BLUE))
        else:
            self.nodes.append(self.button('tool_filter','',14,709,48,44,'folder',{'folder':'inbox' if state['folder']=='unread' else 'unread'},icon='filter'))
            self.nodes.append(self.button('tool_compose','',344,709,48,44,'compose',icon='compose'))
            if state.get('remote_error') or state.get('pending_sync') and not state.get('remote_busy'):
                self.nodes.append(self.button('retry_sync','Retry sync',100,710,206,38,'remote_retry',size=13))
                return
            count = len(visible(state))
            provider='Gmail' if state['mailbox'].get('host','pop.gmail.com')=='pop.gmail.com' else 'Mail'
            status = 'Checking for mail…' if state['syncing'] else state['notice'] or (provider+' · synced' if state['mailbox'].get('synced_at') else 'Sample mailbox' if state['mailbox']['address']=='you@gmail.com' else 'Check for Mail to download')
            self.nodes += [self.text('sync_status',status,72,710,262,18,11,400,GRAY,.5), self.text('message_count',f'{count} messages',72,728,262,18,11,400,INK,.5)]

    def row(self, m, i, y, state):
        ident=f'message_{i}'
        children=[self.button(ident+'_open','',0,y,406,88,'open',{'id':m['id']})]
        if m['unread']:
            children.append(self.stack(ident+'_unread',17,y+18,9,9,BLUE,5))
        if state['editing']:
            children.append(self.text(ident+'_selected','✓' if m['id'] in state['selection'] else '○',12,y+30,25,24,18,600,BLUE))
        children += [self.text(ident+'_sender',short(m['sender'],24),38,y+9,224,24,17,600),
            self.text(ident+'_time',m['time'],269,y+11,108,20,12,400,GRAY,1),
            self.text(ident+'_subject',short(m['subject'],43),38,y+33,338,22,15,600),
            self.text(ident+'_preview',short(m['preview'],49),38,y+56,338,23,13,400,GRAY),
            self.line(ident+'_separator',y+87,38,368)]
        return self.stack(ident,0,y,406,88,children=children)


def build(state):
    page=state['screen']
    provider='Gmail' if state['mailbox'].get('host','pop.gmail.com')=='pop.gmail.com' else 'Mail Account'
    s=Scene(LIGHT if page in ('mailboxes','settings','services','folders','card') else WHITE)
    if page in ('inbox','search'):
        title={'inbox':'Inbox','unread':'Unread','flagged':'Flagged','archive':'Archive'}.get(state['folder'],'Sent' if state['folder']=='sent' else next((f['name'].split('/')[-1] for f in state.get('folders',[]) if state['folder']=='remote:'+f['wire']),'Inbox'))
        s.chrome('Search' if page=='search' else title, ('Cancel','inbox') if page=='search' else ('Mailboxes','mailboxes'), None if page=='search' else ('Done' if state['editing'] else 'Edit','edit'))
        s.nodes += [s.stack('search_surface',20,146,366,40,LIGHT,12),s.icon('search_icon','search',31,157,20,color=GRAY)]
        s.nodes.append(s.field('search_field',state['query'],'Search subjects',61,149,278,34,'search',focus=state.get('search_focused',False)))
        if state['query']:
            s.nodes.append(s.button('clear_search','×',340,149,38,34,'clear_search',color=GRAY,size=22))
        if page=='search':
            s.nodes.append(s.text('results_label',f'Results · {len(visible(state))} messages',22,198,360,24,13,400,GRAY))
        else:
            s.nodes.append(s.stack('segments',20,198,366,33,LIGHT,9))
            s.nodes.append(s.button('all_mail','All Mail',22,200,181,29,'folder',{'folder':'inbox'},bg=WHITE if state['folder']!='unread' else None,color=INK,size=14))
            s.nodes.append(s.button('unread_mail','Unread',204,200,180,29,'folder',{'folder':'unread'},bg=BLUE if state['folder']=='unread' else None,color=WHITE if state['folder']=='unread' else GRAY,size=14))
        rows=visible(state)
        start=min(state.get('list_start',0),max(0,len(rows)-1))
        items=[s.row(rows[i],i,242+88*i,state) for i in range(start,min(len(rows),start+60))]
        footer_y=242+len(rows)*88
        if state.get('loading_more'):
            items.append(s.text('list_footer','Loading older messages…',22,footer_y+8,362,36,13,400,GRAY,.5))
        elif has_more(state):
            items.append(s.button('load_more','Retry loading mail' if state.get('load_error') else 'Load older messages',70,footer_y+8,266,36,'load_more',size=13))
        elif rows:
            items.append(s.text('list_footer','All messages loaded',22,footer_y+8,362,36,12,400,GRAY,.5))
        content=s.stack('list_content',0,242,406,max(462,len(rows)*88+54),children=items)
        s.nodes.append(s.stack('list_scroll',0,242,406,462,children=[content],variant='scroll_y'))
        if not rows:
            s.nodes += [s.icon('empty_icon','mail',177,348,52,color=GRAY),s.text('empty_label','No matching subjects' if state['query'] else 'No messages',20,414,366,30,22,600,GRAY,.5)]
            if state['query']:s.nodes.append(s.text('search_scope','Search covers downloaded mail',20,450,366,24,13,400,GRAY,.5))
        s.toolbar(state)
        if state['editing']:
            s.nodes=s.nodes[:-5]
            s.nodes += [s.button('archive_selected','Archive selected',88,710,232,40,'archive',enabled=bool(state['selection']))]
    elif page=='mailboxes':
        s.chrome('Mailboxes')
        s.nodes.append(s.stack('folders_surface',20,158,366,318,WHITE,13))
        rows=[('Sent','mail','sent'),('Inbox','inbox','inbox'),('Unread','filter','unread'),('Flagged','flag','flagged'),('Drafts','draft','drafts'),('Archive','archive','archive')]
        for i,(label,icon,folder) in enumerate(rows):
            y=159+i*53
            event,payload=('navigate',{'screen':'drafts'}) if folder=='drafts' else ('folder',{'folder':folder})
            s.nodes.append(s.button('folder_'+str(i),label,26,y,350,52,event,payload,icon=icon,color=INK))
            count=len(state['drafts']) if folder=='drafts' else len(visible({**state,'screen':'inbox','folder':folder}))
            s.nodes += [s.text('folder_count_'+str(i),str(count) if count else '',305,y,30,52,16,400,GRAY,1),s.icon('folder_arrow_'+str(i),'next',350,y+17,17,color=GRAY)]
            if i<5:s.nodes.append(s.line('folder_line_'+str(i),y+52,68,318))
        s.nodes += [s.stack('account_surface',20,496,366,76,WHITE,13),s.button('account_open','',20,496,366,76,'navigate',{'screen':'settings'}),s.icon('gmail_icon','mail',34,518,30),
            s.text('account_name',provider,80,504,160,27,17,600),s.text('account_address',state['mailbox']['address'],80,532,245,22,12,400,GRAY),
            s.text('account_status','Connected' if state['mailbox'].get('synced_at') else 'Sample',284,510,88,25,12,400,'34A853',1),
            s.button('settings','Settings',20,590,366,56,'navigate',{'screen':'settings'},bg=WHITE,icon='settings',color=INK),
            s.button('new_mail_card','New Mail card',20,659,240,40,'navigate',{'screen':'card'},icon='mail'),s.button('gmail_folders','Gmail folders',20,709,280,44,'folders',icon='folder'),s.button('compose','',338,709,48,44,'compose',icon='compose')]
    elif page=='read':
        m=next(m for m in state['mailbox']['messages'] if m['id']==state['selected'])
        s.chrome(None,('Inbox','inbox'),('Unread','unread'))
        if state.get('remote_error'):s.nodes.append(s.button('reader_retry_sync','Retry sync',167,40,147,42,'remote_retry',size=14))
        if m.get('html'):
            if not state.get('remote_error') and not m.get('load_remote_images') and re.search(r'(?:src\s*=\s*[\"\x27]?|url\(\s*[\"\x27]?)https?://',m['html'],re.I):
                s.nodes.append(s.button('load_images','Load images',168,40,147,42,'load_images',size=14))
            s.nodes.append({'t':'web','id':'message_html','x':0,'y':88,'w':406,'h':616,
                            'src':document_url(m,state['mailbox']['address'])})
            s.toolbar(state,read=True)
            return s
        chrome_count=len(s.nodes)
        title_lines=mail_lines(m['subject'],364,27,700)
        for i,line in enumerate(title_lines):s.nodes.append(s.text('subject_'+str(i),line,22,92+i*34,364,36,27,700))
        y=max(178,92+len(title_lines)*34+18)
        initials=''.join(word[0] for word in m['sender'].split()[:2]).upper()
        s.nodes += [s.stack('avatar',22,y,44,44,BLUE,22),s.text('initials',initials,22,y,44,44,17,600,WHITE,.5),
            s.text('sender',short(m['sender'],26),80,y,228,25,17,600),s.text('recipient','To: '+short(state['mailbox']['address'],34),80,y+24,280,23,12,400,GRAY),
            s.text('date',m['time'],292,y,90,24,12,400,GRAY,1),s.line('message_rule',y+57)]
        lines=mail_lines(m['body'])
        body_y=y+76
        for i,line in enumerate(lines):s.nodes.append(s.text('body_'+str(i),line,23,body_y+i*24,360,24,15,400))
        reply_y=max(641,body_y+len(lines)*24+24)
        s.nodes.append(s.button('reply_primary','Reply',22,reply_y,122,42,'reply',bg=BLUE,icon='reply',color=WHITE))
        content=s.stack('reader_content',0,88,406,reply_y+60-88,children=s.nodes[chrome_count:])
        s.nodes=s.nodes[:chrome_count]+[s.stack('reader_scroll',0,88,406,616,children=[content],variant='scroll_y')]
        s.toolbar(state,read=True)
    elif page=='compose':
        s.chrome(None,('Cancel','inbox'))
        s.nodes.append(s.button('top_action','Sending…' if state.get('send_busy') else 'Send',314,40,82,42,'send',enabled=not state.get('send_busy') and not state.get('send_uncertain'),size=15))
        s.nodes += [s.text('compose_title','Reply' if state['draft'].get('in_reply_to') else 'New Message',102,46,198,30,17,600,INK,.5),
            s.text('to_label','To:',22,105,45,40,16,400,GRAY),s.field('to',state['draft']['to'],'Recipient',70,105,314,40,'draft_field',{'field':'to'}),s.line('to_rule',153),
            s.text('subject_label','Subject:',22,163,74,40,16,400,GRAY),s.field('subject',state['draft']['subject'],'Subject',101,163,283,40,'draft_field',{'field':'subject'}),s.line('subject_rule',210),
            s.field('body',state['draft']['body'],'Write your message…',23,235,359,360,'draft_field',{'field':'body'},multiline=True),
            s.button('save_draft','Save Draft',208,623,178,44,'save_draft',bg=LIGHT,enabled=not state.get('send_busy'),size=15)]
        if state.get('send_uncertain'):s.nodes.append(s.button('check_sent','Check Sent',20,623,178,44,'check_sent',bg=LIGHT,enabled=not state.get('send_busy'),size=15))
        if state.get('send_busy') or state.get('send_uncertain'):
            for node in s.nodes:
                if node.get('id') in ('to','subject','body'):
                    child=node['c'][0];child.update(t='text');child.pop('focused',None);node.pop('kit',None);s.controls.pop(node['id'],None)
        status=state.get('send_error') or ('Sending securely…' if state.get('send_busy') else 'Sends with your outgoing mail server')
        for i,line in enumerate(mail_lines(status,354,13)[:4]):s.nodes.append(s.text('send_status_'+str(i),line,26,682+18*i,354,18,13,400,'C83434' if state.get('send_error') else GRAY,.5))
    elif page=='drafts':
        s.chrome('Drafts',('Mailboxes','mailboxes'),('New','compose'))
        for i,d in enumerate(state['drafts'][-7:]):
            s.nodes += [s.button('draft_'+str(i),short(d['subject'] or '(No subject)',32),20,160+70*i,366,62,'open_draft',{'index':len(state['drafts'])-len(state['drafts'][-7:])+i},bg=LIGHT,icon='draft',color=INK)]
        if not state['drafts']:s.nodes.append(s.text('no_drafts','No saved drafts',20,350,366,40,22,400,GRAY,.5))
    elif page=='attachments':
        m=next(m for m in state['mailbox']['messages'] if m['id']==state['selected'])
        s.chrome('Attachments',('Message','read'))
        items=[]
        for i,item in enumerate(m.get('attachment_items',[])):
            y=157+i*86
            size=f"{item['size']} bytes" if item['size']<1024 else f"{item['size']/1024:.1f} KB" if item['size']<1_000_000 else f"{item['size']/1_000_000:.1f} MB"
            items += [s.icon('file_icon_'+str(i),'draft',25,y+17,30),s.text('file_name_'+str(i),short(item['filename'],29),66,y+4,242,29,15,600),
                s.text('file_size_'+str(i),size+' · '+short(item['mime'],27),66,y+35,245,25,12,400,GRAY),
                s.button('attachment_'+str(i),'Open',316,y+8,72,48,'attachment_open',{'index':i},enabled=not state.get('attachment_busy'),size=14),s.line('file_rule_'+str(i),y+78)]
        content=s.stack('attachment_content',0,157,406,max(478,len(m.get('attachment_items',[]))*86),children=items)
        s.nodes.append(s.stack('attachment_scroll',0,157,406,478,children=[content],variant='scroll_y'))
        if not items:s.nodes.append(s.text('no_attachments','Loading…' if state.get('attachment_busy') else 'No attachments',20,350,366,36,21,400,GRAY,.5))
        for i,line in enumerate(mail_lines(state.get('attachment_status',''),354,13)[:3]):s.nodes.append(s.text('attachment_status_'+str(i),line,26,654+20*i,354,20,13,400,GRAY,.5))
        if not state.get('attachment_busy') and m.get('attachments') and 'attachment_items' not in m:
            s.nodes.append(s.button('retry_attachments','Retry download',90,711,226,36,'attachments',size=14))
    elif page=='folders':
        moving=state.get('move_mode')
        s.chrome('Move Message' if moving else 'Gmail Folders',('Message','read') if moving else ('Mailboxes','mailboxes'))
        listing=[f for f in state.get('folders',[]) if not moving or f['movable']]
        items=[]
        for i,f in enumerate(listing):
            y=157+i*58
            items.append(s.button('remote_folder_'+str(i),short(f['name'],31),20,y,366,53,'move_folder' if moving else 'remote_folder',{'wire':f['wire']},bg=WHITE,icon='folder',color=INK,size=16,enabled=not state.get('loading_more') and not state.get('remote_busy')))
        content=s.stack('folder_content',0,157,406,max(510,len(listing)*58),children=items)
        s.nodes.append(s.stack('folder_scroll',0,157,406,510,children=[content],variant='scroll_y'))
        status='Loading folders…' if state.get('loading_more') else 'Syncing Gmail changes…' if state.get('remote_busy') else state.get('remote_error','')
        for i,line in enumerate(mail_lines(status,354,13)[:3]):s.nodes.append(s.text('folders_status_'+str(i),line,26,677+19*i,354,19,13,400,GRAY,.5))
        if state.get('remote_error'):s.nodes.append(s.button('retry_folders','Retry',130,721,146,34,'move' if moving else 'folders',size=14))
    elif page=='services':
        form=state['account_form'];busy=state['account_busy']
        s.chrome('Outgoing Mail',('Mail Server','settings'))
        s.nodes += [s.button('save_server','Save',320,40,74,42,'account_save',enabled=not busy),
            s.text('smtp_heading','SMTP SERVER',24,147,358,24,12,400,GRAY),s.stack('smtp_surface',20,180,366,96,WHITE,13)]
        for i,(key,label,placeholder) in enumerate([('smtp_host','Host Name','smtp.example.com'),('smtp_port','Port','465')]):
            y=180+i*48
            s.nodes += [s.text('server_label_'+key,label,33,y,99,48,14),s.field('server_'+key,form[key],placeholder,136,y+5,237,38,'account_field',{'field':key},focus=state.get('settings_focus')=='server_'+key,size=15)]
        s.nodes += [s.text('smtp_security_heading','CONNECTION SECURITY',24,297,358,24,12,400,GRAY),s.stack('smtp_security_surface',20,330,366,38,'E4E4EA',10)]
        for i,(key,label) in enumerate([('tls','SSL / TLS'),('starttls','STARTTLS')]):
            s.nodes.append(s.button('smtp_'+key,label,22+i*182,332,180,34,'smtp_security',{'security':key},bg=WHITE if form['smtp_security']==key else None,color=INK,size=14,enabled=not busy))
        s.nodes += [s.text('smtp_login','Uses the same user name and password.',24,382,358,24,13,400,GRAY,.5),
            s.text('gmail_sync_heading','GMAIL FOLDERS & FLAGS',24,433,358,24,12,400,GRAY),s.stack('gmail_sync_surface',20,467,366,54,WHITE,12),
            s.text('gmail_sync_label','Sync with Gmail',33,467,244,54,16),s.button('gmail_sync_toggle','On' if form['sync_enabled'] else 'Off',299,467,76,54,'account_sync',enabled=not busy and form['host']=='pop.gmail.com',size=15),
            s.text('gmail_sync_help','Read status, stars, archive and labels',24,534,358,24,13,400,GRAY,.5),
            s.text('gmail_sync_server','imap.gmail.com · SSL / TLS · 993',24,561,358,24,12,400,GRAY,.5),
            s.button('test_services','Testing…' if busy else 'Test Outgoing & Sync',20,612,366,46,'services_test',bg=WHITE,enabled=not busy,size=15)]
        for i,line in enumerate(mail_lines(state['account_error'] or state['account_status'],354,13)[:3]):s.nodes.append(s.text('services_status_'+str(i),line,26,681+20*i,354,20,13,400,'C83434' if state['account_error'] else GRAY,.5))
    elif page=='settings':
        form=state['account_form'];busy=state['account_busy']
        s.chrome('Mail Server',('Mailboxes','mailboxes'))
        s.nodes += [s.button('save_server','Save',320,40,74,42,'account_save',enabled=not busy),
            s.text('incoming_heading','INCOMING MAIL · POP3',24,145,358,24,12,400,GRAY),
            s.stack('incoming_surface',20,178,366,240,WHITE,13)]
        for i,(key,label,placeholder) in enumerate([('address','Email','you@example.com'),('username','User Name','Login name'),('host','Host Name','pop.example.com'),('port','Port','995')]):
            y=178+i*48
            s.nodes += [s.text('server_label_'+key,label,33,y,99,48,14),
                s.field('server_'+key,form[key],placeholder,136,y+5,237,38,'account_field',{'field':key},focus=state.get('settings_focus')=='server_'+key,size=15),
                s.line('server_rule_'+key,y+48,33,340)]
        password_label='New password · Change' if state['password_pending'] else 'Saved · Change' if state['password_saved'] else 'Set Password'
        s.nodes += [s.text('password_label','Password',33,370,99,48,14),
            s.button('server_password',password_label,138,370,235,48,'account_password',enabled=not busy,size=14,label_align=1),
            s.text('security_heading','CONNECTION SECURITY',24,434,358,24,12,400,GRAY),
            s.stack('security_surface',20,466,366,36,'E4E4EA',10)]
        for i,(key,label) in enumerate([('tls','SSL / TLS'),('starttls','STARTTLS')]):
            s.nodes.append(s.button('security_'+key,label,22+i*182,468,180,32,'account_security',{'security':key},bg=WHITE if form['security']==key else None,color=INK if form['security']==key else GRAY,size=14,enabled=not busy))
        gmail=form['host'].strip().lower()=='pop.gmail.com'
        if gmail:
            s.nodes += [s.stack('recent_surface',20,518,366,44,WHITE,12),s.text('recent_label','Gmail recent mode',33,518,243,44,15),
                s.button('recent_toggle','On' if form['recent'] else 'Off',299,518,76,44,'account_recent',enabled=not busy,size=15)]
        s.nodes.append(s.button('outgoing_settings','Outgoing mail & Gmail sync',24,566,358,34,'navigate',{'screen':'services'},size=14))
        s.nodes += [s.button('test_server','Testing…' if busy else 'Test Connection',20,608,178,44,'account_test',bg=WHITE,enabled=not busy,size=14),
            s.button('sync','Checking…' if state['syncing'] else 'Check for Mail',208,608,178,44,'sync',bg=WHITE,enabled=not state['syncing'] and not busy,size=14),
            s.button('use_sample','Use sample mailbox',23,709,175,34,'sample',size=13),s.button('use_gmail','Open inbox',204,709,178,34,'live',size=13)]
        status=state['account_error'] or state['error'] or state['account_status']
        for i,line in enumerate(mail_lines(status,354,12)[:2]):
            s.nodes.append(s.text('server_status_'+str(i),line,26,662+i*19,354,19,12,400,'C83434' if state['account_error'] or state['error'] else GRAY,.5))
    elif page=='card':
        s.chrome('Today')
        unread=[m for m in state['mailbox']['messages'] if m['unread'] and not m['archived']]
        c=[s.icon('card_mail_icon','mail',40,178,34),s.text('card_service','Mail',85,181,200,28,18,600),s.text('card_time','Just now',278,181,84,26,12,400,GRAY,1),
            s.text('card_title',f'{len(unread)} new '+('message' if len(unread)==1 else 'messages'),38,229,326,36,26,700)]
        for i,m in enumerate(unread[:2]):
            y=286+i*75
            c += [s.stack('card_dot_'+str(i),39,y+10,9,9,BLUE,5),s.text('card_sender_'+str(i),short(m['sender'],29),62,y,296,25,16,600),s.text('card_subject_'+str(i),short(m['subject'],38),62,y+27,296,24,14,400,GRAY)]
        c += [s.line('card_rule',445,20,366),s.button('card_open','Open Inbox',24,447,180,57,'folder',{'folder':'inbox'}),s.button('card_dismiss','Dismiss',205,447,177,57,'dismiss'),
            s.line('card_source_rule',505,20,366),s.icon('card_source_icon','mail',39,522,21),s.text('card_source',provider,71,519,290,26,12,400,GRAY)]
        if not state['card_dismissed']:s.nodes.append(s.stack('new_mail_card',20,158,366,405,WHITE,22,children=c))
        else:s.nodes.append(s.text('card_empty','You’re all caught up',20,330,366,40,23,600,GRAY,.5))
        s.nodes.append(s.button('open_mail','Open Mail',20,676,366,56,'folder',{'folder':'inbox'},bg=WHITE,icon='mail'))
    return s


def render(state, directory, design_id, reference=None, compile_native=True):
    directory=Path(directory)
    directory.mkdir(parents=True,exist_ok=True)
    scene=build(state)
    contract={'schema_version':1,'id':design_id,'app':'mail','number':1,'title':state['screen'],
        'artboard':[406,776],'palette':{'name':'iOS Mail'},'graphics':{},
        'tree':scene.stack('page',0,0,406,776,scene.background,children=scene.nodes)}
    atomic_json(directory/'contract.json',contract)
    if reference and not (directory/'reference.png').exists():shutil.copy2(reference,directory/'reference.png')
    if not (directory/'reference.png').exists():return contract
    for ident,content in scene.assets.items():
        (directory/'assets').mkdir(exist_ok=True)
        (directory/'assets'/f'{ident}.svg').write_text(content)
    mapped={'schema_version':1,'reference_sha256':hashlib.sha256((directory/'reference.png').read_bytes()).hexdigest(),
        'tree':deepcopy(contract['tree']),'basis':'Reviewed atlas hierarchy with explicit reflow to 406×776 logical points; runtime text comes from service state.'}
    atomic_json(directory/'mapped.json',mapped)
    (directory/'semantic-map.json').unlink(missing_ok=True)
    semantic=propose(directory)
    for entry in semantic['elements']:
        ident=entry['id']
        if ident in scene.assets:
            asset=directory/'assets'/f'{ident}.svg'
            entry.update(role='icon',basis='Reviewed thin-line icon reconstructed as editable native SVG from the email atlas',confidence=1,decision='reviewed',
                asset={'method':'reference_svg','path':f'assets/{ident}.svg','sha256':hashlib.sha256(asset.read_bytes()).hexdigest(),
                    'reference_sha256':mapped['reference_sha256'],'fit':'stretch','clip':False})
        if entry['role']=='input':
            entry['behavior']={'event':'changed','target':ident if ident.endswith('_input') else ident+'_input','property':'text'}
    atomic_json(directory/'semantic-map.json',semantic)
    atomic_json(directory/'service-actions.json',{'schema_version':1,'owner':'mail','controls':scene.controls})
    if compile_native:compile_page(directory)
    return contract
