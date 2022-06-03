"""
. Faça um programa que leia os 3 lados de um triângulo e informe o seu tipo:
Triângulo equilátero ..........................: possui os três lados com medidas iguais.
Triângulo isósceles ...........................: possui dois lados com medidas iguais.
Triângulo escaleno............................: possui os três lados com medidas diferentes.
Lembrando que todos os lados devem ser positivos e que:
|𝑏 − 𝑐| < 𝑎 < 𝑏 +𝑐
|𝑎 − 𝑐| < 𝑏 < 𝑎 + 𝑐
|𝑎 − 𝑏| < 𝑐 < 𝑎 + b
"""
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

eq1 = + (b - c) < a and a < b + c
eq2 = + (a - c) < b and b < a + c
eq3 = + (a - b) < c and c < a + b

if a < 0 or b < 0 or c < 0:
    print('Todos os lados devem ser positivos')

elif not (eq1 and eq2 and eq3):
    print('O triangulo não obedece as condições de existencia')

elif a == b and b == c:
    print('Triangulo Equilatero')

elif a != b != c != a:
    print('Triângulo escaleno')

else:
    print('Triângulo Isóceles')
