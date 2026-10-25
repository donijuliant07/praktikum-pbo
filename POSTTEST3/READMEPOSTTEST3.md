# Sistem Pemesanan Lapangan Bulutangkis Samarinda

Dokumentasi ini berisi penjelasan program, struktur class, serta panduan pengujian untuk sistem pemesanan lapangan bulutangkis. Program ini dibangun menggunakan bahasa pemrograman Python dengan menerapkan prinsip *Object-Oriented Programming* (OOP) lanjutan yang mencakup Relasi UML (Asosiasi, Agregasi, Komposisi), Pewarisan (*Inheritance*), Abstraksi, serta Polimorfisme.

---

## 1. Penjelasan Program

Program ini dirancang untuk menyimulasikan pendataan pemain, petugas GOR, informasi lapangan, dan transaksi pemesanan lapangan bulutangkis. Pada versi lanjutan ini, program berfokus pada:
1. Pemisahan hak akses menggunakan konsep pewarisan (Superclass dan Subclass).
2. Penerapan **Abstraksi** menggunakan *Abstract Base Class* (ABC) sebagai fondasi hierarki pengguna.
3. Penerapan **Polimorfisme** untuk membuat perilaku sistem lebih dinamis (Pewarisan, Duck Typing, dan Operator Overloading).
4. Menghubungkan objek-objek class melalui relasi UML agar dapat saling berinteraksi.

---

## 2. Struktur Class

Program ini terdiri dari beberapa class yang saling terhubung:

### A. Superclass Abstrak `Pengguna`
Merupakan class induk (mewarisi modul `ABC`) yang menyimpan informasi dasar entitas pengguna di dalam sistem dan bertindak sebagai *blueprint*.
- **Atribut Protected & Private:** `_nama`, `_no_hp`, `__id_sistem`.
- **Abstract Method:** 
  * `tampilkan_info()`: Wajib diimplementasikan subclass untuk menampilkan data profil.
  * `hitung_diskon(total_harga)`: Wajib diimplementasikan subclass untuk kalkulasi diskon.
- **Concrete Method:** `sapa_sistem()` yang dapat dipanggil langsung oleh semua turunannya.

---

### B. Subclass `Pemain` dan `Petugas`
Merupakan class turunan (*child class*) dari `Pengguna` yang mengimplementasikan metode abstrak induknya.

**1. Class `Pemain`**
- **Atribut:** `kategori_member`, `__saldo` (Private, default 0), `komunitas`, dll.
- **Method (Polimorfisme & Overriding):**
  * `tampilkan_info()`: Mencetak profil beserta saldo.
  * `hitung_diskon()`: Memberikan diskon 10% khusus untuk member VIP.
- **Relasi Asosiasi:** Method `top_up(mesin, jumlah)` meminjam objek pembayaran (via Duck Typing) secara sementara untuk menambah saldo.

**2. Class `Petugas`**
- **Atribut:** `shift_kerja`.
- **Method (Polimorfisme & Overriding):**
  * `tampilkan_info()`: Mencetak profil beserta shift kerja.
  * `hitung_diskon()`: Memberikan diskon spesial karyawan sebesar 50%.

---

### C. Class `Lapangan`
Menyimpan informasi fasilitas arena bulutangkis.
- **Atribut:** `kode`, `jenis`, `__harga`.
- **Polimorfisme (Operator Overloading):** Menggunakan *magic method* `__str__()` agar saat objek lapangan di-*print*, program langsung mengembalikan string terformat `[Kode] Lapangan Jenis - Harga/jam`.

---

### D. Class `Pemesanan` (Agregasi & Komposisi)
Menangani pencatatan transaksi dengan menggabungkan beberapa objek.
- **Relasi Agregasi:** Menampung referensi objek `Pemain/Petugas` dan `Lapangan` dari luar kelas melalui parameter konstruktor.
- **Relasi Komposisi:** Method `proses_pesanan()` menghitung total biaya, lalu menciptakan objek `StrukTransaksi` secara mutlak di dalam pemesanan tersebut.
- **Method:** `cetak_struk_sewa()` untuk menampilkan bukti cetak transaksi.

---

### E. Class Pendukung & Duck Typing
- **Duck Typing (Polimorfisme):** Terdapat class `QrisPayment` dan `EdcPayment`. Keduanya tidak memiliki hubungan hierarki/pewarisan sama sekali, tetapi keduanya memiliki nama method yang sama yaitu `proses_transaksi()`. Keduanya dapat dipanggil secara bergantian oleh satu fungsi eksekusi umum `jalankan_pembayaran()`.
- **Class `StrukTransaksi`:** Digunakan untuk mencetak rincian biaya. Terhubung dengan class `Pemesanan` melalui relasi *Komposisi*.

---

## 3. Konsep Lanjutan: Penerapan Prinsip SOLID
Program ini mengimplementasikan prinsip SOLID:
1. **Open/Closed Principle (OCP)**: Berkat penerapan *Duck Typing* pada fitur pembayaran, kita bisa menambahkan class media pembayaran baru secara tak terbatas (misalnya Transfer Bank) tanpa memodifikasi kode validasi utama.
2. **Single Responsibility Principle (SRP)**: Tanggung jawab mencetak teks struk dipisahkan ke class `StrukTransaksi`, sehingga class `Pemesanan` murni hanya mengurus data transaksinya saja.

---

## 4. Panduan Pengujian Program

Pengujian program dilakukan secara berurutan di dalam blok `if __name__ == "__main__":`

1. **Bukti Abstraksi:** Sistem menggunakan blok `try-except` untuk membuktikan bahwa class `Pengguna` murni tidak bisa diinstansiasi secara langsung dan memicu `TypeError`.
2. **Setup Data & Operator Overloading:** Menyiapkan objek `lapangan1` dan memanggil fungsi `print(lapangan1)` untuk membuktikan magic method `__str__` berjalan.
3. **Polimorfisme Pewarisan:** Melakukan perulangan (`for`) pada list yang berisi objek Pemain dan Petugas untuk membuktikan *method overriding* pada fungsi induk berjalan secara otomatis.
4. **Duck Typing & Asosiasi (Top Up):** Class Pemain menggunakan dua objek pembayaran yang berbeda (`QrisPayment` dan `EdcPayment`) untuk memproses top-up saldo secara asosiasi.
5. **Agregasi & Komposisi:** Sistem membuat dua pesanan (untuk VIP dan Petugas). Membuktikan kalkulasi potongan harga diskon (10% vs 50%) berjalan dengan benar lewat polimorfisme, menciptakan objek struk, memotong saldo, dan mencetak laporan akhir.

---

## 5. Cara Menjalankan Program

1. Buka terminal atau *command prompt*.
2. Arahkan direktori ke lokasi file Python disimpan.
3. Eksekusi file program utama dengan perintah:
   ```bash
   python posttest3_2509106077_DoniJulianto.py