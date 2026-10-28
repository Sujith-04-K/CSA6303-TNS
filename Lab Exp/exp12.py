alert = input("Enter SOC alert description: ").lower()

if any(k in alert for k in ["ransomware", "active breach", "data exfiltration"]):
    priority = "P1 - Critical"
elif any(k in alert for k in ["malware detected", "privilege escalation", "multiple failed logins"]):
    priority = "P2 - High"
elif any(k in alert for k in ["suspicious login", "port scan", "policy violation"]):
    priority = "P3 - Medium"
else:
    priority = "P4 - Low"

print("Alert Priority:", priority)
