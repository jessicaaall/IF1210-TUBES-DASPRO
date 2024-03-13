# F15 - LOAD


# Fungsi menghitung panjang
def lenmanual(line):

    # KAMUS LOKAL
    # count, i : int

    # ALGORITMA
    count = 0
    for i in line :
        count += 1

    return count


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



# ALGORITMA
import argparse, os

FiturLoad()