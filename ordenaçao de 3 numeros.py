print('\033[7mOrdenação de dois numeros\033[m')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro númro: '))

if a < b < c:
    print(a)
    print(b)
    print(c)
elif a < c < b:
    print(a)
    print(c)
    print(b)
elif b < a < c:
    print(b)
    print(a)
    print(c)

elif b < c < a:
    print(b)
    print(c)
    print(a)

elif c < a < b:
    print(c)
    print(a)
    print(b)


else:
    print(c)
    print(b)
    print(a)