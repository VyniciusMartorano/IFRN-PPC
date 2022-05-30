"""
Faça um programa que leia os 3 ângulos de um triângulo e informe o seu tipo:
Triângulo acutângulo ........................: possui todos os ângulos com medidas menores que 90º.
Triângulo retângulo ...........................: possui um ângulo com medida igual a 90º.
Triângulo obtusângulo ......................: possui um ângulo obtuso, maior que 90º
"""


def VerificaTriangulo(l1, l2, l3):
    if l1 < 0 or l2 < 0 or l3 < 0:
        return 'Todos os lados devem ser positivos'
        
    if (l1 + l2 + l3) != 180:
        return 'A soma dos angulos internos tem que ser 180'

    if l1 < 90 and l2 < 90 and l3 < 90:
        return 'Triangulo acutângulo'
    
    elif l1 == 90 or l2 == 90 or l3 == 90:
        return 'Triangulo retângulo'

    elif l1 > 90 or l2 > 90 or l3 > 90:
        return 'Triângulo obtusângulo'


l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

print(VerificaTriangulo(l1, l2, l3))