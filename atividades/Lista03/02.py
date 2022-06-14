while True:
    x = int(input('Digite um numero inteiro:'))
    if x <= 0:
        print('Digite um valor inteiro positivo')
        continue
    break

if x > 0:
    cont = 0
    for divisor in range(1, x + 1):
        if x % divisor == 0:
            cont += 1
            print(divisor)

    if cont == 2:
        print('O numero é primo')
        
else:
    print('Informe um valor inteiro positivo')