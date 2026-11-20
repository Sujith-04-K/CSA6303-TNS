rules = [
    {"protocol": "TCP", "port": 22, "action": "DENY"},
    {"protocol": "TCP", "port": 443, "action": "ALLOW"},
    {"protocol": "TCP", "port": 22, "action": "ALLOW"}
]

def check_packet(protocol, port):
    for rule in rules:
        if protocol.upper() == rule["protocol"] and port == rule["port"]:
            return rule["action"]
    return "DENY"  # Default-deny

print("TCP port 22:", check_packet("TCP", 22))
print("TCP port 443:", check_packet("TCP", 443))
print("TCP port 80:", check_packet("TCP", 80))
