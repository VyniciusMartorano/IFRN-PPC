bin = input('Digite o numero binario para conversão: ').strip()
bin = bin[::-1]
soma = 0 
for i in range(len(bin)):
    soma += int(bin[i]) * 2 ** i
print(f'O numero "{bin[::-1]}" em decimal é {soma}')