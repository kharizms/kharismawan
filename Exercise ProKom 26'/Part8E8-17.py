def hitung_luas_persegi_panjang(panjang, lebar):
  """Menghitung luas persegi panjang berdasarkan panjang dan lebar."""
  luas = panjang * lebar
  return luas


def sapa_pengguna(nama_depan, nama_belakang):
  """Menampilkan sapaan formal kepada pengguna."""
  nama_lengkap = f"{nama_depan} {nama_belakang}"
  print(f"Selamat datang kembali, {nama_lengkap.title()}!")