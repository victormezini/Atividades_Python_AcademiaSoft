print('\033[34mMatriz (Maior e Menor)\033[m')
print()

l = []
for v in range(5):
    n = int(input('Digite um número inteiro:'))
    l.append(n)

l.sort()

print(l)

print()

print('O maior número digitado é: ', l[4])

print()

print('O menor número digitado foi: ', l[0])
