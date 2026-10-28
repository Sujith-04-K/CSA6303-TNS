access_rules = {
    ("USER", "INTERNET"): True,
    ("USER", "SERVER"): True,
    ("SERVER", "DATABASE"): True,
    ("USER", "DATABASE"): False,
    ("GUEST", "DATABASE"): False,
    ("GUEST", "SERVER"): False
}

source = input("Enter source segment (USER/GUEST/SERVER): ").upper()
destination = input("Enter destination segment (INTERNET/USER/GUEST/SERVER/DATABASE): ").upper()

if access_rules.get((source, destination), False):
    print("ACCESS ALLOWED")
else:
    print("ACCESS DENIED")
    print("Default-deny segmentation blocked the connection.")
