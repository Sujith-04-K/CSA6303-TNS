scenario = input("Enter business scenario: ").lower()

if any(word in scenario for word in ["bank", "payment", "transaction", "fraud"]):
    area = "Banking Fraud Prevention"
elif any(word in scenario for word in ["hospital", "patient", "medical", "healthcare"]):
    area = "Healthcare Data Protection"
elif any(word in scenario for word in ["e-commerce", "online store", "shopping", "retail"]):
    area = "E-commerce Fraud Prevention"
elif any(word in scenario for word in ["factory", "industrial", "iot", "manufacturing"]):
    area = "Industrial Threat Monitoring"
else:
    area = "General Cyber Threat Intelligence"

print("Threat-Intelligence Application:", area)
