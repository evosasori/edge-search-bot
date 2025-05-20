import random

# Daftar kata kerja, kata benda, dan pelengkap untuk membentuk pencarian
kata_kerja = [
    "cara membuat", "tutorial", "tips untuk", "panduan", "proses pembuatan",
    "metode", "langkah-langkah", "petunjuk", "teknik", "resep untuk",
    "rahasia membuat", "bagaimana cara", "strategi", "trik membuat", "sistem"
]

kata_benda = [
    "layangan", "kue", "meja", "kandang ayam", "aplikasi",
    "taman", "website", "kerajinan tangan", "bisnis online", "makanan sehat",
    "tas rajut", "komposter", "hidroponik", "buku digital", "lampu hias",
    "mainan edukasi", "perangkap nyamuk", "alat musik", "boneka", "video tutorial"
]

pelengkap = [
    "dari bambu", "yang mudah", "untuk pemula", "dengan cepat", "di rumah",
    "yang menguntungkan", "tanpa modal besar", "dalam waktu singkat", "dengan bahan bekas",
    "secara otomatis", "yang ramah lingkungan", "kekinian", "yang tahan lama",
    "yang menarik", "untuk bisnis", "dengan bahan alami", "yang praktis", "untuk anak",
    "hemat biaya", "yang kreatif"
]

# Fungsi untuk membuat satu pencarian random
def generate_search():
    return f"{random.choice(kata_kerja)} {random.choice(kata_benda)} {random.choice(pelengkap)}"

# Generate 100 pencarian random
random_searches = [generate_search() for _ in range(100)]

# Simpan ke file txt
with open("random_searches.txt", "w") as file:
    file.write("\n".join(random_searches))

print("100 pencarian random telah disimpan ke file 'random_searches.txt'")
