print('\033[34m Jogo do dado Piratas do caribe\033[m')
print()

from random import randint

dado1 = randint(1, 6)
dado2 = randint(1, 6)
dado3 = randint(1, 6)
dado4 = randint(1, 6)
dado5 = randint(1, 6)
dado6 = randint(1, 6)

resultado = dado1 + dado2 + dado3 + dado4 + dado5 + dado6
n = int(input('veja se está com sorte! Digite um número: '))
if n == resultado:
    print('Parece que a sorte está do seu lado, o resultado foi', n)
else:
    print('HAHAHA A sorte não está mais do eu lado, o resultado foi ', resultado)