from scapy.all import sniff, IP, TCP

# Use the Toshiba's IP
VICTIM_IP = "192.168.1.xx"

def detect_attack(packet):
    # This version is "Wide Open" - it will report ANY TCP packet hitting the Toshiba
    if packet.haslayer(TCP):
        if packet.haslayer(IP) and packet[IP].dst == VICTIM_IP:
            print(f"[ALERT] Packet Detected! Port: {packet[TCP].dport}")

print(f"[*] IDS listening on the Bridge for traffic to {VICTIM_IP}...")

# We use 'count=0' and no filters to force Scapy to grab every single frame
sniff(prn=detect_attack, store=0)