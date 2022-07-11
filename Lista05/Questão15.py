n = int(input('Digite a quantidade de termos que deseja mostrar: '))
i = int(input('Digite o primeiro número que deseja obter os múltiplos: '))
j = int(input('Digite o segundo número que deseja obter os múltiplos: '))
print(f'Os {n} primeiros múltiplos de {i} e {j} são: ')
if i > 0 and j > 0 and n > 0:
    mult = 0
    termo = 0
    while termo < n:
        if mult % i == 0 or mult % j == 0:
            print(mult)
            termo += 1
        mult += 1
else:
    print('Você não informou somente números maiores que 0 anteriormente.')