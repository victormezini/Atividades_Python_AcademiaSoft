print('\033[7mTabuada do 2 ao 9\033[m')

for nt in range(2, 10, 1):
    for n in range(1, 11, 1):
        resultado = nt * n
        print(nt, 'x', n, '=', resultado)