palavra = input('Digite a palavra: ')

cont = 0
while cont < len(palavra):
    print(palavra[0:cont + 1])
    cont += 1