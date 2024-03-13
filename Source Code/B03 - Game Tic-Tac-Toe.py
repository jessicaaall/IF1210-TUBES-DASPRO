# B03 - GAME TIC-TAC-TOE


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



# ALGORITMA
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

FiturTicTacToe()