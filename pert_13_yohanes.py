# =========================================
# 1. MEMBUAT TUPLE DAN TAMPILKAN
# =========================================

data = (1, 2, 3)

print("Tuple:", data)
print("Indeks ke-0:", data[0])


# =========================================
# 2. MENGGUNAKAN TUPLE
# =========================================

buah = ("Apel", "Jeruk", "Mangga")

for item in buah:
    print(item)


# =========================================
# 3. MEMODIFIKASI TUPLE
# =========================================

data = (1, 2, 3)

temp = list(data)
temp[1] = 20

data = tuple(temp)

print(data)


# =========================================
# 4. TUPLE DENGAN len(), +, *, in, not in
# =========================================

angka = (1, 2, 3)

print("len =", len(angka))
print("gabung =", angka + (4, 5))
print("kali =", angka * 2)
print("2 in angka =", 2 in angka)
print("10 not in angka =", 10 not in angka)


# =========================================
# 5. PENUGASAN SIMULTAN PADA TUPLE
# =========================================

(a, b, c) = (10, 20, 30)

print(a)
print(b)
print(c)


# =========================================
# 6. MEMBUAT DICTIONARY DAN TAMPILKAN
# =========================================

mahasiswa = {
    "nama": "Yohanes",
    "umur": 20,
    "prodi": "Informatika"
}

print(mahasiswa)


# =========================================
# 7. MENGAKSES ISI DICTIONARY
# =========================================

mahasiswa = {
    "nama": "Yohanes",
    "umur": 20
}

print(mahasiswa["nama"])
print(mahasiswa["umur"])


# =========================================
# 8. METHOD keys()
# =========================================

mahasiswa = {
    "nama": "Yohanes",
    "umur": 20,
    "prodi": "Informatika"
}

print(mahasiswa.keys())


# =========================================
# 9. METHOD values()
# =========================================

mahasiswa = {
    "nama": "Yohanes",
    "umur": 20,
    "prodi": "Informatika"
}

print(mahasiswa.values())


# =========================================
# 10. METHOD items()
# =========================================

mahasiswa = {
    "nama": "Yohanes",
    "umur": 20,
    "prodi": "Informatika"
}

print(mahasiswa.items())


# =========================================
# 11. METHOD update()
# =========================================

mahasiswa = {
    "nama": "Yohanes",
    "umur": 20
}

mahasiswa.update({
    "umur": 21,
    "prodi": "Informatika"
})

print(mahasiswa)


# =========================================
# 12. METHOD popitem()
# =========================================

mahasiswa = {
    "nama": "Yohanes",
    "umur": 20,
    "prodi": "Informatika"
}

hasil = mahasiswa.popitem()

print("Data yang dihapus:", hasil)
print(mahasiswa)


# =========================================
# 13. MODIFIKASI DICTIONARY
# =========================================

mahasiswa = {
    "nama": "Yohanes",
    "umur": 20
}

# tambah
mahasiswa["prodi"] = "Informatika"

# ubah
mahasiswa["umur"] = 21

# hapus
del mahasiswa["nama"]

print(mahasiswa)


# =========================================
# 14. MENANGANI EXCEPTION
# =========================================

try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil =", hasil)

except ZeroDivisionError:
    print("Tidak bisa dibagi nol")

except ValueError:
    print("Input harus angka")


# =========================================
# 15. MENANGANI MULTIPLE EXCEPTION
# =========================================

try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka

except ZeroDivisionError as e:
    print("Error:", e)

except ValueError as e:
    print("Error:", e)

else:
    print("Hasil =", hasil)

finally:
    print("Program selesai")