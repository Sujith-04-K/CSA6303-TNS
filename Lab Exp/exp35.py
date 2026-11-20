role_permissions = {
    "employee": {"read"},
    "analyst": {"read", "analyze"},
    "admin": {"read", "analyze", "manage_users"}
}

users = {
    "Alice": {"role": "employee", "permissions": {"read", "manage_users"}},
    "Bob": {"role": "analyst", "permissions": {"read", "analyze"}}
}

for username, details in users.items():
    role = details["role"]
    if role not in role_permissions:
        print(username, "has unknown role:", role)
        continue

    required = role_permissions[role]
    actual = details["permissions"]
    excess = actual - required

    if excess:
        print(username, "has excess permissions:", sorted(excess))
    else:
        print(username, "complies with least privilege")
