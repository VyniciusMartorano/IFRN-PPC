"""
3. Faça um programa que solicite ao usuário um valor inteiro positivo e exiba os números primos de 1 até
o valor informado.
"""

num2 = int(input('Digite um valor inteiro: '))
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