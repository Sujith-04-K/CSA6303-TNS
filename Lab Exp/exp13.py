context = input("Is relevant context provided? (yes/no): ").strip().lower()
confidence = input("Is confidence assessed? (yes/no): ").strip().lower()
action = input("Is an actionable recommendation provided? (yes/no): ").strip().lower()

missing = []
if context != "yes":
    missing.append("Context")
if confidence != "yes":
    missing.append("Confidence assessment")
if action != "yes":
    missing.append("Actionability")

if not missing:
    print("Classification: Potentially actionable threat intelligence")
else:
    print("Classification: Incomplete or raw data")
    for item in missing:
        print("-", item, "is missing")
