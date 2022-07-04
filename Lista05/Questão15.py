n = 6

i = 4
j = 5

result = ''
#0,2,3,4,6,8.
cont = 0

for c in range(0, n):
    multI = str(i * c)
    multJ = str(j * c)
    print(cont)
    if cont == n:
        break
    if multI in result and multJ in result:
        continue
    elif multI in result and multJ not in result:
        result += f'{multJ},'
        cont += 1
    elif multJ in result and multI not in result:
        result += f'{multI},'
        cont += 1
    else:
        if multI == multJ:
            result += f'{multI},'
            cont += 1
            continue
        result += f'{multI},{multJ},'
        cont += 2

print(result)
