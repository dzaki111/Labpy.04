data_list = []

def oi_final_grade(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

while True:
    NAMA = input('NAMA : ')
    NIM = input('NIM : ')
    TUGAS = float(input('TUGAS : '))
    UTS = float(input('UTS : '))
    UAS = float(input('UAS : '))

    final_grade = oi_final_grade(TUGAS, UTS, UAS)

    mahasiswa_data = {
        'Nama': NAMA,
        'NIM': NIM,
        'Tugas': TUGAS,
        'UTS': UTS,
        'UAS': UAS,
        'Nilai Akhir': final_grade
    }

    data_list.append(mahasiswa_data)

    p_data = input('Mau nambah data yang lain gak? (ya/tidak): ')
    if p_data.lower() != 'ya':
        break

print('\n| NO | NAMA       | NIM        | TUGAS     | UTS       | UAS       | AKHIR     |')
print("=" * 70)
for idx, student in enumerate(data_list, start=1):
    print(f"| {idx:<2} | {student['Nama']:<10} | {student['NIM']:<10} | "
          f"{student['Tugas']:<10.2f} | {student['UTS']:<10.2f} | {student['UAS']:<10.2f} | "
          f"{student['Nilai Akhir']:<10.2f} |")
