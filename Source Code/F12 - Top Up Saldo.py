# F12 - TOP UP SALDO


# Fungsi menghitung panjang
def lenmanual(line) :

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



# ALGORITMA
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbol = ['-', '+']

FiturTopUp()