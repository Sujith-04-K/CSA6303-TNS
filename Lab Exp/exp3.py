policy = input("Paste draft security policy text:\n").lower()

requirements = {
    "Scope": ["scope", "applies to"],
    "Roles and Responsibilities": ["responsibilities", "roles"],
    "Enforcement": ["enforcement", "disciplinary action"],
    "Review Cycle": ["review annually", "review cycle", "review every"],
    "Approval Authority": ["approved by", "approval authority"]
}

missing = []
for element, keywords in requirements.items():
    if not any(keyword in policy for keyword in keywords):
        missing.append(element)

if missing:
    print("\nMissing governance elements:")
    for element in missing:
        print("-", element)
else:
    print("\nAll required elements appear to be present.")

print("This is a keyword check, not a full compliance assessment.")
