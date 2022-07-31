"""
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 9
(inclusive), gerados aleatoriamente. Determinar as quantidades para cada número que foi gerado.
"""
from random import randint
array = []
n = int(input('Digite o a quantidade de elementos que você deseja na matriz: '))
qtd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(n):
    num = randint(0, 9)
    if num == 0: qtd[0] += 1
    elif num == 1: qtd[1] += 1
    elif num == 2: qtd[2] += 1
    elif num == 3: qtd[3] += 1
    elif num == 4: qtd[4] += 1
    elif num == 5: qtd[5] += 1
    elif num == 6: qtd[6] += 1
    elif num == 7: qtd[7] += 1
    elif num == 8: qtd[8] += 1
    elif num == 9: qtd[9] += 1
    array.append(num)

print(f'Matriz gerada: {array}')

for i in range(0, 10):
    print(f'O NUMERO {i} APARECEU {qtd[i]}x')

