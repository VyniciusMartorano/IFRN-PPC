num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
resp1 = num1
resp2 = num2
while True:
    resto = num1 % num2 
    num1 = num2
    num2 = resto
    if resto != 0:
        mdc = resto
    else:
        break
print(f'O máximo divisor comum entre {resp1} e {resp2} é: {mdc}')

