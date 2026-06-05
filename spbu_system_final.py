
# spbu_system_final.py
import os
import json
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class SPBUSystem:
    def __init__(self):
        self.harga_bbm = {
            "premium": 8000,
            "pertalite": 10000,
            "pertamax": 14000,
            "solar": 6800,
            "dexlite": 12500
        }

        self.stok_bbm = {
            "premium": 1000,
            "pertalite": 1000,
            "pertamax": 800,
            "solar": 1200,
            "dexlite": 600
        }

        self.posisi = {
            "pos1": {"nama": "Pompa Premium", "status": "Aktif"},
            "pos2": {"nama": "Pompa Pertalite", "status": "Aktif"},
            "pos3": {"nama": "Pompa Pertamax", "status": "Aktif"},
            "pos4": {"nama": "Pompa Solar", "status": "Aktif"},
            "pos5": {"nama": "Pompa Dexlite", "status": "Aktif"}
        }

        self.transaksi = []
        self.histori_stok = []
        self.histori_pompa = []
        self.histori_harga = []

        self.petugas_aktif = "Admin SPBU"
        self.load_data()

    def load_data(self):
        try:
            if os.path.exists("spbu_data.json"):
                with open("spbu_data.json", "r", encoding="utf-8") as f:
                    data = json.load(f)

                self.stok_bbm = data.get("stok_bbm", self.stok_bbm)
                self.harga_bbm = data.get("harga_bbm", self.harga_bbm)
                self.transaksi = data.get("transaksi", [])
                self.posisi = data.get("posisi", self.posisi)
                self.histori_stok = data.get("histori_stok", [])
                self.histori_pompa = data.get("histori_pompa", [])
                self.histori_harga = data.get("histori_harga", [])
        except Exception as e:
            print("Gagal memuat data:", e)

    def save_data(self):
        data = {
            "stok_bbm": self.stok_bbm,
            "harga_bbm": self.harga_bbm,
            "transaksi": self.transaksi,
            "posisi": self.posisi,
            "histori_stok": self.histori_stok,
            "histori_pompa": self.histori_pompa,
            "histori_harga": self.histori_harga,
            "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        with open("spbu_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def tampilkan_menu_utama(self):
        clear()
        print("=== SISTEM ADMINISTRASI SPBU ===")
        print(f"Petugas : {self.petugas_aktif}")
        print("1. Input Transaksi")
        print("2. Kelola Harga BBM")
        print("3. Kelola Stok")
        print("4. Kelola Posisi Pompa")
        print("5. Laporan Transaksi")
        print("6. Lihat Stok & Status")
        print("7. Histori Sistem")
        print("0. Keluar")

    def input_transaksi(self):
        clear()

        for i, (pos, info) in enumerate(self.posisi.items(), 1):
            print(f"{i}. {info['nama']} - {info['status']}")

        try:
            pos_index = int(input("Pilih Pompa: ")) - 1
            posisi = list(self.posisi.keys())[pos_index]

            if self.posisi[posisi]["status"] != "Aktif":
                print("Pompa tidak aktif.")
                input()
                return
        except:
            return

        print("\nJenis BBM")
        for i, bbm in enumerate(self.harga_bbm.keys(), 1):
            print(f"{i}. {bbm.capitalize()}")

        try:
            pilih = int(input("Pilih BBM: ")) - 1
            jenis = list(self.harga_bbm.keys())[pilih]

            liter = float(input("Jumlah liter: "))

            if liter <= 0:
                print("Liter harus lebih dari 0.")
                input()
                return

            if liter > self.stok_bbm[jenis]:
                print("Stok tidak cukup.")
                input()
                return

        except:
            return

        total = int(liter * self.harga_bbm[jenis])

        self.stok_bbm[jenis] -= liter

        trx = {
            "id": len(self.transaksi) + 1,
            "jenis": jenis,
            "liter": liter,
            "total": total,
            "posisi": posisi,
            "petugas": self.petugas_aktif,
            "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.transaksi.append(trx)
        self.save_data()

        print("\n=== STRUK ===")
        print("BBM :", jenis)
        print("Liter :", liter)
        print("Total : Rp{:,.0f}".format(total))

        input("\nEnter...")

    def upgrade_harga(self):
        clear()

        for i, (bbm, harga) in enumerate(self.harga_bbm.items(), 1):
            print(f"{i}. {bbm.capitalize()} - Rp{harga:,}")

        try:
            pilih = int(input("Pilih BBM: ")) - 1
            bbm = list(self.harga_bbm.keys())[pilih]

            harga_lama = self.harga_bbm[bbm]
            harga_baru = int(input("Harga Baru: "))

            if harga_baru <= 0:
                return

            self.harga_bbm[bbm] = harga_baru

            self.histori_harga.append({
                "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "jenis": bbm,
                "harga_lama": harga_lama,
                "harga_baru": harga_baru
            })

            self.save_data()

        except:
            pass

    def kelola_stok(self):
        clear()

        print("1. Tambah Stok")
        print("2. Lihat Stok")

        pilih = input("Pilih: ")

        if pilih == "1":
            print("\nPilih BBM")

            for i, bbm in enumerate(self.stok_bbm.keys(), 1):
                print(f"{i}. {bbm.capitalize()}")

            try:
                idx = int(input("Pilih: ")) - 1
                bbm = list(self.stok_bbm.keys())[idx]

                tambah = float(input("Jumlah tambah (L): "))

                if tambah <= 0:
                    print("Jumlah harus > 0")
                    input()
                    return

                sebelum = self.stok_bbm[bbm]
                self.stok_bbm[bbm] += tambah

                self.histori_stok.append({
                    "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "jenis": bbm,
                    "stok_awal": sebelum,
                    "tambah": tambah,
                    "stok_akhir": self.stok_bbm[bbm]
                })

                self.save_data()

                print("Stok berhasil ditambahkan.")

            except:
                print("Input salah.")

            input()

        elif pilih == "2":
            self.lihat_stok_status()

    def kelola_posisi(self):
        clear()

        for i, (pos, info) in enumerate(self.posisi.items(), 1):
            print(f"{i}. {info['nama']} - {info['status']}")

        try:
            pilih = int(input("Pilih pompa: ")) - 1
            posisi = list(self.posisi.keys())[pilih]

            lama = self.posisi[posisi]["status"]
            baru = "Nonaktif" if lama == "Aktif" else "Aktif"

            self.posisi[posisi]["status"] = baru

            self.histori_pompa.append({
                "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "pompa": self.posisi[posisi]["nama"],
                "status_lama": lama,
                "status_baru": baru
            })

            self.save_data()

        except:
            pass

    def lihat_laporan_lengkap(self):
        clear()

        total = sum(t["total"] for t in self.transaksi)

        print("=== LAPORAN ===")
        print("Total Pendapatan : Rp{:,.0f}".format(total))
        print("Jumlah Transaksi :", len(self.transaksi))

        for t in self.transaksi[-20:]:
            print(f"{t['id']} | {t['jenis']} | {t['liter']}L | Rp{t['total']:,}")

        input("\nEnter...")

    def lihat_stok_status(self):
        clear()

        for bbm in self.harga_bbm:
            print(
                f"{bbm.capitalize():12} "
                f"Stok:{self.stok_bbm[bbm]:.0f}L "
                f"Harga:Rp{self.harga_bbm[bbm]:,}"
            )

        print("\nStatus Pompa")
        for _, info in self.posisi.items():
            print(f"{info['nama']} - {info['status']}")

        input("\nEnter...")

    def lihat_histori(self):
        clear()

        print("=== HISTORI STOK ===")
        for h in self.histori_stok[-10:]:
            print(h)

        print("\n=== HISTORI POMPA ===")
        for h in self.histori_pompa[-10:]:
            print(h)

        print("\n=== HISTORI HARGA ===")
        for h in self.histori_harga[-10:]:
            print(h)

        input("\nEnter...")

    def run(self):
        while True:
            self.tampilkan_menu_utama()

            pilih = input("Pilih menu: ")

            if pilih == "1":
                self.input_transaksi()
            elif pilih == "2":
                self.upgrade_harga()
            elif pilih == "3":
                self.kelola_stok()
            elif pilih == "4":
                self.kelola_posisi()
            elif pilih == "5":
                self.lihat_laporan_lengkap()
            elif pilih == "6":
                self.lihat_stok_status()
            elif pilih == "7":
                self.lihat_histori()
            elif pilih == "0":
                self.save_data()
                break

if __name__ == "__main__":
    SPBUSystem().run()
