print('Conselheiro do jogo de 21')
pontos = int(input('Digite o seu ponto: '))

if pontos > 21:
    print('Você perdeu')
elif pontos == 21:
    print('Parabéns você ganhou!')
elif 15 < pontos <= 20:
    print('Aconselho a parar')
elif 10 <= pontos <= 15:
    print('Há um risco, mas aconselho a comprar mais uma carta')
else:
    print('Compre mais uma carta')
