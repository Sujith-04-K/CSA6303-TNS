report = input("Enter report description: ").lower()
audience = input("Enter intended audience: ").lower()

strategic = ["business risk", "long-term", "executive", "trend", "market impact"]
tactical = ["tactics", "techniques", "procedures", "mitre", "ttps"]
operational = ["attacker ip", "attack campaign", "incident", "ioc", "campaign details"]

scores = {
    "Strategic Intelligence": sum(k in report for k in strategic) + int("executive" in audience),
    "Tactical Intelligence": sum(k in report for k in tactical),
    "Operational Intelligence": sum(k in report for k in operational)
}
best = max(scores, key=scores.get)
if scores[best] == 0:
    print("Classification: Insufficient information")
else:
    print("Classification:", best)
