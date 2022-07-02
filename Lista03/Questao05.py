"""
Faça um programa que solicite valores inteiros ao usuário e a medida que o usuário o informe o valor o
programa deverá informar se o valor digitado é par ou ímpar. O programa encerra quando o usuário
informar o valor 0 (ZERO).
"""

while True:
    num = int(input('Digite um numero inteiro: \n[0] Encerrar Programa \n'))
    if num == 0:
        print('Você optou por fechar o programa')
        break

    if num % 2 == 0: 
        print(f'O valor {num} é PAR')

    else:
        print(f'O valor {num} é IMPAR')
        