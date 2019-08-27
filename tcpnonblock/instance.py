import socket
import threading
import time
from .utils import *

class TCPSocketServerInstance:
    def __init__(self, cr, addr, server):
        self.cr = cr
        self.addr = addr
        self.ip = self.addr[0]
        self.server = server

        self.thd = None

        self.open = False

        self.running = True

    def main(self):
        self.server.on_connect(self)
        if hasattr(self, 'connect'):
            self.connect()
        while self.server.running and self.running:
            self.recv_loop()
        self.close()

    def start(self):
        self.thd = threading.Thread(target=self.main, daemon=True)
        self.thd.start()

    def send(self, msg):
        encode = msg.encode(self.server.charset)
        self.cr.send(encode)

    def recv_loop(self):
        recv = self.cr.recv(4096)
        if recv != b'':
            decode = recv.decode(self.server.charset)
            self.server.cal_on_message(self, decode)
            if hasattr(self, 'message'):
                self.message(decode)
        else:
            self.running = False

    def recv(self):
        recv = self.cr.recv(4096)
        decode = recv.decode(self.server.charset)
        return decode

    def close(self):
        self.running = False
        try:
            self.cr.close()
        except:
            pass
        try:
            self.server.connected.remove(self)
        except:
            pass
        self.server.on_disconnect(self)
        if hasattr(self, 'disconnect'):
            self.disconnect()

    def connect(self):
        pass

    def disconnect(self):
        pass

    def message(self, msg):
        pass
