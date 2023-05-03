print('\033[1mExercicio da tabuada\033[m')

for i in range(1, 11):
    row = f'{i:2d} x 2 = {i * 2:2d}   {i:2d} x 3 = {i * 3:2d}   {i:2d} x 4 = {i * 4:2d}   {i:2d} x 5 = {i * 5:2d}   {i + 4:2d} x 6 = {(i + 4) * 6:2d}   {i + 4:2d} x 7 = {(i + 4) * 7:2d}   {i + 4:2d} x 8 = {(i + 4) * 8:2d}   {i + 4:2d} x 9 = {(i + 4) * 9:2d}   {i + 4:2d} x 10 = {(i + 4) * 10:2d}'
    print(row)
