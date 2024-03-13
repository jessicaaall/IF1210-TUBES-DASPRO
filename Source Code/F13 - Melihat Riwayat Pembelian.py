# F13 - MELIHAT RIWAYAT PEMBELIAN


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



# Prosedur fitur melihat riwayat pembelian
def FiturRiwayat():
    # Menampilkan datafileriwayat pembelian game

    # KAMUS LOKAL
    # daftar : matrix of str
    # i : int

    # ALGORITMA
    global datalogin, datafileriwayat

    print()
    print("\033[1m==========  R I W A Y A T  P E M B E L I A N  ==========\033[0m")
    print()

    daftar = []

    for i in range(1, lenmanual(datafileriwayat)):          # memeriksa datafileriwayat dari id user yang telah login sebelumnya 
        if datafileriwayat[i][3] == datalogin[0]:                   # jika id user yang login ditemukan pada datafileriwayat, data riwayat pembelian game ditambahkan ke array daftar
            daftar += [[datafileriwayat[i][0], datafileriwayat[i][1], inttoharga(datafileriwayat[i][2]), datafileriwayat[i][4]]]

    if daftar == []:                                        # jika array daftar kosong
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah "buy_game" untuk membeli.')
        print()
    else:                                                   # jika array daftar tidak kosong
        print('Daftar game :')
        print()
        cetakTabelMatrix(daftar)



# ALGORITMA
FiturRiwayat()