# B02 - MAGIC CONCH SHELL


# Fungsi menghitung panjang
def lenmanual(line):

    # KAMUS LOKAL
    # count, i : int

    # ALGORITMA
    count = 0
    for i in line :
        count += 1

    return count


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



# ALGORITMA
import time

FiturMagicConchShell()