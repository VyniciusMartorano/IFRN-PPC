"""
Na definição da Wikipedia, números triangulares são aqueles que representam o total de pontos que
formam triângulos equiláteros em um plano (veja a definição detalhada em
https://pt.wikipedia.org/wiki/Número_triangular).
Faça um programa que solicite ao usuário um número inteiro positivo e informe se ele é (ou não)
triangular, de acordo com a definição
"""

"""
vitor
ordAtual = 3
ordPassada = ordAtual - 1

form = n * (n + 1) / 2
"""

"""
numero anterior + termo atual

t_5 = 15
t_6 = 6 + t_5 = 21
"""

"""
termoDesejado = 15
ordemDesejado = 6

termo = 15
ordem = 5

t = (ordem * (ordem + 1) / 2) + ordemDesejado

print(f'Ordem: {ordemDesejado}\nTermo: {t}')
"""
termoDesejado = int(input('Digite um número para saber se é triangular: '))
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
    


