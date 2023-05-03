print('\033[7mCalcule o volume de uma caixa\033[m\n')

base = int(input('Valor da base da caixa: '))
largura = int(input('Valor da largura da caixa: '))
altura = int(input('Valor da altura da caixa: '))

volume = base * largura * altura

print(f'O volume da caixa é de: {volume}')
