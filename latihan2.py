# nilai = int(input('masukan nilai ujianmu :'))
# if 85 <= nilai <= 100:
#     print('nilai kamu A')
# elif 70 <= nilai <= 84:
#     print('nilai kamu B')
# elif 55 <= nilai <= 69:
#     print('nilai kamu C')
# elif 40 <= nilai <= 54:
#     print('nilai kamu D')
# elif  nilai < 39:
#     print('nilai kamu E')
# else:
#     print('jangan masukan yang gak ada')

# angka = int(input('masukan angka dari 1-7 :'))
# if angka==1:
#     print('hari senin')
# elif angka==2:
#     print('hari selasa')
# elif angka==3:
#     print('hari rabu')
# elif angka==4:
#      print('hari kamis')

# bb = float(input('masukan berat badan anda :'))
# tb = float(input('masukan tinggi badan anda :'))

# bmi = bb/ (tb **2)
# if bmi < 18.5:
#     print('kurus')
# elif 18.5 <= bmi < 24.9:
#     print('normal')
# elif 25 <= bmi < 29.9:
#     print('overhit')
# else:
#     print('opsite')

# Meminta input berat badan dan tinggi badan dari pengguna
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

# Menghitung BMI
bmi = berat / (tinggi ** 2)

# Menentukan kategori BMI
if bmi < 18.5:
    kategori = "Kurus"
elif 18.5 <= bmi < 24.9:
    kategori = "Normal"
elif 25 <= bmi < 29.9:
    kategori = "Overweight"
else:
    kategori = "Obesitas"

# Mencetak hasil
print(f"BMI Anda adalah: {bmi:.2f}")
print(f"Kategori BMI: {kategori}")
