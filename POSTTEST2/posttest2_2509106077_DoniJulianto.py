class MesinPembayaran:
    def __init__(self, nama_mesin):
        self.nama_mesin = nama_mesin

    def proses_transaksi(self, jumlah):
        print(f"[{self.nama_mesin}] Sedang memproses transaksi Rp{jumlah}...")
        return True

class StrukTransaksi:
    def __init__(self, id_struk, total_biaya):
        self.id_struk = id_struk
        self.total_biaya = total_biaya

    def cetak_detail(self):
        return f"Struk: {self.id_struk} | Total Bayar: Rp{self.total_biaya}"

class Pengguna:
    def __init__(self, nama, no_hp):
        self._nama = nama
        self._no_hp = no_hp
        self.__id_sistem = id(self)

    def tampilkan_info(self):
        return f"Nama: {self._nama} | HP: {self._no_hp}"

class Pemain(Pengguna):
    komunitas = "PB Samarinda"
    diskon_member = 10
    total_pemain = 0

    def __init__(self, nama, no_hp, kategori_member):
        super().__init__(nama, no_hp)
        self.kategori_member = kategori_member
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

    def top_up(self, mesin, jumlah):
        if mesin.proses_transaksi(jumlah):
            self.saldo += jumlah
            print(f"Top-up Sukses! Saldo {self._nama} bertambah menjadi Rp{self.saldo}")

    def tampilkan_info(self):
        return f"[PEMAIN - {self.kategori_member}] {self._nama} ({self._no_hp}) | Saldo: Rp{self.saldo}"

    @classmethod
    def dari_string(cls, data):
        nama, no_hp, kategori = data.split("-")
        return cls(nama, no_hp, kategori)

    @staticmethod
    def cek_nomor(no_hp):
        return str(no_hp).startswith("08")

class Petugas(Pengguna):
    def __init__(self, nama, no_hp, shift_kerja):
        super().__init__(nama, no_hp)
        self.shift_kerja = shift_kerja

    def tampilkan_info(self):
        return f"[PETUGAS - Shift {self.shift_kerja}] {self._nama} ({self._no_hp})"

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

    def __init__(self, pemain, lapangan):
        self.pemain = pemain
        self.lapangan = lapangan
        self.__durasi = 0
        self.struk = None
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

    def proses_pesanan(self):
        if self.durasi > 0:
            total = self.lapangan.harga * self.durasi
            id_struk = f"{Pemesanan.prefix_id}-00{Pemesanan.total_transaksi}"
            self.struk = StrukTransaksi(id_struk, total)
            self.pemain.saldo -= total
            return True
        return False

    def cetak_struk_sewa(self):
        if self.struk:
            return f"[{self.struk.id_struk}] Pemesan: {self.pemain._nama} | Lapangan: {self.lapangan.kode} | Durasi: {self.durasi} jam\n   => {self.struk.cetak_detail()}"
        return "Pemesanan belum diproses!"

    @classmethod
    def ubah_prefix(cls, prefix_baru):
        cls.prefix_id = prefix_baru

    @staticmethod
    def hitung_biaya_estimasi(harga_per_jam, jam):
        return harga_per_jam * jam


if __name__ == "__main__":
    print("=== 1. UJI COBA INHERITANCE (SUPERCLASS & SUBCLASS) ===")
    pemain1 = Pemain("Doni", "08123456789", "Reguler")
    pemain2 = Pemain.dari_string("Andi-08987654321-VIP")
    petugas1 = Petugas("Pak RT", "08111222333", "Pagi")

    print(pemain1.tampilkan_info())
    print(pemain2.tampilkan_info())
    print(petugas1.tampilkan_info())

    print("\n=== 2. UJI COBA RELASI ASOSIASI ===")
    mesin_edc = MesinPembayaran("EDC BCA")
    pemain1.top_up(mesin_edc, 200000)
    pemain2.saldo = 50000 

    print("\n=== 3. SETUP LAPANGAN ===")
    lapangan1 = Lapangan("L01", "Karpet Vinyl")
    lapangan1.harga = 50000
    print(lapangan1.info())

    print("\n=== 4. UJI COBA RELASI AGREGASI & KOMPOSISI ===")
    pesanan1 = Pemesanan(pemain1, lapangan1)
    pesanan1.durasi = 2
    
    pesanan1.proses_pesanan()
    print(pesanan1.cetak_struk_sewa())

    print(f"\nSisa Saldo {pemain1._nama}: Rp{pemain1.saldo}")