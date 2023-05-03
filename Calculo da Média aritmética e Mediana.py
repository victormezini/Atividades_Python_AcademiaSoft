print('\033[34mCálculo da Média aritmética e Mediana\033[m\n')

l = []
for v in range(20):
    n = int(input(f'Digite o {v+1}° número inteiro: '))
    l.append(n)

print(l)

media = sum(l) / len(l)
print(f'A média aritmética é: {media:.2f}')

l.sort()
tamanho = len(l)
if tamanho % 2 == 0:
    mediana = (l[tamanho//2 - 1] + l[tamanho//2]) / 2
else:
    mediana = l[tamanho//2]

print(f'A mediana é: {mediana:.2f}')
