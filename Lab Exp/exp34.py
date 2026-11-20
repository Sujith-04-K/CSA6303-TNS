events = [
    {"ip": "198.51.100.10", "failed_logins": 12, "ioc": True},
    {"ip": "192.0.2.20", "failed_logins": 2, "ioc": False},
    {"ip": "203.0.113.30", "failed_logins": 9, "ioc": False}
]

print("Hypothesis-based hunting:")
for event in events:
    if event["failed_logins"] >= 5:
        print("Suspicious login activity:", event["ip"])

print("\nIntelligence-based hunting:")
for event in events:
    if event["ioc"]:
        print("Known IOC match:", event["ip"])

values = [event["failed_logins"] for event in events]
average = sum(values) / len(values)
threshold = average * 1.5

print("\nAnalytics-based hunting:")
for event in events:
    if event["failed_logins"] > threshold:
        print("Statistical anomaly:", event["ip"])
