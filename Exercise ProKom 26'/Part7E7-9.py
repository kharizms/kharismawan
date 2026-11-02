pesanan_sandwich = [
    "pastrami",
    "tuna",
    "pastrami",
    "roast beef",
    "turkey",
    "pastrami",
    "egg salad",
]
sandwich_selesai = []

print("Maaf, stok daging pastrami di deli sedang habis hari ini!\n")


while "pastrami" in pesanan_sandwich: # Menghapus semua kemunculan 'pastrami' dari daftar pesanan
  pesanan_sandwich.remove("pastrami")

while pesanan_sandwich:
  sandwich_saat_ini = pesanan_sandwich.pop(0)
  print(f"Saya telah membuat sandwich {sandwich_saat_ini} Anda.")
  sandwich_selesai.append(sandwich_saat_ini)

print("\n=== Daftar Sandwich yang Selesai Dibuat ===")
for sandwich in sandwich_selesai:
  print(f"- Sandwich {sandwich.title()}")