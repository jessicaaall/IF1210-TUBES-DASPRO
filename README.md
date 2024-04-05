# Program BNMO 1
BNMO adalah sebuah robot game milik Indra dan Doni yang membantu mereka melepas stress ketika mendapatkan tugas selama di Institut Teknologi Bandung. BNMO dulunya memiliki sistem inventarisasi dan toko game yang baik. Indra dan Doni sedang menjalani kuliah 2 semester di ITB dan merasa kesulitan dan stress. Doni menghabiskan waktu dengan BNMO untuk bermain game. Namun, Indra lebih suka bersenang-senang bermain gacha, akan tetapi ia terus mengalami kerugian. Pada suatu saat, Indra membanting BNMO sehingga BNMO pun rusak. Doni merasa depresi ketika ia mengetahui bahwa BNMO rusak. Doni pun segera memperbaiki BNMO dan ia pun meminta bantuan untuk memperbaiki BNMO tersebut karena Doni tidak cukup ahli dalam ngoding.

## Deskripsi BNMO
Program BNMO yang menggunakan bahasa Python ini memiliki beberapa fungsional. Pada saat pertama kali program BNMO dijalankan, terdapat fungsional load untuk melakukan loading data ke dalam sistem dengan memberikan input nama folder yang berisi file penyimpanan. Kemudian, untuk dapat mengakses fungsional-fungsional yang terdapat di BNMO, pengguna harus melakukan login terlebih dahulu. Apabila belum melakukan login, fungsional yang dapat diakses hanyalah help dan login saja. Pada fungsional login, pengguna akan diminta untuk melakukan input username dan password. Apabila username dan password benar atau sesuai, maka pengguna berhasil login. Akses fungsional yang terdapat di BNMO bergantung pada role dari pengguna yang telah login, dimana terdapat dua jenis role, yaitu user atau admin. Fungsional BNMO yang hanya dapat diakses admin adalah register; menambah game ke toko game; mengubah game pada toko game; mengubah stok game di toko game; dan top up saldo. Sementara itu, fungsional BNMO yang hanya dapat diakses user adalah membeli game; melihat game yang dimiliki; mencari game yang dimiliki dari ID dan tahun rilis; dan melihat riwayat pembelian. Fungsional BNMO lainnya yang dapat diakses admin dan juga user adalah listing game di toko berdasarkan ID, tahun rilis, dan harga; mencari game di toko dari ID, nama game, harga, kategori, dan tahun rilis; magic conch shell; game tic-tac-toe; save; dan exit. Fungsional save digunakan untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan. Sementara itu, fungsional untuk keluar dari BNMO adalah exit.

## Fitur BNMO
Program BNMO memiliki beberapa fitur sebagai berikut.
1. F02 - Register
2. F03 - Login
3. F04 - Menambah game ke toko game
4. F05 - Mengubah game pada toko game
5. F06 - Mengubah stok game di toko
6. F07 - Listing game di toko berdasarkan ID, tahun rilis, dan harga
7. F08 - Membeli game
8. F09 - Melihat game yang dimiliki
9. F10 - Mencari game yang dimiliki berdasarkan ID dan tahun rilis
10. F11 - Mencari game di toko berdasarkan ID, nama game, harga, kategori, dan tahun rilis
11. F12 - Top up saldo
12. F13 - Melihat riwayat pembelian
13. F14 - Help
14. F15 - Load
15. F16 - Save
16. F17 - Exit
17. B01 - Cipher
18. B02 - Magic Conch Shell
19. B03 - Game Tic-Tac-Toe

## Data File Eksternal
Program BNMO perlu membaca beberapa data dari file eksternal untuk mengoperasikan sistem. Format file eksternal yang dibaca adalah file dengan ekstensi _csv_. Terdapat 4 file yang perlu dibaca oleh program, yaitu _user.csv_, _game.csv_, _riwayat.csv_, dan _kepemilikan.csv_. File _user.csv_ digunakan untuk menyimpan data pengguna program BNMO, file _game.csv_ digunakan untuk menyimpan daftar game yaang tersedia pada toko, file _riwayat.csv_ menyimpan riwayat pembelian game oleh pengguna program, sementara file _kepemilikan.csv_ menyimpan daftar game yang dimiliki oleh pengguna program.

## Cara Menjalankan Program
Command di bawah ini digunakan untuk menjalankan program BNMO.
```
python {nama file program}.py {nama folder data}
```
Bagian {nama file program} diisi dengan nama file dari program utama yang akan dijalankan dan bagian {nama folder data} diisi dengan nama folder yang berisi file-file csv sebagai data eksternal untuk program. Berikut contoh penulisan command untuk menjalankan program.
```
python Main_Program.py data
```
Untuk melakukan login dengan role _admin_ atau menggunakan role _pengguna yang sudah ada_, dapat dilihat pada folder _data_ file _user (password unciphered).csv_.
