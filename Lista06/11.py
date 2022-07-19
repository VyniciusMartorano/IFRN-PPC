"""
Seguindo a definição da Constante de Kaprekar (veja a definição detalhada em
https://pt.wikipedia.org/wiki/Constante_de_Kaprekar), faça um programa que leia um
número inteiro positivo de 4 dígitos e diga se esse número converge ou não para a Constante de Kaprekar
e, se convergir, em quantas interações ele converge.
"""

num = '6174'

soma = 0
for n in num:
    soma += int(n)


if int(num) % soma == 0:
    if 
else:
    print('O numero não converge para a constante de Kaprekar')
