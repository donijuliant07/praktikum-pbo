# Sistem Pemesanan Lapangan Bulutangkis Samarinda

Dokumentasi ini berisi penjelasan program, struktur class, serta panduan pengujian untuk sistem pemesanan lapangan bulutangkis. Program ini dibangun menggunakan bahasa pemrograman Python dengan menerapkan prinsip *Object-Oriented Programming* (OOP) dasar yang mencakup Class & Object, Atribut & Method, serta Encapsulation & Property.

---

## 1. Penjelasan Program

Program ini dirancang untuk menyimulasikan pendataan pemain, informasi lapangan, dan transaksi pemesanan lapangan bulutangkis. Program berfokus pada pengamanan data menggunakan mekanisme enkapsulasi (getter dan setter) untuk memastikan input data seperti saldo, harga, dan durasi bernilai valid sebelum disimpan ke dalam sistem.

---

## 2. Struktur Class

Program ini terdiri dari **3 class utama** yang berdiri sendiri tanpa pewarisan:

### A. Class `Pemain`
Mengelola data identitas dan saldo e-wallet pengguna.
* **Atribut Kelas:**
  * `komunitas`: Nama komunitas default ("PB Samarinda").
  * `diskon_member`: Persentase diskon (10).
  * `total_pemain`: Menghitung jumlah objek pemain yang dibuat.
* **Atribut Instance:**
  * `nama`: Nama pengguna.
  * `no_hp`: Nomor handphone pengguna.
  * `__saldo`: Saldo pengguna (Private, default 0).
* **Method:**
  * `tampilkan_info()` (*Instance Method*): Menampilkan profil dan saldo pemain.
  * `dari_string(cls, data)` (*Class Method*): Membuat objek pemain dari string berformat `"Nama-NoHP"`.
  * `cek_nomor(no_hp)` (*Static Method*): Memastikan nomor HP diawali dengan `"08"`.
* **Property (Getter & Setter):**
  * `@property def saldo`: Mengambil nilai saldo.
  * `@saldo.setter`: Memperbarui nilai saldo dengan validasi (menolak dan mencetak peringatan jika input $< 0$).

---

### B. Class `Lapangan`
Menyimpan informasi fasilitas arena bulutangkis.
* **Atribut Kelas:**
  * `kota`: Lokasi GOR ("Samarinda").
  * `jam_operasional`: Waktu operasional ("08:00 - 23:00").
  * `total_lapangan`: Menghitung total lapangan yang terdaftar.
* **Atribut Instance:**
  * `kode`: Kode lapangan (misal: "L01").
  * `jenis`: Tipe lantai lapangan (misal: "Karpet Vinyl").
  * `__harga`: Harga sewa per jam (Private, default 0).
* **Method:**
  * `info()` (*Instance Method*): Menampilkan detail kode, jenis, dan harga lapangan.
  * `ubah_jam(cls, jam_baru)` (*Class Method*): Memperbarui jam operasional secara global.
  * `validasi_kode(kode)` (*Static Method*): Mengecek apakah panjang kode lapangan minimal 3 karakter.
* **Property (Getter & Setter):**
  * `@property def harga`: Mengambil nilai harga.
  * `@harga.setter`: Memperbarui nilai harga dengan validasi (menolak dan mencetak peringatan jika input $< 0$).

---

### C. Class `Pemesanan`
Menangani pencatatan transaksi sewa lapangan.
* **Atribut Kelas:**
  * `prefix_id`: Awalan nomor struk ("TRX").
  * `mata_uang`: Satuan mata uang ("IDR").
  * `total_transaksi`: Menghitung total transaksi pemesanan.
* **Atribut Instance:**
  * `nama_pemesan`: Nama pemain yang melakukan pemesanan.
  * `kode_lapangan`: Kode lapangan yang disewa.
  * `__durasi`: Lama sewa dalam jam (Private, default 0).
* **Method:**
  * `cetak_struk()` (*Instance Method*): Menampilkan bukti transaksi penyewaan.
  * `ubah_prefix(cls, prefix_baru)` (*Class Method*): Mengubah awalan ID transaksi secara global.
  * `hitung_biaya_estimasi(harga_per_jam, jam)` (*Static Method*): Menghitung perkiraan total biaya.
* **Property (Getter & Setter):**
  * `@property def durasi`: Mengambil nilai durasi.
  * `@durasi.setter`: Memperbarui durasi sewa dengan validasi (menolak dan mencetak peringatan jika input $\le 0$).

---

## 3. Panduan Pengujian Program

Pengujian program dilakukan secara berurutan di dalam blok `if __name__ == "__main__":`. Berikut adalah skenario yang dijalankan:

1. **Uji Coba Class Pemain:**
   * Pembuatan 2 objek: `pemain1` menggunakan inisialisasi standar, `pemain2` menggunakan *class method* `dari_string`.
   * Uji *setter* valid: Pengisian saldo `pemain1` sebesar 200000 berhasil.
   * Uji *setter* invalid: Pengisian saldo `pemain2` sebesar -50000 ditolak dan memunculkan peringatan.
   * Pemanggilan *instance method* `tampilkan_info()` dan *static method* `cek_nomor()`.

2. **Uji Coba Class Lapangan:**
   * Pembuatan 2 objek: `lapangan1` dan `lapangan2`.
   * Uji *setter* valid: Pengisian harga `lapangan1` sebesar 50000 berhasil.
   * Uji *setter* invalid: Pengisian harga `lapangan2` sebesar -10000 ditolak dan memunculkan peringatan.
   * Pemanggilan *instance method* `info()`, *class method* `ubah_jam()`, dan *static method* `validasi_kode()`.

3. **Uji Coba Class Pemesanan:**
   * Pembuatan 2 objek pesanan yang menghubungkan nama pemain dan kode lapangan.
   * Uji *setter* valid: Durasi `pesanan1` diset 2 jam.
   * Uji *setter* invalid: Durasi `pesanan2` diset 0 jam (ditolak dan memunculkan peringatan).
   * Pemanggilan *instance method* `cetak_struk()`, *class method* `ubah_prefix()` (mengubah TRX menjadi BOOK), dan perhitungan biaya melalui *static method* `hitung_biaya_estimasi()`.

---

## 4. Cara Menjalankan Program

1. Buka terminal atau *command prompt*.
2. Arahkan direktori ke lokasi file Python disimpan.
3. Eksekusi file program utama dengan perintah:
   ```bash
    python posttest1_2509106077_DoniJulianto.py