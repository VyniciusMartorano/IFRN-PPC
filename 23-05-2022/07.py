"""
A Organização Mundial de Saúde (OMS) utiliza o Índice de Massa Corporal (IMC) como critério para dar
uma indicação sobre a condição de peso de uma pessoa adulta.
"""

def IMC(peso: float, altura: float):
    indice = peso / (altura ** 2)

    if indice < 18.5:
        return f'Abaixo do peso'
    
    elif indice >= 18.5 and indice < 25:
        return f'Peso normal'

    elif indice >= 25 and indice < 30:
        return f'Sobrepeso'

    elif indice >= 30 and indice < 35:
        return f'Obesidade Grau 1'
    
    elif indice >= 35 and indice < 40:
        return f'Obesidade Grau 2'
    
    elif indice >= 40:
        return f'Obesidade Grau 3 ou Mórbida'


peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

print(f'A sua condição é de {IMC(peso, altura)}')
