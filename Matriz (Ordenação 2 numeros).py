print('\033[34mMatriz (Ordenação 2 numeros)\033[m')
print()

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    n1, n2 = n2, n1

print([n1, n2])
