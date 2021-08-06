pessoas = ['Maria', 'Joao', 'Alberto', 'Alvaro', 'Jessica', 'Joao']
print()
print('Lista de pessoas: ', pessoas)
pos = 0
while pos != - 1:
try:
    pos = pessoas.index('Joao', pos)
    print('Encontrado na posição:', pos)
    pos += 1
except:
    pos = - 1
print('Fim do programa')