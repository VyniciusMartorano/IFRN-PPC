"""
Faça um programa que leia duas coordenadas (X e Y) de um ponto e informe em que quadrante do plano
cartesiano ele está.
"""

def VerificaCoordenadas(x: float, y: float):
    if x > 0 and y > 0:
        return f'A coordenada ({x}, {y}) está no 1 quadrante'

    if x < 0 and y > 0:
        return f'A coordenada ({x}, {y}) está no 2 quadrante'

    if x < 0 and y < 0:
        return f'A coordenada ({x}, {y}) está no 3 quadrante'

    if x > 0 and y < 0:
        return f'A coordenada ({x}, {y}) está no 4 quadrante'


x = float(input('Digite o valor da coordenada X: '))
y = float(input('Digite o valor da coordenada Y: '))

print(VerificaCoordenadas(x, y))