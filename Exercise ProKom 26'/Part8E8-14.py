def buat_mobil(pabrikan, model, **info_tambahan):
  """Menyimpan informasi tentang mobil dalam sebuah dictionary."""
  mobil = {
      "pabrikan": pabrikan.title(),
      "model": model.title(),
  }
  for kunci, nilai in info_tambahan.items():
    mobil[kunci] = nilai

  return mobil


mobil = buat_mobil("subaru", "outback", warna="biru", paket_derek=True)

print(mobil)