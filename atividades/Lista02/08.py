"""
Faça um programa que leia os valores de a, b e c e calcule as raízes de uma equação do 2º grau.
Lembrando que para ser uma equação do 2º grau, o valor de a não pode ser 0 (zero).
"""

ax = float(input('Digite o valor de Ax: '))
bx = float(input('Digite o valor de Bx: '))
c = float(input('Digite o valor de C: '))

delta = bx ** 2 - 4 * ax * c
if ax == 0:
    print('Ax não pode ser 0')

elif delta < 0:
    print('Delta é negativo')

else:
    xPositivo = (- bx + (delta**(1 / 2))) / (2 * ax)
    xNegativo = (- bx - (delta**(1 / 2))) / (2 * ax)

    if delta == 0:
        print(f'Resultado: ({xPositivo:.2f}, {xNegativo:.2f})')

    else:
        print(f'Resultado: ({xPositivo:.2f}, {xNegativo:.2f})')




