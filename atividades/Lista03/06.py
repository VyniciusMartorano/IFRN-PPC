"""
Dado que uma Progressão Aritmética (P.A.) é uma sequência de números onde a diferença entre dois termos consecutivos é sempre a mesma. Essa diferença constante é chamada de razão da P.A.

Faça um programa que solicite ao usuário um valor inteiro inicial e a razão da P.A. e:

a. Solicite um novo valor inteiro positivo correspondente a quantidade de elementos da P.A. e
exiba os valores dessa P.A.;

b. Informe se a P.A. é constante, crescente ou decrescente;

c. Calcular a soma dos elementos dessa P.A.;

d. Solicitar um outro valor inteiro correspondente a enésima posição de um elemento da P.A. e exibir o valor desse elemento.
"""

razao = int(input('Digite a Razão da P.A: '))
while True:
    tamPA = int(input('Digite o numero de termos da P.A: '))
    if tamPA <= 0:
        print('Digite um valor inteiro positivo')
        continue
    else:
        break
    
a1 = int(input('Digite o valor do A1: '))
while True:
    enes = int(input('Digite qual posição deseja buscar na P.A: '))
    if enes <= 0:
        print('Digite um valor inteiro positivo')
        continue
    break

cont = 0

while cont < tamPA:
    print(a1 + razao * cont)
    cont += 1

cont = 0
while cont <= enes:
    enesima = a1 + razao * cont
    if cont == enes - 1:
        print(f'O valor da posição {enes} é {enesima}')
    cont += 1
    
if razao > 0: print('A P.A é crescente')

elif razao < 0: print('A P.A é decrescente')

elif razao == 0: print('A P.A é constante')

print(f'Soma: {(tamPA * (a1 + (a1 + ((tamPA-1)*razao))))/2}')    
