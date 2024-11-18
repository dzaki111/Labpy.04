# labpy.04
#### Nama   = DZAKI ARIF RAHMAN  
#### Kelas  = TI.24.A4  
#### NIM    = 312410312  
#### Matkul = BAHASA PEMOGRAMAN

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
def oi_final_grade(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
```

### 3. Loop untuk Input Data Mahasiswa
Loop utama program meminta pengguna untuk memasukkan data mahasiswa. Setelah data dimasukkan, program akan bertanya apakah pengguna ingin menambahkan data lagi. Jika pengguna memilih `y`, program akan meminta data baru. Jika pengguna memilih `t`, loop akan berhenti dan data akan ditampilkan.

```python
data_list = []

while True:
    NAMA = input('NAMA : ')
    NIM = input('NIM : ')
    TUGAS = input('TUGAS : ')
    UTS = input('TUGAS : ')
    UAS = input('TUGAS : ')

    final_grade = oi_final_grade(TUGAS * 0.30) + (UTS * 0.35) + (UAS * 0.30)

    mahasiswa_data ={
    'NAMA': NAMA,
    'NIM' : NIM,
    'TUGAS' :TUGAS,
    'UTS' :UTS,
    'UAS' :UAS,
   }

    data_list.append(mahasiswa_data)

    p_data = input('mau nambah data yang lain gak? (ya/tidak)')
    if p_data.lower() != 'ya':
        break
```
### 4. Menampilkan Data Mahasiswa dalam Format Tabel
Setelah loop berhenti, program menampilkan semua data mahasiswa yang sudah dimasukkan dalam format tabel yang rapi.

```python
print('\n| NO | NAMA | NIM | TUGAS | UTS | UAS | AKHIR |')
print("=" * 55)
for idx, student in enumerate(data_list, start=1):
    print(f"| {idx:<2} | {student['Nama']:<10} | {student['NIM']:<10} | "
          f"{student['Tugas']:<10} | {student['UTS']:<10} | {student['UAS']:<10} | "
          f"{student['Nilai Akhir']:<10.2f} |")

```
## FULL kodingannya

![Screenshot 2024-11-17 151500](https://github.com/user-attachments/assets/d7168227-2f3f-42fd-8f54-16ac4b010d39)

## Contoh Penggunaan Program

### Input
Misalnya, pengguna memasukkan data seperti berikut:
```plaintext
Nama : zaki 1
NIM : 1234
Nilai Tugas : 70
Nilai UTS : 65
Nilai UAS : 80
Tambah data(y/t)? ya
Nama : zaki 2
NIM : 2345
Nilai Tugas : 65
Nilai UTS : 80
Nilai UAS : 80
Tambah data(y/t)? ya
Nama : zaki 3
NIM : 3456
Nilai Tugas : 80
Nilai UTS : 40
Nilai UAS : 40
Tambah data(y/t)? tidak
```

### Output
Program akan menampilkan data dalam format tabel seperti berikut:
```plaintext
| No |     Nama     |  NIM  | Tugas |  UTS  |  UAS  |  Akhir  |
=======================================================
| 1  | zaki 1       | 1234  | 70.00 | 65.00 | 80.00 |  71.75  |
| 2  | zaki 2       | 2345  | 65.00 | 80.00 | 90.00 |  79.00  |
| 3  | zaki 3       | 3456  | 80.00 | 40.00 | 40.00 |  52.00  |
```
## HASIL SCREENSHOUT VSC

![Screenshot 2024-11-17 151445](https://github.com/user-attachments/assets/355e2868-1a92-4b55-93f8-5e180a1a7d8f)

## Flowchart

<img width="223" alt="image" src="https://github.com/user-attachments/assets/034e5fbb-cece-4274-9f5d-d35352e104ad">


