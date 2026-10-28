raw_events = [
    {"source": "VPN", "user": "alice", "event": "failed_login"},
    {"source": "Windows", "user": "alice", "event": "failed_login"},
    {"source": "VPN", "user": "alice", "event": "failed_login"},
    {"source": "Firewall", "user": "bob", "event": "allowed"}
]

# Normalize events into a common schema.
normalized = [
    {"source": e["source"], "username": e["user"].lower(),
     "event_type": e["event"]}
    for e in raw_events
]

# Correlate failed logins by user.
failures = {}
for event in normalized:
    if event["event_type"] == "failed_login":
        user = event["username"]
        failures[user] = failures.get(user, 0) + 1

# Generate alerts.
for user, count in failures.items():
    if count >= 3:
        print(f"ALERT: {count} failed logins for user {user}")

print("SIEM pipeline completed.")
