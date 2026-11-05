def kirim_pesan(daftar_pesan, daftar_terkirim):
  """Mencetak dan memindahkan pesan ke daftar pesan terkirim."""
  while daftar_pesan:
    pesan_saat_ini = daftar_pesan.pop(0)
    print(f"Mengirim pesan: '{pesan_saat_ini}'")
    daftar_terkirim.append(pesan_saat_ini)


pesan_teks = [
    "Hei kau",
    "Uy, hei juga!",
    "Ayok kenalan.",
]
pesan_terkirim = []

print("=== MEMPROSES PENGIRIMAN PESAN ===")
kirim_pesan(pesan_teks, pesan_terkirim)

print("\n=== STATUS LIST SETELAH PENGIRIMAN ===")
print(f"Daftar pesan asli: {pesan_teks}")
print(f"Daftar pesan terkirim: {pesan_terkirim}")