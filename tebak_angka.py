import random

angkamin = 1
angkamaks =15
angkarahasia = random.randint(angkamin,angkamaks)

print('progam tebak angka')
print('kami sudah menyiapkan angka rahasia dari 1 sampai 10 silahkan tebak')
print('='*30)

while True:
    jawaban = int(input('masukan tebakan anda :'))
    if jawaban == angkarahasia:
        print('selamat, tebakan benar :',angkarahasia)
        break
    elif jawaban > angkarahasia:
        print("tebakan anda terlalu besar")
    else:   
        print('tebakan anda terlalu kecil')



# print('='*50)
# print('kalkulator sederhana')
# print('='*50)
# print('\n')
# angka1 = int(input('masukan angka pertama :'))
# angka2 = int(input('masukan angka kedua :'))
# operator = input('pilih operator(+,*,/,-):')
# if operator == '+':
#     hasil = angka1 + angka2
#     print(hasil)
# elif operator=='-':
#     hasil = angka1 + angka2
#     print(hasil)
# elif operator=='/':
#     hasil = angka1 + angka2
#     print(hasil)
# elif operator== '*':
#     hasil = angka1 + angka2
#     print(hasil)
# else:
#     print('jangan maksakan yang gak ada yah!!')