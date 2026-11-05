def buat_sandwich(*bahan_tambahan):
  """Mencetak daftar bahan sandwich yang dipesan."""
  print("\nMembuat sandwich dengan bahan-bahan berikut:")
  for bahan in bahan_tambahan:
    print(f"  - {bahan}")

buat_sandwich("keju cheddar", "daging asap", "selada")
buat_sandwich("telur mata sapi", "tomat")
buat_sandwich(
    "daging sapi", "keju", "saus tomat", "mayones", "bawang bombay"
)