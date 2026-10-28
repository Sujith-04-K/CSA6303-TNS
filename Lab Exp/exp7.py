from collections import Counter

raw_logs = [
    "2026-10-28,login,success",
    "2026-10-28,login,failed",
    "2026-10-28,firewall,blocked",
    "2026-10-28,login,failed"
]

# Logstash-style parsing
events = []
for line in raw_logs:
    date, event_type, status = line.split(",")
    events.append({"date": date, "event_type": event_type, "status": status})

# Elasticsearch-style in-memory index
index = {i: event for i, event in enumerate(events)}

# Kibana-style aggregation
counts = Counter(event["status"] for event in index.values())

print("Structured events:")
for event in index.values():
    print(event)

print("\nStatus aggregation:")
for status, count in counts.items():
    print(f"{status}: {count}")
