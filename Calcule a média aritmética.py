print('\033[7mCalcule a média aritmética\033[m\n')

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
nota4 = int(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média aritmética é: {media:.1f}')
