array = []
x = int(input('Informe a quantidade de elementos da lista: '))
for i in range(x):
    num = int(input("Digite um número:[0 encerrar] "))
    if num == 0:
        print('Voce decidiu encerrar o programa')
        break
    for chave, value in enumerate(array):
        if num < value:
            array.insert(chave, num)
            break
    else:
        array.append(num)
    print(f'Array atual: {array}')