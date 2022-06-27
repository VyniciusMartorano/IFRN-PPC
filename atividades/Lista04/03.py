"""
Faça um programa que solicite ao usuário uma frase, uma palavra antiga e uma palavra nova. O
programa deverá imprimir a frase digitada, as duas palavras digitadas (a antiga e a nova) e a frase
substituindo a palavra antiga pela palavra nova.
"""

frase = input('Digite a frase: ')
palavraAnt = input('Digite a palavra a ser trocada: ')
palavraNov = input('Digite a nova palavra: ')


print(f'A nova frase: {frase.replace(palavraAnt, palavraNov)}')