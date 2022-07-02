string = input('Digite a string: ')
vogais = 'AÁÀÂÃEÊÉÈOÓÒIÍÌU'
qtdVogais = 0

for letter in string.strip():
    if letter.upper() in vogais:
        qtdVogais += 1

print(f'A string "{string}" possui {qtdVogais} vogais')
