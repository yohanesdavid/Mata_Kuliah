# =========================================
# 1. RETURN TANPA EKSPRESI
# Memanggil fungsi tanpa argumen
# =========================================

def fungsi():
    print("Halo dari fungsi")
    return

fungsi()


# =========================================
# 2. RETURN TANPA EKSPRESI
# Memanggil fungsi dengan argumen False
# =========================================

def cek(status):
    if not status:
        return
    print("Status True")

cek(False)


# =========================================
# 3. RETURN DENGAN EKSPRESI
# Menyimpan nilai yang direturn ke variabel
# =========================================

def kuadrat(x):
    return x ** 2

hasil = kuadrat(5)

print("\n3. Return dengan ekspresi")
print("Hasil =", hasil)


# =========================================
# 4. RETURN DENGAN EKSPRESI
# Mengabaikan nilai return
# =========================================

def kali_dua(x):
    return x * 2

kali_dua(10)

print("\n4. Nilai return diabaikan")


# =========================================
# 5. KEYWORD NONE
# =========================================

def contoh_none():
    return None

print("\n5. Keyword None")
print(contoh_none())


# =========================================
# 6. LIST SEBAGAI ARGUMENT DARI FUNGSI
# =========================================

def jumlahkan(data):
    return sum(data)

angka = [1, 2, 3, 4, 5]

print("\n6. List sebagai argument")
print(jumlahkan(angka))


# =========================================
# 7. GANTI ARGUMENT SAAT PEMANGGILAN
# =========================================

print("\n7. Ganti argument")

print(jumlahkan([10, 20, 30]))
print(jumlahkan([5, 5, 5, 5]))


# =========================================
# 8. LIST SEBAGAI HASIL DARI FUNGSI
# =========================================

def buat_list():
    return [10, 20, 30, 40]

print("\n8. List sebagai hasil fungsi")
print(buat_list())


# =========================================
# 9. KUIS 23
# =========================================

def luas_persegi(sisi):
    return sisi * sisi

print("\n9. Kuis 23")
print(luas_persegi(5))


# =========================================
# 10. KUIS 24
# =========================================

def tahun_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    return False

def hari_didalam_bulan(tahun, bulan):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        return 28
    return None

data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]

print("\n10. Kuis 24")

for i in range(len(data_uji)):
    thn = data_uji[i]
    bln = data_bulan[i]

    print(thn, bln, "->", end=" ")

    hasil = hari_didalam_bulan(thn, bln)

    if hasil == data_hasil[i]:
        print("OK")
    else:
        print("Gagal")


# =========================================
# 11. KUIS 25
# =========================================

def tahun_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    return False

def hari_didalam_bulan(tahun, bulan):
    if bulan in [1,3,5,7,8,10,12]:
        return 31
    elif bulan in [4,6,9,11]:
        return 30
    elif bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        return 28
    return None

def hari_pada_tahun(tahun, bulan, hari):
    if bulan < 1 or bulan > 12:
        return None

    jumlah_hari = hari_didalam_bulan(tahun, bulan)

    if hari < 1 or hari > jumlah_hari:
        return None

    total = hari

    for b in range(1, bulan):
        total += hari_didalam_bulan(tahun, b)

    return total

print("\n11. Kuis 25")
print(hari_pada_tahun(2000, 12, 31))


# =========================================
# 12. KUIS 26
# =========================================
def cek_prima(bilangan):
    if bilangan <= 1:
        return False

    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False

    return True


for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")

print()

# =========================================
# 13. KUIS 27
# =========================================
def cek_prima(bilangan):
    if bilangan <= 1:
        return False

    for i in range(2, int(bilangan ** 0.5) + 1):
        if bilangan % i == 0:
            return False

    return True


for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")

print()
# =========================================
# 14. KUIS 28
# =========================================
def Liter100km_ke_mpg(liter):
    mil = 100000 / 1609.344
    galon = liter / 3.785411784
    return mil / galon


def mpg_ke_Liter100km(mil):
    km100 = 100000 / 1609.344
    liter = 3.785411784
    return liter / (mil / km100)


print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.0))

print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))