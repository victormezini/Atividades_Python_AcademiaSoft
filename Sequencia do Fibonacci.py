print('\033[7mSequencia do Fibonacci\033[m')

na = 0
n = 1

for i in range(10):
    f = n + na
    na = n
    n = f
    print(f)
