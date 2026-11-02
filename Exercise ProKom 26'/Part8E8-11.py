def kirim_pesan(daftar_pesan, daftar_terkirim):
  """Mencetak dan memindahkan pesan dari salinan list."""
  while daftar_pesan:
    pesan_saat_ini = daftar_pesan.pop(0)
    print(f"Mengirim pesan: '{pesan_saat_ini}'")
    daftar_terkirim.append(pesan_saat_ini)


pesan_teks = [
    "Halo, tugas prokommu udah selesai?",
    "Waduh, belum e!",
    "Gasin garap bareng.",
]
pesan_terkirim = []

print("=== MEMPROSES PENGIRIMAN PESAN (MENGGUNAKAN SALINAN LIST) ===")
kirim_pesan(pesan_teks[:], pesan_terkirim)

print("\n=== STATUS LIST SETELAH PENGIRIMAN ===")
print(f"Daftar pesan asli: {pesan_teks}")
print(f"Daftar pesan terkirim: {pesan_terkirim}")