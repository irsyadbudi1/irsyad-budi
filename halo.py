def segitiga_bintang(n):
    """
    Membuat segitiga bintang dengan tinggi n
    """
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

# Contoh penggunaan
tinggi = int(input("Masukkan tinggi segitiga: "))
segitiga_bintang(tinggi)
