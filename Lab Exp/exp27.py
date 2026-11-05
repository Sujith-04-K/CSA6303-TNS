signatures = [
    {"protocol": "TCP", "port": 80, "pattern": "suspicious_payload"},
    {"protocol": "TCP", "port": 443, "pattern": "known_exploit"}
]

def inspect(protocol, port, payload):
    for rule in signatures:
        if (protocol.upper() == rule["protocol"]
                and port == rule["port"]
                and rule["pattern"] in payload.lower()):
            print("IDS ALERT: Context and content matched")
            return
    print("No matching IDS signature")

inspect("TCP", 80, "suspicious_payload detected")
inspect("UDP", 80, "suspicious_payload detected")
