"""
faça um programa que leia dois valores inteiros (A e B) correspondentes aos catetos de um triângulo e
calcule a hipotenusa. Lembrando que a hipotenusa só deverá ser calculada se os valores informados
forem positivos.
hipo **2 = cat1 ** 2 + cat2 ** 2


"""
from math import sqrt


def hipotenusa(cat1, cat2):
    if cat1 < 0 or cat2 < 0:
        return 'Os catetos precisam ser positivos'

    hipo = sqrt(cat1 ** 2 + cat2 ** 2)
    return f'O valor da hipotenusa do triangulo com os catetos {cat1} e {cat2} é {hipo}'


cat1 = int(input('Digite o valor do cateto 1: '))
cat2 = int(input('Digite o valor do cateto 2: '))
print(hipotenusa(cat1=cat1, cat2=cat2))