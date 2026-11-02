rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "bengawan": "indonesia",
    "mississippi": "united states",
    "danube": "germany",
}

print("--- Informasi Sungai ---")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\n--- Daftar Sungai ---")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\n--- Daftar Negara ---")
for country in rivers.values():
    print(f"- {country.title()}")