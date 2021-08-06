print('\033[34m 1 ao 200 e a raiz quadrada \033[m')

import math

print()
print('\033[32m Número ______  raiz\033[m')
print()

for nu in range(1, 201, 1):
    print('{} -------------- {}' .format(nu, math.sqrt(nu)))