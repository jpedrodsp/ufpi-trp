import threading
import socket

class Client(threading.Thread):
    _socket = None

    def __init__(self):
        threading.Thread.__init__(self)
        pass

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.sendto("Hello, World".encode('utf-8'), ("localhost", 5960))
        ack_resp, addr = self._socket.recvfrom(1024)
        if decode_ack(ack_resp.decode('utf-8')):
            print('ok')
        else:
            print('fail')
        pass

def decode_ack(response):
    response = str(response)
    _sr = response.split(':')
    if len(_sr):
        print(_sr)
        if (_sr[0] == "ACK"):
            return True
        else:
            return False

if __name__ == '__main__':
    clientthread = Client()
    clientthread.start()
    clientthread.join()