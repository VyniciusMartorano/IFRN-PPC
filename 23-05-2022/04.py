"""
Faça um programa que leia um valor inteiro e informe se ele é um número par positivo, par negativo,
ímpar positivo, ímpar negativo ou se é nulo
"""

def VerifyValue(value: int):
    if value == 0:
        return 'O valor é nulo'

    if value % 2 == 0:
        if value > 0:
            return f'O valor {value} é par e positivo'
        else:
            return f'O valor {value} é par e Negativo'
    else:
        if value > 0:
            return f'O valor {value} é Impar e positivo'
        else:
            return f'O valor {value} é Impar e Negativo'


value = int(input('Digite um valor inteiro: '))

print(VerifyValue(value))