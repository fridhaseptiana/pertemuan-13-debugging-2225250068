# Pertemuan 13 - Debugging dan Testing

Nama: Fridha Septiana  
NIM: 2225250068  
Kelas: 3E

## Kasus

Program ini digunakan untuk mengolah data nilai mahasiswa, meliputi menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi. Program awal memiliki tiga bug yang menyebabkan hasil perhitungan dan penentuan status tidak sesuai dengan hasil yang diharapkan.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | [80, 60, 90, 70] | 75.0 | 60.0 | FAIL |
| T2 | [100, 80] | 90.0 | 36.0 | FAIL |
| T3 | 60 | Lulus | Tidak lulus | FAIL |
| T4 | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | [80, 60, 90, 70] | 90 | 0 | FAIL |

## Bug Report

**B01 - Kesalahan Perhitungan Rata-rata**

Gejala: Hasil rata-rata tidak sesuai dengan jumlah data.

Lokasi: Fungsi `hitung_rata_rata()`.

Akar penyebab: Program menggunakan angka 5 sebagai pembagi tetap sehingga tidak menyesuaikan jumlah data dalam list.

Perbaikan: Mengganti pembagi tetap dengan `len(nilai)` agar pembagian mengikuti jumlah elemen dalam list.

**B02 - Kesalahan Batas Kelulusan**

Gejala: Nilai 60 dinyatakan tidak lulus.

Lokasi: Fungsi `status()`.

Akar penyebab: Operator `>` hanya menerima nilai yang lebih besar dari 60, sehingga nilai 60 tidak termasuk dalam kategori lulus.

Perbaikan: Mengganti operator `>` menjadi `>=`.

**B03 - Kesalahan Pencarian Nilai Tertinggi**

Gejala: Program menghasilkan nilai tertinggi sebesar 0, padahal data memiliki nilai yang lebih besar.

Lokasi: Fungsi `nilai_tertinggi()`.

Akar penyebab: Nilai awal `tertinggi` ditetapkan 0 dan kondisi perbandingan menggunakan operator `<`, sehingga logika pencarian nilai tertinggi tidak berjalan dengan benar.

Perbaikan: Menginisialisasi `tertinggi` dengan elemen pertama list dan mengganti operator `<` menjadi `>`.

## Retest

Setelah program diperbaiki, seluruh test case dijalankan kembali dengan hasil berikut.

| ID | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| T1 | 75.0 | 75.0 | PASS |
| T2 | 90.0 | 90.0 | PASS |
| T3 | Lulus | Lulus | PASS |
| T4 | Tidak lulus | Tidak lulus | PASS |
| T5 | 90 | 90 | PASS |

Seluruh test case berhasil setelah perbaikan. Program telah menghasilkan rata-rata yang sesuai, menentukan status kelulusan berdasarkan batas nilai 60, dan menemukan nilai tertinggi dengan benar.

## Cara Menjalankan

Jalankan program melalui terminal VS Code menggunakan perintah:

`python3 praktik/praktik_4_debugging.py`

## Refleksi

Teknik debugging dan testing yang paling membantu adalah penggunaan test case dan tracing. Test case membantu menemukan kondisi yang menghasilkan output salah, sedangkan tracing membantu memahami proses eksekusi program dan menemukan akar penyebab bug. Setelah perbaikan dilakukan, seluruh test case dijalankan kembali untuk memastikan hasilnya sesuai dengan yang diharapkan.
