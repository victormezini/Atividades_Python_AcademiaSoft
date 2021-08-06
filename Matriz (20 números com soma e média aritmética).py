print('\033[34mMatriz (20 números com soma e média aritmética)\033[m')
print()

l = []
for v in range(20):
    n = int(input('Digite um número inteiro:'))
    l.append(n)

s1 = n
s2 = n

m = (n * n * n * n * n * n * n * n * n * n * n * n * n * n * n * n * n * n * n * n) / 4

while s1 <=n:
 s2 += s1 + 1
 s1 += 1

#s = (n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n)

#m = (n * n * n * n * n * n * n * n * n * n * n * n * n * n * n * n * n * n * n * n) / 4

print('Números ------------- Soma -------------- Média')

print()

print('\n{} -------------- {} -------------- {}'.format(l, s2, m))
