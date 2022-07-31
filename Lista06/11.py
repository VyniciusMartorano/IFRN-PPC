"""
Seguindo a definição da Constante de Kaprekar (veja a definição detalhada em
https://pt.wikipedia.org/wiki/Constante_de_Kaprekar), faça um programa que leia um
número inteiro positivo de 4 dígitos e diga se esse número converge ou não para a Constante de Kaprekar
e, se convergir, em quantas interações ele converge.
"""

n = str(input('Informe um número entre 0 e 10000: ')).strip()
inicio = n
cont = 0
if len([*n]) <= 4 and int(n) > 0:
    while n != '6174':
        x1 = [*n]
        x2 = [*n]
        while len(x1) < 4 and len(x2) < 4:   
            num = '0'
            x1.append(num)
            x2.insert(0, '0')
        if x1[0] == x1[1] == x1[2] == x1[3]: 
            print(f'O número {n} não tem constante Kaprekar.')
            break
        x1.sort(reverse=True)
        x2.sort()
        maior = ''
        menor = ''
        for i in range(4):                   
            maior += x1[i]
            menor += x2[i]
        res = int(maior) - int(menor)       
        n = str(res)                         
        cont += 1
    if cont > 0:
        print(f'O número {inicio} tem {cont} repetições até chegar a constante de Kaprekar, 6174')
else: print('O número informado não pode ter mais que 4 dígitos (entre 0 e 10000).')