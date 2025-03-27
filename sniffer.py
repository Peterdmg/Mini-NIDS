from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())

print("[*] Starting packet capture on interface en0...")
sniff(iface="en0", prn=process_packet, store=False)
