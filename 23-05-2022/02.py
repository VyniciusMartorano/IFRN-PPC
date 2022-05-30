"""
Faça um programa que leia a coordenada cartesiana de dois pontos e calcule a distância entre eles
"""
from math import sqrt

x1 = float(input('Digite o valor da coordenada do eixo X1: '))
y1 = float(input('Digite o valor da coordenada do eixo Y1: '))
x2 = float(input('Digite o valor da coordenada do eixo X2: '))
y2 = float(input('Digite o valor da coordenada do eixo Y2: '))


def distanciaEntreDoisPontos(x1, y1, x2, y2):
    
    resultado = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return f'A distancia entre os vetores ({x1}, {y1}) e ({x2}, {y2}) é {resultado:.2f}'


print(distanciaEntreDoisPontos(x1, y1, x2, y2))
