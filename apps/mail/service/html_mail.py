"""Build a local, inert HTML email document for the platform WebView."""
import base64
import html
import re
from html.parser import HTMLParser


class EmailHTML(HTMLParser):
    blocked={'script','iframe','object','embed','applet','form','button','input','textarea','select','template','title'}
    void={'area','br','col','hr','img','wbr','source'}

    def __init__(self,images):
        super().__init__(convert_charrefs=False)
        self.images=images;self.parts=[];self.hidden=[]

    def handle_starttag(self,tag,attrs):
        if self.hidden:
            if tag==self.hidden[-1]:self.hidden.append(tag)
            return
        if tag in self.blocked:
            if tag not in ('input','embed'):self.hidden.append(tag)
            return
        if tag in ('html','head','body','meta','base','link','title'):return
        cleaned=[]
        for key,value in attrs:
            if value is None or key.startswith('on') or key in ('srcdoc','action','formaction','ping','target','srcset'):continue
            if key in ('href','src','background','xlink:href'):
                value=value.strip()
                if value.lower().startswith('cid:'):value=self.images.get(value[4:].strip('<>'),'')
                if not (value.startswith('#') or re.match(r'^(https?://|mailto:|data:image/(png|jpeg|gif|webp|svg\+xml);base64,)',value,re.I)):continue
            cleaned.append(f'{key}="{html.escape(value,quote=True)}"')
        self.parts.append('<'+tag+(' '+' '.join(cleaned) if cleaned else '')+'>')

    def handle_startendtag(self,tag,attrs):
        self.handle_starttag(tag,attrs)
        if tag not in self.void:self.handle_endtag(tag)

    def handle_endtag(self,tag):
        if self.hidden:
            if tag==self.hidden[-1]:self.hidden.pop()
            return
        if tag not in self.blocked|self.void|{'html','head','body','meta','base','link','title'}:self.parts.append('</'+tag+'>')

    def handle_data(self,data):
        if not self.hidden:self.parts.append(data)

    def handle_entityref(self,name):
        if not self.hidden:self.parts.append('&'+name+';')

    def handle_charref(self,name):
        if not self.hidden:self.parts.append('&#'+name+';')


def document(message,address):
    parser=EmailHTML(message.get('inline_images',{}));parser.feed(message['html']);parser.close()
    # Email copy is passive content. Embedded MIME images work offline; remote
    # resources and active content cannot execute or submit data from the reader.
    image_sources='data: https: http:' if message.get('load_remote_images') else 'data:'
    policy=f"default-src 'none'; img-src {image_sources}; style-src 'unsafe-inline'; font-src data:; base-uri 'none'; form-action 'none'; frame-src 'none'"
    subject=html.escape(message['subject']);sender=html.escape(message['sender']);recipient=html.escape(address)
    date=html.escape(message['time'])
    return f'''<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="{policy}">
<title>{subject}</title><style>
html,body{{margin:0!important;padding:0!important;background:#fff!important;color:#1c1c1e;font-family:-apple-system,BlinkMacSystemFont,sans-serif;font-size:16px;overflow-wrap:anywhere}}
.octos-header{{padding:8px 22px 18px!important;border-bottom:1px solid #e2e2e7!important;margin:0 0 18px!important;display:block!important;background:#fff!important;color:#1c1c1e!important}}
.octos-subject{{font:700 27px/1.25 -apple-system,sans-serif!important;margin:0 0 24px!important}}
.octos-sender{{font:600 17px/1.4 -apple-system,sans-serif!important}}
.octos-recipient,.octos-date{{font:400 12px/1.6 -apple-system,sans-serif!important;color:#8e8e93!important}}
.octos-date{{float:right!important}}
.octos-content{{padding:0 22px 28px!important;line-height:1.55}}
.octos-content img{{max-width:100%!important;height:auto}}
.octos-content table{{max-width:100%!important}}
.octos-content pre{{white-space:pre-wrap;overflow-wrap:anywhere}}
</style></head><body><section class="octos-header"><div class="octos-subject">{subject}</div>
<span class="octos-date">{date}</span><div class="octos-sender">{sender}</div><div class="octos-recipient">To: {recipient}</div></section>
<main class="octos-content">{''.join(parser.parts)}</main></body></html>'''


def document_url(message,address):
    return 'data:text/html;charset=utf-8;base64,'+base64.b64encode(document(message,address).encode()).decode('ascii')
