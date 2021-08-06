print('\033[34m Jogo da velha modificado \033[m')
print()

velha = []
for i in range(9):
    linha = []
    for l in range(9):
        linha.append('_')
    velha.append(linha)

peca = 'X'
while True:
    for lin in range(9):
        for col in range(9):
            print(velha[lin][col], end=' ')
        print()

    lin = int(input('\033[31m Digite a linha escolhida: \033[m'))
    print()
    col = int(input('\033[31m Digite a coluna escolhida: \033[m'))

    velha[lin][col] = peca

    if peca == 'X':
        peca = 'O'
    else:
        peca = 'X'