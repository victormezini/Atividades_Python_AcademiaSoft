print('\033[34m desenho de um retângulo\033[m')
print()

b = int(input('Informe a altura do retângulo: '))
print()
c = int(input('Informe a largura do retângulo: '))
print()

for a in range(b):
    print('*' * c)