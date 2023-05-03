print('\033[34m1 ao 200 e o quadrado\033[m\n')
print('\033[32mNúmero   Quadrado\033[m\n')

for nu in range(1, 201):
    print(f'{nu:<8}-------------- {nu ** 2}')
