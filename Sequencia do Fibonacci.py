
f = 0
n = 1
na = 0

print('\033[7mSequencia do Fibonacci\033[m')
for jogando in range (0,10,1):
    jogando = jogando + 1
    f = n + na
    na = n
    n = f
    print (f)