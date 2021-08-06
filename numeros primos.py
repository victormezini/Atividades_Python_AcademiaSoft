from sys import exit
n1 = int(input('Digite um numero inteiro: '))
for n2 in range(2, n1):
    if n1 % n2 == 0:
        exit('Este numero não é primo')
print('Este numero é primo')