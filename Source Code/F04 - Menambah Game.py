# F04 - MENAMBAH GAME KE TOKO GAME


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



# ALGORITMA
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

FiturTambahGame()