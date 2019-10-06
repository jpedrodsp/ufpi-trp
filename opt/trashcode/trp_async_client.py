import threading
import socket
from src.trp import trp_packet


class TRP_async_client(threading.Thread):
    _socket = None
    ready = False
    send_buffer = []
    destination = None
    packet_count = 0

    # User Mechanisms
    def set_destination(self, target_host, target_port):
        self.destination = (target_host, target_port)

    def send_data(self, data):
        if self._socket and self.destination:
            new_packet = trp_packet.create_packet(self.packet_count, data)
            self.send_buffer.append(new_packet)

    def ready_connection(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ready = True

    def close_connection(self):
        self.ready = False

    # Class Mechanisms
    def __init__(self):
        threading.Thread.__init__(self)
        self.send_buffer = []

    def run(self) -> None:
        print("Starting TRP client...")
        if self._socket:
            print("Socket connection created sucessfully.")
            if self.destination:
                print("Destination is known.")
                while self.ready:
                    #print("Connection is ready to send data.")
                    while len(self.send_buffer):
                        # Try to send packet
                        print("Sending", self.send_buffer[0])
                        self._socket.sendto(str(self.send_buffer[0]).encode('utf-8'), self.destination)
                        # Wait for packet ack
        print("Ending TRP client...")

a = TRP_async_client()
a.set_destination("localhost", 5690)
a.ready_connection()
a.start()
a.join()