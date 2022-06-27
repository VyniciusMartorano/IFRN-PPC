"""
3. Faça um programa que solicite ao usuário um valor inteiro positivo e exiba os números primos de 1 até
o valor informado.
"""
while True:
    num2 = int(input('Digite um valor inteiro: '))
    if num2 <= 0:
        print('Digite um valor inteiro positivo')
        continue
    break

cont = 1
while cont <= num2:
    num = cont
    if num > 1:    
        i = 2
        while i < num: 
            if num % i == 0:
                break
            i += 1
        else:
            print(f'{num} É PRIMO')
    cont += 1