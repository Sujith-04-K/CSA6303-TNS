incident = input("Describe the security incident: ").lower()

if any(k in incident for k in ["ransomware", "infected endpoint"]):
    action = "Isolate the affected endpoint from the network"
elif any(k in incident for k in ["stolen password", "account takeover"]):
    action = "Restrict the account and revoke active sessions"
elif any(k in incident for k in ["data exfiltration", "data leak"]):
    action = "Restrict affected data paths and preserve evidence"
elif any(k in incident for k in ["ddos", "traffic flood"]):
    action = "Apply upstream filtering or DDoS mitigation"
elif "vulnerable server" in incident:
    action = "Restrict exposure and apply an approved mitigation"
else:
    action = "Escalate for investigation and determine containment needs"

print("Recommended containment:", action)
print("Validate the recommendation with the incident-response team.")
