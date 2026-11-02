pesanan_sandwich = ["tuna", "roast beef", "turkey", "egg salad"]
sandwich_selesai = []

while pesanan_sandwich:
  sandwich_saat_ini = pesanan_sandwich.pop(0)
  print(f"Saya telah membuat sandwich {sandwich_saat_ini} Anda.")
  sandwich_selesai.append(sandwich_saat_ini)

print("\n=== Daftar Sandwich yang Selesai Dibuat ===")
for sandwich in sandwich_selesai:
  print(f"- Sandwich {sandwich.title()}")