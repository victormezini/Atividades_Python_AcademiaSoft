from random import random
mario = {'hp': 100, 'dano': 3, 'cooldown': 1, 'cooldown_count':0, 'sorte':0.4}
sonic = {'hp': 100, 'dano': 8, 'cooldown': 5, 'cooldown_count':0, 'sorte':0.8}
minion = {'hp':2, 'dano':0.1, 'cooldown': 1}
lista_inimigos = [minion.copy() for _ in range(5)]

def calcula_regras(personagem, inimigo):
    if personagem['sorte'] > random():
        inimigo['hp'] = inimigo['hp'] - personagem['dano']
    personagem['cooldown_count'] = personagem['cooldown']
def pintar(personagem):
    print(personagem['nome'], personagem)

jogando = True
while jogando:
    #calculando as regras
    calcula_regras(mario, sonic)
    calcula_regras(sonic, mario)
    if sonic['hp'] <= 0:
        print('O Mario ganhou!')
        jogando = False
    elif mario['hp'] <=0:
        print('o sonic ganhou')
        jogando = False
        print('mario:', mario)
        print('sonic:', sonic)
print('fim de jogo')
