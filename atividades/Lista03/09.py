"""
Faça um programa que calcule a soma dos números positivos digitados pelo usuário. O programa deve
permitir que o usuário digite uma quantidade não determinada de números. O programa encerra e
imprime o valor da soma quando o usuário digitar o valor 0 (ZERO).

"""
soma = 0

while True:
    num = int(input('Digite um valor\n[0]Parar Programa\n: '))
    if num > 0:
        soma += num
    elif num == 0:
        print(f'A soma dos numeros digitados é {soma}')
        break

