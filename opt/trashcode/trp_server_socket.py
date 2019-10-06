import socket
from src.trp import trp_packet

default_socket_buffer_size = 1024

class TRP_server_socket:
    _socket = None
    hostport = 6900
    is_ready = False
    receiving_buffer = []

    def __init__(self, hostport):
        self.hostport = hostport

    def start(self):
        if not self._socket:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self._socket.bind(("localhost", self.hostport))
            self._socket.accept()
            print("TRP socket server initialized.")
            self.is_ready = True
            print("TRP server node initialized.")

    def stop(self):
        if self._socket:
            if self.is_ready:
                self.is_ready = False
            self._socket.close()
            print("TRP node closed.")

    def send_data(self, data, destination_address=None):
        if self._socket and self.is_ready:
            new_packet = trp_packet.create_packet(self.send_buffer.count(), data)
            self.send_buffer.append(new_packet)
            print("TRP packet added to send_buffer:", str(new_packet))
            return new_packet
        return None

    def send_ack(self, packet):
        if self._socket and self.is_ready:
            new_packet = trp_packet.create_packet(self.send_buffer.count(), data)
            self.send_buffer.append(new_packet)
            return new_packet
        return None

    def receive_data_loop(self):
        if self._socket and self.is_ready:
            while (self.is_ready):
                data, addr = self._socket.recv(default_socket_buffer_size)
                if data:
                    print("Received data from", addr)
                    print(data)
                    _split_result = data.split(trp_packet.packet_separator)
                    if _split_result:
                        if _split_result[0] == "DAT":
                            new_packet = trp_packet.create_packet(int(_split_result[1]), _split_result[2])
                            # Answer with a ACK packet

                            #todo
                        elif _split_result[0] == "ACK":
                            new_packet = trp_packet.create_ack(int(_split_result[1]))
                            #todo
        return None
