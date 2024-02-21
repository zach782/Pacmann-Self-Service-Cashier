


# Latar Belakang Problems
Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana unutk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli, serta fitur yang lain.
Harapan Andi, customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan Programmer untuk membuatkan fitur-fitur agar sistem self-service di supermarket itu bisa berjalan dengan lancar.


# Requirements atau Objectives
### 1. Requirements
Untuk membuat sistem kasir yang self-service, Programmer membutuhkan beberapa fungsi maupun method dalam pengoperasiannya. Antara lain sebagai berikut:
Fungsi add_item : digunakan untuk menambahkan item yang ingin dibeli customer.
Fungsi update_item_name : digunakan untuk memperbarui nama barang yang terdapat kesalahan dalam penginputannya.
Fungsi update_item_qty : digunakan untuk memperbarui jumlah barang yang terdapat kesalahan dalam penginputannya.
Fungsi update_item_price : digunakan untuk memperbarui harga barang yang terdapat kesalahan dalam penginputannya.
Fungsi delete_item merupakan : digunakan untuk menghapus salah satu item yang batal dibeli oleh customer.
Fungsi reset_transaction : digunakan untuk menghapus semua transaksi.
Fungsi check_order : digunakan untuk memeriksa orderan yang telah dimasukkan dalam keranjang belanjaan.
Fungsi total_price : digunakan untuk menghitung total belanja yang diharus dibayarkan oleh customer.


### 2. Objectives
Bagaimana customer dapat melakukan transaski? : Programmer perlu membuat class Transaction yang digunakan untuk membuat objek transaksi.
Bagaimana cara memudahkan customer berbelanja dengan sistem self-service? : Programmer perlu menambahkan fitur belanja seperti tambah barang yang akan dibeli, jumlah barang yang akan dibeli, harga barang menggunakan method add_item().
Bagaimana jika customer salah memasukkan nama barang yang ingin dibeli tanpa menghapus semua barangnya? : Programmer perlu menggunakan method update_item_name untuk mengubah nama barang yang terjadi kesalahan dalam penginputannya.
Bagaimana jika customer salah memasukkan jumlah barang yang ingin dibeli tanpa menghapus semua barangnya? : Programmer perlu menggunakan method update_item_qty untuk mengubah jumlah barang yang terjadi kesalahan dalam penginputannya.
Bagaimana jika customer salah memasukkan harga barang yang ingin dibeli tanpa menghapus semua barangnya? : Programmer perlu menggunakan method update_item_price untuk mengubah harga barang yang terjadi kesalahan dalam penginputannya.
Bagaimana jika customer ingin menghapus salah satu barang yang batal dibeli? : Programmer perlu menggunakan method delete_item untuk menghapus salah satu barang yang batal dibeli.
Bagaimana jika customer ingin menghapus semua barang yang dibeli? : Programmer perlu menggunakan method reset_item untuk menghapus semua transaksinya.
Bagaimana jika customer ingin memeriksa kembali belanjaannya? : Programmer perlu menggunakan method check_order untuk memeriksa kembali transaksinya, apakah terjadi kesalahan input atau tidak.
Bagaimana jika customer ingin menampilkan total harga belanja? : Programmer perlu menggunakan method total_price untuk menampilkan total keseluruhan yang harus dibayarkan customer.




```python
print("halo")
```