"""
Fazer um programa que solicite ao usuário um valor inteiro positivo e gere o seu valor em binário.
ATENÇÃO: Deverá ser utilizada divisões inteiras para a solução.
"""

num = int(input('Digite um valor para seu binario: '))

resta = 0
binario = ''
while True:
    resta = num % 2
    quo = num // 2
    binario += str(resta)
    num = quo
    if quo < 1:
        break

print(binario[::-1])