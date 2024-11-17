## Muhamad Wafa Mufida Zulfi
## 312410334
## TI.24.A4
## Bahasa Pemograman
# LATIHAN PRAKTIKUM 5

![WhatsApp Image 2024-11-18 at 03 17 50](https://github.com/user-attachments/assets/aa579147-3d3b-4253-9609-ffac8ff31fec)

# ELEMEN PY
```PYTHON

list_a = [1, 2, 3, 4, 5]

print(list_a[2])

print(list_a[1:4])

print(list_a[-1])

list_a[3] = 10
print(list_a)

list_a[3:] = [11, 12, 13]
print(list_a)

list_b = list_a[:2]
print(list_b)

list_b.append("misalnya")
print(list_b)

list_b.extend([14, 15, 16])
print(list_b)

list_a.extend(list_b)
print(list_a)
````
# CODE VISUAL CODE
![Screenshot (9)](https://github.com/user-attachments/assets/7e0d7ea7-d91a-48e6-95a3-5d7643e73ae6)

# HASIL DARI PROGRAM TERSEBUT
![Screenshot (10)](https://github.com/user-attachments/assets/ae41aca9-fff8-4c94-afb2-8c249aa94cd7)

# MENAMBAH DATA.PY 
```PYTHON
class Mahasiswa:
    def init(self, nama, nim, nilai_tugas, nilai_uts, nilai_uas):
        self.nama = nama
        self.nim = nim
        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas

    def hitung_nilai_akhir(self):
        return (self.nilai_tugas + self.nilai_uts + self.nilai_uas) / 3

mahasiswa = []

while True:
    nama = input("Nama: ")
    nim = int(input("NIM: "))
    nilai_tugas = int(input("Nilai Tugas: "))
    nilai_uts = int(input("Nilai UTS: "))
    nilai_uas = int(input("Nilai UAS: "))

    mahasiswa.append(Mahasiswa(nama, nim, nilai_tugas, nilai_uts, nilai_uas))

    tambah_data = input("Tambah data (y/t)? ")
    if tambah_data.lower() == "t":
        break

print("-" * 60)
print("| No | Nama       | NIM  | Tugas | UTS  | UAS  | Akhir     |")
print("-" * 60)
    
for i, mhs in enumerate(mahasiswa):
    nilai_akhir = mhs.hitung_nilai_akhir()
    print(f"| {i+1:<2} | {mhs.nama:<10} | {mhs.nim:<4} | {mhs.nilai_tugas:<5} | {mhs.nilai_uts:<5} | {mhs.nilai_uas:<5} | {nilai_akhir:<9.2f} |")

print("-" * 60)
````

# PENJELASAN CODE MENAMBAH DATA
```PYTHON
class Mahasiswa:
    def _init_(self, nama, nim, nilai_tugas, nilai_uts, nilai_uas):
        self.nama = nama
        self.nim = nim
        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas
_init_: Konstruktor ini digunakan untuk menginisialisasi objek Mahasiswa dengan atribut: nama, nim, nilai_tugas, nilai_uts, nilai_uas

def hitung_nilai_akhir(self):
    return (self.nilai_tugas + self.nilai_uts + self.nilai_uas) / 3
````

### Metode ini mengembalikan nilai akhir mahasiswa, yang merupakan rata-rata dari nilai_tugas, nilai_uts, dan nilai_uas.
```PYTHON
mahasiswa = []
````
### Sebuah daftar kosong mahasiswa disiapkan untuk menyimpan objek Mahasiswa yang akan ditambahkan
```PYTHON
while True:
    nama = input("Nama: ")
    nim = int(input("NIM: "))
    nilai_tugas = int(input("Nilai Tugas: "))
    nilai_uts = int(input("Nilai UTS: "))
    nilai_uas = int(input("Nilai UAS: "))

    mahasiswa.append(Mahasiswa(nama, nim, nilai_tugas, nilai_uts, nilai_uas))

    tambah_data = input("Tambah data (y/t)? ")
    if tambah_data.lower() == "t":
        break
```

### Meminta pengguna untuk memasukkan data mahasiswa berulang kali hingga pengguna memasukkan t untuk berhenti, Setiap input digunakan untuk membuat data Mahasiswa, yang kemudian ditambahkan ke dalam daftar mahasiswa
```PYTHON
print("-" * 60)
print("| No | Nama       | NIM  | Tugas | UTS  | UAS  | Akhir     |")
print("-" * 60)

for i, mhs in enumerate(mahasiswa):
    nilai_akhir = mhs.hitung_nilai_akhir()
    print(f"| {i+1:<2} | {mhs.nama:<10} | {mhs.nim:<4} | {mhs.nilai_tugas:<5} | {mhs.nilai_uts:<5} | {mhs.nilai_uas:<5} | {nilai_akhir:<9.2f} |")

print("-" * 60)
```
### Header tabel dicetak terlebih dahulu, diikuti oleh baris-baris data untuk setiap mahasiswa, Untuk setiap mahasiswa, metode hitung_nilai_akhir dipanggil untuk menghitung nilai akhir, lalu data ditampilkan dalam format tabel

# HASIL DARI PROGRAM TERSEBUT

![Screenshot (11)](https://github.com/user-attachments/assets/5b82ee91-981c-4935-b504-f85f0b6435bf)

# DI BAWAH INI ADALAH FLOWCHARTNYA

![WhatsApp Image 2024-11-18 at 03 36 56](https://github.com/user-attachments/assets/c57507f5-3e64-40d1-8ac4-14ca10ee475d)


