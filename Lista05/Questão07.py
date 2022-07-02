palavra = input('Digite uma palavra para saber se é palindromo: ')
key = False

for i in range(len(palavra)):
    if palavra[i] == palavra[-i - 1]:
        key = True
    else:
        key = False
        break

if key:
    print(f'A palavra {palavra} é PALINDROMO')
else:
    print(f'A palavra {palavra} NÃO é PALINDROMO')
