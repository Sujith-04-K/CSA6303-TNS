controls = [
    ("Firewall", False),
    ("IDS/IPS", False),
    ("Endpoint Protection", True),
    ("Multi-Factor Authentication", False)
]

attack_blocked = False
for control, blocks_attack in controls:
    print("Checking:", control)
    if blocks_attack:
        print("Attack blocked by", control)
        attack_blocked = True
        break
    print("Attack passed this layer")

if attack_blocked:
    print("Protected resource remains unreachable in this simulation")
else:
    print("Attack reached the protected resource in this simulation")
