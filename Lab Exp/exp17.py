control = input("Describe the security control: ").lower()

if any(k in control for k in ["security policy", "management responsibility", "governance"]):
    domain = "Organizational Controls"
elif any(k in control for k in ["employee screening", "awareness training", "termination"]):
    domain = "People Controls"
elif any(k in control for k in ["server room", "physical access", "security camera"]):
    domain = "Physical Controls"
elif any(k in control for k in ["encryption", "access control", "network security", "backup", "logging"]):
    domain = "Technological Controls"
else:
    domain = "Domain requires further review"

print("Likely ISO/IEC 27001:2022 Annex A domain:", domain)
