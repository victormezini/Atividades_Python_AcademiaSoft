print('\033[34m Soma e Média Aritmética\033[m')

numeros = []
for i in range(20):
    n = int(input(f'Digite o {i+1}º valor: '))
    numeros.append(n)

soma = sum(numeros)
media = soma / len(numeros)

print()
print(f'A soma é: {soma}')
print(f'A média aritmética é: {media:.2f}')
