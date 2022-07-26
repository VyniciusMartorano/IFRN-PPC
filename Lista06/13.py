from random import choice


gabarito = []
choices = ['A', 'B', 'C', 'D', 'E']
registros = []
for i in range(10):
    gabarito.append(choice(choices))
    registros.append([])
    for c in range(11):
        if c == 0: registros[i].append(f'Aluno {i + 1}')
        else: registros[i].append(choice(choices))

acertos = 0
for item in registros:
    acertos = 0
    for i in range(1, 11):
        if item[i] == gabarito[i-1]: acertos += 1
    item.append(f'{acertos:.1f}')

print('Gabarito:')
for i in range(0, 10):
    print(f'{i + 1} - {gabarito[i]}')

for i in range(0, 10):
    print(f'{registros[i][0]}')
    print('Gabarito do aluno: ', end='')
    for c in range(1, 11): print(f'{registros[i][c]}', end=' ')
    print(f'\nNota do aluno: {registros[i][11]}')
    print('\n')