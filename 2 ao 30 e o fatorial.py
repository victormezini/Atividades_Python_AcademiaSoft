from math import factorial

print('\033[34m2 ao 30 e o fatorial\033[m\n')
print('\033[32mNúmero   Fatorial\033[m\n')

for numero in range(2, 31):
    print(f'{numero:<8}---------- {factorial(numero)}! =')
