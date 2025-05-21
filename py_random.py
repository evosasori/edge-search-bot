import random

# Daftar kata kerja, kata benda, dan pelengkap untuk membentuk pencarian
kata_kerja = [
    "how to make", "guide", "tips for", "introduction to", "process of making",
    "method", "steps", "instructions", "techniques", "recipe for",
    "secrets to making", "how do you", "strategy", "tricks to make", "system"
]

kata_benda = [
    "birdhouse", "online course", "handmade craft", "garden decoration", "blog",
    "photography", "social media", "digital marketing", "web development", "cooking",
    "yoga", "fitness", "mental health", "travel", "language learning", "personal finance",
    "dog training", "cat grooming", "home cleaning", "time management", "self improvement"
]

pelengkap = [
    "with recycled materials", "in a sustainable way", "for beginners", "quickly at home",
    "that is profitable", "without a large investment", "in a short period", "with natural ingredients",
    "automatically", "that is eco-friendly", "trendy", "that is durable",
    "that is appealing", "for business", "with organic materials", "that is practical", "for kids",
    "cost-effective", "that is innovative"
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
