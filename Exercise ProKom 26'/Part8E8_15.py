def cetak_model_3d(desain_belum_dicetak, model_selesai):
  """Mensimulasikan pencetakan desain hingga tidak ada yang tersisa.

  Memindahkan setiap desain ke model_selesai setelah dicetak.
  """
  while desain_belum_dicetak:
    desain_saat_ini = desain_belum_dicetak.pop(0)
    print(f"Mencetak model: {desain_saat_ini}")
    model_selesai.append(desain_saat_ini)


def tampilkan_model_selesai(model_selesai):
  """Menampilkan semua model yang sudah selesai dicetak."""
  print("\nModel berikut telah berhasil dicetak:")
  for model in model_selesai:
    print(f"- {model}")