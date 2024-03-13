# F06 - UBAH STOK


# Fungsi menghitung panjang
def lenmanual(line):

    # KAMUS LOKAL
    # count, i : int

    # ALGORITMA
    count = 0
    for i in line :
        count += 1

    return count


# Fungsi cek validasi elemen input
# Menghasilkan true apabila seluruh elemen input valid
def cekElmtInput(varInput, elemenValid) :

    # KAMUS LOKAL
    # count, i : int
    # elemen : char

    # ALGORITMA
    count = 0
    for elemen in varInput.lower() :                # cek setiap karakter pada "varInput"
        for i in range(lenmanual(elemenValid)) :
            if (elemen == elemenValid[i]) :         # jika karakter merupakan elemen yang valid, "count" bertambah satu
                count += 1
                break
    
    if (lenmanual(varInput) == count) :             # jika jumlah "count" sama dengan jumlah karakter pada "varInput", seluruh karakter pada "varInput" valid
        return True
    else :
        return False



# Prosedur fitur ubah stok game di toko
def FiturUbahStok() :

    # KAMUS LOKAL
    # IDgame, namaGame : str
    # found : bool
    # i, stokGame, ubahstok, updateStok : int

    # ALGORITMA
    global datafilegame

    print()
    print("\033[1m==========  U B A H  S T O K  ==========\033[0m")
    print()
    IDgame = input("Masukkan ID game\t: ")

    while (IDgame == '') :                                      # selama input ID game kosong, meminta ulang input ID game
        print('\nMohon masukkan ID game.\n')
        IDgame = input("Masukkan ID game\t: ")

    found = False 
    if (lenmanual(datafilegame) > 1) :                          # memeriksa apakah input ID game terdapat pada variabel global "datafilegame"
        for i in range(1, lenmanual(datafilegame)) :
            if (IDgame.upper() == datafilegame[i][0]) :         # input ID game ditemukan pada variabel global "datafilegame"
                namaGame = datafilegame[i][1] 
                stokGame = int(datafilegame[i][5])
                found = True
                break

    if (found == False) :                                       # jika input ID game tidak ditemukan pada variabel global "datafilegame"
        print("\nTidak ada game dengan ID", IDgame + ".")
    else :                                                      # jika input ID game ditemukan pada variabel global "datafilegame",
        ubahstok = input("Masukkan jumlah" + 2*'\t' + ": ")     # meminta input pengubahan jumlah stok game
        
        while (ubahstok == '') or (cekElmtInput(ubahstok,number+[simbol[0]]) == False) :    # selama input ubahstok kosong atau bukan angka
            if (ubahstok == '') :                                                           # jika input ubahstok kosong, pengubahan jumlah stok game dianggap 0
                print('\nMasukan pengubahan stok game kosong.')
                ubahstok = '0'
            else :                                                                          # jika input ubahstok bukan angka, meminta ulang input ubahstok
                print('\nMasukan jumlah stok game harus merupakan angka.\n')
                ubahstok = input("Masukkan jumlah" + 2*'\t' + ": ")      
                                             
        ubahstok = int(ubahstok)

        print()
        updateStok = stokGame + ubahstok                        # hitung hasil update jumlah stok game berdasarkan jumlah stok awal dan pengubahan jumlah stok

        if (updateStok < 0) :                                   # jika hasil update jumlah stok game menjadi kurang dari 0
            print("Stok game", namaGame, "gagal dikurangi karena stok kurang. Stok sekarang :", stokGame, "(<", str(ubahstok*(-1)) + ")")
        else :                                                  # jika hasil update jumlah stok game tidak kurang dari 0
            if (ubahstok < 0) :                                                                         # jika input ubahstok bilangan negatif, stok berkurang
                print("Stok game", namaGame, "berhasil dikurangi. Stok sekarang :", updateStok)
            elif (ubahstok > 0) :                                                                       # jika input ubahstok bilangan positif, stok bertambah
                print("Stok game", namaGame, "berhasil ditambahkan. Stok sekarang :", updateStok)
            else :                                                                                      # jika input ubahstok nol atau kosong, stok tidak berubah
                print("Stok game", namaGame, "tidak berubah. Stok sekarang :", updateStok)

            datafilegame[i][5] = str(updateStok)                # mengubah data jumlah stok game untuk ID game yang diinput
    print()



# ALGORITMA
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbol = ["-", "_"]

FiturUbahStok()