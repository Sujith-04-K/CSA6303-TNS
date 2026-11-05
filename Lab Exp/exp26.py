import hashlib

file_path = input("Enter sample file path: ").strip()
suspicious_strings = [
    b"CreateRemoteThread",
    b"VirtualAlloc",
    b"WriteProcessMemory"
]

try:
    with open(file_path, "rb") as file:
        data = file.read()

    print("SHA-256:", hashlib.sha256(data).hexdigest())
    print("\nStatic analysis:")
    found = False
    for api in suspicious_strings:
        if api.lower() in data.lower():
            print("Suspicious API string:", api.decode())
            found = True
    if not found:
        print("No listed API strings found")

    # Simulated behavior log; no sample is executed.
    behavior_log = [
        "process started",
        "created suspicious child process",
        "attempted network connection"
    ]
    print("\nSimulated dynamic analysis:")
    for event in behavior_log:
        if "suspicious" in event or "network" in event:
            print("Flagged behavior:", event)
except OSError as error:
    print("File error:", error)
