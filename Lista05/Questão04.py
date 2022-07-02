num = int(input('Digite um numero para o seu fatorial: '))

result = 1
if num > 0:
    for i in range(1, num + 1):
        result *= i
    print(f'O fatorial de {num} é {result}')
elif num == 0:
    print(f'O fatorial de 0 é 1')
else:
    print('Valor informado é inválido')