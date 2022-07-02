razao = int(input('Digite a Razão da P.A: '))
tamPA = int(input('Digite o numero de termos da P.A: '))
a1 = int(input('Digite o valor do A1: '))
enes = int(input('Digite qual posição deseja buscar na P.A: '))

if enes > 0 and tamPA > 0: 
    for i in range(tamPA):
        print(a1 + razao * i)
        
    for i in range(enes):
        enesima = a1 + razao * i
        if i == enes - 1:
            print(f'O valor da posição {enes} é {enesima}')
        
    if razao > 0: print('A P.A é crescente')
    elif razao < 0: print('A P.A é decrescente')
    elif razao == 0: print('A P.A é constante')
    print(f'Soma: {(tamPA * (a1 + (a1 + ((tamPA-1)*razao))))/2}')    
else:
    if enes <= 0:
        print('Digite um valor inteiro positivo')
    if tamPA <= 0:
        print('Digite um valor inteiro positivo')