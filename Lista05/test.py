#15

n = 6

i = 2
j = 3

result = '0, '
for c in range(1,n):
    if str(i * c) in result:
        result += f'{j * c}, '
    elif str(j * c) in result:
        result += f'{i * c}, '
    else:
        result += f'{i * c}, {j * c}, '
print(result)