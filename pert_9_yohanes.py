
=======================================
# soal no 1
====================

myList = [8, 10, 6, 2, 4]
print("List awal:", myList)

for i in range(len(myList) - 1):
    for j in range(len(myList) - 1 - i):
        if myList[j] > myList[j + 1]:
            myList[j], myList[j + 1] = myList[j + 1], myList[j]
    print(f"Pass {i+1}: {myList}")

print("List setelah bubble sort:", myList)
print()


# ============================================================
# PROGRAM 2: INTERACTIVE BUBBLE SORT
# ============================================================

myList = []
n = int(input("Berapa banyak elemen yang ingin dimasukkan? "))

for i in range(n):
    val = float(input("Masukkan elemen ke-" + str(i+1) + ": "))
    myList.append(val)

print("List awal:", myList)

swapped = True
while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print("List setelah diurutkan:", myList)
print()


# ============================================================
# PROGRAM 3: METHOD SORT()
# ============================================================

myList = [1, 5, 3, 9, 2]
print("List awal:", myList)

myList.sort()
print("Setelah sort() ascending:", myList)

myList.sort(reverse=True)
print("Setelah sort(reverse=True):", myList)

strList = ["apel", "mangga", "jeruk", "pisang"]
strList.sort()
print("List string setelah sort():", strList)
print()


# ============================================================
# PROGRAM 4: METHOD REVERSE()
# ============================================================
myList = [1, 2, 3, 4, 5]
print("List awal:", myList)

myList.reverse()
print("Setelah reverse():", myList)

strList = ["a", "b", "c", "d"]
strList.reverse()
print("List string setelah reverse():", strList)
print()


# ============================================================
# PROGRAM 5: THE INNER LIFE OF LIST - 1 (COPY LIST)
# ============================================================

list1 = [1, 2, 3]
list2 = list1  # reference yang sama
list3 = list1[:]  # copy value

print("list1:", list1)
print("list2 (reference):", list2)
print("list3 (copy):", list3)

list2[0] = 100
print("\nSetelah list2[0] = 100:")
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

list3[0] = 999
print("\nSetelah list3[0] = 999:")
print("list1:", list1)
print("list3:", list3)
print()


# ============================================================
# PROGRAM 6: SLICE -- 1 [awal:akhir]
# ============================================================

myList = [10, 20, 30, 40, 50, 60, 70]
print("List lengkap:", myList)

slice1 = myList[1:4]
print("myList[1:4]  :", slice1)

slice2 = myList[2:5]
print("myList[2:5]  :", slice2)

slice3 = myList[0:3]
print("myList[0:3]  :", slice3)
print()


# ============================================================
# PROGRAM 7: SLICE -- 2 [positif:negative]
# ============================================================

myList = [10, 20, 30, 40, 50, 60, 70]
print("List lengkap:", myList)

slice1 = myList[1:-2]
print("myList[1:-2] :", slice1)

slice2 = myList[2:-1]
print("myList[2:-1] :", slice2)

slice3 = myList[0:-3]
print("myList[0:-3] :", slice3)
print()


# ============================================================
# PROGRAM 8: SLICE -- 3 [negative:positif]
# ===========================================================

myList = [10, 20, 30, 40, 50, 60, 70]
print("List lengkap:", myList)

slice1 = myList[-5:5]
print("myList[-5:5] :", slice1)

slice2 = myList[-3:6]
print("myList[-3:6] :", slice2)

slice3 = myList[-7:3]
print("myList[-7:3] :", slice3)
print()


# ============================================================
# PROGRAM 9: SLICE -- 4 [:akhir]
# ============================================================

myList = [10, 20, 30, 40, 50, 60, 70]
print("List lengkap:", myList)

slice1 = myList[:4]
print("myList[:4]   :", slice1)

slice2 = myList[:-2]
print("myList[:-2]  :", slice2)

slice3 = myList[:3]
print("myList[:3]   :", slice3)
print()


# ============================================================
# PROGRAM 10: SLICE -- 5 [awal:]
# ============================================================

myList = [10, 20, 30, 40, 50, 60, 70]
print("List lengkap:", myList)

slice1 = myList[3:]
print("myList[3:]   :", slice1)

slice2 = myList[-4:]
print("myList[-4:]  :", slice2)

slice3 = myList[5:]
print("myList[5:]   :", slice3)
print()


# ============================================================
# PROGRAM 11: SLICE -- 6 [:]
# ============================================================

myList = [10, 20, 30, 40, 50]
print("List lengkap:", myList)

sliceAll = myList[:]
print("myList[:]    :", sliceAll)

print("Apakah myList[:] adalah copy?", sliceAll == myList)
print("Apakah myList[:] adalah objek yang sama?", sliceAll is myList)
print()


# ============================================================
# PROGRAM 12: MENGHAPUS SLICE
# ============================================================

myList = [10, 20, 30, 40, 50, 60, 70]
print("List awal:", myList)

del myList[1:4]
print("Setelah del myList[1:4]:", myList)

myList = [10, 20, 30, 40, 50, 60, 70]
del myList[:3]
print("Setelah del myList[:3] pada list baru:", myList)
print()


# ============================================================
# PROGRAM 13: MENGHAPUS SEMUA ELEMEN LIST
# ============================================================

myList = [1, 2, 3, 4, 5]
print("List awal:", myList)

del myList[:]
print("Setelah del myList[:]:", myList)
print("Panjang list:", len(myList))
print("Tipe data:", type(myList))
print()


# ============================================================
# PROGRAM 14: MENGHAPUS LIST
# ============================================================
myList = [1, 2, 3, 4, 5]
print("List awal:", myList)

del myList

try:
    print(myList)
except NameError:
    print("List telah dihapus! (NameError: myList tidak didefinisikan)")
print()


# ============================================================
# PROGRAM 15: PENGGUNAAN OPERATOR in
# ============================================================
myList = [1, 2, 3, 4, 5]
print("List:", myList)

print("3 in myList   :", 3 in myList)
print("10 in myList  :", 10 in myList)

strList = ["apel", "mangga", "jeruk"]
print("\nString list:", strList)
print("'apel' in strList   :", "apel" in strList)
print("'anggur' in strList :", "anggur" in strList)
print()


# ============================================================
# PROGRAM 16: PENGGUNAAN OPERATOR not in
# ============================================================
myList = [1, 2, 3, 4, 5]
print("List:", myList)

print("3 not in myList   :", 3 not in myList)
print("10 not in myList  :", 10 not in myList)

strList = ["apel", "mangga", "jeruk"]
print("\nString list:", strList)
print("'apel' not in strList   :", "apel" not in strList)
print("'anggur' not in strList :", "anggur" not in strList)
print()


# ============================================================
# PROGRAM 17: SIMPLE PROGRAM DARI LIST -- 1
# ============================================================
myList = [1, 2, 3, 4, 5]
total = 0

for i in myList:
    total += i

print("List:", myList)
print("Total penjumlahan elemen:", total)
print("Rata-rata:", total / len(myList))
print()


# ============================================================
# PROGRAM 18: SIMPLE PROGRAM DARI LIST -- 2
# ============================================================
myList = [5, 3, 8, 1, 9, 2]
print("List:", myList)

largest = myList[0]
smallest = myList[0]

for i in myList:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Nilai terbesar:", largest)
print("Nilai terkecil:", smallest)
print()


# ============================================================
# PROGRAM 19: SIMPLE PROGRAM DARI LIST -- 3
# ============================================================
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenList = []
oddList = []

for i in myList:
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)

print("List lengkap:", myList)
print("List bilangan genap:", evenList)
print("List bilangan ganjil:", oddList)
print()


# ============================================================
# PROGRAM 20: KUIS 21
# ============================================================
myList = [1, 2, 3, 4, 5]
newList = myList[-2:]
print("myList:", myList)
print("myList[-2:]:", newList)

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nmyList:", myList)
print("myList[::2]  :", myList[::2])
print("myList[1::2] :", myList[1::2])
print()


# ============================================================
# PROGRAM 21: KUIS 22
# ============================================================
myList = [1, 2, 3, 4, 5]
print("myList:", myList)

myList[1], myList[3] = myList[3], myList[1]
print("Setelah swap index 1 dan 3:", myList)

myList = [5, 1, 3, 2, 4]
myList.sort()
print("\nList setelah sort:", myList)

myList = [1, 2, 3]
myList = myList + [4, 5]
print("\nList setelah concatenation:", myList)
print()


# ============================================================
# PROGRAM 22: (Tambahan - melengkapi sampai 22)
# ============================================================

squares = [x**2 for x in range(1, 6)]
print("List comprehension x**2 untuk range(1,6):", squares)

cubes = [x**3 for x in range(1, 6)]
print("List comprehension x**3 untuk range(1,6):", cubes)

even = [x for x in range(10) if x % 2 == 0]
print("List comprehension bilangan genap 0-9:", even)

print("\n" + "=" * 60)
print("SELESAI - SEMUA PROGRAM TELAH DIJALANKAN")
print("=" * 60)
