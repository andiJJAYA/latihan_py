# # lebih dari >
# # kurang dari <

# # umur=int(input('masukan umur:'))
# # if umur > 13:
# #     print('aku masih kecil')
# x = int(input('masukan nomer'))
# if x > 10:
#     print("x lebih besar dari 10")
# elif x == 10:
#     print("x sama dengan 10")
# else:
#     print("x kurang dari 10")

# Program untuk menunjukkan penggunaan operator logika

# # Input dari pengguna
# age = int(input("Masukkan umur Anda: "))
# has_permission = input("Apakah Anda memiliki izin (ya/tidak)? ")
# is_student = input("Apakah Anda seorang pelajar (ya/tidak)? ")

# # Menggunakan operator and
# if age >= 18 and has_permission:
#     print("Anda dapat memasuki acara.")
# else:
#     print("Anda tidak dapat memasuki acara.")

# # Menggunakan operator or
# if age < 18 or is_student:
#     print("Anda dapat menikmati tiket diskon.")
# else:
#     print("Anda tidak memenuhi syarat untuk tiket diskon.")

# # Menggunakan operator not
# if not has_permission:
#     print("Anda perlu izin untuk mengikuti acara.")
# else:
#     print("Izin Anda telah dikonfirmasi.")


# Soal 1: Cek Bilangan Genap atau Ganjil
# number = int(input("Masukkan sebuah bilangan bulat: "))
# if number % 2 == 0:
#     print("Bilangan tersebut genap.")
# else:
#     print("Bilangan tersebut ganjil.")

# #soal no 2
umur = int(input('masukan umur kamu:'))
if umur < 12:
    print('kamu adalah anak')
elif 12 <= umur <= 17:
    print('kamu adalah remaja')
elif 18 <= umur <= 40:
    print('kamu adalah dewasa')
else: 
    print('kamu adalah tua bngt')

#soal no 3
# pw = input('masukan pasword :')
# if pw == 'rahasia':
#     print('pw benar')
# else:
#     print('pw salah')

# # Soal 4: Cek Nilai
# nilai = int(input("Masukkan nilai (0-100): "))
# if 90 <= nilai <= 100:
#     print("Anda mendapat A.")
# elif 80 <= nilai < 90:
#     print("Anda mendapat B.")
# elif 70 <= nilai < 80:
#     print("Anda mendapat C.")
# elif 60 <= nilai < 70:
#     print("Anda mendapat D.")
# elif 0 <= nilai < 60:
#     print("Anda mendapat F.")
# else:
#     print("Nilai tidak valid. Harap masukkan nilai antara 0 hingga 100.")

# soal no 5
# bilangan = float(input("Masukkan sebuah bilangan: "))

# if bilangan > 0:
#     print("Bilangan tersebut positif.")
# elif bilangan < 0:
#     print("Bilangan tersebut negatif.")
# else:
#     print("Bilangan tersebut adalah nol.")
