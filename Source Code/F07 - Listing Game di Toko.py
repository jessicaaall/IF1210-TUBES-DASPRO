# F07 - LISTING GAME DI TOKO BERDASARKAN ID, TAHUN RILIS, DAN HARGA

# Fungsi menghitung panjang
def lenmanual(line):

    # KAMUS LOKAL
    # count, i : int

    # ALGORITMA
    count = 0
    for i in line :
        count += 1

    return count


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



# Prosedur fitur listing game di toko berdasarkan ID, tahun rilis, dan harga
def FiturListGameToko():
    # Melakukan sorting terhadap game berdasarkan harga dan tahun rilisnya

    # KAMUS LOKAL
    # valid : array [0..6] of str
    # list_game : matrix of str
    # skema : str
    # found : bool
    # i : int


    # Fungsi mengurutkan baris tiap matriks berdasarkan nilai suatu atribut
    def SortMatrix(Matrix, Atribut, AscOrDesc):
        # Mengurutkan baris tiap matriks berdasarkan nilai suatu atribut

        # KAMUS LOKAL
        # i, Pass : int
        # IEks : int            ; indeks nilai ekstrem elemen array of game dari matriks maks/min
        # Emax, Ei : str
        # Temp : array of str

        # ALGORITMA 
        # Sorting menggunakan skema bubble sort
        if lenmanual(Matrix) > 0:
            for Pass in range(lenmanual(Matrix)-1):                                     # Menandai indeks tempat pertukaran
                IEks = Pass
                for i in range(Pass+1, lenmanual(Matrix)):
                    if Atribut == 0:                                                    # Jika atribut 0, akan diambil nilai atribut id
                        Emax = ''; Ei = ''
                        for j in range(4, lenmanual(Matrix[IEks][Atribut])): Emax += Matrix[IEks][Atribut][j]
                        for j in range(4, lenmanual(Matrix[i][Atribut])): Ei += Matrix[i][Atribut][j]
                    else:                                                               # Diambil nilai dari atribut harga atau tahun
                        Emax = Matrix[IEks][Atribut]; Ei = Matrix[i][Atribut] 
                    if int(Emax) < int(Ei) and AscOrDesc == '-': IEks = i               # Jika AscOrDesc "-", akan diambil indeks dengan nilai minimum
                    elif int(Emax) > int(Ei) and AscOrDesc == '+': IEks = i             # Jika AscOrDesc "+", akan diambil indeks dengan nilai maksimum
                Temp = Matrix[IEks]                                                     # Row matriks dengan nilai ekstrim disimpan sementara
                Matrix[IEks] = Matrix[Pass]                                             # Row matriks dengan nilai ekstrim ditukar dengan row Pass tempat pertukaran
                Matrix[Pass] = Temp

        return Matrix



    # ALGORITMA
    global datafilegame
    valid = ['tahun+', 'tahun-', 'harga+', 'harga-', '', 'id+', 'id-']

    print()
    print("\033[1m==========  L I S T  G A M E  D I  T O K O  ==========\033[0m")
    print()
    skema = input('Skema sorting' + '\t' + ': ').lower()
    print()

    list_game = []                                      # Inisiasi matriks list_game
    for i in range(1, lenmanual(datafilegame)):         # Mengisi matriks list_game berdasarkan data dari datafilegame
        list_game += [[datafilegame[i][0], datafilegame[i][1], datafilegame[i][4], datafilegame[i][2], datafilegame[i][3], datafilegame[i][5]]]

    found = False
    for i in range(lenmanual(valid)) :                  # Memvalidasi apakah skema sorting benar
        if skema == valid[i] :                          # Jika benar maka sorting akan dilanjutkan
            found = True
            break

    if found == True :                                  # Skema valid, orting dilanjutkan
        if (skema == '' or skema == 'id+'): cetakTabelMatrix(SortMatrix(list_game,0,'+'))               # Sorting berdasarkan id menaik
        elif skema == 'id-': cetakTabelMatrix(SortMatrix(list_game,0,'-'))                              # Sorting berdasarkan id menurun
        elif skema[0]+skema[1]+skema[2]+skema[3]+skema[4] == 'tahun': cetakTabelMatrix(SortMatrix(list_game,4,skema[5]))    # Sorting berdasarkan tahun
        else: cetakTabelMatrix(SortMatrix(list_game,2,skema[5]))                                                            # Sorting berdasarkan harga
    else: print('Skema sorting tidak valid!')           # Skema sorting tidak valid, menuliskan pesan error
    print()



# ALGORITMA
FiturListGameToko()