print('pilih menu apa?')
print('='*50)
print('1. minuman?')
print('2. maskanan?')
menu = int(input('masukan pilihan anda (1/2):'))

if menu == 1:
    option = input('anda mau milih minumana apa?')
    print('minuman pilihan anda : {}'.format(option))
    print('='*50)
    pilih = input('pilih (dingin/panas):')
    if pilih== 'es':
        print('minuman anda dingin, ditunggu ya!!')
        print('terimakasihhh')
    elif pilih == 'panas':
        print('minuman anda panas, ditunggu ya!!')
        print('terimakasihhh')
    else:
        print('invalid pilihan anda')
elif menu == 2:
    optiion = input('anda mau milih makanan apa?')
    print('makanan pilihan anda : {}'.format(optiion))
    print('='*50)
    print('1. makan disini')
    print('2. dibawa pulang/dibungkus')
    apa = int(input('masukan pilihan anda (1/2):'))
    if apa == 1:
        print('anda makan disini, ditunggu ya pesanana anda!!')
        print('terimakasihhh')
    elif apa == 2:
        print('makanan anda dibungkus, ditunggu ya pesanana anda!!')
        print('terimakasihhh')
    else:
        print('invalid pilihan anda')
else:
    print('maaf pilihan anda invalid')