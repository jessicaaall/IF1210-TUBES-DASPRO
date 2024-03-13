# F02 - REGISTER


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



# ALGORITMA 
charr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
simbol = ["-", "_"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
spasi = [" "]

FiturRegister()