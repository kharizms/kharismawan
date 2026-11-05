group_size = input("Berapa orang yang ada di kelompok makan malammu? ")
group_size = int(group_size)

if group_size > 8:
    print("\nMaaf, kalian harus menunggu sebentar untuk mendapatkan meja.")
else:
    print("\nMeja kalian sudah siap!")