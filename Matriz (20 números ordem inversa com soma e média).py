print('\033[34mMatriz (20 números ordem inversa com soma e média)\033[m')
print()

l = []

for v in range(5):
    n = int(input('Digite um número inteiro: '))
    l.append(n)

l.reverse()
print(l)