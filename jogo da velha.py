print('\033[34m Jogo da velha \033[m')
print()

velha = []
for i in range(3):
    linha = []
    for l in range(3):
        linha.append('_')
    velha.append(linha)

peca = 'X'
while True:
    for lin in range(3):
        for col in range(3):
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