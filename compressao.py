string = "00000111111111111111010110100000111111100001"
b_pixel = 4

dict = {}



temp = ""
comprimido = ""
flag = False
count = 0
countdict = 1
try:
    for e in range(len(string)):
        flag = False
        for i in range(b_pixel):
            temp += string[count]
            count += 1
        print(temp)
        for num in dict:
            if dict[num] == temp:
                comprimido += str(num) + "#"
                flag = True
        if not flag:
            dict[countdict] = temp
            comprimido += str(countdict) + "#"
            countdict += 1

        temp = ""

except IndexError:
    print("Indexerror")

print(dict)
print(comprimido)