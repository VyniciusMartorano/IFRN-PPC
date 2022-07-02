"""
Faça um programa que leia um valor N onde esse valor será os N primeiros números da sequência de
Fibonacci.
Lembrando que a SEQUÊNCIA DE FIBONACCI é uma sequência de números que obedecem a um
padrão em que cada elemento subsequente é a soma dos dois anteriores.
"""

n = int(input('Quantos termos voce quer mostrar: '))
t1 = 0
t2 = 1

print(t1)
print(t2)

cont = 3
while cont <= n:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    cont += 1
