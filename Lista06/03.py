from random import randint


n = int(input('Digite o a quantidade de elementos que você deseja na matriz: '))
pos = 0
numeros = []
for i in range(n):
    numero = randint(0, 99)
    pos = 0
    for valor in numeros:
        if numero < valor:
            numeros.insert(pos, numero)
            break
        pos += 1
    else:
        numeros.append(numero)
    pos += 1


print(f'Lista ordenada: \n{numeros}')