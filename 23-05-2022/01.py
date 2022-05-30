"""
Faça um programa que leia dois valores para as variáveis A e B e efetue a troca dos valores de forma
que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável
A. Apresente os valores trocados.
"""

a = input('Digite um valor para A: ')
b = input('Digite um valor para B: ')

print(f'Valores inciais: \nA: {a}\nB: {b}')
x = b

b = a 
a = x

print('Com a troca')
print(f'A: {a}\nB: {b}')