# F08 - MEMBELI GAME


# Fungsi menghitung panjang
def lenmanual(line) :

    # KAMUS LOKAL
    # count, i : int

    # ALGORITMA
    count = 0
    for i in line :
        count += 1

    return count


# Prosedur fitur beli game
def FiturBeliGame() :

    # KAMUS LOKAL
    # IDgame, namaGame, hargaGame, tahunbeli : str
    # found, punya : bool
    # i, stokGame, temp : int

    # ALGORITMA
    global datalogin, datafileuser, datafilegame, datafileriwayat, datafilekepemilikan

    print()
    print("\033[1m==========  B E L I  G A M E  ==========\033[0m")
    print()

    IDgame = input("Masukkan ID Game\t: ").upper()
    
    while (IDgame == '') :                                  # selama input ID game kosong, meminta ulang input ID game
        print('\nMohon masukkan ID game.\n')
        IDgame = input("Masukkan ID Game\t: ").upper()
    
    print()

    found = False
    if (lenmanual(datafilegame) > 1) :                          
        for i in range(1, lenmanual(datafilegame)) :        # memeriksa apakah input ID game terdapat pada variabel global "datafilegame"
            if (IDgame == datafilegame[i][0]) :
                found = True
                namaGame = datafilegame[i][1]
                hargaGame = datafilegame[i][4]
                stokGame = int(datafilegame[i][5])
                temp = i
                break
    
    if found == False :                                     # jika input ID game tidak ditemukan pada variabel global "datafilegame"
        print("Tidak ada game dengan ID", IDgame + ".")
    else :                                                  # jika input ID game ditemukan pada variabel global "datafilegame"
        punya = False
        if (lenmanual(datafilekepemilikan) > 1) :
            for i in range(1, lenmanual(datafilekepemilikan)) :     # memeriksa apakah ID game beserta ID user terdapat pada variabel global "datafilekepemilikan"
                if (IDgame == datafilekepemilikan[i][0] and datalogin[0] == datafilekepemilikan[i][1]) :
                    punya = True
                    break
        
        if (punya == True) :                                        # jika ID game beserta ID user ditemukan pada variabel global "datafilekepemilikan",
            print("Anda sudah memiliki game", namaGame + ".")       # berarti user sudah memiliki game tersebut
        else :                                                      # jika ID game beserta ID user tidak ditemukan pada variabel global "datafilekepemilikan"
            if (stokGame == 0) :                                            # jika stokGame kosong
                print("Stok game", namaGame, "sedang habis.")
            else :                                                          # jika stokGame tidak kosong
                if (int(datalogin[5]) < int(hargaGame)) :                   # jika saldo user lebih kecil dari harga game
                    print("Saldo Anda tidak cukup untuk membeli game", namaGame + ".")
                else :                                                      # jika saldo user lebih besar atau sama dengan harga game, game berhasil dibeli
                    print('Game "' + namaGame + '" berhasil dibeli!')
                    
                    for i in range(1,lenmanual(datafileuser)) :             
                        if (datafileuser[i][0] == datalogin[0]) :
                            datafileuser[i][5] = str(int(datafileuser[i][5]) - int(hargaGame))      # mengubah saldo pada datafileuser, dimana saldo user dikurangi harga game
                            datalogin[5] = datafileuser[i][5]                                       # data saldo pada datalogin juga diubah
                            break

                    datafilegame[temp][5] = str(stokGame-1)                 # mengubah data stokGame yang dibeli menjadi berkurang satu
                    tahunbeli = str(datetime.date.today().year)             # memperoleh tahun saat ini
                    datafileriwayat += [[IDgame, namaGame, hargaGame, datalogin[0], tahunbeli]]     # menambahkan data beli game pada variabel global "datafileriwayat"
                    datafilekepemilikan += [[IDgame, datalogin[0]]]                                 # menambahkan data beli game pada variabel global "datafilekepemilikan"
    print()



# ALGORITMA
import datetime

FiturBeliGame()