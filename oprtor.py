# Contoh penggunaan operator perbandingan

x = 10
y = 5

# Sama dengan (==)
print(x == y)   # Output: False

# Tidak sama dengan (!=)
print(x != y)   # Output: True

# Lebih besar (>)
print(x > y)    # Output: True

# Lebih kecil (<)
print(x < y)    # Output: False

# Lebih besar atau sama dengan (>=)
print(x >= y)   # Output: True

# Lebih kecil atau sama dengan (<=)
print(x <= y)   # Output: False



print('=',* 100)

#operator aritmatika
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333...
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000 (10^3)

print('=',* 100)

#operator assigment
x = 5
x += 3  # Sama dengan x = x + 3
print(x)  # 8

print('=',* 100)

#operator logika
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False



#operator bitwise
a = 5  # 101
b = 3  # 011
print(a & b)  # 001 -> 1
print(a | b)  # 111 -> 7
print(a ^ b)  # 110 -> 6
print(~a)     # Bitwise NOT -> -6



#operator identitas
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)      # True (karena b adalah referensi a)
print(a is c)      # False (meskipun nilai sama, tapi objek berbeda)



#operator membership
a = [1, 2, 3]
print(2 in a)       # True
print(4 not in a)   # True
