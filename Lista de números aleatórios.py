print('\033[34m lista de números aleatórios\033[m')
print()

from random import randint

l=[]

for y in range(100):
    t = randint(1, 100)
    l.append(t)

print(l)