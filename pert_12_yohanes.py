# =========================================
# 1. VARIABLE LOCAL
# Variable yang berada di dalam fungsi
# =========================================

def fungsi():
    x = 10
    print("Nilai x =", x)

fungsi()


# =========================================
# 2. VARIABLE DI LUAR FUNGSI - 1
# =========================================

x = 20

def tampil():
    print("Nilai x =", x)

tampil()


# =========================================
# 3. VARIABLE DI LUAR FUNGSI - 2
# =========================================

x = 100

def fungsi():
    x = 50
    print("Di dalam fungsi =", x)

fungsi()
print("Di luar fungsi =", x)


# =========================================
# 4. VARIABLE GLOBAL DENGAN KEYWORD GLOBAL
# =========================================

counter = 0

def tambah():
    global counter
    counter += 1

tambah()
tambah()

print("Counter =", counter)


# =========================================
# 5. KUIS IMT
# =========================================

def hitung_imt(berat, tinggi):
    return berat / (tinggi ** 2)

imt = hitung_imt(65, 1.70)

print("IMT =", round(imt, 2))


# =========================================
# 6. FUNGSI SEGITIGA - 1
# =========================================

def segitiga(baris):
    for i in range(1, baris + 1):
        print("*" * i)

segitiga(5)


# =========================================
# 7. FUNGSI SEGITIGA - 2
# =========================================

def segitiga_terbalik(baris):
    for i in range(baris, 0, -1):
        print("*" * i)

segitiga_terbalik(5)


# =========================================
# 8. FUNGSI SEGITIGA - 3
# =========================================

def segitiga_tengah(baris):
    for i in range(1, baris + 1):
        print(" " * (baris - i) + "*" * (2 * i - 1))

segitiga_tengah(5)


# =========================================
# 9. KUIS FAKTORIAL
# =========================================

def faktorial(n):
    hasil = 1

    for i in range(1, n + 1):
        hasil *= i

    return hasil

print("5! =", faktorial(5))


# =========================================
# 10. KUIS FIBONACCI
# =========================================

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

print("Deret Fibonacci:")
fibonacci(10)
print()


# =========================================
# 11. REKURSIF FAKTORIAL
# =========================================

def faktorial_rekursif(n):
    if n == 0 or n == 1:
        return 1

    return n * faktorial_rekursif(n - 1)

print("5! =", faktorial_rekursif(5))


# =========================================
# 12. REKURSIF FIBONACCI
# =========================================

def fibonacci_rekursif(n):
    if n <= 1:
        return n

    return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)

print("Fibonacci ke-10 =", fibonacci_rekursif(10))