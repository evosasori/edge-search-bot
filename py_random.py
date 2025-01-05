import random

# Daftar kata kerja, kata benda, dan pelengkap untuk membentuk pencarian
kata_kerja = ["cara membuat", "tutorial", "tips untuk", "panduan", "proses pembuatan"]
kata_benda = ["layangan", "kue", "meja", "kandang ayam", "aplikasi"]
pelengkap = ["dari bambu", "yang mudah", "untuk pemula", "dengan cepat", "di rumah"]

# Fungsi untuk membuat satu pencarian random
def generate_search():
    return f"{random.choice(kata_kerja)} {random.choice(kata_benda)} {random.choice(pelengkap)}"

# Generate 100 pencarian random
random_searches = [generate_search() for _ in range(100)]

# Simpan ke file txt
with open("random_searches.txt", "w") as file:
    file.write("\n".join(random_searches))

print("100 pencarian random telah disimpan ke file 'random_searches.txt'")
