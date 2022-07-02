cont = 0
while True:
    num = int(input('Informe um valor inteiro positivo: '))
    if num <= 0:
        print('Informe um valor inteiro positivo')
        continue
    break

mult = 0

while mult <= num:
    mult += 1
    divisor = num % mult
    if divisor == 0:
        cont += 1
if cont == 2:
    print(f'O número {num} é um número primo. Ele possui apenas dois divisores, o 1 e ele mesmo ')
else:
    mult = 0
    cont = 0
    print(f'Os divisores de {num} são:')
    while mult <= num:
        mult += 1
        divisor = num % mult
        if divisor == 0:
            cont += 1
            print(mult)