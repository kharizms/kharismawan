tempat = ["Pati", "Kudus", "Demak", "Semarang", "Jepara"]

print("1. Urutan asli:")
print(tempat)

print("\n2. Urutan alfabetis (menggunakan sorted()):")
print(sorted(tempat))

print("\n3. Membuktikan bahwa urutan asli tidak berubah:")
print(tempat)

print("\n4. Urutan abjad terbalik (menggunakan sorted dengan reverse=True):")
print(sorted(tempat, reverse=True))

print("\n5. Membuktikan bahwa urutan asli masih tetap sama:")
print(tempat)

tempat.reverse()
print("\n6. Mengubah urutan secara permanen dengan reverse():")
print(tempat)

tempat.reverse()
print("\n7. Mengembalikan ke urutan asli dengan reverse() lagi:")
print(tempat)

tempat.sort()
print("\n8. Mengubah urutan secara permanen menjadi alfabetis dengan sort():")
print(tempat)

tempat.sort(reverse=True)
print("\n9. Mengubah urutan secara permanen menjadi abjad terbalik dengan sort(reverse=True):")
print(tempat)