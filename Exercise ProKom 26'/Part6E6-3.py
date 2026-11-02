glossary = {
    "dictionary": "Sebuah struktur data untuk menyimpan data berpasangan key-value.",
    "list": "Koleksi item yang berurutan dan dapat diubah (mutable).",
    "tuple": "Koleksi item berurutan yang sifatnya tetap (immutable).",
    "string": "Kumpulan karakter yang diapit oleh tanda kutip.",
    "conditional test": "Evaluasi logika yang menghasilkan nilai True atau False.",
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")