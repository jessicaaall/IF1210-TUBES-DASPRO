# F11 - MENCARI GAME DI TOKO DARI ID, NAMA GAME, HARGA, KATEGORI, DAN TAHUN RILIS


def lenmanual(line):

    # KAMUS LOKAL
    # count, i : int

    # ALGORITMA
    count = 0
    for i in line :
        count += 1

    return count


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

    

# Prosedur fitur mencari game di toko dari id, nama game, harga, kategori, dan tahun rilis
def FiturSearchGameAtStore():
    # Pencarian dilakukan pada toko. Terdapat 5 parameter yang dapat digunakan, yaitu ID Game, Nama Game, Harga, Kategori dan Tahun Rilis Game

    # KAMUS LOKAL
    # id_game, name, harga, kategori, tahun : str
    # searched : matrix of str
    # match : bool
    # i : int

    # ALGORITMA
    global datafilegame

    print()
    print("\033[1m==========  S E A R C H  G A M E  D I  T O K O  ==========\033[0m")
    print()

    id_game = input('Masukan ID Game' + 3*'\t' + ': ').upper()
    name = input('Masukan Nama Game' + 2*'\t' + ': ').upper()
    harga = hargatoint(input('Masukan Harga Game' + 2*'\t' + ': '))
    kategori = input('Masukan Kategori Game' + 2*'\t' + ': ').upper()
    tahun = input('Masukan Tahun Rilis Game' + '\t' + ': ')

    searched = []                                                                   # Inisiasi matriks game yang sesuai kriteria

    for i in range(1, lenmanual(datafilegame)):
        match = True
        if id_game != '' and id_game != datafilegame[i][0]: match = False           # Jika kondisi terpenuhi, berarti id game tidak sesuai dengan kriteria
        if name != '' and name != datafilegame[i][1]: match = False                 # Jika kondisi terpenuhi, berarti nama game tidak sesuai dengan kriteria
        if harga != '' and harga != datafilegame[i][4]: match = False               # Jika kondisi terpenuhi, berarti harga game tidak sesuai dengan kriteria
        if kategori != '' and kategori != datafilegame[i][2]: match = False         # Jika kondisi terpenuhi, berarti kategori game tidak sesuai dengan kriteria
        if tahun != '' and tahun != datafilegame[i][3]: match = False               # Jika kondisi terpenuhi, berarti tahun rilis game tidak sesuai dengan kriteria
        if match:
            searched += [[datafilegame[i][0], datafilegame[i][1], datafilegame[i][4], datafilegame[i][2], datafilegame[i][3], datafilegame[i][5]]]  # Menambahkan game yang sesuai kriteria ke matriks hasil pencarian
    
    print('\n')
    if searched == []:                                              # Jika game yang dicari tidak ada
        print('Tidak ada game yang memenuhi kriteria.')
        print()
    else:                                                           # Jika game yang dicari ada
        print('Daftar game pada toko yang memenuhi kriteria :')
        print()
        cetakTabelMatrix(searched)                                  # Mencetak tabel hasil pencarian



# ALGORITMA
FiturSearchGameAtStore()