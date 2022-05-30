"""
Faça um programa que leia os valores de a, b e c e calcule as raízes de uma equação do 2º grau.
Lembrando que para ser uma equação do 2º grau, o valor de a não pode ser 0 (zero).
"""
from math import sqrt

def bhaskara(ax, bx = 0, c = 0):
    if ax < 0:
        return 'Ax não pode ser 0'
    
    delta = bx ** 2 - 4 * ax * c

    if delta < 0:
        return 'Delta é negativo'

    xPositivo = (- bx + sqrt(delta)) / (2 * ax)
    xNegativo = (+ bx + sqrt(delta)) / (2 * ax)

    if delta == 0:
        return f'Resultado: ({xPositivo}, {xNegativo})'
    
    return f'Resultado: ({xPositivo}, {xNegativo})'


ax = float(input('Digite o valor de Ax: '))
bx = float(input('Digite o valor de Bx: '))
c = float(input('Digite o valor de C: '))

print(bhaskara(ax, bx, c))
