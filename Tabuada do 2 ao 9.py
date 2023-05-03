print('\033[7mTabuada do 2 ao 9\033[m')

for nt in range(2, 10):
    for n in range(1, 11):
        resultado = nt * n
        print(f'{nt} x {n} = {resultado}')
