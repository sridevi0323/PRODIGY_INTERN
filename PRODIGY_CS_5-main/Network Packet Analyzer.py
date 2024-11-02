from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP


def packet_callback(packet):
    """
    Callback function to handle each packet captured by the sniffer.
    Prints relevant information such as source IP, destination IP, and protocol.

    Parameters:
    - packet: The network packet captured by scapy.
    """
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Map protocol numbers to names
        if protocol == 6:
            proto_name = "TCP"
        elif protocol == 17:
            proto_name = "UDP"
        elif protocol == 1:
            proto_name = "ICMP"
        else:
            proto_name = str(protocol)

        # Display packet details
        print(f"[{proto_name}] Source: {ip_src} --> Destination: {ip_dst}")

        # Additional information for TCP/UDP packets
        if proto_name == "TCP" and TCP in packet:
            print(f"   Source Port: {packet[TCP].sport} --> Destination Port: {packet[TCP].dport}")
        elif proto_name == "UDP" and UDP in packet:
            print(f"   Source Port: {packet[UDP].sport} --> Destination Port: {packet[UDP].dport}")
        elif proto_name == "ICMP" and ICMP in packet:
            print("   ICMP Packet")

        # Print payload data if available
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = packet[IP].payload
            print(f"   Payload: {str(payload)}")


if __name__ == "__main__":
    # Start sniffing and set the callback function
    print("Starting packet capture...")
    sniff(prn=packet_callback, store=False)
