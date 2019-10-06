import threading
import time
import socket

class TRP_async_server(threading.Thread):
    _socket = None
    hostport = 4690
    ack_buffer = []

    def __init__(self):
        threading.Thread.__init__(self)
        self.hostport = 4690

    def setHostport(self, new_port):
        self.hostport = new_port

    def run(self) -> None:
        print("Starting TRP server at", self.hostport)
        _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _address = ("localhost", self.hostport)
        _socket.bind(_address)
        while True:
            data = _socket.recv(1024)
            if data:
                print("Data received")
                _socket.close()
                break
        print("Ending TRP server at", self.hostport)

a = TRP_async_server()
a.start()
a.join()