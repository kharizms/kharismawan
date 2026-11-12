guests = ["DimasBOWOK", "DhimasGYM", "Fadhil", "Dicky", "Fikri", "Haykal"]

print("Wah sorry! Meja makannya telat datang, aku cuma bisa invite 2 orang.\n")

# 1. Menggunakan while loop untuk mengeluarkan tamu sampai tersisa 2 orang
while len(guests) > 2:
    popped_guest = guests.pop()
    print(f"Sorry {popped_guest}, aku ga bisa invite kamu.")

print()

# 2. Menggunakan for loop untuk menyapa tamu yang masih tersisa
for guest in guests:
    print(f"Hai {guest}, kamu masih kuundang kok.")

print()

# 3. Mengosongkan list secara otomatis (bisa pakai .clear() atau looping del)
guests.clear()

print("Tamu terkini:", guests)