signatures = ["malicious_payload", "exploit_pattern"]
whitelist = {"192.0.2.50"}

def inspect_traffic(source_ip, payload):
    if source_ip in whitelist:
        print("ALLOW: Trusted source (whitelist)")
        return

    if any(signature in payload.lower() for signature in signatures):
        print("BLOCK: Signature matched")
    else:
        print("ALLOW: No signature matched")

inspect_traffic("198.51.100.10", "malicious_payload detected")
inspect_traffic("192.0.2.50", "malicious_payload detected")
inspect_traffic("198.51.100.20", "normal request")
print("Simulation only: this program does not block real network traffic.")
