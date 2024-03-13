# F05 - MENGUBAH GAME PADA TOKO GAME


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


# Fungsi untuk menghilangkan titik pada notasi harga
def hargatoint(harga):
    
    # KAMUS LOKAL
    # i : int
    # integer : str

    # ALGORITMA
    integer = ''
    for i in range(lenmanual(harga)):
        if harga[i] != '.' :                # karakter pada "harga" yang bukan titik ditambahkan ke "integer"
            integer += harga[i]

    return integer


# Prosedur fitur mengubah game pada toko game
def FiturUbahGame():
    # Mengubah isi data suatu game pada toko game

    # KAMUS LOKAL
    # IDgame : str
    # found, update : bool
    # i, j : int
    # updateGame : array [0..4] of str
    
    # ALGORITMA
    global datafilegame
    
    print()
    print("\033[1m==========  U B A H  G A M E  ==========\033[0m")
    print()

    IDgame = input("Masukkan ID Game\t: ").upper()
    
    while (IDgame == '') :                                              # selama input ID game kosong, meminta ulang input ID game
        print('\nMohon masukkan ID game.\n')
        IDgame = input("Masukkan ID Game\t: ").upper()

    found = False
    if (lenmanual(datafilegame) > 1) :                                  # memeriksa apakah input ID game terdapat pada variabel global "datafilegame"
        for i in range (1, lenmanual(datafilegame)):
            if (IDgame == datafilegame[i][0]) :
                found = True
                break
    
    if found :                                                          # jika input ID game terdapat pada variabel global "datafilegame",
        updateGame = ["" for i in range(5)]                             # meminta input data game yang ingin diubah
        updateGame[1] = input("Masukkan nama game\t: ").upper()
        updateGame[2] = input("Masukkan kategori\t: ").upper()
        updateGame[3] = input("Masukkan tahun rilis\t: ")
        updateGame[4] = hargatoint(input("Masukkan harga\t\t: "))

        if (cekElmtInput(updateGame[3],number) == False or cekElmtInput(updateGame[4],number) == False):    # input tahun rilis atau harga bukan merupakan angka
            print("\nMasukan tahun rilis dan harga harus merupakan angka.")
        else :                                                  # input tahun rilis atau harga merupakan angka
            update = False
            for j in range(lenmanual(updateGame)) :             # mengubah data game pada variabel global "datafilegame" sesuai dengan input updateGame yang tidak kosong
                if (updateGame[j] != "") :                  
                    update = True
                    datafilegame[i][j] = updateGame[j]

            if update == False :                                # semua input updateGame kosong, sehingga tidak ada data game yang berubah
                print("\nTidak ada data game yang berubah.")
            else :                                              # terdapat input updateGame yang tidak kosong, sehingga ada data game yang berubah
                print("\nData game berhasil diubah.")

    else :                                                      # jika input ID game tidak ditemukan pada variabel global "datafilegame", ID game tersebut tidak ada
        print("\nTidak ada game dengan ID", IDgame + ".")

    print()

    
    
# ALGORITMA
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
FiturUbahGame()