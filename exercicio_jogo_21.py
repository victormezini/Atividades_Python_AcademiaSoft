print('Conselheiro do jogo de 21')
pontos = int(input('Digite o seu ponto: '))

if pontos > 21:
    print('você perdeu')
elif pontos == 21:
    print('Parabens você ganho')
elif pontos > 15 and pontos <= 20:
    print('Aconselho a parar')
elif pontos <= 15 and pontos >= 10:
    print('Há um risco mas aconselho a comprar mais uma carta')
else:
    print('Compre mais uma carta')
