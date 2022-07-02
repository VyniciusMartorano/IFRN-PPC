valor = float(input('Que valor você deseja sacar? R$'))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    elif total > 0 and total < 0.01 and ced == 0.01:
        totced += 1
        total = 0
    else:
        if totced > 0 and ced > 1:
            print(f'Total de {totced} cédulas de R${ced}')
        if totced > 0 and ced > 0 and ced <= 1:
            print(f'Total de {totced} moedas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        elif ced == 1:
            ced = 0.50
        elif ced == 0.5:
            ced = 0.25
        elif ced == 0.25:
            ced = 0.10
        elif ced == 0.1:
            ced = 0.05
        elif ced == 0.05:
            ced = 0.01
        totced = 0
        if total == 0:
            break
