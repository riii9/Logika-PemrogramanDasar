# Mendefinisikan fungsi bernama soal1 untuk mengecek validitas tanggal
def soal1():
    # Menampilkan teks header untuk soal nomor 1
    print("\n--- Soal nomor 1 (cek tanggal)---")
    # Meminta input tanggal dari user, mengubahnya ke tipe data integer, lalu menyimpannya ke variabel tanggal
    tanggal = int(input("Masukan tanggal: "))
    # Meminta input bulan dari user, mengubahnya ke tipe data integer, lalu menyimpannya ke variabel bulan
    bulan = int(input("Masukan bulan (bulan ke): "))
    # Meminta input tahun dari user, mengubahnya ke tipe data integer, lalu menyimpannya ke variabel tahun
    tahun = int(input("Masukan tahun: "))

    # Melakukan pengecekan apakah bulan kurang dari 1 atau lebih dari 12
    if bulan < 1 or bulan > 12:
        # Menampilkan pesan bahwa bulan tidak valid jika syarat di atas terpenuhi
        print("Bulan tidak valid")
        # Menghentikan fungsi dan keluar lebih awal jika bulan salah
        return
    # Mengecek apakah tahun habis dibagi 4 untuk menentukan tahun kabisat (True/False)
    is_kabisat = (tahun % 4 == 0)
    # Memeriksa apakah bulan yang dimasukkan adalah bulan Februari (bulan ke-2)
    if bulan == 2:
        # Menentukan max hari 29 jika kabisat, atau 28 jika bukan kabisat
        max_hari = 29 if is_kabisat else 28
    # Memeriksa apakah bulan termasuk dalam daftar bulan yang memiliki 31 hari
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        # Menetapkan nilai max_hari menjadi 31
        max_hari = 31
    # Jika bukan Februari dan bukan bulan 31 hari, maka masuk ke blok ini (bulan 30 hari)
    else:
        # Menetapkan nilai max_hari menjadi 30
        max_hari = 30
    # Mengecek apakah tanggal berada di antara 1 dan max_hari yang sudah ditentukan
    if 1 <= tanggal <= max_hari:
        # Menampilkan pesan jika tanggal valid dan sesuai
        print("Tanggal valid")
    # Jika tanggal di luar rentang max_hari atau kurang dari 1
    else:
        # Menampilkan pesan bahwa tanggal tidak valid
        print("Tanggal tidak valid")

# Mendefinisikan fungsi bernama soal2 untuk mengecek rentang angka dan sifat ganjil/genapnya
def soal2():
    # Menampilkan teks header untuk soal nomor 2
    print("\n--- Soal nomor 2(cek rentang angka)---")
    # Meminta input angka dari user, mengubahnya ke integer, dan menyimpannya ke variabel angka
    angka = int(input("Masukan angka: "))

    # Mengecek apakah angka berada di rentang 10 sampai 20 menggunakan operator logika
    if 10 <= angka & angka <= 20:
        # Jika berada di rentang, cek apakah angka tersebut habis dibagi 2 (genap)
        if angka % 2 == 0:
            # Menampilkan pesan jika angka merupakan bilangan genap di rentang 10-20
            print("Bilangan Genap di Rentang 10-20")
        # Jika tidak habis dibagi 2 (berarti ganjil)
        else:
            # Menampilkan pesan jika angka merupakan bilangan ganjil di rentang 10-20
            print("Bilangan Ganjil di Rentang 10-20")
    # Jika angka berada di luar rentang 10 sampai 20
    else:
        # Menampilkan pesan bahwa angka berada di luar rentang
        print("Di Luar Rentang") 


# Mendefinisikan fungsi bernama soal3 untuk menghitung biaya listrik berdasarkan besaran kWh
def soal3():
    # Menampilkan teks header untuk soal nomor 3
    print("\n--- Soal nomor 3(hitung biaya kwh)---")
    # Meminta input besaran kWh dari user, mengubah ke integer, dan menyimpannya ke variabel kWh
    kWh = int(input("Masukan kWh: "))

    # Mengecek apakah input kWh bernilai negatif (tidak valid)
    if kWh < 0:
        # Menampilkan pesan error jika kWh kurang dari 0
        print("kWh tidak valid!")
    # Mengecek apakah pemakaian kWh kurang dari atau sama dengan 100
    elif kWh <= 100:
        # Menghitung biaya dengan mengalikan 500 dengan jumlah kWh
        biaya = 500 * kWh
        # Menampilkan total biaya yang sudah diformat dengan pemisah ribuan
        print(f"Total biaya: Rp {biaya:,}")
    # Mengecek apakah pemakaian kWh berada di antara 101 sampai 200
    elif 100 < kWh <= 200:
        # Menghitung biaya bertingkat (100 pertama dikali 500, sisanya dikali 750)
        biaya = (500 * 100) + (750 * (kWh - 100))
        # Menampilkan total biaya yang sudah diformat dengan pemisah ribuan
        print(f"Total biaya: Rp {biaya:,}")
    # Jika pemakaian kWh lebih dari 200
    else:
        # Menghitung biaya bertingkat (100*500 + 100*750 + selebihnya*1000)
        biaya = (500 * 100) + (750 * 100) + (1000 * (kWh - 200))
        # Menampilkan total biaya yang sudah diformat dengan pemisah ribuan
        print(f"Total biaya: Rp {biaya:,}")


# Mendefinisikan fungsi bernama soal4 untuk permainan Batu-Gunting-Kertas
def soal4():
    # Menampilkan teks header untuk soal nomor 4
    print("\n--- Soal nomor 4 (Batu-Gunting-Kertas) ---")
    # Meminta input pilihan pemain 1, menghapus spasi ekstra, dan mengubahnya menjadi huruf kecil
    p1 = input("Pemain 1 (batu/gunting/kertas): ").strip().lower()
    # Meminta input pilihan pemain 2, menghapus spasi ekstra, dan mengubahnya menjadi huruf kecil
    p2 = input("Pemain 2 (batu/gunting/kertas): ").strip().lower()

    # Membuat list yang berisi daftar pilihan yang sah dalam permainan
    pilihan_valid = ["batu", "gunting", "kertas"]
    
    # Mengecek apakah input pemain 1 atau pemain 2 tidak ada di dalam daftar pilihan yang valid
    if p1 not in pilihan_valid or p2 not in pilihan_valid:
        # Menampilkan pesan error jika input salah
        print("Error: Input tidak valid! Harus memasukkan 'batu', 'gunting', atau 'kertas'.")
        # Menghentikan fungsi agar tidak lanjut ke pengecekan pemenang
        return

    # Mengecek apakah pilihan pemain 1 sama persis dengan pemain 2
    if p1 == p2:
        # Menampilkan hasil seri karena pilihan sama
        print("Hasil: Seri")
    # Mengecek kombinasi kondisi di mana pemain 1 memenangkan permainan
    elif (p1 == "batu" and p2 == "gunting") or \
         (p1 == "gunting" and p2 == "kertas") or \
         (p1 == "kertas" and p2 == "batu"):
        # Menampilkan pesan bahwa pemain 1 yang menang
        print("Hasil: Pemain 1 menang")
    # Jika tidak seri dan pemain 1 tidak menang, berarti pemain 2 yang menang
    else:
        # Menampilkan pesan bahwa pemain 2 yang menang
        print("Hasil: Pemain 2 menang")


# Mendefinisikan fungsi bernama soal5 untuk menghitung gaji karyawan beserta uang lembur
def soal5():
    # Menampilkan teks header untuk soal nomor 5
    print("\n--- Soal nomor 5 (Gaji Karyawan & Lembur) ---")
    # Meminta input golongan, menghapus spasi, dan mengubahnya menjadi huruf kapital
    golongan = input("Masukan golongan (A/B/C): ").strip().upper()
    
    # Menentukan besaran gaji pokok jika golongan yang dipilih adalah 'A'
    if golongan == 'A':
        gaji_pokok = 5000000
    # Menentukan besaran gaji pokok jika golongan yang dipilih adalah 'B'
    elif golongan == 'B':
        gaji_pokok = 4000000
    # Menentukan besaran gaji pokok jika golongan yang dipilih adalah 'C'
    elif golongan == 'C':
        gaji_pokok = 3000000
    # Jika golongan yang dimasukkan di luar pilihan A, B, atau C
    else:
        # Menampilkan pesan error golongan tidak valid
        print("Error: Golongan tidak valid!")
        # Menghentikan fungsi
        return
    
    # Blok try-except untuk menangkap error jika input jam lembur bukan angka
    try:
        # Meminta input jumlah jam lembur dan mengubahnya ke tipe data integer
        jam_lembur = int(input("Masukan jumlah jam lembur: "))
        # Mengecek apakah jam lembur bernilai negatif
        if jam_lembur < 0:
            # Menampilkan pesan error jika jam lembur negatif
            print("Error: Jam lembur tidak boleh negatif!")
            # Menghentikan fungsi
            return
    # Menangkap error ValueError jika user menginput huruf/simbol alih-alih angka
    except ValueError:
        # Menampilkan pesan error bahwa input harus berupa angka
        print("Error: Input jam lembur harus berupa angka!")
        # Menghentikan fungsi
        return

    # Mengecek apakah jam lembur kurang dari atau sama dengan 5 jam
    if jam_lembur <= 5:
        # Menghitung total lembur (jam lembur dikali 50.000)
        total_lembur = jam_lembur * 50000
    # Jika jam lembur lebih dari 5 jam
    else:
        # Menghitung total lembur progresif (5 jam pertama dikali 50.000 + sisanya dikali 75.000)
        total_lembur = (5 * 50000) + ((jam_lembur - 5) * 75000)

    # Menghitung total keseluruhan gaji dengan menjumlahkan gaji pokok dan total lembur
    total_gaji = gaji_pokok + total_lembur
    
    # Menampilkan teks header untuk rincian gaji
    print(f"\n--- Rincian Gaji ---")
    # Menampilkan informasi golongan karyawan
    print(f"Golongan    : {golongan}")
    # Menampilkan rincian nominal gaji pokok dengan format pemisah ribuan
    print(f"Gaji Pokok  : Rp {gaji_pokok:,}")
    # Menampilkan rincian nominal total lembur dengan format pemisah ribuan
    print(f"Total Lembur: Rp {total_lembur:,}")
    # Menampilkan rincian nominal total keseluruhan gaji dengan format pemisah ribuan
    print(f"Total Gaji  : Rp {total_gaji:,}")


# Mendefinisikan fungsi main sebagai pusat kendali menu utama program
def main():
    # Membuat perulangan tak terbatas (infinite loop) agar menu terus tampil setelah program selesai dijalankan
    while True:
        # Menampilkan garis pembatas dekoratif menu utama
        print("\n==============================")
        # Menampilkan judul teks menu utama program
        print("MENU UTAMA PROGRAM")
        # Menampilkan garis pembatas dekoratif menu utama
        print("==============================")
        # Menampilkan opsi menu pilihan pertama (Soal 1)
        print("1. Soal 1 (Cek Tanggal)")
        # Menampilkan opsi menu pilihan kedua (Soal 2)
        print("2. Soal 2 (Cek Rentang Angka)")
        # Menampilkan opsi menu pilihan ketiga (Soal 3)
        print("3. Soal 3 (Hitung Biaya kWh)")
        # Menampilkan opsi menu pilihan keempat (Soal 4)
        print("4. Soal 4 (Batu-Gunting-Kertas)")
        # Menampilkan opsi menu pilihan kelima (Soal 5)
        print("5. Soal 5 (Gaji Karyawan & Lembur)")
        
        # Meminta input pilihan menu dari user, mengubahnya ke integer, dan menyimpannya ke variabel opsi
        opsi = int(input("Masukan pilihan soal (1-5): "))

        # Memeriksa jika opsi yang dipilih user bernilai 1
        if opsi == 1:
            # Memanggil fungsi soal1() untuk mengeksekusi kode soal pertama
            soal1()
        # Memeriksa jika opsi yang dipilih user bernilai 2
        elif opsi == 2:
            # Memanggil fungsi soal2() untuk mengeksekusi kode soal kedua
            soal2()
        # Memeriksa jika opsi yang dipilih user bernilai 3
        elif opsi == 3:
            # Memanggil fungsi soal3() untuk mengeksekusi kode soal ketiga
            soal3()
        # Memeriksa jika opsi yang dipilih user bernilai 4
        elif opsi == 4:
            # Memanggil fungsi soal4() untuk mengeksekusi kode soal keempat
            soal4()
        # Memeriksa jika opsi yang dipilih user bernilai 5
        elif opsi == 5:
            # Memanggil fungsi soal5() untuk mengeksekusi kode soal kelima
            soal5()
        # Jika user memasukkan angka selain pilihan 1 sampai 5
        else:
            # Menampilkan pesan peringatan bahwa pilihan tidak valid
            print("Pilihan tidak valid, silakan pilih angka 1-5.")
    

# Memeriksa apakah file Python ini dieksekusi secara langsung oleh interpreter (bukan diimpor sebagai modul)
if __name__ == "__main__":
    # Menjalankan fungsi utama main() agar program interaktif mulai berjalan
    main()