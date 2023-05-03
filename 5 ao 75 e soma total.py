print('\033[34m5 ao 75 e a soma total\033[m\n')
print('\033[32mNúmero   Soma Total\033[m\n')

numero = 5
soma_total = 5

while numero <= 75:
    print(f'{numero:<8}-------------- {soma_total}')
    numero += 1
    soma_total += numero
