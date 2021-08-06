def cabecalho():
    print('************************************************')
    print('***\033[34meste programa foi feito pelo prf antonio\033[m***')
    print('************************************************')

def soma_numeros(n1,n2):
    r = n1 + n2
    print(r)
    return r

print('inicio do programa')
cabecalho()
h = soma_numeros(6, 7) * 3
j = soma_numeros(6, 7) / 4
print('\033[33mh: \033[m', h)
print('\033[32mj: \033[m', j)

print('')
print("fim do programa")