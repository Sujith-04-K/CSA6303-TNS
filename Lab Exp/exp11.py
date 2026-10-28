try:
    from scapy.all import sniff
except ImportError:
    raise SystemExit("Scapy is not installed. Run: python -m pip install scapy")

def display_packet(packet):
    print(packet.summary())

interface = input("Enter interface name (blank for default): ").strip() or None
count = int(input("Number of packets to capture: "))
if count <= 0:
    raise ValueError("Packet count must be positive.")

print("Starting packet capture. Use only on networks you are authorized to monitor.")
sniff(iface=interface, count=count, prn=display_packet, store=False)
print("Capture completed.")
