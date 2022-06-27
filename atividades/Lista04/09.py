"""
Faça um programa que emule o jogo da forca. O programa terá uma constante chamada
PALAVRA_CHAVE que armazenara a palavra a ser descoberta. O programa deverá solicitar ao usuário
as letras, à medida que as letras forem sendo digitadas o programa irá exibir se o usuário acertou ou
não. O jogo deverá considerar maiúsculas e minúsculas iguais. O jogador poderá errar 6 vezes antes de
ser enforcado
"""

PALAVRA_CHAVE = 'MAXARANGUAPE'.upper()
tamString = '_' * len(PALAVRA_CHAVE)
string = [*tamString]
acerto = 0
erro = 0

while erro < 6:
    user = input('Digite uma letra para tentar descobrir a palavra: ').upper()
    if not len(user.strip()):
        print('Digite pelo menos uma letra')
        continue
    
    elif len(user) != len(PALAVRA_CHAVE) and len(user) != 1:
        print('Digite apenas uma letra ou a palavra completa')
        continue

    if user in PALAVRA_CHAVE:
        cont = 0
        acerto += 1
        if acerto == len(PALAVRA_CHAVE):
            break
        while True:
            if cont > len(PALAVRA_CHAVE) - 1:
                break
            elif user == PALAVRA_CHAVE[cont] and string[cont] == '_':
                string[cont] = user
                break
            cont += 1
        print(f'Palavra até o momento: {"".join(string)}')
    else:
        erro += 1
        print(f'Você ainda tem {6 - erro} Tentativas')
    

if acerto == len(PALAVRA_CHAVE):
    print(f'Você venceu utilizando {acerto + erro} tentativas')
else:
    print(f'Você perdeu!\nA palavra correta era {PALAVRA_CHAVE}')