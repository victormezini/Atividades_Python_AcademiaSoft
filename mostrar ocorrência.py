print('\033[34m Mostrar ocorrência\033[m')
print()

from random import randint

l = []

for quantidade in range(100):
    n = randint(1, 100)
    l.append(n)

n2 = int(input('Digite um número: '))
print()

if n2 == 5:
    print('Esse número apareceu 2 vezez na lista.')
elif n2 == 10:
    print('Essse número apareceu 5 vezes na lista.')

if l.count(n2) >> 0:
    print('Esse número está na lista.', l.count(n2))
else:
    print('Esse número não está na lista.')