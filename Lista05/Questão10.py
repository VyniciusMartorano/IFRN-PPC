movimentos = input('Digite os movimentos para o robô executar: ').upper().strip()
x = float(input('Digite a posição inicial no eixo X: '))
y = float(input('Digite a posição inicial no eixo Y: '))
movValidos =  'UDRLONEW'
movValidosUser = ''
quadrInicial = ''
posIni = f'({x},{y})'

if x > 0 and y > 0: quadrInicial = 'no 1º Quadrante'
elif x < 0 and y > 0: quadrInicial = 'no 2º Quadrante'
elif x < 0 and y < 0: quadrInicial = 'no 3º Quadrante'
elif x > 0 and y < 0: quadrInicial = 'no 4º Quadrante'
elif x == 0 and y != 0: quadrInicial = 'sob o eixo Y'
elif x != 0 and y == 0: quadrInicial = 'sob o eixo X'
else: quadrInicial = 'na origem do plano cartesiano'
for mov in movimentos:
    if mov in movValidos:
        if mov == 'U': y += 1
        elif mov == 'D': y -= 1
        elif mov == 'R': x += 1
        elif mov == 'L': x -= 1
        elif mov == 'O': 
            y += 1
            x -= 1
        elif mov == 'N':
            y += 1
            x += 1
        elif mov == 'E':
            x += 1
            y -= 1
        elif mov == 'W': 
            x -= 1
            y -= 1
        movValidosUser = movValidosUser + mov

quadrFinal = ''
if x > 0 and y > 0: quadrFinal = 'no 1º Quadrante'
elif x < 0 and y > 0: quadrFinal = 'no 2º Quadrante'
elif x < 0 and y < 0: quadrFinal = 'no 3º Quadrante'
elif x > 0 and y < 0: quadrFinal = 'no 4º Quadrante'
elif x == 0 and y != 0: quadrFinal = 'sob o eixo Y'
elif x != 0 and y == 0: quadrFinal = 'sob o eixo X'
else: quadrFinal = 'na origem do plano cartesiano'


print(f'A posição inicial do robô era {posIni}')
print(f'A posição final do robô: ({x, y})')
print(f'O usuario digitou {len(movValidosUser)}x movimentos válidos')
print(f'Os movimentos válidos foram: {movValidosUser}')
print(f'O robô iniciou {quadrInicial}')
print(f'O robô terminou no {quadrFinal}')
