# def total_beli(harga, jumblah):
#     return harga * jumblah

# harga = int(input('Masukkan harga: '))
# jumblah = int(input('Masukkan jumlah: '))
# hasil = total_beli(harga, jumblah)

# if hasil >= 500:
#     potongan = hasil * 0.1 
# else:
#     potongan = hasil * 0.05  

# total_bayar = hasil - potongan

# print(f'Total beli: {hasil}')
# print(f'Potongan: {potongan}')
# print(f'Total bayar setelah potongan: Rp. {total_bayar}')


def lihat_inventaris(inventaris):
    print("Inventaris saat ini:")
    if not inventaris:
        print("Inventaris kosong.")
    else:
        for barang, jumlah in inventaris.items():
            print(f"{barang}: {jumlah}")

def tambah_barang(inventaris):
    barang = input("Masukkan nama barang yang ingin ditambahkan: ")
    jumlah = int(input("Masukkan jumlah barang yang ingin ditambahkan: "))
    if barang in inventaris:
        inventaris[barang] += jumlah
        print(f"Jumlah {barang} berhasil ditambahkan. Total sekarang: {inventaris[barang]}")
    else:
        inventaris[barang] = jumlah
        print(f"Barang {barang} berhasil ditambahkan dengan jumlah: {jumlah}")

def hapus_barang(inventaris):
    barang = input("Masukkan nama barang yang ingin dihapus: ")
    if barang in inventaris:
        del inventaris[barang]
        print(f"Barang {barang} berhasil dihapus dari inventaris.")
    else:
        print(f"Barang {barang} tidak ditemukan dalam inventaris.")

def ubah_jumlah_barang(inventaris):
    barang = input("Masukkan nama barang yang ingin diubah jumlahnya: ")
    if barang in inventaris:
        jumlah = int(input("Masukkan jumlah baru: "))
        inventaris[barang] = jumlah
        print(f"Jumlah {barang} berhasil diubah menjadi: {jumlah}")
    else:
        print(f"Barang {barang} tidak ditemukan dalam inventaris.")


def main():
    inventaris = {}
    
    print('masukan 5 nama dan jumblah barang yang akan muncul di inventaris')
    barang = input("Masukkan nama barang: ")
    barang = input("Masukkan nama barang: ")
    barang = input("Masukkan nama barang: ")
    barang = input("Masukkan nama barang: ")
    barang = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))
    inventaris[barang] = jumlah
    
    while True:
        print("\nMenu:")
        print("1. Lihat Inventaris")
        print("2. Tambah Barang")
        print("3. Hapus Barang")
        print("4. Ubah Jumlah Barang")
        print("5. Keluar")
        
        opsi = int(input("Pilih opsi: "))
        
        if opsi == 1:
            lihat_inventaris(inventaris)
        elif opsi == 2:
            tambah_barang(inventaris)
        elif opsi == 3:
            hapus_barang(inventaris)
        elif opsi == 4:
            ubah_jumlah_barang(inventaris)
        elif opsi == 5:
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

if __name__ == '__main__':
    main()