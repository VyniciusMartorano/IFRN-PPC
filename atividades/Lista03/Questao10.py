"""
Faça um programa que receba uma quantidade indeterminada de valores numéricos, considere que para
encerrar a entrada de dados deve ser digitado o valor 0 (ZERO) e que ao finalizar a entrada dos valores
(desconsiderando o valor 0), exiba na tela o maior, o menor e a média dos valores digitados. O programa
deverá desconsiderar os valores negativos informados.

"""
maior = soma = cont = 0

while True:
    num = int(input('Digite um valor: \n[0]Parar programa\n: '))
    if num == 0:
        break
    elif num > 0:
        if cont == 0:
            menor = num
        cont += 1
        soma += num
        if num > maior:
            maior = num
                
        elif num < menor:
            menor = num

media = soma / cont

print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
print(f'A media dos valores digitados é {media}')

    
