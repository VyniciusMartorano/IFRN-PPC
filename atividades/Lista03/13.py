"""
Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Fazer um
programa que solicite a massa inicial (em gramas) e que calcule o tempo necessário para que essa
massa se torne menor que 0,5 grama. Ao término, o programa deve exibir a massa inicial, a massa final
e o tempo calculado em horas, minutos e segundos.
"""

massaInicial = float(input('Digite a massa inicial do matérial em gramas: '))
tempoSecs = 0
print(f'Massa inicial: {massaInicial}gm')

while massaInicial > (1 / 2):
    massaInicial /= 2
    tempoSecs += 50

minuto = tempoSecs // 60
hora = minuto // 60
segundo = tempoSecs % 60
time = f'{hora}:{minuto}:{segundo}'

print(f'Massa final: {massaInicial}')

print(f'Tempo de decomposicao: {time}')

