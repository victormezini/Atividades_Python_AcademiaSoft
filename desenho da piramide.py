print('\033[34m Desenho da piramide\033[m')
print()

b = int(input('Qual a altura que deseja?: '))
a1 = 1

for f in range(b - 1):
    print('*' * a1)
    a1 +=1

print('*' * a1)

for f in range(b):
    print('*' * a1)
    a1 -= 1