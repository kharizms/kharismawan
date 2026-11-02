person_1 = {
    "first_name": "Afif",
    "last_name": "Kharismawan",
    "age": 19,
    "city": "Pati",
}
person_2 = {
    "first_name": "Dicky",
    "last_name": "Hestu Pratama",
    "age": 19,
    "city": "Manokwari",
}
person_3 = {
    "first_name": "Fadhil",
    "last_name": "Pratama Harin",
    "age": 19,
    "city": "Grobogan",
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Name: {full_name}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city']}\n")