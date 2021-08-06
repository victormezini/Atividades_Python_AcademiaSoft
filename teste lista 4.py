pessoas = ['Maria', 'Joao', 'Alberto', 'Alvaro', 'Jessica', 'Joao']
print()
print('Lista de pessoas: ', pessoas)
print()
try:
    n = pessoas.index('Joao', 2)
    print('Encontrado a Joao na posição:', n)
except:
      print('Não encontrou o Joao')
print()
print('Fim do programa')