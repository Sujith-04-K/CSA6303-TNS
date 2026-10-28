report = input("Enter post-incident report:\n").lower()

areas = {
    "Patch Management": ["patch", "security update", "outdated software"],
    "Security Awareness": ["awareness", "phishing training", "training"],
    "Monitoring": ["monitoring", "logging", "detection"],
    "Backup Strategy": ["backup", "recovery copy", "restore"],
    "Access Control": ["access control", "least privilege", "permissions"]
}

found = [area for area, keywords in areas.items()
         if any(keyword in report for keyword in keywords)]

print("\nImprovement areas identified:")
if found:
    for area in found:
        print("-", area)
else:
    print("No matching areas found")
