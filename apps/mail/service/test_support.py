"""Local TLS SMTP fixture. Never forwards mail beyond the test process."""
from pathlib import Path
import socketserver
import ssl
import subprocess
import tempfile
import threading


class SMTPFixture:
    def __init__(self,mode='ok'):
        self.mode=mode;self.messages=[];self.commands=[];self.temp=tempfile.TemporaryDirectory();directory=Path(self.temp.name)
        key=directory/'key.pem';cert=directory/'cert.pem'
        subprocess.run(['openssl','req','-x509','-newkey','rsa:2048','-nodes','-keyout',str(key),'-out',str(cert),'-days','1','-subj','/CN=localhost','-addext','subjectAltName=DNS:localhost,IP:127.0.0.1'],check=True,capture_output=True)
        server_context=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER);server_context.load_cert_chain(cert,key)
        self.context=ssl.create_default_context(cafile=str(cert));owner=self
        class Server(socketserver.ThreadingTCPServer):
            daemon_threads=True;allow_reuse_address=True
            def get_request(self):
                sock,address=super().get_request();sock.settimeout(10)
                return server_context.wrap_socket(sock,server_side=True),address
            def handle_error(self,*args):pass
        class Handler(socketserver.StreamRequestHandler):
            def reply(self,line):self.wfile.write(line+b'\r\n');self.wfile.flush()
            def handle(self):
                self.reply(b'220 localhost test SMTP')
                while True:
                    line=self.rfile.readline(100000)
                    if not line:return
                    command=line.split(b' ',1)[0].strip().upper();owner.commands.append(command.decode())
                    if command==b'EHLO':self.reply(b'250-localhost\r\n250 AUTH PLAIN')
                    elif command==b'AUTH':self.reply(b'535 Login failed' if owner.mode=='auth_fail' else b'235 Authenticated')
                    elif command==b'RCPT':self.reply(b'550 Rejected' if owner.mode=='reject_recipient' else b'250 OK')
                    elif command==b'DATA':
                        if owner.mode=='reject_data':self.reply(b'554 Rejected');continue
                        self.reply(b'354 End with dot');lines=[]
                        while True:
                            part=self.rfile.readline(100000)
                            if not part:return
                            if part==b'.\r\n':break
                            lines.append(part[1:] if part.startswith(b'..') else part)
                        owner.messages.append(b''.join(lines))
                        if owner.mode=='disconnect_data':return
                        self.reply(b'250 Accepted')
                    elif command==b'QUIT':
                        if owner.mode!='quit_error':self.reply(b'221 Bye')
                        return
                    else:self.reply(b'250 OK')
        self.server=Server(('127.0.0.1',0),Handler);self.port=self.server.server_address[1]
        self.thread=threading.Thread(target=self.server.serve_forever,daemon=True);self.thread.start()
    def __enter__(self):return self
    def __exit__(self,*args):self.server.shutdown();self.server.server_close();self.thread.join();self.temp.cleanup()
