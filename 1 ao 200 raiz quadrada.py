import math

print('\033[34m1 ao 200 e a raiz quadrada\033[m\n')
print('\033[32mNúmero   Raiz\033[m\n')

for nu in range(1, 201):
    print(f'{nu:<8}-------------- {math.sqrt(nu):.2f}')
