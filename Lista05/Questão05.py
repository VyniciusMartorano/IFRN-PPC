n = int(input('Quantos termos voce quer mostrar: '))
if n > 0:
    t1 = 0
    t2 = 1

    print(t1)
    print(t2)
    for i in range(3, n + 1):
        t3 = t1 + t2
        print(t3)
        t1 = t2
        t2 = t3
else:
    print('Quantidade inválida')