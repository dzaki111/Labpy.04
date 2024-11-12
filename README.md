### Tugas Praktikum - Program Pengelolaan Data Mahasiswa
## Deskripsi Program
Program ini adalah aplikasi sederhana berbasis command-line untuk mengelola data mahasiswa, termasuk nama, NIM, nilai tugas, UTS, dan UAS. Program memungkinkan pengguna untuk memasukkan data sebanyak-banyaknya dan menampilkan daftar data mahasiswa dalam format tabel. Nilai akhir setiap mahasiswa dihitung secara otomatis berdasarkan bobot yang ditentukan.

## Fitur Program
Input Data Mahasiswa: Program meminta pengguna untuk memasukkan nama, NIM, nilai tugas, UTS, dan UAS untuk setiap mahasiswa.
Perhitungan Nilai Akhir: Program menghitung nilai akhir berdasarkan bobot:
**Tugas: 30%
**UTS: 35%
** UAS: 35%
Tabel Output: Program menampilkan data semua mahasiswa dalam format tabel yang rapi.
Pengulangan: Pengguna dapat memasukkan data untuk beberapa mahasiswa hingga memilih untuk berhenti.
Struktur Program
1. Inisialisasi List
Program menyimpan data setiap mahasiswa dalam list data_list. Setiap data mahasiswa disimpan dalam dictionary yang berisi informasi lengkap: nama, NIM, nilai tugas, UTS, UAS, dan nilai akhir.

2. Fungsi calculate_final_grade
Fungsi ini digunakan untuk menghitung nilai akhir mahasiswa berdasarkan bobot nilai tugas, UTS, dan UAS. Fungsi menerima parameter nilai tugas, UTS, dan UAS, lalu mengembalikan hasil perhitungan nilai akhir.

python
Salin kode
def calculate_final_grade(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
3. Loop untuk Input Data Mahasiswa
Loop utama program meminta pengguna untuk memasukkan data mahasiswa. Setelah data dimasukkan, program akan bertanya apakah pengguna ingin menambahkan data lagi. Jika pengguna memilih y, program akan meminta data baru. Jika pengguna memilih t, loop akan berhenti dan data akan ditampilkan.

python
Salin kode
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
4. Menampilkan Data Mahasiswa dalam Format Tabel
Setelah loop berhenti, program menampilkan semua data mahasiswa yang sudah dimasukkan dalam format tabel yang rapi.

python
Salin kode
print("\n| No |    Nama    |  NIM  | Tugas | UTS | UAS |  Akhir  |")
print("=" * 55)
for idx, student in enumerate(data_list, start=1):
    print(f"| {idx:<2} | {student['Nama']:<10} | {student['NIM']:<5} | "
          f"{student['Tugas']:<5} | {student['UTS']:<3} | {student['UAS']:<3} | "
          f"{student['Nilai Akhir']:<7.2f} |")
Contoh Penggunaan Program
Input
Misalnya, pengguna memasukkan data seperti berikut:

yaml
Salin kode
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
Output
Program akan menampilkan data dalam format tabel seperti berikut:

markdown
Salin kode
| No |    Nama    |  NIM  | Tugas | UTS | UAS |  Akhir  |
=======================================================
| 1  | Ari        | 1234  | 70    | 65  | 80  |  71.75  |
| 2  | Bambang    | 2345  | 65    | 80  | 90  |  79.00  |
Flowchart
Anda dapat membuat flowchart berdasarkan langkah-langkah berikut:

Mulai.
Inisialisasi list data_list.
Loop untuk menerima input nama, NIM, nilai tugas, UTS, dan UAS.
Hitung nilai akhir.
Simpan data dalam dictionary dan tambahkan ke data_list.
Tanyakan apakah ingin menambah data lagi. Jika y, kembali ke langkah 3. Jika t, lanjut ke langkah 7.
Tampilkan data dalam format tabel.
Selesai.
Langkah-Langkah Menggunakan Program
Jalankan program di terminal atau IDE.
Masukkan data setiap mahasiswa sesuai dengan prompt yang diberikan.
Pilih y untuk menambah data mahasiswa baru atau t untuk menampilkan semua data.
Data akan ditampilkan dalam format tabel di terminal.
Cara Menyimpan dan Mengunggah Kode ke GitHub
Buat repository baru di GitHub.
Clone repository ke komputer Anda.
Simpan file program dan README.md di folder repository lokal.
Jalankan perintah berikut di terminal untuk commit dan push kode ke GitHub:
bash
Salin kode
git add .
git commit -m "Menambahkan program pengelolaan data mahasiswa"
git push origin main
