def compressao(string):
    apontador = 0
    resultado = ''
    while apontador < len(string):
        contador, res_temp = sequencia(apontador, string)
        if contador > 4:
            resultado += 's' + str(contador) + res_temp
        else:
            resultado += contador * res_temp
        apontador += contador
    return resultado

def descompressao(string):
    resultado = ''
    contador = 0
    while contador < len(string):
        if string[contador] == 's':
            resultado += int(string[contador + 1]) * string[contador + 2]
            contador += 3
        else:
            resultado += string[contador]
            contador += 1
    return resultado

def sequencia(apontador, string):
    contador = 0
    caractere = string[apontador]
    i = 0
    while apontador + i < len(string) and string[apontador + i] == caractere:
        contador += 1
        i += 1
    return contador, caractere

def leitura(nome):
    with open(nome, 'r') as file:
        lista = file.read().splitlines()
    return lista

def criar(nome):
    with open(nome, 'w'):
        pass

def escrever(nome, linha):
    with open(nome, 'a') as file:
        file.write(linha + '\n')

criar('sup.txt')
linhas = leitura('supressao.txt')
for linha in linhas:
    escrever('sup.txt', compressao(linha))

criar('supressao1.txt')
linhas = leitura('supressao.txt')
for linha in linhas:
    escrever('supressao1.txt', descompressao(linha))
