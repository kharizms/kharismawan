# Penyesuaian 4-11
pizzas = ["pepperoni", "meat lovers", "cheese lovers"]
friend_pizzas = pizzas[:]

pizzas.append("hawaiian")
friend_pizzas.append("veggie")

print("Pizza favoritku:")
for pizza in pizzas:
    print(pizza)

print("\nPizza favorit temanku:")
for pizza in friend_pizzas:
    print(pizza)
    
# Penyesuaian 4-12
makananku = ["pizza", "donat kentang", "bomboloni"]
makanan_kawan = ["pizza", "donat jco", "croissant"] #variabel makananKawan diubah menjadi makanan_kawan agar konsisten dengan gaya penamaan snake_case

print("Makanan favoritku:")
for food in makananku:
    print(food)

print("\nMakanan favorit temanku:")
for food in makanan_kawan:
    print(food)
    
# Penyesuaian 4-13
# Warteg Kharisma Bahari References uhuy
foods = ("kering tempe", "sayur semur tahu", "opor ayam", "sop sayur", "sate ayam")

print("Menu awal Warteg Kharisma Bahari:")
for food in foods:
    print(f"- {food}")

foods = ("sayur mangut", "orak-arik tahu", "bakso", "telur dadar", "usus ayam")

print("\nMenu setelah direvisi:")
for food in foods:
    print(f"- {food}")