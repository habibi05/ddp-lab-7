# Nama: Habibi
# NIM: 0110220247
# Kelas: TI07

def convert_list(multilist):
  # Tulis kode fungsi convert_list() di bawah ini
  # Hapus pass jika implementasi sudah dibuat

  # Buat nama variabel newMultilist dengan tipe data array
  newMultilist = []
  # Lakukan perulangan dengan nilai yang diterima sebagai parameter multilist
  for baris in multilist:
    # lakukan perulangan kembali dengan nilai yanga ada di variabel baris
    for elemen in baris:
      #tambahkan nilai kedalam variabel newMultilist
      newMultilist.append(elemen)
  # kembalikan nilai yang ada di varibel newMultilist
  return newMultilist

def get_nilai(filename, nama):
  # Tulis kode fungsi get_nilai() di bawah ini
  # Hapus pass jika implementasi sudah dibuat

  # buka file dengan nama file yang diterima oleh parameter filename, dan simpan datanya kedalam variabel f
  f = open(filename)
  # lakukan perulangan dengan data yang ada di variabel f
  for each_line in f:
    # masukan nilai each_line yang sudah dipisah menggunakan split dan simpan di variabel data
    data = each_line.split()
    # lakukan pengecekan, jika nilai yang ada di variabel data dan index ke 0 sama dengan nilai yang diterima oleh parameter nama
    if data[0].lower() == nama.lower():
      # jika sama maka akan mengembalikan nilai dalam bentuk float
      return round(float(data[1]))
  # panggil fungsi close untuk menyatakan telah selesai membuka file
  f.close()

def nilai_max(filename):
  # Tulis kode fungsi nilai_max() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  
  # Buat nama variabel list_nilai dengan tipe data array
  list_nilai = []
  # buka file dengan nama file yang diterima oleh parameter filename, dan simpan datanya kedalam variabel f
  f = open(filename)
  # lakukan perulangan dengan data yang ada di variabel f
  for each_line in f:
    # masukan nilai each_line yang sudah dipisah menggunakan split dan simpan di variabel data
    data = each_line.split()
    # masukan nilai data dan index ke 0 kedalam variabel nama
    nama = data[0]
    # masukan nilai data dan index ke 1 kedalam variabel nama dan bertipe float
    nilai = float(data[1])
    #tambahkan nilai kedalam variabel list_nilai, dengan nilai sebagai index 0 dan nama sebagai index 1
    list_nilai.append([nilai, nama])
  # panggil fungsi close untuk menyatakan telah selesai membuka file
  f.close()
  
  # mencari nilai max yang ada di variabel list_nilai
  max_nilai = max(list_nilai)
  # kembalikan nilai dari variabel max_nilai dengan index ke 1 baru index ke 2
  return max_nilai[1],max_nilai[0]





# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = convert_list([[1,2], [3,4], [5,6]])
  print(f"convert_list([[1,2], [3,4], [5,6]]) = {r} \n(solusi: [1, 2, 3, 4, 5, 6])")
  print()
  r = get_nilai('nilai1.txt','joni')
  print(f"get_nilai('nilai1.txt','joni') = {r} \n(solusi: 76)")
  print()
  r = get_nilai('nilai2.txt','joni')
  print(f"get_nilai('nilai2.txt','joni') = {r} \n(solusi: None)")
  print()
  r = nilai_max('nilai1.txt')
  print(f"nilai_max('nilai1.txt') = {r} \n(solusi: ('Zack', 88.05)")
  print()
  r = nilai_max('nilai2.txt')
  print(f"nilai_max('nilai2.txt') = {r} \n(solusi: ('Arya', 90.00)")
  print()

if __name__ == '__main__':
  test()