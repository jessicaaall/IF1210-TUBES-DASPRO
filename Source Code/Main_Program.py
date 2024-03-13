# TUGAS BESAR DASAR PEMROGRAMAN IF1210


# Program Binomo
# Binomo merupakan sebuah robot game. Program ini merupakan sistem operasi dari robot BNMO
# Program ini berisikan sistem inventarisasi & toko game. Di samping fitur tersebut, sistem operasi
# ini juga memiliki fitur game yang tertanam langsung pada sistem.

# -------------------------------------------------------------------------------------------------------------------
# KAMUS
# -------------------------------------------------------------------------------------------------------------------

# datafileuser          : matrix of str         ; Berisikan data user dari user.csv
# datafilegame          : matrix of str         ; Berisikan data game dari game.csv
# datafileriwayat       : matrix of str         ; Berisikan data riwayat pembelian dari riwayat.csv
# datafilekepemilikan   : matrix of str         ; Berisikan data kepemilikan game dari kepemilikan.csv
# charr                 : array [0..25] of str
# simbol                : array [0..1] of str
# number                : array [0..9] of str
# spasi                 : array [0..0] of str
# datalogin             : array [0..5] of str   ; Berisikan data pengguna yang login
# run                   : bool



# -------------------------------------------------------------------------------------------------------------------
# FUNGSI KONSTRUKTOR DAN VALIDASI SERTA PROSEDUR PENGOLAHAN DATA
# -------------------------------------------------------------------------------------------------------------------


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


# Fungsi validasi input username 
# Mengembalikan username yang sudah valid beserta password
def usernameValid(username,password) :

    # KAMUS LOKAL
    # inputUsername : bool

    # ALGORITMA
    inputUsername = False
    while inputUsername == False :
        if cekElmtInput(username, charr+simbol+number) == False :   # jika terdapat elemen di username yang tidak valid, meminta ulang input username beserta password
            print()
            print("Username hanya dapat mengandung alfabet A-Z, a-z, underscore “_”, strip “-”, dan angka 0-9.")
            print()
            print("----------------------------------------")
            print("Silahkan masukkan ulang username dan password.")
            print()
            username = input("Masukkan username" + '\t' + ": ")
            password = input("Masukkan password" + '\t' + ": ")
        else :
            inputUsername = True

    return [username, password]


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


# Fungsi mengecek apakah elemen terdapat dalam array
# Mengembalikan true apabila elemen terdapat dalam array
def isElmtInArr (elmt,arr) :

    # KAMUS LOKAL
    # found : bool
    # i : int

    # ALGORITMA
    found = False
    for i in range(lenmanual(arr)) :
        if (elmt == arr[i]) :               # jika elemen ditemukan dalam array, mengembalikan true
            found = True
            break

    return found





# -------------------------------------------------------------------------------------------------------------------
# FITUR - FITUR
# -------------------------------------------------------------------------------------------------------------------



# F02 - REGISTER
# Prosedur fitur register
def FiturRegister() :

    # KAMUS LOKAL
    # nama, username, password, password_to_ciphered, id, role, saldo : str
    # usernameSama : bool
    # i : int
    # arrRegister : array [0..5] of str


    # Fungsi validasi input nama
    # Mengembalikan nama yang telah valid
    def namaValid(nama) :

        # KAMUS LOKAL
        # inputNama : bool

        # ALGORITMA
        inputNama = False
        while inputNama == False :
            if cekElmtInput(nama, charr+spasi) == False :       # jika terdapat elemen di nama yang tidak valid (bukan huruf atau spasi), meminta ulang input nama
                print()
                print("Nama hanya dapat mengandung alfabet A-Z, a-z dan spasi.")
                print("Silahkan masukkan ulang nama yang sesuai.")
                print()
                nama = input("Masukkan nama" + 2*'\t' + ": ")
            else :
                inputNama = True

        return nama


    # Fungsi memastikan input nama benar (khususnya untuk kasus apabila pengguna typo)
    # Mengembalikan nama yang sudah benar
    def namaYakinBenar(nama) :

        # KAMUS LOKAL
        # benar : str

        # ALGORITMA
        nama = namaValid(nama)

        print()
        print("Nama" + 3*'\t' + ": " + nama)
        benar = input("Apakah nama sudah sesuai? (y/n)" + '\t' + '>>  ').lower()        # memunculkan pertanyaan
        print("----------------------------------------")

        if (benar == 'n') :                                     # jika pengguna menjawab "n", input nama dan validasi nama diulangi
            nama = input("Masukkan nama" + 2*'\t' + ": ")
            nama = namaYakinBenar(nama)
        elif (benar != 'n' and benar != 'y') :                  # jika pengguna menjawab selain "n" dan "y", pertanyaan dimunculkan kembali
            nama = namaYakinBenar(nama)

        return nama


    # ALGORITMA
    global datafileuser

    print()
    print("\033[1m===============  R E G I S T E R  ===============\033[0m")
    print()
    nama = input("Masukkan nama" + 2*'\t' + ": ")
    username = input("Masukkan username" + '\t' + ": ")
    password = input("Masukkan password" + '\t' + ": ")

    if (nama != '' and username != '' and password != '') :                 # jika input nama, username, dan password tidak kosong
        nama = namaYakinBenar(nama).upper()                                 # validasi nama (pada validasi nama, dapat diminta ulang input nama)

        if (nama != '') :                                                   # jika setelah validasi nama, nama tidak kosong
            [username,password] = usernameValid(username,password)          # validasi username (pada validasi username, dapat diminta ulang input username beserta password)

            if (username != '' and password != '') :                        # jika setelah validasi username, username dan password tidak kosong
                usernameSama = False
                for i in range(1, lenmanual(datafileuser)) :                        # pengecekan apakah username bersifat unik
                    if (username == datafileuser[i][1]) :                           # jika username yang sama ditemukan pada variabel global "datafileuser"
                        usernameSama = True                                         # username tidak bersifat unik
                        break
                
                if (usernameSama == True) :                                         # jika username tidak bersifat unik
                    print("\nUsername", username, "sudah terpakai.")
                    print("Silahkan menggunakan username lain.\n")

                else :                                                              # jika username bersifat unik
                    password_to_ciphered = FiturCipher(password.upper(),True)       # transformasi password menjadi ciphered

                    id = 'ID' + str(lenmanual(datafileuser))
                    role = 'USER'
                    saldo = '0'
                    arrRegister = [id, username, nama.upper(), password_to_ciphered, role, saldo]
                    datafileuser += [arrRegister]                                   # menambahkan data register pada variabel global "datafileuser"
                        
                    print()
                    print('Username', username, 'dengan nama', nama, 'telah berhasil register ke dalam "Binomo".')
                    print()

            else :                                                          # jika setelah validasi username, username atau password kosong, register gagal
                print('\nRegister gagal. Informasi register tidak lengkap.\n')
                
        else :                                                              # jika setelah validasi nama, nama kosong, register gagal
            print('\nRegister gagal. Informasi register tidak lengkap.\n')

    else :                                                                  # jika input nama, username, atau password kosong, register gagal
        print('\nRegister gagal. Informasi register tidak lengkap.\n')




# F03 - LOGIN
# Prosedur fitur login
def FiturLogin() :

    # KAMUS LOKAL
    # username, password : str


    # Fungsi cek apakah username dan password yang diinput terdapat pada variabel global "datafileuser" 
    # Mengembalikan data pengguna yang melakukan login
    def cekLogin(username,password) :

        # KAMUS LOKAL
        # found : bool
        # i : int

        # ALGORITMA
        found = False
        while found == False :
            [username, password] = usernameValid(username,password)             # validasi input username sehingga diperoleh username yang mengandung elemen yang valid

            for i in range(1, lenmanual(datafileuser)) :                                                                # cek isi "datafileuser" 
                if (username == datafileuser[i][1]) and (FiturCipher(password.upper(),True) == datafileuser[i][3]) :    # username dan password yang diinput ditemukan pada "datafileuser"
                    found = True
                    break
            
            if (found == False) :                                               # jika username dan password tidak ditemukan pada "datafileuser", 
                print()                                                         # meminta ulang input username dan password
                print('Password atau username salah atau tidak ditemukan.')
                print()
                print("----------------------------------------")
                print("Silahkan masukkan ulang username dan password.")
                print()
                username = input("Masukkan username" + '\t' + ": ")
                password = input("Masukkan password" + '\t' + ": ")
        
        return datafileuser[i]



    # ALGORITMA
    global datalogin, datafileuser

    print()
    print("\033[1m===============  L O G I N  ===============\033[0m")
    print()
    username = input("Masukkan username" + '\t' + ": ")
    password = input("Masukkan password" + '\t' + ": ")

    datalogin += cekLogin(username,password)                        # Menambahkan data pengguna yang login pada variabel global "datalogin"

    print()
    print('Halo', datalogin[2] + '! Selamat datang di "Binomo".')
    print()




# F04 - MENAMBAH GAME KE TOKO GAME
# Prosedur fitur menambah game ke toko game
def FiturTambahGame() :

    # KAMUS LOKAL
    # tambahgame : array [0..5] of str


    # Fungsi input tambah game
    def InputTambahGame() :
        
        # KAMUS LOKAL
        # tambahgame : array [0..5] of str

        # ALGORITMA
        tambahgame = ["" for i in range (6)]
        tambahgame[0] = "GAME" + str(lenmanual(datafilegame))
        tambahgame[1] = input("Masukkan nama game" + '\t' + ": ").upper()
        tambahgame[2] = input("Masukkan kategori" + '\t' + ": ").upper()
        tambahgame[3] = input("Masukkan tahun rilis" + '\t' + ": ")
        tambahgame[4] = hargatoint(input("Masukkan harga" + 2*'\t' + ": "))
        tambahgame[5] = input("Masukkan stok awal" + '\t' + ": ")

        return tambahgame


    # Fungsi untuk memeriksa apakah terdapat input yang kosong
    # Mengembalikan true jika terdapat input yang kosong
    def cekInputKosong(tambahgame) :

        # KAMUS LOKAL
        # found : bool
        # i : int

        # ALGORITMA
        found = False
        for i in range(lenmanual(tambahgame)) :
            if (tambahgame[i] == "") :              # jika terdapat elemen pada array "tambahgame" yang kosong, mengembalikan nilai True
                found = True
                break
        
        return found


    # Fungsi validasi input tambah game ke toko game terisi semua
    def cekInputTambahGame() :

        # KAMUS LOKAL
        # tambahgame : array [0..5] of str
        
        # ALGORITMA
        tambahgame = InputTambahGame()

        # selama terdapat input tambahgame yang kosong, atau tahun rilis, harga, atau stok awal dari game yang ditambahkan bukan merupakan angka,
        # meminta ulang input tambahgame
        while (cekInputKosong(tambahgame) == True or cekElmtInput(tambahgame[3], number) == False or cekElmtInput(tambahgame[4], number) == False or cekElmtInput(tambahgame[5], number) == False) :
            print()
            if cekElmtInput(tambahgame[3], number) == False or cekElmtInput(tambahgame[4], number) == False or cekElmtInput(tambahgame[5], number) == False :
                print("Masukan tahun rilis, harga, dan stok awal harus merupakan angka.")
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
            print()
            tambahgame = InputTambahGame()
        
        return tambahgame


    # Fungsi memeriksa apakah input game yang akan ditambahkan ada pada toko game
    # Mengembalikan true apabila game yang akan ditambahkan sudah ada pada toko game
    def isTambahGameBaru(tambahgame) :

        # KAMUS LOKAL
        # found : bool
        # i : int

        # ALGORITMA
        found = False
        if (lenmanual(datafilegame) > 1) :
            for i in range(1, lenmanual(datafilegame)) :

                # jika input tambahgame terdapat pada variabel global "datafilegame", game pernah ditambahkan ke toko game sebelumnya
                if (datafilegame[i][1] == tambahgame[1] and datafilegame[i][2] == tambahgame[2] and datafilegame[i][3] == tambahgame[3] and datafilegame[i][4] == tambahgame[4]) :
                    found = True
                    break
        
        return found



    # ALGORITMA
    global datafilegame

    print()
    print("\033[1m==========  T A M B A H  G A M E  K E  T O K O  ==========\033[0m")
    print()
    
    tambahgame = cekInputTambahGame()
    print()

    if isTambahGameBaru(tambahgame) == True :                                           # jika game yang akan ditambahkan sudah ada pada toko game
        print("Tambah game gagal. Game", tambahgame[1], "sudah ada pada toko game.")
    else :                                                                              # jika game yang akan ditambahkan belum ada pada toko game
        datafilegame += [tambahgame]                                                    # data game baru ditambahkan pada variabel global "datafilegame"
        print("Selamat! Berhasil menambahkan game", tambahgame[1] + ".")
    print()




# F05 - MENGUBAH GAME PADA TOKO GAME
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




# F06 - UBAH STOK
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





# F07 - LISTING GAME DI TOKO BERDASARKAN ID, TAHUN RILIS, DAN HARGA
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




# F08 - MEMBELI GAME
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




# F09 - MELIHAT GAME YANG DIMILIKI
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




# F10 - MENCARI GAME YANG DIMILIKI DARI ID DAN TAHUN RILIS
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




# F11 - MENCARI GAME DI TOKO DARI ID, NAMA GAME, HARGA, KATEGORI, DAN TAHUN RILIS
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




# F12 - TOP UP SALDO
# Prosedur fitur top up saldo
def FiturTopUp() :

    # KAMUS LOKAL
    # username, nama : str
    # found : bool
    # topupsaldo, i, saldo, updateSaldo : int

    # ALGORITMA
    global datalogin, datafileuser

    print()
    print("==========  T O P  U P  S A L D O  ==========")
    print()
    username = input("Masukkan username" + '\t' + ": ")
    topupsaldo = hargatoint(input("Masukkan saldo" + 2*'\t' + ": "))

    while (username == '') :                                        # selama input username kosong, meminta ulang input username
        print('\nMohon masukkan username.\n')
        username = input("Masukkan username" + '\t' + ": ")
    
    while (topupsaldo == '') or (cekElmtInput(topupsaldo,number+[simbol[0]]) == False) :    # selama input topupsaldo kosong atau bukan angka, meminta ulang input topupsaldo 
        if (topupsaldo == '') :                                         
            print('\nMohon masukkan nominal saldo yang ingin diisi.\n')
        else : 
            print('\nMasukan saldo harus merupakan angka.\n')
        topupsaldo = hargatoint(input("Masukkan saldo" + 2*'\t' + ": "))
   
    topupsaldo = int(topupsaldo)

    found = False 
    for i in range(1, lenmanual(datafileuser)) :                                        # memeriksa apakah input username terdapat pada variabel global "datafileuser"
        if (username == datafileuser[i][1]) and (datafileuser[i][4] == 'USER') :        # dan role dari username tersebut adalah user
            nama = datafileuser[i][2] 
            saldo = int(datafileuser[i][5])
            found = True
            break
    
    print()                                                     # jika input username tidak ditemukan pada variabel global "datafileuser"
    if (found == False) :                                       # atau role dari username tersebut bukan user
        print('Username "' + username + '" dengan role USER tidak ditemukan.')
    else :                                                      # jika input username ditemukan pada variabel global "datafileuser" dan role dari username adalah user
        updateSaldo = saldo + topupsaldo                        # hitung hasil update saldo berdasarkan saldo awal dan top up saldo
        if (updateSaldo < 0) :                                              # jika hasil update saldo menjadi kurang dari nol, top up gagal
            print("Top up gagal. Masukan saldo tidak valid. Saldo sekarang :", saldo, "(<", str(topupsaldo*(-1)) + ")")
        else :                                                              # jika hasil update saldo tidak lebih kecil dari nol
            if (topupsaldo < 0) :                                                                       # jika input topupsaldo bilangan negatif, saldo berkurang
                print("Top up berhasil. Saldo", nama, "berkurang menjadi", str(updateSaldo) + ".")
            elif (topupsaldo > 0) :                                                                     # jika input topupsaldo bilangan positif, saldo bertambah
                print("Top up berhasil. Saldo", nama, "bertambah menjadi", str(updateSaldo) + ".")
            else :                                                                                      # jika input topupsaldo sama dengan nol, saldo tidak berubah
                print("Saldo", nama, "tidak berubah. Saldo tetap", str(updateSaldo) + ".")
            datafileuser[i][5] = str(updateSaldo)                           # mengubah data saldo untuk username yang diinput
            datalogin[5] = str(updateSaldo)                                 # mengubah data saldo pada datalogin
    print()




# F13 - MELIHAT RIWAYAT PEMBELIAN
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




# F15 - LOAD
# Prosedur fitur load
def FiturLoad():
    # Loading data ke sistem

    # KAMUS LOKAL
    # parser : ArgumentParser
    # args : Namespace
    # e : tuple
    # dirs, notfound : array of str
    # found : bool
    # folder_read : str
    # i : int


    # Fungsi memisahkan teks berdasarkan delimiter tertentu
    # Mengembalikan teks dalam bentuk array
    def splitline(line,delimiter) :

        # KAMUS LOKAL
        # hasil : array of str
        # kata : str
        # i : int

        # ALGORITMA
        hasil = []
        kata = ''
        for i in range(lenmanual(line)) :
            if line[i] == delimiter :       # jika karakter adalah tanda pemisah, "kata" ditambahkan ke array "hasil"
                hasil += [kata]
                kata = ''                   # variabel "kata" menjadi kosong (untuk diisi dengan kata berikutnya)
            elif line[i] == '\n' :          # jika karakter adalah newline, "kata" tidak berubah
                kata = kata
            else :                          # jika karakter bukan tanda pemisah dan bukan newline, karakter ditambahkan ke "kata"
                kata += line[i]
        hasil += [kata]

        return hasil


    # Fungsi membaca file user.csv dan menyimpannya ke datafile
    def bacafile(filecsv,folder_read) :

        # KAMUS LOKAL
        # file : file of str
        # bacafile, line : array of str
        # row : str

        # ALGORITMA
        datafile = []                                   # inisiasi matriks

        file = open(folder_read+'\\'+filecsv, 'r')      # membuka file csv
        bacafile = file.readlines()                     # mengubah file csv menjadi array of row

        for row in bacafile :                           # mengubah tiap row menjadi array of column
            line = splitline(row,";")
            datafile += [line]
        
        file.close()                                    # menutup file

        return datafile



    # ALGORITMA
    global datafileuser, datafilegame, datafileriwayat, datafilekepemilikan, run

    parser = argparse.ArgumentParser(description='Loading data ke sistem', add_help=False)          # Membuat format argumen
    parser.add_argument('nama_folder', metavar='<nama_folder>', type=str)

    for e in os.walk(os.getcwd()):                                                                  # Mencari list folder yang ada pada direktori
        if e[0] == os.path.dirname(os.path.realpath(__file__)):                                     # Jika direktori program sesuai dengan os.walk, akan disimpan nama-nama folder yang ada pada direktori
            dirs = e[1]
    # Referensi dari https://www.youtube.com/watch?v=cdblJqEUDNo

    run = False

    try :                                                               # Mencoba memecahkan argumen
        parser.error = print('', end='')
        args = parser.parse_args()

        folder_read = args.nama_folder    
        
        found = False
        for i in range (lenmanual(dirs)):                               # Mencari apakah folder masukan ada di dalam direktori
            if folder_read == dirs[i]:                                  # Jika folder ada di direktori, mengembalikan true
                found = True

        if found:                                                       # Jika folder ditemukan, folder akan dibaca
            for e in os.walk(os.getcwd()):                              # Mencari list file yang ada dalam folder
                if e[0] == os.path.dirname(os.path.realpath(__file__))+'\\'+folder_read:        # Jika direktori folder sama dengan os.walk, akan disimpan nama-nama file yang ada pada folder
                    file = e[2]
            
            notfound = []
            if not isElmtInArr('user.csv', file): notfound += ['user.csv']                        # Jika kondisi terpenuhi, file user.csv tidak ditemukan dalam folder
            if not isElmtInArr('game.csv', file): notfound += ['game.csv']                        # Jika kondisi terpenuhi, file game.csv tidak ditemukan dalam folder
            if not isElmtInArr('riwayat.csv', file): notfound += ['riwayat.csv']                  # Jika kondisi terpenuhi, file riwayat.csv tidak ditemukan dalam folder
            if not isElmtInArr('kepemilikan.csv', file): notfound += ['kepemilikan.csv']          # Jika kondisi terpenuhi, file kepemilikan.csv tidak ditemukan dalam folder

            if lenmanual(notfound) == 0:                                # Jika semua file ditemukan, akan dibaca semua file
                print('\nLoading...')
                datafileuser = bacafile('user.csv',folder_read)
                datafilegame = bacafile('game.csv',folder_read)
                datafileriwayat = bacafile('riwayat.csv',folder_read)
                datafilekepemilikan = bacafile('kepemilikan.csv',folder_read)
                print()
                print('\033[1m====================================================================')
                print('|||||                                                          |||||')
                print('|||||      S E L A M A T  D A T A N G  D I  "B I N O M O"      |||||')
                print('|||||                                                          |||||')
                print('====================================================================\033[0m')
                run = True
            else :                                                      # Jika ada file yang tidak ditemukan, akan menulis pesan error
                print('\nFile',end=' ')
                for i in range(lenmanual(notfound)):
                    print(notfound[i], end='')
                    if lenmanual(notfound) > 2 and i != lenmanual(notfound)-1: print(',', end=' ')
                    else: print(' ',end='')
                    if i == lenmanual(notfound)-2: print('dan',end=' ')
                print(f'tidak ditemukan dalam {folder_read}')
                run = False
            
        else:                                                           # Jika folder tidak ditemukan, akan menulis pesan error
            print(f'\nFolder "{args.nama_folder}" tidak ditemukan.')
            run = False
        print()

    except :                                                            # Jika argumen tidak bisa dipecahkan, akan menuliskan pesan error
        print('\nTidak ada nama folder yang diberikan!')
        parser.error = print('Usage : ' + '\033[3m'+ 'python', os.path.basename(__file__), '<nama folder>' + '\033[0m\n')
        run = False




# F16 - SAVE
# Prosedur fitur save
def FiturSave() :

    # KAMUS LOKAL
    # namaFolder, locFolder : str


    # Prosedur menulis datafile ke file csv
    def tulisfile(filecsv,folder_write,datafile) :

        # KAMUS LOKAL
        # file : file of str
        # i, j : int

        # ALGORITMA
        file = open(folder_write+'\\'+filecsv, 'w')
        
        for i in range(lenmanual(datafile)) :
            file.write(datafile[i][0])                      # menulis data indeks 0
            for j in range(1,lenmanual(datafile[i])) :
                file.write(';' + datafile[i][j])            # menulis data indeks selanjutnya dengan didahului separator semicolon
            file.write('\n')                                # menulis newline setelah data indeks terakhir ditulis
        
        file.close()



    # ALGORITMA
    global datafileuser, datafilegame, datafileriwayat, datafilekepemilikan

    print()
    print("\033[1m===============  S A V E  ===============\033[0m")
    print()
    namaFolder = input('Masukkan nama folder penyimpanan\t: ')

    # selama input nama folder kosong atau terdapat elemen di nama folder yang tidak valid (bukan huruf, bukan simbol "_" dan "-", bukan angka, dan bukan spasi), meminta ulang input nama folder
    while (namaFolder == '' or namaFolder == ' ' or cekElmtInput(namaFolder,charr+simbol+number+spasi) == False) :  
        if (namaFolder == '' or namaFolder == ' ') :                        # jika input nama folder kosong
            print('\nMohon masukkan nama folder penyimpanan.\n')
        else :                                                              # jika terdapat elemen di nama folder yang tidak valid
            print('\nNama folder penyimpanan hanya dapat mengandung alfabet A-Z, a-z, underscore "_", strip "-", angka 0-9, dan spasi.\n')
        namaFolder = input('Masukkan nama folder penyimpanan\t: ')

    locFolder = os.path.dirname(os.path.realpath(__file__)) + '\\' + namaFolder         # folder akan dibuat pada direktori program

    if not os.path.exists(locFolder) :                              # jika folder belum ada, membuat folder
        os.makedirs(locFolder)
    
    print('\nSaving...\n')

    tulisfile('user.csv',locFolder,datafileuser)                    # menulis file user.csv dalam folder "namaFolder"
    tulisfile('game.csv',locFolder,datafilegame)                    # menulis file game.csv dalam folder "namaFolder"
    tulisfile('riwayat.csv',locFolder,datafileriwayat)              # menulis file riwayat.csv dalam folder "namaFolder"
    tulisfile('kepemilikan.csv',locFolder,datafilekepemilikan)      # menulis file kepemilikan.csv dalam folder "namaFolder"

    print('Data telah disimpan pada folder "' + namaFolder + '".')
    print()




# F17 - EXIT
# Prosedur fitur exit
def FiturExit() :

    # KAMUS LOKAL
    # inputValid : bool
    # simpan : str
    
    # ALGORITMA
    inputValid = False
    while (inputValid == False) :                                           # selama input simpan bukan 'y' dan 'n', meminta ulang input simpan
        print()
        print("\033[1m===============  E X I T  ===============\033[0m")
        print()
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)\t>>  ").lower()
        print()

        if (simpan == 'y') :                                                # jika input simpan 'y', memanggil prosedur fitur save
            FiturSave()
            inputValid = True
        elif (simpan == 'n') :                                              # jika input simpan 'n', tidak dilakukan penyimpanan
            print('Data tidak disimpan.')
            inputValid = True
    
    print()
    print("\033[1m================================================")
    print('=====  Anda berhasil keluar dari "Binomo"  =====')
    print("================================================\033[0m")
    print()





# -------------------------------------------------------------------------------------------------------------------
# BONUS
# -------------------------------------------------------------------------------------------------------------------



# B01 - CIPHER
# Fungsi untuk melakukan transformasi ke ciphered dan sebaliknya
def FiturCipher(input_pass:str, encrypt_True:bool) :
    # Mengenskripsi data menggunakan algoritma vigenere cipher
    # Transformasi ke ciphered jika "encrypt_True" bernilai True
    # Transformasi dari ciphered ke semula jika "encrypt_True" bernilai False

    # KAMUS LOKAL
    # key, keystream, cipher : str
    # i, j, order, col : int
    # tabularecta : matrix of str

    # ALGORITMA
    key = 'LOREMIPSUM'

    # Membuat keystream
    keystream = ''
    for i in range(lenmanual(input_pass)):
        keystream += (key[i % lenmanual(key)])
    
    # Inisialisasi tabel tabularecta
    tabularecta = [['' for j in range(93)] for i in range(26)]

    for i in range(26):
        for j in range(93):
            if i+j >= 26: order = (i + j +1) % 94 + 33
            else: order = (i + j) % 94 + 33
            tabularecta[i][j] = chr(order)                                      # Mengisi tabel tabularecta dengan karakter kunci

    # Mengkonversi kata
    cipher = ''
    for i in range(lenmanual(input_pass)):
        if encrypt_True:                                                        # Jika encrypt_True bernilai true, kata akan dienkripsi
            for j in range(lenmanual(tabularecta[0])):
                if tabularecta[0][j] == input_pass[i]:                          # Mencari hasil karakter pengganti yang cocok pada tabularecta
                    col = j
            cipher += tabularecta[ord(keystream[i])-65][col]
        else:                                                                   # Jika encrypt_True bernilai false, kata akan didekripsi
            for j in range(lenmanual(tabularecta[0])):
                if tabularecta[ord(keystream[i])-65][j] == input_pass[i]:       # Mencari kunci karakter tabularecta yang cocok untuk dikembalikan
                    col = j
            cipher += tabularecta[0][col]
        
    return cipher

    # Algoritma diadaptasi dari definisi dan metode enkripsi vigenere cipher pada
    # https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher dan https://youtu.be/SkJcmCaHqS0



# B02 - MAGIC CONCH SHELL
# Prosedur fitur magic conch shell / kerang ajaib
def FiturMagicConchShell():
    # Menjawab pertanyaan secara acak dari daftar jawaban

    # KAMUS LOKAL
    # ask : str
    # answer : array of str
    # waktu : struct_time
    # num : float
    # i : int

    # ALGORITMA
    answer = ['Iya.', 'Tidak.', 'Bisa jadi.', 'Mungkin.', 'Tentu saja.', 'Tidak mungkin.', 'Jangan halu.', 'Terserah.', 'Tidak tahu.', 'Hmmm.']
    print()
    print("\033[1m==========  M A G I C  C O N C H  S H E L L  ==========\033[0m")
    print()
    ask = input('Apa pertanyaanmu?\t')

    waktu = time.localtime(time.time())                                 # Mengambil waktu lokal

    num = waktu.tm_sec % (lenmanual(answer))                               # Menyesuaikan detik yang didapatkan dengan variasi jawaban
    for i in range(waktu.tm_sec) :
        num = (waktu.tm_min * num + time.time()) % (lenmanual(answer))  # Mengasilkan angka acak dengan skema LCG menggunakan basis waktu

    print(f'\n{answer[int(num)]}')
    print()



# B03 - GAME TIC-TAC-TOE
# Prosedur fitur game tic-tac-toe
def FiturTicTacToe():

    # KAMUS LOKAL
    # win, giliran, board_status : str
    # board : matrix of str
    # board_full, kosong, cekisi : bool
    # i, j, X, Y, isi : int

    # ALGORITMA
    print()
    print("\033[1m==========  G A M E  T I C - T A C - T O E  ==========\033[0m")
    print()

    win = ''
    board = [[' ' for j in range(3)] for i in range(3)]
    board_full = False
    giliran = 'X'

    print('Legenda :\nX Pemain 1\nO Pemain 2')

    while not board_full:                           # Menjalankan program hingga papan permainan penuh
        
        isi = 0
        for i in range(3) :                         # Mengecek jumlah papan permainan yang terisi
            for j in range(3) :
                if board[i][j] != ' ' : 
                    isi+=1
        if isi == 9 :                               # Jika semua slot pada papan sudah terisi, akan menghasilkan nilai True untuk menghentikan permainan
            board_full = True

        print('\n\nSTATUS PAPAN\n')                 # Mencetak kondisi papan terbaru
        for i in range(3):
            for j in range(3) :
                print(board[i][j], end='')
                if j != 2 : 
                    print('|', end='')
            if i != 2 : 
                print('\n-+-+-')
            else: print('\n')

        # Mengisi slot pada papan permainan
        if win == '' and not board_full:                            # Jika belum ada yang menang dan papan masih ada yang kosong, maka akan meminta isi
            print(f'\nGiliran pemain "{giliran}"')
            X = input('X : ')
            Y = input('Y : ')
            kosong = True
            cekisi = False
            while X == '' or Y == '' or cekElmtInput(X,number) == False or cekElmtInput(Y,number) == False :            # Validasi nilai X dan Y
                print('\nKotak tidak valid')
                print(f'\nGiliran pemain "{giliran}"')
                X = input('X : ')
                Y = input('Y : ')
            X = int(X) - 1
            Y = int(Y) - 1
            while kosong :
                while X > 2 or X < 0 or Y < 0 or Y > 2 :            # Validasi masukan koordinat slot
                    if not cekisi:                                  # Jika kotak tidak valid maka akan menulis pesan eror
                        print('\nKotak tidak valid.')
                    print(f'\nGiliran pemain "{giliran}"')
                    X = input('X : ')
                    Y = input('Y : ')
                    while X == '' or Y == '' or cekElmtInput(X,number) == False or cekElmtInput(Y,number) == False:     # Validasi nilai X dan Y
                        print('\nKotak tidak valid')
                        print(f'\nGiliran pemain "{giliran}"')
                        X = input('X : ')
                        Y = input('Y : ')
                    X = int(X) - 1
                    Y = int(Y) - 1
                    cekisi = False
                if board[Y][X] != ' ' :                             # Validasi isi slot pada papan 
                    print('\nKotak sudah terisi.')
                    X=999
                    Y=999
                    cekisi = True
                else :                                              # Jika papan masih kosong dan koordinat valid, maka slot diisi
                    board[Y][X] = giliran
                    kosong = False
        
        # Mengecek pemenang untuk menghentikan permainan
        if win != '' : 
            board_full = True
        
        # Mengecek apakah ada yang sudah menang
        for i in range(3) :
            board_status = ''
            for j in range(3) :
                board_status += board[i][j]
            if board_status == 'XXX' or board_status == 'OOO' :         # Jika kondisi terpenuhi, sudah ada pemenang secara horizontal
                win = giliran
        for i in range(3) :
            board_status = ''
            for j in range(3) :
                board_status += board[j][i]
            if board_status == 'XXX' or board_status == 'OOO' :         # Jika kondisi terpenuhi, sudah ada pemenang secara vertikal
                win = giliran
        board_status = ''
        for i in range(3) :
            board_status += board[i][i]
        if board_status == 'XXX' or board_status == 'OOO' :             # Jika kondisi terpenuhi, sudah ada pemenang secara diagonal negatif
            win = giliran
        board_status = ''
        for i in range(3) :
            board_status += board[-i-1][i]
        if board_status == 'XXX' or board_status == 'OOO' :             # Jika kondisi terpenuhi, sudah ada pemenang secara diagonal positif
            win = giliran

        # Mengubah giliran main
        if giliran == 'X' :                         # Jika sekarang giliran X, akan diubah ke O
            giliran = 'O'
        else :                                      # Jika sekarang giliran O, akan diubah ke X
            giliran = 'X'

    if win != '':                                   # Jika win tidak kosong, mencetak pemain yang menang
        print(f'\nPemain "{giliran}" menang.')
    else:                                           # Jika win kosong, mencetak pesan seri
        print('\nSeri. Tidak ada yang menang.')
    print()





# -------------------------------------------------------------------------------------------------------------------
# PROSEDUR PROGRAM UTAMA
# -------------------------------------------------------------------------------------------------------------------



# Prosedur untuk menjalankan program utama
def main() :

    # KAMUS LOKAL
    # menu : str

    # ALGORITMA
    global datalogin

    aksesAdmin = ['register', 'login', 'tambah_game', 'ubah_game', 'ubah_stok', 'list_game_toko', 'search_game_at_store', 'topup', 'help', 'save', 'exit', 'kerangajaib', 'tictactoe']
    aksesUser = ['login', 'list_game_toko', 'buy_game', 'list_game', 'search_my_game', 'search_game_at_store', 'riwayat', 'help', 'save', 'exit', 'kerangajaib', 'tictactoe']

    print()
    menu = input("Masukkan menu \t>>>  ").lower()
    print()

    if (datalogin == []) :                  # jika "datalogin" kosong, berarti pengguna belum login
        if (menu == 'help') :
            FiturHelp()
        elif (menu == 'login') :
            FiturLogin()
        elif (menu != 'help' and menu != 'login' and (isElmtInArr(menu,aksesAdmin) == True or isElmtInArr(menu,aksesUser) == True)) :   # perintah valid, namun tidak dijalankan karena belum login
            print('Maaf, Anda harus login terlebih dahulu untuk mengirim perintah selain "login" dan "help".')
        else :                                                                                                                      # perintah tidak valid / tidak ada
            print('Perintah Anda tidak valid. Ketik perintah "help" untuk melihat panduan penggunaan sistem.')
        main()

    else :
        if (datalogin[4] == 'ADMIN') :      # jika role dari pengguna yang login adalah admin
            if (menu == 'register') :
                FiturRegister()
            elif (menu == 'login') :
                print('Anda telah melakukan login.')
            elif (menu == 'tambah_game') :
                FiturTambahGame()
            elif (menu == 'ubah_game') :
                FiturUbahGame()
            elif (menu == 'ubah_stok') :
                FiturUbahStok()
            elif (menu == 'list_game_toko') :
                FiturListGameToko()
            elif (menu == 'search_game_at_store') :
                FiturSearchGameAtStore()
            elif (menu == 'topup') :
                FiturTopUp()
            elif (menu == 'help') :
                FiturHelp()
            elif (menu == 'save') :
                FiturSave()
            elif (menu == 'exit') :
                FiturExit()
            elif (menu == 'kerangajaib') :
                FiturMagicConchShell()
            elif (menu == 'tictactoe') :
                FiturTicTacToe()
            else :                                                      # perintah di luar akses role admin
                if (isElmtInArr(menu,aksesUser) == True) :              # jika perintah dapat diakses role user
                    print('Maaf, Anda harus menjadi user untuk menjalankan menu "' + menu + '".')
                else :                                                  # jika perintah juga tidak dapat diakses role user, yang berarti perintah tidak valid / tidak ada
                    print('Perintah Anda tidak valid. Ketik perintah "help" untuk melihat panduan penggunaan sistem.')
            
        else :                                                          # datalogin[4] == 'USER'    /   role dari pengguna yang login adalah user
            if (menu == 'login') :
                print('Anda telah melakukan login.')
            elif (menu == 'list_game_toko') :
                FiturListGameToko()
            elif (menu == 'buy_game') :
                FiturBeliGame()
            elif (menu == 'list_game') :
                FiturListMyGame()
            elif (menu == 'search_my_game') :
                FiturSearchMyGame()
            elif (menu == 'search_game_at_store') :
                FiturSearchGameAtStore()
            elif (menu == 'riwayat') :
                FiturRiwayat()
            elif (menu == 'help') :
                FiturHelp()
            elif (menu == 'save') :
                FiturSave()
            elif (menu == 'exit') :
                FiturExit()
            elif (menu == 'kerangajaib') :
                FiturMagicConchShell()
            elif (menu == 'tictactoe') :
                FiturTicTacToe()
            else :                                                      # perintah di luar akses role user
                if (isElmtInArr(menu,aksesAdmin) == True) :             # jika perintah dapat diakses role admin
                    print('Maaf, Anda tidak memiliki izin untuk menjalankan menu "' + menu + '". Mintalah ke administrator untuk melakukan hal tersebut.')
                else :                                                  # jika perintah juga tidak dapat diakses role admin, yang berarti perintah tidak valid / tidak ada
                    print('Perintah Anda tidak valid. Ketik perintah "help" untuk melihat panduan penggunaan sistem.')
        
        if (menu != 'exit') :                                           # jika perintah bukan exit, menjalankan prosedur main lagi
            main()




# ALGORITMA UTAMA
import datetime, time, argparse, os

charr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
simbol = ["-", "_"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
spasi = [" "]

datalogin = []

FiturLoad()
if run == False :
    quit()
main()