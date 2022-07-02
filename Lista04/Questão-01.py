string = input('Digite a string: ')
vogais = 'AÁÀÂÃEÊÉÈOÓÒIÍÌU'
qtdVogais = 0

i = 0
while i < len(string.strip()):
    if string[i].upper() in vogais:
        qtdVogais += 1
    i += 1

print(f'A string "{string}" possui {qtdVogais} vogais')
