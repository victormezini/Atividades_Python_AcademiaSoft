print('\033[7mConversor de temperatura\033[m')

Tc = float(input('Digite a temperatura em graus Celsius: '))

Tf = (9/5) * Tc + 32

print(f'A temperatura em graus Fahrenheit é de: {Tf:.2f}')
