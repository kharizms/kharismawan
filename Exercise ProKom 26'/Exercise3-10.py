gunung = ["Rinjani", "Semeru", "Kerinci", "Merbabu"]

print(f"Jumlah awal gunung dalam list: {len(gunung)}")

gunung.append("Arjuno Welirang")
print("Setelah append('Arjuno Welirang'):", gunung)

gunung.insert(1, "Jayawijaya")
print("Setelah insert(1, 'Jayawijaya'):", gunung)

popped_gunung = gunung.pop()
print(f"Gunung yang dihapus menggunakan pop(): {popped_gunung}")
print("List setelah pop():", gunung)

gunung.remove("Kerinci")
print("Setelah remove('Kerinci'):", gunung)

del gunung[0]
print("Setelah menghapus elemen pertama menggunakan del:", gunung)

print("Urutan sementara (sorted()):", sorted(gunung))
print("List asli setelah sorted():", gunung)

gunung.reverse()
print("Setelah reverse():", gunung)

gunung.sort()
print("Setelah sort() secara alfabetis:", gunung)

gunung.sort(reverse=True)
print("Setelah sort(reverse=True):", gunung)