glossary = {
    "dictionary": (
        "Sebuah struktur data untuk menyimpan data berpasangan key-value."
    ),
    "list": "Koleksi item yang berurutan dan dapat diubah (mutable).",
    "tuple": "Koleksi item berurutan yang sifatnya tetap (immutable).",
    "string": "Kumpulan karakter yang diapit oleh tanda kutip.",
    "conditional test": "Evaluasi logika yang menghasilkan nilai True atau False.",
    "loop": "Blok kode yang mengulangi serangkaian instruksi beberapa kali.",
    "key": "Pengenal unik dalam dictionary untuk mengakses value.",
    "value": "Data yang disimpan di dalam key pada sebuah dictionary.",
    "mutable": "Sifat objek yang dapat diubah nilainya setelah dibuat.",
    "immutable": "Sifat objek yang tidak dapat diubah setelah dibuat.",
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")