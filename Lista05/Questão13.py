num = int(input('Digite o valor: '))
n = num
if num < 0:
    num = - num

count = 0
valor = 1
while valor <= num:
    valor *= 10
    count += 1

print(f'O numero {n} tem {count} digito(s)')