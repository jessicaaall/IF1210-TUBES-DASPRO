# F03 - LOGIN


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



# ALGORITMA 
charr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
simbol = ["-", "_"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
spasi = [" "]

datalogin = []

FiturLogin()