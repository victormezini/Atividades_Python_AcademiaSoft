print('\033[34mMatriz (Ordenação 2 numeros)\033[m')
print()

l = []
for v in range(2):
    n = int(input('Digite um número inteiro: '))
    l.append(n)
    l.sort()
print(l)