def tampilkan_pesan(daftar_pesan):
  """Mencetak setiap pesan teks dari list yang diberikan."""
  for pesan in daftar_pesan:
    print(pesan)


pesan_teks = [
    "Hai",
    "Hai juga!",
    "Kamu asik, siapa namamu?",
]

tampilkan_pesan(pesan_teks)