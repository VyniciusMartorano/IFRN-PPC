"""
Faça um programa que leia um número e imprima o seu fatorial.
"""

while True:
    num = int(input('Digite um numero para o seu fatorial: '))
    if num >= 0:
        break
    else:
        print('Valor inválido')
        continue

resultado = 1
cont = 1

if num > 0:
    while cont <= num:
        resultado *= cont
        cont += 1
    print(f'O fatorial de {num} é {resultado}')

else:
    print(f'O fatorial de 0 é 1')