print('\033[7mTabuada\033[m')
print()
for num_tabuada in range (1, 11 ,1):
    for numero in range(0,11,1):
        resultado = num_tabuada * numero
        print(num_tabuada, 'x', numero, '=', resultado)