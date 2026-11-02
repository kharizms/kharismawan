def deskripsikan_kota(nama_kota, negara="indonesia"):
  """Menampilkan kalimat deskripsi kota dan negaranya."""
  print(f"{nama_kota.title()} berada di {negara.title()}.")


deskripsikan_kota("surakarta")

deskripsikan_kota("yogyakarta")

deskripsikan_kota("tokyo", negara="jepang")