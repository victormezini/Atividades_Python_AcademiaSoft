print('\033[34mMatriz (20 números com soma e média aritmética)\033[m')
print()

l = []
for v in range(20):
    n = int(input('Digite um número inteiro:'))
    l.append(n)

soma = sum(l)
media = soma / len(l)

print('Números ------------- Soma -------------- Média')
print()
print('{} -------------- {} -------------- {}'.format(l, soma, media))
