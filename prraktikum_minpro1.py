# AHMAD RIBBIY ALDI (2509116100/C)
akun = ("aldi", 123)
saldo = [100]

print("")
print("==== Selamat Datang di ATM ====")

username = input("Masukkan username: ")
pin = int(input("Masukkan PIN: "))

if (username, pin) == akun:
 while True:  
    print("-" * 30)
    print("Menu ATM:")
    print("1. Cek Saldo")
    print("2. Setor Uang")
    print("3. Tarik Uang")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")
    if pilihan == "1":  
        print("Saldo Anda saat ini: Rp ",saldo[0])

    elif pilihan == "2": 
        jumlah = int(input("Masukkan jumlah setor: Rp "))
        saldo[0] += jumlah         
        print("Setor berhasil! Saldo terbaru: Rp ", saldo[0])

    elif pilihan == "3":  
        jumlah = int(input("Masukkan jumlah tarik: Rp "))
        if jumlah > saldo[0]:
            print("Saldo tidak mencukupi!")
        else:
            saldo[0] -= jumlah      
            print("Tarik berhasil! Saldo terbaru: Rp ", saldo[0])
    elif pilihan == "4":
        print("Terimakasih Telah menggunakan ATM")
        break
    else:
        print("Pilihan tidak valid!")
else:
    print("Login gagal! Username atau PIN salah.")
