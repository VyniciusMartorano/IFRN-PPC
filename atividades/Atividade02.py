p1 = {
    'a': 3,
    'b': 16,
    'nome': 'MIRIAM',
    'prof': 'ADVOGADO'
}

p2 = {
    'a': 5,
    'b': 64,
    'nome': 'PEDRO',
    'prof': 'MEDICO'
}

p3 = {
    'a': 2.5,
    'b': 9,
    'nome': 'ANA',
    'prof': 'PROFESSOR'
}

TESTE = False
pessoas = [p1, p2, p3]
results = []

for pessoa in pessoas:
    A = pessoa['a']
    B = pessoa['b']
    NOME = pessoa['nome']
    PROFISSAO = pessoa['prof']

    expreA = (A + 1 >= ((B) ** ( 1/2 ))) or (NOME != 'ANA')
    expreB = (A + 1 >= ((B) ** (1/2))) and (PROFISSAO == 'MEDICO')
    expreC = (NOME != 'ANA') or (PROFISSAO == 'MEDICO') and (A + 1 >= ((B) ** (1/2)))
    expreD = not TESTE and (( A + 1 ) >= ((B) ** (1/2))) or not (PROFISSAO == 'MEDICO')
    expreE = not ((A + 1 >= ((B) ** (1/2))) and TESTE)

    results.append([expreA, expreB, expreC, expreD, expreE])

r = results

print(f'{"A":>6}{"B":>5}{"C":>5}{"D":>5}{"E":>5}')
print(f'1) {r[0][0]} {r[0][1]} {r[0][2]} {r[0][3]} {r[0][4]}')
print(f'2) {r[1][0]} {r[1][1]} {r[1][2]} {r[1][3]} {r[1][4]}')
print(f'3) {r[2][0]} {r[2][1]} {r[2][2]} {r[2][3]} {r[2][4]}')




