current_users = ["Prince","Edwin","Nyarko","Jesse","Bentil","kwabena"]
new_users = ["Abam","Kofi","Yaw","Edwin","Prince"]
current_names = [current_name.lower() for current_name in current_users]

    

for new_user in new_users:
    if new_user in current_names:
        print(f"{new_user} Enter new user name")
    else:
        print(f"{new_user} name is available")
print(current_names)
