print('\033[34m Ordenar 10 números\033[m')
print()

l=[]

for x in range(10):
    n = int(input('digite um numero inteiro: '))
    l.append(n)
    l.sort()
print(l)