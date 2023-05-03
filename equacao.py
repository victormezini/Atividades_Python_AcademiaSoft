from math import sqrt

print('\033[1mPrograma de equação de segundo grau\033[m')
nome = input('Digite o seu nome: ')
ra = int(input('Digite o seu RA: '))
programa = input('Coloque o nome do programa: ')

print('*' * 93)
print(f'******    Programação II - 2º Ciclo Jogos Digitais {" " * 30}******')
print(f'******    Nome: {nome}{" " * (39 - len(nome))} RA: {ra}{" " * (22 - len(str(ra)))}******')
print(f'******    Programa: {programa}{" " * (40 - len(programa))}******')
print('*' * 93)

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = b ** 2 - 4 * a * c
raizdelta = sqrt(delta)

if delta >= 0:
    x1 = (-b + raizdelta) / (2 * a)
    x2 = (-b - raizdelta) / (2 * a)
    print(f'x1 = {x1:.2f}')
    print(f'x2 = {x2:.2f}')
else:
    parte_real = -b / (2 * a)
    parte_imaginaria = abs(raizdelta) / (2 * a)
    print(f'x1 = {parte_real:.2f} + {parte_imaginaria:.2f}i')
    print(f'x2 = {parte_real:.2f} - {parte_imaginaria:.2f}i')
