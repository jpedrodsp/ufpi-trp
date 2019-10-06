import socket
import time
import src.trp.trp_defaults
import src.trp.trp_packet

class TRP_server:
    _socket = None
    hostport = src.trp.trp_defaults.default_host_port
    packet_count = 0
    is_open = False

    def __init__(self):
        self.packet_count = 0
        self._socket = None
        self.hostport = src.trp.trp_defaults.default_host_port
        self.is_open = False
        pass

    def open(self, hostport):
        self.hostport = hostport
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _address_tuple = ("localhost", hostport)
        self._socket.bind(_address_tuple)
        self.is_open = True

    def close(self):
        self.is_open = False
        self._socket.close()

    def receive(self, hostport):
        if not self.is_open:
            self.open(hostport)
        self._socket = socket.socket()
        while self.is_open:
            packet, recv_addr = self._socket.recvfrom(src.trp.trp_defaults.default_buffer_max_size)
            if packet:
                if src.trp.trp_packet.is_packet(str(packet).decode('utf-8')):
                    recv_packet = src.trp.trp_packet.convert_text_to_packet(str(packet))
                    if recv_packet:
                        ack_packet = src.trp.trp_packet.create_ack(recv_packet.id)
                        self._socket.sendto(str(ack_packet).encode('utf-8'), recv_addr)
                        return recv_packet.data
        return None