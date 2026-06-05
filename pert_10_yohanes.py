# =========================================
# 1. LIST COMPREHENSIONS
# =========================================

kuadrat = [x**2 for x in range(1, 11)]
print("1. List Comprehensions")
print(kuadrat)


# =========================================
# 2. ARRAY 2 DIMENSI
# =========================================

matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n2. Array 2 Dimensi")
for baris in matriks:
    print(baris)


# =========================================
# 3. LIST MULTIDIMENSI
# =========================================

data = [
    ["Andi", 85],
    ["Budi", 90],
    ["Citra", 88]
]

print("\n3. List Multidimensi")
for nama, nilai in data:
    print(f"Nama: {nama}, Nilai: {nilai}")


# =========================================
# 4. FUNGSI BERPARAMETER
# =========================================

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

print("\n4. Fungsi Berparameter")
print("Luas =", luas_persegi_panjang(10, 5))


# =========================================
# 5. KUIS 1
# =========================================

genap = [x for x in range(1, 21) if x % 2 == 0]

print("\n5. Kuis 1")
print(genap)


# =========================================
# 6. KUIS 2
# =========================================

nilai = [80, 75, 90, 85, 95]

print("\n6. Kuis 2")
print("Nilai tertinggi :", max(nilai))
print("Nilai terendah  :", min(nilai))
print("Rata-rata       :", sum(nilai)/len(nilai))


# =========================================
# 7. KUIS 3
# =========================================

buah = ["Apel", "Jeruk", "Mangga", "Anggur"]

print("\n7. Kuis 3")
for i, item in enumerate(buah, start=1):
    print(f"{i}. {item}")


# =========================================
# 8. SLICE 4
# =========================================

angka = [10,20,30,40,50,60,70,80,90]

print("\n8. Slice 4")
print("3 data pertama :", angka[:3])
print("3 data terakhir:", angka[-3:])
print("Data tengah    :", angka[2:7])
print("Selang 2       :", angka[::2])