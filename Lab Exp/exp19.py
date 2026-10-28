from collections import Counter

events = [
    {"user": "alice", "status": "failed", "source": "VPN"},
    {"user": "bob", "status": "success", "source": "Web"},
    {"user": "alice", "status": "failed", "source": "VPN"},
    {"user": "carol", "status": "success", "source": "VPN"}
]

# Search filter: failed VPN events.
filtered = [event for event in events
            if event["status"] == "failed" and event["source"] == "VPN"]

print("Search results:")
for event in filtered:
    print(event)

# Stats count by status.
counts = Counter(event["status"] for event in events)
print("\nStats count by status:")
for status, count in counts.items():
    print(status, count)
