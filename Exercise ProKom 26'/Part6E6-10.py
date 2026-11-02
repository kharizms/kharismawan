favorite_numbers = {
    "afif": [7, 21, 99],
    "fadhil": [27, 45],
    "belva": [7, 12],
    "dicky": [10, 19, 88],
    "fikri": [19, 5],
}

for name, numbers in favorite_numbers.items():
    print(f"Nomor favorit {name.title()} adalah:")
    for number in numbers:
        print(f"\t- {number}")
    print()