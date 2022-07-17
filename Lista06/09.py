from random import randint


pos = False
n = int(input('Digite o a quantidade de elementos que você deseja na matriz: '))
user = int(input('Digite um valor para verificar se existe na matriz'))
array = []
cont = 0
for i in range(n):
    num = randint(0, 1000)
    if user == num:
        pos = cont
    array.append(num)
    cont += 1


if pos:
    print(f'O valor {user} está localizado na posição {pos} da lista')
else:
    print('O valor não existe na lista')