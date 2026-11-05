perintah = "\nMasukkan topping pizza yang kamu inginkan:"
perintah += "\n(Ketik 'quit' jika sudah selesai) "

while True:
    topping = input(perintah)

    if topping == "quit":
        break
    else:
        print(f"Kami akan menambahkan {topping} ke pizza kamu!")