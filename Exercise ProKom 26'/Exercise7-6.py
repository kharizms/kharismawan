prompt = "\nMasukkan topping pizza yang Anda inginkan:"
prompt += "\n(Ketik 'quit' untuk selesai) "

# Versi 1: Menggunakan tes kondisi langsung pada while statement 
print("=== VERSI 1: Tes Kondisi di While ===")
topping = ""
while topping != "quit":
  topping = input(prompt)
  if topping != "quit":
    print(f"Menambahkan {topping} ke pizza!")

# Versi 2: Menggunakan variabel penanda (active flag)
print("\n=== VERSI 2: Variabel Active Flag ===")
active = True
while active:
  topping = input(prompt)
  if topping == "quit":
    active = False
  else:
    print(f"Menambahkan {topping} ke pizza!")

# Versi 3: Menggunakan perintah break
print("\n=== VERSI 3: Perintah Break ===")
while True:
  topping = input(prompt)
  if topping == "quit":
    break
  print(f"Menambahkan {topping} ke pizza!")