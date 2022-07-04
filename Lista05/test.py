import math 



numero = abs(int(input('Digite o valor: ')))
x = 1 if numero == 0 else math.floor(math.log10(numero)) + 1
print(f'O numero {numero} tem {x} digito(s)')




    

