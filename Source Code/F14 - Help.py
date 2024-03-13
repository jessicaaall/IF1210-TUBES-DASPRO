# F14 - HELP


# Prosedur fitur help
def FiturHelp() :

    # KAMUS LOKAL
    # -

    # ALGORITMA
    global datalogin

    print()
    print("\033[1m===============  H E L P  ===============\033[0m")
    print()

    if (datalogin == []) :                                                          # jika variabel global "datalogin" kosong, yang berarti pengguna belum login
        print("1.  login" + 2*'\t' + ": Untuk melakukan login ke dalam sistem")
        print("2.  help" + 2*'\t' + ": Untuk melihat panduan penggunaan sistem")

    elif (datalogin[4] == "ADMIN") :                                                # jika role pengguna yang telah login adalah admin
        print("1.  register" + 3*'\t' + ": Untuk melakukan registrasi user baru")
        print("2.  login" + 3*'\t' + ": Untuk melakukan login ke dalam sistem")
        print("3.  tambah_game" + 3*'\t' + ": Untuk menambah game yang dijual di toko")
        print("4.  ubah_game" + 3*'\t' + ": Untuk mengubah informasi game yang dijual di toko")
        print("5.  ubah_stok" + 3*'\t' + ": Untuk mengubah stok game yang dijual di toko")
        print("6.  list_game_toko" + 2*'\t' + ": Untuk melihat daftar game yang dijual di toko berdasarkan ID, tahun rilis, atau harga")
        print("7.  search_game_at_store" + '\t' + ": Untuk melihat daftar game yang dijual di toko berdasarkan ID, nama game, harga, kategori, dan tahun rilis")
        print("8.  topup" + 3*'\t' + ": Untuk menambahkan atau mengurangi saldo user")
        print("9.  help" + 3*'\t' + ": Untuk melihat panduan penggunaan sistem")
        print("10. save" + 3*'\t' + ": Untuk menyimpan data setelah melakukan perubahan ke dalam file di dalam folder")
        print("11. exit" + 3*'\t' + ": Untuk keluar dari aplikasi")
        print("12. kerangajaib" + 3*'\t' + ": Dapat menjawab pertanyaan secara ajaib")
        print("13. tictactoe" + 3*'\t' + ": Bermain game tic-tac-toe")

    elif (datalogin[4] == "USER") :                                                 # jika role pengguna yang telah login adalah user
        print("1.  login" + 3*'\t' + ": Untuk melakukan login ke dalam sistem")
        print("2.  list_game_toko" + 2*'\t' + ": Untuk melihat daftar game yang dijual di toko berdasarkan ID, tahun rilis, atau harga")
        print("3.  buy_game" + 3*'\t' + ": Untuk membeli game yang dijual di toko")
        print("4.  list_game" + 3*'\t' + ": Untuk melihat daftar game yang dimiliki")
        print("5.  search_my_game" + 2*'\t' + ": Untuk melihat daftar game yang dimiliki berdasarkan ID dan tahun rilis")
        print("6.  search_game_at_store" + '\t' + ": Untuk melihat daftar game yang dijual di toko berdasarkan ID, nama game, harga, kategori, dan tahun rilis")
        print("7.  riwayat" + 3*'\t' + ": Untuk melihat riwayat pembelian game")
        print("8.  help" + 3*'\t' + ": Untuk melihat panduan penggunaan sistem")
        print("9.  save" + 3*'\t' + ": Untuk menyimpan data setelah melakukan perubahan ke dalam file di dalam folder")
        print("10. exit" + 3*'\t' + ": Untuk keluar dari aplikasi")
        print("11. kerangajaib" + 3*'\t' + ": Dapat menjawab pertanyaan secara ajaib")
        print("12. tictactoe" + 3*'\t' + ": Bermain game tic-tac-toe")

    print()
    print("\033[1m=========================================\033[0m")
    print()



# ALGORITMA
FiturHelp()