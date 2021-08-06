from random import randint

jogando = true
while jogando == true:
    a = randint(1, 6)
    b = int(input('Digite um número entre 1 e 6, ou 0 para sair:'))
    if b == 0:
        #break
        jogando = false
        continue

    if b > 6 or b < 0:
         print('Numero invalido')
         # continue
    else:
         if a== b:
               print('Parabens você acertou')
          else:
               print('Que pena você errou, o dado mostoru o número', a)