# F16 - SAVE


# Fungsi menghitung panjang
def lenmanual(line) :

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



# ALGORITMA
import os

charr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
simbol = ["-", "_"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
spasi = [" "]

FiturSave()