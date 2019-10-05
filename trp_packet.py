packet_separator = "|:|"
default_time_limit = 10

class TRP_data_packet:
    id = None
    data = None
    time_limit = 0

    def __init__(self, id, data, time_limit):
        self.id = id
        self.data = data
        self.time_limit = time_limit

    def __str__(self):
        return "DAT" + packet_separator + str(self.id) + packet_separator + str(self.time_limit) + packet_separator + str(self.data)

class TRP_ack_packet:
    id = None
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "ACK" + packet_separator + str(self.id)

def create_packet(id, data):
    new_data_packet = TRP_data_packet(id, data, default_time_limit)
    return new_data_packet

def create_ack(id):
    new_ack_packet = TRP_ack_packet(id)
    return new_ack_packet