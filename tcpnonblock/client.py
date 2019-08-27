import socket
import threading
import time
from . import utils

class TCPSocketClient:
    def __init__(self, threaded=False, charset="UTF-8"):
        self.host = None
        self.port = None

        self.sock = socket.socket()
        self.state = 0
        self.threaded = threaded
        self.thd = None
        self.charset = charset

        self.cal_on_open = emptyCallback
        self.cal_on_close = emptyCallback
        self.cal_on_message = emptyCallback
        self.cal_on_send = emptyCallback

        self.running = True

        self.pullBuffer = None

    def connect(self, host, port):
        self.host = host
        self.port = port
        if self.host == "localhost" or self.host == "172.0.0.1":
            host = socket.gethostname()
        self.sock.connect((host, port))

        self._start()

    def main(self):
        self.cal_on_open()
        while self.running:
            recv = self.sock.recv(2048)
            if recv == b'':
                self.close()
            else:
                if self.pullBuffer:
                    self.pullBuffer = recv.decode(self.charset)
                else:
                    self.cal_on_message(recv.decode(self.charset))

    def recv(self, buffer=2048):
        self.pullBuffer = True
        while self.pullBuffer:
            pass
        buff = self.pullBuffer
        self.pullBuffer = None
        return buff

    def send(self, msg):
        self.sock.send(msg.encode(self.charset))
        self.cal_on_send(msg)

    def close(self):
        self.cal_on_close()
        self.running = False
        try:
            self.sock.close()
        except:
            pass

    def _start(self):
        if self.threaded:
            self.thd = threading.Thread(target=self.main, daemon=True)
            self.thd.start()
            time.sleep(0.1)
        else:
            self.main()
            time.sleep(0.1)

    def on_open(self, func):
        self.cal_on_open = func

    def on_message(self, func):
        self.cal_on_message = func

    def on_close(self, func):
        self.cal_on_close = func

    def on_send(self, func):
        self.cal_on_send = func
