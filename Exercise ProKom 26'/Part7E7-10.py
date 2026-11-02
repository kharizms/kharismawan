respon_survei = {}
survei_aktif = True

while survei_aktif:
  nama = input("\nSiapa nama Anda? ")
  tujuan = input(
      "Jika Anda bisa mengunjungi satu tempat di dunia, ingin pergi ke mana? "
  )

  # Menyimpan jawaban ke dalam dictionary
  respon_survei[nama] = tujuan

  lanjut = input(
      "Apakah ada orang lain yang ingin mengikuti survei? (ya/tidak) "
  )
  if lanjut.lower() == "tidak":
    survei_aktif = False

print("\n=== Hasil Polling Liburan Impian ===")
for nama, tempat in respon_survei.items():
  print(f"{nama.title()} ingin sekali mengunjungi {tempat.title()}.")