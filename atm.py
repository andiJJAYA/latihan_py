# Penarikan Tunai : Menarik uang tunai dari rekening.
# Setoran Tunai : Menyetor uang tunai ke rekening.
# Cek Saldo : Melihat jumlah saldo yang tersedia di rekening.
# Transfer : Mengirim uang antar rekening, baik di bank yang sama maupun berbeda.
# Tagihan Pembayaran : Membayar berbagai tagihan seperti listrik, udara, dan telepon.
# Pembelian Pulsa : Membeli pulsa telepon seluler.
# Cetak Bukti Transaksi : Mencetak struk sebagai bukti transaksi yang telah dilakukan.
# Ganti PIN : Mengubah nomor identifikasi pribadi (PIN) untuk keamanan.

print('selamat datang di ATM saya')
print('masukan dulu jumblahm uang kamu!!')
setor = int(input('masukan setoran kamu : Rp.'))
print('pilih option :')
print('1. cek saldo')
print('2. tarik tunai')
print('3. setor tunai')
print('4. transfer uang')
print('5. ganti pin')
print('6. beli pulsa')


saldo = setor 

while True:
    option = int(input('silahkan pilih option :'))
    
    if option == 1:
        print(f'Saldo kamu Berjumblah Rp.{saldo}')
        print('pilih menu')
        print('1. kembali ke menu awal')
        print('2. program berhenti')
        pilih = int(input('masukan nomer(1/2):'))
        if pilih == 2:
            print('Terima kasih! Program selesai.')
            break
    
    elif option == 2:
        tarik = int(input('Masukkan jumlah tarik tunai: '))
        if tarik > saldo:
            print('Saldo tidak cukup!')
        else:
            saldo -= tarik
            print(f'Anda telah menarik Rp.{tarik}. Saldo sekarang Rp.{saldo}')
            print('1. kembali ke menu awal')
            print('2. program berhenti')
            pilih = int(input('masukan nomer(1/2):'))
            if pilih == 2:
                print('Terima kasih! Program selesai.')
                break
    
    elif option == 3:
        setor = int(input('Masukkan jumlah setor tunai: '))
        saldo += setor
        print(f'Anda telah setor Rp.{setor}. Saldo sekarang Rp.{saldo}')
        print('1. kembali ke menu awal')
        print('2. program berhenti')
        pilih = int(input('masukan nomer(1/2):'))
        if pilih == 2:
            print('Terima kasih! Program selesai.')
            break

    elif option==4:
        no_rek = int(input('masukan no rekening :'))
        transfer = int(input('masukan nominal transferan :'))
        if transfer > saldo:
            print('Saldo tidak cukup!')
        else:
            saldo -= transfer
            print(f'transferan berjumblah : {transfer}, kamu berhasil mengirim ke no rekening ({no_rek}), sisa saldo kamu berjumblah ({saldo})')
            print('1. kembali ke menu awal')
        print('2. program berhenti')
        pilih = int(input('masukan nomer(1/2):'))
        if pilih == 2:
            print('Terima kasih! Program selesai.')
            break
    elif option==5:
        dulu = int(input('masukan 6 pin dulu :'))
        sekarang = int(input('masukan 6 pin baru :'))
        print(f'pin berhasil diubah, dari {dulu}, ke pin baru, ini adalah pin anda : {sekarang}')
        print('1. kembali ke menu awal')
        print('2. program berhenti')
        pilih = int(input('masukan nomer(1/2):'))
        if pilih == 2:
            print('Terima kasih! Program selesai.')
            break
    elif option == 6:
        print('selamat datang di jasa pelayanan beli pulsa')
        print('='*40)
        print('1. pulsa : 10.000/rp.12.000')
        print('2. pulsa : 15.000/rp.17.000')
        print('3. pulsa : 20.000/rp.22.000')
        masukan = int(input('masukan pulihan anda :'))
        if masukan == 1:
            harga = 12000
            if saldo > harga:
                saldo -= harga
                print(f'yeah!! selamat pulsa (10.000) anda berhasil terbeli Rp.12.000, saldo anda sekarang {saldo}')
            else:
                print('Saldo tidak cukup!')
        elif masukan == 2:
            harga = 17000
            if saldo > harga:
                saldo -= harga
                print(f'yeah!! selamat pulsa (15.000) anda berhasil terbeli Rp.17.000, saldo anda sekarang {saldo}')
            else:
                print('Saldo tidak cukup!')
        elif masukan ==3:
            harga=22000
            if saldo > harga:
                saldo -= harga
                print(f'yeah!! selamat pulsa (20.000) anda berhasil terbeli Rp.22.000, saldo anda sekarang {saldo}')
            else:
                print('Saldo tidak cukup!')
        else:
            print('pilihan tidak validd')
            print('1. kembali ke menu awal')
            print('2. program berhenti')
            pilih = int(input('masukan nomer(1/2):'))
            if pilih == 2:
                print('Terima kasih! Program selesai.')
                break
            
    else:
        print('Pilihan tidak valid, silakan coba lagi.')


def display_menu():
    print('Selamat datang di ATM saya')
    print('Masukkan dulu jumlah uang kamu!!')
    setor = int(input('Masukkan setoran kamu: Rp. '))
    return setor

def display_options():
    print('Pilih opsi:')
    print('1. Cek saldo')
    print('2. Tarik tunai')
    print('3. Setor tunai')
    print('4. Transfer uang')
    print('5. Ganti PIN')
    print('6. Beli pulsa')

def check_saldo(saldo):
    print(f'Saldo kamu berjumlah Rp.{saldo}')

def tarik_tunai(saldo):
    tarik = int(input('Masukkan jumlah tarik tunai: '))
    if tarik > saldo:
        print('Saldo tidak cukup!')
    else:
        saldo -= tarik
        print(f'Anda telah menarik Rp.{tarik}. Saldo sekarang Rp.{saldo}')
    return saldo

def setor_tunai(saldo):
    setor = int(input('Masukkan jumlah setor tunai: '))
    saldo += setor
    print(f'Anda telah setor Rp.{setor}. Saldo sekarang Rp.{saldo}')
    return saldo

def transfer_uang(saldo):
    no_rek = input('Masukkan no rekening: ')
    transfer = int(input('Masukkan nominal transferan: '))
    if transfer > saldo:
        print('Saldo tidak cukup!')
    else:
        saldo -= transfer
        print(f'Transferan berjumlah: Rp.{transfer}, kamu berhasil mengirim ke no rekening ({no_rek}), sisa saldo kamu berjumlah Rp.{saldo}')
    return saldo

def ganti_pin():
    dulu = input('Masukkan PIN lama (6 digit): ')
    sekarang = input('Masukkan PIN baru (6 digit): ')
    print(f'PIN berhasil diubah dari {dulu} ke PIN baru: {sekarang}')

def beli_pulsa(saldo):
    print('Selamat datang di jasa pelayanan beli pulsa')
    print('=' * 40)
    print('1. Pulsa: 10.000 / Rp. 12.000')
    print('2. Pulsa: 15.000 / Rp. 17.000')
    print('3. Pulsa: 20.000 / Rp. 22.000')
    
    masukan = int(input('Masukkan pilihan Anda: '))
    
    if masukan == 1:
        harga = 12000
    elif masukan == 2:
        harga = 17000
    elif masukan == 3:
        harga = 22000
    else:
        print('Pilihan tidak valid.')
        return saldo
    
    if saldo >= harga:
        saldo -= harga
        print(f'Yeah!! Pulsa berhasil terbeli, saldo Anda sekarang Rp.{saldo}')
    else:
        print('Saldo tidak cukup!')
    
    return saldo

def main():
    saldo = display_menu()
    
    while True:
        display_options()
        option = int(input('Silakan pilih opsi: '))
        
        if option == 1:
            check_saldo(saldo)
        elif option == 2:
            saldo = tarik_tunai(saldo)
        elif option == 3:
            saldo = setor_tunai(saldo)
        elif option == 4:
            saldo = transfer_uang(saldo)
        elif option == 5:
            ganti_pin()
        elif option == 6:
            saldo = beli_pulsa(saldo)
        else:
            print('Pilihan tidak valid, silakan coba lagi.')

        # Ask if the user wants to return to the menu or exit
        if input('Apakah Anda ingin kembali ke menu? (y/n): ').lower() != 'y':
            print('Terima kasih! Program selesai.')
            break

if __name__ == "__main__":
    main()


def greet(name):
    print(f'hello {name}')

if __name__ == '__main__':
    greet('sarip')