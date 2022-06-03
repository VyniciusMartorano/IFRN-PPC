"""
Faça um programa que leia a idade de 5 pessoas e o sexo de cada uma (assuma que só podem ser
informados a letra H para homes e a letra M para mulheres) e que calcule e mostre:
a. A idade média das 5 pessoas;
b. A idade média dos homens;
c. A idade média das mulheres.
"""

cont = 0

mediaGeral = 0
mediaHom = 0
mediaMul = 0

hom = 0
mul = 0

while cont < 5:
    cont += 1
    while True:
        idade = int(input(f'Digite a idade da {cont}ª Pessoa: '))
        if idade < 0:
            print('Digite uma idade valida')
            continue
        else:
            break

    while True:
        sexo = str(input(f'Digite o sexo da {cont}ª Pessoa\n[H]Masculino\n[M]Feminino\n: '))
        if sexo == 'M' or sexo == 'H':
            break
        else:
            print('Opção inválida')
            continue

    mediaGeral += idade

    if sexo == 'M':
        mul += 1
        mediaMul += idade

    elif sexo == 'H':
        hom += 1
        mediaHom += idade
    
mediaGeral = mediaGeral / 5
mediaHom = mediaHom / hom
mediaMul = mediaMul / mul

print(f'A média geral é de {mediaGeral} anos')
print(f'A média das mulheres é de {mediaMul} anos')
print(f'A média dos homens é de {mediaHom} anos')



