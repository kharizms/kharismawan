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