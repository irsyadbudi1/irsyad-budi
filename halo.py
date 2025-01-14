def segitiga_bintang(n):
    """
    Membuat segitiga bintang dengan tinggi n
    """
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def segitiga_bintang_terbalik(n):
    """
    Membuat segitiga bintang terbalik dengan tinggi n
    """
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

# Contoh penggunaan
tinggi = int(input("Masukkan tinggi segitiga: "))
print("Segitiga biasa:")
segitiga_bintang(tinggi)
print("\nSegitiga terbalik:")
segitiga_bintang_terbalik(tinggi)
