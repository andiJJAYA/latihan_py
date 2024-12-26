# c = input('masukan angka :')

#no 1
angka1=float(input("masukkan bilangan 1 :"))
angka2=float(input("masukkan bilangan 2 :"))

penjumlahan= angka1 + angka2
pengurangan= angka1 - angka2
pembagian= angka1 / angka2
perkalian= angka1 * angka2

print("hasil dari penjumlahan",penjumlahan)
print("hasil dari pengurangan",pengurangan)
print("hasil dari pembagian",pembagian)
print("hasil dari perkalian",perkalian)

# no 2
def jumlah(angka1,angka2):
    return angka1 +angka2

a = int(input('masukan angka 1 :'))
b = int(input('masukan angka 2 :'))

hasil =jumlah(a,b)
print(f'hasil',(hasil))

#no 3
angka = int(input('masukan angka:'))
if angka % 2 == 0:
    print('angka genap')
else:
    print('angka ganjil')

list_hari = ['senin','selasa','rabu','kamis','jumat','sabtu','minggu']
pertama = list_hari[0]
terakhir = list_hari[-1]
keempat = list_hari[3]
print(f'hari pertama',(pertama),'hari terakhir',(terakhir),'hari keempat',(keempat))
