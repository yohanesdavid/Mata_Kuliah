# NO 1: Indexing list
# ============================================================
numbers = [10, 5, 7, 2, 1]
print("NO 1 - Indexing list:")
print("Original list:", numbers)
print("\nList content:")
for i in range(len(numbers)):
    print(f"Element at index {i}:", numbers[i])
print()

# ============================================================
# NO 2: Mengakses isi list
# ============================================================
numbers = [10, 5, 7, 2, 1]
print("NO 2 - Mengakses isi list:")
print("Original list content:", numbers)
print("\nFirst element:", numbers[0])
print("Second element:", numbers[1])
print("Third element:", numbers[2])
print("Fourth element:", numbers[3])
print("Fifth element:", numbers[4])
print()

# ============================================================
# NO 3: Fungsi len()
# ============================================================
numbers = [10, 5, 7, 2, 1]
print("NO 3 - Fungsi len():")
print("List content:", numbers)
print("Number of elements in list:", len(numbers))
print()

# ============================================================
# NO 4: Menghapus elemen dari list
# ============================================================
numbers = [10, 5, 7, 2, 1]
print("NO 4 - Menghapus elemen dari list:")
print("Original list content:", numbers)
del numbers[1]
print("New list content:", numbers)
print("New list length:", len(numbers))
print()

# ============================================================
# NO 5: Negative index
# ============================================================
numbers = [10, 5, 7, 2, 1]
print("NO 5 - Negative index:")
print("Original list:", numbers)
print("Last element:", numbers[-1])
print("Second to last element:", numbers[-2])
print("Third to last element:", numbers[-3])
print("Fourth to last element:", numbers[-4])
print("Fifth to last element:", numbers[-5])
print()

# ============================================================
# NO 6: Kuis 19
# ============================================================
print("NO 6 - Kuis 19:")
hat_list = [1, 2, 3, 4, 5]
print("Original list:", hat_list)

# Ganti nilai tengah list pakai input user
hat_list[2] = int(input("Enter a number to replace the middle element: "))
print("Updated list:", hat_list)

# Hapus elemen terakhir
del hat_list[-1]
print("List after removing last element:", hat_list)

# Tampilkan panjang dan isi list terbaru
print("List length:", len(hat_list))
print("Final list content:", hat_list)
print()

# ============================================================
# NO 7: Contoh 1 append() dan insert()
# ============================================================
print("NO 7 - Contoh 1 append() dan insert():")
my_list = []

for i in range(5):
    my_list.append(i + 1)

print("List after append:", my_list)

my_list.insert(0, 0)
print("List after insert(0, 0):", my_list)

my_list.insert(-1, 6)
print("List after insert(-1, 6):", my_list)

print("List length:", len(my_list))
print()

# ============================================================
# NO 8: Contoh 2 (Code1)
# ============================================================
print("NO 8 - Contoh 2 (Code1):")
my_list = []

for i in range(5):
    my_list.append(i + 1)

print("List content:", my_list)
print()

# ============================================================
# NO 9: Contoh 2 (Code2)
# ============================================================
print("NO 9 - Contoh 2 (Code2):")
my_list = []

for i in range(5):
    my_list.insert(0, i + 1)

print("List content:", my_list)
print()

# ============================================================
# NO 10: Menggunakan list (Code1)
# ============================================================
print("NO 10 - Menggunakan list (Code1):")
my_list = [10, 1, 8, 3, 5]
print("Original list:", my_list)

total = 0

for i in range(len(my_list)):
    total += my_list[i]

print("Total:", total)
print()

# ============================================================
# NO 11: Menggunakan list (Code2)
# ============================================================
print("NO 11 - Menggunakan list (Code2):")
my_list = [10, 1, 8, 3, 5]
print("Original list:", my_list)

total = 0

for i in my_list:
    total += i

print("Total:", total)
print()

# ============================================================
# NO 12: List in action 2 (swap)
# ============================================================
print("NO 12 - List in action 2 (swap):")
my_list = [10, 1, 8, 3, 5]
print("Original list:", my_list)

length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print("Reversed list:", my_list)
print()

# ============================================================
# NO 13: Kuis 20
# ============================================================
print("NO 13 - Kuis 20:")

# Langkah 1: Buatlah sebuah list kosong dengan nama exo
exo = []
print("Langkah 1:", exo)

# Langkah 2: Gunakan method append() untuk menambahkan anggota: Suho, Kai, Chanyeol dan Sehun
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
print("Langkah 2:", exo)

# Langkah 3: Gunakan for untuk menambahkan anggota: DO, Baekhyun, Kris, Lay, Luhan, Tao, dan Chen
anggota_baru = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for anggota in anggota_baru:
    exo.append(anggota)
print("Langkah 3:", exo)

# Langkah 4: Hapuslah anggota: Kris, Luhan dan Tao
exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")
print("Langkah 4:", exo)

# Langkah 5: Gunakan method insert() untuk menambahkan anggota Xiumin pada elemen ketiga dari terakhir
exo.insert(-2, "Xiumin")
print("Langkah 5:", exo)
print("Jumlah anggota exo:", len(exo))
