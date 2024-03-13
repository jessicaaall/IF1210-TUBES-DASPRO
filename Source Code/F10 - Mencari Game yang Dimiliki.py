# F10 - MENCARI GAME YANG DIMILIKI DARI ID DAN TAHUN RILIS


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

    

# Prosedur fitur mencari game yang dimiliki dari ID dan tahun rilis
def FiturSearchMyGame():
    # Mendapatkan informasi game sesuai dengan query yang diminta oleh pengguna pada inventory.

    # KAMUS LOKAL
    # id_game, tahun : str
    # mygame, searched : matrix of str
    # match : bool
    # i : int

    # ALGORITMA
    global datalogin, datafilegame, datafilekepemilikan

    print()
    print("\033[1m==========  S E A R C H  G A M E  Y A N G  D I M I L I K I  ==========\033[0m")
    print()
    
    mygame = listmygame(datalogin[0], datafilegame, datafilekepemilikan)                # Membuat matriks mygame berisi game yang dimiliki user
    
    id_game = input('Masukan ID Game' + 3*'\t' + ': ').upper()
    tahun = input('Masukan Tahun Rilis Game' + '\t' + ': ')
    searched = []                                                                       # Inisiasi matriks game yang sesuai kriteria

    print()
    for i in range(1,lenmanual(mygame)):                                                # Mencocokkan game pada matriks mygame dengan kriteria sesuai
        match = True
        if id_game != '' and id_game != mygame[i][0]: match = False                     # Jika kondisi terpenuhi, berarti id game tidak sesuai dengan kriteria
        if tahun != '' and tahun != mygame[i][3]: match = False                         # Jika kondisi terpenuhi, berarti tahun rilis game tidak sesuai dengan kriteria
        if match:
            searched += [[mygame[i][0], mygame[i][1], mygame[i][4], mygame[i][2], mygame[i][3]]]        # Menambahkan game yang sesuai kriteria ke matriks hasil pencarian
    
    print()
    if searched == []:                                                                  # Jika game yang dicari tidak ada
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria.')
        print()
    else:                                                                               # Jika game yang dicari ada
        print('Daftar game pada inventory yang memenuhi kriteria :')
        print()
        cetakTabelMatrix(searched)  



# ALGORITMA
FiturSearchMyGame()