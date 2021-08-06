#alunos = ['joao', 'maria', 'beto', 'beronaldo', 'alfredo', 'julio', 'sara']
#print(alunos[2])

#texto = ('carapicuiba')
#palavra = list(texto)

print('____________\033[7m Notas \033[m____________')
print()

nomes = ['\033[34mprog 2\033[m', '\033[34mDSPTI\033[m', '\033[34mportugues\033[m', '\033[34mredes\033[m', '\033[34mS.O.\033[m', '\033[34mingles\033[m', '\033[34mcalculo\033[m']

notas = []

notas.append(6)
notas.append(8.5)
notas.append(10)
notas.append(7)
notas.append(9)
notas.append(9.2)
notas.append(5)

dis = input('Digite o nome da disciplina extracurricular: ')
nomes.append(dis)
n = float(input('Digite a nota dessa disciplina: '))
notas.append(n)

for indice in range(0, len(nomes)):

#print('A nota de', nomes[indice],'é', notas[indice])

     txt = "A nota de {:^20} é: {:>5}".format(nomes[indice], notas[indice])
     print(txt)
