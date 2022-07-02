num = int(input('Digite um valor para seu binario: '))
if num >= 0:
    bin = ''
    for i in range(num, 0, -1):
        bin += str(num % 2)
        num = num // 2
        if num == 0:
            break
    print(bin[::-1])
else:
    print('Digite um valor inteiro positivo')