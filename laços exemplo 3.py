print('\033[7mInicio\033[m')

i = 12

while i >= 0:
    if i % 2 ==0:
       print(i)

    i = i - 1
    if i == 6:
        continue
    if 1 % 2 == 0:
        print(i)
print('final')