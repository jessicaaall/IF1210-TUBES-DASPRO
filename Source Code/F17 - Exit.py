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



# ALGORITMA
FiturExit()