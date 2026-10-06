class Pemain:
    komunitas = "PB Samarinda"
    diskon_member = 10
    total_pemain = 0

    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp
        self.__saldo = 0
        Pemain.total_pemain += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, jumlah):
        if jumlah < 0:
            print("Peringatan: Saldo tidak boleh negatif!")
        else:
            self.__saldo = jumlah

    def tampilkan_info(self):
        return f"Pemain: {self.nama} ({self.no_hp}) | Saldo: Rp{self.saldo}"

    @classmethod
    def dari_string(cls, data):
        nama, no_hp = data.split("-")
        return cls(nama, no_hp)

    @staticmethod
    def cek_nomor(no_hp):
        return str(no_hp).startswith("08")


class Lapangan:
    kota = "Samarinda"
    jam_operasional = "08:00 - 23:00"
    total_lapangan = 0

    def __init__(self, kode, jenis):
        self.kode = kode
        self.jenis = jenis
        self.__harga = 0
        Lapangan.total_lapangan += 1

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai):
        if nilai < 0:
            print("Peringatan: Harga tidak boleh negatif!")
        else:
            self.__harga = nilai

    def info(self):
        return f"Lapangan {self.kode} ({self.jenis}) | Harga: Rp{self.harga}/jam"

    @classmethod
    def ubah_jam(cls, jam_baru):
        cls.jam_operasional = jam_baru

    @staticmethod
    def validasi_kode(kode):
        return len(kode) >= 3


class Pemesanan:
    prefix_id = "TRX"
    mata_uang = "IDR"
    total_transaksi = 0

    def __init__(self, nama_pemesan, kode_lapangan):
        self.nama_pemesan = nama_pemesan
        self.kode_lapangan = kode_lapangan
        self.__durasi = 0
        Pemesanan.total_transaksi += 1

    @property
    def durasi(self):
        return self.__durasi

    @durasi.setter
    def durasi(self, jam):
        if jam <= 0:
            print("Peringatan: Durasi harus lebih dari 0 jam!")
        else:
            self.__durasi = jam

    def cetak_struk(self):
        return f"[{Pemesanan.prefix_id}] Pemesan: {self.nama_pemesan} | Lapangan: {self.kode_lapangan} | Durasi: {self.durasi} jam"

    @classmethod
    def ubah_prefix(cls, prefix_baru):
        cls.prefix_id = prefix_baru

    @staticmethod
    def hitung_biaya_estimasi(harga_per_jam, jam):
        return harga_per_jam * jam


if __name__ == "__main__":
    print(" 1. UJI COBA CLASS PEMAIN ")
    pemain1 = Pemain("Doni", "08123456789")
    pemain2 = Pemain.dari_string("Andi-08987654321")

    pemain1.saldo = 200000
    
    pemain2.saldo = -50000

    print(pemain1.tampilkan_info())
    print(pemain2.tampilkan_info())

    print(f"Apakah nomor HP pemain1 valid? {Pemain.cek_nomor(pemain1.no_hp)}")


    print("\n 2. UJI COBA CLASS LAPANGAN ")
    lapangan1 = Lapangan("L01", "Karpet Vinyl")
    lapangan2 = Lapangan("L02", "Lantai Kayu")

    lapangan1.harga = 50000
    
    lapangan2.harga = -10000

    print(lapangan1.info())
    print(lapangan2.info())

    Lapangan.ubah_jam("07:00 - 24:00")
    print(f"Jam operasional terbaru: {Lapangan.jam_operasional}")

    print(f"Apakah kode 'L01' valid? {Lapangan.validasi_kode('L01')}")


    print("\n 3. UJI COBA CLASS PEMESANAN ")
    pesanan1 = Pemesanan(pemain1.nama, lapangan1.kode)
    pesanan2 = Pemesanan(pemain2.nama, lapangan2.kode)

    pesanan1.durasi = 2

    pesanan2.durasi = 0

    print(pesanan1.cetak_struk())
    print(pesanan2.cetak_struk())

    Pemesanan.ubah_prefix("BOOK")
    print(f"Struk setelah ubah prefix: {pesanan1.cetak_struk()}")

    estimasi = Pemesanan.hitung_biaya_estimasi(lapangan1.harga, pesanan1.durasi)
    print(f"Estimasi biaya sewa: Rp{estimasi}")