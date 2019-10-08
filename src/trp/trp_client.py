import sys
sys.path.append('src/trp')

import socket
import time
import trp_defaults
import trp_packet

class TRP_client:
    _socket = None
    packet_count = 0

    def __init__(self):
        self.packet_count = 0
        self._socket = None
        pass

    def send(self, data, target_host, target_port):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.settimeout(trp_defaults.default_timeout)
        _address_tuple = (target_host, target_port)

        new_packet = trp_packet.create_packet(self.packet_count, data=data.encode('utf-8'))
        packet_acknowledged = False
        retry_timer = 1
        while not packet_acknowledged:
            #print("waiting for packet", new_packet.id)
            while True:
                try:
                    self._socket.sendto(str(new_packet).encode('utf-8'), _address_tuple)
                    resp, addr = self._socket.recvfrom(trp_defaults.default_buffer_max_size)
                    break
                except socket.timeout:
                    print("Client timeout. Retrying")
                    pass
            #print("received from server", resp)
            if trp_packet.convert_text_to_ack(resp.decode('utf-8')):
                packet_acknowledged = True
            else:
                time.sleep(retry_timer)
                retry_timer = retry_timer * 1.5
        self._socket.close()
