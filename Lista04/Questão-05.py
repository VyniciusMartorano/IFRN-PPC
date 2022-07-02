"""
Faça um programa que receba duas palavras e informe se uma é anagrama da outra.
Lembrando que anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra.
Exemplo: IRACEMA é um anagrama de AMERICA; ROMA é um anagrama de AMOR;
"""

palavra1 = input('Digite a primeira palavra: ').upper()
palavra2 = input('Digite a segunda palavra: ').upper()
var = True


if not len(palavra1) == len(palavra2):
    print('Não é anagrama')
    var = False
else:
    cont = 0
    while cont < len(palavra1):
        if palavra1[cont] in palavra2:
            cont += 1
        else:
            var = False
            print('Não é anagrama')
            break

if var:
    print(f'As palavras digitadas são anagramas uma da outra')