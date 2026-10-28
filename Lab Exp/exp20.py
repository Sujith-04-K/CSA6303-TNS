description = input("Describe the network threat: ").lower()

categories = {
    "Phishing": ["fake email", "phishing", "credential theft"],
    "DoS/DDoS": ["denial of service", "ddos", "traffic flood"],
    "Malware": ["ransomware", "trojan", "malicious software"],
    "Man-in-the-Middle": ["intercepts communication", "mitm", "traffic interception"]
}

matches = [name for name, keywords in categories.items()
           if any(keyword in description for keyword in keywords)]

if matches:
    print("Threat Category:", matches[0])
else:
    print("Threat category could not be identified")
