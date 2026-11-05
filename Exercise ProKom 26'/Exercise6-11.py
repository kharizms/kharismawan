kota = {
    "surakarta": {
        "negara": "indonesia",
        "populasi": "522.000 jiwa",
        "fact": "Dikenal sebagai Kota Budaya dan pusat batik.",
    },
    "yogyakarta": {
        "negara": "indonesia",
        "populasi": "422.000 jiwa",
        "fact": "Terkenal dengan kawasan Malioboro dan Kesultanan.",
    },
    "tokyo": {
        "negara": "jepang",
        "populasi": "14 juta jiwa",
        "fact": "Salah satu kota dengan otaku terbanyak.",
    },
}

for city_name, city_info in kota.items():
    print(f"Kota: {city_name.title()}")
    print(f"\tNegara: {city_info['negara'].title()}")
    print(f"\tPopulasi: {city_info['populasi']}")
    print(f"\tFakta Unik: {city_info['fact']}\n")
