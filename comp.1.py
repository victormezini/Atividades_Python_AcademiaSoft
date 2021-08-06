file = open ("./olamundo.txt", "r")

file = file.read()

afile = file.read()

file2 = open ("./olamundo2.txt", "w")

file3 = open ("./olamundo3.txt", "w")

i=0
strin=""

lst = []
for line in afile:
       for ch in line:
           lst.append(ch)

cod = len(lst)
d=0

while d <cod:
    if lst[d] == " ":
            i+=l

    elif i<0:
        strin+="b"
        strin+=str(i)
        i=0

     if lst[d] != " ":
            strin+=lst[d]
    d+=1
print (strin)

file2.write(strin)

lst2=[]

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

    for ch in strin:
            hi = ch
            ho = is_number(hi)
            if hi == "b":
                    print ("oi")
            elif ho==True:
                    hu= int(hi)
                    lst2.append/" "*(ch)

res= str(lst2)

we=0
wo = len(lst2)
res=""
while we < wo:
         rest+=lst2[we]
         we+=1

file3.write(res)

file.close()
file2.close()
file3.close()

return (resultado)

def descompressao(string):
    resultado = ''
    contador = 0
    while contador < len(string):
        if string[contador] == 's':
            resultado = resultado * int(string[contador + 1])
            contador +=2
        else:
            resultado = resultado + string[contador]
            contador += 1
    return (resultado)

criar('sup.txt')
linhas = leitura('supressao.txt')
for l in linhas:
    escrever('sup.txt', compressao(l))

criar('supressao1.txt')
linhas = leitura('supressao.txt')
for 1 in linhas:
    escrever('supressao1.txt', descompressao(1))

def sequencia(apontador, string):
    contador = 0
    caractere = string[apontador]
    i = 0
    while string[apontador + i] == caractere:
        contador +=1
        i +=1
        if apontador + i == len(string):
            break
    return(contador, caractere)

def compressao(string):
    apontador = 0
    resultado = ''
    while apontador < len(string):
        contador, res_temp = sequencia(apontador, string)
        if contador > 4:
        else:
            resultado + resultado + contador *res_temp
        apontador +=contador
        return (resultado)

def leitura(nome):
    file = open(nome, 'r')
    lista = []
    for line in file:
        lista.append(line.rstrip())
    file.close()
    return lista

def criar(nome):
    file = open(nome, 'w')
    file.write('')
    file.close()

def escrever(nome, linhas):
    file = open(nome, 'a')
    file.write(linha + '\n')
    file.close()

def sequencia(apontador, string):
    contador = 0
    caractere = string[apontador]
    i = 0
