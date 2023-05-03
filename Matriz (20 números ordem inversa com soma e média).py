print('\033[34mMatriz (20 números ordem inversa com soma e média)\033[m')
print()

l = []

for v in range(20):
    n = int(input('Digite um número inteiro: '))
    l.append(n)

l.reverse()

soma = sum(l)
media = soma / len(l)

print('Números ------------- Soma -------------- Média')
print('{} -------------- {} -------------- {}'.format(l, soma, media))
