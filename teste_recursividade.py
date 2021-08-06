def calculo1(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero + calculo1(numero - 1)


numA = int(input("Digite um número:"))
res = calculo1(numA)

print("A resposta questão é: ", res)