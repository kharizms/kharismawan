prompt = "\nBerapa usia kamu?"
prompt += "\n(Ketik 'selesai' untuk mengakhiri program) "

while True:
    input_usia = input(prompt)

    if input_usia == "selesai":
        break

    usia = int(input_usia)

    if usia < 3:
        print("Tiket kamu gratis!")
    elif usia <= 12:
        print("Harga tiket kamu adalah $10.")
    else:
        print("Harga tiket kamu adalah $15.")