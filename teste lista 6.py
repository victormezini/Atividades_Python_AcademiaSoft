pessoas = ['Maria', 'Joao', 'Alberto', 'Alvaro', 'Jessica', 'Joao']

pessoas_novas = ['Luiz', 'Fatima', 'Marilia']
print('Lista de pessoas: ', pessoas)
pessoas.extend(pessoas_novas)
print('Lista de pessoas: ', pessoas)
print('Há:', pessoas.count('Maria'), 'Maria(s) na lista de pessoas')
print('Há:', pessoas.count('Joao'), 'Joao(s) na lista de pessoas')
pessoas_copia = pessoas.copy()
pessoas.remove('Maria')
print(pessoas_copia)

pessoas.reverse()
print(pessoas)