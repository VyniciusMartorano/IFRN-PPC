senha_padrao = 'swordfish'
while True:
    user = input('Digite a senha: ')
    if user != senha_padrao:
        print('Senha incorreta')
        continue
    else:
        print('Parabéns!!Você acertou a palavra-chave')
        break
