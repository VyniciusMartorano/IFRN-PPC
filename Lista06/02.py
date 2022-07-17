"""
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 99
(inclusive), gerados aleatoriamente. Determinar as quantidades de elementos que estão no primeiro
quartil (valores entre 0 e 24), no segundo quartil (entre 25 e 49), no terceiro quartil (entre 50 e 74) e no
quarto quartil (entre 75 e 99).
"""
from random import randint
array = []
n = int(input('Digite o a quantidade de elementos que você deseja na matriz: '))
qtd = [0, 0, 0, 0]
for i in range(n):
    num = randint(0, 99)
    if num >= 0 and num <= 24: qtd[0] += 1
    elif num >= 25 and num <= 49: qtd[1] += 1
    elif num >= 50 and num <= 74: qtd[2] += 1
    elif num >= 75 and num <= 99: qtd[3] += 1
    array.append(num)

print(f"""
{array}

Elementos no primeiro quartil: {qtd[0]}
Elementos no segundo quartil: {qtd[1]}
Elementos no terceiro quartil: {qtd[2]}
Elementos no quarto quartil: {qtd[3]}
""")