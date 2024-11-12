
# Tugas Praktikum - Program Pengelolaan Data Mahasiswa

## Deskripsi Program
Program ini adalah aplikasi sederhana berbasis command-line untuk mengelola data mahasiswa, termasuk nama, NIM, nilai tugas, UTS, dan UAS. Program memungkinkan pengguna untuk memasukkan data mahasiswa sebanyak-banyaknya dan menampilkan daftar data mahasiswa dalam format tabel. Nilai akhir setiap mahasiswa dihitung secara otomatis berdasarkan bobot yang telah ditentukan.

## Fitur Program
1. **Input Data Mahasiswa**: Program meminta pengguna untuk memasukkan nama, NIM, nilai tugas, UTS, dan UAS untuk setiap mahasiswa.
2. **Perhitungan Nilai Akhir**: Program menghitung nilai akhir berdasarkan bobot:
   - Tugas: 30%
   - UTS: 35%
   - UAS: 35%
3. **Tabel Output**: Program menampilkan data semua mahasiswa dalam format tabel yang rapi.
4. **Pengulangan**: Pengguna dapat memasukkan data untuk beberapa mahasiswa hingga memilih untuk berhenti.

## Struktur Program

### 1. Inisialisasi List
Program menyimpan data setiap mahasiswa dalam list `data_list`. Setiap data mahasiswa disimpan dalam dictionary yang berisi informasi lengkap: nama, NIM, nilai tugas, UTS, UAS, dan nilai akhir.

### 2. Fungsi `calculate_final_grade`
Fungsi ini digunakan untuk menghitung nilai akhir mahasiswa berdasarkan bobot nilai tugas, UTS, dan UAS. Fungsi menerima parameter nilai tugas, UTS, dan UAS, lalu mengembalikan hasil perhitungan nilai akhir.

```python
def calculate_final_grade(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
```

### 3. Loop untuk Input Data Mahasiswa
Loop utama program meminta pengguna untuk memasukkan data mahasiswa. Setelah data dimasukkan, program akan bertanya apakah pengguna ingin menambahkan data lagi. Jika pengguna memilih `y`, program akan meminta data baru. Jika pengguna memilih `t`, loop akan berhenti dan data akan ditampilkan.

```python
data_list = []

while True:
    # Input data mahasiswa
    nama = input("Nama : ")
    nim = input("NIM : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS : "))
    uas = float(input("Nilai UAS : "))
    
    # Perhitungan nilai akhir
    final_grade = calculate_final_grade(tugas, uts, uas)
    
    # Simpan data mahasiswa
    student_data = {
        "Nama": nama,
        "NIM": nim,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": final_grade
    }
    data_list.append(student_data)

    # Pilihan untuk menambahkan data lagi
    more_data = input("Tambah data(y/t)? ")
    if more_data.lower() != 'y':
        break
```

### 4. Menampilkan Data Mahasiswa dalam Format Tabel
Setelah loop berhenti, program menampilkan semua data mahasiswa yang sudah dimasukkan dalam format tabel yang rapi.

```python
print("\n| No |    Nama    |  NIM  | Tugas | UTS | UAS |  Akhir  |")
print("=" * 55)
for idx, student in enumerate(data_list, start=1):
    print(f"| {idx:<2} | {student['Nama']:<10} | {student['NIM']:<5} | "
          f"{student['Tugas']:<5} | {student['UTS']:<3} | {student['UAS']:<3} | "
          f"{student['Nilai Akhir']:<7.2f} |")
```

## Contoh Penggunaan Program

### Input
Misalnya, pengguna memasukkan data seperti berikut:
```plaintext
Nama : Ari
NIM : 1234
Nilai Tugas : 70
Nilai UTS : 65
Nilai UAS : 80
Tambah data(y/t)? y
Nama : Bambang
NIM : 2345
Nilai Tugas : 65
Nilai UTS : 80
Nilai UAS : 90
Tambah data(y/t)? t
```

### Output
Program akan menampilkan data dalam format tabel seperti berikut:
```plaintext
| No |    Nama    |  NIM  | Tugas | UTS | UAS |  Akhir  |
=======================================================
| 1  | zaki       | 1234  | 70    | 65  | 80  |  71.75  |
| 2  | udin       | 2345  | 65    | 80  | 90  |  79.00  |
| 3  | santoso    | 2345  | 65    | 80  | 90  |  79.00  |
```

## Flowchart
Flowchart untuk program ini dapat diuraikan sebagai berikut:

1. **Mulai**: Program dimulai.
2. **Inisialisasi List**: Buat list `data_list` untuk menyimpan data mahasiswa.
3. **Loop Input Data**: Lakukan loop untuk menerima input data (nama, NIM, tugas, UTS, UAS).
4. **Hitung Nilai Akhir**: Menghitung nilai akhir berdasarkan nilai tugas, UTS, dan UAS dengan bobot yang telah ditentukan.
5. **Simpan Data**: Simpan data dalam dictionary dan tambahkan ke `data_list`.
6. **Tambah Data?**: Tanyakan apakah ingin menambah data lagi. Jika jawabannya `y`, kembali ke langkah 3. Jika `t`, lanjut ke langkah 7.
7. **Tampilkan Tabel Data**: Tampilkan semua data mahasiswa yang tersimpan dalam format tabel.
8. **Selesai**: Program berakhir.

## Langkah-Langkah Menggunakan Program
1. Jalankan program di terminal atau IDE.
2. Masukkan data setiap mahasiswa sesuai dengan prompt yang diberikan.
3. Pilih `y` untuk menambah data mahasiswa baru atau `t` untuk menampilkan semua data.
4. Data akan ditampilkan dalam format tabel di terminal.

## Cara Menyimpan dan Mengunggah Kode ke GitHub
1. Buat repository baru di GitHub.
2. Clone repository ke komputer Anda.
3. Simpan file program dan `README.md` di folder repository lokal.
4. Jalankan perintah berikut di terminal untuk mengunggah kode ke GitHub:

   ```bash
   git add .
   git commit -m "Menambahkan program pengelolaan data mahasiswa"
   git push origin main
   ```
