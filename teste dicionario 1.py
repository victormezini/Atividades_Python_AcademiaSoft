wilson = {'vida': 70, 'fome': False, 'graveto': 30, 'frio': False}

print(wilson['frio'])
print(wilson['vida'])
print(wilson.keys())
print(wilson.values())

if 'hp' in wilson:
    print('wilson tem hp')
else:
    print('wilson não tem hp')
try:
    wilson['hp'] = wilson['hp'] + 10
    print('hp incrementado')
except:
    print('Opa não posso incrementar o hp do wilson')
print('fim do programa')