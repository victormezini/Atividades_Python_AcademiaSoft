print('\033[34mMatriz (Ordenação 3 numeros)\033[m')
print()

l = []
for v in range(3):
    n = int(input('Digite um número inteiro: '))
    l.append(n)
l.sort()
print(l)
