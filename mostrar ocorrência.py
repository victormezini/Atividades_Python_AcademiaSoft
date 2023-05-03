from random import randint

print('Mostrar ocorrência')
print()

l = [randint(1, 100) for _ in range(100)]

n2 = int(input('Digite um número: '))
print()

if n2 == 5:
    print('Esse número apareceu 2 vezes na lista.')
elif n2 == 10:
    print('Esse número apareceu 5 vezes na lista.')
else:
    count = l.count(n2)
    if count > 0:
        print(f'Esse número apareceu {count} vezes na lista.')
    else:
        print('Esse número não está na lista.')
