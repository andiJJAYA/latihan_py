# #data = input('masukan data:')
# #print('data =',data)

# a = 11
# b = 5
# hasil = a + b
# print(a,'+',b,'=',hasil)

# hasil = a ** b
# print(a,'**',b,'=',hasil)

# hasil = a % b
# print(a,'%',b,'=',hasil)

# hasil = a // b
# print(a,'//',b,'=',hasil)

# a = 2
# b = 7
# c = 3

# #prioritas operasi
# hasil = a ** b / c // (a + b) % c # () prioritas
# print(a,'**',b,'/',c,'//',a,'+',b,'%',c, '=', hasil)
# Input data

nama_supplier = input("Masukkan Nama Supplier: ")
nama_barang = input("Masukkan Nama Barang: ")
jml_brg = int(input("Masukkan Jumlah Barang: "))
harga_brg = float(input("Masukkan Harga Barang: "))

total_beli = jml_brg * harga_brg
print("\nSupplier:", nama_supplier)
print("Barang:", nama_barang)
print("Total beli:", total_beli)
