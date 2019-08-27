import socket
import threading
import time
from .utils import *
from .instance import *

class TCPSocketServer:
    def __init__(self, threaded=False, charset="UTF-8", backlog=5, instance=TCPSocketServerInstance):
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.state = 0
        self.thread = None
        self.threaded = threaded
        self.charset = charset
        self.backlog = backlog
        self.thd = None
        self.instance = instance

        self.cal_on_start = emptyCallback
        self.cal_on_stop = emptyCallback
        self.cal_on_connect = emptyCallback
        self.cal_on_disconnect = emptyCallback
        self.cal_on_message = emptyCallback

        self.running = True

        self.connected = []

    def listen(self, host, port, start=False):
        self.host = host
        self.port = port
        self.sock.bind((self.host, self.port))
        if start:
            self.start()

    def main(self):
        self.cal_on_start(self.host, self.port)
        self.sock.listen(self.backlog)
        while self.running:
            cr, addr = self.sock.accept()
            inst = self.instance(cr, addr, self)
            self.connected.append(inst)
            # self.on_open(inst)
            inst.start()

    def close(self):
        self.cal_on_stop()
        self.running = False
        try:
            self.sock.close()
        except:
            pass
        self.clean_up()

    def clean_up(self):
        for c in self.connected:
            try:
                c.close()
                del c
            except:
                pass

        self.connected = []
        self.running = False

        del self.sock
        del self.thd
        del self

    def start(self):
        if self.threaded == True:
            self.thd = threading.Thread(target=self.main, daemon=True)
            self.thd.start()
            time.sleep(0.1)
        else:
            self.main()

    def on_start(self, func):
        self.cal_on_start = func

    def on_stop(self, func):
        self.cal_on_stop = func

    def on_connect(self, func):
        self.cal_on_connect = func

    def on_disconnect(self, func):
        self.cal_on_disconnect = func

    def on_message(self, func):
        self.cal_on_message = func

    def client_instance(self, class_handler):
        self.instance = class_handler
