print('\033[34m 2 ao 30 e o fatorial\033[m')
print()
print('\033[32mNúmero ---------Fatorial\033[m')
print()

from math import factorial

for numero in range(2, 31, 1):
    print('{} ---------- {}! =' .format(numero,numero), factorial(numero))