import threading
import socket

class Server(threading.Thread):
    _socket = None

    def __init__(self):
        threading.Thread.__init__(self)
        pass

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(("localhost", 5960))
        data, addr = self._socket.recvfrom(1024)
        print(data.decode('utf-8'))
        # ACK
        self._socket.sendto(str("ACK:" + str(data)).encode('utf-8'), addr)
        pass

if __name__ == '__main__':
    serverthread = Server()
    serverthread.start()
    serverthread.join()