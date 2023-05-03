print('\033[34mLista de números aleatórios\033[m')
print()

from random import randint

l = [randint(1, 100) for _ in range(100)]
print(l)
