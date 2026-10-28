baseline = {
    "firewall_enabled": True,
    "mfa_enabled": True,
    "disk_encryption": True,
    "automatic_updates": True
}

current = {
    "firewall_enabled": True,
    "mfa_enabled": False,
    "disk_encryption": True,
    "automatic_updates": False
}

failed = []
for control, required in baseline.items():
    if current.get(control) != required:
        failed.append(control)

if failed:
    print("Controls failing baseline:")
    for control in failed:
        print("-", control)
else:
    print("All controls meet the baseline")
