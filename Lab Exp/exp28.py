from collections import Counter

# Simulated web access log lines: IP METHOD PATH
logs = [
    "198.51.100.10 GET /",
    "198.51.100.10 GET /login",
    "198.51.100.10 GET /products",
    "198.51.100.10 GET /cart",
    "192.0.2.20 GET /"
]

threshold = 3
counts = Counter(line.split()[0] for line in logs)

for ip, count in counts.items():
    if count > threshold:
        print(f"Possible DoS activity: {ip} ({count} requests)")

print("This simple count does not use a time window.")
