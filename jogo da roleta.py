print('\033[34mJogo da roleta\033[m')
print()

import random
money_player = float('1000')
money_machine = float('5000')
while money_player > 0:
        print('\033[31m Você tem a quantia de: \033[m', money_player)
        print('\033[31m O banco tem a quantia de :\033[m', money_machine)
        numeros = [0,36]
        print('\nEscolha uma aposta, sendo:\nAposta 1: numero impar \nAposta 2: numero par \nAposta 3: numero especifico entre 0 e 36')
        print()
        aposta = int(input('\033[35m Qual vai ser a sua aposta? 1, 2 ou 3 ?\033[m'))

        if aposta == 1:
            investimento = float(input('Quanto vai de apostar ?'))

        elif aposta == 2:
            investimento = float(input('Quanto vai de apostar ?'))

        elif aposta == 3:
            numero = input('\033[35m Qual número que você gostaria de apostar ?\033[m')
            investimento = float(input('\033[35m Quanto que você gostaria de apostar ?\033[m'))
        print('Somente numeros entro 1 e 3')
        print('O número selecionado foi:')
        sort = (random.randrange(0,36))
        print(sort)

        if (aposta == 1) and not(sort %2 == 0):
            print('Parabéns! Você ganhou !')
            money_player = (money_player + (investimento*2))
            money_machine = (money_machine - (investimento*2))

        elif (aposta == 2) and (sort %2 == 0):
            print('Parabéns! Você ganhou !')
            money_player = (money_player + (investimento*2))
            money_machine = (money_machine - (investimento*2))

        elif (aposta == 3) and (sort == numero):
            print('voce ganhou !')
            money_player = (money_player + (investimento*30))
            money_machine = (money_machine - (investimento*30))

        elif (aposta == 3) and not(sort == numero):
            print('Que pena, você perdeu !')
            money_player = (money_player - (investimento))
            money_machine = (money_machine + (investimento))

        elif (sort == 0):
            print('Que pena, você perdeu !')
            money_player = (money_player - investimento)
            money_machine = (money_machine + investimento)

        else:
            print('Que pena, você perdeu !')
            money_player = (money_player - investimento)
            money_machine = (money_machine + investimento)

if (money_player <= 0):
    print('Você faliu!')
    breakpoint

elif (money_machine <= 0):
    print('Você faliu a banca, parabens!')
    breakpoint