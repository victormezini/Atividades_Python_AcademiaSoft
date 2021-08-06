#print('\033[7m programa para digitar 3 numeros e somar\033[m')

#n1 = int(input('digite um numero: '))
#n2 = int(input('digite outro numero'))
#n3 = int(input('digite mais outro numero'))
#soma = n1 + n2 + n3
#print('A soma dos numeros é:', soma)


print('\033[7m programa de somar 3 numeros e somar\033[m ')
i = 1
soma = 0
while i <= 3:
    n = int(input('digite um numero: '))
    i = i + 1
    soma = soma + n

print('O valor da soma é:', soma)