pessoas = ['Maria', 'Joao', 'Alberto', 'Alvaro', 'Jessica']

print('Antes do insert: ', pessoas)
pessoas.insert(2, 'Fernando')
print('Depois: ', pessoas)
pessoas.remove('Alvaro')
print('Depois do remove: ', pessoas)
#del pessoas [2]
p = pessoas.pop(2)
# p = pessoas.pop(2)
del pessoas[2]
print('Depois do Del:')