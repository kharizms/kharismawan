pet_1 = {"jenis": "kucing", "owner": "budi"}
pet_2 = {"jenis": "burung", "owner": "siti"}
pet_3 = {"jenis": "hamster", "owner": "andi"}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Animal: {pet['jenis'].title()}")
    print(f"\tOwner: {pet['owner'].title()}\n")