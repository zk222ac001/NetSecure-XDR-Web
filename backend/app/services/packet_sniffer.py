from scapy.all import sniff

captured_packets = []

def process_packet(packet):

    try:

        packet_data = {

            "src": packet[0].src,
            "dst": packet[0].dst,
            "summary": packet.summary()
        }

        captured_packets.append(packet_data)

    except:
        pass

def start_sniffer():

    sniff(
        prn=process_packet,
        store=False
    )