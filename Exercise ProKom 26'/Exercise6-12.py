cities = {
    "surakarta": {
        "negara": "indonesia",
        "populasi": "522.000 jiwa",
        "mata_uang": "Rupiah (IDR)",
        "bahasa": "Bahasa Indonesia / Jawa",
        "fact": "Dikenal sebagai Kota Budaya dan pusat batik.",
    },
    "tokyo": {
        "negara": "jepang",
        "populasi": "14 juta jiwa",
        "mata_uang": "Yen (JPY)",
        "bahasa": "Bahasa Jepang",
        "fact": "Salah satu kota dengan otaku terbanyak di dunia.",
    },
}

for city_name, info in cities.items():
    print(f"=== {city_name.upper()} ===")
    print(f"Negara     : {info['negara'].title()}")
    print(f"Populasi   : {info['populasi']}")
    print(f"Mata Uang  : {info['mata_uang']}")
    print(f"Bahasa     : {info['bahasa']}")
    print(f"Fakta Unik : {info['fact']}\n")