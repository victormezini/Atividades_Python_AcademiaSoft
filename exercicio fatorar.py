print('\033[7m Exercicio de fatoração \033[m')

numero = int(input('Digite um número: '))

for i in range(1, numero+1):
    fator = i * (i - 1)
    print(f'{i} x {i-1} = {fator}')
