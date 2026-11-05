def format_kota_negara(kota, negara):
  """Mengembalikan nama kota dan negara yang diformat dengan rapi."""
  return f"{kota.title()}, {negara.title()}"


pasangan_1 = format_kota_negara("surakarta", "indonesia")
pasangan_2 = format_kota_negara("tokyo", "jepang")
pasangan_3 = format_kota_negara("kuala lumpur", "malaysia")

print(pasangan_1)
print(pasangan_2)
print(pasangan_3)