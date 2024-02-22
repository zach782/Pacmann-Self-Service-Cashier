import os
from tabulate import tabulate
os.system("clear")

class Transaction:
    """
    class Transaction digunakan sebagai Template untuk membuat objek id transaksi
    """
    def __init__(self, inputNo=None, inputNamaItem=None, inputJumlah=None, inputHarga=None):
        """
        Fungsi init memiliki atribut objek
        1. no sebagai nomor item dalam tabel
        2. nama sebagai nama item
        3. jumlah sebagai jumlah item yang ingin dibeli
        4. harga sebagai harga per item
        5. total sebagai harga total dari jumlah dikali harga per item
        6. list keranjang untuk menampung identitas barang
        """
        self.no = inputNo
        self.nama = inputNamaItem
        self.jumlah = inputJumlah
        self.harga = inputHarga
        self.total = 0
        self.keranjang = []
    def add_item(self, no, nama, jumlah, harga):
        """
        Fungsi add_item untuk menambahkan nomor tabel, nama item, jumlah item, 
        harga item, harga total kedalam list keranjang, harga total didapat dari
        jumlah item dikali harga per item
        """
        try:
            harga_total = jumlah * harga
            tambah = [no, nama, jumlah, harga, harga_total]
            self.keranjang.append(tambah)
            self.total += harga_total
            print("\nIsi keranjang:")
            headers = ["No", "Nama Barang", "Jumlah", "Harga/Item", "Harga Total"]
            print(tabulate(self.keranjang, headers=headers, tablefmt="grid"))
        except NameError:
            print("Masukkan nama yang valid !!!")
    def update_item_name(self, nama_lama, nama_baru):
        """
        Fungsi update_item_name memiliki paramater nama_lama dan nama_baru,
        nama_lama digunakan untuk mengupdate nama item berdasarkan nama item yang ingin diubah
        dan nama_baru akan digunakan untuk nama terbaru pada list keranjang 
        """
        try:
            item_ditemukan = False
            for indeks, barang in enumerate(self.keranjang):
                if barang[1] == nama_lama:
                    self.keranjang[indeks] = [barang[0],nama_baru, barang[2], barang[3], barang[4]]
                    item_ditemukan = True
            if not item_ditemukan:
                print(f"Item dengan nama '{nama_lama}' tidak ditemukan dalam keranjang.")
            else:
                print("\nIsi keranjang Setelah Nama Item Diubah:")
                headers = ["No", "Nama Barang", "Jumlah", "Harga/Item", "Harga Total"]
                print(tabulate(self.keranjang, headers=headers, tablefmt="grid"))
        except Exception as e:
            print(f"Terjadi kesalahan saat mengubah nama item: {e}")
    def update_item_qty(self, nama_barang, jumlah_baru):
        """
        Fungsi update_item_qty memiliki parameter nama_barang, jumlah_baru 
        digunakan untuk mengubah jumlah item yang ingin dibeli berdasarkan
        nama item yang ingin diubah jumlahnya
        """
        try:
            for index, barang in enumerate(self.keranjang):
                if barang[1] == nama_barang:
                    harga_per_item = barang[3]
                    harga_total_baru = jumlah_baru * harga_per_item
                    selisih_harga = barang[4] - harga_total_baru
                    updated_barang = barang[0], barang[1], jumlah_baru, barang[3], harga_total_baru
                    self.keranjang[index] = updated_barang
                    self.total -= selisih_harga
        except IndexError as e:
            print(f"Terjadi kesalahan indeks: {e}")
        except TypeError as e:
            print(f"Terjadi kesalahan tipe data: {e}")
        print("\nIsi keranjang Setelah Jumlah Diubah:")
        headers = ["No", "Nama Barang", "Jumlah", "Harga/Item", "Harga Total"]
        print(tabulate(self.keranjang, headers=headers, tablefmt="grid"))
        print("")
    def update_item_price(self, nama_barang, harga_baru):
        """
        Fungsi update_item_price memiliki parameter nama_barang, harga_baru 
        digunakan untuk mengubah harga per item yang ingin dibeli berdasarkan
        nama item yang ingin diubah harga per itemnya
        """
        try:
            for indeks, barang in enumerate(self.keranjang):
                if barang[1] == nama_barang:
                    harga_per_item_baru = harga_baru
                    harga_total_baru = harga_per_item_baru * barang[2]
                    selisih_harga = barang[4] - harga_total_baru
                    self.keranjang[indeks] = barang[0], barang[1], barang[2], harga_per_item_baru, harga_total_baru
                    self.total -= selisih_harga
        except IndexError as e:
            print(f"Terjadi kesalahan indeks: {e}")
        except TypeError as e:
            print(f"Terjadi kesalahan tipe data: {e}")
        print("\nIsi keranjang Setelah Harga / Item diubah:")
        headers = ["No", "Nama Barang", "Jumlah", "Harga", "Harga Total"]
        print(tabulate(self.keranjang, headers=headers, tablefmt="grid"))
    def delete_item(self, nama_item):
        """
        Fungsi delete_item memiliki parameter nama_item yang akan digunakan
        untuk menghapus item berdasarkan nama item yang ingin dihapus
        """
        try:
            for barang in self.keranjang:
                if barang[1] == nama_item:
                    self.total -= barang[4]
                    self.keranjang.remove(barang)
                    self.total_price()
        except IndexError as e:
            print(f"Terjadi kesalahan indeks: {e}")
        except TypeError as e:
            print(f"Terjadi kesalahan tipe data: {e}")
        print("\nIsi keranjang Setelah Item dihapus:")
        headers = ["No", "Nama Barang", "Jumlah", "Harga", "Harga Total"]
        print(tabulate(self.keranjang, headers=headers, tablefmt="grid"))
    def reset_transaction(self):
        """
        Fungsi reset_transaction digunakan untuk mereset atau menghapus semua
        item yang sudah dimasukan ke list keranjang mulai dari nomor item, nama item, 
        jumlah, harga/item, harga total
        """
        self.keranjang = []
        self.total = 0
        print("")
        print("Transaction telah di-reset. keranjang kosong.")
        print("Isi keranjang:")
        headers = ["No", "Nama Barang", "Jumlah", "Harga/Item", "Harga Total"]
        print(tabulate(self.keranjang, headers=headers, tablefmt="grid"))
    def check_order(self):
        """
        Fungsi check_order digunakan untuk mengecek identitas item mulai dari
        nama, jumlah, harga per item
        """
        for indeks, barang in enumerate(self.keranjang):
            try:
                if not barang[1]:
                    print(f"Nama barang pada item {indeks + 1} belum diinput.")
                elif not barang[2]:
                    print(f"Jumlah barang pada item {indeks + 1} belum diinput.")
                elif not barang[3]:
                    print(f"Harga barang pada item {indeks + 1} belum diinput.")
                else:
                    print("Semua data pada item", indeks + 1, "telah diinput.")
            except IndexError as e:
                print(f"Item {indeks + 1} tidak lengkap: {e}")
        print("Pengecekan selesai\n")
    def total_price(self):
        """
        Fungsi total_price digunakan untuk melihat total harga dari semua
        item yang akan dibeli, jika total harga memenuhi ketentuan diskon,
        maka total harga akan dapat potongan diskon
        """
        diskon = 0
        total_harga = self.total
        try:
            if total_harga > 500000:
                diskon = 0.1
                print(f"\nAnda Mendapat diskon sebesar 10%,")
            elif total_harga > 300000:
                diskon = 0.08
                print(f"\nAnda Mendapat diskon sebesar 8%,")
            elif total_harga > 200000:
                diskon = 0.05
                print(f"\nAnda Mendapat diskon sebesar 5%,")
            elif total_harga < 200000:
                print("\nAnda Tidak Mendapat Diskon,")

            if diskon > 0:
                total_diskon = total_harga * diskon
                total_harga -= total_diskon
        except IndexError as e:
            print(f"Terjadi kesalahan indeks: {e}")
        except TypeError as e:
            print(f"Terjadi kesalahan tipe data: {e}")
        print("Isi keranjang Total Harga Yang Harus Dibayarkan:")
        headers = ["No", "Nama Barang", "Jumlah", "Harga/Item", "Harga Total"]
        print(tabulate(self.keranjang, headers=headers, tablefmt="grid"))
        print("")
        print(f"Total Belanja Anda Sebesar: Rp {total_harga}")
        print("")
    def menu(self):
        """
        Fungsi menu digunakan sebagai interaksi antara customer
        dan sistem supermarket, customer dapat melakukan berbagai 
        operasi seperti menambahkan item, memperbarui detail item, 
        menghapus item, memeriksa pesanan, dan menghitung total harga
        """
        no = 0
        while True:
            no = no + 1
            print("\n==================Supermarket Andi==================")
            print("\n1. Tambah barang")
            print("2. Ubah Nama Barang")
            print("3. Ubah Jumlah Barang")
            print("4. Ubah Harga / Item")
            print("5. Hapus Data")
            print("6. Reset Data")
            print("7. Cek Order")
            print("8. Cek Total Harga")
            print("9. Keluar\n")
            pilih = int(input("Silahkan pilih Menu 1-9 = "))
            if pilih == 1:
                nama_barang = str(input("masukan nama barang = "))
                jumlah_barang = int(input("masukan jumlah barang = "))
                harga_barang = int(input("masukan harga barang = "))
                self.add_item(no, nama_barang, jumlah_barang, harga_barang)
            elif pilih == 2:
                nama_lama = str(input("masukan nama yang ingin diubah = "))
                nama_baru = str(input("masukan nama baru = "))
                self.update_item_name(nama_lama, nama_baru)
            elif pilih == 3:
                nama_barang = str(input("masukan nama yang ingin diubah = "))
                jumlah_baru = int(input("masukan jumlah baru = "))
                self.update_item_qty(nama_barang, jumlah_baru)
            elif pilih == 4:
                nama_barang = str(input("masukan nama yang ingin diubah = "))
                harga_baru = int(input("masukan harga baru = "))
                self.update_item_price(nama_barang, harga_baru)
            elif pilih == 5:
                nama_barang = str(input("masukan nama yang ingin dihapus = "))
                self.delete_item(nama_barang)
            elif pilih == 6:
                self.reset_transaction()
            elif pilih == 7:
                self.check_order()
            elif pilih == 8:
                self.total_price()
            elif pilih == 9:
                break
            else:
                print("Menu tidak tersedia")

# trnsct_123 = Transaction()
# trnsct_123.menu()
print("Program Selesai\n")