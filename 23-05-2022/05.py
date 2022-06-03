"""
Faça um programa que leia um valor inteiro correspondente a um ano entre 1900 e 2100 e diga se o ano
informado é bissexto ou não.
"""
ano = int(input('Digite o ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É bissexto')
else:
    print('Não é bissexto')
