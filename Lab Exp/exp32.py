properties = [
    ("Encryption enabled", "Confidentiality", True),
    ("Unauthorized access prevented", "Confidentiality", False),
    ("File integrity verified", "Integrity", True),
    ("Backup service available", "Availability", False)
]

violations = set()
for description, principle, status in properties:
    if not status:
        violations.add(principle)
        print("Failed property:", description)

print("\nCIA principles violated:")
if violations:
    for principle in sorted(violations):
        print("-", principle)
else:
    print("None detected")
