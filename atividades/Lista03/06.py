"""
Dado que uma Progressão Aritmética (P.A.) é uma sequência de números onde a diferença entre dois termos consecutivos é sempre a mesma. Essa diferença constante é chamada de razão da P.A.

Faça um programa que solicite ao usuário um valor inteiro inicial e a razão da P.A. e:

a. Solicite um novo valor inteiro positivo correspondente a quantidade de elementos da P.A. e
exiba os valores dessa P.A.;

b. Informe se a P.A. é constante, crescente ou decrescente;

c. Calcular a soma dos elementos dessa P.A.;

d. Solicitar um outro valor inteiro correspondente a enésima posição de um elemento da P.A. e exibir o valor desse elemento.
"""

r = int(input('Digite a Razão da P.A: '))
while True:
    n = int(input('Digite o numero de termos da P.A: '))
    if n <= 0:
        print('Digite um valor inteiro positivo')
        continue
    else:
        break
    
a1 = int(input('Digite o valor do A1: '))

enes = int(input('Digite qual posição deseja buscar na P.A: '))
cont = 0

while cont < n:
    print(a1 + r*cont)
    cont += 1

cont = 0
while cont <= enes:
    
    enesima = a1 + r * cont

    if cont == enes - 1:
        print(f'O valor da posição {enes} é {enesima}')
    cont += 1
    

if r > 0:
    print('A P.A é crescente')

elif r < 0:
    print('A P.A é decrescente')

elif r == 0:
    print('A P.A é constante')


print(f'Soma: {(n * (a1 + (a1 + ((n-1)*r))))/2}')    
