import scapy.all as scapy
from scapy.layers import http

def summary_of_packets(packet):
    print("\n--- Summary ---")
    print(f"Packet_Name: {packet.name}")
    print(f"Origin (IP): {packet[scapy.IP].src if packet.haslayer(scapy.IP) else 'No IP found'}")
    print(f"Destination: {packet[scapy.IP].dst if packet.haslayer(scapy.IP) else 'N/A'}")
    print(f"Details: {packet.summary()}\n")

def process_packet(packet):
    # Print the basic packet summary
    print(packet.summary())
    
    # Call summary_of_packets for detailed structured output
    summary_of_packets(packet)
    
    # used to detect the HTTP requests
    if packet.haslayer(http.HTTPRequest):
        print("[HTTP Request]")
        print(f"Host: {packet[http.HTTPRequest].Host}")
        print(f"Path: {packet[http.HTTPRequest].Path}")

def sniffing(interface):
    print(f"Sniffing on interface: {interface}")
    # Filter for the sniffer, pretty raw at the moment however you can add more from the Scapy docs.
    scapy.sniff(iface=interface, store=False, prn=process_packet, filter="tcp")


"""
Just to spectify, if you attempt to run this code an error will arise due to the fact that the "sniffing()" statement requires YOUR unique network identifier.

This can be done by using the "SCAPY test.py" program. This program will run and create a list of all network identifiers.

However, you dont have to do this you can just enter 'sniffer(Wi-Fi)', 'sniffer(ethernet)' or 'sniffer(eth0)'.
"""

# Calling the sniffing tool
sniffing(r'\Device\NPF_{ED2197AA-3F1E-4B29-AB1A-A50E1898FB7E}')


