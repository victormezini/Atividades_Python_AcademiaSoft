print('\033[34m Desenho de um triângulo\033[m')
print()

al = int(input('Qual a altura que você quer: '))

print()

la = int(input('Informe a largura: '))
n = 1

for a in range (al):
    for a in range(la):
        while n <= la:
            print('*' * n)
            n +=1

