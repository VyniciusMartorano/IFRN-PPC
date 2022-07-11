n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
if n1 > 0 and n2 > 0:
    for n1 in range(1, n1 + 1):
        if (n1 % n1 == 0) and (n2 % n1 == 0):
            mdc = n1
    print(f'O máximo divisor comum entre {n1} e {n2} é: {mdc}')
else: 
    print('Você não informou valores inteiros positivos.')
