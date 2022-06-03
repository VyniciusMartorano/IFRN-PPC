"""
A Organização Mundial de Saúde (OMS) utiliza o Índice de Massa Corporal (IMC) como critério para dar
uma indicação sobre a condição de peso de uma pessoa adulta.
"""


peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

indice = peso / (altura ** 2)

if indice < 18.5:
    print(f'Abaixo do peso')

elif indice >= 18.5 and indice < 25:
    print(f'Peso normal')

elif indice >= 25 and indice < 30:
    print(f'Sobrepeso')

elif indice >= 30 and indice < 35:
    print(f'Obesidade Grau 1')

elif indice >= 35 and indice < 40:
    print(f'Obesidade Grau 2')

elif indice >= 40:
    print(f'Obesidade Grau 3 ou Mórbida')

