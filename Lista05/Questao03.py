r = float(input('Digite a Razão da P.G: '))
n = int(input('Digite o numero de termos da P.G: '))
a1 = int(input('Digite o a1 da P.G: '))
enes = int(input('Digite qual posição deseja buscar na P.G: '))

if n > 0 and a1 != 0 and enes > 0:
    if r == 1:
        print(f'Essa PG é constante e todos os valores são iguais a {a1}')
        soma = 0
        for i in range(n):    
            print(a1 * (r ** i))
            soma += a1 * (r ** i)
        print(f'Soma: {soma}')

    elif r == 0 and a1 == 0:
        for i in range(n):
            print(a1 * (r ** i))
        print('PG é constante e todos os valores são iguais a 0')

    else:
        for i in range(n):
            print(a1 * (r ** i))
        
        for i in range(enes):
            enesima = a1 * (r ** i)
            if i == enes - 1:
                print(f'O valor da posição {enes} é {enesima}')

        if a1 < 0 and r > 0: print('A P.G é decrescente')
        elif r > 0 and a1 > 0: print('A P.G é crescente')
        elif a1 != 0 and r < 0: print('A P.G é oscilante')
        print(f'Soma: {(a1 * ((r**n)-1))/(r-1)}')   
else:
    if n <= 0:
        print('Digite um valor inteiro positivo')
    if a1 == 0:
        print('O primeiro termo não pode ser 0')
    if enes <= 0:
        print('Digite um valor inteiro positivo')
    

