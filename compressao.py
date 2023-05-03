string = "00000111111111111111010110100000111111100001"
b_pixel = 4

dict = {}

temp = ""
comprimido = ""
count = 0
countdict = 1

try:
    while count < len(string):
        temp = string[count:count+b_pixel]
        count += b_pixel
        if temp in dict.values():
            for num, value in dict.items():
                if value == temp:
                    comprimido += str(num) + "#"
                    break
        else:
            dict[countdict] = temp
            comprimido += str(countdict) + "#"
            countdict += 1

except IndexError:
    print("IndexError")

print(dict)
print(comprimido)
