# F09 - MELIHAT GAME YANG DIMILIKI


# Fungsi menghitung panjang
def lenmanual(line):

    # KAMUS LOKAL
    # count, i : int

    # ALGORITMA
    count = 0
    for i in line :
        count += 1

    return count


# Fungsi mengubah bilangan menjadi notasi harga yang mengandung titik
def inttoharga(integer):
    
    # KAMUS LOKAL
    # i, n : int
    # harga : str

    # ALGORITMA
    harga = '' 
    n = 0
    for i in range(lenmanual(str(integer))-1,-1,-1):        # pengulangan dilakukan secara mundur
        if n % 3 == 0 and n != 0 :                          # apabila "n" habis dibagi 3 dan bukan 0, yang berarti setiap kelipatan tiga dari belakang,
            harga = '.' + harga                             # ditambahkan titik di depan "harga"
        harga = str(integer)[i] + harga
        n += 1

    return harga
    

# Fungsi menghasilkan daftar game yang dimiliki pengguna
def listmygame(id_user, datafilegame, datafilekepemilikan):
    
    # KAMUS LOKAL
    # i, j : int
    # id_game : str
    # mygame : matrix of str

    # ALGORITMA
    mygame = [['id', 'nama', 'kategori', 'tahun_rilis', 'harga']]       # Membuat matriks mygame dengan isi atribut

    for i in range(1, lenmanual(datafilekepemilikan)):                  # Mencari game yang dimiliki user
        if datafilekepemilikan[i][1] == id_user:                        # Jika ID User ditemukan pada data kepemilikan game, game akan dimasukan ke matriks mygame
            id_game = datafilekepemilikan[i][0]
            for j in range(1, lenmanual(datafilegame)):
                if (datafilegame[j][0] == id_game) :               
                    mygame += [[datafilegame[j][0], datafilegame[j][1], datafilegame[j][2], datafilegame[j][3], inttoharga(datafilegame[j][4])]]        # Memasukan game yang sesuai ke matriks mygame
                    break

    return mygame


# Prosedur mencetak tabel dari data matriks
def cetakTabelMatrix(Matrix):
    
    # KAMUS LOKAL
    # i, j, Max : int
    # lenAtribut : array of int

    # ALGORITMA
    if lenmanual(Matrix) > 0:

        # Mencari panjang atribut maksimal
        lenAtribut = [0 for j in range(lenmanual(Matrix[0]))]           # Inisiasi array panjang atribut
        for i in range(lenmanual(Matrix[0])):                           # Mengisi array panjang atribut
            Max = lenmanual(Matrix[0][i])
            for j in range(lenmanual(Matrix)):                          # Mencari nilai maksimum dari panjang data pada suatu atribut
                if lenmanual(Matrix[j][i]) > Max: 
                    Max = lenmanual(Matrix[j][i])
            lenAtribut[i] = Max

        # Mencetak tabel
        for i in range(lenmanual(Matrix)):
            print(str(i+1) + '.' + (lenmanual(str(lenmanual(Matrix)))-lenmanual(str(i+1))+1)*' ', end='')       # Mencetak penomoran tabel
            for j in range(lenmanual(Matrix[0])):
                print(Matrix[i][j]+(lenAtribut[j]-lenmanual(Matrix[i][j]))*' ', end='')                         # Mencetak isi cell pada tabel
                if j != lenmanual(Matrix[0]) - 1:print(" | ", end='')                                           # Mencetak batas tabel
            print()
    else:
        print("Data kosong.")
    print()



# Prosedur fitur melihat game yang dimiliki
def FiturListMyGame() :

    # KAMUS LOKAL
    # daftarmygame, daftargame : matriks of str
    # i : int
    
    # ALGORITMA
    global datalogin, datafilegame, datafilekepemilikan

    print()
    print("\033[1m==========  L I S T  G A M E  Y A N G  D I M I L I K I  ==========\033[0m")
    print()

    daftarmygame = listmygame(datalogin[0], datafilegame, datafilekepemilikan)

    if (lenmanual(daftarmygame) > 1) :                      # jika daftarmygame tidak kosong, mencetak isi daftarmygame
        print("Daftar game :")
        print()
        daftargame = []
        for i in range(1, lenmanual(daftarmygame)) : 
            daftargame += [daftarmygame[i]]
        cetakTabelMatrix(daftargame)
    else :                                                  # jika daftarmygame kosong, berarti user tidak memiliki game
        print('Maaf, kamu belum membeli game. Ketik perintah "buy_game" untuk beli.')
        print()



# ALGORITMA
FiturListMyGame()