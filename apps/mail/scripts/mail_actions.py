"""Asynchronous mail operations; only the UI thread changes visible state."""
from copy import deepcopy
from datetime import datetime, timezone
from email import policy
from email.parser import BytesParser
import threading
import uuid
import gmail_sync
import sending
import attachments
from account import candidate
from mailbox import decode_message, merge_mailbox, fetch_gmail, atomic_json


class MailActions:
    def worker(self,kind,job,epoch=None):
        token=self.mailbox_epoch if epoch is None else epoch
        def work():
            try:data=job()
            except Exception:data={'error':'The mail service could not be reached. Check settings and retry.'}
            self.updates.put((kind,data,token))
        threading.Thread(target=work,daemon=True).start()

    def retry_remote(self):
        if self.state['pending_sync']:self.start_remote();self.mount()
        else:self.start_sync()

    def selected_message(self):
        return next(m for m in self.state['mailbox']['messages'] if m['id']==self.state['selected'])

    def sync_allowed(self):
        return self.account.get('sync_enabled') and self.account['host']=='pop.gmail.com' and self.state['mailbox']['address']!='you@gmail.com'

    def overlay_pending(self):
        for m in self.state['mailbox']['messages']:
            for key,value in self.state['pending_sync'].get(m['id'],{}).get('values',{}).items():
                if key.startswith('label:'):
                    labels=set(m.get('labels',[]));labels.add(key[6:]) if value else labels.discard(key[6:]);m['labels']=sorted(labels)
                else:m[key]=value
                if key=='archived':
                    labels=set(m.get('labels',[]));labels.discard('\\Inbox') if value else labels.add('\\Inbox');m['labels']=sorted(labels)

    def queue_changes(self,before):
        if not self.sync_allowed():return
        old={m['id']:m for m in before}
        for m in self.state['mailbox']['messages']:
            if m['id'] not in old or m.get('source')!='gmail':continue
            changes={key:m[key] for key in ('unread','flagged','archived') if m.get(key)!=old[m['id']].get(key)}
            if changes:self.queue_values(m['id'],changes)
        self.overlay_pending();self.start_remote()

    def queue_values(self,ident,values):
        pending=self.state['pending_sync'];previous=pending.get(ident,{}).get('values',{})
        pending[ident]={'version':uuid.uuid4().hex,'values':{**previous,**values}}
        self.state.update(remote_error='',notice='Syncing Gmail changes…')
        self.persist()

    def start_remote(self):
        if not self.sync_allowed() or not self.state['pending_sync'] or self.state['remote_busy'] or self.state['syncing'] or self.state['loading_more']:return
        self.state.update(remote_busy=True,remote_error='')
        config=dict(self.account);rows=deepcopy(self.state['mailbox']['messages']);pending=deepcopy(self.state['pending_sync'])
        def work():
            gmail_sync.headers(config,rows)
            result=gmail_sync.apply(config,rows,pending);result['identities']={m['id']:m.get('message_id','') for m in rows}
            return result
        self.worker('remote_done',work)

    def start_services_test(self):
        if self.state['account_busy']:return
        try:config=candidate(self.state['account_form'],self.settings_password)
        except ValueError as e:self.state.update(account_error=str(e));self.mount();return
        self.state.update(account_busy=True,account_error='',account_status='Testing outgoing mail and Gmail sync…',settings_focus=None);self.mount()
        def work():
            if not sending.smtp_test(config):raise RuntimeError('SMTP test failed')
            if config.get('sync_enabled'):
                client=gmail_sync.connect(config)
                try:gmail_sync.folders(client)
                finally:gmail_sync.close(client)
            return {'ok':True}
        self.worker('services_test',work,self.settings_generation)

    def restore_send_state(self):
        self.state.update(send_uncertain=False,send_error='')
        draft=self.state['draft'];draft.setdefault('id',uuid.uuid4().hex)
        record=sending.find_record(self.account,draft['id'])
        if record and record['status'] in ('sending','uncertain'):
            self.state.update(send_uncertain=True,send_error='Delivery is unconfirmed. Check Sent before sending again.')
        elif record and record['status']=='sent':self.sent_success(record)

    def start_send(self):
        if self.state['send_busy'] or self.state['send_uncertain']:return
        if self.state['mailbox']['address']=='you@gmail.com':
            self.state['send_error']='Open your mail account to send a message.';self.mount();return
        draft=deepcopy(self.state['draft']);draft.setdefault('id',uuid.uuid4().hex);self.state['draft']=draft
        try:sending.prepare(self.account,draft)
        except ValueError as e:self.state['send_error']=str(e);self.mount();return
        self.state.update(send_busy=True,send_error='');self.persist();self.mount()
        config=dict(self.account)
        def work():
            try:return {'record':sending.submit(config,draft)}
            except sending.SendFailure as e:return {'error':str(e),'uncertain':e.uncertain}
        self.worker('send_done',work)

    def sent_success(self,record):
        draft={'to':record['to'],'subject':record['subject'],'body':record['body']}
        msg,_=sending.prepare(self.account,draft,record['message_id'])
        m=decode_message(msg.as_bytes(),'sent:'+record['message_id'])
        m.update(unread=False,archived=True,labels=['\\Sent'],date=record.get('sent_at',datetime.now(timezone.utc).isoformat()),server_state=True)
        self.state['mailbox']=merge_mailbox(self.state['mailbox'],{'messages':[m]})
        self.state['drafts']=[d for d in self.state['drafts'] if d.get('id')!=record['draft_id']]
        if self.state['draft'].get('id')==record['draft_id']:
            self.state['draft']={'to':'','subject':'','body':''}
            if self.state['screen']=='compose':self.state['screen']='inbox'
        self.state.update(send_busy=False,send_uncertain=False,send_error='',notice='Message sent')

    def check_sent(self):
        if self.state['send_busy']:return
        record=sending.find_record(self.account,self.state['draft'].get('id',''))
        if not record:return
        if not self.sync_allowed():self.state['send_error']='Check Sent in your provider’s mail app before creating another message.';self.mount();return
        self.state.update(send_busy=True,send_error='Checking Gmail Sent…');self.mount();config=dict(self.account)
        def work():
            if gmail_sync.confirm_sent(config,record['message_id']):
                record.update(status='sent',sent_at=datetime.now(timezone.utc).isoformat());atomic_json(sending.record_path(config,record['draft_id']),record)
                return {'record':record}
            return {'error':'Not found in Sent yet. Wait, then check again. This draft will not resend automatically.','uncertain':True}
        self.worker('send_done',work)

    def start_attachments(self):
        self.state.update(screen='attachments',attachment_status='')
        message=deepcopy(self.selected_message())
        if 'attachment_items' in message or not message.get('attachments'):self.mount();return
        self.state.update(attachment_busy=True,attachment_status='Downloading attachments…');self.mount();config=dict(self.account)
        def work():
            if config['host']=='pop.gmail.com' and config.get('sync_enabled'):
                gmail_sync.headers(config,[message]);result=gmail_sync.hydrate(config,message)
            else:
                result=fetch_gmail(1,uids={message['uid']},account=config,max_message=40_000_000)['messages']
                if not result:raise RuntimeError('Message unavailable')
                result=result[0]
            return {'message':result}
        self.worker('attachments_done',work)

    def open_file(self,index):
        if self.state['attachment_busy']:return
        self.state.update(attachment_busy=True,attachment_status='Opening attachment…');self.mount()
        config=dict(self.account);message=deepcopy(self.selected_message())
        self.worker('attachment_opened',lambda:{'status':attachments.open_attachment(attachments.materialize(config,message,index))})

    def start_folders(self,move=False):
        if self.state['loading_more']:return
        self.state.update(screen='folders',move_mode=move)
        if not self.sync_allowed():self.state['remote_error']='Enable Gmail sync in Mail Server settings.';self.mount();return
        self.state.update(loading_more=True,remote_error='');self.mount();config=dict(self.account)
        def work():
            client=gmail_sync.connect(config)
            try:return {'folders':gmail_sync.folders(client)}
            finally:gmail_sync.close(client)
        self.worker('folders_done',work)

    def start_folder(self,wire,more=False):
        if self.state['loading_more'] or self.state['remote_busy']:return
        folder=next(f for f in self.state['folders'] if f['wire']==wire)
        self.state.update(screen='inbox',folder='remote:'+wire,loading_more=True,load_error='')
        if not more:self.state['query']=''
        if not more:self.state.update(list_scroll=0,list_start=0)
        page=self.state['folder_pages'].get(self.state['folder'],{});before=page.get('cursor') if more else None
        self.mount();config=dict(self.account)
        self.worker('folder_done',lambda:{'folder':wire,'append':more,**gmail_sync.fetch_folder(config,folder,before)})

    def move_message(self,wire):
        if not self.sync_allowed():return
        target=next(f for f in self.state['folders'] if f['wire']==wire and f['movable'])
        message=self.selected_message();values={}
        if target['label']=='\\Inbox':values['archived']=False
        else:values.update({'label:'+target['label']:True,'archived':True})
        current=next((f for f in self.state['folders'] if self.state['folder']=='remote:'+f['wire']),None)
        if current and current['movable'] and current['label']!=target['label'] and not current['label'].startswith('\\'):
            values['label:'+current['label']]=False
        self.queue_values(message['id'],values);self.overlay_pending();self.start_remote()
        self.state.update(screen='inbox',move_mode=False);self.mount()

    def mail_action(self,event,payload):
        actions={'send':self.start_send,'check_sent':self.check_sent,'attachments':self.start_attachments,
                 'services_test':self.start_services_test,'folders':self.start_folders,'move':lambda:self.start_folders(True),
                 'remote_retry':self.retry_remote,
                 'attachment_open':lambda:self.open_file(payload['index']),
                 'remote_folder':lambda:self.start_folder(payload['wire']),
                 'move_folder':lambda:self.move_message(payload['wire'])}
        if event not in actions:return False
        actions[event]();return True

    def mail_update(self,kind,data,epoch):
        if kind=='services_test':
            if epoch==self.settings_generation:
                self.state.update(account_busy=False,account_error=data.get('error',''),account_status='Outgoing mail and Gmail sync connected.' if data.get('ok') else 'Connection test failed.');self.mount()
            return True
        if kind not in ('remote_done','send_done','attachments_done','attachment_opened','folders_done','folder_done'):return False
        if epoch!=self.mailbox_epoch:return True
        s=self.state
        if kind=='remote_done':
            s['remote_busy']=False
            for ident,version in data.get('done',[]):
                if s['pending_sync'].get(ident,{}).get('version')==version:s['pending_sync'].pop(ident)
            for m in s['mailbox']['messages']:
                if data.get('identities',{}).get(m['id']):m['message_id']=data['identities'][m['id']]
            s.update(remote_error=data.get('error',''),notice='Gmail updated' if not s['pending_sync'] else 'Gmail changes pending')
            if not s['remote_error']:self.start_remote()
        elif kind=='send_done':
            s.update(send_busy=False,send_error=data.get('error',''),send_uncertain=data.get('uncertain',s['send_uncertain']))
            if data.get('record'):self.sent_success(data['record'])
        elif kind=='attachments_done':
            s.update(attachment_busy=False,attachment_status=data.get('error',''))
            if data.get('message'):
                # A reader download must not overwrite a newer local flag action.
                incoming={**data['message'],'server_state':False}
                s['mailbox']=merge_mailbox(s['mailbox'],{'messages':[incoming]});self.overlay_pending()
        elif kind=='attachment_opened':s.update(attachment_busy=False,attachment_status=data.get('error') or data.get('status',''))
        elif kind=='folders_done':
            s.update(loading_more=False,remote_error=data.get('error',''))
            if 'folders' in data:s['folders']=data['folders']
        elif kind=='folder_done':
            s.update(loading_more=False,load_error=data.get('error',''))
            if 'messages' in data:
                s['mailbox']=merge_mailbox(s['mailbox'],{'messages':data['messages']});self.overlay_pending()
                key='remote:'+data['folder']
                old_ids=s['folder_pages'].get(key,{}).get('ids',[]) if data.get('append') else []
                incoming_ids={m['id'] for m in data['messages']};incoming_rfc={m.get('message_id') for m in data['messages'] if m.get('message_id')}
                new_ids=[m['id'] for m in s['mailbox']['messages'] if m['id'] in incoming_ids or m.get('message_id') in incoming_rfc]
                s['folder_pages'][key]={**{k:data[k] for k in ('cursor','more')},'ids':list(dict.fromkeys(old_ids+new_ids))}
                s['notice']=f"{data['skipped']} messages exceed 40 MB" if data['skipped'] else 'Folder updated'
        if kind in ('folder_done','folders_done'):self.start_remote()
        if kind=='remote_done' and (s['screen']=='compose' or s['screen']=='read' and not s['remote_error']):self.persist()
        else:self.mount()
        return True
