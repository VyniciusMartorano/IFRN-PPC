"""
Dado que uma Progressão Geométrica (P.G.) é a uma sequência numérica cujo quociente (q) ou razão entre um número e outro (exceto o primeiro) é sempre igual. Vale lembrar que essa razão é sempre constante e pode ser qualquer número racional (positivos, negativos, frações) exceto o número zero (0).
Faça um programa que solicite ao usuário um valor inteiro inicial e a razão da P.G. e:

a. Solicite um novo valor inteiro positivo correspondente a quantidade de elementos da PG e
exiba os valores dessa P.G.;

b. Informe se a P.G. é constante, oscilante, crescente ou decrescente;

c. Calcular a soma dos elementos dessa P.G;

d. Solicitar um outro valor inteiro correspondente a enésima posição de um elemento da P.G. e
exibir o valor desse elemento

"""
while True:
    r = int(input('Digite a Razão da P.G: '))
    if r == 0:
        print('A razão não pode ser 0')
        continue
    else:
        break

while True:
    n = int(input('Digite o numero de termos da P.G: '))
    if n <= 0:
        print('Digite um valor inteiro positivo')
        continue
    else:
        break

while True:
    a1 = int(input('Digite o a1 da P.G: '))
    if a1 == 0:
        print('O primeiro termo não pode ser 0')
        continue
    else:
        break

enes = int(input('Digite qual posição deseja buscar na P.G: '))
cont = 0

while cont < n:
    print(a1 * (r ** cont))
    cont += 1
    

cont = 0
while cont <= enes:
    
    enesima = a1*(r**cont)

    if cont == enes - 1:
        print(f'O valor da posição {enes} é {enesima}')
    cont += 1
    

if r > 0:
    print('A P.G é crescente')

elif a1 != 0 and r < 0:
    print('A P.G é oscilante')

elif r < 0:
    print('A P.G é decrescente')

elif r == 0:
    print('A P.G é constante')


print(f'Soma: {(a1 * ((r**n)-1))/(r-1)}')    


