print('\033[34m Jogo pedra papel e tesoura\033[m')
print()

from random import randint

escolhas = ('pedra', 'papel', 'tesoura')
maquina = randint(0, 2)

print('''\033[35msuas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA\033[m''')
print()

player = int (input('\033[32m Então, qual vai ser a sua jogada?:\033[m '))
print()

print('O seu adversario escolheu {}'.format(escolhas[maquina]))
print()
print('Sua jogada foi essa: {}'.format(escolhas[player]))
print()

if maquina == 0:
    if player == 0:
        print ('Ops! Vocês empataram')
    elif player == 1:
        print ('Parabèns! Você ganhou o jogo')
    elif player == 2:
        print ('Que pena, você perdeu')
    else:
        print ('Algo de errado não está certo')
elif maquina == 1:
    if player == 0:
        print ('Que pena, você perdeu')
    elif player == 1:
        print ('Ops! Vocês empataram')
    elif player == 2:
        print ('Parabèns! Você ganhou o jogo')
    else:
        print ('Algo de errado não está certo')
elif maquina == 2:
    if player == 0:
        print ('Parabèns! Você ganhou o jogo')
    elif player == 1:
        print ('Que pena, você perdeu')
    elif player == 2:
        print ('Ops! Vocês empatarame')
    else:
        print ('Algo de errado não está certo')