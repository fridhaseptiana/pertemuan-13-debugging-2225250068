# Kasus 01: Batas Kelulusan
def status_lulus(nilai):
    # Bug: Menggunakan operator '>' seharusnya '>=' agar nilai 60 lulus
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"

# Pengujian
print("Nilai 75:", status_lulus(75))
print("Nilai 60:", status_lulus(60))  # Ini akan menghasilkan FAIL/salah sebelum diperbaiki
print("Nilai 59:", status_lulus(59))