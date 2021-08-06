print('\033[1mPrograma de equação de segundo grau\033[m')
nome=str(input('Digite o seu nome: '))
ra=int(input('Digite o seu RA: '))
programa=str(input('Coloque o nome do programa: '))
print('*********************************************************************************************')

print('******    Programação II -  2º Ciclo Jogos Digitais                                   ******')

print('******   Nome:' ,nome,'           RA:' ,ra,'                ******')

print('******   Programa :' ,programa,'                                        ******')

print('*********************************************************************************************')

a= float(input('Digite o valor de A='))
b= float(input('Digite o valor de B='))
c= float(input('Digite o valor de C='))
delta = b**2-4*a*c
print('Delta=', delta)
raizdelta=delta**0.5
print('Raiz de delta= ', raizdelta)
x1=(-b+raizdelta)/(2*a)
print('x1 = ', x1)
x2=(-b-raizdelta)/(2*a)
print('x2 = ', x2)