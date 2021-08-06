print('\033[7mPar ou Impar\033[m')

num = int(input('Digite um número: '))

if int(num) % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')