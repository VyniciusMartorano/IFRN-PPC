"""
3. Faça um programa que solicite ao usuário um valor inteiro positivo e exiba os números primos de 1 até
o valor informado.
"""


def primo(num):
    if num > 1:
        if num == 2:
            print(f'{num}')
            
        for i in range(2,num):
            if (num % i) == 0:
                print(f'{num} NÃO é primo')
                break
            else:
                print(f'{num} é um numero primo')
                break
    elif num == 1:
        print('O numero não é primo')
    else:
        print(f'Digite um numero inteiro positivo')

primo(2)