from statistics import median, pvariance, pstdev
from random import randint

n = int(input('Digite o a quantidade de elementos que você deseja na matriz: '))
soma = 0
array = []
for i in range(n):
    num = randint(0, 99)
    soma += num
    array.append(num)

array.sort()


print(f"""
{array}
a) Média: {(soma / n):.2f}
b) Médiana: {median(array)}
c) Variancia: {pvariance(array):.2f}
d) Desvio-padrão: {pstdev(array):.2f}
""")
