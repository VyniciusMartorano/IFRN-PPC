"""
Faça um programa que leia um valor inteiro correspondente a um ano entre 1900 e 2100 e diga se o ano
informado é bissexto ou não.
"""

def anoBissexto(ano):
    if ano <= 0:
        return False 
    
    elif ano % 400 == 0:
        return True
    
    elif ano % 100 == 0:
        return False

    elif ano % 4 == 0:
        return True
     
    else:
        return False


ano = int(input('Digite o ano: '))
if anoBissexto(ano):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
