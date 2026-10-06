# Sistem Pemesanan Lapangan Bulutangkis Samarinda

Dokumentasi ini berisi penjelasan program, struktur class, serta panduan pengujian untuk sistem pemesanan lapangan bulutangkis. Program ini dibangun menggunakan bahasa pemrograman Python dengan menerapkan prinsip *Object-Oriented Programming* (OOP) lanjutan yang mencakup Relasi UML (Asosiasi, Agregasi, Komposisi) serta Pewarisan (*Inheritance*).

---

## 1. Penjelasan Program

Program ini dirancang untuk menyimulasikan pendataan pemain, petugas GOR, informasi lapangan, dan transaksi pemesanan lapangan bulutangkis. Pada versi ini, program berfokus pada pemisahan hak akses menggunakan konsep pewarisan (Superclass dan Subclass) serta menghubungkan objek-objek class melalui relasi UML agar dapat saling berinteraksi secara dinamis.

---

## 2. Struktur Class

Program ini terdiri dari beberapa class yang saling terhubung melalui relasi dan pewarisan:

### A. Superclass `Pengguna`
Merupakan class induk yang menyimpan informasi dasar entitas pengguna di dalam sistem.
- **Atribut Protected:**
  * `_nama`: Nama pengguna (Dapat diakses langsung oleh subclass).
  * `_no_hp`: Nomor handphone (Dapat diakses langsung oleh subclass).
- **Atribut Private:**
  * `__id_sistem`: ID internal pengguna (Eksklusif hanya milik superclass).
- **Method:**
  * `tampilkan_info()` (*Instance Method*): Menampilkan data dasar pengguna.

---

### B. Subclass `Pemain` dan `Petugas`
Merupakan class turunan (*child class*) dari `Pengguna` yang mengimplementasikan pemanggilan `super()`.

**1. Class `Pemain`**
- **Atribut Kelas:** `komunitas`, `diskon_member`, `total_pemain`.
- **Atribut Instance:**
  * `kategori_member`: Atribut unik subclass pemain (misal: VIP, Reguler).
  * `__saldo`: Saldo pengguna (Private, default 0).
- **Method:**
  * `tampilkan_info()` (*Method Overriding*): Mendefinisikan ulang fungsi induk untuk mencetak profil beserta saldo.
  * `top_up(mesin, jumlah)` (*Relasi Asosiasi*): Meminjam objek `MesinPembayaran` secara sementara untuk menambah saldo.
- **Property (Getter & Setter):** Mengambil dan memvalidasi nilai `saldo` agar tidak negatif.

**2. Class `Petugas`**
- **Atribut Instance:**
  * `shift_kerja`: Atribut unik subclass petugas (misal: Pagi, Malam).
- **Method:**
  * `tampilkan_info()` (*Method Overriding*): Mendefinisikan ulang fungsi induk untuk mencetak profil beserta shift kerja.

---

### C. Class `Lapangan`
Menyimpan informasi fasilitas arena bulutangkis secara mandiri.
- **Atribut Kelas:** `kota`, `jam_operasional`, `total_lapangan`.
- **Atribut Instance:** `kode`, `jenis`, `__harga`.
- **Method:** `info()`, `ubah_jam()`, `validasi_kode()`.
- **Property (Getter & Setter):** Mengambil dan memvalidasi nilai `harga` agar tidak negatif.

---

### D. Class `Pemesanan` (Agregasi & Komposisi)
Menangani pencatatan transaksi dengan menggabungkan beberapa objek.
- **Atribut Kelas:** `prefix_id`, `mata_uang`, `total_transaksi`.
- **Atribut Instance:**
  * `pemain` & `lapangan` (*Relasi Agregasi*): Menampung objek Pemain dan Lapangan dari luar. Jika pemesanan dihapus, pemain dan lapangan tetap ada.
  * `struk` (*Relasi Komposisi*): Menampung objek `StrukTransaksi`.
  * `__durasi`: Lama sewa dalam jam (Private).
- **Method:**
  * `proses_pesanan()` (*Instance Method*): Mengalkulasi biaya, memotong saldo, dan menciptakan objek `StrukTransaksi` secara mutlak di dalam pemesanan.
  * `cetak_struk_sewa()` (*Instance Method*): Menampilkan bukti transaksi.
- **Property (Getter & Setter):** Mengambil dan memvalidasi nilai `durasi`.

---

### E. Class Pendukung
- **Class `MesinPembayaran`:** Digunakan untuk memproses transaksi. Terhubung dengan class `Pemain` melalui relasi *Asosiasi* (penggunaan sementara).
- **Class `StrukTransaksi`:** Digunakan untuk mencetak rincian biaya. Terhubung dengan class `Pemesanan` melalui relasi *Komposisi* (diciptakan dan bergantung sepenuhnya pada pemesanan).

---

## 3. Panduan Pengujian Program

Pengujian program dilakukan secara berurutan di dalam blok `if __name__ == "__main__":`. Berikut adalah skenario yang dijalankan:

1. **Uji Coba Inheritance (Superclass & Subclass):**
   * Pembuatan objek `pemain1`, `pemain2`, dan `petugas1`.
   * Pemanggilan method `tampilkan_info()` untuk membuktikan bahwa *Method Overriding* pada masing-masing subclass berjalan dengan format yang berbeda.

2. **Uji Coba Relasi Asosiasi:**
   * Pembuatan objek `mesin_edc` dari class `MesinPembayaran`.
   * Class `Pemain` menggunakan objek `mesin_edc` untuk melakukan top-up saldo sebesar Rp200.000.

3. **Setup Class Lapangan:**
   * Pembuatan objek `lapangan1` dengan harga sewa Rp50.000 per jam.

4. **Uji Coba Relasi Agregasi & Komposisi:**
   * **Agregasi:** Class `Pemesanan` menerima objek `pemain1` dan `lapangan1` sebagai bagian dari transaksinya.
   * **Komposisi:** Pemanggilan `proses_pesanan()` dilakukan. Sistem secara otomatis memotong saldo pemain dan menciptakan objek `StrukTransaksi` di dalam pesanan tersebut.
   * Pemanggilan `cetak_struk_sewa()` untuk mencetak hasil akhir beserta sisa saldo pemain.

---

## 4. Cara Menjalankan Program

1. Buka terminal atau *command prompt*.
2. Arahkan direktori ke lokasi file Python disimpan.
3. Eksekusi file program utama dengan perintah:
   ```bash
   python posttest2_2509106077_DoniJulianto.py