"""
Faça um programa que leia a coordenada cartesiana de dois pontos e calcule a distância entre eles
"""

x1 = float(input('Digite o valor da coordenada do eixo X1: '))
y1 = float(input('Digite o valor da coordenada do eixo Y1: '))
x2 = float(input('Digite o valor da coordenada do eixo X2: '))
y2 = float(input('Digite o valor da coordenada do eixo Y2: '))


resultado = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**(1 / 2)

print(f'A distancia entre os vetores ({x1}, {y1}) e ({x2}, {y2}) é {resultado:.2f}')

