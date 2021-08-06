print('\033[34m 5 ao 75 e a soma total \033[m')
print()
print('\033[32m Número ______  soma total\033[m')
print()

n1 = 5
n2 = 5

while n1 <= 75:
    print('{} -------------- {}'.format(n1, n2))
    n2 += n1 + 1
    n1 += 1