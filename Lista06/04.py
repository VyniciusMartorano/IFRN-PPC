from random import randint


n = int(input('Digite o a quantidade de elementos que você deseja na matriz: '))

array = []
for i in range(n):
    num = randint(0, 99)
    array.append(num)

array.sort(reverse=True)
print(f'Lista ordenada: \n{array}')