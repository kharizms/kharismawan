current_users = ["admin", "DimasBOWOK", "DhimasGYM", "Fadhil", "Belva"]

current_users_lower = [user.lower() for user in current_users]

new_users = ["Dicky", "Fikri", "Fadhil", "Kelvin", "Belva"]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' sudah digunakan. Silakan masukkan username lain.")
    else:
        print(f"Username '{new_user}' tersedia.")