# =========================
# No 1 - Perulangan While Contoh 1
# =========================
while True:
    teks = input("Masukkan teks: ")
    print("Kamu mengetik:", teks)


# =========================
# No 2 - Perulangan While Contoh 2
# =========================
detik = 3

while detik > 0:
    print("Peluncuran dalam", detik)
    detik -= 1

print("Roket diluncurkan!")


# =========================
# No 3 - Ganjil dan Genap dengan While
# =========================
angka = 1

while angka <= 5:
    if angka % 2 == 0:
        print(angka, "Genap")
    else:
        print(angka, "Ganjil")
    angka += 1


# =========================
# No 4 - Kuis 15 (Tebak Angka)
# =========================
secret = 777
tebakan = 0

while tebakan != secret:
    tebakan = int(input("Tebak angka: "))

    if tebakan != secret:
        print("Hahaha! Kamu nyangkut deh di loop saya")
        print("Coba tebak lagi")

print("Selamat, Muggle! Kamu bebas sekarang!")


# =========================
# No 5 - Perulangan For Contoh 1
# =========================
print("a")
for i in range(10):
    print(i)

print("b")
for i in range(2, 8):
    print(i)

print("c")
for i in range(2, 8, 3):
    print(i)

print("d")
for i in range(1, 1):
    print(i)

print("e")
for i in range(2, 1):
    print(i)


# =========================
# No 6 - Eksponensial 2
# =========================
for i in range(11):
    print("2^", i, "=", 2 ** i)


# =========================
# No 7 - Break dan Continue
# =========================
print("BREAK")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("CONTINUE")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# =========================
# No 8 - Kuis 16 (Implementasi Break)
# =========================
while True:
    kata = input("Masukkan kata: ")

    if kata.upper() == "STOP":
        break

    print("Input:", kata)


# =========================
# No 9 - Kuis 17 (Implementasi Continue)
# =========================
teks = input("Masukkan kalimat: ").upper()

for huruf in teks:
    if huruf in "AIUEO":
        continue
    print(huruf)


# =========================
# No 10 - While dengan Else
# =========================
i = 1

while i < 5:
    print(i)
    i += 1
else:
    print(i)


# =========================
# No 11 - For dengan Else
# =========================
for i in range(5):
    print(i)
else:
    print("Loop selesai")


# =========================
# No 12 - Ekspresi Logika
# =========================
p = True
q = False

print(not (p and q))
print((not p) or (not q))

print(not (p or q))
print((not p) and (not q))


# =========================
# No 13 - Logical vs Bitwise
# =========================
a = 5
b = 3

print(a and b)
print(a & b)

print(not a)
print(~a)


# =========================
# No 14 - Binary Shifting
# =========================
angka = 17

print("Ges