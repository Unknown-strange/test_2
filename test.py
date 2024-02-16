current_users = ["Prince","Edwin","Nyarko","Jesse","Bentil"]
new_users = ["Abam","Kofi","Yaw","Edwin","Prince"]

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} Enter new user name")
    else:
        print(f"{new_user} name is available")