"""
10. Um robô pode se mover em oito sentidos em um plano cartesiano: U (cima); D (baixo); R (direita); L
(esquerda); O (noroeste/cima-esquerda); N (nordeste/cima-direita); E (sudeste/baixo-direita) e W
(sudoeste/baixo-esquerda).
Faça um programa que:
(a) solicite ao usuário a posição inicial do robô (suas coordenadas X e Y);
(b) solicite ao usuário uma string. Letras maiúsculas e minúsculas são indistintas e aquelas
informadas que estejam fora das estabelecidas (U, D, R, L, O, N, E e W) devem ser ignoradas.
(c) Com base em cada letra válida (U, D, R, L, O, N, E e W), o robô deverá se deslocar 1 (uma)
unidade em cada eixo (X e Y) por vez em função da direção.
Ao final, indique:
(a) a posição inicial do robô (coordenadas X e Y);
(b) a posição final do robô (coordenadas X e Y);
(c) quantos movimentos válidos ele executou;
(d) quais foram os movimentos válidos que ele executou;
(e) em que quadrante ele iniciou (posição inicial de X e Y) e;
(f) em que quadrante ele terminou (posição final de X e Y)
"""

movimentos = input('Digite os movimentos para o robô executar: ').upper().strip()
x = float(input('Digite a posição inicial no eixo X: '))
y = float(input('Digite a posição inicial no eixo X: '))
cont = 0
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
while cont < len(movimentos):
    if movimentos[cont] in movValidos:
        if movimentos[cont] == 'U': y += 1
        elif movimentos[cont] == 'D': y -= 1
        elif movimentos[cont] == 'R': x += 1
        elif movimentos[cont] == 'L': x -= 1
        elif movimentos[cont] == 'O': 
            y += 1
            x -= 1
        elif movimentos[cont] == 'N':
            y += 1
            x += 1
        elif movimentos[cont] == 'E':
            x += 1
            y -= 1
        elif movimentos[cont] == 'W': 
            x -= 1
            y -= 1
        movValidosUser = movValidosUser + movimentos[cont]
    cont += 1

quadrFinal = ''
if x > 0 and y > 0: quadrFinal = '1º Quadrante'
elif x < 0 and y > 0: quadrFinal = '2º Quadrante'
elif x < 0 and y < 0: quadrFinal = '3º Quadrante'
elif x > 0 and y < 0: quadrFinal = '4º Quadrante'

print(f'A posição inicial do robô era {posIni}')
print(f'A posição final do robô: ({x, y})')
print(f'O usuario digitou {len(movValidosUser)}x movimentos válidos')
print(f'Os movimentos válidos foram: {movValidosUser}')
print(f'O robô iniciou {quadrInicial}')
print(f'O robô terminou no {quadrFinal}')
