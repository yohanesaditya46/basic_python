import os
nama = []
telepon=[]
awal = 0

while True:
    print ("Selamat Datang!")
    print("--Menu--")
    print (" 1.Daftar Kontak\n 2.Tambah Kontak\n 3.Keluar")
    pilihan = int(input("Masukkan Pilihan\t: "))

    if pilihan == 2 :
        os.system('cls')
        nama1 = input("Nama\t : ")
        nama.append(nama1)
        telepon1 = int (input("Nomor Telepon\t : "))
        telepon.append(telepon1)
        print ("Kontak berhasil ditambahkan")
        awal += 1
    elif pilihan == 1 :
        os.system('cls')
        print("Daftar Kontak")
        print("--------------")
        for i in range (0,awal):
            print(str (i+1) + "."+ "Nama\t :" + str (nama[i]))
            print ("Nomor Telepon\t : " + str (telepon[i]))
        
    elif pilihan == 3:
        os.system('cls')
        print("Sampai Jumpa\n")
        continue