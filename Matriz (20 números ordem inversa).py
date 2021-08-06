print('\033[34mMatriz (20 números ordem inversa)\033[m')
print()

l = []
while v in range(20):
    n = int(input('Digite um número inteiro:'))
    l.append(n)
l.reverse()

print(l)
