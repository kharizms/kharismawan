def buat_profil(nama_depan, nama_belakang, **info_tambahan):
  """Membangun dictionary berisi informasi lengkap tentang pengguna."""
  profil = {
      "nama_depan": nama_depan.title(),
      "nama_belakang": nama_belakang.title(),
  }
  for kunci, nilai in info_tambahan.items():
    profil[kunci] = nilai

  return profil

profil_saya = buat_profil(
    "afif",
    "kharismawan",
    lokasi="surakarta",
    bidang_studi="teknik industri",
    minat="rantai pasok berkelanjutan",
)

print(profil_saya)