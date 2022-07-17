from random import randint


n = 8
soma = 0
array = []
for i in range(n):
    num = randint(0, 99)
    soma += num
    array.append(num)

array.sort()
if n % 2 == 0:
    mediana = (array[len(array) // 2] + array[(len(array) // 2) - 1]) / 2
else:
    mediana = array[n // 2]

soma2 = 0
for i in array: soma2 += (i - soma / n) ** 2
variancia = soma2 / len(array) 

print(f"""
{array}
a) Média: {(soma / n):.2f}
b) Médiana: {mediana}
c) Variancia: {variancia:.2f}
d) Desvio-Padrão: {(variancia ** 1 / 2):.2f}
""")

