
valor = 153.53

total = valor
parcialValue = 100
totCed = 0

while True:
    if total >= parcialValue:
        total -= parcialValue
        totCed += 1
    else:
        if totCed > 0:
            if parcialValue >= 1:
                print(f'Total de {totCed} cedulas de R${parcialValue}')
            else:
                print(f'Total de {totCed} moedas de {parcialValue} centavos')

        if parcialValue == 100:
            parcialValue = 50

        elif parcialValue == 50:
            parcialValue = 20

        elif parcialValue == 20:
            parcialValue = 10

        elif parcialValue == 10:
            parcialValue = 5

        elif parcialValue == 5:
            parcialValue = 2

        elif parcialValue == 2:
            parcialValue = 1

        elif parcialValue == 1:
            parcialValue = 1 / 2

        elif parcialValue == 1 / 2:
            parcialValue = 1 / 4

        elif parcialValue == 1 / 4:
            parcialValue = 1 / 10
        
        elif parcialValue == 1 / 10:
            parcialValue = 1 / 20
        
        elif parcialValue == 1 / 20:
            parcialValue = 1 / 100

        totCed = 0
        if total == 0 or total < 1 / 100:
            break
