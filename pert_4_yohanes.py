# No 1 - Membuat fungsi input kemudian tampilkan ke konsol
es = input("Paling enak : ")
print(es, "enak banget woyy")

# No 2 - Membuat fungsi input dengan argumen
angka = input("Berapa usiamu : ")
print("Usiaku :", angka)

# No 3 - Memahami hasil dari fungsi input
a = input("Masukan angka pertama : ")
b = input("Masukan angka kedua : ")
print(a + b)

# No 4 - Mengkonversi tipe data float pada fungsi input
a = float(input("Masukan : "))
b = float(input("Masukan : "))
print("Hasil pengurangan :", a - b)

# No 5 - Menghitung sisi miring segitiga dengan variabel hypo
a = float(input("Masukan sisi a : "))
b = float(input("Masukan sisi b : "))
hypo = (a**2 + b**2) ** 0.5
print("Sisi miring segitiga adalah :", hypo)

# No 6 - Menghitung sisi miring segitiga tanpa variabel hypo
a = float(input("Masukan sisi a : "))
b = float(input("Masukan sisi b : "))
print("Sisi miring segitiga adalah :", (a**2 + b**2) ** 0.5)

# No 7 - Operator Konkatenasi
kata_depan = "Halo"
kata_belakang = "Dunia"
hasil = kata_depan + " " + kata_belakang
print(hasil)

# No 8 - Operator Replikasi
pembatas = "=" * 20
teriak = "Gol! " * 3
print(pembatas)
print(teriak)
print(pembatas)

# No 9 - Konversi ke String
nilai = 87.7
print("Nilai akhir : " + str(nilai))

# No 10 - Melihat tipe data dari suatu variabel
x = input("Enter a number : ")
print(type(x))

# No 11 - Kuis 7
a = float(input("Masukan nilai a : "))
b = float(input("Masukan nilai b : "))
print("Hasil penjumlahan :", a + b)
print("Hasil pengurangan :", a - b)
print("Hasil pembagian :", a / b)
print("Hasil perkalian :", a * b)
print("Selamat kamu sudah pintar matematika")

# No 12 - Kuis 8
x = float(input("Masukan nilai x : "))
y = 1.0 / (x + 1.0 / (x + 1.0 / (x + 1.0 / x)))
print("Hasil y =", y)

# No 13 - Kuis 9
jam = int(input("Masukan jam mulai : "))
menit = int(input("Masukan menit mulai : "))
durasi = int(input("Masukan durasi (menit) : "))

total_menit = menit + durasi
jam += total_menit // 60
menit = total_menit % 60
jam = jam % 24

print(f"Acara berakhir pukul {jam:02d}:{menit:02d}")