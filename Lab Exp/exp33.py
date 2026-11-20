action = input("Describe the incident response action: ").lower()

phases = {
    "Preparation": ["incident plan", "training", "prepare tools"],
    "Identification": ["detect incident", "investigate alert", "identify"],
    "Containment": ["isolate system", "block attacker", "contain"],
    "Eradication": ["remove malware", "remove persistence", "eradicate"],
    "Recovery": ["restore service", "restore backup", "recover"],
    "Lessons Learned": ["post-incident review", "lessons learned", "improve"]
}

matches = [phase for phase, keywords in phases.items()
           if any(keyword in action for keyword in keywords)]

if matches:
    print("Incident Response Phase:", matches[0])
else:
    print("Phase requires further analysis")
