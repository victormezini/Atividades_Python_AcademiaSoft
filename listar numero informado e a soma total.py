print('\033[34m Mostrar lista de 1 até o número informado e a soma total\033[m')
print()

n1 = 1
n = int(input('\033[31m Digite um número aqui: \033[m'))
s = 0
print()

while n1 <= n:
    print(n1)
    s += n1
    n1 += 1

print('\033[34m O resultado da soma dos números é: ',s)