favorite_places = {
    "afif": ["kampus uns", "perpustakaan", "taman kota"],
    "dicky": ["bursa saham", "kafe kopi"],
    "belva": ["event anime", "warjaw"],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t- {place.title()}")
    print()