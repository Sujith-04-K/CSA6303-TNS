import hashlib
import json

def record_hash(record):
    data = json.dumps(record, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()

# Build a valid example chain, linking each record to the previous hash.
records = []
previous_hash = "GENESIS"
for timestamp, description in [
    (100, "Evidence collected"),
    (110, "Evidence transferred"),
    (120, "Evidence analyzed")
]:
    record = {
        "timestamp": timestamp,
        "description": description,
        "previous_hash": previous_hash
    }
    records.append(record)
    previous_hash = record_hash(record)

# Verify links and non-decreasing timestamps.
previous_hash = "GENESIS"
last_timestamp = float("-inf")
valid = True

for record in records:
    if record["timestamp"] < last_timestamp:
        print("Timestamp order violation:", record["description"])
        valid = False
    if record["previous_hash"] != previous_hash:
        print("Broken hash link:", record["description"])
        valid = False

    previous_hash = record_hash(record)
    last_timestamp = record["timestamp"]

print("Chain of custody:", "VALID" if valid else "INVALID")
