palavra = input('Digite uma palavra para saber se é palindromo: ')

contPos = 0
contNeg = -1
var = True

while contPos < len(palavra):
    if palavra[contPos] == palavra[contNeg]:
        contPos += 1
        contNeg -= 1
    else:
        print('Não é palindromo')
        var = False
        break

if var:
    print(f'A palavra "{palavra}" é palindromo!')