from collections import Counter

firewall_logs = [
    {"ip": "198.51.100.40", "event": "blocked_connection"}
]
windows_logs = [
    {"ip": "198.51.100.40", "event": "failed_login"},
    {"ip": "198.51.100.40", "event": "failed_login"},
    {"ip": "198.51.100.40", "event": "failed_login"}
]
vpn_logs = [
    {"ip": "198.51.100.40", "event": "successful_login"}
]

blocked_ips = {e["ip"] for e in firewall_logs
               if e["event"] == "blocked_connection"}
failed_counts = Counter(e["ip"] for e in windows_logs
                        if e["event"] == "failed_login")
successful_vpn_ips = {e["ip"] for e in vpn_logs
                      if e["event"] == "successful_login"}

for ip, count in failed_counts.items():
    if count >= 3 and ip in blocked_ips and ip in successful_vpn_ips:
        print("CORRELATED ALERT:", ip)
        print("Repeated failures, firewall activity, and VPN success")
