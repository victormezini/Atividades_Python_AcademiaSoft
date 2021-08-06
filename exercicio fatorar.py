print('\033[7m Exercicio de fatoração \033[m')

numero = int(input('Digite um numero: '))

for numero in range(0, numero+1, 1):
    fator = numero * numero -1

    print(fator)