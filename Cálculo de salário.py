print('\033[7mCálculo de salário\033[m')

htrabalhadas=int(input('Horas trabalhadas no mês: '))

valortrabalhada=int(input('Valor da hora trabalhada: '))

percdesconto=int(input('Percentual de desconto: '))

SalarioBruto = htrabalhadas * valortrabalhada

print('Salario bruto: ', htrabalhadas * valortrabalhada)