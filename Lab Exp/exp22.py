logs = [
    ("alice", "failed"),
    ("alice", "failed"),
    ("alice", "failed"),
    ("alice", "success"),
    ("bob", "failed")
]

user = input("Enter username to investigate: ").strip().lower()
threshold = 3
failures = 0
detected = False

for username, status in logs:
    if username.lower() != user:
        continue

    if status == "failed":
        failures += 1
    elif status == "success":
        if failures >= threshold:
            detected = True
        failures = 0

if detected:
    print("ALERT: Possible brute-force pattern detected")
else:
    print("No qualifying pattern detected")
