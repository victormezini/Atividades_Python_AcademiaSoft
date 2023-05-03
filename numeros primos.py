n1 = int(input('Digite um número inteiro: '))

# Verifica se o número é menor ou igual a 1, que não é primo
if n1 <= 1:
    print('Este número não é primo.')
    exit()

# Verifica se o número é divisível por algum número entre 2 e a raiz quadrada dele
for n2 in range(2, int(n1 ** 0.5) + 1):
    if n1 % n2 == 0:
        print('Este número não é primo.')
        exit()

print('Este número é primo.')
