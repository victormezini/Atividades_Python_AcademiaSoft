print('\033[34mMatriz (Maior e Menor)\033[m')
print()

l = []
for v in range(5):
    n = int(input('Digite um número inteiro: '))
    l.append(n)

maior = max(l)
menor = min(l)

print(l)
print(f'\nO maior número digitado é: {maior}')
print(f'O menor número digitado é: {menor}')
