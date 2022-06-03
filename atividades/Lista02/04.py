"""
Faça um programa que leia um valor inteiro e informe se ele é um número par positivo, par negativo,
ímpar positivo, ímpar negativo ou se é nulo
"""

value = int(input('Digite um valor inteiro: '))

if value == 0:
    print('O valor é nulo')

elif value % 2 == 0:
    if value > 0:
        print(f'O valor {value} é par e positivo')
    else:
        print(f'O valor {value} é par e Negativo')
else:
    if value > 0:
        print(f'O valor {value} é Impar e positivo')
    else:
        print(f'O valor {value} é Impar e Negativo')

