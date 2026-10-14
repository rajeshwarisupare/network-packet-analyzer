

from scapy.all import ARP, ICMP, IP, IPv6, TCP, UDP, Raw, sniff
from scapy.error import Scapy_Exception


PACKET_COUNT = 20
PAYLOAD_PREVIEW_BYTES = 32


def analyze_packet(packet):
    source_ip = "N/A"
    destination_ip = "N/A"
    ip_version = "N/A"

    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        ip_version = "IPv4"
    elif packet.haslayer(IPv6):
        source_ip = packet[IPv6].src
        destination_ip = packet[IPv6].dst
        ip_version = "IPv6"
    elif packet.haslayer(ARP):
        source_ip = packet[ARP].psrc
        destination_ip = packet[ARP].pdst

    if packet.haslayer(ARP):
        protocol = "ARP"
    elif packet.haslayer(TCP):
        protocol = "TCP"
    elif packet.haslayer(UDP):
        protocol = "UDP"
    elif packet.haslayer(ICMP):
        protocol = "ICMP"
    elif any(layer.__name__.startswith("ICMPv6") for layer in packet.layers()):
        protocol = "ICMPv6"
    else:
        protocol = "Other"

    print("=" * 50)
    print("Source IP      :", source_ip)
    print("Destination IP :", destination_ip)
    print("IP Version     :", ip_version)
    print("Protocol       :", protocol)
    print("Packet Length  :", len(packet), "bytes")
    print("Packet Data    :", packet.summary())

    if packet.haslayer(Raw):
        payload = bytes(packet[Raw].load)
        preview = payload[:PAYLOAD_PREVIEW_BYTES].hex(" ")
        suffix = " ..." if len(payload) > PAYLOAD_PREVIEW_BYTES else ""
        print("Payload        :", preview + suffix)
    else:
        print("Payload        : (none)")


def main():
    print("Network Packet Analyzer Started")
    print(f"Capturing up to {PACKET_COUNT} packets...")
    print("Press Ctrl+C to stop early.\n")

    try:
        sniff(prn=analyze_packet, count=PACKET_COUNT, store=False)
    except PermissionError:
        print("Permission denied. Run VS Code with appropriate privileges.")
    except KeyboardInterrupt:
        print("\nPacket capturing stopped.")
    except OSError as error:
        print(f"Capture failed: {error}")
        print("On Windows, verify that Npcap is installed and a capture interface is available.")
    except Scapy_Exception as error:
        print(f"Capture failed: {error}")


if __name__ == "__main__":
    main()
