# some_file.py
import sys
sys.path.append('src/trp')

import time
import threading
import trp_client
import trp_server

test_port = 1600

class TRP_CLIENT_THREAD(threading.Thread):
    client = trp_client.TRP_client()
    def __init__(self):
        threading.Thread.__init__(self)
        self.client = trp_client.TRP_client()

    def run(self) -> None:
        print("Start of client")
        self.client.send("hello weed", "localhost", test_port)
        print("End of client")


class TRP_SERVER_THREAD(threading.Thread):
    server = trp_server.TRP_server()
    def __init__(self):
        threading.Thread.__init__(self)
        self.client = trp_server.TRP_server()

    def run(self) -> None:
        print("Start of server")
        print("Server received", self.server.receive(test_port))
        print("End of server")

t1 = TRP_SERVER_THREAD()
t1.start()
time.sleep(2)

t2 = TRP_CLIENT_THREAD()
t2.start()
t1.join()
t2.join()