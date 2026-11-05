def buat_album(nama_musisi, judul_album, jumlah_lagu=None):
  """Membangun dictionary yang mendeskripsikan album musik."""
  album = {
      "musisi": nama_musisi.title(),
      "judul": judul_album.title(),
  }

  if jumlah_lagu:
    album["jumlah_lagu"] = jumlah_lagu

  return album

album_1 = buat_album("Homecomings", "US")
album_2 = buat_album("髭男dism", "Pretender")
album_3 = buat_album("Mosawo", "Koiiro")

print(album_1)
print(album_2)
print(album_3)

album_opsional = buat_album("Homecomings", "New Neighbors", jumlah_lagu=12)
print(album_opsional)