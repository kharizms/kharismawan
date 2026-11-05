def buat_album(nama_musisi, judul_album, jumlah_lagu=None):
  """Membangun dictionary yang mendeskripsikan album musik."""
  album = {
      "musisi": nama_musisi.title(),
      "judul": judul_album.title(),
  }

  if jumlah_lagu:
    album["jumlah_lagu"] = jumlah_lagu

  return album


prompt_musisi = "\nMasukkan nama musisi (ketik 'keluar' untuk selesai): "
prompt_judul = "Masukkan judul album: "

while True:
  musisi = input(prompt_musisi)
  if musisi.lower() == "keluar":
    break

  judul = input(prompt_judul)
  if judul.lower() == "keluar":
    break

  album_baru = buat_album(musisi, judul)
  print(f"\nAlbum berhasil dibuat: {album_baru}")