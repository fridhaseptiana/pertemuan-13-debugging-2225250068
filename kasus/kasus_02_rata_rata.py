# Kasus 02: Menghitung Rata-rata
def rata_rata(data):
    total = sum(data)
    # Bug: Pembagi menggunakan angka statis 5, padahal panjang data bisa berubah
    return total / 5

nilai_mahasiswa = [80, 90, 70]
print("Rata-rata:", rata_rata(nilai_mahasiswa))