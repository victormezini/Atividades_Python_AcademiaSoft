print('\033[34mMatriz (20 números em ordem inversa)\033[m')
print()

l = []

for v in range(20):
    n = int(input('Digite um número inteiro: '))
    l.append(n)

l.reverse()

print(l)
