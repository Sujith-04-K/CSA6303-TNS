incident = input("Enter incident narrative: ").lower()

categories = {
    "Phishing": ["phishing", "fake email", "malicious link"],
    "Unpatched Vulnerability": ["unpatched", "missing security update", "known cve"],
    "Misconfiguration": ["misconfigured", "publicly exposed", "default password"],
    "Insider Threat": ["employee stole", "insider", "unauthorized employee"],
    "Supply-Chain Compromise": ["compromised vendor", "malicious update", "third-party software"]
}

matches = [name for name, keywords in categories.items()
           if any(keyword in incident for keyword in keywords)]

if matches:
    print("Possible root cause:", matches[0])
else:
    print("Root cause requires further investigation")
