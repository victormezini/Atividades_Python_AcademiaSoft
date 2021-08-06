from random import randint

a = randint(1, 6)

b = int(input('Digite um número:'))

if a== b:
    print('Parabens você acertou')
else:
    print('Que pena você errou, o dado mostoru o número', a)
