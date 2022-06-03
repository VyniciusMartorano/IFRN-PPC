"""
Faça um programa que leia duas coordenadas (X e Y) de um ponto e informe em que quadrante do plano
cartesiano ele está.
"""


x = float(input('Digite o valor da coordenada X: '))
y = float(input('Digite o valor da coordenada Y: '))

if x > 0 and y > 0:
    print(f'A coordenada ({x}, {y}) está no 1 quadrante')

elif x < 0 and y > 0:
    print(f'A coordenada ({x}, {y}) está no 2 quadrante')

elif x < 0 and y < 0:
    print(f'A coordenada ({x}, {y}) está no 3 quadrante')

elif x > 0 and y < 0:
    print(f'A coordenada ({x}, {y}) está no 4 quadrante')
