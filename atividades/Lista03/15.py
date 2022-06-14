"""
Na definição da Wikipedia, números triangulares são aqueles que representam o total de pontos que
formam triângulos equiláteros em um plano (veja a definição detalhada em
https://pt.wikipedia.org/wiki/Número_triangular).
Faça um programa que solicite ao usuário um número inteiro positivo e informe se ele é (ou não)
triangular, de acordo com a definição
"""
"""
numero anterior + termo atual

t_5 = 15
t_6 = 6 + t_5 = 21
"""

while True:
    termoDesejado = int(input('Digite um número para saber se é triangular: '))
    if termoDesejado < 0:
        print('Digite um valor inteiro maior ou igual a zero')
        continue
    break

cont = 0

triangular = 0
while cont < termoDesejado:
    cont += 1
    termo = (cont * (cont + 1) / 2)
    if termo == termoDesejado:
        triangular = 1

if triangular == 1:
    print(f'O número {termoDesejado} é Triangular')
else:
    print(f'O número {termoDesejado} não é Triangular')
    


