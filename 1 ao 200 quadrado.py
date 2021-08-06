print('\033[34m 1 ao 200 e o quadrado \033[m')
print()
print('\033[32m Número ______  Quadrado\033[m')
print()

for nu in range(1, 201, 1):
    print('{} -------------- {}' .format(nu, nu * nu))