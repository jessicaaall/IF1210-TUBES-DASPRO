# B01 - CIPHER


# Fungsi menghitung panjang
def lenmanual(line):

    # KAMUS LOKAL
    # count, i : int

    # ALGORITMA
    count = 0
    for i in line :
        count += 1

    return count



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

