print('\033[7mCálculo de salário\033[m')

horas_trabalhadas = int(input('Horas trabalhadas no mês: '))
valor_hora = float(input('Valor da hora trabalhada: '))
perc_desconto = float(input('Percentual de desconto: '))

salario_bruto = horas_trabalhadas * valor_hora
desconto = salario_bruto * perc_desconto / 100
salario_liquido = salario_bruto - desconto

print(f'Salário bruto: R${salario_bruto:.2f}')
print(f'Desconto: R${desconto:.2f}')
print(f'Salário líquido: R${salario_liquido:.2f}')
