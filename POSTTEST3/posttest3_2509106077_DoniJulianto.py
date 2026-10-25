from abc import ABC, abstractmethod

class QrisPayment:
    def proses_transaksi(self, jumlah):
        print(f"[QRIS] Scan barcode berhasil. Memproses Rp{jumlah:,}...")
        return True

class EdcPayment:
    def proses_transaksi(self, jumlah):
        print(f"[EDC BCA] Gesek kartu berhasil. Memproses Rp{jumlah:,}...")
        return True

def jalankan_pembayaran(metode_bayar, jumlah):
    return metode_bayar.proses_transaksi(jumlah)

class StrukTransaksi:
    def __init__(self, id_struk, total_biaya):
        self.id_struk = id_struk
        self.total_biaya = total_biaya

    def cetak_detail(self):
        return f"Struk: {self.id_struk} | Total Bayar: Rp{self.total_biaya:,}"

class Pengguna(ABC):
    def __init__(self, nama, no_hp):
        self._nama = nama
        self._no_hp = no_hp
        self.__id_sistem = id(self)

    @abstractmethod
    def tampilkan_info(self):
        pass

    @abstractmethod
    def hitung_diskon(self, total_harga):
        pass

    def sapa_sistem(self):
        print(f"Sistem: Halo {self._nama}, selamat datang di aplikasi pemesanan!")

class Pemain(Pengguna):
    komunitas = "PB Samarinda"
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
        if jumlah >= 0:
            self.__saldo = jumlah

    def top_up(self, mesin, jumlah):
        if jalankan_pembayaran(mesin, jumlah):
            self.saldo += jumlah
            print(f"Top-up Sukses! Saldo bertambah menjadi Rp{self.saldo:,}")

    def tampilkan_info(self):
        return f"[PEMAIN - {self.kategori_member}] {self._nama} ({self._no_hp}) | Saldo: Rp{self.saldo:,}"

    def hitung_diskon(self, total_harga):
        if self.kategori_member.upper() == "VIP":
            return total_harga * 0.10
        return 0

class Petugas(Pengguna):
    def __init__(self, nama, no_hp, shift_kerja):
        super().__init__(nama, no_hp)
        self.shift_kerja = shift_kerja

    def tampilkan_info(self):
        return f"[PETUGAS - Shift {self.shift_kerja}] {self._nama} ({self._no_hp})"

    def hitung_diskon(self, total_harga):
        return total_harga * 0.50

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
        self.__harga = nilai if nilai >= 0 else 0

    def __str__(self):
        return f"[{self.kode}] Lapangan {self.jenis} - Harga: Rp{self.harga:,}/jam"

class Pemesanan:
    prefix_id = "TRX"
    total_transaksi = 0

    def __init__(self, pengguna, lapangan):
        self.pengguna = pengguna
        self.lapangan = lapangan
        self.__durasi = 0
        self.struk = None 

    @property
    def durasi(self):
        return self.__durasi

    @durasi.setter
    def durasi(self, jam):
        self.__durasi = jam if jam > 0 else 0

    def proses_pesanan(self):
        if self.durasi > 0:
            total_awal = self.lapangan.harga * self.durasi
            potongan = self.pengguna.hitung_diskon(total_awal)
            total_akhir = total_awal - potongan

            Pemesanan.total_transaksi += 1
            id_struk = f"{self.prefix_id}-00{self.total_transaksi}"
            
            self.struk = StrukTransaksi(id_struk, total_akhir)
            
            if isinstance(self.pengguna, Pemain):
                self.pengguna.saldo -= total_akhir
            return True
        return False

    def cetak_struk_sewa(self):
        if self.struk:
            return f"Pesanan a.n {self.pengguna._nama} | {self.lapangan.kode} | Durasi: {self.durasi} jam\n  => {self.struk.cetak_detail()}"
        return "Pemesanan belum diproses!"

if __name__ == "__main__":
    print("=== 1. BUKTI ABSTRAKSI ===")
    try:
        user_anonim = Pengguna("Anonim", "0800112233")
    except TypeError as e:
        print(f"TERTANGKAP ERROR ABSTRAKSI: {e}\n")

    print("=== 2. SETUP DATA & OPERATOR OVERLOADING ===")
    lapangan1 = Lapangan("L01", "Karpet Vinyl")
    lapangan1.harga = 50000
    print(lapangan1)

    print("\n=== 3. POLIMORFISME PEWARISAN ===")
    pemain_vip = Pemain("Doni", "08123456", "VIP")
    petugas_pagi = Petugas("Pak RT", "08111222", "Pagi")
    
    daftar_user = [pemain_vip, petugas_pagi]
    for u in daftar_user:
        u.sapa_sistem()
        print(u.tampilkan_info())
        print("-" * 30)

    print("\n=== 4. DUCK TYPING & ASOSIASI (Top Up) ===")
    qris = QrisPayment()
    edc = EdcPayment()
    pemain_vip.top_up(qris, 200000)
    pemain_vip.top_up(edc, 50000)

    print("\n=== 5. AGREGASI & KOMPOSISI (Proses Pemesanan) ===")
    pesanan_pemain = Pemesanan(pemain_vip, lapangan1)
    pesanan_pemain.durasi = 2
    pesanan_pemain.proses_pesanan()
    print(pesanan_pemain.cetak_struk_sewa())
    print(f"Sisa Saldo {pemain_vip._nama}: Rp{pemain_vip.saldo:,}")

    print("\n-------------------------")
    pesanan_petugas = Pemesanan(petugas_pagi, lapangan1)
    pesanan_petugas.durasi = 2
    pesanan_petugas.proses_pesanan()
    print(pesanan_petugas.cetak_struk_sewa())