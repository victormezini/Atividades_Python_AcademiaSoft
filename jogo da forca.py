print('\033[34m Jogo da forca \033[m')
print()

palavra = input('\033[31mDigite a palavra secreta: \033[m').lower().strip()

for x in range(100):
     print()
digitadas = []
acertos = []
erros = 0

while True:
     senha = ""
     for letra in palavra:
         senha += letra if letra in acertos else '_'
     print(senha)
     if senha == palavra:
         print('\033[35m Você acertou!\033[m')
         break
     tentativa = input("\nDigite uma letra:").lower().strip()
     if tentativa in digitadas:
         print('\033[32mVocê já digitou esta letra!\033[m')
         continue
     else:
         digitadas += tentativa
         if tentativa in palavra:
               acertos += tentativa
         else:
               erros += 1
               print('\033[31 Você errou!\033[m')
     print('X==:==\nX  :   ')
     print('X  O   ' if erros >= 1 else 'X')
     linha2 = ""
     if erros == 2:
         linha2 = "  |   "
     elif erros == 3:
         linha2 = " \|   "
     elif erros >= 4:
         linha2 = " \|/ "
     print("X%s" % linha2)
     linha3 = ""
     if erros == 5:
         linha3 += " /     "
     elif erros >= 6:
         linha3 += " / \ "
     print('X%s' % linha3)
     print('X\n===========')
     if erros == 6:
         print('\033[31m Morreu\033[m!')
         break