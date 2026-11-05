guests = ["DimasBOWOK", "DhimasGYM", "Fadhil", "Dicky", "Fikri", "Haykal"]

print("Wah sorry! Meja makannya telat datang, aku cuma bisa invite 2 orang.\n")

popped_guest_1 = guests.pop()
print(f"Sorry {popped_guest_1}, aku ga bisa invite kamu.")

popped_guest_2 = guests.pop()
print(f"Sorry {popped_guest_2}, aku ga bisa invite kamu.")

popped_guest_3 = guests.pop()
print(f"Sorry {popped_guest_3}, aku ga bisa invite kamu.")

popped_guest_4 = guests.pop()
print(f"Sorry {popped_guest_4}, aku ga bisa invite kamu.\n")

# Mengirim pesan kepada 2 orang yang masih tersisa di list
print(f"Hai {guests[0]}, kamu masih kuundang kok.")
print(f"Hai {guests[1]}, kamu masih kuundang kok.\n")

del guests[0]
del guests[0]

print("Tamu terkini:", guests)