"""
Faça um programa que verifique e mostre os números entre 1.000 e 2.000 (inclusive) que, quando divididos por 11, produzam resto igual a 5
"""
cont = 1000

while cont < 2000:
    if cont % 11 == 5:
        print(cont)
    cont += 1
    
