
while True:
    num1 = int(input('Digite um valor: '))
    if num1 <= 0:
        print('Digite um valor inteiro positivo')
        continue
    break

print('Os numeros primos serão exibidos abaixo: ')

currentNum = num1 + 1
cont = 2

if num1 == 2:
    print(f'2 é primo')
else:
    while cont < num1:
        currentNum -= 1
        cache = 0
        cont2 = 1
        while cont2 < currentNum + 1:
            if currentNum % cont2 == 0:
                cache += 1
            cont2 += 1
        if cache > 2:
            ...
        else:
            print(f'{currentNum}')
        cont += 1



