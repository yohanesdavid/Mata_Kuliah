# No 1 - Membuat dan menggunakan variabel

var = 10
nilai = 95
nama_mahasiswa = "Yohanes David"

print("var =", var)
print("nilai =", nilai)
print("nama mahasiswa =", nama_mahasiswa)


# No 2 - Variabel Nama

Nama = "Budi"

print(Nama)


# No 3 - Memasukkan nilai baru ke variabel yang sudah ada

umur = 18
print("Umur awal =", umur)

umur = 19
print("Umur baru =", umur)


# No 4 - Variabel Tabungan

tabungan = 50000
print("Tabungan awal =", tabungan)

tabungan = 80000 + 70000
print("Nilai Tabungan =", tabungan)


# No 5 - Shortcut Operators

angka = 20
print("Nilai awal:", angka)

angka += 5
print("Setelah += :", angka)

angka -= 3
print("Setelah -= :", angka)

angka *= 2
print("Setelah *= :", angka)

angka //= 4
print("Setelah //= :", angka)

angka %= 3
print("Setelah %= :", angka)

angka **= 2
print("Setelah **= :", angka)


# No 6 - Solving Simple Mathematical Problem

a = 3.0
b = 4.0

c = (a**2 + b**2) ** 0.5

print("c =", c)


# No 7 - Kuis 3

tabungan1 = 50000
tabungan2 = 75000
tabungan3 = 100000

print(tabungan1, tabungan2, tabungan3, sep=", ")

jumlahTabungan = tabungan1 + tabungan2 + tabungan3

print("Jumlah Tabungan adalah", jumlahTabungan)


# No 8 - Kuis 4

miles = 10
kilometers = round(miles * 1.61, 2)

print(miles, "mile =", kilometers, "kilometer")

kilometers = 16.1
miles = round(kilometers / 1.61, 2)

print(kilometers, "kilometer =", miles, "mile")


# No 9 - Kuis 5

for x in [0, 1, -1]:
    y = x**3 + x**2

    print("x =", x)
    print("y =", y)