from math import pi

def paralelogramo(base, altura):
    return base * altura

def quadrado(lado):
    return lado**2

def retangulo(base, altura):
    return base * altura

def triangulo(base, altura):
    return (base * altura) / 2

def trapezio(baseMaior, baseMenor, altura):
    return ((baseMaior + baseMenor) * altura) / 2

def losango(diagonalMaior, diagonalMenor):
    return (diagonalMaior + diagonalMenor) / 2

def circulo(raio):
    return 2 * pi * raio



print(paralelogramo(2, 4))
print(quadrado(2))
print(retangulo(2, 4))
print(triangulo(2, 4))
print(trapezio(5, 3, 6))
print(losango(5, 3))
print(circulo(2))